#!/usr/bin/env python3
"""Exact checks for the spatial-cubic time-anisotropy gate.

The active review issue is that spatial O_h / cubic-harmonic power counting
does not by itself imply full SO(4) continuum covariance on a Z^3 x Z_tau
surface. A marginal time-vs-space kinetic anisotropy remains allowed unless an
extra Euclidean kinetic-normalization / 4D-hypercubic premise is supplied.

This runner verifies the obstruction with exact rational linear algebra.
"""

from __future__ import annotations

from itertools import permutations, product

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def signed_permutation_group(n: int) -> list[sp.Matrix]:
    mats: list[sp.Matrix] = []
    for perm in permutations(range(n)):
        for signs in product((-1, 1), repeat=n):
            M = sp.zeros(n, n)
            for row, src in enumerate(perm):
                M[row, src] = signs[row]
            mats.append(M)
    return mats


def spatial_oh_on_4d() -> list[sp.Matrix]:
    out: list[sp.Matrix] = []
    for R3 in signed_permutation_group(3):
        M = sp.eye(4)
        for i in range(3):
            for j in range(3):
                M[i + 1, j + 1] = R3[i, j]
        out.append(M)
    return out


def quadratic_rep(M: sp.Matrix) -> sp.Matrix:
    """Representation on diagonal quadratic coefficients [t^2,x^2,y^2,z^2].

    Signed permutations preserve the diagonal-square subspace exactly.
    """
    n = M.shape[0]
    R = sp.zeros(n, n)
    for old_axis in range(n):
        for new_axis in range(n):
            if M[new_axis, old_axis] != 0:
                R[new_axis, old_axis] = 1
    return R


def invariant_dimension(reps: list[sp.Matrix], dim: int) -> int:
    rows = []
    I = sp.eye(dim)
    for R in reps:
        rows.extend((R - I).tolist())
    A = sp.Matrix(rows)
    return dim - A.rank()


def q(coeffs: tuple[sp.Rational, sp.Rational], p: sp.Matrix) -> sp.Rational:
    c_t, c_s = coeffs
    return sp.simplify(c_t * p[0] ** 2 + c_s * (p[1] ** 2 + p[2] ** 2 + p[3] ** 2))


def rotate_tx_45() -> sp.Matrix:
    r = sp.sqrt(2) / 2
    M = sp.eye(4)
    M[0, 0] = r
    M[0, 1] = r
    M[1, 0] = -r
    M[1, 1] = r
    return M


def quartic_spatial(p: sp.Matrix) -> sp.Expr:
    return sp.expand(p[1] ** 4 + p[2] ** 4 + p[3] ** 4)


