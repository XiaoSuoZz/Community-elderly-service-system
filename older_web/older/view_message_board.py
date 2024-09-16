from os import stat
from matplotlib.style import use
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from django.db.models import Q

@api_view(['GET',"POST"])
# 发布留言
def messageBoardSend(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  message = request.POST.get('message')
  try:
    if not user_id or not message:
      raise Exception("参数错误")
    newData = MessageBoard(user_id=user_id, message=message, status=1)
    newData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取留言列表
def messageBoardList(request):
  # 获取参数
  page_index = int(request.POST.get('page_index'))
  page_size = int(request.POST.get('page_size'))
  try:
    messageList = MessageBoard.objects.all().order_by('status')
    total_count = messageList.count()
    messageList=messageList[(page_index - 1) * page_size : page_index * page_size]
    dataList = []
    for item in messageList:
      obj = {}
      obj['id'] = item.id
      obj['user_id'] = item.user_id
      obj['message'] = item.message
      obj['create_time'] = item.create_time
      obj['status'] = item.status
      obj['user_name'] = User.objects.get(id=item.user_id).name
      obj['user_phone'] = User.objects.get(id=item.user_id).phone
      dataList.append(obj)
    data = {}
    data["list"] = dataList
    data["total_count"] = total_count
    return JsonResponse({"code": 0, "data": data }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
  

@api_view(['GET',"POST"])
# 处理留言
def messageBoardDeal(request):
  # 获取参数
  id = request.POST.get('id')
  try:
    if not id:
      raise Exception("参数错误")
    checkData = MessageBoard.objects.get(id=id)
    if not checkData:
      raise Exception("留言不存在")
    checkData.status = 2
    checkData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
