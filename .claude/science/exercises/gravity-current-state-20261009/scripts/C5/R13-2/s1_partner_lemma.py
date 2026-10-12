# R13-2 s1: Lemma P (continuity / partner lemma) checked on random local, cubic-covariant, PSD quadratic Hamiltonians
# of 6 symmetric-tensor canonical pairs (h,E).  H = 1/2 x^T Hk x, x=(h,E); omega = |Im eig(J Hk)|.
# Claim: if both TT modes along z are gapless, then the C4v E-sector (2 vector modes) and one A1 (scalar) mode are
# gapless too (omega -> 0), because at k=0 TT(z) components lie in the cubic irreps Eg (xx-yy) and T2g (xy), whose
# other members are the vector (xz,yz in T2g) and scalar (2zz-xx-yy in Eg) directions. Gapping the partners by a
# local mass gaps the TT component in the same irrep.
import numpy as np, sys
from common import *
rng=np.random.default_rng(7)
offs=[np.zeros(3)]+[s*e for e in np.eye(3) for s in (1,-1)]+[np.array(v,float) for v in [(1,1,0),(1,-1,0),(0,1,1),(0,1,-1),(1,0,1),(1,0,-1)]]
Ptr=np.outer(trv,trv)/3.0
TT2g=np.zeros((6,6));
for v in (xy,yz,xz): TT2g+=np.outer(v,v)
Eg=np.eye(6)-Ptr-TT2g
def make_model(mass_h, flat=False, m=12):
    Mh=[rng.normal(size=(m,6)) for _ in offs]; Ne=[rng.normal(size=(m,6))*0.6 for _ in offs]; N0=rng.normal(size=(m,6))
    Ah0=rng.normal(size=(m,6))
    def Araw(k):
        q=2*np.sin(k/2)
        if flat:   # h enters only through R(h): exactly vector-gauge invariant potential (L-type h side)
            Ah=Mh[0]@Rmap(q)
        else:
            Ah=sum(M*(np.exp(1j*k@r)-1) for M,r in zip(Mh,offs))
        Ah=Ah+Ah0@mass_h
        AE=N0+sum(M*np.exp(1j*k@r) for M,r in zip(Ne,offs))
        return np.hstack([Ah,AE])
    def Hk(k):
        acc=np.zeros((12,12),complex)
        for R,D in zip(G48,D48):
            DD=np.block([[D,np.zeros((6,6))],[np.zeros((6,6)),D]])
            A=Araw(R@k); acc+=DD.T@(A.conj().T@A)@DD
        H=acc/48; return 0.5*(H+H.conj().T)
    return Hk
def report(name,Hk,ks=(0.08,0.04,0.02,0.01)):
    print(f"--- {name}"); H0=Hk(np.zeros(3)); print("   min eig H(0) = %.2e (PSD)"%np.linalg.eigvalsh(H0).min())
    for sname,vs in SECT.items():
        W=np.array([sector_omegas(Hk(np.array([0,0,k])),vs) for k in ks])   # rows: k, cols: modes in sector (sorted)
        # leakage check: H(k) block-diagonal in C4v sectors
        line=[]
        for j in range(W.shape[1]):
            w=W[:,j]
            if w[-1]>1e-3 and w[0]/w[-1]<1.5: line.append(f"omega~{w[-1]:.3f} (gapped)")
            elif np.all(w<1e-9): line.append("omega=0 identically (flat)")
            else:
                ex=np.polyfit(np.log(ks),np.log(np.maximum(w,1e-300)),1)[0]; line.append(f"omega(k=0.01)={w[-1]:.2e}, exponent {ex:.3f}")
        print(f"   {sname:24s}: "+'; '.join(line))
    # block-diagonality check
    k=np.array([0,0,0.03]); H=Hk(k); allv=[v for vs in SECT.values() for v in vs]
    P=np.array(allv).T; Pf=np.block([[P,np.zeros_like(P)],[np.zeros_like(P),P]]); Hs=Pf.T@H@Pf
    lab=[s for s,vs in SECT.items() for _ in vs]*2
    off=max(abs(Hs[i,j]) for i in range(12) for j in range(12) if lab[i]!=lab[j])
    print("   max coupling between different C4v sectors at k=0.03 z: %.1e"%off)
print("Lemma P checks (random local cubic-covariant PSD Hessians, 12-row symbols, range <= sqrt2):")
report("V1: h only through lattice differences + trace mass (B'(0)=b P_trace); E generic", make_model(Ptr))
report("V2: as V1 plus a T2g mass on h (tries to gap the vector partners)", make_model(Ptr+TT2g))
report("V3: as V2 plus an Eg mass on h (gaps all traceless h at k=0)", make_model(Ptr+TT2g+Eg))
report("V4: h only through R(h) (exact quadratic vector-gauge invariance) + trace mass", make_model(np.zeros((6,6)),flat=True))
for seed in (11,12,13):
    rng=np.random.default_rng(seed); report(f"V1 seed {seed}", make_model(Ptr))
