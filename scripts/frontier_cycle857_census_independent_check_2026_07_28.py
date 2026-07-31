#!/usr/bin/env python3
"""Cycle 857 independent adversarial checker for the census formula.

The Cycle-719 source and the Cycle-857 primary are SHA-pinned, BLOCKLISTED
text/AST inputs.  Neither module is imported or executed.  All census,
quotient, constraint, orbit, and bit certificates below use a separate
bit-mask implementation.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle857_census_theorem_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import comb, log2
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CORE_PATH, PRIMARY_PATH = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PRIMARY_PATH: "484f5bf49c15157abf233f852832f9d3781fc82c47a87a768d7959072274642f",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    PRIMARY_PATH: "c39abaca7902fbf355917a21e19eba375a6b1ab0",
}
EXPECTED_CORE_FUNCTION_AST_SHA256 = {
    "interleaved_program": "b5ca56177e52bcec0745fba7dd03eeb68851f670628d38d9cf916dcd109314eb",
    "held_certificate": "01194c16a7201bed6fcbc82e3dd804e9066419ef57edff7d6140b2a2d2252095",
    "held_physical_program_and_track": "b9df78cea656f4f3b9329908cb749ddf9cf97adf6c68343b83c8b22906f13db1",
}

FIXTURE_BANKS = 2
MIN_K = 2
MAX_K = 5
EXPECTED_STRATA = {2: 176, 3: 308, 4: 220, 5: 44}
EXPECTED_ORBIT_STRATA = {2: 16, 3: 28, 4: 20, 5: 4}
EXPECTED_RELAXED = (792, 748, 4048, 935)
EXPECTED_TIGHTENED = (572, 704, 220, 561)


class _Blocklist(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids source import: {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
FIREWALL = _Blocklist()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_text(*args: str) -> str:
    return subprocess.run(
        ("git", *args), cwd=ROOT, check=True, capture_output=True,
        text=True, timeout=20,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
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


def function_nodes(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def derive_core_axes(core_payload: bytes) -> dict[str, object]:
    """Derive n and p from the pinned Cycle-719 source without executing it."""

    tree = ast.parse(core_payload, filename=CORE_PATH)
    functions = function_nodes(tree)
    ast_hashes = {
        name: sha256(ast.dump(
            functions[name], include_attributes=False,
        ).encode("utf-8")).hexdigest()
        for name in EXPECTED_CORE_FUNCTION_AST_SHA256
        if name in functions
    }

    # Independent label projection of the reviewed/pinned interleaving AST.
    labels: list[tuple[str, int]] = [("source", 0)]
    for bank in range(FIXTURE_BANKS):
        labels.append(("bank", bank))
        if bank > 0:
            labels.append(("cross", bank - 1))
        if bank + 1 < FIXTURE_BANKS:
            labels.extend((
                ("handoff", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    for edge in range(FIXTURE_BANKS - 2, -1, -1):
        labels.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    labels.append(("finalizer", 0))

    ring_size = len(labels)
    phase_labels = tuple(range(2 * FIXTURE_BANKS))
    ast_exact = ast_hashes == EXPECTED_CORE_FUNCTION_AST_SHA256
    return {
        "fixture_banks": FIXTURE_BANKS,
        "station_labels": tuple(labels),
        "ring_size": ring_size,
        "phase_labels": phase_labels,
        "function_AST_sha256": ast_hashes,
        "function_AST_sha256_exact": ast_exact,
        "derivation": (
            "Pinned interleaved_program label projection: source + banks + "
            "crosses + three forward edge stations + three reverse edge "
            "stations + finalizer. For b=2 this is 11. Pinned "
            "held_certificate iterates range(2*b), giving phases 0..3."
        ),
        "pass": bool(ast_exact and ring_size == 11 and phase_labels == (0, 1, 2, 3)),
    }


def occupied(mask: int, stations: int) -> tuple[int, ...]:
    return tuple(site for site in range(stations) if mask & (1 << site))


def cyclic_separated(mask: int, stations: int, distance: int) -> bool:
    """Own admissibility predicate: no occupied pair is < distance apart."""

    sites = occupied(mask, stations)
    return all(
        not (mask & (1 << ((site + delta) % stations)))
        for site in sites
        for delta in range(1, distance)
    )


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    shift %= stations
    full = (1 << stations) - 1
    return ((mask << shift) | (mask >> (stations - shift))) & full


def enumerate_census(
    stations: int, phases: tuple[int, ...], minimum_k: int, maximum_k: int,
    distance: int = 2,
) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for mask in range(1 << stations):
        count = mask.bit_count()
        if minimum_k <= count <= maximum_k and cyclic_separated(
            mask, stations, distance,
        ):
            rows.extend((count, phase, mask) for phase in phases)
    return tuple(rows)


def setup_orbits(
    setups: tuple[tuple[int, int, int], ...], stations: int,
) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    universe = set(setups)
    pending = set(setups)
    result: list[tuple[tuple[int, int, int], ...]] = []
    while pending:
        count, phase, mask = min(pending)
        row = tuple(sorted({
            (count, phase, rotate_mask(mask, shift, stations))
            for shift in range(stations)
        }))
        if not set(row) <= universe:
            raise AssertionError(("translation closure", count, phase, mask))
        result.append(row)
        pending.difference_update(row)
    return tuple(sorted(result, key=lambda row: row[0]))


def enumeration_certificate(core_axes: dict[str, object]) -> tuple[
    dict[str, object], tuple[tuple[int, int, int], ...]
]:
    stations = int(core_axes["ring_size"])
    phases = tuple(int(value) for value in core_axes["phase_labels"])
    setups = enumerate_census(stations, phases, MIN_K, MAX_K)
    orbits = setup_orbits(setups, stations)
    strata = {
        count: sum(row[0] == count for row in setups)
        for count in range(MIN_K, MAX_K + 1)
    }
    orbit_strata = {
        count: sum(row[0][0] == count for row in orbits)
        for count in range(MIN_K, MAX_K + 1)
    }
    orbit_histogram = {
        size: sum(len(row) == size for row in orbits)
        for size in sorted({len(row) for row in orbits})
    }
    passed = bool(
        core_axes["pass"]
        and strata == EXPECTED_STRATA
        and orbit_strata == EXPECTED_ORBIT_STRATA
        and len(setups) == 748
        and len(orbits) == 68
        and orbit_histogram == {11: 68}
    )
    certificate = {
        "finding": (
            "Independent bit-mask admissibility on the SHA-pinned Cycle-719 "
            "n=11, p=4 axes gives 176/308/220/44, total 748, partitioned "
            "into exactly 68 free C11 translation orbits."
        ),
        "core_axes": core_axes,
        "admissibility": (
            "A simple C11 bit mask is admissible iff no occupied site has an "
            "occupied clockwise neighbor; phases are a separate 0..3 axis."
        ),
        "stratum_counts": strata,
        "orbit_stratum_counts": orbit_strata,
        "total": len(setups),
        "orbit_count": len(orbits),
        "orbit_size_histogram": orbit_histogram,
        "setup_sha256": digest(setups),
        "orbit_sha256": digest(orbits),
        "pass": passed,
    }
    return certificate, setups


def gaps_from_separators(total: int, separators: tuple[int, ...]) -> tuple[int, ...]:
    cuts = (0,) + separators + (total,)
    return tuple(right - left for left, right in zip(cuts, cuts[1:]))


def separators_from_gaps(gaps: tuple[int, ...]) -> tuple[int, ...]:
    running = 0
    result = []
    for gap in gaps[:-1]:
        running += gap
        result.append(running)
    return tuple(result)


def positive_gap_vectors(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        gaps_from_separators(total, separators)
        for separators in combinations(range(1, total), parts - 1)
    )


def mask_from_gaps(origin: int, gaps: tuple[int, ...], stations: int) -> int:
    mask = 1 << origin
    site = origin
    for gap in gaps[:-1]:
        site = (site + gap + 1) % stations
        mask |= 1 << site
    if (site + gaps[-1] + 1) % stations != origin:
        raise AssertionError(("gaps do not close", origin, gaps, stations))
    return mask


def gaps_from_mask(mask: int, origin: int, stations: int) -> tuple[int, ...]:
    if not mask & (1 << origin):
        raise ValueError("the distinguished origin must be occupied")
    count = mask.bit_count()
    site = origin
    gaps = []
    for _ in range(count):
        empty = 0
        step = 1
        while not mask & (1 << ((site + step) % stations)):
            empty += 1
            step += 1
            if step > stations:
                raise AssertionError("nonempty mask scan failed to close")
        gaps.append(empty)
        site = (site + step) % stations
    if site != origin:
        raise AssertionError(("distinguished-source scan failed", mask, origin))
    return tuple(gaps)


def rotate_tuple(row: tuple[int, ...], shift: int = 1) -> tuple[int, ...]:
    shift %= len(row)
    return row[shift:] + row[:shift]


def tuple_rotation_orbits(
    rows: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    pending = set(rows)
    result = []
    while pending:
        representative = min(pending)
        orbit = tuple(sorted({
            rotate_tuple(representative, shift)
            for shift in range(len(representative))
        }))
        result.append(orbit)
        pending.difference_update(orbit)
    return tuple(sorted(result, key=lambda row: row[0]))


def labeled_source_orbit(
    origin: int, gaps: tuple[int, ...], stations: int,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    result = []
    current_origin = origin
    current_gaps = gaps
    for _ in range(len(gaps)):
        result.append((current_origin, current_gaps))
        current_origin = (current_origin + current_gaps[0] + 1) % stations
        current_gaps = rotate_tuple(current_gaps)
    return tuple(result)


def formula_structure_certificate(
    core_axes: dict[str, object], setups: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    stations = int(core_axes["ring_size"])
    phases = tuple(int(value) for value in core_axes["phase_labels"])
    setup_set = set(setups)
    result_rows = []
    all_pass = True

    for count in range(MIN_K, MAX_K + 1):
        empty_sites = stations - count
        separators = tuple(combinations(range(1, empty_sites), count - 1))
        gaps = positive_gap_vectors(empty_sites, count)
        separator_roundtrip = bool(
            len(gaps) == len(set(gaps))
            and {separators_from_gaps(row) for row in gaps} == set(separators)
            and all(
                gaps_from_separators(empty_sites, separators_from_gaps(row)) == row
                for row in gaps
            )
        )
        binomial_value = comb(stations - count - 1, count - 1)

        admissible_masks = tuple(sorted({
            mask for setup_count, _phase, mask in setups
            if setup_count == count
        }))
        labeled_domain = tuple(
            (origin, row)
            for origin in range(stations)
            for row in gaps
        )
        mapped_labeled = tuple(
            (mask_from_gaps(origin, row, stations), origin)
            for origin, row in labeled_domain
        )
        expected_labeled = tuple(sorted(
            (mask, source)
            for mask in admissible_masks
            for source in occupied(mask, stations)
        ))
        observed_labeled = tuple(sorted(mapped_labeled))
        inverse_exact = all(
            gaps_from_mask(mask, source, stations) == row
            for (origin, row), (mask, source) in zip(labeled_domain, mapped_labeled)
            if source == origin
        )
        spacing_bijection_exact = bool(
            observed_labeled == expected_labeled
            and inverse_exact
            and all(cyclic_separated(mask, stations, 2) for mask, _ in mapped_labeled)
        )

        source_quotient_orbits = []
        quotient_fibers_exact = True
        pending = set(labeled_domain)
        while pending:
            origin, row = min(pending)
            orbit = labeled_source_orbit(origin, row, stations)
            masks = {mask_from_gaps(site, vector, stations) for site, vector in orbit}
            quotient_fibers_exact &= len(orbit) == count and len(set(orbit)) == count
            quotient_fibers_exact &= len(masks) == 1
            source_quotient_orbits.append(orbit)
            pending.difference_update(orbit)
        quotient_fibers_exact &= len(source_quotient_orbits) == len(admissible_masks)

        shape_orbits = tuple_rotation_orbits(gaps)
        shape_orbit_histogram = {
            size: sum(len(row) == size for row in shape_orbits)
            for size in sorted({len(row) for row in shape_orbits})
        }
        integral = binomial_value % count == 0
        shape_count = binomial_value // count if integral else -1

        constructed = {
            (count, phase, rotate_mask(
                mask_from_gaps(0, min(shape), stations), origin, stations,
            ))
            for shape in shape_orbits
            for phase in phases
            for origin in range(stations)
        }
        expected_stratum = {
            setup for setup in setup_set if setup[0] == count
        }
        product_bijection_exact = constructed == expected_stratum and len(constructed) == (
            shape_count * len(phases) * stations
        )
        phase_axis_exact = all(
            {phase for setup_count, phase, setup_mask in setups
             if setup_count == count and setup_mask == mask} == set(phases)
            for mask in admissible_masks
        )
        translation_axis_free = all(
            len({rotate_mask(
                mask_from_gaps(0, min(shape), stations), shift, stations,
            ) for shift in range(stations)}) == stations
            for shape in shape_orbits
        )
        formula_value = binomial_value * len(phases) * stations // count
        row_pass = bool(
            separator_roundtrip
            and len(gaps) == binomial_value
            and spacing_bijection_exact
            and quotient_fibers_exact
            and integral
            and shape_orbit_histogram == {count: shape_count}
            and phase_axis_exact
            and translation_axis_free
            and product_bijection_exact
            and formula_value == EXPECTED_STRATA[count]
        )
        all_pass &= row_pass
        result_rows.append({
            "k": count,
            "spacing_bars_bijection": {
                "empty_sites_sum": empty_sites,
                "separator_slots": empty_sites - 1,
                "separators_chosen": count - 1,
                "formula": f"C({stations - count - 1},{count - 1})",
                "positive_distinguished_source_gap_vectors": len(gaps),
                "roundtrip_exact": separator_roundtrip,
            },
            "gap_vector_to_labeled_placement_bijection_exact": spacing_bijection_exact,
            "origin_factor": {
                "axis": "C11 translation of a canonical gap-rotation class",
                "choices": stations,
                "free_exact": translation_axis_free,
            },
            "phase_factor": {
                "axis": "Cycle-719 held_certificate event seed",
                "labels": phases,
                "cartesian_exact": phase_axis_exact,
            },
            "source_label_quotient": {
                "action": (
                    "move the distinguished source clockwise and cyclically "
                    "rotate its positive-gap vector"
                ),
                "quotient_size": count,
                "all_fibers_exact": quotient_fibers_exact,
                "quotient_orbit_count": len(source_quotient_orbits),
            },
            "binomial_divisible_by_k": integral,
            "gap_rotation_orbit_histogram": shape_orbit_histogram,
            "shape_choices_after_source_quotient": shape_count,
            "constructed_shape_x_phase_x_origin_bijection_exact": product_bijection_exact,
            "formula": f"C({10 - count},{count - 1})*4*11/{count}",
            "formula_value": formula_value,
            "enumerated_value": len(expected_stratum),
            "pass": row_pass,
        })

    if all_pass:
        finding = (
            "The formula is structurally certified, not merely numerically "
            "matched: C(10-k,k-1) is bijective to positive circular empty-gap "
            "vectors based at a distinguished source; the free k-fold source "
            "relabeling quotient produces gap-rotation shapes; those shapes "
            "cross bijectively with four core event phases and eleven free "
            "translations. Division by k is integral for k=2..5."
        )
        verdict = "STRUCTURE_CERTIFIED"
    else:
        finding = (
            "PRIMARY REFUTED: at least one claimed factor lacks the required "
            "spacing, phase, origin, or source-label quotient bijection even "
            "if its numerical product happens to match."
        )
        verdict = "PRIMARY_REFUTED_STRUCTURE"
    return {
        "finding": finding,
        "verdict": verdict,
        "factor_axis_map": {
            "C(10-k,k-1)": "distinguished-source positive circular gap vectors",
            "4": "Cycle-719 event-seed phase labels 0..3",
            "11": "free translations of each canonical gap-rotation shape",
            "/k": "exact quotient by the cyclic distinguished-source action",
        },
        "rows": tuple(result_rows),
        "pass": bool(all_pass),
    }


def constraint_table_certificate(core_axes: dict[str, object]) -> dict[str, object]:
    stations = int(core_axes["ring_size"])
    ambient_phases = tuple(range(5))
    ambient = tuple(
        (mask.bit_count(), phase, mask)
        for mask in range(1 << stations)
        if 1 <= mask.bit_count() <= 6
        for phase in ambient_phases
    )
    names = (
        "MIN_MULTISOURCE_k_ge_2",
        "PACKING_WINDOW_k_le_5",
        "PAIRWISE_SEPARATION_distance_ge_2",
        "CORE_PHASE_MEMBERSHIP_phase_lt_4",
    )

    def minimum(setup: tuple[int, int, int]) -> bool:
        return setup[0] >= 2

    def packing(setup: tuple[int, int, int]) -> bool:
        return setup[0] <= 5

    def separation(setup: tuple[int, int, int]) -> bool:
        return cyclic_separated(setup[2], stations, 2)

    def phase_member(setup: tuple[int, int, int]) -> bool:
        return setup[1] < 4

    predicates = (minimum, packing, separation, phase_member)
    tightened = (
        lambda setup: setup[0] >= 3,
        lambda setup: setup[0] <= 4,
        lambda setup: cyclic_separated(setup[2], stations, 3),
        lambda setup: setup[1] < 3,
    )

    base = tuple(
        setup for setup in ambient
        if all(predicate(setup) for predicate in predicates)
    )
    relaxed_counts = []
    tightened_counts = []
    rows = []
    for index, name in enumerate(names):
        relaxed = tuple(
            setup for setup in ambient
            if all(
                predicate(setup)
                for other, predicate in enumerate(predicates)
                if other != index
            )
        )
        active = list(predicates)
        active[index] = tightened[index]
        one_notch_tight = tuple(
            setup for setup in ambient
            if all(predicate(setup) for predicate in active)
        )
        relaxed_counts.append(len(relaxed))
        tightened_counts.append(len(one_notch_tight))
        rows.append({
            "constraint": name,
            "base": len(base),
            "relaxed": len(relaxed),
            "relaxation_delta": len(relaxed) - len(base),
            "tightened": len(one_notch_tight),
            "tightening_delta": len(base) - len(one_notch_tight),
        })

    separated_masks = tuple(
        mask for mask in range(1 << stations)
        if cyclic_separated(mask, stations, 2)
    )
    follower_injection_exact = all(
        len({(site + 1) % stations for site in occupied(mask, stations)})
        == mask.bit_count()
        and all(
            not mask & (1 << ((site + 1) % stations))
            for site in occupied(mask, stations)
        )
        for mask in separated_masks
    )
    packing_implied = bool(
        follower_injection_exact
        and all(2 * mask.bit_count() <= stations for mask in separated_masks)
    )
    relaxed_tuple = tuple(relaxed_counts)
    tightened_tuple = tuple(tightened_counts)
    passed = bool(
        len(base) == 748
        and relaxed_tuple == EXPECTED_RELAXED
        and tightened_tuple == EXPECTED_TIGHTENED
        and relaxed_counts[1] == len(base)
        and packing_implied
    )
    return {
        "finding": (
            "Independent one-at-a-time counterfactuals reproduce relaxed "
            "792/748/4048/935 and tightened 572/704/220/561. The no-op is "
            "PACKING_WINDOW_k_le_5 (748 -> 748): distance>=2 injects every "
            "source into its distinct empty clockwise follower, so k<=11-k "
            "and hence k<=5; the packing window is implied by separation."
        ),
        "ambient": "all simple C11 masks with k=1..6 and formal phases 0..4",
        "ambient_count": len(ambient),
        "intersection_count": len(base),
        "relaxed_counts_in_named_order": relaxed_tuple,
        "tightened_counts_in_named_order": tightened_tuple,
        "rows": tuple(rows),
        "no_op_relaxation": "PACKING_WINDOW_k_le_5",
        "no_op_implication_certificate": {
            "argument": (
                "The clockwise-successor map sends each occupied site to a "
                "distinct empty site under distance>=2. Thus k<=11-k."
            ),
            "follower_injection_exhaustive_exact": follower_injection_exact,
            "packing_implied_by_separation_exact": packing_implied,
        },
        "intersection_sha256": digest(base),
        "pass": passed,
    }


def bit_identity_certificate(enumeration: dict[str, object]) -> dict[str, object]:
    total = int(enumeration["total"])
    families = int(enumeration["orbit_count"])
    origins = 11
    factorization_exact = total == families * origins
    free_action_exact = enumeration["orbit_size_histogram"] == {origins: families}
    displayed_total = log2(total)
    displayed_family = log2(families)
    displayed_allocation = log2(origins)
    return {
        "finding": (
            "The exact identity log2(748)=log2(68)+log2(11) is the logarithm "
            "of the certified free-action factorization 748=68*11. The "
            "within-family allocation bits are log2(11); log2(68) selects the "
            "translation-orbit family."
        ),
        "exact_integer_factorization": "748=68*11",
        "exact_log_identity": "log2(748)=log2(68)+log2(11)",
        "family_choice_bits": "log2(68)",
        "allocation_bits_named": "log2(11)",
        "decimal_display": {
            "log2_748": round(displayed_total, 15),
            "log2_68": round(displayed_family, 15),
            "log2_11": round(displayed_allocation, 15),
            "floating_residual": displayed_total - (
                displayed_family + displayed_allocation
            ),
        },
        "factorization_exact": factorization_exact,
        "free_C11_action_exact": free_action_exact,
        "pass": bool(factorization_exact and free_action_exact),
    }


def source_controls() -> tuple[dict[str, object], bytes]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    rows = []
    for path in AUDIT_INPUT_PATHS:
        payload = payloads[path]
        sha = sha256(payload).hexdigest()
        blob = git_blob(payload)
        rows.append({
            "path": path,
            "exists": (ROOT / path).is_file(),
            "worktree_relative": not Path(path).is_absolute(),
            "access": "SHA_PINNED_WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": sha,
            "expected_sha256": EXPECTED_SHA256[path],
            "sha256_exact": sha == EXPECTED_SHA256[path],
            "git_blob": blob,
            "expected_git_blob": EXPECTED_GIT_BLOBS[path],
            "git_blob_exact": blob == EXPECTED_GIT_BLOBS[path],
            "HEAD_git_blob": git_text("rev-parse", f"HEAD:{path}"),
        })

    direct_frontier_imports = []
    dynamic_import_calls = []
    for node in ast.walk(self_tree):
        if isinstance(node, ast.Import):
            direct_frontier_imports.extend(
                alias.name for alias in node.names
                if alias.name.startswith("frontier_cycle")
            )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.startswith("frontier_cycle"):
                direct_frontier_imports.append(module)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "__import__":
                dynamic_import_calls.append("__import__")
            elif (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "import_module"
            ):
                dynamic_import_calls.append("import_module")

    blocked_loaded = tuple(sorted(
        module for module in sys.modules
        if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    base_pass = bool(
        literal_paths == AUDIT_INPUT_PATHS
        and all(
            row["exists"]
            and row["worktree_relative"]
            and row["sha256_exact"]
            and row["git_blob_exact"]
            and row["HEAD_git_blob"] == row["expected_git_blob"]
            for row in rows
        )
        and not direct_frontier_imports
        and not dynamic_import_calls
        and not blocked_loaded
        and not FIREWALL.hits
        and CORE_PATH in trees
        and PRIMARY_PATH in trees
    )
    return ({
        "finding": (
            "Both the Cycle-719 source primary and Cycle-857 target are exact "
            "SHA-256/Git-blob matches, read only as worktree-relative text/AST, "
            "and BLOCKLISTED from import. Full derivation replay is deterministic; "
            "runtime is below 1400 s and stdout below 150 KB."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_rows": tuple(rows),
        "BLOCKLISTED_MODULES": BLOCKLISTED_MODULES,
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "dynamic_import_calls": tuple(dynamic_import_calls),
        "blocked_modules_loaded": blocked_loaded,
        "firewall_hits": tuple(FIREWALL.hits),
        "source_controls_pass": base_pass,
        "pass": False,
    }, payloads[CORE_PATH])


def derive_suite(core_payload: bytes) -> tuple[
    dict[str, object], dict[str, object], dict[str, object], dict[str, object]
]:
    core_axes = derive_core_axes(core_payload)
    enumeration, setups = enumeration_certificate(core_axes)
    structure = formula_structure_certificate(core_axes, setups)
    constraints = constraint_table_certificate(core_axes)
    bits = bit_identity_certificate(enumeration)
    return enumeration, structure, constraints, bits


def render(
    certificates: dict[str, dict[str, object]], report: dict[str, object],
) -> str:
    lines = []
    for name, certificate in certificates.items():
        status = "PASS" if certificate["pass"] else "FAIL"
        lines.append(f"{status} {name} :: {compact(certificate)}")
        lines.append(f"FINDING {name} :: {certificate['finding']}")
    for row in certificates["THE_FORMULA_STRUCTURE"]["rows"]:
        lines.append(
            f"STRUCTURE k={row['k']} :: {row['formula']}="
            f"{row['formula_value']} enumeration={row['enumerated_value']} "
            f"integral={row['binomial_divisible_by_k']} "
            f"bijection={row['constructed_shape_x_phase_x_origin_bijection_exact']}"
        )
    for row in certificates["THE_CONSTRAINT_TABLE"]["rows"]:
        lines.append(
            f"CONSTRAINT {row['constraint']} :: base={row['base']} "
            f"relaxed={row['relaxed']} tightened={row['tightened']}"
        )
    lines.append("SUMMARY_JSON " + compact(report))
    if not certificates["THE_FORMULA_STRUCTURE"]["pass"]:
        lines.append("PRIMARY_REFUTED_STRUCTURE")
    lines.append(
        "CYCLE857_CENSUS_INDEPENDENT_CHECK_PASS"
        if report["pass"] else "CYCLE857_CENSUS_INDEPENDENT_CHECK_FAIL"
    )
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, dict[str, object]], report: dict[str, object],
    controls_base: bool,
) -> str:
    controls = certificates["CONTROLS"]
    for _attempt in range(20):
        controls["pass"] = bool(
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        report["pass"] = all(
            certificate["pass"] for certificate in certificates.values()
        )
        output = render(certificates, report)
        size = len(output.encode("utf-8"))
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    controls, core_payload = source_controls()
    source_controls_pass = bool(controls["source_controls_pass"])
    suite = derive_suite(core_payload)
    replay = derive_suite(core_payload)
    deterministic = suite == replay
    elapsed = monotonic() - started
    blocked_loaded_end = tuple(sorted(
        module for module in sys.modules
        if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls.update({
        "determinism_replay": {
            "method": (
                "repeat AST axis derivation, bit-mask enumeration, C11 orbit "
                "partition, bars/gaps/source quotient bijections, constraint "
                "counterfactuals, and exact bit factorization"
            ),
            "full_replay_exact": deterministic,
        },
        "blocked_modules_loaded_at_end": blocked_loaded_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "certificate_digest_sha256": digest(suite),
    })
    controls_base = bool(
        source_controls_pass
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not blocked_loaded_end
        and not FIREWALL.hits
    )
    certificates = {
        "THE_ENUMERATION": suite[0],
        "THE_FORMULA_STRUCTURE": suite[1],
        "THE_CONSTRAINT_TABLE": suite[2],
        "THE_BIT_IDENTITY": suite[3],
        "CONTROLS": controls,
    }
    report = {
        "cycle": 857,
        "checker": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "primary_structure_verdict": suite[1]["verdict"],
        "stratum_counts": suite[0]["stratum_counts"],
        "total": suite[0]["total"],
        "orbit_count": suite[0]["orbit_count"],
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    output = stable_render(certificates, report, controls_base)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(
            "FAIL CONTROLS :: " + compact({
                "exception_type": type(error).__name__,
                "exception": str(error),
                "pass": False,
            }) + "\nCYCLE857_CENSUS_INDEPENDENT_CHECK_FAIL\n"
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
