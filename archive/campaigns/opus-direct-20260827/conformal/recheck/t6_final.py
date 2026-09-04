"""T6 -- dense s-grids at L=32 and L=64 (matched by s_64 = 4 s_32, i.e. equal s*kappa^2),
saved to npz, plus a systematic scan over fit models and windows."""
import numpy as np, math, itertools, sys
from meas import heat_diff, lda
import cont

S64 = np.array([4,5,6,8,10,13,16,20,25,32,40,50,64],float)
S32 = S64/4.0
CH = {'TT':(0,1,-1,0), 'CF':(1,1,1,1)}
out = {}
for L,SV in ((32,S32),(64,S64)):
    for tag,P in CH.items():
        acc,rp,rf,el = heat_diff(L,0.05,P,1,SV,chunk=1024)
        kk = 2*math.pi/L
        Vc,Sc,Ia2 = cont.integrals(L,0.05,P,kk); Vc0,Sc0,_ = cont.integrals(L,0.0,P,kk)
        out[f'{tag}{L}_s']=SV
        out[f'{tag}{L}_F']=(4*np.pi*SV)**2*acc
        out[f'{tag}{L}_x']=np.array([rp['vol']-rf['vol'], rp['S']-rf['S'],
                                     Vc-Vc0, Sc-Sc0, Ia2])
        out[f'{tag}{L}_lda']=lda(L,0.05,P,1,SV)
        print(f"  done L={L} {tag}  [{el:.0f}s]",flush=True)
np.savez("t6.npz", **out)

MODELS = {'A+Bs':          lambda s:[s**0,s],
          'A+Bs+Cs2':      lambda s:[s**0,s,s**2],
          'A+Bs+Cs2+Ds3':  lambda s:[s**0,s,s**2,s**3],
          'A+Bs+D/s':      lambda s:[s**0,s,1/s],
          'A+Bs+Cs2+D/s':  lambda s:[s**0,s,s**2,1/s],
          'Bs+Cs2 (dVol fixed)':      lambda s:[s,s**2],
          'Bs+Cs2+Ds3 (dVol fixed)':  lambda s:[s,s**2,s**3]}

def scan(tag,L,useLDA):
    s=out[f'{tag}{L}_s']; F=out[f'{tag}{L}_F'].copy()
    dV,dS,dVc,dSc,Ia2 = out[f'{tag}{L}_x']
    if useLDA: F = F - out[f'{tag}{L}_lda']
    res=[]
    for name,bf in MODELS.items():
        fixed = 'fixed' in name
        for lo,hi in ((s[1],s[-3]),(s[2],s[-2]),(s[2],s[-1]),(s[3],s[-1]),(s[1],s[-1]),(s[0],s[-4])):
            m=(s>=lo)&(s<=hi); X=np.stack(bf(s[m]),1)
            y = (F-dV)[m] if fixed else F[m]
            c,*_=np.linalg.lstsq(X,y,rcond=None)
            B = c[0] if fixed else c[1]
            res.append((3*B/dS, name, lo, hi))
    return res

print()
for L in (32,64):
    for tag in ('TT','CF'):
        for useLDA in (False,True):
            r=scan(tag,L,useLDA); v=np.array([x[0] for x in r])
            lab = f"L={L} {tag} {'LDA-sub' if useLDA else 'raw    '}"
            print(f"  {lab}: 3B/dS over {len(v)} model x window variants: "
                  f"median {np.median(v):7.4f}  range [{v.min():7.4f},{v.max():7.4f}]  "
                  f"IQR [{np.percentile(v,25):7.4f},{np.percentile(v,75):7.4f}]")
    print()

print("=== matched physics (s_64 = 4 s_32, equal s*kappa^2): raw ratio and a2+LDA-corrected ===")
print("   s*kappa^2    TT L32    TT L64  |    CF L32    CF L64      (raw)")
print("                                  |                          (a2+LDA corrected)")
for j in range(len(S64)):
    row=[]; row2=[]
    for tag in ('TT','CF'):
        for L,SV in ((32,S32),(64,S64)):
            s=SV[j]; F=out[f'{tag}{L}_F'][j]; dV,dS,dVc,dSc,Ia2=out[f'{tag}{L}_x']
            A=out[f'{tag}{L}_lda'][j]; den=s*dS/3
            row.append((F-dV)/den); row2.append((F-dV-A-s*s*Ia2)/den)
    print(f"   {S32[j]*(2*np.pi/32)**2:8.4f}  {row[0]:8.4f} {row[1]:9.4f}  | {row[2]:9.4f} {row[3]:9.4f}   raw")
    print(f"             {row2[0]:8.4f} {row2[1]:9.4f}  | {row2[2]:9.4f} {row2[3]:9.4f}   corrected")

print()
print("=== plateau fits in RATIO space on the fully-subtracted ratio")
print("    r(s) = [F - dVol_simp - LDA(s) - s^2 Int a2] / (s dS/3) = r0 + p/s + q s  ===")
for L,SV in ((32,S32),(64,S64)):
    for tag in ('TT','CF'):
        s=out[f'{tag}{L}_s']; F=out[f'{tag}{L}_F']; dV,dS,dVc,dSc,Ia2=out[f'{tag}{L}_x']
        A=out[f'{tag}{L}_lda']
        r=(F-dV-A-s*s*Ia2)/(s*dS/3)
        vals=[]
        for lo,hi in ((s[1],s[-3]),(s[2],s[-2]),(s[2],s[-1]),(s[3],s[-1]),(s[1],s[-1])):
            m=(s>=lo)&(s<=hi)
            for basis in (['1','1/s'],['1','s'],['1','1/s','s'],['1','1/s','s','1/s2']):
                X=np.stack([{'1':s[m]**0,'1/s':1/s[m],'s':s[m],'1/s2':s[m]**-2}[b] for b in basis],1)
                c,*_=np.linalg.lstsq(X,r[m],rcond=None); vals.append(c[0])
        vals=np.array(vals)
        print(f"  L={L} {tag}: raw r over s-grid {r.min():.4f}..{r.max():.4f} ; "
              f"r0 over 20 fits: median {np.median(vals):.4f} range [{vals.min():.4f},{vals.max():.4f}]")
