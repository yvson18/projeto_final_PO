from leitura_de_arquivos import processamento_dos_dados
import gurobipy as gp
from gurobipy import GRB

def main():

    rj,dj,pj,wj = processamento_dos_dados('random_instance.txt')
    
    m = gp.Model("mip1")

    print(rj)
    print(dj)
    print(pj)
    print(wj)

    var_atrasos = []
    var_terminos = []
    ordem = []

    
    #CRIAÇÃO DAS VARIÁVEIS BINÁRIAS QUE DEFINEM A ORDEM DOS PEDIDOS
    i = 1
    j = 1
    aux = 1
    while(aux <=len(rj)): #Criação do nó fantasma
        decisao_ordem = m.addVar(vtype=GRB.BINARY, name='x'+str(0)+str(aux))
        ordem.append(decisao_ordem)
        aux+=1
        
    while(i <= len(rj)): #Criação dos nós das tarefas
        while(j <= len(rj)):
            if(i != j):
                decisao_ordem = m.addVar(vtype=GRB.BINARY, name='x'+str(i)+str(j))
                ordem.append(decisao_ordem)
            j+=1
        j=1
        i+=1
        
    #CRIAÇÃO DAS VARIÁVEIS INTEIRAS QUE DEFINEM AS RESTRIÇÕES DE TÉRMINO 
    i = 1
    var_terminos.append(m.addVar(ub=1, name='vy0')) #Término do nó fantasma (y0)
    while(i <= len(rj)):
        termino = m.addVar(ub=1, name ='vy'+str(i))
        termino.vType = GRB.INTEGER
        var_terminos.append(termino)
        i+=1
    
    #CRIAÇÃO DAS VARIÁVEIS INTEIRAS QUE DEFINEM AS RESTRIÇÕES DE ATRASO
    i = 1
    var_atrasos.append(m.addVar(ub=1, name='va0')) #atraso do nó fantasma (y0)
    while(i <= len(rj)):
        atraso = m.addVar(ub=1, name ='va'+str(i))
        atraso.vType = GRB.INTEGER
        var_atrasos.append(atraso)
        i+=1

    #CRIAÇÃO DAS RESTRIÇÕES DE TÉRMINO
    i = 1
    m.addConstr(var_terminos[0] >= 0, 'v0')
    m.addConstr(var_terminos[0] <= 0, 'v0')
    while(i <= len(rj)):
        m.addConstr(var_terminos[i] >= dj[i-1] + rj[i-1], 'y'+str(i))
        i+=1
    
    #CRIAÇÃO DAS RESTRIÇÕES DE ATRASO
    i = 1
    m.addConstr(var_atrasos[0] >= 0, 'a0')
    m.addConstr(var_atrasos[0] <= 0, 'a0')
    while(i <= len(rj)):
        m.addConstr(var_atrasos[i] >= var_terminos[i] - pj[i-1], 'a'+str(i))
        i+=1    
    
if __name__ == "__main__":
    main()
