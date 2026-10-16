import sympy as sp, pickle, itertools
from exact_setup import *
eb=pickle.load(open('q2_basis.pkl','rb'))
alg=Alg(2,perm_rep2)
B=alg.basis(); bidx={b:t for t,b in enumerate(B)}
G=rotations()
C4x=[R for R in G if R[0,0]==1 and R[2,1]==1][0]   # (x,y,z)->(x,-z,y)
M=perm_rep2(C4x); print('M',M, 'M^2',M*M)
def elem(a,Mat):
    return {(a,i,j):Mat[i,j] for i in range(2) for j in range(2) if Mat[i,j]!=0}
comm=[elem(0,sp.eye(2)),elem(1,sp.eye(2)),elem(0,M),elem(1,M)]
CM=sp.Matrix([[c.get(b,0) for c in comm] for b in B])
def line_X(syms,p):
    """X^{(j)} for line p*pi + t e1: dict j -> 16-vector of linear forms"""
    X={}
    for el,s in zip(eb,syms):
        for n,d in el.items():
            j=int(n[0]); sg=(-1)**(int(sum(pi*ni for pi,ni in zip(p,n)))%2)
            v=X.setdefault(j,sp.zeros(16,1))
            for b,c in d.items(): v[bidx[b]]+=sg*c*s
    return X
def eig_forms(syms,p):
    X=line_X(syms,p); out={}
    for j,v in X.items():
        # solve CM * coef = v
        coef=(CM.T*CM).inv()*CM.T*v
        assert sp.simplify(CM*coef-v)==sp.zeros(16,1), 'not in commutant'
        al,be,ga,de=[sp.expand(x) for x in coef]
        for sg in (1,-1):
            for mu in (1,-1):
                out[(sg,mu,j)]=sp.expand(al+sp.I*sg*be+mu*ga+sp.I*sg*mu*de)
    return out
if __name__=="__main__":
    u=sp.symbols('u1:20')
    for p in [(0,0,0),(0,1,1)]:
        F=eig_forms(u,p)
        rows=[[sp.diff(F[k],x) for x in u] for k in sorted(F)]
        print(p,'rank of eigen-coefficient map',sp.Matrix(rows).rank())
    F=eig_forms(u,(0,0,0)); F.update({('pi',)+k:v for k,v in eig_forms(u,(0,1,1)).items()})
    rows=[[sp.diff(F[k],x) for x in u] for k in sorted(F,key=str)]
    print('both lines rank',sp.Matrix(rows).rank())
