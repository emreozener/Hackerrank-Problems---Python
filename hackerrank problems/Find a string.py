def count_substring(string, sub_string):
    #returns how much given sub_string occurs in given string
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