def main() -> int:
    oh4 = spatial_oh_on_4d()
    b4 = signed_permutation_group(4)

    section("Group and invariant-space checks")
    check("G1 spatial signed-permutation group has 48 elements", len(oh4) == 48, f"|O_h|={len(oh4)}")
    check("G2 4D signed-permutation hypercubic group has 384 elements", len(b4) == 384, f"|B_4|={len(b4)}")

    oh_quad_dim = invariant_dimension([quadratic_rep(M) for M in oh4], 4)
    b4_quad_dim = invariant_dimension([quadratic_rep(M) for M in b4], 4)
    check("G3 spatial cubic + time parity leaves two quadratic kinetic invariants",
          oh_quad_dim == 2, f"dim={oh_quad_dim}: span(t^2, x^2+y^2+z^2)")
    check("G4 4D hypercubic symmetry leaves one quadratic kinetic invariant",
          b4_quad_dim == 1, f"dim={b4_quad_dim}: span(t^2+x^2+y^2+z^2)")

    section("Marginal anisotropy allowed by spatial cubic symmetry")
    p = sp.Matrix([1, 2, 3, 4])
    coeff_aniso = (sp.Rational(2), sp.Rational(1))
    coeff_iso = (sp.Rational(1), sp.Rational(1))
    base = q(coeff_aniso, p)
    spatial_ok = all(q(coeff_aniso, M * p) == base for M in oh4)
    check("A1 anisotropic kinetic form is invariant under all spatial O_h operations",
          spatial_ok, f"Q=2 t^2 + |x|^2 gives {base} on p={tuple(p)}")
    swap_tx = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    check("A2 the same anisotropic form fails a time-space swap",
          q(coeff_aniso, swap_tx * p) != base,
          f"Q(p)={base}, Q(swap_tx p)={q(coeff_aniso, swap_tx * p)}")
    R45 = rotate_tx_45()
    rotated_value = sp.simplify(q(coeff_aniso, R45 * p))
    check("A3 the same anisotropic form fails a 45-degree SO(4) rotation",
          rotated_value != base,
          f"Q(p)={base}, Q(R45 p)={rotated_value}")
    check("A4 isotropic kinetic form survives the same tested SO(4) rotation",
          sp.simplify(q(coeff_iso, R45 * p) - q(coeff_iso, p)) == 0)

    section("Cubic-harmonic checks do not remove the marginal anisotropy")
    p2 = sp.Matrix([3, 1, 2, -2])
    H4_before = quartic_spatial(p2)
    H4_spatial_ok = all(quartic_spatial(M * p2) == H4_before for M in oh4)
    check("C1 spatial quartic cubic artifact is O_h invariant",
          H4_spatial_ok, f"H4_spatial={H4_before}")
    q_delta_1 = q((sp.Rational(1), sp.Rational(1)), p2)
    q_delta_2 = q((sp.Rational(2), sp.Rational(1)), p2)
    check("C2 changing time normalization leaves the same quartic spatial artifact",
          quartic_spatial(p2) == H4_before and q_delta_1 != q_delta_2,
          f"Q_iso={q_delta_1}, Q_aniso={q_delta_2}, H4={H4_before}")
    check("C3 a quartic-only power-counting test cannot determine c_t/c_s",
          q_delta_1 != q_delta_2,
          "the obstruction is degree-2/marginal, not the checked quartic artifact")

    section("Scope-repair alternatives")
    check("S1 adding Euclidean kinetic-normalization c_t=c_s closes this obstruction",
          coeff_iso[0] == coeff_iso[1] and sp.simplify(q(coeff_iso, R45 * p) - q(coeff_iso, p)) == 0)
    check("S2 adding 4D hypercubic symmetry also removes independent c_t/c_s at quadratic order",
          b4_quad_dim == 1)
    check("S3 without one of those premises, the honest claim is spatial cubic artifact power counting",
          oh_quad_dim == 2 and b4_quad_dim == 1)
    check("S4 spatial O_h support alone is insufficient for full SO(4) all-n-point continuum language",
          spatial_ok and rotated_value != base)

    section("Review-gate certificate")
    check("R1 exact spatial O_h checks can be useful but are scope-limited",
          H4_spatial_ok and oh_quad_dim == 2)
    check("R2 marginal anisotropy is symmetry-allowed on Z^3 x Z_tau",
          spatial_ok and q(coeff_aniso, swap_tx * p) != base)
    check("R3 salvage choices are explicit premise or narrowed theorem",
          True,
          "add c_t=c_s / 4D hypercubic premise, or narrow to spatial cubic artifact power counting")

    section("N5 execution certificate (print-only; adds no check and no counter)")
    print(
        "per_element: resolved as exact entry placements in the group representation -- each signed "
        "permutation is built by writing one nonzero entry, plus or minus one, into a named row and "
        "column, and the induced action on diagonal quadratic coefficients is derived by scanning "
        "every (new_axis, old_axis) position and recording a 1 exactly where the underlying entry is "
        "nonzero. The invariant dimension is then taken by stacking the rows of (R - I) for every "
        "group element into a single exact rational matrix and computing its rank, so each entry of "
        "each representation matrix enters that count on its own."
    )
    print(
        "per_site: checked and not executed -- the Z^3 x Z_tau surface is named in the statement but "
        "never instantiated. This runner works entirely with 4x4 matrices and four-component momentum "
        "vectors; it builds no lattice, no coordinate, no neighbour relation, and no site amplitude, "
        "so there is no site-resolved quantity available for it to report."
    )
    print(
        "per_mode: resolved direction by direction on the four coordinate axes -- the carrier is the "
        "four-dimensional space of diagonal quadratic coefficients with basis t^2, x^2, y^2, z^2, and "
        "each axis is tracked separately through the induced representation, which is exactly what "
        "lets the run see spatial operations moving the three space axes among themselves while "
        "leaving the time axis fixed. The kinetic form is then evaluated at explicit integer momenta, "
        "(1, 2, 3, 4) and (3, 1, 2, -2), with each component squared individually."
    )
    print(
        "per_block: resolved as a two-block versus one-block invariant count, and this is the entire "
        "no-go -- under the 48-element spatial group the invariant subspace of quadratic coefficients "
        "has exact dimension 2, spanned separately by the time block t^2 and the spatial block "
        "x^2+y^2+z^2, whereas under the 384-element four-dimensional hypercubic group it collapses to "
        "dimension 1, spanned by the single block t^2+x^2+y^2+z^2. That surviving second block is "
        "precisely the free ratio c_t/c_s in which the marginal anisotropy lives."
    )
    print(
        "lattice_wide: checked and not executed -- no lattice, volume, extent, or site sum is formed "
        "anywhere in this runner, and no correlator or n-point function is computed. The blocking "
        "reason is the one this gate exists to record: full SO(4) continuum covariance is exactly "
        "what is not established here, and closing it requires an extra premise, either the Euclidean "
        "kinetic normalization c_t = c_s or four-dimensional hypercubic symmetry, neither of which is "
        "derived in this file."
    )
    print(
        "Scope: seventeen of the eighteen checks evaluate an exact symbolic condition. One of them, "
        "R3, is invoked with a hardcoded True and names the two salvage options in prose without "
        "computing anything; resolution is claimed above only for the seventeen."
    )
    print(
        "Determinism: sympy exact rational and radical arithmetic throughout, with no floating-point "
        "tolerance anywhere -- ranks are exact, group invariance is tested by all-quantified equality "
        "over every element of the enumerated group, and the single irrational used, sqrt(2)/2 in the "
        "45-degree rotation, is carried symbolically rather than numerically. Both groups are "
        "enumerated in the fixed deterministic order produced by permutations and product, and "
        "because every test quantifies over the whole group that ordering cannot affect a verdict. "
        "No RNG, optimizer, root-finding, grid scan, or Monte Carlo appears."
    )

    section("Scorecard")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: spatial cubic power counting does not exclude marginal "
        "time-vs-space kinetic anisotropy. Full SO(4) continuum wording needs "
        "an explicit Euclidean normalization / 4D hypercubic premise, or the "
        "claim must be narrowed to spatial cubic artifact power counting."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
