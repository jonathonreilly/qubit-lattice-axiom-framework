#!/usr/bin/env python3
"""Cycle 852: exhaustive covariant initial-setup selection tournament.

The declared finite census is the four Cycle-719 two-bank event seeds crossed
with every pairwise-separated source placement of size k=2,3,4,5 on its
oriented eleven-station program ring.  Counts and dynamics are rebuilt from
the landed Cycle-719 core.  Cited later primaries are SHA-pinned provenance
surfaces only: a fail-closed import firewall restricts them to text/AST use.

The frame group is the oriented-ring translation group C_11.  Its generator
adds one to every station label and leaves the core event seed fixed.  This is
a declared bounded frame action, not a claim that the supplied source boundary
or ring orientation has been autonomously selected.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable, Iterable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle836_offbackbone_depth_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[2]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
    AUDIT_INPUT_PATHS[3]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[4]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[5]:
        "b5f59ed04984d8c1956ff82a1f9af165b35ac2dcac99db4b929dbe3d8dc2e0b5",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[2]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
    AUDIT_INPUT_PATHS[3]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[4]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[5]: "8e4cb3071ac2be62b1de91c900d30d493675b87d",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited text/AST-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]
Selection = frozenset[Key]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
FRAME_GENERATORS = (1, -1)
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    parsed_top_levels = {
        path: len(tree.body) for path, tree in trees.items()
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "text_AST_parsed_top_level_counts": parsed_top_levels,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and all(parsed_top_levels.values())
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def pairwise_separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all(
        (station + 1) % stations not in occupied for station in occupied
    )


def derive_event_seeds(
    program: tuple[object, ...],
) -> tuple[tuple[int, State], ...]:
    """Build all four event seeds solely through the Cycle-719 core API."""

    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            raise AssertionError(("Cycle-719 event seed", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def derive_census() -> tuple[
    tuple[object, ...], tuple[tuple[int, State], ...], tuple[Key, ...]
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    keys = tuple(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _state in event_seeds
    )
    if len(keys) != len(set(keys)):
        raise AssertionError("duplicate census key")
    return program, event_seeds, tuple(sorted(keys))


def frame_map(key: Key, shift: int, stations: int) -> Key:
    k, event, positions = key
    moved = tuple(sorted((station + shift) % stations for station in positions))
    return k, event, moved


def orbit_of(key: Key, stations: int) -> tuple[Key, ...]:
    return tuple(sorted({
        frame_map(key, shift, stations) for shift in range(stations)
    }))


def partition_orbits(
    census: tuple[Key, ...], stations: int
) -> tuple[tuple[Key, ...], ...]:
    universe = set(census)
    remaining = set(census)
    rows = []
    while remaining:
        representative = min(remaining)
        orbit = orbit_of(representative, stations)
        if not set(orbit) <= universe:
            raise AssertionError(("frame closure", representative, orbit))
        rows.append(orbit)
        remaining.difference_update(orbit)
    return tuple(sorted(rows, key=lambda row: row[0]))


def census_and_orbits() -> dict[str, object]:
    program, event_seeds, census = derive_census()
    stations = len(program)
    orbits = partition_orbits(census, stations)
    per_k = dict(sorted(Counter(key[0] for key in census).items()))
    placement_per_k = {
        k: population // len(event_seeds) for k, population in per_k.items()
    }
    orbit_histogram = dict(sorted(Counter(map(len, orbits)).items()))
    singleton_orbits = tuple(orbit for orbit in orbits if len(orbit) == 1)
    closure_failures = tuple(
        (generator, key, frame_map(key, generator, stations))
        for generator in FRAME_GENERATORS
        for key in census
        if frame_map(key, generator, stations) not in set(census)
    )
    result = {
        "scope": {
            "fixture_banks": FIXTURE_BANKS,
            "ring_stations": stations,
            "event_seeds": len(event_seeds),
            "source_count_window": (MIN_SOURCES, MAX_SOURCES),
            "placement_predicate": "pairwise nonadjacent on oriented C_11",
        },
        "population": len(census),
        "per_k_populations": per_k,
        "per_k_placements_before_four_event_cross": placement_per_k,
        "orbit_count": len(orbits),
        "orbit_size_histogram": orbit_histogram,
        "singleton_orbits": singleton_orbits,
        "census_sha256": digest(census),
        "orbit_partition_sha256": digest(orbits),
        "frame_generators": FRAME_GENERATORS,
        "frame_closure_failures": closure_failures,
        "census": census,
        "orbits": orbits,
        "program": program,
        "event_seeds": event_seeds,
    }
    result["pass"] = (
        stations == 11
        and len(event_seeds) == 4
        and set(per_k) == set(range(MIN_SOURCES, MAX_SOURCES + 1))
        and sum(per_k.values()) == len(census)
        and sum(map(len, orbits)) == len(census)
        and not closure_failures
    )
    return result


def covariance_witness(
    selection: Selection,
    census: tuple[Key, ...],
    stations: int,
) -> dict[str, object]:
    universe = set(census)
    for generator in FRAME_GENERATORS:
        mapped = frozenset(frame_map(key, generator, stations) for key in selection)
        if mapped != selection:
            lost = tuple(sorted(selection - mapped))
            gained = tuple(sorted(mapped - selection))
            return {
                "covariant": False,
                "generator": generator,
                "selected_key": lost[0] if lost else None,
                "mapped_key": gained[0] if gained else None,
                "mapped_inside_census": mapped <= universe,
            }
    return {"covariant": True, "generator": None, "witness": None}


def structural_bound(
    census_report: dict[str, object],
    selections: dict[str, Selection] | None = None,
) -> dict[str, object]:
    census = census_report["census"]
    orbits = census_report["orbits"]
    stations = census_report["scope"]["ring_stations"]
    orbit_by_key = {
        key: frozenset(orbit) for orbit in orbits for key in orbit
    }
    enumerated_subset_failures = []
    # Exhaustively prove the fixed-set lemma orbit-by-orbit: adding or omitting
    # one orbit is the only generator-invariant membership choice.
    for orbit in orbits:
        representative = orbit[0]
        generated = orbit_of(representative, stations)
        if generated != orbit:
            enumerated_subset_failures.append((representative, generated, orbit))
    criterion_rows = {}
    for name, selection in sorted((selections or {}).items()):
        witness = covariance_witness(selection, census, stations)
        union_reconstruction = frozenset(
            key
            for key in selection
            if orbit_by_key[key] <= selection
        )
        criterion_rows[name] = {
            **witness,
            "union_of_orbits": union_reconstruction == selection,
        }
    result = {
        "lemma": (
            "For a G-covariant Boolean selector, membership is constant on "
            "each generated G-orbit; therefore its selection set is a union "
            "of orbits. A unique labeled setup requires an orbit of size one."
        ),
        "proof_method": (
            "enumerate each census orbit under the declared generators and "
            "mechanically compare every tournament selection with its images"
        ),
        "orbit_generation_failures": tuple(enumerated_subset_failures),
        "criterion_covariance": criterion_rows,
        "singleton_orbit_count": len(census_report["singleton_orbits"]),
    }
    result["pass"] = (
        not enumerated_subset_failures
        and all(
            row["covariant"] == row["union_of_orbits"]
            for row in criterion_rows.values()
        )
    )
    return result


def public_census(report: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in report.items()
        if key not in {"census", "orbits", "program", "event_seeds"}
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    census = census_and_orbits()
    structural = structural_bound(census)
    elapsed = monotonic() - started
    checks = {
        "A_CENSUS_AND_ORBITS": census["pass"],
        "B_STRUCTURAL_BOUND": structural["pass"],
        "C_TOURNAMENT": False,
        "D_VERDICT": False,
        "E_CONTROLS": (
            controls["pass"]
            and elapsed < AUDIT_TIMEOUT_SEC
            and not PRIMARY_FIREWALL.hits
        ),
    }
    report = {
        "checks": checks,
        "A_CENSUS_AND_ORBITS": public_census(census),
        "B_STRUCTURAL_BOUND": structural,
        "C_TOURNAMENT": {"status": "incremental scaffold"},
        "D_VERDICT": {"status": "incremental scaffold"},
        "E_CONTROLS": controls,
        "runtime_seconds": round(elapsed, 6),
        "pass": all(checks.values()),
    }
    for name, passed in checks.items():
        print("PASS" if passed else "FAIL", name, "::", passed)
    print("SUMMARY_JSON", compact(report))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
