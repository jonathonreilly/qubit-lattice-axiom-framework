#!/usr/bin/env python3
"""Fast certificate for the cached finite-lattice BH entropy comparison."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/BH_ENTROPY_DERIVED_NOTE.md"
CACHE = REPO_ROOT / "logs/runner-cache/frontier_bh_entropy_derived.txt"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "bh_entropy_derived_note"
RUNNER_PATH = "scripts/frontier_bh_entropy_derived.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** bounded_theorem",
        "Status:** bounded finite-lattice cache certificate",
        "not a derivation of the Bekenstein-Hawking coefficient",
        "finite observations",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE",
        "retained",
        "L = 64",
        "L = 96",
        "c_Widom",
        "asymptote",
    ]
    for phrase in forbidden:
        check(f"note omits broad-scope phrase: {phrase}", phrase not in text)


def cache_header_checks(cache: str) -> None:
    print("\n=== finite-lattice BH entropy cache ===")
    for phrase in [
        "runner: scripts/frontier_bh_entropy_derived.py",
        "exit_code: 0",
        "status: ok",
        "CHECKS PASSED: 5/5",
    ]:
        check(f"cache contains: {phrase}", phrase in cache)


def cache_area_checks(cache: str) -> None:
    r2_2d = re.search(r"PASS 2D area law \(R\^2 > 0\.999\): True\s+\(R\^2 = (?P<value>\d\.\d{6})\)", cache)
    r2_3d = re.search(r"PASS 3D area law \(R\^2 > 0\.998\): True\s+\(R\^2 = (?P<value>\d\.\d{6})\)", cache)
    check("2D area-law row parsed", r2_2d is not None)
    check("3D area-law row parsed", r2_3d is not None)
    if r2_2d is not None:
        value = float(r2_2d.group("value"))
        check("2D finite fit R^2 exceeds 0.999", value > 0.999, f"{value:.6f}", kind="C")
        check("2D finite fit R^2 matches certificate", math.isclose(value, 0.999664, abs_tol=1e-12), f"{value:.6f}", kind="C")
    if r2_3d is not None:
        value = float(r2_3d.group("value"))
        check("3D finite fit R^2 exceeds 0.998", value > 0.998, f"{value:.6f}", kind="C")
        check("3D finite fit R^2 matches certificate", math.isclose(value, 0.998952, abs_tol=1e-12), f"{value:.6f}", kind="C")


def cache_rt_ratio_checks(cache: str) -> None:
    mean_2d = re.search(r"Mean RT ratio \(2D\): (?P<value>\d\.\d{4})\s+\(dev (?P<dev>\d+\.\d)%\)", cache)
    mean_3d = re.search(r"Mean RT ratio \(3D\): (?P<value>\d\.\d{4})\s+\(dev (?P<dev>\d+\.\d)%\)", cache)
    pass_2d = "2D finite-L comparison within 15% of 1/4: True" in cache
    pass_3d = "3D finite-L comparison within 15% of 1/4: False" in cache
    check("2D finite RT mean parsed", mean_2d is not None)
    check("3D finite RT mean parsed", mean_3d is not None)
    check("2D finite comparison is near 1/4", pass_2d, kind="C")
    check("3D finite comparison is not near 1/4", pass_3d, kind="C")
    if mean_2d is not None:
        value = float(mean_2d.group("value"))
        dev = float(mean_2d.group("dev"))
        check("2D finite RT mean is 0.2364", math.isclose(value, 0.2364, abs_tol=1e-12), f"{value:.4f}", kind="C")
        check("2D finite RT deviation is 5.4 percent", math.isclose(dev, 5.4, abs_tol=1e-12), f"{dev:.1f}", kind="C")
    if mean_3d is not None:
        value = float(mean_3d.group("value"))
        dev = float(mean_3d.group("dev"))
        check("3D finite RT mean is 0.1222", math.isclose(value, 0.1222, abs_tol=1e-12), f"{value:.4f}", kind="C")
        check("3D finite RT deviation is 51.1 percent", math.isclose(dev, 51.1, abs_tol=1e-12), f"{dev:.1f}", kind="C")


def cache_additional_checks(cache: str) -> None:
    monotone = re.search(r"Monotone decrease for g >= 0\.5: (?P<value>True|False)", cache)
    species = re.search(r"RT ratio spread across species: (?P<value>\d\.\d{6})", cache)
    summary_species = re.search(r"SPECIES UNIVERSALITY: RT ratio spread = (?P<value>\d\.\d+e[+-]\d+)", cache)
    check("gravity monotonicity row parsed", monotone is not None)
    check("species spread row parsed", species is not None)
    check("summary species spread row parsed", summary_species is not None)
    if monotone is not None:
        check("gravity modulation is monotone for g >= 0.5", monotone.group("value") == "True", kind="C")
    if species is not None:
        check("printed species spread rounds to zero", float(species.group("value")) == 0.0, species.group("value"), kind="C")
    if summary_species is not None:
        value = float(summary_species.group("value"))
        check("summary species spread is below 1e-12", value < 1e-12, f"{value:.2e}", kind="C")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type remains bounded_theorem", row.get("claim_type") == "bounded_theorem")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 70, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    cache = CACHE.read_text(encoding="utf-8")
    cache_header_checks(cache)
    cache_area_checks(cache)
    cache_rt_ratio_checks(cache)
    cache_additional_checks(cache)
    audit_metadata_checks()
    print("\nBH entropy finite-lattice cache certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
