from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.db.models import Q
import os

@api_view(['GET',"POST"])
# 获取分类列表
def videoCateList(request):
  try:
    list = DictVideoCateS(DictVideoCate.objects.all(), many = True).data
    data = {}
    data['list'] = list
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取视频列表
def videoList(request):
  # 获取参数
  page_index = int(request.POST.get('page_index'))
  page_size = int(request.POST.get('page_size'))
  cate_id = request.POST.get('cate_id')
  try:
    list = Video.objects.all()
    if cate_id:
      list = list.filter(cate_id=cate_id)
    total_count = list.count()
    list=list[(page_index - 1) * page_size : page_index * page_size]
    print(list)
    print(total_count)
    data = {}
    data["list"] = VideoS(list, many = True).data
    data["total_count"] = total_count
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取视频详情
def videoDetail(request):
  # 获取参数
  id = request.POST.get('id')
  user_id = request.POST.get('user_id')
  try:
    video = Video.objects.get(id=id)
    if not video:
      raise Exception("不存在")
    data = VideoS(video).data
    if user_id:
      favCheck = FavVideo.objects.filter(Q(video_id=id), Q(user_id=user_id))
      if favCheck.exists():
        data['fav'] = 1
      else:
        data['fav'] = 0
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 添加视频
def videoAdd(request):
  # 获取参数
  cate_id = request.POST.get('cate_id')
  title = request.POST.get('title')
  content = request.POST.get('content')
  img_url = request.POST.get('img_url')
  video_url = request.POST.get('video_url')
  try:
    video = Video(
      cate_id = cate_id,
      title = title,
      img_url = img_url,
      video_url = video_url,
      content = content
    )
    video.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 上传视频封面
def videoUploadImg(request):
  # 获取参数
  file_obj = request.FILES.get('file')
  try:
    file_path=os.path.join('static','video_file', 'img', file_obj.name)
    f = open(file_path, 'wb')
    print(file_obj, type(file_obj))
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    return JsonResponse({"code": 0, "data": file_path}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 上传视频
def videoUploadVideo(request):
  # 获取参数
  file_obj = request.FILES.get('file')
  try:
    file_path=os.path.join('static','video_file', 'video', file_obj.name)
    f = open(file_path, 'wb')
    print(file_obj, type(file_obj))
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    return JsonResponse({"code": 0, "data": file_path}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)


@api_view(['GET',"POST"])
# 收藏视频
def videoFav(request):
  # 获取参数
  video_id = request.POST.get('video_id')
  user_id = request.POST.get('user_id')
  try:
    if not video_id or not user_id:
      raise Exception("参数错误")
    checkFav = FavVideo.objects.filter(Q(video_id=video_id), Q(user_id=user_id))
    if checkFav.exists():
      checkFav = checkFav.first()
      checkFav.delete()
    else:
      favData = FavVideo(user_id=user_id, video_id=video_id)
      favData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取个人收藏列表
def videoFavList(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  try:
    if not user_id:
      raise Exception("参数错误")
    checkFav = FavVideo.objects.filter(user_id=user_id)
    list = []
    for item in checkFav:
      itemData = {}
      itemData['id'] = item.id
      itemData['user_id'] = item.user_id
      itemData['video_id'] = item.video_id
      itemData['video_info'] = VideoS(Video.objects.get(id=item.video_id), many=False).data
      list.append(itemData)
    return JsonResponse({"code": 0, "data": list}, safe=False)
  except Exception as e:
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
