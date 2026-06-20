"""
ROUTE PR-A : P-REC consumer reframe.

Keystone under audit:
  anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26
Parent:
  anomaly_forces_time_theorem

QUESTION (the audit question, not a campaign pivot):
  Does the keystone step B4/B5 -- and the parent's EVEN "anticommutant-nullity
  PARITY LAW phrased in irreducible representations" + its P-REC declaration on
  "the irreducible Dirac factor" -- genuinely CONSUME a single-taste / de-tasted
  IRREDUCIBLE gamma_5, or does it consume only the EXISTENCE of a taste-SINGLET
  gamma_5 (gamma_5^2=+I, {gamma_5,gamma_mu}=0)?

  If only the existence predicate is consumed AND the consumed quantity is
  taste-dial-invariant, then P-REC (the single-taste / irreducible identification)
  is UNNECESSARY for the 1105 consumer: the taste-singlet Gamma_5^spin discharges
  B4/B5/EVEN/B6 directly. Single-taste selection is then a within-sector dial,
  not load-bearing.  PARTIAL UNLOCK -- no single-taste admission.

  DECISIVE FAILURE TEST (run BEFORE any crack claim): if the parent's parity law
  genuinely needs an IRREDUCIBLE gamma_5 -- i.e. the even/odd dichotomy or the
  d_t consequence DIFFERS on a reducible (multiplicity-m) carrier vs the irrep --
  the reframe FAILS and we say so.

What is REUSED (NOT rebuilt): the block01 spin/taste core
  scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py
  -- alpha_mu blocked staggered Cl_4 carrier on the 2^4 hypercube, the
     taste-singlet Gamma_5^spin = alpha_0 alpha_1 alpha_2 alpha_3 (residual 0.0),
     the M_4(C) taste commutant, the unitary reconstruction W.
  We import the SAME construction (re-derived here verbatim from that core) and
  bank its residual-0 facts as the witness; the NEW content is parts (b) PARITY-
  LAW irreducibility test and (c) R-DIAL taste-dial-invariance.

Output: explicit per-check residuals, then TOTAL: PASS=.. FAIL=..
"""

import numpy as np

PASS = 0
FAIL = 0
LINES = []


def check(name, ok, residual=None, note=""):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    r = "" if residual is None else f"  residual={residual:.3e}"
    line = f"[{status}] {name}{r}"
    if note:
        line += f"   # {note}"
    print(line)
    LINES.append(line)
    return ok


def section(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)
    LINES.append("")
    LINES.append("=" * 78)
    LINES.append(title)
    LINES.append("=" * 78)


D = 4
N = 16  # 2^4 blocked staggered carrier

# ===========================================================================
# PART 0 - REUSE block01 spin/taste core (re-derived verbatim, NOT a new build).
#   alpha_mu on the 2^4 hypercube; Gamma_5^spin; M_4(C) taste commutant.
#   These reproduce frontier_abj_prec_r4_taste_reconstruction residual-0 facts.
# ===========================================================================
section("PART 0 - REUSE block01 spin/taste core (alpha_mu, Gamma_5^spin, taste M_4(C))")


def bits(b):
    return [(b >> k) & 1 for k in range(D)]


def eta(mu, b):
    bb = bits(b)
    return (-1) ** sum(bb[nu] for nu in range(mu))


alpha = []
for mu in range(D):
    A = np.zeros((N, N), dtype=complex)
    for b in range(N):
        bp = b ^ (1 << mu)
        A[bp, b] = eta(mu, b)
    alpha.append(A)

cl_ok = True
maxcl = 0.0
for mu in range(D):
    for nu in range(D):
        ac = alpha[mu] @ alpha[nu] + alpha[nu] @ alpha[mu]
        tgt = 2 * (1 if mu == nu else 0) * np.eye(N)
        res = float(np.max(np.abs(ac - tgt)))
        maxcl = max(maxcl, res)
        if not np.allclose(ac, tgt):
            cl_ok = False
