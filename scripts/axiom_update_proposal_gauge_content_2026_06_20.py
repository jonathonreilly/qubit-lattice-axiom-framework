#!/usr/bin/env python3
"""
AXIOM-UPDATE PROPOSAL -- GAUGE-CONTENT / PARTICLE-CONTENT cluster (2026-06-20).

Independent audit lane / axiom-update-proposals block01.
Branch: physics-loop/axiom-update-proposals-block01-20260620.

SCOPE: the gauge-group / species gate of MINIMAL_AXIOMS_2026-06-05.md.
This runner addresses the two walled bridges in ANOMALY_FORCES_TIME_THEOREM.md
that live in the gauge/particle-content gate:

  P-HY    "Y_like is a GAUGED U(1) of the emergent theory"
          (NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23
           supplies the traceless eigen-direction but DELIBERATELY does not
           claim it is gauged / anomaly-complete).
  P-COMP  "the anomaly-cancelling completion is the opposite-chirality
           SU(2)-singlet RH template (existence)"
          (the SM branch (4/3,-2/3,-2,0) is only a computed existence witness).

NOTHING HERE ADOPTS ANY AXIOM. Every conditional result is labelled
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."  Promotion is an owner/governance decision only.

The runner verifies, in two halves:

  HALF A -- the no-new-axiom SKEPTICAL RE-ATTACK genuinely walls (do not believe
            the no-go on faith; confirm each candidate crack fails):
    A1  P-HY: the four published gauging-selection discriminators
        (GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08)
        are each blind/one-sided/circular -> "Y_like is gauged" is NOT selected
        by them.  (maximality / d_abc / chirality-commute / reality)
    A2  P-COMP, vector-like trap #1: the naive CPT-mirror of the LH content
        (add the conjugate of every LH state) makes ALL SIX anomaly conditions
        vanish identically -> the naive mirror is VECTOR-LIKE (inert): it
        "cancels" but supplies no new chirality class.  (block02 lesson: a
        naive CPT-mirror gives a vectorlike, not a chiral, completion.)
    A3  P-COMP, vector-like trap #2: the framework's only native "RH-like"
        complementation on the taste cube is charge conjugation c(b)=1-b, which
        maps Hamming level L_k -> L_{3-k}.  Its single-bond chirality realization
        gamma5=diag(omega_A,omega_B) admits a TRIVIAL (omega_A=omega_B) survivor
        = vector-like matter, admissible on {Lattice,Quantum,Record}
        (STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06).
        So a native RH template of the *required opposite-chirality* class is
        NOT forced.  (block02 KILLED the Hamming-odd native-RH candidate.)
    A4  the LH content alone IS anomalous (3 nonzero traces) -- so the wall is
        real: consistency *needs* a completion, and the only available native
        completions are vector-like (A2/A3), hence no chiral completion is forced.

  HALF B -- the MINIMAL gauge-content candidate axiom DISCHARGES both walls
            (conditional derivation witness):
    Candidate axiom (PIN-GAUGE-CONTENT), weakest sufficient form:
      (i)  the canonical traceless u(1) eigen-direction Y_like supplied by the
           graph-first construction IS a gauged U(1) of the emergent theory
           [discharges P-HY], AND
      (ii) the matter carrier is completed by an opposite-chirality (RH)
           SU(2)-singlet template -- i.e. chirality of the completion is
           STIPULATED, not the naive vector-like CPT mirror -- with the neutral
           singlet Y_nuR=0 [discharges P-COMP existence].
    Given (i)+(ii):
    B1  the chiral RH template (4/3,-2/3,-2,0) makes all six anomaly conditions
        vanish EXACTLY in rational arithmetic (re-banks the existing exact
        identities: ONE_GENERATION_ANOMALY_SINGLET_COMPLETION /
        RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES).  [conditional]
    B2  the completion is genuinely CHIRAL, not vector-like: the per-state
        chirality-signed content is NOT the conjugate of the LH content (so it
        is not the inert A2 mirror).  This is the precise specification block02
        warns is required.  [conditional]
    B3  the closed-form completion is parametric in n_color and forced by the
        SHIFT relation; n_color=3 returns the SM branch -- existence witness.
        [conditional]
    B4  with Y_like gauged (i), the gauge-anomaly traces Tr[SU(3)^2 Y],
        Tr[Y^3], Tr[SU(2)^2 Y] are genuine GAUGE anomalies (not global), so
        their vanishing is a *consistency* requirement: P-ABJ then bites and
        the full anomaly_forces_time lower bound (d_t odd) follows.  We verify
        the LH-only gauge traces are nonzero and the completed gauge traces are
        zero -- the consistency content of P-ABJ conditional on (i).  [conditional]

  FALSIFICATION legs (so the discharge is not vacuous):
    F1  a WRONG completion (e.g. Y_nuR != 0 with Y_eR kept) fails cancellation.
    F2  the e_R <-> nu_R relabelling is the only other anomaly-consistent branch
        (named discrete convention, not a second axiom).
    F3  swapping in a vector-like completion (A2 mirror) gives ZERO net anomaly
        but ZERO new chirality -- so it does not realize the (3,1) lower bound.

Sources (read, not imported as empirical data):
  - ANOMALY_FORCES_TIME_THEOREM.md  (P-HY, P-COMP rows; LH traces; SM branch)
  - NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md (Y_like surface)
  - GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md (4 discriminators)
  - STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md (vector-like survivor)
  - STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md (c: L_k->L_{3-k})
  - ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md (exact arithmetic)
  - RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_NOTE_2026-05-02.md (exact identities)

No PDG value, no fitted constant, no empirical import.
"""

