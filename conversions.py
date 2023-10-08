def convertCelsiusToKelvin(celsius):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins.
    """
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit.
    """
    return (celsius * 1.8) + 32

def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5/9)
    return kelvin

def convertKelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def convertKelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    return celsius