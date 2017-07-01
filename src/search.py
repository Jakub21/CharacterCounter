################
def get_total(text, chrlist):
    amount = 0
    for c in text:
        if c in chrlist:
            amount += 1
    return amount


################
def get_amnt(text, c, merge):
    amount = 0
    for q in text:
        if merge: #Ignore case
            if q.upper() == c or q.lower() == c:
                amount += 1
        else: #Case sensitive searching
            if q == c:
                amount += 1
    return amount


################
def get_perc(total, amount):
    p = amount / total
    p *= 100
    p = round(p, 3)
    return p




################
def controller(defines, text, chrlist):
    total = get_total(text, chrlist)
    data = []
    for c in chrlist:
        c_amnt = get_amnt(text, c, defines["mergecase"])
        c_perc = get_perc(total, c_amnt)
        c_data = (c, c_amnt, c_perc)
        if defines["mergecase"]:
            if c not in defines["lowercase"]:
                data.append(c_data)
        else:
            data.append(c_data)


    ################
    if defines["incr_order"]:
        data.sort(reverse = True, key=lambda tup: tup[1])

    ################
    return data
