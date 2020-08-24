
"""
# Question 1

It is important to learn how to read and search through the Python documentation. 
The answers to all of the questions in this quiz can be found within the official Python 3 documentation.

What module provides support for arithmetic on rational numbers?

Just give the name of the module (such as random) with no spaces.

answer: fractions 
https://docs.python.org/3/library/fractions.html
"""

"""
# Question 2

What function could you use to create a complete copy of a nested dictionary (a dictionary that has dictionaries as values)?

If you think the answer is a builtin function just give the function name (such as int) with no spaces, parentheses, or arguments.

If you think the answer is a function contained within a module, give the answer in the form module.function with no other spaces, parentheses, or arguments.

answer:  copy.deepcopy
https://docs.python.org/3.6/library/copy.html#module-copy
"""

"""
# Question 3

What function would you use to open a web page in a new browser window from a Python program?

If you think the answer is a builtin function just give the function name (such as int) with no spaces, parentheses, or arguments.

If you think the answer is a function contained within a module, give the answer in the form module.function with no other spaces, parentheses, or arguments.

(If there are multiple functions that you could use, give only one.)

answer: webbrowser.open
https://docs.python.org/3.6/library/webbrowser.html#module-webbrowser

"""

"""
# Question 4

What Python module allows you to read and write WAV audio files?

Just give the name of the module (such as random) with no spaces.

answer: wave
https://docs.python.org/3.6/library/wave.html?highlight=wav

"""

"""
# Question 5

What is the pickle module?

https://docs.python.org/3.6/library/pickle.html#module-pickle

"Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
and “unpickling” is the inverse operation, whereby a byte stream 
(from a binary file or bytes-like object) is converted back into an object hierarchy. 

answer: A module that allows you to convert Python objects into a byte stream and back...

"""

"""
# Question 6  DID NOT LIST ALL CORRECT ANSWERS

What python data types are immutable?

https://docs.python.org/3.6/reference/expressions.html#index-7

https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a
some of the immutable data types are:
 int, float, decimal, bool, string, tuple, and range.

Answers:
    float
    string
    tuple
    frozenset
    bytes
    
Wrong answers:
    dict
    set
    bytearray
    list
"""

"""
# Question 7  WRONG???

How do you open a file over the network at a specified URL?

Just give the name of the function (including any module name(s) with periods) 
with no spaces, parentheses, or arguments.

from urllib import request
CORRECT answer?: urllib.request.urlopen 
"""
import urllib
from urllib import request
url =  'https://storage.googleapis.com/codeskulptor-isp/course4/isp_gdp.csv'
 
 
with request.urlopen(url) as response:
    output = response.read(100)
print(output)

''' Output:
b'Country Name,Country Code,Indicator Name,Indicator Code,1960,1961,1962,1963,1964,1965,1966,1967,1968'
'''


























