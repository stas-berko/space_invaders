
examples_separator = '---------------------'
greeting = "Hello"
words_separator = " "
exclamation_mark = "!"
greetings_count = 9
names = ["Elisabeth", "Joan", "Alex", "David", "John", "Marie", "Michael"]


print(examples_separator) ####################################################################################

for i in range(0,5):
    print(greeting + str(i)) #i.__str__()


print(examples_separator) ####################################################################################

for name in names:
    print(greeting + words_separator + name + exclamation_mark)


# print(examples_separator) ####################################################################################
#
# for i in range(0, greetings_count):
#     print(greeting + " " + names[i] + exclamation_mark)
#

print(examples_separator) ####################################################################################

for i in range(0, greetings_count):
    print(greeting + " " + names[i % len(names)] + exclamation_mark)


print(examples_separator) ####################################################################################

for i in range(len(names)):
    print(greeting + words_separator + names[i] + exclamation_mark + words_separator + "Your number is" + words_separator + str(i+1))


print(examples_separator) ####################################################################################

for (i, name) in zip(range(len(names)), names):
    print(greeting + words_separator + name + exclamation_mark + words_separator + "Your number is" + words_separator + str(i+1))

