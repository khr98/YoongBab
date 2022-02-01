# 요일을 한글로 넣으면 숫자를 반환해주는 함수입니다
# 월요일 0 부터 시작 일요일은 6

def weekConverter(week):
    realWeek = week[0]

    if realWeek == "월":
        return 0
    elif realWeek == "화":
        return 1
    elif realWeek == "수":
        return 2
    elif realWeek == "목":
        return 3
    elif realWeek == "금":
        return 4
