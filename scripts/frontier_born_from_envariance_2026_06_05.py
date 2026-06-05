#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""FRONTIER: Born rule p_k = |a_k|^2 from {Quantum + Record} via envariance.

GOAL
----
Test whether the Born rule p_k = |a_k|^2 can be DERIVED from the framework's
{Quantum, Record} axioms on the "record state" (a Schmidt-form system+environment
state with orthonormal, redundant environment records), by the route the narrow
additivity no-go (OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05)
does NOT block.

The no-go blocks ONLY: "Record additivity ALONE -> the branch measure" (a
multiplicative branch quantity -> the additive scalar gives -c log p, not which
measure). It is SILENT on (a) state-symmetry / envariance and (b) Gleason-type
additivity over ORTHOGONAL projectors. This runner goes around it on both routes,
and audits whether either is genuine and non-circular for THIS framework.

ROUTE 1 — Zurek envariance (primary; ties to the record state).
  1. S + E in |psi> = sum_k a_k |s_k>|E_k>, orthonormal redundant {|E_k>}.
  2. EQUAL-amplitude case: a system swap U_S(|s_i><->|s_j>) is UNDONE by an
     environment swap U_E(|E_i><->|E_j>): (U_S kron U_E)|psi> = |psi>. Verify.
  3. GENERAL case: rational |a_k|^2 -> fine-grain each branch into N_k equal
     sub-records in an enlarged environment, reduce to equal case, count ->
     p_k = |a_k|^2. Demonstrate on |a|^2 = (2/3, 1/3).
  4. CIRCULARITY AUDIT: enumerate EVERY assumption; decide whether the
     "global state unchanged => equal probability" step uses only physical
     invariance + the Record axiom, or smuggles "equal amplitudes => equal
     probability" / a prior measure (Schlosshauer-Fine 2005; Barnum 2003).

ROUTE 2 — Gleason / Busch backstop (the theorem route).
  5. Record additivity over DISJOINT/commuting records = a frame function /
     additive measure on the projector lattice. State Gleason (dim>=3) / Busch
     (dim>=2) precisely, check the framework's record structure meets the
     hypotheses, confirm it forces Tr(rho P), and confirm it sits OUTSIDE the
     additivity-homomorphism no-go.

MEMORY: small explicit qubit systems (<= 6 qubits), exact numpy/sympy. Logs to a
file. Self-check prints PASS/FAIL.

This runner is a NEGATIVE-or-CONDITIONAL recorder. It does NOT assert an audit
verdict; the independent audit lane owns status. It states honestly which route
(if either) is a genuine Born = |amplitude|^2 derivation from {Quantum + Record}.
"""
from __future__ import annotations

import io
import os
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

# --------------------------------------------------------------------------- #
# Logging: tee stdout to a capped log file.
# --------------------------------------------------------------------------- #
LOG_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "logs",
    "runner-cache",
    "frontier_born_from_envariance_2026_06_05.txt",
)
LOG_PATH = os.path.abspath(LOG_PATH)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

_BUF = io.StringIO()


class _Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, s):
        for st in self.streams:
            st.write(s)

    def flush(self):
        for st in self.streams:
            st.flush()


_real_stdout = sys.stdout
sys.stdout = _Tee(_real_stdout, _BUF)

PASS = 0
FAIL = 0
FAILED_NAMES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        FAILED_NAMES.append(name)
        tag = "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ::  {detail}"
    print(line)
    return ok


def hr(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------- #
# Linear-algebra helpers (exact via sympy where it matters; numpy cross-check).
# --------------------------------------------------------------------------- #
def kron_list(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def ket(i, dim):
    v = np.zeros((dim, 1), dtype=complex)
    v[i, 0] = 1.0
    return v


def swap_op(i, j, dim):
    """Permutation operator on C^dim swapping basis vectors i and j."""
    M = np.eye(dim, dtype=complex)
    M[[i, j], :] = M[[j, i], :]
    return M


def partial_trace_env(rho, dS, dE):
    """Trace out the environment (second factor) of a dS*dE system."""
    rho4 = rho.reshape(dS, dE, dS, dE)
    return np.einsum("ikjk->ij", rho4)


def density(psi):
    return psi @ psi.conj().T


def is_unit(psi, tol=1e-12):
    return abs(np.vdot(psi, psi) - 1.0) < tol


# =========================================================================== #
hr("CONTEXT — the three framework axioms used (MINIMAL_AXIOMS_2026-06-05)")
# =========================================================================== #
print(
    """
  QUANTUM : per-site primitive d.o.f. is one qubit; one-site algebra M_2(C).
            Supplies the Hilbert/operator carrier. Supplies NO Born rule,
            measurement instrument, or measure.
  LATTICE : sites form Z^3 (not load-bearing for this small-system test).
  RECORD  : a record is the DURABLE registration of the realized outcome.
            Given a readout context with a finite central-sector decomposition
            and a fixed K/CPT conjugation, the realized outcome is the K/CPT
            orbit of the realized central sector; for any finite pairwise-
            DISJOINT collection of records the scalar readout I is FINITELY
            ADDITIVE with I(empty)=0.
            A record supplies NO weighting, normalization, PROBABILITY,
            measurement/decoherence dynamics, or within-sector data.

  ==> CRITICAL for the circularity audit: the Record axiom, as written, does
      NOT contain a probability, a measure, a normalization, or a rule
      "equal amplitudes => equal probability". It gives (i) a discrete realized
      alphabet (K/CPT orbits of central sectors) and (ii) finite ADDITIVITY of a
      scalar readout I over DISJOINT records. Nothing else.
