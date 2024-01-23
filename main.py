import random
import time
from collections import Counter

from Card import Card


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
        print("." * i)  # This is to simulate CPU thinking, slows the tempo of the game
        time.sleep(1)  # Sleeping for 4 seconds


def removeMatchCards(hand, matches) -> []:
    for match in matches:
        for card in match:  # Iterate through each card in the match
            hand.remove(card)  # Remove only matching cards from hand
    return hand


def printHand(player_hand):
    print("Your hand:")
    for card in player_hand:  # Iterate over users hand and print the cards (uses the toString in card)
        print(card)


def checkCPUHand(cpu_hand, player_hand, select_card):
    matches_in_hand = [card for card in cpu_hand if card.value == select_card]  # Collect all matching cards
    if matches_in_hand:
        for card in matches_in_hand:  # Transfer all matching cards
            cpu_hand.remove(card)
            player_hand.append(card)
        return True  # Cards were found and transferred
    return False  # No matching cards were found


def check_game_over(player_hand, cpu_hand, deck) -> bool:
    if len(player_hand) <= 0 and len(cpu_hand) <= 0 and len(deck) <= 0:
        return True
    return False


if __name__ == "__main__":
    suit = ['heart', 'diamonds', 'spades', 'clubs']

    is_playing = True
    print("Welcome to Go Fish!")
    print("The goal is to collect the most 'books' (four of a kind) of cards.")
    print("Each player has 7 cards in the beginning.")
    print("Each player (you and the CPU) take turns asking for a value of a card")
    print("Guessing a card correctly will give it too you")

    while is_playing:
        # Start Go Fish Application

        stop_continue = input(
            "Would you like to continue? Type X to exit (any other character to continue): ").strip()  # Request the user's input on quitting
        print()
        if stop_continue.upper() == "X":
            is_playing = False  # Quit the application
        else:

            # Start a new game for players
            current_game_inprogress = True
            deck = [Card(card_value, card_suit) for card_value in range(1, 13) for card_suit in suit]  # Creating the
            # Deck of cards
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

                while True:  # Input validation loop for card selection
                    pos = input("It's your turn. What card would you like to ask for? 1(A), 11(J), 12(Q), 13(K) ")
                    if pos.isdigit() and 1 <= int(pos) <= 13:
                        select_card = int(pos)  # Convert input to integer
                        if checkCPUHand(cpu_hand, player_hand, select_card):
                            print("CPU had a match! You got a card.")
                        else:
                            print("Go fish!")
                            random_card = random.choice(deck)
                            player_hand.append(random_card)
                            deck.remove(random_card)
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 13.")

                printHand(player_hand)

                while True:  # Input validation loop for matches
                    matches_input = input("Do you have any matches? Type Y for yes and N for no: ")
                    if matches_input.upper() == "Y":  # Player believes they have match
                        matches = check_matches(player_hand)  # Checking for matches in player_hand
                        if matches:  # Matches were found
                            playermatches.append(matches)  # Adding matches to player matches
                            player_hand = removeMatchCards(player_hand, matches)   # Removing matched cards from player hand
                            print("You made a match! Well done.")
                            break # Break Validation
                        else:
                            print("Quit lying, you ain't got no matches!")
                            break # Break Validation
                    if matches_input.upper() == "N":  # User doesn't have matches aren't called liars
                        break  # Break Validation
                    else:
                        print("Invalid input. Please enter Y for yes or N for no.")

                cpu_turn_animation()  # Simulate CPU thinking

                if len(cpu_hand) >= 1:
                    random_card = random.choice(cpu_hand)  # Selecting a card to ask for from hand
                    select_card = int(random_card.value)  # Convert input to integer

                    print("CPU has asked if you have any " + str(select_card) + "'s?")
                    if checkCPUHand(player_hand, cpu_hand,
                                    select_card):  # Checking CPU Hand versus Player hand for the card CPU selects
                        print("You had a match! CPU got a card.")
                    else:
                        print("CPU went fishing!")
                        random_card = random.choice(deck)  # Get random card from deck
                        cpu_hand.append(random_card)  # Add random card to cpu_hand
                        deck.remove(random_card)  # Removing card from deck

                    matches = check_matches(cpu_hand)
                    if matches:
                        cpumatches.append(matches)  # Adding matches to the cpus matches list
                        cpu_hand = removeMatchCards(cpu_hand, matches)  # Removed matched cards from players hand
                        print("CPU had a match!")

                    print()
                    print("CPU's turn finished.")
                else:
                    if len(deck) > 5:
                        for i in range(1, 5):
                            random_card = random.choice(deck)  # Get random card from deck
                            cpu_hand.append(random_card)  # Add random card to cpu_hand
                            deck.remove(random_card)
                    else:
                        for i in range(1, len(deck)):
                            random_card = random.choice(deck)  # Get random card from deck
                            cpu_hand.append(random_card)  # Add random card to cpu_hand
                            deck.remove(random_card)


                if check_game_over(player_hand, cpu_hand,
                                   deck):  # Checks if the deck, cpu_hand and player_hand are empty (end of game)
                    print("Game is over, both of you and the CPU are out of cards and the deck is empty.")
                    print()

                    if len(cpumatches) > len(playermatches):  # Player has less matches than the CPU (CPU wins)
                        print("You lost!")
                        print("CPU books: " + len(cpumatches))
                        print("Player books: " + len(playermatches))
                        current_game_inprogress = False

                    elif len(playermatches) > len(cpumatches):  # Player has more matches than the CPU (player wins)
                        print("You win!")
                        print("CPU books: " + len(cpumatches))
                        print("Player books: " + len(playermatches))
                        current_game_inprogress = False

                    elif len(playermatches) == len(cpumatches):  # Player and CPU have tied (no one wins)
                        print("The game ended in a tie!")
                        print("CPU books: " + len(cpumatches))
                        print("Player books: " + len(playermatches))
                        current_game_inprogress = False

