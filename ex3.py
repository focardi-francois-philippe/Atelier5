from ex1 import *
def choose_element_list(list_in_which_to_choose:list)->all:
    nombre_de_la_liste_tirer = random.randint(0,len(list_in_which_to_choose))
    nombre_retourner = list_in_which_to_choose[nombre_de_la_liste_tirer]
    return nombre_retourner
liste_alea = gen_list_random_int()
print("LISTE DE BASE :",liste_alea,"element aleatoire de la liste",choose_element_list(liste_alea))