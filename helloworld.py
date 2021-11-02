print('pares')
for number in range(0,100):
    if number%2 == 0:
        print(number,',',end='')
  
print()
print('impares')
for number in range(1,100,2):
       print(number,',',end='')

print()

print('ascii')
givenString = "ABCDE JESUS */#%$"
var = givenString[0]
for i in range(0,len(givenString)):
    print(ord(givenString[i]),',',end='')


print()

print('primos')
for i in range(2, 100): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i,',',end='')

print()
            