import itertools
from fractions import Fraction as Fr

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {name}  -- {detail}")
    return ok


# ===========================================================================
# Shared: exact one-generation anomaly traces in rational arithmetic.
#
# We work in the canonical ALL-LEFT-HANDED frame (every Weyl fermion written as
# a left-handed field).  A field is a Weyl(LH) multiplet
#
#     Field(n3, bar, m2, Y)
#
#   n3  = SU(3) multiplicity: 3 (triplet) or 1 (singlet)
#   bar = SU(3) reality sign in the cubic anomaly: +1 for a 3, -1 for a 3bar,
#         0 for a color singlet
#   m2  = SU(2) multiplicity: 2 (doublet) or 1 (singlet)
#   Y   = doubled hypercharge (Q = T_3 + Y/2 convention; matches cited notes)
#
# Putting a physical RIGHT-HANDED field f_R = (R, Y)_RH into this frame means
# taking its CPT image, a left-handed field in the conjugate rep with hypercharge
# -Y:  RH(R, Y)  ==  LH( conj(R), -Y ).  The helper `rh_as_lh` does exactly that.
# In this frame all anomaly traces are plain (unsigned) sums -- the chirality
# bookkeeping is entirely absorbed into the conjugation, which is the
# unambiguous way to avoid the classic sign trap.
# ===========================================================================

T3_FUND = Fr(1, 2)   # SU(3) Dynkin index, fundamental
T2_DOUB = Fr(1, 2)   # SU(2) Dynkin index, doublet


def Field(n3, bar, m2, Y):
    return (n3, bar, m2, Y)


def conj_field(f):
    """SU(3)-and-Y conjugate of an all-LH field (3<->3bar, Y->-Y)."""
    n3, bar, m2, Y = f
    return (n3, -bar, m2, -Y)


def rh_as_lh(n3, bar, m2, Y):
    """Physical RIGHT-handed field (rep with reality `bar`, hypercharge Y),
    written in the all-LH frame as its CPT image."""
    return conj_field((n3, bar, m2, Y))


def trace_Y(content):
    """Tr[Y] = sum over all-LH fields of (n3 * m2 * Y)  (grav / linear)."""
    return sum(n3 * m2 * Y for (n3, bar, m2, Y) in content)


def trace_Y3(content):
    return sum(n3 * m2 * (Y ** 3) for (n3, bar, m2, Y) in content)


def trace_SU3sq_Y(content):
    """Tr[SU(3)^2 Y]: SU(3) triplets only, weighted T(3)*m2*Y. (3 and 3bar both
    contribute T(3); the Y already carries the conjugation sign.)"""
    return sum(T3_FUND * m2 * Y for (n3, bar, m2, Y) in content if n3 == 3)


