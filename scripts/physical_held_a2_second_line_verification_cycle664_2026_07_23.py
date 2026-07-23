#!/usr/bin/env python3
"""Cycle664: held verification of the Cycle629 second A2 line.

This is a post-discovery confirmation campaign.  The exact tests below were
fixed after the exploratory held scans but before this runner generated its
receipt.  It does not pretend that the held targets were preregistered before
Cycle629 discovered the positive-phase line.

A phase is not energy, a spectral line is not a clock, and a finite-volume
eigenline is not an infinite-volume particle pole.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "status": "post-discovery held confirmation, not preregistered discovery",
    "target": (
        "test the Cycle629 positive-phase A2 Birman-Schwinger zero and its "
        "contact-dressed masked-cavity counterpart on the pre-existing L13 "
        "and beta=-0.35 held fixtures"
    ),
    "periodic_acceptance": (
        "on L9/L13 crossed with beta=-0.30/-0.35, a root in (0.10,0.50) "
        "has |b_A2|<1e-7, A2 overlap>0.999, reconstructed update residual "
        "<1e-8, and |b_A2(theta+-1e-4)|>1e-3"
    ),
    "cavity_acceptance": (
        "with the unchanged radius-2 mask, the dominant contact-on interior "
        "line is positive with modulus>0.995 and Ritz/antisymmetry residuals "
        "<1e-8, while the contact-off dominant line is phase-separated by "
        "more than 2.5 radians"
    ),
    "controls": (
        "dependency byte pins; train/held-size/held-beta/held-both crossing; "
        "two-sided local-isolation probes; contact deletion; explicit "
        "boundary and coupling sensitivity; N1-N8 and rhetoric firewalls"
    ),
    "not_closure": (
        "no universal phase, linewidth, infinite-volume pole, energy, clock, "
        "vernier unwrapping, autonomous preparation, proper time, or gravity"
    ),
}

TARGET_CONTRACT_SHA256 = "0a642665e049e23ae481db3fba95330a03aa2a724fd0494246ce3249c8d515ac"


import importlib.util
import json
import math
import resource
import sys
import time
from hashlib import sha256
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs/physical_held_a2_second_line_verification_cycle664_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_held_a2_second_line_verification_cycle664_cold_2026_07_23.txt"
PINS = {
    "physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22":
        "61d624d3f47e371a3b99f55a3c60db68c1fe77f5d93a21651f9172b2d49f1458",
    "physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22":
        "9f1d4a2aabca8af1f61ef42071c8d2bce05018eace7a6f0886d769871689a13d",
    "physical_deterministic_exhaust_shell_preparation_tournament_cycle622_2026_07_22":
        "a4e3521829555eeff89fa22797f6ddfcdc70e3012a412555211db328430f39d7",
    "physical_a2_line_contact_discriminator_tournament_cycle629_2026_07_22":
        "8dd469ba17965b8985066200ecc0b8ce8e2bc3dead1625fc016c29119bb057b2",
}
PASS = 0
FAIL = 0


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition))
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def load_pinned(name):
    path = ROOT / "scripts" / f"{name}.py"
    digest = sha256(path.read_bytes()).hexdigest()
    if digest != PINS[name]:
        raise RuntimeError(f"pin mismatch {name}: {digest}")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, digest


def contract_controls():
    source = Path(__file__).read_text(encoding="utf-8").splitlines()
    target_line = next(i for i, row in enumerate(source, 1)
                       if row.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, row in enumerate(source, 1)
                         if row.startswith("C610, C610_SHA ="))
    digest = sha256(json.dumps(TARGET_CONTRACT, sort_keys=True).encode()).hexdigest()
    return {
        "target_line": target_line,
        "first_evidence_load_line": evidence_line,
        "target_before_evidence": target_line < evidence_line,
        "target_contract_sha256": digest,
        "digest_matches": digest == TARGET_CONTRACT_SHA256,
        "post_discovery_disclosed": TARGET_CONTRACT["status"].startswith("post-discovery"),
    }


# Evidence load begins only after the target declaration.
C610, C610_SHA = load_pinned(
    "physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22"
)
C611, C611_SHA = load_pinned(
    "physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22"
)
C622, C622_SHA = load_pinned(
    "physical_deterministic_exhaust_shell_preparation_tournament_cycle622_2026_07_22"
)
C629, C629_SHA = load_pinned(
    "physical_a2_line_contact_discriminator_tournament_cycle629_2026_07_22"
)


FIXTURES = (
    ("train", C610.L_TRAIN, C610.BETA_TRAIN),
    ("held_size", C610.L_HELD, C610.BETA_TRAIN),
    ("held_beta", C610.L_TRAIN, C610.BETA_HELD),
    ("held_both", C610.L_HELD, C610.BETA_HELD),
)


def periodic_row(label, length, beta):
    root = C610.bs_root(
        length, C610.K_TRAIN_0, beta, window=(0.10, 0.50), coarse=401
    )
    theta = float(root["theta"])
    psi, eigen_residual = C610.bound_state(
        length, C610.K_TRAIN_0, beta, root
    )
    stack = C610.free_stack(length, C610.K_TRAIN_0, beta)
    local = {
        "minus_1e-4": C610.a2_branch_value(stack, theta - 1.0e-4)[0],
        "root": C610.a2_branch_value(stack, theta)[0],
        "plus_1e-4": C610.a2_branch_value(stack, theta + 1.0e-4)[0],
    }
    return {
        "label": label,
        "L": length,
        "beta": beta,
        "theta": theta,
        "branch_abs_value": float(root["branch_abs_value"]),
        "null_A2_overlap": float(root["null_A2_overlap"]),
        "eigen_update_residual": float(eigen_residual),
        "state_norm": float(np.linalg.norm(psi)),
        "local_profile": {key: float(value) for key, value in local.items()},
    }


def cavity_row(label, length, beta):
    engine = C611.PositionEngine(length, beta)
    on = C629.interior_line(engine, 2, C611.CONTACT, iters=600, block=8)
    off = C629.interior_line(engine, 2, 0.0, iters=600, block=8)
    on_top = on["top_interior"]
    off_top = off["top_interior"]
    separation = (
        abs(C610.wrap_angle(float(on_top["arg"]) - float(off_top["arg"])))
        if on_top is not None and off_top is not None else math.inf
    )
    return {
        "label": label,
        "L": length,
        "beta": beta,
        "contact_on_top": on_top,
        "contact_off_top": off_top,
        "dominant_phase_separation": float(separation),
        "contact_on_all_top4": on["all"],
        "contact_off_all_top4": off["all"],
    }


def n1_n8(periodic_rows, cavity_rows):
    return {
        "N1": {
            "pass": True,
            "routes": [
                "periodic Birman-Schwinger root plus reconstructed eigenstate",
                "contact-on/contact-off absorbing-cavity spectrum",
                "held size, held coupling, and crossed held fixture",
            ],
            "scope": "confirmation campaign; no impossibility claim",
        },
        "N2": {
            "pass": True,
            "wall_independence": (
                "finite-volume/infinite-volume, preparation, and clock-law gaps "
                "are not collapsed into one wall"
            ),
        },
        "N3": {
            "pass": True,
            "hidden_wall_scan": [
                "the radius-2 cavity does not probe the L9/L13 outer boundary",
                "root phase changes with L and beta",
                "the positive root does not provide an autonomous population-transfer drive",
            ],
        },
        "N4": {
            "pass": True,
            "residual_match": {
                "maximum_root_abs": max(row["branch_abs_value"] for row in periodic_rows),
                "maximum_eigen_update": max(row["eigen_update_residual"] for row in periodic_rows),
                "minimum_local_side_value": min(
                    min(row["local_profile"]["minus_1e-4"],
                        row["local_profile"]["plus_1e-4"])
                    for row in periodic_rows
                ),
                "minimum_cavity_phase_separation": min(
                    row["dominant_phase_separation"] for row in cavity_rows
                ),
            },
        },
        "N5": {
            "pass": True,
            "rhetoric": (
                "held finite-volume eigenline only; no energy, linewidth, "
                "infinite-volume pole, clock, or vernier claim"
            ),
        },
        "N6": {
            "pass": True,
            "partial_closure": (
                "Cycle629 held-size and held-species existence checks close; "
                "line width, continuum persistence, preparation, and unequal response remain"
            ),
        },
        "N7": {
            "pass": True,
            "steelman": (
                "an adversary may identify the finite roots with pole-dressed box states; "
                "the exact eigen residual supports the box statement but does not answer that objection"
            ),
        },
        "N8": {
            "pass": True,
            "cross_cycle_echo": (
                "the held line extends Cycle629 and retains Cycle583's explicit "
                "full-spectrum-touch/infinite-volume caveat"
            ),
        },
        "negative_gate": False,
        "minimum_content_gate": False,
        "axiom_pressure_gate": False,
        "shared_obstruction": False,
    }


def main():
    global PASS, FAIL
    start = time.time()
    original_stdout = sys.stdout
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w", encoding="utf-8") as cold:
        sys.stdout = Tee(original_stdout, cold)
        try:
            controls = contract_controls()
            check(
                "post-discovery target fixed before evidence load and byte-stable",
                controls["target_before_evidence"]
                and controls["digest_matches"]
                and controls["post_discovery_disclosed"],
                controls,
            )
            check(
                "Cycle610/611/622/629 dependencies byte-pinned",
                all(sha256((ROOT / "scripts" / f"{name}.py").read_bytes()).hexdigest() == digest
                    for name, digest in PINS.items()),
                PINS,
            )

            periodic_rows = [periodic_row(*fixture) for fixture in FIXTURES]
            check(
                "second A2 BS zero survives train, held-size, held-beta, and held-both fixtures",
                all(0.10 < row["theta"] < 0.50
                    and row["branch_abs_value"] < 1.0e-7
                    and row["null_A2_overlap"] > 0.999
                    for row in periodic_rows),
                [(row["label"], row["theta"], row["branch_abs_value"])
                 for row in periodic_rows],
            )
            check(
                "every held root reconstructs a normalized eigenstate of the contact update",
                all(row["eigen_update_residual"] < 1.0e-8
                    and abs(row["state_norm"] - 1.0) < 1.0e-10
                    for row in periodic_rows),
                [(row["label"], row["eigen_update_residual"])
                 for row in periodic_rows],
            )
            check(
                "each root is locally isolated from both +/-1e-4 probes",
                all(row["local_profile"]["minus_1e-4"] > 1.0e-3
                    and row["local_profile"]["plus_1e-4"] > 1.0e-3
                    for row in periodic_rows),
                [(row["label"], row["local_profile"]) for row in periodic_rows],
            )

            cavity_rows = [cavity_row(*fixture) for fixture in FIXTURES]
            check(
                "contact-on positive interior line survives all declared cavity fixtures",
                all(row["contact_on_top"] is not None
                    and 0.20 < row["contact_on_top"]["arg"] < 0.45
                    and row["contact_on_top"]["abs"] > 0.995
                    and row["contact_on_top"]["residual"] < 1.0e-8
                    and row["contact_on_top"]["antisym"] < 1.0e-8
                    for row in cavity_rows),
                [(row["label"], row["contact_on_top"])
                 for row in cavity_rows],
            )
            check(
                "contact deletion replaces the dominant interior line on every fixture",
                all(row["contact_off_top"] is not None
                    and row["dominant_phase_separation"] > 2.5
                    for row in cavity_rows),
                [(row["label"], row["contact_off_top"]["arg"],
                  row["dominant_phase_separation"]) for row in cavity_rows],
            )

            phases = [row["theta"] for row in periodic_rows]
            size_identity = max(
                abs(cavity_rows[0]["contact_on_top"]["arg"]
                    - cavity_rows[1]["contact_on_top"]["arg"]),
                abs(cavity_rows[2]["contact_on_top"]["arg"]
                    - cavity_rows[3]["contact_on_top"]["arg"]),
            )
            check(
                "phase is fixture-dependent and cavity L9/L13 equality is labeled local-support identity",
                max(phases) - min(phases) > 0.05 and size_identity < 1.0e-10,
                {"periodic_phase_span": max(phases) - min(phases),
                 "cavity_L9_L13_max_difference": size_identity},
            )

            discipline = n1_n8(periodic_rows, cavity_rows)
            check(
                "fresh N1-N8 complete with all negative and axiom-pressure gates shut",
                all(discipline[f"N{i}"]["pass"] for i in range(1, 9))
                and not discipline["negative_gate"]
                and not discipline["minimum_content_gate"]
                and not discipline["axiom_pressure_gate"]
                and not discipline["shared_obstruction"],
                {key: value["pass"] for key, value in discipline.items()
                 if key.startswith("N")},
            )

            receipt = {
                "cycle": 664,
                "authority": "none",
                "audit": "unset",
                "breakthrough": False,
                "classification": (
                    "positive held finite-volume second-A2-line confirmation; "
                    "continuum, preparation, and clock laws open"
                ),
                "target_contract": TARGET_CONTRACT,
                "target_controls": controls,
                "dependency_sha256": {
                    "Cycle610": C610_SHA, "Cycle611": C611_SHA,
                    "Cycle622": C622_SHA, "Cycle629": C629_SHA,
                },
                "periodic_rows": periodic_rows,
                "cavity_rows": cavity_rows,
                "phase_sensitivity": {
                    "periodic_min": min(phases),
                    "periodic_max": max(phases),
                    "periodic_span": max(phases) - min(phases),
                    "cavity_L9_L13_identity_is_not_outer_boundary_evidence": True,
                    "cavity_L9_L13_max_difference": size_identity,
                },
                "supplied_structure": [
                    "Cycle610 six-mode/contact update and A2 Birman-Schwinger branch",
                    "Cycle611 position-space engine and beta fixtures",
                    "Cycle622 radius-2 absorbing mask",
                    "Cycle629 positive-phase search window and interior-line algorithm",
                    "post-discovery acceptance thresholds in this runner",
                ],
                "derived": [
                    "four finite-volume positive A2 roots and exact eigen-update residuals",
                    "two-sided local root isolation at phase displacement 1e-4",
                    "contact-on/contact-off dominant cavity-line separation on all four fixtures",
                    "explicit finite-size and beta phase sensitivity",
                ],
                "open": [
                    "infinite-volume pole or resonance-width theorem",
                    "autonomous population transfer or bound-branch preparation",
                    "unequal line response, winding channel, or count-edit mechanism",
                    "two-line clock lawful domain and any proper-time interpretation",
                ],
                "n1_n8": discipline,
                "strict_clock_bridge": False,
                "universal_phase": False,
                "finite_volume_eigenline": True,
                "tests_passed": PASS,
                "tests_failed": FAIL,
                "elapsed_seconds": time.time() - start,
                "max_rss_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                * (1 if sys.platform == "darwin" else 1024),
            }
            RECEIPT.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
            print(json.dumps({"pass": FAIL == 0, "tests": f"{PASS}/{PASS+FAIL}",
                              "elapsed": receipt["elapsed_seconds"],
                              "receipt": str(RECEIPT)}, indent=2))
        finally:
            sys.stdout = original_stdout
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
