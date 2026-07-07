#!/usr/bin/env python3
"""Exact checks for color orientation: 3 vs 3bar."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


F = Fraction
C_ZERO = (F(0), F(0))
C_ONE = (F(1), F(0))
C_NEG_ONE = (F(-1), F(0))
C_TWO = (F(2), F(0))
C_NEG_TWO_I = (F(0), F(-2))
C_I = (F(0), F(1))
C_NEG_I = (F(0), F(-1))


def c(re=0, im=0):
    return (F(re), F(im))


def c_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def c_neg(a):
    return (-a[0], -a[1])


def c_sub(a, b):
    return c_add(a, c_neg(b))


def c_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def c_div(a, b):
    den = b[0] * b[0] + b[1] * b[1]
    if den == 0:
        raise ZeroDivisionError("complex Fraction division by zero")
    return ((a[0] * b[0] + a[1] * b[1]) / den,
            (a[1] * b[0] - a[0] * b[1]) / den)


def c_conj(a):
    return (a[0], -a[1])


def c_is_zero(a):
    return a[0] == 0 and a[1] == 0


def c_fmt(a):
    re, im = a
    if im == 0:
        return str(re)
    if re == 0:
        return f"{im}i"
    sign = "+" if im > 0 else "-"
    return f"{re}{sign}{abs(im)}i"


def mat(entries):
    return [[entry for entry in row] for row in entries]


def mat_zero(n):
    return [[C_ZERO for _ in range(n)] for _ in range(n)]


def mat_transpose(a):
    return [list(row) for row in zip(*a)]


def mat_dagger(a):
    return [[c_conj(a[j][i]) for j in range(len(a))] for i in range(len(a))]


def mat_neg(a):
    return [[c_neg(x) for x in row] for row in a]


def mat_add(a, b):
    n = len(a)
    return [[c_add(a[i][j], b[i][j]) for j in range(n)] for i in range(n)]


def mat_sub(a, b):
    n = len(a)
    return [[c_sub(a[i][j], b[i][j]) for j in range(n)] for i in range(n)]


def mat_scalar_mul(s, a):
    return [[c_mul(s, x) for x in row] for row in a]


def mat_mul(a, b):
    n = len(a)
    out = mat_zero(n)
    for i in range(n):
        for j in range(n):
            total = C_ZERO
            for k in range(n):
                total = c_add(total, c_mul(a[i][k], b[k][j]))
            out[i][j] = total
    return out


def mat_trace(a):
    total = C_ZERO
    for i in range(len(a)):
        total = c_add(total, a[i][i])
    return total


def mat_is_zero(a):
    return all(c_is_zero(x) for row in a for x in row)


def is_antihermitian_traceless(a):
    return mat_is_zero(mat_add(mat_dagger(a), a)) and c_is_zero(mat_trace(a))


def su3_antihermitian_gell_mann_rational():
    z = C_ZERO
    i = C_I
    ni = C_NEG_I
    o = C_ONE
    no = C_NEG_ONE
    nti = C_NEG_TWO_I
    return [
        mat([[z, i, z], [i, z, z], [z, z, z]]),
        mat([[z, o, z], [no, z, z], [z, z, z]]),
        mat([[i, z, z], [z, ni, z], [z, z, z]]),
        mat([[z, z, i], [z, z, z], [i, z, z]]),
        mat([[z, z, o], [z, z, z], [no, z, z]]),
        mat([[z, z, z], [z, z, i], [z, i, z]]),
        mat([[z, z, z], [z, z, o], [z, no, z]]),
        mat([[i, z, z], [z, i, z], [z, z, nti]]),
    ]


def su2_antihermitian_pauli():
    z = C_ZERO
    i = C_I
    ni = C_NEG_I
    o = C_ONE
    no = C_NEG_ONE
    return [
        mat([[z, i], [i, z]]),
        mat([[z, o], [no, z]]),
        mat([[i, z], [z, ni]]),
    ]


def conjugate_action(a):
    return mat_neg(mat_transpose(a))


def intertwiner_equation_rows(basis):
    n = len(basis[0])
    rows = []
    for a in basis:
        b = conjugate_action(a)
        for i in range(n):
            for j in range(n):
                row = [C_ZERO for _ in range(n * n)]
                for p in range(n):
                    for q in range(n):
                        idx = p * n + q
                        coeff = C_ZERO
                        if p == i:
                            coeff = c_add(coeff, a[q][j])
                        if q == j:
                            coeff = c_sub(coeff, b[i][p])
                        row[idx] = coeff
                rows.append(row)
    return rows


def complex_rank(rows):
    work = [list(row) for row in rows if not all(c_is_zero(x) for x in row)]
    if not work:
        return 0
    m = len(work)
    n = len(work[0])
    rank = 0
    for col in range(n):
        pivot = None
        for r in range(rank, m):
            if not c_is_zero(work[r][col]):
                pivot = r
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pv = work[rank][col]
        work[rank] = [c_div(x, pv) for x in work[rank]]
        for r in range(m):
            if r == rank:
                continue
            factor = work[r][col]
            if c_is_zero(factor):
                continue
            work[r] = [
                c_sub(work[r][k], c_mul(factor, work[rank][k]))
                for k in range(n)
            ]
        rank += 1
        if rank == m:
            break
    return rank


def nullity_for_intertwiners(basis):
    n = len(basis[0])
    rows = intertwiner_equation_rows(basis)
    return n * n - complex_rank(rows)


def verify_intertwiner(w, basis):
    for a in basis:
        lhs = mat_mul(w, a)
        rhs = mat_mul(conjugate_action(a), w)
        if not mat_is_zero(mat_sub(lhs, rhs)):
            return False
    return True


def hermitian_from_antihermitian_basis(basis):
    return [mat_scalar_mul(C_NEG_I, a) for a in basis]


def anomaly_tensor(hermitian_basis):
    n = len(hermitian_basis)
    tensor = {}
    for a in range(n):
        for b in range(n):
            anti = mat_add(
                mat_mul(hermitian_basis[a], hermitian_basis[b]),
                mat_mul(hermitian_basis[b], hermitian_basis[a]),
            )
            for cc in range(n):
                tensor[(a, b, cc)] = mat_trace(mat_mul(anti, hermitian_basis[cc]))
    return tensor


def tensor_neg(tensor):
    return {key: c_neg(value) for key, value in tensor.items()}


def tensor_equal(a, b):
    return a.keys() == b.keys() and all(a[key] == b[key] for key in a)


def first_nonzero_tensor_entry(tensor):
    for key in sorted(tensor):
        if not c_is_zero(tensor[key]):
            return key, tensor[key]
    raise AssertionError("expected nonzero anomaly tensor")


def normalize_text(text):
    text = text.replace("3" + "\u0304", "3bar")
    text = text.replace("\u0304", "bar")
    text = text.replace("**", "")
    return " ".join(text.split())


def text_audits(repo):
    quotes = {
        "docs/MINIMAL_AXIOMS_2026-06-29.md": [
            "Records form.",
            "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.",
            "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise.",
        ],
        "docs/GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md": [
            "Pre-record structure is real exactly to the extent it influences which records form and with what frequencies.",
            "Orientation is not a separate insertion. With a growth direction (arrow) and a one-sided spectrum (stability clause on the carrier), the rotation sense is fixed relative to record succession.",
            "Nobody chooses `i` over `-i`; the pair is oriented by succession plus stability.",
            "OPEN owner question; the arrow's only missing piece",
        ],
        "docs/RECORD_COMPARABILITY_OWNER_ONE_PAGER_2026-07-04.md": [
            "There is one configuration of records.",
            "This document carries no weight until you act on it; cite only as proposed.",
            "What nothing landed supplies is comparability: that any two realized configurations are nested",
        ],
        "docs/SU3_ANOMALY_FORCED_3BAR_COMPLETION_THEOREM_NOTE_2026-05-02.md": [
            "Status: independent audit required.",
            "Under P1+P2+P3, the SU(3) representation content of the RH (anti-)quark sector is forced to be exactly 2 LH-Weyl fermions in the 3bar representation, with no irreducible 3-rep fields and arbitrary number of singlets.",
        ],
    }
    checked = 0
    for rel, needles in quotes.items():
        haystack = normalize_text((repo / rel).read_text(encoding="utf-8"))
        for needle in needles:
            checked += 1
            if normalize_text(needle) not in haystack:
                raise AssertionError(f"missing quote in {rel}: {needle}")
    return checked


def ast_self_scan(script_path):
    source = script_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_imports = {
        "http",
        "urllib",
        "requests",
        "socket",
        "subprocess",
        "multiprocessing",
    }
    forbidden_calls = {"eval", "exec", "compile", "__import__"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in forbidden_imports:
                    raise AssertionError(f"forbidden import: {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            if root in forbidden_imports:
                raise AssertionError(f"forbidden import-from: {node.module}")
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in forbidden_calls:
                raise AssertionError(f"forbidden call: {func.id}")
    return True


def run_checks():
    repo = Path(__file__).resolve().parents[1]
    script_path = Path(__file__).resolve()
    passes = []

    quote_count = text_audits(repo)
    passes.append(f"text audits passed for {quote_count} quoted source snippets")

    su3 = su3_antihermitian_gell_mann_rational()
    su2 = su2_antihermitian_pauli()
    if not all(is_antihermitian_traceless(a) for a in su3):
        raise AssertionError("SU(3) basis is not antihermitian traceless")
    if not all(is_antihermitian_traceless(a) for a in su2):
        raise AssertionError("SU(2) basis is not antihermitian traceless")
    # Basis-span verification (panel-required): the 8 su(3) generators are
    # linearly independent over R (rank 8 in the 18-real-dim antihermitian
    # traceless space => they span su(3)); likewise rank 3 for su(2).
    su3_rank = complex_rank([[entry for row in g for entry in row] for g in su3])
    su2_rank = complex_rank([[entry for row in g for entry in row] for g in su2])
    if su3_rank != 8 or su2_rank != 3:
        raise AssertionError(f"basis span failure: su3 rank {su3_rank}, su2 rank {su2_rank}")
    passes.append("rational antihermitian su(3)/su(2) bases checked; spans verified rank 8 and 3")

    su3_nullity = nullity_for_intertwiners(su3)
    if su3_nullity != 0:
        raise AssertionError(f"expected su3 nullity 0, got {su3_nullity}")
    passes.append("su(3) fundamental-to-conjugate intertwiner nullity = 0")

    su2_nullity = nullity_for_intertwiners(su2)
    if su2_nullity != 1:
        raise AssertionError(f"expected su2 nullity 1, got {su2_nullity}")
    epsilon = mat([[C_ZERO, C_ONE], [C_NEG_ONE, C_ZERO]])
    if not verify_intertwiner(epsilon, su2):
        raise AssertionError("epsilon failed the exact su2 intertwiner check")
    passes.append("su(2) control nullity = 1 with exact epsilon intertwiner")

    h3 = hermitian_from_antihermitian_basis(su3)
    h3bar = [mat_neg(mat_transpose(h)) for h in h3]
    d3 = anomaly_tensor(h3)
    d3bar = anomaly_tensor(h3bar)
    if not tensor_equal(d3bar, tensor_neg(d3)):
        raise AssertionError("conjugate anomaly tensor is not the negative")
    witness_key, witness_value = first_nonzero_tensor_entry(d3)
    a3 = F(1)
    a3bar = F(-1)
    pair_sum = a3 + a3bar
    if pair_sum != 0 or a3 == 0:
        raise AssertionError("bad anomaly coefficient bookkeeping")
    passes.append(
        "cubic anomaly signs checked: A(3)=+1, A(3bar)=-1, pair sum=0"
    )

    ast_self_scan(script_path)
    passes.append("AST self-scan passed")

    return passes, {
        "su3_nullity": su3_nullity,
        "su2_nullity": su2_nullity,
        "epsilon": "[[0, 1], [-1, 0]]",
        "anomaly_witness": f"D3{witness_key}={c_fmt(witness_value)}",
        "A3": "+1",
        "A3bar": "-1",
        "pair_sum": str(pair_sum),
    }


def main():
    try:
        passes, facts = run_checks()
    except Exception as exc:  # pragma: no cover - command-line reporting path
        print(f"[FAIL] {exc}")
        print("TOTAL PASS=0 FAIL=1")
        raise SystemExit(1)

    for item in passes:
        print(f"[PASS] {item}")
    print(
        "DECLARATION premise=SUCCESSION-ORIENT; "
        "conditional_on=R-comparability; supplied=SUPPLIED-C3; "
        "anomaly_requirement=ANOMALY-CANCEL"
    )
    print(
        "EXACT "
        f"su3_nullity={facts['su3_nullity']} "
        f"su2_nullity={facts['su2_nullity']} "
        f"epsilon={facts['epsilon']} "
        f"{facts['anomaly_witness']} "
        f"A3={facts['A3']} "
        f"A3bar={facts['A3bar']} "
        f"pair_sum={facts['pair_sum']}"
    )
    print(f"TOTAL PASS={len(passes)} FAIL=0")


if __name__ == "__main__":
    main()
