# -*- coding: utf-8 -*-


a = int(input('podaj kwote')) #enter amount
b = float(input('podaj stope opreconetowania rocznego ')) # enter intrest
c = int(input(' przez ile lat ')) #how many years

wynik = a + (a * b * c)


print ('Twoje *stan_początkowy* {}zł przez *czas* {}  na lokacie *oprocentowanie* {} urośnie do *wynik* {}.' .format(a , c, b , wynik) )
end = input('wcisnij enter by zakonczyc')


