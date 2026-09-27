def raise_to_the_degrses(number):
    i = 0
    while True:
        result = number ** i
        yield number ** i
        if result > 200 ** 20:
            return
        i += 1


res = raise_to_the_degrses(1234)
print(res)
for el in res:
    print(el)
    print()
#23427578159707888905981888711157141234541953024
#10485760000000000000000000000000000000000000000

