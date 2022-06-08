def mutate_string(string, position, character):
    string = str(string)
    position = int(position)
    l_string = list()
    for i in string:
        l_string += i
    l_string[position] = character
    return "".join(l_string)

#changes character of an input to a desired input at a desired index
