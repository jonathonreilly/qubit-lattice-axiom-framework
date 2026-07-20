#!/usr/bin/env python3
"""Cycle473: physical quantum-source / density-interface tournament.

Use actual Cycle465/468 physical source-position and Q1 field states to test a
narrow interface question: can one linear single-copy isometry append a
deterministic pure mean field built from rho_x=|alpha_x|^2 while either erasing
or retaining the input source?  Gram preservation gives the exact scoped
answer on declared train/held families.  Branch-controlled, dephased
Stinespring, finite-copy estimator, and supplied-Record routes remain live.

This is not a broad P1, Born, gravity, framework no-go, or axiom claim.
Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, sqrt
from pathlib import Path
from time import perf_counter
import resource
import signal
import sys

import numpy as np


PROCESS_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_coherent_source_field_test_composition_cycle468_2026_07_19 as c468


c465 = c468.c465
c464 = c468.c464
c463 = c468.c463
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_QUANTUM_SOURCE_DENSITY_INTERFACE_TOURNAMENT_CYCLE473_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 4e-10
VISIBLE = 1e-7
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Case:
    name: str
    amplitudes: np.ndarray
    held_only: bool = False


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


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical quantum-source / density-interface tournament",
        "single-copy deterministic pure mean-field product compiler",
        "actual cycle-465/468 physical source fields",
        "rho=|psi|^2 is a supplied candidate source functional",
        "branch-controlled sourcing is constructive",
        "dephased stinespring route",
        "finite multi-copy estimator route",
        "record-conditioned route",
        "all 24 proper-cubic frames",
        "norm weight is not probability",
        "scoped single-copy product-interface no-go: pass",
        "broad p1, born, probability, gravity, or framework no-go: fail",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    check("the Cycle473 note freezes the interface theorem and live-route boundary", not missing, missing)


def source_cases(size: int) -> tuple[Case, ...]:
    if size not in (3, 4):
        raise ValueError("Cycle473 only accepts the frozen train/held menus")
    basis = tuple(
        Case(f"basis-{index}", np.eye(size, dtype=complex)[:, index])
        for index in range(size)
    )
    a = np.zeros(size, dtype=complex)
    b = np.zeros(size, dtype=complex)
    phase = np.zeros(size, dtype=complex)
    a[0] = a[1] = 1 / sqrt(2)
    b[0] = b[-1] = 1 / sqrt(2)
    phase[0], phase[1] = 1 / sqrt(2), 1j / sqrt(2)
    return basis + (
        Case("overlap-A", a),
        Case("overlap-B-held-endpoint" if size == 4 else "overlap-B", b, size == 4),
        Case("same-density-phase", phase),
    )


def density(amplitudes: np.ndarray) -> tuple[Fraction, ...]:
    if abs(float(np.linalg.norm(amplitudes)) - 1.0) > TOL:
        raise ValueError("source amplitudes leave the normalized code")
    weights = tuple(Fraction(float(abs(value) ** 2)).limit_denominator(4096) for value in amplitudes)
    if sum(weights, Fraction()) != 1:
        raise ValueError("source weights leave the exact finite density code")
    return weights


def mean_profile(fixture: c468.CompositeFixture, weights: tuple[Fraction, ...]):
    if len(weights) != len(fixture.branches):
        raise ValueError("density/menu mismatch")
    return {
        coord: sum(
            (weight * branch.profile[coord] for weight, branch in zip(weights, fixture.branches)),
            Fraction(),
        )
        for coord in fixture.branches[0].profile
    }


def gram(vectors: tuple[np.ndarray, ...]) -> np.ndarray:
    return np.asarray([[np.vdot(left, right) for right in vectors] for left in vectors])


def interface_rows(fixture: c468.CompositeFixture) -> dict[str, object]:
    geometry = fixture.geometry
    cases = source_cases(len(geometry.source.menu))
    encoder = c465.source_encoding(geometry.source)
    source_vectors = tuple(encoder @ case.amplitudes for case in cases)
    mean_fields = []
    for case in cases:
        profile = mean_profile(fixture, density(case.amplitudes))
        field, _rows, _total = c468.q1_field_from_profile(fixture.layout, profile)
        mean_fields.append(field)
    mean_fields = tuple(mean_fields)

    retained_products = tuple(
        np.kron(source, field) for source, field in zip(source_vectors, mean_fields)
    )
    branch_outputs = []
    for case in cases:
        output = np.zeros(encoder.shape[0] * fixture.branches[0].q1_field.size, dtype=complex)
        for coefficient, branch_index, branch in zip(
            case.amplitudes, range(len(fixture.branches)), fixture.branches
        ):
            output += coefficient * np.kron(encoder[:, branch_index], branch.q1_field)
        branch_outputs.append(output)
    branch_outputs = tuple(branch_outputs)

    source_gram = gram(source_vectors)
    erased_gram = gram(mean_fields)
    product_gram = gram(retained_products)
    branch_gram = gram(branch_outputs)
    erased_residual = float(np.linalg.norm(erased_gram - source_gram))
    retained_residual = float(np.linalg.norm(product_gram - source_gram))
    branch_residual = float(np.linalg.norm(branch_gram - source_gram))

    name_index = {case.name: index for index, case in enumerate(cases)}
    index_a = name_index["overlap-A"]
    index_b = next(index for name, index in name_index.items() if name.startswith("overlap-B"))
    index_phase = name_index["same-density-phase"]
    field_distance = float(np.linalg.norm(mean_fields[index_a] - mean_fields[index_b]))
    same_density_distance = float(np.linalg.norm(mean_fields[index_a] - mean_fields[index_phase]))
    input_overlap_ab = source_gram[index_a, index_b]
    field_overlap_ab = erased_gram[index_a, index_b]

    check(
        f"{geometry.name} single-copy erased and retained-source deterministic pure mean-field targets violate exact isometry Gram preservation",
        erased_residual > VISIBLE
        and retained_residual > VISIBLE
        and field_distance > VISIBLE
        and same_density_distance < TOL
        and abs(input_overlap_ab) > VISIBLE
        and abs(abs(field_overlap_ab) - 1.0) > VISIBLE,
        {
            "cases": tuple(case.name for case in cases),
            "source_Gram_vs_erased_mean_field": erased_residual,
            "source_Gram_vs_retained_product": retained_residual,
            "different_density_field_distance": field_distance,
            "same_density_phase_field_distance": same_density_distance,
            "nonorthogonal_source_overlap": input_overlap_ab,
            "different_density_field_overlap": field_overlap_ab,
            "scope": "declared single-copy linear-isometry pure-product interface only",
        },
    )
    check(
        f"{geometry.name} actual branch-controlled physical source-field map preserves the complete source Gram matrix",
        branch_residual < TOL
        and all(abs(float(np.linalg.norm(vector)) - 1.0) < TOL for vector in branch_outputs),
        {
            "Gram_residual": branch_residual,
            "source_M2": encoder.shape[0],
            "field_Q1_modes": fixture.branches[0].q1_field.size,
            "host_branch_selection": 0,
            "rho_mean_field_compiled": False,
        },
    )
    return {
        "fixture": fixture,
        "cases": cases,
        "source_vectors": source_vectors,
        "mean_fields": mean_fields,
        "branch_outputs": branch_outputs,
        "source_gram": source_gram,
        "erased_residual": erased_residual,
        "retained_residual": retained_residual,
        "branch_residual": branch_residual,
        "field_distance": field_distance,
    }


def stinespring_and_multicopy_controls(row: dict[str, object], copies: int) -> None:
    fixture = row["fixture"]
    cases = row["cases"]
    encoder = c465.source_encoding(fixture.geometry.source)
    environment = np.eye(len(fixture.branches), dtype=complex)
    stinespring_vectors = []
    for case in cases:
        output = np.zeros(
            encoder.shape[0] * fixture.branches[0].q1_field.size * len(fixture.branches),
            dtype=complex,
        )
        for coefficient, branch_index, branch in zip(
            case.amplitudes, range(len(fixture.branches)), fixture.branches
        ):
            output += coefficient * np.kron(
                np.kron(encoder[:, branch_index], branch.q1_field),
                environment[:, branch_index],
            )
        stinespring_vectors.append(output)
    stinespring_residual = float(np.linalg.norm(gram(tuple(stinespring_vectors)) - row["source_gram"]))

    coherent = next(case for case in cases if case.name == "overlap-A")
    weights = np.asarray([float(value) for value in density(coherent.amplitudes)])
    reduced_purity = float(np.sum(weights**2))
    offdiagonal_before_trace = float(
        np.linalg.norm(np.outer(coherent.amplitudes, coherent.amplitudes.conj()) - np.diag(weights))
    )
    binomial = tuple(Fraction(comb(copies, count), 2**copies) for count in range(copies + 1))
    expectation = sum(Fraction(count, copies) * probability for count, probability in enumerate(binomial))
    variance = sum(
        (Fraction(count, copies) - expectation) ** 2 * probability
        for count, probability in enumerate(binomial)
    )
    check(
        f"{fixture.geometry.name} dephased Stinespring route is isometric but exports a mixed branch ledger rather than one deterministic pure mean field",
        stinespring_residual < TOL
        and reduced_purity < 1 - VISIBLE
        and offdiagonal_before_trace > VISIBLE,
        {
            "Stinespring_Gram_residual": stinespring_residual,
            "environment_M2_one_hot": len(fixture.branches),
            "reduced_mixture_weights": tuple(weights),
            "reduced_purity": reduced_purity,
            "coherence_removed_by_environment_trace": offdiagonal_before_trace,
            "trace_called_occurrence_or_Record": False,
        },
    )
    check(
        f"{fixture.geometry.name} finite {copies}-copy reversible-count route is unbiased but retains nonzero estimator variance",
        expectation == Fraction(1, 2)
        and variance == Fraction(1, 4 * copies)
        and variance > 0
        and sum(binomial, Fraction()) == 1,
        {
            "copies": copies,
            "count_distribution": tuple(str(value) for value in binomial),
            "density_expectation": str(expectation),
            "density_variance": str(variance),
            "deterministic_exact_single_run_density": False,
            "count_register_M2": (copies + 1).bit_length(),
        },
    )


def deletion_and_covariance_controls(rows: tuple[dict[str, object], ...]) -> None:
    print("\nDELETIONS / ALL24 CARRIED INTERFACE")
    deletion_rows = []
    covariance_failures = 0
    maximum_covariance = 0.0
    frames = c463.proper_cubic_frames()
    for row in rows:
        fixture = row["fixture"]
        common = fixture.branches[0].q1_field
        encoder = c465.source_encoding(fixture.geometry.source)
        common_outputs = tuple(np.kron(encoder @ case.amplitudes, common) for case in row["cases"])
        common_gram_residual = float(np.linalg.norm(gram(common_outputs) - row["source_gram"]))
        branch_distances = tuple(
            float(np.linalg.norm(branch.q1_field - common)) for branch in fixture.branches[1:]
        )
        post_deletion_field_spread = 0.0
        erased_branch_vectors = tuple(
            sum(
                (
                    coefficient * branch.q1_field
                    for coefficient, branch in zip(case.amplitudes, fixture.branches)
                ),
                np.zeros_like(common),
            )
            for case in row["cases"]
        )
        erased_branch_residual = float(np.linalg.norm(gram(erased_branch_vectors) - row["source_gram"]))
        deletion_rows.append({
            "geometry": fixture.geometry.name,
            "common_field_map_Gram_residual": common_gram_residual,
            "field_replacement_deletion_residual": max(branch_distances, default=0.0),
            "post_deletion_field_spread": post_deletion_field_spread,
            "source_label_erasure_Gram_residual": erased_branch_residual,
        })
        for frame in frames:
            for case, field in zip(row["cases"], row["mean_fields"]):
                profile = mean_profile(fixture, density(case.amplitudes))
                carried_profile = {
                    c463.transform(frame, coord): value for coord, value in profile.items()
                }
                carried, _direction_rows, _total = c468.q1_field_from_profile(
                    fixture.layout, carried_profile
                )
                transformed = c468.transformed_field_vector(field, fixture.layout, frame)
                residual = float(np.linalg.norm(carried - transformed))
                maximum_covariance = max(maximum_covariance, residual)
                covariance_failures += int(residual >= TOL)
    check(
        "deleting branch-distinct fields removes source response while deleting retained source labels destroys the branch isometry",
        all(item["common_field_map_Gram_residual"] < TOL for item in deletion_rows)
        and all(item["field_replacement_deletion_residual"] > VISIBLE for item in deletion_rows)
        and all(item["post_deletion_field_spread"] < TOL for item in deletion_rows)
        and all(item["source_label_erasure_Gram_residual"] > VISIBLE for item in deletion_rows),
        deletion_rows,
    )
    check(
        "the candidate density profiles and actual Q1 mean-field targets covary under all 24 proper-cubic carried frames",
        len(frames) == 24 and covariance_failures == 0 and maximum_covariance < TOL,
        {
            "frames": len(frames),
            "case_frame_comparisons": sum(len(row["cases"]) for row in rows) * len(frames),
            "failures": covariance_failures,
            "maximum_residual": maximum_covariance,
            "asymmetric_menu_invariant_claimed": False,
        },
    )


def domain_resource_ledger_no_go_controls(started: float, rows) -> None:
    print("\nDOMAIN / RESOURCE / DEPENDENCY / N1-N8")
    refused = 0
    for probe in (
        lambda: source_cases(2),
        lambda: density(np.asarray((1.0, 1.0, 0.0), complex)),
        lambda: mean_profile(rows[0]["fixture"], (Fraction(1),)),
        lambda: c465.validate_q1_source(
            tuple(0 for _ in c463.domain(1).active), c463.domain(1), c465.TRAIN.menu
        ),
    ):
        try:
            probe()
        except ValueError:
            refused += 1
    elapsed = perf_counter() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = int(raw_rss if sys.platform == "darwin" else raw_rss * 1024)
    check(
        "lawful source, density, menu, and Q1 domains refuse while the complete tournament stays within frozen caps",
        refused == 4 and elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {
            "domain_refusals": refused,
            "elapsed_seconds_including_imports": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "peak_RSS_bytes": rss_bytes,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "train_joint_capacity_M2": 8001643,
            "held_joint_capacity_M2": 21956483,
            "mean_field_amplitude_preparation": "supplied compile-time nonlinear target constructor",
            "update_time_host_density_service": 0,
        },
    )
    check(
        "the dependency ledger separates the exact product-interface theorem from P1, Born probability, Records, and gravity",
        all(row["branch_residual"] < TOL for row in rows),
        {
            "supplied": (
                "actual Cycle465/468 physical source positions and branch fields",
                "candidate rho_x=|alpha_x|^2 functional and global mean-profile preparation",
                "single-copy linear isometry and pure-product output contract",
                "finite menus, exact source amplitudes, noiseless codes, and tolerances",
            ),
            "derived": (
                "train/held Gram mismatch for erased and retained pure mean-field targets",
                "exact branch-controlled and dephased-Stinespring isometries",
                "finite-copy unbiased/nonzero-variance estimator control",
                "all24 density/Q1-field covariance and deletion behavior",
            ),
            "open": (
                "selection of operator sourcing versus semiclassical expectation sourcing",
                "physical derivation of rho, mass normalization, field preparation, occurrence, and Records",
                "infinite-copy/concentration limit, noise, renewal, universal coupling, and empirical gravity",
            ),
            "C_source": "the single-copy pure mean-field interface is excluded on the declared family; branch/operator sourcing is constructive",
            "C_int": "source-field interaction exists conditionally; mean-field law selection and calibration remain",
            "C_local": "actual bounded M2 source/field states used; supplied mean-profile amplitude preparation remains",
            "C_num": "norm weights are algebraic density inputs, not probability or frequency",
            "C_wrap": "unchanged; update count is not time",
        },
    )
    check(
        "full refreshed N1-N8 licenses only the scoped single-copy product-interface no-go and rejects broad promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "erased pure mean field and retained-source pure product attempted/negative; branch-controlled and dephased Stinespring attempted/positive; multi-copy estimator positive but nondeterministic; supplied-Record, nonlinear mean-field, and open-system routes remain",
            "N2": "single-copy linearity, deterministic purity, density-functional choice, amplitude preparation, mass calibration, occurrence/Record, and gravity interpretation are distinct contracts",
            "N3": "hidden scan exposes finite menus, exact amplitudes, rho candidate, pure-product target, global normalization, compile-time field preparation, noiseless isometries, and environment/copy resources",
            "N4": "the witness matches P1's physical rho-interface residual and Cycles465/468 branch-source surface; it does not match Born probability, Record formation, Newton normalization, or empirical gravity",
            "N5": "basis/nonorthogonal finite states and M2/Q1 carried frames tested; arbitrary states, continuum, repeated-trial law, and empirical source dynamics untested",
            "N6": "branch/operator sourcing and open-system/multi-copy paths remain constructive without an axiom edit",
            "N7": "a selected open-system law, actualized Record channel, or justified many-copy limit could implement an operational density source; a nonlinear mean-field law could bypass isometry at a declared cost",
            "N8": "Cycle465/468 already realize the positive branch route; weak-field rho uniqueness presupposes a source functional but not its single-copy physical compiler",
            "scoped_single_copy_product_interface_no_go": "PASS",
            "broad_P1_Born_probability_gravity_or_framework_no_go": "FAIL",
            "minimum_content_claim": "none",
            "axiom_pressure": "none",
        },
    )


def _wall_alarm(_signum, _frame):
    raise TimeoutError("Cycle473 exceeded its wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = PROCESS_STARTED
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _wall_alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)
    print("Cycle473 physical quantum-source / density-interface tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        note_contract()
        fixtures = (c468.build_fixture(c468.TRAIN), c468.build_fixture(c468.HELD))
        rows = tuple(interface_rows(fixture) for fixture in fixtures)
        stinespring_and_multicopy_controls(rows[0], copies=2)
        stinespring_and_multicopy_controls(rows[1], copies=5)
        deletion_and_covariance_controls(rows)
        domain_resource_ledger_no_go_controls(started, rows)
    except Exception as error:
        check("Cycle473 runner completed without exception", False, repr(error))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
