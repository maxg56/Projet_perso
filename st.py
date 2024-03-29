from typing import List ,Union ,Tuple
def valeur_et_indice_du_max(valeurs:List[Union[int,float]])-> Union[None,Tuple[Union[int,float],int]]:
    """rechrece le  maxi et rnvouaa  de son idise """
    if valeurs == [] :
        return None
    
    max_i = 0
    maxi = valeurs[0]
    for i, val  in enumerate(valeurs):
        if maxi < val:
            maxi = val 
            max_i = i
    return maxi , max_i

#Tste
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == None



def maxi (lise : List[Union[int,float]]) ->  Union[int,float, None]:
    if lise == []:
        return None
    ma = lise[0]
    for val in  lise :
        if val > ma :
            ma = val 
    return ma

#Tste
assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == 9
assert maxi([1, 1, 1, 99, 99]) == 99
assert maxi([10]) == 10
assert maxi([]) == None


def max_i(valeurs : List[Union[int,float]])->  Union[int,float, None]:
    if valeurs == [] :
        return None
    
    max_i = 0
    for i, val  in range(len(valeurs)):
        if valeurs[max_i] < valeurs[i] :
            max_i = i
    return  max_i