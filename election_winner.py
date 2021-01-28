'''
Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
'''

input = ["john", "johnny", "jackie",
         "johnny", "john", "jackie",
         "jamie", "jamie", "john",
         "johnny", "jamie", "johnny",
         "john"]


# Method-1
def election_winner(input):
    dict = {}
    for i in input:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    max_vote = max(dict.values())
    output_lst = list()
    for i in dict.items():
        if i[1] == max_vote:
            output_lst.append(i[0])
    print(sorted(output_lst)[0])


if __name__ == "__main__":
    election_winner(input)
