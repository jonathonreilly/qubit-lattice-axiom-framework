#!/usr/bin/env python3
"""B18 part 2: steps built only from taste-covariant ingredients.
Taste content (from taste_obstruction.py): T_i = (-1)^{x_i} (V = 1) commutes with S^2 and with every
on-site factor, but not with S or R_L; the H_link tastes (diagonal V_i) commute with R_L and S^2 but
with no O-symmetric on-site factor except scalars.  Hence the taste-covariant words are
(A) words in S^{+-2} and B1 Clifford-phase on-site factors (exact taste (-1)^{x_i}: W(k+pi e_i) = W(k)),
(B) words in S^{+-2} and R_L (planar: every corner-plane sector is independent of its normal momentum).
For (A) the eight cube points are one node (identical copies), and k = 0 (with its seven pi-shifts)
is a second O-fixed point.  We search family (A) for spin-1/2 Weyl doublets at k*, find every node
at the same quasi-energy, and report speeds, isotropy and Berry fluxes.  Prints PASS/FAIL, TOTAL."""
import time, pickle
exec(open('b18lib.py').read())
from scipy.optimize import minimize
t0=time.time()
PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
S2=lambda k: SK(k)@SK(k); S2i=lambda k: (SK(k)@SK(k)).conj().T
onH=[(f"H{a}{b}",UHf(a,b)) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",ULf(a,b,c)) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]+[(l[0]+"*"+h[0],l[1]@h[1]) for h in onH for l in onL]
small=onH+onL
# (B) planar decoupling of S^2/R_L words, checked on a few words
rng=np.random.default_rng(11)
planes=[[0,1,4,5],[2,3,6,7],[8,9,10,11]]; normal=[2,1,0]
wordsB=[lambda k: S2(k)@RL(k), lambda k: S2(k)@RL(k)@S2i(k)@RL(k), lambda k: RL(k)@S2(k)@S2(k)@RL(k)@S2i(k)]
okB=True; multB=[]
for W in wordsB:
    for _ in range(3):
        k=rng.uniform(-np.pi,np.pi,3); M=W(k)
        for p,n in zip(planes,normal):
            o=[i for i in range(12) if i not in p]; k2=k.copy(); k2[n]+=rng.uniform(0.3,2)
            okB&=np.allclose(M[np.ix_(p,o)],0) and np.allclose(M[np.ix_(p,p)],W(k2)[np.ix_(p,p)])
    multB.append(sorted(m for _,m in levels(W,kst)))
check("(B) words in S^{+-2} and R_L split into three corner-plane sectors, each independent of its normal momentum "
      "(so no point nodes); at k* every level is a multiple of 6 here", okB and all(all(m%6==0 for m in mb) for mb in multB), f"k* multiplicities {multB}")
# (A) exact taste: W(k + pi e_i) = W(k) for words in S^{+-2} and on-site factors
k=rng.uniform(-np.pi,np.pi,3); U=cands[100][1]
check("(A) T_i = (-1)^{x_i} is an exact symmetry of every word in S^{+-2} and on-site factors: W(k+pi e_i) = W(k)",
      all(np.allclose(S2(k+np.pi*e)@U,S2(k)@U) for e in EX))
# search family (A)
fams=[]
fams+= [("S2."+un,(lambda U: (lambda k: S2(k)@U))(U)) for un,U in cands]
fams+= [("S2i."+un,(lambda U: (lambda k: S2i(k)@U))(U)) for un,U in cands]
fams+= [(f"S2.{a}.S2.{b}",(lambda A,B: (lambda k: S2(k)@A@S2(k)@B))(A,B)) for (a,A) in small for (b,B) in small]
fams+= [(f"S2.{a}.S2i.{b}",(lambda A,B: (lambda k: S2(k)@A@S2i(k)@B))(A,B)) for (a,A) in small for (b,B) in small]
print(f"{len(fams)} taste-symmetric words in family (A)",flush=True)
q=1e-4
DX=[EX[0],EX[1],EX[2],np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3),np.array([0.3,-0.5,0.81])/np.linalg.norm([0.3,-0.5,0.81])]
G0=np.zeros(3)
def pair(W,k0,d,E,qq=q):
    s=[]
    for sg in (1,-1):
        ee=wrap(np.angle(np.linalg.eigvals(W(k0+sg*qq*d)))-E); ee=np.sort(ee[np.abs(ee)<50*qq])
        if len(ee)!=2: return np.nan
        s.append((ee[1]-ee[0])/(2*qq))
    return np.mean(s)
