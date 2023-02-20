from django.shortcuts import render, redirect
from base.models import User,Product,Item
from . forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from PIL import Image
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
import datetime
from base.models import Product
import json
from django.http import JsonResponse,Http404
from rest_framework import viewsets,status,mixins,generics
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import ItemSerializer,productSerializer


class ItemList(generics.ListCreateAPIView):
    """ 
    List / Creat
    """
    queryset =Item.objects.all()
    serializer_class =ItemSerializer
class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Retrieve / UPdate / Destroy
    """
    queryset =Item.objects.all()
    serializer_class =ItemSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = productSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.save(author =self.request.user)
        serializer.save()


def login_page(request):
    page = 'login'
    
    if request.method == 'POST':
        user = authenticate(
            email=request.POST['email'], 
            password=request.POST['password']
            )
        
        if user is not None:
            login(request, user)
            messages.info(request, 'U successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Email OR Passwor is incorrect')
            return redirect('login')
    
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def register_page(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, 'Your account was created')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    
    page = 'register'
    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def logout_page(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def index(request):
    return render(request, 'base/index.html')


def group(request):
    return render(request, 'base/group.html')

def events(request):
    return render(request, 'base/events.html')

def plans(request):
    return render(request, 'base/plans.html')

def members(request):
    return render(request, 'base/members.html')

def profile(request):
    return render(request, 'base/profile.html')

def member_setting(request):
    return render(request, 'base/member_setting.html')

def mb_edit(request):
    return render(request, 'base/mb_edit.html')

member_category = list() # 會員類別內容
member_level=list()
def creat_member(request):
    global member_category
    update_time = datetime.datetime.now().date()
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name',None)
        brand_details = request.POST.get('brand_details',None)
        creat_time = request.POST.get('creat_time ',update_time)
        if brand_name :   
                return render(request,'base/member_category.html',{'msg':'{} , {} , {}'.format(brand_name,brand_details,creat_time)})
        else:
                return render(request,'base/member_category.html', {'msg':'請輸入完整資訊'})
         
    return render(request,'base/member_category.html',{'msg':'品牌名稱請輸入 日出 or 醉月樓','update_time':update_time})
# 屬性-標籤:
# (1) 會員標籤
# (2) 交易標籤

# (3) 自訂標籤
def member_level(request):
    global member_category,member_level
    update_time = datetime.datetime.now().date()
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name',None)
        brand_detils = request.POST.get('brand_detils',None)
        level_detils = request.POST.get('level_detils',None)
        if brand_name :   
                return render(request,'base/member_level.html',{'msg':'{},{},{}'.format(brand_name,brand_detils,update_time,level_detils)})
        else:
                
                return render(request,'base/member_level.html', {'msg':'請輸入完整資訊'})
         
    return render(request,'base/member_level.html',{'msg':'品牌名稱請輸入 日出 or 醉月樓','update_time':update_time})






def dashboard(request):
    return render(request, 'base/dashboard.html')

def schedule(request):
    return render(request, 'base/schedule.html')

def label(request):
    return render(request, 'base/label.html')

def account(request):
    return render(request, 'base/account.html')

def email(request):
    return render(request, 'base/email.html')

def SMS(request):
    return render(request, 'base/SMS.html')

def campaign(request):
    return render(request, 'base/campaign.html')

def system_setting(request):
    return render(request, 'base/system_setting.html')

def tools(request):
    return render(request, 'base/tools.html')