'''
%.2f 小数点后保留2位，四舍五入，不够补0
%03d 宽度为3位，不够的前面补0，显示格式化时间很好用
'''

# 格式化字符串
name = 'dolin'
age = 18
height = 66.665

formatStr = '姓名：%s,年龄：%03d,体重：%.4f' % (name, age, height)
print(formatStr)

formatStr = '姓名：%(xm)s,年龄：%(nl)03d,体重：%(tz).4f' % (
    {'xm': name, 'nl': age, 'tz': height})
print(formatStr)

formatStr = '{0},{1},{0}'
formatStr = formatStr.format(name, age)
print(formatStr)

dic = {
    'name': 'dolin',
    'age': 18
}
formatStr = '{name},{age}'.format(**dic)
print(formatStr)

point = (10, 20)
formatStr = '{0[0]},{0[1]}'.format(point)
print(formatStr)

# 字符串切片（大致同数组的切片）
formatStr = 'hello world'
index = formatStr.find('world')  # 目前字符串第一个字符的索引位置
print(index)
newStr = formatStr[:6]  # 切 0 - 6 不包括索引为6的字符
print(newStr)

# python3 新特性
msg = 'HELLO "Dolin"'
print(msg.title())

str1 = '123'
str2 = '456'
full_str = f'{str1} 😄 {str2}'
print(full_str)

print(0.1 + 0.2)
print(3 * 0.1)
print(4 / 2)

max_num = 5_000_000
print(max_num)
