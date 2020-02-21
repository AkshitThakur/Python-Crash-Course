"""
dimensions = (200,20)
#dimensions[1] = 30#error:TypeError: 'tuple' object does not support item assignment.
for d in dimensions:
	print(d)
#overwrite tuple:
dimensions=(400,30)
for d in range(len(dimensions)):
	print(dimensions[d])

#exe:
food = ("dal_makhni","chaumin","momo's","maggie","matar_panir")
f = ()
for foo in range(len(food)):
	f.append(food[foo])
print(f[foo])
#tuple do not support append pop & other fxn.
"""
food = ("dal_makhni","chaumin","momo's","maggie","matar_panir")
food = ("dal_makhni","maggie","matar_panir")
for f in food:
	print(food[f])