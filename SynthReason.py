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
parameters = 75
size = 100
def convert(lst):
    return (lst.split())
def process(user,file):
    with open(file, encoding="utf8") as f:
        text = f.read()
    sentences = text.split('.')
    output = ""
    sentences = sorted(sentences)
    for line in sentences:
        words = sorted(convert(user), reverse = True)
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
            db = []
            if len(dataY) > 0:
                while(n < parameters and var < len(dataX) and var < len(dataY)):
                    var +=1
                    varA = random.randint(0,7)
                    varB = random.randint(0,7)
                    if returnWords(dataY,var,varA).find(dataX[var+varB]) > -1:
                        db.append(varA)
                        db.append(varB)
                        n+=1
                while(m < size):
                    var = random.randint(0,len(dataX)-10)
                    if var < len(dataX)-5:
                        i = len(db)-2
                        while(i > 0):
                            varA = db[i]
                            varB = db[i+1]
                            i-=1
                            if len(dataX[var+db[i+1]])> db[i]:
                                sync += returnWords(dataY,var,varB) and returnWords(dataY,var,varA)
                                break
                        m+=1
                    k += 1
                    if k > 100:
                        k = 0
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