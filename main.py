



import sys, Card
def main() -> int:
    suit = ['heart', 'diamonds', 'spades', 'clubs']

    is_playing = True
    playerhand = []
    cpuhand = []
    cpumatches = []
    playermatches = []

    deck = [Card(card_value, card_suit) for card_value in range(1, 14) for card_suit in suit]

    while (is_playing):
        # Start Go Fish Application
        print("Welcome to Go Fish! Type X to exit and C to continue.")
        stop_continue = input()  # Request the users input on quiting

        if stop_continue == "X":
            is_playing = False  # Quit the application
        else:
            # Start new game for players
            current_game_inprogress = True

            while (current_game_inprogress):
                print("Do you have any matches?") # Ask the user if they have matches
                matches_input = input()
                for card in playerhand:
                   for card in playerhand:

    return 0


if __name__ == "__main__":
    sys.exit(main())
