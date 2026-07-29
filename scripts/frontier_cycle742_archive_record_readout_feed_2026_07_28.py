#!/usr/bin/env python3
"""Cycle 742: bounded archive feed through the landed Record readout carrier.

Cycle 741's three-slot archive is embedded site by site into Cycle 693's
concrete ``Record(site, content)`` shape.  The bit-to-content injection and
the source decoder are declared junction conventions.  This runner proves
byte preservation through that mathematical readout path; it does not turn
the reversible archive sites into permanent framework Records.
"""
from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693
import frontier_cycle741_physical_bank_renewal_2026_07_28 as N741


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/ARCHIVE_RECORD_READOUT_FEED_CYCLE742_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
R693_SHA256 = "d5403ebbf51d8ecfaf621d5e0983d333b8df9a7d589145095b598c530ac15ab4"
R693_FROZEN_PASS_COUNT = 6
R693_FROZEN_FAIL_COUNT = 0
N741_SHA256 = "9365f7b8cd1a6e6a33473e11b8df01c14b3142d90173aba053c2c3983fb5b681"

BIT_TO_M2_ENCODING = {
    "0": "(Fraction(0), Fraction(0), Fraction(0), Fraction(0))",
    "1": "(Fraction(1), Fraction(0), Fraction(0), Fraction(0))",
}
C_SOURCE_FIREWALL = (
    "Any W5 `C_source` that decodes an archive site, packet, or image into "
    "`O` must therefore be an explicit junction convention or a separately "
    "derived physical decoder, not something attributed to Record."
)
PERMANENCE_WALL = (
    "byte preservation is proven, permanence is NOT; the locking mechanism "
    "remains the named W5 gap"
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool, detail: object = "") -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{json.dumps(detail, sort_keys=True, default=str)}"
    )
    return passed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def bits_sha256(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def nested_bits_sha256(packets: tuple[tuple[int, ...], ...]) -> tuple[str, ...]:
    return tuple(bits_sha256(packet) for packet in packets)


def archive_sites() -> tuple[tuple[int, int, int], ...]:
    layout = N741.K.M.R12.full_wire_layout()
    data_sites = tuple(layout["wire_sites"])
    return tuple(
        (
            data_sites[wire][0],
            data_sites[wire][1] + 11 * (slot + 1),
            data_sites[wire][2],
        )
        for slot in range(N741.ARCHIVE_SLOTS)
        for wire in N741.RECORD_WIRES
    )


def embed_archive(
    archives: tuple[tuple[int, ...], ...],
) -> tuple[R693.Record, ...]:
    if len(archives) != N741.ARCHIVE_SLOTS:
        raise ValueError(("archive slots", len(archives)))
    if any(len(slot) != N741.RECORD_WIDTH for slot in archives):
        raise ValueError("archive slot width")
    sites = archive_sites()
    bits = tuple(bit for slot in archives for bit in slot)
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("archive is not binary")
    return tuple(
        R693.Record(
            site=site,
            content=(R693.F(bit), R693.F(0), R693.F(0), R693.F(0)),
        )
        for site, bit in zip(sites, bits)
    )


def readout_bits(records: tuple[R693.Record, ...]) -> tuple[int, ...]:
    """Recover ordered bits solely through R693's public singleton readout."""
    values = tuple(R693.record_readout((record,)) for record in records)
    if any(value not in (R693.F(0), R693.F(1)) for value in values):
        raise ValueError("readout left the declared bit image")
    return tuple(int(value) for value in values)


def split_archive_bits(
    bits: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    if len(bits) != N741.ARCHIVE_WIDTH:
        raise ValueError(("archive width", len(bits)))
    return tuple(
        bits[
            slot * N741.RECORD_WIDTH:
            (slot + 1) * N741.RECORD_WIDTH
        ]
        for slot in range(N741.ARCHIVE_SLOTS)
    )


def payloads_from_record_image(
    image: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    if len(image) != N741.RECORD_WIDTH:
        raise ValueError(("record image width", len(image)))
    restored = list(N741.GENESIS_STATE)
    for wire, bit in zip(N741.RECORD_WIRES, image):
        restored[wire] = bit
    banks, _links = N741.K.M.unpack_state(
        tuple(restored), N741.FIXTURE_BANKS
    )
    return N741.cell_payloads(banks)


def run_r693_anchor(path: Path) -> dict[str, object]:
    environment = dict(os.environ)
    scripts_path = str(path.parent)
    prior_pythonpath = environment.get("PYTHONPATH")
    environment["PYTHONPATH"] = (
        scripts_path
        if not prior_pythonpath
        else scripts_path + os.pathsep + prior_pythonpath
    )
    completed = subprocess.run(
        [sys.executable, str(path), "--no-receipt"],
        cwd=path.parents[1],
        env=environment,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    lines = completed.stdout.splitlines()
    pass_lines = tuple(line for line in lines if line.startswith("PASS "))
    fail_lines = tuple(line for line in lines if line.startswith("FAIL "))
    summaries = tuple(
        json.loads(line.removeprefix("SUMMARY_JSON "))
        for line in lines
        if line.startswith("SUMMARY_JSON ")
    )
    summary = summaries[0] if len(summaries) == 1 else {}
    frozen = {
        "returncode": completed.returncode,
        "pass_lines": len(pass_lines),
        "fail_lines": len(fail_lines),
        "summary_pass_count": summary.get("pass_count"),
        "summary_fail_count": summary.get("fail_count"),
        "summary_pass": summary.get("pass"),
        "terminal_present":
            "RESULT RECORD_FIXES_ADDITIVE_FORM_NOT_FINITE_COMPLEX_EVENT_ALGEBRA"
            in lines,
        "stderr_empty": completed.stderr == "",
        "stdout_bytes": len(completed.stdout.encode()),
    }
    frozen["all_frozen_counts_exact"] = (
        frozen["returncode"] == 0
        and frozen["pass_lines"] == R693_FROZEN_PASS_COUNT
        and frozen["fail_lines"] == R693_FROZEN_FAIL_COUNT
        and frozen["summary_pass_count"] == R693_FROZEN_PASS_COUNT
        and frozen["summary_fail_count"] == R693_FROZEN_FAIL_COUNT
        and frozen["summary_pass"] is True
        and frozen["terminal_present"] is True
        and frozen["stderr_empty"] is True
    )
    return frozen


def root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets: list[ast.AST] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            raw = node.targets if isinstance(node, ast.Assign) else (node.target,)
            targets.extend(raw)
        elif isinstance(node, (ast.Delete, ast.NamedExpr)):
            raw = node.targets if isinstance(node, ast.Delete) else (node.target,)
            targets.extend(raw)
    return tuple(targets)


def no_write_ast_audit(
    r693_source: str,
    runner_source: str,
) -> dict[str, object]:
    r693_tree = ast.parse(r693_source)
    runner_tree = ast.parse(runner_source)
    r693_archive_identifiers = tuple(
        sorted({
            node.id
            for node in ast.walk(r693_tree)
            if isinstance(node, ast.Name) and "archive" in node.id.lower()
        })
    )
    module_target_writes = tuple(
        ast.unparse(target)
        for target in assignment_targets(runner_tree)
        if root_name(target) in {"R693", "N741"}
    )
    mutator_calls = []
    for node in ast.walk(runner_tree):
        if not isinstance(node, ast.Call):
            continue
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and root_name(node.args[0]) in {"R693", "N741"}
        ):
            mutator_calls.append(ast.unparse(node))
    return {
        "R693_archive_identifiers": r693_archive_identifiers,
        "R693_archive_identifier_count": len(r693_archive_identifiers),
        "runner_R693_N741_assignment_targets": module_target_writes,
        "runner_R693_N741_setattr_delattr_calls": tuple(mutator_calls),
        "pass":
            not r693_archive_identifiers
            and not module_target_writes
            and not mutator_calls,
    }


def main() -> int:
    started = perf_counter()
    r693_path = Path(R693.__file__).resolve()
    n741_path = Path(N741.__file__).resolve()
    runner_path = Path(__file__).resolve()
    hashes_before = {
        "R693": file_sha256(r693_path),
        "N741": file_sha256(n741_path),
    }

    anchor = run_r693_anchor(r693_path)
    check(
        "A_R693_anchor_unchanged_sha_and_frozen_counts",
        hashes_before["R693"] == R693_SHA256
        and anchor["all_frozen_counts_exact"],
        {
            "frozen_fail_count": R693_FROZEN_FAIL_COUNT,
            "frozen_pass_count": R693_FROZEN_PASS_COUNT,
            "observed": anchor,
            "sha256": hashes_before["R693"],
        },
    )

    word = N741.renewal_word()
    data = N741.GENESIS_STATE
    archives = (N741.ZERO_ARCHIVE_SLOT,) * N741.ARCHIVE_SLOTS
    generation_rows: list[dict[str, object]] = []
    archive_snapshots: list[tuple[tuple[int, ...], ...]] = []
    all_schema_roundtrips = True
    all_feed_exact = True

    for generation, directions in enumerate(
        N741.GENERATION_DIRECTIONS, start=1
    ):
        exhausted, fill = N741.fill_generation(data, directions)
        source_banks, _source_links = N741.K.M.unpack_state(
            exhausted, N741.FIXTURE_BANKS
        )
        source_payloads = N741.cell_payloads(source_banks)
        image = N741.record_image(exhausted)
        prior_archives = archives
        combined = N741.pack_combined(exhausted, archives)
        renewed = N741.K.A.apply_semantic(combined, word)
        data, archives = N741.split_combined(renewed)
        expected_archives = (image,) + prior_archives[:-1]

        before_readout = archives
        records = embed_archive(archives)
        flat_readout = readout_bits(records)
        read_archives = split_archive_bits(flat_readout)
        read_payloads = payloads_from_record_image(read_archives[0])
        aggregate_readout = R693.record_readout(records)
        after_readout = archives

        schema_roundtrip = (
            len(records) == N741.ARCHIVE_WIDTH == 909
            and read_archives == archives
            and before_readout == after_readout
            and aggregate_readout == sum(flat_readout)
        )
        packet_matches = tuple(
            bytes(observed) == bytes(expected)
            for observed, expected in zip(
                read_payloads, source_payloads
            )
        )
        feed_exact = (
            fill["violation_count"] == 0
            and fill["packet_count"] == N741.CAPACITY_ORBITS
            and archives == expected_archives
            and data == N741.GENESIS_STATE
            and len(source_payloads) == len(read_payloads) == 4
            and len(packet_matches) == 4
            and all(packet_matches)
        )
        all_schema_roundtrips &= schema_roundtrip
        all_feed_exact &= feed_exact
        archive_snapshots.append(archives)
        generation_rows.append({
            "archive_sha256":
                tuple(bits_sha256(slot) for slot in archives),
            "archive_sites_embedded": len(records),
            "archive_write_during_readout": before_readout != after_readout,
            "feed_exact": feed_exact,
            "generation": generation,
            "packet_byte_matches": packet_matches,
            "packet_sha256": nested_bits_sha256(read_payloads),
            "packets_read": len(read_payloads),
            "readout_archive_roundtrip": schema_roundtrip,
        })

    sites = archive_sites()
    layout = N741.K.M.R12.full_wire_layout()
    assigned_operating_sites = set(layout["assigned_sites"])
    embedding = {
        "archive_M2_sites": len(sites),
        "archive_slots": N741.ARCHIVE_SLOTS,
        "bit_to_M2_encoding": BIT_TO_M2_ENCODING,
        "C_source": (
            "For lexicographic (slot,offset), read the Cycle-741 archive bit "
            "and inject b as Record content (Fraction(b),0,0,0); site, slot "
            "age, generation, direction, and packet provenance are "
            "non-content metadata."
        ),
        "C_source_firewall": C_SOURCE_FIREWALL,
        "collection_convention": (
            "A supplied archive contributes all 909 sitewise Records in "
            "lexicographic (slot,offset) order. A blank register therefore "
            "has 909 zero-content Records; the absent collection is ()."
        ),
        "content_equality": "matrix-tuple equality independent of site metadata",
        "layout_bijection":
            len(sites) == len(set(sites)) == N741.ARCHIVE_WIDTH,
        "operating_site_collisions":
            len(set(sites) & assigned_operating_sites),
        "record_content_scalars": 4,
        "record_site_dimension": 3,
        "site_formula": (
            "(x_w, y_w + 11*(slot+1), z_w), "
            "w=RECORD_WIRES[offset]"
        ),
        "zero_fitted_parameters": True,
    }
    check(
        "B_embedding_exact_909_site_schema_roundtrip",
        N741.ARCHIVE_SLOTS == 3
        and N741.RECORD_WIDTH == 303
        and N741.ARCHIVE_WIDTH == 909
        and embedding["layout_bijection"]
        and embedding["operating_site_collisions"] == 0
        and embedding["zero_fitted_parameters"]
        and all_schema_roundtrips
        and len(generation_rows) == 3,
        embedding,
    )

    check(
        "C_readout_reproduces_four_archived_payloads_all_three_generations",
        all_feed_exact
        and len(generation_rows) == 3
        and all(
            row["packets_read"] == 4
            and all(row["packet_byte_matches"])
            for row in generation_rows
        ),
        {
            "generation_rows": generation_rows,
            "readout_entry_point": "R693.record_readout((record,))",
        },
    )

    final_archives = archives
    final_records = embed_archive(final_archives)
    final_readout = readout_bits(final_records)
    corrupted_flat = list(
        bit for slot in final_archives for bit in slot
    )
    corruption_index = 0
    corrupted_flat[corruption_index] ^= 1
    corrupted_archives = split_archive_bits(tuple(corrupted_flat))
    corrupted_records = embed_archive(corrupted_archives)
    corrupted_readout = readout_bits(corrupted_records)
    changed_indices = tuple(
        index
        for index, (left, right) in enumerate(
            zip(final_readout, corrupted_readout)
        )
        if left != right
    )
    aggregate_changed = (
        R693.record_readout(final_records)
        != R693.record_readout(corrupted_records)
    )
    blank_archives = (
        N741.ZERO_ARCHIVE_SLOT,
    ) * N741.ARCHIVE_SLOTS
    blank_records = embed_archive(blank_archives)
    blank_readout = readout_bits(blank_records)
    controls = {
        "aggregate_readout_changed": aggregate_changed,
        "blank_909_site_readout_all_zero": not any(blank_readout),
        "blank_aggregate_readout": str(R693.record_readout(blank_records)),
        "corrupted_bit_index": corruption_index,
        "empty_collection_readout": str(R693.record_readout(())),
        "ordered_changed_indices": changed_indices,
    }
    check(
        "D_corruption_detection_and_empty_archive_controls",
        changed_indices == (corruption_index,)
        and aggregate_changed
        and len(blank_records) == 909
        and not any(blank_readout)
        and R693.record_readout(blank_records) == R693.F(0)
        and R693.record_readout(()) == R693.F(0),
        controls,
    )

    isolation = no_write_ast_audit(
        r693_path.read_text(encoding="utf-8"),
        runner_path.read_text(encoding="utf-8"),
    )
    hashes_after = {
        "R693": file_sha256(r693_path),
        "N741": file_sha256(n741_path),
    }
    isolation.update({
        "archive_snapshots_immutable":
            len(archive_snapshots) == 3
            and all(
                row["archive_write_during_readout"] is False
                for row in generation_rows
            ),
        "input_hashes_after": hashes_after,
        "input_hashes_before": hashes_before,
        "input_modules_byte_unchanged": hashes_after == hashes_before,
        "N741_sha_pinned": hashes_before["N741"] == N741_SHA256,
    })
    check(
        "E_no_write_subprocess_and_AST_isolation_audit",
        isolation["pass"]
        and isolation["archive_snapshots_immutable"]
        and isolation["input_modules_byte_unchanged"]
        and isolation["N741_sha_pinned"],
        isolation,
    )

    supplies = (
        "sitewise Record granularity: all 3*303 archive sites",
        "physical content injection 0->diag(0,0), 1->diag(1,0)",
        "explicit total C_source with site/age/generation/direction/provenance non-content",
        "lexicographic all-sites collection convention and empty tuple value",
        "mathematical additive group G=(Q,+) and singleton trace weight; physical availability not claimed",
        "bounded domain: exactly three exhausted images, four packets each, newest-first; no fourth renewal",
    )
    pre_boundary_checks = tuple(CHECKS.values())
    boundary = {
        "byte_preservation_proven": all(pre_boundary_checks),
        "embedding_convention_supplied": True,
        "junction_feed_achieved": all(pre_boundary_checks),
        "locking_mechanism_status": "NEEDS-NEW-MECHANISM",
        "permanence_boundary": PERMANENCE_WALL,
        "record_permanence_claimed": False,
        "supplies": supplies,
    }
    check(
        "F_honest_boundary_keys",
        all(pre_boundary_checks)
        and boundary["record_permanence_claimed"] is False
        and boundary["junction_feed_achieved"] is True
        and boundary["embedding_convention_supplied"] is True
        and boundary["permanence_boundary"] == PERMANENCE_WALL
        and boundary["locking_mechanism_status"]
        == "NEEDS-NEW-MECHANISM"
        and len(boundary["supplies"]) == 6,
        boundary,
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "claim_boundary": boundary,
        "controls": controls,
        "embedding": embedding,
        "generation_feed": generation_rows,
        "isolation_audit": isolation,
        "pass": all(CHECKS.values()),
        "r693_anchor": {
            "frozen_counts": anchor,
            "sha256": hashes_before["R693"],
        },
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE742_ARCHIVE_RECORD_READOUT_FEED_PASS"
            if all(CHECKS.values())
            else "CYCLE742_ARCHIVE_RECORD_READOUT_FEED_HONEST_FAIL"
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode())))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
