class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    
    conversion_factors = {
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Celsius', 'Fahrenheit'): lambda x: (x * 1.8) + 32,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: (x + 459.67) * (5/9),
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32,
    }

    conversion_function = conversion_factors.get((fromUnit, toUnit))
    if conversion_function:
        return conversion_function(value)
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} not possible")

if __name__ == '__main__':
    # Example usage
    try:
        result = convert('Celsius', 'Fahrenheit', 0)
        print(f"0 Celsius in Fahrenheit: {result}")
    except ConversionNotPossible as e:
        print(e)
