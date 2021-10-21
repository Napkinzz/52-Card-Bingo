#******************
# CMPUT 175 ASSIGNMENT 2
# PLAYINGCARDS.PY
# Author: LUKAS WASCHUK 
# Collaborators/References: N/A 
#******************
from queues import CircularQueue

class Card:
    def __init__(self, rank, suit, faceUp):
        '''
        INIT method, checks rank, suit, and faceUp to see if they are valid inputs. 
        then assigns them to "private" variables that only the class can call.

        Inputs:
                rank(str): the rank of the card
                suit(str): the suit of the card
                faceUp(bool): whether the card is faced up or down, as a boolean
        
        Returns:
                None
        '''
        validRanks = { 'A', 'a','2', '3', '4', \
                      '5', '6', '7', '8', '9', \
                      'T', 't', 'J', 'j', 'Q', \
                      'q', 'K', 'k'}
        validSuits = {'S', 's', 'H', 'h', 'D', \
                      'd', 'C', 'c'}
        assert rank in validRanks, "NOT A VALID RANK"
        assert suit in validSuits, "NOT A VALID SUIT"
        assert isinstance(faceUp, bool)==True, "NOT A VALID FACE UP/DOWN VALUE"

        self.__rank = rank.upper()
        self.__suit = suit.upper()
        self.__faceUp = faceUp 

    def getRank(self):
        '''
        Returns the rank of the card

        Inputs:
                None
        
        Returns:
                self.__rank(str): the rank of the card.
        '''
        return self.__rank 

    def getSuit(self):
        '''
        Returns the suit of the card.

        Inputs:
                None 
        
        Returns:
                self.__suit(str): the suit of the card. 
        '''
        return self.__suit 

    def isFaceUp(self):
        '''
        Returns a boolean value corresponding to the orientation of the card.
        True = faced UP; False = faced DOWN

        Inputs:
                None
        
        Returns:
                self.__facedUp(bool): the boolean value corresponding to the cards orientation.
        '''
        return self.__faceUp

    def turnOver(self):
        '''
        Turns the card over. i.e flips the boolean (orientation) of the card. Returns nothing.

        Inputs:
                None

        Returns:
                None
        '''
        self.__faceUp = not self.__faceUp

    def __eq__(self, anotherCard):
        '''
        check the current card with some other instance of the card class to see if they 
        are equivilant.

        Inputs:
                anotherCard(Card): some other instance of the Card class.

        Returns:
                Boolean: True - if they match 
                         False - if they dont match 
        '''
        if self.getRank() == anotherCard.getRank() and \
            self.getSuit() == anotherCard.getSuit():
            return True
        else:
            return False 

    def __str__(self):
        '''
        returns the string representation of the card 

        Inputs:
                None
        
        Returns:
                A string, 2 types. One for faced up, and one for faced down. 
        '''
        if self.__faceUp == False:
            return " [ ]  "
        else:
            return "[ {}{} ]".format(self.__rank, self.__suit)


