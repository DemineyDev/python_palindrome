# Program that checks whether a word input by the user is a palindrome
print('***HELLO USER***')
print("Let's check if your word is a palindrome")
user_word = input("Please enter your word: ")   #Get a string from the user input

def check_palindrome(str):    # Function that checks if the word is a palindrome
    str_list = list(str)     # Convert the string to a list
    str_list.reverse()      # Reverse the list in place
    reversed = "".join(str_list)    # Join the reversed list into a string
    if reversed.lower() == str.lower():    # Compare the two strings using if statement
        return "Your word is a palindrome"
    else:
        return "Your word is not a palindrome"

print(check_palindrome(user_word))    # Function works as expected