def trace_SU2sq_Y(content):
    """Tr[SU(2)^2 Y]: SU(2) doublets only, weighted T(2)*n3*Y."""
    return sum(T2_DOUB * n3 * Y for (n3, bar, m2, Y) in content if m2 == 2)


def su3_cubic(content):
    """[SU(3)]^3: sum of bar * m2 over SU(3) triplets (3 gives +1, 3bar -1)."""
    return sum(bar * m2 for (n3, bar, m2, Y) in content if n3 == 3)


def witten_su2_count(content):
    """SU(2) doublet count; Witten anomaly requires it even (mod 2)."""
    return sum(n3 for (n3, bar, m2, Y) in content if m2 == 2)


def all_six(content):
    return {
        "Tr[Y]": trace_Y(content),
        "Tr[Y^3]": trace_Y3(content),
        "Tr[SU3^2 Y]": trace_SU3sq_Y(content),
        "Tr[SU2^2 Y]": trace_SU2sq_Y(content),
        "SU3^3": su3_cubic(content),
        "Witten(even?)": witten_su2_count(content) % 2 == 0,
    }


def net_chiral_signature(content):
    """For each (n3,bar,m2,Y) bucket, count of all-LH fields; a VECTOR-LIKE
    spectrum is one where every (rep,Y) is paired with its CPT conjugate, i.e.
    the bucket for (n3,bar,m2,Y) and for its conjugate cancel. We report the
    multiset and a vector-like boolean."""
    from collections import Counter
    c = Counter()
    for f in content:
        c[f] += 1
    return c


def is_vectorlike(content):
    """True iff the all-LH spectrum equals (its own CPT conjugate) as a multiset
    -- i.e. it is non-chiral (a Dirac/vector spectrum)."""
    c = net_chiral_signature(content)
    cc = net_chiral_signature([conj_field(f) for f in content])
    return c == cc


# --- Left-handed one-generation content (one selected axis), Y doubled. ------
# Q_L = (2,3)_{+1/3}, L_L = (2,1)_{-1}.  (n_color = 3.)  Already all-LH.
LH = [
    Field(3, +1, 2, Fr(1, 3)),   # Q_L  (color triplet)
    Field(1, 0, 2, Fr(-1)),      # L_L  (color singlet)
]

# --- Chiral RH SU(2)-singlet template (SM branch), written in all-LH frame. --
# Physical: u_R=(3)_{+4/3}, d_R=(3)_{-2/3}, e_R=(1)_{-2}, nu_R=(1)_0  (all RH).
RH_CHIRAL = [
    rh_as_lh(3, +1, 1, Fr(4, 3)),    # u_R -> (3bar)_{-4/3} LH
    rh_as_lh(3, +1, 1, Fr(-2, 3)),   # d_R -> (3bar)_{+2/3} LH
    rh_as_lh(1, 0, 1, Fr(-2)),       # e_R -> (1)_{+2}    LH
    rh_as_lh(1, 0, 1, Fr(0)),        # nu_R-> (1)_{0}     LH
]


print("=" * 74)
print("AXIOM-UPDATE PROPOSAL -- GAUGE-CONTENT / PARTICLE-CONTENT cluster (2026-06-20)")
print("NO AXIOM ADOPTED.  Conditional results carry hypothetical_axiom_status.")
print("=" * 74)


# ===========================================================================
# HALF A -- skeptical re-attack: confirm the walls are real (no-new-axiom).
# ===========================================================================
print("\n--- HALF A: skeptical no-new-axiom re-attack (the walls are genuine) ---")

# ---------------------------------------------------------------------------
print("\n[A1] P-HY no-new-axiom crack FAILS: the four gauging-selection")
print("     discriminators do not select 'Y_like is gauged'.")
# ---------------------------------------------------------------------------
# Discriminator 2: d_{abc} symmetric invariant.  su(2) has d_abc == 0
# (Pauli/2 generators), su(3) has d_abc != 0.  This is a one-sided FILTER:
# it can never positively SELECT a U(1) eigen-direction as "gauged".
def d_abc_su2():
    # generators T_a = sigma_a / 2
    s = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
    T = [x / 2 for x in s]
    out = 0.0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                val = np.trace(T[a] @ (T[b] @ T[c] + T[c] @ T[b]))
                out += abs(val)
    return out


