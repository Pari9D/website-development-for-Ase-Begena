from django.urls import path
from . import views

urlpatterns = [
    path('api/bagans/', views.bagan_list_api),
    path('api/bagans/<int:id>/', views.bagan_detail_api),
]