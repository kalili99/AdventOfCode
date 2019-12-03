#--- Part Two ---
f= open('input_one_P2','r')
k=0
for line in f:
    n=(int(line)/3)-2
    while (n>0):
          k+=int(n)
          n=int(n/3)-2
f.close()
print(k)
