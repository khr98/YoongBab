# import requests
import datetime
# from bs4 import BeautifulSoup
from datetime import datetime
#
#
# 주말인지 판단해주는 함수
def is_weekend(d):
    return d.weekday() > 4


def print_whichday(year, month, day):
    r = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    aday = datetime.date(year, month, day)
    bday = aday.weekday()
    return r[bday]
#
#
# def get_request_query(url, operation, params, serviceKey):
#     import urllib.parse as urlparse
#     params = urlparse.urlencode(params)
#     request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
#     return request_query
#
# def get_holiday(whenyouliveyear):
#     year = whenyouliveyear
#     mykey = "FsSEbKLvuyBOw8JjAFaUVdG61eh6gVwOgNq7K5HNcEomRYOr2p4w%2BmI0TE4wEbYs0uR50fr4wMmhTE0sNsFq4g%3D%3D"
#     holiday = []
#     for month in range(1, 13):
#         if month < 10:
#             month = '0' + str(month)
#         else:
#             month = str(month)
#         url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
#         operation = 'getRestDeInfo'
#         params = {'solYear': year, 'solMonth': month}
#         request_query = get_request_query(url, operation, params, mykey)
#         get_data = requests.get(request_query)
#         if get_data.ok:
#             soup = BeautifulSoup(get_data.content, 'html.parser')
#             item = soup.findAll('item')
#             # print(item);
#             for i in item:
#                 day = int(i.locdate.string[-2:])
#                 holiday.append(i.locdate.string)
#
#     return holiday
#
#     # 공휴일인지 판단
# def get_vacation():
#
#     today = datetime.today()
#     is_weekend_today = is_weekend(today)
#     temp_today = today.strftime("%Y%m%d")
#     is_holiday_today = False
#     is_vacation_today = False
#     for i in get_holiday(2021):
#         if i == temp_today:
#             is_holiday_today = True
#             break
#     if is_weekend_today or is_holiday_today:
#         is_vacation_today = True
#
#     return is_vacation_today
#
# get_vacation()
####### 2번째 방법 해외 공휴일 사이트 직접 크롤링

import requests, bs4

url = 'https://www.timeanddate.com/holidays/south-korea/'
response = requests.get(url).text.encode('utf-8')
response = bs4.BeautifulSoup(response, 'html.parser')

# 1. 테이블 영역 찾기.
tableData = response.find('table', {'id': 'holidays-table'})
# tableData

# 2. 컬럼 헤더 찾기.
theadTags = tableData.find('thead')

thTags = theadTags.find_all('th')

columnHeaderList = []

thTagsLen = len(thTags)
for i in range(0, thTagsLen):
    elements = thTags[i].text.strip()
    columnHeaderList.append(elements)

columnHeaderList  # 결과 : ['Date', '', 'Name', 'Type']

# 3. body 데이터 찾기.
tbodyTags = tableData.find('tbody')
thTags = tbodyTags.find_all('th')
# thTags[0].text # 디버깅용. (0:30)

tdTags = tbodyTags.find_all('td')
# tdTags[i].text # 디버깅용. (0:30) * 3이라 (0:90)이다.

rowList = []
columnList = []

thTagsLen = len(thTags)



   # 공휴일인지 판단
def get_vacation():

    for i in range(0, thTagsLen):
        rowList.append(thTags[i].text)
        # columnList.append(tdTags[3 * i].text)
        # columnList.append(tdTags[3 * i + 1].text)
        # columnList.append(tdTags[3 * i + 2].text)

        # rowList.append(columnList)
        # columnList = []ro

    today = datetime.today()
    is_weekend_today = is_weekend(today)
    temp_today = today.strftime("%Y%m%d")
    is_holiday_today = False
    is_vacation_today = False
    for i in rowList:
        if i == temp_today:
            is_holiday_today = True
            break
    if is_holiday_today:
        is_vacation_today = True

    return is_vacation_today

