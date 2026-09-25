#!/usr/bin/env python3
"""Finite diagnostics for the conditional claims in the paired source note.

Random examples do not establish universal theorems; use the explicit proofs
and premises in that note. No native physical law or audit grade is claimed.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_THE_COMPRESSION_UPDATE_IS_THE_ONE_DISTANT_UPDATE_CONSISTENT_WITH_LOCALITY_OF_MARGINALS_AND_AFFINE_JOINT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

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
inter_dims = []
for sa, sb in itertools.product((1, -1), repeat=2):
    # E_qr <= P_q (x) I and E_qr <= I (x) P_r: support in the intersection of the two ranges
    w = np.linalg.eigvalsh(np.kron(proj(a, sa), I2) + np.kron(I2, proj(b, sb)))
    inter_dims.append(int(np.sum(np.abs(w - 2) < 1e-9)))
# with E_qr = c_qr P_q (x) P_r, the four marginal conditions are linear in c; solve them
signs = list(itertools.product((1, -1), repeat=2))
cols = [np.kron(proj(a, sa), proj(b, sb)).ravel() for sa, sb in signs]
rows_A, rhs = [], []
for sa in (1, -1):
    rows_A.append([cols[k] if signs[k][0] == sa else 0 * cols[k] for k in range(4)])
    rhs.append(np.kron(proj(a, sa), I2).ravel())
for sb in (1, -1):
    rows_A.append([cols[k] if signs[k][1] == sb else 0 * cols[k] for k in range(4)])
    rhs.append(np.kron(I2, proj(b, sb)).ravel())
Amat = np.vstack([np.array(r).T for r in rows_A])
bvec = np.concatenate(rhs)
csol, _, rank_c, _ = np.linalg.lstsq(Amat, bvec, rcond=None)
resid_c = np.linalg.norm(Amat @ csol - bvec)
check("joint laws are product projectors: each E_qr lies on the line where the ranges of P_q (x) I and I (x) P_r meet, and the marginals fix c = 1",
      inter_dims == [1, 1, 1, 1] and rank_c == 4 and resid_c < 1e-12 and np.allclose(csol, 1, atol=1e-12),
      f"range intersection dimensions {inter_dims}; marginal system rank {rank_c}, residual {resid_c:.0e}, unique solution c = {np.round(np.real(csol), 12).tolist()}")


# ------------------------------------------------ 2. compression on the partner
def lueders_partner(rho, P):
    M = np.kron(P, I2) @ rho @ np.kron(P, I2)
    red = np.einsum("ijik->jk", M.reshape(2, 2, 2, 2))
    p = float(np.trace(red).real)
    if p <= 0:
        raise ValueError("undefined conditional state for zero-probability outcome")
    return red / p


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
formula_dev, par_gap = 0.0, 0.0
for trial in range(101):
    n1 = unit(rng.normal(size=3))
    n2 = n1 if trial == 100 else unit(rng.normal(size=3))
    for s1, s2 in itertools.product((1, -1), repeat=2):
        joint = np.real(np.trace(np.kron(proj(n1, s1), proj(n2, s2)) @ rs))
        prod = np.real(np.trace(np.kron(proj(n1, s1), I2) @ rs)) * np.real(np.trace(np.kron(I2, proj(n2, s2)) @ rs))
        formula_dev = max(formula_dev, abs(abs(joint - prod) - abs(n1 @ n2) / 4))
        if trial == 100:
            par_gap = max(par_gap, abs(joint - prod))
check("a reset update fails: leaving the partner unchanged gives p_q p_r, which misses the joint law on a singlet by |a.b|/4",
      formula_dev < 1e-12 and abs(par_gap - 0.25) < 1e-12,
      f"largest deviation from |a.b|/4 over 100 random axis pairs {formula_dev:.0e}; gap at parallel axes {par_gap:.3f}")


# ------------------------------------------------ 4. the whole rest
def lueders_rest(rho, P):
    M = np.kron(P, np.eye(4)) @ rho @ np.kron(P, np.eye(4))
    red = np.einsum("iaib->ab", M.reshape(2, 4, 2, 4))
    p = float(np.trace(red).real)
    if p <= 0:
        raise ValueError("undefined conditional state for zero-probability outcome")
    return red / p


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

# ------------------------------------------------ 5. two-possibility menus are antipodal
# compression consistency puts each effect on its possibility, E_k = e_k P_k; completeness e1 P1 + e2 P2 = I
# has a solution exactly when P1 and P2 are orthogonal (antipodal Bloch vectors), with e1 = e2 = 1
res_ = []
for ang in (np.pi, 0.9 * np.pi, 0.5 * np.pi, 0.2 * np.pi):
    n1 = np.array([0.0, 0.0, 1.0])
    n2 = np.array([np.sin(ang), 0.0, np.cos(ang)])
    A = np.array([proj(n1, 1).ravel(), proj(n2, 1).ravel()]).T
    e, resid, _, _ = np.linalg.lstsq(A, I2.ravel(), rcond=None)
    err = np.linalg.norm(A @ e - I2.ravel())
    res_.append((round(float(np.degrees(ang)), 1), round(float(err), 12), np.round(np.real(e), 6).tolist()))
check("two-possibility menus are antipodal: e1 P1 + e2 P2 = I is solvable only for antipodal possibilities, with e1 = e2 = 1",
      res_[0][1] < 1e-12 and res_[0][2] == [1.0, 1.0] and all(r[1] > 1e-3 for r in res_[1:]),
      "angle between possibilities (deg), completeness residual, weights: " + "; ".join(f"{r[0]}: {r[1]:.3f} {r[2]}" for r in res_))


Pm=(I2-PX)/2
rest=np.diag([1.0,0,0,0]).astype(complex)
rho_reg=np.kron(Pm,rest)
reg=lueders_rest(rho_reg,Pm)
M=np.kron(Pm,np.eye(4))@rho_reg@np.kron(Pm,np.eye(4))
blocks=M[:4,:4]+M[4:,4:]
check("minus-X positive-probability partial-trace regression",np.isfinite(reg).all() and np.allclose(reg,rest) and np.allclose(reg,blocks/np.trace(blocks)))
try:
    lueders_rest(np.kron(np.diag([1.,0]),rest),np.diag([0.,1.]))
    zero_rejected=False
except ValueError:
    zero_rejected=True
check("zero-probability conditional branch is explicitly undefined",zero_rejected)

# Scope resolutions are provenance, not additional numerical checks.
print('N5 resolution: Require positive outcome probability for a conditional state; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Correct the rest partial trace by identifying site indices; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Specify complete partner tomography and joint Born premises; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Separate partner uniqueness from global instrument uniqueness; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Retain larger supported menus as a counterroute; see the explicit conditional proof and limitation in the paired note.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
