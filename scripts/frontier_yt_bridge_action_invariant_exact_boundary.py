#!/usr/bin/env python3
"""Exact response-moment theorem and YT bridge nonselection boundary.

This runner deliberately contains no observed top endpoint, fitted bridge
profile, RG constants, or retention cut.  It checks the exact algebra behind
the response-compression theorem and constructs a local stable-action
counterfamily showing that locality and positivity do not select a unique
``I_2`` or UV centroid.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_PATHS = {
    "scale_reference": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic_isotropy": ROOT
    / "docs"
    / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized_state": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
}
SOURCE_NOTE = (
    ROOT
    / "docs"
    / "YT_BRIDGE_ACTION_INVARIANT_GENERIC_SELECTOR_NONSELECTION_NO_GO_NOTE_2026-07-12.md"
)
DEFAULT_OUTPUT = (
    ROOT
    / "outputs"
    / "yt_bridge_action_invariant_exact_boundary_2026-07-12.json"
)


@dataclass(frozen=True)
class Check:
    name: str
    check_class: str
    passed: bool
    detail: str


CHECKS: list[Check] = []


def record(name: str, check_class: str, passed: bool, detail: str) -> None:
    CHECKS.append(Check(name, check_class, bool(passed), detail))
    tag = "PASS" if passed else "FAIL"
    print(f"[{tag} ({check_class})] {name}: {detail}")


def exact_response_identities() -> None:
    q0, q1, q2 = sp.symbols("q_0 q_1 q_2", positive=True)
    x0, x1, x2 = sp.symbols("x_0 x_1 x_2", real=True)
    a, b, d = sp.symbols("a b d", real=True)
    qs = (q0, q1, q2)
    xs = (x0, x1, x2)
    area = sum(qs)
    centroid = sum(q * x for q, x in zip(qs, xs)) / area

    affine_response = sum(q * (a * x + b) for q, x in zip(qs, xs))
    affine_closed = area * (a * centroid + b)
    affine_residual = sp.factor(affine_response - affine_closed)
    record(
        "affine-two-moment-identity",
        "A",
        affine_residual == 0,
        "sum q_i(a x_i+b) = A(a c+b) identically",
    )

    variance = sum(q * (x - centroid) ** 2 for q, x in zip(qs, xs)) / area
    quadratic_response = sum(
        q * (a * x + b + d * x**2) for q, x in zip(qs, xs)
    )
    quadratic_residual = sp.factor(
        quadratic_response
        - area * (a * centroid + b + d * centroid**2)
        - d * area * variance
    )
    record(
        "quadratic-curvature-variance-identity",
        "A",
        quadratic_residual == 0,
        "R - A K(c) = d A Var_q(x) exactly for K=a x+b+d x^2",
    )

    u, v, mu = sp.symbols("u v mu", real=True)
    popoviciu_gap = sp.factor(
        (v - u) ** 2 / 4 - (mu - u) * (v - mu)
    )
    expected_gap = sp.factor((mu - (u + v) / 2) ** 2)
    record(
        "interval-variance-bound-factorization",
        "A",
        sp.simplify(popoviciu_gap - expected_gap) == 0,
        "(v-u)^2/4-(mu-u)(v-mu)=(mu-(u+v)/2)^2",
    )

    s, z = sp.symbols("s z", real=True)
    endpoint = z**2 + z**3
    path_integral = sp.integrate(sp.diff((s * z) ** 2 + (s * z) ** 3, s), (s, 0, 1))
    record(
        "finite-endpoint-path-identity",
        "A",
        sp.simplify(path_integral - endpoint) == 0,
        "E(z)-E(0)=integral_0^1 dE(sz)/ds ds for nonlinear E=z^2+z^3",
    )


def moment_falsifiers() -> None:
    # Equal zeroth moment, different centroid: a nonconstant affine kernel
    # distinguishes the profiles exactly.
    x_left = Fraction(3, 4)
    x_right = Fraction(1, 1)
    area_left = area_right = Fraction(1, 1)
    response_left = area_left * x_left
    response_right = area_right * x_right
    record(
        "i2-alone-not-exact-for-nonconstant-affine-kernel",
        "A",
        area_left == area_right and response_left != response_right,
        (
            f"equal A={area_left}; c={x_left} gives R={response_left}, "
            f"c={x_right} gives R={response_right} for K=x"
        ),
    )

    # Equal zeroth and first moments, different variance: curvature sees the
    # profile detail discarded by (A,c).
    center = Fraction(7, 8)
    delta_profile = ((center, Fraction(1)),)
    split_profile = (
        (Fraction(3, 4), Fraction(1, 2)),
        (Fraction(1), Fraction(1, 2)),
    )

    def moments(profile: tuple[tuple[Fraction, Fraction], ...]):
        area = sum(weight for _, weight in profile)
        centroid = sum(x * weight for x, weight in profile) / area
        response = sum(x**2 * weight for x, weight in profile)
        return area, centroid, response

    area_delta, centroid_delta, response_delta = moments(delta_profile)
    area_split, centroid_split, response_split = moments(split_profile)
    record(
        "two-moments-not-exact-for-curved-kernel",
        "A",
        (
            area_delta == area_split == 1
            and centroid_delta == centroid_split == center
            and response_delta != response_split
        ),
        (
            "both profiles have A=1 and c=7/8; "
            f"K=x^2 responses are {response_delta} and {response_split}"
        ),
    )


def local_action_minimizer(kappa: Fraction) -> tuple[Fraction, ...]:
    """Minimize sum (q[j+1]-q[j])^2 + kappa sum q[j]^2.

    The four-point chain has fixed q[0]=0 and q[3]=1.  The two interior
    Euler equations are solved in exact rational arithmetic.
    """

    two_plus = Fraction(2, 1) + kappa
    denominator = two_plus**2 - 1
    q1 = 1 / denominator
    q2 = two_plus / denominator
    return (Fraction(0), q1, q2, Fraction(1))


def discrete_moments(profile: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
    xs = (Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1))
    total = sum(profile)
    action_average = total / len(profile)
    centroid = sum(x * q for x, q in zip(xs, profile)) / total
    return action_average, centroid


def action_counterfamily() -> None:
    profile_0 = local_action_minimizer(Fraction(0))
    profile_1 = local_action_minimizer(Fraction(1))
    a_disc_0, c_disc_0 = discrete_moments(profile_0)
    a_disc_1, c_disc_1 = discrete_moments(profile_1)

    expected_0 = (Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1))
    expected_1 = (Fraction(0), Fraction(1, 8), Fraction(3, 8), Fraction(1))
    euler_0 = (2 * profile_0[1] - profile_0[2], -profile_0[1] + 2 * profile_0[2] - 1)
    euler_1 = (3 * profile_1[1] - profile_1[2], -profile_1[1] + 3 * profile_1[2] - 1)
    record(
        "local-stable-action-counterfamily",
        "A",
        (
            profile_0 == expected_0
            and profile_1 == expected_1
            and euler_0 == (0, 0)
            and euler_1 == (0, 0)
            and (a_disc_0, c_disc_0) == (Fraction(1, 2), Fraction(7, 9))
            and (a_disc_1, c_disc_1) == (Fraction(3, 8), Fraction(31, 36))
        ),
        (
            "S_kappa=sum(Delta q)^2+kappa sum(q^2), q=(0,*,*,1): "
            f"kappa=0 -> q={profile_0}, A_disc={a_disc_0}, c_disc={c_disc_0}; "
            f"kappa=1 -> q={profile_1}, A_disc={a_disc_1}, c_disc={c_disc_1}"
        ),
    )

    # The Hessian on the two interior variables is
    # 2 [[2+kappa,-1],[-1,2+kappa]].  Sylvester positivity is exact.
    for kappa in (Fraction(0), Fraction(1)):
        leading_minor = 2 * (2 + kappa)
        determinant = 4 * ((2 + kappa) ** 2 - 1)
        record(
            f"strict-convexity-kappa-{kappa}",
            "A",
            leading_minor > 0 and determinant > 0,
            f"H leading minor={leading_minor}, determinant={determinant}",
        )


def source_surface_firewalls() -> dict[str, str]:
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_text = SOURCE_NOTE.read_text(encoding="utf-8")
    normalized_axiom_text = re.sub(r"\s+", " ", axiom_text)
    required_axiom_boundaries = (
        "does not choose a Hamiltonian or transfer operator",
        "source/action and physical-observable identification",
        "time metric",
        "A choice not fixed by the supplied structure remains a named conditional or open dependency",
    )
    missing_axiom_boundaries = [
        phrase
        for phrase in required_axiom_boundaries
        if phrase not in normalized_axiom_text
    ]
    record(
        "minimal-axiom-nonselection-boundary-present",
        "B",
        not missing_axiom_boundaries,
        (
            "current axiom memo withholds dynamics/source-action/time and "
            "keeps unfixed choices open"
            if not missing_axiom_boundaries
            else f"missing phrases: {missing_axiom_boundaries}"
        ),
    )

    primitive_needles = {
        "scale_reference": (
            "This is a units conversion, not a physics axiom",
            "no mass ratio, coupling, mixing angle, phase, selector, readout bridge",
        ),
        "kinetic_isotropy": (
            "It carries no dimensionless dynamical content",
            "No mass ratio, coupling, mixing angle, phase, or selector is supplied",
        ),
        "realized_state": (
            "This is pointwise evaluation, not a state-selection rule",
            "no state, averaging over alternatives, measure, weighting, probability rule",
        ),
    }
    for name, path in PRIMITIVE_PATHS.items():
        normalized_text = re.sub(r"\s+", " ", path.read_text(encoding="utf-8"))
        missing = [needle for needle in primitive_needles[name] if needle not in normalized_text]
        record(
            f"approved-primitive-scope-{name}",
            "B",
            not missing,
            "approved primitive remains inside its declared narrow scope"
            if not missing
            else f"missing scope text: {missing}",
        )

    required_note_needles = (
        "Generic-Selector Nonselection No-Go",
        "Moment-response lemma",
        "No-Go Discipline",
        "actual_current_surface_status: no-go",
        "target_claim_type: no_go",
        "claim_type_reason:",
    )
    missing_note_needles = [
        phrase for phrase in required_note_needles if phrase not in note_text
    ]
    record(
        "source-note-claim-firewall",
        "B",
        not missing_note_needles,
        (
            "exact theorem, nonselection boundary, N1-N8 discipline, and "
            "claim-status firewall are present"
            if not missing_note_needles
            else f"missing phrases: {missing_note_needles}"
        ),
    )

    runner_text = Path(__file__).read_text(encoding="utf-8")
    forbidden_modules = ("numpy", "scipy")
    used_forbidden = [
        module
        for module in forbidden_modules
        if f"import {module}" in runner_text or f"from {module}" in runner_text
    ]
    record(
        "no-numerical-transport-stack-proof-import",
        "B",
        not used_forbidden,
        "runner uses exact standard-library/SymPy algebra and no numerical transport stack",
    )

    hashes = {
        "minimal_axioms_sha256": hashlib.sha256(
            AXIOM_PATH.read_bytes()
        ).hexdigest(),
        "source_note_sha256": hashlib.sha256(SOURCE_NOTE.read_bytes()).hexdigest(),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    hashes.update(
        {
            f"{name}_primitive_sha256": hashlib.sha256(path.read_bytes()).hexdigest()
            for name, path in PRIMITIVE_PATHS.items()
        }
    )
    return hashes


def write_certificate(output_path: Path, hashes: dict[str, str]) -> None:
    payload = {
        "schema_version": 1,
        "artifact": "yt_bridge_action_invariant_exact_boundary",
        "actual_current_surface_status": "no-go",
        "target_claim_type": "no_go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "claim_type_reason": (
            "generic chain locality, fixed endpoints, and strict convexity "
            "admit an exact coefficient counterfamily with different moments"
        ),
        "audit_required_before_effective_retained": True,
        "forbidden_inputs": [
            "observed y_t endpoint",
            "fitted selector",
            "chosen bridge profile family",
            "target-conditioned retention cut",
            "hard-coded physical constants",
        ],
        "hashes": hashes,
        "checks": [asdict(check) for check in CHECKS],
        "summary": {
            "pass": sum(check.passed for check in CHECKS),
            "fail": sum(not check.passed for check in CHECKS),
        },
        "remaining_blocker": (
            "derive the physical microscopic bridge operator, YT observable "
            "map, and a uniform finite-response kernel bound"
        ),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    print("=" * 78)
    print("YT BRIDGE ACTION INVARIANT — EXACT RESPONSE / NONSELECTION BOUNDARY")
    print("=" * 78)
    exact_response_identities()
    moment_falsifiers()
    action_counterfamily()
    hashes = source_surface_firewalls()
    write_certificate(args.output, hashes)

    passed = sum(check.passed for check in CHECKS)
    failed = sum(not check.passed for check in CHECKS)
    print("-" * 78)
    try:
        display_output = args.output.resolve().relative_to(ROOT.resolve())
    except ValueError:
        display_output = args.output.resolve()
    print(f"CERTIFICATE: {display_output}")
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
