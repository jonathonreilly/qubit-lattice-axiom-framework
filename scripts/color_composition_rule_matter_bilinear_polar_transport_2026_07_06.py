#!/usr/bin/env python3
from __future__ import annotations

import ast
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOC_ROUTING = ROOT / "docs" / "COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md"
DOC_NON_AUTONOMY = ROOT / "docs" / "INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md"


PASSES = 0
FAILS = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASSES, FAILS
    if condition:
        PASSES += 1
        suffix = f" {detail}" if detail else ""
        print(f"[PASS] {name}{suffix}")
    else:
        FAILS += 1
        suffix = f" {detail}" if detail else ""
        print(f"[FAIL] {name}{suffix}")


def F(n: int, d: int = 1) -> Fraction:
    return Fraction(n, d)


def matmul(a, b):
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def eye(n: int):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def diag(vals):
    n = len(vals)
    return [[vals[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def equal(a, b) -> bool:
    return a == b


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def rank_fraction(a) -> int:
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if m[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        pv = m[rank][col]
        m[rank] = [x / pv for x in m[rank]]
        for r in range(rows):
            if r != rank and m[r][col] != 0:
                factor = m[r][col]
                m[r] = [m[r][c] - factor * m[rank][c] for c in range(cols)]
        rank += 1
    return rank


def integer_cube_root(n: int):
    if n < 0:
        root = integer_cube_root(-n)
        return None if root is None else -root
    lo, hi = 0, max(1, n)
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid ** 3
        if cube == n:
            return mid
        if cube < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def is_perfect_cube_fraction(x: Fraction) -> bool:
    return integer_cube_root(x.numerator) is not None and integer_cube_root(x.denominator) is not None


def exact_witnesses():
    u0 = [
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(1), F(0), F(0)],
    ]
    d = diag([F(1), F(2), F(4)])
    m = matmul(u0, d)
    mtm = matmul(transpose(m), m)
    d2 = matmul(d, d)
    polar_ok = (
        equal(matmul(transpose(u0), u0), eye(3))
        and equal(mtm, d2)
        and equal(matmul(u0, d), m)
        and rank_fraction(m) == 3
    )
    check("exact_polar_witness_signed_perm_times_rational_diagonal", polar_ok, "rank=3 detD=8")

    gx = [
        [F(0), F(1), F(0)],
        [F(1), F(0), F(0)],
        [F(0), F(0), -F(1)],
    ]
    gy = [
        [F(1), F(0), F(0)],
        [F(0), F(0), F(1)],
        [F(0), -F(1), F(0)],
    ]
    mp = matmul(matmul(gy, m), transpose(gx))
    up = matmul(matmul(gy, u0), transpose(gx))
    pp = matmul(matmul(gx, d), transpose(gx))
    cov_ok = (
        equal(matmul(up, pp), mp)
        and equal(matmul(transpose(up), up), eye(3))
        and equal(matmul(transpose(mp), mp), matmul(pp, pp))
    )
    check("exact_covariance_signed_permutation_frames", cov_ok)

    # Determinant reduction applies to the POLAR UNITARY, not to D or M.
    # Witness 1: polar U of the main witness is u0 (even signed permutation),
    # det = +1 exactly -- the determinant-one branch is represented exactly.
    det_u = det3(u0)
    # Witness 2: an odd signed permutation u1 has det = -1; the rational cube
    # root r = -1 gives U_SU = -u1 with det(-u1) = (-1)^3 * (-1) = +1 exactly.
    # The other two cube roots of -1 are irrational (complex); the three
    # branches differ by cube roots of unity -- the Z_3 ambiguity, stated as
    # an algebraic fact and represented exactly on the rational branch.
    u1 = [
        [F(0), F(1), F(0)],
        [F(1), F(0), F(0)],
        [F(0), F(0), F(1)],
    ]
    det_u1 = det3(u1)
    u1_su = [[-x for x in row] for row in u1]
    z3_ok = (
        det_u == 1
        and det_u1 == -1
        and det3(u1_su) == 1
        and equal(matmul(transpose(u1_su), u1_su), eye(3))
    )
    check(
        "exact_det_and_z3_bookkeeping_on_polar_unitaries",
        z3_ok,
        "det(polarU)=1 exact; odd-permutation case det=-1 reduced exactly on "
        "the rational Z_3 branch; ambiguity = cube roots of unity",
    )

    gz = [
        [F(0), F(0), F(1)],
        [-F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
    ]
    uxy, uyz, uzx = u0, gx, gy
    f_x, f_y, f_z = gx, gy, gz
    uxy_p = matmul(matmul(f_y, uxy), transpose(f_x))
    uyz_p = matmul(matmul(f_z, uyz), transpose(f_y))
    uzx_p = matmul(matmul(f_x, uzx), transpose(f_z))
    w = trace(matmul(matmul(uzx, uyz), uxy))
    wp = trace(matmul(matmul(uzx_p, uyz_p), uxy_p))
    check("exact_path_ordered_wilson_invariance", w == wp, f"W={w}")

    rank_def = diag([F(1), F(2), F(0)])

    def exact_diagonal_polar(dmat):
        # For a diagonal real matrix, M = U P with P = |diag| and
        # U = diag(sign) exactly (signs of nonzero entries).
        n = len(dmat)
        u_fac = [[F(0)] * n for _ in range(n)]
        p_fac = [[F(0)] * n for _ in range(n)]
        for i in range(n):
            entry = dmat[i][i]
            if entry == 0:
                return None, None
            sgn = F(1) if entry > 0 else -F(1)
            u_fac[i][i] = sgn
            p_fac[i][i] = abs(entry)
        return u_fac, p_fac

    # COMPUTED polar factors (not hard-coded) at shrinking rational epsilon:
    # the +eps family's polar unitary is I for every eps; the -eps family's
    # is diag(1,1,-1) for every eps; the two constant families disagree, so
    # no single continuous unitary extension exists at the rank-2 limit
    # along these paths.
    limit_ok = True
    for k in (2, 4, 8, 64):
        eps = F(1, k)
        u_plus, p_plus = exact_diagonal_polar(diag([F(1), F(1), eps]))
        u_minus, p_minus = exact_diagonal_polar(diag([F(1), F(1), -eps]))
        if u_plus is None or u_minus is None:
            limit_ok = False
            break
        if not (equal(u_plus, eye(3)) and equal(u_minus, diag([F(1), F(1), -F(1)]))):
            limit_ok = False
            break
        if not (equal(matmul(u_plus, p_plus), diag([F(1), F(1), eps]))
                and equal(matmul(u_minus, p_minus), diag([F(1), F(1), -eps]))):
            limit_ok = False
            break
    rank_ok = (
        rank_fraction(m) == 3
        and rank_fraction(rank_def) == 2
        and limit_ok
    )
    check(
        "exact_rank_exhibits_and_boundary_discontinuity",
        rank_ok,
        "polar factors COMPUTED exactly at eps=1/2,1/4,1/8,1/64: constant I "
        "vs constant diag(1,1,-1); divergent at the rank-2 limit",
    )

    return u0, d


def random_unitary(rng):
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    return q * phases


def random_full_rank_matrix(rng):
    for _ in range(100):
        m = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        m = m + 0.75 * np.eye(3)
        s = np.linalg.svd(m, compute_uv=False)
        if s[-1] > 0.15:
            return m, s[-1]
    raise RuntimeError("could not draw a matrix with the requested gap")


def polar_np(m):
    left, s, vh = np.linalg.svd(m)
    u = left @ vh
    p = vh.conj().T @ np.diag(s) @ vh
    return u, p, s


def numeric_controls():
    rng = np.random.default_rng(20260706)
    max_cov = 0.0
    min_gap = 10.0
    for _ in range(16):
        m, gap = random_full_rank_matrix(rng)
        gx = random_unitary(rng)
        gy = random_unitary(rng)
        u, p, s = polar_np(m)
        mp = gy @ m @ gx.conj().T
        up, pp, sp = polar_np(mp)
        max_cov = max(
            max_cov,
            np.linalg.norm(up - gy @ u @ gx.conj().T),
            np.linalg.norm(pp - gx @ p @ gx.conj().T),
            abs(abs(np.linalg.det(u)) - 1.0),
        )
        min_gap = min(min_gap, gap, s[-1], sp[-1])
    check("seeded_numeric_covariance_controls", max_cov < 1e-10 and min_gap > 0.15, f"max_dev={max_cov:.2e} min_gap={min_gap:.2e}")

    links = [random_full_rank_matrix(rng)[0] for _ in range(3)]
    gaps = []
    us = []
    for link in links:
        u, _p, s = polar_np(link)
        us.append(u)
        gaps.append(s[-1])
    uxy, uyz, uzx = us
    gx, gy, gz = random_unitary(rng), random_unitary(rng), random_unitary(rng)
    uxy_p = gy @ uxy @ gx.conj().T
    uyz_p = gz @ uyz @ gy.conj().T
    uzx_p = gx @ uzx @ gz.conj().T
    w = np.trace(uzx @ uyz @ uxy)
    wp = np.trace(uzx_p @ uyz_p @ uxy_p)
    wilson_dev = abs(w - wp)
    check("seeded_numeric_wilson_invariance", wilson_dev < 1e-10 and min(gaps) > 0.15, f"dev={wilson_dev:.2e} min_gap={min(gaps):.2e}")


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def text_audits():
    routing_quotes = [
        "**Precondition (load-bearing):** the construction is defined **only when the cross-site bilinear is full rank**.",
        "Full rank still requires three independent occupied color directions.",
        "This is a *kinematic* carrier/routing existence result.",
    ]
    non_autonomy_quotes = [
        "The non-autonomy exhibit is a bounded route constraint, not a no-go against all gauge dynamics.",
        "Alternative routes left open: carry `(U_eff,Q)` or `M` rather than `U_eff` alone; restrict to the minimal-occupancy sector; seek coarse-grained slaving of hidden data; use non-quadratic or record-coupled matter dynamics; use a different compression or connection-level variable.",
    ]
    routing_text = normalize_text(DOC_ROUTING.read_text(encoding="utf-8"))
    non_text = normalize_text(DOC_NON_AUTONOMY.read_text(encoding="utf-8"))
    routing_ok = all(normalize_text(q) in routing_text for q in routing_quotes)
    non_ok = all(normalize_text(q) in non_text for q in non_autonomy_quotes)
    check("text_audit_june8_routing_quotes", routing_ok, f"quotes={len(routing_quotes)}")
    check("text_audit_june8_non_autonomy_quotes", non_ok, f"quotes={len(non_autonomy_quotes)}")


def ast_self_scan():
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_imports = {"os", "subprocess", "socket", "requests", "urllib", "http", "ftplib"}
    forbidden_calls = {"eval", "exec", "compile", "__import__"}
    imported = set()
    called = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                called.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                called.add(node.func.attr)
    ok = not (imported & forbidden_imports) and not (called & forbidden_calls)
    check("ast_self_scan_no_network_no_subprocess", ok)


def main() -> int:
    exact_witnesses()
    numeric_controls()
    text_audits()
    ast_self_scan()
    print("DECLARATION premise=SUPPLIED-C3; untouched_walls=ST1/ST2_generator_rate_action,graded_constraint_port3_port4; no_dynamics_no_weights_no_probabilities")
    print("EXACT polar_witness=Fractions signed_permutation_x_diag; covariance=signed_permutation_frames; wilson=path_ordered_trace")
    print(f"TOTAL PASS={PASSES} FAIL={FAILS}")
    return 0 if FAILS == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
