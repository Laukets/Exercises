def tab():
    a = 1
    b = 1
    print('a\t b\ta*b')
    for i in range(13):
        for i in range(11):
            c = a * b
            print(a,'\t',b,'\t',c)
            b = b + 1
        b = 0
        a = a + 1
        print('\n')

tab()