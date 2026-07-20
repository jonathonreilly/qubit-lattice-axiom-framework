#!/usr/bin/env python3
"""Finite Lagrangian-polarization checks for the fixed KCPT lattice surface.

The integer lattice, parity, and signed-permutation objects are rebuilt from
their definitions.  The shell complex structures contain sqrt(2) and sqrt(3)
coefficients and are therefore checked numerically at declared tolerances.
This runner reads no Markdown or environment-selected fixture.
"""
import itertools
import numpy as np

L, N = 4, 64
TOL0 = 1e-12      # rational-zero blocks
TOL_EIG = 1e-8    # eigen / rank
TOLREJ = 1e-6     # rejector floor

EXPECTED_LABELS = [
    "parity-involution",
    "parity-plane-dimensions",
    "staggered-parity-definition",
    "complex-structure-representative-signs",
    "chiral-sign-reversal",
    "lagrangian-diagonal-blocks",
    "off-diagonal-nonzero-rejector",
    "symplectic-structural-inverse",
    "complex-structure-anticommutation",
    "commutator-nonzero-rejector",
    "complex-structure-parity-blocks",
    "plane-exchange-rank",
    "antisymplectic-action",
    "reality-form-action",
    "conjugation-nontrivial-rejector",
    "eigenspace-swap",
    "ambient-group-centralizer-count",
    "ambient-grading-classification",
    "orientation-sibling-sign-reversal",
    "orientation-sibling-parity-blocks",
    "orientation-sibling-nontrivial-rejector",
    "complex-structure-squares",
    "counting-metric-definition",
    "symplectic-form-definition",
    "hermitian-form-definition",
    "hermitian-holomorphic-positivity",
    "kahler-compatibility",
]

PASS = FAIL = 0
LABELS = []


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    LABELS.append(tag)
    PASS, FAIL = PASS + (1 if ok else 0), FAIL + (0 if ok else 1)
    print(f"{'PASS' if ok else 'FAIL'} {tag} - {desc}")
    return ok


def nrm(X):
    return float(np.max(np.abs(X)))


# ---------------- finite-surface construction ----------------------------------------
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

# supplied Kaehler data (built directly from J_full)
g = np.eye(N)
w = -Jfull                                        # omega, matrix J_full^T g = -J_full
h = g.astype(complex) + 1j * w.astype(complex)    # h = g + i*omega


# ---------------- ambient signed-permutation reconstruction --------------------------
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

# ========================================================== verification checks ===
# Real parity polarization
g1 = (eqm(Seps @ Seps, np.eye(N, dtype=np.int64))
      and eqm(Seps.T @ Seps, np.eye(N, dtype=np.int64))
      and round(float(np.trace(Seps))) == 0
      and set(np.unique(eps).tolist()) <= {-1, 1})
gate("parity-involution", g1,
     "S_eps real orthogonal involution: S^2=I, S^T S=I, trace=0, entries +/-1")

g2 = (len(Ip) == 32 and len(Im) == 32 and sorted(Ip.tolist() + Im.tolist()) == list(range(N)))
gate("parity-plane-dimensions", g2,
     "dim L_+ = dim L_- = 32 and the planes partition the 64 basis sites")
expected_eps = np.array(
    [(-1) ** int(sum(coords[i])) for i in range(N)],
    dtype=np.int64,
)
gate("staggered-parity-definition", np.array_equal(eps, expected_eps),
     "S_eps uses +1 on even and -1 on odd staggered-parity sites")
positive_bulk_shells = [
    D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3)
]
gate(
    "complex-structure-representative-signs",
    nrm(Jfull - (Jkerf + sum(positive_bulk_shells))) < TOL0
    and all(
        float(np.vdot(shell, Jbulk).real) > TOLREJ
        for shell in positive_bulk_shells
    ),
    "J_full is the supplied common-positive bulk-shell representative",
)

# Each parity plane is Lagrangian for omega = -J_full
gate("chiral-sign-reversal", nrm(Sf @ Jfull @ Sf + Jfull) < TOL0,
     "S_eps J_full S_eps = -J_full within the declared numerical tolerance")
gate("lagrangian-diagonal-blocks",
     nrm(w[Ip][:, Ip]) < TOL0 and nrm(w[Im][:, Im]) < TOL0,
     "omega vanishes on both diagonal parity blocks")
gate("off-diagonal-nonzero-rejector", nrm(w[Ip][:, Im]) > TOLREJ,
     "off-diagonal L_+ x L_- block is nonzero; vanishing is block-specific")
gate("symplectic-structural-inverse",
     nrm(w @ Jfull - np.eye(N)) < TOL0,
     "omega J_full = I, so omega is nondegenerate without a rounded determinant")

# J_full exchanges the two Lagrangian planes
gate("complex-structure-anticommutation", nrm(Sf @ Jfull + Jfull @ Sf) < TOL0,
     "J_full anticommutes with S_eps: ||S_eps J_full + J_full S_eps|| < 1e-12")
