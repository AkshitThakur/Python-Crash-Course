"""
a="last_element"
variable = ["fetch","read",'write',a]
#Accessing Elements in a List:
print(variable[1].title()+"\t",
	variable[2].upper()+"\t",
	variable[0].lower()+"\t",
	variable[-1].split('_'))

#Using Individual Values from a List:
x = ["honda","bmw","farrari"]
print("My first vehical/car is "+x[0]+" and others are "+x[1]+","+x[-1]+".")

#exercise:
names = ["akshit","adviteeya","ajay","abhay","aman","aman"]
print(
	"My self "+names[0].title()+" & i have some classmate & their names are given bellow: "+names[1]+","+names[2]+","+names[-1]+".")

#Changing, Adding, and Removing Elements:
names.append("Anchal")
names.insert(0,a)
del names[4]
print(names.pop(0))
names.remove("aman")
names.remove("aman")
print(names)


invited_peoples = ["ajay","adviteeya","Anchal"]
c_m = invited_peoples.pop(0)
invited_peoples.insert(0,"aman")
invited_peoples.insert(3,"abhay")
invited_peoples.append("aryan")
x = [invited_peoples.pop(0),invited_peoples.pop(2)]
invited_peoples.sort(reverse=True)
sorted(invited_peoples)
invited_peoples.reverse()
i_p = len(invited_peoples)
print(
	f"Hey {invited_peoples[0].title()} you are here, its been a very long time sence we met.\n",
	"Hello {} good to see follow me its a time of joy.\n".format(invited_peoples[1].title()),
	"%s bro.. you are late where were you everyone is looking for you." % invited_peoples[2].title(),
	f"\n{c_m.title()} cannot make it. so i invited my lovely friends {invited_peoples[-3].title()}, {invited_peoples[-2].title()}, {invited_peoples[-1].title()}",
	"\nThe dinner plan gone very big so i donnot send inviation to two of my friend named %s " % x[0].title(),x[1].title(),
	"The number of people i have to deal with now is %s" % i_p
	)

places = ["mumbai","los_angeles","maimi","france","london"]
print("My list is %s" % sorted(places))

magicians = ["dumble_door","harry_portter","voldemote","sevalice_snake"]
lines = ["run!!! he will kill us",",cast the spell please.",",we love to look the magic.",",its good to see you"]

for magician in range(len(magicians)):
	print(magicians[magician].title() +" "+ lines[magician])
print("magicians facinates me !!!")

for magician in magicians:
	print(magician)

#exercise:
pizza = ["dominose","kfc","mini"]
for p in range(len(pizza)):
	print(pizza[p].title() + " is quite great pizza in all.")
print("I fucking love pizza.I drink pizza,think pizza!!")

animals = ["cat","dog","rat","elephanent","horse"]
dis = ["is smart","is loyal","ohh i hate this one","is quite big, compared to others","is fast,i like its specility"]
an = sorted(animals)
di = sorted(dis)
for a in range(len(animals)):
	print(an[a].title()+" "+di[a] + ".")
print("dog is most loyal in all animals.")


l = list(range(1,7,2))
for i in range(len(l)):
	print(l[i])

n = []
for entery in range(1,4):
	enter = input("enter %s:" % entery)
	n.append(enter)
print(n)

q = []
decide = input("no. of time to iterate: ")
for i in range(int(decide)):
	y = input("Enter %s name: " % i)
	q.append(y)
print(q)


list = [i for i in range(0,9)]
print(list,
	min(list),max(list),sum(list)
	)

list = []
for i in range(0,20,3):
	list.append(i)
	print(i)

print(
	min(list),max(list),sum(list)
	)

list = [i**3 for i in range(0,20)]
for x in list:
	print(x)


#slice:
list = ["ak","aj","adv","am","ar"]
for i in range(len(list)):
	print(list[i:i+8],list[i+2:],list[:i+4])

lis =["akshit",2,"adviteeya","ajay","aman"]
list1 = lis
list2 = lis[:]
lis.append('cannoli')
list1.append('ice cream')
list2.append("x")
print(list2,list1)


l = [i for i in range(0,10)]
print(l[:4],l[3:8],l[6:])

my_pizza = ["dominoze","kfc","big_bite"]
frd_pizza = my_pizza[:]
my_pizza.append("tummy-tummy")
frd_pizza.append("so_good")
for i in range(len(my_pizza)):
	print("my fav pizza is "+my_pizza[i].title())
for i in range(len(frd_pizza)):
	print("my frd fav pizza is "+frd_pizza[i].title())
print(list(my_pizza+frd_pizza))
"""

