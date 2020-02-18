#Temperatur Convert
TempStr = input("请输入带有符号的温度值： ")   #TempStr: 字符串变量
if TempStr[-1] in ['F', 'f']:  #TempStr[-1]: 字符串TempStr最后一个字符
    C = (eval(TempStr[0:-1]) - 32) / 1.8 
    #eval(TempStr[0:-1])：
    #表示除去TempStr最后一个字符，进行评估运算
    #e.g. eval(82F) --> 变为一个数字类型，参与后续计算
    print("转换后的温度为{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后温度为{:.2f}F".format(F))
else:
    print("格式错误")