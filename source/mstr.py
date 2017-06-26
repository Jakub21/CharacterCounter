################
def getspacing(in_str, maxamount, mod = 0):
    '''Amount of spaces that sets start of next word where it's desired'''
    spacing = ""
    r = maxamount-len(in_str) + mod
    for i in range(r):
        spacing += " "
    return spacing


################
def convert_dic_str(defines, in_dic, text):
    '''Converts dictionary to str. Output is formatted in columns.
        DictValue must be a tuple with len matching that specified in defines.
    '''
    max_spacing = defines["spacing"]
    output = "Char  Amount  Percentage\n"
    for define in in_dic:
        if define == "total_":
            continue
        spacing = getspacing(define, max_spacing)
        output += define
        output += spacing

        value0 = str(in_dic[define][0])
        spacing = getspacing(value0, max_spacing, defines["s_mod_0"])
        output += value0
        output += spacing

        output += str(in_dic[define][1])
        output += "\n"


    if defines["a_total"]:
        output += "Total"

        spacing = getspacing("Total", max_spacing)
        output += spacing
        amount = str(in_dic["total_"][0])
        output += amount

        spacing = getspacing(amount, max_spacing, defines["s_mod_0"])
        output += spacing
        output += str(in_dic["total_"][1])
        output += " chars were checked"



    return output
