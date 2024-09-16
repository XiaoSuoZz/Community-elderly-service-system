from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from django.db.models import Q

@api_view(['GET',"POST"])
# 获取地区列表
def areaList(request):
  # 获取参数
  level = request.POST.get('level')
  p_code = request.POST.get('p_code')
  try:
    areaList = DictArea.objects.all()
    if level:
      areaList = areaList.filter(level=level)
    if p_code:
      areaList = areaList.filter(p_code=p_code)
    dataList = []
    for item in areaList:
      itemData = {}
      itemData["id"] = item.id
      itemData["code"] = item.code
      itemData["p_code"] = item.p_code
      itemData["name"] = item.name
      itemData["level"] = item.level
      dataList.append(itemData)
    data = {}
    data["list"] = dataList
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
  