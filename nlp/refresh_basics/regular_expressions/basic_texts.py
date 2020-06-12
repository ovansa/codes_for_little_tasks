import re

# 1.0. To match a simple text pattern
text = "All i want to say is that they don't really care about us. We want to care about you."
pattern = "care"

print(pattern in text)

# 1.1. To match a simple text pattern using regex function

match = re.search(pattern, text) # Returns the first match

print(match.span())

# 1.2. To match all occurrence of a simple string pattern

all_matches = re.findall('care', text) # Returns all matches

print(len(all_matches))

# 1.3. To get span of all matching string pattern

for match in re.finditer('care', text):
    print(match.span())
