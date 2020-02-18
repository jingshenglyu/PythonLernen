M = eval(input("请输入数字:"))
OP = input("请输入操作符+，-，*，/：")
N = eval(input("请输入数字:"))

if(OP == '+'):
    C1 = M + N
    print("{:.2f}".format(C1))
elif(OP == '-'):
    C2 = M - N
    print("{:.2f}".format(C2))
elif(OP == '*'):
    C3 = M * N
    print("{:.2f}".format(C3))
elif(OP == '/'):
    C4 = M / N
    print("{:.2f}".format(C4))