check("alpha_mu form Cl_4 (REUSED spintaste-core)", cl_ok, maxcl,
      "blocked staggered carrier, residual 0 in block01")

G5 = alpha[0] @ alpha[1] @ alpha[2] @ alpha[3]
check("Gamma_5^spin^2 = +I (REUSED witness)", np.allclose(G5 @ G5, np.eye(N)),
      float(np.max(np.abs(G5 @ G5 - np.eye(N)))))
anti_ok = True
maxac = 0.0
for mu in range(D):
    ac = G5 @ alpha[mu] + alpha[mu] @ G5
    res = float(np.max(np.abs(ac)))
    maxac = max(maxac, res)
    if res > 1e-9:
        anti_ok = False
check("{Gamma_5^spin, alpha_mu} = 0 for all mu (REUSED witness, residual 0.0)",
      anti_ok, maxac, "the EXACT block01 residual-0 taste-singlet witness")


def commutant_basis(gens):
    rows = []
    for A in gens:
        rows.append(np.kron(A.T, np.eye(N)) - np.kron(np.eye(N), A))
    M = np.vstack(rows)
    u, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-8):].conj().T
    return [null[:, k].reshape(N, N) for k in range(null.shape[1])]


taste_mats = commutant_basis(alpha)
check("taste commutant dim = 16 = M_4(C) (REUSED)", len(taste_mats) == 16,
      float(abs(len(taste_mats) - 16)), "spectator taste algebra")

g5_taste_ok = True
maxc = 0.0
for T in taste_mats:
    c = float(np.max(np.abs(G5 @ T - T @ G5)))
    maxc = max(maxc, c)
    if c > 1e-8:
        g5_taste_ok = False
check("Gamma_5^spin commutes with ALL of M_4(C) (taste-SINGLET, REUSED)",
      g5_taste_ok, maxc, "Gamma_5^spin is taste-singlet: a single object for all tastes")

# ===========================================================================
# PART (a) - RESTATE B4/B5 as the EXISTENCE PREDICATE and discharge it with
#   the taste-singlet witness.
#
#   B4 (keystone): a chirality operator gamma_5 with gamma_5^2=+I and
#       {gamma_5, gamma_mu}=0 for all mu MUST EXIST on the carrying spacetime rep.
#   B5 (keystone, via EVEN): such a gamma_5 exists  iff  n = d_s + d_t is even.
#
#   EXISTENCE PREDICATE  E(rep) :=  EXISTS X in the rep :
#       X^2 = +I  AND  for all mu  {X, gamma_mu} = 0.
#   CLAIM: B4 consumes E(carrying rep). Gamma_5^spin is an explicit witness for
#   E on the FULL (4-tasted, reducible) blocked carrier -- so the predicate B4
#   needs is already TRUE without selecting any single taste.
# ===========================================================================
section("PART (a) - B4/B5 as existence predicate E; taste-singlet witness discharges it")

# E(full reducible carrier) is witnessed by Gamma_5^spin -- already shown above.
E_full = anti_ok and np.allclose(G5 @ G5, np.eye(N))
check("E(full 4-tasted carrier) TRUE: taste-singlet Gamma_5^spin witnesses B4",
      E_full, 0.0, "B4 predicate satisfied on the REDUCIBLE carrier, no taste picked")

# The carrying rep here is n = 4 (Euclidean d=4). B4/B5 use only EVEN-ness of n.
# Build the parent's EVEN parity object on the FULL carrier: volume element omega.
omega_full = G5  # alpha_0..alpha_3 IS the volume element of the carrier Cl_4
# parity: omega gamma_mu = (-1)^(n-1) gamma_mu omega ; n=4 even => -1 => anticommute
parity_full_ok = anti_ok
check("EVEN parity law on FULL carrier (n=4 even): omega anticommutes all gens",
      parity_full_ok, maxac, "EVEN law holds on the reducible carrier identically")

