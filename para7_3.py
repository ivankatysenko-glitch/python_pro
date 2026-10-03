def raise_to_the_degrss(number, max_dagree):
    i = 0
    for j in range(max_dagree):
        yield number ** i
        i += 1


res = raise_to_the_degrss(1234, 20)
print(res)

for el in res:
    print(el)
    print( )
print("new")
for el in res:
    print(el)
    print( )