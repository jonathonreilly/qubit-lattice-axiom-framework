#!/usr/bin/env python3
"""A record updates the rest of the lattice by compression: collapse from locality of marginals.

Open PR 9083 derived the one-site Born law P(q | rho) = Tr(P_q rho) from
locality of marginals (D-loc) and the lock (a record q leaves its own site
in P_q). This runner shows that the same reading fixes how a record updates
every other site (supplied models, finite diagnostics, no physical reading):

1. Joint laws are product projectors: effects E_qr >= 0 for records q at
   site i and r at site j whose marginals are each site's Born law whatever
   the other site does (D-loc) satisfy E_qr = P_q (x) P_r. The ranges of
   P_q (x) I and I (x) P_r meet in one line, and E_{-q,-r} >= 0 forces the
   full weight on it.
2. Sequential consistency gives compression on the partner: from the joint
   law, the partner's state after record q, read along every axis, is
   Tr_i[(P_q (x) I) rho (P_q (x) I)] / p_q (random mixed and entangled
   pairs).
3. A reset update fails: leaving the partner's state unchanged gives joint
   probabilities p_q p_r, which differ from Tr[(P_q (x) P_r) rho] on
   entangled pairs.
4. The whole rest: for three qubits, full two-qubit tomography of the rest
   after a record on the first reproduces the Lueders compression of the
   rest.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 300

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
I2 = np.eye(2, dtype=complex)
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]])
PZ = np.diag([1.0 + 0j, -1.0])
PAULI = [I2, PX, PY, PZ]


def unit(v):
    return v / np.linalg.norm(v)


def proj(n, sign):
    return 0.5 * (I2 + sign * sum(n[k] * PAULI[k + 1] for k in range(3)))


def random_state(nq, rank):
    d = 2 ** nq
    G = rng.normal(size=(d, rank)) + 1j * rng.normal(size=(d, rank))
    rho = G @ G.conj().T
    return rho / np.trace(rho)


# ------------------------------------------------ 1. product projectors
a, b = unit(rng.normal(size=3)), unit(rng.normal(size=3))
Pa, Pb = proj(a, 1), proj(b, 1)
A1 = np.kron(Pa, I2)
B1 = np.kron(I2, Pb)
# intersection of the ranges of two projectors: eigenvalue-2 space of their sum
w = np.linalg.eigvalsh(A1 + B1)
inter = int(np.sum(np.abs(w - 2) < 1e-9))
# on that line E_{++} = c P_a (x) P_b, and E_{--} = I - A1 - B1 + E_{++} has smallest eigenvalue c - 1
mins = []
for c in (0.0, 0.5, 0.9, 1.0):
    Emm = np.eye(4) - A1 - B1 + c * np.kron(Pa, Pb)
    mins.append(np.linalg.eigvalsh(Emm).min())
check("joint laws are product projectors: the ranges of P_q (x) I and I (x) P_r meet in one line, and E_(-q,-r) >= 0 forces c = 1",
      inter == 1 and all(abs(m - (c - 1)) < 1e-12 for m, c in zip(mins, (0.0, 0.5, 0.9, 1.0))),
      f"range intersection dimension {inter}; smallest eigenvalue of E_(-q,-r) at c = 0, 0.5, 0.9, 1: {np.round(mins, 12).tolist()}")


# ------------------------------------------------ 2. compression on the partner
def lueders_partner(rho, P):
    M = np.kron(P, I2) @ rho @ np.kron(P, I2)
    red = np.einsum("ijik->jk", M.reshape(2, 2, 2, 2))
    return red / np.trace(red)


def tomography_partner(rho, P):
    """Partner state after record P, from joint probabilities along x, y, z."""
    pq = np.real(np.trace(np.kron(P, I2) @ rho))
    r = []
    for k in range(3):
        n = np.eye(3)[k]
        pp = np.real(np.trace(np.kron(P, proj(n, 1)) @ rho)) / pq
        r.append(2 * pp - 1)
    return 0.5 * (I2 + sum(r[k] * PAULI[k + 1] for k in range(3)))


worst = 0.0
for _ in range(200):
    rho = random_state(2, int(rng.integers(1, 5)))
    P = proj(unit(rng.normal(size=3)), rng.choice([1, -1]))
    worst = max(worst, np.linalg.norm(tomography_partner(rho, P) - lueders_partner(rho, P)))
check("sequential consistency gives compression on the partner: the partner's state after record q is the Lueders conditional state",
      worst < 1e-12, f"200 random pairs (ranks 1-4); largest deviation {worst:.1e}")

# ------------------------------------------------ 3. a reset update fails
singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
rs = np.outer(singlet, singlet.conj())
dev = 0.0
for _ in range(100):
    n1, n2 = unit(rng.normal(size=3)), unit(rng.normal(size=3))
    for s1, s2 in itertools.product((1, -1), repeat=2):
        joint = np.real(np.trace(np.kron(proj(n1, s1), proj(n2, s2)) @ rs))
        prod = np.real(np.trace(np.kron(proj(n1, s1), I2) @ rs)) * np.real(np.trace(np.kron(I2, proj(n2, s2)) @ rs))
        dev = max(dev, abs(joint - prod))
check("a reset update fails: leaving the partner unchanged gives p_q p_r, which differs from the product-projector joint law on a singlet",
      dev > 0.2, f"largest |Tr[(P_q (x) P_r) rho] - p_q p_r| over 100 axis pairs {dev:.3f} (bound 1/4)")


# ------------------------------------------------ 4. the whole rest
def lueders_rest(rho, P):
    M = np.kron(P, np.eye(4)) @ rho @ np.kron(P, np.eye(4))
    red = np.einsum("iajb->ab", M.reshape(2, 4, 2, 4))
    return red / np.trace(red)


def tomography_rest(rho, P):
    pq = np.real(np.trace(np.kron(P, np.eye(4)) @ rho))
    est = np.zeros((4, 4), dtype=complex)
    for k1 in range(4):
        for k2 in range(4):
            O = np.kron(PAULI[k1], PAULI[k2])
            # expectation of a Pauli product from joint record probabilities of product projectors
            val = np.real(np.trace(np.kron(P, O) @ rho)) / pq
            est += val * O / 4
    return est


worst3 = 0.0
for _ in range(100):
    rho = random_state(3, int(rng.integers(1, 9)))
    P = proj(unit(rng.normal(size=3)), rng.choice([1, -1]))
    worst3 = max(worst3, np.linalg.norm(tomography_rest(rho, P) - lueders_rest(rho, P)))
check("the whole rest: two-qubit tomography of the rest after a record reproduces its Lueders compression",
      worst3 < 1e-12, f"100 random three-qubit states; largest deviation {worst3:.1e}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
