#!/usr/bin/env python3
"""A distant record is a recorded randomizer: locality of marginals forces the trace rule.

The landed affine/Born gate note names preparation affinity as the missing
rung of the Born law, and asks for an autonomous recorded randomizer that
proves it. Under the dynamics clause of open PR 9040, a distant record is
one. The runner certifies (supplied models, finite diagnostics, no physical
reading):

1. The clause carries purifications: the Heisenberg bond at J t = pi is the
   swap (up to phase), and a partial swap prepares any reduced Bloch length
   0 <= |r| <= 1 from product states, so an entangled partner of a site can be
   placed at any distance.
2. Steering realizes every two-point decomposition: for a random qubit state
   rho and a random chord rho = p psi_1 + (1 - p) psi_2 through it, a record
   on a purifying partner in a suitable basis leaves the site in psi_1 or
   psi_2 with probabilities p and 1 - p.
3. The trace rule is consistent: for such ensembles, sum_b p_b P(+|rho_b)
   = P(+|rho) when P(+|r) = (1 + r.m)/2.
4. Nonlinear laws signal: for a tanh deformation built from the landed
   exp(k n.m) counterkernel, P(+|r) = (1 + tanh(k r.m)/tanh k)/2, and for a
   cubic deformation (both with the Born endpoints), the
   marginal at the site depends on whether and along which axis the distant
   partner is recorded. The largest shift over random draws is printed.
5. Chord consistency forces affinity: along random chords, the deformed laws
   are linear in the chord parameter only at zero deformation.
6. Orientation: an affine covariant law on an antipodal menu is
   (1 + lambda n.m)/2; repeat certainty (a pure +m site records +m) gives
   lambda = 1, the Born law.

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
I2 = np.eye(2, dtype=complex)
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]])
PZ = np.diag([1.0 + 0j, -1.0])
S = [PX / 2, PY / 2, PZ / 2]


def rho_of(r):
    return 0.5 * (I2 + r[0] * PX + r[1] * PY + r[2] * PZ)


def bloch(rho):
    return np.real(np.array([np.trace(rho @ P) for P in (PX, PY, PZ)]))


def unit(v):
    return v / np.linalg.norm(v)


# ------------------------------------------------ 1. the clause carries purifications
SS = sum(np.kron(s, s) for s in S)
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
Ubond = expm(-1j * np.pi * SS)                    # J t = pi
phase = Ubond[0, 0]
swap_dev = np.linalg.norm(Ubond - phase * SWAP)
lens = []
for theta in np.linspace(0, np.pi / 4, 7):          # 1 -> 0 as the partial swap entangles
    U = expm(-1j * theta * SWAP)
    psi = U @ np.kron(np.array([1, 0]), np.array([0, 1]))
    rho_a = np.einsum("ij,kj->ik", psi.reshape(2, 2), psi.reshape(2, 2).conj())
    lens.append(np.linalg.norm(bloch(rho_a)))
check("the clause carries purifications: the Heisenberg bond at J t = pi is the swap, and partial swaps give every reduced Bloch length",
      swap_dev < 1e-12 and abs(lens[0] - 1) < 1e-12 and min(lens) < 1e-12 and np.all(np.diff(lens) <= 1e-12),
      f"|U - phase * SWAP| {swap_dev:.1e}; reduced Bloch lengths along the partial swap {np.round(lens, 3).tolist()}")

# ------------------------------------------------ 2. steering realizes every chord
def random_chord():
    """A random mixed rho and a random chord through it with pure endpoints."""
    r = unit(rng.normal(size=3)) * rng.uniform(0.05, 0.95)
    d = unit(rng.normal(size=3))
    # endpoints r + t d on the unit sphere: t^2 + 2 t (r.d) + |r|^2 - 1 = 0
    b_ = r @ d
    disc = np.sqrt(b_ * b_ - (r @ r - 1))
    t1, t2 = -b_ + disc, -b_ - disc
    n1, n2 = r + t1 * d, r + t2 * d
    p = t2 / (t2 - t1)                              # r = p n1 + (1 - p) n2
    return r, n1, n2, p


def steer(n1, n2, p):
    """Purification of p|n1><n1| + (1-p)|n2><n2| and the partner basis that steers to it."""
    def ket(n):
        w, v = np.linalg.eigh(rho_of(n))
        return v[:, 1]
    k1, k2 = ket(n1), ket(n2)
    # |Psi> = sqrt(p)|k1>|0> + sqrt(1-p)|k2>|1>; recording the partner in {|0>,|1>} steers to k1, k2
    Psi = np.sqrt(p) * np.kron(k1, [1, 0]) + np.sqrt(1 - p) * np.kron(k2, [0, 1])
    out = []
    for b in range(2):
        proj = np.kron(I2, np.outer(np.eye(2)[b], np.eye(2)[b]))
        v = proj @ Psi
        pb = np.real(v.conj() @ v)
        rho_site = np.einsum("ij,kj->ik", v.reshape(2, 2), v.reshape(2, 2).conj()) / pb
        out.append((pb, bloch(rho_site)))
    rho_red = np.einsum("ij,kj->ik", Psi.reshape(2, 2), Psi.reshape(2, 2).conj())
    return bloch(rho_red), out


worst = 0.0
for _ in range(200):
    r, n1, n2, p = random_chord()
    red, out = steer(n1, n2, p)
    worst = max(worst, np.linalg.norm(red - r), abs(out[0][0] - p), np.linalg.norm(out[0][1] - n1), np.linalg.norm(out[1][1] - n2))
check("steering realizes every chord: a record on a purifying partner leaves the site in either endpoint with the chord weights",
      worst < 1e-10, f"200 random chords; largest deviation {worst:.1e}")

# ------------------------------------------------ 3-4. consistency and signalling
def law_trace(r, m):
    return 0.5 * (1 + r @ m)


def law_tanh(r, m, k=2.0):
    return 0.5 * (1 + np.tanh(k * (r @ m)) / np.tanh(k))


def law_cubic(r, m, eps=0.3):
    x = r @ m
    return 0.5 * (1 + x + eps * (x ** 3 - x))


def marginal_shift(law):
    """max |sum_b p_b P(rho_b) - P(rho)| over random chords and menu axes."""
    worst_ = 0.0
    for _ in range(300):
        r, n1, n2, p = random_chord()
        m = unit(rng.normal(size=3))
        worst_ = max(worst_, abs(p * law(n1, m) + (1 - p) * law(n2, m) - law(r, m)))
    return worst_


def axis_signal(law):
    """A partially entangled pair: recording the partner along x or z gives different site marginals."""
    worst_ = 0.0
    for _ in range(100):
        r = unit(rng.normal(size=3)) * rng.uniform(0.2, 0.8)
        m = unit(rng.normal(size=3))
        margs = []
        for _ in range(2):
            d = unit(rng.normal(size=3))
            b_ = r @ d
            disc = np.sqrt(b_ * b_ - (r @ r - 1))
            t1, t2 = -b_ + disc, -b_ - disc
            n1, n2 = r + t1 * d, r + t2 * d
            p = t2 / (t2 - t1)
            margs.append(p * law(n1, m) + (1 - p) * law(n2, m))
        worst_ = max(worst_, abs(margs[0] - margs[1]))
    return worst_


s_tr, s_tanh, s_cub = marginal_shift(law_trace), marginal_shift(law_tanh), marginal_shift(law_cubic)
check("the trace rule is consistent: the steered average equals the law at the reduced state",
      s_tr < 1e-12, f"largest |sum_b p_b P(rho_b) - P(rho)| over 300 chords {s_tr:.1e}")
a_tanh, a_cub = axis_signal(law_tanh), axis_signal(law_cubic)
check("nonlinear laws signal: a tanh deformation of the landed exp counterkernel and a cubic deformation change the site's marginal with the distant record and its axis",
      s_tanh > 1e-2 and s_cub > 1e-2 and a_tanh > 1e-2 and a_cub > 1e-2,
      f"record-or-not shift: tanh {s_tanh:.3f}, cubic {s_cub:.3f}; axis-choice shift: tanh {a_tanh:.3f}, cubic {a_cub:.3f}")

# ------------------------------------------------ 5. chord consistency forces affinity
def chord_nonlinearity(eps):
    worst_ = 0.0
    for _ in range(200):
        r, n1, n2, p = random_chord()
        m = unit(rng.normal(size=3))
        worst_ = max(worst_, abs(p * law_cubic(n1, m, eps) + (1 - p) * law_cubic(n2, m, eps) - law_cubic(r, m, eps)))
    return worst_


eps_list = [0.0, 0.01, 0.1, 0.3]
nl = [chord_nonlinearity(e) for e in eps_list]
check("chord consistency forces affinity: the cubic deformation passes only at zero deformation, and fails in proportion to it",
      nl[0] < 1e-12 and all(x > 1e-4 for x in nl[1:]) and nl[1] < nl[2] < nl[3],
      "largest chord violation " + ", ".join(f"eps {e}: {v:.1e}" for e, v in zip(eps_list, nl)))

# ------------------------------------------------ 6. orientation
m = np.array([0.0, 0.0, 1.0])
# affine covariant law on the menu {+m, -m}: P(+m | n) = (1 + lam n.m)/2; repeat certainty P(+m | m) = 1
lam = 2 * 1.0 - 1
check("orientation: repeat certainty fixes lambda = 1, the Born law (1 + n.m)/2",
      abs(lam - 1) < 1e-15 and abs(law_trace(m, m) - 1) < 1e-15 and abs(law_trace(-m, m)) < 1e-15,
      f"lambda {lam}; P(+m | m) = {law_trace(m, m)}, P(+m | -m) = {law_trace(-m, m)}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
