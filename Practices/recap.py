print("This is my first code on jupiter")


name = input("Whats your name?")
print(f"Welcome, {name}!")


phone = "(123) 456-7890"
print(phone.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))


numberArray = [11,21,31,41,51]
for i in numberArray:
    print (i)


count = 1
while count < 6:
    print (count)
    count+= 1


def add(a,b):
    return a+b

print(f"Addition: {add(5,6)}")


dirty_names = [ "    mUkta akhter        ", "                 siAM     ", "mOOOn         "]
clean_names = []

# for name in dirty_names:
    # clean_names.append(name.strip().lower
    
clean_names = [name.strip().title() for name in dirty_names]

print(clean_names)


