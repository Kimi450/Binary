def Binary():
    #prints the list the binary patterns for every variable to be used
    var=int(input("Please enter the number of variables: "))
    print("")
    varNum=1
    printCounter=int(var)#variable's position in the Truth Table
    for v in range(1,var+1):
        finalLstLoop=2**(var-varNum)-1
        patternLst=[]
        print("Variable repetition pattern position in the Truth Table: ",printCounter)
        form=int((2**varNum)/2)#make sure they appear once or in multiples of 2
        #prints of 1's and 0's for a variable
        for i in range(form):
            patternLst.append(0)
        for i in range(form):
            patternLst.append(1)
        varLst=list(patternLst) #new list, not pointing to the same list(no infinite loop)
        for _ in range(finalLstLoop):
            for item in patternLst:
                varLst.append(item)
        print(varLst)
        print("")
        varNum+=1
        printCounter-=1
        if varNum>var:
            return
