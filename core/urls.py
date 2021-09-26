from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>', views.DeleteJob, name='delete'),
]