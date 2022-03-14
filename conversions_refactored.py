temperature=['degree_kelvin','degree_celsius','degree_farenhite']
distance=['mm','cm','m','km']

print("Conversion units in Temperature :",temperature)
print("Conversion units in Distance :",distance)
fromUnit = input('Enter pre conversion value: ')
toUnit = input('Enter post conversion value: ')
value = float(input("Enter value: "))
temp = fromUnit + "To" + toUnit
temp = temp.lower()
count=0
answer=0
if fromUnit in temperature:
    if toUnit in temperature:
        if 'degree_kelvintodegree_kelvin' == temp:
            answer = value
        if 'degree_kelvintodegree_celsius' == temp:
            answer = value - 273.15
        if 'degree_kelvintodegree_farenhite' == temp:
            answer = ((value - 273.15) * 9/5 + 32) 
        if 'degree_celsiustodegree_celsius' == temp:
            answer = value
        if 'degree_celsiustodegree_kelvin' == temp:
            answer = value + 273.15
        if 'degree_celsiustodegree_farenhite' == temp:
            answer = (value * 9/5) + 32 
        if 'degree_farenhitetodegree_farenhite' == temp:
            answer = value
        if 'degree_farenhitetodegree_celsius' == temp:
            answer = ((value - 32) * 5/9)
        if 'degree_farenhitetodegree_kelvin' == temp:
            answer = ((value - 32) * 5/9) + 273.15
        print("\nAnswer: ",answer,"",toUnit)        
    else:
        print("\nConversion Not Possible")
    
if fromUnit in distance:
    if toUnit in distance:
        if 'mmtocm' == temp:
            answer = value / 10
        if 'mmtom' == temp:
            answer = value / 1000
        if 'mmtokm' == temp:
            answer = value / 1000000 
        if 'mmtomm' == temp:
            answer = value
        if 'cmtocm' == temp:
            answer = value
        if 'cmtomm' == temp:
            answer = value * 10 
        if 'cmtom' == temp:
            answer = value / 100
        if 'cmtokm' == temp:
            answer = value / 100000
        if 'mtom' == temp:
            answer = value
        if 'mtomm' == temp:
            answer = value * 1000 
        if 'mtocm' == temp:
            answer = value * 100
        if 'mtokm' == temp:
            answer = value / 1000 
        if 'kmtokm' == temp:
            answer = value
        if 'kmtomm' == temp:
            answer = value * 1000000
        if 'kmtocm' == temp:
            answer = value * 100000
        if 'kmtom' == temp:
            answer = value * 1000
        print("\nAnswer: ",answer,"",toUnit)        
    else:
        print("\nConversion Not Possible")