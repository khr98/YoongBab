from pytimekr import pytimekr
from datetime import date
import datetime

holiday_list = pytimekr.holidays() #holidays메소드는 리스트 형태로 관련값 반환

def is_holiday():
    result = False;
    weekno = datetime.datetime.today().weekday()
    for holiday in holiday_list:
        if (holiday == date.today() or weekno > 4):
            result = True;
        else:
            pass;
    return(result);