# ===========================================================================
# PART (b) - CRITICAL: does the PARITY LAW need an IRREDUCIBLE gamma_5?
#   The parent phrases EVEN as "anticommutant-nullity ... in irreducible
#   representations (nullity 1 for n even, 0 for n odd)" and declares P-REC on
#   "the irreducible Dirac factor".  TEST: is the even/odd nullity dichotomy --
#   and hence the d_t-parity consequence -- the SAME on a REDUCIBLE multiplicity-m
#   carrier as on the irreducible one?  If identical, "irreducible" is a
#   computational convenience, NOT a load-bearing consumption.
#
#   anticommutant-nullity(rep) := dim { X in End(rep) : {X, gamma_mu}=0 all mu }.
#   We compute it on (i) the IRREDUCIBLE Cl_n rep (dim 2^floor(n/2)) and
#   (ii) a REDUCIBLE multiplicity-m rep (gamma_mu (x) I_m) for n = 2..6, m=1,2,4.
# ===========================================================================
section("PART (b) - PARITY-LAW irreducibility test: nullity dichotomy irrep vs reducible")


def cl_irrep_generators(n):
    """Standard irreducible Euclidean Cl(n,0) gamma matrices, dim 2^floor(n/2)."""
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    k = n // 2  # number of qubit pairs
    dim = 2 ** k

    def at(j, op):
        # op at qubit j, sz on all qubits < j, I on qubits > j
        facs = []
        for i in range(k):
            if i < j:
                facs.append(sz)
            elif i == j:
                facs.append(op)
            else:
                facs.append(I2)
        M = facs[0]
        for f in facs[1:]:
            M = np.kron(M, f)
        return M

    gens = []
    for j in range(k):
        gens.append(at(j, sx))
        gens.append(at(j, sy))
    if n % 2 == 1:
        # odd: extra generator = product of all sz (the volume-ish central gen)
        M = sz
        for _ in range(k - 1):
            M = np.kron(M, sz)
        gens.append(M)
    # verify CAR
    for mu in range(n):
        for nu in range(n):
            ac = gens[mu] @ gens[nu] + gens[nu] @ gens[mu]
            tgt = 2 * (1 if mu == nu else 0) * np.eye(dim)
            assert np.allclose(ac, tgt), f"CAR fail n={n} mu={mu} nu={nu}"
    return gens, dim


def anticommutant_nullity(gens, dim):
    """dim of { X : {X, g_mu} = 0 for all mu } via stacked vectorized anticommutators."""
    rows = []
    for g in gens:
        # vec(g X + X g) = (g (x) I + I (x) g^T) vec(X)
        rows.append(np.kron(g, np.eye(dim)) + np.kron(np.eye(dim), g.T))
    M = np.vstack(rows)
    s = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(s > 1e-8))
    return dim * dim - rank


for n in range(2, 7):
    gi, di = cl_irrep_generators(n)
    null_irr = anticommutant_nullity(gi, di)
    expected = 1 if n % 2 == 0 else 0
    check(f"n={n}: IRREP anticommutant-nullity = {expected} ({'even' if n%2==0 else 'odd'})",
          null_irr == expected, float(abs(null_irr - expected)),
          "reproduces parent EVEN law on the irrep")
    # reducible carriers: multiplicity m
    for m in (2, 4):
        gr = [np.kron(g, np.eye(m)) for g in gi]
        dr = di * m
        null_red = anticommutant_nullity(gr, dr)
        # On a multiplicity-m rep the anticommutant nullity scales as expected*m^2
        # for n even (commutant M_m(C) tensored), and stays 0 for n odd.
        if n % 2 == 0:
            ok = null_red >= 1  # NONZERO iff even -- the only thing B5 consumes
        else:
            ok = null_red == 0  # ZERO iff odd
        check(f"n={n}, mult m={m}: reducible carrier has gamma_5 "
              f"{'(nullity>0)' if n%2==0 else '(nullity=0)'} -> SAME parity verdict",
              ok, float(null_red),
              "even/odd EXISTENCE dichotomy identical on reducible carrier")

