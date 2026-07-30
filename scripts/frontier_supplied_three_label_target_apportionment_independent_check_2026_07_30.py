#!/usr/bin/env python3
"""Independent integer check of the supplied three-label comparator fixture."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/SUPPLIED_THREE_LABEL_TARGET_APPORTIONMENT_COMPARATOR_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
PRIMARY_PATH = (
    "scripts/frontier_supplied_three_label_target_apportionment_"
    "comparator_2026_07_30.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_supplied_three_label_target_apportionment_independent_check_2026_07_30.py",
    "scripts/frontier_supplied_three_label_target_apportionment_comparator_2026_07_30.py",
    "docs/SUPPLIED_THREE_LABEL_TARGET_APPORTIONMENT_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-07-30.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PRIMARY_SHA256 = (
    "c4c9320fc3003967809cf5fb82f2d5a429a8230e9b44a7965d99c37456434ef7"
)
TARGET_NUMERATORS = (
    36_002_393_478_282_646,
    21_194_155_104_147_802,
    42_803_451_417_569_552,
)
TARGET_DENOMINATOR = 100_000_000_000_000_000
PROFILE_SIZES = (8, 32, 128, 512)
EXPECTED_PROFILE_COUNTS = (
    (3, 2, 3),
    (11, 7, 14),
    (46, 27, 55),
    (184, 109, 219),
)
TOLERANCE_PAIRS = ((3, 50), (1, 50), (1, 500), (1, 1000))
EXPECTED_DISAGREEMENT_COUNTS = (
    (0, 2, 3, 3),
    (0, 0, 3, 3),
    (0, 0, 0, 2),
    (0, 0, 0, 0),
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def declared_hashes() -> dict[str, str]:
    return {relative: digest(ROOT / relative) for relative in AUDIT_INPUT_PATHS}


def integer_apportionment(size: int) -> tuple[int, ...]:
    quotients = []
    remainders = []
    for numerator in TARGET_NUMERATORS:
        quotient, remainder = divmod(size * numerator, TARGET_DENOMINATOR)
        quotients.append(quotient)
        remainders.append(remainder)
    order = sorted(
        range(len(remainders)),
        key=lambda index: (remainders[index], -index),
        reverse=True,
    )
    for index in order[: size - sum(quotients)]:
        quotients[index] += 1
    return tuple(quotients)


def integer_disagreement_counts(
    size: int, counts: tuple[int, ...]
) -> tuple[int, ...]:
    residual_numerators = tuple(
        count * TARGET_DENOMINATOR - target_numerator * size
        for count, target_numerator in zip(counts, TARGET_NUMERATORS, strict=True)
    )
    residual_denominator = size * TARGET_DENOMINATOR
    return tuple(
        sum(
            abs(residual_numerator) * tolerance_denominator
            > tolerance_numerator * residual_denominator
            for residual_numerator in residual_numerators
        )
        for tolerance_numerator, tolerance_denominator in TOLERANCE_PAIRS
    )


def clean_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def run_primary(root: Path) -> tuple[int | str, str]:
    try:
        completed = subprocess.run(
            [sys.executable, str(root / PRIMARY_PATH)],
            cwd=root,
            env=clean_environment(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        return completed.returncode, completed.stdout
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout or ""
        output = (
            raw.decode("utf-8", errors="replace")
            if isinstance(raw, bytes)
            else raw
        )
        return "timeout", output


def parse_primary(output: str) -> tuple[tuple[int, int] | None, dict | None]:
    matches = re.findall(
        r"^SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)\s+RUNTIME_SEC\s+[0-9.]+$",
        output,
        re.MULTILINE,
    )
    summary = tuple(map(int, matches[-1])) if matches else None
    payload = None
    for line in output.splitlines():
        if line.startswith("RESULT_JSON "):
            try:
                payload = json.loads(line.removeprefix("RESULT_JSON "))
            except json.JSONDecodeError:
                payload = None
    return summary, payload


def target_normalization_mutation_control() -> dict[str, object]:
    with tempfile.TemporaryDirectory(
        prefix="three-label-comparator-pin-"
    ) as temp_name:
        temp_root = Path(temp_name)
        for relative in (PRIMARY_PATH, NOTE_PATH):
            destination = temp_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        primary = temp_root / PRIMARY_PATH
        source = primary.read_text(encoding="utf-8")
        mutated = source.replace(
            "42_803_451_417_569_552",
            "42_803_451_417_569_551",
            1,
        )
        primary.write_text(mutated, encoding="utf-8")
        returncode, output = run_primary(temp_root)
        summary, payload = parse_primary(output)
        return {
            "returncode": returncode,
            "summary": summary,
            "payload_present": payload is not None,
            "normalization_failure_seen": (
                "supplied target is an exact rational simplex" in output
                and "FAIL" in output
            ),
        }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    hashes_before = declared_hashes()

    primary_sha = digest(ROOT / PRIMARY_PATH)
    check(
        "primary source matches the independent hard pin",
        primary_sha == EXPECTED_PRIMARY_SHA256,
        primary_sha,
    )

    apportioned = tuple(integer_apportionment(size) for size in PROFILE_SIZES)
    disagreement_rows = tuple(
        integer_disagreement_counts(size, counts)
        for size, counts in zip(PROFILE_SIZES, apportioned, strict=True)
    )
    check(
        "independent integer route reconstructs every supplied apportionment and disagreement row",
        apportioned == EXPECTED_PROFILE_COUNTS
        and disagreement_rows == EXPECTED_DISAGREEMENT_COUNTS
        and sum(TARGET_NUMERATORS) == TARGET_DENOMINATOR,
        {
            "apportioned": apportioned,
            "disagreement_rows": disagreement_rows,
        },
    )

    control_rows = tuple(
        integer_disagreement_counts(size, (size, 0, 0))
        for size in PROFILE_SIZES
    )
    check(
        "independent integer route reconstructs the hostile-control census",
        all(row == (3, 3, 3, 3) for row in control_rows),
        control_rows,
    )

    returncode, output = run_primary(ROOT)
    summary, payload = parse_primary(output)
    check(
        "clean black-box primary agrees with the independent integer route",
        returncode == 0
        and summary is not None
        and summary[1] == 0
        and payload is not None
        and payload.get("fixture_kind")
        == "authored-largest-remainder-target-apportionment"
        and tuple(
            tuple(row["counts"]) for row in payload.get("profile_rows", ())
        )
        == apportioned
        and tuple(
            tuple(row["disagreement_counts"])
            for row in payload.get("profile_rows", ())
        )
        == disagreement_rows
        and payload.get("boundaries", {}).get("asymptotic_convergence_claimed")
        is False
        and payload.get("boundaries", {}).get("born_law_selected") is False,
        {"returncode": returncode, "summary": summary, "payload": payload},
    )

    mutation = target_normalization_mutation_control()
    check(
        "one-numerator mutation makes the production primary fail closed",
        mutation["returncode"] != 0
        and mutation["summary"] is not None
        and mutation["summary"][1] > 0
        and mutation["normalization_failure_seen"] is True,
        mutation,
    )

    hashes_after = declared_hashes()
    check(
        "declared source inputs stayed byte-stable",
        hashes_before == hashes_after
        and set(hashes_after) == set(AUDIT_INPUT_PATHS),
        hashes_after,
    )

    runtime = perf_counter() - started
    result = {
        "all_checks_pass": FAIL == 0,
        "check_totals": {"fail": FAIL, "pass": PASS},
        "independent_apportionments": apportioned,
        "independent_control_rows": control_rows,
        "independent_disagreement_rows": disagreement_rows,
        "primary_sha256": primary_sha,
        "runtime_seconds": round(runtime, 6),
    }
    print("SUMMARY PASS", PASS, "FAIL", FAIL, "RUNTIME_SEC", f"{runtime:.6f}")
    print("RESULT_JSON", json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
