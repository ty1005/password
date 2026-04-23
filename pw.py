password = 'a123456'
i = 3 #3次機會
while True:
    question = input('請輸入密碼：')
    if question == password:
        print('登入成功')
        break #逃出while
    else:
    	i = i - 1
    print('密碼錯誤！還有', i,'次機會')
    if i == 0:
	    break