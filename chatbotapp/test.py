from openpyxl import load_workbook

from ..models import RDB


def add_rdb():
    # data_only=True로 해줘야 수식이 아닌 값으로 받아온다.
    load_wb = load_workbook("/Users/hyerim/Yoongbab/excel", data_only=True)
    # 시트 이름으로 불러오기
    load_ws = load_wb['경기알앤디비']

    # 셀 주소로 값 출력
    print(load_ws['D3'].value)
    tempKorea = load_ws['D4'].value + "," + load_ws['D5'].value +"," + load_ws['D6'].value + "," + load_ws['D7'].value + "," + load_ws['D8'].value +  "," + load_ws['D9'].value
    tempSpecial = load_ws['D10'].value + "," + load_ws['D11'].value +"," + load_ws['D12'].value + "," + load_ws['D13'].value + "," + load_ws['D14'].value +  "," + load_ws['D15'].value
    RDB.objects.create(data=load_ws['D3'].value,korea=tempKorea,special=tempSpecial)


add_rdb()