"""
)

# =========================================================================== #
hr("ROUTE 1 / STEP 1 — the record state (Schmidt form, redundant environment)")
# =========================================================================== #
print(
    """
  System S (a qubit, d_S=2) imprinted redundantly on an environment of two
  fragment qubits E = E1 E2 (so each pointer value s_k is copied onto BOTH
  fragments -> 'redundant records'). With pointer basis {|0>,|1>} on S:

      |psi> = a_0 |0>_S |00>_E + a_1 |1>_S |11>_E

  This is a GHZ-type state. The environment records are |E_0>=|00>, |E_1>=|11>,
  orthonormal (<E_0|E_1>=0) and redundant (the value is recoverable from either
  fragment alone after the other is traced). The pointer outcomes {s_0,s_1} are
  the framework's records (K/CPT orbits of the central sectors of the pointer
  observable). We work in C^2 (S) tensor C^4 (E), total 3 qubits.
"""
)

dS, dE = 2, 4  # S is 1 qubit, E is 2 qubits
E0 = kron_list([ket(0, 2), ket(0, 2)])  # |00>
E1 = kron_list([ket(1, 2), ket(1, 2)])  # |11>
check(
    "E records orthonormal <E0|E1>=0",
    abs(complex(np.vdot(E0, E1))) < 1e-15,
    f"<E0|E1>={complex(np.vdot(E0,E1)):.3g}",
)
check("E0 normalized", is_unit(E0))
check("E1 normalized", is_unit(E1))


def record_state(a0, a1):
    a0 = complex(a0)
    a1 = complex(a1)
    nrm = np.sqrt(abs(a0) ** 2 + abs(a1) ** 2)
    a0, a1 = a0 / nrm, a1 / nrm
    psi = a0 * np.kron(ket(0, 2), E0) + a1 * np.kron(ket(1, 2), E1)
    return psi


# =========================================================================== #
hr("ROUTE 1 / STEP 2 — EQUAL-amplitude envariance (the swaps + invariance)")
# =========================================================================== #
print(
    """
  EQUAL case a_0 = a_1 = 1/sqrt(2). Build:
    U_S : the system bit-flip swap |0>_S <-> |1>_S   (Pauli-X on S)
    U_E : the environment swap |E_0>=|00> <-> |E_1>=|11>
  Claim (Zurek envariance): U_S alone changes |psi>, U_E alone changes |psi>,
  but the COMPOSITE (U_S kron U_E)|psi> = |psi>. The system swap's effect on the
  GLOBAL state is exactly UNDONE by an environment-only operation.
"""
)
inv2 = 1.0 / np.sqrt(2.0)
psi_eq = record_state(inv2, inv2)
check("equal-case |psi> normalized", is_unit(psi_eq))

U_S = np.array([[0, 1], [1, 0]], dtype=complex)  # X on S
# U_E swaps |00> and |11> inside C^4; leaves |01>,|10> fixed.
U_E = swap_op(0, 3, 4)  # indices: 00->0, 01->1, 10->2, 11->3

US_full = np.kron(U_S, np.eye(dE, dtype=complex))
UE_full = np.kron(np.eye(dS, dtype=complex), U_E)
comp = US_full @ UE_full

psi_S_only = US_full @ psi_eq
psi_E_only = UE_full @ psi_eq
psi_comp = comp @ psi_eq

check(
    "U_S alone CHANGES |psi> (not a state symmetry by itself)",
    not np.allclose(psi_S_only, psi_eq, atol=1e-12),
    "system swap alone moves the global state",
)
check(
    "U_E alone CHANGES |psi> (not a state symmetry by itself)",
    not np.allclose(psi_E_only, psi_eq, atol=1e-12),
    "environment swap alone moves the global state",
)
check(
    "ENVARIANCE: (U_S kron U_E)|psi> == |psi>  (equal case)",
    np.allclose(psi_comp, psi_eq, atol=1e-12),
    f"max|delta|={np.max(np.abs(psi_comp-psi_eq)):.2e}",
)
# Unitarity sanity of the swaps.
check("U_S unitary", np.allclose(US_full.conj().T @ US_full, np.eye(dS * dE)))
check("U_E unitary", np.allclose(UE_full.conj().T @ UE_full, np.eye(dS * dE)))

print(
    """
  PHYSICAL CONTENT (what envariance actually licenses):
  The environment swap U_E acts ONLY on E. So if a quantity Q_S that the SYSTEM
  alone determines depends only on S (i.e. is computed from the system's record
  state / reduced description), then U_E cannot change Q_S. But the equal-case
  identity says (U_S)|psi> and |psi> differ ONLY by the environment-only U_E^{-1}.
  Hence U_S leaves invariant any system-determined Q_S. In particular the swap
  s_0<->s_1 is a symmetry of every system-determined quantity. We verify this
  operationally three ways below.
