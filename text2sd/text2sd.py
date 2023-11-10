""" This file containing the function needed to convert .txt file into .puml """

import re

INPUT_FILENAME = "./text2sd/sample/[Input] Sample.txt"

def count_leading_tab(line):
    """Return the number of leading tab in a string"""
    return line.lstrip().count('\t')

def property_identifier(line):
    pattern = r"\s*(?P<cls>\w+)\.(?P<method>[\w(), ]+)\s>>\s(?P<ret>[\w<>]+):?"
    matches = re.match(pattern, line)
    return matches.groupdict() if matches else None

def formatted_caller(caller, called):
    caller_prop = property_identifier(caller)
    called_prop = property_identifier(called)
    return f"{caller_prop['cls']} -> {called_prop['cls']}: {called_prop['method']}"

def formatted_return(caller, called):
    caller_prop = property_identifier(caller)
    called_prop = property_identifier(called)
    return f"{caller_prop['cls']} <-- {called_prop['cls']}: {called_prop['ret']}"

def process(file, caller_line="", called_line=""):
    print(formatted_caller(caller_line, called_line))
    print(formatted_return(caller_line, called_line))



def main():
    """ Run the program """
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        caller_line = input_file.readline()
        called_line = input_file.readline()
        print(f"caller {caller_line}")
        # caller_tab_count = count_leading_tab(caller_line)
        process(input_file, caller_line[:-1], called_line[:-1])
        # if ":" in caller_line:
        #     print(f"{caller_line[:-1]} : {caller_tab_count}")
        #     current_tab_count = caller_tab_count + 1
        #     while (current_tab_count > (caller_tab_count)):
        #         current_line = input_file.readline()
        #         current_tab_count = count_leading_tab(current_line)


if __name__ == "__main__":
    main()