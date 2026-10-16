# Q2: complexified system (U, V=U^{-1} independent) with case split on C4-line (t,0,0) eigenvalue monomials.
import sympy as sp, pickle, itertools, sys, time
from exact_setup import *; from sysgen import walk, product
from q2_lines import eig_forms, eb, alg
G=[sp.Matrix(R) for R in rotations()]
def canon(s):
    v=sp.Matrix(s); return max(tuple(R*v) for R in G)
u=sp.symbols('u1:20'); v=sp.symbols('v1:20')
U=walk(eb,u); V=walk(eb,v)
W=product(alg,U,V)
base=[]
for s,Z in W.items():
    if canon(s)!=s: continue
    for b,c in Z.items():
        c=sp.expand(c)
        if s==(0,0,0) and b[0]==0 and b[1]==b[2]: c=sp.expand(c-1)
        if c!=0: base.append(c)
base=list(set(base)); print('UV=I eqs at orbit reps',len(base))
FU=eig_forms(u,(0,0,0)); FV=eig_forms(v,(0,0,0))
labels=[(1,1),(1,-1),(-1,1),(-1,-1)]
def gs(e):
    e=sp.expand(e)
    if e==0: return '0'
    syms=sorted(e.free_symbols,key=str)
    p=sp.Poly(e,*syms) if syms else None
    if p is None:
        return '(%s)'%gnum(e)
    out=[]
    for mon,c in p.terms():
        m='*'.join('%s^%d'%(s,k) if k>1 else str(s) for s,k in zip(syms,mon) if k>0)
        out.append('(%s)'%gnum(c)+('*'+m if m else ''))
    return '+'.join(out)
def gnum(c):
    c=sp.nsimplify(sp.expand(c)); re,im=sp.Rational(sp.re(c)),sp.Rational(sp.im(c))
    return '%s+(%s)*I'%(re,im)
out=open('q2_cases.sing','w'); out.write('option(redSB);\n'); n=0
for a in itertools.product([-1,0,1],repeat=4):
    if sum(a)!=0: continue
    lin=[]
    for lab,aa in zip(labels,a):
        for j in (-1,0,1):
            if j!=aa: lin.append(FU[lab+(j,)])
            if j!=-aa: lin.append(FV[lab+(j,)])
    sol=sp.linsolve(lin,list(u)+list(v))
    tag='a=%s'%(a,)
    if sol==sp.EmptySet: out.write('"%s inconsistent";\n'%tag); continue
    sol=list(sol)[0]; sub=dict(zip(list(u)+list(v),sol))
    free=sorted(set().union(*[sp.sympify(s).free_symbols for s in sol]),key=str)
    eqs=[sp.expand(e.subs(sub)) for e in base]
    eqs+= [sp.expand(FU[lab+(aa,)].subs(sub)*FV[lab+(-aa,)].subs(sub)-1) for lab,aa in zip(labels,a)]
    eqs=[e for e in set(eqs) if e!=0]
    n+=1
    out.write('ring r%d=(0,I),(%s),dp; minpoly=I^2+1;\nideal Q=%s;\n'%(n,','.join(map(str,free)),',\n'.join(gs(e) for e in eqs)))
    out.write('int t=timer; ideal J=std(Q); "%s nfree=%d dim=",dim(J)," time",timer-t; if(dim(J)>=0){J;}\nkill r%d;\n'%(tag,len(free),n))
    print(tag,'free',len(free),flush=True)
out.write('quit;\n')
