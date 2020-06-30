import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r"abc")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


digit = re.compile(r"\d")
matches = digit.finditer(text_to_search)
for match in matches:
    print(match)

phone_number = re.compile(r"(\d\d\d).(\d\d\d).(\d\d\d)")
phone_number = re.compile(r"(\d\d\d)[-.](\d\d\d)[-.](\d\d\d)")
phone_number = re.compile(r"\d{3}[-.]\d{3}[-.]\d{3}")
matches = phone_number.finditer(text_to_search)
for match in matches:
    print(match)


variables = re.compile(r"\w+")
matches = variables.finditer(text_to_search)
for match in matches:
    print(match)


variables = re.compile(r"([a-z]|[A-Z])\w*")
matches = variables.finditer(text_to_search)
for match in matches:
    print(match)


with open("data.txt") as file:
    contents = file.read()

matches = phone_number.finditer(contents)
for match in matches:
    print(match)


email = re.compile(r"\w+@\w+\.com")
matches = email.finditer(contents)
for match in matches:
    print(match)
