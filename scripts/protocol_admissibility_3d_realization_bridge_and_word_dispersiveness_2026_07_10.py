#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Protocol--Admissibility 3D realization bridge and composite-word dispersiveness.

Checks, on the named availability-rule model B and explicit conditional
protocol-realization conditions, the algebraic consequences relevant to the two
physical inputs named by the 3D factorized-protocol selection note:

  * factor covariance modulo local U(1) frames forces zero
    site-modulus translation defect (a necessary, not sufficient, shadow);
  * the 24 proper cubic rotations act transitively on the six
    nearest-neighbor offsets, so a single covariant variation forces all-axis
    constituent-factor support;
  * exact normal form for words in the six decorated movers, the
    support law, and the characteristic-polynomial dispersiveness dichotomy
    (a word is char-poly flat iff its net displacement is (0,0,0)).

Every construction is rebuilt locally (the sibling selection runner is NOT
imported).  There is no randomness, no audit metadata is read, and there is no
network or git access.  The 30 checks cover surface reconstruction, factor
covariance, rotation transport, word reduction, and source-note quote pins.
Final line: TOTAL: PASS=30 FAIL=0.

Determinism note: this runner prints no git state (its stdout is SHA-pinned into
a committed cache and must be reproducible); the human author runs
`git diff --stat` / `git status --porcelain` separately during review.
"""
from __future__ import annotations

import itertools
import os
import re
import sys

import numpy as np

PASS, FAIL = 0, 0
TOL = 1.0e-10
L = 4


def check(label, ok, detail=""):
    """Record one computed boolean."""
    global PASS, FAIL
    verdict = bool(ok)
    if verdict:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def heading(text):
    print(f"\n{text}")
    print("=" * 96)


# ---------------------------------------------------------------------------
# Cell (2^3 Bloch) constructions -- copied conventions from the selection runner.
comps = list(itertools.product((0, 1), repeat=3))
idx = {p: i for i, p in enumerate(comps)}


def eta_val(mu, p):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** p[0]
    return (-1) ** (p[0] + p[1])


def S_axis(kvec, axis, decorated=True):
    S = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(-1j * kvec[axis]) if p[axis] == 0 else 1.0
        S[idx[p], idx[q]] += (eta_val(axis, q) if decorated else 1.0) * phase
    return S


def S_axis_reverse(kvec, axis, decorated=True):
    S = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(+1j * kvec[axis]) if p[axis] == 1 else 1.0
        S[idx[p], idx[q]] += (eta_val(axis, q) if decorated else 1.0) * phase
    return S


THETA = np.pi / 5


def mixed_cycle_tick(kvec):
    Um = np.zeros((8, 8), dtype=complex)
    cycle0 = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    moves = ["across", "across", "within", "within"]
    for i, move in enumerate(moves):
        src, tgt = cycle0[i], cycle0[(i + 1) % 4]
        axis = [a for a in range(3) if src[a] != tgt[a]][0]
        sign = +1 if tgt[axis] == 1 else -1
        phase = np.exp(1j * sign * kvec[axis]) if move == "across" else 1.0
        Um[idx[tgt], idx[src]] = phase
    cycle1 = [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    for i in range(4):
        src, tgt = cycle1[i], cycle1[(i + 1) % 4]
        Um[idx[tgt], idx[src]] = 1.0
    return Um


def staircase(kvec):
    W = np.zeros((8, 8), dtype=complex)
    for p in comps:
        axis = 0 if (p[0] + p[1]) % 2 == 0 else 1
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        sign = +1 if q[axis] == 1 else -1
        phase = np.exp(1j * sign * kvec[axis]) if q[axis] == 0 else 1.0
        W[idx[q], idx[p]] = phase
    return W


def pairing_bloch(kvec, axis):
    M = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(-1j * kvec[axis]) if p[axis] == 1 else np.exp(+1j * kvec[axis])
        M[idx[q], idx[p]] = phase
    return M


def pairing_factor_bloch(axis):
    """One nearest-neighbor pairing factor on `axis` (Bloch form)."""
    return lambda kvec: (
        np.cos(THETA) * np.eye(8) + 1j * np.sin(THETA) * pairing_bloch(kvec, axis)
    )


def diag_bloch(_kvec):
    return np.diag([np.exp(1j * THETA * ((-1) ** sum(p))) for p in comps])


# ---------------------------------------------------------------------------
# Site (L=4 ring, 64 sites) constructions.
coords = list(itertools.product(range(L), repeat=3))
site_idx = {x: i for i, x in enumerate(coords)}
coords_arr = np.array(coords, dtype=int)


def shifted(x, axis, amount):
    y = list(x)
    y[axis] = (y[axis] + amount) % L
    return tuple(y)


def site_shift(axis, direction, decorated=True):
    F = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        target = shifted(source, axis, direction)
        parity = tuple(v % 2 for v in source)
        phase = eta_val(axis, parity) if decorated else 1.0
        F[site_idx[target], site_idx[source]] = phase
    return F


def cell_translation(axis):
    """Whole-cell (two-site) translation on `axis`, built independently."""
    T = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        target = shifted(source, axis, +2)
        T[site_idx[target], site_idx[source]] = 1.0
    return T


T_cell = [cell_translation(a) for a in range(3)]


def site_mixed_cycle():
    F = np.zeros((L**3, L**3), dtype=complex)
    cycles = {
        0: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
        1: [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],
    }
    for source in coords:
        p = tuple(v % 2 for v in source)
        cycle = cycles[p[2]]
        i = cycle.index(p)
        q = cycle[(i + 1) % 4]
        axis = [a for a in range(3) if p[a] != q[a]][0]
        amount = -1 if p[2] == 0 else q[axis] - p[axis]
        target = shifted(source, axis, amount)
        F[site_idx[target], site_idx[source]] = 1.0
    return F


def site_staircase():
    F = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        p = tuple(v % 2 for v in source)
        axis = 0 if (p[0] + p[1]) % 2 == 0 else 1
        target = shifted(source, axis, +1)
        F[site_idx[target], site_idx[source]] = 1.0
    return F


def site_pairing(axis):
    M = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        amount = +1 if source[axis] % 2 == 1 else -1
        target = shifted(source, axis, amount)
        M[site_idx[target], site_idx[source]] = 1.0
    return M


def site_pairing_factor(axis):
    """One nearest-neighbor pairing factor on `axis` (site form)."""
    return np.cos(THETA) * np.eye(L**3) + 1j * np.sin(THETA) * site_pairing(axis)


def pairflat_bloch(kvec):
    """The parent inventory's single composite P_PAIRFLAT constituent factor."""
    return compose([pairing_factor_bloch(axis)(kvec) for axis in range(3)], 8)


