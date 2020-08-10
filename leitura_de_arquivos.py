import re

def processamento_dos_dados(path_file):
    with open(path_file,'r') as manipulador:
        lista_de_dados = manipulador.readlines()

    rj_num = [int(rj_num_indice) for rj_num_indice in lista_de_dados[:][0].split() if rj_num_indice.isdigit()]
    dj_num = [int(dj_num_indice) for dj_num_indice in lista_de_dados[:][1].split() if dj_num_indice.isdigit()]
    pj_num = [int(pj_num_indice) for pj_num_indice in lista_de_dados[:][2].split() if pj_num_indice.isdigit()]
    wj_num = [int(wj_num_indice) for wj_num_indice in lista_de_dados[:][3].split() if wj_num_indice.isdigit()]
    
    #debug
    #print(rj_num)
    #print(dj_num)
    #print(pj_num)
    #print(wj_num)

    return rj_num, dj_num, pj_num, wj_num

def main():
 
    parametros = processamento_dos_dados('random_instance.txt')

    print(parametros)

if __name__ == "__main__":
    main()    