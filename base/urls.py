from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint),
    path('advocates/', views.advocate_list, name='advocates'),
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),
    path('sentiment/', views.sentiment_list)
    # path('advocates/<str:username>/', views.advocate_details, name='advocate'),
]
