import json

from random import randint

import doctest


scenarios = [
    [0, 0],
    [1, 0],
    [1, 'n'],
    [2, 0],
    [2, 'n'],
    [3, 0],
    [3, 'n']
]


types = [ "General", "Cat1A", "Specialty" ]

specialties = [
  { "board": "Internal Medicine",
    "primaries": [
      "Internal Medicine"
    ],
    "subs": [
      "Addiction Medicine",
      "Adult and Pediatric Allergy and Immunology",
      "Clinical Cardiac Electrophysiology",
      "Cardiology",
      "Correctional Medicine",
      "Critical Care Medicine",
      "Endocrinology",
      "Gastroenterology",
      "Geriatric Medicine",
      "Hematology",
      "Hospice and Palliative Medicine",
      "Infectious Diseases",
      "Interventional Cardiology",
      "Nephrology",
      "Oncology",
      "Pain Medicine",
      "Pulmonary Diseases",
      "Rheumatology",
      "Sleep Medicine",
      "Sports Medicine",
      "Undersea and Hyperbaric Medicine",
    ],
    "total_required": 120,
    "cat1a_required": False
  }, 
   { "board": "Neuromusculoskeletal Medicine",
    "primaries": [
      "Neuromusculoskeletal Medicine & OMM"
    ],
    "subs": [
      "Pain Medicine",
      "Sports Medicine",
    ],
    "total_required": 150,
    "cat1a_required": False
  },
  { 
    "board": "Ophthalmology & Otolaryngology-HNS",
    "primaries": [
      "Facial Plastic Surgery",
      "Ophthalmology",
      "Otolaryngology & Facial Plastic Surgery",
      "Otolaryngology",
      "Otorhinolaryngology",
    ],
    "subs": [
      "Otolaryngic Allergy",
      "Sleep Medicine"
    ],
    "total_required": 120,
    "cat1a_required": True
  },
]

def randomBoard():
    return specialties[randint(0, 2)]

    

def aoaId():
    return str(randint(200000, 500000))

def makeReport():
    """docstring for makeReport"""
    

    

str(3)



report = { "aoa_id": "234099", "cme_facets": [ { "type": "General", "earned": 78.5, "required": 120.0, }, { "type": "Cat1A", "earned": 31.5, "required": 0.0, }, ] }

report['cme_facets'][0]

l = range(0, len(specialties))

list(range(0, len(specialties)))

print(json.dumps(report, sort_keys=True, indent=4))

def generateScenario(scenario):
    boards = specialties[:]
    for scenario in scenarios:
        print(range(0, len(boards)))
#        boardIndices = list(range(0, len(specialties)))
        print(boardIndices)
#        primaries = []
#        subs = []
#        for primary in scenario[0]:
#            board = boards.pop(randint(0, (len(boards) - 1)))
#            print(board)
            #primary = board['primaries'].pop(randint(0, len(board['primaries'] - 1))])
            #print(primary)




def randomTypes(num=2):
  return 2

print(randint(0, 9))


print(getTypes())


{
  "cme_facets": [
    
  ]
}

randint(0, 0)


l = [1, 3, 5]

sum(l)

sum([1, 3, 5])

(1/10) + (5/10) + (4/10) * 10

([randint(0, 4) for i in range(0, 4)])

def randomSegments(segmentCount=1, total=120.0, segments=[]):
    if segmentCount == 1:
        return segments.append(total)

    segment = randint(0, total)
    return randomSegments(segmentCount - 1, \
                          total - segment, \
                          segments.append(segment))


l = [5]

while len(l) < 3:
    l.append(0)


scene = [{'primary': 'Facial Plastic Surgery', 'subs': ['Sleep Medicine', 'Otolaryngic Allergy']}, {'primary': 'Otorhinolaryngology', 'subs': []}, {'primary': 'Otolaryngology', 'subs': []}]

[s for s in scene]




