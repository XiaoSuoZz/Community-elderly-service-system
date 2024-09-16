from rest_framework import serializers
from .models import *

# 序列化，将orm数据模型中的数据集转换成数组

# 用户
class UserS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'care_level', 'account', 'password', 'name', 'sex', 'birth_place_code', 'area_code', 'area_detail', 'phone', 'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship', 'is_marry', 'is_live_alone', 'is_disability', 'diseases_history', 'major_diseases_history', 'status', 'birthday', 'create_time']

# 视频分类
class DictVideoCateS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DictVideoCate
        fields = ['id', 'name', 'status']

# 视频
class VideoS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'cate_id', 'title', 'img_url', 'video_url', 'content', 'status', 'create_time']

# 视频收藏
class FavVideoS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavVideo
        fields = ['id', 'user_id', 'video_id', 'create_time']

# 新闻分类
class DictNewsCateS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DictNewsCate
        fields = ['id', 'name', 'status']

# 新闻
class NewsS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'cate_id', 'title', 'content', 'status', 'create_time']

# 新闻收藏
class FavNewsS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavNews
        fields = ['id', 'user_id', 'news_id', 'create_time']

# 留言板
class MessageBoardS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageBoard
        fields = ['id', 'user_id', 'message', 'status', 'create_time']

# 预约服务
class AppointmentS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'user_id', 'type' 'detail', 'comment', 'date', 'time', 'status', 'create_time']

# 即时呼叫
class InstantCallS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InstantCall
        fields = ['id', 'user_id', 'status', 'create_time']