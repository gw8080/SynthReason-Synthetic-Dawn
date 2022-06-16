# SynthReason - Synthetic Dawn - intelligent symbolic manipulation
# BSD 2-Clause License
# 
# Copyright (c) 2022, GeorgeFW1101 - George Wagenknecht
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import random
import re
size = 100
targetNgramSize = 3
spread = 3
def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return -1
def convert(lst):
    return (lst.split())
def formatSentences(sync):
    sentences = sync.split('.')
    i = 0
    total = ""
    while(i < len(sentences)-1):
        total += sentences[i] + "."
        i += 1
    return total
def process(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    sentences = text.split('.')
    output = ""
    sentences = sorted(sentences)
    for line in sentences:
        words = convert(user)
        for word in words:
            if line.find(" " + word + " ") > -1:
                output += line + ". "
                break
    return output
def returnWords(dataX,pos,length):
    ngram = ""
    n = 0
    while(n < length and pos+length < len(dataX)):
        ngram += dataX[pos+n] + " "
        n+=1
    return ngram
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
    print("SynthReason - Synthetic Dawn")
    filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
    while(True):
        print()
        user = re.sub('\W+',' ',input("USER: "))
        stat = 0
        x = 0
        counter = 0
        counterB = 0
        while(stat < len(convert(user)) and counterB < len(files)):
            stat = 0
            counterB += 1
            random.shuffle(files)
            for file in files: 
                sync = ""
                data = convert(process(user,file.strip()))
                db = ''.join(data)
                if len(data) > 100:
                    n = 1
                    counter = 0
                    prevA = 0
                    prevB = 0
                    n = index_of((convert(user)[random.randint(0,len(convert(user))-1)]),data)+1
                    while(n < len(data) and n > 0):
                        string = returnWords(data,n,random.randint(targetNgramSize,targetNgramSize*random.randint(1,2)))
                        stringB = returnWords(data,random.randint(1,len(data)),random.randint(1,targetNgramSize))
                        if string.find("a") + string.find("e") + string.find("i") + string.find("o") + string.find("u") == stringB.find("b") + stringB.find("c") + stringB.find("d") + stringB.find("f") + stringB.find("g") + stringB.find("h") + stringB.find("j") + stringB.find("k") + stringB.find("l") + stringB.find("m") + stringB.find("n") + stringB.find("p") + stringB.find("q") + stringB.find("r") + stringB.find("s") + stringB.find("t") + stringB.find("v") + stringB.find("w") + stringB.find("x") + stringB.find("y") + stringB.find("z"):
                            if sync.find(stringB) == -1:
                                sync += stringB
                                n+=1
                        counter += 1
                        if counter > 100:  
                            counter = 0
                            n+=1
                        if len(convert(sync)) >= size:
                            break
                    stat = 0
                    words = convert(user)
                    for word in words:
                        if sync.find(" " + word + " " ) > -1 and len(word) > 0:
                            stat+=1
                sync = formatSentences(sync)
                if len(convert(sync)) > size and stat > len(convert(user))/2.5:
                    print()                
                    print("using" ,file.strip(), "answering:", user)
                    print("AI:" ,sync)
                    f = open(filename, "a", encoding="utf8")
                    f.write("\n")
                    f.write("using " + file.strip() + " answering: " + user)
                    f.write("\n")
                    f.write(sync)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                    x+=1
                    if x >= spread:
                        break
            if x >= spread:
                break
