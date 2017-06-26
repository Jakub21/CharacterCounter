################
import source.mstr as mstr


################
def engine(target, subject):
    '''Tells how many times a character was found in text.'''
    result = 0
    for i in range(len(subject)):
        if subject[i] == target:
            result += 1
    return result


################
def e_feeder(charlist, text):
    '''Main engine feeder. Organizes data sent to engine.'''
    text_length = len(text)
    total = 0
    counter = []

    #Find total (for percentage)
    for c in charlist:
        amount = engine(c, text)
        total += amount

    #Count chars
    for c in charlist:
        amount = engine(c, text)
        percentage = 100 * (amount / total)
        percentage = round(percentage, 4)
        cdata = (amount, percentage)
        counter.append(cdata)

    #Save to dict
    result = {}
    index = 0
    for row in counter:
        result.update({charlist[index]: counter[index]})
        index += 1

    #Append total char count (only chars that are counted)
    checked_perc = 100 * (total / text_length)
    checked_perc = round(checked_perc, 4)
    total_data = (total, checked_perc)
    result.update({"total_": total_data})
    return result
