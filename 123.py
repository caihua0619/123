aa = input('請問你學號')
print('你的學號是',aa)
bb = input('請問你姓名')
print('你的姓名是',bb)
cc = int (input('請問你年齡'))
dd = 2025
D = dd-cc
print('你的出生年份是',D)
if cc>=18:
    print('您已成年')
    adult_status="已成年"
else:
    print('您未成年')
    adult_status="未成年"
reversed_name = bb[::-1]
print('你的姓名反轉後是:', reversed_name)
print("\n===== 使用者資訊 =====")
print('你的名字',bb)
print('你的姓名',aa)
print('你的出生年份',D)
print('成年判斷',adult_status)