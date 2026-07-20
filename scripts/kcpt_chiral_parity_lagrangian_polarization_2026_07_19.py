#!/usr/bin/env python3
"""KCPT Unit 11 exact Lagrangian-polarization runner.

Reads the landed Units 8/9/10 objects on the L=4, N=64 staggered lattice through
standard symplectic / Kaehler geometry.  Writing C^64 = L_+ (+) L_- for the +-1
eigenspaces of the staggered chiral parity S_eps = diag((-1)^{x1+x2+x3}) (Unit 9),
and taking the Unit-10 symplectic convention omega(x,y) = g(J_full x,y) with
g = I_64 (matrix omega = J_full^T g = -J_full), it verifies:

  T1  S_eps is a real involution; L_+ , L_- are the even/odd staggered-parity site
      sets, dim 32 each, L_+ (+) L_- = C^64.                        [G1, G2]
  T2  each L_+- is LAGRANGIAN for omega: the diagonal parity blocks of omega (hence
      of J_full) vanish -- this is Unit 9's T4 S_eps J_full S_eps = -J_full written
      in parity blocks; omega is nondegenerate.                     [G3, G4, G5, G6]
  T3  J_full anticommutes with S_eps, so it EXCHANGES the two Lagrangian planes as a
      rank-32 isomorphism L_+ -> L_- (the Kaehler polarization intertwiner).
                                                                    [G7, G8, G9, G10]
  T4  S_eps is ANTISYMPLECTIC (S_eps^T omega S_eps = -omega) and acts on h = g + i*omega
      as the reality/CP conjugation h -> conj(h), swapping the +-i eigenspaces of J_full.
                                                                [G11, G12, G13, G14, G19]
  T5  every element of the order-768 ambient group G_amb preserves the unordered pair
      {L_+, L_-}; the subgroup fixing each plane is the centralizer C_G_amb(S_eps) of
      order 384, giving an index-2 grading (preserve vs swap).      [G15, G16]
  T6  the sibling J_alt = J_ker - J_bulk is also reversed by S_eps, so it exchanges the
      SAME L_+-; the polarization is common to both orientations, only the intertwiner
      differs (J_full - J_alt = 2 J_bulk != 0).                     [G17a, G17b, G17c]

Every "vanishing block" gate is sliced from an INDEPENDENTLY built matrix (J_full from
the D2/V8/J64 shell construction; S_eps from coords), never a matrix set to zero, and is
paired with a discriminating rejector (G5, G8, G13, G17c, G18) that FAILS for a
trivial/wrong object.  Load-bearing block identities are exact-rational and land at 0.0;
the float gates (eig/rank/square) are redundant and tagged in their descriptions.
"""
import itertools
import os
import numpy as np

L, N = 4, 64
TOL0 = 1e-12      # rational-zero blocks
TOL_EIG = 1e-8    # eigen / rank
TOLREJ = 1e-6     # rejector floor

DOCS = os.environ.get("KCPT_DOCS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"
SELF_NOTE = "KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md"

PASS = FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    PASS, FAIL = PASS + (1 if ok else 0), FAIL + (0 if ok else 1)
    print(f"{'PASS' if ok else 'FAIL'} {tag} - {desc}")
    return ok


def note_text(basename):
    try:
        with open(os.path.join(DOCS, basename), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def nrm(X):
    return float(np.max(np.abs(X)))


# ---------------- construction (self-contained; mirrors the landed Unit-9 runner) ----
def idx(a, b, c):
    return (a * L + b) * L + c


coords = np.zeros((N, 3), dtype=np.int64)
for a in range(L):
    for b in range(L):
        for c in range(L):
            coords[idx(a, b, c)] = (a, b, c)


def eta_mu(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** int(x[0])
    return (-1) ** int(x[0] + x[1])


e = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
D2 = np.zeros((N, N), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for mu in range(3):
        D2[i, idx(*((x + e[mu]) % L))] += eta_mu(mu, x)
        D2[i, idx(*((x - e[mu]) % L))] -= eta_mu(mu, x)

SUBSETS = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
sidx = {frozenset(S): k for k, S in enumerate(SUBSETS)}
FULL = frozenset({0, 1, 2})
V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))


def sgn_subset(S):
    Sset = frozenset(S)
    return ((-1) ** len(Sset & frozenset({0, 2}))) * (1 if 1 in Sset else -1)


J64 = np.zeros((8, 8), dtype=np.int64)
for k, S in enumerate(SUBSETS):
    T = frozenset(S) ^ frozenset({1})
    J64[sidx[T], k] = 64 * sgn_subset(S)

Jker_int = V8 @ J64 @ V8.T                       # == 64^2 * J_ker

M = D2 @ D2
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * np.eye(N, dtype=np.int64) for m in range(4)]
Q = []
for m in range(4):
    P = np.eye(N, dtype=np.int64)
    for mp in range(4):
        if mp != m:
            P = P @ Fac[mp]
    Q.append(P)
Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)                                 # (384, -128, 128, -384)

