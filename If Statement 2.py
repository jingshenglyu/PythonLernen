# if else if

# age = input("please enter your age:")
# Programm input your content.
#  Content is string.

# print(type(age))

age = int(input("please enter your age:"))
# Programm input your content.
#  Content is string.

print(type(age))

if age<21:
    print("you can't smoke")

elif age == 21:
    print("now you are 21, you can go to smoke")
elif age == 100:
    print("you are 100 years old,please quit smoking")
else:
    print("you can smoke")