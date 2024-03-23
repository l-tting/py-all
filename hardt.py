# # n = int(input("Enter no: "))
# # for i in range(0,n+1):
# #     print(i,end='')
# # if __name__ == '__main__':
# #     N = int(input())
# #     list = []
# #     for i in range (1,N):
# #         list.append(i)
# #     print(list)
#         # liss = lis.append(i[1])
#         # print(liss)
#         # lisss.insert(
# if __name__ == '__main__':
#     N = int(input())
#     list = []
#     for i in range (1,N):
#         num = input().split()
#         if num[0]=="insert":
#             list.insert(int(num[1]),int(num[2]))
#         elif num[0]=="print":
#             print(list)
#         elif num[0]== "remove":
#             list.remove(int(num[1]))
#         elif num[0]=="append":
#             list.append(int(num[1]))
#         elif num[0]== "sort":
#             list.sort()
#         elif num[0] == "pop":
#             list.pop()
#         elif num[0]== "reverse":
#             list.reverse()
#     print(list)
nums = sorted([2,3,4,5,11,10,7])
def func(i):
    return i**2
print(map(func,nums))