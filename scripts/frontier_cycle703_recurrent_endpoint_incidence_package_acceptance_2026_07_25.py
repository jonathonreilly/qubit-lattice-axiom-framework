#!/usr/bin/env python3
"""Fail-closed acceptance replay for the load-bearing Cycle-703/704 surfaces.

This is an integration runner, not an additional physics derivation.  It pins
and executes the seven independent runners that carry the three scoped route
negatives, finite common-E closure, returned-work edge-qubit preparation,
scaled local-Gauss edge-qubit tableaus/update, and the conditional Cycle-612
software bridge.  Each child runs in a fresh interpreter.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import TYPE_CHECKING

# These imports are intentionally type-check-only: the citation-graph walker
# follows them into the complete source packet, while runtime isolation keeps
# module globals from allowing one child to certify another.
if TYPE_CHECKING:
    import frontier_common_e_gauge_corrected_physical_rom_composition_2026_07_25
    import frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25
    import frontier_cycle703_bksf_patch_tableau_covariance_2026_07_25
    import frontier_cycle703_local_encoding_rephase_cohomology_2026_07_25
    import frontier_cycle703_reversible_echo_ack_controller_2026_07_25
    import frontier_cycle703_two_frame_colored_rephase_2026_07_25
    import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0

CHILDREN = (
    (
        "same_register_rephase_negative",
        "scripts/frontier_cycle703_local_encoding_rephase_cohomology_2026_07_25.py",
        "d8b9ce2faa9c8ca5f64be558b9fa1a4734f9ecfe749454c3708ea49968a5fc0c",
        "CYCLE703_REPHASE_ODD_ORBITS_4_22_34_HELD_100_156",
    ),
    (
        "colored_two_frame_held_negative",
        "scripts/frontier_cycle703_two_frame_colored_rephase_2026_07_25.py",
        "d9e88ba7e9a2eaa01095f755b1b6c1819708a17b480b866ccb4f51069b8bbfce",
        "CYCLE703_TWO_FRAME_TRAIN_EXACT_HELD_714_906_FORCED_CONFLICTS_251_224",
    ),
    (
        "exact_three_M2_support_negative",
        "scripts/frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25.py",
        "a324dfadc0f6269d738539dca84fbe43bd2b596700235839f712207198ff8586",
        "RESULT EXACT_THREE_DATA_M2_TRANSLATOR_NO_UNITARY_N1_N8_PASS_LARGER_SUPPORT_OPEN",
    ),
    (
        "finite_common_E",
        "scripts/frontier_common_e_gauge_corrected_physical_rom_composition_2026_07_25.py",
        "45be1df3bb00f76bae77278bc1aea242df8af82b1828630e7f7a1132f2ad162e",
        "ACTUAL_59941_ROW_GAUGE_CORRECTED_CAR_COMPILER_CLOSED",
    ),
    (
        "returned_work_preparation",
        "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py",
        "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
        "CYCLE703_ECHO_WORK_RETURNED_SYNDROME_BANK_FACTORS_AND_STAYS_INERT",
    ),
    (
        "scaled_local_Gauss",
        "scripts/frontier_cycle703_bksf_patch_tableau_covariance_2026_07_25.py",
        "8240ab7d3cd27f3058a7b44c1cfe35dda638cf011fbdd12ccecc1bc8054043c9",
        "RESULT PATCH_AND_PERIODIC_BKSF_TABLEAU_COVARIANCE_POSITIVE_GEOMETRIC_PREPARATION_OPEN",
    ),
    (
        "conditional_Cycle612_bridge",
        "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
        "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a",
        "RESULT LOCAL_GAUSS_ENDPOINT_SOFTWARE_PACKET_INTERFACE_CLOSED_PHYSICAL_BANK_OPEN",
    ),
)


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def replay_child(
    name: str, relative_path: str, expected_sha256: str, terminal: str
) -> dict[str, object]:
    path = ROOT / relative_path
    actual_sha256 = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    hash_ok = actual_sha256 == expected_sha256
    check(f"{name} source pin", hash_ok, actual_sha256)
    if not hash_ok:
        return {
            "name": name,
            "path": relative_path,
            "returncode": None,
            "source_sha256": actual_sha256,
            "terminal_present": False,
            "fail_lines": ["source pin mismatch"],
        }

    environment = os.environ.copy()
    environment["PYTHONHASHSEED"] = "0"
    run = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        timeout=1800,
        check=False,
    )
    lines = run.stdout.splitlines()
    fail_lines = [line for line in lines if line.startswith("FAIL ")]
    terminal_present = terminal in lines
    stderr_clean = not run.stderr.strip()
    check(
        f"{name} isolated replay",
        run.returncode == 0 and not fail_lines and terminal_present and stderr_clean,
        {
            "returncode": run.returncode,
            "fail_lines": len(fail_lines),
            "terminal_present": terminal_present,
            "stderr_clean": stderr_clean,
            "stdout_lines": len(lines),
        },
    )
    return {
        "name": name,
        "path": relative_path,
        "returncode": run.returncode,
        "source_sha256": actual_sha256,
        "terminal_present": terminal_present,
        "fail_lines": fail_lines,
        "stderr": run.stderr.strip(),
    }


def main() -> int:
    rows = [replay_child(*child) for child in CHILDREN]
    summary = {
        "audit": "unset",
        "authority": "none",
        "claim_scope": "Cycle703/704 package acceptance; no new physics claim",
        "pass": PASS,
        "fail": FAIL,
        "children": rows,
        "terminal": "CYCLE703_RECURRENT_ENDPOINT_INCIDENCE_PACKAGE_ACCEPTANCE_CLOSED",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        return 1
    print("CYCLE703_RECURRENT_ENDPOINT_INCIDENCE_PACKAGE_ACCEPTANCE_CLOSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
