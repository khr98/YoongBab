from django.urls import path
from . import views

app_name='chatbot'

urlpatterns = [
    path('', views.menu_list, name="list"),
    path('create/', views.menu_create, name="create"),
]