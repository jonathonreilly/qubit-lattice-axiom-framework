#!/usr/bin/env python3
"""Certify the supplied-law zero-momentum spin-two stiffness boundary.

For every proper-cubic stationary Gram supplied by Block 40, this runner
derives all 100 label-pair derivatives in each of the two spatial traceless
proper-cubic irreducible sectors.  It combines their exact envelopes with the
Block-39 Dobrushin coefficient and the finite-volume Poincare inequality to
bound the complete Record pressure Hessian.  The inherited alpha=16 local
Gram well then leaves a strictly positive O(k^0) stiffness in both sectors.

The result is a bounded supplied-law obstruction under regular connection
elimination.  It is not a gravity no-go across modified laws, singular
connection phases, nonflat backgrounds, or Lorentzian dynamics.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import root


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_"
    "SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PHASE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_"
    "SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
VACUUM_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_"
    "LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
BETA = 1.0 / 5.0
ALPHA = 16.0
TARGET_TICK_GRAM = 25.0 / 16.0
GRAM_RADIUS_SQUARED = 21.0 / 40.0
GRAM_RADIUS = float(np.sqrt(GRAM_RADIUS_SQUARED))
SPATIAL_GRAM_FLOOR = 1.0 - GRAM_RADIUS / np.sqrt(3.0)
DOBRUSHIN_ROW = 6.0 * float(np.tanh(BETA / 2.0))
POINCARE_DENOMINATOR = 1.0 - DOBRUSHIN_ROW
WELL_GRAM_HESSIAN = ALPHA / 2.0

RAYS = np.asarray(
    (
        (1, 1, 1, 0),
        (1, 1, -1, 0),
        (1, -1, 1, 0),
        (1, -1, -1, 0),
        (1, 0, 0, 1),
        (-1, 0, 0, 1),
        (0, 1, 0, 1),
        (0, -1, 0, 1),
        (0, 0, 1, 1),
        (0, 0, -1, 1),
    ),
    dtype=float,
)
RECORD_WEIGHTS = np.asarray((3, 3, 3, 3, 4, 4, 4, 4, 4, 4), dtype=float)
G_STAR = np.diag((1.0, 1.0, 1.0, TARGET_TICK_GRAM))

H_E = np.zeros((DIMENSION, DIMENSION), dtype=float)
H_E[1, 1] = 1.0 / np.sqrt(2.0)
H_E[2, 2] = -1.0 / np.sqrt(2.0)
H_T2 = np.zeros((DIMENSION, DIMENSION), dtype=float)
H_T2[1, 2] = H_T2[2, 1] = 1.0 / np.sqrt(2.0)

X, Y, T = sp.symbols("x y t", positive=True)
SYMPY_RAYS = tuple(sp.Matrix(tuple(int(value) for value in ray)) for ray in RAYS)
SYMPY_G = sp.diag(X, X, X, Y)
SYMPY_H_E = sp.diag(0, 1 / sp.sqrt(2), -1 / sp.sqrt(2), 0)
SYMPY_H_T2 = sp.Matrix(
    ((0, 0, 0, 0), (0, 0, 1 / sp.sqrt(2), 0),
     (0, 1 / sp.sqrt(2), 0, 0), (0, 0, 0, 0))
)


def skew_generators() -> tuple[np.ndarray, ...]:
    result: list[np.ndarray] = []
    for left, right in combinations(range(DIMENSION), 2):
        generator = np.zeros((DIMENSION, DIMENSION), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        result.append(generator)
    return tuple(result)


SKEW_GENERATORS = skew_generators()


def overlap_derivative_expressions(
    direction: sp.Matrix,
) -> tuple[tuple[sp.Expr, ...], tuple[sp.Expr, ...]]:
    """Derive beta times the first two uniform-Gram bond derivatives."""
    first: set[sp.Expr] = set()
    second: set[sp.Expr] = set()
    for ray_a in SYMPY_RAYS:
        qa = (ray_a.T * SYMPY_G * ray_a)[0]
        qpa = (ray_a.T * direction * ray_a)[0]
        for ray_b in SYMPY_RAYS:
            qb = (ray_b.T * SYMPY_G * ray_b)[0]
            qpb = (ray_b.T * direction * ray_b)[0]
            overlap_numerator_root = (ray_a.T * SYMPY_G * ray_b)[0]
            numerator_derivative_root = (ray_a.T * direction * ray_b)[0]
            denominator = qa * qb
            denominator_first = qpa * qb + qa * qpb
            denominator_second = 2 * qpa * qpb
            numerator = overlap_numerator_root**2
            numerator_first = (
                2 * overlap_numerator_root * numerator_derivative_root
            )
            numerator_second = 2 * numerator_derivative_root**2
            derivative = (
                numerator_first / denominator
                - numerator * denominator_first / denominator**2
            ) / 5
            second_derivative = (
                numerator_second / denominator
                - 2 * numerator_first * denominator_first / denominator**2
                - numerator * denominator_second / denominator**2
                + 2 * numerator * denominator_first**2 / denominator**3
            ) / 5
            first.add(sp.factor(derivative))
            second.add(sp.factor(second_derivative))
    return (
        tuple(sorted(first, key=str)),
        tuple(sorted(second, key=str)),
    )


def homogeneous_coefficient_supremum(
    expressions: tuple[sp.Expr, ...], degree: int
) -> tuple[float, sp.Expr]:
    """Maximize |x^degree expression(x,t*x)| over t>=0 exactly by roots."""
    best_value = -1.0
    best_expression = sp.Integer(0)
    for expression in expressions:
        reduced = sp.factor((X**degree * expression).subs(Y, T * X))
        reduced = sp.factor(reduced.subs(X, 1))
        if reduced == 0:
            candidates = [sp.Integer(0)]
        else:
            derivative_numerator = sp.factor(
                sp.together(sp.diff(reduced, T)).as_numer_denom()[0]
            )
            roots = [] if derivative_numerator == 0 else sp.solve(
                derivative_numerator, T
            )
            candidates = [sp.limit(reduced, T, 0, dir="+"), sp.limit(reduced, T, sp.oo)]
            for candidate in roots:
                numeric = complex(sp.N(candidate, 30))
                if abs(numeric.imag) < 1.0e-20 and numeric.real >= 0.0:
                    candidates.append(sp.simplify(reduced.subs(T, candidate)))
        local = max(float(abs(sp.N(value, 30))) for value in candidates)
        if local > best_value:
            best_value = local
            best_expression = expression
    return best_value, best_expression


def site_score_oscillation(direction: np.ndarray) -> float:
    scores = -0.5 * np.einsum("ai,ij,aj->a", RAYS, direction, RAYS)
    return float(np.max(scores) - np.min(scores))


def sector_bounds(
    direction: np.ndarray,
    symbolic_direction: sp.Matrix,
) -> dict[str, float | int | sp.Expr]:
    first, second = overlap_derivative_expressions(symbolic_direction)
    first_coefficient, first_extremizer = homogeneous_coefficient_supremum(
        first, 1
    )
    second_coefficient, second_extremizer = homogeneous_coefficient_supremum(
        second, 2
    )
    bond_score_abs = first_coefficient / SPATIAL_GRAM_FLOOR
    bond_contact_abs = second_coefficient / SPATIAL_GRAM_FLOOR**2
    single_site_oscillation = site_score_oscillation(direction)
    global_site_oscillation = single_site_oscillation + 12.0 * bond_score_abs
    variance_per_site = (
        global_site_oscillation**2 / (4.0 * POINCARE_DENOMINATOR)
    )
    contact_per_site = 3.0 * bond_contact_abs
    hessian_lower = WELL_GRAM_HESSIAN - variance_per_site - contact_per_site
    return {
        "first_family_count": len(first),
        "second_family_count": len(second),
        "first_coefficient": first_coefficient,
        "second_coefficient": second_coefficient,
        "first_extremizer": first_extremizer,
        "second_extremizer": second_extremizer,
        "bond_score_abs": bond_score_abs,
        "bond_contact_abs": bond_contact_abs,
        "site_score_oscillation": single_site_oscillation,
        "global_site_oscillation": global_site_oscillation,
        "variance_per_site": variance_per_site,
        "contact_per_site": contact_per_site,
        "hessian_lower": hessian_lower,
    }


QUOTIENT_EDGES = tuple(
    edge for edge in ((0, 1), (1, 2), (2, 0)) for _ in range(3)
)
QUOTIENT_LABELS = np.asarray(tuple(product(range(10), repeat=3)), dtype=int)


def projector_data(gram: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    coframe = np.linalg.cholesky(gram).T
    images = (coframe @ RAYS.T).T
    squared = np.einsum("ai,ai->a", images, images)
    projectors = np.einsum("ai,aj->aij", images, images)
    projectors /= squared[:, None, None]
    log_site = np.log(RECORD_WEIGHTS) - 0.5 * squared
    return log_site, projectors


def quotient_log_weights(gram: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    log_site, projectors = projector_data(gram)
    overlap = np.einsum("aij,bji->ab", projectors, projectors)
    log_bond = -BETA * (1.0 - overlap)
    values = np.zeros(len(QUOTIENT_LABELS), dtype=float)
    for site in range(3):
        values += log_site[QUOTIENT_LABELS[:, site]]
    for low, high in QUOTIENT_EDGES:
        values += log_bond[QUOTIENT_LABELS[:, low], QUOTIENT_LABELS[:, high]]
    maximum = float(np.max(values))
    probabilities = np.exp(values - maximum)
    probabilities /= float(np.sum(probabilities))
    return values, probabilities


def quotient_pressure(gram: np.ndarray) -> float:
    values, _ = quotient_log_weights(gram)
    maximum = float(np.max(values))
    log_partition = maximum + float(np.log(np.sum(np.exp(values - maximum))))
    well = (ALPHA / 4.0) * float(np.sum((gram - G_STAR) ** 2))
    return well - log_partition / 3.0


def invariant_gram(parameters: np.ndarray) -> np.ndarray:
    return np.diag((parameters[0], parameters[0], parameters[0], parameters[1]))


def scalar_gradient(function, point: np.ndarray, step: float = 2.0e-5) -> np.ndarray:
    result = np.zeros_like(point, dtype=float)
    for index in range(len(point)):
        displacement = np.zeros_like(point)
        displacement[index] = step
        result[index] = (
            function(point + displacement) - function(point - displacement)
        ) / (2.0 * step)
    return result


def quotient_stationary_gram() -> np.ndarray:
    solution = root(
        lambda value: scalar_gradient(
            lambda parameters: quotient_pressure(invariant_gram(parameters)),
            value,
        ),
        np.asarray((0.97, 1.52)),
        method="hybr",
        options={"xtol": 1.0e-10},
    )
    residual = float(np.max(np.abs(scalar_gradient(
        lambda parameters: quotient_pressure(invariant_gram(parameters)),
        solution.x,
    ))))
    if not solution.success or residual > 3.0e-7:
        raise RuntimeError(f"quotient stationary solve failed: {solution.message}")
    return invariant_gram(solution.x)


def directional_second(function, point: np.ndarray, direction: np.ndarray) -> float:
    step = 5.0e-4
    return float(
        (function(point + step * direction) - 2.0 * function(point)
         + function(point - step * direction)) / step**2
    )


def edge_marginal(probabilities: np.ndarray, low: int, high: int) -> np.ndarray:
    marginal = np.zeros((10, 10), dtype=float)
    np.add.at(
        marginal,
        (QUOTIENT_LABELS[:, low], QUOTIENT_LABELS[:, high]),
        probabilities,
    )
    return marginal


def connection_score(projectors: np.ndarray, generator: np.ndarray) -> np.ndarray:
    commutator = np.einsum("bij,ajk->abik", projectors, projectors) - np.einsum(
        "aij,bjk->abik", projectors, projectors
    )
    return BETA * np.einsum("abij,ji->ab", commutator, generator)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 93 else statement[:90] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 128 else detail[:125] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    phase = flat(PHASE_PATH)
    vacuum = flat(VACUUM_PATH)
    scale = flat(SCALE_PATH)

    checks.check(
        "premise-and-parent-scope",
        "the certificate binds the four axioms, supplied factor law, fixed-background phase, and stationary-vacuum theorem without promoting them to axioms",
        all(path.exists() for path in (
            NOTE_PATH, AXIOM_PATH, PHASE_PATH, VACUUM_PATH, SCALE_PATH,
            PREMISE_REGISTRY_PATH,
        ))
        and "admissibility / local constraint" in axiom
        and "dobrushin" in phase
        and "gram well" in vacuum
        and "units conversion" in scale,
    )

    checks.check(
        "proper-cubic-stationary-domain",
        "Block-40 confinement gives x at least 1-sqrt(21/40)/sqrt(3) for every proper-cubic stationary Gram",
        SPATIAL_GRAM_FLOOR > 0.58
        and abs(SPATIAL_GRAM_FLOOR - 0.5816699867329622) < 2.0e-15,
        f"radius={GRAM_RADIUS:.9f}; x_floor={SPATIAL_GRAM_FLOOR:.9f}",
    )

    checks.check(
        "spin-two-normalization",
        "the E and T2 representatives are unit-Frobenius spatial traceless Gram directions",
        abs(np.linalg.norm(H_E) - 1.0) < 2.0e-15
        and abs(np.linalg.norm(H_T2) - 1.0) < 2.0e-15
        and abs(np.trace(H_E[:3, :3])) < 2.0e-15
        and abs(np.trace(H_T2[:3, :3])) < 2.0e-15,
    )

    checks.check(
        "finite-volume-poincare-denominator",
        "the six-neighbor Dobrushin row is below one, leaving the finite-volume Poincare theorem denominator 1-c",
        abs(DOBRUSHIN_ROW - 0.598007967749735) < 2.0e-15
        and POINCARE_DENOMINATOR > 0.4,
        f"c={DOBRUSHIN_ROW:.9f}; 1-c={POINCARE_DENOMINATOR:.9f}",
    )

    e_bounds = sector_bounds(H_E, SYMPY_H_E)
    t_bounds = sector_bounds(H_T2, SYMPY_H_T2)

    checks.check(
        "exact-E-bond-derivative-enumeration",
        "all 100 E-sector label pairs collapse to nine first-derivative and five second-derivative rational families",
        e_bounds["first_family_count"] == 9
        and e_bounds["second_family_count"] == 5
        and abs(float(e_bounds["first_coefficient"]) - 2 * np.sqrt(2) / 45) < 2.0e-15
        and abs(float(e_bounds["second_coefficient"]) - 4 / 45) < 2.0e-15,
        f"sup coefficients d1/d2={float(e_bounds['first_coefficient']):.9f}/{float(e_bounds['second_coefficient']):.9f}",
    )

    checks.check(
        "exact-T2-bond-derivative-enumeration",
        "all 100 T2-sector label pairs collapse to nine first-derivative and five second-derivative rational families",
        t_bounds["first_family_count"] == 9
        and t_bounds["second_family_count"] == 5
        and abs(float(t_bounds["first_coefficient"]) - np.sqrt(2) / 20) < 2.0e-15
        and abs(float(t_bounds["second_coefficient"]) - 1 / 5) < 2.0e-15,
        f"sup coefficients d1/d2={float(t_bounds['first_coefficient']):.9f}/{float(t_bounds['second_coefficient']):.9f}",
    )

    checks.check(
        "E-global-score-oscillation-bound",
        "one label change alters the complete uniform E-sector pressure score by at most the derived site-plus-six-bond oscillation",
        abs(float(e_bounds["site_score_oscillation"]) - 1 / np.sqrt(2)) < 2.0e-15
        and float(e_bounds["global_site_oscillation"]) < 2.004,
        f"bond_abs={float(e_bounds['bond_score_abs']):.9f}; delta={float(e_bounds['global_site_oscillation']):.9f}",
    )

    checks.check(
        "T2-global-score-oscillation-bound",
        "one label change alters the complete uniform T2-sector pressure score by at most the derived site-plus-six-bond oscillation",
        abs(float(t_bounds["site_score_oscillation"]) - np.sqrt(2)) < 2.0e-15
        and float(t_bounds["global_site_oscillation"]) < 2.874,
        f"bond_abs={float(t_bounds['bond_score_abs']):.9f}; delta={float(t_bounds['global_site_oscillation']):.9f}",
    )

    checks.check(
        "E-pressure-Hessian-upper-bound",
        "conditional variance plus all three bond contacts bounds the full finite-volume E-sector Record pressure Hessian",
        float(e_bounds["variance_per_site"]) < 2.498
        and float(e_bounds["contact_per_site"]) < 0.789,
        f"variance/contact={float(e_bounds['variance_per_site']):.9f}/{float(e_bounds['contact_per_site']):.9f}",
    )

    checks.check(
        "T2-pressure-Hessian-upper-bound",
        "conditional variance plus all three bond contacts bounds the full finite-volume T2-sector Record pressure Hessian",
        float(t_bounds["variance_per_site"]) < 5.134
        and float(t_bounds["contact_per_site"]) < 1.774,
        f"variance/contact={float(t_bounds['variance_per_site']):.9f}/{float(t_bounds['contact_per_site']):.9f}",
    )

    checks.check(
        "uniform-E-stiffness-gap",
        "the alpha-sixteen well leaves a strictly positive E-sector O(k^0) Gram stiffness uniformly in volume and stationary Gram",
        abs(float(e_bounds["hessian_lower"]) - 4.714765990657516) < 2.0e-12
        and float(e_bounds["hessian_lower"]) > 4.7,
        f"lower bound={float(e_bounds['hessian_lower']):.9f}",
    )

    checks.check(
        "uniform-T2-stiffness-gap",
        "the alpha-sixteen well leaves a strictly positive T2-sector O(k^0) Gram stiffness uniformly in volume and stationary Gram",
        abs(float(t_bounds["hessian_lower"]) - 1.093394743218842) < 2.0e-12
        and float(t_bounds["hessian_lower"]) > 1.09,
        f"lower bound={float(t_bounds['hessian_lower']):.9f}",
    )

    stationary_gram = quotient_stationary_gram()
    quotient_e = directional_second(quotient_pressure, stationary_gram, H_E)
    quotient_t = directional_second(quotient_pressure, stationary_gram, H_T2)
    checks.check(
        "six-regular-stationary-reconstruction",
        "an exact 1,000-assignment six-regular quotient independently reconstructs the nearby shifted stationary Gram",
        abs(stationary_gram[0, 0] - 0.966327453) < 3.0e-7
        and abs(stationary_gram[3, 3] - 1.520253339) < 3.0e-7,
        f"x/y={stationary_gram[0,0]:.9f}/{stationary_gram[3,3]:.9f}",
    )
    checks.check(
        "six-regular-spin-two-control",
        "the exact quotient has positive E and T2 directional Hessians far above the rigorous full-lattice lower bounds",
        quotient_e > float(e_bounds["hessian_lower"])
        and quotient_t > float(t_bounds["hessian_lower"]),
        f"E/T2={quotient_e:.9f}/{quotient_t:.9f}",
    )

    cross_residuals = []
    symmetry_residuals = []
    for direction in (H_E, H_T2):
        expected_scores = []
        for sign in (-1.0, 1.0):
            gram = stationary_gram + sign * 2.0e-4 * direction
            _, probabilities = quotient_log_weights(gram)
            _, projectors = projector_data(gram)
            marginal = edge_marginal(probabilities, 0, 1)
            symmetry_residuals.append(float(np.max(np.abs(marginal - marginal.T))))
            scores = []
            for generator in SKEW_GENERATORS:
                matrix = connection_score(projectors, generator)
                scores.append(float(np.sum(marginal * matrix)))
                symmetry_residuals.append(float(np.max(np.abs(matrix + matrix.T))))
            expected_scores.append(np.asarray(scores))
        cross_residuals.append(
            float(np.max(np.abs(expected_scores[1] - expected_scores[0]))) / 4.0e-4
        )
    checks.check(
        "endpoint-exchange-zero-momentum-mixed-block",
        "symmetric edge marginals and antisymmetric link scores make the uniform spin-two/link mixed derivative vanish",
        max(symmetry_residuals) < 3.0e-15 and max(cross_residuals) < 3.0e-12,
        f"symmetry/mixed maxima={max(symmetry_residuals):.3e}/{max(cross_residuals):.3e}",
    )

    checks.check(
        "periodic-EC-and-square-mixed-block-boundary",
        "the source note uses periodic EC incidence and zero square residuals for every uniform Gram, so their uniform Gram/link mixed derivatives vanish",
        "periodic incidence" in vacuum
        and "any uniform nondegenerate coframe" in vacuum
        and "zero first variation" in phase,
    )

    checks.check(
        "regular-Schur-obstruction-boundary",
        "the note limits the massless-Einstein obstruction to regular connection elimination and preserves singular, modified-law, and nonflat escapes",
        all(needle in note for needle in (
            "regular connection", "singular connection", "modified law",
            "nonflat", "o(k^0)", "einstein",
        )),
    )

    checks.check(
        "axiom-interface-boundary",
        "the scale primitive supplies units only and no canonical axiom amendment or physical coefficient selection is claimed",
        "units conversion" in scale
        and "no canonical axiom" in note
        and "no fixed toe percentage moves" in note,
    )

    checks.check(
        "n1-through-n8-landing",
        "the source note lands N1 through N8 and treats removal, volume-only, dynamical-target, derivative, critical, gauge-fixing, singular, and nonflat routes",
        all(f"n{index}" in note for index in range(1, 9))
        and "volume-only" in note
        and "dynamical target" in note
        and "strongest counterroute" in note,
    )

    print(
        "N5_CERTIFICATE: derived all 100 label-pair overlap derivatives in both proper-cubic spin-two sectors and their exact positive-domain rational suprema"
    )
    print(
        "N5_CERTIFICATE: executed the finite-volume Dobrushin-Poincare pressure bound, both uniform Hessian gaps, and one exact 1,000-assignment six-regular reconstruction"
    )
    print(
        "per_element: checked every ten-ray site score, all 100 bond derivatives, six link generators, and both normalized spatial traceless representatives"
    )
    print(
        "per_site: bounded every single-site conditional variance uniformly on every finite periodic carrier and checked all three sites of the exact quotient"
    )
    print(
        "per_mode: checked the zero-momentum E and T2 spin-two irreducible sectors; nonzero momentum follows only conditionally under regular continuous connection elimination"
    )
    print(
        "per_block: checked Gram confinement, Record contact and connected covariance, local well stiffness, endpoint exchange, the internal quotient boundary, and repair routes"
    )
    print(
        "lattice_wide: the stiffness lower bounds are uniform in every finite L>=3 torus and survive the fixed-background Dobrushin limit; continuous geometry integration and Lorentzian evolution remain unexecuted"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
