import numpy as np
from kd import kd_gammas
from ovcore import build_DW, overlap_report
s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
s3=np.array([[1,0],[0,-1]],dtype=complex)
Gam,Gbar,G=kd_gammas(2); CL=1j*Gam[0]@Gam[1]

print("== A. Spectral identity: is D_KD(n) = D_W(+n) (+) D_W(-n) ? ==")
L=6
for n in [0,1,2,3]:
    a=np.sort_complex(np.linalg.eigvals(build_DW(L,n,Gam)))
    same=np.sort_complex(np.concatenate([np.linalg.eigvals(build_DW(L,n,[s1,s2]))]*2))
    opp =np.sort_complex(np.concatenate([np.linalg.eigvals(build_DW(L,n,[s1,s2])),
                                         np.linalg.eigvals(build_DW(L,-n,[s1,s2]))]))
    print(f"  n={n}:  vs 2x D_W(+n): {np.max(np.abs(a-same)):.2e}   "
          f"vs D_W(+n)+D_W(-n): {np.max(np.abs(a-opp)):.2e}")

print("\n== B. r=0.5 rows: why did GW fail? (m_rho must lie strictly inside a Wilson window) ==")
print(f"{'r':>5} {'m_rho':>6} {'minSV(A)':>10} {'GWviol':>10} {'idx(G)':>9} {'idx(CL)':>9}")
for r,m in [(0.5,1.0),(0.5,0.5),(0.5,0.25),(0.5,0.75),(1.0,1.0),(1.0,2.0),(1.0,3.0)]:
    d1=overlap_report(8,2,Gam,G,mrho=m,r=r); d2=overlap_report(8,2,Gam,CL,mrho=m,r=r)
    print(f"{r:>5} {m:>6} {d1['minSV']:10.2e} {max(d1['gw'],d2['gw']):10.2e} "
          f"{d1['index']:9.5f} {d2['index']:9.5f}")
print("  (2d Wilson doubler masses sit at m = 0, 2r, 4r; overlap valid only strictly between them.)")
