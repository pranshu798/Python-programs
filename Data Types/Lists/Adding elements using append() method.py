#Python Program to demonstrate Addition of elements in a List
#Creating a List
List = []
print("Initial blank List: ")
print(List)

#Addition of Elements in the list
List.append(1)
List.append(2)
List.append(4)
print("\nList after addition of three elements: ")
print(List)

#Adding elements to the List using Iterator
for i in range(1,4):
    List.append(i)
print(("\nList after addition of elements from 1-3: "))
print(List)

#Adding Tuples to the List
List.append((5,6))
print("\nList after addition of a Tuple: ")
print(List)

#Addition of List to a List
List2 = ['Python','Pranshu']
List.append(List2)
print("\nList after addition of a List: ")
print(List)