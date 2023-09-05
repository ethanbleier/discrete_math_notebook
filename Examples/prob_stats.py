# Probability and Statistics
import itertools
import pprint
import random
from math import comb

def coin_toss():
    return random.choice(['Heads', 'Tails'])

def roll_dice():
    return random.randint(1, 6)

print("Probability and Statistics:")
print("Coin Toss:", coin_toss())
print("Dice Roll:", roll_dice())

k = 2
elements = [1,2,3]
num_combs = comb(len(elements), k)
print("Number of combinations:", num_combs)

combs = list(itertools.combinations(elements, k))
print("Combinations using itertools: ")
pprint.pprint(combs)

# Generate and print a sample poker hand
n_poker_cards = 52
k_poker_hand = 5
poker_hand = random.sample(range(1, n_poker_cards + 1), k_poker_hand)
print("Sample Poker Hand:", poker_hand)