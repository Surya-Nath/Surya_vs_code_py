import json
import random

class MathGame:
    def __init__(self, rounds=5):
        self.rounds = rounds
        self.score = 0

    def factorial(self, n):
        # Recursive factorial
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def play_round(self):
        num = random.randint(1, 6)
        correct_answer = self.factorial(num)
        print(f"\nRound: Factorial of {num}?")
        try:
            user_input = int(input("Your answer: "))
            if user_input == correct_answer:
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong. Correct answer is {correct_answer}")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

    def save_score(self):
        data = {"score": self.score}
        with open("score.json", "w") as f:
            json.dump(data, f)
        print("\n📂 Score saved to score.json")

    def start(self):
        print("🎮 Welcome to the Math Game!")
        for _ in range(self.rounds):
            self.play_round()
        print(f"\nFinal Score: {self.score}/{self.rounds}")
        self.save_score()


if __name__ == "__main__":
    game = MathGame(rounds=3)  # play 3 rounds
    game.start()
