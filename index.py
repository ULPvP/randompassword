import random
words="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%^&*()`"
while 1:
  password_long = int(input("你的密碼想要多少個字？"))
  password_count = int(input("你想要刷多少個密碼？"))
  for x in range(0,password_count):
    password = ""
    for x in range(0,password_long):
      password_character = random.choice(words)
      password = password + password_character
    print("你的密碼:", password)
  break
