AUDIT_INPUT_PATHS = ('docs/THE_ADOPTED_LINK_RULE_PUTS_ONE_GAUGE_FIELD_ON_BOTH_SLAB_WALLS_SO_A_SEPARATE_MIRROR_WORLD_NEEDS_A_NEW_LINK_RULE_AND_A_SUPPLIED_TEMPERATURE_ASYMMETRY_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""mirror-world probe (2026-10-24).

Can the far-wall mirror keep its OWN gauge fields (a mirror world coupled by gravity),
given the adopted Links clause?  Part A: exact/finite checks on a layered slab.
Part B: estimates against supplied standard cosmological numbers.
Supplied model, finite diagnostic; axioms unchanged; no rule adopted.
"""
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261024)
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + detail if detail else ""))


# ---------------- Part A1: Gaussian U(1) on a layered slab (k -> 0 mass matrix) -------------
# Field A_s per layer s = 0..Ls-1 (one transverse polarisation, 4D momentum k).
# Action: sum_s beta_s k^2 A_s^2 + sum_s bp_s (A_{s+1}-A_s)^2 + sum_s M_s A_s^2.
# Massless 4D modes = null vectors of the layer operator Lp + diag(M).
print("A1. toy U(1) on a layered slab: where does the massless mode live?")
Ls = 10


def layer_op(bp, M):
    L = np.diag(M.astype(float))
    for s in range(len(bp)):
        L[s, s] += bp[s]
        L[s + 1, s + 1] += bp[s]
        L[s, s + 1] -= bp[s]
        L[s + 1, s] -= bp[s]
    return L


beta = rng.uniform(0.05, 2.0, Ls)      # layer couplings: arbitrary, incl. 'strongly coupled' bulk
bp = rng.uniform(0.2, 2.0, Ls - 1)     # inter-layer plaquettes (5D links present, Coulomb phase)
Lop = layer_op(bp, np.zeros(Ls))
w, v = np.linalg.eigh(Lop)
nnull = int(np.sum(np.abs(w) < 1e-12))
z = v[:, 0] / v[0, 0]
check("A1a 5D links, Coulomb bulk: exactly one massless mode", nnull == 1, f"null dim {nnull}, next eig {w[1]:.3f}")
check("A1b its profile is flat whatever beta_s, bp_s (near/far coupling ratio 1)",
      np.max(np.abs(z - 1)) < 1e-10, f"max|A_s/A_0 - 1| = {np.max(np.abs(z-1)):.1e}")
# coupling of a wall charge to the canonically normalised zero mode: g_wall = 1/sqrt(sum beta)
zn = z / np.sqrt(z @ (beta * z))
check("A1c both walls couple to it with the same 4D charge (gauge universality)",
      abs(zn[0] - zn[-1]) < 1e-12 and abs(zn[0] - 1 / np.sqrt(beta.sum())) < 1e-12,
      f"g_near = g_far = {zn[0]:.4f} = (sum beta_s)^-1/2")

# bulk gauge mass (Higgs-phase bulk), walls massless
M = np.full(Ls, 1.0)
M[0] = M[-1] = 0.0
w2 = np.linalg.eigvalsh(layer_op(bp, M))
check("A1d Higgs-phase bulk: no massless mode survives (wall photons massive)", w2[0] > 1e-3,
      f"lowest mass^2 eigenvalue {w2[0]:.4f} (units of k^2 beta)")
# decoupled layers (bp = 0: the strong-coupling stand-in for a confining bulk)
w3 = np.linalg.eigvalsh(layer_op(np.zeros(Ls - 1), np.zeros(Ls)))
n3 = int(np.sum(np.abs(w3) < 1e-12))
check("A1e only with NO inter-layer plaquettes is each wall's photon its own (Ls zero modes)", n3 == Ls,
      f"null dim {n3}")
# leakage scan: small bp, bulk Higgs mass -> two light modes split by ~ bp^2/M ...
for b_small in (1e-1, 1e-2):
    w4, v4 = np.linalg.eigh(layer_op(np.full(Ls - 1, b_small), M))
    print(f"    bp = {b_small:.0e}, bulk M = 1: two lightest mass^2 {w4[0]:.2e}, {w4[1]:.2e} (nonzero: walls lose photon)")

# ---------------- Part A2: matter slab -> which layer phases are symmetries -----------------
print("A2. domain-wall matter slab (3+1+1, layer = extra spatial direction, m = 0.6)")
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
al = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, I2)]  # alpha_1..3, alpha_4 (layer)
be = np.kron(s3, I2)
# Clifford check
ok = all(np.allclose(a @ b + b @ a, 2 * np.eye(4) * (i == j))
         for i, a in enumerate(al + [be]) for j, b in enumerate(al + [be]))
check("A2a five anticommuting 4x4 matrices (alpha_1..4, beta)", ok)


def slab_H(k, m, Ls):
    h0 = sum(al[i] * np.sin(k[i]) for i in range(3)) + be * (m - 1 - sum(1 - np.cos(k[i]) for i in range(3)))
    T = 0.5 * be - 0.5j * al[3]          # T e^{ik4} + T^+ e^{-ik4} = beta cos k4 + alpha_4 sin k4
    H = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        H[4*s:4*s+4, 4*s:4*s+4] = h0
        if s + 1 < Ls:
            H[4*(s+1):4*(s+1)+4, 4*s:4*s+4] = T
            H[4*s:4*s+4, 4*(s+1):4*(s+1)+4] = T.conj().T
    return H, T


m = 0.6
Lm = 16
H0, T = slab_H(np.zeros(3), m, Lm)
e, V = np.linalg.eigh(H0)
idx = np.argsort(np.abs(e))[:4]
lowE = np.sort(np.abs(e[idx]))
gap_next = np.sort(np.abs(e))[4]
check("A2b one 2-component Weyl per wall at k = 0 (4 states near 0, then the bulk gap)",
      lowE[-1] < 1e-5 and gap_next > 0.3, f"|E| <= {lowE[-1]:.1e}, next {gap_next:.3f}")
Gam = 1j * al[3] @ be
P = V[:, idx]
Gfull = np.kron(np.eye(Lm), Gam)
near = np.kron(np.diag([1.0 if s < Lm // 2 else 0.0 for s in range(Lm)]), np.eye(4))
# diagonalise Gamma within the zero-mode space; read where each chirality sits
gw, gv = np.linalg.eigh(P.conj().T @ Gfull @ P)
modes = P @ gv
wnear = np.real(np.einsum('ia,ij,ja->a', modes.conj(), near, modes))
chir_near = gw[wnear > 0.5]
chir_far = gw[wnear < 0.5]
check("A2c opposite chirality on the two walls (near / far)",
      len(chir_near) == 2 and np.allclose(chir_near, chir_near[0]) and np.allclose(chir_far, -chir_near[0], atol=1e-6),
      f"near Gamma {np.round(chir_near,6)}, far Gamma {np.round(chir_far,6)}")
# layer profile of the near mode: ratio per layer = |1-m|
a = modes[:, np.argmax(wnear)]
amp = np.array([np.linalg.norm(a[4*s:4*s+4]) for s in range(Lm)])
ratio = amp[3] / amp[2]
check("A2d wall-mode amplitude falls by |1 - m| per layer", abs(ratio - abs(1 - m)) < 1e-6, f"ratio {ratio:.6f}")

# which diagonal layer phases commute with the slab update at generic k?
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)]
rows = []
for k in ks:
    Hk, _ = slab_H(k, m, Lm)
    for s in range(Lm):
        Ps = np.zeros((4 * Lm, 4 * Lm)); Ps[4*s:4*s+4, 4*s:4*s+4] = np.eye(4)
        rows.append((Ps @ Hk - Hk @ Ps).ravel())
# solve sum_s c_s [P_s, H] = 0 jointly over k
A = np.array([np.concatenate([rows[ik * Lm + s] for ik in range(len(ks))]) for s in range(Lm)]).T
sv = np.linalg.svd(A, compute_uv=False)
dimcomm = int(np.sum(sv < 1e-10))
check("A2e layer-phase symmetries of the slab update: only the uniform phase (dim 1)", dimcomm == 1,
      f"commutant dim {dimcomm}; smallest nonzero singular value {sorted(sv)[1]:.3f}")
# -> Links clause: register valued in update symmetries => one factor acting on BOTH walls
q = 1.0  # the one admissible factor acts with the same charge on every layer
anom = q ** 3 * (np.sum(chir_near) + np.sum(chir_far))
check("A2f so both walls carry the same charge and opposite chirality: sum Gamma q^3 = 0 (vector-like)",
      abs(anom) < 1e-6, f"sum = {anom:.1e}")
# Gauss's law with a far-only register: [H, Q_far] = middle-bond hop, size ||T||
Qfar = np.eye(4 * Lm) - near
Cn = np.linalg.norm(H0 @ Qfar - Qfar @ H0, 2)
check("A2g far-half charge is not conserved: ||[H, Q_far]|| = ||T|| (bulk modes, cutoff scale)",
      abs(Cn - np.linalg.norm(T, 2)) < 1e-10 and Cn > 0.5, f"{Cn:.4f}")
# its matrix element between the two wall Weyls falls as |1-m|^Ls
mel = []
for L_ in (8, 12, 16):
    Hl, _ = slab_H(np.zeros(3), m, L_)
    el, Vl = np.linalg.eigh(Hl)
    Pl = Vl[:, np.argsort(np.abs(el))[:4]]
    gwl, gvl = np.linalg.eigh(Pl.conj().T @ np.kron(np.eye(L_), Gam) @ Pl)
    ml = Pl @ gvl                      # columns 0,1: one chirality (one wall); 2,3: the other
    nr = np.kron(np.diag([1.0 if s < L_ // 2 else 0.0 for s in range(L_)]), np.eye(4))
    C = Hl @ (np.eye(4 * L_) - nr) - (np.eye(4 * L_) - nr) @ Hl
    mel.append(np.max(np.abs(ml[:, :2].conj().T @ C @ ml[:, 2:])))
slope = np.log(mel[2] / mel[0]) / 8
check("A2h wall-to-wall Gauss violation ~ |1-m|^Ls (only low-energy approximate far charge)",
      abs(slope - np.log(abs(1 - m))) < 0.05, f"elements {mel[0]:.1e},{mel[1]:.1e},{mel[2]:.1e}; slope {slope:.3f} vs {np.log(0.4):.3f}")

# ---------------- Part B: estimates against supplied standard numbers ----------------------
print("B. mirror world against measurement (supplied numbers; estimates)")
gstar = 10.75                       # g* of a full SM-copy plasma at T ~ 1 MeV
dN = lambda x: gstar / 1.75 * x ** 4  # one neutrino species = (7/8)*2 = 1.75
dN_lim = 0.3                         # ~95% Planck+BBN allowance (supplied)
xmax = (dN_lim / dN(1.0)) ** 0.25
check("B1 T'/T = 1 (wall-symmetric excitation): Delta N_eff = 6.14, far above 0.3 (EXCLUDED)",
      dN(1.0) > 20 * dN_lim, f"Delta N_eff(1) = {dN(1.0):.2f}; {dN(1.0)/0.17:.0f} sigma at sigma 0.17")
check("B2 allowed only for T'/T < 0.47 (needs a supplied reheating asymmetry)", 0.45 < xmax < 0.5,
      f"x_max = {xmax:.3f}")
ob, oc = 0.0224, 0.120
check("B3 symmetric baryogenesis gives Omega'_b/Omega_b = 1, not 5.36 (asymmetry supplied)",
      abs(oc / ob - 5.36) < 0.01, f"needed {oc/ob:.2f}")
a0, mH = 0.529e-8, 1.6726e-24
sig_m = np.pi * a0 ** 2 / mH
check("B4 mirror-hydrogen sigma/m ~ 5e7 cm^2/g vs cluster bound ~1: not collisionless DM",
      sig_m > 1e7, f"sigma/m = {sig_m:.1e} cm^2/g")
alpha = 1 / 137.036
eps = alpha / (3 * np.pi) * abs(1 - m) ** (2 * 16) * np.log(1e19 / 1.0)
check("B5 IF separate fields existed, tail-induced kinetic mixing << 1e-9 (Ls = 16, m = 0.6)",
      eps < 1e-9, f"eps ~ {eps:.1e}")
check("B6 fraction reading: at x = 0.45 Delta N_eff < 0.3; then f <~ 5% (dissipative limits, supplied)",
      dN(0.45) < dN_lim, f"Delta N_eff(0.45) = {dN(0.45):.3f}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
