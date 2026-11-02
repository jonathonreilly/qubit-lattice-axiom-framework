# Runner for docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md
# Requirements: Python 3, numpy, scipy (generated with numpy 2.5.4, scipy 1.18.1). No file I/O; output to stdout.
# Run from the repo root:  python3 scripts/mdtn_ed_part1_reps_and_plaquette_2026_10_31.py > logs/runner-cache/mdtn_ed_part1_reps_and_plaquette_2026_10_31.txt
"""Part 1: (a) Gauss-law singlet multiplicities for ASQR SU(2)/SU(3) on a 6-valent Z^3 site;
(b) full-Hilbert-space ED of the j_max=1/2 truncated Kogut-Susskind SU(2) single plaquette
    (4 links x C^5), checking gauge invariance, the physical (Gauss) sector, and the band picture;
(c) gauge-invariant single-plaquette chain for j_max = 1/2, 1, 3/2, 2, 10: gap vs g.
Conventions: H_KS = (g^2/2) sum_l E_l^2 - (1/(2 g^2)) sum_P (Tr U_P + h.c.).
"""
import numpy as np, itertools, math
np.set_printoptions(precision=6, suppress=True)

# ---------- (a) singlet multiplicities ----------
def su2_inv(k, N=400):
    th = (np.arange(N)+0.5)*np.pi/N
    chi = 2*np.cos(th/2)            # character of spin-1/2 at class angle th in [0,2pi): use u = th*2
    # Weyl: int f = (2/pi) int_0^pi sin^2(t) f(t) dt with chi_1/2 = 2 cos t
    t = th
    return (2/np.pi)*np.sum(np.sin(t)**2*(2*np.cos(t))**k)*(np.pi/N)
