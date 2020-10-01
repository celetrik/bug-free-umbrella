print ("what kind of snack do you like?")
print("1. cookies")
print("2. pastries")
print("3. none")
preference = input()

if preference == "1":
    print("what flavor of cookies do you like?")
    print("1. Chocolate")
    print("2. Gingerbread")
    print("3. vanilla")
    flavor = input()

    if flavor == "1" or "3":
        print("nice")
    else:
        print("weird, but ok")
elif preference == "2":
    print("what type of pastry do you like?")
    print("1. doughnuts")
    print("2. spring rolls")
    print("3. meat pies")
    pastry = input()

    if pastry == "1" or "3":
        print("You are really basic")
    else:
        print("You are adventurous")
else:
    print("You are a cultist")


