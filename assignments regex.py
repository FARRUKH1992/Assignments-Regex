import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Regex pattern to extract all valid emails
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Extract all emails
emails = re.findall(pattern, text)

# Filter out emails from exclude.com
filtered_emails = [email for email in emails if not email.endswith('@exclude.com')]

print(filtered_emails)