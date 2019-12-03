#--- Day 1: The Tyranny of the Rocket Equation ---
f=open('input_one','r')
k=0
for line in f:
    n=(int(line)/3)-2
    k+=int(n)
f.close()
print(k)
