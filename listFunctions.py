lst = [745, 200, 300]
print(lst)

#append item to the end of the list
lst.append(4)
lst.append(4)
lst.append(4)
print(lst)

#show the number of occurence of a specfic item
print(lst.count(4))

# to get the length of the list
print(len(lst))

lst.pop() #pops out the last eliment from the list
print(lst)
print(len(lst))

total = sum(lst) # calculates the sum of the list items
avg = total / len(lst)
print(avg)