gate("commutator-nonzero-rejector", nrm(Sf @ Jfull - Jfull @ Sf) > TOLREJ,
     "commutator is nonzero; anticommutation is not a both-zero coincidence")
gate("complex-structure-parity-blocks",
     nrm(Jfull[Ip][:, Ip]) < TOL0 and nrm(Jfull[Im][:, Im]) < TOL0,
     "J_full diagonal parity blocks vanish: J(L_+) subset L_-, J(L_-) subset L_+")
rk = int(np.linalg.matrix_rank(Jfull[Im][:, Ip], tol=1e-9))
gate("plane-exchange-rank", rk == 32,
     f"J_full: L_+ -> L_- is a rank-{rk} isomorphism (expected 32)")

# S_eps antisymplectic reality involution
gate("antisymplectic-action", nrm(Sf.T @ w @ Sf + w) < TOL0,
     "ANTISYMPLECTIC: ||S_eps^T omega S_eps + omega|| < 1e-12")
gate("reality-form-action", nrm(Sf.T @ h @ Sf - np.conj(h)) < TOL0,
     "REALITY: S_eps^T h S_eps = conjugate(h) = g - i omega")
gate("conjugation-nontrivial-rejector", nrm(h - np.conj(h)) > TOLREJ,
     "h differs from its conjugate because omega is nonzero")
evals, evecs = np.linalg.eig(Jfull)
sel = np.abs(evals - 1j) < TOL_EIG
V = evecs[:, sel]
SV = Sf.astype(complex) @ V
gate("eigenspace-swap",
     V.shape[1] == 32 and nrm(Jfull @ SV - (-1j) * SV) < TOL_EIG,
     f"+i eigenspace dim {V.shape[1]}; S_eps sends it to the -i eigenspace")

# Ambient preserve/swap grading
cent = sum(1 for U in Gamb if eqm(U @ Seps, Seps @ U))
gate("ambient-group-centralizer-count", len(Gamb) == 768 and cent == 384,
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
gate("ambient-grading-classification",
     neither == 0 and preserve + swap == 768
     and preserve == 384 == cent and swap == 384,
     f"preserve {preserve}, swap {swap}, neither {neither}; kernel is centralizer")

# Orientation sibling over the same polarization
gate("orientation-sibling-sign-reversal", nrm(Sf @ Jalt @ Sf + Jalt) < TOL0,
     "S_eps J_alt S_eps = -J_alt")
gate("orientation-sibling-parity-blocks",
     nrm(Jalt[Ip][:, Ip]) < TOL0 and nrm(Jalt[Im][:, Im]) < TOL0,
     "J_alt also exchanges the same parity planes")
gate("orientation-sibling-nontrivial-rejector",
     nrm((Jfull - Jalt) - 2 * Jbulk) < TOL0
     and nrm(Jfull - Jalt) > TOLREJ,
     "J_full - J_alt = 2 J_bulk and is nonzero")

# Genuine complex structures
gate("complex-structure-squares",
     nrm(Jfull @ Jfull + np.eye(N)) < TOL0
     and nrm(Jalt @ Jalt + np.eye(N)) < TOL0,
     "J_full^2 = J_alt^2 = -I within the declared numerical tolerance")

# Defining Kähler data: independent mutation-sensitive identities.
gate("counting-metric-definition", np.array_equal(g, np.eye(N)),
     "g is exactly the fixed counting metric I_64")
gate("symplectic-form-definition",
     nrm(w - Jfull.T @ g) < TOL0 and nrm(w + Jfull) < TOL0,
     "omega = J_full^T g = -J_full")
gate("hermitian-form-definition",
     nrm(h - (g.astype(complex) + 1j * w.astype(complex))) < TOL0,
     "h = g + i omega")
holomorphic_gram = V.conj().T @ h @ V
wrong_sign_gram = V.conj().T @ (g.astype(complex) - 1j * w) @ V
gate(
    "hermitian-holomorphic-positivity",
    float(np.min(np.linalg.eigvalsh(holomorphic_gram))) > TOLREJ
    and nrm(wrong_sign_gram) < TOL_EIG,
    "h is positive on the +i plane; the wrong g-i omega sign collapses there",
)

# Metric and Hermitian compatibility
inv = max(nrm(U.T @ g @ U - g) for U in Gamb)
comp = nrm(Jfull.T @ g @ Jfull - g)
gate("kahler-compatibility",
     nrm(h - h.conj().T) < TOL0 and inv < 1e-9 and comp < 1e-9 and float(np.min(np.linalg.eigvalsh(g))) > 0,
     "h Hermitian; g is ambient-invariant, J_full-compatible, and positive definite")

if LABELS != EXPECTED_LABELS:
    print(f"FAIL gate-manifest-drift - {LABELS} != {EXPECTED_LABELS}")
    FAIL += 1
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
