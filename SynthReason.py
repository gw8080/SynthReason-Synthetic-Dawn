#	SynthReason - Synthetic Dawn - intelligent symbolic manipulation
#	Copyright (C) 2022 George Wagenknecht
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
import random
parameters = 50
size = 200
def convert(lst):
    return (lst.split())
def process(user,file):
    with open(file, encoding="utf8") as f:
        text = f.read()
    sentences = text.split('.')
    output = ""
    sentences = sorted(sentences)
    for line in sentences:
        words = sorted(convert(user), reverse = False)
        stat = 0
        for word in words:
            if line.find(word) > -1:
                output += line + " "
                break
    return output
def returnWords(dataX,pos,length):
    ngram = ""
    n = 0
    while(n < length and pos+n < len(dataX)):
        ngram += dataX[pos+n] + " "
        n+=1
    return ngram
with open("fileList.dat", encoding="utf8") as f:
    files = f.readlines()
    print("SynthReason - Synthetic Dawn")
    while(True):
        user = input("USER: ")
        filename = "Compendium#" + user + "#" + str(random.randint(0,10000000)) + ".txt"
        for file in files:       
            sync = ""
            m = 0
            n = 0
            k = 0
            var = 0
            with open(file.strip(), encoding="utf8") as x:
                data = x.read()
            dataX = convert(data)
            dataY = convert(process(user,file.strip()))
            dbA = []
            dbB = []
            dbC = []
            dbD = []
            dbE = []
            dbF = []
            dbX = []
            if len(dataY) > 0:
                while(n < parameters):
                    var = random.randint(0,len(dataY))
                    varA = random.randint(0,7)
                    varC = random.randint(0,7)
                    varD = random.randint(0,7)
                    varE = random.randint(0,7)
                    varF = random.randint(0,7)
                    if len(dataY) > var+varA and len(dataY) > var+varF:
                        prospect = convert(returnWords(dataY,var,varA))
                        if len(prospect) > 0:
                            varB = random.randint(0,len(prospect)-1)
                            if var+varA < len(dataY) and var+varB < len(dataY) and var+varC < len(dataY) and var+varD < len(dataY):
                                if len(dataY[var+varA]) == varB and len(dataY[var+varC]) == varD:
                                    dbX.append(returnWords(convert(data),var,varA))
                                    sync += returnWords(convert(data),var,varA)
                                    n+=1
                dataY = dbX
                if len(sync) > 0:
                    print()
                    print("using",file.strip())
                    print(sync)
                    f = open(filename, "a", encoding="utf8")
                    f.write("using " + file.strip())
                    f.write("\n")
                    f.write(sync)
                    f.write("\n")
                    f.write("\n")
                    f.close()