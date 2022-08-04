import requests


def http_get(url):
    ''' http get req '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        res = requests.get(url, headers=headers, verify=False)
        res_status = res.status_code
        if res_status == 200:
            return res
    except requests.RequestException:
        return None
