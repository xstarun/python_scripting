#./...
actual_number = 99
y= "hello"
z = 3.45
running = True

while running :
  guess = int(input ("guessed number is "))
  if guess == actual_number: 
   print("you guesed right")
   running = False
  elif  guess > actual_number:
   print("guess something lower than than")

  else :
   print ("Guess something Higher Number than that")
else:  	
     print("while loop is over ")


 	



"""
if z == 3.45 or y == "hello":
	x= x+1
	y = y +"  " +"world"

print (x)
print (y)
for n in [1,2,3,4,5]:
     print (n**2)
"""
"""
for n in range(2, 10):
    for x in range(2, n): 
      if n % x == 0:
      print (n) "equals", x, "*", n/x 
      break 
  else: # loop fell through without finding a factor 
  	  print (n), ’is a prime number’
  	  """
    