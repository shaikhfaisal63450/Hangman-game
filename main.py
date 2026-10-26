import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)  # 👉 for testing only, remove later

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
display = placeholder  # ⭐ keep display outside loop

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            result = "lose"

    if "_" not in display:
        game_over = True
        result = "win"

    print(stages[lives])

# ----------------------------
# ⭐ After loop ends, decide win/lose & stars
# ----------------------------
if result == "win":
    print("**************************** YOU WIN ****************************")
    if lives >= 5:
        print("🏆 Rating: ⭐⭐⭐ (Excellent!)")
    elif lives >= 3:
        print("🏆 Rating: ⭐⭐ (Good Job!)")
    else:
        print("🏆 Rating: ⭐ (Close call!)")

elif result == "lose":
    print(f"*********************** It was {chosen_word}! You lose **********************")
