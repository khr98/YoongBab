import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbotapp.functions.menuFormatting import makeWeekendReply, menuFormat
from chatbotapp.functions.is_vacation import is_holiday
from chatbotapp.functions.weekdayConverter import weekConverter
from .kakaojsonformat.response import insert_text, make_reply, insert_replies
from .form import *
import json
from datetime import date, timedelta


# Create your views here.

@csrf_exempt
def menu_list(request):
    menus = ChaSeDae.objects.all();
    return render(request, template_name='menu_list.html', context={'menus': menus})


@csrf_exempt
def chaSeDae_create(request):
    if request.method == 'POST':
        form = chaSeDaeForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save()
            return redirect('chatbot:list')
    else:
        form = chaSeDaeForm()
    ctx = {'form': form}
    return render(request, template_name='menu_form.html', context=ctx)


@csrf_exempt
def nano_create(request):
    if request.method == 'POST':
        form = nanoForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save()
            return redirect('chatbot:list')
    else:
        form = nanoForm()
    ctx = {'form': form}
    return render(request, template_name='menu_form.html', context=ctx)


@csrf_exempt
def RDB_create(request):
    if request.method == 'POST':
        form = RDBForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save()
            return redirect('chatbot:list')
    else:
        form = RDBForm()
    ctx = {'form': form}
    return render(request, template_name='menu_form.html', context=ctx)


@csrf_exempt
def get_chaSeDae(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    menus = ChaSeDae.objects.all()

    # 오늘이 일요일인데 금요일을 호출한다
    # 30일인데 28일꺼 호출
    #  오늘 기준으로
    # 호출한 요일 - 오늘 요일 값을 오늘날짜에 날짜 연산으로 더해주면됌
    # delta 는 오늘기준으로 사용자가 선택한요일의 차이값입니다
    delta = weekConverter(return_str) - datetime.datetime.today().weekday()

    # selectedDay 는 사용자가 선택한 요일에 상응하는 날짜입니다
    selectedDay = date.today() + timedelta(days=delta)
    if return_str == "차세대융합기술원" or return_str == "🚗🚗🚗차세대융합기술원":

        if is_holiday():
            response = insert_text("공휴일에는 식단을 제공하지 않습니다😊\n 행복한 하루 되세요")
            return JsonResponse(response)

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
        # 여기서 menu 가 왜 안올까요???
        menu = ChaSeDae.objects.filter(date=selectedDay)[0]

        print(menu)

        text += menuFormat("[맘스]", menu.moms)
        text += menuFormat("[셰프]", menu.chef)
        text += menuFormat("[정찬]", menu.special)
        text += menuFormat("[샐러드]", menus[0].salad)
        text += menuFormat("[저녁]", menus[0].dinner)
        text += menuFormat("[TakeOut]", menus[0].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
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
        return JsonResponse(response)

    elif return_str == "차세대융합기술원문의사항":
        text = "📪 문의사항 : 우혜림 영양사 [prefla@naver.com] \n" \
               "031-888-9497 로 연락 바랍니다."
        response = insert_text(text)
        response = makeWeekendReply("차세대융합기술원", response)
        return JsonResponse(response)


@csrf_exempt
def get_nano(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    menus = Nano.objects.all();

    if return_str == "한국나노기술원" or return_str == "🍚한국나노기술원":
        # 여기에 데이터 베이스에서 차세대 융합기술원에서 하루 전체 메뉴가져오는 로직 지금은 text 로 dummy 로 쓰겠음
        if is_holiday():
            response = insert_text("공휴일에는 식단을 제공하지 않습니다😊\n 행복한 하루 되세요")
            return JsonResponse(response)
        text = "오늘 한국나노기술원 식단\n\n"
        menu = Nano.objects.filter(date=date.today())[0]

        text += menuFormat("[정성이 가득한 점심 A코너]", menu.lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menu.lunchB)
        text += menuFormat("[PLUS]", menu.plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menu.dinner)

        # 실제 보여줄 음식에 대한 메뉴는 위에서 처리했다 이 밑에는 이제 사용자의 클릭을 유도하는 메뉴 생성
        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)

        return JsonResponse(response)

    elif return_str == "월요일한국나노기술원":
        text = "월요일 한국나노기술원식단\n\n"

        text += menuFormat("[정성이 가득한 점심 A코너]", menus[0].lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menus[0].lunchB)
        text += menuFormat("[PLUS]", menus[0].plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menus[0].dinner)

        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)

    elif return_str == "화요일한국나노기술원":
        text = "화요일 한국나노기술원식단\n\n"

        text += menuFormat("[정성이 가득한 점심 A코너]", menus[1].lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menus[1].lunchB)
        text += menuFormat("[PLUS]", menus[1].plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menus[1].dinner)

        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)

    elif return_str == "수요일한국나노기술원":
        text = "수요일 한국나노기술원식단\n\n"

        text += menuFormat("[정성이 가득한 점심 A코너]", menus[2].lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menus[2].lunchB)
        text += menuFormat("[PLUS]", menus[2].plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menus[2].dinner)

        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)

    elif return_str == "목요일한국나노기술원":
        text = "목요일 한국나노기술원식단\n\n"

        text += menuFormat("[정성이 가득한 점심 A코너]", menus[3].lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menus[3].lunchB)
        text += menuFormat("[PLUS]", menus[3].plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menus[3].dinner)

        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)

    elif return_str == "금요일한국나노기술원":
        text = "금요일 한국나노기술원식단\n\n"

        text += menuFormat("[정성이 가득한 점심 A코너]", menus[4].lunchA)
        text += menuFormat("[정성이 가득한 점심 B코너]", menus[4].lunchB)
        text += menuFormat("[PLUS]", menus[4].plus)
        text += menuFormat("[하루를 마무리 하는 저녁]", menus[4].dinner)

        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)

    elif return_str == "한국나노기술원문의사항":
        text = "⏰ 운영시간안내\n- 중식 11:30 ~ 13:10\n" \
               "- 석식 17:30 ~ 18:30\n\n" \
               "📃 상기 식단은 시장 동향에 따라 변경될 수 있는 점 양해 바랍니다.\n\n" \
               "📜 원산지 표시\n" \
               "쌀(국내산), 배추김치(맛김치 - 배추: 국내산, 고춧가루: 중국산)" \
               "깍두기(무 : 국내산, 고춧가루 : 중국산) 우육(호주산,미국산), 돈육" \
               "(국내산,수입산), 계육(국산) 식육가공품(국내산/수입산)\n\n" \
               "제공되는 메뉴 및 원산지는 식자재 수급 현황에 따라 변경 될 수 있으니" \
               "정확한 정보는 식당 입구에 게시된 일일메뉴표를 참고바랍니다."
        response = insert_text(text)
        response = makeWeekendReply("한국나노기술원", response)
        return JsonResponse(response)
    else:
        text = "error"
        response = insert_text(text)
        return JsonResponse(response)


