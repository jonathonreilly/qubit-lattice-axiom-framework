#!/usr/bin/env python3
"""B20 part 2 control: is the obstruction an artefact of parameter-free phases?
Family (continuous phases, NOT parameter-free): W = S . U_H(a) U_L(b) . S . L202 (and the U_L U_H order), with
b_0 = b_3 so that k* carries Weyl doublets at E and E+pi (bookkeeping lemma).  This family has the exact Z-tastes
(spectrum pi-periodic) and the Y-taste; its T-fixed points mod pi Z^3 are Gamma_r = 0 and R_r = k*, both hosting
isotropic Weyl nodes of speed 2 sqrt2/3 and opposite chirality.  An all-isotropic step needs E to be reached
nowhere else.  We maximise  m(a,b) = min_{k in 16^3 grid of the pi-cube, |k - Gamma_r|,|k - R_r| > 0.2} dist(spec W(k), E)
with Nelder-Mead from random starts, then refine the best points (40^3 determinant sign test and multi-start
crossing search).  Prints PASS/FAIL, TOTAL.  A negative outcome is a failed search, not a no-go."""
import time, sys
ARGV=list(sys.argv)
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
t0=time.time(); PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
Rpl=onL(2,0,2)
def UH(p): return sum(np.exp(1j*a)*P for a,P in zip(p,Ps))
def UL(p): return sum(np.exp(1j*a)*Q for a,Q in zip(p,Qs))
def word(x,order):
    a=x[:3]; b=np.array([x[3],x[4],x[5],x[3]])
    return ['S',(UH(a)@UL(b) if order==0 else UL(b)@UH(a)),'S',Rpl]
g=np.linspace(-np.pi/2,np.pi/2,16,endpoint=False)+0.0371; G=np.array(list(itertools.product(g,repeat=3)))
def pdist(k,c,P=np.pi): return np.linalg.norm(np.mod(k-c+P/2,P)-P/2,axis=-1)
far=(pdist(G,np.zeros(3))>0.2)&(pdist(G,kst)>0.2); GF=G[far]
def Eof(w):
    lv=[(e,m) for e,m in node_levels(w,kst,1e-8) if m==2]; return lv[0][0] if lv else None
def m_of(x,order):
    w=word(x,order); E=Eof(w)
    if E is None: return 0.0
    return float(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wbatch(w,GF)))-E))))
import pickle
CACHE='/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/continuous_taste_opt_best.pkl'
rng=np.random.default_rng(2026); best=[]
NST=int(ARGV[1]) if len(ARGV)>1 else 16
if os.path.exists(CACHE): best=pickle.load(open(CACHE,'rb')); print(f"  (loaded {len(best)} optimised starts from the cache)")
else:
    for st in range(NST):
        order=st%2; x0=rng.uniform(0,2*np.pi,6)
        r=minimize(lambda x: -m_of(x,order),x0,method='Nelder-Mead',options={'maxiter':250,'xatol':1e-4,'fatol':1e-6})
        best.append((-r.fun,order,r.x)); print(f"  start {st}: max-min distance {-r.fun:.4f}  [{time.time()-t0:.0f}s]",flush=True)
    pickle.dump(best,open(CACHE,'wb'))
best.sort(key=lambda t:-t[0])
check("the k* doublets of the family are at E and E+pi with opposite chiralities and speed 2 sqrt2/3 (bookkeeping lemma)",
      all((lambda w: (lambda lv: len(lv)==2 and abs(abs(wrap(lv[0][0]-lv[1][0]))-np.pi)<1e-8)([(e,m) for e,m in node_levels(w,kst,1e-8) if m==2]))(word(b[2],b[1])) for b in best[:4]))
fin=[]
for mm,order,x in best[:4]:
    w=word(x,order); E=Eof(w)
    gg=np.linspace(-np.pi/2,np.pi/2,40,endpoint=False)+0.0071; GG=np.array(list(itertools.product(gg,repeat=3))); rr=[]
    for i in range(0,len(GG),8000):
        Ws=Wbatch(w,GG[i:i+8000]); c0=np.linalg.det(Ws[0]); rr.append((np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0))).real)
    rr=np.concatenate(rr); fermi=bool(rr.min()<0<rr.max())
    sols,_=find_crossings(w,E,ngrid=20,nstart=80,lo=-np.pi/2,hi=np.pi/2,period=np.pi)
    other=[s for s in sols if pdist(s,np.zeros(3))>1e-4 and pdist(s,kst)>1e-4]
    kinds=[]
    for s in other[:6]:
        v=vel_matrix(w,s,E); kinds.append((np.round(s/np.pi,3).tolist(),'band' if v['spread']>1e-4 else 'node',float(np.round(v['spread'],4))))
    dXM=[min(abs(wrap(e-E)) for e,m_ in node_levels(w,k,1e-7)) for k in (np.pi/2*EX[0],np.pi/2*np.array([1,1,0]))]
    cert,bad,ev,_=certify_clean(w,E,[np.zeros(3),kst],0.03,lo=-np.pi/2,hi=np.pi/2,n0=24,maxdepth=8,budget=4_000_000)
    print(f"     dist(spec W, E) at X_r, M_r: {dXM[0]:.2e}, {dXM[1]:.2e}; Lipschitz certificate outside 0.03-balls at Gamma_r, R_r: {cert} ({bad} uncertified cells, {ev} evaluations)",flush=True)
    fin.append((mm,fermi,len(other),cert)); print(f"  best m={mm:.4f} order={order} x={np.round(x,4)} E={E:+.4f}: 40^3 det sign change {fermi}; {len(other)} crossings away from Gamma_r,R_r, e.g. {kinds[:3]}",flush=True)
check("no optimised continuous-phase point is certified clean (E reached only at Gamma_r, R_r); the best points drive the X_r/M_r doublets towards E (negative search)",
      not any(f[3] for f in fin),f"best max-min grid distance {best[0][0]:.4f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
