a = "1"
b = "2"
print(a+b) #--this operation will add the string and print 12
#string are alawys enclosed with quotes

#-----Explicit Typecasting-----
print(int(a)+int(b)) #the data type has been changed to integer,
#hence will be printing 3.

#print(a+int(b)) #--will give an error, it needs to be same datatype
#of both variables to perform the operation

#------Implicit Typecasting-----
c = 1.9 #float
d = 8 #int
print(c+d) #---This is called implicit typec conversion, python converts 
#-small data types to highe data types to prevent data loss


