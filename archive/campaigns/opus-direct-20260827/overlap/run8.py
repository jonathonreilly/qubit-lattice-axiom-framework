"""Stable index route: H = CH*(D_W - m) hermitian; index = -(1/2)Tr sign(H). Cross-check vs SVD in d=2."""
import numpy as np
from kd import kd_gammas
from ovcore import build_DW, overlap_report
s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
s3=np.array([[1,0],[0,-1]],dtype=complex)
Gam,Gbar,G=kd_gammas(2); CL=1j*Gam[0]@Gam[1]

def idx_herm(DW,CH,mrho=1.0,a=1.0):
    N=DW.shape[0]//CH.shape[0]; C=np.kron(np.eye(N),CH)
    H=C@(DW-(mrho/a)*np.eye(DW.shape[0]))
    hh=np.max(np.abs(H-H.conj().T)); w,v=np.linalg.eigh((H+H.conj().T)/2)
    sg=v@np.diag(np.sign(w))@v.conj().T
    Dov=(1.0/a)*(np.eye(DW.shape[0])+C@sg)
    gw=np.max(np.abs(C@Dov+Dov@C-a*(Dov@C@Dov)))
    return dict(herm=hh, gap=np.min(np.abs(w)), gw=gw, index=-0.5*np.sum(np.sign(w)))

print("d=2 cross-check: SVD-polar index vs hermitian-sign index (must agree)")
for n in [1,2,3]:
    for lab,CH in [("grade G",G),("Clifford CL",CL)]:
        DW=build_DW(8,n,Gam); a=overlap_report(8,n,Gam,CH); b=idx_herm(DW,CH)
        print(f"  n={n} {lab:12s}: SVD={a['index']:+8.5f}  herm-sign={b['index']:+8.5f}  "
              f"gap={b['gap']:.3f} GW={b['gw']:.2e}")
