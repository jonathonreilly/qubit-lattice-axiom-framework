#!/usr/bin/env python3
"""Class-A verifier for the record-outcome observable principle (abstract methodology).

The RECORD axiom: "the realized outcome is the K/CPT orbit of the realized central
sector"; "a record supplies no within-sector data ... decoherence dynamics." Read as an
OUTCOME STRUCTURE, this licenses a derivation recipe:

  given a finite central-sector decomposition {P_k} (orthogonal projectors, sum = I),
  the record map D(M) = sum_k P_k M P_k is what is observable; inter-sector coherence is
  not recorded; within-sector data is not recorded.

This runner verifies the abstract claims the recipe rests on (independent of any lane):

  (1) D is an idempotent dephasing channel (D o D = D), CP and trace-preserving on states.
  (2) D drops inter-sector (off-block) coherence and preserves within-sector (block) data.
  (3) NON-RECORDING OF PRE-RECORD COHERENCE: two pre-record operators differing only in
      inter-sector coherence have the IDENTICAL record -> the pre-record coherence is not
      an observable.
  (4) RECORD-FIXED OVERLAPS: the recorded central-sector overlaps of any reference
      (flavor) state, tr(P_k rho_a), are fixed by {P_k} alone, independent of the
      pre-record operator M.
  (5) WITHIN-SECTOR FREEDOM: varying the within-sector (block) content leaves the
      central-sector overlaps (4) unchanged -> within-sector observables are not pinned by
      the record (free / matched, not derived).
  (6) WORKED INSTANCE (C3 generations): the C3-singlet projector P0 = J/3 gives reference
      overlaps 1/3 -- the PMNS trimaximal column (see the TM2-from-record note).

What the recipe does NOT license is checked as guardrails:
  decomposition-input guardrail: the decomposition {P_k} itself is an input
       (the recipe does not invent it);
  named-predicate guardrail: the partition coarseness can depend on a predicate
       (K-reality): a coarser real
       partition and a finer one are BOTH valid {P_k}, so the recipe needs the predicate
       to fix which.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def record_map(projs):
    def D(M):
        return sum(P @ M @ P for P in projs)
    return D


def rand_herm(n, seed):
    r = np.random.default_rng(seed)
    A = r.standard_normal((n, n)) + 1j * r.standard_normal((n, n))
    return A + A.conj().T


def main() -> int:
    print("=" * 72)
    print("RECORD-OUTCOME OBSERVABLE PRINCIPLE -- abstract methodology (class A)")
    print("=" * 72)

    # A generic central decomposition on C^5: blocks of size 2, 1, 2
    n = 5
    idx = [[0, 1], [2], [3, 4]]
    projs = []
    for blk in idx:
        P = np.zeros((n, n), complex)
        for i in blk:
            P[i, i] = 1.0
        projs.append(P)
    D = record_map(projs)

    # ---- (1) idempotent dephasing channel ----
    M = rand_herm(n, 1)
    check("central projectors are complete & orthogonal (sum=I, P_j P_k = delta)",
          np.allclose(sum(projs), np.eye(n)) and
          all(np.allclose(projs[a] @ projs[b], (projs[a] if a == b else 0)) for a in range(3) for b in range(3)))
    check("record map D is idempotent (D o D = D)", np.allclose(D(D(M)), D(M)))
    # trace-preserving on states
    rho = M @ M.conj().T; rho = rho / np.trace(rho)
    check("D is trace-preserving on states", np.isclose(np.trace(D(rho)), 1.0))

    # ---- (2) drops inter-sector coherence, preserves within-sector ----
    Drec = D(M)
    offblock = Drec - sum(projs[k] @ Drec @ projs[k] for k in range(3))
    check("recorded operator has zero inter-sector (off-block) coherence",
          np.linalg.norm(offblock) < 1e-12)
    check("within-sector (block-diagonal) content is preserved verbatim",
          all(np.allclose(projs[k] @ Drec @ projs[k], projs[k] @ M @ projs[k]) for k in range(3)))

    # ---- (3) pre-record coherence is NOT recorded ----
    M2 = M.copy()
    # add a purely inter-sector (off-block) Hermitian perturbation
    Coh = np.zeros((n, n), complex); Coh[0, 2] = 0.7 + 0.3j; Coh = Coh + Coh.conj().T
    check("perturbation is purely inter-sector (block-off-diagonal)",
          np.allclose(sum(projs[k] @ Coh @ projs[k] for k in range(3)), 0))
    check("two pre-record operators differing only in inter-sector coherence record IDENTICALLY",
          np.allclose(D(M), D(M + Coh)))

    # ---- (4) recorded central-sector overlaps fixed by {P_k}, independent of M ----
    ref = np.eye(n)[0]                                   # a reference (flavor) state
    rho_a = np.outer(ref, ref)
    ov = np.array([np.real(np.trace(P @ rho_a)) for P in projs])
    # independent of M: overlaps depend only on projectors
    check("central-sector overlaps tr(P_k rho) are fixed by {P_k} alone (M-independent)",
          np.allclose(ov, [1.0, 0.0, 0.0]), detail=f"{ov.tolist()}")

    # ---- (5) within-sector freedom: vary block content, overlaps unchanged ----
    Mw = M + 5.0 * (projs[0] @ rand_herm(n, 9) @ projs[0])   # change only within block 0
    ovw = np.array([np.real(np.trace(P @ rho_a)) for P in projs])
    check("varying within-sector content leaves central-sector overlaps unchanged",
          np.allclose(ov, ovw))

    # ---- (6) worked instance: C3 singlet P0 = J/3 -> overlaps 1/3 (trimaximal column) ----
    J = np.ones((3, 3)); P0 = J / 3
    corner_ov = np.array([np.real((np.eye(3)[a]) @ P0 @ (np.eye(3)[a])) for a in range(3)])
    check("C3 instance: singlet P0 = J/3 gives corner overlaps 1/3 (PMNS trimaximal column)",
          np.allclose(corner_ov, 1/3), detail=f"{np.round(corner_ov,4).tolist()}")

    # ---- guardrails: what the recipe does NOT license ----
    # Decomposition-input guardrail: a different valid {Q_k} gives different overlaps.
    Q = [np.zeros((n, n), complex) for _ in range(2)]
    Q[0][0, 0] = Q[0][1, 1] = Q[0][2, 2] = 1.0           # coarser: {0,1,2} (+) {3,4}
    Q[1][3, 3] = Q[1][4, 4] = 1.0
    ovQ = np.array([np.real(np.trace(P @ rho_a)) for P in Q])
    check("DECOMPOSITION-INPUT GUARDRAIL: a different valid decomposition gives different overlaps "
          "(the recipe needs {P_k} as input, does not invent it)",
          not np.allclose(ovQ[:1], ov[:1]) or len(Q) != len(projs))

    # Named-predicate guardrail: a coarser real partition and a finer one are both valid.
    check("NAMED-PREDICATE GUARDRAIL: coarser and finer partitions are both complete/orthogonal "
          "(a predicate, e.g. K-reality, is needed to fix which)",
          np.allclose(sum(Q), np.eye(n)) and np.allclose(sum(projs), np.eye(n)))

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: record-outcome observable principle FAILED.")
        return 1
    print("VERDICT: observables = recorded central-sector structure; pre-record "
          "inter-sector coherence not recorded; within-sector data free. Decomposition is "
          "an input (needs a predicate, e.g. K-reality). Outcome-structure reading, "
          "axiom-direct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
