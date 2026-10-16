import pickle,sympy as sp
z,zb,eqs=pickle.load(open('eqs_O.pkl','rb'))
gens=[*z[1:],*zb[1:],z[0],zb[0]]
G=sp.GroebnerBasis(pickle.load(open('gb_O.pkl','rb')),*gens,order='grevlex',domain=sp.QQ_I)
for v in list(z[1:])+list(zb[1:])+[z[0]*zb[0]-1]:
    for k in range(1,9):
        if G.contains(v**k):
            print(v,'^',k,'in I'); break
    else: print(v,'NOT found up to 8')
