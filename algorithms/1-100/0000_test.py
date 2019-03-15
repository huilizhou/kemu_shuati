# dict = {-1: 2, 0: 1, 1: 1, 2: 1, -4: 1}
# neg = list(filter(lambda x: x < 0, dict))
# print(neg)

# pos_dict = [3, 2, 4, 5, 1, 4]

# for i, v in enumerate(pos_dict):
#     print(i, v)

# L = ["flower", "flow", "flight"]
# print(min(L))
# print(max(L))


# str = "aner"
# print(list(str))


# L = ['a', 'b', 'c', 'b', 'a']
# s = "".join(L)
# print(s)

# print(ord("f"))

# for i in ["eat", "tea", "tan", "ate", "nat", "bat"]:
#     s = list(i)
#     print(s)

# i = "acb"
# a = "".join(sorted(i))

# print(a)


# matrix = [[0 for _ in range(4)]for _ in range(4)]
# print(matrix)


# res = 0
# nums2 = "23"
# for i in range(len(nums2) - 1, -1, -1):
#     print(nums2[i], i)

# n = 3
# factor = [0] * n
# # print(factor)
# factor[0] = 1
# for i in range(1, n):
#     factor[i] = factor[i - 1] * i
# print(factor)

# names = ["Cecilia", "Lise", "Marie"]
# letters = [len(n) for n in names]

# # # print(letters)

# longest_name = None
# max_letters = 0

# # for i in range(len(names)):
# #     count = letters[i]
# #     if count > max_letters:
# #         longest_name = names[i]
# #         max_letters = count
# # print(longest_name)

# for i, name in enumerate(names):
#     count = letters[i]
#     if count > max_letters:
#         longest_name = name
#         max_letters = count
# print(longest_name)

# for name, count in zip(names, letters):
#     if count > max_letters:
#         longest_name = name
#         max_letters = count
# print(longest_name)

# names.append("Rosalind")
# for name, count in zip(names, letters):
#     print(name)

# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # c = [4, 5, 6, 7, 8]
# # print(list(zip(a, b)))
# # print(list(zip(a, c)))

# a1, a2 = zip(*[(1, 2), (3, 4), (5, 6)])
# print(list(a1))
# print(list(a2))

# idx = [(2, 3), (3, 4)]
# idx.append((1, 2))

# print(idx.pop())

# j = 1
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# for k in matrix:
#     k[j] = 0
#     print(k)

# print(bin(-4).count("1"))

# class Solution:
#     def maxmultipy(self, nums):
#         nums.sort()
#         return max(max(nums[0] * nums[1] * nums[2], nums[-1] * nums[0] * nums[1]), nums[-1] * nums[-2] * nums[-3])


# print(Solution().maxmultipy([2, 1, 3]))

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __repr__(self):
#         if self is None:
#             return "None"
#         else:
#             return "{} -> {}".format(self.val, repr(self.next))


# class Solution:
#     def printListNodeFromtailtohead(self, head):
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next
#         res = res[::-1]
#         cur = dummy = ListNode(0)
#         for i in res:
#             cur.next = ListNode(i)
#             cur = cur.next
#         return dummy.next


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)

# print(Solution().printListNodeFromtailtohead(head))
