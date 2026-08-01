#!/usr/bin/env python3
"""Cycle 703 (gravity lane) - finite-range law-identification tournament.

Executes the successor experiment named by the Cycle-700 landed note: replace the
supplied nearest-neighbour law by a three-parameter supplied family of finite-range
competitors and ask whether the executed double-relational ratio suite separates
them.  All machinery (box lattices, frozen source, detector sites, double-relational
ratio, Bessel-Green prediction) is imported from the Cycle-700 runner unchanged.

Supplied competitor family, on the odd-L boxes of the Cycle-700 runner:

    A_L(w) = A_L + w_F S_F + w_B S_B + w_2 S_2,   w >= 0 componentwise,

with A_L the Cycle-700 base law and the three deformation shells built by ONE
generic builder in the Cycle-700 face-matrix convention (off-diagonal -1 per in-box
shell neighbour, diagonal equal to the in-box shell-neighbour count of the site):

    S_F : the 12 offsets, permutations of (+-1, +-1, 0)   [Cycle-700's face shell]
    S_B : the 8 offsets (+-1, +-1, +-1)
    S_2 : the 6 offsets (+-2, 0, 0), (0, +-2, 0), (0, 0, +-2)

Gate blocks: a landed anchors, b shell builders, c scale-blindness lemma,
d second-moment isotropy lemma, e first-order response, f grid tournament,
g adversarial search plus held-out boxes, h discipline.

Usage:
    python3 scripts/physical_finite_range_law_tournament_cycle703_2026_08_01.py
    python3 scripts/physical_finite_range_law_tournament_cycle703_2026_08_01.py --no-receipt
"""

from __future__ import annotations

import importlib.util
import json
import sys
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
from time import perf_counter

import numpy as np
from scipy.sparse import coo_matrix, csc_matrix
from scipy.sparse.linalg import eigsh, splu

_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]
_OUT: list[str] = []
_PASS = 0
_FAIL = 0


def emit(line: str) -> None:
    _OUT.append(line)


def check(label: str, ok: bool, measured: object = "", pinned: object = "") -> bool:
    global _PASS, _FAIL
    if len(label) > 34 or not all(c.islower() or c.isdigit() or c == "_" for c in label):
        raise ValueError("invalid check label: " + label)
    if ok:
        _PASS += 1
        emit("PASS " + label)
    else:
        _FAIL += 1
        emit("FAIL " + label + " measured=" + str(measured) + " pinned=" + str(pinned))
    return ok


