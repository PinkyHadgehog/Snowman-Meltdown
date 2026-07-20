from game_logic import play_game


def main():
    while True:
        play_game()

        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()

        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()