import re

line = "class1.method1(param1, param2) >> Some<Thing>:"
pattern = r"(?P<cls>\w+)\.(?P<methods>[\w(), ]+)\s>>\s(?P<ret>[\w<>]+):"

matches = re.match(pattern, line)

if matches:
    print(matches.group('cls'))
    print(matches.group('methods'))
    print(matches.group('ret'))
else:
    print("No match found.")