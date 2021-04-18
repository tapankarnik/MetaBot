from headlineGPT import createHeadline
from correctionGPT import makeCorrections
from regularGPT import regularResponse


def numberOfLines(filename):
    file = open(filename,"r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    return Counter

def main(bigprompt, inputText):
    nolines = numberOfLines(bigprompt)
    if nolines == 0:
        headline = createHeadline(inputText)
        f = open(bigprompt,"a")
        f.write(headline)
    elif nolines !=0:
        #first check if not analysis
        if inputText.startswith("analysis"):
            # f[-1]  = correction(inputText)
            makeCorrections(bigprompt,inputText)
        else:
            regularResponse(inputText)
            #do regular inference
    





if __name__ == "__main__":
    print("Welcome! what kind of chatbot do you want?")
    inp = input()
    main('bigprompt.txt', inp)
    for i in range(3):
        print("talk")
        inp = input()
        main('bigprompt.txt', inp)
