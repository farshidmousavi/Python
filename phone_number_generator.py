#Fast way to generator smal phone or x number list with range and aria code
#Simple to use
airiaCode = 216 #Aria code

phoneRange = '0000000000' #10 digit == 10 zero (0) 
def phones(num,range):
    return int((str(num)+range)[:-(len(str(num)))])

file = open(airiaCode.__str__()+".txt",'w+')
for i in range(phones(airiaCode,phoneRange),phones(airiaCode+1,phoneRange)):
    file.write(i.__str__()+'\n')
file.close()
