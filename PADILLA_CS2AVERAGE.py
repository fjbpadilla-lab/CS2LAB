#A1
list1 = []
for a in range(4):
    items = input("Item: ")
    list1.append(items)
print("1: ", list1[0])
print("2: ", list1[1])
print("3: ", list1[2]) 
print("4: ", list1[3])

#A2
list2 = []
for b in range(5):
    scores = int(input("Score: "))
    list2.append(scores)

index = 0
amount = 0
for items in range(len(list2)):
    amount = amount + list2[index]
    index = index + 1

    
print("Total: ", amount)
print("Average: ", amount / len(list2))

#A3
list3 = []
for c in range(5):
    scores1 = int(input("Score: "))
    list3.append(scores1)
  
count = 0
for items1 in list3:
    if items1 >= 75:
        count = count + 1
print(count, "out of", len(list3), "passed.")

#A4
list4 = []
for d in range(5):
    scores2 = int(input("Score: "))
    list4.append(scores2)

highest = list4[0]

for items2 in range(1, len(list4)):
    if items2 > list4[0]:
        highest = highest

print("Highest:", highest)

#A5
list5 = []
for e in range(5):
    names = input("Name: ")
    list5.append(names)

find = input("Look for?: ") 

response = 0
for names in list5:
    if find == names:
        response = response + 1
    else:
        response = response
    
if response == 0:
    print(find, "is not in the list.")
if response == 1:
    print(find, "is in the list.") 
    