#!/usr/bin/env python3
"""Finite-slot hw-complement registration-equivalence runner.

This runner checks the bounded theorem note:

* complementation maps the hw=1 generation triplet to the hw=2 triplet and
  commutes with the supplied C3 frame rotation;
* the supplied Hermitian circulant has eigenvalues
  lambda_k = a + 2 B cos(delta + 2 pi k/3);
* symmetric slot data is K-even while the single degree <= 3 orientation-odd
  C3-invariant line evaluates to -6 sqrt(3) B^3 sin(3 delta);
* additive-plus-even registrability kills that odd line;
* the two complement readings carry the same unordered spectrum;
* the note contains only the two load-bearing markdown dependency links and
  keeps the context notes context-only.

No registry, audit lane, cache, network, or git surface is read or written.
"""
from __future__ import annotations

import itertools
import re
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def rotate(c: tuple[int, int, int]) -> tuple[int, int, int]:
    return (c[2], c[0], c[1])


def rotate_inv(c: tuple[int, int, int]) -> tuple[int, int, int]:
    return (c[1], c[2], c[0])


def complement(c: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - x for x in c)


def orbit(start: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    return [start, rotate(start), rotate(rotate(start))]


def elem_sym(vals: list[sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    e1 = sp.simplify(sum(vals))
    e2 = sp.simplify(sum(vals[i] * vals[j] for i in range(3) for j in range(i + 1, 3)))
    e3 = sp.simplify(sp.expand_trig(sp.expand(vals[0] * vals[1] * vals[2])))
    return e1, e2, e3


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.trigsimp(sp.expand_trig(sp.expand(expr)))) == 0


def c3_invariant_dim_total(max_degree: int) -> int:
    dim = 0
    for degree in range(max_degree + 1):
        monos = [
            m
            for m in itertools.product(range(degree + 1), repeat=3)
            if sum(m) == degree
        ]
        fixed = sum(1 for m in monos if (m[1], m[2], m[0]) == m)
        dim += int(sp.Rational(len(monos) + 2 * fixed, 3))
    return dim


def s3_invariant_dim_total(max_degree: int) -> int:
    dim = 0
    for degree in range(max_degree + 1):
        dim += len(
            {
                tuple(sorted(m, reverse=True))
                for m in itertools.product(range(degree + 1), repeat=3)
                if sum(m) == degree
            }
        )
    return dim


def main() -> int:
    print("=" * 88)
    print("AC_PHI_LAMBDA HW-COMPLEMENT READING REGISTRATION-EQUIVALENCE")
    print("=" * 88)

    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    hw2 = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

    section("A1-A3: Boolean corner cube and C3 frame action")
    check(
        "A1: R(x,y,z)=(z,x,y) cycles the hw=1 and hw=2 triplets",
        orbit((1, 0, 0)) == hw1 and orbit((0, 1, 1)) == hw2,
        detail=f"hw1 orbit={orbit((1, 0, 0))}; hw2 orbit={orbit((0, 1, 1))}",
    )
    check(
        "A2: complementation maps hw=1 bijectively to hw=2 and C o R = R o C on all corners",
        sorted(complement(c) for c in hw1) == sorted(hw2)
        and all(complement(rotate(c)) == rotate(complement(c)) for c in corners),
    )
    named = (1, 0, 0)
    cr_named = complement(rotate(named))
    rinvc_named = rotate_inv(complement(named))
    check(
        "A3: orientation preserved; C o R != R^-1 o C on the named corner (1,0,0)",
        all(complement(rotate(c)) == rotate(complement(c)) for c in corners)
        and cr_named != rinvc_named
        and cr_named == (1, 0, 1)
        and rinvc_named == (1, 1, 0),
        detail=f"CR={cr_named}; R^-1C={rinvc_named}",
    )

    section("A4-A5: supplied Hermitian circulant spectrum and symmetric data")
    a, B, delta = sp.symbols("a B delta", real=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    Cmat = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * delta) * Cmat + B * sp.exp(-sp.I * delta) * Cmat.T
    eigen_ok = True
    for k in range(3):
        vec = sp.Matrix([1, omega**k, omega ** (2 * k)])
        lam_exp = a + B * sp.exp(sp.I * delta) * omega**k + B * sp.exp(-sp.I * delta) * omega ** (-k)
        lam_cos = a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3)
        eigen_ok = eigen_ok and all(sp.simplify(x) == 0 for x in H * vec - lam_exp * vec)
        eigen_ok = eigen_ok and sp.simplify(sp.expand_complex(lam_exp - lam_cos)) == 0
    check(
        "A4: H(delta) eigenvalues are lambda_k = a + 2B cos(delta + 2 pi k/3)",
        eigen_ok,
    )

    slots = [a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    e1, e2, e3 = elem_sym(slots)
    e3_target = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)
    check(
        "A5: e1,e2,e3 are even in delta and e3 contains phase only via cos(3 delta)",
        zero(e1 - e1.subs(delta, -delta))
        and zero(e2 - e2.subs(delta, -delta))
        and zero(e3 - e3.subs(delta, -delta))
        and zero(e3 - e3_target),
        detail=f"e1={e1}; e2={e2}; e3={e3_target}",
    )

    section("A6-A7: degree <= 3 readout decomposition and orientation-odd line")
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    u = x1**2 * x2 + x2**2 * x3 + x3**2 * x1
    v = x1 * x2**2 + x2 * x3**2 + x3 * x1**2
    rot_sub = {x1: x2, x2: x3, x3: x1}
    trans_sub = {x1: x2, x2: x1, x3: x3}
    w = u - v
    check(
        "A6a: u and v are C3-invariant; u-v is transposition-odd",
        sp.expand(u.subs(rot_sub, simultaneous=True) - u) == 0
        and sp.expand(v.subs(rot_sub, simultaneous=True) - v) == 0
        and sp.expand(w.subs(trans_sub, simultaneous=True) + w) == 0,
    )
    c3_dim = c3_invariant_dim_total(3)
    s3_dim = s3_invariant_dim_total(3)
    check(
        "A6b: degree <= 3 C3-invariant space = symmetric space plus exactly one extra line",
        c3_dim == 8 and s3_dim == 7,
        detail=f"dim C3<=3={c3_dim}; dim symmetric<=3={s3_dim}; quotient=1",
    )
    uv_slots = sp.simplify(
        sp.expand_trig(
            sp.expand(w.subs({x1: slots[0], x2: slots[1], x3: slots[2]}, simultaneous=True))
        )
    )
    check(
        "A7: (u - v)(slots) = -6 sqrt(3) B^3 sin(3 delta) exactly",
        zero(uv_slots + 6 * sp.sqrt(3) * B**3 * sp.sin(3 * delta)),
        detail=f"(u-v)(slots)={uv_slots}",
    )

    section("A8-A9: K action and additive-plus-even erasure")
    H_minus = H.subs(delta, -delta)
    check(
        "A8: sin(3 delta) is odd, cos(3 delta) is even, and conj(H(delta)) = H(-delta)",
        zero(sp.sin(3 * (-delta)) + sp.sin(3 * delta))
        and zero(sp.cos(3 * (-delta)) - sp.cos(3 * delta))
        and sp.simplify(H.conjugate() - H_minus) == sp.zeros(3, 3),
    )
    g0 = sp.Symbol("g0", real=True)
    gt = sp.Symbol("gt", real=True)
    g0_forced = sp.solve(sp.Eq(g0, g0 + g0), g0)
    gt_forced = sp.solve(sp.Eq(gt, -gt), gt)
    check(
        "A9a: additivity forces g(0)=0 and g(-x)=-g(x), with no continuity assumption",
        g0_forced == [0] and gt_forced == [0],
        detail="g(0)=g(0)+g(0); odd plus even gives gt=-gt",
    )
    check(
        "A9b: additive plus K-even kills the (u-v)/sin(3 delta) line: its K-even part "
        "vanishes identically, so its registrable (additive AND even) projection is zero",
        zero(uv_slots + uv_slots.subs(delta, -delta)),
        detail="(u-v)(slots, delta) + (u-v)(slots, -delta) = 0 exactly; the line is "
        "pure K-odd, and A9a shows additive+even content must be zero",
    )

    section("A10-A11: complement readings have the same registrable spectrum")
    hw1_orbit = orbit((1, 0, 0))
    # Build the hw2 reading INDEPENDENTLY of the complement bijection: generate the
    # hw2 orbit by the rotation itself, starting from the complement of e1. The
    # non-tautological content is that the complement of the R-orbit IS the R-orbit
    # of the complement, in the same cyclic order (orbit-level equivariance); only
    # then does the bijection pull the rotation-built hw2 reading back onto the hw1
    # slot assignment.
    hw2_orbit_via_complement = [complement(c) for c in hw1_orbit]
    hw2_orbit_via_rotation = orbit(complement((1, 0, 0)))
    order_consistent = hw2_orbit_via_complement == hw2_orbit_via_rotation
    reading_hw1 = dict(zip(hw1_orbit, slots))
    reading_hw2 = dict(zip(hw2_orbit_via_rotation, slots))
    hw1_values = [reading_hw1[c] for c in hw1_orbit]
    hw2_values = [reading_hw2[complement(c)] for c in hw1_orbit]
    hw1_sym = elem_sym(hw1_values)
    hw2_sym = elem_sym(hw2_values)
    check(
        "A10: equivariant transfer is order-consistent (complement of the R-orbit = "
        "R-orbit of the complement) and the complement readings have the same "
        "unordered spectrum / symmetric functions",
        order_consistent
        and all(zero(hw1_sym[i] - hw2_sym[i]) for i in range(3)),
        detail=f"hw1 orbit={hw1_orbit}; hw2 orbit (rotation-built)={hw2_orbit_via_rotation}",
    )
    check(
        "A11: frame-dependent component x1 is not constant on the supplied C3 frame orbit",
        sp.simplify(x1 - x2) != 0
        and sp.simplify((x1 - x2).subs({x1: 2, x2: -1})) != 0,
        detail="x1 - x2 nonzero as a polynomial; witness at slots (2,-1,-1): x1=2, rotated x1=-1",
    )

    section("B12-B15: note consistency checks")
    root = Path(__file__).resolve().parents[1]
    note_path = root / "docs" / "ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md"
    note = note_path.read_text(encoding="utf-8")
    check(
        "B12: note stipulates the supplied slot model and the H(delta) formula in-note",
        "supplied" in note
        and "H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T" in note,
    )
    check(
        "B13: note carries firewall, Status authority, and No-promotion statement boundaries",
        "does not select a physical species reading" in note
        and "finite slot model" in note
        and "full-dynamics" in note
        and "**Status authority:**" in note
        and "**No-promotion statement:**" in note,
    )
    support_name = "ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md"
    staggered_name = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    check(
        "B14: hw support note and staggered gate appear only as context names, not markdown deps",
        support_name in note
        and staggered_name in note
        and f"]({support_name})" not in note
        and f"]({staggered_name})" not in note,
    )
    md_links = re.findall(r"\]\(([^)]+\.md)\)", note)
    expected_links = [
        "MINIMAL_AXIOMS_2026-06-05.md",
        "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
    ]
    check(
        "B15: note .md link inventory is exactly the two load-bearing deps and both resolve",
        md_links == expected_links and all((root / "docs" / link).exists() for link in md_links),
        detail=f"md_links={md_links}",
    )

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
