################
#SearchScript


################
def perc(amount, total):
    '''Get percentage(var1/var2).'''
    ################
    q = amount / total
    q *= 100
    q = round(q, 4)
    return q


################
def engine(text, c):
    '''How many times char is found in text.'''
    ################
    count = 0
    for ltr in text:
        if c == ltr:
            count += 1
        #print("'", t, "'", sep = "", end = " ")
    return count


def remempty(datalist):
    '''Removes object from list when their value is (0,0).'''
    ################
    i = 0
    newlist = []
    for c in datalist:
        if c[0] != 0:
            if c[1] != 0:
                newlist.append(datalist[i])
        i += 1
    return newlist


def mergecase(datalist):
    '''Loads results from both lowerc. and upperc. letters and merges them.'''
    ################
    index = 0
    newdata = []
    for cdata in datalist:
        c = cdata[2]
        if c == c.upper():
            break #When uppercase letter is found
        uindex = index + 26
        #print("MCS", c, index, uindex, sep = "\t")
        new_amount = (datalist[index][0] + datalist[uindex][0])
        new_perc   = (datalist[index][1] + datalist[uindex][1])
        newtuple   = (new_amount, new_perc, c)
        newdata.append(newtuple)
        index += 1
    return newdata


################
def controller(defines, text, chrlist):
    '''Calls function from this file.'''
    ################
    total = 0
    for c in chrlist:
        total += engine(text, c)
        #Amount of listed chars
    ################
    datalist = []
    for c in chrlist:
        amount = engine(text, c)
        percentage = perc(amount, total)
        cdata = (amount, percentage, c)
        datalist.append(cdata)
    ################
    if defines["mergecase"]:
        datalist = mergecase(datalist)
    ################
    if defines["rem_empty"]:
        datalist = remempty(datalist)
    ################
    data = {}
    for i in range(len(datalist)):
        key = datalist[i][2]
        val = datalist[i][:-1]
        d = {key : val,}
        data.update(d)
    ################
    if defines["app_total"]:
        totaldata = (total, 100)
        data.update({"__total__" : totaldata})
    ################
    return data
