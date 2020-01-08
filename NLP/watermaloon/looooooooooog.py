from math import log

EntQuan = 0.955
ptQuan = 5 / 8
sizeQuan = 8

EntShao = 0.98
ptShao = 3 / 7
sizeShao = 7

EntYing = -1
ptYing = 0
sizeYing = 2

GenEnt = [(EntQuan, sizeQuan), (EntShao, sizeShao), (EntYing, sizeYing)]
baseEnt = 0.998


def getEnt(w):
    if (w == 0):
        result1 = 0
        result2 = 1
    else:
        result1 = w * log(w, 2)
        result2 = (1 - w) * log((1 - w), 2)
    ent = -1 * (result1 + result2)
    return w, ent


w, ent = getEnt(ptYing)
# print(w, 'ent = : ', ent)


def getNodeGain(coef, baseEnt):
    sumCoef = sum([(x * y) / 17 for [x, y] in coef])
    # print('sumCoef', sumCoef)
    result = baseEnt - sumCoef
    return result


genGainGen = getNodeGain(GenEnt, baseEnt)
print('genGainGen', genGainGen)

EntQing = 1
SizeQing = 6

EntWu = 0.918
SizeWu = 6

EntQian = 0.722
SizeQian = 5

SeEnt = [(EntQing, SizeQing), (EntWu, SizeWu), (EntQian, SizeQian)]

GainSe = getNodeGain(SeEnt, baseEnt)
# print('GainSe',GainSe)
