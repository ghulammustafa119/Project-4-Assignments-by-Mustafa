# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!





def print_multiple(message, times):
    if times <= 0:
        print("Please enter a positive number of times.")
    else:
        for i in range(times):
            print(message)

def main():
    msg = input("Enter a message: ")
    times = int(input("How many times do you want to print it? "))
    print_multiple(msg, times)
    
if __name__ == "__main__":
    main()
