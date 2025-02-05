name = "Lisa"
print(name)

def test():
    print(f"At first the name in this function is {name}")
    name = "Jacob"
    print(f"The name in this function is {name}")
    return
test()
print(f"The name at this point is {name}")