def catalan(m): return math.comb(2*m, m)//(m+1)
print("(a) SU(2): dim Inv(2^{(x)k}), k=0..6:", [round(su2_inv(k),10) for k in range(7)])
print("    Catalan C_{k/2} for even k:", [catalan(k//2) if k%2==0 else 0 for k in range(7)])

def su3_inv(a, b, N=48):
    t = 2*np.pi*np.arange(N)/N
    T1, T2 = np.meshgrid(t, t, indexing='ij')
    z1, z2 = np.exp(1j*T1), np.exp(1j*T2); z3 = 1/(z1*z2)
    chi3 = z1+z2+z3; chi3b = np.conj(chi3)
    vd = (z1-z2)*(z1-z3)*(z2-z3)
    val = np.mean(np.abs(vd)**2*chi3**a*chi3b**b)/6
    return val.real
print("    SU(3): dim Inv(3^{(x)a} (x) 3bar^{(x)b}), a+b<=6, a-b = 0 mod 3:")
for n in range(0, 7):
    row = []
    for a in range(n+1):
        b = n-a
        v = su3_inv(a, b)
        row.append((a, b, int(round(v))))
        assert abs(v-round(v)) < 1e-8
    print("     degree", n, ":", [(a, b, d) for (a, b, d) in row if d])

# ---------- (b) full-space single plaquette, j<=1/2 ----------
# link basis: index 0 = |j=0>, 1+2*i+j = |1/2; i (left/start index), j (right/end index)>, psi_ij = sqrt2 D_ij
eps = np.array([[0, 1], [-1, 0]])
U = np.zeros((2, 2, 5, 5))          # U[a,b] truncated multiplication by D_ab
for a in range(2):
    for b in range(2):
        for i in range(2):
            for j in range(2):
                U[a, b, 1+2*i+j, 0] = (1/np.sqrt(2))*(a == i)*(b == j)
                U[a, b, 0, 1+2*i+j] = eps[a, i]*eps[b, j]/np.sqrt(2)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def Lgen(s):   # generator of psi(g)->psi(h^{-1} g), h = exp(i th s/2): d/dth -> -(i s/2) acting on first index
    M = np.zeros((5, 5), complex)
    A = -1j*s/2
    for i in range(2):
        for j in range(2):
            for k in range(2):
                M[1+2*k+j, 1+2*i+j] += A[i, k]      # |ij> -> sum_k A_ik |kj>
    return M
def Rgen(s):   # psi(g)->psi(g h): |ij> -> sum_k (i s/2)_{kj} |ik>
    M = np.zeros((5, 5), complex)
    A = 1j*s/2
    for i in range(2):
        for j in range(2):
            for k in range(2):
                M[1+2*i+k, 1+2*i+j] += A[k, j]
    return M
nL = 4; I5 = np.eye(5)
def emb(op, l):
    out = np.array([[1.0]])
    for m in range(nL):
        out = np.kron(out, op if m == l else I5)
    return out
# links l: site l -> site l+1 (mod 4).  site x: start of link x, end of link x-1
G = []
for x in range(4):
    for s in sig:
        G.append(emb(Lgen(s), x) + emb(Rgen(s), (x-1) % 4))
# check commutation of truncated U with gauge generators is covariant: build Tr U_P
dim = 5**nL
TrU = np.zeros((dim, dim))
for a, b, c, d in itertools.product(range(2), repeat=4):
    TrU += emb(U[a, b], 0)@emb(U[b, c], 1)@emb(U[c, d], 2)@emb(U[d, a], 3)
n_op = np.diag([0, 1, 1, 1, 1.0])
Nflux = sum(emb(n_op, l) for l in range(4))
print("(b) max|[G, TrU]| =", max(np.abs(g@TrU-TrU@g).max() for g in G), "; TrU hermitian:", np.allclose(TrU, TrU.T))
C = sum(g.conj().T@g for g in G)    # Casimir-sum; kernel = gauge-invariant subspace
w, v = np.linalg.eigh(C); phys = v[:, np.abs(w) < 1e-9]
print("    dim H_phys =", phys.shape[1])
Hred_T = phys.conj().T@TrU@phys; Hred_N = phys.conj().T@Nflux@phys
print("    N on phys:", np.round(np.linalg.eigvalsh(Hred_N), 8), "; |<1|TrU|0>| =", np.round(np.abs(np.linalg.eigvalsh(Hred_T)), 8))
for g2 in [4.0, 2.0, 1.0]:
    H = (3*g2/8)*Nflux - (1/(2*g2))*2*TrU
    ef = np.linalg.eigvalsh(H)
    Hp = phys.conj().T@H@phys; ep = np.linalg.eigvalsh(Hp)
    print(f"    g^2={g2}: full-space lowest 6 = {np.round(ef[:6],5)}; phys = {np.round(ep,5)}; phys gap = {ep[1]-ep[0]:.5f};"
          f" exact 2-level sqrt((3g^2/2)^2+4/g^4) = {np.sqrt((1.5*g2)**2+4/g2**2):.5f}")

# ---------- (c) gauge-invariant single plaquette chain ----------
def chain_gap(g2, jmax):
    js = np.arange(0, jmax+1e-9, 0.5)
    H = np.diag(2*g2*js*(js+1)) - (1/g2)*(np.eye(len(js), k=1)+np.eye(len(js), k=-1))
    e = np.linalg.eigvalsh(H); return e[1]-e[0]
print("(c) single-plaquette gauge-invariant chain, gap vs g^2 (units: H_KS):")
print("     g^2   " + "  ".join(f"jmax={j:<4}" for j in [0.5, 1, 1.5, 2, 10]) + "  strong-coupling 3g^2/2")
for g2 in [4, 2, 1.5, 1, 0.75, 0.5, 0.3]:
    print(f"    {g2:5.2f}  " + "  ".join(f"{chain_gap(g2,j):9.5f}" for j in [0.5, 1, 1.5, 2, 10]) + f"  {1.5*g2:9.5f}")

# ---------- (d) operator norm of the truncated plaquette operator on the FULL 625-dim space ----------
ev = np.linalg.eigvalsh(TrU)
print("(d) full-space spectrum of truncated Tr U_P (j<=1/2): min =", round(ev.min(), 10), " max =", round(ev.max(), 10),
      " => ||Tr U_P|| =", round(np.abs(ev).max(), 10))