def load_module(root: Path, alias: str, relative: str):
    spec = importlib.util.spec_from_file_location(alias, root / relative)
    if spec is None or spec.loader is None:
        raise ImportError(relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C700 = load_module(
    ROOT,
    "cycle703_c700",
    "scripts/physical_operational_source_response_readout_chain_cycle700_2026_07_25.py",
)
# The Cycle-700 runner performs its own Cycle-696 import inside main(); reuse its
# loader (its own import stanza) so the source-scale constant comes from the same
# module object the landed cycle used.
C696 = load_module(
    ROOT,
    "cycle703_c696",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
)
SRC_SCALE = C696.SRC_SCALE

# ----------------------------------------------------------------- constants ---
L_LADDER = (9, 13, 19)
L_HOLDOUT = (7, 11, 15, 17)
W_ZERO = (0.0, 0.0, 0.0)
GRID_VALUES = (0.0, 0.25, 0.5, 1.0)
THRESHOLD_FACTOR = 10.0
SEARCH_STEP0 = 0.25
SEARCH_STEP_STOP = 1.0e-3
SEARCH_PROBE_CAP = 250
L1_FLOOR = 1.0e-3
SEARCH_BUDGET_S = 700.0
WALL_BUDGET_S = 900.0

LANDED_NN = (-4.112204466641254, -3.938488211332885, -3.9169789686578382)
LANDED_PRED = -3.913233185406517
LANDED_PRED_SPLIT = -3.9132331854898643
LANDED_MUT19 = -4.0411929130059585
LANDED_SEP = 0.12421394434812028
LANDED_STATIC_ERR = 0.0037457832
LANDED_SEP_RATIO = 33.161007665936864
LANDED_THRESHOLD = 0.037457832

OFFSETS_NN = tuple(sorted({tuple(0 if i != a else s for i in range(3))
                           for a in range(3) for s in (-1, 1)}))
OFFSETS_F = tuple(sorted({tuple(v) for v in
                          [(a, b, 0) for a in (-1, 1) for b in (-1, 1)]
                          + [(a, 0, b) for a in (-1, 1) for b in (-1, 1)]
                          + [(0, a, b) for a in (-1, 1) for b in (-1, 1)]}))
OFFSETS_B = tuple(sorted(product((-1, 1), repeat=3)))
OFFSETS_2 = tuple(sorted({tuple(0 if i != a else 2 * s for i in range(3))
                          for a in range(3) for s in (-1, 1)}))
SHELL_OFFSETS = (OFFSETS_F, OFFSETS_B, OFFSETS_2)
SHELL_MOMENTS = (8, 8, 8)

CHARGE_SITES = [((0, 0, 0), 1)]
for _axis in range(3):
    for _step in (-3, 3):
        _site = [0, 0, 0]
        _site[_axis] = _step
        CHARGE_SITES.append((tuple(_site), -3))


def g12(value: float) -> float:
    return float("%.12g" % value)


# ------------------------------------------------------------- shell builder ---
def build_shell(L: int, offsets) -> csc_matrix:
    """Graph-Laplacian shell matrix: -1 per in-box shell bond, in-box degree diagonal."""
    n = L ** 3
    flat = np.arange(n)
    gx, gy, gz = flat // (L * L), (flat // L) % L, flat % L
    rows = [flat]
    cols = [flat]
    vals = [np.zeros(n)]
    degree = np.zeros(n)
    for d in offsets:
        yx, yy, yz = gx + d[0], gy + d[1], gz + d[2]
        inside = ((yx >= 0) & (yx < L) & (yy >= 0) & (yy < L) & (yz >= 0) & (yz < L))
        target = (yx * L + yy) * L + yz
        rows.append(flat[inside])
        cols.append(target[inside])
        vals.append(-np.ones(int(inside.sum())))
        degree += inside
    vals[0] = degree
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                      shape=(n, n)).tocsc()


BASE: dict = {}
SHELLS: dict = {}
SOURCE: dict = {}
DETECT: dict = {}
FACTOR0: dict = {}
RATIOS: dict = {}
SOLVE_COUNT = [0]


def prepare(L: int) -> None:
    if L in BASE:
        return
    lap, _unused = C700.build_laplacian(L)
    BASE[L] = lap
    SHELLS[L] = [build_shell(L, offs) for offs in SHELL_OFFSETS]
    SOURCE[L] = C700.frozen_source(L, SRC_SCALE)
    DETECT[L] = [(s[0] * L + s[1]) * L + s[2] for s in C700.detector_sites(L)]


def assemble(L: int, w) -> csc_matrix:
    prepare(L)
    mat = BASE[L]
    for s in range(3):
        if w[s] != 0.0:
            mat = mat + w[s] * SHELLS[L][s]
    return mat


def fresh_ratio(L: int, w) -> float:
    SOLVE_COUNT[0] += 1
    phi = splu(csc_matrix(assemble(L, w))).solve(SOURCE[L])
    return float(C700.detector_ratio(phi, L))


def ratio(L: int, w) -> float:
    key = (L, w)
    hit = RATIOS.get(key)
    if hit is not None:
        return hit
    value = fresh_ratio(L, w)
    RATIOS[key] = value
    return value


def detector_pair(phi, L):
    i = DETECT[L]
    return phi[i[0]] - phi[i[1]], phi[i[2]] - phi[i[3]]


def separation(w, boxes=L_LADDER, baseline=None) -> float:
    base = baseline if baseline is not None else NN
    return max(abs(ratio(L, w) - base[L]) for L in boxes)


def objective(w):
    norm1 = w[0] + w[1] + w[2]
    if norm1 < L1_FLOOR:
        return None
    return separation(w) / norm1


# ------------------------------------------------------- block a: anchors ------
for _L in L_LADDER:
    prepare(_L)
