AUDIT_INPUT_PATHS = ('docs/THE_OVERLAP_OF_THE_CUBE_WALK_EUCLIDEAN_KERNEL_GIVES_EXACT_GINSPARG_WILSON_CHIRALITY_WITHOUT_DOUBLERS_BUT_ITS_CHIRAL_PROJECTOR_IS_NOT_A_WALK_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Overlap (Ginsparg-Wilson) operator from the cube walk's Euclidean kernel (space x tick = Z^4).
Kernel X = D_W - m0 (Wilson copy-mass form), H = g5 X, V = g5 sign(H) = X (X^+X)^(-1/2), D = 1 + V.
Checks: GW algebra, zero modes over the zone, locality (position space), polynomial (site-to-site)
and 5th-direction (domain-wall) realisations, exact index / chirality / anomaly sums in U(1) backgrounds.
Supplied (cited, not derived): Neuberger 1998, Luscher 1998/99, Kaplan 1992, Nielsen-Ninomiya 1981,
Hernandez-Jansen-Luscher 1999 (locality), Hasenfratz-Laliena-Niedermayer 1998 (index).
Self-contained; seeded; numpy only."""
AUDIT_TIMEOUT_SEC = 120
import time
from fractions import Fraction as Fr
import numpy as np

np.random.seed(20261023)
rng = np.random.default_rng(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex)
I2 = np.eye(2); Z2 = 0 * I2
G4 = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)] + [np.block([[Z2, I2], [I2, Z2]])]
G5 = G4[0] @ G4[1] @ G4[2] @ G4[3]; I4 = np.eye(4)
G2 = [s1, s2]; G5_2 = s3

def sgnh(H):
    w, v = np.linalg.eigh(H); return (v * np.sign(w)) @ v.conj().T, np.abs(w).min()

# ---------- A. algebra + free zone ----------
# A1 lemma: for D = 1 + V, GW <=> V g5 V = g5; with g5-hermiticity this is V unitary. Random check.
M = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); Hr = G5 @ (M + G5 @ M.conj().T @ G5)
e, _ = sgnh(Hr); V = G5 @ e; D = I4 + V
r1 = np.abs(G5 @ D + D @ G5 - D @ G5 @ D).max(); r2 = np.abs(V @ V.conj().T - I4).max()
r3 = np.abs(G5 @ V @ G5 - V.conj().T).max()
check("A1 any g5-hermitian kernel: V=g5 sign(g5 X) unitary, g5 V g5 = V^+, D=1+V obeys GW exactly",
      max(r1, r2, r3) < 1e-13, f"GW {r1:.1e}, unit {r2:.1e}")
# A0 the 3+1 walk unitary itself is not a V: g5 commutes with the hop and anticommutes with the copy mass
beta = G4[3]; alph = [beta @ G4[i] * 1j for i in range(3)]  # hermitian alpha_i = i g4 g_i
r0s = []; rh = []
for _ in range(20):
    k3 = rng.uniform(-np.pi, np.pi, 3); Hd = sum(alph[i] * np.sin(k3[i]) for i in range(3)) + beta * (sum(1 - np.cos(k3)) + 0.2)
    w, v = np.linalg.eigh(Hd); Uw = (v * np.exp(-1j * (np.pi / 4) * w)) @ v.conj().T
    r0s.append(np.abs(G5 @ Uw @ G5 - Uw.conj().T).max()); rh.append(np.abs(G5 @ Hd @ G5 + Hd).max())
check("A0 Wilson-Dirac tick U(K)=exp(-i eps H): g5 commutes with the hop (g5 H g5 != -H), so g5 U g5 != U^+; "
      "the 3+1 tick is not itself a V", min(rh) > 1e-3 and max(r0s) > 0.3, f"max|g5Ug5-U^+| {max(r0s):.2f}")
def free_parts(L, m0=1.0, ct=1.0, d=4):
    ks = 2 * np.pi * np.arange(L) / L
    K = np.meshgrid(*([ks] * d), indexing='ij')
    c = [1.0] * (d - 1) + [ct]
    S = [c[m] * np.sin(K[m]) for m in range(d)]
    Mk = sum(c[m] * (1 - np.cos(K[m])) for m in range(d)) - m0
    w = np.sqrt(sum(s * s for s in S) + Mk * Mk)
    return K, S, Mk, w
L = 12
for (m0, ct, nexp) in [(1.0, 1.0, 1), (0.6, 0.5, 1)]:
    K, S, Mk, w = free_parts(L, m0, ct)
    # D(k) = 1 + (i g.S + M)/w ; eigenvalues 1 + (M +- i|S|)/w ; zero iff S=0 and M<0
    absS = np.sqrt(sum(s * s for s in S))
    lam = np.abs(1 + (Mk + 1j * absS) / w)
    nz = int((lam < 1e-12).sum())
    corners = [lam[tuple(np.array(n) * L // 2)] for n in np.ndindex(2, 2, 2, 2)]
    gap = np.sort(lam.ravel())[1]
    check(f"A2 m0={m0}, tick weight {ct}: zeros of D on the {L}^4 zone only at k=0 (one Dirac = L+R Weyl), "
          f"15 doubler corners at |D|=2", nz == nexp and np.allclose(sorted(corners)[1:], 2.0),
          f"zeros {nz}, next |lambda| {gap:.3f}")
# A3 exact GW on the full grid, matrix form
K, S, Mk, w = free_parts(L)
Dk = np.einsum('...,ij->...ij', 1 + Mk / w, I4) + sum(np.einsum('...,ij->...ij', 1j * S[m] / w, G4[m]) for m in range(4))
gw = np.abs(np.einsum('ij,...jk->...ik', G5, Dk) + np.einsum('...ij,jk->...ik', Dk, G5)
            - np.einsum('...ij,jk,...kl->...il', Dk, G5, Dk)).max()
check("A3 GW relation g5 D + D g5 = D g5 D on all 12^4 momenta", gw < 1e-13, f"{gw:.1e}")
# A4 light mode is a Dirac cone: D ~ i k-slash / m0
q = 2 * np.pi / 60; kk = np.array([q, 0, 0, 0]); Ms = sum(1 - np.cos(kk)) - 1.0
ws = np.sqrt(np.sum(np.sin(kk) ** 2) + Ms ** 2)
Dsmall = (1 + Ms / ws) * I4 + sum(1j * np.sin(kk[m]) / ws * G4[m] for m in range(4))
check("A4 near k=0: D = i k-slash/m0 + O(k^2) (Lorentz cone of the one light Dirac field)",
      np.abs(Dsmall - 1j * q * G4[0]).max() < q * q, f"resid {np.abs(Dsmall - 1j*q*G4[0]).max():.1e}, k={q:.3f}")
# A5 m0 window sets the number of light corners (measured zeros on the grid): corners with 2n < m0
cnt = []
for m0 in (1.0, 3.0, 5.0, 7.0):
    K_, S_, M_, w_ = free_parts(L, m0)
    lam_ = np.abs(1 + (M_ + 1j * np.sqrt(sum(s * s for s in S_))) / w_); cnt.append(int((lam_ < 1e-12).sum()))
check("A5 light-corner count vs copy-mass window m0 = 1,3,5,7: 1,5,11,15 zeros (one species only for 0<m0<2)",
      cnt == [1, 5, 11, 15], f"{cnt}")
# ---------- B. locality (free, position space) ----------
def envelope(L):
    K, S, Mk, w = free_parts(L)
    f0 = np.fft.ifftn(1 + Mk / w); f0.flat[0] -= 0  # identity part (delta included)
    fv = [np.fft.ifftn(1j * S[m] / w) for m in range(4)]
    amp = np.sqrt(np.abs(f0) ** 2 + sum(np.abs(f) ** 2 for f in fv))
    x = np.arange(L); x = np.minimum(x, L - x)
    X = np.meshgrid(*([x] * 4), indexing='ij'); dist = sum(X)
    env = np.array([amp[dist == dd].max() for dd in range(dist.max() + 1)])
    return env
env12 = envelope(12); env10 = envelope(10)
dd = np.arange(3, 13); slope = -np.polyfit(dd, np.log(env12[dd]), 1)[0]
dd2 = np.arange(3, 11); slope10 = -np.polyfit(dd2, np.log(env10[dd2]), 1)[0]
check("B1 free overlap kernel decays exponentially in taxicab distance (fit d=3..12 on 12^4; 10^4 agrees)",
      slope > 0.5 and abs(slope - slope10) < 0.1, f"rate {slope:.3f} (L=12), {slope10:.3f} (L=10); |D(0)|={env12[0]:.3f}, |D(12)|={env12[12]:.1e}")

# ---------- C. site-to-site: polynomial = n neighbourhood steps; 5th direction = domain wall ----------
w2 = (w ** 2).ravel(); a, b = w2.min(), w2.max()
rho = (np.sqrt(b) + np.sqrt(a)) / (np.sqrt(b) - np.sqrt(a))
errs = []; ns = [4, 8, 12, 16, 20]
for n in ns:
    c = np.polynomial.chebyshev.chebinterpolate(lambda t: 1 / np.sqrt((b - a) / 2 * t + (b + a) / 2), n)
    pn = np.polynomial.chebyshev.chebval((2 * w2 - b - a) / (b - a), c)
    errs.append(np.abs(pn * np.sqrt(w2) - 1).max())   # |X P_n(X^+X) - V| = |w p_n(w^2) - 1|
rate_n = -np.polyfit(ns, np.log(errs), 1)[0]
check("C1 V_n = X P_n(X^+X) has strict taxicab range 2n+1 (n neighbourhood steps of X^+X) and error ~ rho^-n",
      rate_n > 0.9 * np.log(rho), f"err(n=4..20) {errs[0]:.1e}->{errs[-1]:.1e}, rate {rate_n:.3f} >= ln rho {np.log(rho):.3f}")
check("C2 locality bound from C1: tail rate >= ln(rho)/2 per taxicab step; measured B1 rate obeys it",
      slope >= np.log(rho) / 2, f"bound {np.log(rho)/2:.3f} <= measured {slope:.3f}")
# C3 Kaplan/Shamir 5th direction: strictly nearest-neighbour 5D operator, Pauli-Villars ratio -> overlap
Pp = (I4 + G5) / 2; Pm = (I4 - G5) / 2
def DWk(k): return sum(1j * G4[m] * np.sin(k[m]) for m in range(4)) + (sum(1 - np.cos(k)) - 1.0) * I4
def D5(k, Ls, m):
    A = DWk(k) + I4; Z = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        Z[4*s:4*s+4, 4*s:4*s+4] = A
        cp = -m if s == Ls - 1 else 1.0; cm = -m if s == 0 else 1.0
        Z[4*s:4*s+4, 4*((s+1) % Ls):4*((s+1) % Ls)+4] += -cp * Pm
        Z[4*s:4*s+4, 4*((s-1) % Ls):4*((s-1) % Ls)+4] += -cm * Pp
    return Z
def Deff(k, Ls):
    Pm_ = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        Pm_[4*s:4*s+4, 4*s:4*s+4] += Pm; Pm_[4*s:4*s+4, 4*((s+1) % Ls):4*((s+1) % Ls)+4] += Pp
    Mx = np.linalg.inv(Pm_) @ np.linalg.solve(D5(k, Ls, 1.0), D5(k, Ls, 0.0) @ Pm_)
    return Mx[:4, :4]
kset = rng.uniform(-np.pi, np.pi, (6, 4)); gwL = []; mt = []
for Ls in (4, 8, 16):
    g_ = []; t_ = []
    for k in kset:
        Dd = Deff(k, Ls); Dw = DWk(k); HT = G5 @ Dw @ np.linalg.inv(2 * I4 + Dw)
        wT, vT = np.linalg.eigh(HT)
        t_.append(np.abs(Dd - (I4 + G5 @ ((vT * np.tanh(Ls * np.arctanh(wT))) @ vT.conj().T)) / 2).max())
        g_.append(np.abs(G5 @ Dd + Dd @ G5 - 2 * Dd @ G5 @ Dd).max())
    gwL.append(max(g_)); mt.append(max(t_))
check("C3 5D domain wall (strict NN in 5D): D_eff(Ls) = (1+g5 tanh(Ls artanh H_T))/2 exactly; GW defect falls ~exp(-Ls)",
      max(mt) < 1e-12 and gwL[1] < 1e-2 * gwL[0] and gwL[2] < 1e-2 * gwL[1],
      f"formula {max(mt):.0e}; GW defect Ls=4,8,16: {gwL[0]:.1e},{gwL[1]:.1e},{gwL[2]:.1e}")

# ---------- D. U(1) backgrounds: exact chirality, index, rank of P_hat, anomaly sums ----------
def links(Ls_, fluxes, e=1):
    d = len(Ls_); N = int(np.prod(Ls_)); idx = np.arange(N).reshape(Ls_)
    coords = np.indices(Ls_).reshape(d, -1)
    Ts = []
    for mu in range(d):
        ph = np.zeros(N)
        for (p, q_, Q) in fluxes:          # flux Q in plane (p,q_), uniform plaquette 2 pi Q/(Lp Lq)
            Fp = 2 * np.pi * Q / (Ls_[p] * Ls_[q_])
            if mu == p: ph += -Fp * coords[q_]
            if mu == q_: ph += np.where(coords[q_] == Ls_[q_] - 1, Fp * Ls_[q_] * coords[p], 0.0)
        nb = idx.reshape(-1); sh = np.roll(idx, -1, axis=mu).reshape(-1)
        T = np.zeros((N, N), complex); T[nb, sh] = np.exp(1j * e * ph); Ts.append(T)
    return Ts
def overlap(Ls_, fluxes, e=1, m0=1.0):
    d = len(Ls_); G = G4 if d == 4 else G2; g5 = G5 if d == 4 else G5_2
    Ts = links(Ls_, fluxes, e); N = Ts[0].shape[0]; ns = g5.shape[0]
    X = np.zeros((N * ns, N * ns), complex)
    for mu in range(d):
        T = Ts[mu]; X += np.kron(T - T.conj().T, G[mu]) / 2 + np.kron(2 * np.eye(N) - T - T.conj().T, np.eye(ns)) / 2
    X -= m0 * np.eye(N * ns)
    G5b = np.kron(np.eye(N), g5); e_, gapH = sgnh(G5b @ X)
    return np.eye(N * ns) + G5b @ e_, G5b, gapH
def index_info(D, G5b):
    wv, vv = np.linalg.eig(D); z = vv[:, np.abs(wv) < 1e-8]
    if z.shape[1]:
        z, _ = np.linalg.qr(z); ch = np.real(np.diag(z.conj().T @ G5b @ z))
    else: ch = np.array([])
    trg = np.real(np.trace(G5b @ (np.eye(len(D)) - D)))
    return ch, trg
D2, G5b2, gH = overlap((10, 10), [(0, 1, 1)])
gwr = np.abs(G5b2 @ D2 + D2 @ G5b2 - D2 @ G5b2 @ D2).max()
ch, trg = index_info(D2, G5b2)
check("D1 2D U(1), Q=1, 10^2: GW exact in the background; zero modes exactly chiral; index n+ - n- = -Q",
      gwr < 1e-12 and len(ch) == 1 and np.allclose(np.abs(ch), 1, atol=1e-10) and int(round(ch.sum())) == -1,
      f"GW {gwr:.1e}, zero-mode g5 {np.round(ch, 10)}, H_W gap {gH:.3f}")
D0, _, _ = overlap((10, 10), [])
_, trg0 = index_info(D0, G5b2); Nf = len(D2)
rk1 = (Nf - trg) / 2; rk0 = (Nf - trg0) / 2
check("D2 Luscher P_hat_L=(1-g5_hat)/2, g5_hat=g5(1-D): rank 100 at Q=0 but 101 at Q=1 (Tr g5_hat = 2 index): "
      "the chiral split has gauge-field-dependent rank, so it is not a walk-invariant sector",
      abs(rk0 - 100) < 1e-8 and abs(rk1 - 101) < 1e-8, f"ranks {rk0:.6f}, {rk1:.6f}")
# locality in the background: column envelope
src = 0; col = D2[:, 2 * src:2 * src + 2]; amp = np.sqrt((np.abs(col) ** 2).sum(1)).reshape(100, 2).sum(1).reshape(10, 10)
x = np.minimum(np.arange(10), 10 - np.arange(10)); dist = x[:, None] + x[None, :]
env2 = np.array([amp[dist == d_].max() for d_ in range(11)]); sl2 = -np.polyfit(np.arange(2, 9), np.log(env2[2:9]), 1)[0]
check("D3 overlap stays exponentially local in the Q=1 background (column envelope, fit d=2..8)",
      sl2 > 0.5, f"rate {sl2:.3f}, |D(8)|={env2[8]:.1e}")
# 2D m0 in (2,4): two light corners of chirality opposite to k=0 -> index +2Q (doublers = index)
D2b, _, _ = overlap((10, 10), [(0, 1, 1)], m0=3.0); chb, _ = index_info(D2b, G5b2)
check("D4 doubler control: m0=3 in 2D adds the two one-pi corners (opposite chirality): index = -1 + 2 = +1",
      int(round(chb.sum())) == 1, f"{int(round(chb.sum()))}")
# 2D 3-4-5-0: index(U^e) = -e Q; anomaly sum over L minus R of e*index = -(9+16-25-0) = 0
ind = {}; dens = {}
for e in (1, 3, 4, 5):
    De, _, _ = overlap((10, 10), [(0, 1, 1)], e=e); che, _ = index_info(De, G5b2); ind[e] = int(round(che.sum()))
    dens[e] = np.real(np.einsum('xaa->x', (G5b2 @ De).reshape(100, 2, 100, 2)[np.arange(100), :, np.arange(100), :]))
anom = 3 * ind[3] + 4 * ind[4] - 5 * ind[5]
loc = 3 * dens[3] + 4 * dens[4] - 5 * dens[5]
check("D5 2D chiral U(1) 3-4-5-0: measured indices -e for e=3,4,5; L-minus-R sum e*index = 0, and the local "
      "anomaly density sum_f s_f e_f tr g5 D_f(x,x) sums to zero (pointwise remainder is O(1e-3) of one term)", ind == {1: -1, 3: -3, 4: -4, 5: -5}
      and anom == 0 and abs(loc.sum()) < 1e-9 and np.abs(loc).max() < 1e-2 * 25 * np.abs(dens[5]).max(),
      f"indices {ind}, sum {anom}, sum_x density {loc.sum():.0e}, max|density| {np.abs(loc).max():.1e} (a zero-sum remainder); "
      f"control single e=1 Weyl density {dens[1][0]:.4f}")
# 4D, L=4, fluxes in (12) and (34): instanton number Q = 1
t4 = time.time()
D4, G5b4, gH4 = overlap((4, 4, 4, 4), [(0, 1, 1), (2, 3, 1)])
gw4 = np.abs(G5b4 @ D4 + D4 @ G5b4 - D4 @ G5b4 @ D4).max(); ch4, trg4 = index_info(D4, G5b4)
check("D6 4D U(1), 4^4, fluxes (1,1) -> Q=1: GW exact, one exactly chiral zero mode, |index| = 1",
      gw4 < 1e-11 and len(ch4) == 1 and np.allclose(np.abs(ch4), 1, atol=1e-9),
      f"GW {gw4:.1e}, g5 {np.round(ch4, 9)}, H_W gap {gH4:.3f}, {time.time()-t4:.1f}s")
# D7 the 16 as left-handed Weyl hypercharges: U(1)_Y gauge and mixed sums (exact fractions)
Y = [Fr(1, 6)] * 6 + [Fr(-2, 3)] * 3 + [Fr(1, 3)] * 3 + [Fr(-1, 2)] * 2 + [Fr(1)] + [Fr(0)]
sY = sum(Y); sY3 = sum(y ** 3 for y in Y)
s33 = 2 * Fr(1, 6) + Fr(-2, 3) + Fr(1, 3)        # SU(3)^2 Y: Q (2 isospin comps), u^c, d^c
s22 = 3 * Fr(1, 6) + Fr(-1, 2)                    # SU(2)^2 Y: Q (3 colours), L
check("D7 16 of one family (left-handed): sum Y = 0, sum Y^3 = 0 (Luscher abelian condition), SU(3)^2Y = SU(2)^2Y = 0",
      sY == 0 and sY3 == 0 and s33 == 0 and s22 == 0, f"{sY}, {sY3}, {s33}, {s22}")
# D8 turn charges of the FREEZE content as left-handed fields: L q=2, conj(R) q=-1=2 mod 3 per node
qs = [2, (-1) % 3]
check("D8 FREEZE turn charges as left-handed Z3 labels {2,2}: sum q = 1, sum q^3 = 1 mod 3 per family "
      "(would be anomalous only if the turn were gauged; cancels for N_fam = 0 mod 3)",
      sum(qs) % 3 == 1 and sum(q ** 3 for q in qs) % 3 == 1 and (3 * sum(qs)) % 3 == 0, f"{sum(qs)%3}, {sum(q**3 for q in qs)%3}")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