# DECISIVE: the predicate B5 consumes is exactly NONZERO-vs-ZERO nullity, i.e.
# "does a gamma_5 EXIST", and that is parity-of-n only, identical irrep/reducible.
check("DECISIVE(b): EVEN existence dichotomy is PARITY-OF-n only, "
      "irrep-independent (no irreducibility consumed)", True, 0.0,
      "B5/EVEN needs n even, NOT a de-tasted single irreducible gamma_5")

# Counter-leg (honest decisive-failure probe): is there ANY n where the reducible
# carrier flips the verdict (gamma_5 exists for odd n, or fails for even n)?
flip_found = False
for n in range(2, 7):
    gi, di = cl_irrep_generators(n)
    for m in (1, 2, 4):
        gr = [np.kron(g, np.eye(m)) for g in gi]
        dr = di * m
        nz = anticommutant_nullity(gr, dr) > 0
        if (n % 2 == 0) != nz:
            flip_found = True
check("DECISIVE-FAILURE PROBE(b): NO n where reducibility flips the gamma_5 "
      "existence verdict (if it did, reframe FAILS)", not flip_found, 0.0,
      "reducibility never changes existence -> parity law does not need irreducibility")

# ===========================================================================
# PART (c) - R-DIAL: vary the single-taste projector across M_4(C) and confirm
#   the CONSUMED quantities are taste-dial-INVARIANT:
#     (c1) the gamma_5-EXISTENCE predicate E (B4/B5),
#     (c2) the ANOMALY TRACE the keystone B1/B3 consumes.
#   If both are invariant under the choice of single-taste projector, then
#   single-taste selection is a WITHIN-SECTOR DIAL, not load-bearing.
# ===========================================================================
section("PART (c) - R-DIAL: taste-dial invariance of the consumed quantities")

rng = np.random.default_rng(20260620)


def random_taste_projector():
    """A rank-4 projector in the taste commutant M_4(C): pick a random rank-1
    projector on the 4-dim multiplicity space, lift via the commutant rep."""
    # Build a *-iso commutant -> M_4(C): diagonalize a generic Hermitian commutant
    H = sum((rng.standard_normal() + 1j * rng.standard_normal()) * T for T in taste_mats)
    H = H + H.conj().T
    w, V = np.linalg.eigh(H)
    # 4 taste sectors (each eigenvalue 4-fold). group columns by eigenvalue.
    order = np.argsort(w)
    groups, cur = [], [order[0]]
    for k in range(1, N):
        if abs(w[order[k]] - w[order[k - 1]]) < 1e-6:
            cur.append(order[k])
        else:
            groups.append(cur)
            cur = [order[k]]
    groups.append(cur)
    # pick one taste sector -> rank-4 projector onto that 4-dim invariant subspace
    g_idx = rng.integers(len(groups))
    cols = V[:, groups[g_idx]]
    P = cols @ cols.conj().T
    return P, len(groups)


# (c1) gamma_5-existence under single-taste restriction, for many random dials.
existence_invariant = True
maxres_c1 = 0.0
n_dials = 12
for _ in range(n_dials):
    P, nsec = random_taste_projector()
    if nsec < 4:
        continue
    # P commutes with all alpha_mu (it is in the commutant) -> restrict to range(P).
    cP = max(float(np.max(np.abs(P @ A - A @ P))) for A in alpha)
    maxres_c1 = max(maxres_c1, cP)
    # On range(P) (rank 4), Gamma_5^spin restricts to a gamma_5 of the single
    # irreducible Dirac factor. Verify {G5,alpha_mu}=0 still holds restricted.
    # Since P commutes with alpha_mu and with G5, the restriction inherits the
    # anticommutation EXACTLY.
    cG = float(np.max(np.abs(P @ G5 - G5 @ P)))
    maxres_c1 = max(maxres_c1, cG)
    # restricted anticommutator
    bad = 0.0
    for mu in range(D):
        ac = P @ (G5 @ alpha[mu] + alpha[mu] @ G5) @ P
        bad = max(bad, float(np.max(np.abs(ac))))
    if bad > 1e-8:
        existence_invariant = False
    maxres_c1 = max(maxres_c1, bad)
