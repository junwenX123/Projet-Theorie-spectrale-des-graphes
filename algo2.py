import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# charge un fichier .mtx directement dans un graphe de networkx
def load_mtx_graph(filename):
    g = nx.Graph()
    with open(filename) as f:
        lines = f.readlines()
        f.close()

    firstLineRead = False
    for l in lines:
        if(l[0] != '%'):
            if(not firstLineRead):
                parametres = l.split()
                nbNoeuds = int(parametres[0])
                for i in range(1, int(nbNoeuds)+1):
                    g.add_node(i)
                firstLineRead = True
            else:
                nodes = l.split()
                g.add_edge(int(nodes[0]), int(nodes[1]))
    return g

# crée un fichier png à partir d'un graphe networkx
def renderGraph(g, pictureName):
    plt.clf()
    nx.draw(g)
    plt.savefig("rendus/"+pictureName+".png")

def renderGraph(g, pictureName, s, zeroIndexed = True):
    if zeroIndexed:
        shift = 1
    else:
        shift = 0
    colors = []
    for node in g:
        if s.count(node-shift):
            colors.append('blue')
        else:
            colors.append('green')
    plt.clf()
    nx.draw(g, node_color = colors)
    plt.savefig("rendus/"+pictureName+".png")

# sauvegarde une matrice en un fichier .mtx
# optionnnellement, on peut mettre un commentaire
def save_matrix(mat, filename, comment = ""):
    file = open(filename, "w+")
    n = len(mat)
    m = len(mat[0])
    file.write("% fichier mtx généré par save_matrix\n")
    if(comment != ""):
        file.write("% "+comment+"\n")
    entries = 0
    for sub in mat:
        for i in sub:
            if(i!=0):
                entries+=1
    file.write(str(n)+" "+str(m)+" "+str(entries)+"\n")
    for i in range(0,n):
        for j in range(0,m):
            if(mat[i][j]!=0):
                file.write(str(i+1)+" "+str(j+1)+" "+str(mat[i][j])+"\n")
    file.close()

# charge un fichier mtx sous matrice d'adjacence 
def load_mtx_mat(filename, unoriented = True):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
    mat = None
    n, m, k = None,None,None
    firstLineRead = False
    for l in lines:
        if(l[0] != '%'):
            if(not firstLineRead):
                parametres = l.split()
                n = int(parametres[0])
                m = int(parametres[1])
                k = int(parametres[2])
                mat = [[0 for i in range(0, m)] for i in range(0,n)]
                firstLineRead = True
            else:
                nodes = l.split()
                i,j = int(nodes[0]),int(nodes[1])
                if len(nodes) == 2:
                    mat[i-1][j-1] = 1
                else:
                    mat[i-1][j-1] = int(nodes[2])
                if unoriented:
                    mat[j-1][i-1] = mat[i-1][j-1]
    return mat
    
# ici la matrice est sous forme de matrice d'adjacence
def mat_to_graph(mat):
    g = nx.Graph()
    n,m = len(mat),len(mat[0])
    for i in range(0,n):
        g.add_node(i+1)
    for i in range(0, n):
        for j in range(0,m):
            if mat[i][j] == 1:
                g.add_edge(i+1, j+1)
    return g

# renvoie la matrice laplacienne du graph de la matrice d'adjacence donnée en argument
def adj_to_lap(mat):
    n = len(mat)
    lap = [[0 for i in range(0,n)] for i in range(0,n)]
    deg = [0 for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            lap[i][j] = -mat[i][j]
            deg[i] -= lap[i][j]
    for i in range(0, n):
        lap[i][i] = deg[i]
    return lap

def affiche_matrice(mat):
    for i in range(0,len(mat)):
        for j in range(0, len(mat[i])):
            print(mat[i][j], end=" ")
        print("")

def inverse_permutation(p):
    n = len(p)
    pinv = [0 for i in range(0,n)]
    for i in range(0,n):
        pinv[p[i]] = i
    return pinv

# applique une permutation de [1,n] aux éléments d'une liste v
def applique_permutation(p, v):
    res = []
    for i in v:
        res.append(p[i])
    return res

def matrix_to_csv(mat, filename):
    file = open(filename, "w+")
    n = len(mat)
    m = len(mat[0])
    entries = 0
    for sub in mat:
        for i in sub:
            if(i!=0):
                entries+=1
    for i in range(0,n):
        for j in range(i+1,m):
            if(mat[i][j]!=0):
                file.write(str(i+1)+','+str(j+1)+"\n")
    file.close()

def complement(S, n):
    SC = []
    SS = sorted(S)
    j = 0
    for i in range(n):
        if j < len(SS) and SS[j]==i:
            j+=1
        else:
            SC.append(i)
    return SC

# only supports undirected graphs atm
# only supports 0-indexed partitions atm
def matrix_to_gml(mat, filename, partitions = None):
    n = len(mat)
    if partitions == None:
        partitions = [[0 for i in range(n)]]
    part = [0 for i in range(n)]
    for p in range(0, len(partitions)):
        for i in partitions[p]:
            part[i] = p
    tab = "  "
    file = open("exports/"+filename+".graphml", "w+")
    file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    file.write("<graphml>\n")
    p = 1
    file.write(tab*p + "<key id=\"d0\" for=\"node\" attr.name=\"groupe\" attr.type=\"int\">\n" )
    p+=1
    file.write(tab*p + "<default>-1</default>\n")
    p -= 1
    file.write(tab*p + "</key>\n")

    file.write(tab*p + "<graph id=\"G\" edgedefault=\"undirected\">\n")
    p+=1
    for i in range(0,n):
        file.write(tab*p + "<node id=\"" + str(i) + "\">\n")
        p+=1
        file.write(tab*p + "<data key=\"d0\">" + str(part[i]) + "</data>\n")
        p-=1
        file.write(tab*p+ "</node>\n") 
    for i in range(0, n):
        for j in range(i+1, n):
            if mat[i][j] != 0:
                file.write(tab*p + "<edge source=\""+ str(i) +"\" target=\""+ str(j) + "\"/>\n")
    p-=1
    file.write(tab*p + "</graph>\n")
    file.write("</graphml>")