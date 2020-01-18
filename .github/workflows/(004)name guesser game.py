import random
lista = ['ala', 'tomek', 'marek'] #list of all names
x = random.choice(lista) # choose one random name from the list above
c = ()
print (random.sample(x, len(x)))
while c != x:
    c = str(input('zgadnij moje imie, lub wpisz q by wyjsc'))
    if c == 'q' or c =='Q': #break loop when you write Q
        break
else:
    print('zgadles')
