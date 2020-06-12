# Using Groups with Identifiers and Quantifiers

import re


# text = "My Phone number is 888-99-00000. I am a man and the child."
#
# pattern_one = r'(\d{3})-(\d{2})-(\d{5})' # 1. Grouping pattern
#
# match_one = re.search(pattern_one, text)
#
# # Print out a specific group of the returned pattern
# print(match_one.group(2))
#
# pattern_two = r'man|woman|child' # 2. Matches any of the provided string separated by pipes
#
# match_two = re.search(pattern_two, text)
# match_two_one = re.findall(pattern_two, text)

# Finds and prints all matching patterns
# for match_two_two in re.findall(pattern_two, text):
#     print(match_two_two)

# print(match_two_one)
#
# print(re.findall(r'..at', 'Tat, is Mat, LAT their Plat, inn the Phati')) # 3. Using wild cards ...
#
# print(re.findall(r'\d$', '5 Pattern ending with a number 4')) # 4. In whole string, finds pattern ending with a number
#
# print(re.findall(r'^\d', '6 Pattern starting with a number 4')) # 5. In whole string, finds pattern starting with a number
#
# print(re.findall(r'[^\d]+', '6 Pattern starting with a number 4')) # 6. Excludes any digit. + sign returns the result as joined strings as opposed to single characters
#
# print(' '.join(re.findall(r'[^!.?,]+', 'This text string has puntuations. I love it! What about you?'))) # 7. Excludes any puntuations
# print(re.findall(r'[^!.?,]+', 'This text string has puntuations. I love it! What about you?'))
#
# text = 'Only find the hyphen-words. Where are the logish-dash words?'
# print(re.findall(r'[\w]+-[\w]+', text)) # Matches a group of alpha numerics - alphanumerics

print(re.findall(r'[^Author]+', """First_Name Last_Name, Title, Extension, EmailAUTHORS:
Amy Baker, Finance Chair, x345, abaker@ourcompany.com

Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com

Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com"""))
