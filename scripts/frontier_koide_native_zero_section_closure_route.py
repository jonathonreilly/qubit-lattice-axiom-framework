#!/usr/bin/env python3
"""Supplied rational, commutant and endpoint-law algebra.
The endpoint law and selected=1 are separate supplied definitions. No physical
phase identification or independent physical target provenance is established.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md',)

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def historical(name, condition, detail=""):
    print(f"HISTORICAL_UNSCORED old assertion={name!r}; observed={bool(condition)}; old detail={detail!r}")


def require_weight(w):
    # Common domain of the original Q/K definitions: w !=0,1.
    if w.is_number and (w == 0 or w == 1):
        raise ValueError("common Q/K domain excludes w=0,1 (z=-1,+1)")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def q_from_weight(w_plus: sp.Expr) -> sp.Expr:
    require_weight(sp.sympify(w_plus))
    r = sp.simplify((1 - w_plus) / w_plus)
    return sp.simplify((1 + r) / 3)


def ktl_from_weight(w_plus: sp.Expr) -> sp.Expr:
    require_weight(sp.sympify(w_plus))
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
    PASSES.clear()
    for p in AUDIT_INPUT_PATHS:
        if not (ROOT/p).is_file():
            print(f"FAIL missing input {p}")
            return 1
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
    historical(
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
        "C.1 solver diagnostic returns no real rank-one commutation solution; exact norm proof below",
        alpha_solutions == [],
        "A rank-one Brannen line inside the real primitive is extra non-equivariant boundary data.",
    )
    historical(
        "C.2 route delta implication reads the whole defined real primitive, not a CP1 line",
        True,
        "This records the defined route boundary without deriving a physical endpoint identification.",
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
        "D.2 supplied affine map F(phi)=phi+c and F(0)=0 imply c=0",
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
        "E.1 supplied endpoint formula and selected=1,c=0 give delta_open=eta",
        sp.simplify(delta_open.subs(native_delta_law) - eta) == 0,
        f"delta_open={sp.simplify(delta_open.subs(native_delta_law))}",
    )
    record(
        "E.2 Q and delta are implied inside the defined zero-section route",
        q_from_weight(sp.Rational(1, 2)) == sp.Rational(2, 3)
        and sp.simplify(delta_open.subs(native_delta_law)) == sp.Rational(2, 9),
        "Supplied z=0 and endpoint law selected*eta+c with selected=1,c=0 give these values.",
    )

    section("F. Physical bridge boundary")

    historical(
        "F.1 the defined route is not the old rank-one selected-line bridge",
        True,
        "It implies delta only by replacing rank-one selection with the whole real Z3 primitive endpoint.",
    )
    historical(
        "F.2 physical closure still requires three identification theorems",
        True,
        "Need physical proof of zero-source readout, real-primitive Brannen endpoint, and unit-preserving determinant-line readout.",
    )
    historical(
        "F.3 no hidden target import is used",
        True,
        "The value 2/9 is computed from the finite Z3 sum; Q follows from the defined zero source.",
    )
    historical(
        "F.4 current-surface physical Koide closure remains unclaimed",
        True,
        "No physical Brannen endpoint, determinant-line unit, or charged-lepton zero-source identification is derived here.",
    )

    record("G.1 exact common-domain rational identities",
           sp.simplify(q_from_weight(w_plus)-2/(3*(1+z))) == 0
           and sp.simplify(ktl_from_weight(w_plus)+z/(1-z**2)) == 0)
    rejected=[]
    for endpoint in (-1,1):
        try:
            ktl_from_weight(sp.Rational(1+endpoint,2))
        except ValueError:
            rejected.append(endpoint)
    record("G.2 both excluded domain endpoints fail closed",rejected == [-1,1])
    norm_squared=sp.trigsimp(sum(x*x for x in comm_line))
    record("G.3 exact commutator Frobenius norm squared is3/2 for every real alpha",
           sp.trigsimp(norm_squared-sp.Rational(3,2)) == 0)
    omega=sp.Rational(-1,2)+sp.I*sp.sqrt(3)/2
    record("G.4 both root-of-unity summands have denominator3",
           all(sp.simplify((omega**k-1)*(omega**(2*k)-1)-3)==0 for k in (1,2)))
    print("INFO: spectator is absent from delta_open; representation classification does not select this endpoint law.")
    print("INFO: physical source, endpoint, phase and anomaly identifications remain unproved; no exhaustive list claimed.")
    n_pass=sum(bool(ok) for _,ok,_ in PASSES)
    n_total=len(PASSES)
    print(f"PASSED: {n_pass}/{n_total}")
    ok=n_pass==n_total
    print(f"SUPPLIED_ROUTE_MATH_CHECKS={'PASS' if ok else 'FAIL'}")
    print("SUPPLIED_ENDPOINT_LAW=selected*eta+c; selected=1,c=0")
    print("PHYSICAL_IDENTIFICATION_PROVED=FALSE")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