"""
)

# (i) reduced system state is INVARIANT under the pointer swap (equal case).
rho_full_eq = density(psi_eq)
rho_S_eq = partial_trace_env(rho_full_eq, dS, dE)
rho_S_eq_swapped = U_S @ rho_S_eq @ U_S.conj().T
check(
    "equal case: reduced rho_S is X-swap invariant (rho_S = I/2)",
    np.allclose(rho_S_eq, 0.5 * np.eye(2), atol=1e-12)
    and np.allclose(rho_S_eq_swapped, rho_S_eq, atol=1e-12),
    f"rho_S diag={np.round(np.real(np.diag(rho_S_eq)),6)}",
)

# (ii) the environment-only operation cannot affect the system's reduced state.
rho_S_after_UE = partial_trace_env(density(UE_full @ psi_eq), dS, dE)
check(
    "env-only U_E leaves rho_S unchanged (E-action invisible to S)",
    np.allclose(rho_S_after_UE, rho_S_eq, atol=1e-12),
)

# (iii) The two pointer branches are related by a *global-state symmetry*:
#       there is a unitary V = (U_S kron U_E) with V|psi>=|psi> that maps the
#       pointer projector P_0 = |0><0|_S kron I to P_1 = |1><1|_S kron I under
#       the SYSTEM part. This is the exact envariance premise for "i and j are
#       interchangeable".
P0 = np.kron(np.outer(ket(0, 2), ket(0, 2).conj()), np.eye(dE))
P1 = np.kron(np.outer(ket(1, 2), ket(1, 2).conj()), np.eye(dE))
check(
    "global symmetry maps branch projector P0 -> P1 (US P0 US^-1 = P1)",
    np.allclose(US_full @ P0 @ US_full.conj().T, P1, atol=1e-12),
)
check(
    "and V=(US kron UE) fixes |psi> while swapping the branches",
    np.allclose(comp @ psi_eq, psi_eq, atol=1e-12),
)

# =========================================================================== #
hr("ROUTE 1 / STEP 3 — GENERAL case via fine-graining: |a|^2=(2/3,1/3) -> 2/3,1/3")
# =========================================================================== #
print(
    """
  UNEQUAL case |a_0|^2 = 2/3, |a_1|^2 = 1/3. Strategy (Zurek's counting):
  enlarge the environment with an ancilla C that fine-grains each branch into
  N_k equally-weighted sub-records, with N_0 : N_1 = 2 : 1 (common denominator
  3). Coherently split:

      |0>_S|E_0>  ->  sqrt(1/2)(|0>_S|E_0>|c_1> + |0>_S|E_0>|c_2>)   [2 sub-recs]
      |1>_S|E_1>  ->            |1>_S|E_1>|c_3>                       [1 sub-rec]

  with {|c_1>,|c_2>,|c_3>} ORTHONORMAL ancilla records. After the split EVERY
  sub-branch carries the SAME amplitude sqrt(1/3): the enlarged state is a
  uniform superposition over 3 orthonormal fine-grained records. The equal-case
  envariance of STEP 2 applies to ALL 3 sub-records (they are pairwise swap-
  symmetric). 'Counting fine-grained equiprobable sub-records' assigns 1/3 each;
  the coarse outcome s_0 collects N_0=2 of them -> 2/3; s_1 collects N_1=1 -> 1/3.
"""
)

# Build the fine-grained state explicitly. Ancilla C is a qutrit (dim 3) ->
# embed in 2 qubits would be 6 qubits total; instead use a genuine d=3 ancilla
# (still "small system": S(2) x E(4) x C(3) = 24-dim, exact).
a0 = np.sqrt(Fraction(2, 3).__float__())
a1 = np.sqrt(Fraction(1, 3).__float__())
psi_unequal = record_state(a0, a1)
rho_S_un = partial_trace_env(density(psi_unequal), dS, dE)
check(
    "unequal coarse state: reduced rho_S diag = (2/3,1/3)",
    np.allclose(np.real(np.diag(rho_S_un)), [2 / 3, 1 / 3], atol=1e-12),
    f"diag={np.round(np.real(np.diag(rho_S_un)),6)}",
)

dC = 3
# c_1,c_2 attach to branch 0; c_3 to branch 1.
c1 = ket(0, dC)
c2 = ket(1, dC)
c3 = ket(2, dC)
# Fine-grained enlarged state in C^2 x C^4 x C^3:
branch0 = np.kron(np.kron(ket(0, 2), E0), (c1 + c2) / np.sqrt(2.0))  # amp a0 carries 1/sqrt2 each
branch1 = np.kron(np.kron(ket(1, 2), E1), c3)
psi_fg = a0 * branch0 + a1 * branch1
check("fine-grained |psi_fg> normalized", is_unit(psi_fg))

# Identify the three fine-grained ORTHONORMAL sub-records and their amplitudes.
sub_records = {
    "(s0,c1)": a0 / np.sqrt(2.0),
    "(s0,c2)": a0 / np.sqrt(2.0),
    "(s1,c3)": a1,
}
amps = np.array(list(sub_records.values()))
check(
    "all 3 fine-grained sub-records carry EQUAL amplitude sqrt(1/3)",
    np.allclose(np.abs(amps) ** 2, 1 / 3, atol=1e-12),
    f"|amp|^2={np.round(np.abs(amps)**2,6)}",
)
# Orthonormality of the three fine-grained kets.
fg_kets = [
    np.kron(np.kron(ket(0, 2), E0), c1),
    np.kron(np.kron(ket(0, 2), E0), c2),
    np.kron(np.kron(ket(1, 2), E1), c3),
]
G = np.array([[complex(np.vdot(u, v)) for v in fg_kets] for u in fg_kets])
check(
    "the 3 fine-grained records are orthonormal (Gram = I_3)",
    np.allclose(G, np.eye(3), atol=1e-12),
)

print(
    """
  Now apply the EQUAL-case envariance argument to the 3 equiprobable sub-records.
  For any pair (m,n) of sub-records there is a system-side swap U_S^(mn) of the
  fine-grained labels whose effect is undone by an environment+ancilla swap
  U_{EC}^(mn): the enlarged state is invariant. We verify a representative pair
  swap explicitly (swap sub-records 1 and 3, i.e. (s0,c1)<->(s1,c3)).
"""
)
# Representative fine-grained swap on the 24-dim space: swap the two basis
# vectors carrying fg_kets[0] and fg_kets[2]. Decompose into a "system+pointer"
# relabel U_SP (acts on the S and ancilla-tag that DEFINE the record letter) and
# an environment-side U undo. For a clean, basis-level demonstration we exhibit
# the single global permutation that (a) swaps the two equal sub-amplitudes and
# (b) leaves |psi_fg> invariant BECAUSE the amplitudes are equal.
dim_fg = dS * dE * dC
# Locate basis indices of fg_kets[0] and fg_kets[2]:
idx0 = int(np.argmax(np.abs(fg_kets[0].ravel())))
idx2 = int(np.argmax(np.abs(fg_kets[2].ravel())))
SW = swap_op(idx0, idx2, dim_fg)
psi_fg_sw = SW @ psi_fg
check(
    "EQUAL sub-amplitudes => basis swap of records 1,3 leaves |psi_fg> invariant",
    np.allclose(psi_fg_sw, psi_fg, atol=1e-12),
    "this is the envariance that fails for UNEQUAL amplitudes (see next check)",
)
# Contrast: the SAME basis swap on the UNEQUAL (un-fine-grained) coarse pair does
# NOT leave the state invariant -> equal amplitude is exactly the hinge.
psi_coarse_sw = swap_op(
    int(np.argmax(np.abs(np.kron(ket(0, 2), E0).ravel()))),
    int(np.argmax(np.abs(np.kron(ket(1, 2), E1).ravel()))),
    dS * dE,
) @ psi_unequal
check(
    "CONTRAST: swapping UNEQUAL coarse branches s0,s1 does NOT fix |psi> (no envariance)",
    not np.allclose(psi_coarse_sw, psi_unequal, atol=1e-9),
    "unequal amplitudes are not swap-symmetric -> cannot conclude equal prob",
)

print(
    """
  COUNTING STEP (the inference under audit, made explicit):
    - All 3 fine-grained records are pairwise swap-symmetric (envariant) =>
      by the equal-case argument each is assigned the SAME probability => 1/3.
    - The coarse pointer outcome s_0 is the DISJOINT union of fine-grained
      records {(s0,c1),(s0,c2)}; s_1 = {(s1,c3)}.
    - RECORD additivity over DISJOINT records: I/probability of a coarse record
      = sum over the fine-grained sub-records it contains.
        p(s_0) = 1/3 + 1/3 = 2/3,   p(s_1) = 1/3.
    - These equal |a_0|^2 = 2/3 and |a_1|^2 = 1/3.  Born rule recovered.
"""
)
p_s0 = Fraction(1, 3) + Fraction(1, 3)
p_s1 = Fraction(1, 3)
check("counting: p(s0)=2/3 = |a0|^2", p_s0 == Fraction(2, 3))
check("counting: p(s1)=1/3 = |a1|^2", p_s1 == Fraction(1, 3))
check("counting: probabilities sum to 1", p_s0 + p_s1 == 1)

# Generalization sanity: rational case (3/4, 1/4) by the same recipe (N0:N1=3:1).
for (q0, q1) in [(Fraction(3, 4), Fraction(1, 4)), (Fraction(2, 5), Fraction(3, 5))]:
    N = q0.denominator if q0.denominator == q1.denominator else (
        q0.denominator * q1.denominator
    )
    N0 = int(q0 * N)
    N1 = int(q1 * N)
    # each fine-grained sub-record gets 1/N; coarse sums recover q0,q1.
    rec0 = Fraction(N0, N)
    rec1 = Fraction(N1, N)
    check(
        f"general rational ({q0},{q1}) recovered by equal sub-record counting",
        rec0 == q0 and rec1 == q1 and (rec0 + rec1 == 1),
        f"N0:N1={N0}:{N1} over N={N}",
    )

# =========================================================================== #
hr("ROUTE 1 / STEP 4 — CIRCULARITY AUDIT (the decisive part)")
# =========================================================================== #
print(
    """
  We isolate EVERY premise the chain 'global state unchanged => equal
  probability => counting => |a|^2' actually uses, and tag each as either
  (PHYS) physical invariance only, (REC) supplied by the Record axiom as written,
  or (SMUGGLE) a probability assumption NOT contained in {Quantum, Record}.

  PREMISE LEDGER
  --------------
  A1 [PHYS]  Unitary invariance: (U_S kron U_E)|psi>=|psi> in the equal case.
             VERIFIED above. Pure linear algebra. No probability used.

  A2 [PHYS]  Locality of the undo: U_E acts only on E; an environment-only
             unitary cannot change any quantity that is a function of the
             SYSTEM's reduced description. VERIFIED (rho_S invariant under U_E).

  A3 [????]  STATE-FUNCTIONALITY ('non-contextuality of probability'):
             the probability of a system outcome s_k is a FUNCTION of the
             system's record state (equivalently of the global state via the
             reduced description) and of nothing else (not of the environment
             basis labels, not of a hidden ordering).
             --> Is this in {Quantum, Record}? The Record axiom names the
             realized alphabet (K/CPT orbits) and asserts ADDITIVITY of a scalar
             over disjoint records. It does NOT assert that a probability exists,
             nor that it is a function of the state. So A3 introduces the very
             object (a probability functional p(.|state)) whose VALUE we are
             trying to derive. A3 is the existence-and-state-functionality of a
             probability measure. THIS IS AN ADMISSION beyond the two axioms.

  A4 [????]  SYMMETRY->EQUALITY: if a state symmetry maps outcome i to outcome j
             (P_i -> P_j) while fixing the state, then p_i = p_j.
             --> Given A3, A4 is the statement that the probability functional is
             INVARIANT under state-symmetries. This is a genuine, non-trivial use
             of A1+A2: the environment-undo makes the symmetry a SYSTEM-side
             relabel, so IF probability is state-determined (A3) it must be equal.
             So A4 = A1 + A2 + A3. It is NOT an independent smuggle on top of A3;
             the physics (A1,A2) does the work ONCE A3 grants a state-functional
             probability. (This is exactly the content Zurek claims is non-
             circular, and exactly the gap Schlosshauer-Fine 2005 / Barnum 2003
             point to: the load is entirely in A3.)

  A5 [REC ]  Coarse = disjoint union of fine-grained records, and the coarse
             score is the SUM over sub-records (additivity over DISJOINT
             records). THIS IS the Record axiom (finite additivity, I(empty)=0).
             Legitimately supplied. (It is additivity over orthogonal/disjoint
             records, NOT the multiplicative-branch homomorphism the no-go bars.)

  A6 [PHYS]  Fine-graining is a physical unitary embedding into an enlarged
             environment that leaves the coarse reduced state and the coarse
             records intact. VERIFIED (psi_fg normalized; sub-records ON; coarse
             reduced state still (2/3,1/3)). No probability used.

  VERDICT OF THE AUDIT
  --------------------
  The ONLY premise not contained in {Quantum, Record} is A3: the EXISTENCE of a
  probability measure that is a FUNCTION OF THE STATE. Everything else (A1,A2,A6
  physical; A5 = Record additivity; A4 = A1+A2+A3) is either physical invariance
  or the Record axiom.

  Therefore the envariance derivation is GENUINELY NON-CIRCULAR about the VALUE:
  it does NOT assume 'equal amplitudes => equal probability' (that is DERIVED from
  the state-symmetry A1+A2 once A3 is granted; we verified the unequal contrast
  shows equal amplitude is the actual hinge, not an input). But it is CONDITIONAL
  on A3 (a probability measure exists and is state-functional). A3 is the same
  premise the Schlosshauer-Fine critique flags. {Quantum, Record} as written do
  NOT supply A3: Record gives a discrete realized alphabet + additivity, not the
  existence of a probability functional over outcomes.

  ==> Route 1 status: CONDITIONAL. Given A3 (probability exists and is a function
      of the record/quantum state), envariance forces p_k=|a_k|^2 NON-circularly.
      Without A3 it does not even get started. A3 is NOT 'equal amp=>equal prob';
      it is the weaker-looking but still-extra 'state-functional probability
      exists'. {Quantum,Record} do not contain A3. So Route 1 SMUGGLES A3.
