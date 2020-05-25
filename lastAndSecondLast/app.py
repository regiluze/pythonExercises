def lastLetters(word):
    result = word[-2:][::-1]
    return "{first} {second}".format(first=result[0], second=result[1])



if __name__ == '__main__':
    w1 = "bat"
    kk = lastLetters(w1)
    if kk == "E L":
        print("YEAHHHH!!!")
    else:
        print(kk)
        print("----")
        print("PUTA MIERDAAAAAAAA!!!")
