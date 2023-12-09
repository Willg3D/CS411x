# William Glass
# CS 411x Algorithms
# HW6
# 2023-12-8


import itertools # using combinations function


## Standard Deck Suits and Ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

#costPerAttempt = 1

# Dictionary to store the payouts for each hand type
handPayouts = {
    'Royal Flush': 250,
    'Straight Flush': 100,
    'Three Aces': 100,
    'Three of a Kind': 30,
    'Straight': 15,
    'Flush': 5,
    'Pair': 1,
    'High Card': 0,
}


###################################
#####  Card Hands Functions   #####
###################################

def sortHand(hand):
    rankValues = {rank: index for index, rank in enumerate(ranks)}
    return sorted(hand, key=lambda card: rankValues.get(card.split()[0], len(ranks)))

def isSameSuit(hand):
    if all(card.split()[-1] == hand[0].split()[-1] for card in hand):
        return True
    else:
        return False
    
def isSameRank(hand):
    if all(card.split()[0] == hand[0].split()[0] for card in hand):
        return True
    else:
        return False

def isConsecutiveRank(hand): # must provide sorted list and only works with size 3 hand
    rankValues = {rank: index for index, rank in enumerate(ranks)}
    rankIndices = [rankValues[card.split()[0]] for card in hand]
    return rankIndices[2] - rankIndices[0] == 2 and rankIndices[1] - rankIndices[0] == 1

def determineHandType(hand):
    hand = sortHand(hand)

    if isRoyalFlush(hand):
        return 'Royal Flush'
    elif isStraightFlush(hand):
        return 'Straight Flush'
    elif isThreeAces(hand):
        return 'Three Aces'
    elif isThreeOfAKind(hand):
        return 'Three of a Kind'
    elif isStraight(hand):
        return 'Straight'
    elif isFlush(hand):
        return 'Flush'
    elif isPair(hand):
        return 'Pair'
    else:
        return 'High Card'
    
def generateAllPossibleHands():
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    return list(itertools.combinations(deck, 3))


###################################
## Boolean Poker Hands Functions ##
###################################

def isRoyalFlush(hand):
    if isSameSuit(hand):
            handRanks = [card.split()[0] for card in hand]  # Extract first word (ranks) from the hand
            if {'Ace', 'King', 'Queen'}.issubset(handRanks):
                return True

# 3 cards in same suit with consecutively increasing ranks (A,Q,K acceptable)
def isStraightFlush(hand):
    if isSameSuit(hand) and isConsecutiveRank(hand):
        return True
    else:
        return False
    
def isThreeAces(hand):
    handRanks = [card.split()[0] for card in hand]  # Extract first word (ranks) from the hand
    aceCount = handRanks.count('Ace')
    if aceCount == 3:
        return True
    else:
        return False

# 3 cards in same ranks (suite does not matter)
def isThreeOfAKind(hand):
    if isSameRank(hand):
       return True
    else:
       return False
   
# 3 cards with consecutively increasing ranks (suite does not matter) (A,Q,K acceptable)
def isStraight(hand):

    if isConsecutiveRank(hand) and not isStraightFlush(hand):
        return True
        
    handRanks = [card.split()[0] for card in hand]  # Extract first word (ranks) from the hand

    if {'Ace', 'King', 'Queen'}.issubset(handRanks):
        return True
    return False

# 3 cards in the same suit (sequence doesnt matter)
def isFlush(hand):
    if isSameSuit(hand) and not isConsecutiveRank(hand):
        return True
    else:
        return False

# 2 cards in the same rank
def isPair(hand):
    for rank in ranks:
        pair = [f'{rank} of {suit}' for suit in suits]
        if sum(card in hand for card in pair) == 2:
            return True
    return False


###################################
##   Computing Best Hold Code    ##
###################################

def calcExpectedValue(hold, remainingDeck):
    totalValue = 0
    hold = list(hold) # Ensure hold is a list for concatenation

    # Calculate how many cards need to be drawn
    holdCount = len(hold)
    numCardsToDraw = 3 - holdCount

    # Generate all possible combinations of draws from the remaining deck and store them in a list
    allPossibleDraws = list(itertools.combinations(remainingDeck, numCardsToDraw))
    possibleDrawsCount = len(allPossibleDraws)

    # Iterate over each possible draw
    for draw in allPossibleDraws:
        # Form a new hand by combining the hold with this draw
        newHand = hold + list(draw)

        handType = determineHandType(newHand)
        totalValue += handPayouts[handType]

    # Return the average value (expected value) of holding these cards
    return totalValue / possibleDrawsCount

# Creates the remaining deck based on cards in hand
def createRemainingDeck(hand):
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    for card in hand:
        deck.remove(card)
    return deck

def findBestHold(hand):
    # holds consists of all hold combinations (redrawing 0,1,2, or 3 cards)
    holds = [hand] + list(itertools.combinations(hand, 2)) + list(itertools.combinations(hand, 1)) + [()]
    remainingDeck = createRemainingDeck(hand)
    bestHold = None
    maxEv = 0

    for hold in holds:
        ev = calcExpectedValue(hold, remainingDeck)
        if ev > maxEv:
            maxEv = ev
            bestHold = hold

    return bestHold, maxEv

###################################
##     Main Section of Code      ##
###################################

sampleHands = [
    ['Ace of Spades', 'Queen of Hearts', 'King of Hearts'],  # High cards with a potential royal flush
    ['Ace of Hearts', 'Queen of Hearts', 'King of Hearts'],  # royal flush
    ['Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds'],  # Three aces
    ['2 of Clubs', '3 of Diamonds', '4 of Hearts'],  # Straight
    ['Jack of Spades', 'Jack of Clubs', 'Jack of Hearts'],  # Three of a kind, jacks
    ['9 of Hearts', '10 of Hearts', 'Jack of Hearts'],  # Flush
    ['7 of Diamonds', '8 of Diamonds', 'Jack of Diamonds'],  # High cards with a potential flush
    ['King of Clubs', 'King of Diamonds', 'Queen of Spades'],  # Pair of kings
    ['Ace of Clubs', '5 of Diamonds', '9 of Spades'],  # No obvious hand
    ['4 of Clubs', '4 of Spades', '6 of Hearts'],  # Pair of fours
]


# Analyze each sample hand
for hand in sampleHands:
    bestHold, bestEv = findBestHold(hand)
    print(f"Best hold for {hand}: {bestHold} with E[x] = {bestEv:.2f}")