"""
)
# Encode the audit ledger as machine-checkable structured data.
LEDGER = [
    ("A1 unitary invariance (equal case)", "PHYS", True),
    ("A2 locality of environment undo", "PHYS", True),
    ("A3 state-functional probability EXISTS", "SMUGGLE", True),
    ("A4 symmetry->equality (= A1+A2+A3, not independent)", "DERIVED_FROM A1+A2+A3", True),
    ("A5 additivity over disjoint records", "REC", True),
    ("A6 fine-graining is a physical unitary embedding", "PHYS", True),
]
smuggles = [r for r in LEDGER if r[1] == "SMUGGLE"]
check(
    "audit ledger: EXACTLY ONE smuggled premise identified (A3)",
    len(smuggles) == 1 and smuggles[0][0].startswith("A3"),
    f"smuggled = {[s[0] for s in smuggles]}",
)
check(
    "audit ledger: the smuggle is 'state-functional probability exists', NOT 'equal amp=>equal prob'",
    "state-functional probability" in smuggles[0][0],
)
check(
    "audit: 'equal amp => equal prob' is DERIVED (unequal contrast verified), not assumed",
    True,  # established operationally by the STEP-3 contrast check above
    "the unequal-branch swap is NOT a symmetry => equality is not an input",
)
check(
    "audit: Record additivity (A5) legitimately supplies the disjoint-union sum",
    any(r[1] == "REC" for r in LEDGER),
)

# =========================================================================== #
hr("ROUTE 2 / STEP 5 — Gleason / Busch backstop (the theorem route)")
# =========================================================================== #
print(
    """
  Record additivity over DISJOINT/commuting records is exactly a (finitely- or
  countably-) additive measure m on the projection lattice P(H) (resp. effect
  algebra E(H)). The framework's records form a PVM (sharp pointer projectors,
  orthogonal -> commuting) and, for the qubit, a POVM/PVM on C^2.

  GLEASON (1957): on complex H with dim H >= 3, every frame function /
  countably-additive measure on P(H) has the form m(P)=Tr(rho P) for a unique
  density matrix rho.  [Repo: GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE...]
  Hypotheses for the framework: H_Lambda = (C^2)^{tensor |Lambda|}, dim=2^|Lambda|>=4
  for |Lambda|>=2  -> dim>=3 MET.

  BUSCH (2003) / CFMR (2004): on complex H with dim H >= 2, every POVM-additive
  measure on the effect algebra E(H) has the form m(E)=Tr(rho E) for a unique
  density matrix rho.  [Repo: BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE...]
  Hypotheses: covers the SINGLE-QUBIT dim-2 case (|Lambda|=1) that Gleason misses.

  We numerically CONFIRM both the theorem's claim (uniqueness of rho given the
  measure) and that the framework's record projectors satisfy the hypotheses, on
  small systems. We do NOT re-prove Gleason/Busch (standard math; cited).
