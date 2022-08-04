print('='*50)


arr1 = [1, 2, 3, 4, 5]
arr2 = ['a', 'b', 'c']
arr1.extend(arr2)
print(arr1)

# 出栈
print(arr1.pop())
print(arr1)

arr1.remove('b')
print(arr1)

# 遍历
arr1 = ('a', 'b', 'c', 'd', 'e')
for index in range(len(arr1)):
    print('index:%d,obj:%s' % (index, arr1[index]))
print('='*50)
for i, obj in enumerate(arr1):
    print('index:%d,obj:%s' % (i, obj))

# 生成100以内的偶数列表
testList = [i for i in range(1, 101) if i % 2 == 0]
print(testList)

print('='*50)

# 生成二维数组
testList = [(i, j) for i in range(3) for j in range(3)]
print(testList)

# 生成 2 的 n 次方列表
nums = [2 ** num for num in range(1, 11)]
# 切片
print(nums[-3:])
print(2 in nums)
print(2 not in nums)
for index, obj in enumerate(nums):
    print(f'index: {index} --- num: {obj}')

print(min(nums))
print(max(nums))
print(sum(nums))
