import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suites = {'hearts', 'spades', 'clubs', 'diamonds'}

# A single card will be represented as a tuple (rank, suit)
# Examples:
#   ('A', 'diamonds')
#   ('2', 'spades')
#   ('1', 'diamonds') is invalid since '1' is not a valid rank

# A hand will be represented as a set of cards
# Example:
# {('A', 'spades'),
#  ('A', 'hearts'),
#  ('A', 'diamonds'),
#  ('A', 'clubs'),
#  ('5', 'spade')}

# gen_full_deck()
# Returns the set of all 52 possible cards (13 ranks x 4 suites)
def gen_full_deck():
    result = set()
    for r in ranks:
        for s in suites:
            next_card = (r, s)
            result.add(next_card)
    return result

Full_Deck = gen_full_deck()

print("Done")


# draw_hands(num_players, num_cards)
# Returns a list containing one random hand (set) for each player
def draw_hands(num_players, num_cards):
    deck_as_list = list(Full_Deck)
    random.shuffle(deck_as_list)
    result_hands = []
    for p in range(num_players):
        result_hands.append(set())
    for c in range(num_cards):
        for p in range(num_players):
            next_card = deck_as_list.pop()
            result_hands[p].add(next_card)
    return result_hands

Player_Hands = draw_hands(2,2)

print("Done")


# is_four_of_a_kind(hand)
# Returns True if hand containts four cards with the same rank
def is_four_of_a_kind(hand):
    pass

# four_of_a_kind() Test Cases
print('Four of a Kind',
      is_four_of_a_kind({('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'),
                         ('A', 'clubs'), ('5', 'spade')}))
print('Four of a Kind',
      is_four_of_a_kind({('2', 'spades'), ('A', 'hearts'), ('A', 'diamonds'),
                         ('A', 'clubs'), ('5', 'spade')}))

# is_full_house(hand)
# Returns true of hand contains 3 cards of one rank and 2 cards of another
def is_full_house(hand):
    pass

# if_full_house() Test Cases
print('Full  House',
      is_full_house({('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'),
                     ('3', 'clubs'), ('3', 'spade')}))
print('Full  House',
      is_full_house({('A', 'spades'), ('A', 'hearts'), ('K', 'diamonds'),
                     ('3', 'clubs'), ('3', 'spade')}))
print('Full  House',
      is_full_house({('3', 'spades'), ('A', 'hearts'), ('A', 'diamonds'),
                     ('3', 'clubs'), ('3', 'hearts')}))

# is_flush(hand)
# Returns True if hand contains 5 cards of the same suit
def is_flush(hand):
    pass

# is_flush(hand) Test Cases
print("Flush: ", is_flush({('A', 'spades'), ('J', 'spades'), ('Q', 'spades'),
                           ('3', 'spades'), ('4', 'spades')}))
print("Flush: ", is_flush({('A', 'spades'), ('J', 'spades'), ('Q', 'spades'),
                           ('3', 'hearts'), ('4', 'spades')}))


def rank_index(card):
    return ranks.index(card[0])

# is_straight(hand)
# Returns True if the hand contains five cards of sequential rank, not all of
# the same suit
def is_straight(hand):
    pass


print('Straight: ',
      is_straight({('10', 'spades'), ('J', 'spades'), ('Q', 'spades'),
                   ('K', 'spades'), ('A', 'spades')}))
print('Straight: ',
      is_straight({('9', 'spades'), ('10', 'spades'), ('J', 'diamonds'),
                   ('Q', 'spades'), ('K', 'spades')}))
print('Straight: ',
      is_straight({('9', 'spades'), ('10', 'spades'), ('2', 'spades'),
                   ('Q', 'spades'), ('K', 'spades')}))

# is_straight_flush(hand)
# Returns True if hand contains 5 cards of sequential rank, all of the same suit
def is_straight_flush(hand):
    pass

print('Straight Flush: ',
      is_straight_flush({('10', 'spades'), ('J', 'spades'), ('Q', 'spades'),
                         ('K', 'spades'), ('A', 'spades')}))
print('Straight Flush: ',
      is_straight_flush({('9', 'spades'), ('10', 'spades'), ('J', 'diamonds'),
                         ('Q', 'spades'), ('K', 'spades')}))
print('Straight Flush: ',
      is_straight_flush({('9', 'spades'), ('10', 'spades'), ('2', 'spades'),
                         ('Q', 'spades'), ('K', 'spades')}))

winning_hands = ['High Card',
         'One Pair',
         'Two Pair',
         'Three of a Kind',
         'Straight',
         'Flush',
         'Full House',
         'Four of a Kind',
         'Straight Flush']


def highest_hand(hand):
    if is_straight_flush(hand):
        return 'Straight Flush'
    elif is_four_of_a_kind(hand):
        return 'Four of a Kind'
    elif is_full_house(hand):
        return 'Full House'
    elif is_flush(hand):
        return 'Flush'
    elif is_straight(hand):
        return 'Straight'
    # elif is_three_of_a_kind(hand):
    #     return 'Three of a Kind'
    # elif is_two_pair(hand):
    #     return 'Two Pair'
    # elif is_one_pair(hand):
    #     return 'One Pair'
    else:
        return 'High Card'

# highest_hand(hand) Test Cases
player1 = {('10', 'spades'), ('J', 'spades'), ('Q', 'spades'),
           ('K', 'spades'), ('A', 'spades')}
player2 = {('A', 'spades'), ('J', 'spades'), ('Q', 'spades'),
           ('3', 'spades'), ('4', 'spades')}
print('HH Player 1:', highest_hand(player1))
print('HH Player 2:', highest_hand(player2))


def winner(hand1, hand2):
    hh_player1 = highest_hand(hand1)
    hh_player2 = highest_hand(hand2)
    if winning_hands.index(hh_player1) > winning_hands.index(hh_player2):
        print(f'First Player wins with a {hh_player1}')
    elif winning_hands.index(hh_player1) < winning_hands.index(hh_player2):
        print(f'Second Player wins with a {hh_player2}')
    else:
        print(f'It\'s a tie!')

winner(player1, player2)
winner(player2, player1)
