from django.urls import path
from . import views

app_name='chatbot'

urlpatterns = [
    path('', views.menu_list, name="list"),
    path('create/chaSaDae/', views.menu_create, name="create-chaSaDae"),
    path('create/nano/', views.menu_create, name="create-nano"),
    path('create/R-DB/', views.menu_create, name="create-R-DB"),
    path('menu/chaSeDae/', views.get_chaSeDae, name="menu-chaSeDae"),
    path('menu/nano/', views.get_nano, name="menu-nano"),
    path('menu/R-DB/', views.get_R-DB, name="menu-R-DB"),
]