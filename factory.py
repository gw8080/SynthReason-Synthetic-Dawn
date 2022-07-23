# SynthReason - Synthetic Dawn - Intelligent symbolic manipulation
# Copyright (c) 2022, gw8080 - George Wagenknecht
# All rights reserved.
import random
from numpy import random
size = 550
targetNgramSize = 3
thoughtSignature = 10
def process(thoughtSignature, data,file,ini):     
        with open(file, encoding='UTF-8') as f:
            text = f.read()
        string = returnWords(data,ini,targetNgramSize)
        words = convert(string)
        for word in words:
            x = 1
            if x < len(word):
                totalA = ""
                while(thoughtSignature == round(len(word)/x)):
                    if len(word[x]) == 1:
                        totalA += word[x]
                        x+=1
                    if string.find(" " + word + " ") >string.find( totalA):
                        return string
        return ""
def convert(lst):
    return (lst.split())
def returnWords(dataX,pos,length):
    ngram = ""
    n = 0
    while(n < length and pos+length < len(dataX)):
        ngram += dataX[pos+n] + " "
        n+=1
    return ngram
with open("fileList.conf", encoding='UTF-8') as f:
    files = f.readlines()
    print("SynthReason - Synthetic Dawn")
    filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
    with open("fileList.conf", encoding='UTF-8') as f:
        files = f.readlines()
        for file in files:
            sync = ""
            with open(file.strip(), encoding='UTF-8') as f:
                data = convert(f.read())
            n=0
            while(n < size):
                x = random.uniform(1, 12, size=(4, 30))[0]
                for y in x:        
                    check = process(round(y),data,file.strip(),random.randint(0,len(data)))
                    if check is not None:
                        sync += check
                        n+=1
            print()
            print("AI:" ,sync)
            f = open(filename, "a", encoding="utf8")
            f.write("\n")
            f.write("using " + file.strip())
            f.write("\n")
            f.write(sync)
            f.write("\n")
            f.close()
