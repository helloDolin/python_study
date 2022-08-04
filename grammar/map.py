import json


test_map = {
    'a': 1,
    'b': 2,
    'c': 3
}
for item in test_map.items():
    print(item)

for key, value in test_map.items():
    print(f'{key}:{value}')

print(test_map.get('a'))
print(test_map.get('aa', 100))

print(test_map.items())  # key与value封装到元组里了
print(test_map.keys())
print(test_map.values())

str = json.dumps(test_map, indent=4)  # 字典转json串
print(type(str))
print(str)

pythonObj = json.loads(str)  # json串转字典
print(type(pythonObj))
print(pythonObj)
