#!/usr/bin/env python3
"""Cold package acceptance for the Cycle-871 endpoint/packet composition."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as primary
import frontier_cycle871_selected_openreference_seam_cycle714_packet_bridge_check_2026_08_02 as independent
import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as cycle713
import frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26 as cycle714
import frontier_cycle718_cycle612_interval_bridge_2026_07_26 as cycle718


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1500
CHILD_TIMEOUT_SEC = 600
OUTPUT = (
    ROOT
    / "outputs"
    / "cycle871_openreference_endpoint_packet_package_acceptance_receipt_2026_08_02.json"
)
AUDIT_INPUT_PATHS = (
    "docs/OPENREFERENCE_MATTER_ENDPOINT_CAUSAL_INTERVAL_PACKET_CYCLE871_BOUNDED_THEOREM_NOTE_2026-08-02.md",
    "scripts/frontier_cycle871_openreference_endpoint_packet_package_acceptance_2026_08_02.py",
    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py",
    "outputs/cycle871_openreference_endpoint_packet_bridge_receipt_2026_08_02.json",
    "scripts/frontier_cycle871_selected_openreference_seam_cycle714_packet_bridge_check_2026_08_02.py",
    "outputs/cycle871_selected_openreference_seam_cycle714_packet_bridge_check_receipt_2026_08_02.json",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

IMPORTED_HELPER_MODULES = (
    primary,
    independent,
    cycle713,
    cycle714,
    cycle718,
)

RUNNERS = (
    {
        "name": "cycle871_primary",
        "source": "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py",
        "source_sha256": "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
        "marker": "CYCLE871_OPENREFERENCE_ENDPOINT_PACKET_PASS",
        "receipt": "outputs/cycle871_openreference_endpoint_packet_bridge_receipt_2026_08_02.json",
        "receipt_sha256": "fc1b34f4802aed2888010e299f8d641ee0f6448d83483fcc83bdb1d063dc0861",
    },
    {
        "name": "cycle871_independent",
        "source": "scripts/frontier_cycle871_selected_openreference_seam_cycle714_packet_bridge_check_2026_08_02.py",
        "source_sha256": "79855daab192d81af82c1c4f141ad6a7c45974a97db326f8a81f523c962c1b4b",
        "marker": "CYCLE871_SELECTED_OPENREFERENCE_SEAM_CYCLE714_PACKET_BRIDGE_CHECK_PASS",
        "receipt": "outputs/cycle871_selected_openreference_seam_cycle714_packet_bridge_check_receipt_2026_08_02.json",
        "receipt_sha256": "e8ceb57382957f08b523e96e617153ea9fd6807cc756bc6f5568ccdf67d52cdf",
    },
    {
        "name": "cycle713_endpoint_regression",
        "source": "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
        "source_sha256": "b61f98d0b44c1496883e8ab2ae1db065772ed053c77b6661a0153086acfd0e2f",
        "marker": "CYCLE713_PHYSICAL_M2_ENDPOINT_INSTRUMENT_BRIDGE_PASS",
    },
    {
        "name": "cycle714_packet_regression",
        "source": "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
        "source_sha256": "357e52e75d014cdab338f2655e8b1d2b18e64915a7826fd93a10a2ac3fd03347",
        "marker": "CYCLE714_FIXED_PACKET_COHERENT_COMPOSITION_PASS",
    },
    {
        "name": "cycle718_interval_regression",
        "source": "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
        "source_sha256": "f197b896ec97def6dabed308b3b3cd5fa5fd307878e50ab5a1ffc73208f0946f",
        "marker": "CYCLE718_CYCLE612_INTERVAL_BRIDGE_PASS",
    },
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def receipt_failures(name: str, payload: dict[str, object]) -> tuple[str, ...]:
    if name == "cycle871_primary":
        return () if (
            payload.get("status") == "pass"
            and not payload.get("validation_failures")
            and not payload.get("provenance", {}).get("pinned_input_failures")
            and not payload.get("provenance", {}).get("unpinned_declared_inputs")
        ) else ("primary receipt semantics",)
    if name == "cycle871_independent":
        return () if (
            payload.get("status")
            == "cycle871-selected-openreference-seam-cycle714-packet-bridge-check-pass"
            and all(payload.get("checks", {}).values())
            and not payload.get("dependency_pin_failures")
        ) else ("independent receipt semantics",)
    return (f"unknown receipt owner:{name}",)


def main() -> int:
    failures: list[str] = []
    rows: list[dict[str, object]] = []
    for contract in RUNNERS:
        name = contract["name"]
        source = ROOT / contract["source"]
        observed_source = digest(source)
        source_match = observed_source == contract["source_sha256"]
        if not source_match:
            failures.append(f"{name}:source pin")
            rows.append({
                **contract,
                "observed_source_sha256": observed_source,
                "executed": False,
            })
            continue
        try:
            completed = subprocess.run(
                (sys.executable, "-B", contract["source"]),
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=CHILD_TIMEOUT_SEC,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{name}:timeout>{CHILD_TIMEOUT_SEC}s")
            rows.append({
                **contract,
                "observed_source_sha256": observed_source,
                "executed": False,
                "timeout_seconds": CHILD_TIMEOUT_SEC,
            })
            continue

        marker_seen = contract["marker"] in completed.stdout
        if completed.returncode != 0:
            failures.append(f"{name}:exit={completed.returncode}")
        if not marker_seen:
            failures.append(f"{name}:terminal marker")

        receipt_semantic_failures: tuple[str, ...] = ()
        observed_receipt = None
        receipt_match = None
        if "receipt" in contract:
            receipt_path = ROOT / contract["receipt"]
            observed_receipt = digest(receipt_path) if receipt_path.is_file() else None
            receipt_match = observed_receipt == contract["receipt_sha256"]
            if not receipt_match:
                failures.append(f"{name}:receipt pin")
            if receipt_path.is_file():
                receipt_semantic_failures = receipt_failures(
                    name, json.loads(receipt_path.read_text())
                )
            else:
                receipt_semantic_failures = ("missing receipt",)
            failures.extend(
                f"{name}:{failure}" for failure in receipt_semantic_failures
            )

        rows.append({
            **contract,
            "observed_source_sha256": observed_source,
            "source_pin_match": source_match,
            "observed_receipt_sha256": observed_receipt,
            "receipt_pin_match": receipt_match,
            "receipt_semantic_failures": receipt_semantic_failures,
            "returncode": completed.returncode,
            "terminal_marker_seen": marker_seen,
            "executed": completed.returncode == 0,
        })

    artifact = Path(__file__).resolve()
    report: dict[str, object] = {
        "cycle": 871,
        "status": "pass" if not failures else "fail",
        "authority": "none",
        "audit": "unset",
        "artifact": {
            "path": str(artifact.relative_to(ROOT)),
            "sha256": digest(artifact),
        },
        "static_audit_helper_modules": tuple(
            module.__name__ for module in IMPORTED_HELPER_MODULES
        ),
        "runner_rows": rows,
        "validation_failures": failures,
        "package_acceptance_pass": not failures,
        "acceptance_scope": (
            "cold execution, source/receipt pins, terminal markers, receipt "
            "semantics, and unchanged Cycle713/714/718 interface regressions"
        ),
    }
    report["content_sha256_before_hash_field"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True, default=str) + "\n")
    print(
        "CYCLE871_ENDPOINT_PACKET_PACKAGE_ACCEPTANCE_PASS"
        if not failures
        else "CYCLE871_ENDPOINT_PACKET_PACKAGE_ACCEPTANCE_FAIL"
    )
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
