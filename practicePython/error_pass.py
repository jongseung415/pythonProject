try:
    f = open("나없는파일","r")
except FileNotFoundError as e:
    pass
    #print(f"{e}")
# else:
#     print("keep going")