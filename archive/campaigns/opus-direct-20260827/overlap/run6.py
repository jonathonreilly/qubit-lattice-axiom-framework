import numpy as np
from kd import kd_gammas, ext_ops
from ovcore import build_DW, overlap_report, table
s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
s3=np.array([[1,0],[0,-1]],dtype=complex)

print("== 1. Is D_KD literally 2^(d/2) copies of Wilson-Dirac? (d=2, so 2 copies) ==")
Gam,Gbar,G=kd_gammas(2); L=6
for n in [0,1,2,3]:
    a=np.sort_complex(np.linalg.eigvals(build_DW(L,n,Gam)))
    b=np.sort_complex(np.linalg.eigvals(build_DW(L,n,[s1,s2])))
    print(f"  n={n}: ||spec(D_KD) - 2x spec(D_Wilson)||_inf = "
          f"{np.max(np.abs(a-np.sort_complex(np.concatenate([b,b])))):.2e}")

print("\n== 2. Taste algebra = commutant of the Gammas in the 2^d fibre ==")
for d in [2,4]:
    Gm,_,Gg=kd_gammas(d); f=1<<d
    M=np.zeros((d*f*f,f*f),dtype=complex)
    for a in range(d):
        M[a*f*f:(a+1)*f*f,:]=np.kron(Gm[a],np.eye(f))-np.kron(np.eye(f),Gm[a].T)
    s=np.linalg.svd(M,compute_uv=False); nc=int(np.sum(s<1e-9))
    print(f"  d={d}: fibre {f},  dim(commutant)={nc}  -> tastes = sqrt = {int(round(np.sqrt(nc)))} "
          f"(2^(d/2)={2**(d//2)})")

print("\n== 3. Robustness: does the 0-vs-2n split survive L, mass, Wilson r? ==")
CL=1j*Gam[0]@Gam[1]
print(f"{'L':>3} {'m_rho':>6} {'r':>5} | {'idx(G) n=1,2,3':>22} | {'idx(CL) n=1,2,3':>22} | {'maxGW':>9}")
for L in [6,8,10]:
    for mrho,r in [(1.0,1.0),(0.5,1.0),(1.5,1.0),(1.0,0.5)]:
        gs=[];cs=[];gw=0
        for n in [1,2,3]:
            dA=overlap_report(L,n,Gam,G,mrho=mrho,r=r); dB=overlap_report(L,n,Gam,CL,mrho=mrho,r=r)
            gs.append(round(dA['index'],6)); cs.append(round(dB['index'],6))
            gw=max(gw,dA['gw'],dB['gw'])
        print(f"{L:>3} {mrho:>6} {r:>5} | {str(gs):>22} | {str(cs):>22} | {gw:9.1e}")