NN = {L: ratio(L, W_ZERO) for L in L_LADDER}
R_PRED = float(C700.infinite_prediction(C700.green_evaluator(False), CHARGE_SITES))
R_PRED_SPLIT = float(C700.infinite_prediction(C700.green_evaluator(True), CHARGE_SITES))
W_MUT = (float(C700.FACE_MUTATION_WEIGHT), 0.0, 0.0)
R_MUT19 = ratio(19, W_MUT)
SEP_MUT = abs(R_MUT19 - NN[19])
STATIC_ERR19 = abs(NN[19] - R_PRED_SPLIT)
SEP_RATIO = SEP_MUT / STATIC_ERR19
THRESHOLD = THRESHOLD_FACTOR * STATIC_ERR19

a1_err = max(abs(NN[L] - LANDED_NN[i]) for i, L in enumerate(L_LADDER))
check("a1_landed_nn_ladder", a1_err <= 1e-12, "%.3e" % a1_err, "1e-12")
check("a2_bessel_green_prediction", abs(R_PRED - LANDED_PRED) <= 1e-12,
      "%.3e" % abs(R_PRED - LANDED_PRED), "1e-12")
check("a3_bessel_green_split", abs(R_PRED_SPLIT - LANDED_PRED_SPLIT) <= 1e-12,
      "%.3e" % abs(R_PRED_SPLIT - LANDED_PRED_SPLIT), "1e-12")
check("a4_landed_face_mutation_ratio", abs(R_MUT19 - LANDED_MUT19) <= 1e-12,
      "%.3e" % abs(R_MUT19 - LANDED_MUT19), "1e-12")
check("a5_landed_separation", abs(SEP_MUT - LANDED_SEP) <= 1e-12,
      "%.3e" % abs(SEP_MUT - LANDED_SEP), "1e-12")
check("a6_static_residual_and_ratio",
      abs(STATIC_ERR19 - LANDED_STATIC_ERR) <= 1e-6
      and abs(SEP_RATIO - LANDED_SEP_RATIO) <= 1e-6,
      "%.10g/%.12g" % (STATIC_ERR19, SEP_RATIO), "1e-6")
check("a7_comparison_threshold", abs(THRESHOLD - LANDED_THRESHOLD) <= 1e-5,
      "%.10g" % THRESHOLD, "1e-5")
emit("anchors sep=%.12g staticerr19=%.12g thr=%.10g" % (SEP_MUT, STATIC_ERR19, THRESHOLD))

# ------------------------------------------------- block b: shell builders -----
for _L, _label in ((19, "b1_face_shell_exact_l19"), (9, "b2_face_shell_exact_l9")):
    prepare(_L)
    _lap, _face = C700.build_laplacian(_L, face_mutation=True)
    _diff = (SHELLS[_L][0] - _face).tocsc()
    _diff.eliminate_zeros()
    check(_label, _diff.nnz == 0, _diff.nnz, 0)

_counts = (len(OFFSETS_F), len(OFFSETS_B), len(OFFSETS_2))
_interior = ((4 * 9) + 4) * 9 + 4
_degrees = tuple(int(round(float(SHELLS[9][s].diagonal()[_interior]))) for s in range(3))
check("b3_shell_offsets_and_degrees", _counts == (12, 8, 6) and _degrees == (12, 8, 6),
      "%s/%s" % (_counts, _degrees), "(12, 8, 6)")


def bond_energy(L: int, offsets, v) -> float:
    total = 0.0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                vi = v[i]
                for d in offsets:
                    ax, ay, az = x + d[0], y + d[1], z + d[2]
                    if 0 <= ax < L and 0 <= ay < L and 0 <= az < L:
                        total += (vi - v[(ax * L + ay) * L + az]) ** 2
    return 0.5 * total


