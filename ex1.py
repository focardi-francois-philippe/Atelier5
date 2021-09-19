import random
def gen_list_random_int(int_binf=0,int_bsup=10,nombres_de_chiffre=10)->list:
    """genere une liste avec des nombres aleatoire

    Args:
        int_binf (int, optional): nombre minimum. Defaults to 0.
        int_bsup (int, optional): nombre maximum. Defaults to 10.
        nombres_de_chiffre (int, optional): nombres de chiffre voulu dans la liste . Defaults to 10.

    Returns:
        list: liste retourner avec des nombres compris entre int_binf et (int_bsup exclu)
    """
    list_nombre_retourner = []
    for i in range(nombres_de_chiffre):
        nombre = random.randint(int_binf,int_bsup)
        list_nombre_retourner.append(nombre)
    return list_nombre_retourner
