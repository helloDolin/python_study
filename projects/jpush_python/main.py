from conf import app_key, master_secret, apns_production, ios_push_alias, single_alias, android_push_alias
import json
import jpush
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Session
import datetime


_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")


def http_get(url):
    session = Session()
    session.auth = (app_key, master_secret)
    try:
        response = session.get(url, params={})
        data = json.loads(response.text)
        print(data)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def http_delete(url):
    session = Session()
    session.auth = (app_key, master_secret)
    try:
        response = session.delete(url, params={})
        print(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# def https_request(body, url, content_type=None, params=None):
#     https = requests.Session()
#     https.auth = (app_key, master_secret)
#     headers = {}
#     headers['user-agent'] = 'jpush-api-python-client'
#     headers['connection'] = 'keep-alive'
#     headers['content-type'] = 'application/json;charset:utf-8'
#     # print url,body
#     response = https.request('POST', url, data=body,
#                              params=params, headers=headers)
#     # 合并返回
#     return dict(json.loads(response.content), **{'status_code': response.status_code})


def android_send_push_with_alias():
    push = _jpush.create_push()
    alias = android_push_alias
    alias1 = {"alias": alias}
    push.audience = jpush.audience(
        alias1
    )

    android_msg = jpush.android(alert="Dolin test Android -- alert",
                                title="Dolin test Android -- title",
                                extras={
                                    "msg_content": "{\"url\":\"\/merchant/purchase/detail/spec_revision/record\",\"pageType\":2,\"param\":{\"id\":\"2021070119524293912256862632\",\"title\":\"门店禁用提醒\",\"content\":\"您的哈啰电动车杨柳雪镇店因信息修改已禁用，请注意联系运营人员启用\"}}"
                                },)

    push.notification = jpush.notification(
        alert="Hello, JPush!", android=android_msg)
    push.platform = jpush.all_
    print(push.payload)
    push.send()


def ios_send_push_with_alias(msg_contet):
    ''' iOS 通过别名方式发送通知 '''
    push = _jpush.create_push()
    alias = ios_push_alias
    alias1 = {"alias": alias}
    print(alias1)
    push.audience = jpush.audience(
        alias1
    )

    cur_date_str = datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒  第%U周')
    title = f'Dolin title  {cur_date_str}'
    body = f'Dolin body {cur_date_str}'

    ios = jpush.ios(alert={"title": title, "body": body},
                    mutable_content=True,
                    # order_sell
                    sound="order_sell",
                    extras={
        "msg_content": msg_contet
    })

    push.notification = jpush.notification(
        ios=ios)
    push.options = {"apns_production": apns_production}
    push.platform = jpush.all_
    print(push.payload)
    push.send()


def select_all_devices_by_alias(alias):
    ''' 获取指定 alias 下的设备，最多输出 10 个 '''
    url = 'https://device.jpush.cn/v3/aliases/{}'.format(alias)
    http_get(url)


def delete_alias(alias):
    ''' 删除别名 '''
    url = 'https://device.jpush.cn/v3/aliases/{}'.format(alias)
    http_delete(url)


def main():
    dic = {
        "url": "/merchant/add_wechat/home",
        "pageType": 2,
        "param": {
            "oid": "子订单 id",
            "storeId": "归属门店 id"
        }
    }

    msg_content = json.dumps(dic)

    ios_send_push_with_alias(msg_content)

    # android_send_push_with_alias()

    # select_all_devices_by_alias(single_alias)

    # delete_alias(single_alias)


if __name__ == '__main__':
    main()
