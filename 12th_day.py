names = "Samir,Krishna"
print(len(names)) #prints out the total length of the string
print(names[0:5]) #Prints out the letter from 0 index to n-1 index
fruit = "Mango"
MangoLen = len(fruit)

#-- M-0, A-1, N-2, G-3. O-4


print("mango is a", MangoLen, "letter word")
print(fruit[1:4])
print(fruit[:]) #python is smart enough to auto consider the len of fruit(variable)

print(fruit[0:len(fruit)-3]) #it returns the negetive indexing
print(fruit[0:-3])

print(fruit[-1:len(fruit)-3]) #this wont make sense (5-1) = 4 and (5-3) = 2
print(fruit[-3:-1]) #this will print 'ng'


#quiz
nm = 'Harry'
print(nm[-4:-2]) 

name = 'ShreeKrishna'
for i in name: 
    print(i) #prints out the every single character 