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
    words = convert(user)
    for line in sentences:
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
    with open("questions.conf", encoding='ISO-8859-1') as f:
    	questions = f.readlines()
    filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
    random.shuffle(questions)
    for question in questions:
        print()
        user = re.sub('\W+',' ',question)
        stat = 0
        x = 0
        counter = 0
        counterB = 0
        while(stat < len(convert(user))/2.5 and counterB < len(files)/4):
            stat = 0
            counterB += 1
            random.shuffle(files)
            for file in files:
                with open(file.strip(), encoding='ISO-8859-1') as f:
                    text = f.read()
                    dataB = convert(text)
                sync = ""
                data = convert(process(user,file.strip()))
                db = ''.join(data)
                if len(data) > 100:
                    n = 1
                    counter = 0
                    prevA = 0
                    prevB = 0
                    A = 1
                    while(n < len(data) and n > 0):
                        string = returnWords(data,random.randint(1,len(data)),random.randint(1,A))
                        if len(string) > 0:
                            n = index_of(convert(string)[random.randint(0,len(convert(string))-1)], data)+1
                            if len(string) == len(returnWords(dataB,n,random.randint(1,targetNgramSize))):
                                if sync.find(string) == -1:
                                    sync = string + sync
                                    n+=1
                                    A+=1
                        counter += 1
                        if counter > 150:
                            counter = 0
                            n+=1
                        if len(convert(sync)) >= size:
                            break
                    stat = 0
                    words = convert(user)
                    for word in words:
                        if sync.find(" " + word + " " ) > -1 and len(word) > 0:
                            stat+=1
                if len(convert(sync)) > size and stat > len(convert(user))/2.5:
                    print()                
                    syncB = formatSentences(sync)
                    print("using" ,file.strip() + "," ,"answering:", user)
                    print("AI:" ,syncB)
                    f = open(filename, "a", encoding="utf8")
                    f.write("\n")
                    f.write("using " + file.strip() + ", answering: " + user)
                    f.write("\n")
                    f.write(syncB)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                    x+=1
                    if x >= spread:
                        break
            if x >= spread:
                break

