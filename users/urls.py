"""为应用程序users定义URL模式"""


from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
	# Login page.登录
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),
    	name='login'),

     # Logout page.注销
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

     # Registration page.注册
    path('register/', views.register, name='register'),
]