"""
A few boolean expression puzzles to solve.
You can assume all numbers are integers.
Do not call any of these functions from this file... Do that from the main.py file.
"""


def is_sweltering():
    """
    This function asks the user for the current temperature (in Farenheit).
    It returns True if that temperature is very hot, False otherwise.
    Hot is defined as any temperature over 90 degrees Farenheit.

      :returns: True if the temperature is over 90, False otherwise.
    """
    # write your code for this function below this line.
    current_temperature = float(input("What is the current temperature (in Farenheit)? "))
    if current_temperature > 90:
        return True
    else:
        return False


def is_warm():
    """
    This function asks the user for the current temperature (in Farenheit).
    It returns True if that temperature is very warm, False otherwise.
    Warm is defined as any temperature between 75 and 87 degrees Farenheit, inclusive.

      :returns: True if the temperature is between 75 and 87, inclusive, False otherwise.
    """
    # write your code for this function below this line.
    current_temperature = float(input("What is the current temperature (in Farenheit)? "))
    if current_temperature >= 75 and current_temperature <= 87:
        return True
    else:
        return False


def is_humid():
    """
    This function asks the user whether it is currently humid.
    We assume the user will answer either "yes" or "no".
    It returns True if so, False otherwise.

      :returns: True if it is humid today, False otherwise.
    """
    # write your code for this function below this line.
    is_it_humid = input("Is it currently humid? ")
    if is_it_humid == 'yes':
        return True
    else:
        return False 



def is_inclement():
    """
    This function asks the user what the weather forecast is today.
    We allow the user to respond any way they want.
    If they respond with any of the following, we return True, otherwise we return False: "rain", "snow", "sleet"

      :returns: True if it is raining, snowing, or sleeting today, False otherwise.
    """
    # write your code for this function below this line.
    weather_forecast = input("What is the weather forecast for today? ")
    if weather_forecast in ["rain", "snow", "sleet"]:
        return True
    else:
        return False
    



def is_typical_new_york_summer():
    """
    This function asks the user what the temperature is today and whether it is humid.
    If they respond that the temperature is above 90 degrees Farenheit and that it is humid, we return True, otherwise False.
    Requirements:
    - You must use the functions, is_sweltering() and is_humid() defined above to determine these two facts.
    - In other words, you cannot use the input function direclty in the code you write for this function.

      :returns: True if the temperature is over 90 and it is humid, False otherwise.
    """
    # write your code for this function below this line.
    determine_swelter = is_sweltering()
    determine_humidity = is_humid()
    if determine_swelter and determine_humidity:
        return True
    else:
        return False


def is_cool_and_nice():
    """
    This function determines whether it is cool and nice today.  It does so by relying on other functions defined above.
    Requirements:
    - You must use the functions, is_sweltering(), is_warm(), is_humid(), and is_inclement() defined above to determine whether it is cool and nice today.
    - The weather is considered cool if these functions all return False.

      :returns: True if the weather is cool and nice today, False otherwise.
    """
    # write your code for this function below this line.
    determine_swelter = is_sweltering()
    determine_warmth = is_warm()
    determine_humidity = is_humid()
    determine_inclement = is_inclement()

    if not determine_swelter and not determine_warmth and not determine_humidity and not determine_inclement:
        return True
    else:
        return False
