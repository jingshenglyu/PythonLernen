<font face="Arial">

<!-- TOC -->

- [CH1 Introduction](#ch1-introduction)
    - [1.1. Basic Background](#11-basic-background)
        - [1.1.1. C: Compiling Programming language](#111-c-compiling-programming-language)
    - [1.1.2. Python: Interpreted Programming language](#112-python-interpreted-programming-language)
    - [1.1.3. Cpython VS Ipython](#113-cpython-vs-ipython)
    - [1.2. Run](#12-run)
        - [1.2.1. Run Python File](#121-run-python-file)
        - [1.2.2. Coding for Python](#122-coding-for-python)
    - [1.3 Input and Output](#13-input-and-output)
- [CH2 Python Basis](#ch2-python-basis)
    - [2.1. Date Type](#21-date-type)
    - [2.2. Char String and Encoding](#22-char-string-and-encoding)
        - [2.2.1. Why Encoding?](#221-why-encoding)
        - [2.2.2. Encoding](#222-encoding)
        - [2.2.3. String <--> Encoding](#223-string----encoding)
            - [2.2.3.1. ord(): get String](#2231-ord-get-string)
            - [2.2.3.2. chr(): to String](#2232-chr-to-string)
            - [2.2.3.3. encode(): String --> Bytes](#2233-encode-string----bytes)
            - [2.2.3.4. decode(): Bytes --> String](#2234-decode-bytes----string)
    - [2.3. Formatting](#23-formatting)
        - [2.3.1. Placeholder](#231-placeholder)
    - [2.4. Tuple() and List[]](#24-tuple-and-list)
        - [2.4.1 Why Tuple() firstly?](#241-why-tuple-firstly)
    - [2.5. Conditonals and Looping](#25-conditonals-and-looping)
    - [2.6. Dict{} and set()](#26-dict-and-set)
        - [2.6.1. Dict{}: dictionary.](#261-dict-dictionary)
        - [2.6.2. Set()](#262-set)
        - [2.6.3 Difference between dict{} and set()](#263-difference-between-dict-and-set)
    - [Summary for CH2](#summary-for-ch2)
- [CH3 Function](#ch3-function)
    - [3.1. Call a function](#31-call-a-function)
        - [3.1.1. Abstract](#311-abstract)
        - [3.1.2. Built-in function:](#312-built-in-function)
    - [3.2. Define a function](#32-define-a-function)
        - [3.2.1 example:](#321-example)
        - [3.2.2. Placeholder](#322-placeholder)
        - [3.2.3. Return "more values"](#323-return-more-values)
    - [3.3. Arguments of Function](#33-arguments-of-function)
        - [3.3.1. Local Argument](#331-local-argument)
        - [3.3.2. Default Argument](#332-default-argument)
        - [3.3.3. Variable Arguments](#333-variable-arguments)
        - [3.3.4. Keyword Argument](#334-keyword-argument)
        - [3.3.5. Namekeyword Argument](#335-namekeyword-argument)
        - [3.3.6. Arguments Combination](#336-arguments-combination)

<!-- /TOC -->

# CH1 Introduction

## 1.1. Basic Background
### 1.1.1. C: Compiling Programming language
* <font color="grey" size=1 face="Lucida Grande">You <em><b>don't</b></em> send the source code. You can only push the executable file<b>(.exe file)</b>. The others can't use .exe file to operate your source code.</font>
## 1.1.2. Python: Interpreted Programming language
* <font color="grey" size=1 face="Lucida Grande">You <em><b>must</b></em> send the source code.</font>
</font>

## 1.1.3. Cpython VS Ipython
* Cp: interpreter base on C using `>>>`.
* Ip: <b>interactive interpreter</b> base on Cp using `In[n]`.

## 1.2. Run 
### 1.2.1. Run Python File
1.2.1.1. Write down `!/usr/bin/env python3` on your .py file at the first line. For example, save as `hello.py`. 

1.2.1.2. Add Permission for `hello.py`
Input this command on your terminal `$ chmod a+x hello.py`

1.2.1.3. Run this .py File
`$ ./hello.py`

### 1.2.2. Coding for Python
* Don't use WORD from Microsoft for python code. As a tip, please add this coding style for your .py code `# -*- coding: utf-8 -*-`

## 1.3 Input and Output
Code(.py file):
```
yourname = input('pleas enter your name: ')
print('hello,', yourname)
```
Terminal:
```
please enter your name: Tom
hello, Tom
```

# CH2 Python Basis

## 2.1. Date Type
* int / float / bool / string(char string) / None(!= 0)
* variable / constant

## 2.2. Char String and Encoding
### 2.2.1. Why Encoding?
* <font size=0.01 face="Lucida Grande">As countries have their own standards, conflicts will inevitably arise, resulting in.
Unicode was born. All languages are coded into one set of codes, so that no more
There's a garbled problem. However, if
The text you write is basically all in English, Unicode requires twice as much storage as ASCII.
space, which is very uneconomical to store and transmit. In the spirit of economy, the emergence of the UTF-8 code to convert the Unicode into "variable-length encoding".
UTF-8 encodes a Unicode character into 1-6 bytes depending on the size of the number, commonly used
English letters are encoded as 1 byte, Chinese characters are usually 3 bytes, and only very obscure characters are encoded as
4-6 bytes. If the text you are transmitting contains a large number of English characters, you can save space by using UTF-8 encoding.</font>
### 2.2.2. Encoding
* <b>ASCII</b> for English   
* <b>GB2312</b> for Chinese

<table>
<thead>
  <tr>
    <th></th>
    <th>ASCII</th>
    <th>Unicode</th>
    <th>UTF-8</th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>EN</td>
    <td>1 byte</td>
    <td>2 byte</td>
    <td>1 byte</td>
    <td></td>
  </tr>
  <tr>
    <td>CN</td>
    <td>x</td>
    <td>2 byte</td>
    <td>3 byte</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

### 2.2.3. String <--> Encoding

#### 2.2.3.1. ord(): get String
```
>>> ord('中')
20013
>>> ord('A')
65
``` 
#### 2.2.3.2. chr(): to String
```
>>> char(66)
'B'
```

#### 2.2.3.3. encode(): String --> Bytes
```
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```
<font color="grey" size=1 face="Lucida Grande">1. b+'String': date type = bytes
e.g. b'ABC'  
2. \x##: Can't show it using ASCII
</font>

#### 2.2.3.4. decode(): Bytes --> String
```
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

## 2.3. Formatting
### 2.3.1. Placeholder
* %d(int) | %f(float) | %s(string) | %x(hexadecimal int)  
  
  <font color="grey" size=1 face="Lucida Grande">It <b>takes a place</b> in the formatted string(or other date types) and <b>doesn't appear</b> in the final print result.</font>
* Example: output 
```
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```
If you don't know which one do you use, you can always use `%s`.  
If you want to output "%", you can use `%%`
```
>>> print('Age:%s, Gender:%s' %(25,M))
Age:25, Gender:M

>>> print('gowth rate: %d %%' % (60))
gowth rate: 60 %

```

## 2.4. Tuple() and List[]
### 2.4.1 Why Tuple() firstly?
The elements of List[] <b><em>can</em></b> be changed.  
The elements of Tuple() <b><em>can't</em></b> be changed.  

Example of list[]:
```
>>> list = ['Mike', 'Tom', 'Jan']
>>> print(list)
['Mike', 'Tom', 'Jan']
>>> list[2] = 'Jerry'
>>> print(list)
['Mike', 'Tom', 'Jerry']
```
Example of tuple():
```
>>> tuple = ('Mike', 'Tom', 'Jan')
>>> print(tuple)
('Mike', 'Tom', 'Jan')
>>> tuple[2] = 'Jerry'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
* <b>Why</b> tuple()?  
Our source code is <font size=4><b>safer</b></font>, if the data can't be easily changed.

* <b>What</b> changed?
```
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```
* * Why is ['A','B'] changed by ['X','Y']?  
<font color="grey" size=1 face="Lucida Grande">The tuple()'s elements do seem to change, but it's <font size=4><b><em>not the tuple's elements</em></b></font> that change it's  <font size=4><b><em>the list[]'s elements</em></b></font>.
Therefore, the so-called "unchanged" elements of tuple are Say, "Tuple's.
The point of each element is always the same. That is, pointing to 'a', cannot be changed to pointing to 'b', pointing to a list,
You can't change it to point to another object. But the list it points to is itself variable!</font>

## 2.5. Conditonals and Looping
* if/elif/else 
* while | for

## 2.6. Dict{} and set()
### 2.6.1. Dict{}: dictionary.  
* For other programming language this is <b><em>map</em></b>. With <b><em>key-value</em></b> it can store the data.

* dict{}: It can be used to find the value very fastly.  
But it will use the large store-place. 
* <b>Hash</b>: We use this key-value to find the right value quickly. It is called <b>Hash</b>.

### 2.6.2. Set()
* set(): a set of **key** and **no duplikated** key. The defination is the same as the **set** from mathmatic. You can make the **and**, **or** operation.
```
>>> s1 = set([1,2,3])
>>> s2 = set([2,3,4])
>>> s1&s2
{2, 3}
>>> s1|s2
{1, 2, 3, 4}
```

### 2.6.3 Difference between dict{} and set()
Dict{} use **key-value**. Set() has only key **no value**.

## Summary for CH2
* list[]: a simple collection of data, can **use indexes**;

* tuple(): a collection of data that can be used as a whole and **cannot be modified**;

* dict{}: use **keys and values** to find data;

* set(): data **appear only once**, only care whether the data appear, do not care its location;

# CH3 Function
## 3.1. Call a function
### 3.1.1. Abstract 
* The function is a form for **code abstract**.  
### 3.1.2. Built-in function:  
* We can check the [function](https://docs.python.org/3/library/functions.html) of python3 and know how to use the built-in functions.
```
>>> max(2, 3, 1, -5)
3
```
## 3.2. Define a function
### 3.2.1 example:
```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```
* If you want to call this `my_abs`
function. You can save this file as abstest.py. Then you can use `from abstest import my_abs` to call this function in other .py files. We will learn `import` in [Module]().

### 3.2.2. Placeholder  
If now you **don't know** how to write the expression for this function. You can first use `pass` as a **Placeholder**. Without placeholder, you will get **error** when you run your code.

### 3.2.3. Return "more values"
* Run this code to calculate the new location:
```
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    # We define clockwise as moving in a positive direction.

    return nx, ny
```
* Calculate the new location with calling the `move` function:
```
>>> x, y = move(100, 100, 60, math.pi/6)
>>> print(x, y)
151.96152422706632 70.0
```
* Wait! Why does it return **two values** for this example?  
It is fake. Let us print this result.
```
>>> r = move(100, 100, 60, math.pi/6)
>>> print(r)
(151.96152422706632 70.0)
```
* Ah! The result is a **tuple**. It is also a single value for return.

  * Practice: Definete a function`quadratic(a, b, c)` to calculate the **results** of **Quadratic Equation**  
  **Input**: print(quadratic(2, 3, 1))    
  **Output**: (-0.5, -1.0)  
  [Code for QuaFunc](https://github.com/jingshenglyu/Python_Learning/blob/master/LXF_Py/practice/3.2.2.%20quadratic.py)

## 3.3. Arguments of Function
### 3.3.1. Local Argument
```
def power(x):
    return x*x
```
* `x` of `power(x)` is a local argument. This function is used to calculate the power of a number. If we want to know the **n-th power** of a number, we should change the arguments of this function. It should be `power(x, n)`.

### 3.3.2. Default Argument
* If we want to define a function `power(x, n)`, we can firstly think, how to calculate `power(5)`. We don't need to write `power(5, 2)`. Because `power()` means a number multiply self twice. We should here **Default Argument**.   
  
  * Code:
```
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))

25
125
```
* Why should we use default arguments?  
It can make our code **easier**, when we need **only one** argument for calling function.
* Default Argument: It must be pointed to **unchanged element**.

### 3.3.3. Variable Arguments
* We want to define a function to calculate `a^2 + b^2 + c^2 + ...`. We don't know how many arguments should we use. So the code is followed:
```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
`*numbers`: It means the argument is variable.   
Let's test it
```
>>> calc(1, 2)
5
>>> calc()
0
```
* <b>We can add a `*` before a list or tuple. Then it will be variable. </b>

### 3.3.4. Keyword Argument
* We use `**kw` to declare the keyword argument. 
```
def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:', kw)
```
* Why should we use **keyword argument**?
  * If we want to register the information of the students. The **necessary** information is 'name' and 'age'. But the students can also write down some **optional information**. For this **optional information** we can use **keyword argument**.

* Calling this function we can kown that this **keyword argument** is **dict{}**.

```
>>> person('Jack',20)
name: Jack, age: 20, other: {}
extra = {}
```

* We can also so write:
```
extra = {'city': 'Beijing'}
person('Jack', 20, **extra)
Name: Jack, age: 20, other: {'city': 'Beijing'}
```

### 3.3.5. Namekeyword Argument
* If we want to **limit** the keyword argument, we can use **namekeyword argument**.
```
def person(name, age, *, city, job):
    print(name, age, city, job)
```

* The arguments after `*` are **namekeyword argument**. If the user want to input other information to **namekeyword argument**, there is error.

### 3.3.6. Arguments Combination
* The programmer can use '**local argument**','**default argument**', '**variable argument**' / '**namekeyword argument**' and '**keyword argument**'. They must be in this order.
```
def f1(a, b, c=0, *args, **kw):
    print('a=',a, 'b=',b, 'c=',c, 'args=',args, 'kw=',kw)
```
* For every function, you can call it with `func(*arg, **kw)`.