hits=[]
for nm,W in fams:
    W0=W(kst)
    for E,m in levels(lambda k: W0,kst):
        if m!=2: continue
        v=[pair(W,kst,d,E) for d in DX]
        if np.any(np.isnan(v)) or min(v)<1e-3: continue
        eg=np.abs(wrap(np.angle(np.linalg.eigvals(W(G0)))-E)); mG=int(np.sum(eg<1e-7))
        hits.append((nm,float(E),float(np.mean(v)),float(np.ptp(v)),mG))
print(f"{len(hits)} (word, level) pairs with a spin-1/2 Weyl doublet at k*  [{time.time()-t0:.0f}s]",flush=True)
import collections
print("multiplicity at k=0 at the node quasi-energy:",dict(collections.Counter(h[4] for h in hits)))
print("distinct k* speeds:",sorted({round(h[2],6) for h in hits}))
check("every k* Weyl doublet in family (A) is isotropic (O-forced)", all(h[3]<1e-5 for h in hits), f"max spread {max(h[3] for h in hits) if hits else 0:.1e}")
# nodes at k=0 when it carries a doublet at E
gam=[]
for nm,E,v,a,mG in hits:
    if mG==2:
        W=dict(fams)[nm]; vg=[pair(W,G0,d,E) for d in DX]; gam.append((nm,E,v,vg))
okG=[g for g in gam if not np.any(np.isnan(g[3])) and min(g[3])>1e-3]
print(f"{len(gam)} hits also have a doublet at k=0 at E; {len(okG)} of those are linear Weyl nodes; speeds at k=0:",
      sorted({round(np.mean(g[3]),6) for g in okG}))
# cleanliness: grid of the reduced zone (period pi), excluding balls around k* and 0 (mod pi)
g=np.linspace(-np.pi/2,np.pi/2,10,endpoint=False)+0.037
GR=[np.array(t) for t in itertools.product(g,repeat=3)]
def dmod(k,c): return np.linalg.norm(np.angle(np.exp(2j*(k-c)))/2)
GR=[k for k in GR if dmod(k,kst)>0.35 and dmod(k,G0)>0.35]
# a coarse prefilter at 5^3 first, then the full 10^3 grid on survivors
g5=np.linspace(-np.pi/2,np.pi/2,5,endpoint=False)+0.051
G5=[np.array(t) for t in itertools.product(g5,repeat=3) if dmod(np.array(t),kst)>0.35 and dmod(np.array(t),G0)>0.35]
res=[]
for nm,E,v,a,mG in hits:
    W=dict(fams)[nm]
    m5=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))) for k in G5)
    res.append((m5,nm,E,v,mG))
res.sort(reverse=True)
print("best by 5^3 far-grid distance to E:",[(round(r[0],3),r[1],round(r[2],4),r[4]) for r in res[:8]],flush=True)
top=[]
for m5,nm,E,v,mG in res[:40]:
    if m5<0.05: break
    W=dict(fams)[nm]
    m10=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))) for k in GR)
    top.append((m10,nm,E,v,mG))
top.sort(reverse=True)
print("best by 10^3 far-grid distance:",[(round(r[0],3),r[1],round(r[2],4),r[4]) for r in top[:8]],flush=True)
# refined minimisation from the 20 grid points nearest to E, for the best 5
def gapf(W,E): return lambda k: np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E)))
final=[]
for m10,nm,E,v,mG in top[:5]:
    W=dict(fams)[nm]; f=gapf(W,E)
    vals=sorted(GR,key=f)[:20]; best=np.inf; bk=None
    for k0 in vals:
        r=minimize(f,k0,method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-12,'maxiter':4000})
        if f(r.x)<best and dmod(r.x,kst)>0.05 and dmod(r.x,G0)>0.05: best=f(r.x); bk=r.x
    final.append((best,nm,E,v,mG,bk))
    print(f"  refined: {nm:22s} E={E:+.4f} v*={v:.6f} mult(k=0)={mG}  min |eps-E| away from k*,0: {best:.2e} at {np.round(bk,4)}",flush=True)
clean=[f_ for f_ in final if f_[0]>1e-3]
check("no word in family (A) found with E reached only at k* and k=0 (refined; a negative search result, not a no-go)",
      not clean, f"best refined distance {max(f_[0] for f_ in final) if final else 0:.2e}")
pickle.dump(dict(hits=hits,gam=gam,res=res[:200],top=top,final=[f_[:5] for f_ in final]),open('taste_symmetric_steps.pkl','wb'))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
