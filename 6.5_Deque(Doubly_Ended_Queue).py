import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque:", de)

# using append() to insert 4 at the end of deque
de.append(4)
print("After append(4):", de)

# using appendleft() to insert 6 at the beginning of deque
de.appendleft(6)
print("After appendleft(6):", de)

# using pop() to delete 4 from the right end of deque
de.pop()
print("After pop():", de)

# using popleft() to delete 6 from the left end of deque
de.popleft()
print("After popleft():", de)

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)
print("After insert(4, 3):", de)

# using count() to count the occurrences of 3
print("Count of 3:", de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)
print("After remove(3):", de)

# Printing current size of deque
print("Size of deque:", len(de))

# using pop() to delete 6 from the right end of deque
de.pop()
print("After pop():", de)

# Printing current size of deque
print("Size of deque:", len(de))

# Accessing the front element of the deque
print("Front element:", de[0])

# Accessing the back element of the deque
print("Back element:", de[-1])

# using extend() to add 4, 5, 6 to the right end
de.extend([4, 5, 6])
print("After extend([4, 5, 6]):", de)

# using extendleft() to add 7, 8, 9 to the left end
de.extendleft([7, 8, 9])
print("After extendleft([7, 8, 9]):", de)

# using rotate() to rotate the deque by 3 to the left
de.rotate(-3)
print("After rotate(-3):", de)

# using reverse() to reverse the deque
de.reverse()
print("After reverse():", de)
