#  to calculate number of microstates.

a = int(input("Enter the no. of particles:\n"))
print("This is the value of ni:\n ni=", (a))

x = int(input("Enter the no. of energy states present:\n"))
print("this is the value of gi:\n gi=", (x))

b = 'particles are distinguishable'
c = 'particles are indistinguishable and there is no restriction over filling'
d = '''particles are indistinguishable and there is restriction over filling
we can only have single particle in every state.'''

A = input("Type of particles?:\n")

def MaxwellMicrostate(a,x):
  MaxwellMicrostate = x**a
  print(MaxwellMicrostate)

def Factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * Factorial(n-1)

if (A=="b"):
  print(b)
  print("We will use maxwell-boltzmann distribution.")
  print("no. of microstates:") 
  MaxwellMicrostate(a,x)

elif (A=="c"):
  print(c)
  print("We will use bose-einstien distribution.")
  print("No. of microstates:")
  print((Factorial(a+x-1))/((Factorial(a))*(Factorial(x-1))))
  
else:
  print(d)
  if(x<a):
    print("This is an invalid case\n we can not use fermi-dirac distibution here.")
  elif(x>=a):
    print("We will use fermi-dirac distribution.")
    print("No. of microstates:")
    print((Factorial(x))/((Factorial(a))*(Factorial(x-a))))


print(" YOU GOT WHAT YOU WANTED;)")
    