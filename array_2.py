import array

a = array.array('i',[1,2,3,4,5])
b = array.array('i',[6,7,8,9,10])
c = array.array('i')

for i in range(1,6):
    soma = a[i-1]+b[i-1]
    c.append(soma)

print(c)
