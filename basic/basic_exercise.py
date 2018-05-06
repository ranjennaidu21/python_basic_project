#calculate simple interest exercise using principal , interest rate , number of years

p = input('Enter principal\n')
n = input('Enter number of years\n')
r = input('Enter the interest rate\n')

#above when use input it will automatically store as string value
#so we need to cast to integer to perform the calculation
#you can do converstion of string to int as below
p = int(p)
n = int(n)
r = int(r)

si = (p*n*r)/100
print('The simple interest rate is: ')
print(si)

#test comment added