_flat9 = np.arange(9 ** 3)
_FIELDS = ((_flat9 // 81).astype(float), ((_flat9 // 9) % 9).astype(float),
           (_flat9 % 9).astype(float))
_b4_worst = 0.0
for _s in range(3):
    for _v in _FIELDS:
        _quad = float(_v @ (SHELLS[9][_s] @ _v))
        _bond = bond_energy(9, SHELL_OFFSETS[_s], _v)
        _b4_worst = max(_b4_worst, abs(_quad - _bond) / max(1.0, abs(_bond)))
check("b4_shell_bond_energy_identity", _b4_worst <= 1e-9, "%.3e" % _b4_worst, "1e-9")

prepare(13)
_eig = float(eigsh(csc_matrix(assemble(13, (1.0, 1.0, 1.0))), k=1, which="SA",
                   return_eigenvectors=False)[0])
check("b5_mixed_law_positive_definite", _eig > 0.0, "%.10g" % _eig, "> 0")

# ------------------------------------------- block c: scale-blindness lemma ----
def scaled_ratio(L: int, w, factor: float) -> float:
    SOLVE_COUNT[0] += 1
    phi = splu(csc_matrix(assemble(L, w) * factor)).solve(SOURCE[L])
    return float(C700.detector_ratio(phi, L))


W_MIXED = (0.5, 0.25, 0.25)
for _label, _w in (("c1_scale_blind_nn_law", W_ZERO),
                   ("c2_scale_blind_mixed_law", W_MIXED)):
    _ref = ratio(13, _w)
    _dev = max(abs(scaled_ratio(13, _w, c) - _ref) for c in (2.0, 0.5, 17.0))
    check(_label, _dev <= 1e-12, "%.3e" % _dev, "1e-12")

# --------------------------------------------- block d: second-moment lemma ----
def second_moment(offsets):
    mom = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for d in offsets:
        for i in range(3):
            for j in range(3):
                mom[i][j] += d[i] * d[j]
    return mom


_d1_ok = True
for _offs, _m in zip((OFFSETS_NN,) + SHELL_OFFSETS, (2,) + SHELL_MOMENTS):
    _mom = second_moment(_offs)
    for i in range(3):
        for j in range(3):
            _d1_ok = _d1_ok and _mom[i][j] == (_m if i == j else 0)
check("d1_shell_second_moments", _d1_ok, "isotropic m=(2,8,8,8)", "m*I")

K_HAT = np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0)


def symbol(w, k) -> float:
    total = sum(1.0 - np.cos(float(np.dot(k, d))) for d in OFFSETS_NN)
    for s in range(3):
        if w[s] != 0.0:
            total += w[s] * sum(1.0 - np.cos(float(np.dot(k, d)))
                                for d in SHELL_OFFSETS[s])
    return float(total)


SIGMA_W = 1.0 + 4.0 * (W_MIXED[0] + W_MIXED[1] + W_MIXED[2])
_dev_a = abs(symbol(W_MIXED, 1e-2 * K_HAT) / 1e-4 - SIGMA_W)
_dev_b = abs(symbol(W_MIXED, 5e-3 * K_HAT) / 2.5e-5 - SIGMA_W)
_d2_ratio = _dev_a / _dev_b
check("d2_symbol_quadratic_limit", 3.0 <= _d2_ratio <= 5.0,
      "%.4g/%.4g r=%.4f" % (_dev_a, _dev_b, _d2_ratio), "[3,5]")

# --------------------------------------------- block e: first-order response ---
JAC = np.zeros((3, 3))
for _a, _L in enumerate(L_LADDER):
    FACTOR0[_L] = splu(BASE[_L])
    _phi0 = FACTOR0[_L].solve(SOURCE[_L])
    _n0, _d0 = detector_pair(_phi0, _L)
    for _s in range(3):
        _u = -FACTOR0[_L].solve(SHELLS[_L][_s] @ _phi0)
        _nu, _du = detector_pair(_u, _L)
        JAC[_a, _s] = (_nu * _d0 - _n0 * _du) / (_d0 * _d0)

_fd = {}
for _eps in (1e-3, 5e-4):
    _mat = np.zeros((3, 3))
    for _a, _L in enumerate(L_LADDER):
        for _s in range(3):
            _wp = [0.0, 0.0, 0.0]
            _wp[_s] = _eps
            _wm = [0.0, 0.0, 0.0]
            _wm[_s] = -_eps
            _mat[_a, _s] = (ratio(_L, tuple(_wp)) - ratio(_L, tuple(_wm))) / (2.0 * _eps)
    _fd[_eps] = _mat
_err_a = np.abs(_fd[1e-3] - JAC)
_err_b = np.abs(_fd[5e-4] - JAC)
_e1_ok = True
_worst = (0, 0)
for _i in range(3):
    for _j in range(3):
        _tol = 1e-9 * max(1.0, abs(JAC[_i, _j]))
        _rat = _err_a[_i, _j] / _err_b[_i, _j] if _err_b[_i, _j] > 0.0 else float("inf")
        _e1_ok = _e1_ok and (_err_b[_i, _j] <= _tol or 3.0 <= _rat <= 5.0)
        if _err_b[_i, _j] > _err_b[_worst]:
            _worst = (_i, _j)
