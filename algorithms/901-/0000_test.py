# S = 'abcdjj'
# print(S[2].isalpha())


# basket = {'apple', 'orange', 'apple', 'pear', 'banana', 'orange'}
# print(basket)

# a = set('abracadabra')
# b = set('alacazam')
# # print(a)
# # print(b)
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# thisset = set(("Google", "Runoob", "Taobao"))
# # thisset.add("Facebook")
# thisset.update([1, 2], [1, 4])
# print(thisset)
# # thisset.remove("7")
# thisset.discard("7")
# thisset.clear()
# print(thisset)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# # x.intersection_update(y, z)
# r = x.intersection(y, z)
# print(r, x, y, z)


# for i in range(10, -1, -1):
#     print(i)

# res = [2, 3, 2, 3, 1, 5]
# print(list(set(res)))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def test(self, head):
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().test(head))