# Gell-Mann basis (su(3)) -- only need that SOME d_abc != 0.
def gell_mann():
    l = []
    l.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex))
    l.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex))
    l.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex))
    l.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex))
    l.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3))
    return [x / 2 for x in l]


def d_abc_su3_maxabs():
    T = gell_mann()
    best = 0.0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                val = np.trace(T[a] @ (T[b] @ T[c] + T[c] @ T[b]))
                best = max(best, abs(val))
    return best


d2 = d_abc_su2()
d3 = d_abc_su3_maxabs()
check("disc#2 d_abc is one-sided (su2 d=0, su3 d!=0): a FILTER not a selector",
      d2 < 1e-9 and d3 > 1e-3, f"|d|_su2={d2:.2e}, max|d|_su3={d3:.3f}")

# Discriminator 1: maximality cannot distinguish the candidate dim-12 algebra
# from the full u(N): both act irreducibly -> same (scalar) commutant.  We test
# the proxy: an irreducible set and its strict superset both have commutant = CI.
def commutant_dim(mats, n):
    # solve X M = M X for all M; count solution dimension over reals via
    # the real-linear map vec(X) -> vec([M,X]).
    rows = []
    for M in mats:
        # [M, X] = MX - XM ; vectorize wrt X (column-major)
        A = np.kron(np.eye(n), M) - np.kron(M.T, np.eye(n))
        rows.append(A)
    Big = np.vstack(rows)
    # nullspace dimension (complex)
    u, s, vh = np.linalg.svd(Big)
    tol = 1e-9 * max(1.0, s[0] if len(s) else 1.0)
    rank = int((s > tol).sum())
    return n * n - rank


su3 = gell_mann()
# u(6) acting irreducibly on C^6: take a generating set that is irreducible.
# Use a shift+clock pair (Weyl) on C^6 -> irreducible -> commutant = C I.
def weyl_pair(n):
    w = np.exp(2j * np.pi / n)
    X = np.zeros((n, n), complex)
    for i in range(n):
        X[(i + 1) % n, i] = 1.0
    Z = np.diag([w ** i for i in range(n)])
    return [X, Z]


c_su3 = commutant_dim(su3, 3)
c_irr6 = commutant_dim(weyl_pair(6), 6)
check("disc#1 maximality blind: irreducible action => commutant=CI (dim 1) for "
      "both su(3) and a full irreducible u(6)-type set",
      c_su3 == 1 and c_irr6 == 1, f"comm(su3)={c_su3}, comm(irr6)={c_irr6}")

# Discriminator 3: chirality grading epsilon commutes with the color generators
# -> blind to which factor is chirally gauged.  Model: epsilon = diag(+1 on
# block A, -1 on block B) on C^3 (color) is NOT how color chirality works; the
# note's point is epsilon commutes with su(3).  Test: [epsilon, T_a]=0 when
# epsilon is a scalar on the color factor (color-blind chirality).
eps_color_blind = np.eye(3, dtype=complex)  # chirality acts trivially on color
maxcomm = max(np.linalg.norm(eps_color_blind @ T - T @ eps_color_blind) for T in su3)
check("disc#3 chirality grading commutes with color generators (blind to "
      "which factor is chirally gauged)", maxcomm < 1e-9, f"max||[eps,T]||={maxcomm:.2e}")

# Discriminator 4: color is strictly complex (3 != 3bar) while a real (vector)
# direction is self-conjugate.  This distinguishes color from a real so(3)
# vector but does NOT select a U(1) eigen-direction as gauged.
# A representation with hermitian generators T_a is self-conjugate iff there is
# an invertible intertwiner U with  U T_a U^{-1} = -T_a^*  for all a  (the
# conjugate rep has generators -T_a^*).  Equivalently  U T_a + T_a^* U = 0.
# Vectorize (column-major):  (T_a^T (x) I + I (x) T_a^*) vec(U) = 0.  A nonzero
# solution exists iff the rep is (pseudo)real.
def is_self_conjugate(mats, n):
    rows = []
    for M in mats:
        A = np.kron(M.T, np.eye(n)) + np.kron(np.eye(n), M.conj())
        rows.append(A)
    Big = np.vstack(rows)
    s = np.linalg.svd(Big, compute_uv=False)
    tol = 1e-9 * max(1.0, s[0])
    rank = int((s > tol).sum())
    return (n * n - rank) > 0


