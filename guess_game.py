import os
continue_or_no = 'y'
while(continue_or_no == 'y'):
    number_a = raw_input('enter a:')
    os.system('clear')
    number_b = raw_input('enter b:')
    os.system('clear')
    count_a = 0
    count_b = 0

    while(True):

        guess_a = raw_input("guess number a:")
        if guess_a == number_a:
            count_a += 1
            print "congratulation !"
            print "you used ",count_a,"times to get the right number"
            continue_or_no = raw_input("input y to continue or input n to terminate:")
            if continue_or_no == 'y':
                break
            else:
                break
                
        else:
            count_a += 1
            big_or_small = guess_a > number_a
            if big_or_small == True:
                print "it's big"
            else:
                print "it's small"
            
        guess_b = raw_input("guess number b:")
        if guess_b == number_b:
            count_b += 1
            print "congratulation !"
            print "you used ",count_b,"times to get the right number"
            continue_or_no = raw_input("input y to continue or input n to terminate:")
            if continue_or_no == 'y':
                break
            else:
                break
        else:
            count_b += 1
            big_or_small = guess_b > number_b
            if big_or_small == True:
                print "it's big"
            else:
                print "it's small"
