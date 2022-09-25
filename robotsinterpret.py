import requests


def parseLine(line):
    try:
        if line[0] == "#":
            return [-1] # -1 means comment, not useful to progrm
        elif line[:8] == "Disallow":
            return [0, line[10:]] # 0 is to show disallow, line[10:] gives path
        elif line[:5] == "Allow":
            return [1, line[7:]] # 1 means allow, line[7:] gives path
        elif line[:10] == "User-agent":
            return [2, line[12:]]
        else:
            return [-1]        
    except:
        return [-1]


def interpretRobots(domain):
    try:
        txt = requests.get(domain + "/robots.txt").text
        print(txt)
    except:
        print("error")
        return 1

    txt = txt.splitlines()

    # if user-agent: * and disallow:/, then leave
    isCurrentUserAgent = False

    allowed = []
    disAllowed = []

    for i in txt:
        parsedLine = parseLine(i)

        if isCurrentUserAgent:
            if parsedLine[0] == -1:
                continue
            elif parsedLine[0] == 0:
                disAllowed.append(parsedLine[1])
            elif parsedLine[0] == 1:
                allowed.append(parsedLine[1])
            elif parsedLine[0] == 2:
                if parsedLine[1] != "*":
                    break; 
        else:
            if parsedLine[0] == 2:
                if parsedLine[1] == "*":
                    isCurrentUserAgent = True

    print(allowed)
    print(disAllowed)


