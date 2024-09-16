from django.shortcuts import render

# 页面渲染
#登陆页面
def login(request):
  return render(request, 'login.html')

def user(request):
  return render(request, 'user.html')
def video(request):
  return render(request, 'video.html')
def news(request):
  return render(request, 'news.html')
def message_board(request):
  return render(request, 'message_board.html')
def appointment(request):
  return render(request, 'appointment.html')
