#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The K/CPT-orbit clause is equivalent to a K-invariant registered surface
========================================================================
Companion runner for
docs/KCPT_ORBIT_CLAUSE_KINVARIANT_SURFACE_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-10.md.

CONTEXT.  The Record axiom (MINIMAL_AXIOMS_2026-06-05) states: given a
readout context with a finite central-sector decomposition and a fixed K/CPT
conjugation, the realized outcome is the K/CPT ORBIT of the realized central
sector.  As part of the owner-directed axiom scrub, this runner checks the
exact equivalence that locates that clause's content: the orbit quotient is
INTERCHANGEABLE with a statement about the registered scalar surface.

SETTING (finite-dimensional, exact).  A context is a finite central-sector
decomposition {P_k, k in S} (orthogonal, sum = I) plus an antiunitary K with
K P_k K^{-1} = P_{pi(k)} for an involution pi on the label set S (K^2 = +1 or
-1; both occur below).  A registered scalar assignment is a map iota: S -> R
(per-sector registered value, extended additively over disjoint records).
Outcomes-by-registration are the indistinguishability classes:
k ~ k'  iff  iota(k) = iota(k') for every admissible iota.

THE THEOREM.
  (T1, forward)   If the admissible surface is pi-INVARIANT (iota o pi =
                  iota) and ORBIT-SEPARATING (some admissible iota separates
                  every orbit pair), then the indistinguishability classes
                  are EXACTLY the K/CPT orbits: the orbit clause's outcome
                  structure is reproduced as a theorem.
  (T2, converse)  If some admissible iota separates two sectors in one
                  orbit, the orbit is NOT an indistinguishability class:
                  "outcome = orbit" is inconsistent with
                  individuation-by-registration.  Hence the orbit clause is
                  EQUIVALENT to the K-invariance of the registered surface
                  (given separation and individuation-by-registration).
  (T3, overlaps)  For sector-overlap readouts iota_rho(k) = tr(P_k rho):
                  the transport identity tr(P_{pi(k)} rho) = tr(P_k rho_K)
                  holds exactly (rho_K = the K-image state), so
                  pi-symmetry of overlaps  <=>  the sector-resolved
                  K-reality defect tr(P_k (rho - rho_K)) vanishes for all k.
                  K-real states give pi-symmetric overlaps; the generic
                  (non-K-real) state separates an orbit pair; the
                  symmetrization (rho + rho_K)/2 is K-real for BOTH K^2 = +1
                  and K^2 = -1.

