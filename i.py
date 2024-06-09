import random

# Function for player to pick their numbers
#guess1 is for a single ticket
#guess 2 is for a second ticket
#guess2_  is  nested list containing guess1 and guess 2
#the function returns a list and a nested list
def pickYourNumber():
    guess1 = random.sample(range(1, 10), 6)
    guess2 = random.sample(range(1, 10), 6)
    guess2_ = [guess1, guess2]
    return guess1, guess2_


#check to see if either of two tickets are winning return win or lose
#the third set is the winning ticket
#nested_list consists of two list, each corresponding to two tickets
def twoTickets(nested_list, third_list):

    third_set = set(third_list)
    for sublist in nested_list:
        if third_set.issubset(sublist):
            return "win"
    return "lose"

#check to see if single ticket is a win return win or lose
#list1 is ticket 1 and list two is the winning ticket
def oneTicket(list1, list2):
    # Convert lists to sets for efficient membership testing
    set1 = set(list1)
    set2 = set(list2)

    # Check if set1 is a subset of set2
    if set1.issubset(set2):
        return "win"
    else:
        return "lose"


# Function to run the lottery and check for wins
def runLottery():
    computerPick = random.sample(range(1, 10), 6)
    oneTicket_, twoTickets_ = pickYourNumber()
    oneTicketResult = oneTicket(oneTicket_, computerPick)
    twoTicketResult = twoTickets(twoTickets_, computerPick)

    #print(oneTicketResult)
    #print(twoTicketResult)
    return oneTicketResult, twoTicketResult
    
    

# Main function to simulate the lottery over n weeks
def total(n):
    oneTicketWins = 0
    twoTicketWins = 0
    print("working")
    for _ in range(n):
        print(_)
        x1, x2 = runLottery()

        if x1 == "win":
            oneTicketWins += 1
        if x2 == "win":
            twoTicketWins += 1
        if n/1000000 == 1:
            print("million")
    

    print(f"Number of wins with one ticket: {oneTicketWins}")
    print(f"Number of wins with two tickets: {twoTicketWins}")
    if oneTicketWins > 0:  # Avoid division by zero
        print("Increased chance of winning with two tickets is: {:.2f}".format(twoTicketWins / oneTicketWins))
    else:
        print("No wins with one ticket to compare.")

# Run the lottery simulation for 10,000,000 weeks

total(1000000)