#Manuel Duran 1584885
def exact_change(user_total):
    #checking for change
    if(user_total<=0):
        #print no change
        print("no change")
        #return 0 for all changes
        return(0,0,0,0,0)
    else:
        #obtaining total dollar count
        num_dollars=user_total//100
        #obtaining count of quarter
        num_quarters=(user_total%100)//25
        #obtaining count of dimes
        num_dimes=(user_total%100%25)//10
        #obtaining count of nikel
        num_nikels=(user_total%100%25%10)//5
        #obtaining count of pennis
        num_pennies=user_total%100%25%10%5
        #returns count of each change
        return(num_dollars,num_quarters,num_dimes,num_nikels,num_pennies)
if __name__ == '__main__':
    #accepting input
    input_val=int(input())
    #calling exact_change function and assigning values
    num_dollars,num_quarters,num_dimes,num_nikels,num_pennies=exact_change(input_val)
    #check if num_dollars is 1
    if(num_dollars==1):
        #print 1 dollar
        print("1 dollar")
        #check if num_dollars is greater than 1
    elif(num_dollars>1):
        #print number of dollar
        print("{} dollars".format(num_dollars))
        #check if num_quarters is 1
    if(num_quarters==1):
        #print 1 quarter
        print("1 quarter")
        #heck if num_quarters is greater than 1
    elif(num_quarters>1):
        #print number of quarter
        print("{} quarters".format(num_quarters))
        #check if num_dimes is 1
    if(num_dimes==1):
        #print 1 dimes
        print("1 dime")
    #check if num_dimes is greater than 1
    elif(num_dimes>1):
        #print number of dimes
        print("{} dimes".format(num_dimes))
        #check if num_nikels is 1
    if(num_nikels==1):
        #print 1 nikel
        print("1 nickel")
        #check if num_nikels is greater than 1
    elif(num_nikels>1):
        #print number of nikel
        print("{} nickels".format(num_nikels))
        #check if num_pennies is 1
    if(num_pennies==1):
        #print 1 pennie
        print("1 penny")
        #check if num_pennies is greater than 1
    elif(num_pennies>1):
        #print number of pennis
        print("{} pennies".format(num_pennies))