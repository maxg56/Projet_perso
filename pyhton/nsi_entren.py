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
def maxi (lise : List[Union[int,float]]) ->  Union[int,float, None]:
    """reshrche du maxi """
    if lise == []:
        return None
    maxs = lise[0]
    for val in  lise :
        if val > maxs :
            maxs = val 
    return maxs
def max_i(valeurs : List[Union[int,float]])->  Union[int,float, None]:
    if valeurs == [] :
        return None
    
    max_i = 0
    for i in range(len(valeurs)):
        if valeurs[max_i] < valeurs[i] :
            max_i = i
    return  max_i
#Tste
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == None
assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == 9
assert maxi([1, 1, 1, 99, 99]) == 99
assert maxi([10]) == 10
assert maxi([]) == None
assert max_i([10,2,6,8])==0
assert max_i([-1,-2,5.0]) == 2
assert max_i([]) == None



def mini (lise : List[Union[int,float]]) ->  Union[int,float, None]:
    if lise == []:
        return None
    mini = lise[0]
    for val in  lise :
        if val < mini :
            mini = val 
    return mini

def valeur_et_indice_du_mini(valeurs:List[Union[int,float]])-> Union[None,Tuple[Union[int,float],int]]:
    """rechrece le  maxi et rnvouaa  de son idise """
    if valeurs == [] :
        return None
    
    mini_i = 0
    mini = valeurs[0]
    for i, val  in enumerate(valeurs):
        if mini > val:
            mini = val 
            mini_i = i
    return mini , mini_i

def mini_i(valeurs : List[Union[int,float]])->  Union[int,float, None]:
    if valeurs ==[]:
        return None 
    mini_I =0
    for i in range(len(valeurs)):
        if valeurs[mini_I] > valeurs[i]:
            mini_I =i
    return mini_I


def tri_selection(val:List[Union[int,float]])-> List[Union[int,float]]:

    for  i in range(len(val)):
        j = mini_i(val[:i]) 
        j += i
        val[j+1],val[i] = val[j+1],val[i]
    return val

                                                  # Example usage:
values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_values = tri_selection(values)
print(sorted_values)                                           