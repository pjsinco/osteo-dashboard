import json
from random import randint, uniform
import doctest
from specialties import specialties
from Report import Report 

types = [ "General", "Cat1A", "Specialty" ]

reqs = { 'normal': 120.0, 'high' : 150.0 }

CAT_1A_MAX = 30.0

def randomBoard():
    return specialties[randint(0, len(specialties))]


def aoaId():
    return str(randint(200000, 500000))


def randomCredit(maxCredits=120.0):
    return round(uniform(0.0, maxCredits) * 2) / 2


def getFacet(creditCount=0.0, cmeType="General", req=120.0):
    return {
        "type": cmeType,
        "earned": creditCount,
        "required": 120.0
    }

def hasValidSubCount(scenes, numSubs):
    count = 0
    for scene in scenes:
        for sub in scene['subs']:
            count += 1

    return count == numSubs

def sumAllSpecialties(scenes):
    count = 0
    for i in range(0, len(scenes)):
        if scenes[i]['primary'] != '':
            count += 1
        for j in range(0, len(scenes[i]['subs'])):
            if scenes[i]['subs'][j] != '':
                count += 1

    return count
        

def makeReport(numPrimaries, numSubs, req=120.0, need1a=False):

    report = {
        'aoa_id': aoaId(),
    }

    totalCredits = randomCredit(req)
    creditsList = randomCredits(numPrimaries + numSubs + 1, totalCredits, [])

    if len(creditsList) == 1:
        # No specialties, no 1a
        report['cme_facets'] = [getFacet(creditsList[0], 'General', req)]

        if need1a:
            reqCount = CAT_1A_MAX
        else:
            reqCount = 0.0

        report['cme_facets'].append(getFacet(creditsList[0], 'Cat1A', reqCount))

        if numPrimaries != 0:
            report['cme_facets'].append([getFacet(creditsList[0], 'Specialty', req)])

        return report

    elif len(creditsList) == 2:
        pass
       
    
    for credit in creditsList:
        # [15.5]
        # [15.5, 23.0]
        # [15.5, 23.0, 34.5]
        pass

    if numPrimaries == 0:
        return report

    scenes = generateScenario(numPrimaries, numSubs)


    while not hasValidSubCount(scenes, numSubs):
        scenes = generateScenario(numPrimaries, numSubs)

    if need1a:
        assert sumAllSpecialties(scenes) == numPrimaries + numSubs + 1
    else:
        assert sumAllSpecialties(scenes) == numPrimaries + numSubs
    
    totalCredits = randomCredit(req)
    creditsList = randomCredits(numPrimaries + numSubs, totalCredits, [])

    if need1a:
        assert sumAllSpecialties(scenes) + 1 == len(creditsList)
    else:
        assert sumAllSpecialties(scenes) == len(creditsList)

    for i in range(0, len(scenes)):
        #report['cme_facets'].append()
        pass
        #facets.append(getFacet(scenes[i], "specialty-" + scenes[i]))

    #facets.insert(0, aoaId())

    #return facets;
    
    return scenes
    
    #for scene in scenes:
        
    
    

def getBoardFromPrimary(primary):
    for board in specialties:
        for pri in board['primaries']:
            if pri == primary:
                return board
    return False


def getAllPrimaries():
    allPrimaries = []
    
    for board in specialties:
        for primary in board['primaries']:
            allPrimaries.append(primary)

    return allPrimaries;
    

def getPrimaries(count=1):

    allPrimaries = getAllPrimaries()

    selected = []
            
    for i in range(0, count):
        if len(allPrimaries) <= 0:
            break

        selected.append(allPrimaries.pop(randint(0, (len(allPrimaries) - 1))))

    return selected


def getSubs(primary, subsCount=1):

    if subsCount == 0:
        return []

    board = getBoardFromPrimary(primary)
    allSubs = board['subs'][:]

    selected = []

    for i in range(0, subsCount):
        if (len(allSubs) <= 0):
            break

        selected.append(allSubs.pop(randint(0, (len(allSubs) - 1))))

    return selected


def fillSubs(primaries, totalSubs=1):
    subs = []
    flatList = []
    creditList = addends(len(primaries), totalSubs, [])

    assert len(creditList) == len(primaries)
    
    for i in range(0, len(primaries)):
        primary = primaries[i]
        subs.append({
            'primary': primary,
            'subs': getSubs(primary, creditList[i])
        })
    
    return subs

def addends(count=1, total=1, addendList=[]):

    if count == 1:
        addendList.append(total) 
        return addendList

    if total == 0:
        addendList.append(total)
        return addends(count - 1, total, addendList)

    addend = randint(1, total)
    addendList.append(addend)

    return addends(count - 1,\
                   total - addend, \
                   addendList)


    
def randomCredits(creditCount=1, total=1.0, credits=[]):

    if creditCount == 1:
        credits.append(total)
        credits.sort()
        return credits

    credit = randomCredit(total)
    credits.append(credit)
    credits.sort()

    return randomCredits(creditCount - 1, \
                         total - credit, \
                         credits)
        

def generateScenario(numPrimaries, numSubs):

    if numPrimaries == 0:
        return

    primaries = getPrimaries(numPrimaries)
    chunks = fillSubs(primaries, numSubs)

    return chunks

#def makeUser(numPrimaries=0, \
#             numSubs=0, \
#             atLeast1ReqHigh=False, \
#             atLeast1Cat1A=False):
#
#    report = makeReport(numPrimaries, )
    

if __name__ == '__main__':

    maxPrimariesToTest = 3
    maxSubsToTest = 4

    report = Report(4, 3)
    print(report)

    #print(makeReport(0, 0))

    #print(randomCredits(2, 30, []))

    #print(sumAllSpecialties([{'primary': '', 'subs': []}]))

    #print(sumAllSpecialties([{'primary': 'Neuromusculoskeletal Medicine & OMM', 'subs': ['Sports Medicine']}, {'primary': 'Internal Medicine', 'subs': ['Cardiology', 'Clinical Cardiac Electrophysiology', 'Geriatric Medicine']}]))


    #print(makeReport(2, 1))

    for i in range(0, maxPrimariesToTest + 1):
        for j in range(0, maxSubsToTest + 1):
            if i == 0 and j == 1:
                break
            #print(makeReport(i, j))

    
