import random
def CardDecor(id):  #定义52张牌，按从小到达牌出id最小是方块2，最大是黑桃A，数字和花色用Decor和Nmu函数通过id来查询
    decors=["♦","♣","♥","♠"]
    return decors[id % 4]
def CardNum(id):
    return id//4+2
def CardNanme(id):   #牌名，展示名称的 花色和数字
    names = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    return CardDecor(id)+names[CardNum(id)-2]
def CardsKindId(idList):  #将表示牌的id的list传入，排序，判断是哪一种牌型，牌型越大，数值越大，以便后续计算分数，如果利用set函数特性可以让判断更简单
    idList.sort()
    if CardNum(idList[0]) == CardNum(idList[1]) and CardNum(idList[0]) == CardNum(idList[2]):
        return 5
    if CardDecor(idList[0]) == CardDecor(idList[1]) and CardDecor(idList[0]) == CardDecor(idList[2]) and (CardNum(idList[2]) - CardNum(idList[1])) == 1 and (CardNum(idList[1]) - CardNum(idList[0])) == 1:
        return 4
    if CardDecor(idList[0]) == CardDecor(idList[1]) and CardDecor(idList[0]) == CardDecor(idList[2]):
        return 3
    if (CardNum(idList[2]) - CardNum(idList[1])) == 1 and (CardNum(idList[1]) - CardNum(idList[0])) == 1 :
        return 2
    if CardNum(idList[0]) == CardNum(idList[1]) or CardNum(idList[1]) == CardNum(idList[2]):
        return 1
    return 0
def CardsKind(kindid):     #将牌型代码替换为展示牌型的文字
    kind=["单张","对子","顺子","同花","同花顺","豹子"]
    return kind[kindid]
if __name__ == '__main__':
    pai=list(range(0,51))  #建立牌组
    random.shuffle(pai)    #洗牌
    score=[0,0,0,0,0]
    for i in range(5):     #按顺序分牌，每人3张,打印他的牌，判断牌型，并利用牌型和pai中的最大id计算得分，得分最高者为赢家
        myPai=[pai[i*3+0],pai[i*3+1],pai[i*3+2]]
        print(f"牌友{i}的牌是:{CardNanme(myPai[0])}\t{CardNanme(myPai[1])}\t {CardNanme(myPai[2])}",end="\t")
        print(f"他的牌型是:{CardsKind(CardsKindId(myPai))}")
        score[i]=CardsKindId(myPai)*100+max(myPai)
    print(f"赢家是牌友{score.index(max(score))}")
