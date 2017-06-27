################
#Main structure


################
from src import definer
from src import fstream
from src import charlist
from src import search
from src import mstr


################
def execute():
    '''Core of program.'''
    ################
    defines = definer.load_def()
    text    = fstream.l_dir(defines)
    chrlist = charlist.getcl(defines)
    result  = search.controller(defines, text, chrlist)
    res_txt = mstr.converter(defines, result)

    #If further conversion is added, call it here

    ################
    if defines["printrslt"]:
        print(res_txt)
    ################
    if defines["rs_tofile"]:
        fstream.writestr(defines, res_txt)
