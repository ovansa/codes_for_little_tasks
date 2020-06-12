#! python3

import re, pyperclip

# Create a regex for emails

email_regex = re.compile('''

[a-zA-Z0-9_.+]+ # name
@               # symbol
[a-zA-Z0-9_.+]  # domain name
''', re.VERBOSE)

# Get text of clipboard

text = pyperclip.paste()

extracted_email = email_regex.findall(text)

print(extracted_email)

# Extract emails from clipboard

# Copy extracted emails to clipboard