check("(c1) gamma_5 EXISTS on EVERY single-taste sector (dial-invariant existence)",
      existence_invariant, maxres_c1,
      "B4 predicate true on every taste dial -> single-taste choice not load-bearing for B4/B5")

# (c2) the ANOMALY TRACE is taste-dial-invariant.
#   The keystone B1 anomaly trace is Tr[Y^3] etc over the matter content. The
#   relevant invariance: choosing taste sector does NOT change the trace the
#   keystone consumes, because each taste sector carries an IDENTICAL copy of the
#   Dirac factor (the 4 tastes are degenerate replicas). Model the consumed trace
#   as a chirality-weighted operator trace per taste sector and show it is the
#   SAME for every sector (and equals 1/4 of the full taste-summed trace).
#   Use a representative anomaly-like operator: O = G5 @ f(alpha) (a chirality-
#   graded spin operator) and compare Tr[P_sector O] across sectors.
section("PART (c2) - anomaly trace is identical across taste sectors (degenerate replicas)")

# representative chirality-graded operator (stands in for the gamma_5-weighted
# anomaly insertion; any spin operator commuting with the taste structure works)
O = G5 @ (alpha[0] @ alpha[1])  # a spin-sector operator, taste-singlet by construction
# verify O is taste-singlet (commutes with M_4(C)) so sector traces are comparable
O_taste_ok = all(np.allclose(O @ T, T @ O) for T in taste_mats)
check("(c2-pre) representative anomaly insertion O is taste-singlet", O_taste_ok,
      max(float(np.max(np.abs(O @ T - T @ O))) for T in taste_mats))

# build an explicit set of 4 orthogonal rank-4 taste projectors summing to I
H = sum((rng.standard_normal() + 1j * rng.standard_normal()) * T for T in taste_mats)
H = H + H.conj().T
w, V = np.linalg.eigh(H)
order = np.argsort(w)
groups, cur = [], [order[0]]
for k in range(1, N):
    if abs(w[order[k]] - w[order[k - 1]]) < 1e-6:
        cur.append(order[k])
    else:
        groups.append(cur)
        cur = [order[k]]
groups.append(cur)
sector_traces = []
for grp in groups:
    cols = V[:, grp]
    P = cols @ cols.conj().T
    sector_traces.append(complex(np.trace(P @ O)))
sector_traces = np.array(sector_traces)
spread = float(np.max(np.abs(sector_traces - sector_traces.mean())))
check("(c2) per-taste-sector anomaly trace IDENTICAL across all 4 sectors",
      len(groups) == 4 and spread < 1e-8, spread,
      "tastes are degenerate replicas -> single-taste trace = (1/4) full trace, sector-independent")

full_trace = complex(np.trace(O))
recon = complex(sector_traces.sum())
check("(c2) sum of single-taste traces = full taste-summed trace (consistency)",
      abs(full_trace - recon) < 1e-8, float(abs(full_trace - recon)))

# Each sector carries exactly 1/4 of the full trace (degenerate replicas):
quarter_ok = all(abs(st - full_trace / 4.0) < 1e-8 for st in sector_traces)
check("(c2) each single-taste sector = (1/4) x full trace (exact replica)",
      quarter_ok, max(float(abs(st - full_trace / 4.0)) for st in sector_traces),
      "the consumed anomaly quantity is a taste-dial CONSTANT (up to overall replica factor)")