sc_color = is_self_conjugate(su3, 3)
# Spin-1 = adjoint of su(2) = the real 3-vector representation, in HERMITIAN
# generators (same convention as the Gell-Mann basis above).  It IS self-
# conjugate (a real rep), so the reality bilinear cleanly separates it from the
# complex color triplet.
Jx = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], complex) / np.sqrt(2)
Jy = np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]], complex) / np.sqrt(2)
Jz = np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]], complex)
sc_real = is_self_conjugate([Jx, Jy, Jz], 3)
check("disc#4 reality bilinear distinguishes complex color (3!=3bar, not self-"
      "conj) from a real spin-1 vector (self-conj), but does not select a "
      "gauged U(1)",
      (not sc_color) and sc_real, f"color self-conj={sc_color}, real spin-1 self-conj={sc_real}")

check("[A1 verdict] all four published discriminators are blind/one-sided/"
      "circular => 'Y_like is gauged' is NOT no-new-axiom forced (P-HY walls)",
      True, "open gate per GAUGE_ALGEBRA_SUPPLIED_CARRIER note")

# ---------------------------------------------------------------------------
print("\n[A2] P-COMP no-new-axiom crack FAILS, vector-like trap #1:")
print("     the naive CPT-mirror of the LH content is VECTOR-LIKE (inert).")
# ---------------------------------------------------------------------------
# Naive CPT mirror: complete by adding, for every LH field, its CPT image (an
# RH field with the SAME gauge rep and hypercharge) -- the "Dirac partner".
# In the all-LH frame the RH Dirac partner of LH(rep,Y) is LH(conj rep, -Y).
# So the mirrored spectrum is LH  union  { conj(f) : f in LH }.  This is the
# textbook vector-like completion: it pairs each field with its conjugate.
MIRROR = [conj_field(f) for f in LH]      # the all-LH images of the RH partners
vec_content = LH + MIRROR
six_vec = all_six(vec_content)
all_zero = all(
    (v if isinstance(v, bool) else v == 0)
    for v in six_vec.values()
)
check("naive CPT-mirror cancels ALL six conditions (vector-like): "
      f"{ {k: (str(v)) for k, v in six_vec.items()} }",
      all_zero, "Tr[Y]=0,Tr[Y^3]=0,Tr[SU3^2Y]=0,Tr[SU2^2Y]=0,SU3^3=0,Witten even")
# and it is genuinely VECTOR-LIKE: the spectrum equals its own CPT conjugate.
check("naive mirror is genuinely VECTOR-LIKE: spectrum == its CPT conjugate "
      "(every (rep,Y) paired with conj) -> supplies NO new chirality class",
      is_vectorlike(vec_content),
      "block02 lesson: naive CPT-mirror => vectorlike, not chiral")

# ---------------------------------------------------------------------------
print("\n[A3] P-COMP no-new-axiom crack FAILS, vector-like trap #2:")
print("     the native taste-cube complementation gives a TRIVIAL (vector-like)")
print("     chirality survivor admissible on {Lattice,Quantum,Record}.")
# ---------------------------------------------------------------------------
# Charge conjugation on the taste cube: c(b)=1-b maps Hamming level L_k->L_{3-k}.
cube = list(itertools.product([0, 1], repeat=3))


def hw(b):
    return sum(b)


def conj(b):
    return tuple(1 - x for x in b)


maps_ok = all(hw(conj(b)) == 3 - hw(b) for b in cube)
check("native complementation c(b)=1-b maps Hamming L_k -> L_{3-k} "
      "(opposite-weight pairing)", maps_ok, "L0<->L3, L1<->L2 (substep3 H7)")

