# Print anagrams together in Python using List and Dictionary
# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'

def anagram_togethr(input):
    dict_obj = {}
    for i in input:
        key = "".join(sorted(i))
        if key in dict_obj:
            dict_obj[key].append(i)
        else:
            dict_obj[key] = []
            dict_obj[key].append(i)
    print(f"dict_obj: {dict_obj}")
    output = ""
    for obj in dict_obj.items():
        output = output + ' '.join(obj[1]) + ' '
    print(output)


def mirrorChars(input, k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))
    prefix = input[0:k - 1]
    suffix = input[k - 1:]
    mirror = ""
    for i in range(0, len(suffix)):
        mirror += dictChars[suffix[i]]
    print(prefix + mirror)


def default(num1, num2):
    return "Incorrect operation"


switcher = {
    1: anagram_togethr,
    2: mirrorChars
}


def switch(operation, input_to_process, k):
    if operation == 1:
        return switcher.get(operation, default)(input_to_process)
    if operation == 2:
        return switcher.get(operation, default)(input_to_process, k)


print('''You can perform operation
1. Bring all anagram together
2. mirror characters in a string
''')

if __name__ == "__main__":
    choice = int(input("Select operation from 1, 2: "))
    if choice == 1:
        input_to_process = ['cat', 'dog', 'tac', 'god', 'act']  # change as per your testcase
        switch(choice, input_to_process)
    if choice == 2:
        input_to_process = 'paradox'  # change as per your testcase
        k = 3
        switch(choice, input_to_process, k)
