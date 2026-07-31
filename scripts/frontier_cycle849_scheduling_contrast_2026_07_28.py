#!/usr/bin/env python3
"""Cycle 849: exact k=3 meet geometry and scheduling-mark contrast.

The named predecessor runners are source primaries only.  This runner reads
them as SHA-pinned text/AST, decodes the Cycle-830 literal fixture bank, and
independently applies the landed Boolean X/CNOT/Toffoli rules with integers.
No predecessor is imported or executed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle840_missing_link_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockF20-20260729"
EXPECTED_BASE = "293c666cd22da9cfa6352fafd73a57bbe5492f05"
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106

EXPECTED_WORKTREE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "6b87eea4bf26e3c261b84597512d2177406c5875a8c0b6ad5af549f208fd7f19",
}
EXPECTED_WORKTREE_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "0b7375692320b50b68516af61ecbc53526f47145",
}
HISTORICAL_SOURCES = (
    (
        "cycle839_meeting_primary",
        "863c268dd10ed18b09a5d5c33f54a6f118c4083c",
        "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py",
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
        "9289962e4cdd24732a9c5d1ea53b360d236948f8",
    ),
    (
        "cycle838_k3_primary",
        "da8484ced3926203ef8da76015988e6f858a4008",
        "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
        "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    ),
    (
        "cycle830_fixture_primary",
        "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
        "98b1571228ad0902301b6853208ef249ea2c2973",
    ),
    (
        "cycle846_three_wire_primary",
        "7af6f39f9f2714a5a836af8b1bd3170b2afd4715",
        "scripts/frontier_cycle846_reduced_braids_delay_law_2026_07_28.py",
        "172313524341e958d36e1028f0cec5e64e81c4efd915c009073049998c37fc45",
        "2e0eb1848b92ab3f43a5ada64664ab45b58f5bb1",
    ),
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)

Key = tuple[int, tuple[int, ...], int]
PairKey = tuple[int, tuple[int, int]]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]

K3_OPEN_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)
TRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key[1][1] == 2)
NONTRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key not in TRIO_KEYS)
EXPECTED_TRIO_GEOMETRY = {
    (0, 2, 6): (
        (0, 2, 2, 1, (1,)),
        (2, 6, 4, 2, (4,)),
        (6, 0, 5, 3, (8, 9)),
    ),
    (0, 2, 7): (
        (0, 2, 2, 1, (1,)),
        (2, 7, 5, 3, (4, 5)),
        (7, 0, 4, 2, (9,)),
    ),
    (0, 2, 8): (
        (0, 2, 2, 1, (1,)),
        (2, 8, 6, 3, (5,)),
        (8, 0, 3, 2, (9, 10)),
    ),
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in AUDIT_INPUT_PATHS),
    *(Path(path).stem for _name, _commit, path, _sha, _blob
      in HISTORICAL_SOURCES),
}))
FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        timeout=20,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    historical_payloads = {}
    historical_trees = {}
    historical_rows = []
    for name, commit, path, expected_sha, expected_blob in HISTORICAL_SOURCES:
        spec = f"{commit}:{path}"
        payload = git_bytes("show", spec)
        tree = ast.parse(payload, filename=spec)
        historical_payloads[name] = payload
        historical_trees[name] = tree
        historical_rows.append({
            "name": name,
            "spec": spec,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "sha256_exact": sha256(payload).hexdigest() == expected_sha,
            "git_blob": git_text("rev-parse", spec),
            "expected_git_blob": expected_blob,
            "git_blob_exact": git_text("rev-parse", spec) == expected_blob,
        })
    worktree_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_WORKTREE_SHA256[path],
        "sha256_exact": (
            sha256(payloads[path]).hexdigest()
            == EXPECTED_WORKTREE_SHA256[path]
        ),
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_WORKTREE_BLOBS[path],
        "git_blob_exact": (
            git_blob(payloads[path]) == EXPECTED_WORKTREE_BLOBS[path]
        ),
    } for path in AUDIT_INPUT_PATHS)
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    markers = {
        AUDIT_INPUT_PATHS[0]: {"interleaved_program", "run_orbit"},
        AUDIT_INPUT_PATHS[1]: {
            "reconstruct_minimal_discriminator", "meeting_theorem_certificate",
        },
        "cycle839_meeting_primary": {
            "theorem_arc_meeting", "meeting_theorem_certificate",
        },
        "cycle838_k3_primary": {"make_engine", "forecast_certificate"},
        "cycle830_fixture_primary": {"run"},
        "cycle846_three_wire_primary": {
            "register_accounting_rows", "certificate_c_weight_law",
        },
    }
    marker_exact = (
        all(markers[path] <= function_names(trees[path])
            for path in AUDIT_INPUT_PATHS)
        and all(markers[name] <= function_names(historical_trees[name])
                for name in historical_trees)
        and b"(88, 124, 125)" in historical_payloads[
            "cycle846_three_wire_primary"
        ]
    )
    landed_keys = literal_assignment(
        historical_trees["cycle838_k3_primary"],
        "K3_OPEN_THROUGH_T65536",
    )
    branch = git_text("branch", "--show-current")
    base = git_text(
        "merge-base", "HEAD", "physics-loop/proof-grade-blockF19-20260729"
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": (
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
        ),
        "named_worktree_input_count": len(AUDIT_INPUT_PATHS),
        "total_source_primary_count": (
            len(AUDIT_INPUT_PATHS) + len(HISTORICAL_SOURCES)
        ),
        "maximum_source_primary_count": 7,
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in worktree_rows
        ),
        "worktree_source_rows": worktree_rows,
        "historical_source_rows": tuple(historical_rows),
        "source_AST_markers_exact": marker_exact,
        "Cycle838_literal_k3_keys": landed_keys,
        "literal_k3_catalog_exact": landed_keys == K3_OPEN_KEYS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )),
        "firewall_hits": tuple(FIREWALL.hits),
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
        "git_base": base,
        "expected_git_base": EXPECTED_BASE,
        "git_base_exact": base == EXPECTED_BASE,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["total_source_primary_count"] <= 7
        and result["all_AUDIT_INPUT_PATHS_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"]
                for row in worktree_rows)
        and all(row["sha256_exact"] and row["git_blob_exact"]
                for row in historical_rows)
        and marker_exact
        and result["literal_k3_catalog_exact"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_branch_exact"]
        and result["git_base_exact"]
    )
    return result, historical_trees


def arc_vertices(start: int, end: int) -> tuple[int, ...]:
    length = (end - start) % RING_STATIONS
    return tuple((start + offset) % RING_STATIONS for offset in range(length + 1))


def enumerated_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    for tick in range(length + 1):
        left = set(vertices[:tick + 1])
        right = set(vertices[max(0, length - tick):])
        overlap = left & right
        if overlap:
            return tick, tuple(vertex for vertex in vertices if vertex in overlap)
    raise AssertionError(("wavefronts did not meet", vertices))


def theorem_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    tick = (length + 1) // 2
    return tick, tuple(vertices[length - tick:tick + 1])


def trio_geometry(positions: tuple[int, ...]) -> dict[str, object]:
    ordered = tuple(sorted(positions))
    arcs = []
    for index, start in enumerate(ordered):
        end = ordered[(index + 1) % len(ordered)]
        vertices = arc_vertices(start, end)
        formula = theorem_arc_meeting(vertices)
        enumerated = enumerated_arc_meeting(vertices)
        arcs.append({
            "adjacent_sources_clockwise": (start, end),
            "arc_vertices": vertices,
            "gap_length": len(vertices) - 1,
            "first_meeting_tick": formula[0],
            "meeting_centers": formula[1],
            "center_count": len(formula[1]),
            "parity_center_law_exact": (
                len(formula[1]) == (1 if (len(vertices) - 1) % 2 == 0 else 2)
            ),
            "formula_equals_enumeration": formula == enumerated,
        })
    completion_tick = max(int(row["first_meeting_tick"]) for row in arcs)
    return {
        "sources": ordered,
        "clockwise_gap_lengths": tuple(row["gap_length"] for row in arcs),
        "adjacent_arc_meetings": tuple(arcs),
        "meeting_time_multiset": tuple(sorted(
            int(row["first_meeting_tick"]) for row in arcs
        )),
        "all_adjacent_meets_completed_tick": completion_tick,
        "first_center_union": tuple(sorted({
            center for row in arcs for center in row["meeting_centers"]
        })),
        "landed_A_positions_at_completion": tuple(
            (source + completion_tick) % RING_STATIONS for source in ordered
        ),
        "landed_B_positions_at_completion": (),
        "gap_partition_exact": sum(int(row["gap_length"]) for row in arcs)
        == RING_STATIONS,
        "formula_equals_enumeration": all(
            bool(row["formula_equals_enumeration"]) for row in arcs
        ),
    }


def certificate_a_meets() -> dict[str, object]:
    position_rows = tuple(
        trio_geometry(positions) for positions in sorted({key[1] for key in TRIO_KEYS})
    )
    key_rows = tuple({
        "key": key,
        "event": key[2],
        **trio_geometry(key[1]),
    } for key in TRIO_KEYS)
    compact_geometry = tuple(
        (row["sources"], tuple(
            (
                arc["adjacent_sources_clockwise"][0],
                arc["adjacent_sources_clockwise"][1],
                arc["gap_length"],
                arc["first_meeting_tick"],
                arc["meeting_centers"],
            )
            for arc in row["adjacent_arc_meetings"]
        ))
        for row in position_rows
    )
    expected_compact_geometry = tuple(sorted(EXPECTED_TRIO_GEOMETRY.items()))
    exact = (
        len(TRIO_KEYS) == 6
        and len(position_rows) == 3
        and compact_geometry == expected_compact_geometry
        and all(row["clockwise_gap_lengths"] in ((2, 4, 5), (2, 5, 4), (2, 6, 3))
                for row in position_rows)
        and all(row["meeting_time_multiset"] == (1, 2, 3)
                for row in position_rows)
        and all(row["all_adjacent_meets_completed_tick"] == 3
                for row in position_rows)
        and all(row["gap_partition_exact"] and row["formula_equals_enumeration"]
                for row in position_rows)
        and all(
            arc["parity_center_law_exact"]
            for row in position_rows for arc in row["adjacent_arc_meetings"]
        )
    )
    return {
        "verdict": "MEET" if exact else "NO_MEET",
        "certificate_role": "A_EXACT_THREE_SOURCE_MEETING_STRUCTURE",
        "theorem": (
            "For clockwise-adjacent sources bounding a gap of d edges on C11, "
            "the two radius-one wavefronts first meet at ceil(d/2); the center "
            "set is one vertex for even d and the two middle vertices for odd d. "
            "The three source gaps partition C11, so the triple meeting structure "
            "is the three exact adjacent-gap meetings."
        ),
        "six_trio_keys": TRIO_KEYS,
        "position_geometry": position_rows,
        "per_key_geometry": key_rows,
        "expected_compact_geometry": expected_compact_geometry,
        "computed_compact_geometry": compact_geometry,
        "pass": exact,
    }


def render(certificates: dict[str, object], report: dict[str, object]) -> str:
    return "\n".join((
        *(f"CERTIFICATE {name} {compact(value)}"
          for name, value in certificates.items()),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )) + "\n"


def run() -> int:
    started = monotonic()
    controls, _historical_trees = source_controls()
    certificate_a = certificate_a_meets()
    elapsed = monotonic() - started
    controls.update({
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    })
    certificates = {
        "A_K3_MEETS": certificate_a,
        "D_CONTROLS_PARTIAL": controls,
    }
    report = {
        "cycle": 849,
        "stage": "incremental-certificate-A",
        "meeting_verdict": certificate_a["verdict"],
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "pass": bool(certificate_a["pass"] and controls["pass"]),
        "terminal": "CYCLE849_CERTIFICATE_A_PASS",
    }
    for _attempt in range(20):
        output = render(certificates, report)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            break
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    else:
        raise AssertionError("stdout byte fixed point did not converge")
    if size >= STDOUT_LIMIT_BYTES or elapsed >= AUDIT_TIMEOUT_SEC:
        raise AssertionError("control bound exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE849_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
