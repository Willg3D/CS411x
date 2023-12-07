# William Glass
# CS 411x Algorithms
# HW6
# 2023-12-8


import itertools # using combinations function


## Standard Deck Suits and Ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

costPerAttempt = 1

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

# Initialize a dictionary to store the probabilities for each hand type
handProbabilities = { 
    'Royal Flush': 0,   
    'Straight Flush': 0,
    'Three Aces': 0,
    'Three of a Kind': 0,
    'Straight': 0,
    'Flush': 0,
    'Pair': 0,
    'High Card': 0,
}
# Initialize a dictionary to store the returns for each hand type
handReturns = {  
    'Royal Flush': 0,  
    'Straight Flush': 0,
    'Three Aces': 0,
    'Three of a Kind': 0,
    'Straight': 0,
    'Flush': 0,
    'Pair': 0,
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
##     Main Section of Code      ##
###################################


