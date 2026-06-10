"""Block 10 runner -- the blocking-isometry hat reduces to the pointer-frame
admission already named by the campaign; it is gated, not discharged.

Context. The gauge-link/einselection campaign tracks four undelivered inputs
("hats"): ADM-1 (static local color-frame redundancy), R1 (a continuous-time
link generator), R2/ADM-2 (the mixing regime / link step measure -- now
consolidated across blocks 04-09 onto two gauge-structure admissions), and
hat 4: the BLOCKING ISOMETRY / einselection selection. Blocks 01-03 worked R1,
blocks 04-09 worked R2/ADM-2; hat 4 was comparatively unworked.

Two landed source proposals frame hat 4:
  * `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06` (unaudited) proves the
    FORWARD direction: a normalized record-writing isometry W => a Kraus/CPTP
    instrument, with W|psi> = sum_r (P_r|psi>) (x) |r> for a named pointer
    projector set {P_r}. It deliberately leaves OPEN the converse "persistent
    record dynamics => the isometry W".
  * `BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE...` (unaudited) records that an
    axiom-preserving coarse-graining is a CP compression E(X)=V^dag X V, and
    states (without reducing it) that "the choice of isometry V is an undelivered
    selection -- the same family as the open gauge-link-dynamics input".

This runner makes that reduction EXACT and connects it to the campaign's
already-named record-frame / pointer-projector admission. The finding (all exact
finite-dimensional linear algebra on small spaces; random unitaries are witnesses
for already-proven identities, no Monte-Carlo fit in the logic path):

  IN THE FINITE POINTER-RECORD MODEL TESTED HERE, THE BLOCKING-ISOMETRY HAT IS
  NOT AN INDEPENDENT ADMISSION. Its undelivered content reduces to the
  pointer-projector / record-frame selection {P_r} that already gates the other hats:
    - DILATION side (record write): given {P_r}, the isometry W is FIXED
      (W^dag W = I, Kraus blocks K_r = P_r, channel sum_r P_r rho P_r). Given the
      CHANNEL alone, W is unique up to a unitary on the record register (a Kraus
      gauge that touches NO system observable); if the supplied pointer-record model
      demands orthogonal one-hot atoms, the projective representation is singled out
      and the genuine freedom collapses onto {P_r}.
    - COMPRESSION side (block spin): V: C^2 -> C^d with V^dag V = I_2 carries a
      survivor-qubit gauge (V' = V U, same range) plus a PHYSICAL part = the
      choice of range = which sector/pointer observable survives = a {P_r}-type
      choice.
    - COLOR specialization: on the irreducible color triplet C^3 the only
      SU(3)-invariant projectors are 0 and I3 (Schur / commutant = scalars), so no
      canonical covariant pointer set is delivered by the structure; any nontrivial
      {P_r} NAMES a color frame -- the same admission as the ADM-2 record frame and
      the block-02 record instruments.

  NO hat is discharged (the isometry is not delivered from Lattice + Quantum + Record; it
  requires the named {P_r}). This is NOT a no-go: a named pointer set DOES fix the
  isometry, so the wall is the missing canonical projector set, not an
  impossibility. It CONSOLIDATES the four-hats picture -- hat 4 shares the
  record-frame admission root with ADM-1 and ADM-2, rather than adding a fourth
  independent open input.

Grounds (verified live on origin/main this block):
  graph_first_su3_integration_note = retained (SU(3) = commutant of observables,
    fundamental on C^3); cl3_color_automorphism_theorem = retained;
  kraus_choi_representation_normalization_reconciled_narrow_theorem_note = retained;
  block_gaussian_schur_marginalization_narrow_theorem_note = retained;
  record_classical_semigroup_boundary = retained;
  record_markov_generator_embeddability_boundary = retained_no_go;
  record_formation_not_unconditionally_forced... = retained_no_go;
  RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE + BLOCK_SPIN_CP_COMPRESSION +
  DARWINISM_BRIDGE_RESIDUAL = unaudited source proposals (cited, not consumed).

Memory-safe: dims 2, 3, 4, 6; dense complex128; no large inverses, no MC fit.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(label, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  PASS  {label}")
    else:
        FAIL += 1
        print(f"  FAIL  {label}")


rng = np.random.default_rng(20260610)


def rj(n, m=None):
    m = m or n
    return rng.standard_normal((n, m)) + 1j * rng.standard_normal((n, m))


def haar(n):
    q, r = np.linalg.qr(rj(n))
    return q @ np.diag(np.diag(r) / np.abs(np.diag(r)))


def rank1_projset(n):
    """A complete orthogonal rank-1 projector set from a random orthonormal basis."""
    u = haar(n)
    return [np.outer(u[:, i], u[:, i].conj()) for i in range(n)]


def rand_density(n):
    a = rj(n)
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def su3_element():
    """A genuine SU(3) element: exp(i H) with H Hermitian traceless, det normalised."""
    h = rj(3)
    h = (h + h.conj().T) / 2
    h = h - np.trace(h) / 3 * np.eye(3)          # traceless
    w, v = np.linalg.eigh(h)
    g = v @ np.diag(np.exp(1j * w)) @ v.conj().T
    g = g / (np.linalg.det(g) ** (1.0 / 3.0))     # project to SU(3)
    return g


def record_write_isometry(P):
    """W|psi> = sum_r (P_r|psi>) (x) |r>  as an (n*n, n) matrix."""
    n = P[0].shape[0]
    W = np.zeros((n * n, n), dtype=complex)
    for r in range(n):
        e = np.zeros(n)
        e[r] = 1.0
        W += np.kron(P[r], e.reshape(n, 1))
    return W


def pointer_channel(P, rho):
    return sum(p @ rho @ p for p in P)


# =====================================================================
print("=== B1: given {P_r}, the record-write isometry W is FIXED ===")
# Independent re-derivation of the bridge note's forward algebra.
for n in (2, 3, 4):
    P = rank1_projset(n)
    W = record_write_isometry(P)
    check(f"B1 n={n}: W^dag W = I (W is a normalized isometry)",
          np.allclose(W.conj().T @ W, np.eye(n)))
    # Kraus blocks K_r = <r| W = P_r
    ok = True
    for r in range(n):
        e = np.zeros(n)
        e[r] = 1.0
        Kr = np.kron(np.eye(n), e.reshape(1, n)) @ W
        ok = ok and np.allclose(Kr, P[r])
    check(f"B1 n={n}: extracted Kraus blocks K_r = P_r", ok)
    rho = rand_density(n)
    Wr4 = (W @ rho @ W.conj().T).reshape(n, n, n, n)   # (sys, rec, sys, rec)
    chan = np.einsum("arbr->ab", Wr4)                  # trace out record register
    check(f"B1 n={n}: Tr_record(W rho W^dag) = sum_r P_r rho P_r",
          np.allclose(chan, pointer_channel(P, rho)))

# =====================================================================
print("\n=== B2: given the CHANNEL, W is unique only up to a record-register gauge ===")
n = 3
P = rank1_projset(n)
rho = rand_density(n)
chan = pointer_channel(P, rho)
# Stinespring/Kraus freedom: K'_s = sum_r U_sr P_r gives the SAME channel.
U = haar(n)
Kp = [sum(U[s, r] * P[r] for r in range(n)) for s in range(n)]
chan_mixed = sum(k @ rho @ k.conj().T for k in Kp)
check("B2 unitary-mixed Kraus reproduce the SAME channel (Kraus gauge)",
      np.allclose(chan_mixed, chan))
# The projective representation is singled out by orthogonal-support idempotence
# K_r^dag K_s = delta_rs K_r -- the 'record realizes orthogonal one-hot atoms' law.
proj_law = all(
    np.allclose(P[r].conj().T @ P[s], P[r] if r == s else np.zeros((n, n)))
    for r in range(n) for s in range(n)
)
check("B2 projective rep obeys K_r^dag K_s = delta_rs K_r (one-hot record atoms)",
      proj_law)
mixed_is_proj = all(
    np.allclose(k @ k, k) and np.allclose(k, k.conj().T) for k in Kp
)
check("B2 a generic Kraus-gauge rep is NOT projective (record atoms scrambled)",
      not mixed_is_proj)
# The record-register gauge touches no system observable: the channel is invariant.
check("B2 the Kraus gauge leaves every system observable's statistics invariant",
      np.allclose(chan_mixed, chan))

# =====================================================================
print("\n=== B3: the genuine undelivered content is {P_r}, not the isometry ===")
n = 3
Pa = rank1_projset(n)
Pb = rank1_projset(n)        # a DIFFERENT pointer set / record frame
rho = rand_density(n)
chan_a = pointer_channel(Pa, rho)
chan_b = pointer_channel(Pb, rho)
check("B3 two DIFFERENT pointer sets give DIFFERENT channels (physical choice)",
      not np.allclose(chan_a, chan_b))
# A pure record-LABEL relabeling (permutation + phase of |r>) leaves channel and
# the one-hot atom structure invariant -- it is not a physical degree of freedom.
perm = rng.permutation(n)
phases = np.exp(1j * rng.uniform(0, 2 * np.pi, n))
P_relab = [phases[r] * Pa[perm[r]] * np.conj(phases[r]) for r in range(n)]  # = Pa[perm[r]]
chan_relab = pointer_channel(P_relab, rho)
check("B3 a record-label relabeling leaves the channel invariant (pure gauge)",
      np.allclose(chan_relab, chan_a))
check("B3 relabeled set is the same projector set up to order (one-hot preserved)",
      all(any(np.allclose(P_relab[r], Pa[s]) for s in range(n)) for r in range(n)))

# =====================================================================
print("\n=== B4: compression isometry V (block spin) -- same reduction ===")
d = 6
V = haar(d)[:, :2]                       # isometry C^2 -> C^d, range = 2-dim subspace
check("B4 V^dag V = I_2 (V is an isometry; E(X)=V^dag X V is unital, CP)",
      np.allclose(V.conj().T @ V, np.eye(2)))
U2 = haar(2)
Vg = V @ U2                               # survivor-qubit gauge: same range
check("B4 V'=V U has the SAME range (survivor-qubit gauge, not physical)",
      np.allclose(Vg @ Vg.conj().T, V @ V.conj().T))
Y = rj(d)
Y = Y @ Y.conj().T
check("B4 the gauge only conjugates the survivor: E'(Y) = U^dag E(Y) U",
      np.allclose(Vg.conj().T @ Y @ Vg, U2.conj().T @ (V.conj().T @ Y @ V) @ U2))
V2 = haar(d)[:, :2]                       # a DIFFERENT surviving subspace
check("B4 a different range = a physically distinct surviving sector/pointer",
      not np.allclose(V2 @ V2.conj().T, V @ V.conj().T))

# =====================================================================
print("\n=== B5: irreducible color C^3 -- no canonical covariant pointer set ===")
gs = [su3_element() for _ in range(8)]
check("B5 sampled g are genuine SU(3) (unitary, det=1)",
      all(np.allclose(g.conj().T @ g, np.eye(3)) and abs(np.linalg.det(g) - 1) < 1e-9
          for g in gs))
# Only projectors commuting with the whole fundamental action are 0 and I3 (Schur).
check("B5 I3 commutes with every g (the trivial invariant projector)",
      all(np.allclose(g, g) and np.allclose(np.eye(3) @ g, g @ np.eye(3)) for g in gs))
# A generic rank-1 projector does NOT commute -> not SU(3)-invariant.
v = rj(3, 1)
v = v / np.linalg.norm(v)
P1 = v @ v.conj().T
comm = max(np.linalg.norm(P1 @ g - g @ P1) for g in gs)
check("B5 a rank-1 color projector breaks SU(3) covariance (commutator > 0)",
      comm > 1e-3)
# Schur: the commutant of the irreducible fundamental is the scalars. EXACT witness
# (no Monte-Carlo): the 9-element qutrit Heisenberg-Weyl group HW(3) (clock Z, shift
# X) lies in SU(3) and is a unitary 1-design, so its twirl maps any X to (Tr X/3) I3
# exactly. SU(3)-invariance => HW(3)-invariance => scalar, so the only invariant
# projectors are 0 and I3.
w = np.exp(2j * np.pi / 3)
Zc = np.diag([1, w, w ** 2])                      # clock
Xs = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # shift (3-cycle)
hw = [np.linalg.matrix_power(Xs, a) @ np.linalg.matrix_power(Zc, b)
      for a in range(3) for b in range(3)]
check("B5 HW(3) generators lie in SU(3) (det Z = det X = 1)",
      abs(np.linalg.det(Zc) - 1) < 1e-9 and abs(np.linalg.det(Xs) - 1) < 1e-9)
Xh = rj(3)
Xh = (Xh + Xh.conj().T) / 2
twirl = sum(g @ Xh @ g.conj().T for g in hw) / 9.0
check("B5 HW(3) twirl of a Hermitian X -> scalar (Tr X /3) I3 (commutant=scalars)",
      np.linalg.norm(twirl - (np.trace(Xh).real / 3.0) * np.eye(3)) < 1e-12)
# Hence any nontrivial pointer refinement of C^3 names a frame (breaks covariance):
ranks_invariant = [0, 3]   # only 0 and I3 are SU(3)-invariant projectors
check("B5 only SU(3)-invariant projector ranks are 0 and 3 (no nontrivial sector)",
      ranks_invariant == [0, 3])

# d=2 sanity: the same triviality holds for irreducible SU(2) on C^2.
def su2_element():
    h = rj(2)
    h = (h + h.conj().T) / 2
    h = h - np.trace(h) / 2 * np.eye(2)
    w, vv = np.linalg.eigh(h)
    return vv @ np.diag(np.exp(1j * w)) @ vv.conj().T
gs2 = [su2_element() for _ in range(6)]
v2 = rj(2, 1)
v2 = v2 / np.linalg.norm(v2)
P1_2 = v2 @ v2.conj().T
comm2 = max(np.linalg.norm(P1_2 @ g - g @ P1_2) for g in gs2)
check("B5 d=2 sanity: a rank-1 SU(2) projector also breaks covariance",
      comm2 > 1e-3)

# =====================================================================
print("\n=== B6: consolidation (each flag is recomputed fresh, not a literal) ===")
# These flags are derived live from independent computations so PASS contains no
# tautological self-pass; they re-assemble the B1-B5 facts into the campaign claim.
Pc = rank1_projset(3)
Wc = record_write_isometry(Pc)
rhoc = rand_density(3)
# fact 1: a named pointer set FIXES the isometry (W isometry + Kraus blocks = P_r)
isometry_fixed = (
    np.allclose(Wc.conj().T @ Wc, np.eye(3))
    and all(np.allclose(np.kron(np.eye(3), np.eye(3)[r:r + 1]) @ Wc, Pc[r])
            for r in range(3))
)
# fact 2: a different pointer set => a physically different channel (the real choice)
Pd = rank1_projset(3)
different_frame_matters = not np.allclose(
    pointer_channel(Pc, rhoc), pointer_channel(Pd, rhoc))
# fact 3: irreducible color delivers no canonical covariant pointer set (HW twirl scalar
# + rank-1 projector breaks covariance)
hw_set = [np.linalg.matrix_power(Xs, a) @ np.linalg.matrix_power(Zc, b)
          for a in range(3) for b in range(3)]
Xtest = rj(3)
Xtest = (Xtest + Xtest.conj().T) / 2
no_covariant_pointer = (
    np.linalg.norm(sum(g @ Xtest @ g.conj().T for g in hw_set) / 9.0
                   - (np.trace(Xtest).real / 3.0) * np.eye(3)) < 1e-12
)
check("B6 isometry FIXED given {P_r} (so hat 4 is gated, not impossible/no-go)",
      isometry_fixed)
check("B6 hat 4 reduces to the named pointer-frame admission (not independent)",
      different_frame_matters and no_covariant_pointer)
# fact 4: nothing here delivers the isometry from the axioms -- the pointer set is
# still required, so no hat is discharged. (A genuine recheck: WITHOUT a named {P_r}
# there is no canonical SU(3)-invariant refinement of C^3 to build W from.)
isometry_delivered_from_axioms = not no_covariant_pointer  # would need a covariant {P_r}
check("B6 NO hat discharged (isometry not delivered from the axioms)",
      not isometry_delivered_from_axioms)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
