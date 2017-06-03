# Python Markdoc Documentation
This tool will create markdown documentation automatically.

It will use google docstrings and will also refrence scripts that you have imported automatically. 

### How To Use
This is very simple to use and all you need to do is to run `pymarkdoc` where your **pymarkdoc.yml** is.

`& pymarkdoc myscript.py`

However every script you want to be documented has to have a docstring at the very begining of the file.

### Example

This is an example on what the code below will look like when converted to markdown.


```python
"""Documentation for myscript
"""
import example.bass
import math

class myclass(object):
    """This is my class that does things.
    """
    var1 = 0 # Variable 1
    var2 = 1 # Variable 2

    def myfunction(self, number: int, x: int=1) -> float:
        """ This function adds x to the number then multiplies it by pi.
        
        Args:
            number (int): The number you want to add
            x (int, optional): The amount you want to add. Defaults to None.

        Returns:
            int: The result of the added number

        Examples:
            This is an example of how to add numbers using the function.

            >>> myfunction(number=10, x=2)
            37.6991118...
        """
        try:
            sum = number + x # The sum of number and x 
            return sum * math.pi
        except Exception:

```

This is the directory tree.
    
    root
    |---example
    |   |---bass.py
    |---myscript.py
    |---pymarkdoc.yml

This will then output the md file below.

# Myscript

###### Documentation for myscript

### Modules

* [bass](link)
* [math](https://docs.python.org/3.6/library/math.html)

### Classes

##### myclass
    
This is my class that does things.

**Attributes**
+ var1: Variable 1
+ var2: Variable 2

### Functions

##### myfunction
```python
myfunction(number, x=1)
```

**Arguments**
+ `number` __int__: The number you want to add
+ `x` __int__: The amount you want to add. Defaults to None.

**Returns**
+ __int__: The result of the added number

**Examples**
```python
#This is an example of how to add numbers using the function

>>> myfunction(number=10, x=2)
#37.6991118...
```

### Todo:

+ The Core!
