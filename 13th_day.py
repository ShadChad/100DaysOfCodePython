# Strings Are Immutable
a = "Samir"  
print(len(a))  #prints out the length
print(a.upper()) #Prints all the strings in uppercase
print(a.lower()) #Prints all the strings in lowercase
#strings are immutable in python none of this method will change the string intial value,
#rather python will create a new string by given method



b = "!!!!!!Samir ,Samir !!!!!"
print(b.rstrip("!")) #It'll strip the trailing characters and ignores the leading characters
print(b.replace("Samir","Hari")) #It'll replace all the occurance of "Samir" to "Hari"
print(b.split(" ")) #It'll split the strings on every occurance of space and will create a list of every splited string


blogHeading = "introduction TO Js"
print(blogHeading.capitalize()) #returns only the first character as capitalize and all the other characters as lower
print(len(blogHeading))
print(blogHeading.center(60)) #it brings the string in the center
print(b.count("Samir")) #returns the number of time "Samir" is found i=on string :"b" 



c = "Welcome to the Console"
print(c.endswith("ole")) #returns true if the string endswith "ole" as it does
print(c.endswith('to', 4,10)) #returns true because "to" ends between 4,10 indexing


d = "He's name is john. He is an honest man"
print(d.find("is")) #returns the index of first occuring of the provided value inside findmethod
print(d.find("hie")) #returns -1 if it doesnt find anything

print(d.index("is")) #same as find method, returns the index
#print(d.index("ishhhh")) ------------#throws an exception while find method doesnt


e = "WelcomeToTheConsole9"
print(e.isalnum()) #returns true, al is A-Z, a-z , 0-9
print(e.isalpha()) #returns false as the string contain num, only returns true when the string contains only aplha
print(e.islower()) #returns true when all the characters of the string is lower,else false
print(e.isupper()) #same as lower method only returns true when all the characters are upper
print(e.isprintable()) #returns true if all the characters of the string is printable

f = "welcome to the console.\nThank you"
print(f)
print(f.isprintable()) #returns false because \n isnt printable , all the characters that is in the string should be printable or else it'll throw false

g = "      "
print(g.isspace()) #returns true if the string only contain a space or even a tab

h = "World Health Organization"
print(h.istitle()) #This only returns true if first lette of every word is capital or else false

i = "To Kill a moCking bird"
print(i.istitle()) #returns false

print(i.startswith("To")) #returns true if the strings starts with the given value
print(i.startswith("t")) #returns false

print(i.swapcase()) #it swaps every character to its opposite case, lower to upper and vice-versa

print(i.title()) #returns every first letter to uppercase and all other remaining to lower


















