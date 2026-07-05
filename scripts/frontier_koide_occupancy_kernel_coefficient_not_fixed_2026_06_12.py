#!/usr/bin/env python3
"""Exact runner for the 2026-06-12 Koide occupancy-kernel bounded note."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md"
SUBSTEP1 = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
SUBSTEP2 = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md"

RESULTS: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((label, bool(ok), detail))


def simplify_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def monomial_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[tuple[int, ...] | None, int]:
    if set(left).intersection(right):
        return None, 0
    inversions = sum(1 for x in left for y in right if x > y)
    sign = -1 if inversions % 2 else 1
    return tuple(sorted(left + right)), sign


def poly_clean(poly: dict[tuple[int, ...], sp.Expr]) -> dict[tuple[int, ...], sp.Expr]:
    out: dict[tuple[int, ...], sp.Expr] = {}
    for mono, coeff in poly.items():
        coeff = sp.simplify(coeff)
        if coeff != 0:
            out[mono] = coeff
    return out


def poly_add(*polys: dict[tuple[int, ...], sp.Expr]) -> dict[tuple[int, ...], sp.Expr]:
    out: dict[tuple[int, ...], sp.Expr] = {}
    for poly in polys:
        for mono, coeff in poly.items():
            out[mono] = out.get(mono, sp.Integer(0)) + coeff
    return poly_clean(out)


def poly_scale(poly: dict[tuple[int, ...], sp.Expr], scalar: sp.Expr) -> dict[tuple[int, ...], sp.Expr]:
    return poly_clean({mono: scalar * coeff for mono, coeff in poly.items()})


def poly_mul(
    left: dict[tuple[int, ...], sp.Expr],
    right: dict[tuple[int, ...], sp.Expr],
) -> dict[tuple[int, ...], sp.Expr]:
    out: dict[tuple[int, ...], sp.Expr] = {}
    for mono_l, coeff_l in left.items():
        for mono_r, coeff_r in right.items():
            mono, sign = monomial_mul(mono_l, mono_r)
            if mono is None:
                continue
            out[mono] = out.get(mono, sp.Integer(0)) + sign * coeff_l * coeff_r
    return poly_clean(out)


def poly_pow(poly: dict[tuple[int, ...], sp.Expr], exponent: int) -> dict[tuple[int, ...], sp.Expr]:
    out: dict[tuple[int, ...], sp.Expr] = {(): sp.Integer(1)}
    for _ in range(exponent):
        out = poly_mul(out, poly)
    return out


def quadratic_action(matrix: sp.Matrix) -> dict[tuple[int, ...], sp.Expr]:
    n = matrix.rows
    terms: dict[tuple[int, ...], sp.Expr] = {}
    for i in range(n):
        for j in range(n):
            coeff = -matrix[i, j]
            if coeff != 0:
                terms[(i, n + j)] = terms.get((i, n + j), sp.Integer(0)) + coeff
    return poly_clean(terms)


def grassmann_exp(action: dict[tuple[int, ...], sp.Expr], n_pairs: int) -> dict[tuple[int, ...], sp.Expr]:
    out: dict[tuple[int, ...], sp.Expr] = {(): sp.Integer(1)}
    power: dict[tuple[int, ...], sp.Expr] = {(): sp.Integer(1)}
    for k in range(1, n_pairs + 1):
        power = poly_mul(power, action)
        out = poly_add(out, poly_scale(power, sp.Rational(1, math.factorial(k))))
    return out


def berezin_partition(matrix: sp.Matrix) -> tuple[sp.Expr, dict[tuple[int, ...], sp.Expr]]:
    n = matrix.rows
    action = quadratic_action(matrix)
    expanded = grassmann_exp(action, n)
    top_monomial = tuple(range(2 * n))
    top_coeff = expanded.get(top_monomial, sp.Integer(0))
    orientation = -1 if (n * (n + 1) // 2) % 2 else 1
    return sp.simplify(orientation * top_coeff), expanded


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
    return -1 if inversions % 2 else 1


def determinant_by_permutations(matrix: sp.Matrix) -> sp.Expr:
    n = matrix.rows
    total = sp.Integer(0)
    for perm in itertools.permutations(range(n)):
        term = sp.Integer(permutation_sign(perm))
        for i, j in enumerate(perm):
            term *= matrix[i, j]
        total += term
    return sp.simplify(total)


def all_matrix_zero(matrix: sp.Matrix) -> bool:
    return all(simplify_zero(entry) for entry in matrix)


# A-class: symbolic Berezin expansion and kernel freedom.
a00, a01, a10, a11 = sp.symbols("a00 a01 a10 a11")
M2 = sp.Matrix([[a00, a01], [a10, a11]])
Z2, E2 = berezin_partition(M2)
expected2 = determinant_by_permutations(M2)
check(
    "Berezin determinant identity: symbolic 2x2 expansion extracts the determinant polynomial",
    simplify_zero(Z2 - expected2)
    and expected2 == a00 * a11 - a01 * a10
    and tuple(range(4)) in E2,
)

m = sp.symbols("m00 m01 m02 m10 m11 m12 m20 m21 m22")
M3 = sp.Matrix(3, 3, m)
Z3, E3 = berezin_partition(M3)
expected3 = determinant_by_permutations(M3)
check(
    "Berezin determinant identity: symbolic 3x3 expansion gives the six-term permutation formula",
    simplify_zero(Z3 - expected3)
    and len(list(itertools.permutations(range(3)))) == 6
    and tuple(range(6)) in E3,
)

s, d00, d01, d10, d11 = sp.symbols("s d00 d01 d10 d11")
M_block = sp.Matrix([[s, 0, 0], [0, d00, d01], [0, d10, d11]])
Z_block, _ = berezin_partition(M_block)
doublet_det = determinant_by_permutations(sp.Matrix([[d00, d01], [d10, d11]]))
check(
    "Kernel-coefficient witness: block-diagonal singlet plus doublet factorizes from the expansion",
    simplify_zero(Z_block - s * doublet_det),
)

lam, q = sp.symbols("lambda q", positive=True)
M_doublet = sp.Matrix([[d00, d01], [d10, d11]])
Z_doublet, _ = berezin_partition(M_doublet)
Z_doublet_scaled, _ = berezin_partition(lam * M_doublet)
Z_pair, _ = berezin_partition(sp.Matrix([[q]]))
Z_pair_scaled, _ = berezin_partition(sp.Matrix([[lam * q]]))
check(
    "Kernel-coefficient witness: doublet rank-2 scaling is lambda^2 and paired rank-1 scaling is lambda",
    simplify_zero(Z_doublet_scaled - lam**2 * Z_doublet)
    and simplify_zero(Z_pair_scaled - lam * Z_pair),
)

action_scaled = quadratic_action(lam * M_doublet)
check(
    "Kernel-coefficient witness: Grassmann nilpotency and dimension are preserved under lambda scaling",
    len(action_scaled) == 4 and poly_pow(action_scaled, 3) == {},
)

A, B, delta = sp.symbols("A B delta")
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
h1 = A + B * sp.exp(sp.I * delta) * omega + B * sp.exp(-sp.I * delta) * omega**2
h2 = A + B * sp.exp(sp.I * delta) * omega**2 + B * sp.exp(-sp.I * delta) * omega
M_circulant_doublet = sp.Matrix([[h1, 0], [0, h2]])
rotation_doublet = sp.Matrix([[omega, 0], [0, omega**2]])
check(
    "Kernel-coefficient witness: supplied circulant class remains C3-equivariant after lambda scaling",
    all_matrix_zero(M_circulant_doublet * rotation_doublet - rotation_doublet * M_circulant_doublet)
    and all_matrix_zero((lam * M_circulant_doublet) * rotation_doublet - rotation_doublet * (lam * M_circulant_doublet)),
)

g = sp.symbols("g", positive=True)
base_weight = sp.pi / g
Z_cells = [2 * sp.pi / g, sp.pi / g]
rho_cells = [sp.simplify(base_weight / z) for z in Z_cells]
r_cells = [sp.simplify(1 / (2 * rho)) for rho in rho_cells]
rank1_lambdas = [sp.simplify(z / base_weight) for z in Z_cells]
rank2_lambdas = [sp.sqrt(sp.simplify(z / base_weight)) for z in Z_cells]
check(
    "Occupancy-atom localization: lambda freedom realizes both Z_d weight cells under the rho map",
    rho_cells == [sp.Rational(1, 2), sp.Integer(1)]
    and r_cells == [sp.Integer(1), sp.Rational(1, 2)]
    and rank1_lambdas == [sp.Integer(2), sp.Integer(1)]
    and rank2_lambdas == [sp.sqrt(2), sp.Integer(1)],
)

check(
    "Occupancy-atom localization: no check pins r; lambda-free admissible r set is the full binary",
    set(r_cells) == {sp.Integer(1), sp.Rational(1, 2)},
)

# B-class: retained source greps and note consistency.
substep1 = SUBSTEP1.read_text(encoding="utf-8")
substep2 = SUBSTEP2.read_text(encoding="utf-8")
note = NOTE.read_text(encoding="utf-8")
flat1 = re.sub(r"\s+", " ", substep1)
flat2 = re.sub(r"\s+", " ", substep2)

check(
    "Source boundary: substep1 carries evaluates-exactly/det/unique-surviving/single-pair text",
    all(fragment in flat1 for fragment in ["evaluates exactly to", "det(M)", "unique surviving", "single-pair"]),
)

check(
    "Source boundary: substep2 carries the no-physical-identification sentence fragment",
    "make **no** claim that the framework's physical dynamical staggered-Dirac operator" in flat2,
)

absent_fragments = [
    "transfer matrix",
    "transfer-matrix",
    "reflection positivity",
    "reflection-positivity",
    "time direction",
]
source_lower = (substep1 + "\n" + substep2).lower()
check(
    "Source boundary: retained notes do not supply transfer/time/reflection-positivity strings",
    all(fragment not in source_lower for fragment in absent_fragments),
)

note_lower = note.lower()
check(
    "Note hygiene: supplied-circulant/prerequisite/live-route language appears without closing phrases",
    "supplied circulant class" in note
    and "route is live" in note_lower
    and "prerequisite" in note_lower
    and all(
        forbidden not in note_lower
        for forbidden in ["closes " + "the route", "only " + "route", "ex" + "hausted"]
    ),
)

check(
    "Note hygiene: firewall keeps the occupancy binary open and avoids the forbidden r-forcing phrase",
    "the occupancy binary stays open" in note_lower and ("forces r" + " = 1/2") not in note_lower,
)

md_links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", note)
context_names = [
    "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
    "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md",
]
context_ok = True
for context_name in context_names:
    context_ok = context_ok and f"`{context_name}`" in note
    context_ok = context_ok and f"]({context_name})" not in note
    for match in re.finditer(re.escape(context_name), note):
        start, end = match.span()
        context_ok = context_ok and start > 0 and end < len(note) and note[start - 1] == "`" and note[end] == "`"
resolved = [(NOTE.parent / link).resolve().exists() for link in md_links]
check(
    "Note hygiene: link inventory has exactly two load-bearing markdown note links and backticked context names",
    len(md_links) == 2 and all(resolved) and context_ok,
)

check(
    "Note hygiene: no-promotion statement is present",
    "**No-promotion statement:**" in note,
)

script_text = Path(__file__).read_text(encoding="utf-8")
forbidden_det_call = "." + "det("
check(
    "Runner hygiene: explicit expansion path is used and no matrix-det call substitutes for the determinant identity",
    "grassmann_exp" in script_text
    and "top_monomial" in script_text
    and forbidden_det_call not in script_text,
)


passed = sum(1 for _, ok, _ in RESULTS if ok)
failed = sum(1 for _, ok, _ in RESULTS if not ok)

for label, ok, detail in RESULTS:
    suffix = f" :: {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} - {label}{suffix}")

print(f"SUMMARY: PASS={passed} FAIL={failed}")
if failed:
    raise SystemExit(1)