@csrf_exempt
def get_R_DB(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    menus = RDB.objects.all();

    if return_str == "경기 RDB" or return_str == "🍙경기 RDB":
        if is_holiday():
            response = insert_text("공휴일에는 식단을 제공하지 않습니다😊\n 행복한 하루 되세요")
            return JsonResponse(response)
        text = "오늘 경기 RDB 식단\n\n"
        menu = RDB.objects.filter(date=date.today())[0]

        text += menuFormat("[한식]", menu.korea)
        text += menuFormat("[일품]", menu.special)
        text += menuFormat("[점심 플러스바]", menu.lunch_plus)
        text += menuFormat("[석식]", menu.dinner)
        text += menuFormat("[저녁 플러스바]", menu.dinner_plus)
        text += menuFormat("[TaktOut]", menu.takeOut)

        # 실제 보여줄 음식에 대한 메뉴는 위에서 처리했다 이 밑에는 이제 사용자의 클릭을 유도하는 메뉴 생성
        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)

        return JsonResponse(response)

    elif return_str == "월요일경기 RDB":
        text = "월요일 경기 RDB 식단\n\n"

        text += menuFormat("[한식]", menus[0].korea)
        text += menuFormat("[일품]", menus[0].special)
        text += menuFormat("[점심 플러스바]", menus[0].lunch_plus)
        text += menuFormat("[석식]", menus[0].dinner)
        text += menuFormat("[저녁 플러스바]", menus[0].dinner_plus)
        text += menuFormat("[TaktOut]", menus[0].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)

    elif return_str == "화요일경기 RDB":
        text = "화요일 경기 RDB 식단\n\n"

        text += menuFormat("[한식]", menus[1].korea)
        text += menuFormat("[일품]", menus[1].special)
        text += menuFormat("[점심 플러스바]", menus[1].lunch_plus)
        text += menuFormat("[석식]", menus[1].dinner)
        text += menuFormat("[저녁 플러스바]", menus[1].dinner_plus)
        text += menuFormat("[TaktOut]", menus[1].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)

    elif return_str == "수요일경기 RDB":
        text = "수요일 경기 RDB 식단\n\n"

        text += menuFormat("[한식]", menus[2].korea)
        text += menuFormat("[일품]", menus[2].special)
        text += menuFormat("[점심 플러스바]", menus[2].lunch_plus)
        text += menuFormat("[석식]", menus[2].dinner)
        text += menuFormat("[저녁 플러스바]", menus[2].dinner_plus)
        text += menuFormat("[TaktOut]", menus[2].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)


    elif return_str == "목요일경기 RDB":
        text = "목요일 경기 RDB 식단\n\n"

        text += menuFormat("[한식]", menus[3].korea)
        text += menuFormat("[일품]", menus[3].special)
        text += menuFormat("[점심 플러스바]", menus[3].lunch_plus)
        text += menuFormat("[석식]", menus[3].dinner)
        text += menuFormat("[저녁 플러스바]", menus[3].dinner_plus)
        text += menuFormat("[TaktOut]", menus[3].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)

    elif return_str == "금요일경기 RDB":
        text = "금요일 경기 RDB 식단\n\n"

        text += menuFormat("[한식]", menus[4].korea)
        text += menuFormat("[일품]", menus[4].special)
        text += menuFormat("[점심 플러스바]", menus[4].lunch_plus)
        text += menuFormat("[석식]", menus[4].dinner)
        text += menuFormat("[저녁 플러스바]", menus[4].dinner_plus)
        text += menuFormat("[TaktOut]", menus[4].takeOut)

        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)

    elif return_str == "경기 RDB문의사항":
        text = "📪 문의사항 : 조혜성 영양사 [hyeseong92@daum.net] \n" \
               "010-3168-9547 로 연락 바랍니다."
        response = insert_text(text)
        response = makeWeekendReply("경기 RDB", response)
        return JsonResponse(response)


@csrf_exempt
def get_etc(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == "📬건의사항":
        openurl = "https://open.kakao.com/o/si30eZVd"
        response = insert_text(
            "⁉️오류제보 / 기능 건의 ⁉️\n {}\n 링크를 클릭후 \n 편하게 채팅해주세요\n 여러분들의 오류제보가 \n 융밥을 더 성장시킵니다".format(openurl))
        # reply = make_reply("🏡홈으로", "홈")
        # answer = insert_replies(answer, reply)
        return JsonResponse(response)
