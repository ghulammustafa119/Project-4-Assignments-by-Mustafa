# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.



# import random
# Num_Rounds = 5
# def highe_low_game():
#     score = 0
#     print("Welcome to the High-Low Game!")
#     print("-"*20)
    
#     for round_nums in range(1,Num_Rounds + 1):
#         print(f"Round {round_nums}")
#         user_num = random.randint(1,100)
#         computer_num = random.randint(1,100)
#         print(f"You Number is {user_num}")
        
#         while True:
#           user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
#           if user_guess in ["higher","lower"]:
#               break
#           else:
#               print("Please enter either 'higher' or 'lower'")
              
#         if (user_guess == "higher" and user_num > computer_num) or (user_guess == "lower" and user_num < computer_num):
#             print(f"You were right! The computer's number was {computer_num}")
#             score += 1
#         else:
#             print(f"Aww, that's incorrect. The computer's number was {computer_num}")      
#         print(f"Your score is now {score}")
#     print("Thanks for playing!")
    
#     if score == Num_Rounds:
#         print("Wow! You played perfectly! 🎉")
#     elif score >= Num_Rounds //2:
#         print("Good job, you played really well! 👍")
#     else:
#         print("Better luck next time! 😢")

# highe_low_game()



import tkinter as tk
import random

NUM_ROUNDS = 5

class HighLowGame:
    def __init__(self, master):
        self.master = master
        self.master.title("High-Low Game")
        self.setup_ui()
        self.start_game()

    def setup_ui(self):
        self.label = tk.Label(self.master, text="Welcome to the High-Low Game!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.round_label = tk.Label(self.master, font=("Helvetica", 14))
        self.round_label.pack(pady=5)

        self.number_label = tk.Label(self.master, font=("Helvetica", 14))
        self.number_label.pack(pady=5)

        self.result_label = tk.Label(self.master, font=("Helvetica", 12))
        self.result_label.pack(pady=5)

        self.score_label = tk.Label(self.master, font=("Helvetica", 12))
        self.score_label.pack(pady=5)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.higher_button = tk.Button(self.button_frame, text="Higher", command=lambda: self.make_guess("higher"))
        self.higher_button.pack(side=tk.LEFT, padx=10)

        self.lower_button = tk.Button(self.button_frame, text="Lower", command=lambda: self.make_guess("lower"))
        self.lower_button.pack(side=tk.LEFT, padx=10)

        self.restart_frame = tk.Frame(self.master)

        self.play_again_button = tk.Button(self.restart_frame, text="Play Again", command=self.start_game)
        self.exit_button = tk.Button(self.restart_frame, text="Exit", command=self.master.quit)

    def start_game(self):
        self.score = 0
        self.round = 1

        self.label.config(text="Welcome to the High-Low Game!")
        self.higher_button.config(state="normal")
        self.lower_button.config(state="normal")

        self.play_again_button.pack_forget()
        self.exit_button.pack_forget()
        self.restart_frame.pack_forget()

        self.next_round()

    def next_round(self):
        if self.round > NUM_ROUNDS:
            self.end_game()
            return

        self.user_number = random.randint(1, 100)
        self.computer_number = random.randint(1, 100)

        self.round_label.config(text=f"Round {self.round}")
        self.number_label.config(text=f"Your number is {self.user_number}")
        self.result_label.config(text="")
        self.score_label.config(text=f"Score: {self.score}")

    def make_guess(self, guess):
        if (guess == "higher" and self.user_number > self.computer_number) or \
           (guess == "lower" and self.user_number < self.computer_number):
            self.result_label.config(text=f"You were right! The computer's number was {self.computer_number}")
            self.score += 1
        else:
            self.result_label.config(text=f"Aww, that's incorrect. The computer's number was {self.computer_number}")

        self.score_label.config(text=f"Score: {self.score}")
        self.round += 1
        self.master.after(1500, self.next_round)

    def end_game(self):
        self.label.config(text="Thanks for playing!")
        self.round_label.config(text="")
        self.number_label.config(text="")
        self.higher_button.config(state="disabled")
        self.lower_button.config(state="disabled")

        if self.score == NUM_ROUNDS:
            self.result_label.config(text="Wow! You played perfectly!")
        elif self.score >= NUM_ROUNDS // 2:
            self.result_label.config(text="Good job, you played really well!")
        else:
            self.result_label.config(text="Better luck next time!")

        # Show "Play Again" and "Exit" buttons
        self.play_again_button.pack(side=tk.LEFT, padx=10)
        self.exit_button.pack(side=tk.LEFT, padx=10)
        self.restart_frame.pack(pady=10)

# Run the game
root = tk.Tk()
game = HighLowGame(root)
root.mainloop()
