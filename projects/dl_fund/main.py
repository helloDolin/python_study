import imp
from requests import Session
import requests
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from openpyxl import load_workbook
import datetime
from util import http

# 与 接口 parameters 对应（顺序不对应）
TOKENS = [
    'BTC',
    'ETH',
    'BNB'
]


# def http_get(url):
#     ''' http get req '''
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
#     res = requests.get(url, headers=headers, verify=False)
#     res_status = res.status_code
#     if res_status == 200:
#         return res


def get_fear_greed_index():
    url = 'https://api.alternative.me/fng/'
    res = http_get(url)

    resData = json.loads(res.text)
    resData = resData['data'][0]

    name = resData['value_classification']
    value = resData['value']

    print(f'恐惧贪婪指数：{value}\nname：{name}')


def read_net_data():
    ''' 获取 token 价格 '''
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol': ','.join(TOKENS),
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'af108ddb-cc3a-429e-b408-087dc8a71a11',
    }

    session = Session()
    session.headers.update(headers)

    result = []
    try:
        response = session.get(url, params=parameters)
        print('😀😀😀 ============== response.text ============== begin')
        print(response.text)
        print('😀😀😀 ============== response.text ============== end')
        data = json.loads(response.text)

        for obj in TOKENS:
            price = data['data'][obj]['quote']['USD']['price']
            if obj == 'BTC' or obj == 'ETH' or obj == 'BNB':
                print(round(price))
            else:
                print(round(price, 6))
            result.append(price)

        # print(result)
        return result

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def write_2_excel(arr):
    excel_path = '/Users/liaoshaolin/Desktop/dl_fund/DLFunds.xlsx'
    workBook = load_workbook(excel_path)
    workSheet = workBook['mine']

    for index in range(len(arr)):
        workSheet[f'D{index + 2}'] = round(arr[index], 2)
    workBook.save(excel_path)

# TODO：恐惧贪婪指数写入到本地文件，形成图形，btc 999 指数


def main():
    arr = read_net_data()
    # write_2_excel(arr)
    get_fear_greed_index()
    print(datetime.datetime.now().strftime(
        '\n%Y年%m月%d日%H时%M分%S秒  第%U周\nps：商户快比实际多一周'))


if __name__ == '__main__':
    main()
