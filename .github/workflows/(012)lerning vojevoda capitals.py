import random
random.seed()

score = 0
choose = (input('witaj w grze do nauki wojewódź! Nacisnij enter by kontynuować.'))


Woj = ['województwo dolnośląskie ','województwo kujawsko-pomorskie ','województwo lubelskie ', 'województwo lubuskie ',  'województwo łódzkie ', ' województwo małopolskie ', 'województwo mazowieckie ', 'województwo opolskie ', 'województwo podkarpackie ', 'województwo podlaskie ', 'województwo pomorskie ', 'województwo śląskie ', 'województwo świętokrzyskie ', 'województwo warmińsko-mazurskie ', 'województwo wielkopolskie ', 'województwo zachodniopomorskie ']
cap = ['Wrocław', 'Bydgoszcz', 'Lublin', 'Zielona Góra', 'Łódź', 'Kraków', 'Warszawa', 'Opole','Rzeszów', 'Białystok', 'Gdańsk', 'Katowice', 'Kielce', 'Olsztyn', 'Poznań', 'Szczecin']
while choose != 'n': # n is a exit button, look line 26
    for x in range(1,6):
        print ('numer próby : ' , x)
        scolpe = random.randint(0,len(Woj)-1)
        for y in range(1,6):
            guess = input('podaj stolice wojewodzctwa ' + Woj[scolpe]).capitalize() # capitalize first letter if user forget to do this
            if guess == cap[scolpe]:
                score = score + 1 #add one point for every right answer
                print ('poprawna odpowiedz')
                break
            else:
                print ('spróbuj jeszcze raz')
                if y == 5: # user have 5 chance to answer, then program show right answer and jump to next qestion
                    print ('prawidłowa odpowiedź to: ' + cap[scolpe])    

    print('twoj wynik to: ', score)
    choose = input('Czy chcesz zagrać jeszcze raz? y/n')
else:
    print('dziękuje za gre!')