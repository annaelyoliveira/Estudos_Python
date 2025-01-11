primos = []
for i in range (10,51):
    primo = True
    for c in range (2, i):
        if i % c == 0:
            primo = False
            break
    if primo: 
        primos.append(i)
print(primos)

for x in range (2, 3):
    print(x)
