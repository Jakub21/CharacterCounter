################
from source import fstream, engine, mstr


################
def get_ch_list(idmin, idmax):
    '''Get list of characters with ID between idmin and idmax.'''
    result = []
    for q in range(idmax-idmin+1):
        result.append(chr(q+idmin))
    return result


################
def getvalues(defines):
    '''Main function of program.'''
    text = fstream.l_dir(defines)
    charlist = get_ch_list(defines["chr_bgn"], defines["chr_end"])

    result = engine.e_feeder(charlist, text)
    res_text = mstr.convert_dic_str(defines, result, text)

    #Print result (Simple text columns in console)
    if defines["prt_res"]:
        print(res_text)

    #Save result to file
    if defines["wrt_res"]:
        fstream.writedic(defines, res_text)


    return result
