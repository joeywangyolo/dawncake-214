from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from base.models import Product,Item

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin']
        
    def get_isAdmin(self, obj):
        return obj.is_staff
        
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

class ItemSerializer(serializers.ModelSerializer):
    author =UserSerializer(read_only=True)
    class Meta:
        model = Item
        fields ='__all__'

class UserDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email"]
class productSerializer(serializers.HyperlinkedModelSerializer):
    # author = UserDescSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'

   

