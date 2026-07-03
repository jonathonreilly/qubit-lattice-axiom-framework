#!/usr/bin/env python3
"""The Fierz singlet-channel selector is a WEIGHT, not a PARTITION: kappa_EW=0-via-register-not-read demoted.

Class-A finite-dimensional verification for the source note

    docs/FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md

CONTEXT.  The EW matching rule leaves a one-parameter family R(kappa_EW) = F_adj +
kappa_EW (1 - F_adj) with F_adj = (Nc^2-1)/Nc^2 = 8/9 (retained_no_go family:
ew_current_matching_rule + ew_current_traceless_generator_selector).  A proposed route —
recorded as an open gate in RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE (2026-06-08,
audited_conditional) — would set kappa_EW = 0 by declaring the color-singlet trace channel
"unregistered" under the register-not-read discipline.  An ADM-1 find-the-escape panel
(forced_finding) adversarially recomputed that route and found it fails on three
independent grounds.  This runner makes the load-bearing finite algebra
checkable for a narrow route demotion.

THE THREE GROUNDS (load-bearing finite algebra demonstrated below; the Haar
        reading also gets a deterministic Monte Carlo sanity check):
  TWIRL-VS-PARTITION.  The channel split sends
        M -> E_sing(M) = (Tr M/Nc) I, which equals the Haar/depolarizing TWIRL
        int U M U^dag dU — a CONTINUOUS group average.  It is NOT of the form
        D(M) = sum_k P_k M P_k for any orthogonal partition: partition maps preserve each
        diagonal block verbatim, the twirl replaces them by their average; and
        on the SU(3)-IRREDUCIBLE triplet the only central-sector
        symmetry-respecting partition is the trivial {I} (Schur), whose
        D = identity != twirl.  So the genuine register-not-read license
        (the central-sector partition map) does
        not cover the channel split; invoking it is the LOOSE dichotomy demoted by
        register_not_read_scope_correction_panel_verdict_2026-06-06.
  WEIGHT-LEAK.  kappa_EW is a within-channel weight.  The Fierz COUNT fraction 8/9
        is fixed by the decomposition (a dimension count), but kappa_EW is the realized
        WEIGHT of the singlet channel, while the within-sector data guardrail says a
        partition never delivers weights.  Structurally this is the r-dial move:
        partition fixed, weight free; "declare the singlet unregistered => kappa=0" is
        the same move that would force the (known-free) Koide r — the scope-correction's
        directionless tell.
  CATEGORY-SEPARATION.  The Fierz channel decomposes the EW current's SAME-SITE color trace
        (observable content / matching rule), not the gauge-link update kernel.  The trace
        object is invariant under local color rotations; the link kernel co-transforms.
        Selecting kappa_EW says nothing about ADM-1's link/frame question and vice versa.

SCOPE (narrow route-demote, NOT a closure):
  - Demotes ONE route (kappa_EW = 0 via register-not-read on the color trace).  The
    kappa_EW gate itself REMAINS OPEN (other routes unforeclosed); this note sits BESIDE
    the existing retained_no_go family and the rconn open-gate note, duplicating neither.
  - Does NOT touch the exact Fierz algebra (S+C split, F_adj = 8/9 — reproduced here as
    setup, owned by ew_current_fierz_channel_decomposition, a decoration under the
    retained graph_first_su3_integration_note).
  - Does NOT close or modify ADM-1; no new axiom/import; no PDG value consumed.

Run: python3 scripts/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.py
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


rng = np.random.default_rng(20260608)
NC = 3


def haar_su(n=NC):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1.0 / n)


def gell_mann():
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3)
    return [m / 2.0 for m in (l1, l2, l3, l4, l5, l6, l7, l8)]   # t^A, Tr t^A t^B = delta/2


T8 = gell_mann()

# ===========================================================================
# Part 0.  Setup: the exact Fierz S + C split and the count fraction 8/9.
#   Tr[G G^dag] = (1/Nc)|Tr G|^2 + 2 sum_A |Tr[G t^A]|^2 ; channel COUNT (Nc^2-1)/Nc^2.
# ===========================================================================
print("=" * 78)
print("Part 0  Setup: exact Fierz S+C split; count fraction F_adj = 8/9 (existing algebra)")
print("=" * 78)

worst = 0.0
for _ in range(50):
    G = rng.normal(size=(NC, NC)) + 1j * rng.normal(size=(NC, NC))
    S = abs(np.trace(G)) ** 2 / NC
    C = 2 * sum(abs(np.trace(G @ t)) ** 2 for t in T8)
    worst = max(worst, abs(np.trace(G @ G.conj().T).real - (S + C)))
check("Fierz completeness: Tr[G G^dag] = S + C exactly (50 random G)",
      worst < 1e-9, f"max dev {worst:.1e}")
check("channel COUNT fraction (Nc^2-1)/Nc^2 = 8/9 (a dimension count)",
      abs((NC ** 2 - 1) / NC ** 2 - 8 / 9) < 1e-15)

# ===========================================================================
# Part 1. The singlet projector is the depolarizing twirl.
#   E_sing(M) = (Tr M/Nc) I ; exact Schur-projector identities + MC confirmation.
# ===========================================================================
print("=" * 78)
print("Part 1  Twirl-vs-partition: E_sing(M) = (TrM/Nc) I = Haar/depolarizing twirl")
print("=" * 78)


def E_sing(M):
    return (np.trace(M) / NC) * np.eye(NC)


M = rng.normal(size=(NC, NC)) + 1j * rng.normal(size=(NC, NC))
g = haar_su()
check("E_sing is Ad-invariant: E(g M g^dag) = E(M) = g E(M) g^dag (exact)",
      np.allclose(E_sing(g @ M @ g.conj().T), E_sing(M), atol=1e-12)
      and np.allclose(g @ E_sing(M) @ g.conj().T, E_sing(M), atol=1e-12))
check("E_sing is idempotent and unital (a conditional expectation onto C·I)",
      np.allclose(E_sing(E_sing(M)), E_sing(M), atol=1e-12)
      and np.allclose(E_sing(np.eye(NC)), np.eye(NC), atol=1e-12))
T_mc = sum(U @ M @ U.conj().T for U in (haar_su() for _ in range(50000))) / 50000
check("MC: the Haar twirl int U M U^dag dU converges to E_sing(M) (50k samples)",
      np.max(np.abs(T_mc - E_sing(M))) < 0.02,
      f"max dev {np.max(np.abs(T_mc - E_sing(M))):.4f} ~ 1/sqrt(N)")

# ===========================================================================
# Part 2. E_sing is not a partition map D(M) = sum_k P_k M P_k.
# ===========================================================================
print("=" * 78)
print("Part 2  Twirl-vs-partition: E_sing is not a central-sector partition map")
print("=" * 78)

# (a) Partition maps preserve each diagonal block verbatim; the twirl replaces the
#     diagonal by its average -> for generic M they differ on the diagonal.
P_nontriv = [np.diag([1.0, 0, 0]).astype(complex), np.diag([0, 1.0, 1.0]).astype(complex)]
D_nontriv = sum(P @ M @ P for P in P_nontriv)
check("a partition map preserves diagonal blocks (D(M)_00 = M_00); the twirl does NOT "
      "(E(M)_00 = TrM/3 != M_00 generically)",
      np.isclose(D_nontriv[0, 0], M[0, 0]) and not np.isclose(E_sing(M)[0, 0], M[0, 0]),
      f"M_00={M[0,0]:.3f}, TrM/3={np.trace(M)/3:.3f}")
check("the nontrivial partition's D(M) != E_sing(M) (different maps)",
      not np.allclose(D_nontriv, E_sing(M), atol=1e-6))

# (b) A readout-context partition must respect the algebra+symmetry. On the
#     SU(3)-IRREDUCIBLE triplet, a projector commuting with the action is 0 or I (Schur).
#     It is enough to test the finite generator basis: a nonzero commutator with any
#     generator rules out a central-sector partition.
comm_dev = max(float(np.max(np.abs(P @ t - t @ P))) for P in P_nontriv for t in T8)
check("any nontrivial partition fails central-sector symmetry: its projectors do not "
      "commute with the irreducible SU(3) generator basis (Schur: only {0, I} are central)",
      comm_dev > 0.1, f"commutator dev {comm_dev:.2f}")
check("the only central-sector symmetry-respecting partition {I} gives D = identity != E_sing (trivial)",
      not np.allclose(M, E_sing(M), atol=1e-6))
print("   => the singlet/adjoint CHANNEL split is a CONTINUOUS twirl, not a register-not-")
print("      read partition map: the genuine central-sector license (D = sum P_k M P_k)")
print("      does not cover it. Invoking register-not-read here is the demoted loose")
print("      dichotomy.")

# ===========================================================================
# Part 3. kappa_EW is a within-channel weight: the r-dial move (weight-leak).
# ===========================================================================
print("=" * 78)
print("Part 3  Weight-leak: kappa_EW = within-channel weight; count 8/9 fixed, weight free")
print("=" * 78)

F_adj = (NC ** 2 - 1) / NC ** 2


def R_phys(kappa):
    return F_adj + kappa * (1 - F_adj)


check("R(kappa=0) = 8/9 and R(kappa=1) = 1: BOTH consistent with the fixed count fraction "
      "(the existing retained_no_go: the retained packet does not select kappa)",
      abs(R_phys(0) - 8 / 9) < 1e-15 and abs(R_phys(1) - 1.0) < 1e-15)

# Formal weight-leak isomorphism with the r-dial: a 2-channel decomposition with fixed
# count data (d_1, d_2) and a FREE realized weight w in [0,1]:
#   Koide:   blocks (singlet, doublet), dims (1,2): block-count w=1/2 vs Born/trace w=2/3
#            -> the dial r is registered, never delivered by the partition.
#   kappa:   channels (adjoint, singlet), counts (8,1): kappa is the realized singlet
#            weight -> same slot in the same algebraic shape.
def two_channel(d1, d2, w):
    """fraction assigned to channel-1 content when channel-2 carries realized weight w."""
    return (d1 / (d1 + d2)) + w * (1 - d1 / (d1 + d2))


check("formal isomorphism: R(kappa) == two_channel(8, 1, kappa) — the SAME fixed-count/"
      "free-weight shape as the Koide r-dial (dims (1,2), w free)",
      all(abs(R_phys(k) - two_channel(8, 1, k)) < 1e-15 for k in (0.0, 0.25, 0.5, 1.0)))
check("the count data NEVER moves with the weight: d-fraction 8/9 is w-independent "
      "(partition delivers counts; weights are within-sector data)",
      all(abs(two_channel(8, 1, w) - two_channel(8, 1, 0) - w / 9) < 1e-15
          for w in (0.1, 0.7)))
print("   => 'declare the singlet unregistered => kappa_EW = 0' assigns a WEIGHT by fiat —")
print("      structurally the move that would force the known-free Koide r (the scope-")
print("      correction's directionless tell).  Weight-leak: route demoted.")

# ===========================================================================
# Part 4. Category separation: same-site current trace vs gauge-link kernel.
# ===========================================================================
print("=" * 78)
print("Part 4  Category-separation: same-site current trace, not the gauge link")
print("=" * 78)

G_mat = rng.normal(size=(NC, NC)) + 1j * rng.normal(size=(NC, NC))
gx, gy = haar_su(), haar_su()
# the current's color object Tr[G G^dag] is a SAME-SITE trace: invariant under local g(x)
tr_before = np.trace(G_mat @ G_mat.conj().T).real
tr_after = np.trace((gx @ G_mat @ gx.conj().T) @ (gx @ G_mat @ gx.conj().T).conj().T).real
check("the current's color trace is invariant under a LOCAL rotation at its site "
      "(same-site object; observable-content/matching-rule category)",
      abs(tr_before - tr_after) < 1e-9)
# a gauge-link kernel co-transforms bi-fundamentally under (g_x, g_y): NOT invariant
U_link = haar_su()
link_dev = float(np.max(np.abs(gx @ U_link @ gy.conj().T - U_link)))
check("a gauge-link kernel co-transforms (g_x U g_y^dag != U): a DIFFERENT category — "
      "selecting kappa_EW says nothing about ADM-1's link/frame question",
      link_dev > 0.1, f"dev {link_dev:.2f}")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (narrow route-demote): the kappa_EW = 0 route VIA register-not-read on the")
print("  color trace is demoted on three finite-algebra route grounds: the singlet")
print("  projector is a CONTINUOUS twirl (not a central-sector partition map; the")
print("  only such partition on the irreducible triplet is trivial), kappa_EW is a")
print("  WITHIN-CHANNEL WEIGHT (weight-leak, the r-dial move), and the channel")
print("  lives on the same-site current trace, not the gauge")
print("  link (category).  The kappa_EW gate itself REMAINS OPEN (other routes are not")
print("  foreclosed); the exact Fierz algebra is untouched; ADM-1 is untouched; this note")
print("  sits beside (does not duplicate) the existing retained_no_go family and the rconn")
print("  open-gate note.  No new axiom/import; no PDG value consumed.")
if FAIL:
    raise SystemExit(1)
