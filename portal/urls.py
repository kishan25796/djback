from django.urls import path
from . import views

urlpatterns = [
    path('hw/', views.homew, name = "homew"),
    path('hw/<str:pk>/', views.gethw, name = "home"),
]