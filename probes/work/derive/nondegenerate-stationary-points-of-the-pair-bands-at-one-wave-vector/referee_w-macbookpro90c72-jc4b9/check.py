#!/usr/bin/env python3
"""Independent referee for the pair-band stationary points, attempt 1.

The band gradient and Hessian are derived again and compared with direct
differentiation. The degenerate-stationary ideal is rebuilt and its
Groebner basis is recomputed. The attempt's script is not imported.
"""
from __future__ import annotations

import time

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def double_angles(tans):
    """cos 2K and sin 2K from tan K, as rational numbers."""
    cosines, sines = [], []
    for tangent in tans:
        den = 1 + tangent ** 2
        cosines.append((1 - tangent ** 2) / den)
        sines.append(2 * tangent / den)
    return cosines, sines


def band_system(tans):
    """Polynomial system for a degenerate stationary point off the cones.

    k1 = K0/2 + q and k2 = K0/2 - q. Circle coordinates are cos 2k1 and
    sin 2k1. Signed energies e1, e2 absorb the four band signs.
    """
    dim = len(tans)
    cos1 = sp.symbols(f"c1:{dim + 1}")
    sin1 = sp.symbols(f"s1:{dim + 1}")
    energy1, energy2, inverse = sp.symbols("e1 e2 z")
    cos_k, sin_k = double_angles(tans)
    cos2 = [cos_k[axis] * cos1[axis] + sin_k[axis] * sin1[axis] for axis in range(dim)]
    sin2 = [sin_k[axis] * cos1[axis] - cos_k[axis] * sin1[axis] for axis in range(dim)]
    square1 = sum((1 - cos1[axis]) / 2 for axis in range(dim))
    square2 = sum((1 - cos2[axis]) / 2 for axis in range(dim))
    stationary = [sp.expand(sin1[axis] * energy2 - sin2[axis] * energy1) for axis in range(dim)]

    def hessian(cosines, sines, energy):
        def entry(row, col):
            diagonal = cosines[row] / energy if row == col else 0
            return diagonal - sines[row] * sines[col] / (4 * energy ** 3)

        return sp.Matrix(dim, dim, entry)

    total = hessian(cos1, sin1, energy1) + hessian(cos2, sin2, energy2)
    cleared = sp.together(total.det())
    numerator = sp.expand(sp.numer(cleared))
    denominator = sp.factor(sp.denom(cleared))
    equations = [cos1[axis] ** 2 + sin1[axis] ** 2 - 1 for axis in range(dim)]
    equations += [sp.expand(sp.together(energy1 ** 2 - square1)), sp.expand(sp.together(energy2 ** 2 - square2))]
    equations += [sp.expand(sp.together(item)) for item in stationary]
    equations.append(inverse * energy1 * energy2 - 1)
    generators = [inverse, energy1, energy2, *cos1, *sin1]
    pack = {
        "cos1": cos1,
        "sin1": sin1,
        "cos2": cos2,
        "sin2": sin2,
        "e1": energy1,
        "e2": energy2,
        "hessian": total,
        "numerator": numerator,
        "denominator": denominator,
    }
    return equations, generators, pack


def monomial_in_energies(denominator, energy1, energy2):
    if denominator == 1:
        return True
    factors = sp.factor_list(denominator)[1]
    allowed = {energy1, energy2, -energy1, -energy2}
    return all(sp.factor(base) in allowed or base in allowed for base, _exp in factors)


def agrees_with_differentiation(tans, shifts):
    dim = len(tans)
    wave = [sp.atan(tangent) for tangent in tans]
    query = sp.symbols(f"q1:{dim + 1}")
    _equations, _gens, pack = band_system(tans)
    point = {query[axis]: shifts[axis] for axis in range(dim)}
    ok = True
    signs = ((1, 1),) if dim == 3 else ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for sign1, sign2 in signs:
        first = [wave[axis] / 2 + query[axis] for axis in range(dim)]
        second = [wave[axis] / 2 - query[axis] for axis in range(dim)]
        band = sign1 * sp.sqrt(sum(sp.sin(component) ** 2 for component in first))
        band += sign2 * sp.sqrt(sum(sp.sin(component) ** 2 for component in second))
        gradient = [sp.diff(band, query[axis]).subs(point) for axis in range(dim)]
        second_deriv = sp.Matrix(dim, dim, lambda row, col: sp.diff(band, query[row], query[col]).subs(point))
        replacement = {pack["cos1"][axis]: sp.cos(2 * first[axis].subs(point)) for axis in range(dim)}
        replacement.update({pack["sin1"][axis]: sp.sin(2 * first[axis].subs(point)) for axis in range(dim)})
        replacement[pack["e1"]] = sign1 * sp.sqrt(sum(sp.sin(component.subs(point)) ** 2 for component in first))
        replacement[pack["e2"]] = sign2 * sp.sqrt(sum(sp.sin(component.subs(point)) ** 2 for component in second))
        predicted = [
            (pack["sin1"][axis] / (2 * pack["e1"]) - pack["sin2"][axis] / (2 * pack["e2"])).subs(replacement)
            for axis in range(dim)
        ]
        hess = pack["hessian"].subs(replacement)
        ok = ok and all(abs(sp.N(gradient[axis] - predicted[axis], 50)) < sp.Float("1e-40") for axis in range(dim))
        ok = ok and all(
            abs(sp.N(second_deriv[row, col] - hess[row, col], 50)) < sp.Float("1e-40")
            for row in range(dim)
            for col in range(dim)
        )
    return ok


