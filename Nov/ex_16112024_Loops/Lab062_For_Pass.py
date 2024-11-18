for i in range(0,10,1):
    if i==6 or i==5:
        print(i)
    else:
        pass # pass is placeholder statement that does nothing
    # it is used  when a statement is syntactically required but no action is needed


    #  / i / condition  / O/P
    #  / 0 / 0==6  -> false  / 0/P  -> nothing printed
    #  / 1 / 1==6  -> false  / 0/P  -> nothing printed
    #  / 2 / 2==6  -> false  / 0/P  -> nothing printed
    #  / 3 / 3==6  -> false  / 0/P  -> nothing printed
    #  / 4 / 4==6  -> false  / 0/P  -> nothing printed
    #  / 5 / 5==6  -> true  / 0/P  -> 5
    #  / 6 / 6==6  -> true  / 0/P  -> 6
    #  / 7 / 7==6  -> false  / 0/P  -> nothing printed
    #  / 8 / 8==6  -> false  / 0/P  -> nothing printed
    #  / 9 / 9==6  -> false  / 0/P  -> nothing printed
    #  / 10 / 10==6  -> false  / 0/P  -> nothing printed