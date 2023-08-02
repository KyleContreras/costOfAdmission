#-----------------------------------------------------#
#                                                     #
#       Welcome to Escape Artists Escape Room         #
#                                                     #
#-----------------------------------------------------#

# Main function
def MainMenu():
    print("C: Calculate admission cost")
    print("D: Display admission options")
    print("X: Exit application")

    menuChoice = input("Choose an option: ")

    if menuChoice == 'C' or menuChoice == 'c':
        CalculateAdmission()
    elif menuChoice == 'D' or menuChoice == 'd':
        DisplayFees()
    elif menuChoice == 'X' or menuChoice == 'x':
        print("Exiting application")

# Asks user for party size and session time. Costs calculated here.
def CalculateAdmission():
    timeLength = int(input("Select a session length (35, 60, or 75): "))
    partySize = int(input("How many will be in your party?: "))
    cost = 0.00
    groupCost = 0.00
    pricePerPerson = 0.00

    if timeLength == 35:
        cost += 85.00
    elif timeLength == 60:
        cost += 130.00
    elif timeLength == 75:
        cost += 155.00
        #cost = round(cost + 155.00, 2)
        
    groupCost = CalculateServiceFee(cost)

    pricePerPerson = round(groupCost/partySize, 2)

    print("Group total: " + "$" + str(groupCost))
    print("Cost per person: " + "$" + str(pricePerPerson))

    goToMenu = input("Press 'm' to return to the main menu: ")

    if goToMenu == 'M' or goToMenu == 'm':
        MainMenu()
    

# Displays admission options for user
def DisplayFees():
    print("35 minutes of times: " + "$" + str(85.00))
    print("60 minutes of times: " + "$" + str(130.00))
    print("75 minutes of times: " + "$" + str(155.00))

    goToMenu = input("Press 'm' to return to the main menu: ")

    if goToMenu == 'M' or goToMenu == 'm':
        MainMenu()
        
# Calculates the service fee charge
def CalculateServiceFee(subtotal):
    subTotal = subtotal
    serviceFee = subTotal * 0.05

    finalCost = round(subTotal + serviceFee, 2)
    
    return finalCost

MainMenu()
