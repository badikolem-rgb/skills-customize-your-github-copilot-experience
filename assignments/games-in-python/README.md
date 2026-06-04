
# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python that uses string handling, loops, conditionals, and user input to guide players through guessing a hidden word.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Implement the initial game setup by choosing a secret word at random and preparing the variables needed to track guesses and attempts.

#### Requirements
Completed program should:
- Use a predefined list of words
- Randomly select one word to guess
- Initialize variables for guessed letters, incorrect guesses, and maximum allowed wrong attempts
- Display the initial hidden word progress using underscores for unguessed letters

### 🛠️ Game Loop and Guess Handling

#### Description
Create the main Hangman loop to process player guesses, update the displayed progress, and detect win or lose conditions.

#### Requirements
Completed program should:
- Prompt the player to guess a single letter each turn
- Reveal correct letters in the hidden word and keep wrong guesses separate
- Reduce remaining attempts for incorrect guesses
- End the game when the word is fully guessed or the player runs out of attempts
- Show a win message if the player guesses the word, or a lose message if they fail

### 🛠️ Input Validation and Feedback

#### Description
Add user-friendly validation and feedback so the game handles repeated guesses and invalid input cleanly.

#### Requirements
Completed program should:
- Reject empty input or more than one letter
- Inform the player when a letter has already been guessed
- Continue the game without penalizing repeated valid guesses
- Display the updated progress after each turn
