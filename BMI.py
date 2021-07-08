# BMI 計算公式
hight = input('請輸入你的身高(公尺):')
hight = float(hight)
weight = input('請輸入你的體重(公斤):')
weight = float(weight)
bmi = weight/(hight*hight)
if bmi < 18.5 :
	print('你的體重過輕!')
elif bmi >= 18.5 and bmi < 24:
	print('你的體重正常喔!')
elif bmi >= 24 and bmi < 27:
	print('你過重了!') 
elif bmi >= 27 and bmi < 30:
	print('你是輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你是重度肥胖!')
else:
	print('你是重度肥胖!該減肥了!')
