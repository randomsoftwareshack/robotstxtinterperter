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
            return [2, line[12:]] # 2 means user-agent, line[12:] gives userid
        elif line[:7].lower() == "sitemap":
            return [3, line[9:]] # 3 means sitemap, line[9:] gives path
        else:
            return [-1]        
    except:
        return [-1]

def interpretRobots(domain):
    try:
        txt = requests.get(domain + "/robots.txt" if domain[-1] != "/" else domain + "robots.txt").text.splitlines()
    except:
        return [{}, []]

    total = {}
    sitemaps = []

    userId = ""

    for i in txt:
        parsedLine = parseLine(i)

        if parsedLine[0] == 3: # 3 is sitemap, so add to sitemap
            sitemaps.append(parsedLine[1])

        if userId != "":
            if parsedLine[0] == -1: # -1 is comment/error, so just skip line
                continue
            elif parsedLine[0] == 0: # 0 means disAllowed, append to userId disAllowed
                total[userId]["disAllowed"].append(parsedLine[1])
            elif parsedLine[0] == 1: # 1 means allowed, append to userId allowed
                total[userId]["allowed"].append(parsedLine[1])
            elif parsedLine[0] == 2: # 2 means userId, so switch userIDs, create new key pair
                userId = parsedLine[1]
                total[userId] = {"allowed": [], "disAllowed": []} 
                    
        elif parsedLine[0] == 2: # again for userID, if userID isn't registered
            userId = parsedLine[1]
            total[userId] = {"allowed": [], "disAllowed": []}

    return [total, sitemaps]
