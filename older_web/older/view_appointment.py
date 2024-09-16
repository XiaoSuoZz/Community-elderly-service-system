from rest_framework.decorators import api_view
from django.http import JsonResponse

from older.serializers import AppointmentS
from .models import *
from django.db.models import Q

@api_view(['GET',"POST"])
# 预约服务
def appointmentAdd(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  type = request.POST.get('type')
  detail = request.POST.get('detail')
  date = request.POST.get('date')
  time = request.POST.get('time')
  try:
    if not user_id or not date or not time:
      raise Exception("参数错误")
    checkAppointment = Appointment.objects.filter(Q(date=date), Q(time=time), ~Q(status=0))
    if checkAppointment.exists():
      raise Exception("预约失败：该时间无法预约")
    newData = Appointment(user_id=user_id, type=type, detail=detail, date=date, time=time, status=1)
    newData.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 获取预约列表
def appointmentList(request):
  # 获取参数
  page_index = int(request.POST.get('page_index'))
  page_size = int(request.POST.get('page_size'))
  user_id = request.POST.get('user_id')
  type = request.POST.get('type')
  status = request.POST.get('status')
  date = request.POST.get('date')
  try:
    appointmentList = Appointment.objects.filter(~Q(status=0)).order_by('status')
    if user_id:
      appointmentList = Appointment.objects.filter(user_id=user_id)
    if type:
      appointmentList = Appointment.objects.filter(type=type)
    if date:
      appointmentList = Appointment.objects.filter(date=date)
    if status:
      appointmentList = Appointment.objects.filter(status=status)
    total_count = appointmentList.count()
    appointmentList=appointmentList[(page_index - 1) * page_size : page_index * page_size]
    dataList = []
    for item in appointmentList:
      obj = {}
      obj['id'] = item.id
      obj['type'] = item.type
      obj['date'] = item.date
      obj['time'] = item.time
      obj['detail'] = item.detail
      obj['comment'] = item.comment
      obj['status'] = item.status
      obj['create_time'] = item.create_time
      obj['user_id'] = item.user_id
      obj['user_name'] = User.objects.get(id=item.user_id).name
      obj['user_phone'] = User.objects.get(id=item.user_id).phone
      obj['user_address'] = User.objects.get(id=item.user_id).area_detail
      dataList.append(obj)
    data = {}
    data["list"] = dataList
    data["total_count"] = total_count
    return JsonResponse({"code": 0, "data": data }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
  

@api_view(['GET',"POST"])
# 获取当日已预约的时间
def appointmentDateList(request):
  # 获取参数
  date = request.POST.get('date')
  try:
    if not date:
      raise Exception("参数错误")
    checkData = Appointment.objects.filter(Q(date=date), ~Q(status=0)).values('time')
    list = []
    for item in checkData:
      list.append(item['time'])
    return JsonResponse({"code": 0, "data": list}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
