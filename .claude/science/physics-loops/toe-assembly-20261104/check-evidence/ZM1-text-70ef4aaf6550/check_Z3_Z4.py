# Theorem Z3 / Z4 on the smallest L_cube instance, by a different path from the text:
# numerically solve the constraint system (CAR + gauge invariance at a site outside S_u) and look at the solutions.
# System: sites x (the representative site) and y, one link l=(x,y) of spin S, matter modes c_x, c_y.
# Psi = Tx c_x + Tx' c_x^dag + Ty c_y + Ty' c_y^dag with T in the link algebra M_{2S+1}(C).
# Gauss generator at y (LW1 sec.1): G_y = n_y - E_l  (l points into y).
import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(11)
def setup(S):
    d=int(round(2*S+1)); m=np.arange(-S,S+1)
    E=np.diag(m).astype(complex)
    a=np.array([[0,1],[0,0]],complex); z=np.diag([1,-1]).astype(complex); i2=np.eye(2)
    cx=np.kron(a,i2); cy=np.kron(z,a)            # Jordan-Wigner
    I4=np.eye(4); Id=np.eye(d)
    k=lambda link,mat: np.kron(link,mat)
    ops=[k(Id,cx),k(Id,cx.conj().T),k(Id,cy),k(Id,cy.conj().T)]
    Gy=k(Id,cy.conj().T@cy)-k(E,I4)
    return d,ops,Gy,k,I4
def build(p,d,ops,k,I4):
    T=(p[:4*d*d]+1j*p[4*d*d:]).reshape(4,d,d)
    return sum(k(T[i],I4)@ops[i] for i in range(4)),T
def resid(p,d,ops,Gy,k,I4,car=True,gauge=True):
    Psi,T=build(p,d,ops,k,I4); out=[]
    if car:
        out+= [Psi@Psi, Psi@Psi.conj().T+Psi.conj().T@Psi-np.eye(Psi.shape[0])]
    if gauge: out.append(Gy@Psi-Psi@Gy)
    v=np.concatenate([o.ravel() for o in out]); return np.concatenate([v.real,v.imag])
for S in [0.5,1.0]:
    d,ops,Gy,k,I4=setup(S); worst=0; nconv=0; ctl1=0; ctl2=0
    for trial in range(30):
        p0=rng.normal(size=8*d*d)
        r=least_squares(resid,p0,args=(d,ops,Gy,k,I4),xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=3000)
        if np.linalg.norm(r.fun)<1e-9:
            nconv+=1; _,T=build(r.x,d,ops,k,I4); worst=max(worst,np.linalg.norm(T[2]),np.linalg.norm(T[3]))
        r1=least_squares(resid,p0,args=(d,ops,Gy,k,I4,True,False),xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=3000)
        if np.linalg.norm(r1.fun)<1e-9:
            _,T=build(r1.x,d,ops,k,I4); ctl1=max(ctl1,np.linalg.norm(T[2])+np.linalg.norm(T[3]))
    # control 2: gauge invariance alone allows the transported hop J^dag c_y, which is not a fermion
    m=np.arange(-S,S+1); J=np.zeros((d,d),complex)
    for i in range(d-1): J[i+1,i]=np.sqrt(S*(S+1)-m[i]*(m[i]+1))
    Psi=k(J.conj().T,I4)@ops[2]
    print(f"Z3 instance S={S}: {nconv}/30 runs reached an exact solution of CAR + [G_y,Psi]=0; max ||T_y||,||T'_y|| over them = {worst:.2e} (claim: 0)")
    print(f"   control A (CAR only, no gauge condition): max ||T_y||+||T'_y|| = {ctl1:.3f} (nonzero expected)")
    print(f"   control B (gauge only): Psi=J^dag c_y has ||[G_y,Psi]||={np.linalg.norm(Gy@Psi-Psi@Gy):.1e}, ||Psi^2||={np.linalg.norm(Psi@Psi):.1e}, ||{{Psi,Psi*}}-1||={np.linalg.norm(Psi@Psi.conj().T+Psi.conj().T@Psi-np.eye(4*d)):.3f} (not a fermion)")
# Z3(d) algebra: [Lambda,T]=T with finite spectrum forces nilpotent; normal + nilpotent = 0
d=6; Lam=np.diag([0,0,1,1,2,3.]).astype(complex)
# solution space of [Lam,T]=T
basis=[(i,j) for i in range(d) for j in range(d) if abs(Lam[i,i]-Lam[j,j]-1)<1e-12]
T=np.zeros((d,d),complex)
for (i,j) in basis: T[i,j]=rng.normal()+1j*rng.normal()
print("Z3(d): generic solution of [Lambda,T]=T: ||[Lam,T]-T||=%.1e, ||T^N||=%.1e with N=4 distinct eigenvalues, normality defect ||TT*-T*T||=%.2f"%(np.linalg.norm(Lam@T-T@Lam-T),np.linalg.norm(np.linalg.matrix_power(T,4)),np.linalg.norm(T@T.conj().T-T.conj().T@T)))
# Z4 instance: H = sum_{x in S} G_x has at least |S|+1 distinct eigenvalues (L_cube, chain of |S| sites with spin-1/2 links at both ends and between)
import itertools
for nS in [1,2,3,4]:
    # matter eigenvalues 0..nS; internal links cancel; two boundary links contribute -E_in + E_out in {-1,0,1}
    ev=set()
    for occ in itertools.product((0,1),repeat=nS):
        for e_in in (-.5,.5):
            for e_out in (-.5,.5): ev.add(sum(occ)+e_out-e_in)
    print(f"Z4 instance |S|={nS}: distinct eigenvalues of H = {len(ev)} >= |S|+1 = {nS+1}")
