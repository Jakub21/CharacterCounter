################
def load():
    '''Defines are loaded from here. Call anytime you need them.'''
    defines = {
        #LOADING FILES
        #Directory
        "inp_dir" : "\\input\\",

        #ENGINE
        #ASCII ID of first and last chars
        "chr_bgn" : 97,  #'a'
        "chr_end" : 122, #'z'

        #SAVING RESULT
        #Save result to file
        "wrt_res" : True,
        #Output location
        "res_dir" : "\\result\\",
        "o_fname" : "result.txt",

        #PROCESSING RESULT TEXT
        #Append total chars to result-text
        "a_total" : True,
        #Amount of spacing in result text
        "spacing" : 6,
        "s_mod_0" : 2,

        #PRINT RESULT ON SCREEN
        #Print text
        "prt_res" : True,
    }
    return defines
