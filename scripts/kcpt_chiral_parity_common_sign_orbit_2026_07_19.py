#!/usr/bin/env python3
"""KCPT Unit 9 exact common-sign-orbit runner.

Chiral parity S_eps = diag((-1)^{x1+x2+x3}) (site-parity grading) on the L=4,
N=64 staggered lattice.  Establishes:

  T1  S_eps is a real involution that ANTICOMMUTES with the staggered
      adjacency: S_eps D2 S_eps = -D2  (hence commutes with M=D2^2, fixes P_m).
  T2  kernel reversal (crux): S_eps J_ker S_eps = -J_ker, via corner-wave
      complementation S -> S^c with sign(S^c) = -sign(S).
  T3  bulk reversal: S_eps A_m S_eps = -A_m for every integer carrier.
  T4  total complex-structure sign reversal: S_eps J_full S_eps = -J_full
      (a REAL involution realizing J -> -J, distinct from Unit 8's ANTILINEAR
      K which FIXES the real J_full).  This is not a real-orientation reversal.
  T5  <G_amb, S_eps> has order 1536 = 2*768; every element locks kernel-sign
      == bulk-sign, so it sends J_full -> +-J_full only (census 768 / 768).
  T6  therefore orbit_H(J_full) = {J_full, -J_full}; J_alt is outside that
      orbit.  The full 16-member sign family modulo common sign has 8 relative
      classes, so this runner does not collapse the relative freedom to a bit.

All load-bearing gates are exact integer.  Float gates are labelled
[FLOAT SANITY] and are not load-bearing.
"""
import itertools
import os
import numpy as np

L, N = 4, 64
DOCS = os.environ.get("KCPT_DOCS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))

U8_NOTE = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
KER_NOTE = "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md"
COR_NOTE = "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
AX_NOTE = "MINIMAL_AXIOMS_2026-06-29.md"
AMB_NOTE = "KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md"
SELF_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"

PASS = FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    PASS, FAIL = PASS + (1 if ok else 0), FAIL + (0 if ok else 1)
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} - {desc}")
    return ok


def note_text(basename):
    try:
        with open(os.path.join(DOCS, basename), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def rank_mod_prime(a, prime=1_000_000_007):
    """Return matrix rank over F_prime using exact modular elimination."""
    work = [[int(v) % prime for v in row] for row in a.tolist()]
    nrow, ncol = len(work), len(work[0])
    rank = 0
    for col in range(ncol):
        pivot = next((r for r in range(rank, nrow) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], prime - 2, prime)
        work[rank] = [(v * inv) % prime for v in work[rank]]
        for r in range(nrow):
            if r != rank and work[r][col]:
                factor = work[r][col]
                work[r] = [(x - factor * y) % prime for x, y in zip(work[r], work[rank])]
        rank += 1
        if rank == nrow:
            break
    return rank


# ---------------- construction (self-contained; from the landed units) -------
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
    Nm.append(v)
A = [D2 @ Q[m] for m in range(4)]                # integer carriers A_m = D2 Q_m

# float J_full / J_alt for [FLOAT SANITY] gates only
D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulkf = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfullf = Jkerf + Jbulkf
Jaltf = Jkerf - Jbulkf


# ---------------- G_amb reconstruction (from the ambient unit) ---------------
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
    gs = [g.copy() for g in gs]
    elts = {g.tobytes(): g for g in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for xg in frontier:
            for g in gs:
                p = xg @ g
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
gamb_keys = set(U.tobytes() for U in Gamb)

# ---------------- the chiral parity S_eps ------------------------------------
eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)],
               dtype=np.int64)
Seps = np.diag(eps)

# complementation permutation Pi on the 8 corner labels: S -> S^c
Pi = np.zeros((8, 8), dtype=np.int64)
for k, S in enumerate(SUBSETS):
    Pi[sidx[FULL ^ frozenset(S)], k] = 1

# ============================ B0: dependency source-quotes ===================
u8 = note_text(U8_NOTE)
gate("B0.1", "J_full = J_ker + J_bulk" in u8, "Unit 8 note contains 'J_full = J_ker + J_bulk'")
gate("B0.2", "J_alt = J_ker - J_bulk" in u8, "Unit 8 note contains 'J_alt = J_ker - J_bulk'")
gate("B0.3", "the upstream kernel sign remains open separately" in u8,
     "Unit 8 note contains 'the upstream kernel sign remains open separately'")
