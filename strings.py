#Changing Case in a String with Methods:
var = "Today is valentine day."
print(var.title(),
	var.upper(),
	var.lower()
	)


first_name = "akshit"
last_name = "thakur"
#concatenation process:
full_name = first_name.title() + "\t" + last_name.title()
f = "akshit" + "\t" + "rajput"
print(full_name,f)


#Adding Whitespace to Strings with Tabs or Newlines:
print("I\n\tlike\n\t\tpython.\n\tThink\n\tPython")


#Exercise:
var1 = "Hello akshit do you want to lear python Today"
print(var1.title(),
	var1.upper(),
	var1.lower()
	)

author = "akshit thakur"
quotes = "A person who never made a mistake never tried anything new."
print(author.title() + " once said," + "\"" + quotes.lower() + "\"")

x = " ak"
y = "ak "
z=" a k "
print(x.rstrip()+y.lstrip()+z.strip())