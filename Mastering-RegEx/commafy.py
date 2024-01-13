#!/usr/bin/python3

###
# Example of how to use a Regular Expression to insert commas in numbers
#  greater than 999 to make them easier to read
###

# Regular Expressions are not built in to Python so we import them
import re

# Prompt the user for a number to input
str_number = input("Please enter a number greater than 999.\nThe greater the number, the better: ")

# RegEx:
#  r'' - Python - notes this as a regular expression pattern
#  ^   - Beginning of string
#  \d{4,} - Match 4 or more digits
#  $   - End of string
#  Note: Python does not have a global flag to add in the pattern
regex_digits = re.compile(r'^\d{4,}$')
# RegEx:
#  ?<= - Positive Lookbehind (Check if we can match this before our current position)
#  \d  - 1 Digit
#  ?=  - Positive Lookahead (Check if we can match this after our current position)
#  ()  - Group
#  (?: - Do NOT assign a variable to this group (By default groups are assigned variables, this would be assigned to the variable '1')
#  \d{3} - Match exactly 3 digits
#  ()  - Match this group 1 or more times
#  ?!  - Negative Lookahead (Check if we do not match after our current position)
regex_comma_replace = re.compile(r'(?<=\d)(?=(?:\d{3})+(?!\d))')

if regex_digits.match(str_number) :
    # Convert the number
    # This is how we insert the commas into the string (Number)
    str_number = re.sub(regex_comma_replace, ',', str_number)

    # Output the formatted string
    print(f"{str_number}")
else :
    # the number has less than 4 digits
    print("Please enter at least 4 digits!")