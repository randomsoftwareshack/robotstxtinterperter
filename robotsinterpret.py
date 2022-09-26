import requests

def parseLine(line):
    

    try:
        if line[0] == "#":
            return [-1] # -1 means comment, not useful to progrm
        elif line[:8].lower() == "disallow":
            return [0, line[10:]] # 0 is to show disallow, line[10:] gives path
        elif line[:5].lower() == "allow":
            return [1, line[7:]] # 1 means allow, line[7:] gives path
        elif line[:10].lower() == "user-agent":
            return [2, line[12:]]
        elif line[:7].lower() == "sitemap":
            return [3, line[9:]]
        else:
            return [-1]        
    except:
        return [-1]

def interpretRobots(domain):
    try:
        txt = requests.get(domain + "/robots.txt" if domain[-1] != "/" else domain + "robots.txt").text.splitlines()
    except:
        return [{}, []]
    print(txt)

    # if user-agent: * and disallow:/, then leave
    sitemaps = {}

    total = {}
    sitemaps = []

    userId = ""

    for i in txt:
        parsedLine = parseLine(i)

        if parsedLine[0] == 3:
            sitemaps.append(parsedLine[1])

        if userId != "":
            if parsedLine[0] == -1:
                continue
            elif parsedLine[0] == 0:
                total[userId]["disAllowed"].append(parsedLine[1])
            elif parsedLine[0] == 1:
                total[userId]["allowed"].append(parsedLine[1])
            elif parsedLine[0] == 2:
                userId = parsedLine[1]
                total[userId] = {"allowed": [], "disAllowed": []} 
                    
        elif parsedLine[0] == 2:
            userId = parsedLine[1]
            total[userId] = {"allowed": [], "disAllowed": []}

    return [total, sitemaps]