from random import randint, uniform, shuffle
from specialties import specialties

REQ_PRIMARY = 30.0
REQ_SUB = 13.0
CAT_1A_MAX = 30.0

class Report(object):

    def __init__(self, \
                 numPrimaries=0, \
                 numSubs=0, \
                 need1a=False, \
                 req=120.0):

        self.report = {}
        self.numPrimaries = numPrimaries
        self.numSubs = numSubs
        self.req = req
        if need1a: 
            self.req1a = CAT_1A_MAX
        else:
            self.req1a = 0.0


        self.primaries = self._getPrimaries()
        self.chunks = self._fillSubs()

        self.creditList = \
            self._randomCredits(self.numPrimaries + 1, self._randomCredit(self.req))
        assert len(self.creditList) == self.numPrimaries + 1

        self.generalCredits = sum(self.creditList)

        if self.coinFlipIsHeads:
            self.creditList.pop(0)

        # Sanity check
        assert self._sumAllSpecialties(self.chunks) == self.numPrimaries +\
                                                       self.numSubs

        self.facets = self.generateFacets()
        
        self.report['aoa_id'] = self._aoaId()
        self.report['cme_facets'] = self.facets


    def __str__(self):
        #return str(self.specialtiesCount)
        return ', '.join([str(prop) for prop in [self.report]])


    def coinFlipIsHeads(self):
        return randint(0, 1) == 0


    def generateFacets(self):
        facets = []
        facets.append({
            'type': 'General',
            'desc': 'Total Credits',
            'earned': self.generalCredits,
            'required': self.req,
        })

        facets.append({
            'type': 'Cat1A',
            'desc': 'Category 1-A',
            'earned': self._randomCredit(self.generalCredits),
            'required': self.req1a
        })

        for i in range(0, len(self.chunks)):
            pri = self.chunks[i]['primary']
            subs = self.chunks[i]['subs']

            priCredit = self.creditList[i]

            facets.append({
                'desc': pri,
                'required': REQ_PRIMARY,
                'earned': priCredit,
                'type': 'Primary',
                'subs': []
            })
        
            if not subs:
                facets[-1]['subs'] = []
            else:
                credits = self._randomCredits(len(subs) + 1, priCredit, [])
                assert(len(credits) == len(subs) + 1)

                # Flip a coin ot decide whether the user earned credit
                # in his primary exclusive of his subs
                if self.coinFlipIsHeads():
                    credits.pop(0)                

                for j in range(0, len(subs)):
                    credit = credits[j]
                    facets[-1]['subs'].append({
                        'desc': subs[j],
                        'earned': credit,
                        'required': REQ_SUB
                    })

        return facets


    def _makeFacets(self, chunks):
        if len(chunks) == 0:
            return None

        for chunk in self.chunks:
            pass            


    def _randomCredit(self, maxCredits=120.0):
        return round(uniform(0.0, maxCredits) * 2) / 2


    def _randomCredits(self, creditCount=1, total=1.0, credits=[]):
        if creditCount == 1:
            credits.append(total)
            shuffle(credits)
            return credits
    
        credit = self._randomCredit(total)
        credits.append(credit)
        credits.sort()
    
        return self._randomCredits(creditCount - 1, \
                             total - credit, \
                             credits)
        
        
    def _aoaId(self):
        return str(randint(200000, 500000))


    def _sumAllSpecialties(self, scenes):
        count = 0
        for i in range(0, len(scenes)):
            if scenes[i]['primary'] != '':
                count += 1
            for j in range(0, len(scenes[i]['subs'])):
                if scenes[i]['subs'][j] != '':
                    count += 1

        return count


    def _hasValidSubCount(self, scenes, numSubs):
        count = 0
        for scene in scenes:
            for sub in scene['subs']:
                count += 1
    
        return count == numSubs


    def _addends(self, count=1, total=1, addendList=[]):
        if count == 1:
            addendList.append(total) 
            return addendList
    
        if total == 0:
            addendList.append(total)
            return self._addends(count - 1, total, addendList)
    
        addend = randint(1, total)
        addendList.append(addend)
    
        return self._addends(count - 1,\
                       total - addend, \
                       addendList)
    
    
    def _getBoardFromPrimary(self, primary):
        for board in specialties:
            for pri in board['primaries']:
                if pri == primary:
                    return board
        return False


    def _getAllPrimaries(self):
        allPrimaries = []
        
        for board in specialties:
            for primary in board['primaries']:
                allPrimaries.append(primary)
    
        return allPrimaries;


    def _getPrimaries(self):
    
        allPrimaries = self._getAllPrimaries()
    
        selected = []
                
        for i in range(0, self.numPrimaries):
            if len(allPrimaries) <= 0:
                break
    
            selected.append(allPrimaries.pop(randint(0, (len(allPrimaries) - 1))))
    
        return selected


    def _getSubs(self, primary, subsCount=1):
    
        if subsCount == 0:
            return []
    
        board = self._getBoardFromPrimary(primary)
        allSubs = board['subs'][:]
    
        selected = []
    
        for i in range(0, subsCount):
            if (len(allSubs) <= 0):
                break
    
            selected.append(allSubs.pop(randint(0, (len(allSubs) - 1))))
    
        return selected
    
    
    def _fillSubs(self):
        subs = []
        flatList = []
        creditList = self._addends(len(self.primaries), self.numSubs, [])
    
        assert len(creditList) == len(self.primaries)
        
        for i in range(0, len(self.primaries)):
            primary = self.primaries[i]
            subs.append({
                'primary': primary,
                'subs': self._getSubs(primary, creditList[i])
            })
        
        return subs

