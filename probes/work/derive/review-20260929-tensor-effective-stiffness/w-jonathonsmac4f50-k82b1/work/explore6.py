import sympy as sp, itertools
R=sp.Rational
# so(3) generators on R^3
def gen(a):
    G=sp.zeros(3)
    for i in range(3):
        for j in range(3):
            G[i,j]=-sp.LeviCivita(a,i,j)
    return G
Gs=[gen(a) for a in range(3)]
I3=sp.eye(3)
def kron3(A,B,C): return sp.kronecker_product(A,sp.kronecker_product(B,C))
Ltot=[kron3(g,I3,I3)+kron3(I3,g,I3)+kron3(I3,I3,g) for g in Gs]
Cas=-sum((L*L for L in Ltot),sp.zeros(27))   # eigenvalue J(J+1)
# subspace S: y_ij q_k with y sym traceless: build basis vectors as 27-vectors
def vec(y,q):
    return sp.Matrix([y[i,j]*q[k] for i in range(3) for j in range(3) for k in range(3)])
# helicity tensors at q=z
z=sp.Matrix([0,0,1])
ys={'0':sp.diag(-1,-1,2),'1':sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),'2':sp.diag(1,-1,0)}
# projectors onto J eigenspaces of Cas on all 27-dim, then evaluate |P_J v|^2 for v=vec(y,z)
ev=Cas.eigenvals(); print(ev)
res={}
for J in (1,2,3):
    # projector via Lagrange interpolation in Cas on eigenvalue set
    lam=J*(J+1); P=sp.eye(27)
    for mu in ev:
        if mu!=lam: P=P*(Cas-mu*sp.eye(27))/(lam-mu)
    P=sp.simplify(P)
    row=[]
    for m,y in ys.items():
        v=vec(y,z); nr=(v.T*v)[0]; pj=P*v
        row.append(sp.nsimplify((pj.T*pj)[0]/nr))
    res[J]=row; print(J,row)
