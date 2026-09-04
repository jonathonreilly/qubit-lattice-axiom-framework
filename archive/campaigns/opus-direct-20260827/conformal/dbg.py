import numpy as np
from kd import kd_gammas
from ovcore import build_DW
s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
Gam,Gbar,G=kd_gammas(2); L=4
def key(w): 
    o=np.lexsort((np.round(w.imag,9), np.round(w.real,9))); return w[o]
def cmp(a,b):
    a,b=key(a),key(b); return np.max(np.abs(a-b))
for n in [0,1,2]:
    A=np.linalg.eigvals(build_DW(L,n,Gam))
    Bp=np.linalg.eigvals(build_DW(L,n,[s1,s2])); Bm=np.linalg.eigvals(build_DW(L,-n,[s1,s2]))
    print(f" n={n}  KD vs 2xW(+n): {cmp(A,np.concatenate([Bp,Bp])):.2e}   "
          f"KD vs W(+n)+W(-n): {cmp(A,np.concatenate([Bp,Bm])):.2e}   "
          f"W(+n) vs W(-n): {cmp(Bp,Bm):.2e}")
# taste-restricted gammas, explicit
T=Gbar[0]@Gbar[1]; w,v=np.linalg.eig(T)
for sgn,lab in [(1j,'+i'),(-1j,'-i')]:
    k=np.where(np.abs(w-sgn)<1e-9)[0]; W,_=np.linalg.qr(v[:,k])
    gt=[W.conj().T@x@W for x in Gam]
    print(f"\n taste {lab}: i*g1*g2 =\n{np.round(1j*gt[0]@gt[1],6)}")
    print(f"   G|taste =\n{np.round(W.conj().T@G@W,6)}")
