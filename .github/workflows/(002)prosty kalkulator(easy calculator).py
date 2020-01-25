print ('witaj w prostym kalkulatorze')
code = (input('nacisnij ENTER aby kontynuowac'))
while code != 5:
    print ('jeśli chcesz dodawać kliknij 1')
    print ('jeśli chcesz odejmować kliknij 2')
    print ('jeśli chcesz mnożyć kliknij 3')
    print ('jeśli chcesz dzielić kliknij 4')
    print ('jeśli chcesz wyjsc kliknij 5')
    code = int(input('co chcesz zrobic?'))
    if code == (1): #addition
        num1 = float(input('wpisz liczbe')) #write first number
        num2 = float(input('wpisz liczbe')) #write second number
        print (num1 + num2)
    elif code == (2): #subtraction
        num1 = float(input('wpisz liczbe')) 
        num2 = float(input('wpisz liczbe')) 
        print (num1 - num2)
    elif code == (3): #multiplication
        num1 = float(input('wpisz liczbe')) 
        num2 = float(input('wpisz liczbe')) 
        print (num1 * num2)
    elif code == (4): #division
        num1 = float(input('wpisz liczbe')) 
        num2 = float(input('wpisz liczbe')) 
        try:
            num2 != 0 
            print (num1 / num2)
        except ZeroDivisionError as blad:
            print("you can't divide by 0")
else:
    print('KONIEC')
