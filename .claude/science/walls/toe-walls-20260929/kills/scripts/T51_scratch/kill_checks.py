"""T51 kill checks (Claude Sonnet 5.5, same family as attacker). Independent re-implementation, not importing attack code.
K1 r>1 / negative r at retained rungs; K2 symmetric singlet-doublet entry delta (entry's own named cheapest test);
K3 T50 sibling: lightest RH eigenvalue over the joint window and T50-chain Dm2_31; K4 plain-language statement
'solar box needs split near 0.70'; K5 IO box; K6 anarchy with Gaussian light-mass ensemble."""
import numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9                      # eV*GeV
A0 = MPl*aLM**7; B0 = MPl*aLM**8
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3); RAT=(0.0268,0.0328)

def gaps_from_RH(lams):
    m = np.sort(c/np.abs(np.asarray(lams,float)))
    return m, m[1]**2-m[0]**2, m[2]**2-m[0]**2, m.sum()

print('== K0 benchmark from full 3x3 matrix')
M = np.array([[A0,0,0],[0,aLM/2*B0,B0],[0,B0,aLM/2*B0]])
s = np.linalg.svd(M, compute_uv=False); m,d21,d31,S = gaps_from_RH(s)
print(' masses meV', np.round(m*1e3,3), 'dm21 %.3e dm31 %.3e Sigma %.1f meV'%(d21,d31,S*1e3), 'ratio d21/7.41e-5 = %.1f'%(d21/7.41e-5))

print('\n== K1 retained rungs, r over (-50,50) incl. |r|>1 (attack scanned 0<r<0.99 only)')
rs = np.concatenate([np.linspace(-50,50,2000001)])
ms = c/A0*np.ones_like(rs)
with np.errstate(divide='ignore'):
    me = c/(B0*np.abs(1+rs)); mo = c/(B0*np.abs(rs-1))
M3 = np.sort(np.stack([ms,me,mo]),axis=0)
d21 = M3[1]**2-M3[0]**2; d31 = M3[2]**2-M3[0]**2
okA = (ATM[0]<=d31)&(d31<=ATM[1]); okS=(SOL[0]<=d21)&(d21<=SOL[1])
print(' r with dm31 in ATM box:', (np.abs(rs[okA]).min(), np.abs(rs[okA]).max()) if okA.any() else None)
print(' r with dm21 in SOL box:', okS.any(), ' min dm21 over all r =', np.nanmin(d21[np.isfinite(d21)]), '(SOL lo 6.92e-5)')
print(' joint:', (okA&okS).any())
# at atm-box r>1: what is dm21?
sel = okA & (np.abs(rs)>1)
print(' at r>1 with atm box: dm21 range', d21[sel].min(), d21[sel].max(), ' (x SOL hi: %.1f..%.1f)'%(d21[sel].min()/SOL[1], d21[sel].max()/SOL[1]))

print('\n== K2 add symmetric singlet-doublet entry delta (M12=M13=delta), retained A,B,eps=alpha/2*B, delta real')
def mat(delta, A=A0, B=B0, r=aLM/2):
    return np.array([[A,delta,delta],[delta,r*B,B],[delta,B,r*B]])
res=[]
ds = np.concatenate([np.linspace(0,30*B0,300001)])
for d in ds:
    pass
# vectorised
def sv(dl):
    out=[]
    for d in dl:
        out.append(np.linalg.svd(mat(d),compute_uv=False))
    return np.array(out)
