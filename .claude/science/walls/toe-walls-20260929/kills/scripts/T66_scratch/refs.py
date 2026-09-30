"""Continuum ADM reference functionals (K=1, alpha=1) as (coef, slots[(label,nderiv)]) lists."""
import sympy as sp
from fractions import Fraction as F
from match import sympy_terms
x=sp.Symbol('x',positive=True)
s=sp.Symbol('s')
h=[sp.Function(n)(x) for n in ('hx','hy','hz')]; Q=[sp.Function(n)(x) for n in ('Px','Py','Pz')]
N,M,XI=[sp.Function(n)(x) for n in ('N','M','xi')]
D=lambda f,n=1: sp.diff(f,x,n)
K=sp.Integer(1); a=sp.Integer(1)   # K=1, alpha=1: 1/(4a)=1/4
Xc=[x,sp.Symbol('y'),sp.Symbol('z')]
gg=[1+s*hh for hh in h]
gm=sp.diag(*gg); gi=sp.diag(*[1/g_ for g_ in gg])
def Gm(a_,b,c): return sum(gi[a_,d]*(sp.diff(gm[d,b],Xc[c])+sp.diff(gm[d,c],Xc[b])-sp.diff(gm[b,c],Xc[d])) for d in range(3))/2
def Rm(a_,b,c,d):
    r=sp.diff(Gm(a_,b,d),Xc[c])-sp.diff(Gm(a_,b,c),Xc[d])
    r+=sum(Gm(a_,c,e)*Gm(e,b,d)-Gm(a_,d,e)*Gm(e,b,c) for e in range(3)); return r
Rc=sp.Matrix(3,3,lambda b,d: sum(Rm(a_,b,a_,d) for a_ in range(3)))
Rs=sum(gi[b,d]*Rc[b,d] for b in range(3) for d in range(3))
sg=sp.sqrt(gg[0]*gg[1]*gg[2])
sgR=sp.expand(sp.series(sg*Rs,s,0,3).removeO())
V2=sgR.coeff(s,2)
Tf=(sum(g_**2*(s*p_)**2 for g_,p_ in zip(gg,Q))-sp.Rational(1,2)*sum(g_*s*p_ for g_,p_ in zip(gg,Q))**2)/sg/(4*a)
T3=sp.expand(sp.simplify(sp.expand(sp.series(Tf,s,0,4).removeO()).coeff(s,3)))
fmap={h[0]:('h',0),h[1]:('h',1),h[2]:('h',2),Q[0]:('P',0),Q[1]:('P',1),Q[2]:('P',2),N:('N',0),M:('M',0),XI:('X',0)}
xi0=(K/(4*a))*(D(N)*M-N*D(M))
REF={
 'T3': sympy_terms(N*T3, fmap),
 'V2': sympy_terms(N*V2, fmap),
 'G2': sympy_terms(XI*(Q[0]*D(h[0])-2*D(h[0]*Q[0])+Q[1]*D(h[1])+Q[2]*D(h[2])), fmap),
 'xi1': sympy_terms(2*Q[0]*D(-h[0]*xi0), fmap),   # G1[xi1_cont]
 'chi': [],
}
if __name__=='__main__':
    for k,v in REF.items(): print(k,len(v)); 
    print(REF['G2'])
