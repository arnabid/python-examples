def add(x=6, y=7, Noop = False):
	if Noop:
		return None
	else:
		return x + y

op1 = lambda: add(y=9)
op2 = lambda: add(2, 6, Noop = True)

print (op1())
print (op2())