def basis_is_one(equations, generators):
    basis = sp.groebner(equations, *generators, order="grevlex", domain=sp.QQ)
    polynomials = list(basis)
    return polynomials == [sp.Integer(1)], polynomials


def tilt_square(tans):
    """Squared gradient of eps(K0) in the q coordinate, at the opposite cone k=0."""
    numerator = sum((tangent / (1 + tangent ** 2)) ** 2 for tangent in tans)
    denominator = sum(tangent ** 2 / (1 + tangent ** 2) for tangent in tans)
    return sp.together(numerator / denominator)


def main():
    plane = [sp.Rational(5, 6), sp.Rational(18, 5)]
    space = [sp.Rational(5, 6), sp.Rational(18, 5), sp.Rational(1, 2)]
    diff_ok = agrees_with_differentiation(plane, [sp.Rational(1, 4), sp.Rational(-1, 5)])
    diff_ok = diff_ok and agrees_with_differentiation(space, [sp.Rational(1, 4), sp.Rational(-1, 5), sp.Rational(1, 7)])
    check(
        "differentiation",
        diff_ok,
        "gradient and Hessian match direct differentiation at q=(1/4,-1/5) for all four plane bands "
        "and at q=(1/4,-1/5,1/7) for the positive space band, to 40 digits",
    )

    equations, generators, pack = band_system(plane)
    denom_ok = monomial_in_energies(pack["denominator"], pack["e1"], pack["e2"]) and pack["numerator"] != 0
    started = time.time()
    full_one, _full = basis_is_one(equations + [pack["numerator"]], generators)
    dropped = [item for item in equations]
    bare_one, _bare = basis_is_one(dropped, generators)
    check(
        "plane",
        denom_ok and full_one and not bare_one,
        f"at tan K0=(5/6, 18/5) the degenerate system has Groebner basis [1] "
        f"({time.time() - started:.1f}s); without the Hessian numerator the basis is not [1]. "
        f"The Hessian denominator is a monomial in the signed energies",
    )

    space_equations, space_generators, space_pack = band_system(space)
    space_denom = monomial_in_energies(space_pack["denominator"], space_pack["e1"], space_pack["e2"])
    started = time.time()
    space_one, _space = basis_is_one(space_equations + [space_pack["numerator"]], space_generators)
    degree = sp.total_degree(space_pack["numerator"])
    check(
        "space",
        space_denom and space_one and space_pack["numerator"] != 0,
        f"at tan K0=(5/6, 18/5, 1/2) the same system has Groebner basis [1] "
        f"({time.time() - started:.0f}s); Hessian numerator total degree {degree}",
    )

    zero = [sp.Integer(0), sp.Integer(0)]
    zero_equations, zero_generators, zero_pack = band_system(zero)
    zero_one, _zero = basis_is_one(zero_equations + [zero_pack["numerator"]], zero_generators)
    check(
        "flat control",
        not zero_one,
        "at K0=0 the band eps(q)-eps(-q) is identically zero, and the degenerate system is not the unit ideal",
    )

    plane_tilt = tilt_square(plane)
    space_tilt = tilt_square(space)
    check(
        "cones",
        plane_tilt == sp.Rational(139761000, 606502321)
        and space_tilt == sp.Rational(2653455542, 8714332815)
        and plane_tilt < 1
        and space_tilt < 1,
        f"opposite-cone gradient squares are {plane_tilt} and {space_tilt}, both below 1",
    )

    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. At tan K0 = (5/6, 18/5) and (5/6, 18/5, 1/2) the ideal of a "
        "degenerate stationary point of any band pair off the cones is the unit ideal, so every such "
        "stationary point is nondegenerate. The opposite-cone gradients have squared length below 1. "
        "Real stationary points were not counted, and the resultant degrees inside T6 were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - every stationary point of every band pair off the cones is nondegenerate at "
        "tan K0 = (5/6, 18/5) and (5/6, 18/5, 1/2), and the cone tilts are strictly below 1",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
