from django.urls import path 

from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.SuccessView.as_view(), name='success')
]
