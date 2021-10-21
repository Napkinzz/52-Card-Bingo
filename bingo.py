#******************
# CMPUT 175 ASSIGNMENT 2
# BINGO.PY
# Author: LUKAS WASCHUK 
# Collaborators/References: N/A 
#******************
from playingCards import Card, Deck
from random import randint

class Bingo:
    def __init__(self):
        '''
        Init for Bingo class, creates a 5x5 grid of None. Defaults play mode to "L"

        Inputs:
                None
        
        Returns:
                None
        '''
        
        self.__playMode = 'L'
        self.__grid = [[None, None, None, None, None],\
                       [None, None, None, None, None],\
                       [None, None, None, None, None],\
                       [None, None, None, None, None],\
                       [None, None, None, None, None]]

    def populate(self, cards, playMode):
        '''
        Fills the grid using a "deck" of cards (circular queue), will assign a new play mode if not "L"

        Inputs:
                cards(deck/queue): the deck of cards to be added to the 5x5 grid.
                playMode(str): L C F, the play modes for the game 
        
        Returns:
                None 
        '''
        assert cards.deckSize() >= 25, "NOT ENOUGH CARDS IN DECK"
        assert playMode in ["L", "C", "F"], "NOT A VALID PLAY MODE"
        self.__playMode = playMode

        for row in self.__grid:
            for i in range(5):
                card = cards.dealCard()
                row[i] = card 
        self.__grid[2][2].turnOver()
        
    def search(self, card, rankOnly):
        '''
        Searchs the grid for a entered card. Uses a parameter rankOnly to choose whether to look 
        only at the ranks of the cards, or the ranks and the suits.

        Inputs:
                card(card): the card to be looked for 
                rankOnly(bool): the boolean for for specific the search will be 

        Returns:
                Boolean: True - if the card is found / matched 
                         False - if the card is not found / matched 
        '''
        assert isinstance(rankOnly, bool), "RANKONLY VALUE MUST BE BOOLEAN"
        grid = self.__grid 
        found = None
        if rankOnly == True:   
            for row in grid:
                for item in row:
                    if item.getRank() == card.getRank():
                        if item.isFaceUp() == True:
                            item.turnOver()
                            found = True
            if found == True:
                return True
            else:
                return False 

        elif rankOnly == False:   
            for row in grid:
                for item in row:
                    if (item.getRank() == card.getRank()) and (item.getSuit() == card.getSuit()):
                        if item.isFaceUp() == True:
                            item.turnOver()
                            return True 
        else:
            return False 

    def Lcheck(self):
        '''
        Sub method of the isBingo() method. This will perform the "check" for the "L"(line) gamemode. 
        This will check every column, row, and diagonals for all the cards of the respective rows.. etc
        to be faced down. When / if a row is found with everything faced down the method will return true
        otherwise it will return false. 

        Inputs:
                None

        Returns:
                Boolean: True - if there is a bingo
                         False - if there is no bingo
        '''
        grid = self.__grid 

        #ROWS
        for row in grid:
            bingoHorizontal = True
            for item in row:
                if item.isFaceUp()==True:
                    bingoHorizontal = False
            if bingoHorizontal == True:
                return True
        
        #COLUMNS
        for i in range(5):
            bingoVerticle = True 
            for k in range(5):
                if grid[k][i].isFaceUp()==True:
                    bingoVerticle = False 
            if bingoVerticle == True:
                return True 
        
        #UPPER DAIG (TOP RIGHT TO BOTTOM LEFT )
        if (grid[0][0].isFaceUp()==False and grid[1][1].isFaceUp()==False and
            grid[2][2].isFaceUp()==False and grid[3][3].isFaceUp()==False and
            grid[4][4].isFaceUp()==False):
            return True 

        #LOWER DAIG (BOTTOM LEFT TO TOP RIGHT)
        if (grid[4][0].isFaceUp()==False and grid[3][1].isFaceUp()==False and
            grid[2][2].isFaceUp()==False and grid[1][3].isFaceUp()==False and
            grid[0][4].isFaceUp()==False):
            return True 
        else:
            return False



    def Ccheck(self):
        '''
        Sub method of the isBingo() method. This one will check for a bingo in the "C"(corners) 
        playmode. It will check the corners of the grid.

        Inputs:
                None

        Returns:
                Boolean: True - if there is a bingo
                         False - if there is no bingo
        '''
        grid = self.__grid

        #CHECKS THE 4 CORNERS
        if (grid[0][0].isFaceUp()==False and grid[0][4].isFaceUp()==False and
            grid[4][0].isFaceUp()==False and grid[4][4].isFaceUp()==False):
            return True
        else:
            return False 
        
    def Fcheck(self):
        '''
        Sub method of the isBingo() method. Will check for a bingo in the "F"(full) playmode. 
        Check every cell in the 5x5 grid if the cards are ALL faced down.

        Inputs:
                None

        Returns:
                Boolean: True - if there is a bingo
                         False - if there is no bingo
        '''
        grid = self.__grid
        bingo = True 
        for row in grid:
            for item in row:
                if item.isFaceUp()==True:
                    bingo = False
        return bingo

    def isBingo(self):
        '''
        Check the grid for faced down cards to form a bingo(win) depending on the game mode 
        selected when the grid was created. Will call upon sub functions to return a boolean 
        respective to the game mode selected. 

        Inputs:
                None
        
        Returns:
                Note: Will call upon a subfuntion to return the boolean.
                Boolean: True - if there is a bingo
                         False - if there is no bingo
        '''
        # CORNERS GAME MODE 
        if self.__playMode == "C":
            return self.Ccheck()

        # FULL GAME MODE SELECTED 
        elif self.__playMode == "F":
            return self.Fcheck()

        # DEFAULT / LINES GAME MODE SELECTED
        else:
            return self.Lcheck()

    def clear(self):
        '''
        Clears the 5x5 grid and resets it to NONE in every position. Returns the list of all the cards.

        Inputs:
                None
        
        Returns:    
                cardList(list): the list containing all the cards in the 5x5 grid before it was 
                                cleared
        '''
        cardList = []

        for row in self.__grid:
            for i in range(5):
                cardList.append((row[i]))
                row[i] = None

        return cardList 

    def __str__(self):
        '''
        string method for bingo. returns the 5x5 grid as a string.

        Inputs:
                None

        Returns:
                string(str): the string rep of the grid 
        '''
        string = ''
        for row in self.__grid:
            for item in row:
                string = string + str(item)
            string = string + '\n'
        return string 


