# Pig Game, a game where you roll a die, and as long as the roll isn't a one, that score gets added
# onto your total score. If the dice rolls a one, your score is reset. First to 50 wins. When you roll, you can
# choose to either roll again, or pass your turn to the next person. This can be a multiplayer or single player game.
import random


class PigGame:
    # Defines class variables.
    def __init__(self, player_count, target_score):
        self.player_count = player_count
        self.target_score = target_score

    # Creates dictionary of players, their number, and their score.
    def game_initialize(self):
        player_book = {}
        for player in range(self.player_count):
            player_book[f'Player #{player + 1}'] = 0
        return player_book

    # Checks for if the player score is greater or equal to target score to see if they won.
    def game_win(self, player_score):
        if player_score >= self.target_score:
            return 'Win'
        else:
            return 'Continue'


def main():
    # Create menu for game, initialized PigGame class, with target score and player count being filled
    print('Welcome to Pig Game!')
    player_count = int(input("How many players will be playing today?: "))
    target_score = int(input("What will be your target score?: "))
    game = PigGame(player_count, target_score)
    running = True
    player = 1
    # Create dictionary of players
    player_book = game.game_initialize()
    # While loop to keep the game running
    while running:
        # Make sure player count never exceeded defined number of players.
        if player > player_count:
            player = 1
        menu_choice = int(input(f'Player #{player}:\n'
                                '1. Roll the Dice\n'
                                '2. Pass your turn\n'
                                'What do you select?: '))
        if menu_choice == 1:
            # Use of random to generate a random dice roll.
            roll = random.randint(1, 6)
            # If a player rolls 1, their score is reset and turn is passed.
            if roll == 1:
                print("You rolled a 1! Score is reset and your turn is passed to the next player.")
                player_book[f'Player #{player}'] = 0
                player += 1
            # If roll not one, score is tallied and player can roll again or pass it.
            else:
                player_book[f'Player #{player}'] += roll
                print(f'You rolled a {roll}!, Your score is now {player_book[f'Player #{player}']}')
                win_check = game.game_win(player_book[f'Player #{player}'])
                # Check if the game has been won
                if win_check == 'Win':
                    # If won, end the game
                    print(f'Player {player} has won the Pig!')
                    break
                elif win_check == 'Continue':
                    # If not won, prints how many points are needed to win.
                    print(f'Player needs {target_score-player_book[f'Player #{player}']} point(s) to win!')
        if menu_choice == 2:
            # If turn is passed, key for other player and continue the game.
            player += 1
            print('You have passed your turn.')
            continue


if __name__ == '__main__':
    main()