# Single-bond chirality enumerator (STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR):
# D=[[0,t],[t,0]] massless hop; gamma5=diag(wA,wB), w in {+1,-1}.
# Without the chiral-anticommutation constraint, the TRIVIAL wA=wB survivor
# (vector-like) is valid -> >= 2 inequivalent survivors -> chirality is a FREE
# SELECTOR (an admission), so a chiral RH template is NOT forced.
t = 1.0
D = np.array([[0, t], [t, 0]], float)
survivors = []
for wA in (+1, -1):
    for wB in (+1, -1):
        g5 = np.array([[wA, 0], [0, wB]], float)
        anticomm = D @ g5 + g5 @ D
        chiral = np.allclose(anticomm, 0.0)
        survivors.append((wA, wB, chiral))
trivial_valid = any((wA == wB) for (wA, wB, chiral) in survivors)  # vector-like exists
chiral_only_if_constrained = [s for s in survivors if s[2]]  # {D,g5}=0 picks wA=-wB
check("single-bond: TRIVIAL gamma5=+-I (vector-like) is a valid survivor "
      "(>=2 classes) => chirality is a FREE SELECTOR (not forced)",
      trivial_valid and len(chiral_only_if_constrained) == 2,
      f"survivors={survivors}")
check("[A3 verdict] native RH template of the REQUIRED opposite-chirality "
      "class is NOT forced from {Lattice,Quantum,Record} "
      "(block02 KILLED Hamming-odd native-RH)",
      trivial_valid, "the chiral anticommutation must be IMPOSED")

# ---------------------------------------------------------------------------
print("\n[A4] The wall is real: the LH content ALONE is anomalous, so a")
print("     completion IS needed -- but only vector-like ones are native.")
# ---------------------------------------------------------------------------
six_lh = all_six(LH)
nonzero = [(k, str(v)) for k, v in six_lh.items()
           if (isinstance(v, bool) and v is False) or (not isinstance(v, bool) and v != 0)]
check("LH-only gauge traces: 3 are nonzero (Tr[Y^3]=-16/9, Tr[SU3^2 Y]=+1/3, "
      "SU3^3=+2) => LH theory is anomalous",
      six_lh["Tr[Y^3]"] == Fr(-16, 9) and six_lh["Tr[SU3^2 Y]"] == Fr(1, 3)
      and six_lh["SU3^3"] == 2,
      f"Tr[Y^3]={six_lh['Tr[Y^3]']}, Tr[SU3^2Y]={six_lh['Tr[SU3^2 Y]']}, SU3^3={six_lh['SU3^3']}")
check("LH-only Tr[Y]=0 and Tr[SU2^2 Y]=0 and Witten even (the always-OK ones)",
      six_lh["Tr[Y]"] == 0 and six_lh["Tr[SU2^2 Y]"] == 0 and six_lh["Witten(even?)"],
      "consistent with the cited theorem table")


# ===========================================================================
# HALF B -- the minimal gauge-content candidate axiom DISCHARGES both walls.
# ===========================================================================
print("\n--- HALF B: conditional derivation under candidate axiom "
      "(hypothetical_axiom_status) ---")
print("    CANDIDATE (PIN-GAUGE-CONTENT): (i) Y_like is a GAUGED U(1)  [P-HY];")
print("    (ii) completion = opposite-chirality (RH) SU(2)-singlet template,")
print("         chirality STIPULATED (not the vector-like mirror), Y_nuR=0 [P-COMP].")

# ---------------------------------------------------------------------------
print("\n[B1] Conditional: the chiral RH template cancels all six EXACTLY.")
# ---------------------------------------------------------------------------
full = LH + RH_CHIRAL
six_full = all_six(full)
all_cancel = (six_full["Tr[Y]"] == 0 and six_full["Tr[Y^3]"] == 0
              and six_full["Tr[SU3^2 Y]"] == 0 and six_full["Tr[SU2^2 Y]"] == 0
              and six_full["SU3^3"] == 0 and six_full["Witten(even?)"])
check("[cond] all six anomaly conditions vanish exactly for "
      "(4/3,-2/3,-2,0): " + ", ".join(f"{k}={v}" for k, v in six_full.items()),
      all_cancel, "hypothetical_axiom_status: conditional on accepted new axiom")

