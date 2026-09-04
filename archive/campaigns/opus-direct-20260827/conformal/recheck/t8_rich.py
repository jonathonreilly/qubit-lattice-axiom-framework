"""T8 -- continuum (a -> 0) extrapolation at FIXED PHYSICS.
Same physical torus and same physical wave: L = 16, 32, 64 with n = 1 and
s_L = s_64 (L/64)^2, i.e. equal s*kappa^2.  Lattice artifacts are O(a^2) = O(1/L^2);
the s^2 heat-kernel term is physical and a-independent, so it is subtracted first
using the continuum Gilkey Int a_2 (an independent calculation, not a fit).
Richardson:  r_cont = (4 r_64 - r_32)/3   (2-pt);  3-pt in a^2 for 16/32/64."""
import numpy as np, math
from meas import heat_diff, lda
import cont

S64=np.array([4,5,6,8,10,13,16,20,25,32,40,50,64],float)
CH={'TT':(0,1,-1,0),'CF':(1,1,1,1)}
D={}
for L in (16,32,64):
    SV=S64*(L/64.0)**2
    for tag,P in CH.items():
        acc,rp,rf,el=heat_diff(L,0.05,P,1,SV,chunk=1024)
        kk=2*math.pi/L
        Vc,Sc,Ia2=cont.integrals(L,0.05,P,kk); Vc0,Sc0,_=cont.integrals(L,0.0,P,kk)
        F=(4*np.pi*SV)**2*acc; dV=rp['vol']-rf['vol']; dS=rp['S']-rf['S']
        A=lda(L,0.05,P,1,SV)
        D[(tag,L)]=dict(s=SV,raw=(F-dV)/(SV*dS/3), a2=(F-dV-SV*SV*Ia2)/(SV*dS/3),
                        lda=(F-dV-A)/(SV*dS/3), both=(F-dV-A-SV*SV*Ia2)/(SV*dS/3),
                        dV=dV,dS=dS,Ia2=Ia2,Vc=Vc-Vc0,Sc=Sc-Sc0)
        print(f"  done L={L} {tag} [{el:.0f}s]  dVol={dV:.4f} dS={dS:.5f} Ia2={Ia2:.5f}",flush=True)
np.savez("t8.npz", **{f"{t}{L}_{k}":v for (t,L),d in D.items() for k,v in d.items()
                      if isinstance(v,np.ndarray)})
print()
for key,lab in (('raw','RAW ratio'),('a2','raw - s^2 Int a2 (continuum, not fitted)'),
                ('both','raw - s^2 Int a2 - LDA')):
    print(f"=== {lab} ===")
    print("  s*kappa^2 |    TT L16     L32     L64   Rich(32,64)  Rich(16,32,64) |"
          "    CF L16     L32     L64   Rich(32,64)  Rich(16,32,64)")
    for j in range(len(S64)):
        line=f"   {S64[j]*(2*np.pi/64)**2:8.4f} |"
        for tag in ('TT','CF'):
            v=[D[(tag,L)][key][j] for L in (16,32,64)]
            r2=(4*v[2]-v[1])/3.0
            # 3-point fit r(a^2) = r0 + c1 a^2 + c2 a^4 with a^2 ~ 1/L^2
            x=np.array([1/16.0**2,1/32.0**2,1/64.0**2])
            c=np.linalg.solve(np.vander(x,3,increasing=True),np.array(v)); r3=c[0]
            line+=f" {v[0]:8.4f}{v[1]:8.4f}{v[2]:8.4f}  {r2:9.4f} {r3:11.4f}  |"
            if tag=='TT': line=line[:-1]+" |"
        print(line)
    print()
