from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.db.models import Q
import os

@api_view(['GET',"POST"])
# 获取分类列表
def newsCateList(request):
  try:
    list = DictNewsCateS(DictNewsCate.objects.all(), many = True).data
    data = {}
    data['list'] = list
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取列表
def newsList(request):
  # 获取参数
  page_index = int(request.POST.get('page_index'))
  page_size = int(request.POST.get('page_size'))
  cate_id = request.POST.get('cate_id')
  try:
    list = News.objects.all()
    if cate_id:
      list = list.filter(cate_id=cate_id)
    total_count = list.count()
    list=list[(page_index - 1) * page_size : page_index * page_size]
    print(list)
    print(total_count)
    data = {}
    data["list"] = NewsS(list, many = True).data
    data["total_count"] = total_count
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取新闻详情
def newsDetail(request):
  # 获取参数
  id = request.POST.get('id')
  user_id = request.POST.get('user_id')
  try:
    news = News.objects.get(id=id)
    if not news:
      raise Exception("不存在")
    data = NewsS(news).data
    if user_id:
      favCheck = FavNews.objects.filter(Q(news_id=id), Q(user_id=user_id))
      if favCheck.exists():
        data['fav'] = 1
      else:
        data['fav'] = 0
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 添加新闻
def newsAdd(request):
  # 获取参数
  cate_id = request.POST.get('cate_id')
  title = request.POST.get('title')
  content = request.POST.get('content')
  try:
    news = News(
      cate_id = cate_id,
      title = title,
      content = content
    )
    news.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 收藏新闻
def newsFav(request):
  # 获取参数
  news_id = request.POST.get('news_id')
  user_id = request.POST.get('user_id')
  try:
    if not news_id or not user_id:
      raise Exception("参数错误")
    checkFav = FavNews.objects.filter(Q(news_id=news_id), Q(user_id=user_id))
    if checkFav.exists():
      checkFav = checkFav.first()
      checkFav.delete()
    else:
      favData = FavNews(user_id=user_id, news_id=news_id)
      favData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取个人收藏列表
def newsFavList(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  try:
    if not user_id:
      raise Exception("参数错误")
    checkFav = FavNews.objects.filter(user_id=user_id)
    list = []
    for item in checkFav:
      itemData = {}
      itemData['id'] = item.id
      itemData['user_id'] = item.user_id
      itemData['news_id'] = item.news_id
      itemData['news_info'] = NewsS(News.objects.get(id=item.news_id), many=False).data
      list.append(itemData)
    return JsonResponse({"code": 0, "data": list}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
