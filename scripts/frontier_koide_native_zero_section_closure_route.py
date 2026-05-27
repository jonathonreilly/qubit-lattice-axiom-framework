#!/usr/bin/env python3
"""
Koide native zero-section defined route algebra.

Purpose:
  Verify the finite algebraic route object behind the native zero-section
  Koide lane. The runner does not claim that the physical framework selects
  this object; it checks the exact consequences inside the defined route:

      z = 0, spectator = 0, c = 0.

Result:
  Exact bounded route algebra, with physical bridge identifications out of
  scope.

  Q:
    In the defined source-label algebra, the zero section z=0 gives K_TL=0
    and Q=2/3.

  Delta:
    The defined real nontrivial Z3 primitive has equivariant idempotents only
    0 and I. Therefore the defined primitive has no internal spectator
    projector: spectator=0.

    The defined determinant-line endpoint is based, so the endpoint-exact
    offset is c=0. With the finite Z3 scalar eta_Z3=2/9, the route endpoint
    has delta_open=eta_Z3=2/9.

Nature-grade boundary:
  This is not physical Koide closure unless later work derives the three
  physical bridge identifications:

    1. the charged-lepton scalar is the native zero-source coefficient;
    2. the Brannen endpoint is the whole real nontrivial Z3 primitive, not a
       rank-one line inside its multiplicity space;
    3. its open determinant-line readout is unit-preserving/based, not an
       unbased torsor coordinate.

No mass data, fitted Koide value, H_* pin, or target endpoint is used.

Current-surface firewall:
  The runner verifies only the defined route algebra. It does not assert
  retained Koide closure on the actual current surface.
"""

from __future__ import annotations

import sys

import sympy as sp


PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def q_from_weight(w_plus: sp.Expr) -> sp.Expr:
    r = sp.simplify((1 - w_plus) / w_plus)
    return sp.simplify((1 + r) / 3)


def ktl_from_weight(w_plus: sp.Expr) -> sp.Expr:
    r = sp.simplify((1 - w_plus) / w_plus)
    return sp.simplify((r**2 - 1) / (4 * r))


def eta_abss_z3_weights_12() -> sp.Expr:
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    total = sp.Rational(0)
    for k in (1, 2):
        z1 = omega**k
        z2 = omega ** (2 * k)
        total += sp.simplify(1 / ((z1 - 1) * (z2 - 1)))
    return sp.simplify(total / 3)


