#!/usr/bin/env python3
"""Exact audit companion for the abstract bilinear continuity theorem.

This runner intentionally avoids the staggered/Kawamoto-Smit carrier and any
physical density bridge. It checks only finite matrix-unit algebra:

    [E_ij, E_pq] = delta_jp E_iq - delta_qi E_pj

and the resulting symbolic continuity equation for an arbitrary
number-conserving bilinear H = sum c_ij E_ij.
"""

from __future__ import annotations

from itertools import product
import sys

import sympy as sp


RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")


def matrix_unit(n: int, i: int, j: int) -> sp.Matrix:
    m = sp.zeros(n, n)
    m[i, j] = 1
    return m


def bil_commutator(a: dict[tuple[int, int], sp.Expr], b: dict[tuple[int, int], sp.Expr]) -> dict[tuple[int, int], sp.Expr]:
    out: dict[tuple[int, int], sp.Expr] = {}
    for (i, j), x in a.items():
        for (p, q), y in b.items():
            if j == p:
                out[(i, q)] = out.get((i, q), 0) + x * y
            if q == i:
                out[(p, j)] = out.get((p, j), 0) - x * y
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


def dict_diff(a: dict[tuple[int, int], sp.Expr], b: dict[tuple[int, int], sp.Expr]) -> dict[tuple[int, int], sp.Expr]:
    keys = set(a) | set(b)
    return {k: sp.simplify(a.get(k, 0) - b.get(k, 0)) for k in keys if sp.simplify(a.get(k, 0) - b.get(k, 0)) != 0}


def negate(a: dict[tuple[int, int], sp.Expr]) -> dict[tuple[int, int], sp.Expr]:
    return {k: -v for k, v in a.items()}


def add_into(target: dict[tuple[int, int], sp.Expr], source: dict[tuple[int, int], sp.Expr]) -> None:
    for k, v in source.items():
        target[k] = sp.simplify(target.get(k, 0) + v)
        if target[k] == 0:
            del target[k]


def part_0_matrix_units() -> None:
    print("\n[Part 0] matrix-unit commutator identity")
    n = 4
    ok = True
    max_nonzero = 0
    for i, j, p, q in product(range(n), repeat=4):
        lhs = matrix_unit(n, i, j) * matrix_unit(n, p, q) - matrix_unit(n, p, q) * matrix_unit(n, i, j)
        rhs = (matrix_unit(n, i, q) if j == p else sp.zeros(n, n)) - (
            matrix_unit(n, p, j) if q == i else sp.zeros(n, n)
        )
        diff = lhs - rhs
        if diff != sp.zeros(n, n):
            ok = False
            max_nonzero += 1
    record("[E_ij,E_pq] structure constants hold in concrete Mat_4", ok, f"bad_cells={max_nonzero}")


def symbolic_objects(n: int = 4):
    c = sp.IndexedBase("c")
    h = {(i, j): c[i, j] for i in range(n) for j in range(n)}
    q_global = {(p, p): sp.Integer(1) for p in range(n)}
    return c, h, q_global


def inflow_current(c: sp.IndexedBase, p: int, q: int) -> dict[tuple[int, int], sp.Expr]:
    if p == q:
        return {}
    return {
        (q, p): sp.I * c[q, p],
        (p, q): -sp.I * c[p, q],
    }


def part_1_symbolic_continuity() -> None:
    print("\n[Part 1] symbolic local continuity for arbitrary bilinear")
    n = 4
    c, h, q_global = symbolic_objects(n)

    hq = bil_commutator(h, q_global)
    record("global number charge Q commutes with arbitrary H", len(hq) == 0)

    all_local_ok = True
    all_div_ok = True
    nontrivial = False
    for p in range(n):
        rho_p = {(p, p): sp.Integer(1)}
        drho = {k: sp.I * v for k, v in bil_commutator(h, rho_p).items()}
        inflow: dict[tuple[int, int], sp.Expr] = {}
        for q in range(n):
            add_into(inflow, inflow_current(c, p, q))
        div_outflow = negate(inflow)
        if dict_diff(drho, inflow):
            all_local_ok = False
        if dict_diff(drho, negate(div_outflow)):
            all_div_ok = False
        nontrivial = nontrivial or bool(drho)
    record("i[H,rho_p] equals sum_q J_{p<-q} for every p", all_local_ok and nontrivial)
    record("d rho_p/dt + (div J)_p = 0 with outflow divergence", all_div_ok and nontrivial)

    total_drho: dict[tuple[int, int], sp.Expr] = {}
    for p in range(n):
        rho_p = {(p, p): sp.Integer(1)}
        add_into(total_drho, {k: sp.I * v for k, v in bil_commutator(h, rho_p).items()})
    record("sum_p d rho_p/dt vanishes exactly", len(total_drho) == 0)


