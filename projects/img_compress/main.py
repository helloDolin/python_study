import os
import shutil
import tinify
import logging
from logger import logger

# 需要压缩文件路径 （首页相关 icon 资源）
srcRootDirStr = '/Users/dolin999/Desktop/dev/dev_merchant/HLMerchant_iOS/HLMerchant/HLMerchant/Supporting Files/Assets.xcassets/ModuleEntrance'
# 输出路径
destRootDirStr = '/Users/dolin999/Desktop/result'


def get_size(path):
    ''' 获取指定路径下文件大小总和 '''
    result = 0
    # 获取path目录下所有文件
    fileList = os.listdir(path)
    for fileName in fileList:
        # 获取 path 与 filename 组合后的路径
        pathTmp = os.path.join(path, fileName)
        # 是目录，递归
        if os.path.isdir(pathTmp):
            result += get_size(pathTmp)
        # 不是目录，计算文件大小
        else:
            result += os.path.getsize(pathTmp)
    return result


def get_img_count(path):
    ''' 获取指定路径下图片个数 '''
    result = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            fileName, fileSuffix = os.path.splitext(name)
            if fileSuffix == '.png' or fileSuffix == '.jpg':
                result += 1
    return result


def compress():
    ''' 压缩 '''
    fileCount = 0

    tinify.key = 'PnScrjQbfs4LHbVgg1mr4410vlvmdCjY'

    # 创建输出目录
    if(os.path.isdir(destRootDirStr)):
        shutil.rmtree(destRootDirStr)
    os.makedirs(destRootDirStr)

    #  os.walk 文档 https://www.runoob.com/python/os-walk.html
    for root, dirs, files in os.walk(srcRootDirStr):
        for name in files:
            newFromFilePath = os.path.join(root, name)
            newToFilePath = os.path.join(destRootDirStr, name)
            fileName, fileSuffix = os.path.splitext(name)
            if fileSuffix == '.png':
                logger.info('png 格式图片名为：%s' % fileName)
                logger.info('newFromFilePath : %s' % newFromFilePath)
                logger.info('newToFilePath : %s' % newToFilePath)
                fileCount += 1
                # 压缩
                source = tinify.from_file(newFromFilePath)
                source.to_file(newToFilePath)

            if fileSuffix == '.jpg':
                logger.info('😀 jpg格式图片名为：%s' % fileName)

    logger.info('图片个数为：%s' % fileCount)
    logger.info('压缩图片个数：%s' % tinify.compression_count)


def main():
    logger.info('😀 😀 😀 === begin === 😀 😀 😀')

    print('目标路径下文件大小: %s 字节' % get_size(srcRootDirStr))
    print('目标路径下图片个数: %s 张' % get_img_count(srcRootDirStr))

    compress()

    logger.info('😀 😀 😀 === end === 😀 😀 😀')


if __name__ == '__main__':
    main()
