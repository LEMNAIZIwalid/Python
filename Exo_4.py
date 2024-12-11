M_list = ['WALID' , 'YOUNNESS' , 'HOUSSAM' , 'WALID' , 'SOUFIAN' , 'SARA' , 'HOUSSAM' , 'MOHAMED']
def compte_occurences(list):
    dico = {}
    for i in list:
        if i in dico:
            dico[i] +=1
        else:
            dico[i] = 1
    return dico
print("le nombre d'occurences dans la liste est : ",compte_occurences(M_list))

