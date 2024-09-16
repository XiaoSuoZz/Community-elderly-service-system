from rest_framework.decorators import api_view
from django.http import JsonResponse

from .serializers import *
from .models import *
from django.db.models import Q

@api_view(['GET',"POST"])
# 一键呼叫
def instantCallAdd(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  try:
    newData = InstantCall(user_id=user_id, status=1)
    newData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取最新的一键呼叫
def instantCallList(request):
  try:
    callList = InstantCall.objects.filter(Q(status=1)).order_by('-create_time')
    list = []
    for item in callList:
      obj = {}
      obj['id'] = item.id
      obj['user_id'] = item.user_id
      obj['create_time'] = item.create_time
      obj['status'] = item.status
      obj['user_info'] = UserS(User.objects.get(id=item.user_id), many=False).data
      list.append(obj)
    return JsonResponse({"code": 0, "data": list }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
  

@api_view(['GET',"POST"])
# 一键呼叫已处理
def instantCallDeal(request):
  # 获取参数
  id = request.POST.get('id')
  try:
    checkData = InstantCall.objects.get(id=id)
    if checkData:
      checkData.status=2
      checkData.save()
    return JsonResponse({"code": 0 }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)