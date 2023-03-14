def lab32():

    i = False
    s = []
    while i == False:
        inp = input()
        if inp == 'stop':
            i = True
        else:
            s.append(inp)

    print(" ".join(s))

def lab33():
    word = input()
    if 'ф' in word:
        print('Ого! Это редкое слово!')
    elif 'Ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print('Эх...Это не очень редкое слово...')

def lab34():
    from random import randint
    i = 0
    j = 0
    while i < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        res = int(input(str(a) + '+' + str(b) + '='))
        if res != a + b:
            print('ответ неверный')
            i += 1
        else:
            print('Правильно!')
            j += 1
    if i == 3:
        print('игра окончена. Правильных ответов:', j)

lab32()
lab33()
lab34()