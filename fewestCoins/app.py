#!/bin/python3


def containsAllCoinsType(text, types):
    for t in text:
        if t not in types:
            return False
    return True

def fewestCoins(coins):
    coins_types = set(coins)
    matches = []
    for n in range(1,len(coins)):
        subString1 = coins[:n]
        subString2 = coins[-n:]
        if containsAllCoinsType(coins_types, subString1):
            matches.append(subString1)
        if containsAllCoinsType(coins_types, subString2):
            matches.append(subString2)
    return min(list(map(lambda x: len(x), matches)))

if __name__ == '__main__':
    w1 = "asdfkjeghfalawefhaef"
    print(">?>>>>?>>>>> w1 ", w1)
    result = fewestCoins(w1)
    if result == 13:
        print("YEAH!!!!!!")
    else:
        print(result)
        print("------")
        print("PUTAAAAAAAA")
