import os
import requests


def is_has_file(file_path):
    ''' 文件路径是否存在 '''
    return os.path.exists(file_path)


def download_img(path, img_url, img_name):
    ''' 下载图片 '''
    if(is_has_file(path) == False):
        os.mkdir(path)
    with open(f'{path}/{img_name}.jpg', 'wb') as f:
        img = requests.get(img_url).content
        f.write(img)
