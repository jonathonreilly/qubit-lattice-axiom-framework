"""The discriminator: reality of Gammas vs reality of the CHIRALITY vs taste counting."""
import numpy as np
from kd import kd_gammas
from ovcore import table, overlap_report, build_DW, full_chir
rng=np.random.default_rng(7); L=8
Gam,Gbar,G = kd_gammas(2); I4=np.eye(4)
CL = 1j*Gam[0]@Gam[1]          # Clifford chirality
print("Clifford chirality CL = i*Gam1*Gam2 on the SAME real Gammas:")
print(f"  herm={np.max(np.abs(CL-CL.conj().T)):.1e}  CL^2-I={np.max(np.abs(CL@CL-I4)):.1e} "
      f" {{CL,Gam}}={max(np.max(np.abs(CL@g+g@CL)) for g in Gam):.1e}  TrCL={np.real(np.trace(CL)):.1e}")
print(f"  conj(G)  - G  = {np.max(np.abs(G.conj()-G)):.1e}    (grade chirality is REAL)")
print(f"  conj(CL) + CL = {np.max(np.abs(CL.conj()+CL)):.1e}   (Clifford chirality is IMAGINARY)")

print("\n== antiunitary test: A = K (complex conjugation). Does A D_n A^-1 = D_{-n}? ==")
for lab,Gm in [("real KD Gammas",Gam)]:
    for n in [1,2,3]:
        Dn=build_DW(L,n,Gm); Dm=build_DW(L,-n,Gm)
        print(f"  {lab}: ||conj(D_{n}) - D_(-{n})|| = {np.max(np.abs(Dn.conj()-Dm)):.2e}")
print("  => A=K maps flux n -> -n exactly.  [A,G]=0 (G real) but {A,CL}=0 (CL imaginary).")
print("  R59 criterion: index even in n  <=>  antiunitary exists AND commutes with the chirality.")

print("\n"+"="*78)
print("A) real Gammas + REAL grade chirality G      (framework's stated setup)")
table("KD f=4, chirality G", L, Gam, G, ns=(-3,-2,-1,0,1,2,3))
print("\nB) SAME real Gammas + IMAGINARY Clifford chirality i*Gam1*Gam2")
table("KD f=4, chirality i*G1*G2", L, Gam, CL, ns=(-3,-2,-1,0,1,2,3))

print("\n"+"="*78)
print("C) does the complexified (unitary-conjugated) fibre change either answer?")
def rand_u(k):
    M=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)); Q,R=np.linalg.qr(M)
    return Q@np.diag(np.diag(R)/np.abs(np.diag(R)))
S=np.zeros((4,4),dtype=complex); Up,Um=rand_u(2),rand_u(2)
for i,ii in enumerate([0,3]):
    for j,jj in enumerate([0,3]): S[ii,jj]=Up[i,j]
for i,ii in enumerate([1,2]):
    for j,jj in enumerate([1,2]): S[ii,jj]=Um[i,j]
GamS=[S@g@S.conj().T for g in Gam]; GS=S@G@S.conj().T; CLS=S@CL@S.conj().T
print(f"  max|Im Gamma'| = {max(np.max(np.abs(g.imag)) for g in GamS):.4f}  (Gammas complexified)")
for n in [1,2,3]:
    Dn=build_DW(L,n,GamS); Dm=build_DW(L,-n,GamS)
    print(f"  ||conj(D'_{n}) - D'_(-{n})|| = {np.max(np.abs(Dn.conj()-Dm)):.3f}  <- naive reality diagnostic now FAILS")
table("complexified fibre, chirality G'", L, GamS, GS, ns=(1,2,3))
table("complexified fibre, chirality CL'", L, GamS, CLS, ns=(1,2,3))

print("\n"+"="*78)
print("D) can a 2-dim (single-taste) Clifford rep in d=2 have REAL Gammas AND a real chirality?")
s1=np.array([[0,1],[1,0]],dtype=float); s3=np.array([[1,0],[0,-1]],dtype=float)
best=None
for _ in range(200000):
    c=rng.normal(size=3)
    M=c[0]*s1+c[1]*s3+c[2]*np.eye(2)          # general real symmetric 2x2
    v=max(np.max(np.abs(M@s1+s1@M)), np.max(np.abs(M@s3+s3@M)), abs(np.trace(M@M)-2))
    if best is None or v<best[0]: best=(v,c)
print(f"  Gam1=s1, Gam2=s3 (the only real symmetric anticommuting pair up to O(2)).")
print(f"  best real symmetric CH with {{CH,Gam}}=0 and CH^2=I over 2e5 random tries: residual = {best[0]:.4f}")
print(f"  (algebraically: CH must be prop. to sigma_2, which is imaginary. NO real 2d option.)")