check("e1_jacobian_fd_convergence", _e1_ok,
      "%.3e/%.3e" % (_err_a[_worst], _err_b[_worst]), "ratio in [3,5]")

SVALS = np.linalg.svd(JAC, compute_uv=False)
SIGMA_MIN = float(SVALS.min())
check("e2a_sigma_min_positive", SIGMA_MIN > 1.0e-4,
      "%.10g sv=%.6g,%.6g,%.6g" % (SIGMA_MIN, SVALS[0], SVALS[1], SVALS[2]), "> 1e-4")

_row13, _row19 = JAC[1], JAC[2]
DEV_1319 = float(1.0 - float(np.dot(_row13, _row19))
                 / (float(np.linalg.norm(_row13)) * float(np.linalg.norm(_row19))))
check("e2b_rows_1319_collinear", DEV_1319 < 5.0e-3, "%.6e" % DEV_1319, "< 5.0e-3")

NEARNULL = np.linalg.svd(JAC)[2][int(np.argmin(SVALS))]
check("e2c_nearnull_outside_cone",
      float(NEARNULL.min()) < -0.05 and float(NEARNULL.max()) > 0.05,
      "%.6g,%.6g,%.6g" % tuple(float(v) for v in NEARNULL), "mixed sign")

CONIC_STEPS = 400


def conic_value(uf: float, ub: float) -> float:
    """max_L |(J u)_L| at the simplex point u = (uf, ub, 1 - uf - ub)."""
    return float(np.max(np.abs(JAC @ np.array([uf, ub, 1.0 - uf - ub]))))


_gi, _gj = np.meshgrid(np.arange(CONIC_STEPS + 1), np.arange(CONIC_STEPS + 1),
                       indexing="ij")
_keep = (_gi + _gj) <= CONIC_STEPS
_uf = _gi[_keep] / float(CONIC_STEPS)
_ub = _gj[_keep] / float(CONIC_STEPS)
_cvals = np.max(np.abs(np.stack([_uf, _ub, 1.0 - _uf - _ub], axis=1) @ JAC.T), axis=1)
_cbest = int(np.argmin(_cvals))
_su = [float(_uf[_cbest]), float(_ub[_cbest])]
CONIC_SEARCH = float(_cvals[_cbest])
_cstep = 1.0 / CONIC_STEPS
while _cstep >= 1.0e-6:
    _moved = None
    for _axis in range(2):
        for _sign in (1.0, -1.0):
            _p = list(_su)
            _p[_axis] += _sign * _cstep
            _p[0] = min(1.0, max(0.0, _p[0]))
            _p[1] = min(1.0 - _p[0], max(0.0, _p[1]))
            _val = conic_value(_p[0], _p[1])
            if _val < CONIC_SEARCH:
                CONIC_SEARCH, _moved = _val, _p
    if _moved is not None:
        _su = _moved
    else:
        _cstep *= 0.5

# max_L |(J u)_L| is convex and piecewise linear on the weight simplex, so the
# minimum of t subject to the nine half-planes below is attained at a basic
# vertex.  A coordinate pattern search can stall on a kink ridge and return a
# value above the true minimum, so the search above is kept only as an
# upper-bound cross-check and the reported minimum comes from a deterministic
# enumeration of every vertex (pure numpy on the 3x3 Jacobian).
_planes = []
for _a in range(3):
    _cf, _cb, _c0 = JAC[_a, 0] - JAC[_a, 2], JAC[_a, 1] - JAC[_a, 2], JAC[_a, 2]
    _planes.append(([_cf, _cb, -1.0], -_c0))
    _planes.append(([-_cf, -_cb, -1.0], _c0))
_planes.append(([-1.0, 0.0, 0.0], 0.0))
_planes.append(([0.0, -1.0, 0.0], 0.0))
_planes.append(([1.0, 1.0, 0.0], 1.0))
_pa = np.array([p[0] for p in _planes])
_pb = np.array([p[1] for p in _planes])
CONIC_MIN = float("inf")
CONIC_U = [0.0, 0.0]
for _tri in combinations(range(len(_planes)), 3):
    _rows = list(_tri)
    _sub = _pa[_rows]
    if abs(float(np.linalg.det(_sub))) < 1.0e-9:
        continue
    _x = np.linalg.solve(_sub, _pb[_rows])
    if float(np.max(_pa @ _x - _pb)) > 1.0e-9:
        continue
    _val = conic_value(float(_x[0]), float(_x[1]))
    if _val < CONIC_MIN:
        CONIC_MIN, CONIC_U = _val, [float(_x[0]), float(_x[1])]
