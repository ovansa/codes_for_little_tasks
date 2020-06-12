# Using Identifiers and Quantifiers

import re


text = "My Phone number is 888-99-00000"

pattern_one = r'\d\d\d-\d\d-\d\d\d\d\d' # Pattern 1

phone_number_one = re.search(pattern_one, text)

print(f'From Pattern 1 - {phone_number_one.group()}') # Prints the matching pattern

pattern_two = r'\d{3}-\d{2}-\d{5}' # Pattern 2

phone_number_two = re.search(pattern_two, text)

print(f'From Pattern 2 - {phone_number_two.group()} in Position {phone_number_two.span()}')
