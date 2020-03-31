
examples_separator = '---------------------'
greeting = "Hello"
words_separator = " "
exclamation_mark = "!"
greetings_count = 9
names = ["Elisabeth", "Joan", "Alex", "David", "John", "Marie", "Michael"]


print(examples_separator)

for i in range(0,5):
    print(greeting + str(i)) #i.__str__()

print(examples_separator)

for name in names:
    print(greeting + " " + name + "!")


# print(examples_separator)
#
# for i in range(0, greetings_count):
#     print(greeting + " " + names[i] + "!")
#

print(examples_separator)

for i in range(0, greetings_count):
    print(greeting + " " + names[i % len(names)] + "!")



