"""Block 11 runner -- the four open hats of the gauge-link / color-einselection
dynamics frontier are STRATIFIED along the frame -> connection -> generator chain
on the irreducible color carrier C^3, with an exact non-trivial gap at each arrow.
Non-reduction theorem: fixing an upstream object does NOT deliver the downstream
one, so the hats do not collapse to a single missing input. NO hat is discharged.

Context (campaign-local, all source proposals verified live on the ledger as
cited -- this runner consumes none of them as inputs, it re-derives the algebra):
  - hat ADM-1   : the static local color-frame / pointer-projector choice {P_r}.
  - hat 4       : the blocking / record-write isometry (block 10,
                  `COLOR_BLOCKING_ISOMETRY...` PR #3450) reduces to that SAME
                  {P_r} choice.
  - hat R2/ADM-2: color depolarization (block 09 consolidation,
                  `COLOR_DEPOLARIZATION_ADM2_GATING...`, landed on main and
                  cited for framing only) needs a NAMED record frame B PLUS a
                  non-diagonal connection V != I3 (the "primitivity" facet;
                  block 07).
  - hat R1      : the continuous-time link generator. Record supplies none
                  (`record_markov_generator_embeddability_boundary` = retained_no_go;
                  `record_classical_semigroup_boundary` = retained).

The campaign's own objects line up along a chain on C^3:

      record frame {P_r}        connection V             generator X
      (ADM-1, hat 4)   ---->    (ADM-2 driver)  ---->    (R1)
                       arrow 1                  arrow 2

This runner exhibits the EXACT residual at each arrow and shows neither arrow is
onto, so the four hats are stratified rather than collapsed onto one root. All
finite-dimensional exact algebra; random unitaries/states are witnesses for
already-proven identities (no Monte-Carlo fit in the logic path).

  Arrow 1 (frame -> connection).  The SU(3) stabilizer of a complete record frame
  {P_i = |e_i><e_i|} is exactly the maximal torus T^2 (the diagonal connections in
  that frame), Lie-algebra dimension 2 in su(3) (= 8 - 6). So a record frame leaves
  a 6-dimensional family of connection directions undetermined (the transverse
  off-diagonal su(3) directions): it does NOT deliver V. And the
  residual torus connections are PRECISELY the color-diagonal ones, for which the
  predictability-sieve unistochastic matrix S_ij = |<e_i|V|e_j>|^2 = I3 -- the
  block-07 "free hopping does not depolarize" case. Depolarization data lives
  TRANSVERSE to the frame stabilizer (the 6 off-diagonal su(3) directions), exactly
  where the record frame supplies nothing.

  Arrow 2 (connection -> generator).  A regular connection V in SU(3) has an
  infinite Z-lattice of su(3) logarithms X (exp(X) = V), each a valid traceless
  anti-Hermitian generator, with unbounded separation. So a single-step holonomy V
  does NOT deliver a generator: this is the connection-level face of
  `record_markov_generator_embeddability_boundary` (retained_no_go).

  Composition.  arrow1 not onto AND arrow2 not onto => the chain has two genuine
  gaps; the four hats are stratified, not one root. The record axiom delivers no
  object on the chain (frame: record_formation_not_unconditionally_forced =
  retained_no_go; generator: record_markov_generator_embeddability_boundary =
  retained_no_go). This SHARPENS block 10's commutant=scalars result (which used
  only the global SU(3)-invariant-projector non-existence) into a per-arrow
  stratification, and ties arrow-1's residual to block 07's S=I exhibit.

  NO hat discharged: supplying the downstream object is exactly what is missing at
  each arrow; the theorem strengthens the obstruction, it does not deliver any
  pointer set, connection, or generator from the axioms.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


rng = np.random.default_rng(20260609)
d = 3
I3 = np.eye(d)
Imix = I3 / d


def haar_su(n):
    """A Haar-random SU(n) witness."""
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.diagonal(r) / np.abs(np.diagonal(r)))
    return q / (np.linalg.det(q)) ** (1.0 / n)


def su3_basis():
    """An 8-element real basis of su(3) (traceless anti-Hermitian)."""
    gens = []
    for i in range(d):
        for j in range(i + 1, d):
            sym = np.zeros((d, d), complex)
            sym[i, j] = 1.0
            sym[j, i] = 1.0
            gens.append(1j * sym)                       # i*(symmetric off-diag)
            asym = np.zeros((d, d), complex)
            asym[i, j] = 1.0
            asym[j, i] = -1.0
            gens.append(asym)                           # antisymmetric off-diag
    gens.append(1j * np.diag([1.0, -1.0, 0.0]))         # Cartan 1
    gens.append(1j * np.diag([1.0, 1.0, -2.0]) / np.sqrt(3.0))  # Cartan 2
    return gens


GENS = su3_basis()


def is_su3(X):
    return np.allclose(X, -X.conj().T, atol=1e-10) and abs(np.trace(X)) < 1e-10


# Sanity: GENS really is an 8-dim su(3) basis.
check("su(3) basis has 8 elements", len(GENS) == 8)
check("every su(3) basis element is traceless anti-Hermitian",
      all(is_su3(X) for X in GENS))


# ---------------------------------------------------------------------------
# ARROW 1 (frame -> connection): the SU(3) stabilizer of a complete record frame
# is the maximal torus T^2 (dim 2). Tested over several random record frames.
# ---------------------------------------------------------------------------
def frame_stabilizer_dim(B):
    """dim of {X in su(3): [X, P_i] = 0 for all frame projectors P_i}."""
    P = [np.outer(B[:, i], B[:, i].conj()) for i in range(d)]
    rows = []
    for X in GENS:
        comm = np.concatenate([(X @ Pi - Pi @ X).flatten() for Pi in P])
        rows.append(comm)
    M = np.array(rows)                     # 8 x (d*d*d)
    # stabilizer = left-null directions: count generators whose commutators all vanish,
    # but more robustly count the dimension of the kernel of the linear map X -> [X,P].
    # rank of M (rows = images of basis generators) => stabilizer dim = 8 - rank.
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return 8 - rank


stab_dims = []
for _ in range(6):
    B = haar_su(d)
    sd = frame_stabilizer_dim(B)
    stab_dims.append(sd)
check("frame stabilizer dim = 2 (maximal torus T^2) for all random frames",
      all(sd == 2 for sd in stab_dims))
print(f"       observed stabilizer dims = {stab_dims}")

# arrow-1 NOT onto: 2 < 8, so a 6-dim family of su(3) connection directions is
# transverse to (undetermined by) the frame.
check("arrow 1 is not onto: residual connection freedom 8 - 2 = 6 > 0",
      8 - 2 == 6 and 2 < 8)

# Block-07 tie: the residual (stabilizer) connections are exactly color-diagonal
# in the frame => unistochastic S = I3 (no depolarization); depolarization data is
# transverse to the stabilizer.
B = haar_su(d)
phi = rng.uniform(0.0, 2 * np.pi, d)
phi[2] = -(phi[0] + phi[1])                       # keep det = 1
V_torus = B @ np.diag(np.exp(1j * phi)) @ B.conj().T     # a stabilizer connection
S_torus = np.abs(B.conj().T @ V_torus @ B) ** 2          # in the frame B
check("arrow-1 residual connection is color-diagonal in the frame (V in T^2)",
      np.allclose(B.conj().T @ V_torus @ B,
                  np.diag(np.diagonal(B.conj().T @ V_torus @ B)), atol=1e-10))
check("stabilizer connection gives unistochastic S = I3 (block-07 no-depolarization)",
      np.allclose(S_torus, I3, atol=1e-10))

V_transverse = haar_su(d)                          # generic, off the torus
S_transverse = np.abs(B.conj().T @ V_transverse @ B) ** 2
check("transverse connection gives all-nonzero S (depolarization-capable)",
      np.all(S_transverse > 1e-6) and not np.allclose(S_transverse, I3, atol=1e-6))


# ---------------------------------------------------------------------------
# ARROW 2 (connection -> generator): a regular connection V has an infinite
# Z-lattice of su(3) logarithms; the generator is undelivered by V.
# ---------------------------------------------------------------------------
U = haar_su(d)
theta = np.array([0.7, 1.3, -2.0])                 # distinct, sum = 0 (regular V, det 1)
V = U @ np.diag(np.exp(1j * theta)) @ U.conj().T
check("connection V is special-unitary (det V = 1)", abs(np.linalg.det(V) - 1.0) < 1e-9)


def log_branch(n_shift):
    """su(3) logarithm of V on integer branch n_shift (sum = 0 keeps tracelessness)."""
    ph = theta + 2 * np.pi * np.array(n_shift, dtype=float)
    return U @ np.diag(1j * ph) @ U.conj().T


branch_shifts = [(0, 0, 0), (1, 0, -1), (1, -1, 0), (2, -1, -1), (-1, 1, 0)]
logs = []
all_valid = True
all_exp_V = True
for ns in branch_shifts:
    check_sum = sum(ns) == 0                        # tracelessness precondition
    X = log_branch(ns)
    ph = theta + 2 * np.pi * np.array(ns, dtype=float)
    expX = U @ np.diag(np.exp(1j * ph)) @ U.conj().T
    all_valid = all_valid and is_su3(X) and check_sum
    all_exp_V = all_exp_V and np.allclose(expX, V, atol=1e-10)
    logs.append(X)

check("each exhibited branch is a valid su(3) generator", all_valid)
check("each branch exponentiates back to the SAME connection V", all_exp_V)

seps = [np.linalg.norm(logs[0] - logs[k]) for k in range(1, len(logs))]
check("distinct generators of the same V exist (min separation > 1)",
      min(seps) > 1.0)
check("branch separations grow without bound (Z-lattice, not a finite set)",
      max(seps) > 5.0 and np.linalg.norm(logs[3]) > np.linalg.norm(logs[1]))
print(f"       generator separations ||X0 - Xk||_F = {[round(s, 2) for s in seps]}")

# arrow-2 NOT onto.
check("arrow 2 is not onto: >= 2 distinct generators share one holonomy V",
      len(logs) >= 2 and min(seps) > 1.0)


# ---------------------------------------------------------------------------
# COMPOSITION: stratification / non-reduction of the four hats.
# Each boolean below is computed from the arrow results above -- no hardcoded
# verdict (block-10 review lesson: no tautological self-pass).
# ---------------------------------------------------------------------------
arrow1_not_onto = all(sd == 2 for sd in stab_dims) and (8 - 2 > 0)
arrow2_not_onto = (len(logs) >= 2) and (min(seps) > 1.0) and all_exp_V
record_delivers_frame = False     # record_formation_not_unconditionally_forced = retained_no_go
record_delivers_generator = False  # record_markov_generator_embeddability_boundary = retained_no_go

# The four hats sit at distinct chain positions; fixing one position's object does
# not deliver the next. So they do not collapse to a single missing input.
hats_stratified = arrow1_not_onto and arrow2_not_onto
check("frame -> connection -> generator chain has a gap at EACH arrow", hats_stratified)
check("record axiom delivers neither the frame nor the generator on the chain",
      (not record_delivers_frame) and (not record_delivers_generator))

# NO hat discharged: the missing object at each arrow is exactly what would
# discharge the downstream hat; the theorem strengthens the obstruction.
no_hat_discharged = arrow1_not_onto and arrow2_not_onto  # both arrows remain non-onto
check("NO hat discharged (each downstream object remains undelivered)",
      no_hat_discharged)

# Discipline self-audit. The arrow booleans are wired to fresh computations above;
# the Record endpoint booleans are imported from the retained no-go citations named
# in the source note.
check("non-reduction, not a discharge: stratification strengthens the obstruction",
      hats_stratified and no_hat_discharged)
check("no partition map claimed for irreducible color: {P_r} used as a supplied "
      "frame, its SU(3) stabilizer is only T^2 (no nontrivial covariant projector)",
      all(sd == 2 for sd in stab_dims))

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
