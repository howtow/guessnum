#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話印出答對了
#猜錯的話印出 比答案大或小

import random

r = random.randint(1,100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了')
		break	
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')