# float total complex structure and its orientation sibling
D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulk = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfull = Jkerf + Jbulk
Jalt = Jkerf - Jbulk

# the chiral parity and its parity planes
eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)], dtype=np.int64)
Seps = np.diag(eps)
Sf = Seps.astype(float)
Ip = np.where(eps > 0)[0]                         # L_+  standard-basis index set
Im = np.where(eps < 0)[0]                         # L_-  standard-basis index set

# the Unit-10 Kaehler data (built directly from J_full)
g = np.eye(N)
w = -Jfull                                        # omega, matrix J_full^T g = -J_full
h = g.astype(complex) + 1j * w.astype(complex)    # h = g + i*omega


# ---------------- G_amb reconstruction (mirror the Unit-9 runner) --------------------
def perm(fmap):
    P = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P


UR = perm(lambda x: (x[1], x[2], x[0]))
U2 = perm(lambda x: (-x[1], -x[0], -x[2]))
STAB = np.eye(N, dtype=np.int64)
TR = {t: perm(lambda x, t=t: (x[0] - t[0], x[1] - t[1], x[2] - t[2]))
      for t in itertools.product(range(L), repeat=3)}


def signfield(bits):
    a1, a2, a3, b12, b13, b23 = bits
    d = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x1, x2, x3 = coords[i]
        expo = a1 * x1 + a2 * x2 + a3 * x3 + b12 * x1 * x2 + b13 * x1 * x3 + b23 * x2 * x3
        d[i] = (-1) ** int(expo)
    return d


ALLBITS = list(itertools.product([0, 1], repeat=6))
SF = {bits: signfield(bits) for bits in ALLBITS}
BASES = {"stab": STAB, "U2": U2, "UR": UR}


def eqm(a, b):
    return np.array_equal(a, b)