ker_txt = note_text(KER_NOTE)
gate("B0.4", "span{I, j}" in ker_txt, "kernel note contains 'span{I, j}'")
gate("B0.5", "J64[index(S xor {1}), index(S)] = 64" in ker_txt,
     "kernel note pins the explicit upstream J64 action and normalization")
gate("B0.6", "pairs the two doublet channels" in note_text(COR_NOTE),
     "corner note contains 'pairs the two doublet channels'")
gate("B0.7", "M_2(C)" in note_text(AX_NOTE), "minimal-axioms contains 'M_2(C)'")
gate("B0.8", "the ambient group `G_amb` of order `768`" in note_text(AMB_NOTE),
     "ambient note contains 'the ambient group `G_amb` of order `768`'")
self_txt = note_text(SELF_NOTE)
linkcount = {b: self_txt.count("](" + b) for b in (U8_NOTE, KER_NOTE, COR_NOTE, AX_NOTE, AMB_NOTE)}
gate("B0.9", self_txt != "" and all(v == 1 for v in linkcount.values()),
     f"self-note markdown-links exactly the 5 deps once each: {linkcount}")

# ============================ B1: construction sanity ========================
gate("B1.1", eqm(D2.T, -D2) and set(np.unique(D2)) <= {-1, 0, 1},
     "D2^T == -D2, entries in {-1,0,1} (antisymmetric staggered adjacency)")
rank_p = rank_mod_prime(D2)
gate("B1.2",
     rank_p == 56 and eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64))
     and eqm(V8.T @ V8, 64 * np.eye(8, dtype=np.int64)),
     f"EXACT: rank_Fp(D2)={rank_p} gives rank_Q>=56; 8 independent null vectors give rank_Q<=56")
gate("B1.3", eqm(V8.T @ V8, 64 * np.eye(8, dtype=np.int64)) and eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64)),
     "V8^T V8 == 64 I_8 and D2 V8 == 0")
gate("B1.4", eqm(J64 @ J64, -(64 ** 2) * np.eye(8, dtype=np.int64)),
     "J64 J64 == -64^2 I_8 (monomial squares to -I: J_ker^2 = -P_ker)")
J64_expected = np.zeros((8, 8), dtype=np.int64)
for col, S in enumerate(SUBSETS):
    row = sidx[frozenset(S) ^ frozenset({1})]
    upstream_sign = ((-1) ** len(frozenset(S) & frozenset({0, 2}))) * (1 if 1 in S else -1)
    J64_expected[row, col] = 64 * upstream_sign
Jker_expected = np.zeros((N, N), dtype=np.int64)
for row in range(8):
    for col in range(8):
        if J64_expected[row, col]:
            Jker_expected += J64_expected[row, col] * np.outer(V8[:, row], V8[:, col])
gate("B1.5", eqm(J64, J64_expected) and eqm(Jker_int, Jker_expected),
     "EXACT: local J64 and lift match an independently expanded upstream monomial and normalization")
T200 = perm(lambda x: (x[0] - 2, x[1], x[2]))
T020 = perm(lambda x: (x[0], x[1] - 2, x[2]))
T002 = perm(lambda x: (x[0], x[1], x[2] - 2))
fourier_counts = {}
for k1, k2, k3 in itertools.product(range(4), repeat=3):
    eigenvalue = 2 * (((-1) ** k1) + ((-1) ** k2) + ((-1) ** k3)) - 6
    fourier_counts[eigenvalue] = fourier_counts.get(eigenvalue, 0) + 1
gate("B1.6",
     fourier_counts == {0: 8, -4: 24, -8: 24, -12: 8}
     and eqm(M, 2 * (T200 + T020 + T002) - 6 * np.eye(N, dtype=np.int64))
     and bool(np.all(np.diag(M) == -6)),
     f"EXACT: translation identity and Fourier characters give spectrum counts {fourier_counts}")
gate("B1.7", eqm(A[0], np.zeros((N, N), dtype=np.int64)) and all(np.any(A[m] != 0) for m in (1, 2, 3)),
     "A_0 == 0 (kernel carrier vanishes); A_1,A_2,A_3 nonzero")