CONIC_U2 = 1.0 - CONIC_U[0] - CONIC_U[1]
CONIC_UVEC = (CONIC_U[0], CONIC_U[1], CONIC_U2)
CONIC_MARGIN = CONIC_MIN / STATIC_ERR19
check("e2d_conic_linear_response_min",
      CONIC_MIN > THRESHOLD and min(CONIC_UVEC) >= -1.0e-9
      and CONIC_SEARCH >= CONIC_MIN - 1.0e-9
      and CONIC_SEARCH - CONIC_MIN <= 1.0 / CONIC_STEPS,
      "%.10g search=%.10g" % (CONIC_MIN, CONIC_SEARCH), "%.8g" % THRESHOLD)
emit("conic min=%.10g u=%.6g,%.6g,%.6g margin=%.6g"
     % (CONIC_MIN, CONIC_U[0], CONIC_U[1], CONIC_U2, CONIC_MARGIN))

SECANT_EPS = (1.0e-3, 1.0e-2, 5.0e-2, 0.1)


def face_secant(eps: float) -> float:
    """Signed box-19 secant of the ratio along the face-shell weight."""
    return (ratio(19, (eps, 0.0, 0.0)) - NN[19]) / eps


SECANTS = [face_secant(e) for e in SECANT_EPS]
_e3a_gap = abs(SECANTS[0] - JAC[2, 0])
check("e3a_secant_smalleps_matches_j", _e3a_gap <= 0.02 * abs(JAC[2, 0]),
      "%.12g vs %.12g rel=%.6g" % (SECANTS[0], JAC[2, 0], _e3a_gap / abs(JAC[2, 0])),
      "0.02")
check("e3b_secant_saturation_monotone",
      all(abs(SECANTS[i]) > abs(SECANTS[i + 1]) for i in range(3)),
      "%.6g,%.6g,%.6g,%.6g" % tuple(SECANTS), "strictly decreasing")

LANDED_FD = (LANDED_MUT19 - LANDED_NN[2]) / C700.FACE_MUTATION_WEIGHT
_e3c_gap = abs(SECANTS[3] - LANDED_FD)
check("e3c_landed_secant_wiring", _e3c_gap <= 1e-9, "%.3e" % _e3c_gap, "1e-9")
SAT_FACTOR = JAC[2, 0] / SECANTS[3]
emit("secant j19f=%.10g s0.1=%.12g landed=%.12g sat=%.6g"
     % (JAC[2, 0], SECANTS[3], LANDED_FD, SAT_FACTOR))

# ------------------------------------------------ block f: grid tournament -----
_grid_rows = []
_finite = 0
for _w in product(GRID_VALUES, repeat=3):
    if _w == W_ZERO:
        continue
    for _L in L_LADDER:
        if np.isfinite(ratio(_L, _w)):
            _finite += 1
    _grid_rows.append((separation(_w), _w))
_grid_rows.sort()
GRID_MIN, GRID_ARGMIN = _grid_rows[0]
GRID_MARGIN = GRID_MIN / STATIC_ERR19
PURE_QUARTER = [separation(w) for w in ((0.25, 0.0, 0.0), (0.0, 0.25, 0.0),
                                        (0.0, 0.0, 0.25))]
check("f1_grid_ratios_finite", _finite == 189, _finite, 189)
_recheck = max(abs(fresh_ratio(_L, GRID_ARGMIN) - NN[_L]) for _L in L_LADDER)
check("f2_grid_argmin_recheck", abs(_recheck - GRID_MIN) <= 1e-12,
      "%.3e" % abs(_recheck - GRID_MIN), "1e-12")
check("f3_grid_min_sep_over_threshold", GRID_MIN > THRESHOLD,
      "%.10g" % GRID_MIN, "%.10g" % THRESHOLD)
