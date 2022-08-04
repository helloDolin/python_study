from util import io, http
from bs4 import BeautifulSoup


def get_result_list(soup):
    list = soup.find(class_='grid_view').find_all('li')
    for item in list:
        yield {
            'title': item.find(class_='title').string,
            'img_url': item.find('a').find('img').get('src'),
            'index': item.find(class_='').string,
            'score': item.find(class_='rating_num').string,
        }


def download_douban250():
    douban250_url = 'https://movie.douban.com/top250?start='
    res = http.http_get(douban250_url)
    soup = BeautifulSoup(res.text, 'lxml')
    res_list = get_result_list(soup)
    path = '/Users/liaoshaolin/Desktop/resource'
    for i, item in enumerate(res_list):
        img_url = item['img_url']
        img_name = item['title']
        io.download_img(path, img_url, img_name)


def main():
    download_douban250()


if __name__ == '__main__':
    main()
