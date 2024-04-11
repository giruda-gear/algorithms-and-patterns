from typing import List


class ListNode:

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode(None)  # dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)  # head -> 1
        new_node.next = self.head.next  # head -x- 1
        #       new -o- 1
        self.head.next = new_node  # head -o- new -> 1
        if not new_node.next:  # edge case : List is empty
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)  # 9 -> 10(*tail) -> new
        self.tail = self.tail.next  # 9 -> 10 -> new(*tail)

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while i < index and curr:
            # Move curr to node before target node
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                # 9 -> 10(*tail) -> None
                # curr -> target(curr.next) -> curr.next.next
                # curr(*tail) -> None
                self.tail = curr
            curr.next = curr.next.next
            print(curr.next)
            return True
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
