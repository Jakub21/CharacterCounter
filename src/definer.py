################
#Procedures used to load file with settings and defines


################
def getfile():
    '''Loads file with defines. This function needs improvements.'''
    ################
    fstr = open("defines", "r")
    content = fstr.read()
    index = 0
    ################
    is_tab = 0
    for q in content:
        if q == "\t":
            is_tab = 1
            break
    ################
    content = content.split("\n")
    content.remove("")
    for q in enumerate(content):
        i = q[0]
        if "#" in content[i]:
            del content[i]
    return content



################
def converter(mode, data):
    '''Converts values to types specified in loaded file.'''
    ################
    if mode == "bool":
        if data == "True":
            output = True
        elif data == "False":
            output = False
        else:
            output = "error__ConverterBoolDefine"
    ################
    if mode == "str":
        output = ""
        for word in data:
            output += word + " "
        output = output[:-1]
    ################
    if mode == "chr":
        if len(data) > 1:
            output = data[0]
        else:
            output = data
    ################
    if mode == "int":
        try:
            output = int(data)
        except:
            q = float(data)
            output = int(q)
    ################
    if mode == "flt":
        output = float(data)
    ################
    return output


################
def analyzer(instr):
    '''Checks type of variable and calls converter.'''
    ################
    valid_types = ["bool", "str", "chr", "int", "flt"]
    content = instr.split()
    if content[2] != "=":
        error = "Defines_Syntax"
    ################
    def_type = content[0]
    def_name = content[1]
    if def_type == "str":
        defvalue = content[3:]
    else:
        defvalue = content[3]
    ################
    if def_type in valid_types:
        defvalue = converter(def_type, defvalue)
    else:
        error = "Invalid_Define_Type"
    ################
    q = {def_name : defvalue,}
    return q



################
def load_def():
    '''Definer Main. Steers functions and returns ready defines dictionary.'''
    ################
    filec = getfile()
    data = {}
    for line in filec:
        definition = analyzer(line)
        data.update(definition)
    return data