WHAT T3 EXPOSES (not discharges).  Overlap-readout compatibility with the
orbit clause IS sector-resolved K-reality of the realized state.  The
standing K-reality predicate (guardrail G2's named coarseness predicate)
and the axiom's orbit clause are two faces of one structure; whether the
realized state is K-real remains the standing pin, untouched here.

EVERY CLAIM GETS A HOSTILE WITNESS:
  drop pi-invariance  -> Part C: the indicator of a single orbit-mate splits
                         the orbit (T2's witness);
  drop separation     -> Part B: the constant readout (pi-invariant) merges
                         distinct orbits -- classes strictly coarser;
  drop K-reality      -> Part D: a generic state's overlap readout separates
                         an orbit pair (defect != 0);
  degenerate pi = id  -> Part E: orbits are singletons, every readout is
                         pi-invariant, the equivalence degenerates gracefully.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  NO AXIOM IS
CHANGED: this note supplies the equivalence on which a future owner-approved,
separately reviewed slimming of the Record axiom's wording could rest; the decision
is explicitly not taken here.  The K-reality of realized states is not
derived.  Weights/measures are untouched (the orbit clause stays
weight-blind, per the partition-not-weight note).  No new axiom, no
new primitive, no Tier-A admission.

Run: python3 scripts/kcpt_orbit_clause_kinvariant_surface_equivalence_2026_06_10.py
"""
from __future__ import annotations

import itertools
import sys

import numpy as np

PASS, FAIL = 0, 0
TOL = 1e-12
RNG = np.random.default_rng(20260610)


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def classes_from_surface(S, surface):
    """Indistinguishability classes of the label set under a list of readouts."""
    sig = {k: tuple(round(f[k], 12) for f in surface) for k in S}
    classes = {}
    for k in S:
        classes.setdefault(sig[k], []).append(k)
    return sorted(sorted(c) for c in classes.values())


def orbits_of(S, pi):
    seen, out = set(), []
    for k in S:
        if k not in seen:
            orb = sorted({k, pi[k]})
            out.append(orb)
            seen.update(orb)
    return sorted(out)


# ----------------------------------------------------------------------------
print("PART A -- context validity: blocks, involution, both K-squares")
print("=" * 78)
n, d = 4, 2
N = n * d
P = []
for k in range(n):
    Pk = np.zeros((N, N))
    Pk[k * d:(k + 1) * d, k * d:(k + 1) * d] = np.eye(d)
    P.append(Pk)
pi = [1, 0, 2, 3]  # orbit {0,1}, fixed 2, fixed 3
# K^2 = +1 representative: plain block swap
Up = np.zeros((N, N))
Up[0:d, d:2 * d] = np.eye(d)
Up[d:2 * d, 0:d] = np.eye(d)
Up[2 * d:, 2 * d:] = np.eye(2 * d)
# K^2 = -1 representative: block swap twisted by J = [[0,1],[-1,0]]
J = np.array([[0.0, 1.0], [-1.0, 0.0]])
Um = np.zeros((N, N))
Um[0:d, d:2 * d] = J
Um[d:2 * d, 0:d] = J
Um[2 * d:3 * d, 2 * d:3 * d] = J
Um[3 * d:, 3 * d:] = J
check("A1 completeness and orthogonality of the sector decomposition",
      np.allclose(sum(P), np.eye(N), atol=TOL)
      and all(np.allclose(P[a] @ P[b], (P[a] if a == b else 0 * P[a]), atol=TOL)
              for a in range(n) for b in range(n)))
check("A2 K-compatibility: U conj(P_k) U^dag = P_{pi(k)} for both representatives",
      all(np.allclose(U @ np.conj(P[k]) @ U.conj().T, P[pi[k]], atol=TOL)
          for U in (Up, Um) for k in range(n)))
check("A3 K^2 = +1 and K^2 = -1 realized (U conj(U) = +I / -I)",
      np.allclose(Up @ np.conj(Up), np.eye(N), atol=TOL)
      and np.allclose(Um @ np.conj(Um), -np.eye(N), atol=TOL))
check("A4 pi is an involution", all(pi[pi[k]] == k for k in range(n)))

S = list(range(n))
ORB = orbits_of(S, pi)

# ----------------------------------------------------------------------------
print("\nPART B -- T1 forward: pi-invariant + orbit-separating surface => classes = orbits")
print("=" * 78)
# admissible surface: all pi-invariant readouts; a separating basis is the orbit indicators
orbit_indicators = [{k: float(k in orb) for k in S} for orb in ORB]
classes = classes_from_surface(S, orbit_indicators)
check("B1 with the full pi-invariant surface, indistinguishability classes = K/CPT orbits EXACTLY",
      classes == ORB, f"classes = {classes}, orbits = {ORB}")
# random pi-invariant readouts only (no indicators): generically separating
rand_inv = []
for _ in range(3):
    base = {orb_i: RNG.normal() for orb_i in range(len(ORB))}
    f = {}
    for oi, orb in enumerate(ORB):
        for k in orb:
            f[k] = base[oi]
    rand_inv.append(f)
check("B2 three random pi-invariant readouts already reproduce the orbit classes (generic separation)",
      classes_from_surface(S, rand_inv) == ORB)
# hostile: drop separation -- constant readout merges everything
const = [{k: 1.0 for k in S}]
check("B3 hostile witness: the constant (pi-invariant, non-separating) surface gives classes COARSER than orbits",
      classes_from_surface(S, const) != ORB and len(classes_from_surface(S, const)) == 1,
      "the separation condition is load-bearing")

# ----------------------------------------------------------------------------
print("\nPART C -- T2 converse: a separating readout inside an orbit breaks the clause")
print("=" * 78)
ind0 = [{k: float(k == 0) for k in S}]  # indicator of sector 0: NOT pi-invariant (pi(0)=1)
cls_with_bad = classes_from_surface(S, orbit_indicators + ind0)
check("C1 the sector-0 indicator is not pi-invariant and splits the orbit {0,1}",
      [0] in cls_with_bad and [1] in cls_with_bad,
      f"classes = {cls_with_bad}: 'outcome = orbit' fails on this surface")
check("C2 equivalence: orbit clause holds on a surface IFF the surface is pi-invariant (checked both ways on these instances)",
      (classes == ORB) and (cls_with_bad != ORB))

# ----------------------------------------------------------------------------
print("\nPART D -- T3: overlap readouts, the transport identity, and sector-resolved K-reality")
print("=" * 78)
for tag, U in (("K^2=+1", Up), ("K^2=-1", Um)):
    ok_transport, ok_defect, ok_real, ok_sym = True, True, True, True
    for _ in range(12):
        A = RNG.normal(size=(N, N)) + 1j * RNG.normal(size=(N, N))
        rho = A @ A.conj().T
        rho /= np.trace(rho).real
        rhoK = U @ np.conj(rho) @ U.conj().T
        # transport identity
        ok_transport &= all(
            abs(np.trace(P[pi[k]] @ rho).real - np.trace(P[k] @ rhoK).real) < 1e-10
            for k in range(n))
        # defect form: pi-symmetry of overlaps <=> per-sector defect vanishes
        asym = [np.trace(P[k] @ rho).real - np.trace(P[pi[k]] @ rho).real for k in range(n)]
        defect = [np.trace(P[k] @ (rho - rhoK)).real for k in range(n)]
        ok_defect &= all(abs(a - b) < 1e-10 for a, b in zip(asym, defect))
        # symmetrization is K-real for both K-squares; K-real => pi-symmetric overlaps
        rho_r = (rho + rhoK) / 2
        rho_rK = U @ np.conj(rho_r) @ U.conj().T
        ok_real &= np.allclose(rho_rK, rho_r, atol=1e-10)
        ok_sym &= all(abs(np.trace(P[pi[k]] @ rho_r).real - np.trace(P[k] @ rho_r).real) < 1e-10
                      for k in range(n))
    check(f"D1[{tag}] transport identity tr(P_pi(k) rho) = tr(P_k rho_K) on 12 random states",
          ok_transport)
    check(f"D2[{tag}] pi-symmetry of overlaps <=> sector-resolved K-reality defect vanishes",
          ok_defect, "orbit-clause compatibility of overlap readouts IS K-reality at sector resolution")
    check(f"D3[{tag}] the symmetrized state is exactly K-real, and K-real => pi-symmetric overlaps",
          ok_real and ok_sym)
# hostile: the generic state separates the orbit
A = RNG.normal(size=(N, N)) + 1j * RNG.normal(size=(N, N))
rho_g = A @ A.conj().T
rho_g /= np.trace(rho_g).real
sep = abs(np.trace(P[0] @ rho_g).real - np.trace(P[1] @ rho_g).real)
check("D4 hostile witness: a generic (non-K-real) state's overlap readout separates the orbit {0,1}",
      sep > 1e-3, f"|tr(P_0 rho) - tr(P_1 rho)| = {sep:.4f} != 0")

# ----------------------------------------------------------------------------
print("\nPART E -- degenerate boundary: pi = id")
print("=" * 78)
pi_id = [0, 1, 2, 3]
ORB_id = orbits_of(S, pi_id)
sector_indicators = [{k: float(k == j) for k in S} for j in S]
check("E1 pi = id: orbits are singletons and every readout is pi-invariant; classes = sectors",
      ORB_id == [[0], [1], [2], [3]]
      and classes_from_surface(S, sector_indicators) == ORB_id,
      "the equivalence degenerates gracefully; the clause is vacuous exactly when K fixes every sector")

# ----------------------------------------------------------------------------
print("\nPART F -- the substitution check on random contexts")
print("=" * 78)
ok_sub = True
trials = 0
for _ in range(25):
    nn = int(RNG.integers(2, 7))
    Ss = list(range(nn))
    # random involution
    perm = list(Ss)
    RNG.shuffle(perm)
    pi_r = list(range(nn))
    used = set()
    for a, b in zip(perm[0::2], perm[1::2]):
        pi_r[a], pi_r[b] = b, a
    orbs = orbits_of(Ss, pi_r)
    inds = [{k: float(k in orb) for k in Ss} for orb in orbs]
    ok_sub &= classes_from_surface(Ss, inds) == orbs
    trials += 1
check(f"F1 substitution reproduces 'outcome = orbit' on {trials} random label sets and involutions",
      ok_sub, "orbit clause <-> {individuation-by-registration + pi-invariant separating surface}")

# ----------------------------------------------------------------------------
print("\nPART G -- scope honesty: what is NOT proved here")
print("=" * 78)
check("G1 K-reality of REALIZED states is not derived: the generic state has nonzero defect (D4)",
      sep > 1e-3, "the standing K-reality pin (guardrail G2) is exposed at sector resolution, not discharged")
check("G2 weight-blindness is untouched: orbit indicators carry no inter-sector weight (all values in {0,1})",
      all(set(f.values()) <= {0.0, 1.0} for f in orbit_indicators),
      "complementary to the partition-not-weight result; no measure content enters")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
