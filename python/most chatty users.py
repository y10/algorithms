from collections import defaultdict

def parseLine(str:str) -> tuple[str, int]: 
    return ("username", 1)

usersToWordsMap = defaultdict(lambda: 0)
fs = open('./assets/most chatty user list.log')
n = 2

try:
    line = fs.readline()
    while line:
        (username, wordcount) = parseLine(line)
        usersToWordsMap[username] += wordcount
        line = fs.readline()

    usersToWordsList = []
    for [username, wordcount] in usersToWordsMap.items():
        usersToWordsList.append((username, wordcount))
    
    usersToWordsList.sort(key=lambda line: line[1])

    for i in range(len(usersToWordsList), 0, -1):
        (username, wordcount) = usersToWordsList[i-1]
        print(f"Most chatty user '{username}' types {wordcount} words")

        n -= 1
        if n == 0:
            break

finally:
    fs.close()
