#******************
# CMPUT 175 ASSIGNMENT 2
# BINGOTESTS.PY
# Author: LUKAS WASCHUK 
# Collaborators/References: N/A 
#******************
from bingo import Bingo, Table
from playingCards import Card, Deck
from random import randint

if __name__ == '__main__':
            # BINGO TESTS 
    '''
    # KEEP UNCOMMENT OUT FOR ALL THE TESTS BELOW 
    #create a complete deck and check it 
    ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ["S", "H", "D", "C"]
    deck5 = Deck()
    for i in ranks:
        for j in suits:
            deck5.addCard(Card(i, j, False))
    print('is the deck complete? ', deck5.isComplete())
    bingo_grid = Bingo()
    print()
    bingo_grid.populate(deck5, "C")
    '''

    '''
    # VERTICLE CHEC
    bingo_grid.search(Card('A', "S", False), False)
    bingo_grid.search(Card('2', "H", False), False)
    bingo_grid.search(Card('3', "D", False), False)
    bingo_grid.search(Card('4', "C", False), False)
    bingo_grid.search(Card('6', "S", False), False)
    '''

    '''
    # # HORI CHECK
    bingo_grid.search(Card('3', "D", False), False)
    bingo_grid.search(Card('3', "C", False), False)
    bingo_grid.search(Card('4', "H", False), False)
    bingo_grid.search(Card('4', "D", False), False)
    '''

    '''
    # #DOWN DAIG
    bingo_grid.search(Card('A', "S", False), False)
    bingo_grid.search(Card('2', "D", False), False)
    bingo_grid.search(Card('5', "D", False), False)
    bingo_grid.search(Card('7', "S", False), False)
    '''

    '''
    # UP DAIG 
    bingo_grid.search(Card('2', "S", False), False)
    bingo_grid.search(Card('3', "S", False), False)
    bingo_grid.search(Card('5', "S", False), False)
    bingo_grid.search(Card('6', "S", False), False)
    '''
    
    '''
    # FULL CHECK (UNCOMMENT EVERYTHING ABOVE) remmeber to change the game mode at the top 
    bingo_grid.search(Card('A', "H", False), False)
    bingo_grid.search(Card('A', "D", False), False)
    bingo_grid.search(Card('A', "C", False), False)
    bingo_grid.search(Card('2', "C", False), False)
    bingo_grid.search(Card('3', "H", False), False)
    bingo_grid.search(Card('5', "H", False), False)
    bingo_grid.search(Card('5', "C", False), False)
    bingo_grid.search(Card('6', "H", False), False)
    bingo_grid.search(Card('6', "D", False), False)
    bingo_grid.search(Card('6', "C", False), False)
    '''

    '''
    #CORNERS CHECK ---- REMMEBER TO CHANGE THE GAME MODE 
    bingo_grid.search(Card('A', "S", False), False)
    bingo_grid.search(Card('2', "S", False), False)
    bingo_grid.search(Card('6', "S", False), False)
    bingo_grid.search(Card('7', "S", False), False)
    '''
    '''
    print(bingo_grid)
    print('IS THIS A BINGO? ', bingo_grid.isBingo())
    '''


            # TABLE TESTS 
    '''
    ### KEEP UNCOMMENTED OUT FOR ALL THE OTHER TESTS DONT RECOMMENT 
    # creates a table and populates the bingo deck and the call deck
    game = Table()
    game.populateDeck(0, 'bingoDeck.txt')
    game.populateDeck(1, 'callingDeck_corners_Bwins.txt')
    game.dealBingo("L")
    game.displayTable()
    '''


    '''
    #calling a card, updating it and redisplaying the table (makes the called card
    # upside-down if it exists)
    card = game.callCard()
    print('called card is', card)
    game.updateTable(card, False)
    game.displayTable()
    '''

    '''
    # clear decks and shuffle them 
    game.clearTable()
    print('RESET DECKS')
    game.resetDecks()
    
    game.dealBingo("L")
    game.displayTable()
    print()
    '''

    '''
    #calling cards to maek a bingo for b
    card = Card('J', 'H', False)
    game.updateTable(card, False)

    card = Card('K', 'D', False)
    game.updateTable(card, False)

    card = Card('Q', 'H', False)
    game.updateTable(card, False)

    card = Card('6', 'S', False)
    game.updateTable(card, False)

    # checks for a winner before adding the final card for a bingo
    print('is there a winner present? ', game.isWinner())
    game.displayTable()

    card = Card('7', 'S', False)
    game.updateTable(card, False)

    # checks who won and is there is a winner after a bingo has been made 
    print('is there a winner present? ', game.isWinner())
    print('who won? ', game.whoWon())

    #shows that there is indeed a bingo 
    game.displayTable()
    '''