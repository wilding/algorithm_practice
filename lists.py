class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
        pass

    def delete_first(self):
        current = self.head
        if current:
            self.head = current.next
            return current
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)
        self.top = top

    def push(self, new_element):
        current = self.top
        new_element.next = current
        self.top = new_element
        pass

    def pop(self):
        current = self.top
        if current:
            self.top = current.next
            return current
        else:
            return None

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        pass

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

################################################  solution


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        current = self.head
        for i in range(1, position):
            if current:
                current = current.next
            else:
                break
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if self.head:
            for i in range(2, position):
                if current:
                    current = current.next
                else:
                    break
            new_element.next = current.next
            current.next = new_element
        pass


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                else:
                    current = current.next
        pass

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
        pass

    def delete_first(self):
        current = self.head
        if current:
            self.head = current.next
            return current
        else:
            return None


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
#print "Should print 3"
print ll.head.next.next.value
#print "Should also print 3"
print ll.get_position(3).value
print ll.get_position(47)
print ll.get_position(0)

# Test insert
ll.insert(e4,3)
#print "Should print 4 now"
print ll.get_position(3).value

# Test delete
ll.delete(1)
#print "Should print 2 now"
print ll.get_position(1).value
#print "Should print 4 now"
print ll.get_position(2).value
#print "Should print 3 now"
print ll.get_position(3).value