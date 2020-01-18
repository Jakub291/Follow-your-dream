a = int(9)
s = ('-')
imie = str(input('podaj imie '))
nazwisko = str(input('podaj nazwisko '))
numer = (input('podaj numer tel '))

print('czy imie to litery', imie.isalpha())
print('czy nazwisko to litery', nazwisko.isalpha())
print('czy numer to cyfry', numer.isdigit()	)

print(imie, nazwisko)
print(str.capitalize(imie), str.capitalize(nazwisko))
print(numer.replace("-","")) #remove dash from phone number
print('czy to kobieta', imie.endswith(str('a'),)) #check gender, if name end on a its woman else men

personal = ((imie) + (' ') + (nazwisko) + (' ') + (numer.replace("-","")))
print (personal)
print(len(personal) - 11) #print lenght of name and surname

end = input('nacisnij enter by zakonczyc program')
