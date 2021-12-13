#PassWord encrypter
user_name = input("Enter your User name : ")
PassWord = input("Enter your PassWord : ")
lenght_password = len(PassWord)
encrypting_passWord = '*' * lenght_password
print("hey {2}, your password {0} is {1} letters long. " .format(encrypting_passWord, lenght_password, user_name))
