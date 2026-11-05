# --- 1
import random

CHOICES = ["rock", "paper", "scissors"]
ROUNDS = 3
LABELS = {"player": "You win",
          "computer": "Computer wins",
          "draw": "Draw"}

TEST_MODE = True    # True = fixed computer moves
TEST_MOVES = ["scissors", "rock", "paper"]

def get_computer_choice(round_no):
    if TEST_MODE:
        return TEST_MOVES[round_no - 1]
    return random.choice(CHOICES)        # random module

# --- 2
def decide_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "player"
    return "computer"

# --- 3
def get_player_choice(round_no):
    while True:
        prompt = f"Round {round_no} - rock, paper or scissors? "
        choice = input(prompt).strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Enter rock, paper or scissors.")

# --- 4
def play_match():
    scores = {"player": 0, "computer": 0, "draw": 0}
    summary = []
    for round_no in range(1, ROUNDS + 1):
        player = get_player_choice(round_no)
        computer = get_computer_choice(round_no)
        print(f"You: {player} | Computer: {computer}")
        winner = decide_winner(player, computer)
        scores[winner] += 1
        summary.append(f"Round {round_no}: {LABELS[winner]}")

    print(" | ".join(summary))
    print(f"You {scores['player']} | Computer {scores['computer']}"
          f" | Draws {scores['draw']}")
    if scores["player"] > scores["computer"]:
        print("Result: You win the match!")
    elif scores["player"] < scores["computer"]:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")

# --- 5
def ask_play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Invalid choice. Enter y or n.")

def main():
    print("=== Rock Paper Scissors ===")
    while True:
        play_match()
        if not ask_play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
