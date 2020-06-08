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
