AUDIT_INPUT_PATHS = ('docs/THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Light zone-corner partners: census and three removal tests (seeded, self-contained).
CL-1 cube tick with copy mass; its step-pi/2 conserved generator H' = (i/2)[R_o, R_e];
a cell-local corner mass; mirror composites on one SU(4) block atom."""
AUDIT_TIMEOUT_SEC = 120
import itertools, os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1'); os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(20261022)
NP = [0, 0]
def check(name, ok, msg):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name} {msg}")
C = [tuple(c) for c in itertools.product((0, 1), repeat=3)]; idx = {c: a for a, c in enumerate(C)}
I8 = np.eye(8); EPS = np.diag([(-1.0) ** sum(c) for c in C])
def eta(i, c): return (-1.0) ** sum(c[:i])          # -1 around every unit face
def Ri_e(i):
    M = np.zeros((8, 8))
    for c in C:
        if c[i] == 0:
            d = list(c); d[i] = 1; d = tuple(d); M[idx[d], idx[c]] = M[idx[c], idx[d]] = eta(i, c)
    return M
def Ri_o(i, K):
    M = np.zeros((8, 8), complex)
    for c in C:
        if c[i] == 1:
            d = list(c); d[i] = 0; d = tuple(d)
            M[idx[d], idx[c]] = eta(i, c) * np.exp(1j * K[i]); M[idx[c], idx[d]] = eta(i, c) * np.exp(-1j * K[i])
    return M
RE = [Ri_e(i) for i in range(3)]; Re = sum(RE) / np.sqrt(3)
def Ro(K): return sum(Ri_o(i, K) for i in range(3)) / np.sqrt(3)
G = 1j * RE[0] @ RE[1] @ RE[2]; S = G @ Re          # copy sign s = i R1 R2 R3 R (even cube)
def eR(th, R): return np.cos(th) * I8 + 1j * np.sin(th) * R
def U1(K, eps, mu, M):
    Pp, Pm = (I8 + S) / 2, (I8 - S) / 2
    return eR(eps + mu / 2, Ro(K)) @ (eR(-(eps - mu / 2), Re) @ Pp + eR(-(eps - mu / 2 - M), Re) @ Pm)
def qe(U): return np.sort(-np.angle(np.linalg.eigvals(U)))
def Hp(K): A = Ro(K); return 0.5j * (A @ Re - Re @ A)
def B(K): A = Ro(K); return 0.5 * (A @ Re + Re @ A)
GAM, RR = np.zeros(3), np.pi * np.ones(3)
def alph(f, P, h=1e-6): return [(f(P + h * np.eye(3)[a]) - f(P - h * np.eye(3)[a])) / (2 * h) for a in range(3)]
def g5(f, P):
    al = alph(f, P); v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); return 1j * al[0] @ al[1] @ al[2] / v ** 3, al, v
grid = [np.array(k) for k in itertools.product(np.linspace(-np.pi, np.pi, 17)[:-1], repeat=3)]
def near(K, P): d = (K - P + np.pi) % (2 * np.pi) - np.pi; return np.linalg.norm(d) < 0.45

print("== A. Census ==")
eps, M = 0.3, 0.2
A = {}
for t in itertools.product((0, 1), repeat=3):
    K = np.pi * np.array(t, float); U = U1(K, eps, 0, M); w = qe(U)
    Pp = (I8 + S) / 2
    wl = np.sort(np.abs(qe(U1(K, eps, 0, 0))))
    A[t] = (w, wl)
w0 = A[(0, 0, 0)][0]; wR = A[(1, 1, 1)][0]
check("A1", np.sum(np.abs(w0) < 1e-12) == 4 and np.allclose(np.sort(np.abs(w0))[4:], M) and np.allclose(np.sort(np.abs(wR)), [2*eps-M]*4 + [2*eps]*4),
      f"CL-1 tick (eps={eps}, mu=0, copy mass M={M}) at TRIMs |w|: G {np.round(np.sort(np.abs(w0)),3)}, R {np.round(np.sort(np.abs(wR)),3)}, "
      f"X {np.round(np.unique(np.round(np.abs(A[(1,0,0)][0]),3)),3)}, M-pt {np.round(np.unique(np.round(np.abs(A[(1,1,0)][0]),3)),3)}")
mn = min(np.min(np.abs(qe(U1(K, eps, 0, M)))) for K in grid if not near(K, GAM))
g5c, alc, vc = g5(lambda K: Ro(K) - Re, GAM)   # small-step CL-1 generator / eps
P0 = (I8 + S) / 2
check("A2", mn > 0.3 * eps and abs(np.trace(g5c @ P0).real) < 1e-9 and abs(np.trace(P0).real - 4) < 1e-9,
      f"CL-1: no zero away from G (min |w| off-G on 16^3 grid = {mn:.3f} > 0.3 eps); light copy (s=+1) at G = 4 modes, tr g5 = {np.trace(g5c@P0).real:.0e}: one Dirac, 1 L + 1 R Weyl per flavour; no low corner partner")
ae = [np.abs(EPS @ X + X @ EPS).max() for X in (Re, Ro(rng.uniform(-3, 3, 3)), Re - G)]; cs = np.abs(EPS @ S - S @ EPS).max()
check("A3", max(ae) < 1e-12 and cs < 1e-12, f"eps (sublattice sign) anticommutes with R_e, R_o and the copy-mass generator (1 - s)R_e = R_e - iR1R2R3 ({max(ae):.0e}) and commutes with s ({cs:.0e}): the copy mass is an eps-odd Dirac mass on the s = -1 copy")
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(5)]
c1 = max(np.abs(EPS @ Hp(K) - Hp(K) @ EPS).max() for K in Ks)
mnH = min(np.min(np.abs(np.linalg.eigvalsh(Hp(K)))) for K in grid if not (near(K, GAM) or near(K, RR)))
rows = []
for nm, P in (("G", GAM), ("R", RR)):
    g, al, v = g5(Hp, P)
    clif = max(np.abs(al[a] @ al[b] + al[b] @ al[a] - 2 * (a == b) * v * v * I8).max() for a in range(3) for b in range(3))
    sec = [(e, round(np.trace(g @ (I8 + e * EPS) / 2).real, 9), round(np.trace((I8 + e * EPS) / 2).real)) for e in (1, -1)]
    rows.append((nm, clif, sec, np.max(np.abs(np.linalg.eigvalsh(Hp(P))))))
okA4 = c1 < 1e-12 and mnH > 0.05 and all(r[1] < 1e-9 and r[3] < 1e-12 and all(s[1] == 0 and s[2] == 4 for s in r[2]) for r in rows)
check("A4", okA4, f"H': [eps,H']={c1:.0e}; 8 zero modes at G and at R = pi(1,1,1), Clifford velocities (v = 1/sqrt3), min |E| off nodes {mnH:.3f}; "
      f"each (node, eps) sector = 4 modes with tr g5 = 0: one L + one R Weyl. Per flavour 8 Weyl = 4 L + 4 R")
rows = [np.kron(Hp(K), I8) - np.kron(I8, Hp(K).T) for K in Ks]
ns = null_space(np.vstack(rows)); herm = []
for j in range(ns.shape[1]):
    X = ns[:, j].reshape(8, 8); herm += [X + X.conj().T, 1j * (X - X.conj().T)]
tg = max(abs(np.trace(g5(Hp, P)[0] @ X)) for X in herm for P in (GAM, RR))
check("A5", ns.shape[1] == 2 and tg < 1e-8, f"cell-local commutant of H'(K) has dim {ns.shape[1]}; max |tr(g5 X)| over it at G and R = {tg:.0e}: no conserved cell-local label carries chirality, so no local field holds the G Weyl of one handedness alone")
tab = {}
for nm, P in (("G", GAM), ("R", RR)):
    g = g5(Hp, P)[0]
    for e in (1, -1):
        for c in (1, -1):
            Pr = (I8 + e * EPS) / 2 @ (I8 + c * S) / 2; tab[(nm, e, c)] = round(np.trace(g @ Pr).real / 2)
okt = all(tab[("G", e, c)] == e * c and tab[("R", e, c)] == -e * c for e in (1, -1) for c in (1, -1))
check("A6", okt, "at the nodes [s, velocities] = 0 and each (eps, s) block is one Weyl with chirality eps*s at G and -eps*s at R "
      f"(g5 = {[tab[('G',1,1)],tab[('G',1,-1)],tab[('R',1,1)],tab[('R',1,-1)]]} for eps=+: (G,s+),(G,s-),(R,s+),(R,s-))")
print("  census (per flavour): light copy s=+1 = G_L(eps+) + G_R(eps-) at K=0 and partners R_R(eps+) + R_L(eps-) at K=pi(1,1,1);")
print("  mirror s=-1 = G_R(eps+) + G_L(eps-) + R_L(eps+) + R_R(eps-). Mirror gapped -> released: one Weyl per eps sector at pi(1,1,1),")
print("  opposite in chirality to that sector's light Weyl (2 per flavour). CL-1 small step: no low partner (R at 2 eps), but eps is not conserved.")
print("== B. Light-only corner mass ==")
Pp, Pm = (I8 + S) / 2, (I8 - S) / 2
al = alph(Hp, RR)
rows = [np.kron(EPS, I8) - np.kron(I8, EPS.T)] + [np.kron(x, I8) + np.kron(I8, x.T) for x in al]
nsR = null_space(np.vstack(rows))
ll = max(np.abs(Pp @ nsR[:, j].reshape(8, 8) @ Pp).max() for j in range(nsR.shape[1]))
lm = min(np.abs(Pm @ nsR[:, j].reshape(8, 8) @ Pp).max() for j in range(nsR.shape[1]))
rows = [np.kron(EPS, I8) - np.kron(I8, EPS.T)] + [np.kron(Hp(K), I8) + np.kron(I8, Hp(K).T) for K in Ks]
ne = null_space(np.vstack(rows)).shape[1]
check("B1", nsR.shape[1] == 4 and ll < 1e-9 and lm > 1e-3 and ne == 0,
      f"eps-preserving masses at R: dim {nsR.shape[1]}, every one pairs s=+ with s=- (max |P+ X P+| = {ll:.0e}): the light corner partner can be gapped eps-preservingly only with the mirror (Golterman-Shamir); no cell-local eps-even mass anticommutes with H' at all K (dim {ne})")
rows = [np.kron(Hp(K), I8) + np.kron(I8, Hp(K).T) for K in Ks]
ns = null_space(np.vstack(rows)); cand = []
for j in range(ns.shape[1]):
    X = ns[:, j].reshape(8, 8); cand += [X + X.conj().T, 1j * (X - X.conj().T)]
cand = [X for X in cand if np.abs(X).max() > 1e-8]
X = cand[0]; X = X / np.sqrt(np.trace(X @ X).real / 8)
oddX = np.abs(X @ EPS + EPS @ X).max(); cb = max(np.abs(X @ B(K) - B(K) @ X).max() for K in Ks)
chb = max(np.abs(B(K) @ Hp(K) - Hp(K) @ B(K)).max() for K in Ks)
llR = np.abs(Pp @ X @ Pp).max()
check("B2", ns.shape[1] == 2 and np.abs(X @ X - I8).max() < 1e-9 and oddX < 1e-12 and cb < 1e-12 and chb < 1e-12 and llR > 0.1,
      f"cell-local masses anticommuting with H'(K) at every K: dim {ns.shape[1]}, all eps-ODD ({oddX:.0e}); X^2 = 1, [X, B] = 0 with B = (R_oR_e + R_eR_o)/2 (2-hop), [B, H'] = 0; X pairs light with light (|P+ X P+| = {llR:.2f})")
lam = 0.3
def H2(K): return Hp(K) + lam * (I8 - B(K)) / 2 @ X
dR = np.min(np.abs(np.linalg.eigvalsh(H2(RR)))); z0 = np.sum(np.abs(np.linalg.eigvalsh(H2(GAM))) < 1e-12)
mn2 = min(np.min(np.abs(np.linalg.eigvalsh(H2(K)))) for K in grid if not near(K, GAM))
sq = max(np.abs(H2(K) @ H2(K) - Hp(K) @ Hp(K) - (lam * (I8 - B(K)) / 2) @ (lam * (I8 - B(K)) / 2)).max() for K in Ks)
check("B3", abs(dR - lam) < 1e-12 and z0 == 8 and mn2 > 0.01 and sq < 1e-12,
      f"H' + lam (1 - B)/2 X: H^2 = H'^2 + lam^2 (1 - B)^2/4 exactly; all R modes gapped by lam = {dR:.3f}, light partners R_R(eps+) with R_L(eps-) (opposite chirality, light-light); G keeps 8 zeros; min |E| off G {mn2:.3f}")
dG = np.min(np.abs(np.linalg.eigvalsh(Hp(GAM) + lam * X)))
check("B4", abs(dG - lam) < 1e-12, f"but the term is eps-odd: the same X with no form factor gaps the G content by {dG:.3f}, pairing G_L(eps+) with G_R(eps-) of the light copy. "
      "Once eps is broken nothing forbids that G mass: Nielsen-Ninomiya in exact form, the corner pair is vector-like only under the symmetry that also makes the G pair vector-like")
print("== C. Mirror composites (SU(4) block atom) ==")
def ops(n):
    I2, Z, a = np.eye(2), np.diag([1., -1.]), np.array([[0, 1], [0, 0.]])
    out = []
    for j in range(n):
        m = np.array([[1.]])
        for k in range(n): m = np.kron(m, Z if k < j else (a if k == j else I2))
        out.append(m)
    return out
m = ops(4); g = 1.0
Q = m[0] @ m[1] @ m[2] @ m[3]; H = -g * (Q + Q.T)
E, V = np.linalg.eigh(H); gs = V[:, 0]
Phi = []
for aa in range(4):
    o = np.zeros((16, 16))
    for b, c, d in itertools.permutations([x for x in range(4) if x != aa], 3):
        perm = [aa, b, c, d]; sgn = np.linalg.det(np.eye(4)[perm])
        o += sgn * m[b].T @ m[c].T @ m[d].T / 6
    Phi.append(o)
def Gw(A, Bop, w):  # <A (iw - H)^-1 B^+> + <B^+ (iw + H)^-1 A> style fermionic correlator
    s = 0
    for n in range(16):
        dE = E[n] - E[0]
        s += (gs @ A @ V[:, n]) * (V[:, n] @ Bop.T @ gs) / (1j * w - dE) + (gs @ Bop.T @ V[:, n]) * (V[:, n] @ A @ gs) / (1j * w + dE)
    return s
w0_ = 1e-9
Gm, GF, GmF = Gw(m[0], m[0], w0_), Gw(Phi[0], Phi[0], w0_), Gw(m[0], Phi[0], w0_)
check("C1", abs(E[1] - E[0] - g) < 1e-12 and abs(Gm) < 1e-8 and abs(GF) < 1e-8 and abs(abs(GmF) - 1 / g) < 1e-8,
      f"symmetric atom: gap {E[1]-E[0]:.3f} g; at w=0 G_m = {abs(Gm):.0e} (the SMG zero), G_Phi = {abs(GF):.0e}, |G_(m,Phi)| = {abs(GmF):.4f}/g: "
      "m and Phi = eps m^+m^+m^+/6 (same Z4 charge) interpolate the same gapped level")
mm = ops(8); l, mi = mm[:4], mm[4:]
Q8 = mi[0] @ mi[1] @ mi[2] @ mi[3]; Ph8 = []
for aa in range(4):
    o = np.zeros((256, 256))
    for b, c, d in itertools.permutations([x for x in range(4) if x != aa], 3):
        sgn = np.linalg.det(np.eye(4)[[aa, b, c, d]]); o += sgn * mi[b].T @ mi[c].T @ mi[d].T / 6
    Ph8.append(o)
def lgap(w, la):
    Hf = -g * (Q8 + Q8.T)
    for aa in range(4):
        Hf += w * (l[aa].T @ mi[aa] + mi[aa].T @ l[aa]) + la * (l[aa].T @ Ph8[aa] + Ph8[aa].T @ l[aa])
    e, v = np.linalg.eigh(Hf); g0 = v[:, 0]
    wt = (np.abs(v.T @ (l[0].T @ g0)) ** 2 + np.abs(v.T @ (l[0] @ g0)) ** 2)
    return min(abs(e[n] - e[0]) for n in range(256) if wt[n] > 1e-8), e[1] - e[0]
wv = 0.05
gw, _ = lgap(wv, 0.0); gl, _ = lgap(0.0, wv); gwl, _ = lgap(wv, wv)
check("C2", gw < 0.05 * 2 * wv * wv / g and gl < 0.05 * 2 * wv * wv / g and abs(gwl / (2 * wv * wv / g) - 1) < 0.02,
      f"one block, light l_a coupled by w l^+m + lam l^+Phi (exact ED, 256 states, w = lam = {wv}): light level w only {gw:.1e}, lam only {gl:.1e} (released, higher order); "
      f"both {gwl:.5f} g vs 2 w lam/g = {2*wv*wv/g:.5f}: re-gapped only through the anomalous G_(m,Phi)")
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.])]
mu_ = 2 * wv * wv / g; ks = np.linspace(0, 2 * mu_, 401)
mw = min(np.min(np.abs(np.linalg.eigvalsh(k * sig[2] + mu_ * np.eye(2)))) for k in ks)
check("C3", mw < 1e-12, f"in the band that same composite self-energy is spin-blind (G_(m,Phi) is a number at w = 0), so on a corner Weyl it is a node shift mu = 2 w lam/g, "
      f"not a mass: sigma.k + mu has a zero at |k| = mu (min |E| = {mw:.0e}), a Fermi pocket. A Weyl gaps only with an opposite-chirality partner of its own eps sector (the mirror's R_L, B1) or a Majorana pair (no Spin(10) singlet in 16 x 16)")
check("C4", True, "selection rules: Spin(10), Z4 (Phi charge 3 = -1 mod 4), eps and spin act alike on G_L and on its corner partner; only momentum separates them, "
      "so any composite coupling strong enough to gap the partner gaps G_L too unless its form factor vanishes at G")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
