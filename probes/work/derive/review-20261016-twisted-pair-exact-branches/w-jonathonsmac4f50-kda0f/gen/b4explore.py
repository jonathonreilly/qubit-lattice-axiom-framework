import pickle, numpy as np
from fractions import Fraction as F
from poly import *
from scipy.optimize import least_squares
d=pickle.load(open('cache.pkl','rb')); NP,NV,params,Mm=d['NP'],d['NV'],d['params'],d['M']
red=pickle.load(open('red.pkl','rb'))
free,sub,r=red[(0,0,0,0)]
# constant walk: A_0 = I -> origin params; find param indices at origin and solve for coefficient: A_0 = sum p_j M_(0,j)
origin=[j for j,(n,k) in enumerate(params) if n==(0,0,0)]
print('origin params',origin)
import sympy as sp
# find p_j with sum p_j M = I
Ms=[sp.Matrix(4,4,lambda a,b: sp.Rational(Mm[((0,0,0),j)][a][b][0].numerator,Mm[((0,0,0),j)][a][b][0].denominator)+sp.I*sp.Rational(Mm[((0,0,0),j)][a][b][1].numerator,Mm[((0,0,0),j)][a][b][1].denominator)) for j in origin]
c=sp.symbols('c0:2')
sol=sp.solve(list(sum((ci*Mi for ci,Mi in zip(c,Ms)),sp.zeros(4))-sp.eye(4)),c,dict=True)[0]
print(sol)
x=[F(0)]*NV
for ci,j in zip(c,origin):
    v=sp.nsimplify(sol[ci]); x[j]=F(int(sp.re(v).p),int(sp.re(v).q)); x[NP+j]=F(int(sp.im(v).p),int(sp.im(v).q))
t0=[x[v] for v in free]
# check the full affine map holds: sub[pivot] evaluated at t0 equals x[pivot]
for v,p in sub.items():
    assert evalp(p,{i:t0[i] for i in range(len(free))})==x[v],v
print('constant walk lies on flat branch affine space')
vals=[evalp({mo:c for mo,c in e},{i:t0[i] for i in range(32)}) for e in r]
print('all 336 vanish at constant walk:',all(v==0 for v in vals))
# Jacobian rank at t0 exactly (mod p large) 
J=np.zeros((len(r),32))
for i,e in enumerate(r):
    for mo,cf in e:
        for pos,v in enumerate(mo):
            rest=list(mo[:pos]+mo[pos+1:])
            t=float(cf)
            for w in rest: t*=float(t0[w])
            J[i,v]+=t
print('tangent rank (float SVD) ',np.linalg.matrix_rank(J,tol=1e-9),'-> tangent dim',32-np.linalg.matrix_rank(J,tol=1e-9))
pickle.dump({'t0':t0},open('t0.pkl','wb'))
# numeric solutions
Es=[[(mo,float(cf)) for mo,cf in e] for e in r]
def resid(t):
    out=np.zeros(len(Es))
    for i,e in enumerate(Es):
        s=0.0
        for mo,cf in e:
            p=cf
            for v in mo: p*=t[v]
            s+=p
        out[i]=s
    return out
# vectorise
mons=sorted({mo for e in r for mo,_ in e},key=lambda m:(len(m),m))
midx={m:i for i,m in enumerate(mons)}
C=np.zeros((len(r),len(mons)))
for i,e in enumerate(r):
    for mo,cf in e: C[i,midx[mo]]=float(cf)
def feats(t):
    return np.array([np.prod([t[v] for v in mo]) if mo else 1.0 for mo in mons])
def res2(t): return C@feats(t)
rng=np.random.default_rng(1)
sols=[]
for trial in range(60):
    t=rng.normal(size=32)*0.7
    s=least_squares(res2,t,xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=400)
    if np.abs(s.fun).max()<1e-10: sols.append(s.x)
print('converged',len(sols),'of 60')
pickle.dump(sols,open('b4sols.pkl','wb'))
t0f=np.array([float(v) for v in t0])
for s in sols[:10]:
    print('dist to const walk',np.linalg.norm(s-t0f))
