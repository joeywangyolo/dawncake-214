from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='group'),
    path('events/', views.events, name='events'),
    path('plans/', views.plans, name='plans'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_page, name="logout"),
    path('mb_edit/', views.mb_edit, name="mb_edit"),

    #會員管理、會員設定
    path('members/', views.members, name='members'),
    path('member-setting/', views.member_setting, name='member-setting'),
    url('^creat_member/', views.creat_member, name='creat_member'),
    path('member_level/', views.member_level, name='member_level'),
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