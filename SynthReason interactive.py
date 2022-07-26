# SynthReason - Synthetic Dawn - Intelligent symbolic manipulation
# BSD 2-Clause License
# 
# Copyright (c) 2022, gw8080 - George Wagenknecht
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
import numpy
from scipy.stats import binom 
size = 100
entropy = 1.5
spread = 1
targetNgramSize = 3
thoughtSignature = 10
def process(thoughtSignature, data,file,ini):     
        with open(file, encoding='UTF-8') as f:
            text = f.read()
        string = returnWords(data,ini,thoughtSignature)
        words = convert(string)
        for word in words:
            x = len(words)
            total = ""
            n = 6
            p = 0.6
            r_values = list(range(n + 1)) 
            dist = [binom.pmf(r, n, p) for r in r_values ]
            for element in dist:
                while(x > 0 and round(len(db)/x) >0 and round(len(db)/(element*10)) < len(words) and round(len(db)/x) <len(words)):
                    if string.find(words[round(len(db)/x)]) >total.find(words[round(len(db)/x)]) and total.find(words[ round(len(db)/(element*10))]) == -1   :
                        total += string    
                    x-=1
            return total
        return ""
def convert(lst):
    return (lst.split())
def formatSentences(sync):
    sentences = sync.split('.')
    i = 0
    total = ""
    if(i < len(sentences)-1):
        total += sentences[i] + "."
        return sentences[i] + "."
    return total
def gather(user,file):
    with open(file, encoding='UTF-8') as f:
        text = f.read()
    sentences = text.split('.')
    output = ""
    i = 1
    words = convert(user)
    while(i < len(sentences)-2):
        if len(sentences[i]) > 0:
            for word in words:
                if sentences[i].find(" " + word + " ") > -1:
                    output += sentences[i] + "."
                    break
        i+=1
    return output
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
    with open("questions.conf", encoding='UTF-8') as f:
    	questions = f.readlines()
    filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
    random.shuffle(questions)
    while(True):
        print()
        user = re.sub('\W+',' ',input("USER: "))
        stat = 0
        x = 0
        random.shuffle(files)
        for file in files: 
            counter = 0
            data = convert(gather(user,file.strip()))
            sync = ""
            while(counter < size):
                counter += 1
                stat = 0
                if len(data) > 100:
                    words = convert(user)
                    db = numpy.random.uniform(len(words[random.randint(0,len(words)-1)]), len(words[random.randint(0,len(words)-1)]), len(words[random.randint(0,len(words)-1)]))
                    for element in db:        
                        check = process(round(element),data,file.strip(),random.randint(0,len(data)))
                        if check is not None:
                             sync+= check    
                    if len(convert(sync)) >= size and sync.find(".") > -1:
                            break
            print()
            syncB = formatSentences(sync)
            words = convert(syncB)  
            print("using " , file.strip() ,  " answering: " , user)
            print("AI:" ,syncB)
            f = open(filename, "a", encoding="utf8")
            f.write("\n")
            f.write("using " + file.strip() + " answering: " + user)
            f.write("\n")
            f.write(syncB)
            f.write("\n")
            f.close()
            x+=1
            if x >= spread:
                break
