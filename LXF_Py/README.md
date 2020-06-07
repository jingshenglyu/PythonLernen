<font face="Arial">

- [CH1 Introduction](#ch1-introduction)     
  - [1.1. Basic Background](#11-basic-background)         
    - [1.1.1. C: Compiling Programming language](#111-c-compiling-programming-language)     
    - [1.1.2. Python: Interpreted Programming language](#112-python-interpreted-programming-language)     
    - [1.1.3. Cpython VS Ipython](#113-cpython-vs-ipython)     
  - [1.2 Run](#12-run)         
    - [1.2.1. Run Python File](#121-run-python-file)         
    - [1.2.2 Coding for Python](#122-coding-for-python)     
  - [1.3 Input and Output](#13-input-and-output) 
- [CH2 Python Basis](#ch2-python-basis)     
  - [2.1 Date Type](#21-date-type)     
  - [2.2 Char String and Encoding](#22-char-string-and-encoding)         
    - [2.2.1 Why Encoding?](#221-why-encoding)         
    - [2.2.2 Encoding](#222-encoding)         
    - [2.2.3. String <--> Encoding](#223-string----encoding)             
      - [2.2.3.1. ord(): get String](#2231-ord-get-string)             
      - [2.2.3.2. chr(): to String](#2232-chr-to-string)             
      - [2.2.3.3. encode(): String --> Bytes](#2233-string----bytes)             
      - [2.2.3.4. decode(): Bytes --> String](#2234-decode-bytes----string)   


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

## 1.2 Run 
### 1.2.1. Run Python File
1.2.1.1. Write down `!/usr/bin/env python3` on your .py file at the first line. For example, save as `hello.py`. 

1.2.1.2. Add Permission for `hello.py`
Input this command on your terminal `$ chmod a+x hello.py`

1.2.1.3. Run this .py File
`$ ./hello.py`

### 1.2.2 Coding for Python
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

## 2.1 Date Type
* int / float / bool / string(char string) / None(!= 0)
* variable / constant

## 2.2 Char String and Encoding
### 2.2.1 Why Encoding?
* <font size=0.01 face="Lucida Grande">As countries have their own standards, conflicts will inevitably arise, resulting in.
Unicode was born. All languages are coded into one set of codes, so that no more
There's a garbled problem. However, if
The text you write is basically all in English, Unicode requires twice as much storage as ASCII.
space, which is very uneconomical to store and transmit. In the spirit of economy, the emergence of the UTF-8 code to convert the Unicode into "variable-length encoding".
UTF-8 encodes a Unicode character into 1-6 bytes depending on the size of the number, commonly used
English letters are encoded as 1 byte, Chinese characters are usually 3 bytes, and only very obscure characters are encoded as
4-6 bytes. If the text you are transmitting contains a large number of English characters, you can save space by using UTF-8 encoding.</font>
### 2.2.2 Encoding
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
