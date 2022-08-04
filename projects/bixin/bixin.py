#-*- coding: utf-8 -*-
import json
from openpyxl import Workbook, load_workbook

''' 常量 '''
global_sheetName = '11.8'
global_monthDay = '1108'
global_workBookName = 'bixin_11'


''' json转为python对象 '''
def json2pythonObj(jsonStr):
	return json.loads(jsonStr)

''' 获取月与日 '''
def getMonthDay(timeStr):
	month = timeStr[5:7]
	day = timeStr[8:10]
	return month + day

''' 通过json文件获取json数据 '''
def getJsonDataByFileName(fileName):
	with open('./{}'.format(fileName)) as f:
		return f.read()

''' 将数据写入excel '''
def writeData2excel():
	jsonData =  getJsonDataByFileName('bixin_data.json')
	pythonObjData = json2pythonObj(jsonData)
	readyWrite2excelData = pythonObjData['data']
	readyWrite2excelData.reverse()

	# 整理当天需要写入excel的数据
	newArr = []
	for obj in readyWrite2excelData:
		created_at = obj['created_at']
		created_at = getMonthDay(created_at)
		if created_at == global_monthDay:
			newArr.append(obj)
	
	readyWrite2excelData = newArr

	# 整理买入、卖出的数据
	buyArr = []   # 商家买入arr
	sellArr = []  # 商家卖出arr

	for obj in readyWrite2excelData:
		side = obj['side']
		if side == 'BUY-IN':
			buyArr.append(obj)
		if side == 'SELL-OUT':
			sellArr.append(obj)

	# 获取workSheet
	workBook = load_workbook('./{}.xlsx'.format(global_workBookName))
	workSheet = workBook[global_sheetName]

	for i,obj in enumerate(sellArr):
		volume = obj['volume']
		price = obj['price']
		workSheet['A{}'.format(i + 10)] = float(volume)
		workSheet['E{}'.format(i + 10)] = float(price)

	for i,obj in enumerate(buyArr):
		volume = obj['volume']
		price = obj['price']
		workSheet['L{}'.format(i + 10)] = float(volume)
		workSheet['J{}'.format(i + 10)] = float(price)

	workBook.save('./{}.xlsx'.format(global_workBookName))

def main():
	writeData2excel()

if __name__ == '__main__':
	main()