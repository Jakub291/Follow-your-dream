a = ('''write 'start' to start
write "stop" to stop
write quit to end
write help for help''')

print (a)
b = ("")
started = False

while (b.upper()) != "QUIT":
    b = input("what do you want to do?")
    if (b.upper()) == 'HELP':
        print (a)
    elif (b.upper()) == "START":
        if started ==True:
            print('car is allready started')
        else:
            started = True
            print ('car started')
    elif (b.upper()) == "STOP":
        if started == True:
            print ('car stoped')
            started = False
        else:
            print('car is allready stoped')
    elif (b.upper()) == "QUIT":
        break
    else:
        print('dont know that command')
print('my mission end here')
