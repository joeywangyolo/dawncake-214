from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']