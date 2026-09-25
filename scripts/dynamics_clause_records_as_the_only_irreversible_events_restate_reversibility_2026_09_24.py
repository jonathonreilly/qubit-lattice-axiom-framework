#!/usr/bin/env python3
"""Finite diagnostics for the conditional claims in the paired source note.

Random examples do not establish universal theorems; use the explicit proofs
and premises in that note. No native physical law or audit grade is claimed.
"""
import sys

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_LOCALITY_OF_MARGINALS_MAKES_A_SITE_S_EVOLUTION_BETWEEN_RECORDS_LINEAR_AND_COMPLETELY_POSITIVE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_AS_THE_ONLY_IRREVERSIBLE_EVENTS_RESTATE_REVERSIBILITY_A_CHANNEL_THAT_KEEPS_PURE_STATES_PURE_AND_DISTINGUISHABLE_IS_UNITARY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

import numpy as np
from scipy.linalg import expm

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)


def random_channel(d, k):
    G = rng.normal(size=(d * k, d)) + 1j * rng.normal(size=(d * k, d))
    Q, _ = np.linalg.qr(G)
    return [Q[i * d:(i + 1) * d, :] for i in range(k)]


def random_unitary(d):
    H = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return expm(-1j * (H + H.conj().T))


def apply(kraus, rho):
    return sum(K @ rho @ K.conj().T for K in kraus)


def purity(rho):
    return np.real(np.trace(rho @ rho))


def random_pure(d):
    v = rng.normal(size=d) + 1j * rng.normal(size=d)
    v /= np.linalg.norm(v)
    return np.outer(v, v.conj())


def trace_dist(a, b):
    return 0.5 * np.abs(np.linalg.eigvalsh(a - b)).sum()


# ------------------------------------------------ 1. purity
worst_nonunitary, worst_unitary = 1.0, 0.0
for d in (2, 3):
    for k in (2, 3):
        for _ in range(20):
            kr = random_channel(d, k)
            worst_nonunitary = min(worst_nonunitary, min(purity(apply(kr, random_pure(d))) for _ in range(30)))
    for _ in range(20):
        U = random_unitary(d)
        worst_unitary = max(worst_unitary, max(abs(1 - purity(apply([U], random_pure(d)))) for _ in range(30)))
check("purity: aggregate random examples exhibit purity loss; sampled unitaries preserve purity",
      worst_nonunitary < 0.99 and worst_unitary < 1e-12,
      f"lowest output purity over non-unitary channels {worst_nonunitary:.3f}; unitary purity defect {worst_unitary:.1e}")

# ------------------------------------------------ 2. the replacement channel
phi = random_pure(2)
repl = lambda rho: np.trace(rho) * phi
e0, e1 = np.diag([1.0 + 0j, 0.0]), np.diag([0.0 + 0j, 1.0])
check("the replacement channel keeps purity but sends orthogonal states to the same output",
      abs(purity(repl(random_pure(2))) - 1) < 1e-12 and trace_dist(repl(e0), repl(e1)) < 1e-12 and trace_dist(e0, e1) == 1.0,
      f"output purity 1; trace distance of orthogonal inputs 1 -> {trace_dist(repl(e0), repl(e1)):.1e}")

# ------------------------------------------------ 3. the mechanism
# (a) a channel whose Kraus operators are proportional is a unitary conjugation
U = random_unitary(3)
c = rng.normal(size=3) + 1j * rng.normal(size=3)
c /= np.linalg.norm(c)
kr_prop = [ci * U for ci in c]
dev_prop = max(np.linalg.norm(apply(kr_prop, r) - U @ r @ U.conj().T) for r in [random_pure(3) for _ in range(20)])
# (b) for a generic channel, some input gives non-parallel Kraus outputs K_1 psi, K_2 psi
kr = random_channel(3, 2)
worst_par = 0.0
for _ in range(50):
    v = rng.normal(size=3) + 1j * rng.normal(size=3)
    a1, a2 = kr[0] @ v, kr[1] @ v
    par = abs(np.vdot(a1, a2)) / (np.linalg.norm(a1) * np.linalg.norm(a2))
    worst_par = max(worst_par, 1 - par)
check("mechanism: proportional Kraus operators give a unitary conjugation; a generic channel has non-parallel Kraus outputs",
      dev_prop < 1e-12 and worst_par > 1e-2, f"proportional-Kraus deviation from U rho U^dag {dev_prop:.1e}; largest non-parallelism {worst_par:.3f}")

# ------------------------------------------------ 4. distinguishability
worst_drop, worst_unit = 0.0, 0.0
for _ in range(40):
    kr = random_channel(2, 2)
    U = random_unitary(2)
    for _ in range(30):
        a, b = random_pure(2), random_pure(2)
        worst_drop = max(worst_drop, trace_dist(a, b) - trace_dist(apply(kr, a), apply(kr, b)))
        worst_unit = max(worst_unit, abs(trace_dist(a, b) - trace_dist(U @ a @ U.conj().T, U @ b @ U.conj().T)))
check("distinguishability: aggregate random examples exhibit distance loss; sampled unitaries preserve distances",
      worst_drop > 1e-2 and worst_unit < 1e-12, f"largest drop {worst_drop:.3f}; unitary change {worst_unit:.1e}")

# ------------------------------------------------ 5. the lemma: proportional, or rank at most one with a common range
def worst_nonparallel(A, B, trials=400):
    worst_ = 0.0
    for _ in range(trials):
        v = rng.normal(size=A.shape[1]) + 1j * rng.normal(size=A.shape[1])
        a1, a2 = A @ v, B @ v
        if np.linalg.norm(a1) < 1e-12 or np.linalg.norm(a2) < 1e-12:
            continue
        worst_ = max(worst_, 1 - abs(np.vdot(a1, a2)) / (np.linalg.norm(a1) * np.linalg.norm(a2)))
    return worst_


w_, u_, v_ = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)]
R1a, R1b = np.outer(w_, u_.conj()), np.outer(w_, v_.conj())
rank1_common = worst_nonparallel(R1a, R1b)
rank1_prop = np.linalg.matrix_rank(np.array([R1a.ravel(), R1b.ravel()]), tol=1e-9)
G = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
Uu, sv, Vh = np.linalg.svd(G)
R2 = Uu[:, :2] @ np.diag(sv[:2]) @ Vh[:2]
mixed = worst_nonparallel(R2, R1a, trials=4000)
check("the lemma: parallel outputs on every input mean proportional maps, or two rank-one maps with a common range",
      rank1_common < 1e-12 and rank1_prop == 2 and mixed > 0.99,
      f"rank-one pair with a common range: non-parallelism {rank1_common:.0e}, not proportional (rank {rank1_prop}); "
      f"rank-two with rank-one: non-parallelism up to {mixed:.3f}")


# Scope resolutions are provenance, not additional numerical checks.
print('N5 resolution: Prove the parallel-output linear-map lemma including its kernel; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Retain the pure replacement exception before imposing distances; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Normalize proportional Kraus matrices using trace preservation; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Keep input and output dimensions equal in the unitary classification; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Treat record-only irreversibility as a supplied mathematical requirement; see the explicit conditional proof and limitation in the paired note.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
