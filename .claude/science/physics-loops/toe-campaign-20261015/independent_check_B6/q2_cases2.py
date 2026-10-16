# Q2 complexified, case split on BOTH C4 lines (t,0,0) and (t,pi,pi): eigenvalues of U are monomials z^a, of V z^-a.
import sympy as sp, pickle, itertools, os, re
from exact_setup import *; from sysgen import walk, product
from q2_lines import eig_forms, eb, alg
u=sp.symbols('u1:20'); v=sp.symbols('v1:20')
if os.path.exists('q2_base.pkl'): base=pickle.load(open('q2_base.pkl','rb'))
else:
    G=[sp.Matrix(R) for R in rotations()]
    def canon(s):
        vv=sp.Matrix(s); return max(tuple(R*vv) for R in G)
    W=product(alg,walk(eb,u),walk(eb,v)); base=[]
    for s,Z in W.items():
        if canon(s)!=s: continue
        for b,c in Z.items():
            c=sp.expand(c)
            if s==(0,0,0) and b[0]==0 and b[1]==b[2]: c=sp.expand(c-1)
            if c!=0: base.append(c)
    base=list(set(base)); pickle.dump(base,open('q2_base.pkl','wb'))
labels=[(1,1),(1,-1),(-1,1),(-1,-1)]
lines={'0':(0,0,0),'pi':(0,1,1)}
FU={k:eig_forms(u,p) for k,p in lines.items()}; FV={k:eig_forms(v,p) for k,p in lines.items()}
def gnum(c):
    c=sp.nsimplify(sp.expand(c)); return '%s+(%s)*I'%(sp.Rational(sp.re(c)),sp.Rational(sp.im(c)))
def gs(e):
    e=sp.expand(e)
    syms=sorted(e.free_symbols,key=str)
    if not syms: return '(%s)'%gnum(e)
    out=[]
    for mon,c in sp.Poly(e,*syms).terms():
        m='*'.join('%s^%d'%(s,k) if k>1 else str(s) for s,k in zip(syms,mon) if k>0)
        out.append('(%s)'%gnum(c)+('*'+m if m else ''))
    return '+'.join(out)
good=[(-1,-1,1,1),(-1,0,1,0),(-1,1,1,-1),(0,-1,0,1),(0,0,0,0),(0,1,0,-1),(1,-1,-1,1),(1,0,-1,0),(1,1,-1,-1)]
os.makedirs('q2c2',exist_ok=True); k=0
for a0 in good:
  for a1 in good:
    lin=[]; extra=[]
    for ln,a in (('0',a0),('pi',a1)):
        for lab,aa in zip(labels,a):
            for j in (-1,0,1):
                if j!=aa: lin.append(FU[ln][lab+(j,)])
                if j!=-aa: lin.append(FV[ln][lab+(j,)])
            extra.append((FU[ln][lab+(aa,)],FV[ln][lab+(-aa,)]))
    tag='a0=%s a1=%s'%(a0,a1)
    sol=sp.linsolve(lin,list(u)+list(v))
    if sol==sp.EmptySet:
        print(tag,'linear inconsistent'); continue
    sol=list(sol)[0]; sub=dict(zip(list(u)+list(v),sol))
    free=sorted(set().union(*[sp.sympify(s).free_symbols for s in sol]),key=str)
    eqs=[sp.expand(e.subs(sub)) for e in base]+[sp.expand(x.subs(sub)*y.subs(sub)-1) for x,y in extra]
    eqs=[e for e in set(eqs) if e!=0]
    s='option(redSB);\nring r=(0,I),(%s),dp; minpoly=I^2+1;\nideal Q=%s;\n'%(','.join(map(str,free)),',\n'.join(gs(e) for e in eqs))
    s+='int t=timer; ideal J=std(Q); "%s nfree=%d dim=",dim(J)," time",timer-t; if(dim(J)>=0){J;}\nquit;\n'%(tag,len(free))
    open('q2c2/case%02d.sing'%k,'w').write(s); print(k,tag,'free',len(free),flush=True); k+=1
