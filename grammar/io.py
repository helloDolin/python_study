'''
https://img-blog.csdnimg.cn/a7838185431a43fd90540ea1e727d397.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pma5a6JQWxpY2U=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center

'''


file_path = '/Users/liaoshaolin/Desktop/python_study/work/merchant.py'
with open(file_path, encoding='utf-8') as file_object:
    contents = file_object.readlines()
for content in contents:
    print(content.rstrip())

file_name = '/Users/liaoshaolin/Desktop/test.txt'
with open(file_name, 'a') as file_object:
    file_object.write('\ntxt create success 3')
