################
import os


################
#LoadDirectory
def l_dir(defines):
    '''Load every file from specified sub-directory.'''
    ################
    subdir = defines["inp_dir"]
    original_location = os.getcwd()
    input_location = original_location + subdir

    text = ""
    for filename in os.listdir(input_location):
        filepath = input_location + filename
        f = open(filepath, "r")
        text += f.read()

    output = ""
    for q in enumerate(text):
        index = q[0]
        if text[index] != "\n":
            output += text[index]
    return output


################
#WriteResult
def writestr(defines, indata):
    '''Writes data(str) to file'''
    ################
    #dictionary
    original_location = os.getcwd()
    subdir = defines["res_dir"]
    fname = defines["r_fname"]
    fdir = original_location + subdir + fname
    fstr = open(fdir, "w")
    fstr.write(indata)
