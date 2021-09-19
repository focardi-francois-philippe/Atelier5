from random import randint
from ex1 import gen_list_random_int
def mix_list(list_to_mix:list)->list:
    """melange les elements d'une liste

    Args:
        list_to_mix (list): la liste a melanger

    Returns:
        list:liste mixer
    """
    new_list = list_to_mix.copy()
    liste_a_retourner = []
    for _ in range(len(new_list)):
        index_a_melanger = randint(0,len(new_list)-1)
        liste_a_retourner.append(new_list[index_a_melanger])
        new_list.pop(index_a_melanger)
    return liste_a_retourner

liste_alea = gen_list_random_int(0,10,7)
print("LISTE DE BASE:",liste_alea, mix_list(liste_alea))