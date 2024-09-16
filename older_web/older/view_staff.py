from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from django.db.models import Q

@api_view(['GET',"POST"])
# 工作人员登录
def staffLogin(request):
  # 获取参数
  account = request.POST.get('account')
  password = request.POST.get('password')
  print("staffLogin:", account, password)
  checkStaff = Staff.objects.filter(account=account).first()
  try:
    if not checkStaff:
      raise Exception("登陆失败：用户不存在")
    if checkStaff.status == 0:
      raise Exception("登陆失败：用户已被禁用")
    if checkStaff.password != password:
      # 用户存在,密码不一致,则直接返回错误消息
      raise Exception("登陆失败：密码错误")
    # 登陆成功
    data = {
      'id': checkStaff.id,
      'name': checkStaff.name,
      'account': checkStaff.account,
      'password': checkStaff.password
    }
    return JsonResponse({"code": 0, "data": data}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)