from django.shortcuts import render, redirect
from . models import User
from . forms import CustomUserCreationForm
from . serializers import UserSerializer, UserSerializerWithToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from PIL import Image
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    


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
            return redirect('index')
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
            return redirect('index')
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
# 屬性-標籤
# (1) 會員標籤
# (2) 交易標籤

# (3) 自訂標籤






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