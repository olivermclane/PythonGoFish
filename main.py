import random, time

from Card import Card
from collections import Counter


def check_matches(hand) -> []:
    card_counts = Counter(card.value for card in hand)  # Count card values efficiently
    matches = []
    for value, count in card_counts.items():
        if count >= 4:
            matching_cards = [card for card in hand if card.value == value]  # Find matching cards with suits
            matches.append(matching_cards)  # Add the 4 cards with their suits to the matches list

    return matches

def cpu_turn_animation():
    for i in range(4):
        print("." * i)
        time.sleep(1)


def removeMatchCards(hand, matches) -> []:
    for match in matches:
        for card in match:  # Iterate through each card in the match
            hand.remove(card)  # Remove only matching cards from hand
    return hand


def printHand(player_hand):
    print("Your hand:")
    for card in player_hand:
        print(card)
def checkCPUHand(cpu_hand, player_hand, select_card):
    matches_in_hand = [card for card in cpu_hand if card.value == select_card]  # Collect all matching cards
    if matches_in_hand:
        for card in matches_in_hand:  # Transfer all matching cards
            cpu_hand.remove(card)
            player_hand.append(card)
        return True  # Indicate that cards were found and transferred
    return False  # Indicate that no matching cards were found


def check_game_over(player_hand, cpu_hand, deck) -> bool:
    if len(player_hand) <= 0 and len(cpu_hand) <= 0 and len(deck) <= 0:
        return True
    return False



if __name__ == "__main__":
    suit = ['heart', 'diamonds', 'spades', 'clubs']

    is_playing = True

    while is_playing:
        # Start Go Fish Application
        stop_continue = input("Welcome to Go Fish! Type X to exit (any other character to continue): ").strip()  # Request the user's input on quitting
        print()
        if stop_continue.upper() == "X":
            is_playing = False  # Quit the application
        else:

            # Start a new game for players
            current_game_inprogress = True
            deck = [Card(card_value, card_suit) for card_value in range(1, 13) for card_suit in suit] # Creating the Deck of cards
            player_hand = []
            cpu_hand = []
            cpumatches = []
            playermatches = []

            # Deal Original Hand to both the CPU and Player
            while len(player_hand) < 7 and len(cpu_hand) < 7:
                random_card = random.choice(deck)  # Randomly choose a card from the deck
                player_hand.append(random_card)  # Added card to player deck
                deck.remove(random_card)  # Remove the card from player deck

                random_card = random.choice(deck)
                cpu_hand.append(random_card)
                deck.remove(random_card)

            while current_game_inprogress:
                printHand(player_hand)
                # printHand(cpu_hand)
                # Don't print the CPU's hand in normal gameplay -- Testing

                pos = input(
                    "It's your turn. What card would you like to ask for? 1 (A), 11(J), 12(Q), 13(K) ")

                if pos.isdigit() and 1 <= int(pos) <= 13:
                    select_card = int(pos)  # Convert input to integer
                    if checkCPUHand(cpu_hand, player_hand, select_card):
                        print("CPU had a match! You got a card.")
                    else:
                        print("Go fish!")
                        random_card = random.choice(deck)
                        player_hand.append(random_card)
                        deck.remove(random_card)

                printHand(player_hand)

                matches_input = input("Do you have any matches? Type Y for yes and N for no ")
                if matches_input.upper() == "Y":
                    matches = check_matches(player_hand)
                    print(matches)
                    if matches:
                        playermatches.append(matches)
                        print(matches[0][0].value)
                        player_hand = removeMatchCards(player_hand, matches)
                        print("You made a match! Well done.")
                    else:
                        print("Quit lying, you ain't got no matches!")

                cpu_turn_animation()

                random_card = random.choice(cpu_hand)
                select_card = int(random_card.value)  # Convert input to integer

                print("CPU has asked if you have any " + str(select_card) + "'s?")
                if checkCPUHand(player_hand, cpu_hand, select_card):
                    print("You had a match! CPU got a card.")
                else:
                    print("CPU went fishing!")
                    random_card = random.choice(deck)
                    cpu_hand.append(random_card)
                    deck.remove(random_card)

                matches = check_matches(cpu_hand)
                if matches:
                    cpumatches.append(matches)
                    cpu_hand = removeMatchCards(cpu_hand, matches)
                    print("CPU had a match!")

                print("\nCPU's turn finished.\n")

                if check_game_over(player_hand, cpu_hand, deck):
                    print("Game is over, both of you and the CPU are out of cards and the deck is empty.")
                    print()
                    if len(cpumatches) > len(playermatches):
                        print("You lost!")
                        current_game_inprogress = False
                    elif len(playermatches) > len(cpumatches):
                        print("You win!")
                    elif len(playermatches) == len(cpumatches):
                        print("The game ended in a tie!")





