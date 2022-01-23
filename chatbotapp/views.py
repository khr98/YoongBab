from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from chatbotapp.functions.menuFormatting import makeWeekendReply, menuFormat
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
    menus = ChaSeDae.objects.all();

    if return_str == "차세대융합기술원":
        # 여기에 데이터 베이스에서 차세대 융합기술원에서 하루 전체 메뉴가져오는 로직 지금은 text 로 dummy 로 쓰겠음
        text = "오늘 차세대융합기술원 식단\n\n"
        menu = ChaSeDae.objects.filter(date=date.today())[0]

        text += menuFormat("[맘스]", menu.moms)
        text += menuFormat("[셰프]", menu.chef)
        text += menuFormat("[정찬]", menu.special)
        text += menuFormat("[샐러드]", menu.salad)
        text += menuFormat("[저녁]", menu.dinner)
        text += menuFormat("[TakeOut]", menu.takeOut)

        # 실제 보여줄 음식에 대한 메뉴는 위에서 처리했다 이 밑에는 이제 사용자의 클릭을 유도하는 메뉴 생성
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        return JsonResponse(response)

    elif return_str == "월요일차세대융합기술원":
        text = "월요일 차세대융합기술원식단\n\n"
        
        text += menuFormat("[맘스]", menus[0].moms)
        text += menuFormat("[셰프]", menus[0].chef)
        text += menuFormat("[정찬]", menus[0].special)
        text += menuFormat("[샐러드]", menus[0].salad)
        text += menuFormat("[저녁]", menus[0].dinner)
        text += menuFormat("[TakeOut]", menus[0].takeOut)
        
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        print(response)
        return JsonResponse(response)
    
    elif return_str == "화요일차세대융합기술원":
        text = "화요일 차세대융합기술원식단\n\n"
        
        text += menuFormat("[맘스]", menus[1].moms)
        text += menuFormat("[셰프]", menus[1].chef)
        text += menuFormat("[정찬]", menus[1].special)
        text += menuFormat("[샐러드]", menus[1].salad)
        text += menuFormat("[저녁]", menus[1].dinner)
        text += menuFormat("[TakeOut]", menus[1].takeOut)
        
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        print(response)
        return JsonResponse(response)
    
    elif return_str == "수요일차세대융합기술원":
        text = "수요일 차세대융합기술원식단\n\n"
        
        text += menuFormat("[맘스]", menus[2].moms)
        text += menuFormat("[셰프]", menus[2].chef)
        text += menuFormat("[정찬]", menus[2].special)
        text += menuFormat("[샐러드]", menus[2].salad)
        text += menuFormat("[저녁]", menus[2].dinner)
        text += menuFormat("[TakeOut]", menus[2].takeOut)
        
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        print(response)
        return JsonResponse(response)
    
    elif return_str == "목요일차세대융합기술원":
        text = "목요일 차세대융합기술원식단\n\n"
        
        text += menuFormat("[맘스]", menus[3].moms)
        text += menuFormat("[셰프]", menus[3].chef)
        text += menuFormat("[정찬]", menus[3].special)
        text += menuFormat("[샐러드]", menus[3].salad)
        text += menuFormat("[저녁]", menus[3].dinner)
        text += menuFormat("[TakeOut]", menus[3].takeOut)
        
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        print(response)
        return JsonResponse(response)
    
    elif return_str == "금요일차세대융합기술원":
        text = "금요일 차세대융합기술원식단\n\n"
        
        text += menuFormat("[맘스]", menus[4].moms)
        text += menuFormat("[셰프]", menus[4].chef)
        text += menuFormat("[정찬]", menus[4].special)
        text += menuFormat("[샐러드]", menus[4].salad)
        text += menuFormat("[저녁]", menus[4].dinner)
        text += menuFormat("[TakeOut]", menus[4].takeOut)
        
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        print(response)
        return JsonResponse(response)
        



@csrf_exempt
def get_nano(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == "한국나노기술원":
        answer = "더미"
        return JsonResponse(answer)
    elif return_str == "한국나노기술원문의사항":
        text = "⏰ 운영시간안내\n - 중식 11:30 ~ 13:10\n" \
               "- 석식 17:30 ~ 18:30\n\n" \
               "📃 상기 식단은 시장 동향에 따라 변경될 수 있는 점 양해 바랍니다.\n" \
               "📜 원산지 표시\n" \
               "쌀(국내산), 배추김치(맛김치 - 배추: 국내산, 고춧가루: 중국산)" \
               "깍두기(무 : 국내산, 고춧가루 : 중국산) 우육(호주산,미국산), 돈육" \
               "(국내산,수입산), 계육(국산) 식육가공품(국내산/수입산)\n" \
               "제공되는 메뉴 및 원산지는 식자재 수급 현황에 따라 변경 될 수 있으니" \
               "정확한 정보는 식당 입구에 게시된 일일메뉴표를 참고바랍니다."
        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)


@csrf_exempt
def get_R_DB(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == "경기 RDB":
        answer = "더미"
        return JsonResponse(answer)
    elif return_str == "경기RDB문의사항":
        text = "⏰ 운영시간안내\n - 중식 11:30 ~ 13:10\n" \
               "- 석식 17:30 ~ 18:30\n\n" \
               "📃 상기 식단은 시장 동향에 따라 변경될 수 있는 점 양해 바랍니다.\n" \
               "📜 원산지 표시\n" \
               "쌀(국내산), 배추김치(맛김치 - 배추: 국내산, 고춧가루: 중국산)" \
               "깍두기(무 : 국내산, 고춧가루 : 중국산) 우육(호주산,미국산), 돈육" \
               "(국내산,수입산), 계육(국산) 식육가공품(국내산/수입산)\n" \
               "제공되는 메뉴 및 원산지는 식자재 수급 현황에 따라 변경 될 수 있으니" \
               "정확한 정보는 식당 입구에 게시된 일일메뉴표를 참고바랍니다."