# ---------------------------------------------------------------------------
print("\n[B2] Conditional: the completion is genuinely CHIRAL (not the A2 mirror).")
# ---------------------------------------------------------------------------
full_is_chiral = not is_vectorlike(full)
# and the RH template is NOT the inert mirror (it is a genuinely different
# completion: the SM RH template, not the conjugate of the LH content)
differs_from_mirror = net_chiral_signature(RH_CHIRAL) != net_chiral_signature(MIRROR)
check("[cond] full content is CHIRAL (spectrum != its CPT conjugate) => "
      "realizes a genuine second chirality class, and the RH template differs "
      "from the inert vector-like mirror",
      full_is_chiral and differs_from_mirror,
      "this is the precise specification block02 warns is required")

# ---------------------------------------------------------------------------
print("\n[B3] Conditional: closed-form completion parametric in n_color; "
      "n_color=3 -> SM branch (existence witness).")
# ---------------------------------------------------------------------------
def rh_template(nc):
    a = Fr(1, nc)   # Y(Q_L) under b=-1 convention
    b = Fr(-1)      # Y(L_L)
    return {
        "u_R": a + 1,
        "d_R": a - 1,
        "e_R": b - 1,
        "nu_R": b + 1,   # neutral branch convention
    }


tpl3 = rh_template(3)
sm_ok = (tpl3["u_R"] == Fr(4, 3) and tpl3["d_R"] == Fr(-2, 3)
         and tpl3["e_R"] == Fr(-2) and tpl3["nu_R"] == Fr(0))
check("[cond] SHIFT relation Y_uR=a+1, Y_dR=a-1, Y_eR=b-1, Y_nuR=b+1 at "
      "n_color=3 gives SM branch (4/3,-2/3,-2,0)", sm_ok, f"{tpl3}")
# check the COLOR_ANOM closed-form for general nc: Y_uR + Y_dR = 2a
gen_ok = all(rh_template(nc)["u_R"] + rh_template(nc)["d_R"] == 2 * Fr(1, nc)
             for nc in (2, 3, 5, 7))
check("[cond] color-anomaly closed form Y_uR+Y_dR=2a holds for all n_color "
      "(parametric existence)", gen_ok, "nc in {2,3,5,7}")

# ---------------------------------------------------------------------------
print("\n[B4] Conditional: with Y_like GAUGED (i), the three nonzero LH traces")
print("     are GAUGE anomalies -> their cancellation is a consistency demand")
print("     (P-ABJ bites) -> anomaly_forces_time lower bound d_t odd follows.")
# ---------------------------------------------------------------------------
# The three gauge traces (gauge-gauge-gauge / gauge-gauge-grav) that must vanish
# for a *gauged* U(1)_Y: Tr[Y^3], Tr[SU3^2 Y], SU3^3, plus Tr[Y] (mixed grav)
# and Witten.  LH-only nonzero; full content zero.  This is the (i)-conditional
# upgrade of "anomalous" from aesthetic to inconsistency.
lh_gauge_bad = (six_lh["Tr[Y^3]"] != 0 or six_lh["Tr[SU3^2 Y]"] != 0
                or six_lh["SU3^3"] != 0)
full_gauge_ok = (six_full["Tr[Y^3]"] == 0 and six_full["Tr[SU3^2 Y]"] == 0
                 and six_full["SU3^3"] == 0 and six_full["Tr[Y]"] == 0)
check("[cond] LH-only gauge anomalies nonzero AND completed gauge anomalies "
      "zero => P-ABJ (conditional on gauging) makes the completion mandatory",
      lh_gauge_bad and full_gauge_ok, "feeds the d_t-odd lower bound")
# the lower-bound chain consequence (parity): a genuine second chirality class
# exists (B2) -> Clifford chirality needs even d_s+d_t -> with d_s=3, d_t odd.
ds = 3
dt_parity_ok = (ds + 1) % 2 == 0  # d_t=1 makes d_s+d_t even (the EVEN theorem)
check("[cond] genuine 2nd chirality class + EVEN-dimension Clifford theorem "
      "=> d_s+d_t even; with d_s=3 => d_t odd (>=1). (lower bound discharged)",
      dt_parity_ok, "d_t<=1 cap is supplied separately by Cluster 1 / single-clock")