def site_pairflat():
    """Site form of the parent inventory's single composite P_PAIRFLAT factor."""
    return compose([site_pairing_factor(axis) for axis in range(3)], L**3)


def site_diagonal():
    return np.diag([
        np.exp(1j * THETA * ((-1) ** sum(v % 2 for v in x))) for x in coords
    ])


def compose(matrices, dimension):
    out = np.eye(dimension, dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def forward(axis, decorated=True):
    return lambda kvec: S_axis(kvec, axis, decorated)


def reverse(axis, decorated=True):
    return lambda kvec: S_axis_reverse(kvec, axis, decorated)


site_forward = [site_shift(a, +1, decorated=True) for a in range(3)]
site_reverse = [site_shift(a, -1, decorated=True) for a in range(3)]

protocols = {
    "P_SYM": {
        "bloch_factors": [forward(0), forward(1), forward(2)],
        "site_factors": [site_forward[0], site_forward[1], site_forward[2]],
    },
    "P_SYM_OCT": {
        "bloch_factors": [reverse(0), forward(1), forward(2)],
        "site_factors": [site_reverse[0], site_forward[1], site_forward[2]],
    },
    "P_REORDER": {
        "bloch_factors": [forward(1), forward(0), forward(2)],
        "site_factors": [site_forward[1], site_forward[0], site_forward[2]],
    },
    "P_WEIGHT": {
        "bloch_factors": [forward(0), forward(0), forward(1), forward(2)],
        "site_factors": [site_forward[0], site_forward[0], site_forward[1], site_forward[2]],
    },
    "P_AXIS": {
        "bloch_factors": [forward(0)],
        "site_factors": [site_forward[0]],
    },
    "P_MIX4": {
        "bloch_factors": [mixed_cycle_tick],
        "site_factors": [site_mixed_cycle()],
    },
    "P_STAIR": {
        "bloch_factors": [staircase],
        "site_factors": [site_staircase()],
    },
    "P_PAIRFLAT": {
        "bloch_factors": [pairflat_bloch],
        "site_factors": [site_pairflat()],
    },
    "P_CANCEL": {
        "bloch_factors": [forward(0), reverse(0), forward(1), reverse(1), forward(2), reverse(2)],
        "site_factors": [site_forward[0], site_reverse[0], site_forward[1], site_reverse[1], site_forward[2], site_reverse[2]],
    },
    "P_DIAG": {
        "bloch_factors": [diag_bloch],
        "site_factors": [site_diagonal()],
    },
}


def bloch_protocol(name, kvec):
    return compose([f(kvec) for f in protocols[name]["bloch_factors"]], 8)


def site_protocol(name):
    return compose(protocols[name]["site_factors"], L**3)


# ---------------------------------------------------------------------------
# Filter functionals (copied semantics from the selection runner).
translations = []
for axis in range(3):
    T = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        T[site_idx[shifted(source, axis, +1)], site_idx[source]] = 1.0
    translations.append(T)


def factor_translation_defect(F):
    return max(
        np.max(np.abs(np.abs(T @ F @ T.conj().T) - np.abs(F)))
        for T in translations
    )


def protocol_factor_modulus_defect(name):
    return max(factor_translation_defect(F) for F in protocols[name]["site_factors"])


def is_nearest_neighbor_pair(target, source, axis):
    same_transverse = all(target[a] == source[a] for a in range(3) if a != axis)
    delta = (target[axis] - source[axis]) % L
    return same_transverse and delta in (1, L - 1)


def factor_support_vector(factors):
    vector = []
    for axis in range(3):
        occupied = any(
            abs(F[site_idx[target], site_idx[source]]) > TOL
            for F in factors
            for source in coords
            for target in coords
            if is_nearest_neighbor_pair(target, source, axis)
        )
        vector.append(int(occupied))
    return tuple(vector)


# ---------------------------------------------------------------------------
# Fixed momentum grid for the characteristic-polynomial dispersion measure.
K = [
    (0.3, 0.7, 1.1),
    (1.9, 0.5, 2.3),
    (0.9, 2.7, 1.7),
    (2.9, 1.3, 0.7),
    (0.1, 1.1, 2.1),
    (1.3, 2.9, 0.3),
]

bloch_fn = {}
for _a in range(3):
    bloch_fn[(_a, +1)] = (lambda kvec, a=_a: S_axis(kvec, a, True))
    bloch_fn[(_a, -1)] = (lambda kvec, a=_a: S_axis_reverse(kvec, a, True))


def bloch_word(word, kvec):
    mats = [bloch_fn[l](kvec) for l in word]
    return compose(mats, 8) if mats else np.eye(8, dtype=complex)


def word_dispersion(word):
    polys = [np.poly(bloch_word(word, kvec)) for kvec in K]
    return max(np.max(np.abs(p - polys[0])) for p in polys[1:])


def protocol_dispersion(name):
    polys = [np.poly(bloch_protocol(name, kvec)) for kvec in K]
    return max(np.max(np.abs(p - polys[0])) for p in polys[1:])


# ---------------------------------------------------------------------------
# The six decorated-mover letters as exact real signed permutations on L=4 and
# L=6.  L=4 gives the exact reduction identity; L=6 gives an aliasing-free
# support law (|net_i| <= 5 < 6 so no torus wraparound).
LETTERS = [(0, +1), (0, -1), (1, +1), (1, -1), (2, +1), (2, -1)]


def _signed_perm(ring, axis, direction):
    ring_coords = list(itertools.product(range(ring), repeat=3))
    index = {x: i for i, x in enumerate(ring_coords)}
    perm = np.empty(ring**3, dtype=np.int64)
    sgn = np.empty(ring**3, dtype=np.int64)
    for s, source in enumerate(ring_coords):
        y = list(source)
        y[axis] = (y[axis] + direction) % ring
        perm[s] = index[tuple(y)]
        sgn[s] = eta_val(axis, tuple(v % 2 for v in source))
    return perm, sgn


perm4 = {}
sign4 = {}
for _l in LETTERS:
    perm4[_l], sign4[_l] = _signed_perm(L, _l[0], _l[1])

L6 = 6
coords6 = list(itertools.product(range(L6), repeat=3))
coords6_arr = np.array(coords6, dtype=int)
perm6 = {}
for _l in LETTERS:
    perm6[_l], _ = _signed_perm(L6, _l[0], _l[1])


def net_of(word):
    net = [0, 0, 0]
    for axis, sign in word:
        net[axis] += sign
    return tuple(net)


def sigma_of(word):
    axes = [axis for axis, _ in word]
    inversions = sum(
        1
        for i in range(len(axes))
        for j in range(i + 1, len(axes))
        if axes[i] > axes[j]
    )
    return -1 if inversions % 2 else 1


def direct_signed(word):
    """Exact signed permutation of the L=4 site product M(l1) @ ... @ M(ln)."""
    P = np.arange(L**3)
    Sg = np.ones(L**3, dtype=np.int64)
    for l in reversed(word):
        Sg = Sg * sign4[l][P]
        P = perm4[l][P]
    return P, Sg


# L=12 makes the central exponents m_i load-bearing: T_cell_i^{m_i} shifts 2 m_i
# sites, and for |net_i| <= 5 the residual shift 2 m_i in [-4, 4] never wraps on the
# L=12 ring.  On the L=4 ring a wrong m_i is invisible because T_cell_i^2 = I aliases
# every even shift to the identity; the normal form is therefore realized as an explicit
# operator product on L=12 (not reconstructed from net displacement).
L12 = 12
coords12 = list(itertools.product(range(L12), repeat=3))
idx12 = {x: i for i, x in enumerate(coords12)}
perm12 = {}
sign12 = {}
for _l in LETTERS:
    perm12[_l], sign12[_l] = _signed_perm(L12, _l[0], _l[1])


_shift_cache = {}


def cell_shift_perm(ring, idxmap, axis, twostep):
    """Central cell translation T_cell_axis^{m} as a bare permutation (shift 2m sites)."""
    key = (ring, axis, twostep % ring)
    if key not in _shift_cache:
        ring_coords = list(itertools.product(range(ring), repeat=3))
        perm = np.empty(ring**3, dtype=np.int64)
        for s, src in enumerate(ring_coords):
            y = list(src)
            y[axis] = (y[axis] + twostep) % ring
            perm[s] = idxmap[tuple(y)]
        _shift_cache[key] = perm
    return _shift_cache[key]


def _compose_signed(factors, ring):
    """Compose an ordered list of (perm, sign) signed permutations, left-to-right."""
    P = np.arange(ring**3)
    Sg = np.ones(ring**3, dtype=np.int64)
    for perm, sign in reversed(factors):
        Sg = Sg * sign[P]
        P = perm[P]
    return P, Sg


def direct_signed_12(word):
    """Exact signed permutation of the L=12 site product M(l1) @ ... @ M(ln)."""
    P = np.arange(L12**3)
    Sg = np.ones(L12**3, dtype=np.int64)
    for l in reversed(word):
        Sg = Sg * sign12[l][P]
        P = perm12[l][P]
    return P, Sg


def normal_form_op(word, ring, idxmap, permL, signL, m_override=None):
    """Realize sigma * prod_i T_cell_i^{m_i} * S_0^{e0} S_1^{e1} S_2^{e2} as an explicit
    operator product of central cell translations and residual movers on `ring`."""
    net = net_of(word)
    sigma = sigma_of(word)
    eps = tuple(n % 2 for n in net)
    if m_override is None:
        m = tuple((net[i] - eps[i]) // 2 for i in range(3))
    else:
        m = m_override
    ones_ring = np.ones(ring**3, dtype=np.int64)
    factors = []
    for i in range(3):
        if m[i] != 0:
            factors.append((cell_shift_perm(ring, idxmap, i, 2 * m[i]), ones_ring))
    for i in range(3):
        if eps[i] == 1:
            factors.append((permL[(i, +1)], signL[(i, +1)]))
    P, Sg = _compose_signed(factors, ring)
    return P, sigma * Sg


def measured_support6(word):
    """Site-level per-axis support on the L=6 ring (aliasing-free)."""
    cur = np.arange(L6**3)
    for l in reversed(word):
        cur = perm6[l][cur]
    disp = (coords6_arr[cur] - coords6_arr) % L6
    return tuple(int(np.any(disp[:, axis] != 0)) for axis in range(3))


# ---------------------------------------------------------------------------
# The 24 proper cubic rotations as 3x3 integer signed permutations (det +1).
NN = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
nn_index = {o: i for i, o in enumerate(NN)}

rotations = []
for _perm in itertools.permutations(range(3)):
    for _signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=int)
        for i in range(3):
            R[i, _perm[i]] = _signs[i]
        if round(float(np.linalg.det(R))) == 1:
            rotations.append(R)


def rotate_offset(R, offset):
    return tuple(int(v) for v in (R @ np.array(offset)))


rot_perms = [
    tuple(nn_index[rotate_offset(R, o)] for o in NN) for R in rotations
]


def rotate_profile(profile, rperm):
    """(c o R)[i] = c(R o_i): read the slot the rotation carries i into."""
    return tuple(profile[rperm[i]] for i in range(6))


PROFILES = list(itertools.product((0, 1), repeat=6))


def variation_set(rule):
    """Slots d where flipping only slot d can change the rule value."""
    varied = set()
    for c in PROFILES:
        for d in range(6):
            cp = list(c)
            cp[d] ^= 1
            if rule(c) != rule(tuple(cp)):
                varied.add(d)
    return varied


# ---------------------------------------------------------------------------
heading("Protocol-realization model: six decorated movers and cubic rotations")

site_letter = {l: site_shift(l[0], l[1], decorated=True) for l in LETTERS}
eye64 = np.eye(L**3)

site_unit = max(
    np.max(np.abs(site_letter[l] @ site_letter[l].conj().T - eye64)) for l in LETTERS
)
bloch_unit = max(
    np.max(np.abs(bloch_fn[l](kvec) @ bloch_fn[l](kvec).conj().T - np.eye(8)))
    for l in LETTERS
    for kvec in K
)
check(
    "six decorated movers unitary at site (64) and across the Bloch grid",
    site_unit < TOL and bloch_unit < 1e-10,
    f"site={site_unit:.2e} bloch={bloch_unit:.2e}",
)

anti = 0.0
for l in LETTERS:
    for m in LETTERS:
        if l[0] != m[0]:
            anti = max(
                anti,
                np.max(np.abs(site_letter[l] @ site_letter[m] + site_letter[m] @ site_letter[l])),
            )
check(
    "cross-axis letters anticommute at site level (including inverse letters)",
    anti < 1e-12,
    f"max|{{S_a,S_b}}|={anti:.2e}",
)

sq_err = max(
    np.max(np.abs(site_letter[(i, +1)] @ site_letter[(i, +1)] - T_cell[i])) for i in range(3)
)
central = 0.0
for i in range(3):
    for l in LETTERS:
        central = max(
            central, np.max(np.abs(T_cell[i] @ site_letter[l] - site_letter[l] @ T_cell[i]))
        )
check(
    "S_i^2 equals the independently built cell translation, which is central",
    sq_err < TOL and central < TOL,
    f"square={sq_err:.2e} central={central:.2e}",
)

inv_unit = max(
    np.max(np.abs(site_letter[(i, +1)] @ site_letter[(i, +1)].conj().T - eye64)) for i in range(3)
)
inv_match = max(
    np.max(np.abs(site_letter[(i, -1)] - site_letter[(i, +1)].conj().T)) for i in range(3)
)
check(
    "forward mover unitary and the inverse letter equals its adjoint",
    inv_unit < TOL and inv_match < TOL,
    f"unit={inv_unit:.2e} adjoint={inv_match:.2e}",
)

proper = all(
    np.array_equal(R @ R.T, np.eye(3, dtype=int)) and round(float(np.linalg.det(R))) == 1
    for R in rotations
)
orbit = {rperm[0] for rperm in rot_perms}
products = set()
closed = True
for R1 in rotations:
    for R2 in rotations:
        Rp = R1 @ R2
        if not (
            np.array_equal(Rp @ Rp.T, np.eye(3, dtype=int))
            and round(float(np.linalg.det(Rp))) == 1
        ):
            closed = False
        products.add(tuple(int(v) for v in Rp.flatten()))
distinct = len({tuple(int(v) for v in R.flatten()) for R in rotations})
check(
    "twenty-four proper cubic rotations, closed, transitive on the six NN offsets",
    len(rotations) == 24
    and proper
    and orbit == set(range(6))
    and closed
    and distinct == 24
    and len(products) == 24,
    f"|G|={len(rotations)} orbit={sorted(orbit)} distinct={distinct}",
)

# ---------------------------------------------------------------------------
heading("Factor covariance modulo local frames implies zero modulus defect")

F0 = site_shift(1, +1, decorated=True)  # decorated mover used by frame checks
F0_bare = site_shift(1, +1, decorated=False)  # the exactly covariant bare shift F^{(0)}
bare_cov_err = max(
    np.max(np.abs(translations[a] @ F0_bare @ translations[a].conj().T - F0_bare))
    for a in range(3)
)
g_frame = np.diag([(-1.0) ** (x[0] * x[1]) for x in coords]).astype(complex)
recon_err = np.max(np.abs(g_frame @ F0_bare @ g_frame.conj().T - F0))
dec_noncov_gap = max(
    np.max(np.abs(translations[a] @ F0 @ translations[a].conj().T - F0))
    for a in range(3)
)
mod_defect = factor_translation_defect(F0)
check(
    "decorated mover is a local-frame conjugate of the exactly covariant bare shift, is not itself translation-covariant, and has zero modulus defect",
    bare_cov_err < 1e-12 and recon_err < 1e-12 and dec_noncov_gap > 1.0 and mod_defect < TOL,
    f"bare_cov={bare_cov_err:.2e} recon={recon_err:.2e} dec_noncov_gap={dec_noncov_gap:.2f} modulus_defect={mod_defect:.2e}",
)

theta = np.array([(0.10 + 0.85 * rank) % np.pi for rank in range(L**3)])
g = np.diag(np.exp(1j * theta))
F_frame = g @ F0 @ g.conj().T
frame_defect = factor_translation_defect(F_frame)
check(
    "an arbitrary local-frame decoration preserves zero modulus defect",
    frame_defect < 1e-12,
    f"defect={frame_defect:.2e}",
)

mod_match = np.max(np.abs(np.abs(F_frame) - np.abs(F0)))
check(
    "the frame decoration is modulus-blind (|F| equals |F0| entrywise)",
    mod_match < 1e-12,
    f"max||F|-|F0||={mod_match:.2e}",
)

givens = np.eye(L**3, dtype=complex)
for x0 in range(L):
    for x2 in range(L):
        for lo, hi, angle in [(0, 1, 0.3), (2, 3, 0.9)]:
            a = site_idx[(x0, lo, x2)]
            b = site_idx[(x0, hi, x2)]
            c, s = np.cos(angle), np.sin(angle)
            givens[a, a] = c
            givens[b, b] = c
            givens[a, b] = -s
            givens[b, a] = s
giv_unit = np.max(np.abs(givens @ givens.conj().T - eye64))
giv_support = factor_support_vector([givens])
giv_defect = factor_translation_defect(givens)
check(
    "a site-dependent axis-1 Givens rotation is unitary and NN-supported but has positive modulus defect",
    giv_unit < TOL and giv_support == (0, 1, 0) and giv_defect > 0.05,
    f"unit={giv_unit:.2e} support={giv_support} defect={giv_defect:.3f}",
)

D_alt = np.diag([(-1.0) ** x[1] for x in coords])
dalt_defect = factor_translation_defect(D_alt)
frame_inv = np.max(np.abs(g @ D_alt @ g.conj().T - D_alt))
t1_conj = translations[1] @ D_alt @ translations[1].conj().T
sign_flip = np.max(np.abs(t1_conj - (-D_alt)))
gap = np.max(np.abs(-D_alt - D_alt))
check(
    "a covariant-modulus diagonal that translations sign-flip has zero defect but is not frame-covariant",
    dalt_defect < TOL and frame_inv < 1e-12 and sign_flip < 1e-12 and gap > 1.0,
    f"defect={dalt_defect:.2e} frame_inv={frame_inv:.2e} flip={sign_flip:.2e} gap={gap:.2f}",
)

bare = site_shift(1, +1, decorated=False)
bare_defect = factor_translation_defect(bare)
check(
    "the undecorated bare shift also has zero modulus defect (the functional is not spuriously positive)",
    bare_defect < TOL,
    f"defect={bare_defect:.2e}",
)

# ---------------------------------------------------------------------------
heading("Rotation transitivity and the axis-faithful condition force all-axis support")


def rule_parity(profile):
    return frozenset({0, 1}) if sum(profile) % 2 == 0 else frozenset({0})


def rule_slot0(profile):
    return frozenset({0, 1}) if profile[0] == 1 else frozenset({0})


def is_rotation_covariant(rule):
    for c in PROFILES:
        base = rule(c)
        for rperm in rot_perms:
            if rule(rotate_profile(c, rperm)) != base:
                return False
    return True


cov_parity = is_rotation_covariant(rule_parity)
var_parity = variation_set(rule_parity)
check(
    "the parity availability rule B is rotation-covariant and varies at slot 0",
    cov_parity and 0 in var_parity,
    f"covariant={cov_parity} slot0_in_V={0 in var_parity}",
)
orbit0 = {rperm[0] for rperm in rot_perms}
check(
    "rotation transport carries slot 0 to all six NN directions, and the covariant parity rule varies on exactly that orbit",
    orbit0 == set(range(6)) and var_parity == orbit0,
    f"orbit0={sorted(orbit0)} V(B)={sorted(var_parity)}",
)

cov_slot0 = is_rotation_covariant(rule_slot0)
var_slot0 = variation_set(rule_slot0)
check(
    "control: a single-slot rule varies only at slot 0 and is NOT rotation-covariant",
    var_slot0 == {0} and not cov_slot0,
    f"V(B')={sorted(var_slot0)} covariant={cov_slot0}",
)

support_all = factor_support_vector(
    [site_letter[(0, +1)], site_letter[(1, +1)], site_letter[(2, +1)]]
)
check(
    "the all-axis mover set (S_1,S_2,S_3) has full constituent-factor support",
    support_all == (1, 1, 1),
    f"support={support_all}",
)

support_same = factor_support_vector([site_letter[(0, +1)], site_letter[(0, +1)]])
check(
    "a same-axis mover pair (S_1,S_1) supports only its own axis",
    support_same == (1, 0, 0),
    f"support={support_same}",
)

# ---------------------------------------------------------------------------
heading("Decorated-word normal form, support law, and dispersiveness dichotomy")

all_words = []
for length in range(1, 6):
    for w in itertools.product(LETTERS, repeat=length):
        all_words.append(w)

d1_bad = d2_bad = d3_bad = 0
for w in all_words:
    net = net_of(w)
    perm_direct, sign_direct = direct_signed_12(w)
    perm_normal, sign_normal = normal_form_op(w, L12, idx12, perm12, sign12)
    if not (
        np.array_equal(perm_direct, perm_normal)
        and np.array_equal(sign_direct, sign_normal)
    ):
        d1_bad += 1
    predicted = tuple(int(net[a] != 0) for a in range(3))
    if measured_support6(w) != predicted:
        d2_bad += 1
    disp = word_dispersion(w)
    should_be_flat = net == (0, 0, 0)
    if should_be_flat:
        if disp >= 1e-8:
            d3_bad += 1
    else:
        if disp <= 1e-6:
            d3_bad += 1

check(
    "exact normal form W = sigma * prod T_cell^m * residual movers (all 9330 words, len<=5)",
    len(all_words) == 9330 and d1_bad == 0,
    f"words={len(all_words)} mismatches={d1_bad}",
)

w_reject = ((0, +1),) * 4  # S_0^4: net=(4,0,0), true m=(2,0,0)
m_bad = (4, 0, 0)  # perturb m_0 by +2
pd12, sd12 = direct_signed_12(w_reject)
pb12, sb12 = normal_form_op(w_reject, L12, idx12, perm12, sign12, m_override=m_bad)
caught_12 = not (np.array_equal(pd12, pb12) and np.array_equal(sd12, sb12))
pd4, sd4 = direct_signed(w_reject)
pb4, sb4 = normal_form_op(w_reject, L, site_idx, perm4, sign4, m_override=m_bad)
aliases_4 = np.array_equal(pd4, pb4) and np.array_equal(sd4, sb4)
check(
    "a wrong central exponent m_i is caught on L=12 but aliases to identity on L=4 (m_i is load-bearing)",
    caught_12 and aliases_4,
    f"caught_on_L12={caught_12} aliases_on_L4={aliases_4}",
)
check(
    "support law on the aliasing-free L=6 ring: axis-i occupied iff net_i != 0 (all 9330 words)",
    d2_bad == 0,
    f"mismatches={d2_bad}",
)
check(
    "dispersiveness dichotomy: Bloch char-poly flat (<1e-8) iff net displacement is (0,0,0) (all 9330 words)",
    d3_bad == 0,
    f"anomalies={d3_bad}",
)

witnesses = [
    (((0, +1), (1, +1), (0, -1), (1, -1), (2, +1), (2, -1)), (0, 0, 0), -1, True),
    (((0, +1), (0, -1), (1, +1), (1, -1), (2, +1), (2, -1)), (0, 0, 0), +1, True),
    (((0, +1), (1, +1), (2, +1), (0, +1), (1, +1), (2, +1)), (2, 2, 2), -1, False),
    (((0, +1), (0, +1), (1, +1), (1, +1), (2, +1), (2, +1)), (2, 2, 2), +1, False),
    (((0, +1), (2, +1), (1, +1), (1, -1), (2, -1), (0, -1)), (0, 0, 0), +1, True),
]
d4_bad = 0
for word, exp_net, exp_sigma, exp_flat in witnesses:
    perm_direct, sign_direct = direct_signed_12(word)
    perm_normal, sign_normal = normal_form_op(word, L12, idx12, perm12, sign12)
    ok = (
        net_of(word) == exp_net
        and sigma_of(word) == exp_sigma
        and np.array_equal(perm_direct, perm_normal)
        and np.array_equal(sign_direct, sign_normal)
    )
    if exp_flat:
        ok = (
            ok
            and np.array_equal(perm_direct, np.arange(L12**3))
            and np.array_equal(sign_direct, exp_sigma * np.ones(L12**3, dtype=np.int64))
        )
        dense = max(
            np.max(np.abs(bloch_word(word, kvec) - exp_sigma * np.eye(8))) for kvec in K
        )
        ok = ok and dense < 1e-12
    else:
        ok = ok and word_dispersion(word) > 1e-6
    if not ok:
        d4_bad += 1
check(
    "five named length-6 witnesses: exact normal form, net, sign, and +-I / dispersive value",
    d4_bad == 0,
    f"failed_witnesses={d4_bad}",
)

pc_defect = protocol_factor_modulus_defect("P_CANCEL")
pc_support = factor_support_vector(protocols["P_CANCEL"]["site_factors"])
pc_identity = np.max(np.abs(site_protocol("P_CANCEL") - eye64))
pc_disp = protocol_dispersion("P_CANCEL")
check(
    "P_CANCEL separates the filters: zero modulus defect, full support, composite identity, flat",
    pc_defect < TOL and pc_support == (1, 1, 1) and pc_identity < TOL and pc_disp < 1e-8,
    f"defect={pc_defect:.2e} support={pc_support} identity={pc_identity:.2e} disp={pc_disp:.2e}",
)

pw_support = factor_support_vector(protocols["P_WEIGHT"]["site_factors"])
pw_disp = protocol_dispersion("P_WEIGHT")
pw_defect = protocol_factor_modulus_defect("P_WEIGHT")
check(
    "P_WEIGHT (net (2,1,1)) has full support, zero modulus defect, and is dispersive",
    pw_support == (1, 1, 1) and pw_disp > 1e-7 and pw_defect < TOL,
    f"support={pw_support} disp={pw_disp:.2e} defect={pw_defect:.2e}",
)

id_disp = word_dispersion(())
s1_disp = word_dispersion(((0, +1),))


def signed_matrix(word):
    perm, sign = direct_signed(word)
    M = np.zeros((L**3, L**3))
    for col in range(L**3):
        M[perm[col], col] = sign[col]
    return M


reorder_gap = np.max(
    np.abs(signed_matrix(((0, +1), (1, +1))) - signed_matrix(((1, +1), (0, +1))))
)
check(
    "identity flat, single mover dispersive, and dropping the anticommutation sign is detectable",
    id_disp < 1e-8 and s1_disp > 1e-3 and reorder_gap > 1.0,
    f"id={id_disp:.2e} s1={s1_disp:.3f} reorder_gap={reorder_gap:.2f}",
)


def first_failing_filter(name):
    if protocol_factor_modulus_defect(name) >= TOL:
        return "defect"
    if factor_support_vector(protocols[name]["site_factors"]) != (1, 1, 1):
        return "support"
    if protocol_dispersion(name) <= 1e-7:
        return "dispersion"
    return "survivor"


attribution = {}
for name in protocols:
    attribution.setdefault(first_failing_filter(name), set()).add(name)
check(
    "the three filters jointly retain the four-member necessary-condition survivor set",
    attribution.get("survivor") == {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT"},
    f"survivors={sorted(attribution.get('survivor', set()))}",
)
check(
    "ordered filters attribute each rejection to its first-failing stage (defect/support/dispersion)",
    attribution.get("defect") == {"P_MIX4", "P_STAIR", "P_PAIRFLAT"}
    and attribution.get("support") == {"P_AXIS", "P_DIAG"}
    and attribution.get("dispersion") == {"P_CANCEL"},
    f"defect={sorted(attribution.get('defect', set()))} "
    f"support={sorted(attribution.get('support', set()))} "
    f"dispersion={sorted(attribution.get('dispersion', set()))}",
)

# ---------------------------------------------------------------------------
heading("Source-note quote pins and claim-boundary checks")

repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
note_path = os.path.join(
    repo,
    "docs",
    "PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md",
)
axioms_path = os.path.join(repo, "docs", "MINIMAL_AXIOMS_2026-06-29.md")
parent_path = os.path.join(
    repo,
    "docs",
    "KINETIC_ISOTROPY_3D_FACTORIZED_PROTOCOL_SELECTION_ON_ANALYZED_CLASSES_BOUNDED_THEOREM_NOTE_2026-07-09.md",
)


def _norm(text):
    return re.sub(r"\s+", " ", text).strip()


def _read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


note_norm = _norm(_read(note_path))
axioms_norm = _norm(_read(axioms_path))
parent_norm = _norm(_read(parent_path))

CLAUSE_1 = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice translations and proper cubic rotations."
)
CLAUSE_2 = (
    "For each site, the available possibilities are determined by, and vary "
    "with, the nearest-neighbor conditions."
)
SUPPLIED_1 = (
    "translation covariance of the fixed rule requires each constituent factor "
    "to be fully covariant modulo local"
)
SUPPLIED_2 = "dispersive in the characteristic-polynomial sense used by the runner"

e1 = _norm(CLAUSE_1) in axioms_norm and _norm(CLAUSE_2) in axioms_norm
check(
    "both admissibility clause sentences are present verbatim in the axioms file",
    e1,
    "axiom clauses anchored" if e1 else "MISSING axiom clause",
)

e2 = (
    _norm(CLAUSE_1) in note_norm
    and _norm(CLAUSE_2) in note_norm
    and "algebraic consequences" in note_norm
)
check(
    "the note quotes both axiom clauses and frames its results as conditional algebraic consequences",
    e2,
    "note clauses + framing present" if e2 else "MISSING note clause/framing",
)

e3 = (
    _norm(SUPPLIED_1) in note_norm
    and _norm(SUPPLIED_2) in note_norm
    and _norm(SUPPLIED_1) in parent_norm
    and _norm(SUPPLIED_2) in parent_norm
)
check(
    "the two supplied-input fragments appear in the note and are anchored verbatim in the parent selection note",
    e3,
    "supplied inputs anchored in parent" if e3 else "MISSING supplied input",
)

FORBIDDEN = [
    "only route",
    "last route",
    "exhausted",
    "closes the route",
    "owner-directed",
    "retained",
    "audited_clean",
    "audited_conditional",
    "unaudited",
    "audit_ledger",
    "is sufficient",
    "sufficient for",
    "clean grade",
    "passes the audit",
    "np.random",
    "import random",
    "datetime.now",
    "time.time",
]
note_low = note_norm.lower()
present = [token for token in FORBIDDEN if token.lower() in note_low]
check(
    "the note is free of forbidden status/framing/nondeterminism language",
    not present,
    "clean" if not present else f"PRESENT: {present}",
)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
