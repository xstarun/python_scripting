"""
import datetime
now = datetime.datetime.now()
doc = open("hello.txt","a")
#print (open_file())
doc.writelines ("Writing from the Script side as  on "+ str(now) +"\n")
iterations = sum(1 for line in open("hello.txt"))
print ("script has run for " +str(iterations+1) + " times ")
find = input("Enter search content for the file  ")
print("you searched for  "+ find )
searchresult =[]
with open("hello.txt") as doc:
  for line in doc:  
   for part in line.split():
     if find in part :
     	searchresult.append(find)
     	 #print searchresult()
  if len(searchresult) != 0:
     print ("file contains"+ str(find))
  else:
     print ("file doesn't have word  " + str(find))
     	
        
 #doc.save()
doc.close()
 
 """

 ####################################################################
days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days = days_in_month
def leap_year(year):
  return year%4 ==0

def days_of_month(year,month):
  if month not in range (1,13):
    return ("Invalid Month")
  elif leap_year(year) and month ==2:
     return ("year is leap year and it has 29 days in february")
  elif leap_year(year) and month !=2:
     days = days_in_month[month]
     return("year is leap year and it has "  +str(days)+ " days  in month of "+ str(month))
      
  else:
    days = days_in_month[month]
    return ("year is  Not leap year and it has "  +str(days)+ " days  in month of "+ str(month))     
  #else:
   #return ("year is  Not leap year and it has" +  +" days in month") 
 
print(days_of_month(8000,2))
