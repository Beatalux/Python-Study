numbers=[4,2,93,23,42]
friends =["Kevin","Karen","jim","Oscar","Tim"] #type x matter
print(friends[1])
friends[1]="Mike"
print(friends[1:3]) # print 1,2
friends.append("Rose") #always add at the end
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("jim")
print(friends)
friends.pop()   #remove the last one
print(friends)
print(friends.index("Oscar"))
print(friends.count("Kelly"))
friends.sort()  #ascending
print(friends)
numbers.sort()   
print(numbers)
numbers.reverse()   #reverse the order
print(numbers)
friends.extend(numbers)
print(friends)
friends2=friends.copy()
print(friends2)
friends.clear()
print(friends)
