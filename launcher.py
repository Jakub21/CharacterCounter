################
from source import main
from source import getdefs


################
def launch():
    '''Call this to start program.'''
    defines = getdefs.load()
    main.getvalues(defines)


################
launch()


########
#ORD(A)     65
#ORD(Z)     90
#ORD(a)     97
#ORD(z)     122
