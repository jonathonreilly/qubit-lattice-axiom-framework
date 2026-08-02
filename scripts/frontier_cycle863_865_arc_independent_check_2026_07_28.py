#!/usr/bin/env python3
"""Independent adversarial check of Cycles 863--865: time from records.

The three supervisor primaries are SHA/blob pinned and AST parsed, but are
BLOCKLISTED from import.  The 748-lane replay, clean predicates, event books,
record-age calculations, predictor tests, store-cap extension, and full-orbit
counterfactual are assembled here independently over the pinned Cycle-719
substrate.
"""
from __future__ import annotations

import ast
import atexit
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib
import importlib.abc
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle863_time_from_records_2026_07_28.py",
    "scripts/frontier_cycle864_laws_in_record_time_2026_07_28.py",
    "scripts/frontier_cycle865_offset_law_2026_07_28.py",
)
PRIMARY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in PRIMARY_PATHS)
TRANSITIVE_HEAD_FALLBACK_BLOBS = {
    "frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26":
        "8ec1b8d78585fdb090b5bf1e66050ab769cf14ca",
    "frontier_cycle719_recurrent_matter_history_controller_2026_07_26":
        "c4f75be1ba76a2a43bcb9b7fcc00ead5607af8ea",
    "frontier_cycle719_recurrent_physical_route_core_2026_07_26":
        "8e4684897bbc3a8b50610f9cb72e9b007e9c4368",
    "frontier_cycle719_source_local_finalizer_core_2026_07_26":
        "97cc3de7b95e341326c404047a321dbe2c825eda",
}
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP24-20260729"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "3c353b112f87aa41adde6380fcde147427f0d3f16130aadd97a8119f6dfa8e4c",
    AUDIT_INPUT_PATHS[3]:
        "1693de262d8eda5fc384575ce99be77b5418bf43af86c0ff52614110dea7346a",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5e24b16e80317e2e4012a81ba3b914a1deff3b8a",
    AUDIT_INPUT_PATHS[3]: "61c11a5a8aa310774f7008b44e631f06762b1ab7",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
HEAD_SNAPSHOT_ROOT = Path(tempfile.mkdtemp(prefix="cycle863_865_head_snapshot_"))
HEAD_SNAPSHOT_OID = subprocess.run(
    ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
    text=True, capture_output=True,
).stdout.strip()
archive = subprocess.Popen(
    ["git", "archive", "HEAD", "scripts"], cwd=ROOT,
    stdout=subprocess.PIPE,
)
assert archive.stdout is not None
extracted = subprocess.run(
    ["tar", "-x", "-C", str(HEAD_SNAPSHOT_ROOT)],
    stdin=archive.stdout, capture_output=True,
)
archive.stdout.close()
archive_status = archive.wait()
if archive_status or extracted.returncode:
    raise RuntimeError(("HEAD snapshot extraction failed", archive_status,
                        extracted.returncode, extracted.stderr.decode()))
sys.path.insert(1, str(HEAD_SNAPSHOT_ROOT / "scripts"))
atexit.register(shutil.rmtree, HEAD_SNAPSHOT_ROOT, True)


class _PrimaryBlocklist(importlib.abc.MetaPathFinder):
    """Fail closed before Python can execute any supervisor primary."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST primary import denied: {fullname}")
        return None


PRIMARY_BLOCKLIST = _PrimaryBlocklist()
sys.meta_path.insert(0, PRIMARY_BLOCKLIST)


class _PinnedHeadFallback(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Load only missing tracked Cycle-719 dependencies from exact HEAD blobs."""

    def __init__(self) -> None:
        self.payloads: dict[str, bytes] = {}
        self.loaded: list[str] = []
        self.resolved_blobs: dict[str, str] = {}

    def find_spec(self, fullname, path=None, target=None):
        module = fullname.rsplit(".", 1)[-1]
        if ((ROOT / "scripts" / f"{module}.py").is_file()
                or (HEAD_SNAPSHOT_ROOT / "scripts" / f"{module}.py").is_file()):
            return None
        resolved = subprocess.run(
            ["git", "rev-parse", "--verify", f"HEAD:scripts/{module}.py"],
            cwd=ROOT, text=True, capture_output=True,
        )
        if resolved.returncode:
            return None
        blob = resolved.stdout.strip()
        payload = subprocess.run(
            ["git", "cat-file", "blob", blob], cwd=ROOT, check=True,
            capture_output=True,
        ).stdout
        computed = sha1(
            f"blob {len(payload)}\0".encode("ascii") + payload
        ).hexdigest()
        if computed != blob:
            raise ImportError(("fallback blob mismatch", module, blob))
        self.payloads[fullname] = payload
        self.resolved_blobs[module] = blob
        return importlib.util.spec_from_loader(fullname, self, origin=f"git-blob:{blob}")

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        payload = self.payloads.pop(module.__name__)
        module.__file__ = module.__spec__.origin
        exec(compile(payload, module.__file__, "exec"), module.__dict__)
        self.loaded.append(module.__name__)


PINNED_HEAD_FALLBACK = _PinnedHeadFallback()
sys.meta_path.insert(1, PINNED_HEAD_FALLBACK)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]

BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
HORIZON = 51_115
GLOBAL_STORE_CAP = 4096
BANK_STORE_CAP = 512
PERIOD_SAMPLE = 48
PERIOD_MIN_EVENTS = 64
PERIOD_EXTENSION_SAMPLE = 8
SATURATION_BOUNDARY_CAP = 1_100
SATURATION_LANE_CAP = 64


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    for path, payload in payloads.items():
        ast.parse(payload, filename=path)

    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"), filename=__file__)
    literal = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)

    firewall_results = {}
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.import_module(module)
        except ImportError as exc:
            firewall_results[module] = str(exc)
        else:
            firewall_results[module] = "UNEXPECTED_IMPORT_SUCCESS"

    sha_rows = {path: sha256(data).hexdigest() for path, data in payloads.items()}
    blob_rows = {path: git_blob(data) for path, data in payloads.items()}
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=ROOT, check=True,
        text=True, capture_output=True,
    ).stdout.strip()
    blocked_loaded = tuple(
        module for module in BLOCKLISTED_MODULES if module in sys.modules
    )
    blocked_hits = tuple(PRIMARY_BLOCKLIST.hits)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "branch": branch,
        "blocked_modules_loaded": blocked_loaded,
        "blocklist_hits": blocked_hits,
        "blocklist_results": firewall_results,
        "transitive_head_fallback_blobs": TRANSITIVE_HEAD_FALLBACK_BLOBS,
        "transitive_head_fallback_resolved": PINNED_HEAD_FALLBACK.resolved_blobs,
        "transitive_head_fallback_loaded": tuple(PINNED_HEAD_FALLBACK.loaded),
        "transitive_head_snapshot_oid": HEAD_SNAPSHOT_OID,
    }
    result["pass"] = bool(
        result["literal_ok"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and branch == EXPECTED_BRANCH
        and not blocked_loaded
        and blocked_hits == BLOCKLISTED_MODULES
        and all("BLOCKLIST primary import denied" in v
                for v in firewall_results.values())
        and all(len(blob) == 40 for blob in PINNED_HEAD_FALLBACK.resolved_blobs.values())
        and len(HEAD_SNAPSHOT_OID) == 40
    )
    return result


def separated_on_ring(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all((position + 1) % stations not in occupied for position in occupied)


def event_seed_states(program) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(BANKS)
    rows = []
    for event_index in range(2 * BANKS):
        direction = (1, 0) if event_index % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(prepared, program)
        expected_rail = (1,) + (0,) * (len(program) - 1)
        if after != K.A.apply_semantic(prepared, allocator):
            raise AssertionError(("seed allocator", event_index))
        if rail_a != expected_rail or any(rail_b) or len(trace) != len(program):
            raise AssertionError(("seed rails", event_index))
        rows.append((event_index, prepared))
        state = after
    return tuple(rows)


def independent_census():
    program = K.interleaved_program(BANKS)
    stations = len(program)
    seeds = event_seed_states(program)
    keys = []
    for source_count in range(MIN_SOURCES, MAX_SOURCES + 1):
        for positions in combinations(range(stations), source_count):
            if not separated_on_ring(positions, stations):
                continue
            for event_index, _state in seeds:
                keys.append((source_count, event_index, positions))
    return program, seeds, tuple(sorted(keys))


def watched_bank_wires() -> tuple[int, ...]:
    return (
        K.A.POINTER, K.A.U_TO_V, K.A.V_TO_U, K.A.DIRECTION_OK,
        *K.A.FRESH, *K.A.ZERO_WORK, K.A.TOKEN_OK,
    )


def assemble_clean_predicates():
    """Independently discover packed coordinates for bank/global dirtiness."""

    banks0, links0 = K.B.chain_genesis(BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)

    bank_coordinates: list[set[int]] = [set() for _ in zero_banks]
    for bank_index in range(len(zero_banks)):
        for wire in watched_bank_wires():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(tuple(tuple(bank) for bank in changed), zero_links)
            delta = [i for i, pair in enumerate(zip(baseline, marked))
                     if pair[0] != pair[1]]
            if len(delta) != 1:
                raise AssertionError(("bank coordinate", bank_index, wire, delta))
            bank_coordinates[bank_index].add(delta[0])

    link_coordinates: set[int] = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(tuple(row) for row in changed))
            delta = [i for i, pair in enumerate(zip(baseline, marked))
                     if pair[0] != pair[1]]
            if len(delta) != 1:
                raise AssertionError(("link coordinate", link_index, wire, delta))
            link_coordinates.add(delta[0])

    banks = tuple(tuple(sorted(row)) for row in bank_coordinates)
    global_coordinates = tuple(sorted(
        set(banks[0]) | set(banks[1]) | link_coordinates
        | {K.R3.X.SOURCE_POINTER}
    ))
    return {
        "bank": banks,
        "links": tuple(sorted(link_coordinates)),
        "source_pointer": K.R3.X.SOURCE_POINTER,
        "global": global_coordinates,
    }


def synchronous_chunks(program, positions0: tuple[int, ...]):
    positions = tuple(positions0)
    word = []
    for _ in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple((position + 1) % len(program) for position in positions)
    # Reproduce 863-A's declared equal-slice partition exactly.  This is not
    # reused by the independent bit-sliced replay, whose chunks are assembled
    # station-by-station above.
    per_chunk = len(word) // len(program)
    return tuple(
        tuple(word[start * per_chunk:(start + 1) * per_chunk])
        for start in range(len(program))
    )


def true_synchronous_chunks(program, positions0: tuple[int, ...]):
    """Complete station-by-station chunks, retaining every mapped gate."""

    positions = tuple(positions0)
    chunks = []
    for _ in range(len(program)):
        live = set(positions)
        chunk = []
        for station, row in enumerate(program):
            if station in live:
                chunk.extend(K.mapped_macro(row))
        chunks.append(tuple(chunk))
        positions = tuple((position + 1) % len(program) for position in positions)
    return tuple(chunks)


def initial_states(program, seeds, census):
    seed_map = dict(seeds)
    states = []
    failures = 0
    for _count, event_index, positions in census:
        after, rail_a, rail_b, _trace = K.run_orbit(
            seed_map[event_index], program, token_positions=positions
        )
        expected = tuple(int(station in positions) for station in range(len(program)))
        failures += int(rail_a != expected or any(rail_b))
        states.append(after)
    return tuple(states), failures


def transpose_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compiled_schedules(program, census):
    schedules = []
    stations = len(program)
    for step in range(stations):
        encoded = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane for lane, (_count, _event, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if not mask:
                continue
            for gate in K.mapped_macro(row):
                if gate.kind == "X":
                    encoded.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    encoded.append((1, gate.wires[0], gate.wires[1], 0, mask))
                elif gate.kind == "TOF":
                    encoded.append((2, gate.wires[0], gate.wires[1],
                                    gate.wires[2], mask))
                else:
                    raise AssertionError(("unknown gate", gate))
        source = ["def advance(columns):"]
        for kind, a, b, c, mask in encoded:
            if kind == 0:
                source.append(f" columns[{a}] ^= {mask}")
            elif kind == 1:
                source.append(f" columns[{b}] ^= columns[{a}] & {mask}")
            else:
                source.append(
                    f" columns[{c}] ^= columns[{a}] & columns[{b}] & {mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        schedules.append(namespace["advance"])
    return tuple(schedules)


def clean_mask(columns: list[int], coordinates: tuple[int, ...], universe: int) -> int:
    dirty = 0
    for coordinate in coordinates:
        dirty |= columns[coordinate]
    return universe & ~dirty


def set_bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def append_masked(stores, mask: int, boundary: int, cap: int) -> None:
    for lane in set_bits(mask):
        if len(stores[lane]) < cap:
            stores[lane].append(boundary)


def independent_replay(program, seeds, census, predicates):
    """Exact bit-sliced replay with independently assembled event books."""

    started = monotonic()
    states, init_failures = initial_states(program, seeds, census)
    lane_count = len(census)
    duplicate_lane = lane_count
    simulated_census = census + (census[0],)
    columns = transpose_states(states + (states[0],))
    schedules = compiled_schedules(program, simulated_census)
    universe_all = (1 << (lane_count + 1)) - 1
    universe_primary = (1 << lane_count) - 1
    duplicate_bit = 1 << duplicate_lane
    stations = len(program)

    stores = {
        "global": [[] for _ in census],
        "bank0": [[] for _ in census],
        "bank1": [[] for _ in census],
        "sync": [[] for _ in census],
    }
    totals = Counter()
    sync_on_tick = 0
    e1_boundary: dict[Key, int] = {}
    e2_orbit: dict[Key, int] = {}
    duplicate_mismatches = 0
    bank_event_counts = ([0] * lane_count, [0] * lane_count)
    global_bank_rungs = [[] for _ in census]

    def observe(boundary: int):
        nonlocal duplicate_mismatches, sync_on_tick
        global_all = clean_mask(columns, predicates["global"], universe_all)
        bank0_all = clean_mask(columns, predicates["bank"][0], universe_all)
        bank1_all = clean_mask(columns, predicates["bank"][1], universe_all)
        duplicate_mismatches += int(bool(global_all & 1) != bool(global_all & duplicate_bit))
        duplicate_mismatches += int(bool(bank0_all & 1) != bool(bank0_all & duplicate_bit))
        duplicate_mismatches += int(bool(bank1_all & 1) != bool(bank1_all & duplicate_bit))
        masks = {
            "global": global_all & universe_primary,
            "bank0": bank0_all & universe_primary,
            "bank1": bank1_all & universe_primary,
            "sync": bank0_all & bank1_all & universe_primary,
        }
        for bank_index, kind in enumerate(("bank0", "bank1")):
            for lane in set_bits(masks[kind]):
                bank_event_counts[bank_index][lane] += 1
        for kind, mask in masks.items():
            totals[kind] += mask.bit_count()
            append_masked(
                stores[kind], mask, boundary,
                GLOBAL_STORE_CAP if kind in {"global", "sync"} else BANK_STORE_CAP,
            )
        if boundary % stations == 0:
            sync_on_tick += masks["sync"].bit_count()
        for lane in set_bits(masks["global"]):
            e1_boundary.setdefault(census[lane], boundary)
            if len(global_bank_rungs[lane]) < 129:
                global_bank_rungs[lane].append((
                    bank_event_counts[0][lane], bank_event_counts[1][lane]
                ))
        return masks["global"]

    last_global = observe(0)
    for lane in set_bits(last_global):
        e2_orbit.setdefault(census[lane], 0)

    for orbit in range(1, HORIZON + 1):
        for step, advance in enumerate(schedules, 1):
            advance(columns)
            boundary = (orbit - 1) * stations + step
            last_global = observe(boundary)
        for lane in set_bits(last_global):
            e2_orbit.setdefault(census[lane], orbit)

    return {
        "stations": stations,
        "stores": stores,
        "totals": dict(totals),
        "sync_on_tick": sync_on_tick,
        "e1_boundary": e1_boundary,
        "e2_orbit": e2_orbit,
        "bank_event_counts": bank_event_counts,
        "global_bank_rungs": global_bank_rungs,
        "init_failures": init_failures,
        "duplicate_mismatches": duplicate_mismatches,
        "final_columns_digest": digest(columns),
        "runtime_seconds": round(monotonic() - started, 3),
    }


def eventual_period(sequence: tuple[int, ...]) -> int | None:
    """Match the primary's finite-tail test, including its censoring semantics."""

    tail = sequence[len(sequence) // 2:]
    for period in range(1, len(tail) // 2 + 1):
        if all(tail[i] == tail[i + period]
               for i in range(len(tail) - period)):
            return period
    return None


def extend_global_event_stores(program, seeds, keys, predicates):
    """Second, narrow replay: retain every global event for exactly eight keys."""

    states, failures = initial_states(program, seeds, keys)
    if failures:
        raise AssertionError(("extension initialization", failures))
    columns = transpose_states(states)
    schedules = compiled_schedules(program, keys)
    universe = (1 << len(keys)) - 1
    stores = [[] for _ in keys]

    def observe(boundary: int):
        mask = clean_mask(columns, predicates["global"], universe)
        for lane in set_bits(mask):
            stores[lane].append(boundary)

    observe(0)
    for _orbit in range(1, HORIZON + 1):
        for step, advance in enumerate(schedules, 1):
            advance(columns)
            boundary = (_orbit - 1) * len(program) + step
            observe(boundary)
    return {key: tuple(stores[lane]) for lane, key in enumerate(keys)}


def substrate_certificate(rep, census) -> dict[str, object]:
    stations = rep["stations"]
    e1 = rep["e1_boundary"]
    e2 = rep["e2_orbit"]
    first_sync_matches = 0
    e2_with_sync = 0
    extra_sync_keys = 0
    for lane, key in enumerate(census):
        syncs = rep["stores"]["sync"][lane]
        if key in e2 and syncs:
            e2_with_sync += 1
            first_sync_matches += int(
                syncs[0] == e2[key] * stations
                or (syncs[0] == 0 and e2[key] == 0)
            )
        elif key not in e2 and syncs:
            extra_sync_keys += 1

    intrinsic_e1 = sum(
        1 for lane, key in enumerate(census)
        if key in e1 and rep["stores"]["global"][lane]
        and rep["stores"]["global"][lane][0] == e1[key]
    )
    stored_syncs = [boundary for lane in rep["stores"]["sync"] for boundary in lane]
    sync_total = len(stored_syncs)
    sync_on = sum(boundary % stations == 0 for boundary in stored_syncs)
    sync_fraction = sync_on / sync_total
    result = {
        "certificate": "THE_SUBSTRATE_REPLAY",
        "census_keys": len(census),
        "horizon_orbits": HORIZON,
        "stations": stations,
        "landed_E1": len(e1),
        "landed_E2": len(e2),
        "uncapped_event_totals": rep["totals"],
        "sync_events_total_4096_capped": sync_total,
        "sync_on_tick": sync_on,
        "sync_off_tick": sync_total - sync_on,
        "sync_on_tick_fraction": round(sync_fraction, 9),
        "sync_on_tick_percent": round(100 * sync_fraction, 2),
        "first_sync_equals_landed_E2": f"{first_sync_matches}/{e2_with_sync}",
        "first_sync_extra_keys": extra_sync_keys,
        "intrinsic_E1_identity": f"{intrinsic_e1}/{len(e1)}",
        "init_failures": rep["init_failures"],
        "deterministic_duplicate_mismatches": rep["duplicate_mismatches"],
        "final_columns_digest": rep["final_columns_digest"],
        "finding": (
            "Independent replay confirms E1 as first formation event, but"
            " first two-bank synchronization neither defines the landed E2"
            " census nor concentrates on the supplied orbit tick."
        ),
    }
    result["pass"] = bool(
        len(census) == 748
        and len(e1) == 182
        and len(e2) == 114
        and sync_total == 559_606
        and round(100 * sync_fraction, 2) == 14.16
        and first_sync_matches == 25
        and e2_with_sync == 114
        and extra_sync_keys == 624
        and intrinsic_e1 == 182
        and rep["init_failures"] == 0
        and rep["duplicate_mismatches"] == 0
    )
    return result


def record_age_and_periodicity(program, seeds, census, predicates, rep):
    stations = rep["stations"]
    e2 = rep["e2_orbit"]
    stamp_rung: dict[Key, int] = {}
    censored = 0
    for lane, key in enumerate(census):
        if key not in e2:
            continue
        boundary = e2[key] * stations
        events = rep["stores"]["global"][lane]
        index = bisect_left(events, boundary)
        if index < len(events) and events[index] == boundary:
            stamp_rung[key] = index + 1
        else:
            censored += 1

    cohorts = defaultdict(list)
    for key, rung in stamp_rung.items():
        cohorts[e2[key]].append(rung)
    spread_histogram = Counter(
        max(rungs) - min(rungs) for rungs in cohorts.values()
    )
    multi_member = sum(len(rungs) > 1 for rungs in cohorts.values())

    sampled_keys = []
    period_rows = Counter()
    aperiodic_keys = []
    for lane, key in enumerate(census):
        events = rep["stores"]["global"][lane]
        if len(events) < PERIOD_MIN_EVENTS:
            continue
        sampled_keys.append(key)
        gaps = tuple(right - left for left, right in zip(events, events[1:]))
        period = eventual_period(gaps)
        if period is None:
            aperiodic_keys.append(key)
        else:
            tail_start = len(gaps) // 2
            period_rows[(period, sum(gaps[tail_start:tail_start + period]))] += 1
        if len(sampled_keys) == PERIOD_SAMPLE:
            break

    extension_keys = tuple(aperiodic_keys[:PERIOD_EXTENSION_SAMPLE])
    extended = extend_global_event_stores(program, seeds, extension_keys, predicates)
    extension_rows = []
    artifacts = 0
    for key in extension_keys:
        base = tuple(rep["stores"]["global"][census.index(key)])
        full = extended[key]
        base_period = eventual_period(tuple(b - a for a, b in zip(base, base[1:])))
        full_period = eventual_period(tuple(b - a for a, b in zip(full, full[1:])))
        artifact = bool(len(full) > len(base) and base_period is None
                        and full_period is not None)
        artifacts += int(artifact)
        extension_rows.append({
            "key": key,
            "capped_events": len(base),
            "extended_events": len(full),
            "capped_period": base_period,
            "extended_period": full_period,
            "store_cap_artifact": artifact,
        })

    never_clean = sum(not events for events in rep["stores"]["global"])
    result = {
        "certificate": "THE_864_NUMBERS",
        "stamped_with_rung": len(stamp_rung),
        "rung_censored": censored,
        "scheduler_cohorts_total": len(cohorts),
        "multi_member_cohorts": multi_member,
        "within_cohort_spread_histogram": dict(sorted(spread_histogram.items())),
        "periodicity_sample": len(sampled_keys),
        "eventually_periodic": sum(period_rows.values()),
        "aperiodic_within_4096_store": len(aperiodic_keys),
        "period_rows": [
            {"event_period": period, "scheduler_span": span, "keys": count}
            for (period, span), count in period_rows.most_common()
        ],
        "extension_sample_size": len(extension_keys),
        "store_cap_artifacts_in_extension_sample": artifacts,
        "extension_rows": extension_rows,
        "never_clean_worlds": never_clean,
        "b_axis_discharge_condition": (
            "The evolution axis must be constituted by record order: the"
            " temporal laws must restate in record time and there must be no"
            " second record-clock; only the first leg is numerically probed."
        ),
        "finding": (
            f"The 864 census is reproduced; extending {len(extension_keys)}"
            f" of the 40 capped-aperiodic keys identifies {artifacts} as"
            " finite-store artifacts under the primary's own tail-period test."
        ),
        "stamp_rung": stamp_rung,
        "cohorts": cohorts,
    }
    expected_spreads = {0: 30, 1: 4, 2: 4, 4: 5, 5: 1}
    result["pass"] = bool(
        len(stamp_rung) == 114
        and censored == 0
        and len(cohorts) == 44
        and multi_member == 15
        and dict(sorted(spread_histogram.items())) == expected_spreads
        and len(sampled_keys) == 48
        and sum(period_rows.values()) == 8
        and len(aperiodic_keys) == 40
        and len(extension_keys) == 8
        and never_clean == 566
    )
    return result


def ring_separations(positions: tuple[int, ...], stations: int):
    return tuple(sorted(
        min((right - left) % stations, (left - right) % stations)
        for i, left in enumerate(positions) for right in positions[i + 1:]
    ))


def evaluate_predictor(rows, name: str, values) -> dict[str, object]:
    groups = defaultdict(list)
    for row in rows:
        groups[compact(values(row))].append(row)
    violating_groups = []
    witness = None
    collision_instances = 0
    agreeing_collision_instances = 0
    violation_instances = 0
    for value, members in groups.items():
        collision_instances += len(members) - 1
        offsets = {member["offset"] for member in members}
        if len(offsets) == 1:
            agreeing_collision_instances += len(members) - 1
            continue
        violation_instances += len(members) - 1
        violating_groups.append(value)
        if witness is None:
            first = members[0]
            second = next(member for member in members
                          if member["offset"] != first["offset"])
            witness = {
                "predictor_value": value,
                "offsets": [first["offset"], second["offset"]],
                "keys": [first["key"], second["key"]],
            }
    return {
        "predictor": name,
        "functional": not violating_groups,
        "distinct_values": len(groups),
        "collision_instances": collision_instances,
        "agreeing_collision_instances": agreeing_collision_instances,
        "violation_instances": violation_instances,
        "violating_groups": len(violating_groups),
        "witness": witness,
    }


def offset_rows(census, rep, ages):
    e2 = rep["e2_orbit"]
    stamp_rung = ages["stamp_rung"]
    cohorts = defaultdict(list)
    for key, rung in stamp_rung.items():
        cohorts[e2[key]].append((key, rung))
    lane_for_key = {key: lane for lane, key in enumerate(census)}
    rows = []
    for moment, members in sorted(cohorts.items()):
        if len(members) < 2:
            continue
        base = min(rung for _key, rung in members)
        for key, rung in members:
            source_count, event_index, positions = key
            lane = lane_for_key[key]
            separations = ring_separations(positions, rep["stations"])
            rows.append({
                "moment": moment,
                "key": key,
                "lane": lane,
                "offset": rung - base,
                "rung": rung,
                "predictors": {
                    "event": event_index,
                    "k": source_count,
                    "min_sep": separations[0],
                    "sep_profile": separations,
                    "pos_sum_mod11": sum(positions) % rep["stations"],
                    "min_pos": min(positions),
                    "e1_moment": rep["e1_boundary"][key],
                    "pre_stamp_events": rung - 1,
                },
            })
    return rows


def law_and_vacuity_certificate(census, rep, ages):
    rows = offset_rows(census, rep, ages)
    predictor_names = sorted(rows[0]["predictors"])
    tournament = {
        name: evaluate_predictor(
            rows, name, lambda row, n=name: row["predictors"][n]
        ) for name in predictor_names
    }
    e1 = tournament["e1_moment"]
    rivals = {name: result for name, result in tournament.items()
              if name != "e1_moment"}
    offset_histogram = dict(sorted(Counter(row["offset"] for row in rows).items()))
    result = {
        "certificate": "THE_865_LAW_AND_VACUITY",
        "multi_member_cohorts": len({row["moment"] for row in rows}),
        "member_rows": len(rows),
        "offset_histogram": offset_histogram,
        "tournament": tournament,
        "e1_nonvacuity_arithmetic": {
            "distinct_values": e1["distinct_values"],
            "rows": len(rows),
            "nontrivial_agreement_instances": (
                len(rows) - e1["distinct_values"]
            ),
            "all_collision_instances_checked": e1["collision_instances"],
            "zero_violations": e1["violation_instances"] == 0,
        },
        "rival_witnesses": {name: row["witness"] for name, row in rivals.items()},
        "finding": (
            "The scheduler-valued e1_moment predictor is exactly functional"
            " on all 35 repeated-value collision instances; every one of the"
            " seven declared rivals has an explicit conflicting-offset witness."
        ),
        "rows": rows,
    }
    result["pass"] = bool(
        len({row["moment"] for row in rows}) == 15
        and len(rows) == 85
        and offset_histogram == {0: 41, 1: 15, 2: 13, 3: 9, 4: 6, 5: 1}
        and e1["functional"]
        and e1["distinct_values"] == 50
        and e1["collision_instances"] == 35
        and e1["agreeing_collision_instances"] == 35
        and e1["violation_instances"] == 0
        and len(rivals) == 7
        and all(not row["functional"] and row["witness"] is not None
                for row in rivals.values())
    )
    return result


def ordinal_record_features(row, rep):
    """Features made only from event order, event rung, and coincidence."""

    lane = row["lane"]
    global_events = rep["stores"]["global"][lane]
    bank0 = rep["stores"]["bank0"][lane]
    bank1 = rep["stores"]["bank1"][lane]
    bank_rungs = rep["global_bank_rungs"][lane]
    bank0_set = set(bank0)
    bank1_set = set(bank1)
    global_set = set(global_events)
    merged = sorted(bank0_set | bank1_set)

    order_tokens = tuple(
        "S" if boundary in bank0_set and boundary in bank1_set
        else "0" if boundary in bank0_set else "1"
        for boundary in merged[:128]
    )
    sync_bits = tuple(int(token == "S") for token in order_tokens)
    scheduler_gap8 = tuple(
        right - left for left, right in zip(global_events[:8], global_events[1:9])
    )
    event_index_gap8 = tuple(
        (right[0] - left[0], right[1] - left[1])
        for left, right in zip(bank_rungs[:8], bank_rungs[1:9])
    )
    result = {
        "scheduler_gap_signature_8": scheduler_gap8,
        "event_index_gap_signature_8": event_index_gap8,
        "per_bank_first_event_order_pattern": order_tokens[:16],
        "ladder_rate_class": (
            sum(boundary in global_set for boundary in merged[:64]),
            sum(token == "S" for token in order_tokens[:64]),
            min(64, len(merged)),
        ),
        "sync_event_pattern_prefix": sync_bits[:32],
        "formation_bank_rungs": bank_rungs[0] if bank_rungs else (),
        "formation_plus_event_index_gap8": (
            bank_rungs[0] if bank_rungs else (), event_index_gap8
        ),
    }
    for prefix in (4, 8, 16, 32, 64, 128):
        result[f"bank_order_prefix_{prefix}"] = order_tokens[:prefix]
        result[f"sync_prefix_{prefix}"] = sync_bits[:prefix]
        result[f"ordinal_ladder_rate_{prefix}"] = (
            sum(boundary in global_set for boundary in merged[:prefix]),
            sum(token == "S" for token in order_tokens[:prefix]),
            min(prefix, len(merged)),
        )
    for prefix in (1, 2, 4, 8):
        result[f"global_bank_rung_prefix_{prefix}"] = tuple(bank_rungs[:prefix])
    return result


def intrinsic_predictor_hunt(rep, law):
    rows = law["rows"]
    for row in rows:
        row["record_features"] = ordinal_record_features(row, rep)

    minimum_names = (
        "scheduler_gap_signature_8",
        "event_index_gap_signature_8",
        "per_bank_first_event_order_pattern",
        "ladder_rate_class",
        "sync_event_pattern_prefix",
    )
    all_names = sorted(rows[0]["record_features"])
    evaluations = {
        name: evaluate_predictor(
            rows, name, lambda row, n=name: row["record_features"][n]
        ) for name in all_names
    }

    intrinsic_names = [
        name for name in all_names if name != "scheduler_gap_signature_8"
    ]
    nonvacuous_singles = [
        result for name, result in evaluations.items()
        if name in intrinsic_names and result["functional"]
        and result["collision_instances"] > 0
    ]
    nonvacuous_singles.sort(
        key=lambda result: (-result["collision_instances"],
                            result["distinct_values"], result["predictor"])
    )

    pair_evaluations = []
    if not nonvacuous_singles:
        pair_pool = [
            "event_index_gap_signature_8",
            "per_bank_first_event_order_pattern",
            "ladder_rate_class",
            "sync_event_pattern_prefix",
            "formation_bank_rungs",
            "global_bank_rung_prefix_2",
            "bank_order_prefix_32",
            "ordinal_ladder_rate_64",
        ]
        for left, right in combinations(pair_pool, 2):
            evaluated = evaluate_predictor(
                rows, f"{left}+{right}",
                lambda row, a=left, b=right: (
                    row["record_features"][a], row["record_features"][b]
                ),
            )
            if evaluated["functional"] and evaluated["collision_instances"] > 0:
                pair_evaluations.append(evaluated)
        pair_evaluations.sort(
            key=lambda result: (-result["collision_instances"],
                                result["distinct_values"], result["predictor"])
        )

    found = nonvacuous_singles[:1] or pair_evaluations[:1]
    scheduler_result = evaluations["scheduler_gap_signature_8"]
    if found:
        verdict = "BIRTH_DATUM_GAUGE_RESIDUE_CLOSED_RECORD_NATIVE"
        finding = (
            f"A non-vacuous record-native predictor, {found[0]['predictor']},"
            f" exactly determines all offsets with {found[0]['collision_instances']}"
            " repeated-value agreement instances and zero violations; this"
            " supplies the missing constructive reversal of the scheduler-valued"
            " e1_moment law at the declared census."
        )
    else:
        verdict = "INTRINSIC_HUNT_EXHAUSTED_AT_DECLARED_FAMILY"
        finding = (
            "No tested non-vacuous ordinal record-native predictor determines"
            " every offset. Any functional unique-key signature was rejected as"
            " vacuous; the scheduler-measured gap result is reported separately"
            " and cannot close the birth-datum gauge residue."
        )
    result = {
        "certificate": "THE_INTRINSIC_PREDICTOR_HUNT",
        "minimum_candidates": {
            name: evaluations[name] for name in minimum_names
        },
        "expanded_candidate_count": len(evaluations),
        "expanded_candidates": evaluations,
        "pair_candidates_tested_if_needed": 0 if nonvacuous_singles else 28,
        "nonvacuous_intrinsic_singles": nonvacuous_singles,
        "nonvacuous_intrinsic_pairs": pair_evaluations,
        "selected_predictor": found[0] if found else None,
        "scheduler_gap_signature_result": scheduler_result,
        "scheduler_gap_is_record_native": False,
        "verdict": verdict,
        "finding": finding,
    }
    result["pass"] = bool(
        all(name in evaluations for name in minimum_names)
        and scheduler_result["predictor"] == "scheduler_gap_signature_8"
        and all(evaluations[name]["witness"] is not None
                or evaluations[name]["functional"]
                for name in all_names)
    )
    return result


def availability_after(state: State, settle_word, bank_coordinates):
    available = 0
    errors = 0
    for direction in ((1, 0), (0, 1)):
        try:
            prepared = K.M.prepare_endpoint(state, direction)
            after = K.A.apply_semantic(prepared, settle_word)
        except Exception:
            errors += 1
            continue
        flags_zero = all(
            after[coordinate] == 0
            for bank in bank_coordinates for coordinate in bank
        )
        available += int(flags_zero)
    return available, errors


def a_probe_critique(program, seeds, census, predicates, rep):
    candidates = sorted(
        (rep["stores"]["global"][lane][0], lane)
        for lane, key in enumerate(census)
        if key in rep["e1_boundary"] and rep["stores"]["global"][lane]
        and 0 < rep["stores"]["global"][lane][0] <= SATURATION_BOUNDARY_CAP
    )[:SATURATION_LANE_CAP]
    seed_map = dict(seeds)
    chunk_cache = {}
    one_chunk = {"formation": Counter(), "control": Counter()}
    full_orbit = {"formation": Counter(), "control": Counter()}
    dropped_gate_histogram = Counter()
    errors = 0

    def orbit_word(chunks, start):
        word = []
        for delta in range(len(chunks)):
            word.extend(chunks[(start + delta) % len(chunks)])
        return tuple(word)

    for first, lane in candidates:
        key = census[lane]
        _count, event_index, positions = key
        primary_chunks, complete_chunks = chunk_cache.setdefault(
            positions, (
                synchronous_chunks(program, positions),
                true_synchronous_chunks(program, positions),
            )
        )
        dropped_gate_histogram[
            sum(map(len, complete_chunks)) - sum(map(len, primary_chunks))
        ] += 1
        state, _rail_a, _rail_b, _trace = K.run_orbit(
            seed_map[event_index], program, token_positions=positions
        )
        control_state = None
        for boundary in range(first):
            if boundary == first - 1:
                control_state = state
            state = K.A.apply_semantic(
                state, primary_chunks[boundary % len(primary_chunks)]
            )
        if control_state is None:
            raise AssertionError(("missing control", first, key))

        for label, probe_state, start in (
            ("formation", state, first),
            ("control", control_state, first - 1),
        ):
            one_value, one_errors = availability_after(
                probe_state,
                primary_chunks[start % len(primary_chunks)],
                predicates["bank"],
            )
            orbit_value, orbit_errors = availability_after(
                probe_state, orbit_word(complete_chunks, start), predicates["bank"]
            )
            one_chunk[label][one_value] += 1
            full_orbit[label][orbit_value] += 1
            errors += one_errors + orbit_errors

    one_hist = {label: dict(sorted(hist.items()))
                for label, hist in one_chunk.items()}
    orbit_hist = {label: dict(sorted(hist.items()))
                  for label, hist in full_orbit.items()}
    discriminates = orbit_hist["formation"] != orbit_hist["control"]
    verdict = (
        "FULL_ORBIT_PROBE_DISCRIMINATES_FORMATION_FROM_CONTROL"
        if discriminates else
        "FULL_ORBIT_PROBE_REMAINS_UNINFORMATIVE"
    )
    finding = (
        "After a full-orbit settle the same 64-lane sample "
        + ("does" if discriminates else "does not")
        + " distinguish formation from dirty control; the histograms are the"
        " exact alternative-probe result. The published one-chunk contrast"
        " also relies on equal slicing that drops trailing mapped gates."
    )
    result = {
        "certificate": "THE_A_PROBE_CRITIQUE",
        "sample": {
            "boundary_cap": SATURATION_BOUNDARY_CAP,
            "lane_cap": SATURATION_LANE_CAP,
            "lanes": len(candidates),
        },
        "one_chunk_reproduction": one_hist,
        "equal_slice_trailing_gates_dropped": dict(sorted(dropped_gate_histogram.items())),
        "full_orbit_settle": orbit_hist,
        "full_orbit_discriminates": discriminates,
        "substitution_errors": errors,
        "unique_rejected_state_direction_substitutions": errors // 2,
        "verdict": verdict,
        "finding": finding,
    }
    result["pass"] = bool(
        len(candidates) == 64
        and one_hist == {
            "formation": {0: 60, 2: 4},
            "control": {0: 64},
        }
        and errors == 256
        and sum(orbit_hist["formation"].values()) == 64
        and sum(orbit_hist["control"].values()) == 64
    )
    return result


def public_payload(payload: dict[str, object], hidden: tuple[str, ...]):
    return {key: value for key, value in payload.items() if key not in hidden}


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, seeds, census = independent_census()
    predicates = assemble_clean_predicates()
    rep = independent_replay(program, seeds, census, predicates)

    substrate = substrate_certificate(rep, census)
    ages = record_age_and_periodicity(program, seeds, census, predicates, rep)
    law = law_and_vacuity_certificate(census, rep, ages)
    hunt = intrinsic_predictor_hunt(rep, law)
    probe = a_probe_critique(program, seeds, census, predicates, rep)

    runtime = round(monotonic() - started, 3)
    controls_certificate = {
        "certificate": "CONTROLS",
        **controls,
        "independent_predicate_sizes": {
            "bank0": len(predicates["bank"][0]),
            "bank1": len(predicates["bank"][1]),
            "links": len(predicates["links"]),
            "global": len(predicates["global"]),
        },
        "determinism": {
            "duplicated_lane": census[0],
            "predicate_mismatches": rep["duplicate_mismatches"],
            "final_columns_digest": rep["final_columns_digest"],
        },
        "runtime_seconds": runtime,
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": (
            "All four inputs are literal worktree-relative SHA/blob pins; the"
            " three primaries were AST-parsed only and import-firewalled, and"
            " the duplicate lane matched at every clean predicate boundary."
        ),
    }
    controls_certificate["pass"] = bool(
        controls["pass"]
        and rep["duplicate_mismatches"] == 0
        and runtime < AUDIT_TIMEOUT_SEC
    )

    emitted = (
        substrate,
        public_payload(ages, ("stamp_rung", "cohorts")),
        public_payload(law, ("rows",)),
        hunt,
        probe,
        controls_certificate,
    )
    checks = {payload["certificate"]: payload["pass"] for payload in emitted}
    summary = {
        "arc": "cycles_863_865_time_from_records",
        "checks": checks,
        "runtime_seconds": runtime,
        "replay_runtime_seconds": rep["runtime_seconds"],
        "intrinsic_predictor_verdict": hunt["verdict"],
        "a_probe_verdict": probe["verdict"],
        "pass": all(checks.values()),
    }
    lines = ["CYCLES863_865_ARC_INDEPENDENT_ADVERSARIAL_CHECK"]
    for payload in emitted:
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(
            f"CERTIFICATE {payload['certificate']} {status} {compact(payload)}"
        )
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(
        "CYCLES863_865_ARC_INDEPENDENT_CHECK_"
        + ("PASS" if summary["pass"] else "HONEST_FAIL")
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