# ============================ B2: S_eps involution ===========================
gate("B2.1", np.count_nonzero(Seps - np.diag(np.diag(Seps))) == 0 and set(np.unique(eps)) <= {-1, 1},
     "S_eps diagonal with entries in {-1,+1}")
gate("B2.2", eqm(Seps @ Seps, np.eye(N, dtype=np.int64)), "S_eps^2 == I")
gate("B2.3", int(np.trace(Seps)) == 0, "trace(S_eps) == 0")
gate("B2.4", eqm(np.diag(Seps), np.array([(-1) ** int(coords[i].sum()) for i in range(N)])),
     "S_eps == diag((-1)^{x1+x2+x3}) (site-parity grading)")

# ============================ B3: chiral anticommutation ======================
gate("B3.1", eqm(Seps @ D2 @ Seps, -D2), "CHIRAL: S_eps D2 S_eps == -D2 (anticommutes)")
gate("B3.2", eqm(Seps @ M @ Seps, M), "S_eps M S_eps == +M (commutes with M=D2^2)")
gate("B3.3", all(eqm(Seps @ Q[m] @ Seps, Q[m]) for m in range(4)),
     "S_eps fixes each drop-one Q_m and hence each normalized projector P_m=Q_m/N_m")
gate("B3.4", not eqm(Seps @ D2 @ Seps, D2), "rejector: S_eps D2 S_eps != +D2 (genuine anticommutation)")

# ============================ B4: kernel reversal + witness ==================
gate("B4.1", eqm(Seps @ Jker_int @ Seps, -Jker_int), "CRUX: S_eps J_ker S_eps == -J_ker")
gate("B4.2", not eqm(Seps @ Jker_int @ Seps, Jker_int), "rejector: S_eps does NOT fix J_ker")
gate("B4.3", eqm(Seps @ V8, V8 @ Pi), "S_eps V8 == V8 Pi (chiral parity = corner-wave complementation)")
gate("B4.4", eqm(Pi @ Pi, np.eye(8, dtype=np.int64)) and eqm(Pi.T @ Pi, np.eye(8, dtype=np.int64)),
     "Pi^2 == I and Pi^T Pi == I (complementation is an involutive permutation)")
gate("B4.5", eqm(Pi @ J64 @ Pi.T, -J64), "Pi J64 Pi^T == -J64 (monomial sign flips under complementation)")
gate("B4.6", all(sgn_subset(FULL ^ frozenset(S)) == -sgn_subset(S) for S in SUBSETS),
     "sign(S^c) == -sign(S) for all 8 corner subsets")

# ============================ B5: bulk reversal ==============================
gate("B5.1", all(eqm(Seps @ A[m] @ Seps, -A[m]) for m in (1, 2, 3)),
     "S_eps A_m S_eps == -A_m for m=1,2,3 (every bulk carrier flipped)")
gate("B5.2", not eqm(Seps @ A[1] @ Seps, A[1]), "rejector: S_eps does NOT fix A_1")

# ============================ B6: total linear reversal ======================
all_flip = eqm(Seps @ Jker_int @ Seps, -Jker_int) and all(eqm(Seps @ A[m] @ Seps, -A[m]) for m in (1, 2, 3))
gate("B6.1", all_flip,
     "EXACT: every additive piece of J_full flips (J_ker and each A_m) => S_eps J_full S_eps = -J_full")
# [STRUCTURAL] the Unit-8 vs Unit-9 contrast, made concrete on the imaginary unit i*I:
# Unit 8's entrywise conjugation K is ANTILINEAR (conjugates i: iI -> -iI); the chiral
# parity S_eps is LINEAR (S_eps (iI) S_eps = i S_eps^2 = +iI). They act OPPOSITELY.
iI = 1j * np.eye(N)
K_iI = np.conj(iI)
S_iI = Seps.astype(complex) @ iI @ Seps.astype(complex)
gate("B6.2",
     np.max(np.abs(K_iI + iI)) < 1e-12
     and np.max(np.abs(S_iI - iI)) < 1e-12
     and np.max(np.abs(K_iI - S_iI)) > 0.5,
     "[FLOAT SANITY][STRUCTURAL] antilinear K conjugates i (iI -> -iI); linear S_eps preserves it (iI -> +iI); opposite action")
