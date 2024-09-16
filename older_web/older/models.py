from django.db import models

# 工作人员类
class Staff(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 姓名
    account = models.CharField(max_length=45) # 账户
    password = models.CharField(max_length=45) # 密码
    status = models.SmallIntegerField(default=1) # 状态： 1-有效，2-禁用

    class Meta:
        managed = False
        db_table = 'staff'

# 用户类
class User(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    account = models.CharField(max_length=45) # 账户
    password = models.CharField(max_length=45) # 密码
    name = models.CharField(max_length=45) # 姓名
    sex = models.SmallIntegerField(default=0) # 性别
    birth_place_code = models.CharField(max_length=45) # 籍贯编码
    area_code = models.CharField(max_length=45) # 现住地编码
    area_detail = models.CharField(max_length=200) # 现住地详细地址
    phone = models.CharField(max_length=45) # 电话
    emergency_contact_name = models.CharField(max_length=45) # 紧急联络人姓名
    emergency_contact_phone = models.CharField(max_length=45) # 紧急联络人电话
    emergency_contact_relationship = models.CharField(max_length=45) # 与紧急联络人关系
    is_marry = models.SmallIntegerField(default=0) # 婚姻状况：0-未婚 1-已婚
    is_live_alone = models.SmallIntegerField(default=0) # 是否独居：0-否 1-是
    is_disability = models.SmallIntegerField(default=0) # 是否残疾：0-否 1-是
    diseases_history = models.CharField(max_length=200) # 疾病史 JSON数组
    major_diseases_history = models.CharField(max_length=200) # 重大疾病史 JSON数组
    status = models.SmallIntegerField(default=1) # 状态：0-禁用 1-有效
    birthday = models.DateField() #生日
    care_level = models.SmallIntegerField() # 关照等级：1-5
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = False
        db_table = 'user'


# 地区字典类
class DictArea(models.Model):
    id = models.AutoField(primary_key=True) # id
    code = models.CharField(max_length=45) # 编码
    p_code = models.CharField(max_length=45) # 父地区编码
    level = models.SmallIntegerField(default=0) # 等级 1-省 2-市 3-区县
    name = models.CharField(max_length=45) # 名称

    class Meta:
        managed = False
        db_table = 'dict_area'

# 视频分类字典类
class DictVideoCate(models.Model):
    id = models.AutoField(primary_key=True) # id
    name = models.CharField(max_length=45) # 名称
    status = models.SmallIntegerField(default=1) # 状态 0-作废 1-有效

    class Meta:
        managed = False
        db_table = 'dict_video_cate'

# 新闻分类字典类
class DictNewsCate(models.Model):
    id = models.AutoField(primary_key=True) # id
    name = models.CharField(max_length=45) # 名称
    status = models.SmallIntegerField(default=1) # 状态 0-作废 1-有效

    class Meta:
        managed = False
        db_table = 'dict_news_cate'

# 视频类
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    img_url = models.CharField(max_length=160, blank=True, null=True)
    video_url = models.CharField(max_length=160, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=1, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'

# 视频收藏
class FavVideo(models.Model):
    id = models.AutoField(primary_key=True) # id
    user_id = models.IntegerField() # 用户id
    video_id = models.IntegerField() # 视频id
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fav_video'

# 新闻类
class News(models.Model):
    id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=1, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

# 新闻收藏
class FavNews(models.Model):
    id = models.AutoField(primary_key=True) # id
    user_id = models.IntegerField() # 用户id
    news_id = models.IntegerField() # 新闻id
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fav_news'

# 留言板
class MessageBoard(models.Model):
    id = models.AutoField(primary_key=True) # id
    user_id = models.IntegerField() # 用户id
    message = models.CharField(max_length=160, blank=True, null=True) # 留言内容
    status = models.IntegerField(default=1) # 状态 1-新建 2-已处理
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_board'

# 预约服务
class Appointment(models.Model):
    id = models.AutoField(primary_key=True) # id
    user_id = models.IntegerField() # 用户id
    type = models.IntegerField() # 服务类型 1-家政服务 2-医疗检查 3-药品配送 4-代买购物
    detail = models.CharField(max_length=160, blank=True, null=True) # 详情内容
    comment = models.CharField(max_length=160, blank=True, null=True) # 反馈内容
    status = models.IntegerField(default=1) # 状态 1-新建 2-已处理
    date = models.DateField()
    time = models.TimeField()
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'

# 即时呼叫
class InstantCall(models.Model):
    id = models.AutoField(primary_key=True) # id
    user_id = models.IntegerField() # 用户id
    status = models.IntegerField(default=1) # 状态 1-新建 2-已处理
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instant_call'