def closure_amb(gs):
    gs = [g0.copy() for g0 in gs]
    elts = {g0.tobytes(): g0 for g0 in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for xg in frontier:
            for g0 in gs:
                p = xg @ g0
                key = p.tobytes()
                if key not in elts:
                    elts[key] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


commuting = []
for name, base in BASES.items():
    for bits in ALLBITS:
        dd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = dd @ base @ TR[t]
            if eqm(U @ D2, D2 @ U):
                commuting.append(U.copy())
Gamb = closure_amb(commuting)

# =========================================================================== gates ===
# T1 -- real parity polarization
g1 = (eqm(Seps @ Seps, np.eye(N, dtype=np.int64))
      and eqm(Seps.T @ Seps, np.eye(N, dtype=np.int64))
      and round(float(np.trace(Seps))) == 0
      and set(np.unique(eps).tolist()) <= {-1, 1})
gate("G1", g1, "S_eps real orthogonal involution: S^2=I, S^T S=I, trace=0, entries in {-1,+1}")

g2 = (len(Ip) == 32 and len(Im) == 32 and sorted(Ip.tolist() + Im.tolist()) == list(range(N)))
gate("G2", g2, "dim L_+ = dim L_- = 32 and L_+ (+) L_- partitions the 64 basis sites")

# T2 -- each parity plane is Lagrangian for omega = -J_full
gate("G3", nrm(Sf @ Jfull @ Sf + Jfull) < TOL0,
     "landed Unit-9 T4: ||S_eps J_full S_eps + J_full|| < 1e-12")
gate("G4", nrm(w[Ip][:, Ip]) < TOL0 and nrm(w[Im][:, Im]) < TOL0,
     "LAGRANGIAN: omega vanishes on L_+ and on L_- (diagonal parity blocks = 0)")
gate("G5", nrm(w[Ip][:, Im]) > TOLREJ,
     "REJECTOR: off-diagonal L_+ x L_- block of omega is nonzero (vanishing is block-specific)")
detw = float(np.linalg.det(w))
gate("G6", abs(round(detw)) >= 1,
     f"omega nondegenerate: |round(det omega)| = {abs(round(detw))} >= 1")

# T3 -- J_full exchanges the two Lagrangian planes
gate("G7", nrm(Sf @ Jfull + Jfull @ Sf) < TOL0,
     "J_full anticommutes with S_eps: ||S_eps J_full + J_full S_eps|| < 1e-12")
gate("G8", nrm(Sf @ Jfull - Jfull @ Sf) > TOLREJ,
     "REJECTOR: ||S_eps J_full - J_full S_eps|| nonzero (genuine anticommutation, not both-zero)")
gate("G9", nrm(Jfull[Ip][:, Ip]) < TOL0 and nrm(Jfull[Im][:, Im]) < TOL0,
     "J_full diagonal parity blocks vanish: J(L_+) subset L_-, J(L_-) subset L_+")
rk = int(np.linalg.matrix_rank(Jfull[Im][:, Ip], tol=1e-9))
gate("G10", rk == 32, f"J_full: L_+ -> L_- is a rank-{rk} isomorphism (== 32)")

# T4 -- S_eps antisymplectic reality involution
gate("G11", nrm(Sf.T @ w @ Sf + w) < TOL0,
     "ANTISYMPLECTIC: ||S_eps^T omega S_eps + omega|| < 1e-12")
gate("G12", nrm(Sf.T @ h @ Sf - np.conj(h)) < TOL0,
     "REALITY/CP: ||S_eps^T h S_eps - conj(h)|| < 1e-12 (h -> conj(h) = g - i*omega)")
gate("G13", nrm(h - np.conj(h)) > TOLREJ,
     "REJECTOR: ||h - conj(h)|| nonzero (omega != 0, so conj(h) != h)")
evals, evecs = np.linalg.eig(Jfull)
sel = np.abs(evals - 1j) < TOL_EIG
V = evecs[:, sel]
SV = Sf.astype(complex) @ V
gate("G14", V.shape[1] == 32 and nrm(Jfull @ SV - (-1j) * SV) < TOL_EIG,
     f"ANTI-HOLOMORPHIC: +i eigenspace dim {V.shape[1]}==32; S_eps sends it to the -i eigenspace (< 1e-8)")

# T5 -- ambient index-2 grading
cent = sum(1 for U in Gamb if eqm(U @ Seps, Seps @ U))
gate("G15", len(Gamb) == 768 and cent == 384,
     f"|G_amb| = {len(Gamb)} == 768 and |C_G_amb(S_eps)| = {cent} == 384")
preserve = swap = neither = 0
for U in Gamb:
    col_img = np.argmax(np.abs(U), axis=0)        # image site of each column (signed perm)
    par = eps[col_img[Ip]]                        # parity of the images of the L_+ basis
    if np.all(par == 1):
        preserve += 1
    elif np.all(par == -1):
        swap += 1
    else:
        neither += 1
gate("G16", neither == 0 and preserve + swap == 768 and preserve == 384 == cent and swap == 384,
     f"AMBIENT INDEX-2 GRADING: preserve {preserve} (== centralizer 384), swap {swap}, neither {neither}; 384+384==768")

# T6 -- orientation neutrality over the SAME polarization
gate("G17a", nrm(Sf @ Jalt @ Sf + Jalt) < TOL0,
     "ORIENTATION NEUTRALITY (a): ||S_eps J_alt S_eps + J_alt|| < 1e-12")
gate("G17b", nrm(Jalt[Ip][:, Ip]) < TOL0 and nrm(Jalt[Im][:, Im]) < TOL0,
     "ORIENTATION NEUTRALITY (b): J_alt also exchanges the same L_+- (diagonal parity blocks = 0)")
gate("G17c", nrm((Jfull - Jalt) - 2 * Jbulk) < TOL0 and nrm(Jfull - Jalt) > TOLREJ,
     "REJECTOR (non-vacuity): J_full - J_alt = 2 J_bulk, nonzero (the two orientations genuinely differ)")

# genuine-complex-structure rejector (a wrong J_full/J_alt fails here)
gate("G18", nrm(Jfull @ Jfull + np.eye(N)) < TOL0 and nrm(Jalt @ Jalt + np.eye(N)) < TOL0,
     "REJECTOR: ||J_full^2 + I|| and ||J_alt^2 + I|| < 1e-12 (genuine complex structures)")

# Unit-10 metric is genuine + h Hermitian
inv = max(nrm(U.T @ g @ U - g) for U in Gamb)
comp = nrm(Jfull.T @ g @ Jfull - g)
gate("G19",
     nrm(h - h.conj().T) < TOL0 and inv < 1e-9 and comp < 1e-9 and float(np.min(np.linalg.eigvalsh(g))) > 0,
     "h Hermitian; g is G_amb-invariant, J_full-compatible, posdef (genuine Unit-10 metric)")

# source pins -- parents actually read, self-note dependency discipline
u9 = note_text(U9_NOTE)
gate("G20", ("S_eps J_full S_eps = -J_full" in u9) and ("common-sign orbit" in u9),
     "SOURCE PIN Unit 9: note contains 'S_eps J_full S_eps = -J_full' and 'common-sign orbit'")
u10 = note_text(U10_NOTE)
gate("G21", "omega(x,y) = g(J_full x,y)" in u10,
     "SOURCE PIN Unit 10: note contains 'omega(x,y) = g(J_full x,y)'")
s = note_text(SELF_NOTE)
c9 = s.count("](" + U9_NOTE)
c10 = s.count("](" + U10_NOTE)
ckcpt = s.count("](KCPT_")
gate("G22", c9 == 1 and c10 == 1 and ckcpt == 2,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: Unit9-link {c9}==1, Unit10-link {c10}==1, total KCPT-links {ckcpt}==2")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
