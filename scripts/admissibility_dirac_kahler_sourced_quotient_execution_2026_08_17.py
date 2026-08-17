#!/usr/bin/env python3
"""Block 124: exact execution of the momentum-sourced Gauss quotient.

The four positive quotient directions are ordered by Z4 momentum
k=(0,1,2,3), with pinned principal charges p=(0,1,2,-1).  The committed
Block 123 runner is imported as the authority chain.  Every scientific
calculation uses exact SymPy arithmetic; wall-clock timing is the sole
floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16 as prior


R = sp.Rational
I = sp.I
block121 = prior.block121
block119 = prior.block119
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_momentum_population_definiteness_"
    "2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_momentum_population_"
    "definiteness_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "31e4c7ff7d41db6a78feef19dba2bfbea3dc1830"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block123-momentum-population-definiteness-20260816"
)
PARENT_COMMIT = "954322e0e085d6c3133ce24dca49db2efbd7d0a6"
PARENT_NOTE_BLOB = "560894350af5930f88161455f4db8954730f3e96"
PARENT_RUNNER_BLOB = "7ee63309da28801f0a5fb412dba402819e7d0d66"
PARENT_CACHE_BLOB = "41e2ef00a3a74cabba9b603dbd902cc365bffaa2"
ANCESTOR_COMMITS = (
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_quadric",
    "claim_convention_free_class",
    "break_gauss_solution",
    "break_orientation_pin",
    "break_quotient_isomorphism",
    "break_root_identity",
    "break_sector_preservation",
    "break_violation_formula",
    "break_sum_rule",
    "claim_structural_localization",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
)

P_VALUES = (sp.Integer(0), sp.Integer(1), sp.Integer(2), sp.Integer(-1))
P = sp.diag(*P_VALUES)
P_ALTERNATE = sp.diag(0, 1, -2, -1)
SHEARS = prior.SHEARS


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    ancestors = {
        f"ancestor_{number}": is_ancestor(commit, "HEAD")
        for number, commit in ANCESTOR_COMMITS
    }
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **ancestors,
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


def squared_norm(vector: sp.Matrix) -> sp.Expr:
    return sp.expand((vector.H * vector)[0])


def momentum_numerator(
    vector: sp.Matrix, momentum: sp.Matrix = P
) -> sp.Expr:
    return sp.expand((vector.H * momentum * vector)[0])


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


@dataclass(frozen=True)
class ParametrizationRanks:
    cone: int
    normalized: int
    ray: int
    equation_exact: bool


@dataclass(frozen=True)
class StateFixture:
    name: str
    vector: sp.Matrix
    norm_squared: sp.Expr
    momentum: sp.Expr


@dataclass(frozen=True)
class StateClassCertificate:
    equation: sp.Expr
    alternate_equation: sp.Expr
    pinned_ranks: ParametrizationRanks
    alternate_ranks: ParametrizationRanks
    ambient_real_dimension: int
    cone_dimension: int
    normalized_dimension: int
    ray_dimension: int
    c0_free: bool
    forms_exact: bool
    sets_differ_off_c2_zero: bool
    intersection_exact: bool
    dimensions_convention_invariant: bool
    fixtures: tuple[StateFixture, ...]


def _normalization(coordinates: sp.Matrix) -> sp.Matrix:
    norm_squared = sp.expand(sum(value**2 for value in coordinates))
    return coordinates / sp.sqrt(norm_squared)


def _parametrization_ranks(convention: str) -> ParametrizationRanks:
    """Exact local ranks on a nonsingular chart of each real class cone."""
    a0, b0, a1, b1, a2, b2, a3, b3, t = sp.symbols(
        "a0 b0 a1 b1 a2 b2 a3 b3 t", real=True
    )
    if convention == "p2=+2":
        parameters = (a0, b0, a1, b1, a2, b2, t)
        radius_squared = a1**2 + b1**2 + 2 * (a2**2 + b2**2)
        radius = sp.sqrt(radius_squared)
        denominator = 1 + t**2
        coordinates = sp.Matrix(
            (
                a0,
                b0,
                a1,
                b1,
                a2,
                b2,
                radius * (1 - t**2) / denominator,
                2 * radius * t / denominator,
            )
        )
        equation = (
            coordinates[2] ** 2
            + coordinates[3] ** 2
            + 2 * (coordinates[4] ** 2 + coordinates[5] ** 2)
            - coordinates[6] ** 2
            - coordinates[7] ** 2
        )
        witness = {
            a0: 1,
            b0: 2,
            a1: 1,
            b1: 0,
            a2: 0,
            b2: 0,
            t: 0,
        }
        ray_parameters = parameters[:-1]
        ray_coordinates = coordinates.subs(t, 0)
    elif convention == "p2=-2":
        parameters = (a0, b0, a2, b2, a3, b3, t)
        radius_squared = 2 * (a2**2 + b2**2) + a3**2 + b3**2
        radius = sp.sqrt(radius_squared)
        denominator = 1 + t**2
        coordinates = sp.Matrix(
            (
                a0,
                b0,
                radius * (1 - t**2) / denominator,
                2 * radius * t / denominator,
                a2,
                b2,
                a3,
                b3,
            )
        )
        equation = (
            coordinates[2] ** 2
            + coordinates[3] ** 2
            - 2 * (coordinates[4] ** 2 + coordinates[5] ** 2)
            - coordinates[6] ** 2
            - coordinates[7] ** 2
        )
        witness = {
            a0: 1,
            b0: 2,
            a2: 0,
            b2: 0,
            a3: 1,
            b3: 0,
            t: 0,
        }
        ray_parameters = parameters[:-1]
        ray_coordinates = coordinates.subs(t, 0)
    else:
        raise ValueError(f"unknown momentum convention {convention!r}")

    cone_rank = coordinates.jacobian(parameters).subs(witness).rank()
    normalized_rank = (
        _normalization(coordinates).jacobian(parameters).subs(witness).rank()
    )
    ray_rank = (
        _normalization(ray_coordinates)
        .jacobian(ray_parameters)
        .subs(witness)
        .rank()
    )
    return ParametrizationRanks(
        cone=cone_rank,
        normalized=normalized_rank,
        ray=ray_rank,
        equation_exact=sp.simplify(equation) == 0,
    )


def state_class_certificate() -> StateClassCertificate:
    real = sp.symbols("x0:4", real=True)
    imag = sp.symbols("y0:4", real=True)
    coefficients = sp.Matrix(
        [real[index] + I * imag[index] for index in range(4)]
    )
    equation = momentum_numerator(coefficients)
    alternate_equation = momentum_numerator(coefficients, P_ALTERNATE)
    n1 = real[1] ** 2 + imag[1] ** 2
    n2 = real[2] ** 2 + imag[2] ** 2
    n3 = real[3] ** 2 + imag[3] ** 2
    expected = sp.expand(n1 + 2 * n2 - n3)
    expected_alternate = sp.expand(n1 - 2 * n2 - n3)
    pinned_ranks = _parametrization_ranks("p2=+2")
    alternate_ranks = _parametrization_ranks("p2=-2")

    plus_only = sp.Matrix((0, 0, 1, sp.sqrt(2)))
    minus_only = sp.Matrix((0, sp.sqrt(2), 1, 0))
    intersection_solution = sp.solve(
        (sp.Symbol("n1") + 2 * sp.Symbol("n2") - sp.Symbol("n3"),
         sp.Symbol("n1") - 2 * sp.Symbol("n2") - sp.Symbol("n3")),
        (sp.Symbol("n2"), sp.Symbol("n3")),
        dict=True,
    )
    intersection_exact = (
        sp.expand(equation - alternate_equation - 4 * n2) == 0
        and intersection_solution
        == [{sp.Symbol("n2"): 0, sp.Symbol("n3"): sp.Symbol("n1")}]
        and sp.expand((equation - alternate_equation).subs({real[2]: 0, imag[2]: 0}))
        == 0
    )
    fixtures = tuple(
        StateFixture(name, vector, squared_norm(vector), momentum_numerator(vector))
        for name, vector in (
            ("w=e1+e3", sp.Matrix((0, 1, 0, 1))),
            ("u=2e0+e1+2e2+3e3", sp.Matrix((2, 1, 2, 3))),
        )
    )
    return StateClassCertificate(
        equation=equation,
        alternate_equation=alternate_equation,
        pinned_ranks=pinned_ranks,
        alternate_ranks=alternate_ranks,
        ambient_real_dimension=8,
        cone_dimension=7,
        normalized_dimension=6,
        ray_dimension=5,
        c0_free=all(
            sp.diff(equation, variable) == 0
            and sp.diff(alternate_equation, variable) == 0
            for variable in (real[0], imag[0])
        ),
        forms_exact=(
            sp.expand(equation - expected) == 0
            and sp.expand(alternate_equation - expected_alternate) == 0
        ),
        sets_differ_off_c2_zero=(
            momentum_numerator(plus_only) == 0
            and momentum_numerator(plus_only, P_ALTERNATE) == -4
            and momentum_numerator(minus_only, P_ALTERNATE) == 0
            and momentum_numerator(minus_only) == 4
        ),
        intersection_exact=intersection_exact,
        dimensions_convention_invariant=(
            pinned_ranks == ParametrizationRanks(7, 6, 5, True)
            and alternate_ranks == ParametrizationRanks(7, 6, 5, True)
        ),
        fixtures=fixtures,
    )


@dataclass(frozen=True)
class GaussCertificate:
    incidence: sp.Matrix
    orientation_exact: bool
    zero_sum_image_exact: bool
    symbolic_solution_exact: bool
    gauge_kernel_exact: bool
    witness_source: sp.Matrix
    witness_mean_zero: sp.Matrix
    witness_exact: bool
    opposite_orientation_fails: bool


def gauss_certificate() -> GaussCertificate:
    incidence = block121.periodic_incidence_1d(4)
    expected_incidence = sp.Matrix(
        ((1, 0, 0, -1), (-1, 1, 0, 0), (0, -1, 1, 0), (0, 0, -1, 1))
    )
    gamma_symbols = sp.Matrix(sp.symbols("g0:4", real=True))
    forward_difference = sp.Matrix(
        [gamma_symbols[index] - gamma_symbols[(index + 1) % 4]
         for index in range(4)]
    )
    orientation_exact = (
        incidence == expected_incidence
        and matrix_zero(incidence.T * gamma_symbols - forward_difference)
    )

    r0, r1, r2, lam = sp.symbols("r0 r1 r2 lambda", real=True)
    r3 = -r0 - r1 - r2
    source = sp.Matrix((r0, r1, r2, r3))
    ones = sp.ones(4, 1)
    particular = sp.Matrix((0, -r0, -r0 - r1, r3))
    general = particular + lam * ones
    symbolic_solution_exact = (
        sum(source) == 0
        and matrix_zero(incidence.T * general - source)
    )
    zero_sum_basis = sp.Matrix.hstack(
        *(sp.eye(4).col(index) - sp.eye(4).col(3) for index in range(3))
    )
    zero_sum_image_exact = (
        incidence.rank() == 3
        and matrix_zero(sp.ones(1, 4) * incidence.T)
        and zero_sum_basis.rank() == 3
        and incidence.T.row_join(zero_sum_basis).rank() == 3
    )
    gauge_kernel_exact = (
        incidence.T.nullspace() == [ones]
        and matrix_zero(incidence.T * ones)
    )

    witness_source = sp.Matrix((R(2, 9), -R(1, 9), 0, -R(1, 9)))
    witness_particular = sp.Matrix(
        (
            0,
            -witness_source[0],
            -witness_source[0] - witness_source[1],
            witness_source[3],
        )
    )
    witness_mean_zero = sp.simplify(
        witness_particular - ones * sum(witness_particular) / 4
    )
    expected_mean_zero = sp.Matrix((R(1, 9), -R(1, 9), 0, 0))
    witness_exact = (
        sum(witness_source) == 0
        and witness_mean_zero == expected_mean_zero
        and incidence.T * witness_mean_zero == witness_source
        and sum(witness_mean_zero) == 0
    )
    opposite_result = -incidence.T * witness_mean_zero
    opposite_orientation_fails = (
        opposite_result != witness_source
        and matrix_zero(opposite_result + witness_source)
        and witness_source != sp.zeros(4, 1)
    )
    return GaussCertificate(
        incidence=incidence,
        orientation_exact=orientation_exact,
        zero_sum_image_exact=zero_sum_image_exact,
        symbolic_solution_exact=symbolic_solution_exact,
        gauge_kernel_exact=gauge_kernel_exact,
        witness_source=witness_source,
        witness_mean_zero=witness_mean_zero,
        witness_exact=witness_exact,
        opposite_orientation_fails=opposite_orientation_fails,
    )


@dataclass(frozen=True)
class PhysicalQuotientCertificate:
    carrier_rank: int
    tt_dimension: int
    gravity_solution_dimension: int
    gravity_gauge_dimension: int
    gravity_quotient_fiber_dimension: int
    graph_isomorphism_exact: bool
    matter_dimensions: tuple[int, int, int]


def physical_quotient_certificate(
    state_class: StateClassCertificate, gauss: GaussCertificate
) -> PhysicalQuotientCertificate:
    incidence = gauss.incidence
    carrier_constraint = sp.Matrix.vstack(sp.eye(4), incidence)
    carrier_rank = carrier_constraint.rank()
    tt_dimension = carrier_constraint.cols - carrier_rank
    gravity_solution_dimension = 4 - incidence.T.rank()
    ones = sp.ones(4, 1)
    gravity_gauge_dimension = sp.Matrix.hstack(ones).rank()
    gravity_quotient_fiber_dimension = (
        gravity_solution_dimension - gravity_gauge_dimension
    )
    gauge_projector = sp.eye(4) - ones * ones.T / 4

    r0, r1, r2, lam = sp.symbols("q0 q1 q2 quotient_lambda", real=True)
    r3 = -r0 - r1 - r2
    particular = sp.Matrix((0, -r0, -r0 - r1, r3))
    general = particular + lam * ones
    quotient_unique = matrix_zero(
        gauge_projector * general - gauge_projector * particular
    )
    graph_isomorphism_exact = (
        carrier_rank == 4
        and tt_dimension == 0
        and gravity_solution_dimension == 1
        and gravity_gauge_dimension == 1
        and gravity_quotient_fiber_dimension == 0
        and incidence.T.nullspace() == [ones]
        and gauge_projector.rank() == 3
        and matrix_zero(gauge_projector * ones)
        and matrix_zero(gauge_projector**2 - gauge_projector)
        and quotient_unique
        and gauss.symbolic_solution_exact
        and gauss.zero_sum_image_exact
    )
    return PhysicalQuotientCertificate(
        carrier_rank=carrier_rank,
        tt_dimension=tt_dimension,
        gravity_solution_dimension=gravity_solution_dimension,
        gravity_gauge_dimension=gravity_gauge_dimension,
        gravity_quotient_fiber_dimension=gravity_quotient_fiber_dimension,
        graph_isomorphism_exact=graph_isomorphism_exact,
        matter_dimensions=(
            state_class.cone_dimension,
            state_class.normalized_dimension,
            state_class.ray_dimension,
        ),
    )


@dataclass(frozen=True)
class RootFixtureCertificate:
    shear: sp.Rational
    sectors: tuple[object, ...]
    characteristic_polynomials: tuple[sp.Poly, ...]
    taus: tuple[sp.Rational, ...]
    even_identity_exact: bool
    odd_identity_exact: bool
    stable_root_unique: bool
    odd_root_forced: bool
    even_root_forced: bool
    distinct_even_odd: bool
    polynomial_digest: str


@dataclass(frozen=True)
class RootCertificate:
    fixtures: tuple[RootFixtureCertificate, ...]
    all_pairings_forced: bool
    all_even_odd_distinct: bool


def _normalized_characteristic(polynomial: sp.Poly) -> tuple[sp.Poly, sp.Rational]:
    coefficients = tuple(polynomial.all_coeffs())
    if len(coefficients) != 3 or coefficients[0] == 0:
        raise AssertionError("expected a quadratic transfer characteristic polynomial")
    leading, linear, constant = coefficients
    rho = block119.RHO
    normalized = sp.Poly(
        rho**2 + sp.cancel(linear / leading) * rho + sp.cancel(constant / leading),
        rho,
        domain=sp.QQ,
    )
    tau = sp.Rational(-linear, leading)
    return normalized, tau


def root_certificate() -> RootCertificate:
    fixtures: list[RootFixtureCertificate] = []
    for shear in SHEARS:
        sectors = tuple(block119.make_sectors(shear))
        if len(sectors) != 4:
            raise AssertionError("the quotient must have four momentum lines")
        normalized_and_tau = tuple(
            _normalized_characteristic(sector.polynomial) for sector in sectors
        )
        polynomials = tuple(item[0] for item in normalized_and_tau)
        taus = tuple(item[1] for item in normalized_and_tau)
        original_polynomials = tuple(sector.polynomial for sector in sectors)
        palindromic = all(
            polynomial.all_coeffs()[0] == polynomial.all_coeffs()[2]
            and normalized.all_coeffs() == [1, -tau, 1]
            for polynomial, normalized, tau in zip(
                original_polynomials, polynomials, taus
            )
        )
        unique_flags = tuple(
            abs(tau) > 2
            and polynomial.count_roots(-1, 1) == 1
            and polynomial.eval(0) == 1
            for polynomial, tau in zip(polynomials, taus)
        )
        even_identity_exact = (
            original_polynomials[0] == original_polynomials[2]
            and polynomials[0] == polynomials[2]
            and taus[0] == taus[2]
        )
        odd_identity_exact = (
            original_polynomials[1] == original_polynomials[3]
            and polynomials[1] == polynomials[3]
            and taus[1] == taus[3]
        )
        distinct_even_odd = (
            taus[0] != taus[1]
            and sp.gcd(polynomials[0], polynomials[1]).degree() == 0
        )
        fixtures.append(
            RootFixtureCertificate(
                shear=shear,
                sectors=sectors,
                characteristic_polynomials=polynomials,
                taus=taus,
                even_identity_exact=even_identity_exact,
                odd_identity_exact=odd_identity_exact,
                stable_root_unique=palindromic and all(unique_flags),
                odd_root_forced=(
                    odd_identity_exact and unique_flags[1] and unique_flags[3]
                ),
                even_root_forced=(
                    even_identity_exact and unique_flags[0] and unique_flags[2]
                ),
                distinct_even_odd=distinct_even_odd,
                polynomial_digest=exact_digest(
                    tuple(tuple(poly.all_coeffs()) for poly in polynomials)
                ),
            )
        )
    result = tuple(fixtures)
    return RootCertificate(
        fixtures=result,
        all_pairings_forced=all(
            fixture.even_identity_exact
            and fixture.odd_identity_exact
            and fixture.stable_root_unique
            and fixture.even_root_forced
            and fixture.odd_root_forced
            for fixture in result
        ),
        all_even_odd_distinct=all(
            fixture.distinct_even_odd for fixture in result
        ),
    )


@dataclass(frozen=True)
class TransferCertificate:
    transfer_pairing_exact: bool
    balanced_sector_preserved: bool
    exact_invariant_sector: bool
    violation_formula_exact: bool
    rate_difference_nonzero: bool
    convention_free_coincidence: bool
    invariant_dimensions: tuple[int, int, int]


def transfer_certificate(
    state_class: StateClassCertificate, roots: RootCertificate
) -> TransferCertificate:
    n1, n2, n3_free = sp.symbols("n1 n2 n3", nonnegative=True)
    rho_even, rho_odd = sp.symbols(
        "rho_even rho_odd", positive=True
    )
    n3 = n1 + 2 * n2
    transfer = sp.diag(
        rho_even**2, rho_odd**2, rho_even**2, rho_odd**2
    )
    transfer_pairing_exact = (
        transfer[0, 0] == transfer[2, 2] == rho_even**2
        and transfer[1, 1] == transfer[3, 3] == rho_odd**2
        and roots.all_pairings_forced
    )
    post_numerator = sp.expand(
        rho_odd**4 * n1
        + 2 * rho_even**4 * n2
        - rho_odd**4 * n3
    )
    expected_violation = 2 * n2 * (rho_even**4 - rho_odd**4)
    violation_formula_exact = sp.expand(
        post_numerator - expected_violation
    ) == 0
    balanced_post = sp.expand(post_numerator.subs(n2, 0))
    balanced_sector_preserved = (
        balanced_post == 0
        and transfer[2, 2] != 0
        and transfer[1, 1] == transfer[3, 3]
    )
    class_equation = n1 + 2 * n2 - n3_free
    transferred_equation = (
        rho_odd**4 * n1
        + 2 * rho_even**4 * n2
        - rho_odd**4 * n3_free
    )
    stable_intersection = sp.solve(
        (class_equation, transferred_equation),
        (n2, n3_free),
        dict=True,
    )
    stable_intersection_exact = stable_intersection == [
        {n2: 0, n3_free: n1}
    ]
    rate_difference_nonzero = roots.all_even_odd_distinct and all(
        fixture.stable_root_unique
        and sp.gcd(
            fixture.characteristic_polynomials[0],
            fixture.characteristic_polynomials[1],
        ).degree()
        == 0
        for fixture in roots.fixtures
    )
    exact_invariant_sector = (
        violation_formula_exact
        and rate_difference_nonzero
        and balanced_sector_preserved
        and stable_intersection_exact
    )
    convention_free_coincidence = (
        state_class.intersection_exact and exact_invariant_sector
    )
    return TransferCertificate(
        transfer_pairing_exact=transfer_pairing_exact,
        balanced_sector_preserved=balanced_sector_preserved,
        exact_invariant_sector=exact_invariant_sector,
        violation_formula_exact=violation_formula_exact,
        rate_difference_nonzero=rate_difference_nonzero,
        convention_free_coincidence=convention_free_coincidence,
        invariant_dimensions=(5, 4, 3),
    )


@dataclass(frozen=True)
class LocalizationCertificate:
    projectors: tuple[sp.Matrix, ...]
    densities: tuple[sp.Matrix, ...]
    hermitian_exact: bool
    sum_rule_exact: bool
    sandwich_sum_rule_fails: bool
    universal_total_lemma: bool
    pinned_profile: sp.Matrix
    alternative_profile: sp.Matrix
    witness_profile_exact: bool
    profile_convention_dependent: bool
    quotient_structure_independent: bool


def localization_certificate(
    state_class: StateClassCertificate,
    gauss: GaussCertificate,
    transfer: TransferCertificate,
) -> LocalizationCertificate:
    fourier = sp.Matrix(
        4, 4, lambda site_index, momentum: I ** (-site_index * momentum)
    ) / 2
    projectors = tuple(
        sp.simplify(
            fourier.H
            * sp.diag(*(1 if other == site_index else 0 for other in range(4)))
            * fourier
        )
        for site_index in range(4)
    )
    projector_structure_exact = (
        matrix_zero(fourier.H * fourier - sp.eye(4))
        and matrix_zero(sum(projectors, sp.zeros(4)) - sp.eye(4))
        and all(projector.H == projector for projector in projectors)
        and all(matrix_zero(projector**2 - projector) for projector in projectors)
    )
    densities = tuple(
        sp.simplify((projector * P + P * projector) / 2)
        for projector in projectors
    )
    hermitian_exact = projector_structure_exact and all(
        density.H == density for density in densities
    )
    sum_rule_exact = matrix_zero(sum(densities, sp.zeros(4)) - P)

    sandwiched = tuple(projector * P * projector for projector in projectors)
    sandwiched_total = sp.simplify(sum(sandwiched, sp.zeros(4)))
    sandwich_sum_rule_fails = (
        matrix_zero(sandwiched_total - sp.eye(4) / 2)
        and not matrix_zero(sandwiched_total - P)
    )

    entries = sp.symbols("ell0:48")
    arbitrary = tuple(
        sp.Matrix(4, 4, entries[16 * index:16 * (index + 1)])
        for index in range(3)
    )
    fourth = P - sum(arbitrary, sp.zeros(4))
    admissible_family = arbitrary + (fourth,)
    bra = sp.Matrix(1, 4, sp.symbols("bra0:4"))
    ket = sp.Matrix(4, 1, sp.symbols("ket0:4"))
    universal_total_lemma = (
        matrix_zero(sum(admissible_family, sp.zeros(4)) - P)
        and sp.expand(
            sum((bra * density * ket)[0] for density in admissible_family)
            - (bra * P * ket)[0]
        )
        == 0
    )

    witness = state_class.fixtures[1]
    pinned_profile = sp.Matrix(
        [
            sp.simplify(
                (witness.vector.H * density * witness.vector)[0]
                / witness.norm_squared
            )
            for density in densities
        ]
    )
    alternative_densities = (
        densities[0] + sp.eye(4),
        densities[1] - sp.eye(4),
        densities[2],
        densities[3],
    )
    alternative_profile = sp.Matrix(
        [
            sp.simplify(
                (witness.vector.H * density * witness.vector)[0]
                / witness.norm_squared
            )
            for density in alternative_densities
        ]
    )
    alternative_admissible = (
        all(density.H == density for density in alternative_densities)
        and matrix_zero(sum(alternative_densities, sp.zeros(4)) - P)
    )
    witness_profile_exact = (
        pinned_profile == gauss.witness_source
        and sum(pinned_profile) == 0
        and gauss.incidence.T * gauss.witness_mean_zero == pinned_profile
    )
    profile_convention_dependent = (
        alternative_admissible
        and alternative_profile != pinned_profile
        and sum(alternative_profile) == sum(pinned_profile) == 0
    )
    all_fixture_totals_exact = all(
        sp.expand(
            sum(
                (fixture.vector.H * density * fixture.vector)[0]
                / fixture.norm_squared
                for density in densities
            )
            - fixture.momentum / fixture.norm_squared
        )
        == 0
        for fixture in state_class.fixtures
    )
    quotient_structure_independent = (
        universal_total_lemma
        and all_fixture_totals_exact
        and gauss.zero_sum_image_exact
        and transfer.convention_free_coincidence
    )
    return LocalizationCertificate(
        projectors=projectors,
        densities=densities,
        hermitian_exact=hermitian_exact,
        sum_rule_exact=sum_rule_exact,
        sandwich_sum_rule_fails=sandwich_sum_rule_fails,
        universal_total_lemma=universal_total_lemma,
        pinned_profile=pinned_profile,
        alternative_profile=alternative_profile,
        witness_profile_exact=witness_profile_exact,
        profile_convention_dependent=profile_convention_dependent,
        quotient_structure_independent=quotient_structure_independent,
    )


N5_LINES = (
    "N5: per_element: exact quadric, convention-intersection, gauss-solution, orientation, root-identity, sector-preservation, violation, and sum-rule certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: the paired momenta share one characteristic polynomial with the stable root forced, so the balanced sector is transfer-invariant while unbalanced states violate the class by an exact rate difference",
    "per_block: the momentum-sourced gauss quotient is executed — the physical sector is the convention-free stable balanced class with gravity contributing only its quotiented gauge mode, independent of the admissible localization",
    "lattice_wide: checked and not executed — non-local dressings for the observable wall, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the full gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)

SCOPE_KEYS = (
    "sourced_quotient",
    "class_quadric",
    "balanced_sector",
    "forced_root",
    "gauge_mode",
    "zero_gravity_dimensions",
    "cosmetic",
    "structural",
    "orientation",
    "convention_free",
    "admissible_localization",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "displayed_execution",
    "full_gravity_closer",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "sourced_quotient": "sourced quotient" in note,
        "class_quadric": (
            "class quadric" in note
            or "vanishing expected total momentum" in note
        ),
        "balanced_sector": (
            "balanced sector" in note or "|c_1| = |c_3|" in note
        ),
        "forced_root": (
            "forced" in note or "cannot pick different roots" in note
        ),
        "gauge_mode": (
            "gauge mode" in note or "constant mode" in note
        ),
        "zero_gravity_dimensions": (
            "zero independent dimensions" in note
            or "isomorphic to the matter class" in note
        ),
        "cosmetic": "cosmetic" in note,
        "structural": "structural" in note,
        "orientation": (
            "orientation" in note or "forward-difference" in note
        ),
        "convention_free": (
            "convention-free" in note
            or "convention-independent" in note
        ),
        "admissible_localization": (
            "admissible localization" in note or "sum rule" in note
        ),
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "displayed_execution": (
            "sourced quotient" in note
            and ("executes" in note or "executed" in note)
            and "displayed carrier" in note
        ),
        "full_gravity_closer": (
            "gravity constraint quotient remains unexecuted" in note
            and (
                "beyond the displayed carrier" in note
                or "full-gravity" in note
                or "full gravity" in note
            )
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 123 note/runner/cache and ancestors 122--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 123)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    state_class = state_class_certificate()
    quadric_exact = (
        state_class.forms_exact
        and state_class.c0_free
        and state_class.dimensions_convention_invariant
        and state_class.sets_differ_off_c2_zero
        and state_class.intersection_exact
        and (
            state_class.cone_dimension,
            state_class.normalized_dimension,
            state_class.ray_dimension,
        )
        == (7, 6, 5)
        and all(
            fixture.norm_squared > 0 and fixture.momentum == 0
            for fixture in state_class.fixtures
        )
    )
    if mutation == "break_quadric":
        quadric_exact = False
    convention_free_class_claimed = mutation == "claim_convention_free_class"
    checks.check(
        "B-the-class-quadric",
        "|c1|^2+2|c2|^2=|c3|^2 with c0 free has dims 7/6/5; p2=-2 differs off c2=0 and agrees exactly on the balanced intersection",
        quadric_exact and not convention_free_class_claimed,
    )

    gauss = gauss_certificate()
    gauss_exact = (
        gauss.orientation_exact
        and gauss.zero_sum_image_exact
        and gauss.symbolic_solution_exact
        and gauss.gauge_kernel_exact
        and gauss.witness_exact
    )
    if mutation == "break_gauss_solution":
        gauss_exact = False
    orientation_exact = gauss.opposite_orientation_fails
    if mutation == "break_orientation_pin":
        orientation_exact = False
    checks.check(
        "C-the-gauss-solution",
        "(B4^T Gamma)_j=Gamma_j-Gamma_{j+1}; the closed form and mean-zero witness solve it, while the opposite orientation fails",
        gauss_exact and orientation_exact,
    )

    quotient = physical_quotient_certificate(state_class, gauss)
    quotient_exact = (
        quotient.graph_isomorphism_exact
        and quotient.carrier_rank == 4
        and quotient.tt_dimension == 0
        and quotient.gravity_solution_dimension == 1
        and quotient.gravity_gauge_dimension == 1
        and quotient.gravity_quotient_fiber_dimension == 0
        and quotient.matter_dimensions == (7, 6, 5)
    )
    if mutation == "break_quotient_isomorphism":
        quotient_exact = False
    checks.check(
        "D-the-physical-quotient",
        "the d=2 sourced graph modulo its constant gauge mode is isomorphic to the matter class and gravity adds zero independent dimensions",
        quotient_exact,
    )

    roots = root_certificate()
    root_identity_exact = (
        len(roots.fixtures) == 2
        and roots.all_pairings_forced
        and roots.all_even_odd_distinct
        and all(
            fixture.even_identity_exact
            and fixture.odd_identity_exact
            and fixture.stable_root_unique
            and fixture.even_root_forced
            and fixture.odd_root_forced
            and fixture.distinct_even_odd
            for fixture in roots.fixtures
        )
    )
    if mutation == "break_root_identity":
        root_identity_exact = False
    checks.check(
        "E-the-forced-root-identity",
        "k=0,2 and k=1,3 have identical characteristic polynomials; |tau|>2 uniquely forces each |rho|<1 root, with rho_even!=rho_odd",
        root_identity_exact,
    )

    transfer = transfer_certificate(state_class, roots)
    sector_exact = (
        transfer.transfer_pairing_exact
        and transfer.balanced_sector_preserved
        and transfer.exact_invariant_sector
        and transfer.rate_difference_nonzero
        and transfer.convention_free_coincidence
        and transfer.invariant_dimensions == (5, 4, 3)
    )
    if mutation == "break_sector_preservation":
        sector_exact = False
    violation_exact = transfer.violation_formula_exact
    if mutation == "break_violation_formula":
        violation_exact = False
    checks.check(
        "F-the-stable-balanced-sector",
        "diag(rho_k^2) preserves exactly c2=0, |c1|=|c3|; every c2!=0 class state acquires 2|c2|^2(rho_even^4-rho_odd^4)!=0",
        sector_exact and violation_exact,
    )

    localization = localization_certificate(state_class, gauss, transfer)
    localization_exact = (
        localization.hermitian_exact
        and localization.sum_rule_exact
        and localization.sandwich_sum_rule_fails
        and localization.universal_total_lemma
        and localization.witness_profile_exact
        and localization.profile_convention_dependent
        and localization.quotient_structure_independent
    )
    if mutation == "break_sum_rule":
        localization_exact = False
    structural_localization_claimed = mutation == "claim_structural_localization"
    checks.check(
        "G-the-localization-verdict",
        "D_x={E_x,P}/2 is admissible, E_xPE_x is not; any admissible sum gives total <P>, so only the profile is conventional",
        localization_exact and not structural_localization_claimed,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required sourced-quotient/convention/root/gauge/localization/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "CLASS QUADRIC: <P>=0 iff |c1|^2+2|c2|^2=|c3|^2 with c0 free; "
        "explicit cone/normalized/ray parametrization ranks=7/6/5."
    )
    print(
        "CONVENTION INTERSECTION: p2=+2 and p2=-2 define different classes for c2!=0; "
        "their exact common class is c2=0, |c1|=|c3|, with convention-invariant dimensions."
    )
    print(
        "GAUSS ORIENTATION: rho=(2/9,-1/9,0,-1/9) has Gamma_mean0="
        f"{tuple(gauss.witness_mean_zero)} under Gamma_j-Gamma_(j+1); the opposite sign fails."
    )
    print(
        "PHYSICAL QUOTIENT: d=2 TT dimension=0 and gravity solution/gauge/physical-fiber dimensions="
        f"{quotient.gravity_solution_dimension}/{quotient.gravity_gauge_dimension}/"
        f"{quotient.gravity_quotient_fiber_dimension}; the graph is the matter class."
    )
    print(
        "FORCED ROOTS: k0=k2 and k1=k3 in both fixtures, with unique stable roots and tau_even!=tau_odd; "
        "polynomial sha="
        + "/".join(fixture.polynomial_digest for fixture in roots.fixtures)
        + "."
    )
    print(
        "STABLE BALANCED SECTOR: c2=0, |c1|=|c3| is exactly transfer-invariant; "
        "the unbalanced violation is 2|c2|^2(rho_even^4-rho_odd^4)."
    )
    print(
        "LOCALIZATION: pinned admissible D_x gives witness profile="
        f"{tuple(localization.pinned_profile)}; profile choice is cosmetic, while the total sum rule and quotient structure are structural."
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the lane's first physical gravity quotient exists and carries dynamics — the convention-free transfer-stable balanced sector with exact gauss solutions unique up to the constant gauge mode, its structure independent of the admissible localization"
    )
    print(
        "DECISION_CUT: advance non-local dressings and the naturality classification; reject unbalanced-sector and inadmissible-localization constructions"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
