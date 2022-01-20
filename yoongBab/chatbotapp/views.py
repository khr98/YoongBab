from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.
def menu_list(request):
    menus = ChaSeDae.objects.all();
    return render(request, template_name='menu_list.html', context={'menus':menus})

def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST,request.FILES)
        if form.is_valid():
            menu = form.save()
            return redirect('chatbot:list')
    else:
        form = MenuForm()
    ctx = {'form': form}
    return render(request, template_name='menu_form.html', context=ctx)