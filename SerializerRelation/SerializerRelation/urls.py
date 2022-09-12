
from django.contrib import admin
from django.db import router
from django.urls import path,include
from relation import views
from rest_framework .routers import DefaultRouter


router= DefaultRouter()

router.register('song',views.singerviewset, basename='song'),
router.register('singer', views.songviewset,basename='singer'),



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    
]
