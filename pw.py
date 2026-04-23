password = 'a123456'
i = 3 #3次機會
while i > 0:
    question = input('請輸入密碼：')
    if question == password:
        print('登入成功')
        break #逃出while
    else:
        i = i - 1
        if i > 0:
            print('密碼錯誤！還有', i,'次機會')
        else:
            print('密碼錯誤！已鎖定')
