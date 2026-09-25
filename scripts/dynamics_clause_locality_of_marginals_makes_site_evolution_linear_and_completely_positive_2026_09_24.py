#!/usr/bin/env python3
"""Finite diagnostics for the conditional claims in the paired source note.

Random examples do not establish universal theorems; use the explicit proofs
and premises in that note. No native physical law or audit grade is claimed.
"""
import sys

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_LOCALITY_OF_MARGINALS_MAKES_A_SITE_S_EVOLUTION_BETWEEN_RECORDS_LINEAR_AND_COMPLETELY_POSITIVE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

import numpy as np
from scipy.linalg import expm

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
PAULI = [PX, PY, PZ]


def unit(v):
    return v / np.linalg.norm(v)


def rho_of(r):
    return 0.5 * (I2 + sum(r[k] * PAULI[k] for k in range(3)))


def bloch(rho):
    return np.real(np.array([np.trace(rho @ P) for P in PAULI]))


def rot(axis, ang):
    axis = unit(axis)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def random_chord(r):
    d = unit(rng.normal(size=3))
    b_ = r @ d
    disc = np.sqrt(b_ * b_ - (r @ r - 1))
    t1, t2 = -b_ + disc, -b_ - disc
    n1, n2 = r + t1 * d, r + t2 * d
    return n1, n2, t2 / (t2 - t1)


NAX = unit(np.array([1.0, 2.0, 2.0]))


def precess(r, g=1.5):
    """Weinberg-type: rotation about NAX by an angle proportional to r.NAX."""
    return rot(NAX, g * (r @ NAX)) @ r


def contract(r, eps=0.4):
    return r * (1 - eps * (r @ r))


def axis_shift(evolve, trials=200):
    worst = 0.0
    for _ in range(trials):
        r = unit(rng.normal(size=3)) * rng.uniform(0.1, 0.9)
        m = unit(rng.normal(size=3))
        outs = []
        for _ in range(3):
            n1, n2, p = random_chord(r)
            avg = p * evolve(n1) + (1 - p) * evolve(n2)
            outs.append(0.5 * (1 + avg @ m))
        outs.append(0.5 * (1 + evolve(r) @ m))          # no distant record
        worst = max(worst, max(outs) - min(outs))
    return worst


# ------------------------------------------------ 1. nonlinear evolutions signal
s_prec, s_con = axis_shift(precess), axis_shift(contract)
check("nonlinear evolutions signal: the site's marginal after evolution depends on whether and how a distant partner was recorded",
      s_prec > 1e-2 and s_con > 1e-2, f"largest marginal shift: state-dependent precession {s_prec:.3f}, purity-dependent contraction {s_con:.3f}")


# ------------------------------------------------ 2. linear channels do not
def random_channel():
    """Random qubit channel from a random Stinespring isometry (Kraus operators)."""
    G = rng.normal(size=(4, 2)) + 1j * rng.normal(size=(4, 2))
    Q, _ = np.linalg.qr(G)
    return [Q[2 * k:2 * k + 2, :] for k in range(2)]


def apply(kraus, rho):
    return sum(K @ rho @ K.conj().T for K in kraus)


worst = 0.0
for _ in range(50):
    kr = random_channel()
    ev = lambda r: bloch(apply(kr, rho_of(r)))
    worst = max(worst, axis_shift(ev, trials=20))
check("linear channels do not signal: random completely positive channels give the same marginal for every steering choice",
      worst < 1e-12, f"largest shift over 50 random channels {worst:.1e}")


# ------------------------------------------------ 3. chord consistency forces affinity
def chord_violation(g):
    worst_ = 0.0
    for _ in range(200):
        r = unit(rng.normal(size=3)) * rng.uniform(0.1, 0.9)
        n1, n2, p = random_chord(r)
        worst_ = max(worst_, np.linalg.norm(p * precess(n1, g) + (1 - p) * precess(n2, g) - precess(r, g)))
    return worst_


gs = [0.0, 0.05, 0.5, 1.5]
cv = [chord_violation(g) for g in gs]
check("chord consistency forces affinity: the precession passes only at zero nonlinearity, failing more as it grows",
      cv[0] < 1e-12 and all(x > 1e-4 for x in cv[1:]) and cv[1] < cv[2] < cv[3],
      "largest chord violation " + ", ".join(f"g {g}: {v:.1e}" for g, v in zip(gs, cv)))

# ------------------------------------------------ 4. complete positivity is forced
singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
rho_s = np.outer(singlet, singlet.conj())


def partial_map_on_first(rho4, fmap):
    out = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            Eij = np.zeros((2, 2), dtype=complex)
            Eij[i, j] = 1
            out += np.kron(fmap(Eij), rho4.reshape(2, 2, 2, 2)[i, :, j, :])
    return out


transposed = partial_map_on_first(rho_s, lambda A: A.T)
neg = np.linalg.eigvalsh(transposed).min()
worst_pos = 0.0
for _ in range(50):
    kr = random_channel()
    worst_pos = min(worst_pos, np.linalg.eigvalsh(partial_map_on_first(rho_s, lambda A: apply(kr, A))).min())
