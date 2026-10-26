from dev_engine import *
import time
Ms=commutant_z()
# coin-blind: M = identity (is in commutant)
Mz=np.eye(4,dtype=complex); Mall=build_M_all(Mz)
g=30.0
for N in (16,24,32):
    t=time.time()
    E=34.0
    res=free_G(E,(0,0,0),N)
    S=G1_series(res,0)
    B0=np.linalg.inv(S[0])-Vmat(g,Mall)
    w=np.linalg.eigvalsh((B0+B0.conj().T)/2)
    print(N,time.time()-t,np.round(w[:6],6), np.abs(B0-B0.conj().T).max())
