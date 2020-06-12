#! python3

import re, pyperclip

# Create a regex for phone numbers
re.compile(r'(\d\d\d)', re.VERBOSE)

email_regex = re.compiler('''
#name.+_person@(\d{2,5})?.com

[a-zA-Z0-9_.+]+ # name
@               # symbol
[a-zA-Z0-9_.+]  # domain name
''', re.VERBOSE)



# Get text of clipboard

# Extract phone number from clipboard

# Copy extracted phone to clipboard
