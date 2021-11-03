print('hello world')

gen = (i for i in range(100) if i % 2 == 0)

for x in gen:
    print()

print()

arreglo_num = [1, 2]
arreglo_num.append(4)
print(arreglo_num)

tupla = (1, 2, 3)
print(tupla)

comp = [i for i in range(100) if i % 2 != 0]
comp.append(101)
print(comp)

dic = {'color': 'red', 'size': 123, 'width': 405.5}
if 'color' in dic:
    print(dic['color'])

for key in dic:
    print(key)
    print(dic[key])

    if 'color' in dic:
        print(dic['color'])


def multi(num1, num2):
    return num1*num2





def multiRecurs(v1, v2,i=0 ,acc=0):
    if i < v2:
        return multiRecurs(v1,v2,i+1,v1+acc)
    else:
        return acc
print(multiRecurs(5,3))

def mult2(*args):
    res = 1
    for i in args:
        res*= i
    return res
print(mult2(2,6,4,3))

def multi3(**kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res *= kwargs[key]

    return res

print(multi3(num1=2,num2=6,))

print(multi3(num1=2,num2=6,num3=4,num4=3))
print()
def mult4(*args, **kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res *= kwargs[key]

    for i in args:
        res*=i

    return res       
print(mult4(2,6,num1=4,num2=3))


pares = [i for i in range(50) if i % 2 == 0]
impares = [i for i in range(50) if i % 2 != 0]
res = [i for i in range(100) if i % 2 != 0]

for i in range(51):
    print(pares[i]*impares[i])
   