dl = np.linspace(0, 25*B0, 25001)
S_ = sv(dl)
m3_ = np.sort(c/S_,axis=1)
d21=m3_[:,1]**2-m3_[:,0]**2; d31=m3_[:,2]**2-m3_[:,0]**2; Sg=m3_.sum(axis=1)
ok = (SOL[0]<=d21)&(d21<=SOL[1])&(ATM[0]<=d31)&(d31<=ATM[1])
print(' delta/B window with both boxes:', (dl[ok].min()/B0, dl[ok].max()/B0) if ok.any() else None)
if ok.any():
    print(' delta/A window:', dl[ok].min()/A0, dl[ok].max()/A0, ' Sigma meV range', Sg[ok].min()*1e3, Sg[ok].max()*1e3)
    i = np.where(ok)[0][len(np.where(ok)[0])//2]
    print(' mid point delta/B=%.3f masses meV %s dm21 %.3e dm31 %.3e'%(dl[i]/B0, np.round(m3_[i]*1e3,2), d21[i], d31[i]))
    # natural constants c*alpha^k
    print(' natural staircase deltas (delta = c*alpha^k*MPl) inside window:')
    for k in [6,7,8,9]:
        for cc in [0.25,1/3,0.5,1/np.sqrt(2),2/3,0.75,1,np.sqrt(2),1.5,2,3,4]:
            dd = cc*aLM**k*MPl
            if dl[ok].min()<=dd<=dl[ok].max(): print('   k=%d c=%.3f  delta/B=%.3f'%(k,cc,dd/B0))
print(' Interlacing: with delta, block eigenvalues straddle {A, B(1+r)}; mid RH eigenvalue ~5B reachable only when |lam-| ~ 5B (large delta)')

print('\n== K3 T50 sibling: joint window of the attack (A fixed, B=xB0, r) -> lightest RH eigenvalue x(1-r)B')
xs = np.linspace(2.5,3.5,2001); rr = np.linspace(0.6,0.75,1501)
X,R_ = np.meshgrid(xs,rr)
lam = np.stack([np.full_like(X,A0/B0), X*(1+R_), X*(1-R_)])
mm = np.sort(c/(lam*B0),axis=0)
D21 = mm[1]**2-mm[0]**2; D31 = mm[2]**2-mm[0]**2; Sg=mm.sum(axis=0)
okj=(SOL[0]<=D21)&(D21<=SOL[1])&(ATM[0]<=D31)&(D31<=ATM[1])
lightest = X*(1-R_)
print(' joint window: x %.3f..%.3f, r %.3f..%.3f'%(X[okj].min(),X[okj].max(),R_[okj].min(),R_[okj].max()))
print(' lightest RH eigenvalue / B0: %.4f .. %.4f (retained %.4f)'%(lightest[okj].min(),lightest[okj].max(),1-aLM/2))
print(' middle RH eigenvalue / B0:  %.3f .. %.3f ; ratio middle/lightest %.3f .. %.3f'%((X*(1+R_))[okj].min(),(X*(1+R_))[okj].max(),((1+R_)/(1-R_))[okj].min(),((1+R_)/(1-R_))[okj].max()))
print(' dm31 range in window (T50 chain, m1 kept) %.4e..%.4e ; Sigma %.1f..%.1f meV'%(D31[okj].min(),D31[okj].max(),Sg[okj].min()*1e3,Sg[okj].max()*1e3))
print(' => atm gap depends on lightest RH eigenvalue only (m3^2 - m1^2, m1=c/A fixed). Retained M1=B(1-alpha/2): dm31=%.4e'%(((c/(B0*(1-aLM/2)))**2-(c/A0)**2)))
print(' Note joint window CONTAINS the retained lightest eigenvalue? ', lightest[okj].min()<=1-aLM/2<=lightest[okj].max())

print('\n== K4 plain-language check: at the ratio-window r, what are the absolute gaps? (retained rungs)')
for r in [0.690,0.70,0.716]:
    lam=[A0,B0*(1+r),B0*(1-r)]; m,d21,d31,S=gaps_from_RH(lam)
    print(' r=%.3f dm21=%.3e (x%.1f of SOL hi) dm31=%.3e (x%.1f of ATM hi) ratio=%.4f Sigma=%.0f meV'%(r,d21,d21/SOL[1],d31,d31/ATM[1],d21/d31,S*1e3))

print('\n== K5 IO reading against an IO box (NuFit-5.3 IO |dm2_32| 3sigma approx 2.41-2.58e-3, from memory, NOT repo-quoted)')
for r in [aLM**2, aLM**2*0.9, aLM**2*1.1]:
    lam=[A0,B0*(1+r),B0*(1-r)]; m=np.sort(c/np.array(lam)); m3=m[0]; ma,mb=m[1],m[2]
    print(' r=%.5f dsol=%.3e |dm32| (heavier-lightest)=%.4e mean=%.4e Sigma=%.1f meV'%(r,mb**2-ma**2,mb**2-m3**2,0.5*(ma**2+mb**2)-m3**2,m.sum()*1e3))
print(' retained lightest RH change alpha/2 -> alpha^2: dm31 (T50 chain) changes by', 
      ((c/(B0*(1-aLM**2)))**2-(c/A0)**2)/((c/(B0*(1-aLM/2)))**2-(c/A0)**2)-1)

print('\n== K6 anarchy with the standard (HMW) ensemble: Gaussian LIGHT mass matrix, and M_R^-1 variant')
rng=np.random.default_rng(6151)
N=400000
def ens(kind):
    X = rng.normal(size=(N,3,3))+1j*rng.normal(size=(N,3,3))
    Mm=(X+np.transpose(X,(0,2,1)))/np.sqrt(2)
    s=np.linalg.svd(Mm,compute_uv=False)
    m = s if kind=='light' else 1/s
    m=np.sort(m,axis=1); m=m/m[:,2:3]*np.sqrt(2.5e-3)
    R=(m[:,1]**2-m[:,0]**2)/(m[:,2]**2-m[:,0]**2)
    return R, m.sum(axis=1)
for kind in ['light','RH-inverse']:
    R,Sg=ens(kind)
    print(' %-10s P(R in window)=%.4f  P(R in window & Sigma<72)=%.4f  P(R<=0.0328)=%.3f'%(kind,((R>=RAT[0])&(R<=RAT[1])).mean(),((R>=RAT[0])&(R<=RAT[1])&(Sg<0.072)).mean(),(R<=RAT[1]).mean()))
