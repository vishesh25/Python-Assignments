str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

flag = False

if len(str1) != len(str2):
    flag = False
else:
    for i in str1:
        if i in str2:
            str2.replace(i,'')
            flag = True
            continue
        else:
            flag = False
            break
    
if flag:
    print("True")
else:
    print("False")