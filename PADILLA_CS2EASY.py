#E1
list0 = []
for i in range(5):
    snack = input("Snack: ")
    list0.append(snack)
print(list0)

#E2
list1 = []
num_names = int(input("how many names?: "))
for i in range(num_names):
    names = input("Names: ")
    list1.append(names)
print(list1)
print(num_names, "names stored.")

#E3
list2 = []
for i in range(5):
    scores = input("Scores: ")
    list2.append(scores)
print(list2)

#E5
list3 = []
for i in range(4):
    fruits = input("Fruit: ")
    list3.append(fruits)
print("First fruit:", list3[0])
print("Last fruit:", list3[3])