emit("grid min=%.10g at %s margin=%.6g pure25=%.6g,%.6g,%.6g"
     % (GRID_MIN, GRID_ARGMIN, GRID_MARGIN, PURE_QUARTER[0], PURE_QUARTER[1],
        PURE_QUARTER[2]))

# --------------------------------------------------- block g: ghost search -----
STARTS = [tuple(float(v) for v in w) for w in product((0.0, 1.0), repeat=3)
          if w != (0.0, 0.0, 0.0)]
STARTS += [(0.1, 0.0, 0.0), (0.25, 0.25, 0.25), (0.05, 0.05, 0.05), (0.01, 0.01, 0.01),
           tuple(float(v) for v in GRID_ARGMIN)]

BEST = None
START_OBJS = []
CAPPED = []
PROBES = 0
STARTS_DONE = 0
STARTS_SKIPPED = 0
for _si, _start in enumerate(STARTS):
    if perf_counter() - _STARTED > SEARCH_BUDGET_S:
        STARTS_SKIPPED = len(STARTS) - _si
        break
    _w = _start
    _cur = objective(_w)
    _step = SEARCH_STEP0
    _probes = 0
    _capped = False
    while _step >= SEARCH_STEP_STOP:
        _best_w, _best_v = None, _cur
        for _s in range(3):
            for _sign in (1.0, -1.0):
                _cand = list(_w)
                _cand[_s] = min(1.0, max(0.0, _cand[_s] + _sign * _step))
                _cand = tuple(_cand)
                if _cand[0] + _cand[1] + _cand[2] < L1_FLOOR:
                    continue
                _probes += 1
                _val = objective(_cand)
                if _val is not None and _val < _best_v:
                    _best_v, _best_w = _val, _cand
                if _probes >= SEARCH_PROBE_CAP:
                    break
            if _probes >= SEARCH_PROBE_CAP:
                break
        if _probes >= SEARCH_PROBE_CAP:
            _capped = True
            break
        if _best_w is not None:
            _w, _cur = _best_w, _best_v
        else:
            _step *= 0.5
    STARTS_DONE += 1
    PROBES += _probes
    START_OBJS.append(g12(_cur))
    if _capped:
        CAPPED.append(_si)
    if BEST is None or _cur < BEST[0]:
        BEST = (_cur, _w)

OBJ_MIN, W_STAR = BEST
SEP_STAR = separation(W_STAR)
check("g1_search_bookkeeping",
      STARTS_DONE + STARTS_SKIPPED == len(STARTS) and len(START_OBJS) == STARTS_DONE,
      "done=%d skipped=%d probes=%d capped=%s" % (STARTS_DONE, STARTS_SKIPPED, PROBES,
                                                  CAPPED),
      "12 starts accounted")
_g2_norm = W_STAR[0] + W_STAR[1] + W_STAR[2]
_g2_fresh = max(abs(fresh_ratio(_L, W_STAR) - NN[_L]) for _L in L_LADDER) / _g2_norm
check("g2_ghost_objective_recheck", abs(_g2_fresh - OBJ_MIN) <= 1e-12,
      "%.3e" % abs(_g2_fresh - OBJ_MIN), "1e-12")
check("g3_ghost_obj_min_over_threshold", OBJ_MIN > THRESHOLD,
      "%.10g" % OBJ_MIN, "%.10g" % THRESHOLD)

for _L in L_HOLDOUT:
    prepare(_L)
NN_HOLD = {L: ratio(L, W_ZERO) for L in L_HOLDOUT}
HOLD_STAR = max(abs(ratio(L, W_STAR) - NN_HOLD[L]) for L in L_HOLDOUT)
HOLD_GRID = max(abs(ratio(L, tuple(float(v) for v in GRID_ARGMIN)) - NN_HOLD[L])
                for L in L_HOLDOUT)
NN_HOLD_RESID = {L: abs(NN_HOLD[L] - R_PRED) for L in L_HOLDOUT}
check("g4_holdout_sep_over_threshold", HOLD_STAR > THRESHOLD,
      "%.10g" % HOLD_STAR, "%.10g" % THRESHOLD)
emit("ghost w*=%s obj=%.8g sep=%.8g hold*=%.8g holdgrid=%.8g"
     % (tuple(g12(v) for v in W_STAR), OBJ_MIN, SEP_STAR, HOLD_STAR, HOLD_GRID))
