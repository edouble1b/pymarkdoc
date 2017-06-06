"""Documentation for myscript
"""
import example.bass
import math


class myclass(object):
    """This is my class that does things.
    """
    var1 = 0  # Variable 1
    var2 = 1  # Variable 2

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
            sum = number + x  # The sum of number and x
            return sum * math.pi
        except Exception:
