from bingo import Bingo, Table

def main():
    '''
    Main function for assignment 2 creates the "game" enviroment for the assignment. 

    Inputs:
            None

    Returns:
            None 
    '''
    welcomeBanner()
    game = Table()

    bingoName = getBingoName()
    callingName = getCallingName()
    #bingoName = 'bingoDeck.txt'   #for quicker testing of other methods 
    #callingName = 'callingDeck_full_rankonly_tie.txt' #for quicker testing of other methods 
    game.populateDeck(0, bingoName)
    game.populateDeck(1, callingName)
    run = True
    roundNumber = 0 

    while run:
        roundNumber += 1
        mode, speed = getMode()
        game.dealBingo(mode)
        
        print('\nRound {} beginning...'.format(roundNumber))
        noWinner = True 
        while noWinner:
            game.displayTable()
            card = game.callCard()
            print('Now calling {}'.format(card))
            game.updateTable(card, speed)
            if game.isWinner() == True:
                game.displayTable()
                
                print('Round {}: {}'.format(roundNumber, game.whoWon()))
                noWinner = False

        another = anotherRound()
        if another == "Y":
            game.clearTable()
            game.resetDecks()
        elif another == "N":
            run = False
            print("Thank you for playing. Goodbye.")

    return 


def anotherRound():
    '''
    Asks the user if they want to play another round and validates their input

    Inputs:
            None
    
    Returns:
            another(str): whether or not they want to play another round
    '''
    another = None
    while another not in ["Y", "N"]:
        another = input('Play another round (Y/N)? ').upper()
    return another


def welcomeBanner():
    '''
    WELCOME BANNER FOR THE GAME

    Inputs:
            None

    Returns:
            None 
    '''
    print('******************************')
    print('Welcome to Playing Card Bingo!')
    print('******************************')
    return

def getBingoName():
    '''
    Gets the bingo / grid deck file name, i.e the name that will be used to open the file that contains 
    the cards for the grid / bingo deck. Verifies the name exists and returns the file information in the 
    form of a list.

    Inputs:
            None

    Returns:
            fList(list): the list containing all of the cards.
    '''
    print('Creating bingo deck...')
    check = False 
    while check != True:
        try:
            filename = input('Please enter filename to initialize deck: ')
            with open(filename) as f: #just checking if the file exists
                pass
            check = True 
        except OSError:
            print('Problem with filename provided. Creating bingo deck...')
    return filename

def getCallingName():
    '''
    Gets the call deck file name, i.e the name that will be used to open the file that contains 
    the cards for the call deck. Verifies the name exists and returns the file information in the 
    form of a list.

    Inputs:
            None

    Returns:
            fList(list): the list containing all of the cards.
    '''
    print('Creating calling deck...')
    check = False 
    while check != True:
        try:
            filename = input('Please enter filename to initialize deck: ')
            with open(filename) as f: #just checking if the file exists
                pass
            check = True 
        except OSError:
            print('Problem with filename provided. Creating call deck...')

    return filename

def getMode():
    '''
    Gets the mode / speed round that the user wants to play, validates there is acceptable input for both of 
    the values and returns them to the main() function. 

    Inputs:
            None

    Returns:
            mode(str): the mode the user will play this round (lines, full, corners)
            speed(bool): True - speed mode, only check the ranks of the cards
                         False - slower mode, checks the ranks and the suits of the cards
    '''
    check = False
    while check != True:
        mode = input('Please select playing mode for this round: (L)ine, (C)orners, (F)ull > ').upper()
        if mode in ["L", "C", "F"]:
            check = True 

    check = False
    while check != True:
        speed = input('Play speed round (i.e. compare card ranks only) (Y/N)? ').upper()
        if speed in ["Y", "N"]:
            check = True
    if speed == "Y":
        speed = True

    elif speed == "N":
        speed = False 
    return mode, speed

if __name__ == '__main__':
    main()