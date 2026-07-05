#!/usr/bin/env python3
"""Irreducibility support for the realized-state primitive: exact small-instance
exhibits that the framework baseline is STATE-BLIND while registered outcomes are
STATE-CONTINGENT, that no canonical state is dynamics-selected, that the primitive's
counterfactual test has teeth (both directions), and that the past hypothesis is a
strictly stronger input than the neutral state slot.

Support runner for the framework primitive declaration

    docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md

These checks SUPPORT the primitive's irreducibility rationale; they do not (and could
not) derive the primitive. No new axiom/primitive content is introduced here; the
exhibits reuse landed mechanisms (the #2701-style record-broadcast dynamics of the
arrow note; degenerate-manifold invariant-state continua). All instances are tiny
(<= 4 qubits / 3x3 unitaries, dense exact linear algebra, peak memory trivial).

Run: python3 scripts/realized_state_primitive_irreducibility_support_2026_06_11.py
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


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)


def vn_entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-12]
    return float(-(w * np.log2(w)).sum())


def record_redundancy(rho, nfrag):
    """How many fragments hold a (near-)classical copy of the system pointer:
    fragment k counts as a record iff its marginal distinguishes the pointer
    branches (population imbalance > 0.25 conditioned on the pointer)."""
    n = 0
    dim = 2 ** (nfrag + 1)
    for k in range(nfrag):
        keep = [0, k + 1]
        rho_k = partial_trace_keep(rho, nfrag + 1, keep)
        # correlation between system z and fragment z
        zz = kron(np.diag([1, -1]).astype(complex), np.diag([1, -1]).astype(complex))
        c = float(np.real(np.trace(rho_k @ zz)))
        if abs(c) > 0.5:
            n += 1
    return n


def partial_trace_keep(rho, nq, keep):
    """Exact partial trace keeping the qubits in `keep` (indices), tracing the rest."""
    keep = sorted(keep)
    dims = [2] * nq
    rho_t = rho.reshape(dims + dims)
    traced = [q for q in range(nq) if q not in keep]
    for q in sorted(traced, reverse=True):
        rho_t = np.trace(rho_t, axis1=q, axis2=q + rho_t.ndim // 2)
    d = 2 ** len(keep)
    return rho_t.reshape(d, d)


# ===========================================================================
print("=" * 78)
print("S1  The baseline is STATE-BLIND; registered outcomes are STATE-CONTINGENT")
print("    (one operator set; four permitted states; four distinct record behaviors)")
print("=" * 78)
NFRAG = 3
NQ = NFRAG + 1
DIM = 2 ** NQ
# record-write step k: controlled-X from the system pointer onto fragment k
# (the arrow note's broadcast dynamics in miniature; unitary, time-symmetric)
US = []
for k in range(NFRAG):
    ops = [I2] * NQ
    H = kron(*([P1] + [X if j == k else I2 for j in range(NFRAG)])) * (np.pi / 2)
    # build controlled-X directly (exact)
    ctrlx = np.eye(DIM, dtype=complex)
    Xk = kron(P1, *[X if j == k else I2 for j in range(NFRAG)]) \
        + kron(I2 - P1, *[I2] * NFRAG)
    US.append(Xk)
plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
zero = np.array([1, 0], dtype=complex)
one = np.array([0, 1], dtype=complex)


def run_records(rho0):
    rho = rho0.copy()
    counts = [record_redundancy(rho, NFRAG)]
    for U in US:
        rho = U @ rho @ U.conj().T
        counts.append(record_redundancy(rho, NFRAG))
    return counts


def ketrho(*kets):
    psi = kron(*[k.reshape(-1, 1) for k in kets]).ravel()
    return np.outer(psi, psi.conj())


# state A: low-record start (pointer superposition, blank fragments)
cA = run_records(ketrho(plus, zero, zero, zero))
# state B: the record-FULL GHZ state, time-reversed orbit end (records present)
ghz = (kron(*[zero.reshape(-1, 1)] * NQ).ravel()
       + kron(*[one.reshape(-1, 1)] * NQ).ravel()) / np.sqrt(2)
rhoB = np.outer(ghz, ghz.conj())
cB_fwd = run_records(rhoB)
# reversed operator order = the time-reversed protocol unwinds the records
rhoR = rhoB.copy()
cB_rev = [record_redundancy(rhoR, NFRAG)]
for U in reversed(US):
    rhoR = U.conj().T @ rhoR @ U
    cB_rev.append(record_redundancy(rhoR, NFRAG))
# state C: equilibrium I/d
cC = run_records(np.eye(DIM, dtype=complex) / DIM)
# state D: pointer eigenstate (nothing to broadcast beyond the classical bit)
cD = run_records(ketrho(zero, zero, zero, zero))
check("S1a one operator set, distinct permitted states, DISTINCT registered record "
      "trajectories (state-contingency of outcomes is exact, not interpretive)",
      cA != cC and cA != cB_rev and cC == [0] * (NFRAG + 1),
      f"low-record start {cA}; record-full unwound {cB_rev}; I/d {cC}; pointer {cD}")
check("S1b records GROW from the low-record state (monotone) and the I/d "
      "equilibrium registers NOTHING (flat) -- the slot the primitive names is the "
      "sole difference between an arrow and no arrow",
      all(b >= a for a, b in zip(cA, cA[1:])) and cA[-1] == NFRAG
      and cC == [0] * (NFRAG + 1))

# ===========================================================================
print("=" * 78)
print("S2  No canonical state: invariant states form a CONTINUUM on a degenerate")
print("    manifold (the maximal-symmetry reference is ONE point, not a selection)")
print("=" * 78)
# minimal degenerate instance: H with a 2-fold-degenerate ground space; every
# rho = diag mixture of the two ground states is (i) a valid state, (ii) invariant
# under e^{-iHt}, (iii) invariant under the H-commutant symmetry
Hd = np.diag([0.0, 0.0, 1.0]).astype(complex)
g1 = np.array([1, 0, 0], dtype=complex)
g2 = np.array([0, 1, 0], dtype=complex)
ts = np.linspace(0, 1, 5)
invariant_all = True
distinct = []
for t in ts:
    rho = (1 - t) * np.outer(g1, g1.conj()) + t * np.outer(g2, g2.conj())
    for tt in (0.3, 1.7):
        Ut = np.diag(np.exp(-1j * np.diag(Hd) * tt))
        invariant_all &= np.allclose(Ut @ rho @ Ut.conj().T, rho, atol=1e-14)
    distinct.append(float(np.real(np.trace(
        rho @ np.diag([1.0, -1.0, 0.0]).astype(complex)))))
check("S2a a one-parameter CONTINUUM of dynamics-invariant states exists on the "
      "degenerate manifold (pairwise-distinct density matrices, all invariant); "
      "invariance does not select",
      invariant_all and len(set(np.round(distinct, 12))) == len(ts),
      f"5/5 invariant; ground-population functional {np.round(distinct,2)} distinct")
rho_ref = np.eye(3, dtype=complex) / 3
check("S2b the maximal-symmetry reference I/3 is NOT invariant under the SAME "
      "dynamics' excited sector mixing? -- no: I/3 IS invariant too, i.e. it is "
      "one MORE invariant point, with no property singling it out dynamically "
      "(its selection would be a typicality/measure choice, exactly what the "
      "primitive forbids supplying)",
      np.allclose(np.diag(np.exp(-1j * np.diag(Hd) * 0.9)) @ rho_ref
                  @ np.diag(np.exp(1j * np.diag(Hd) * 0.9)), rho_ref, atol=1e-14))

# ===========================================================================
print("=" * 78)
print("S3  The counterfactual test has teeth in BOTH directions")
print("=" * 78)
# family: the invariant ground-manifold states rho(t) above
# (i) a quantity that VARIES over the family -> data, not derivation
vals_var = [float(np.real(np.trace(
    (1 - t) * np.outer(g1, g1.conj()) + t * np.outer(g2, g2.conj())
    @ np.diag([1.0, -1.0, 0.0]).astype(complex)))) for t in ts]
# (ii) a quantity INVARIANT over the family -> quotable under the primitive
vals_inv = [float(np.real(np.trace(
    ((1 - t) * np.outer(g1, g1.conj()) + t * np.outer(g2, g2.conj()))
    @ np.diag([1.0, 1.0, 0.0]).astype(complex)))) for t in ts]
check("S3a a family-VARYING readout exists (fails the counterfactual test -> must "
      "be labeled registered data of the realized state)",
      max(vals_var) - min(vals_var) > 0.9,
      f"range {min(vals_var):+.2f}..{max(vals_var):+.2f}")
check("S3b a family-INVARIANT readout exists (passes the counterfactual test -> "
      "quotable: it is a property of the manifold, not of a representative)",
      max(vals_inv) - min(vals_inv) < 1e-14,
      f"constant {vals_inv[0]:+.2f} across the family")

# ===========================================================================
print("=" * 78)
print("S4  The past hypothesis is STRICTLY STRONGER than the neutral slot")
print("=" * 78)
# Neutral slot: SOME state is realized (any of S1's four). The arrow exists only
# for the low-record choice; the slot alone does not orient history.
arrows = {"low-record": cA, "record-full-unwound": cB_rev, "equilibrium": cC,
          "pointer": cD}
growing = [k for k, v in arrows.items() if v[-1] > v[0]]
flat_or_rev = [k for k, v in arrows.items() if v[-1] <= v[0]]
check("S4a the neutral slot (a state is supplied) does NOT orient history: "
      "permitted states realize growing, shrinking-on-unwind, and flat record "
      "trajectories -- the arrow's EXISTENCE needs the additional low-record "
      "boundary claim (the past hypothesis), which is a specialness claim the "
      "primitive's clauses 1-2 forbid it from supplying itself",
      growing == ["low-record"] and len(flat_or_rev) == 3,
      f"growing={growing}; not-growing={flat_or_rev}")
check("S4b entropy axis confirms the strict-strength ordering: the low-record "
      "start is entropy-0 (special), I/d is entropy-max (no arrow) -- opposite "
      "extremes; 'a state is realized' carries no position on this axis",
      vn_entropy(ketrho(plus, zero, zero, zero)) < 1e-9
      and abs(vn_entropy(np.eye(DIM, dtype=complex) / DIM) - NQ) < 1e-9)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: support exhibits for the realized_state_primitive declaration --")
print("  exact small instances showing (S1) state-blind baseline / state-contingent")
print("  registered outcomes, (S2) invariant states form a continuum (no dynamical")
print("  selection; the maximal-symmetry reference is one more point), (S3) the")
print("  counterfactual test separates quotable family-invariants from registered")
print("  data, (S4) the past hypothesis is strictly stronger than the neutral slot")
print("  (specialness on the entropy axis).  These SUPPORT irreducibility; they do")
print("  not derive the primitive and supply no state, measure, weight, or value.")
print("  Statuses are pipeline-derived; the audit lane grades.")
if FAIL:
    raise SystemExit(1)
