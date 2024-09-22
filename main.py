n = int(input("введите количество школьников"))
k = int(input("введите количество яблок"))
appl = k//n
apples_left = k % n
print("Каждому школьнику достанется:", appl)
print("Яблок останется в корзинке:", apples_left)