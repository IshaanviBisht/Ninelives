import random

lives = 9

words = [
    "bloom", "gleam", "swift", "grape", "lunar",
    "quilt", "whirl", "flint", "charm", "brisk",
    "crisp", "glint", "plume", "vivid", "prism",
    "tweak", "bliss", "glaze", "hatch", "truce"
]

secret_word = random.choice(words)
clue = list('?????')
star = '\u2B50'  
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0

    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1  
while lives > 0:
    print("Clue: " + ''.join(clue))
    print('Lives left: ' + star * lives)
    guess = input('Guess a letter or the whole word: ').lower()

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print("Incorrect, you lost a life!")
        lives -= 1  

if guessed_word_correctly:
    print("You won!! The secret word was " + secret_word)
else:
    print("You lost! The secret word was " + secret_word)