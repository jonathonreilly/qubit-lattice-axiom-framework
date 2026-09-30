import numpy as np, itertools
from t40_consts import *
rng=np.random.default_rng(20260929)
A2=a2()
S={'a2':A2,'mtau':MTAU,'6a2':6*A2}
A={'mW':MW,'mZ':MZ,'v':V_GF,'v/sqrt2':V_GF/np.sqrt(2)}
NMC=400000
def members_pow(bases,kmin,kmax,lo=1.0,hi=1e6):
    out=[]
    for b in bases:
        for k in range(kmin,kmax+1):
            x=float(b)**k
            if lo<=x<=hi: out.append((f'{b}^{k}',x))
    # dedupe by value (e.g. 2^8=4^4=16^2), keep first label joined
    d={}
    for lab,x in out: d.setdefault(round(x,6),[]).append(lab)
    return [('='.join(v),k) for k,v in d.items()]
def mc_any(T_list, mem, w, nmc=NMC):
    """T_list: list of true ratios; null rescales S by rho (T scales as 1/rho for A/S). Any member within window."""
    vals=np.array([x for _,x in mem]); lv=np.log(vals)
    rho=np.exp(rng.uniform(np.log(0.5),np.log(2.0),nmc))
    hit=np.zeros(nmc,bool)
    for T in T_list:
        lt=np.log(T/rho)             # nulls
        # nearest member in log space
        idx=np.searchsorted(lv,lt); idx=np.clip(idx,1,len(lv)-1)
        d=np.minimum(np.abs(lt-lv[idx-1]),np.abs(lt-lv[idx]))
        hit|=d<=np.log1p(w)
    return hit.mean()
def real_hits(T_list_named, mem, w):
    res=[]
    for name,T in T_list_named:
        for lab,x in mem:
            if abs(T/x-1)<=w: res.append((name,lab,T/x-1))
    return res
out={}
# ---- Family N (lane's)
memN=sorted(members_pow([2,3,4,5,6,7,8,9,10],2,12,100,1000),key=lambda t:t[1])
memN=[(l,x) for l,x in memN]
TN=[MW/A2]
for w in (3.23e-4,1e-3):
    print('Family N window %.3f%%: members in [100,1000]: %d  p_LEE = %.4f   real hits: %s'%(w*100,len(memN),mc_any(TN,memN,w),real_hits([('mW/a2',TN[0])],memN,w)))
# ---- Family B
memB=sorted(members_pow([2,3,4,6,8,16],1,14,3,3e5),key=lambda t:t[1])
combosB=[]
for sn,sv in S.items():
    for an,av in A.items():
        for dn,dv in (('1',1.0),('2',2.0)):
            combosB.append((f'{dn}*{an}/{sn}',dv*av/sv))
TB=[t for _,t in combosB]
for w in (3.23e-4,1e-3):
    p=mc_any(TB,memB,w)
    print('Family B window %.3f%%: %d combos x %d members  p_LEE = %.4f ; real hits:'%(w*100,len(combosB),len(memB),p))
    for r in real_hits(combosB,memB,w): print('    ',r)
# ---- Family C (couplings)
P=P0
ab=ABARE; u=u0(P)
memC=[]
for p_ in range(0,5):
  for q in range(-6,7):
    for j in (0,1):
      for s in range(-2,3):
        x=ab**p_ * u**q * (7/8)**(j/4) * 2.0**s
        if 1e-6<=x<=1: memC.append((f'ab^{p_}u0^{q}(7/8)^{j}/4 2^{s}',x))
d={}
for l,x in memC: d.setdefault(round(x,12),[]).append(l)
memC=sorted([('|'.join(v[:2]),k) for k,v in d.items()],key=lambda t:t[1])
SC={'a2':A2,'mtau':MTAU}; AC={'v':V_GF,'mW':MW,'mZ':MZ}
combosC=[(f'{sn}/{an}',sv/av) for sn,sv in SC.items() for an,av in AC.items()]
# For null: S -> S*rho, T = S/A -> T*rho. Use T_inv trick: pass 1/T so that T_inv/rho matches
def mc_anyC(combos,mem,w,nmc=NMC):
    vals=np.array([x for _,x in mem]); lv=np.log(vals)
    rho=np.exp(rng.uniform(np.log(0.5),np.log(2.0),nmc)); hit=np.zeros(nmc,bool)
    for _,T in combos:
        lt=np.log(T*rho); idx=np.clip(np.searchsorted(lv,lt),1,len(lv)-1)
        d=np.minimum(np.abs(lt-lv[idx-1]),np.abs(lt-lv[idx])); hit|=d<=np.log1p(w)
    return hit.mean()
for w in (2.02e-4,5e-4,1e-3):
    p=mc_anyC(combosC,memC,w)
    print('Family C window %.3f%%: %d combos x %d distinct members p_LEE = %.4f ; real hits:'%(w*100,len(combosC),len(memC),p))
    for name,T in combosC:
        for lab,x in memC:
            if abs(T/x-1)<=w: print('    ',name,lab,'%+.4f%%'%((T/x-1)*100))

# ---- Family C0 (narrow): alpha_bare^m alpha_LM^n, 0<=m,n<=4, single combo m_tau/v and scale variants a2 with Koide factor
c0=[]
for m in range(0,5):
    for n in range(0,5):
        c0.append((f'ab^{m} aLM^{n}',ab**m*alphaLM(P0)**n))
c0=sorted(set(c0),key=lambda t:t[1])
d={}
for l,x in c0: d.setdefault(round(x,14),[]).append(l)
c0=sorted([('|'.join(v),k) for k,v in d.items()],key=lambda t:t[1])
for w in (2.02e-4,1e-3):
    print('Family C0 (alpha monomials only) window %.3f%%: %d members, single target m_tau/v: p_LEE = %.4f ; 6 combos: %.4f'%(w*100,len(c0),mc_anyC([('mtau/v',MTAU/V_GF)],c0,w),mc_anyC(combosC,c0,w)))

# ---- bridge-precision reading: what if a derivation can only be validated at the scheme spread (2%)?
for w in (0.005,0.02):
    print('window %.1f%%: Family N p=%.3f  Family B p=%.3f  Family C p=%.3f  Family C0 p=%.3f'%(w*100,mc_any(TN,memN,w),mc_any(TB,memB,w),mc_anyC(combosC,memC,w),mc_anyC(combosC,c0,w)))
