import wordle

if __name__ == "__main__":
    while True:
        guess = wordle.GuessWord(
        w_str = input(">")
    

        )

        if guess.is_valid():
            

            guess.apply_greens()
            guess.jump_turn()
            print(wordle.GuessWord.counter)
    

