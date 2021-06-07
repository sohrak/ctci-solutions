import unittest


class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    @classmethod
    def create_list(cls, data):
        head = None
        tail = None
        for d in data:
            node = cls(data=d)
            if tail:
                tail.next = node
                tail = node
            else:
                head = node
                tail = node
        return head


def remove_duplicates(head: ListNode):
    seen = set()
    dummy_head = ListNode(next=head)
    current = dummy_head
    while current and current.next:
        if current.next.data in seen:
            # remove
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return dummy_head.next


class Test(unittest.TestCase):
    def test_no_duplicates(self):
        data = [1, 2, 3, 66, -1, 98]
        head = remove_duplicates(ListNode.create_list(data))
        i = 0
        while head:
            self.assertLess(i, len(data))
            self.assertEqual(head.data, data[i])
            head = head.next
            i += 1

    def test_duplicates_removed(self):
        data = [1, 1, 2, 3, 4, 5, 3, 2, -1, 9, -1, 1]
        expected = [1, 2, 3, 4, 5, -1, 9]
        head = remove_duplicates(ListNode.create_list(data))
        i = 0
        while head:
            self.assertLess(i, len(expected))
            self.assertEqual(head.data, expected[i])
            head = head.next
            i += 1

    def test_empty_list(self):
        data = []
        head = remove_duplicates(ListNode.create_list(data))
        self.assertIsNone(head)


if __name__ == '__main__':
    unittest.main()
