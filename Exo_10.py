from collections import Counter



dict1 = {
    # "Full_Name" : "Walid Lemnaizi",
    "Age" : 21,
    "Skills" : 7,
    "hobbies" : 3,
    # "experience" : "3 mois",
    "Diplome" : 3
}

dict2 = {
    # "Full_Name" : "Yassine kabbaj",
    "Age" : 21,
    "Skills" : 5,
    "hobbies" : 3,
    # "experience" : "5 mois",
    "Diplome" : 2
}

def fusionner_dicts(dict1,dict2):
    return dict(Counter(dict1) + Counter(dict2))

print(fusionner_dicts(dict1,dict2))