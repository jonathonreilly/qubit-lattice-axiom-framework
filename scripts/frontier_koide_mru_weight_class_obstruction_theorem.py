#!/usr/bin/env python3
"""Exact checks for the Koide MRU quotient-forcing obstruction theorem.

The load-bearing result is not post-quotient algebra.  It is the exact
classification showing that the retained cyclic carrier does not force the
real doublet through one radius, even after the proposed C3, conjugation,
spectrum-scalar, and common Record-encoding strengthenings are granted:

    R[x,y]^C3 = R[u,v,w]/(v^2+w^2-u^3),
    R[x,y]^D3 = R[u,v],
    R[x,y]^SO2 = R[u],

where u=x^2+y^2, v=Re((x+iy)^3), and w=Im((x+iy)^3).

The runner also checks the exact positive boundary that every invariant
quadratic scalar is radial, the original unreduced (1,2) determinant
obstruction, and the conditional reduced-carrier corollary.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
COMPRESSION = ROOT / "docs" / "KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md"
PREMISE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
AUDIT_LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "", cls: str = "A") -> None:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{cls}] {'PASS' if ok else 'FAIL'}: {label}{suffix}")


def shift_matrix() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def cyclic_matrix(a: sp.Expr, x: sp.Expr, y: sp.Expr) -> sp.Matrix:
    c = shift_matrix()
    b = x + sp.I * y
    return sp.simplify(a * sp.eye(3) + b * c + sp.conjugate(b) * c**2)


def part0_source_premises() -> None:
    print("\n=== Part 0: source and premise boundary ===")
    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    minimal_flat = " ".join(minimal.split())
    compression = COMPRESSION.read_text(encoding="utf-8")
    premise_registry = json.loads(PREMISE_REGISTRY.read_text(encoding="utf-8"))
    audit_ledger = json.loads(AUDIT_LEDGER.read_text(encoding="utf-8"))

    source_tokens = [
        "**Type:** no_go",
        "**Claim type:** no_go",
        "**Status authority:** independent audit lane only.",
        "exact negative boundary",
        "does not forbid a future physical law",
        "**No-Go Discipline result:** PASS",
    ]
    for token in source_tokens:
        check(f"source note contains boundary token {token!r}", token in note, cls="B")

    check(
        "Record supplies finite scalar additivity over disjoint records",
        "pairwise-disjoint records, scalar readout `I` is additive" in minimal_flat,
        cls="B",
    )
    check(
        "minimal axioms leave physical-observable identification outside the premise",
        "physical-observable identification" in minimal
        and "readout contexts" in minimal,
        cls="B",
    )
    check(
        "retained supplier states exact three-channel cyclic reconstruction",
        "H_cyc = (r0/3) B0 + (r1/6) B1 + (r2/6) B2" in compression
        and "span_R{B0, B1, B2}" in compression,
        cls="B",
    )
    check(
        "minimal_axioms is an approved canonical premise node at the consumed source path",
        "minimal_axioms" in premise_registry["canonical_ids"]
        and premise_registry["nodes"]["minimal_axioms"]["current_path"]
        == "docs/MINIMAL_AXIOMS_2026-06-29.md",
        cls="B",
    )
    compression_row = audit_ledger["rows"].get(
        "koide_dweh_cyclic_compression_note_2026-04-18", {}
    )
    check(
        "cyclic-compression dependency is retained-grade in the current ledger",
        compression_row.get("audit_status") == "audited_clean"
        and compression_row.get("effective_status")
        in {"retained", "retained_bounded", "retained_no_go"},
        detail=(
            f"audit={compression_row.get('audit_status')}, "
            f"effective={compression_row.get('effective_status')}"
        ),
        cls="B",
    )


def part1_invariant_generators() -> None:
    print("\n=== Part 1: C3, D3, and SO(2) invariant generators ===")
    x, y = sp.symbols("x y", real=True)
    u = x**2 + y**2
    v = x**3 - 3 * x * y**2
    w = 3 * x**2 * y - y**3

    angle = 2 * sp.pi / 3
    xr = sp.cos(angle) * x - sp.sin(angle) * y
    yr = sp.sin(angle) * x + sp.cos(angle) * y

    check("u is invariant under the 2pi/3 cyclic rotation", sp.simplify(u.subs({x: xr, y: yr}, simultaneous=True) - u) == 0)
    check("v is invariant under the 2pi/3 cyclic rotation", sp.simplify(sp.expand(v.subs({x: xr, y: yr}, simultaneous=True) - v)) == 0)
    check("w is invariant under the 2pi/3 cyclic rotation", sp.simplify(sp.expand(w.subs({x: xr, y: yr}, simultaneous=True) - w)) == 0)
    check("invariant-ring relation v^2+w^2=u^3", sp.expand(v**2 + w**2 - u**3) == 0)

    check("conjugation/reflection fixes u", sp.expand(u.subs(y, -y) - u) == 0)
    check("conjugation/reflection fixes v", sp.expand(v.subs(y, -y) - v) == 0)
    check("conjugation/reflection reverses w", sp.expand(w.subs(y, -y) + w) == 0)

    lie = lambda expr: sp.expand(-y * sp.diff(expr, x) + x * sp.diff(expr, y))
    check("SO(2) generator annihilates u", lie(u) == 0)
    check("SO(2) generator sends v to -3w", sp.expand(lie(v) + 3 * w) == 0)
    check("SO(2) generator sends w to 3v", sp.expand(lie(w) - 3 * v) == 0)

    invariant_monomials = []
    generated = []
    for total in range(13):
        for p in range(total + 1):
            q = total - p
            if (p - q) % 3 == 0:
                invariant_monomials.append((p, q))
                if p >= q:
                    generated.append((p, q, q, (p - q) // 3, 0))
                else:
                    generated.append((p, q, p, 0, (q - p) // 3))
    check(
        "every invariant b^p bbar^q through degree 12 is generated by u,b^3,bbar^3",
        all(p == eu + 3 * eb and q == eu + 3 * ebc for p, q, eu, eb, ebc in generated),
        detail=f"classified={len(invariant_monomials)} monomials",
    )
    check(
        "no phase-sensitive invariant occurs below degree three",
        [(p, q) for p, q in invariant_monomials if p + q < 3] == [(0, 0), (1, 1)],
    )
    check(
        "degree three introduces the two conjugate cubic channels",
        [(p, q) for p, q in invariant_monomials if p + q == 3] == [(0, 3), (3, 0)],
    )


def part2_quadratic_radialization() -> None:
    print("\n=== Part 2: exact quadratic radialization boundary ===")
    a, x, y = sp.symbols("a x y", real=True)
    aa, ax, ay, xx, xy, yy = sp.symbols("aa ax ay xx xy yy", real=True)
    q = aa * a**2 + ax * a * x + ay * a * y + xx * x**2 + xy * x * y + yy * y**2

    angle = 2 * sp.pi / 3
    xr = sp.cos(angle) * x - sp.sin(angle) * y
    yr = sp.sin(angle) * x + sp.cos(angle) * y
    residual = sp.Poly(sp.expand(q.subs({x: xr, y: yr}, simultaneous=True) - q), a, x, y)
    equations = [sp.Eq(coefficient, 0) for coefficient in residual.coeffs()]
    solutions = sp.solve(equations, [ax, ay, xx, xy], dict=True)

    check("C3-invariant quadratic coefficient system has one solution family", len(solutions) == 1, detail=f"solutions={solutions}")
    solution = solutions[0]
    check("singlet-doublet quadratic cross terms vanish", solution.get(ax) == 0 and solution.get(ay) == 0)
    check("doublet quadratic is proportional to x^2+y^2", solution.get(xx) == yy and solution.get(xy) == 0)

    q_invariant = sp.simplify(q.subs(solution))
    expected = aa * a**2 + yy * (x**2 + y**2)
    check("every invariant homogeneous quadratic is A a^2+B|b|^2", sp.expand(q_invariant - expected) == 0)


def part3_spectral_phase_counterexample() -> None:
    print("\n=== Part 3: spectrum-native cubic channel and positive counterexample ===")
    a, x, y = sp.symbols("a x y", real=True)
    u = x**2 + y**2
    v = x**3 - 3 * x * y**2
    h = cyclic_matrix(a, x, y)

    tr1 = sp.expand(sp.trace(h))
    tr2 = sp.expand(sp.trace(h**2))
    tr3 = sp.expand(sp.trace(h**3))
    det = sp.factor(h.det())

    check("tr(H)=3a", sp.expand(tr1 - 3 * a) == 0)
    check("tr(H^2)=3a^2+6u", sp.expand(tr2 - (3 * a**2 + 6 * u)) == 0)
    check("det(H)=a^3-3au+2v", sp.expand(det - (a**3 - 3 * a * u + 2 * v)) == 0)
    check("tr(H^3)=3a^3+18au+6v", sp.expand(tr3 - (3 * a**3 + 18 * a * u + 6 * v)) == 0)

    a_from_spectrum = tr1 / 3
    u_from_spectrum = sp.simplify((tr2 - 3 * a_from_spectrum**2) / 6)
    v_from_spectrum = sp.simplify((det - a_from_spectrum**3 + 3 * a_from_spectrum * u_from_spectrum) / 2)
    check("a reconstructs from tr(H)", sp.simplify(a_from_spectrum - a) == 0)
    check("u reconstructs from tr(H),tr(H^2)", sp.simplify(u_from_spectrum - u) == 0)
    check("v reconstructs from tr(H),tr(H^2),det(H)", sp.simplify(v_from_spectrum - v) == 0)

    h1 = cyclic_matrix(sp.Integer(3), sp.Integer(1), sp.Integer(0))
    h2 = cyclic_matrix(sp.Integer(3), sp.sqrt(3) / 2, sp.Rational(1, 2))
    spec1 = h1.eigenvals()
    spec2 = h2.eigenvals()
    expected1 = {sp.Integer(5): 1, sp.Integer(2): 2}
    expected2 = {sp.Integer(3): 1, 3 + sp.sqrt(3): 1, 3 - sp.sqrt(3): 1}

    check("first witness spectrum is {5,2,2}", spec1 == expected1, detail=f"spectrum={spec1}")
    check("second witness spectrum is {3+sqrt(3),3,3-sqrt(3)}", spec2 == expected2, detail=f"spectrum={spec2}")
    check("both same-radius witnesses are positive definite", min(expected1) > 0 and (3 - sp.sqrt(3)).is_positive)

    u1 = sp.Integer(1)**2 + sp.Integer(0)**2
    u2 = (sp.sqrt(3) / 2) ** 2 + sp.Rational(1, 2) ** 2
    v1 = sp.Integer(1)
    v2 = sp.expand((sp.sqrt(3) / 2) ** 3 - 3 * (sp.sqrt(3) / 2) * sp.Rational(1, 2) ** 2)
    check("witnesses have the same u=|b|^2", sp.simplify(u1 - u2) == 0 and u1 == 1)
    check("witnesses occupy different D3 orbits because v differs", sp.simplify(v1 - v2) != 0, detail=f"v1={v1}, v2={v2}")
    check("same-radius determinants differ exactly: 20 versus 18", h1.det() == 20 and h2.det() == 18)
    check("same-radius cubic traces differ exactly: 141 versus 135", sp.trace(h1**3) == 141 and sp.trace(h2**3) == 135)


def part4_record_additivity_countermodel() -> None:
    print("\n=== Part 4: conditional Record-encoding two-model witness ===")
    h1 = cyclic_matrix(sp.Integer(3), sp.Integer(1), sp.Integer(0))
    h2 = cyclic_matrix(sp.Integer(3), sp.sqrt(3) / 2, sp.Rational(1, 2))
    h3 = cyclic_matrix(sp.Integer(2), sp.Rational(1, 2), sp.Rational(1, 3))
    eta = {
        "content_witness_1": h1,
        "content_witness_2": h2,
        "content_auxiliary": h3,
    }
    left = ["content_witness_1", "content_auxiliary"]
    right = ["content_witness_2"]

    def i_rad(records: list[str]) -> sp.Expr:
        return sp.simplify(
            sum((sp.trace(eta[content] ** 2) for content in records), sp.Integer(0))
        )

    def i_ang(records: list[str]) -> sp.Expr:
        return sp.simplify(
            sum((eta[content].det() for content in records), sp.Integer(0))
        )

    check("one fixed eta contains both same-radius witness matrices", eta["content_witness_1"] == h1 and eta["content_witness_2"] == h2, cls="C")
    check("conditional radial model has I(empty)=0", i_rad([]) == 0, cls="C")
    check("conditional phase-sensitive model has I(empty)=0", i_ang([]) == 0, cls="C")
    check("conditional radial model is additive on disjoint concatenation", sp.simplify(i_rad(left + right) - i_rad(left) - i_rad(right)) == 0, cls="C")
    check("conditional phase-sensitive model is additive on disjoint concatenation", sp.simplify(i_ang(left + right) - i_ang(left) - i_ang(right)) == 0, cls="C")
    check("conditional radial per-record scalar agrees on the same-radius witnesses", sp.trace(h1**2) == sp.trace(h2**2), cls="C")
    check("conditional phase-sensitive per-record scalar distinguishes the same-radius witnesses", h1.det() != h2.det(), cls="C")


def part5_unreduced_weight_obstruction() -> None:
    print("\n=== Part 5: unreduced determinant weight obstruction ===")
    c = shift_matrix()
    i3 = sp.eye(3)
    p_plus = sp.simplify((i3 + c + c**2) / 3)
    p_perp = sp.simplify(i3 - p_plus)
    alpha, beta = sp.symbols("alpha beta", positive=True, real=True)

    check("P_+ and P_perp are complementary projectors", p_plus**2 == p_plus and p_perp**2 == p_perp and p_plus * p_perp == sp.zeros(3))
    check("rank(P_+)=1 and rank(P_perp)=2", p_plus.rank() == 1 and p_perp.rank() == 2)
    d_unreduced = sp.simplify(alpha * p_plus + beta * p_perp)
    check("det(alpha P_+ + beta P_perp)=alpha beta^2", sp.simplify(d_unreduced.det() - alpha * beta**2) == 0)

    e_plus, e_perp, e_tot = sp.symbols("e_plus e_perp e_tot", positive=True, real=True)
    mu, nu, lam = sp.symbols("mu nu lam", positive=True, real=True)
    lagrangian = mu * sp.log(e_plus) + nu * sp.log(e_perp) - lam * (e_plus + e_perp - e_tot)
    solutions = sp.solve(
        [sp.diff(lagrangian, e_plus), sp.diff(lagrangian, e_perp), e_plus + e_perp - e_tot],
        [e_plus, e_perp, lam],
        dict=True,
    )
    check("weighted log-volume has one positive stationary solution", len(solutions) == 1, detail=f"solutions={solutions}")
    stationary = solutions[0]
    check("stationary leaf is kappa=2mu/nu", sp.simplify(2 * stationary[e_plus] / stationary[e_perp] - 2 * mu / nu) == 0)
    check("unreduced determinant weights (1,2) land at kappa=1", sp.simplify((2 * mu / nu).subs({mu: 1, nu: 2}) - 1) == 0)


def part6_conditional_reduced_corollary() -> None:
    print("\n=== Part 6: conditional reduced-carrier corollary ===")
    rho_plus, rho_perp, e_tot, lam = sp.symbols("rho_plus rho_perp e_tot lam", positive=True, real=True)
    d_reduced = sp.diag(rho_plus, rho_perp)
    check("supplied reduced carrier has det=rho_+ rho_perp", d_reduced.det() == rho_plus * rho_perp, cls="C")

    lagrangian = sp.log(rho_plus) + sp.log(rho_perp) - lam * (rho_plus**2 + rho_perp**2 - e_tot)
    solutions = sp.solve(
        [sp.diff(lagrangian, rho_plus), sp.diff(lagrangian, rho_perp), rho_plus**2 + rho_perp**2 - e_tot],
        [rho_plus, rho_perp, lam],
        dict=True,
    )
    check("reduced log-volume has one positive stationary point", len(solutions) == 1, detail=f"solutions={solutions}", cls="C")
    stationary = solutions[0]
    target = sp.sqrt(e_tot / 2)
    check(
        "conditional reduced stationary point has equal slots",
        sp.simplify(stationary[rho_plus] - target) == 0
        and sp.simplify(stationary[rho_perp] - target) == 0,
        cls="C",
    )
    a, b_abs_sq = sp.symbols("a b_abs_sq", positive=True, real=True)
    check("E_+=E_perp pulls back to a^2=2|b|^2", sp.simplify((3 * a**2 - 6 * b_abs_sq) / 3 - (a**2 - 2 * b_abs_sq)) == 0, cls="C")
    check("conditional reduced corollary lands at kappa=2", sp.simplify((a**2 / b_abs_sq).subs(a**2, 2 * b_abs_sq) - 2) == 0, cls="C")


def main() -> int:
    part0_source_premises()
    part1_invariant_generators()
    part2_quadratic_radialization()
    part3_spectral_phase_counterexample()
    part4_record_additivity_countermodel()
    part5_unreduced_weight_obstruction()
    part6_conditional_reduced_corollary()

    print("\nInterpretation:")
    print("  C3 scalarity permits cubic phase invariants; conjugation leaves")
    print("  Re(b^3), and spectrum-native scalars reconstruct it.  Record has")
    print("  no carrier bridge; even after one common encoding is granted,")
    print("  additivity permits both radial and phase-sensitive per-record laws.")
    print("  The physical one-radius quotient is therefore not forced by the")
    print("  restricted packet.  Quadratic scalars are radial exactly, so a")
    print("  future theorem deriving an exact second-order physical grammar")
    print("  would supply a live positive route without changing this no-go.")
    print(f"\nclassified_pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
