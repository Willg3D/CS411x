# William Glass
# CS 411x Algorithms
# HW 4
# 2023-11-1

import itertools # using combinations function


## Standard Deck Suits and Ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Initialize a dictionary to store the probabilities for each hand
handProbabilities = {    
    'Straight Flush': 0,
    'Three of a Kind': 0,
    'Straight': 0,
    'Flush': 0,
    'Pair': 0,
    'High Card': 0,
}
# Initialize a dictionary to store the payouts for each hand
handPayouts = {
    'Straight Flush': 100,
    'Three of a Kind': 30,
    'Straight': 15,
    'Flush': 5,
    'Pair': 1,
    'High Card': 0,
}
# Initialize a dictionary to store the returns for each hand
handReturns = {    
    'Straight Flush': 0,
    'Three of a Kind': 0,
    'Straight': 0,
    'Flush': 0,
    'Pair': 0,
    'High Card': 0,
}

costPerAttempt = 1

###################################
## Boolean Poker Hands Functions ##
###################################

# 3 cards in same suit with consecutively increasing ranks
def isStraightFlush(hand):
    for suit in suits:
        for startRank in range(len(ranks) - 2):  # Check for 3 consecutive ranks
            straightFlush = [f'{ranks[startRank + i]} of {suit}' for i in range(3)]
            if all(card in hand for card in straightFlush):
                return True
    return False

# 3 cards in same ranks (suite does not matter)
def isThreeOfAKind(hand):
    for rank in ranks:
        threeOfAKind = [f'{rank} of {suit}' for suit in suits]
        if sum(card in hand for card in threeOfAKind) == 3:
            return True
    return False

# 3 cards with consecutively increasing ranks (suite does not matter) (A,Q,K acceptable)
def isStraight(hand):
    handRanks = [card.split()[0] for card in hand]  # Extract first word (ranks) from the hand

    # Check for 3 consecutive ranks
    for startRank in range(len(ranks) - 2):
        straight = [ranks[startRank + i] for i in range(3)]
        if all(rank in handRanks for rank in straight):
            if not isStraightFlush(hand):
                return True
        if {'Ace', 'King', 'Queen'}.issubset(handRanks):
            return True
    return False

# 3 cards in the same suit (sequence doesnt matter)
def isFlush(hand):
    handSuits = [card.split()[-1] for card in hand]  # Extract last word (the suit) from the hand
    
    for suit in suits:
        if handSuits.count(suit) >= 3:
            return True
    return False

# 2 cards in the same rank
def isPair(hand):
    for rank in ranks:
        threeOfAKind = [f'{rank} of {suit}' for suit in suits]
        if sum(card in hand for card in threeOfAKind) == 2:
            return True
    return False


###################################
##     Main Section of Code      ##
###################################

# Generate all possible combinations of 3 cards from a standard deck
deck = [rank + ' of ' + suit for rank in ranks for suit in suits]
possibleHands = list(itertools.combinations(deck, 3))

# Calculate the probabilities for each hand
for hand in possibleHands:
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
    expectedReturn = (winProbability * payout) - ((1 - winProbability) * costPerAttempt)
    handReturns[handType] = expectedReturn

# Calculate the total expected return
totalExpectedReturn = sum(handReturns.values())

# Print the probability table
print('Three Card Poker Probability Table:')
for handType, probability in handProbabilities.items():
    print(f'{handType}: {probability*100:.2f}%')

# Print the return table
print('\nThree Card Poker Return Table:')
for handType, ecpectedReturns in handReturns.items():
    print(f'{handType}: ${ecpectedReturns:.2f}')

print(f'\nTotal Expected Return: ${totalExpectedReturn:.2f}\n')
