def main():
    # Takes User Input
    user_input = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
    # Normalizes user input to all lower cases and no spaces around it
    clean_input = (user_input).strip().lower()
    # If clean input is included in the list, return yes, if not return no
    if clean_input in ("42", "forty-two", "forty two"):
        print ("Yes")
    else:
        print ("No")
# Runs main function
main()

#:( input of forty two yields output of Yes
#   expected: "Yes"
#    actual:   "No\n"
#:( input of FoRty TwO yields output of Yes
#    expected: "Yes"
#    actual:   "No\n"
# both problems above happened because of the use of replace() instead of strip()
