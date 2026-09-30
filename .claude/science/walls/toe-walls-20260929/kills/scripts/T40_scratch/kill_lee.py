import numpy as np
from t40_consts import *
rng=np.random.default_rng(12345)
A2=a2(); NMC=400000
S={'a2':A2,'mtau':MTAU,'6a2':6*A2}
A={'mW':MW,'mZ':MZ,'v':V_GF,'v/sqrt2':V_GF/np.sqrt(2)}
def members(bases,kmin,kmax,lo,hi):
    d={}
    for b in bases:
        for k in range(kmin,kmax+1):
            x=float(b)**k
            if lo<=x<=hi: d.setdefault(round(x,6),[]).append(f'{b}^{k}')
    return sorted(d.items())
def mc(Ts,mem,w,rlo=0.5,rhi=2.0):
    lv=np.log(np.array([k for k,_ in mem]))
    rho=np.exp(rng.uniform(np.log(rlo),np.log(rhi),NMC)); hit=np.zeros(NMC,bool)
    for T in Ts:
        lt=np.log(T/rho); idx=np.clip(np.searchsorted(lv,lt),1,len(lv)-1)
        d=np.minimum(np.abs(lt-lv[idx-1]),np.abs(lt-lv[idx])); hit|=d<=np.log1p(w)
    return hit.mean()
w=3.23e-4
memB=members([2,3,4,6,8,16],1,14,3,3e5)
for name,dresses in (("attack script (dress 1,2)",[1,2]),("PREREG (dress 1,2,sqrt2,1/sqrt2)",[1,2,np.sqrt(2),1/np.sqrt(2)])):
    Ts=[dv*av/sv for sv in S.values() for av in A.values() for dv in dresses]
    print("Family B %-36s %2d combos p_LEE(0.032%%)=%.4f  p(0.1%%)=%.4f"%(name,len(Ts),mc(Ts,memB,w),mc(Ts,memB,1e-3)))
# lane-style: ALL perfect powers (b^k, b>=2 integer up to 25, k>=2) in [200,400], single anchor, band matches probe 06-05 section 4
pp=set()
for b in range(2,30):
    for k in range(2,12):
        x=b**k
        if 200<=x<=400: pp.add(x)
print("perfect powers in [200,400]:",sorted(pp))
memL=[(float(x),None) for x in sorted(pp)]
# null rho over [200/256.08, 400/256.08] uniform-log -> emulate lane's flat draw
print("lane-style single anchor p_LEE at 0.032%% (rho in [0.78,1.56]) = %.4f"%mc([MW/A2],memL,w,200/256.08,400/256.08))
# attack's Family N members
memN=members([2,3,4,5,6,7,8,9,10],2,12,100,1000)
print("attack Family N members:",[v for _,v in memN])
print("Family N p(0.032%%)=%.4f"%mc([MW/A2],memN,w))
# sensitivity to rho range for Family B (2-dress) : rho in [0.25,4]
Ts=[dv*av/sv for sv in S.values() for av in A.values() for dv in [1,2]]
print("Family B (attack dresses) rho range x16: p=%.4f ; x4: p=%.4f"%(mc(Ts,memB,w,0.25,4.0),mc(Ts,memB,w)))
