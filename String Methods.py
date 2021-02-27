a = 'hello world!'

# capitalize() = Converts the first character to upper case
print(a.capitalize())

# casefold() = Converts string into lower case
a= a.upper()
print(a)
print(a.casefold())

# center() -- Alligns the text to center place with adding spaces to the front and back for the text
## The number should be more than the len of the txt to see the allignment
print(a.center(20))

# is odd number its only adds to front side and even number then it adds on both sides
## example for below text there will be 6 spaces added before and 5 later
print(a.center(23))


# Count() returns the number of times the value in the string
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


txt = "My name is Ståle"

x = txt.encode()

print(x)

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))