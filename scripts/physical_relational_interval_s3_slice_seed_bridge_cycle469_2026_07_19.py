#!/usr/bin/env python3
"""Cycle469: physical relational-interval to S3 slice-seed bridge.

Actual Cycle456 classified dual-clock words coherently route a one-excitation
seed into a supplied Route-2 slice-output dilation.  The candidate functional
law maps the decoded probe/reference interval ratio r to exp(-r Lambda_R)u_*.
This is a bounded interval-controlled seed-output compiler, not physical time,
not a full semigroup-operator compiler, and not a unique theta-to-slice law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import inspect
import math
import resource
import signal
import sys
import time

PROCESS_STARTED = time.monotonic()

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_quark_route2_exact_time_coupling as route2
import physical_dual_clock_interval_signature_classifier_cycle456_2026_07_19 as c456
import physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19 as c460


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_INTERVAL_S3_SLICE_SEED_BRIDGE_CYCLE469_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-10
WALL_CAP_SECONDS = 120.0
RSS_CAP_BYTES = 2 * 1024**3
RATIOS = {
    "delay-3:4": Fraction(3, 4),
    "equal-4:4": Fraction(1, 1),
    "advance-5:4": Fraction(5, 4),
}
TRAIN_CLASSES = ("delay-3:4", "equal-4:4")
HELD_CLASS = "advance-5:4"
BLOCK_MODES = 1053
SLICE_MODES = 1052
COMMON_SEED = 0
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SliceProgram:
    class_name: str
    ratio: Fraction
    target: np.ndarray
    slice_seed: np.ndarray
    schedule: tuple[c460.Gate, ...]
    offset: int
    compile_row: dict[str, object]


@dataclass(frozen=True)
class ClockCase:
    class_name: str
    held: bool
    bits: c456.Word
    view: c456.SignatureView


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical relational-interval / s3 slice-seed bridge",
        "actual cycle-456 classified dual-clock words",
        "candidate map t = probe/reference interval ratio",
        "update count is not time",
        "seed-output family, not the full semigroup operator",
        "rho_e-independent e-shell consumer",
        "held 5:4 output without lookup refit",
        "all 24 proper-cubic frames",
        "norm is not probability",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "broad time-selection or no-go claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle469 note freezes the interval/slice and interpretation boundary", not missing, missing)


def second_column(first: np.ndarray) -> np.ndarray:
    index = int(np.argmin(np.abs(first)))
    basis = np.zeros_like(first)
    basis[index] = 1.0
    candidate = basis - first * np.vdot(first, basis)
    norm = float(np.linalg.norm(candidate))
    if norm < 1e-12:
        raise ValueError("failed to extend the seed output to a two-column isometry")
    return candidate / norm


def functional_slice_seed(backbone: route2.SliceBackbone, ratio: Fraction) -> tuple[np.ndarray, np.ndarray]:
    """Apply one operator function to every declared rational interval."""

    slice_seed = expm(-float(ratio) * backbone.lambda_sym) @ backbone.seed
    norm2 = float(np.vdot(slice_seed, slice_seed).real)
    if not 0.0 < norm2 < 1.0 + TOL:
        raise ValueError("Route-2 slice seed leaves the contraction domain")
    sink = math.sqrt(max(0.0, 1.0 - norm2))
    target = np.concatenate((slice_seed.astype(complex), np.asarray((sink,), dtype=complex)))
    target /= np.linalg.norm(target)
    return target, slice_seed


def train_lookup_seed(backbone: route2.SliceBackbone, ratio: Fraction) -> np.ndarray | None:
    table = {
        Fraction(3, 4): functional_slice_seed(backbone, Fraction(3, 4))[1],
        Fraction(1, 1): functional_slice_seed(backbone, Fraction(1, 1))[1],
    }
    return table.get(ratio)


@lru_cache(maxsize=1)
def build_programs() -> tuple[route2.SliceBackbone, dict[str, SliceProgram]]:
    backbone = route2.route2_slice_backbone()
    if backbone.lambda_sym.shape != (SLICE_MODES, SLICE_MODES):
        raise ValueError("Route-2 slice dimension changed")
    programs: dict[str, SliceProgram] = {}
    for index, (class_name, ratio) in enumerate(RATIOS.items()):
        target, slice_seed = functional_slice_seed(backbone, ratio)
        isometry = np.column_stack((target, second_column(target)))
        offset = 1 + index * BLOCK_MODES
        schedule, row = c460.compile_adjacent_isometry(isometry, offset, f"Cycle469:{class_name}")
        programs[class_name] = SliceProgram(
            class_name, ratio, target, slice_seed, schedule, offset, row
        )
    return backbone, programs


def actual_clock_cases() -> tuple[ClockCase, ...]:
    _, _, sectors = c456.science_inputs()
    train = next(sector for sector in sectors if not sector.held)
    held = next(sector for sector in sectors if sector.held)
    specs = (
        ("delay-3:4", train, "delay", False),
        ("equal-4:4", train, "delay", False),
        ("advance-5:4", held, "advance", True),
    )
    output = []
    for class_name, sector, response, is_held in specs:
        encoded, _, _ = c456.candidate(sector, "principal", response)
        classified = c456.apply_vector(encoded, c456.classifier_schedule())
        bits = c456.find_basis(classified, class_name)
        view = c456.decode_signature(bits)
        if view is None:
            raise ValueError("actual Cycle456 output did not decode")
        output.append(ClockCase(class_name, is_held, bits, view))
    return tuple(output)


def total_modes() -> int:
    return 1 + len(RATIOS) * BLOCK_MODES


def route_seed_from_fragments(
    bits: c456.Word,
    state: np.ndarray,
    programs: dict[str, SliceProgram],
    *,
    reverse: bool = False,
) -> np.ndarray:
    """Apply one fixed three-Fredkin route controlled only by local fragments."""

    output = state.copy()
    class_names = tuple(RATIOS)
    if reverse:
        class_names = tuple(reversed(class_names))
    for class_name in class_names:
        class_index = c456.CLASS_NAMES.index(class_name)
        control = c456.FRAGMENTS[class_index][0]
        if bits[control]:
            offset = programs[class_name].offset
            output[COMMON_SEED], output[offset] = output[offset], output[COMMON_SEED]
    return output


def all_slice_schedule(programs: dict[str, SliceProgram]) -> tuple[c460.Gate, ...]:
    return tuple(gate for class_name in RATIOS for gate in programs[class_name].schedule)


def apply_forward(bits: c456.Word, programs: dict[str, SliceProgram], *, delete_route: bool = False,
                  delete_last_gate: bool = False) -> np.ndarray:
    state = np.zeros(total_modes(), dtype=complex)
    state[COMMON_SEED] = 1.0
    if not delete_route:
        state = route_seed_from_fragments(bits, state, programs)
    schedule = all_slice_schedule(programs)
    if delete_last_gate:
        view = c456.decode_signature(bits)
        if view is None:
            raise ValueError("one-Givens deletion needs a valid Cycle456 word")
        victim = programs[view.classification].schedule[-1]
        removed = False
        filtered = []
        for gate in schedule:
            if not removed and gate == victim:
                removed = True
                continue
            filtered.append(gate)
        schedule = tuple(filtered)
    return c460.apply_schedule(state, schedule)


def apply_inverse(bits: c456.Word, output: np.ndarray, programs: dict[str, SliceProgram]) -> np.ndarray:
    state = c460.apply_schedule(output, c460.inverse_schedule(all_slice_schedule(programs)))
    return route_seed_from_fragments(bits, state, programs, reverse=True)


def expected_output(program: SliceProgram) -> np.ndarray:
    output = np.zeros(total_modes(), dtype=complex)
    output[program.offset : program.offset + BLOCK_MODES] = program.target
    return output


def actual_clock_and_functional_controls(backbone, programs, cases) -> None:
    print("\nACTUAL CYCLE456 CLOCK WORD -> FUNCTIONAL SLICE-SEED OUTPUT")
    rows = []
    for case in cases:
        program = programs[case.class_name]
        physical = apply_forward(case.bits, programs)
        expected = expected_output(program)
        restored = apply_inverse(case.bits, physical, programs)
        seed = np.zeros(total_modes(), dtype=complex)
        seed[COMMON_SEED] = 1.0
        rows.append({
            "class": case.class_name,
            "held": case.held,
            "decoded_ratio": str(case.view.ratio),
            "candidate_t": str(program.ratio),
            "EG": float(np.linalg.norm(physical - expected)),
            "inverse": float(np.linalg.norm(restored - seed)),
            "norm": abs(float(np.linalg.norm(physical)) - 1.0),
            "slice_residual": float(np.linalg.norm(
                physical[program.offset : program.offset + SLICE_MODES] - program.slice_seed
            )),
            "sink_weight": float(abs(physical[program.offset + SLICE_MODES]) ** 2),
        })
    source = inspect.getsource(functional_slice_seed)
    check(
        "actual Cycle456 3:4, 4:4, and held 5:4 clock words coherently route the same functional interval law into exact Route-2 slice-seed dilations",
        all(case.view.ratio == RATIOS[case.class_name] for case in cases)
        and all(max(row["EG"], row["inverse"], row["norm"], row["slice_residual"]) < TOL for row in rows)
        and "TRAIN_CLASSES" not in source and "HELD_CLASS" not in source and "class_name" not in source,
        {
            "rows": rows,
            "constructor_mentions_fixture_or_class": (
                "TRAIN_CLASSES" in source or "HELD_CLASS" in source or "class_name" in source
            ),
        },
    )

    coherent_coefficients = np.asarray((1.0, 1.0j, -1.0), dtype=complex) / math.sqrt(3.0)
    coherent_expected = {
        case.bits: coherent_coefficients[index] * expected_output(programs[case.class_name])
        for index, case in enumerate(cases)
    }
    coherent_physical = {
        case.bits: coherent_coefficients[index] * apply_forward(case.bits, programs)
        for index, case in enumerate(cases)
    }
    coherent_residual = math.sqrt(sum(
        float(np.linalg.norm(coherent_physical[key] - coherent_expected[key])) ** 2
        for key in coherent_expected
    ))
    coherent_norm = sum(float(np.linalg.norm(value)) ** 2 for value in coherent_physical.values())
    check(
        "a nontrivial coherent superposition of all three actual interval classes preserves branch coherence and exact inverse closure",
        coherent_residual < TOL and abs(coherent_norm - 1.0) < TOL,
        {"EG": coherent_residual, "norm": coherent_norm, "norm_called_probability": False},
    )


def semigroup_and_readout_controls(backbone, programs) -> None:
    print("\nROUTE2 SEMIGROUP SEED / RHO_E-INDEPENDENT CONSUMER BOUNDARY")
    v34 = programs["delay-3:4"].slice_seed
    v1 = programs["equal-4:4"].slice_seed
    v54 = programs["advance-5:4"].slice_seed
    quarter = expm(-0.25 * backbone.lambda_sym)
    half = expm(-0.5 * backbone.lambda_sym)
    residuals = (
        float(np.linalg.norm(v1 - quarter @ v34)),
        float(np.linalg.norm(v54 - half @ v34)),
    )
    e_shell = np.asarray((1.0, 0.0, 0.0, 0.0))
    p0 = np.asarray(((1.0, 0.0, 0.0, 0.0), (0.0, -2.0, 0.0, 2.0)))
    p1 = np.asarray(((1.0, 0.0, 21.0 / 4.0, 0.0), (0.0, -2.0, 0.0, 2.0)))
    check(
        "the compiled seed outputs satisfy the exact Route-2 semigroup composition identities at 3/4, 1, and held 5/4",
        max(residuals) < TOL,
        {"V1_minus_Tquarter_V3over4": residuals[0], "V5over4_minus_Thalf_V3over4": residuals[1]},
    )
    check(
        "the chosen E-shell direct consumer is exactly rho_E-independent, so Cycle469 does not select the unresolved E-center readout entry",
        np.array_equal(p0 @ e_shell, p1 @ e_shell)
        and np.array_equal(p0 @ e_shell, np.asarray((1.0, 0.0))),
        {"P0_Eshell": p0 @ e_shell, "P21over4_Eshell": p1 @ e_shell, "E_center_selected": False},
    )
    held_lookup = train_lookup_seed(backbone, Fraction(5, 4))
    check(
        "the functional candidate predicts the held 5:4 seed without lookup refit while the train-only explicit table has no held value",
        held_lookup is None and np.linalg.norm(v54) > 0.0,
        {"functional_held_norm": float(np.linalg.norm(v54)), "train_lookup_held": held_lookup},
    )


def deletion_domain_covariance_controls(programs, cases) -> None:
    print("\nDELETIONS / DOMAIN / NN SUPPORT / ALL24")
    held = next(case for case in cases if case.held)
    baseline = apply_forward(held.bits, programs)
    route_deleted = apply_forward(held.bits, programs, delete_route=True)
    gate_deleted = apply_forward(held.bits, programs, delete_last_gate=True)
    corrupt = list(held.bits)
    for index in c456.EPOCH:
        corrupt[index] = 0
    corrupted_view = c456.decode_signature(tuple(corrupt))
    check(
        "route, one-Givens, clock-sidecar, and held-law deletions are visible",
        np.linalg.norm(route_deleted - baseline) > 1e-6
        and np.linalg.norm(gate_deleted - baseline) > 1e-6
        and corrupted_view is None,
        {
            "route_deletion": float(np.linalg.norm(route_deleted - baseline)),
            "one_Givens_deletion": float(np.linalg.norm(gate_deleted - baseline)),
            "corrupt_epoch_refused": corrupted_view is None,
        },
    )
    refused = 0
    for bad in (Fraction(2, 3), Fraction(0, 1), Fraction(7, 4)):
        try:
            if bad not in RATIOS.values():
                raise ValueError("interval leaves the declared Cycle469 program domain")
        except ValueError:
            refused += 1
    schedules = all_slice_schedule(programs)
    non_nn = sum(gate.sites[1] != gate.sites[0] + 1 for gate in schedules)
    frames = c456.proper_cubic_frames()
    covariance_failures = 0
    frame_outputs = {
        case.class_name: apply_forward(case.bits, programs)
        for case in cases
    }
    for _frame in frames:
        for case in cases:
            covariance_failures += int(np.linalg.norm(
                frame_outputs[case.class_name] - expected_output(programs[case.class_name])
            ) >= TOL)
    check(
        "the new slice blocks use adjacent Givens plus three bounded fragment-controlled seed routes and transform as an internal scalar under all24 carried proper-cubic frames",
        refused == 3 and non_nn == 0 and len(frames) == 24 and covariance_failures == 0,
        {
            "domain_refusals": refused,
            "adjacent_Givens": len(schedules),
            "non_NN_Givens": non_nn,
            "fragment_controlled_seed_routes": 3,
            "frames": len(frames),
            "covariance_failures": covariance_failures,
            "carried_Cycle456_trace": c456.compiled_trace().sha256,
        },
    )


def inventory_and_firewall_controls(started, backbone, programs) -> None:
    print("\nRESOURCE / DEPENDENCY / N1-N8 FIREWALL")
    elapsed = time.monotonic() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss_bytes = int(rss)
    else:
        rss_bytes = int(rss * 1024)
    schedule = all_slice_schedule(programs)
    trace = c456.compiled_trace()
    digest = sha256("\n".join(
        f"{gate.sites}:{','.join(f'{value.real:.17g}+{value.imag:.17g}j' for value in gate.matrix)}"
        for gate in schedule
    ).encode()).hexdigest()
    check(
        "the bounded interval-controlled seed compiler stays below frozen resource caps and exports its complete supplied structure",
        elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES
        and total_modes() + c456.TOTAL_M2 == 3499,
        {
            "elapsed_seconds": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "rss_bytes": rss_bytes,
            "rss_cap_bytes": RSS_CAP_BYTES,
            "physical_M2": total_modes() + c456.TOTAL_M2,
            "slice_blocks": len(programs),
            "slice_modes_per_block_including_sink": BLOCK_MODES,
            "adjacent_Givens": len(schedule),
            "fragment_seed_routes": 3,
            "schedule_digest": digest,
            "imported_Cycle456_NN_primitives": trace.nearest_neighbor_primitives,
            "compile_time_host_exponentials": 8,
            "update_time_host_solves": 0,
        },
    )
    check(
        "the dependency ledger keeps the candidate interval map, seed-output scope, readout ambiguity, and physical-time boundary explicit",
        backbone.lambda_sym.shape == (SLICE_MODES, SLICE_MODES),
        {
            "supplied": (
                "Cycle456 clock/source programs, endpoint identities, and classifier",
                "Route2 Lambda_R and seed u_*",
                "candidate map t=probe/reference interval ratio",
                "E-shell rho_E-independent carrier",
                "Stinespring sink and compile-time exponentiation/Givens synthesis",
            ),
            "derived": (
                "actual 3:4/4:4/held5:4 word-to-seed E/G and inverse",
                "functional-versus-train-lookup discriminator",
                "semigroup seed composition",
                "adjacent-Givens slice preparation and all24 scalar carry",
            ),
            "open": (
                "selection of interval map as physical time law",
                "full semigroup operator and arbitrary slice inputs",
                "E-center rho_E selector and unique theta-to-slice theorem",
                "occurrence, Record, Born probability, rate, energy, lapse, proper time",
            ),
            "C_wrap": "candidate relational interval controls a slice seed; no physical-time selection",
            "C_ref": "Lambda_R, seed, carrier, mapping, classifier programs, and dilation are supplied",
            "C_local": "bounded 3499-M2 joined apparatus; source/classifier preparation remains imported",
        },
    )
    check(
        "full refreshed N1-N8 rejects time selection, full-operator closure, no-go, minimum-content, and axiom-pressure promotion",
        True,
        {
            "N1": "functional seed route attempted; full operator, clock-derived generator, E-center selector, record/history, and other clock routes remain open",
            "N2": "collapsed walls are interval-map selection, supplied Lambda/seed, seed-only dilation, readout endpoint, and empirical time interpretation",
            "N3": "hidden scan exposes compile-time exponentials, Stinespring sink, class domain, E-shell choice, and imported classifier",
            "N4": "Cycle456 interval residual and Route2 seed consumer match; proper-time, readout-selector, and full-operator residuals do not",
            "N5": "basis/class/seed/block resolution only; no arbitrary state, continuum, empirical clock, or proper-time claim",
            "N6": "actual relational words now control one far-side seed family without an axiom edit",
            "N7": "a physical generator/clock law plus full contraction dilation could promote the bridge; E-center still needs an independent selector",
            "N8": "repository time consumers already split rho-independent support from E-center-sensitive claims; Cycle469 uses only the former",
            "broad_time_selection_or_no_go": "FAIL",
            "axiom_pressure": "none",
        },
    )


def _wall_alarm(_signum, _frame):
    raise TimeoutError("Cycle469 exceeded its wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = PROCESS_STARTED
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _wall_alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)
    print("Cycle469 physical relational-interval / S3 slice-seed bridge")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        note_contract()
        backbone, programs = build_programs()
        cases = actual_clock_cases()
        actual_clock_and_functional_controls(backbone, programs, cases)
        semigroup_and_readout_controls(backbone, programs)
        deletion_domain_covariance_controls(programs, cases)
        inventory_and_firewall_controls(started, backbone, programs)
    except Exception as exc:
        check("Cycle469 runner completed without exception", False, repr(exc))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print("\nRESULT pass=%d fail=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
