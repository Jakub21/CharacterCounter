
from matplotlib import pyplot as plots


def drawplot(defines, data):
    y = []
    x = []
    for line in data:
        y.append(line[1])
        x.append(line[0])
    q = []
    for i in range(len(x)):
        q.append(i)
    plots.xticks(q, x)
    plots.plot(q, y)
    plots.show()
