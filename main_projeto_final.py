from leitura_de_arquivos import processamento_dos_dados

def main():

    rj,dj,pj,wj = processamento_dos_dados('random_instance.txt')

    print(rj)
    print(dj)
    print(pj)
    print(wj)

if __name__ == "__main__":
    main()