import random

from cheese import word_list, logo, stages

def is_valid_answer(character, picked):


    while not character.isalpha() or not len(character) == 1 or (character in picked):
        if character in picked:
            character = input("🔁 Already guessed.  Pick a different letter: ")
        elif len(character) > 1:
            character = input("⚠️ Too many characters.  Guess 1 letter: ")
        elif character.isalpha() == False:
            character = input("⚠️ Invalid character.  Pick a letter: ")
    
    return character

flag = True
testing = True

while flag:
    while testing:
        print(logo)

        choice_of_word = random.choice(word_list)

        placeholder = ""

        for letter in choice_of_word:
            placeholder += "_"

        print(placeholder)

        correct_letters = []
        picked_letters = []

        lives = 7

        testing = False

    character = input("Guess a letter: ").lower()

    guess = is_valid_answer(character, picked_letters)
    
    length1 = len(correct_letters)

    display = ""

    picked_letters.append(guess)

    for letter in choice_of_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    length2 = len(correct_letters)   

    if length1 == length2:
        lives -= 1
        print(f"❌ Your guess {guess} is not in the word.  You lose 1 life.  You now have {lives} lives remaining")
        print(stages[lives])
    else:
        print(f"✅ Correct!  The letter {guess} was in the word!")


    print(display)
    
    if display == choice_of_word:
        print(f"🎉 Congratulations!  You won!  The word was {choice_of_word}")

        continue_game = input("Would you like to play again?  Type in Y for yes or N for no: ").upper()

        if continue_game == 'Y':
            flag = True
            testing = 1
        if continue_game == 'N':
            flag = False
        
        while continue_game != 'Y' and continue_game != 'N':
            continue_game = input("Invalid answer.  Please type in Y to continue playing or N to stop: ").upper()
    elif lives == 0:
        print(f"💀 YOU LOSE.  The word was {choice_of_word}")
        continue_game = input("Would you like to play again?  Type in Y for yes or N for no: ").upper()
        
        while continue_game != 'Y' and continue_game != 'N':
            continue_game = input("Invalid answer.  Please type in Y to continue playing or N to stop: ").upper()

        if continue_game == 'Y':
            flag = True
            testing = True
        if continue_game == 'N':
            flag = False 