from django.urls import path
from . import views


urlpatterns = [
    path('', views.AccountCreate.as_view()),
    
]