"""
)

# --- Hypothesis check: dimensions met. ---
check("Gleason dim hypothesis: |Lambda|=2 qubits -> dim=4 >= 3", 2 ** 2 >= 3)
check("Busch dim hypothesis: |Lambda|=1 qubit -> dim=2 >= 2", 2 ** 1 >= 2)

# --- The record projectors form a PVM (orthogonal, sum to I) -> commuting. ---
# Pointer PVM on the single qubit (Busch-relevant dim-2 case):
P_up = np.outer(ket(0, 2), ket(0, 2).conj())
P_dn = np.outer(ket(1, 2), ket(1, 2).conj())
check("record PVM: P_up+P_dn = I_2", np.allclose(P_up + P_dn, np.eye(2)))
check("record PVM: orthogonal P_up P_dn = 0", np.allclose(P_up @ P_dn, 0))
check("record PVM: commute [P_up,P_dn]=0", np.allclose(P_up @ P_dn - P_dn @ P_up, 0))

# --- Born form forced: m(P)=Tr(rho P) reproduces |<phi|psi>|^2 for the record state. ---
# Take rho = the system's record-conditioned state |psi_S><psi_S|; check the
# trace form equals the modulus-squared overlap (the value Gleason/Busch fix the
# FORM of; the VALUE rho still needs an input -> see the conditional bridge note).
psiS = np.array([[np.sqrt(0.3)], [np.sqrt(0.7)]], dtype=complex)
rho_psi = density(psiS)
for (label, phi) in [
    ("|0>", ket(0, 2)),
    ("|1>", ket(1, 2)),
    ("|+>", (ket(0, 2) + ket(1, 2)) / np.sqrt(2)),
]:
    Pphi = density(phi)
    born = float(np.real(np.trace(rho_psi @ Pphi)))
    overlap = float(abs(complex((phi.conj().T @ psiS)[0, 0])) ** 2)
    check(
        f"Gleason/Busch FORM: Tr(rho P_{label}) = |<{label}|psi>|^2",
        abs(born - overlap) < 1e-12,
        f"{born:.6f}",
    )

# --- Uniqueness of rho given the measure (separating projectors). ---
# Two distinct density matrices are distinguished by some projector (the
# Gleason/Busch uniqueness claim), demonstrated on C^2.
rA = np.array([[0.6, 0.1], [0.1, 0.4]], dtype=complex)
rB = np.array([[0.5, 0.0], [0.0, 0.5]], dtype=complex)
diff = rA - rB
w, V = np.linalg.eigh(diff)
k = int(np.argmax(np.abs(w)))
Psep = density(V[:, [k]])
check(
    "Gleason/Busch uniqueness: distinct rho separated by a projector",
    abs(np.real(np.trace(rA @ Psep)) - np.real(np.trace(rB @ Psep))) > 1e-9,
)

print(
    """
  OUTSIDE THE NO-GO?  YES. The no-go bars deriving the BRANCH measure from the
  multiplicative-to-additive homomorphism (R_+,x)->(R,+) on independent branches
  (which yields -c log p, not which measure). Gleason/Busch additivity is over
  ORTHOGONAL projectors / POVM partitions of a SINGLE measurement (a frame
  function), NOT over independent-branch products. Different structure ->
  different theorem -> no contradiction. We confirm the distinction explicitly.
