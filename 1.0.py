def Binary():
    #prints the list of the binary patterns for every variable to be used
    var = int(input("Please enter the number of variables: "))
    print("")
    varNum = 1
    printCounter = int(var) #variable's position in the Truth Table
    for v in range(1,var+1):
        finalLstLoop = 2 ** (var-varNum) - 1 #calculation for changing number of repetitions
        patternLst = []
        print("Variable repetition pattern's position in the Truth Table: ", printCounter)
        form = int((2 ** varNum) / 2) #make sure they appear once or in multiples of 2
        for i in range(form): #prints of 1's for a variable
            patternLst.append(0)
        for i in range(form): #prints of 1's for a variable
            patternLst.append(1)
        varLst = list(patternLst) #new list, not pointing to the same list(no infinite loop)
        for patterns in range(finalLstLoop): #repeat the patterns to make them the same length
            for item in patternLst:
                varLst.append(item)
        print(varLst)
        print("")
        varNum += 1
        printCounter -= 1
        if varNum > var:
            break
