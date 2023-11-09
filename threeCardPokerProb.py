# William Glass
# CS 411x Algorithms
# HW 4
# 2023-11-6

import itertools # using combinations function


## Standard Deck Suits and Ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

costPerAttempt = 1

# Dictionary to store the payouts for each hand type
handPayouts = {
    'Straight Flush': 100,
    'Three of a Kind': 30,
    'Straight': 15,
    'Flush': 5,
    'Pair': 1,
    'High Card': 0,
}

# Initialize a dictionary to store the probabilities for each hand type
handProbabilities = {    
    'Straight Flush': 0,
    'Three of a Kind': 0,
    'Straight': 0,
    'Flush': 0,
    'Pair': 0,
    'High Card': 0,
}
# Initialize a dictionary to store the returns for each hand type
handReturns = {    
    'Straight Flush': 0,
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


###################################
## Boolean Poker Hands Functions ##
###################################

# 3 cards in same suit with consecutively increasing ranks (A,Q,K acceptable)
def isStraightFlush(hand):
    if isSameSuit(hand) and isConsecutiveRank(hand):
        return True
    elif isSameSuit(hand):
            handRanks = [card.split()[0] for card in hand]  # Extract first word (ranks) from the hand
            if {'Ace', 'King', 'Queen'}.issubset(handRanks):
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
print('Calculating...\n')

# Generate all possible combinations of 3 cards from a standard deck
deck = [rank + ' of ' + suit for rank in ranks for suit in suits]
possibleHands = list(itertools.combinations(deck, 3))

# Calculate the amount each hand type appears
for hand in possibleHands:
    hand = sortHand(hand)

    if isStraightFlush(hand):
        handProbabilities['Straight Flush'] += 1
    elif isThreeOfAKind(hand):
        handProbabilities['Three of a Kind'] += 1
    elif isStraight(hand):
        handProbabilities['Straight'] += 1
    elif isFlush(hand):
        handProbabilities['Flush'] += 1
    elif isPair(hand):
        handProbabilities['Pair'] += 1
    else:
        handProbabilities['High Card'] += 1

totalHands = len(possibleHands)

# Calculate the probabilities
for handType in handProbabilities:
    handProbabilities[handType] /= totalHands

# Calculate the expected returns for each hand type
for handType in handProbabilities:
    winProbability = handProbabilities[handType]
    payout = handPayouts[handType]
    expectedReturn = (winProbability * payout)
    handReturns[handType] = expectedReturn

# Calculate the total expected return
totalExpectedReturn = sum(handReturns.values())

## PRINT SECTION OF CODE ##

# Print the probability table
print('Three Card Poker Probability Table:')
for handType, probability in handProbabilities.items():
    print(f'{handType}: {probability*100:.2f}%')

# Print the return table
print('\nThree Card Poker Return Table:')
for handType, expectedReturns in handReturns.items():
    print(f'{handType}: ${expectedReturns:.2f}')

print(f'\nTotal Expected Return: ${totalExpectedReturn:.2f}\n')
print(f'\nExpected Return After Cost: ${totalExpectedReturn - costPerAttempt:.2f}\n')

