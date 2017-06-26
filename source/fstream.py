################
import os


################
#LoadDirectory
def l_dir(defines):
    '''Load every file from specified sub-directory.'''
    subdir = defines["inp_dir"]
    original_location = os.getcwd()
    input_location = original_location + subdir

    output = ""
    for filename in os.listdir(input_location):
        filepath = input_location + filename
        f = open(filepath, "r")
        output += f.read() + "\n"
    return output


################
#WriteResult
def writedic(defines, dictionary):
    #dictionary
    original_location = os.getcwd()
    subdir = defines["res_dir"]
    fname = defines["o_fname"]
    fdir = original_location + subdir + fname
    fstr = open(fdir, "w")
    fstr.write(dictionary)
