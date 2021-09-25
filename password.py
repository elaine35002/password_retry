# 最多輸入三次，如果正確就印出"登入成功"
# 如果不正確，就印出"密碼錯誤!還有_次機會!"

# 我的程式碼
i = 1
while i <= 3:
	a = 3 - i
	psd = input('請輸入密碼: ')
	if psd == 'a123456':
		 print('登入成功')
		 break
	elif a > 0:
	     print('密碼錯誤!還有',a,'次機會')
	i = i + 1

# 解答

#i = 3 
#password = '123456'
#while True:
#	pwd = input('請輸入密碼')
#	if pwd == password:
#		print('登入成功')
#		break
#	else:
#		i = i - 1
#		print('密碼錯誤!還有', i, '次機會')
#		if i == 0:
#			break

