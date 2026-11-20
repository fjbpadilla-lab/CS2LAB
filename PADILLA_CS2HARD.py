#H1
def find(items, target):
    if target in items:
        result = items.index(target) + 1
        return result
    else:
        return -1

club = []
while True:
    member = input("Member ('done' to stop): ")
    if member.lower() != "done":
        club.append(member)
    else:
        break

search = input("Look for?: ")
result = find(club, search)

if result == -1:
    print(search, "is not a member of the club.")
else:
    print(f"{search} is member number {result}.")
    
#H2
titles = []
stock = []
for a in range(3):
    title = input("Title: ")
    titles.append(title)
    copies = int(input("Copies: "))
    stock.append(copies)
    
find = input("Search title: ")
if find in titles:
    index = titles.index(find)
    copies1 = stock[index]
    print(f"{find} has {copies1} copies.")
else:
    print(f"{find} is not in the library.")

#H3
def count(items, target):
    total = 0
    for i in items:
        if target == i:
            total = total + 1
    return total

lista = []
while True:
    votes = input("Vote ('done' to stop): ")
    if votes.lower() != "done":
        lista.append(votes)
    else:
        break

candidate = input("Candidate: ")
result1 = count(lista, candidate)
print(f"{candidate} has {result1} votes.")
