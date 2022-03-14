temp = input("Please type in the  temperature you like to convert? (e.g., 45F, 102C, 0K, etc... To get Kelvin Converson, type in for ex: 42C to K) : ")
degree = int(temp[:-1])
amount = temp[-1]

def convertCelsiusToFahrenheit():
    if amount.upper() == "C":
        temperature = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit"
    else:
        print("Input correct convention.")
        quit()
    print("The temperature in", o_convention, "is", temperature, "degrees.")#"and in", o_convention1, "is" ,temperature1, "degrees.")


def convertCelsiusToKelvin():
    if amount.upper() == "K":
        temperature = int((round((degree - 32) * 5 / 9)) + 273.15) 
        o_convention = "Kelvin"
    else:
        print("Input correct convention.")
        quit()
    print("The temperature in", o_convention, "is", temperature, "degrees.")#,"and in", o_convention1, "is" ,temperature1, "degrees.")

def convertFarenhiteToCelsius():
    if amount.upper() == "F":
        temperature = int(round((degree - 32) * 5 / 9))
        o_convention = "Celsius"
    else:
        print("Input correct convention.")
        quit()
    print("The temperature in", o_convention, "is", temperature, "degrees.")#,"and in", o_convention1, "is" ,temperature1, "degrees.")

def convertKelvinToCelsius():
    if amount.upper() =="C":
        temperature = int((round((degree - 32) * 5 / 9)) - 273.15) 
        o_convention = "Celsius"
    else:
        print("Input correct convention.")
        quit()
    print("The temperature in", o_convention, "is", temperature, "degrees.")
    