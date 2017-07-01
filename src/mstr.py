################
def converter(defines, invar, tabmode = "normal"):
    '''Loads data from dictionary and saves to str.'''
    '''Tabmode explaination:
        Tabmode has default value "normal"
        Other valid values are: "long"
        Normal means tab with length of 4
        Long meange length is 8.
    '''
    ################
    content = []
    index = 0
    for d in invar:
        value = invar[index]
        content.append(invar[index][0])
        content.append(invar[index][1])
        content.append(invar[index][2])
        index += 1
    ################
    output = ""
    for i in range(len(content)):
        if content[i] != "__total__":
            output += str(content[i])
            if tabmode == "long":
                try:
                    if int(content[i]) < 1000:
                        output += "\t"
                except ValueError:
                    pass
        else:
            output += "Sum"
        if i % 3 == 2:
            output += "\n"
        else:
            output += "\t"
    ################
    return output