emit("nnholdout resid " + " ".join("%d:%.4g" % (L, NN_HOLD_RESID[L]) for L in L_HOLDOUT))

# ---------------------------------------------------- block h: discipline ------
ELAPSED = perf_counter() - _STARTED
check("h1_wall_time_budget", ELAPSED < WALL_BUDGET_S, "%.1f" % ELAPSED, WALL_BUDGET_S)

summary = {
    "cycle": 703,
    "anchors": {
        "nn_ladder": [NN[L] for L in L_LADDER],
        "pred": R_PRED,
        "pred_split": R_PRED_SPLIT,
        "mut19": R_MUT19,
        "sep": SEP_MUT,
        "staticerr19": STATIC_ERR19,
        "sep_ratio": SEP_RATIO,
        "threshold": g12(THRESHOLD),
    },
    "jacobian": [g12(JAC[i, j]) for i in range(3) for j in range(3)],
    "sigma_min": g12(SIGMA_MIN),
    "svals": [g12(v) for v in SVALS],
    "dev_1319": g12(DEV_1319),
    "nearnull": [g12(v) for v in NEARNULL],
    "conic": {"min": g12(CONIC_MIN), "margin": g12(CONIC_MARGIN),
              "search": g12(CONIC_SEARCH),
              "u": [g12(CONIC_U[0]), g12(CONIC_U[1]), g12(CONIC_U2)]},
    "secants": {"eps": list(SECANT_EPS), "s": [g12(v) for v in SECANTS]},
    "sat_factor": g12(SAT_FACTOR),
    "j19f": g12(JAC[2, 0]),
    "landed_fd": g12(LANDED_FD),
    "sigma_w": SIGMA_W,
    "grid": {
        "min_sep": g12(GRID_MIN),
        "argmin": list(GRID_ARGMIN),
        "margin": g12(GRID_MARGIN),
        "pure_quarter": [g12(v) for v in PURE_QUARTER],
        "ratios": _finite,
    },
    "ghost": {
        "w_star": [g12(v) for v in W_STAR],
        "obj_min": g12(OBJ_MIN),
        "sep_star": g12(SEP_STAR),
        "holdout_sep_star": g12(HOLD_STAR),
        "holdout_sep_grid": g12(HOLD_GRID),
        "starts_completed": STARTS_DONE,
        "starts_skipped": STARTS_SKIPPED,
        "probes": PROBES,
        "capped": CAPPED,
        "start_objs": START_OBJS,
    },
    "nn_holdout_residuals": {str(L): g12(NN_HOLD_RESID[L]) for L in L_HOLDOUT},
    "solves": SOLVE_COUNT[0],
    "elapsed_seconds": round(ELAPSED, 2),
}

prospective_pass = _PASS + 1
summary["pass"] = prospective_pass
summary["fail"] = _FAIL
summary_line = "SUMMARY_JSON " + json.dumps(summary, sort_keys=True, separators=(",", ":"))
total_line = "TOTAL: PASS=%d FAIL=%d" % (prospective_pass, _FAIL)
reserved = len("PASS h2_stdout_under_6000") + 1 + len(summary_line) + 1 + len(total_line) + 1
n_stdout = sum(len(s) + 1 for s in _OUT) + reserved
check("h2_stdout_under_6000", n_stdout < 6000, n_stdout, 6000)

summary["pass"] = _PASS
summary["fail"] = _FAIL
summary_line = "SUMMARY_JSON " + json.dumps(summary, sort_keys=True, separators=(",", ":"))
print("\n".join(_OUT))
print(summary_line)
print("TOTAL: PASS=%d FAIL=%d" % (_PASS, _FAIL))

if "--no-receipt" not in sys.argv:
    receipt_body = dict(summary)
    receipt_body["resources"] = {"elapsed_seconds": round(perf_counter() - _STARTED, 2)}
    receipt_body["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    receipt_body["pass_count"] = _PASS
    receipt_body["fail_count"] = _FAIL
    out_dir = ROOT / "outputs"
    out_dir.mkdir(exist_ok=True)
    target = out_dir / "physical_finite_range_law_tournament_cycle703_receipt_2026_08_01.json"
    target.write_text(json.dumps(receipt_body, indent=1, sort_keys=True, default=str) + "\n")

sys.exit(0 if _FAIL == 0 else 1)
