from django.urls import path
from . import views


urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/profile/', views.getUserProfile, name='user-profile'),
    path('api/users/register/', views.registerUser, name='register'),
    path('api/users/', views.getUsers, name='users'),
    
    path('', views.index, name='index'),
    path('group/', views.group, name='group'),
    path('events/', views.events, name='events'),
    path('plans/', views.plans, name='plans'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_page, name="logout"),

    #會員管理、會員設定
    path('members/', views.members, name='members'),
    path('member-setting/', views.member_setting, name='member-setting'),
    path('profile/', views.profile, name='profile'),
    
    
    # 屬性標籤
    path('label/', views.label, name='label'),
    
    # 行銷工具
    path('tools/', views.tools, name='tools'),
    
    # 行銷分析
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # 帳號管理
    path('account/', views.account, name='account'),
]