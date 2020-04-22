# 國家/開車對應年齡程式
country = int(input('請輸入你的國家：'))
age = input('請輸入年齡：')

if country == '台灣':
	if age >= 18:
		print('你可以考駕照摟!')
	else:
		print('你還未成年喔!')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照摟!')
	else:
		print('你還未成年喔!')
else:
	print('請輸入 台灣/美國')