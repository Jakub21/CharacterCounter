################
#Charlist loader


################
def getcl(defines):
    '''Loads charlist from defines.'''
    ################
    output = ""
    ################
    if defines["choosencase"] == "both":
        output += defines["lowercase"]
        output += defines["uppercase"]
    elif defines["choosencase"] == "lower":
        output += defines["lowercase"]
    elif defines["choosencase"] == "upper":
        output += defines["uppercase"]
    ################
    if defines["includenums"]:
        output += defines["numberset"]
    ################
    return output
