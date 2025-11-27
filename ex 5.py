class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp is None:
            print("List is empty!")
            return

        if temp.data == value:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in the list!")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty!")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked List:")
ll.display()

ll.delete(20)
print("After deleting 20:")
ll.display()
