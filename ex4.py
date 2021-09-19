from ex1 import *
def extract_elements_list(extract_elements_list:list,nombre_voulu_extrait:int)->list:
    """extraits nombre_voule_extrait element de la liste aleatoirement 

    Args:
        extract_elements_list (list): liste d'element
        nombre_voulu_extrait (int): nombre d'element a extraire

    Returns:
        list: une liste d'element si nombre_voulu_extrait <= longueur de extract_elements_list sinon []
    """
    liste_retourner  =[]
    liste_copie = extract_elements_list.copy()
    if(nombre_voulu_extrait<=len(extract_elements_list)):
        for _ in range(nombre_voulu_extrait):
            nombre_de_la_liste_tirer = random.randint(0,len(liste_copie)-1)
            liste_retourner.append(liste_copie[nombre_de_la_liste_tirer])
            liste_copie.pop(nombre_de_la_liste_tirer)
    return liste_retourner
liste_alea = gen_list_random_int()
print("LISTE DE BASE :",liste_alea,"element aleatoire de la liste",extract_elements_list(liste_alea,))