class Deck:
    def __init__(self):
        '''
        Creates a circular Queue for the deck 

        Inputs:
                None 
                
        Returns:
                None
        '''
        self.__deck = CircularQueue(52)

    def addCard(self, card):
        '''
        Adds a card to the deck and checks if it is possible. i.e if the deck is full

        Inputs:
                card(Card): the card to be added 
            
        Returns:
                None
        '''
        assert isinstance(card, Card), "Can only add cards to deck"
        if card.isFaceUp() == True:
            card.turnOver()
            
        try:
             self.__deck.enqueue(card)
        except Exception:
            card.turnOver()
            print('Cannot add {}: deck is full.'.format(card))
            
    def dealCard(self):
        '''
        deals a card from the top position of the deck. also checks if the deck is empty.

        Inputs:
                None

        Returns:
                card(Card): the card that was removed from the top of the deck.
        '''
        try:
            card = self.__deck.dequeue()
            card.turnOver()
            return card
        except Exception:
            print("Cannot deal card from an empty deck.")

    def deckSize(self):
        '''
        Returns the size of the deck... i.e the current amount of cards in the deck. 

        Inputs:
                None

        Returns:
                None 
        '''
        return self.__deck.size()

    def isComplete(self):
        '''
        Checks if the deck is complete, (has 52 cards that are not duplicates).

        Note: The only was I was able to come up with a solution to this was just dequeueing / 
        dealing out all of the cards into a list using 'while not in list' to weed out duplicates
        while storing the exact cards / order in a list to enqueue them back into the deck. This 
        made the deck not change in contents / order, but allowed be to check for duplicates.    

        This would have been a "2 liner" solution if we were allowed to import the modules copy
        and deepcopy, but it said we were not allowed. So i have no idea how to check the contents
        of a queue without altering it. 

        That being said, this function does work and it does not alter the "Deck" at all, it 
        just could have been better :)

        Inputs:
                None 

        Returns:
                Boolean: Either True or False depending on the outcome/
        '''     
        isComplete = self
        dqList = []
        rebuild = [] 

        while isComplete.deckSize() != 0:
            card = isComplete.dealCard()
            if card.isFaceUp() != True:
                card.turnOver()
            rebuild.append(card)
            if card not in dqList: #if the cards exists in the list it will not be added.
                dqList.append(card)

        for item in rebuild:
            if card.isFaceUp() != False:
                card.turnOver()
            isComplete.addCard(item)

        if len(dqList)==52: #the only way to get the value of 52 is to have 52 unique cards.
            return True #thus, if there is one duplicate it will not return true.
        else:
            return False
    
    def __str__(self):
        '''
        Returns the string rep of the items in the deck. Since a deck has 52 items the best way 
        to represent them to me was in packs of 9. every 9 items a new line is entered.

        Note: This function endured the same problem as the iscomplete() function, as its hard to 
        look into a queue without altering it. 

        If we could have used the deepcopy module (makes a seperate ID for the item. like a clone)
        this solution would have been a few lines shorter and alot nicer :)
        '''
        deck = self
        count = 0 
        string = ''
        rebuild = []
        while deck.deckSize() != 0:
            card = deck.dealCard()
            if card.isFaceUp() != True:
                card.turnOver()
            rebuild.append(card)
            if count == 9:
                string = string + '\n'
                count = 0
            string = string + str(card)
            count += 1 
        for item in rebuild:
            deck.addCard(item)
            if card.isFaceUp() != False:
                card.turnOver()
        return string 



if __name__ == '__main__':
    
    #JUST A BUNCH OF TESTS 
    
    '''
    # assert checking 
    card = Card('G', 'H', True) # RANK ERROR 
    card = Card('T', 'F', True)  # SUIT ERROR 
    card = Card('T', 'H', 'True') #FACE UP / DOWN ERROR 
    '''

    '''
    # CARD CHECKING 
    #CREATE CARD 
    card = Card('5', 'd', True)

    #FLIP CARD 
    print('Is the card faced up? ', card.isFaceUp())
    print(card)
    card.turnOver()
    print('Is the card faced up? ', card.isFaceUp())
    print(card)
    card.turnOver()

    #RANK / SUIT METHODS 
    print('The rank of the card is ', card.getRank())
    print('The suit of the card is ', card.getSuit())

    #compare check
    card2 = Card('3', 'S', True)
    card3 = Card('5', 'D', True)

    print("CARD 1 IS ", card)
    print("CARD 2 IS ", card2)
    print("CARD 3 IS ", card3)
    print('is card1 equal to card 2? ', card == card2)
    print('is card1 equal to card 3? ', card == card3)  
    print('\nTESTING IS COMPLETE FOR THE CARD CLASS')
    '''
    
    '''
    #DECK TESTING 

    #add card into a full deck 
    deck = Deck()
    card4 = Card("A", "d", False)
    card5 = Card("A", "S", False)
    deck.addCard(card5)
    for i in range(52):
        deck.addCard(card4)
    deck.addCard(card4)

    #deal cards
    card5 = deck.dealCard()
    print(card5)
    print()

    #check size
    print('After dealing one card from a FULL deck the size is, ', deck.deckSize())
    deck.dealCard()
    print('After dealing 2 cards from a FULL deck the size is, ', deck.deckSize())

    '''

    '''
    #deal from an empty deck 
    newDeck = Deck()
    newDeck.dealCard()
    print()
    
    #check completion 
    print('is this incomplete deck complete? ', newDeck.isComplete())
    ''' 

    '''
    #create a complete deck and check it 
    ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ["S", "H", "D", "C"]
    deck5 = Deck()
    for i in ranks:
        for j in suits:
            deck5.addCard(Card(i, j, False))

    print('is this full deck complete? ', deck5.isComplete())
    print(deck5)
    print("DECK TESTING IS COMPLETE")
    '''