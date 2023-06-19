import sys

def main():
    greet = input("How you want to greet?:")
    print(cherry(greet))




def cherry(t):
    words = t.split()  # Split the sentence into words
    first_word = words[0]  # Access the first word using indexing
    first_letter = first_word[0]  # Access the first letter of the first word

    if first_letter == 'H' or first_letter == 'h':
        if first_word.lower() == 'hello':
            return("0$")
        elif first_letter.lower() == 'h':
            return("20$")
    return("100$")

if __name__ == "__main__":
    main()
