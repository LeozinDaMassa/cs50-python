def main():
    # Takes User Input
    user_input = str(input("Greeting:"))
    # Normalizes user input to all lower cases and no spaces around it
    clean_input = (user_input).strip().lower()
    # Checks which value will match with the user input
    if 'hello' in clean_input:
        print ("$0")
    elif clean_input.startswith('h') and clean_input != 'hello':
        print ("$20")
    # Possible Solution
#.  elif 'hello' not in clean_input:
        #print ('$100')
    else:
        print ('$100')

# Runs main function
main()