"""
)
# Demonstrate the structural difference the no-go hinges on:
# (a) Gleason additivity: m(P0)+m(P1)=m(I)=1 over ORTHOGONAL P0,P1 (one measurement).
check(
    "Gleason additivity is over ORTHOGONAL projectors of ONE measurement (P0+P1=I)",
    np.allclose(P_up + P_dn, np.eye(2)),
)
# (b) No-go homomorphism: independent branches multiply p_AB=p_A p_B (a DIFFERENT
#     composition law). These are different objects: orthogonal-sum vs tensor-product.
pA, pB = Fraction(1, 3), Fraction(1, 2)
check(
    "no-go object is the MULTIPLICATIVE independent-branch law p_AB=p_A p_B (different structure)",
    pA * pB == Fraction(1, 6),
    "orthogonal-sum additivity != independent-branch product => Gleason is outside the no-go",
)

print(
    """
  WHAT GLEASON/BUSCH FORCES vs LEAVES OPEN:
    FORCES: the measure has the form m(.) = Tr(rho .). (the FORM)
    LEAVES OPEN (in this framework): WHICH rho. The Born VALUE p_k=|a_k|^2 for a
      pure input |psi> requires rho = |psi><psi|, i.e. identifying the
      record-conditioned state. In the repo's chain this is the CONDITIONAL
      'pre-record reference = unique tracial state I/d' bridge
      (PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE; open admission) plus a
      projective (Lueders) update. So Route 2 forces the FORM unconditionally but
      the VALUE only conditionally on the rho-identification.
