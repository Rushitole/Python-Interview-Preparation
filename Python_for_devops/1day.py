# # print("hello world")
# # # env=input("Enter Cloud Enviromnt :")
# # # if env=="AWS" or env=="aws":
# # #     print("you are in aws platform")


# # import time

# # while True:
# #     time.sleep(2)
# #     print("Hello Rushi")



# dict1={
#     "env":"prd",
#     "server":"aws",
#     "ram":1080,
#     "cpu":8,
#     "active":True
# }

# dict2={
#     "env":"prd",
#     "server":"aws",
#     "ram":1080,
#     "cpu":8,
#     "active":False
# }

# New_lst= [dict1,dict2]

# for env in New_lst:
#     for key,value in env.items():
#         if key=="active" and value==True:
#             print()



l=[]
n=int(input("Enter the list which you want []:"))
for i in range(n):
    num=int(input("enter number: "))
    l.append(num)
print(l)
l.sort()
print("2nd largest :" , l[-2] , "and 2nd smallest" ,l[1])