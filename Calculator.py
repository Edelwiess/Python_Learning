a = input('input the first number: ')
symbol = input ('input calculate symbol (+，-，*, /,^): ')
b = input ('input the second number: ')
a = float(a)
b = float(b)

print(a)
print(symbol)
print(b)

if symbol == '+':
   result = (a+b)
elif symbol == '-':
   result = a-b
elif symbol =='*':
   result = a*b
elif symbol =='^':
   result = pow(a,b)
elif symbol == '/':
   result = a/b
else: 
	print('Invalid Input')

print(a, symbol, b, '=', result)

quit = input('Press any key to quit')
