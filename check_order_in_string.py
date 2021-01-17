'''
Check order of character in string using OrderedDict( )
Input:
string = "engineers rock"
pattern = "er";
Output: true
Explanation:
All 'e' in the input string are before all 'r'.

Input:
string = "engineers rock"
pattern = "egr";
Output: true
Explanation:
There are two 'e' after 'g' in the input string but OrderedDict will take first 'e' so order will be maintained.

Input:
string = "engineers rock"
pattern = "gsr";
Output: false
Explanation:
There are one 'r' before 's' in the input string so Orderdict mapping will not match.
'''

from collections import OrderedDict


def check_order(pattern, input):
    o_dict = OrderedDict.fromkeys(input)
    ptr = 0
    for i in o_dict:
        if i == pattern[ptr]:
            ptr += 1
        if len(pattern) == ptr:
            return True
    else:
        return False


if __name__ == "__main__":
    string = "engineers rock"
    pattern = "gsr"
    print(check_order(pattern, string))
    # False