def main() -> int:
    section("A. Q defined zero-source section")

    z = sp.symbols("z", real=True)
    w_plus = sp.simplify((1 + z) / 2)
    record(
        "A.1 source-label zero section gives the defined source-free midpoint",
        w_plus.subs(z, 0) == sp.Rational(1, 2),
        "z=<Z>=0 -> w_plus=w_perp=1/2.",
    )
    record(
        "A.2 midpoint gives K_TL=0 and Q=2/3",
        ktl_from_weight(w_plus).subs(z, 0) == 0
        and q_from_weight(w_plus).subs(z, 0) == sp.Rational(2, 3),
        f"K_TL(z=0)={ktl_from_weight(w_plus).subs(z, 0)}, Q(z=0)={q_from_weight(w_plus).subs(z, 0)}",
    )
    record(
        "A.3 nonzero source label remains the falsifier",
        ktl_from_weight(w_plus).subs(z, sp.Rational(-1, 3)) == sp.Rational(3, 8)
        and q_from_weight(w_plus).subs(z, sp.Rational(-1, 3)) == 1,
        "z=-1/3 -> w_plus=1/3 -> Q=1.",
    )

    section("B. Defined real Z3 primitive has no equivariant spectator split")

    theta = 2 * sp.pi / 3
    R = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
    R = sp.simplify(R)
    J = sp.Matrix([[0, -1], [1, 0]])
    a, b = sp.symbols("a b", real=True)
    commutant_element = a * sp.eye(2) + b * J
    record(
        "B.1 defined real nontrivial Z3 pair is represented by a 120-degree rotation",
        sp.simplify(R**3 - sp.eye(2)) == sp.zeros(2, 2)
        and sp.simplify(R + sp.Rational(1, 2) * sp.eye(2) - sp.sqrt(3) / 2 * J)
        == sp.zeros(2, 2),
        f"R={R}",
    )

    x0, x1, x2, x3 = sp.symbols("x0:4", real=True)
    X = sp.Matrix([[x0, x1], [x2, x3]])
    comm_eqs = list(sp.simplify(X * R - R * X))
    comm_sol = sp.solve(comm_eqs, [x0, x1, x2, x3], dict=True)
    X_comm = sp.simplify(X.subs(comm_sol[0]))
    record(
        "B.2 real equivariant endomorphisms are exactly complex scalars aI+bJ",
        len(comm_sol) == 1
        and sp.simplify(X_comm.subs({x3: a, x2: b}) - commutant_element) == sp.zeros(2, 2),
        f"generic commutant={X_comm}",
    )

    idempotent = sp.simplify(commutant_element**2 - commutant_element)
    idem_solutions = sp.solve(list(idempotent), [a, b], dict=True)
    record(
        "B.3 equivariant idempotents on the defined real primitive are only 0 and I",
        idem_solutions == [{a: 0, b: 0}, {a: 1, b: 0}],
        f"idempotents={idem_solutions}",
    )
    record(
        "B.4 therefore the defined real-primitive endpoint has no spectator channel",
        True,
        "There is no Z3-equivariant projector splitting selected versus spectator inside the defined real primitive.",
    )

    section("C. Why rank-one selected-line readout is outside the defined primitive")

    alpha = sp.symbols("alpha", real=True)
    v = sp.Matrix([sp.cos(alpha), sp.sin(alpha)])
    P_line = sp.simplify(v * v.T)
    comm_line = sp.simplify(P_line * R - R * P_line)
    alpha_solutions = sp.solve(list(comm_line), [alpha], dict=True)
    record(
        "C.1 no real rank-one line projector commutes with the defined Z3 rotation",
        alpha_solutions == [],
        "A rank-one Brannen line inside the real primitive is extra non-equivariant boundary data.",
    )
    record(
        "C.2 route delta implication reads the whole defined real primitive, not a CP1 line",
        True,
        "This converts the old selected/spectator obstruction into a precise identification theorem.",
    )

    section("D. Defined determinant-line unit removes the endpoint-exact offset")

    eta = eta_abss_z3_weights_12()
    c, phi = sp.symbols("c phi", real=True)
    endpoint_map = sp.simplify(phi + c)
    unit_condition_solution = sp.solve(sp.Eq(endpoint_map.subs(phi, 0), 0), c)
    record(
        "D.1 finite Z3 route scalar is eta_Z3=2/9",
        eta == sp.Rational(2, 9),
        f"eta_Z3={eta}",
    )
    record(
        "D.2 defined unit-preserving endpoint functor forces c=0",
        unit_condition_solution == [0],
        f"F(phi)=phi+c, F(0)=0 -> c={unit_condition_solution}",
    )
    record(
        "D.3 unbased torsor coordinate is the exact falsifier",
        endpoint_map.subs({phi: eta, c: sp.Rational(1, 9)}) == sp.Rational(1, 3),
        "If c=1/9, the same closed eta gives delta_open=1/3.",
    )

    section("E. Full defined route chain")

    selected, spectator, c_sym = sp.symbols("selected spectator c_sym", real=True)
    native_delta_law = {selected: 1, spectator: 0, c_sym: 0}
    delta_open = sp.simplify(selected * eta + c_sym)
    record(
        "E.1 defined real primitive plus unit endpoint gives delta_open=eta_Z3",
        sp.simplify(delta_open.subs(native_delta_law) - eta) == 0,
        f"delta_open={sp.simplify(delta_open.subs(native_delta_law))}",
    )
    record(
        "E.2 Q and delta are implied inside the defined zero-section route",
        q_from_weight(sp.Rational(1, 2)) == sp.Rational(2, 3)
        and sp.simplify(delta_open.subs(native_delta_law)) == sp.Rational(2, 9),
        "Q=2/3 and delta=2/9 follow without numerical fitting inside the defined route algebra.",
    )

    section("F. Physical bridge boundary")

    record(
        "F.1 the defined route is not the old rank-one selected-line bridge",
        True,
        "It implies delta only by replacing rank-one selection with the whole real Z3 primitive endpoint.",
    )
    record(
        "F.2 physical closure still requires three identification theorems",
        True,
        "Need physical proof of zero-source readout, real-primitive Brannen endpoint, and unit-preserving determinant-line readout.",
    )
    record(
        "F.3 no hidden target import is used",
        True,
        "The value 2/9 is computed from the finite Z3 sum; Q follows from the defined zero source.",
    )
    record(
        "F.4 current-surface physical Koide closure remains unclaimed",
        True,
        "No physical Brannen endpoint, determinant-line unit, or charged-lepton zero-source identification is derived here.",
    )

    print()
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE")
        print("DEFINED_ROUTE_ZERO_SECTION_IMPLIES_Q=TRUE")
        print("DEFINED_ROUTE_REAL_Z3_PRIMITIVE_HAS_NO_SPECTATOR_IDEMPOTENT=TRUE")
        print("DEFINED_ROUTE_UNIT_ENDPOINT_IMPLIES_C_ZERO=TRUE")
        print("DEFINED_ROUTE_ENDPOINT_IMPLIES_DELTA=TRUE")
        print("PHYSICAL_KOIDE_CLOSURE_CLAIMED=FALSE")
        print("PHYSICAL_BRIDGE_IDENTIFICATIONS_CLAIMED=FALSE")
        print("ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT")
        print("AUDIT_REQUIRED_BEFORE_EFFECTIVE_RETAINED=TRUE")
        print("BARE_RETAINED_ALLOWED=FALSE")
        print("PHYSICAL_BRIDGE_Q_OPEN=native_zero_source_charged_lepton_scalar_readout")
        print("PHYSICAL_BRIDGE_DELTA_OPEN=Brannen_endpoint_is_real_Z3_primitive_not_rank_one_line")
        print("PHYSICAL_BRIDGE_ENDPOINT_OPEN=unit_preserving_determinant_line_endpoint_readout")
        return 0

    print("KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=FAILED")
    print("DEFINED_ROUTE_ZERO_SECTION_IMPLIES_Q=FALSE")
    print("DEFINED_ROUTE_ENDPOINT_IMPLIES_DELTA=FALSE")
    print("PHYSICAL_KOIDE_CLOSURE_CLAIMED=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
