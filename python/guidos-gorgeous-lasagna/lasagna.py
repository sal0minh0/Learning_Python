"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
"""Constant that assigns the value globally to the program"""

EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: 30):
    """Calculate the time remaining.
    - parameter: elapsed_bake_time, type int = time already elapsed.
    - we are returning: type int => remaining time derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes (EXPECTED_BAKE_TIME) the lasagna has been in the oven as
    an argument and returns how much time still needs to bake."""

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based in the number of layers of the lasagna

    - parameter: number_of_layers, type int = the layers of the lasagna;
    - we returning: type int => preparation time.

    The function get one integer that represent the number of lasagna layers 
    and gives the preparation time cooking."""
    
    return number_of_layers * 2

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total cooking time by the number of layers of the food

    - parameter: number_of_layers, type int = the layers of the lasagna;
    - parameter: elapsed_bake_time, type int = cooking time;
    - we returning: type int => total time.

    This function takes two integers that represents the number of lasagna layers and the
    time spent baking and calculates the total spent in cooking."""
                                                                                 
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time  
            # ^ You have to pass an argument to call the function always                                     
            # when you defined with this param, otherwise you'll get a TypeError

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
    """One Docstrings example"""