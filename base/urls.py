from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint),
    path('advocates/', views.advocate_list),
    path('advocates/<str:username>/', views.advocate_details),
]