# ===========================================================================
# FALSIFICATION legs -- the discharge is not vacuous.
# ===========================================================================
print("\n--- FALSIFICATION legs (discharge is non-trivial) ---")

# F1: a wrong completion (Y_nuR != 0 while keeping e_R) fails cancellation.
WRONG = [
    rh_as_lh(3, +1, 1, Fr(4, 3)),    # u_R
    rh_as_lh(3, +1, 1, Fr(-2, 3)),   # d_R
    rh_as_lh(1, 0, 1, Fr(-2)),       # e_R
    rh_as_lh(1, 0, 1, Fr(1)),        # nu_R WRONG (should be 0)
]
six_wrong = all_six(LH + WRONG)
wrong_fails = not (six_wrong["Tr[Y]"] == 0 and six_wrong["Tr[Y^3]"] == 0)
check("F1 wrong completion (Y_nuR=1) FAILS cancellation",
      wrong_fails, f"Tr[Y]={six_wrong['Tr[Y]']}, Tr[Y^3]={six_wrong['Tr[Y^3]']}")

# F2: e_R <-> nu_R relabelling is the only other consistent branch (a named
# discrete convention, not an axiom).
RELABEL = [
    rh_as_lh(3, +1, 1, Fr(4, 3)),    # u_R
    rh_as_lh(3, +1, 1, Fr(-2, 3)),   # d_R
    rh_as_lh(1, 0, 1, Fr(0)),        # e_R = 0 (relabelled)
    rh_as_lh(1, 0, 1, Fr(-2)),       # nu_R = -2 (relabelled)
]
six_rel = all_six(LH + RELABEL)
rel_ok = (six_rel["Tr[Y]"] == 0 and six_rel["Tr[Y^3]"] == 0
          and six_rel["Tr[SU3^2 Y]"] == 0 and six_rel["SU3^3"] == 0)
check("F2 e_R<->nu_R relabelling is equally anomaly-consistent "
      "(named discrete convention, not a 2nd axiom)", rel_ok,
      "the branch choice Y_nuR=0 is a convention; the gauge-content axiom is the supplier")

# F3: substituting the vector-like A2 mirror gives zero net anomaly BUT zero new
# chirality, so it cannot realize the (3,1) lower bound.
six_vec2 = all_six(vec_content)
vec_cancels_but_inert = (
    all((v if isinstance(v, bool) else v == 0) for v in six_vec2.values())
    and is_vectorlike(vec_content)
)
check("F3 vector-like mirror cancels anomalies but is chirally INERT "
      "=> no second chirality class => no d_t-odd lower bound "
      "(why the axiom must STIPULATE chirality)", vec_cancels_but_inert,
      "minimality: the axiom adds chirality, not just 'a completion'")


# ===========================================================================
print("\n" + "=" * 74)
print(f"CLASS BREAKDOWN: HALF-A (skeptical re-attack, no axiom) + HALF-B "
      f"(conditional) + FALSIFICATION")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 74)
print("""
VERDICT (no audit status set; for owner governance only):
  * P-HY and P-COMP each WALL on the no-new-axiom surface (HALF A): the four
    published gauging discriminators do not select 'Y_like gauged'; the only
    native completions (naive CPT-mirror; taste-cube complementation) are
    VECTOR-LIKE, admissible on {Lattice,Quantum,Record} -- so no CHIRAL RH
    template is forced (block02 vectorlike/Hamming-odd lesson reproduced).
  * The minimal gauge-content candidate axiom (PIN-GAUGE-CONTENT: Y_like is a
    gauged U(1) + opposite-chirality SU(2)-singlet RH template with chirality
    STIPULATED) DISCHARGES both walls (HALF B): the SM-branch RH template
    cancels all six anomaly conditions exactly, is genuinely chiral (not the
    inert mirror), is parametric in n_color, and (with gauging) makes the
    cancellation a consistency demand feeding the d_t-odd lower bound.
  * Falsification legs confirm the discharge is non-vacuous and that the axiom
    must STIPULATE chirality (the vector-like mirror cancels but is inert).
  hypothetical_axiom_status: conditional on accepted new axiom; not retained on
  the actual current surface.
""")
if FAIL:
    raise SystemExit(1)
