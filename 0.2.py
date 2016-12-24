def Binary():
    #prints the binary pattersn for every variable to be used
    var=int(input("Please enter the number of variables: "))
    varNum=1
    for v in range(1,var+1):
        print("Variable repetition patterns starting from the right: ",varNum)
        form=int((2**varNum)/2)#make sure the numbers are 1 or multiples of 2
        #prints of 1's and 0's for a variable
        for i in range(form):
            print(0)
        for i in range(form):
            print(1)
        varNum+=1
        if varNum>var:
            return
        
Binary()
