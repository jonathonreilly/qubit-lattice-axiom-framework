#!/usr/bin/env python3
"""Records as the only irreversible events restate reversibility: a channel that keeps pure states pure and distinguishable is unitary.

Open PR 9084 left reversibility between records supplied (D-rev). A reading
in record language is that records are the only irreversible events
(D-onlyrec): between records no pure state becomes mixed and no two pure
states become less distinguishable. For a channel on a finite system this
is Wigner's condition, so D-onlyrec restates reversibility rather than
deriving it; what the theorem adds is the unitary form. The whole finite
region's evolution between records is taken to be a channel (a premise:
open PR 9084 treats one site with a decoupled partner). The runner
certifies (supplied readings, finite diagnostics, no physical reading):

1. Purity: random non-unitary channels (2 and 3 Kraus operators, qubit and
   qutrit) send some pure state to a mixed one; unitary channels never do.
2. The replacement channel (every state to one pure state) keeps purity but
   sends orthogonal states to the same output, erasing distinguishability.
3. The mechanism: a channel built from proportional Kraus operators is a
   unitary conjugation; a generic channel has non-parallel Kraus outputs.
4. Distinguishability: random non-unitary channels strictly lower the trace
   distance of some pair of pure states; unitaries keep every pair's.
5. The lemma behind 3: two linear maps with parallel outputs on every input
   are proportional, or both have rank at most one with a common range.
   Two rank-one maps with a common range are parallel but not
   proportional; a rank-two and a rank-one map have fully non-parallel
   outputs on some input.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 300

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
check("purity: random non-unitary channels send some pure state to a mixed one; unitary channels never do",
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
check("distinguishability: random non-unitary channels lower the trace distance of some pure pair; unitaries keep every pair's",
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

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
