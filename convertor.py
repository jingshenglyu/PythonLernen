# huansuanqi

# def converter(argument)

def converter(weight):
    ponds = weight/0.45
    print(ponds)

converter(60)

converter(100)

converter(200)

def converter2(weight=100):
    ponds = weight / 0.45
    print(ponds)
# default is 100 ponds.

converter2()
# fixed value