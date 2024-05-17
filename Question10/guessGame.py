import random as r


class GuessGame:
    def __init__(self):
        self.answer = r.randint(1, 100)
        self.guesses = 0

    def guess(self, num):
        self.guesses += 1
        if num == self.answer:
            return True
        elif num < self.answer:
            return 'Too low'
        else:
            return 'Too high'

    def getGuesses(self):
        return self.guesses

    def reset(self):
        self.guesses = 0
        self.answer = r.randint(1, 100)

    def getAnswer(self):
        return f'The answer was {self.answer}'


if __name__ == '__main__':
    gg = GuessGame()
    print("Welcome to the Guessing Game!")
    print("Guess a number between 1 and 100")
    print('Type 0 to exit')
    print('Type -1 to reset the game')
    print('Type -2 to get the answer')
    print('Type -3 to get the number of guesses')
    while True:
        n = int(input('Give input: '))
        if n == 0:
            break
        elif n == -1:
            gg.reset()
            print('Game reset')
        elif n == -2:
            print(gg.getAnswer())
        elif n == -3:
            print(f'Number of guesses: {gg.getGuesses()}')
        else:
            res = gg.guess(n)
            if res == True:
                print(f'Congratulations! You guessed the number in {gg.getGuesses()} guesses')
                print('to play again type -1')
                print('to exit type 0')
            else:
                print(res)

