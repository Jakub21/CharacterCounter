################
#Main structure


################
from src import definer
from src import fstream
from src import charlist
from src import search
from src import mstr
from src import drawer


################
def execute():
    '''Core of program.'''

    ################
    print("CharacterCounter")
    print("Loading files in input directory")


    ################
    defines = definer.load_def()
    text    = fstream.l_dir(defines)
    chrlist = charlist.getcl(defines)
    result  = search.controller(defines, text, chrlist)


    ################
    result_ptxt = mstr.converter(defines, result, "normal")
    result_ftxt = mstr.converter(defines, result, "long")


    ################
    if defines["termprint"]:
        print("Result:")
        print(result_ptxt)


    ################
    if defines["rs_tofile"]:
        print("Saving result to file")
        fstream.writestr(defines, result_ftxt)


    ################
    try:
        drawer.drawplot(defines, result)
    except KeyboardInterrupt:
        import os
        os.system("cls")
        print("CharacterCounter")
    ################
    print("Done.")
