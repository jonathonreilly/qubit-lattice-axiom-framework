import numpy as np, sys
from kd import kd_gammas
from ovcore import table, overlap_report, build_DW, full_chir
np.set_printoptions(linewidth=140, suppress=True)
rng = np.random.default_rng(20260829)
L = 8

s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
s3=np.array([[1,0],[0,-1]],dtype=complex)

print("="*78); print("TASK 2 (control): 2-component Wilson-Dirac fibre, gammas = (s1,s2), chir = s3")
table("WilsonDirac f=2", L, [s1,s2], s3)

print("\n"+"="*78); print("TASK 3: Kahler-Dirac fibre d=2, f=4, real Gammas, G=diag((-1)^k)")
Gam,Gbar,G = kd_gammas(2)
print(f"  max|Im Gamma| = {max(np.max(np.abs(g.imag)) for g in Gam):.1e}  (Gammas are REAL)")
r3 = table("KahlerDirac f=4 REAL", L, Gam, G)

print("\n"+"="*78); print("TASK 4a: similarity transform S in U(2)xU(2) (commutes with G): Gam->S Gam S^-1, G->S G S^-1")
# G eigenspaces: +1 = {0,3}, -1 = {1,2} in bitmask basis
def rand_u(k):
    M = rng.normal(size=(k,k)) + 1j*rng.normal(size=(k,k))
    Q,R = np.linalg.qr(M); return Q@np.diag(np.diag(R)/np.abs(np.diag(R)))
S = np.zeros((4,4),dtype=complex)
Up, Um = rand_u(2), rand_u(2)
pl=[0,3]; mi=[1,2]
for i,ii in enumerate(pl):
    for j,jj in enumerate(pl): S[ii,jj]=Up[i,j]
for i,ii in enumerate(mi):
    for j,jj in enumerate(mi): S[ii,jj]=Um[i,j]
print(f"  S unitary err = {np.max(np.abs(S@S.conj().T-np.eye(4))):.1e}   [S,G] = {np.max(np.abs(S@G-G@S)):.1e}")
GamS = [S@g@S.conj().T for g in Gam]; GS = S@G@S.conj().T
I4=np.eye(4)
print(f"  Clifford preserved: {max(np.max(np.abs(GamS[a]@GamS[b]+GamS[b]@GamS[a]-2*(a==b)*I4)) for a in range(2) for b in range(2)):.1e}")
print(f"  {{G,Gam'}} = {max(np.max(np.abs(GS@g+g@GS)) for g in GamS):.1e}   G unchanged: {np.max(np.abs(GS-G)):.1e}")
print(f"  max|Im Gamma'| = {max(np.max(np.abs(g.imag)) for g in GamS):.4f}  (NO LONGER REAL)")
print(f"  max|Re Gamma'| = {max(np.max(np.abs(g.real)) for g in GamS):.4f}")
r4a = table("KahlerDirac f=4 COMPLEXIFIED (unitary conj)", L, GamS, GS)

print("\n"+"="*78); print("TASK 4a-neg (control that CAN fail): S generic in U(4), does NOT commute with G")
Sg = rand_u(4); GamG=[Sg@g@Sg.conj().T for g in Gam]
print(f"  Clifford still ok: {max(np.max(np.abs(GamG[a]@GamG[b]+GamG[b]@GamG[a]-2*(a==b)*I4)) for a in range(2) for b in range(2)):.1e}")
print(f"  but {{G, Gam'}} with UNTRANSFORMED G = {max(np.max(np.abs(G@g+g@G)) for g in GamG):.4f}  -> no chirality, no index theorem")
d = overlap_report(L,1,GamG,G)
print(f"  forcing it anyway at n=1: chir-herm viol={d['chir_herm']:.3e}  GW viol={d['gw']:.3e}  index={d['index']:.6f}  <- MEANINGLESS")

print("\n"+"="*78); print("TASK 4b (the test that CAN fail): project onto ONE taste. T = Gbar_1 Gbar_2, T^2=-1")
T = Gbar[0]@Gbar[1]
w,v = np.linalg.eig(T)
for sgn,lab in [(+1j,'T=+i'),(-1j,'T=-i')]:
    k = np.where(np.abs(w-sgn)<1e-9)[0]
    W,_ = np.linalg.qr(v[:,k])                 # 4x2 isometry
    Gt = [W.conj().T@g@W for g in Gam]; Ct = W.conj().T@G@W
    I2=np.eye(2)
    cl = max(np.max(np.abs(Gt[a]@Gt[b]+Gt[b]@Gt[a]-2*(a==b)*I2)) for a in range(2) for b in range(2))
    print(f"\n  [{lab}] fibre dim {W.shape[1]}  Clifford err={cl:.1e}  {{C,Gam}}={max(np.max(np.abs(Ct@g+g@Ct)) for g in Gt):.1e} "
          f" C^2-I={np.max(np.abs(Ct@Ct-I2)):.1e}  Tr C={np.real(np.trace(Ct)):.1e}")
    print(f"       max|Im Gamma_taste| = {max(np.max(np.abs(g.imag)) for g in Gt):.4f}   (must be nonzero: no real 2d option)")
    table(f"KD single taste {lab}", L, Gt, Ct)