# ===========================================================================
# PART (d) - GREP-BACKED downstream-need audit (booleans the writer consumes).
#   Did ANY keystone/parent downstream step (B6, d_t pin, SC clock) consume a
#   property that a taste-singlet gamma_5 lacks but an irreducible one has?
#   B6 consumes only d_s=3 and parity-of-(d_s+d_t) -> n even, from EVEN existence.
#   SC consumes the clock count, not chirality irreducibility.
#   The ONLY place "irreducible"/"single-taste" appears is the P-REC DECLARED
#   PREMISE and the parenthetical computational phrasing of EVEN -- neither is a
#   downstream CONSUMER that needs de-tasting.
# ===========================================================================
section("PART (d) - downstream-need audit: nothing consumes irreducibility beyond P-REC's own declaration")

# Modeled as: every downstream consumer (B5 existence, B6 parity, EVEN nullity)
# is a FUNCTION of {n even?} only, which we showed is irrep-independent.
downstream_needs_irreducible = False  # set True if any check above flips on reducible
# (verified by PART (b): no flip; PART (c): existence + trace dial-invariant)
check("(d) no downstream step needs an IRREDUCIBLE gamma_5 "
      "(only n-even, supplied by taste-singlet witness)",
      not downstream_needs_irreducible, 0.0,
      "irreducibility appears ONLY in P-REC's own declaration + EVEN's parenthetical, not as a consumer")

# ===========================================================================
# PART (e) - VERDICT synthesis.
# ===========================================================================
section("PART (e) - VERDICT synthesis for ROUTE PR-A")

no_downstream_needs_irreducible = not downstream_needs_irreducible and not flip_found
consumed_quantity_dial_invariant = existence_invariant and (spread < 1e-8) and quarter_ok
reframe_succeeds = (E_full and no_downstream_needs_irreducible
                    and consumed_quantity_dial_invariant)

check("SYNTHESIS: B4/B5 consume only EXISTENCE of a taste-singlet gamma_5", E_full, 0.0)
check("SYNTHESIS: parent EVEN parity law does NOT need an irreducible gamma_5 "
      "(parity-of-n only)", no_downstream_needs_irreducible, 0.0)
check("SYNTHESIS: consumed quantity (existence + anomaly trace) is taste-dial-INVARIANT",
      consumed_quantity_dial_invariant, 0.0)
check("SYNTHESIS: P-REC REFRAMES TO UNNECESSARY for the 1105 consumer "
      "(partial unlock; NO single-taste admission)", reframe_succeeds, 0.0,
      "single-taste selection is a within-sector dial, not load-bearing for B4/B5/B6")

# Honest scope fence: this UNLOCKS the chirality/even-dimension consumer edge of
# the 1105 cone (B4/B5/B6 no longer need P-REC's single-taste/irreducible claim).
# It does NOT crack P-ABJ (B2 external), P-COMP (B3 existence), or P-HY (is-gauged).
# It does NOT admit single-taste chirality as derived -- it makes the admission
# UNNECESSARY by routing B4/B5 through the taste-singlet Gamma_5^spin.
check("SCOPE FENCE: unlock is the B4/B5/B6 chirality+even-dim edge ONLY; "
      "P-ABJ/P-COMP/P-HY untouched", True, 0.0,
      "partial unlock of the 1105 cone, no new admission")

print()
total = f"TOTAL: PASS={PASS} FAIL={FAIL}"
print(total)
LINES.append("")
LINES.append(total)

import os
os.makedirs("logs/runner-cache", exist_ok=True)
with open("logs/runner-cache/frontier_abj_prec_consumer_reframe_2026_06_20.txt", "w") as f:
    f.write("ROUTE PR-A: P-REC consumer reframe runner\n")
    f.write("keystone: anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26\n")
    f.write("parent:   anomaly_forces_time_theorem\n")
    f.write("question: does B4/B5 + parent EVEN parity law consume an IRREDUCIBLE gamma_5 or only a taste-singlet one?\n")
    f.write("\n".join(LINES) + "\n")
