a = "Hello, World!"
print(a.upper())

# Lower Case
print(a.lower())

# upper Case
print(a.upper())

# remove white spaces ~ TRIM
print(a.strip())

#remove white spaces at left corner ~ LTRIM
a = ' '+a
print(a)
print(a.lstrip())


#remove white spaces at right corner ~ LTRIM
a = a.lstrip()
a = a+' '
print(a)
print(a.rstrip())

# split function to splie a value on with the identifier

print(a.split(","))


# Example using variable to assign the split value
x,y = a.split(",")

print(x)
print(y.strip())


# Cancatenating the strings

a = 'hello'
b = 'world'

c = a+' '+b

print(c);
