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
size = 100
targetNgramSize = 3
thoughtSignature = 1.4
def process(data,file,ini):     
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
    sync = ""
    with open("fileList.conf", encoding='UTF-8') as f:
        files = f.readlines()
        for file in files:
            with open(file.strip(), encoding='UTF-8') as f:
                data = convert(f.read())
            n=0
            while(n < size):
                check = process(data,file.strip(),random.randint(0,len(data)))
                if check is not None:
                    sync += check
                    n+=1
            print()
            print("AI:" ,sync)
    print("using " , file.strip() ,  " answering: " , user)
    f = open(filename, "a", encoding="utf8")
    f.write("\n")
    f.write("using " + file.strip() + " answering: " + user)
    f.write("\n")
    f.write(syncB)
    f.write("\n")
    f.close()