class Table:
    def __init__(self):
        '''
        Init values for the table class. Creates multiple Bingo grids and decks. 

        Inputs:
                None
        
        Returns:
                None
        '''
        self.__playerA = Bingo()
        self.__playerB = Bingo()
        self.__gridDeck = Deck()
        self.__callDeck = Deck()
        self.__gridDiscard = Deck()
        self.__callDiscard = Deck() 

    def populateDeck(self, deckNumber, filename):
        '''
        Fills a deck with cards from a text file, will sort them into one of two decks depending on the input

        Inputs:
                deckNumber(int): 0 - fill the grid / bingo deck 
                                 1 - fill the call deck 
                filename(str): the filename to extract the card order from

        Returns:
                None
        '''
        assert deckNumber in [0, 1], "NOT A VALID DECKNUMBER"
        assert isinstance(filename, str), "ENTER A STRING FOR FILENAME"

        with open(filename) as f:
            fList = f.readlines()
        if deckNumber == 0: #POPULATE BINGO 
            for item in fList:
                try:
                    self.__gridDeck.addCard(Card(item[0], item[1], False))
                except AssertionError:
                    item = item.strip()
                    print('[ {} ] is a invaid card and will not be added to the deck.'.format(item))
            if self.__gridDeck.isComplete() != True:
                raise Exception('Deck created from {} is not valid.'.format(filename))
        
        elif deckNumber == 1: #POPULATE CALLING DECK 
            for item in fList:
                try:
                    self.__callDeck.addCard(Card(item[0], item[1], False))
                except AssertionError:
                    item = item.strip()
                    print('[ {} ] is a invaid card and will not be added to the deck.')
            if self.__callDeck.isComplete() != True:
                raise Exception('Deck created from {} is not valid.'.format(filename))

    def dealBingo(self, mode):
        '''
        Fills player A and B 5x5 bingo grids alternating one card at a time until both have 25 cards. 

        Inputs:
                mode(str): the mode the game will be played (line, full, corners)

        Returns:
                None
        '''
        assert mode in ["L", "C", "F"], "NOT A VALID MODE"
        playerA = self.__playerA
        playerB = self.__playerB
        playerAdeck = Deck()
        playerBdeck = Deck() 

        for x in range(50):
            if x % 2 == 0: #starts on player A
                playerAdeck.addCard(self.__gridDeck.dealCard())  
                
            elif x % 2 == 1: # alternates to player B 
                playerBdeck.addCard(self.__gridDeck.dealCard())
        
        #discarding hte remaining 2 cards 
        while self.__gridDeck.deckSize() != 0:
            self.__gridDiscard.addCard(self.__gridDeck.dealCard())

        playerA.populate(playerAdeck, mode)
        playerB.populate(playerBdeck, mode)
    

    def displayTable(self):
        '''
        Prints the contents of player A and B's bingo grids. Will add BINGO! below their grid if they manage to get
        a bingo.

        Inputs:
                None

        Returns:
                None
        '''
        print('Player A:')
        print(str(self.__playerA),end='')
        if self.__playerA.isBingo() == True:
            print('           BINGO!          ')
            
        else:
            print()
        print('Player B:')
        print(str(self.__playerB),end='')

        if self.__playerB.isBingo() == True:
            print('           BINGO!          ')
        else:
            print()
        

    def callCard(self):
        '''
        Calls the top card from the call deck and returns it. Also places it in the discard deck

        Inputs:
                None

        Returns:    
                card(card): the card object that was removed from the top of call deck.
        '''
        card = self.__callDeck.dealCard()
        self.__callDiscard.addCard(card)
        if card.isFaceUp() != True:
            card.turnOver()
        print('------------------------')
        return card 

    def updateTable(self, card, rankOnly):
        '''
        updates the player's 5x5 bingo grids using the most recently pulled card. 

        Inputs:
                card(card): the card the method will compare against the players bingo grids.
                rankOnly(bool): True - only comparing hte ranks of the cards
                                False = comparing the ranks and suits of the cards

        '''
        self.__playerA.search(card, rankOnly)
        self.__playerB.search(card, rankOnly)


    def clearTable(self):
        '''
        removes all the cards from player A and B's grids, and places them into the discard deck, also puts the 
        remaining cards from the call deck into the call Discard Deck. 

        Inputs:
                None

        Returns:
                None
        '''
        discardA = self.__playerA.clear()
        discardB = self.__playerB.clear()

        for item in discardA:
            self.__gridDiscard.addCard(item)
        for item in discardB:
            self.__gridDiscard.addCard(item)
       
        while self.__callDeck.deckSize() != 0:
            self.__callDiscard.addCard(self.__callDeck.dealCard())

    def resetDecks(self):
        '''
        Shuffles and resets the decks into a state where they can be dealt again to the players, ensureing a random
        order.

        Inputs:
                None

        Returns:
                None 
        '''
        callDiscarded = []
        gridDiscard = []

        while self.__callDiscard.deckSize() != 0: # get the 52 call cards intp a list for shuffling 
            callDiscarded.append(self.__callDiscard.dealCard()) 

        while self.__gridDiscard.deckSize() != 0:
            self.__gridDeck.addCard(self.__gridDiscard.dealCard()) #get all 52 cards for the grids in the same place 

        count = 50 #from -1 to 50 there are 52 integers (counting -1 and 0)
        while self.__gridDeck.deckSize() != 52: #shuffle grid discard and add them back into the deck 
            shuffleValue = randint(-1,count) #using -1 to avoid index error from 0 (cause cound WILL hit 0)
            self.__gridDeck.addCard(gridDiscard.pop(shuffleValue))
            count -= 1

        count = 50 #same thing as above, just different deck
        while self.__callDeck.deckSize() != 52:
            shuffleValue = randint(-1,count) 
            self.__callDeck.addCard(callDiscarded.pop(shuffleValue))
            count -= 1

    def isWinner(self):
        '''
        Checks whether or not either of the players are winners

        Inputs:
                None
        
        Returns:
                Boolean: True - if one of them is a winner 
                         False - if neither of them are winners
        '''
        if self.__playerA.isBingo() == True or self.__playerB.isBingo() == True:
            return True
        else:
            return False

    def whoWon(self):
        '''
        returns a print statement dependant on who won the round of bingo (includes a tie), it will throw a 
        error if there is no winner and this method has been called. It will usually be called after the method
        isWinner() validates that there is actually a winner.

        Inputs:
                None 

        Returns:
                print statements depending on who won the round
        '''
        if self.__playerA.isBingo() == True and self.__playerB.isBingo() == True:
            return "Tie!"
        elif self.__playerA.isBingo() == True:
            return "Player A Won!"
        elif self.__playerB.isBingo() == True:
            return "Player B Won!"
        else:
            raise Exception('Neither player has won...')

################################################################################################################
#               EVERYTHING BELOW IS FOR THE MAIN() FUNCTION 
################################################################################################################

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