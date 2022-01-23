from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .kakaojsonformat.response import insert_text, make_reply, insert_replies
from .form import *
import json
from datetime import date


# Create your views here.

@csrf_exempt
def menu_list(request):
    menus = ChaSeDae.objects.all();
    return render(request, template_name='menu_list.html', context={'menus': menus})


@csrf_exempt
def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save()
            return redirect('chatbot:list')
    else:
        form = MenuForm()
    ctx = {'form': form}
    return render(request, template_name='menu_form.html', context=ctx)


@csrf_exempt
def get_chaSeDae(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    # menus = ChaSeDae.objects.all();

    if return_str == "차세대융합기술원":
        # 여기에 데이터 베이스에서 차세대 융합기술원에서 하루 전체 메뉴가져오는 로직 지금은 text 로 dummy 로 쓰겠음
        text = "오늘 차세대융합기술원 식단\n\n"
        menu = ChaSeDae.objects.filter(date=date.today())[0]
        text += "[맘스]\n"
        momsArray = menu.moms.split(",");

        for mom in momsArray:
            text += mom + '\n'

        text += "\n[셰프]\n"
        chefArray = menu.chef.split(",");
        for chef in chefArray:
            text += chef + '\n'


        print(text);

        # 실제 보여줄 음식에 대한 메뉴는 위에서 처리했다 이 밑에는 이제 사용자의 클릭을 유도하는 메뉴 생성
        answer = insert_text(text)
        reply = make_reply("월", "월요일차세대융합기술원")
        answer = insert_replies(answer, reply)

        reply = make_reply("화", "화요일차세대융합기술원")
        answer = insert_replies(answer, reply)

        return JsonResponse(answer)

    elif return_str == "월요일차세대융합기술원":
        menu = ChaSeDae.objects.filter(date=date.today());
