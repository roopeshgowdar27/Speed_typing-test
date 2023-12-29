import time

def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog"
    print("Type this sentence as fast as you can:")
    print(prompt_text)
    
    input("Press Enter when you're ready to start typing...")
    start_time = time.time()
    
    user_input = input("Type the sentence: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    speed_wpm = (words_typed / time_taken) * 60
    
    print(f"\nYou typed {words_typed} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is approximately {speed_wpm:.2f} words per minute.")

typing_speed_test()
