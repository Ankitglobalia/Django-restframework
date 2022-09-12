
from django.contrib import admin
from django.urls import path
from Detail import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.GetStudent_Api),
    path('studentApi/<int:pk>',views.Student_Api),
]