# The negative eigenvalue becomes a negative record probability through the clause's own operations: a
# record-supplied field rotates the site (open PR 9041), the partner is brought next to it by swaps, and a
# Heisenberg bond acts on the pair; then both form product records. (Product records straight after a
# partial transpose are never negative, and the chosen Heisenberg bond leaves |Phi+> invariant, so the rotation is
# needed.)
S2 = [PX / 2, PY / 2, PZ / 2]
SS2 = sum(np.kron(s_, s_) for s_ in S2)
most_neg = 0.0
for _ in range(300):
    ax = unit(rng.normal(size=3))
    V = expm(-1j * rng.uniform(0, np.pi) * sum(ax[k] * PAULI[k] for k in range(3)) / 2)
    U2 = expm(-1j * rng.uniform(0, 2 * np.pi) * SS2) @ np.kron(V, I2)
    Y2 = U2 @ transposed @ U2.conj().T
    for _ in range(40):
        pa = 0.5 * (I2 + sum(v * P for v, P in zip(unit(rng.normal(size=3)), PAULI)))
        pb = 0.5 * (I2 + sum(v * P for v, P in zip(unit(rng.normal(size=3)), PAULI)))
        most_neg = min(most_neg, np.real(np.trace(np.kron(pa, pb) @ Y2)))
check("transpose counterexample under supplied controls: the transpose on half a singlet, then a field rotation and a Heisenberg bond, gives a negative product-record probability; channels never go negative",
      abs(neg + 0.5) < 1e-12 and worst_pos > -1e-12 and most_neg < -0.05,
      f"transpose: smallest joint eigenvalue {neg:.3f}; most negative product-record probability after rotation and bond {most_neg:.3f}; random channels: smallest eigenvalue {worst_pos:.1e}")

# ------------------------------------------------ 5. reversibility leaves unitaries
def transfer(kraus):
    """Superoperator on vec(rho) (row-major)."""
    return sum(np.kron(K, K.conj()) for K in kraus)


def choi_min_eig(T):
    C = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            Eij = np.zeros((2, 2), dtype=complex)
            Eij[i, j] = 1
            C += np.kron(Eij, (T @ Eij.reshape(4)).reshape(2, 2))
    return np.linalg.eigvalsh((C + C.conj().T) / 2).min()


H = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
U = expm(-1j * (H + H.conj().T))
inv_unitary = choi_min_eig(np.linalg.inv(transfer([U])))
inv_generic = min(choi_min_eig(np.linalg.inv(transfer(random_channel()))) for _ in range(20))
check("reversibility leaves unitaries: a unitary channel's inverse is a channel; a sampled non-unitary channel has a non-CP inverse",
      inv_unitary > -1e-10 and inv_generic < -1e-3,
      f"smallest Choi eigenvalue of the inverse: unitary {inv_unitary:.1e}; worst of 20 random channels {inv_generic:.3f}")

# ------------------------------------------------ 6. the two-site form is imposed on the generator
PAULIS = [I2, np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]


def kron_all(mats):
    out = mats[0]
    for mm in mats[1:]:
        out = np.kron(out, mm)
    return out


def chain_H(n, kind):
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    for i in range(n - 1):
        for a in ((1, 2, 3) if kind == "Heisenberg" else (3,)):
            mats = [I2] * n
            mats[i], mats[i + 1] = PAULIS[a], PAULIS[a]
            H += kron_all(mats) / 4
    return H


nch, centre = 5, 2
strings = list(np.ndindex(*([4] * nch)))
far = [s_ for s_ in strings if any(s_[j] and abs(j - centre) > 1 for j in range(nch))]
X2 = kron_all([PAULIS[1] if j == centre else I2 for j in range(nch)])
outside = {}
for kind in ("Heisenberg", "Ising"):
    H = chain_H(nch, kind)
    row = []
    for t in (0.05, 0.2, 1.0):
        U = expm(-1j * H * t)
        O = U.conj().T @ X2 @ U
        tot = np.real(np.trace(O.conj().T @ O)) / 2 ** nch
        w = sum(abs(np.trace(kron_all([PAULIS[a] for a in s_]) @ O) / 2 ** nch) ** 2 for s_ in far)
        row.append(w / tot)
    outside[kind] = row
check("the two-site form is imposed on the generator: the clause's evolution is not a nearest-neighbour unitary at finite time",
      all(x > 1e-8 for x in outside["Heisenberg"]) and outside["Heisenberg"][0] < outside["Heisenberg"][1] < outside["Heisenberg"][2]
      and max(outside["Ising"]) < 1e-20,
      "weight of U^dag X_2 U outside radius 1 at t = 0.05, 0.2, 1: Heisenberg "
      + ", ".join(f"{x:.1e}" for x in outside["Heisenberg"]) + "; Ising " + ", ".join(f"{x:.0e}" for x in outside["Ising"]))


# Scope resolutions are provenance, not additional numerical checks.
print('N5 resolution: Supply the tensor extension and positivity requirement for CP; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Separate the transpose witness from a universal CP proof; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Prove the same-dimensional channel inverse theorem using Kraus matrices; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Require group time homogeneity for a fixed generator; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Keep generator support independent from finite-time operator support; see the explicit conditional proof and limitation in the paired note.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
