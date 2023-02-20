from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from base import views

app_name = 'products'
router = DefaultRouter()
router.register(r'products',views.ItemViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/',include(router.urls)),
    path('getdata/',include('base.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)