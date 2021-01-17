class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def to_set(self):
        if self is None:
            return None
        current_node = self.head
        convertedSet = set()
        while current_node:
            convertedSet.add(current_node.value)
            current_node = current_node.next
        return convertedSet

def union(llist_1, llist_2):
    if llist_1 is None and llist_2 is None:
        return None 
    unionSet = llist_1.to_set().union(llist_2.to_set())
    llist = LinkedList()
    for value in unionSet:
        llist.append(value)
    return llist  

def intersection(llist_1, llist_2):
    if llist_1 is None or llist_2 is None:
        return None 
    instersection_set = llist_1.to_set().intersection(llist_2.to_set())
    print(f"hiiiiii {llist_1}")
    llist = LinkedList()
    for value in instersection_set:
        llist.append(value)
    return llist
       

# # Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21,8]
element_2 = [6,32,4,9,6,1,11,21,1,8]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# # Test case 3

linked_list_4 = LinkedList()
linked_list_5 = LinkedList()

element_1 = [None]
element_2 = [6,32,4,9,6,1,11,21,1,8]

for i in element_1:
    linked_list_4.append(i)

for i in element_2:
    linked_list_5.append(i)

print(f"Empty one list, Union is: {union(linked_list_4,linked_list_5)}")

print (f"Empty one list, Intersection is: {intersection(linked_list_4,linked_list_5)}")