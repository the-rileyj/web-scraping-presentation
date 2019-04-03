import re

with open("./basic-regex.html") as basic_regex_file:
    text = "".join(basic_regex_file.read().split("\n"))

    match = re.search(r".*<span>(.*)<\/span>.*", text)

    print(match.group(1).strip())

