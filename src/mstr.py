################
def converter(defines, invar):
    '''Loads data from dictionary and saves to str.'''
    ################
    content = []
    for d in invar:
        value = invar[d]
        content.append(d)
        content.append(value[0])
        content.append(value[1])
    ################
    output = ""
    for i in range(len(content)):
        if content[i] != "__total__":
            output += str(content[i])
        else:
            output += "Sum"
        if i % 3 == 2:
            output += "\n"
        else:
            output += "\t"
    ################
    return output