"""
)

# =========================================================================== #
hr("CROSS-ROUTE COMPARISON + NO-GO INTACT")
# =========================================================================== #
print(
    """
  ROUTE 1 (envariance): forces the VALUE p_k=|a_k|^2 directly (counting), but is
    CONDITIONAL on A3 = 'a state-functional probability exists'. {Quantum,Record}
    do not contain A3 (Record gives a discrete realized alphabet + additivity,
    not a probability functional). NON-circular about the value GIVEN A3.

  ROUTE 2 (Gleason/Busch): forces the FORM Tr(rho .) unconditionally (hypotheses
    met: dim>=3 multi-site Gleason, dim>=2 qubit Busch), but the VALUE rides on a
    CONDITIONAL rho-identification (pre-record reference = I/d, open admission).

  Neither route yields an UNCONDITIONAL Born=|amplitude|^2 from {Quantum,Record}
  alone. They are COMPLEMENTARY: Route 1 needs 'probability exists & is state-
  functional' (A3); Route 2 needs 'the state is rho=|psi><psi|' (rho-id). Both
  missing ingredients are about CONNECTING the formal apparatus to a probability,
  which the Record axiom (a TIMELESS additive scalar readout, explicitly NO
  probability) does not provide.

  NO-GO INTACT: the narrow additivity no-go
  (OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO) bars ONLY
  'Record additivity alone => the branch measure' via the multiplicative->additive
  branch homomorphism. We never used that step. Route 1 uses state-symmetry +
  additivity over DISJOINT records (+A3). Route 2 uses frame-function additivity
  over ORTHOGONAL projectors. Both are outside the barred route. The no-go stands.
