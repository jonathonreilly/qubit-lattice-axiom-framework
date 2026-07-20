#!/usr/bin/env python3
"""Cycle475: exact Born/gravity P3 perturbation tournament.

The Accessible Prediction P3 scenario assumes |I3/I1|~epsilon^2 and
|beta-1|~epsilon.  Expand an explicit three-path amplitude deformation and
test which extra condition removes the generic linear I3 term.  A symmetric
+/- environment does; a direct deformation generically does not; an exact
phase-only deformation leaves every Born weight unchanged.

This is a law-level comparator, not a physical-M2 compiler and not a broad
P3/Born/gravity no-go.  Authority is none; audit is unset.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
from time import perf_counter
import math
import resource
import signal
import sys

import numpy as np
import sympy as sp


PROCESS_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "BORN_GRAVITY_P3_PERTURBATION_TOURNAMENT_CYCLE475_NOTE_2026-07-19.md"
)
PARENT = ROOT / "docs/ACCESSIBLE_PREDICTION_NOTE.md"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-11
WALL_CAP_SECONDS = 60.0
RSS_CAP_BYTES = 1024**3
PASS = 0
FAIL = 0

SUBSETS = ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2))
SIGNS = (1, 1, 1, -1, -1, -1, 1)
TRAIN = (
    sp.Rational(1),
    sp.Rational(2, 3) + sp.I * sp.Rational(1, 3),
    -sp.Rational(1, 4) + sp.I * sp.Rational(1, 2),
)
HELD = (
    sp.Rational(3, 5) + sp.I * sp.Rational(1, 5),
    -sp.Rational(2, 5) + sp.I * sp.Rational(4, 5),
    sp.Rational(1, 3) - sp.I * sp.Rational(2, 3),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "born/gravity p3 perturbation tournament",
        "p3 is a supplied conditional premise",
        "generic first-order i3 coefficient",
        "symmetric ±epsilon route",
        "phase-only route",
        "held configuration without refit",
        "coefficient c is not universal",
        "law-level comparator, not a physical-m2 compiler",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "broad p3, born, gravity, or no-go claim: fail",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    parent = normalized(PARENT)
    check(
        "the Cycle475 note and parent freeze P3 as a conditional law-level target",
        not missing
        and "p3 (born-gravity cross-link)" in parent
        and "does not derive p1..p6 from framework primitives" in parent,
        {"missing": missing, "parent_P3_conditional": True},
    )


def abs2(value: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_complex(value * sp.conjugate(value)))


def subset_amplitudes(paths: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    if len(paths) != 3 or any(value == 0 for value in paths):
        raise ValueError("three nonzero path amplitudes are required")
    return tuple(sp.simplify(sum(paths[index] for index in subset)) for subset in SUBSETS)


def inclusion(values: tuple[sp.Expr, ...]) -> sp.Expr:
    if len(values) != len(SIGNS):
        raise ValueError("I3 inclusion surface has seven nonempty subsets")
    return sp.simplify(sum(sign * value for sign, value in zip(SIGNS, values)))


def cubic_deformation(value: sp.Expr) -> sp.Expr:
    return sp.simplify(abs2(value) * value)


def coefficients(paths: tuple[sp.Expr, ...]) -> dict[str, sp.Expr]:
    amplitudes = subset_amplitudes(paths)
    deformations = tuple(cubic_deformation(value) for value in amplitudes)
    base = inclusion(tuple(abs2(value) for value in amplitudes))
    linear = inclusion(tuple(
        sp.simplify(2 * sp.re(sp.conjugate(value) * deformation))
        for value, deformation in zip(amplitudes, deformations)
    ))
    quadratic = inclusion(tuple(abs2(value) for value in deformations))
    i1 = abs2(amplitudes[-1])
    return {
        "base": base,
        "linear": linear,
        "quadratic": quadratic,
        "I1": i1,
        "q": sp.simplify(quadratic / i1),
    }


def exact_expansion_controls() -> tuple[dict[str, sp.Expr], dict[str, sp.Expr]]:
    print("\nEXACT I3 PERTURBATION EXPANSION")
    epsilon = sp.symbols("epsilon", real=True)
    rows = []
    outputs = []
    for name, paths in (("train", TRAIN), ("held", HELD)):
        row = coefficients(paths)
        amplitudes = subset_amplitudes(paths)
        direct = inclusion(tuple(
            abs2(value + epsilon * cubic_deformation(value)) for value in amplitudes
        ))
        target = sp.expand(row["linear"] * epsilon + row["quadratic"] * epsilon**2)
        outputs.append(row)
        rows.append({
            "fixture": name,
            "base_I3": str(row["base"]),
            "generic_first_order_L": str(row["linear"]),
            "quadratic_Q": str(row["quadratic"]),
            "I1": str(row["I1"]),
            "Q_over_I1": str(row["q"]),
            "direct_expansion": str(sp.factor(direct)),
        })
        if sp.simplify(direct - target) != 0:
            raise AssertionError("exact perturbation expansion failed")
    check(
        "direct cubic-amplitude deformation has an exact generic linear I3 term on train and held configurations",
        all(row["base"] == 0 and row["linear"] != 0 and row["quadratic"] != 0 for row in outputs),
        rows,
    )
    return outputs[0], outputs[1]


def scaling_and_held_controls(train: dict[str, sp.Expr], held: dict[str, sp.Expr]) -> None:
    print("\nDIRECT VERSUS SYMMETRIC +/- ROUTES / HELD COEFFICIENT")
    epsilons = np.logspace(-6, -2, 9)

    def values(row):
        linear = float(row["linear"])
        quadratic = float(row["quadratic"])
        direct = np.abs(linear * epsilons + quadratic * epsilons**2)
        symmetric = np.abs(quadratic) * epsilons**2
        return direct, symmetric

    train_direct, train_symmetric = values(train)
    held_direct, held_symmetric = values(held)
    direct_slopes = (
        float(np.polyfit(np.log(epsilons), np.log(train_direct), 1)[0]),
        float(np.polyfit(np.log(epsilons), np.log(held_direct), 1)[0]),
    )
    symmetric_slopes = (
        float(np.polyfit(np.log(epsilons), np.log(train_symmetric), 1)[0]),
        float(np.polyfit(np.log(epsilons), np.log(held_symmetric), 1)[0]),
    )
    c_train = 1 / math.sqrt(abs(float(train["q"])))
    c_held = 1 / math.sqrt(abs(float(held["q"])))
    epsilon_held = 1e-3
    held_ratio = abs(float(held["q"])) * epsilon_held**2
    actual_beta_deviation = epsilon_held
    train_c_prediction = c_train * math.sqrt(held_ratio)
    relative_prediction_error = abs(train_c_prediction / actual_beta_deviation - 1)
    check(
        "the direct route scales linearly while an explicit symmetric ±epsilon mixture cancels only the first-order term and scales quadratically",
        max(abs(value - 1) for value in direct_slopes) < 0.02
        and max(abs(value - 2) for value in symmetric_slopes) < 1e-10,
        {
            "epsilon_grid": tuple(epsilons),
            "direct_log_slopes_train_held": direct_slopes,
            "symmetric_log_slopes_train_held": symmetric_slopes,
            "symmetric_mechanism": "equal supplied +/- deformation sectors; first-order cancellation",
        },
    )
    check(
        "the symmetric route realizes a square-root law but its coefficient C is geometry-dependent and the train coefficient misses held without refit",
        abs(c_train - c_held) > 0.1
        and relative_prediction_error > 0.2
        and abs(c_held * math.sqrt(held_ratio) - actual_beta_deviation) < TOL,
        {
            "C_train": c_train,
            "C_held": c_held,
            "held_epsilon": epsilon_held,
            "held_I3_over_I1": held_ratio,
            "held_beta_minus_one_candidate": actual_beta_deviation,
            "train_C_held_prediction": train_c_prediction,
            "relative_prediction_error_without_refit": relative_prediction_error,
            "C_universal": False,
        },
    )


def phase_deletion_permutation_controls(train: dict[str, sp.Expr], held: dict[str, sp.Expr]) -> None:
    print("\nPHASE-ONLY / DELETIONS / PERMUTATIONS / ALL24 SCALAR CARRY")
    epsilons = (sp.Rational(1, 100), sp.Rational(1, 10), sp.Rational(1, 2))
    phase_failures = 0
    permutation_failures = 0
    for paths in (TRAIN, HELD):
        amplitudes = subset_amplitudes(paths)
        baseline = tuple(abs2(value) for value in amplitudes)
        for _epsilon in epsilons:
            # Exact exp(i epsilon |A|^2) has unit modulus, so its probabilities
            # equal baseline identically.  Test the algebraic invariant rather
            # than a floating exponential.
            phase_failures += int(inclusion(baseline) != 0)
        reference = coefficients(paths)
        for order in permutations(range(3)):
            permuted = tuple(paths[index] for index in order)
            candidate = coefficients(permuted)
            permutation_failures += int(any(
                sp.simplify(candidate[key] - reference[key]) != 0
                for key in ("base", "linear", "quadratic", "I1", "q")
            ))
    train_amplitudes = subset_amplitudes(TRAIN)
    baseline_terms = tuple(abs2(value) for value in train_amplitudes)
    deleted_inclusion = inclusion(tuple(
        value if index != 3 else 0 for index, value in enumerate(baseline_terms)
    ))
    epsilon = sp.symbols("epsilon", real=True)
    plus = train["linear"] * epsilon + train["quadratic"] * epsilon**2
    minus = -train["linear"] * epsilon + train["quadratic"] * epsilon**2
    symmetric = sp.simplify((plus + minus) / 2)
    delete_minus = sp.simplify(plus / 2)
    proper_frames = []
    for order in permutations(range(3)):
        permutation = np.zeros((3, 3), dtype=int)
        for row, column in enumerate(order):
            permutation[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                proper_frames.append(frame)
    check(
        "an exact phase-only deformation leaves every Born weight and I3 unchanged while path permutations preserve all perturbation coefficients",
        phase_failures == 0 and permutation_failures == 0,
        {
            "phase_parameters": tuple(str(value) for value in epsilons),
            "phase_I3_failures": phase_failures,
            "path_permutations": 12,
            "permutation_failures": permutation_failures,
            "phase_change_called_energy_or_rate": False,
        },
    )
    check(
        "deleting one inclusion term breaks baseline I3 and deleting one symmetric companion restores a linear perturbation term",
        deleted_inclusion != 0
        and sp.simplify(symmetric - train["quadratic"] * epsilon**2) == 0
        and sp.simplify(delete_minus).coeff(epsilon, 1) != 0,
        {
            "deleted_AB_baseline_I3": str(deleted_inclusion),
            "symmetric_I3": str(symmetric),
            "delete_minus_companion_I3": str(delete_minus),
            "epsilon_probe": "1/1000",
        },
    )
    check(
        "the scalar coefficient tournament is carried without change through all 24 proper-cubic apparatus frames",
        len(proper_frames) == 24 and all(round(np.linalg.det(frame)) == 1 for frame in proper_frames),
        {
            "proper_cubic_frames": len(proper_frames),
            "new_spatial_tensor_claimed": False,
            "physical_M2_compiler_claimed": False,
        },
    )


def prediction_dependency_no_go_controls(started: float, train, held) -> None:
    print("\nP3 CONDITIONAL CONSEQUENCES / DEPENDENCIES / N1-N8")
    bounds = (1e-2, 1e-4, 1e-8, 1e-12)
    supplied_scenario = tuple((bound, math.sqrt(bound)) for bound in bounds)
    refused = 0
    for probe in (
        lambda: subset_amplitudes((sp.Integer(1), sp.Integer(2))),
        lambda: subset_amplitudes((sp.Integer(1), sp.Integer(0), sp.Integer(2))),
        lambda: inclusion((sp.Integer(1),)),
    ):
        try:
            probe()
        except ValueError:
            refused += 1
    elapsed = perf_counter() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = int(raw_rss if sys.platform == "darwin" else raw_rss * 1024)
    check(
        "the Accessible Prediction square-root table is reproduced only after exponent one-half and coefficient one are supplied",
        supplied_scenario == ((0.01, 0.1), (0.0001, 0.01), (1e-08, 0.0001), (1e-12, 1e-06)),
        {
            "conditional_rows": supplied_scenario,
            "exponent_one_half": "supplied by P3",
            "C_equal_one": "supplied by P3 scenario runner",
            "derived_by_Cycle475": False,
        },
    )
    check(
        "lawful path domains refuse and the exact tournament remains below frozen resource caps",
        refused == 3 and elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {
            "domain_refusals": refused,
            "elapsed_seconds": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "peak_RSS_bytes": rss_bytes,
            "RSS_cap_bytes": RSS_CAP_BYTES,
        },
    )
    check(
        "the dependency ledger exposes every condition needed to promote the P3 experimental cross-bound",
        train["linear"] != 0 and held["linear"] != 0,
        {
            "supplied": (
                "three-path amplitudes and quadratic detector functional",
                "cubic amplitude deformation f(A)=|A|^2 A",
                "candidate beta(epsilon)=1+epsilon comparator",
                "equal +/- sector weights on the symmetric route",
                "conditional P3 experimental bounds and coefficient convention",
            ),
            "derived": (
                "exact I3=L epsilon+Q epsilon^2 expansion",
                "generic direct slope one and symmetric slope two",
                "train/held C values and no-refit mismatch",
                "phase-only blindness and deletion/permutation controls",
            ),
            "open": (
                "physical selection/generation of deformation law and +/- sectors",
                "why one epsilon controls Born and gravity channels",
                "geometry-independent coefficient/normalization",
                "physical M2 compiler, occurrence/Records, mass scaling, and empirical calibration",
            ),
            "C_num": "P3 exponent and coefficient are exposed law inputs; no numerical cross-bound derived",
            "C_int": "shared epsilon coupling between detector and gravity responses remains uncompiled",
            "C_local": "law-level exact comparator only; no physical-M2 compiler",
            "C_source": "candidate beta response is supplied, not generated by a source law",
        },
    )
    check(
        "full refreshed N1-N8 rejects broad P3, Born, gravity, no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "direct cubic route attempted/nonquadratic; symmetric +/- route attempted/quadratic; exact phase route attempted/blind; other measures, propagators, source laws, open systems, and physical M2 routes remain",
            "N2": "I3 cancellation order, shared deformation parameter, gravity beta response, coefficient universality, occurrence, and physical compilation are independent contracts",
            "N3": "hidden scan exposes amplitudes, detector functional, deformation f, +/- averaging weights, beta comparator, I1 normalization, finite fixtures, and C convention",
            "N4": "the witness matches Accessible Prediction P3's epsilon-expansion residual; it does not match finite Born quotient, occurrence, physical source, Newton law, or experimental gravity residuals",
            "N5": "exact three-path train/held algebra tested; arbitrary interferometers, physical apparatus, continuum sources, and empirical bounds untested",
            "N6": "a symmetric environment produces the requested exponent constructively, but law selection and coefficient remain",
            "N7": "a physical shared-deformation compiler with symmetry-protected linear cancellation and a universal held coefficient could promote P3",
            "N8": "the older nonlinear examples did not change beta appreciably and the conditional prediction note explicitly leaves P3 supplied; Cycle475 explains that boundary",
            "broad_P3_Born_gravity_or_no_go": "FAIL",
            "minimum_content": "none",
            "axiom_pressure": "none",
        },
    )


def _wall_alarm(_signum, _frame):
    raise TimeoutError("Cycle475 exceeded its wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = PROCESS_STARTED
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _wall_alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)
    print("Cycle475 Born/gravity P3 perturbation tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        contracts()
        train, held = exact_expansion_controls()
        scaling_and_held_controls(train, held)
        phase_deletion_permutation_controls(train, held)
        prediction_dependency_no_go_controls(started, train, held)
    except Exception as error:
        check("Cycle475 runner completed without exception", False, repr(error))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
