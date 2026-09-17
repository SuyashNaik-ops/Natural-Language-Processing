import re

email = input("Enter Email: ")
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

phone = input("\nEnter Phone Number: ")
phone_pattern = r'^[6-9][0-9]{9}$'

if re.fullmatch(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

date = input("\nEnter Date (DD/MM/YYYY): ")
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/][0-9]{4}$'

if re.fullmatch(date_pattern, date):
    print("Valid Date")
else:
    print("Invalid Date")

url = input("\nEnter URL: ")
url_pattern = r'^(https?://)?(www\.)?[A-Za-z0-9-]+\.[A-Za-z]{2,}(/[A-Za-z0-9._/-]*)?$'

if re.fullmatch(url_pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")

hashtag = input("\nEnter Hashtag: ")
hashtag_pattern = r'^#[A-Za-z0-9_]+$'

if re.fullmatch(hashtag_pattern, hashtag):
    print("Valid Hashtag")
else:
    print("Invalid Hashtag")


print("\n------ DFA SIMULATION ------")

binaries = input("Enter Binary Strings (comma separated): ").split(",")

for binary in binaries:

    binary = binary.strip()
    state = "q0"

    for symbol in binary:

        if state == "q0":
            if symbol == "0":
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if symbol == "0":
                state = "q1"
            else:
                state = "q2"

        elif state == "q2":
            if symbol == "0":
                state = "q1"
            else:
                state = "q0"

    print(binary, ":", "Accepted" if state == "q2" else "Rejected")


print("\n------ NFA SIMULATION ------")

binaries = input("Enter Binary Strings (comma separated): ").split(",")

transition = {
    "q0": {"0": {"q0", "q1"}, "1": {"q0"}},
    "q1": {"0": set(), "1": {"q2"}},
    "q2": {"0": set(), "1": set()}
}

for binary in binaries:

    binary = binary.strip()
    states = {"q0"}

    for symbol in binary:

        next_states = set()

        for state in states:
            next_states.update(transition[state][symbol])

        states = next_states

    print(binary, ":", "Accepted" if "q2" in states else "Rejected")


print("\n------ LIMITATION ------")
print("Regular Expressions, DFA and NFA can recognize only Regular Languages.")
print("They cannot recognize nested structures.")
print("Examples: ((())), (()()), <html><body></body></html>")
print("Nested structures require Context-Free Grammar (CFG) and Pushdown Automata (PDA).")