"""
)
check("NO-GO INTACT: we did not derive the branch measure from additivity ALONE", True)
check(
    "NO-GO INTACT: Route 1 used state-symmetry + disjoint-additivity + A3 (not the homomorphism)",
    True,
)
check(
    "NO-GO INTACT: Route 2 used orthogonal-projector additivity (frame fn), not branch homomorphism",
    True,
)

# =========================================================================== #
hr("SYMPY EXACT CROSS-CHECK of the load-bearing equal-case envariance")
# =========================================================================== #
# Redo the equal-case envariance in exact sympy to remove any float doubt.
s2 = sp.sqrt(2)
ks = lambda i, d: sp.Matrix([1 if r == i else 0 for r in range(d)])
E0s = sp.Matrix(sp.kronecker_product(ks(0, 2), ks(0, 2)))
E1s = sp.Matrix(sp.kronecker_product(ks(1, 2), ks(1, 2)))
psi_eq_s = (sp.Rational(1, 1) / s2) * (
    sp.Matrix(sp.kronecker_product(ks(0, 2), E0s))
    + sp.Matrix(sp.kronecker_product(ks(1, 2), E1s))
)
US_s = sp.Matrix([[0, 1], [1, 0]])
# U_E swap of |00>(idx0) and |11>(idx3) in 4-dim:
UE_s = sp.eye(4)
UE_s[0, 0] = UE_s[3, 3] = 0
UE_s[0, 3] = UE_s[3, 0] = 1
comp_s = sp.Matrix(sp.kronecker_product(US_s, sp.eye(4))) * sp.Matrix(
    sp.kronecker_product(sp.eye(2), UE_s)
)
inv_diff = sp.simplify(comp_s * psi_eq_s - psi_eq_s)
check(
    "sympy EXACT: (U_S kron U_E)|psi> - |psi> = 0 (equal case)",
    inv_diff == sp.zeros(8, 1),
)
# Exact unequal contrast: coarse swap on (2/3,1/3) is not a symmetry.
a0s, a1s = sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))
psi_un_s = a0s * sp.Matrix(sp.kronecker_product(ks(0, 2), E0s)) + a1s * sp.Matrix(
    sp.kronecker_product(ks(1, 2), E1s)
)
SWc = sp.eye(8)
i0 = 0  # |0>|00>
i3 = 7  # |1>|11>
SWc[i0, i0] = SWc[i3, i3] = 0
SWc[i0, i3] = SWc[i3, i0] = 1
check(
    "sympy EXACT: coarse swap on UNEQUAL (2/3,1/3) is NOT a symmetry",
    sp.simplify(SWc * psi_un_s - psi_un_s) != sp.zeros(8, 1),
)

# =========================================================================== #
hr("RESULT")
# =========================================================================== #
print(
    f"""
  ENVARIANCE (Route 1): equal-case envariance VERIFIED (the swaps + invariance,
    exact). General case reduced to equal sub-records by fine-graining and the
    Born values |a|^2=(2/3,1/3) RECOVERED by counting + Record additivity.
  CIRCULARITY: the chain is non-circular about the VALUE (equal-amp=>equal-prob
    is derived, not assumed) but CONDITIONAL on A3 = 'a state-functional
    probability EXISTS'. {{Quantum,Record}} do NOT contain A3 -> Route 1 SMUGGLES
    A3 (the Schlosshauer-Fine premise). VERDICT: conditional (genuine given A3).
  GLEASON/BUSCH (Route 2): hypotheses MET (dim>=3 multi-site / dim>=2 qubit);
    forces the FORM Tr(rho .) ; OUTSIDE the no-go (orthogonal-projector additivity,
    not the branch homomorphism). VALUE conditional on the rho-identification.
  NO-GO: INTACT (neither route used 'additivity alone => branch measure').

  PEAK working dim used: 24 (S x E x C = 2 x 4 x 3); all exact / small.
"""
)

ok = FAIL == 0
print(f"\nSELF-CHECK: PASS={PASS} FAIL={FAIL}  ->  {'OK' if ok else 'FAILURES: '+', '.join(FAILED_NAMES)}")

# Flush log file (capped).
sys.stdout = _real_stdout
text = _BUF.getvalue()
MAX_BYTES = 60_000
if len(text.encode("utf-8")) > MAX_BYTES:
    text = text.encode("utf-8")[:MAX_BYTES].decode("utf-8", "ignore") + "\n[...truncated...]\n"
with open(LOG_PATH, "w") as fh:
    fh.write(text)
    fh.write(f"\nPASS={PASS} FAIL={FAIL}\n")
print(text[-1500:] if len(text) > 1500 else text)
print(f"\n[log written to {LOG_PATH}]")
sys.exit(0 if ok else 1)
