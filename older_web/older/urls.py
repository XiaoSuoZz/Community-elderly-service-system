"""older URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from older import view_staff
from older import view_user
from older import view_area
from older import view_video
from older import view_news
from older import view_message_board
from older import view_appointment
from older import view_instant_call
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('user/', views.user),
    path('video/', views.video),
    path('news/', views.news),
    path('message_board/', views.message_board),
    path('appointment/', views.appointment),

    # web用户登录
    path('staffLogin', view_staff.staffLogin, name='staffLogin'),
    # 用户
    path('userList', view_user.userList, name='userList'),
    path('userAdd', view_user.userAdd, name='userAdd'),
    path('userLogin', view_user.userLogin, name='userLogin'),
    path('userRegister', view_user.userRegister, name='userRegister'),
    path('userDetail', view_user.userDetail, name='userDetail'),
    path('userEdit', view_user.userEdit, name='userEdit'),
    path('userCareLevelAi', view_user.userCareLevelAi, name='userCareLevelAi'),
    # 地区列表
    path('areaList', view_area.areaList, name='areaList'),
    # 视频
    path('videoCateList', view_video.videoCateList, name='videoCateList'),
    path('videoList', view_video.videoList, name='videoList'),
    path('videoUploadImg', view_video.videoUploadImg, name='videoUploadImg'),
    path('videoUploadVideo', view_video.videoUploadVideo, name='videoUploadVideo'),
    path('videoAdd', view_video.videoAdd, name='videoAdd'),
    path('videoDetail', view_video.videoDetail, name='videoDetail'),
    path('videoFav', view_video.videoFav, name='videoFav'),
    path('videoFavList', view_video.videoFavList, name='videoFavList'),
    # 新闻
    path('newsCateList', view_news.newsCateList, name='newsCateList'),
    path('newsList', view_news.newsList, name='newsList'),
    path('newsAdd', view_news.newsAdd, name='newsAdd'),
    path('newsDetail', view_news.newsDetail, name='newsDetail'),
    path('newsFav', view_news.newsFav, name='newsFav'),
    path('newsFavList', view_news.newsFavList, name='newsFavList'),
    # 留言板
    path('messageBoardSend', view_message_board.messageBoardSend, name='messageBoardSend'),
    path('messageBoardList', view_message_board.messageBoardList, name='messageBoardList'),
    path('messageBoardDeal', view_message_board.messageBoardDeal, name='messageBoardDeal'),
    # 预约服务
    path('appointmentAdd', view_appointment.appointmentAdd, name='appointmentAdd'),
    path('appointmentList', view_appointment.appointmentList, name='appointmentList'),
    path('appointmentDateList', view_appointment.appointmentDateList, name='appointmentDateList'),
    # 一键呼叫
    path('instantCallAdd', view_instant_call.instantCallAdd, name='instantCallAdd'),
    path('instantCallList', view_instant_call.instantCallList, name='instantCallList'),
    path('instantCallDeal', view_instant_call.instantCallDeal, name='instantCallDeal')

]
