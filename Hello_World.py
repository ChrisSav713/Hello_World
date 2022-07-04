# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Chris"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 42
print("Hello", num)	# with a comma
print("Hello " + str(num))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "steak"
fave_food2 = "eggs"
print("I love to eat {0} and {1}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string
print(f"I love to eat {fave_food1.upper()} and {fave_food2.upper()}!!!")
aString = "The quick brown fox jumped over the lazy dog"
print("Heres a string: " + aString)
print("There are " + str(aString.count(" ")) + " spaces in the string")
print("The string centered:")
print(aString.center(150))

def doesItContain(searchString):
    if(aString.find(searchString) >= 0):
        print("The string contains the word " + searchString + " it occurs at the index " + str(aString.index(searchString)))
    else:
        print("The string does not contain the word " + searchString)

doesItContain("brown")
doesItContain("blue")
doesItContain("quick")