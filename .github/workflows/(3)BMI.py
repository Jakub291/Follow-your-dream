waga = int(input("podaj swoja wage")) #write your weight
wzrost = float(input("podaj swoj wzrost w metrach")) #write your haight in meters
BMI = waga / (wzrost ** 2)

if (BMI < 18.5):
    print ("twoje BMI to:" , BMI , " i masz niedowage")
elif (BMI >18.5) and (BMI < 24):
    print ("twoje BMI to:" , BMI , " i masz prawidlowa wage")
elif (BMI >24) and (BMI < 26.5):
    print ("twoje BMI to:" , BMI , " i masz lekka nadwage")
elif (BMI > 26.5):
    print ("twoje BMI to:" , BMI , " i masz  nadwage")
if (BMI > 30) and (BMI < 35):
    print ("dodatkowo masz otyłość")
elif (BMI >35) and (BMI < 40):
    print ("dodatkowo masz otyłość II stopnia")
elif (BMI > 40):
    print ("dodatkowo masz otyłość III stopnia")
