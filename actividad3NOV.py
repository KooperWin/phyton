pares = [i for i in range(50) if i % 2 == 0]
impares = [i for i in range(50) if i % 2 != 0]
print(pares)
print(impares)
print()

for i in range(25):
    print(pares[i]*impares[i])