def part_2_support_and_sign() -> None:
    print("\n[Part 2] support envelope, orientation, and sign teeth")
    n = 4
    c, h, _ = symbolic_objects(n)

    support_ok = True
    orientation_ok = True
    zero_pair_ok = True
    for p, q in product(range(n), repeat=2):
        if p == q:
            continue
        jpq = inflow_current(c, p, q)
        jqp = inflow_current(c, q, p)
        if dict_diff(jpq, negate(jqp)):
            orientation_ok = False
        allowed = {(p, q), (q, p)}
        for expr in jpq.values():
            for a, b in product(range(n), repeat=2):
                if (a, b) not in allowed and expr.has(c[a, b]):
                    support_ok = False
        zeroed = {c[p, q]: 0, c[q, p]: 0}
        if any(sp.simplify(expr.subs(zeroed)) != 0 for expr in jpq.values()):
            zero_pair_ok = False
    record("J_{p<-q} = -J_{q<-p} orientation antisymmetry", orientation_ok)
    record("pair current depends only on c_pq and c_qp", support_ok)
    record("pair current vanishes when c_pq=c_qp=0", zero_pair_ok)

    path_support_ok = True
    # Path graph 0-1-2-3: all non-edge currents must vanish after non-edge coefficients are zeroed.
    edges = {(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)}
    zero_non_edges = {c[a, b]: 0 for a, b in product(range(n), repeat=2) if a != b and (a, b) not in edges}
    for p, q in product(range(n), repeat=2):
        if p == q:
            continue
        current = inflow_current(c, p, q)
        is_edge = (p, q) in edges or (q, p) in edges
        if not is_edge and any(sp.simplify(expr.subs(zero_non_edges)) != 0 for expr in current.values()):
            path_support_ok = False
    record("finite graph coefficient support gives the same finite current support", path_support_ok)

    # Sign tooth: flipping the outflow divergence sign makes continuity fail for a generic p.
    p = 0
    rho_p = {(p, p): sp.Integer(1)}
    drho = {k: sp.I * v for k, v in bil_commutator(h, rho_p).items()}
    inflow: dict[tuple[int, int], sp.Expr] = {}
    for q in range(n):
        add_into(inflow, inflow_current(c, p, q))
    wrong_continuity = dict_diff(drho, negate(inflow))  # would require drho = -inflow
    record("flipped continuity sign fails generically", bool(wrong_continuity), f"nonzero_terms={len(wrong_continuity)}")


def part_3_diagonal_terms() -> None:
    print("\n[Part 3] diagonal terms do not create oriented currents")
    n = 4
    c, h, _ = symbolic_objects(n)
    diag_subs = {c[a, b]: 0 for a, b in product(range(n), repeat=2) if a != b}
    diag_ok = True
    for p in range(n):
        rho_p = {(p, p): sp.Integer(1)}
        drho = {k: sp.simplify(v.subs(diag_subs)) for k, v in {k: sp.I * v for k, v in bil_commutator(h, rho_p).items()}.items()}
        drho = {k: v for k, v in drho.items() if v != 0}
        if drho:
            diag_ok = False
    record("pure diagonal H gives d rho_p/dt = 0 for every p", diag_ok)


def main() -> int:
    print("=" * 78)
    print("Abstract bilinear continuity and support-envelope theorem")
    print("No staggered carrier, KS phase, physical density bridge, or external input.")
    print("=" * 78)
    part_0_matrix_units()
    part_1_symbolic_continuity()
    part_2_support_and_sign()
    part_3_diagonal_terms()

    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    n_fail = sum(1 for _, ok, _ in RESULTS if not ok)
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for name, ok, detail in RESULTS:
        suffix = f" ({detail})" if detail else ""
        print(f"  {'PASS' if ok else 'FAIL'} {name}{suffix}")
    print(f"\nTOTAL: {n_pass} PASS / {n_fail} FAIL")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
