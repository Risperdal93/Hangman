import random

class Hangman:
    
    def __init__(self):
        self.word_to_find = list(str(random.choice(self.possible_words)))
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find) 
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.lives = 5
        self.wrongly_guessed_letters = list()
        self.turn_count = 0
        self.error_count = 0
    
    def play(self):    
        letter = input("Type a letter here: ")
        while not letter.isalpha() or len(letter) != 1:
            print("Hey! A LETTER is required! Type a letter here: ") #
        if letter in self.correctly_guessed_letters or letter in self.wrongly_guessed_letters:
             print("Already inputed,try again !")
     
        if letter in self.word_to_find:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter
                    print(" ".join(self.correctly_guessed_letters))
            
                    
        else:
            self.wrongly_guessed_letters.append(letter)
            self.lives -= 1
            self.error_count += 1
            print(f"Incorrect! You have {self.lives} lives left.")
            print(" ".join(self.correctly_guessed_letters))
            print("Wrongly guessed letters:", " ".join(self.wrongly_guessed_letters))

       
    def start_game(self):
        print("Play HANGMAN now! Have fun BeCoders!")
        while self.lives >0:
            print(" ".join(self.correctly_guessed_letters))
            self.play()
            if "_" not in self.correctly_guessed_letters:
                self.well_played()

            if self.lives == 0:
                self.game_over()
                break
    
    """
        Printing greetings, random.word and starts game
        """
    def game_over(self):
            print("Game over... The word was:", ''.join(self.word_to_find))
    """
        Printing game over, reveals word
        """
    def well_played(self):
            print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
    """
        GG WP , reveals word
        """