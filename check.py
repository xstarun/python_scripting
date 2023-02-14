import datetime 
now = datetime.datetime.now()

print (now)


while True:
    s = input('Enter something : ')
    if len(s)<3:
      print("Too Small ")   
      continue
    print ('Length of the string is', len(s))
    if s == 'quit':
        break

print ('Done')
