# 1.문자열 뒤집기
# 문제: 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성해주세요

def reversedWord(my_string):
    wordList = list("korea") # [k,o,r,e,a]
    wordList.reverse()
    reversedWord = "".join(wordList)
    return reversedWord


todoList = ["problemsolving", "practiceguitar","swim","studygraph"]
doneList = [True,False,True,False]

# 1
num = 0
doneList = []
for x in a:
    if b[num] == True:
        doneList = [X]
    num += 1
# 2
doneList = []
for index, item in enumerate(a):
    if b[num] == True:
    doneList.append(item)

# 3
def filterDoneList(todoList, doneList):
    return [item for index, item in enumerate(todoList) if doneList[index]== True]



