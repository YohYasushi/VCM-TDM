def CCR(GENDER, AGE, SCR, WEIGHT):
    if SCR < 0.6:
        SCR=0.60
    else:
        if GENDER == 'M':
            a = (( 140 - AGE ) * WEIGHT ) / ( 72 * SCR)
        elif GENDER == 'F':
            a = 0.850 *  (( 140 - AGE ) * WEIGHT ) / ( 72 * SCR)
        else:
            a = (( 140 - AGE ) * WEIGHT ) / ( 72 * SCR)
    return a

# この関数はscr=0.6未満補正を入れております。