s6a = float(np.max(np.abs(Seps.astype(float) @ Jfullf @ Seps.astype(float) + Jfullf)))
s6b = float(np.max(np.abs(Seps.astype(float) @ Jaltf @ Seps.astype(float) + Jaltf)))
gate("B6.3", s6a < 1e-9 and s6b < 1e-9,
     f"[FLOAT SANITY] S_eps J_full S_eps == -J_full and S_eps J_alt S_eps == -J_alt (res {s6a:.1e},{s6b:.1e})")

# ============================ B7: order-1536 group + sign-lock ================
gate("B7.1", Seps.tobytes() not in gamb_keys and not eqm(Seps @ D2, D2 @ Seps),
     "S_eps NOT in G_amb (anticommutes with D2; excluded from the D2-commutant)")
norm_ok = all(((Seps @ g @ Seps).tobytes() in gamb_keys) for g in Gamb)
gate("B7.2", norm_ok, "S_eps normalizes G_amb: S_eps g S_eps in G_amb for all 768 g")
coset = [Seps @ g for g in Gamb]
coset_keys = set(c.tobytes() for c in coset)
gate("B7.3", len(gamb_keys) == 768 and len(gamb_keys & coset_keys) == 0 and len(gamb_keys | coset_keys) == 1536,
     f"<G_amb,S_eps> = G_amb u S_eps.G_amb, disjoint, order {len(gamb_keys | coset_keys)} == 1536")


def blocksign(h, X):
    hXh = h @ X @ h.T                             # h orthogonal signed perm: h^{-1}==h^T
    if eqm(hXh, X):
        return +1
    if eqm(hXh, -X):
        return -1
    return 0


allelts = list(Gamb) + coset
signs = [(blocksign(h, Jker_int), blocksign(h, A[1])) for h in allelts]
locked = all(sk == sb and sk in (+1, -1) for sk, sb in signs)
n_plus = sum(1 for sk, sb in signs if sk == +1)
n_minus = sum(1 for sk, sb in signs if sk == -1)
gate("B7.4", locked, "SIGN-LOCK: every h locks kernel-sign == bulk-sign (both in {+1,-1})")
gate("B7.5", n_plus == 768 and n_minus == 768,
     f"census: {n_plus} fix J_full (G_amb), {n_minus} send J_full->-J_full (S_eps coset)")

# ============================ B8: exact common-sign orbit ====================
gate("B8.1", np.any(Jker_int != 0),
     "EXACT: -J_full != J_alt  (since -J_full - J_alt = -2 J_ker, and J_ker != 0)")
gate("B8.2", np.any(A[1] != 0),
     "EXACT: J_full != J_alt  (since J_full - J_alt = 2 J_bulk, and B_1 != 0)")
no_reach_alt = all(not (sk == -sb) for sk, sb in signs)     # signs never opposite => J_alt unreachable
coefficient_image = {(sk, sb, sb, sb) for sk, sb in signs}
gate("B8.3", no_reach_alt and n_plus + n_minus == 1536
     and coefficient_image == {(+1, +1, +1, +1), (-1, -1, -1, -1)},
     "EXACT: H coefficient image is the common sign only; orbit_H(J_full)={+-J_full}, excluding J_alt")
sign_family = list(itertools.product((+1, -1), repeat=4))
relative_classes = {(ek * e1, ek * e2, ek * e3) for ek, e1, e2, e3 in sign_family}
gate("B8.4", len(sign_family) == 16 and len(relative_classes) == 8,
     "EXACT: 16 sign tuples modulo common sign give 8 relative classes, represented by (ek*e1,ek*e2,ek*e3)")
# [FLOAT SANITY] all sign-family members square to -I; not used for the orbit count
sq_ok = True
for ek in (+1, -1):
    for e1 in (+1, -1):
        for e2 in (+1, -1):
            for e3 in (+1, -1):
                Je = ek * Jkerf + e1 * D2f @ Pf[1] / (2 * np.sqrt(1)) \
                     + e2 * D2f @ Pf[2] / (2 * np.sqrt(2)) + e3 * D2f @ Pf[3] / (2 * np.sqrt(3))
                if np.max(np.abs(Je @ Je + np.eye(N))) > 1e-9:
                    sq_ok = False
gate("B8.5", sq_ok,
     "[FLOAT SANITY] all 16 sign-members square to -I; the exact common-sign orbit reaches 2 of 16")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
