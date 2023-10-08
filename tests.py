import unittest
from conversions import convertCelsiusToFahrenheit, convertCelsiusToKelvin, convertFahrenheitToKelvin, convertFahrenheitToCelsius, convertKelvinToFahrenheit, convertKelvinToCelsius

class TestTemperatureConversion(unittest.TestCase):

    def test_convertCelsiusToFahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32, places= 2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212, places= 2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(37), 98.6, places=2)
    
    def test_convertCelsiusToKelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-40), 233.15, places=2)

    def test_convertFarenheitToKelvin(self):
        self.assertAlmostEqual(convertFahrenheitToKelvin(32), 273.15, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(100), 310.93, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(-250), 116.48, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(0), 255.37, places=2)

    def test_convertFarenheitToCelcius(self):
        self.assertAlmostEqual(convertFahrenheitToCelsius(0), -17.78, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(100), 37.78, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(-250), -156.67, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(32), 0, places=2)

    def test_convertKelvinToFahrenheit(self):
        self.assertAlmostEqual(convertKelvinToFahrenheit(0), -459.67, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(100), -279.67, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(-250), -909.67, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(32), -402.07, places=2)

    def test_convertKelvinToCelsius(self):
        self.assertAlmostEqual(convertKelvinToCelsius(0), -273.15, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(100), -173.15, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(-250), -523.15, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(32), -241.15, places=2)

    

    
if __name__ == '__main__':
    unittest.main()