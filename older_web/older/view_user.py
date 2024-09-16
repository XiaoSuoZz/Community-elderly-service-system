from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.db.models import Q
from datetime import datetime, timedelta
from .view_ai import *

# 格式化地区的方法
def formatWholeArea(code):
  if not code:
    return ''
  areaArr = []
  area3 = DictArea.objects.get(code = code)
  if area3:
    areaArr.append(area3.name)
    if area3.p_code:
      area2 = DictArea.objects.get(code = area3.p_code)
      if area2:
        areaArr.append(area2.name)
        if area2.p_code:
          area1 = DictArea.objects.get(code = area2.p_code)
          if area1:
            areaArr.append(area1.name)
  areaArr.reverse()
  return (',').join(areaArr)

@api_view(['GET',"POST"])
# 用户登录
def userLogin(request):
  # 获取参数
  account = request.POST.get('account')
  password = request.POST.get('password')
  print("userLogin:", account, password)
  print("userLogin:", request.POST)
  try:
    if not account or not password:
      raise Exception("登陆失败：账户/密码缺失")
    checkUser = User.objects.filter(account=account).first()
    if not checkUser:
      raise Exception("登陆失败：用户不存在")
    if checkUser.status == 0:
      raise Exception("登陆失败：用户已被禁用")
    if checkUser.password != password:
      # 用户存在,密码不一致,则直接返回错误消息
      raise Exception("登陆失败：密码错误")
    checkUser = UserS(checkUser, many = False).data
    return JsonResponse({"code": 0, "data": checkUser}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 用户注册
def userRegister(request):
  # 获取参数
  print(str(request))
  name = request.POST.get('name')
  account = request.POST.get('account')
  password = request.POST.get('password')
  sex = request.POST.get('sex')
  birthDateTimestamp = request.POST.get('birthDateTimestamp')
  birthDate = request.POST.get('birthDate')
  print("userRegister:", name, account)
  try:
    if not name or not account or not password:
      raise Exception("注册失败：信息不完整")
    checkUser = User.objects.filter(account=account).first()
    if checkUser:
      raise Exception("注册失败：该账户已存在")
    newUser = User(
      account=account,
      password = password,
      name = name,
      birthday = birthDate,
      sex = sex
    )
    newUser.save()
    return JsonResponse({"code": 0, "data": ''}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

@api_view(['GET',"POST"])
# 添加用户
def userAdd(request):
  # 获取参数
  account = request.POST.get('account')
  password = request.POST.get('password')
  name = request.POST.get('name')
  phone = request.POST.get('phone')
  birthDate = request.POST.get('birthDate')
  sex = request.POST.get('sex')
  isMarry = request.POST.get('isMarry')
  isLiveAlone = request.POST.get('isLiveAlone')
  isDisability = request.POST.get('isDisability')
  diseasesHistory = request.POST.get('diseasesHistory')
  majorDiseasesHistory = request.POST.get('majorDiseasesHistory')
  emergencyContactName = request.POST.get('emergencyContactName')
  emergencyContactRelationship = request.POST.get('emergencyContactRelationship')
  emergencyContactPhone = request.POST.get('emergencyContactPhone')
  birthPlace = request.POST.get('birthPlace')
  areaCode = request.POST.get('areaCode')
  areaDetail = request.POST.get('areaDetail')
  checkUser = User.objects.filter(account=account).first()
  try:
    if checkUser:
      raise Exception("添加失败：该账户已注册")
    newUser = User(
      account=account,
      password = password,
      name = name,
      phone = phone,
      birthday = birthDate,
      sex = sex,
      is_marry = isMarry,
      is_live_alone = isLiveAlone,
      is_disability = isDisability,
      diseases_history = diseasesHistory,
      major_diseases_history = majorDiseasesHistory,
      emergency_contact_name = emergencyContactName,
      emergency_contact_relationship = emergencyContactRelationship,
      emergency_contact_phone = emergencyContactPhone,
      birth_place_code = birthPlace,
      area_code = areaCode,
      area_detail = areaDetail,
    )
    newUser.save()
    return JsonResponse({"code": 0}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)
    
@api_view(['GET',"POST"])
# 用户列表
def userList(request):
  # 获取参数
  page_index = int(request.POST.get('page_index'))
  page_size = int(request.POST.get('page_size'))
  name = request.POST.get('name')
  sex = request.POST.get('sex')
  age = request.POST.get('age')
  isMarry = request.POST.get('isMarry')
  careLevel = request.POST.get('careLevel')
  isLiveAlone = request.POST.get('isLiveAlone')
  isDisability = request.POST.get('isDisability')
  try:
    userList = User.objects.all()
    if name:
      userList = userList.filter(name__icontains=name)
    if sex:
      userList = userList.filter(sex=sex)
    if careLevel:
      userList = userList.filter(care_level=careLevel)
    if age:
      today = datetime.today()
      start_year = today.year - int(age) - 1
      end_year = today.year - int(age)
      start_date = datetime.strptime('-'.join([str(start_year), str(today.month), str(today.day)]), '%Y-%m-%d')
      end_date = datetime.strptime('-'.join([str(end_year), str(today.month), str(today.day)]), '%Y-%m-%d')
      userList = userList.filter(Q(birthday__gt=start_date), Q(birthday__lt=end_date))
    if isMarry:
      userList = userList.filter(is_marry=isMarry)
    if isLiveAlone:
      userList = userList.filter(is_live_alone=isLiveAlone)
    if isDisability:
      userList = userList.filter(is_disability=isDisability)  
    total_count = userList.count()
    userList=userList[(page_index - 1) * page_size : page_index * page_size]
    dataList = []
    today = datetime.today()
    for item in userList:
      obj = {}
      obj['id'] = item.id
      obj['account'] = item.account
      obj['name'] = item.name
      obj['sex'] = item.sex
      obj['birth_place_code'] = item.birth_place_code
      if item.birth_place_code:
        obj['birth_place_str'] = DictArea.objects.get(code=item.birth_place_code).name
      obj['area_code'] = item.area_code
      if item.area_code:
        obj['area_str'] = formatWholeArea(item.area_code)
      obj['area_detail'] = item.area_detail
      obj['phone'] = item.phone
      obj['emergency_contact_name'] = item.emergency_contact_name
      obj['emergency_contact_phone'] = item.emergency_contact_phone
      obj['emergency_contact_relationship'] = item.emergency_contact_relationship
      obj['is_marry'] = item.is_marry
      obj['is_live_alone'] = item.is_live_alone
      obj['is_disability'] = item.is_disability
      obj['diseases_history'] = item.diseases_history
      obj['major_diseases_history'] = item.major_diseases_history
      obj['birthday'] = item.birthday.strftime("%Y-%m-%d")
      obj['age'] = today.year - item.birthday.year
      obj['care_level'] = item.care_level
      dataList.append(obj)
    data = {}
    data["list"] = dataList
    data["total_count"] = total_count
    return JsonResponse({"code": 0, "data": data }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)

    
@api_view(['GET',"POST"])
# 用户详情
def userDetail(request):
  # 获取参数
  id = int(request.POST.get('id'))
  try:
    userData = User.objects.get(id=id)
    if not userData:
      raise Exception("获取用户信息失败")
    obj = {}
    obj['id'] = userData.id
    obj['account'] = userData.account
    obj['password'] = userData.password
    obj['name'] = userData.name
    obj['sex'] = userData.sex
    obj['birth_place_code'] = userData.birth_place_code
    if userData.birth_place_code:
      obj['birth_place_str'] = DictArea.objects.get(code=userData.birth_place_code).name
    obj['area_code'] = userData.area_code
    if userData.area_code:
      obj['area_str'] = formatWholeArea(userData.area_code)
    obj['area_detail'] = userData.area_detail
    obj['phone'] = userData.phone
    obj['emergency_contact_name'] = userData.emergency_contact_name
    obj['emergency_contact_phone'] = userData.emergency_contact_phone
    obj['emergency_contact_relationship'] = userData.emergency_contact_relationship
    obj['is_marry'] = userData.is_marry
    obj['is_live_alone'] = userData.is_live_alone
    obj['is_disability'] = userData.is_disability
    obj['diseases_history'] = userData.diseases_history
    obj['major_diseases_history'] = userData.major_diseases_history
    obj['birthday'] = userData.birthday.strftime("%Y-%m-%d")
    obj['age'] = datetime.today().year - userData.birthday.year
    obj['care_level'] = userData.care_level
    return JsonResponse({"code": 0, "data": obj }, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)


@api_view(['GET',"POST"])
# 编辑用户
def userEdit(request):
  # 获取参数
  id = request.POST.get('id')
  password = request.POST.get('password')
  name = request.POST.get('name')
  phone = request.POST.get('phone')
  birthDate = request.POST.get('birthDate')
  sex = request.POST.get('sex')
  isMarry = request.POST.get('isMarry')
  isLiveAlone = request.POST.get('isLiveAlone')
  isDisability = request.POST.get('isDisability')
  diseasesHistory = request.POST.get('diseasesHistory')
  majorDiseasesHistory = request.POST.get('majorDiseasesHistory')
  emergencyContactName = request.POST.get('emergencyContactName')
  emergencyContactRelationship = request.POST.get('emergencyContactRelationship')
  emergencyContactPhone = request.POST.get('emergencyContactPhone')
  birthPlace = request.POST.get('birthPlace')
  areaCode = request.POST.get('areaCode')
  areaDetail = request.POST.get('areaDetail')
  checkUser = User.objects.get(id=id)
  try:
    if not checkUser:
      raise Exception("保存失败：查无此用户")
    checkUser.password = password
    checkUser.name = name
    checkUser.phone = phone
    checkUser.birthday = birthDate
    checkUser.sex = sex
    checkUser.is_marry = isMarry
    checkUser.is_live_alone = isLiveAlone
    checkUser.is_disability = isDisability
    checkUser.diseases_history = diseasesHistory
    checkUser.major_diseases_history = majorDiseasesHistory
    checkUser.emergency_contact_name = emergencyContactName
    checkUser.emergency_contact_relationship = emergencyContactRelationship
    checkUser.emergency_contact_phone = emergencyContactPhone
    checkUser.birth_place_code = birthPlace
    checkUser.area_code = areaCode
    checkUser.area_detail = areaDetail
    checkUser.save()
    return JsonResponse({"code": 0}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)


@api_view(['GET',"POST"])
# 关注评级
def userCareLevelAi(request):
  # 获取参数
  id = request.POST.get('id')
  checkUser = User.objects.get(id=id)
  try:
    # if not checkUser:
    #   raise Exception("识别失败：查无此用户")
    is_marry = str(checkUser.is_marry)
    is_live_alone = str(checkUser.is_live_alone)
    is_disability = str(checkUser.is_disability)
    diseases_history = str(len(json.loads(checkUser.diseases_history)))
    major_diseases_history = str(len(json.loads(checkUser.major_diseases_history)))
    checkUser.care_level = ai_level(is_marry, is_live_alone, is_disability, diseases_history, major_diseases_history)
    print(checkUser.care_level)
    checkUser.save()
    return JsonResponse({"code": 0, "data": str(checkUser.care_level)}, safe=False)
  except Exception as e:
    print(str(e))
    return JsonResponse({"code": -1, "data": str(e)}, safe=False)