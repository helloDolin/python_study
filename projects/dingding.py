import requests
import json
import time
import datetime


def send_normal_msg(text):
    headers = {'Content-Type': 'application/json'}
    webhook = f'https://oapi.dingtalk.com/robot/send?access_token=dbea0b26bf621cad3c34bb6456ddb4d8ec7e91956afe6cfabed46f6096998ad3'
    data = {
        'msgtype': 'text',
        'text': {'content': text},
        'isAtAll': True
    }

    res = requests.post(webhook, data=json.dumps(data), headers=headers)
    print(res)


def send_markdown(msg):
    headers = {'Content-Type': 'application/json'}
    webhook = f'https://oapi.dingtalk.com/robot/send?access_token=dbea0b26bf621cad3c34bb6456ddb4d8ec7e91956afe6cfabed46f6096998ad3'
    date_str = datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒  第%U周')
    content = f'#### {msg} \n\n {date_str} \n '
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": date_str,
            "text": content,
        },
        "at": {
            "isAtAll": True
        }
    }

    res = requests.post(webhook, data=json.dumps(data), headers=headers)
    print(res)


def get_hour():
    if datetime.datetime.now().hour < 12:
        return 11
    return 17


def eat():
    startTime = datetime.datetime(datetime.datetime.now(
    ).year, datetime.datetime.now().month, datetime.datetime.now().day, get_hour(), 35, 0)
    while datetime.datetime.now() < startTime:
        print(datetime.datetime.now())
        time.sleep(1)
    for i in range(0, 3):
        # send_normal_msg(f'EAT,go go go 😄😄😄 \n {i + 1}')
        send_markdown(f'eat,go go go 😄😄😄 - {i + 1}')


def main():
    # send_msg()
    # 延迟 5s 执行
    # timer = threading.Timer(5, func)
    # timer.start()
    eat()


if __name__ == '__main__':
    main()
