#!/usr/bin/env python3
"""Independent bounded checker for the Cycle 728 marked-edge theorem.

The Cycle 728 primary is parsed only as source data.  It is deliberately
blocked from import, and none of its executable definitions are reused.
"""

from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
from importlib.abc import MetaPathFinder
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
PRIMARY_IMPORT_BLOCKLIST = (
    "frontier_cycle728_bksf_holonomy_compression_2026_07_28",
)

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / AUDIT_INPUT_PATHS[0]


class _PrimaryImportBlocker(MetaPathFinder):
    """Make an accidental import of the audited primary an immediate failure."""

    def find_spec(self, fullname, path=None, target=None):
        del path, target
        if fullname in PRIMARY_IMPORT_BLOCKLIST:
            raise ImportError(f"independent-check blocklist rejected {fullname}")
        return None


_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


FROZEN: dict[str, object] = {}
CONVENTIONS: dict[str, object] = {}

REQUIRED_FROZEN_NAMES = (
    "FROZEN_PROGRAM_CENSUS",
    "FROZEN_SUPPORT_CENSUS",
    "FROZEN_AMENDED_SUPPORT_CENSUS",
    "FROZEN_CONTROL_CENSUS",
    "FROZEN_TWIST_CONTROL_CENSUS",
    "FROZEN_ENUMERATION_CENSUS",
    "FROZEN_EXHAUSTIVE_RESULT_CENSUS",
    "FROZEN_AMENDED_H_SECTOR_CENSUS",
    "FROZEN_HOLONOMY_CENSUS",
    "FROZEN_R1_PULLBACK",
    "FROZEN_R2_PULLBACK",
    "FROZEN_R_PULLBACK",
    "FROZEN_R_ROW_SET_PERMUTED",
    "FROZEN_R_COUNTEREXAMPLE",
    "FROZEN_WITNESS_PAIR",
    "FROZEN_MARKED_EDGE_WITNESS_PAIR",
    "FROZEN_RADIUS1_WINDOW_CENSUS",
)
REFUTATION_LITERAL_NAMES = (
    "FROZEN_EXHAUSTIVE_RESULT_CENSUS",
    "FROZEN_HOLONOMY_CENSUS",
    "FROZEN_R_ROW_SET_PERMUTED",
    "FROZEN_R_COUNTEREXAMPLE",
    "FROZEN_WITNESS_PAIR",
)
R_LITERAL_NAMES = (
    "FROZEN_R1_PULLBACK",
    "FROZEN_R2_PULLBACK",
    "FROZEN_R_PULLBACK",
)
TWIST_LITERAL_NAMES = (
    "FROZEN_AMENDED_SUPPORT_CENSUS",
    "FROZEN_TWIST_CONTROL_CENSUS",
    "FROZEN_ENUMERATION_CENSUS",
    "FROZEN_AMENDED_H_SECTOR_CENSUS",
    "FROZEN_MARKED_EDGE_WITNESS_PAIR",
    "FROZEN_RADIUS1_WINDOW_CENSUS",
)


def _assignment_nodes(tree: ast.AST) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for node in getattr(tree, "body", ()):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            found[node.targets[0].id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            found[node.target.id] = node.value
    return found


def _literal(node: ast.AST) -> object:
    return ast.literal_eval(node)


def _compact(value: object, limit: int = 1400) -> str:
    text = json.dumps(value, sort_keys=True, default=repr, separators=(",", ":"))
    if len(text) <= limit:
        return text
    return json.dumps(
        {
            "sha256": sha256(text.encode()).hexdigest(),
            "unbounded_characters": len(text),
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _mask(width: int) -> int:
    return (1 << width) - 1


def _next_source_bits(value: int, width: int) -> int:
    """Output bit s receives input bit s+1 on the cyclic chain."""

    return ((value >> 1) | ((value & 1) << (width - 1))) & _mask(width)


def _previous_source_bits(value: int, width: int) -> int:
    """Output bit s receives input bit s-1 on the cyclic chain."""

    return (((value << 1) & _mask(width)) | (value >> (width - 1))) & _mask(
        width
    )


def _first_edge(width: int) -> tuple[int, int]:
    return min((site, (site + 1) % width) for site in range(width))


def _row_mask(a: int, b: int, refs: int, h: int, width: int) -> int:
    """Evaluate every amended local row, independently of the primary."""

    marked = _first_edge(width)[0]
    boundary = refs ^ _next_source_bits(refs, width)
    return (a ^ b ^ boundary ^ (h << marked)) & _mask(width)


def _token_parity(a: int, b: int) -> int:
    parity = 0
    rails = a ^ b
    while rails:
        parity ^= rails & 1
        rails >>= 1
    return parity


def _reference_extension(
    a: int, b: int, h: int, width: int
) -> tuple[int, int]:
    """Solve the row recurrence from ref_0=0 and return its closure bit."""

    rails = a ^ b
    refs = 0
    current = 0
    closure = 0
    marked = _first_edge(width)[0]
    for site in range(width):
        following = current ^ ((rails >> site) & 1)
        if site == marked:
            following ^= h
        if site + 1 < width:
            refs |= following << (site + 1)
            current = following
        else:
            closure = following
    return refs, closure


def extraction() -> tuple[bool, dict[str, object]]:
    """AST-extract all frozen source literals without executing Cycle 728."""

    source = PRIMARY_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PRIMARY_PATH))
    nodes = _assignment_nodes(tree)
    literal_values: dict[str, object] = {}
    literal_failures: dict[str, str] = {}
    requested = REQUIRED_FROZEN_NAMES + (
        "AUDIT_TIMEOUT_SEC",
        "NOTE_PATH",
        "AUDIT_INPUT_PATHS",
        "EXHAUSTIVE_SEED",
    )
    for name in requested:
        try:
            literal_values[name] = _literal(nodes[name])
        except Exception as exc:
            literal_failures[name] = f"{type(exc).__name__}: {exc}"

    FROZEN.clear()
    FROZEN.update(
        (name, literal_values[name])
        for name in REQUIRED_FROZEN_NAMES
        if name in literal_values
    )
    CONVENTIONS.clear()
    CONVENTIONS.update(
        (name, literal_values[name])
        for name in (
            "AUDIT_TIMEOUT_SEC",
            "NOTE_PATH",
            "AUDIT_INPUT_PATHS",
            "EXHAUSTIVE_SEED",
        )
        if name in literal_values
    )

    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    self_nodes = _assignment_nodes(self_tree)
    try:
        self_audit_paths = _literal(self_nodes["AUDIT_INPUT_PATHS"])
    except Exception as exc:
        self_audit_paths = f"{type(exc).__name__}: {exc}"
    try:
        self_blocklist = _literal(self_nodes["PRIMARY_IMPORT_BLOCKLIST"])
    except Exception as exc:
        self_blocklist = f"{type(exc).__name__}: {exc}"

    expected_inputs = (
        "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    )
    categories = {
        "refutation": REFUTATION_LITERAL_NAMES,
        "R_pullback": R_LITERAL_NAMES,
        "witness": (
            "FROZEN_WITNESS_PAIR",
            "FROZEN_MARKED_EDGE_WITNESS_PAIR",
            "FROZEN_RADIUS1_WINDOW_CENSUS",
        ),
        "twist": TWIST_LITERAL_NAMES,
    }
    categories_literal = {
        key: all(name in literal_values for name in names)
        for key, names in categories.items()
    }
    primary_was_not_imported = all(
        name not in sys.modules for name in PRIMARY_IMPORT_BLOCKLIST
    )
    passed = (
        not literal_failures
        and len(FROZEN) == len(REQUIRED_FROZEN_NAMES)
        and all(categories_literal.values())
        and isinstance(literal_values.get("AUDIT_INPUT_PATHS"), tuple)
        and self_audit_paths == expected_inputs
        and self_blocklist == PRIMARY_IMPORT_BLOCKLIST
        and primary_was_not_imported
    )
    return passed, {
        "ast_only": True,
        "extracted_frozen_literals": len(FROZEN),
        "literal_failures": literal_failures,
        "literal_categories": categories_literal,
        "primary_AUDIT_tuple_literal": isinstance(
            literal_values.get("AUDIT_INPUT_PATHS"), tuple
        ),
        "checker_AUDIT_tuple_literal_and_exact": self_audit_paths
        == expected_inputs,
        "blocklist": self_blocklist,
        "primary_imported": not primary_was_not_imported,
    }


def _agreement_and_coboundary(refs: int, width: int) -> tuple[int, int]:
    agreement_xor = 0
    difference_xor = 0
    for site in range(width):
        left = (refs >> site) & 1
        right = (refs >> ((site + 1) % width)) & 1
        agreement_xor ^= int(left == right)
        difference_xor ^= left ^ right
    return agreement_xor, difference_xor


def _holonomy_row(width: int) -> tuple[tuple[str, object], ...]:
    agreements: Counter[int] = Counter()
    differences: Counter[int] = Counter()
    for refs in range(1 << width):
        agreement, difference = _agreement_and_coboundary(refs, width)
        agreements[agreement] += 1
        differences[difference] += 1
    return (
        ("stations", width),
        ("reference_states", 1 << width),
        (
            "agreement_value_census",
            tuple((str(key), value) for key, value in sorted(agreements.items())),
        ),
        (
            "disagreement_value_census",
            tuple((str(key), value) for key, value in sorted(differences.items())),
        ),
    )


def coboundary_refutation_recount() -> tuple[bool, dict[str, object]]:
    observed = (_holonomy_row(10), _holonomy_row(11))
    expected = FROZEN["FROZEN_HOLONOMY_CENSUS"]
    constant_proof = all(
        dict(row)["agreement_value_census"]
        == ((str(dict(row)["stations"] & 1), dict(row)["reference_states"]),)
        and dict(row)["disagreement_value_census"]
        == (("0", dict(row)["reference_states"]),)
        for row in observed
    )
    return observed == expected and constant_proof, {
        "ring10": dict(observed[0]),
        "ring11": dict(observed[1]),
        "matches_frozen": observed == expected,
        "agreement_is_ring_size_parity": constant_proof,
        "coboundary_is_identically_zero": constant_proof,
    }


def _symbolic_twist_identity(width: int) -> bool:
    remaining: set[tuple[str, int]] = set()
    marked = _first_edge(width)[0]
    for site in range(width):
        row = {
            ("A", site),
            ("B", site),
            ("ref", site),
            ("ref", (site + 1) % width),
        }
        if site == marked:
            row.add(("h", marked))
        remaining.symmetric_difference_update(row)
    expected = {
        (rail, site)
        for rail in ("A", "B")
        for site in range(width)
    } | {("h", marked)}
    return remaining == expected


def _shape_from_template(
    observed: dict[str, object], template: tuple[tuple[str, object], ...]
) -> tuple[tuple[str, object], ...]:
    return tuple((name, observed[name]) for name, _value in template)


def twist_theorem_recount() -> tuple[bool, dict[str, object]]:
    """Complete per-h enumeration of all 2^22 ring-11 rail states."""

    width = 11
    rail_mask = _mask(width)
    total = 1 << (2 * width)
    seed = CONVENTIONS["EXHAUSTIVE_SEED"]
    fixed_refs = int.from_bytes(sha256(seed).digest(), "big") & rail_mask
    fixed_boundary = fixed_refs ^ _next_source_bits(fixed_refs, width)
    original_holonomy = _agreement_and_coboundary(fixed_refs, width)[0]

    original = {
        "telescope_failures": 0,
        "local_satisfied_states": 0,
        "local_satisfied_even_token_states": 0,
        "local_satisfied_token_holonomy_matches": 0,
        "token_parity_equals_holonomy_states": 0,
        "exact_sector_separation_failures": 0,
    }
    sectors: list[dict[str, object]] = []

    for h in (0, 1):
        counts: dict[str, object] = {
            "h": h,
            "rail_states": total,
            "twist_telescope_failures": 0,
            "fixed_ref_satisfied_states": 0,
            "fixed_ref_matching_states": 0,
            "compression_a_failures": 0,
            "token_parity_sector_states": 0,
            "projected_satisfied_states": 0,
            "projected_exact_separation_failures": 0,
            "canonical_extension_failures": 0,
            "complement_extension_failures": 0,
            "satisfying_reference_extensions": 0,
        }
        for packed in range(total):
            a = packed & rail_mask
            b = packed >> width
            rails = a ^ b
            parity = rails.bit_count() & 1
            untwisted_rows = rails ^ fixed_boundary
            amended_rows = untwisted_rows ^ h

            counts["twist_telescope_failures"] += (
                (amended_rows.bit_count() & 1) != (parity ^ h)
            )
            fixed_satisfied = amended_rows == 0
            in_sector = parity == h
            counts["fixed_ref_satisfied_states"] += fixed_satisfied
            counts["fixed_ref_matching_states"] += fixed_satisfied and in_sector
            counts["compression_a_failures"] += fixed_satisfied and not in_sector
            counts["token_parity_sector_states"] += in_sector

            closure = parity ^ h
            projected_satisfied = closure == 0
            if in_sector:
                canonical, recurrence_closure = _reference_extension(
                    a, b, h, width
                )
                complement = canonical ^ rail_mask
                canonical_failure = (
                    recurrence_closure != 0
                    or _row_mask(a, b, canonical, h, width) != 0
                )
                complement_failure = (
                    _row_mask(a, b, complement, h, width) != 0
                )
                counts["canonical_extension_failures"] += canonical_failure
                counts["complement_extension_failures"] += complement_failure
                projected_satisfied = not (
                    canonical_failure or complement_failure
                )
                counts["satisfying_reference_extensions"] += (
                    2 if projected_satisfied else 0
                )
            counts["projected_satisfied_states"] += projected_satisfied
            counts["projected_exact_separation_failures"] += (
                projected_satisfied != in_sector
            )

            if h == 0:
                observed_telescope = untwisted_rows.bit_count() & 1
                all_local = untwisted_rows == 0
                holonomy_sector = parity == original_holonomy
                original["telescope_failures"] += observed_telescope != parity
                original["local_satisfied_states"] += all_local
                original["local_satisfied_even_token_states"] += (
                    all_local and parity == 0
                )
                original["local_satisfied_token_holonomy_matches"] += (
                    all_local and holonomy_sector
                )
                original["token_parity_equals_holonomy_states"] += (
                    holonomy_sector
                )
                original["exact_sector_separation_failures"] += (
                    all_local != holonomy_sector
                )
        sectors.append(counts)

    expected_sector_templates = FROZEN["FROZEN_AMENDED_H_SECTOR_CENSUS"]
    observed_sector_census = tuple(
        _shape_from_template(sectors[h], expected_sector_templates[h])
        for h in (0, 1)
    )
    observed_original_census = _shape_from_template(
        original, FROZEN["FROZEN_EXHAUSTIVE_RESULT_CENSUS"]
    )
    enumeration = (
        ("ring_stations", width),
        ("rail_bits", 2 * width),
        ("rail_states", total),
        ("method", "exhaustive_all_2^(2*11)_rail_states"),
    )
    symbolic = {
        ring: _symbolic_twist_identity(ring) for ring in (11, 35, 130)
    }
    sectors_match = observed_sector_census == expected_sector_templates
    original_matches = (
        observed_original_census == FROZEN["FROZEN_EXHAUSTIVE_RESULT_CENSUS"]
    )
    enumeration_matches = enumeration == FROZEN["FROZEN_ENUMERATION_CENSUS"]
    passed = (
        sectors_match
        and original_matches
        and enumeration_matches
        and all(symbolic.values())
        and all(row["twist_telescope_failures"] == 0 for row in sectors)
        and all(row["fixed_ref_satisfied_states"] == 2048 for row in sectors)
        and all(row["fixed_ref_matching_states"] == 2048 for row in sectors)
        and all(row["compression_a_failures"] == 0 for row in sectors)
        and all(row["projected_satisfied_states"] == 2097152 for row in sectors)
        and all(
            row["projected_exact_separation_failures"] == 0 for row in sectors
        )
    )
    return passed, {
        "enumeration": dict(enumeration),
        "fixed_reference_mask": fixed_refs,
        "original_refutation_census": original,
        "original_census_matches_frozen": original_matches,
        "h_sectors": sectors,
        "h_sector_censuses_match_frozen": sectors_match,
        "symbolic_identity_by_ring": symbolic,
    }


def _radius_one_sites(center: int, width: int) -> tuple[int, ...]:
    return tuple(
        sorted({(center - 1) % width, center, (center + 1) % width})
    )


def _ring_distance(left: int, right: int, width: int) -> int:
    return min((left - right) % width, (right - left) % width)


def _window_witness(center: int, width: int) -> dict[str, object]:
    sites = _radius_one_sites(center, width)
    edge = _first_edge(width)
    if set(edge) <= set(sites):
        raise ValueError(("window includes marked edge", center, sites))
    window_mask = sum(1 << site for site in sites)
    for token_site in range(width):
        if token_site in edge or _ring_distance(token_site, center, width) <= 1:
            continue
        a = 1 << token_site
        refs, closure = _reference_extension(a, 0, 1, width)
        if closure:
            continue
        for candidate in (refs, refs ^ _mask(width)):
            differences = (a | candidate) & window_mask
            if differences == 0 and _row_mask(a, 0, candidate, 1, width) == 0:
                return {
                    "center": center,
                    "sites": sites,
                    "token_flip_site": token_site,
                    "token_flip_distance": _ring_distance(
                        token_site, center, width
                    ),
                    "A_mask": a,
                    "B_mask": 0,
                    "refs_mask": candidate,
                    "h": 1,
                    "rail_ref_bits_observed": 3 * len(sites),
                    "observed_bit_differences": differences.bit_count(),
                }
    raise AssertionError(("no independent radius-one witness", center))


def witness_recount() -> tuple[bool, dict[str, object]]:
    width = 11
    edge = _first_edge(width)
    windows = tuple(
        _window_witness(center, width)
        for center in range(width)
        if not set(edge) <= set(_radius_one_sites(center, width))
    )
    representative = next(row for row in windows if row["center"] == 8)
    marked_pair = (
        (
            ("ring_stations", width),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", 0),
            ("h", 0),
        ),
        (
            ("ring_stations", width),
            ("A_mask", representative["A_mask"]),
            ("B_mask", representative["B_mask"]),
            ("refs_mask", representative["refs_mask"]),
            ("h", representative["h"]),
        ),
    )
    marked_rows = []
    for item in marked_pair:
        state = dict(item)
        marked_rows.append(
            _row_mask(
                state["A_mask"],
                state["B_mask"],
                state["refs_mask"],
                state["h"],
                width,
            )
        )

    window_census = (
        ("ring_stations", width),
        ("marked_edge", edge),
        ("radius", 1),
        ("windows_excluding_marked_edge", len(windows)),
        (
            "windows_with_indistinguishable_witness",
            sum(row["observed_bit_differences"] == 0 for row in windows),
        ),
        (
            "rail_ref_bits_per_window",
            min(row["rail_ref_bits_observed"] for row in windows),
        ),
        (
            "maximum_observed_bit_differences",
            max(row["observed_bit_differences"] for row in windows),
        ),
        (
            "minimum_token_flip_distance",
            min(row["token_flip_distance"] for row in windows),
        ),
        ("representative_window_center", representative["center"]),
        ("representative_window_sites", representative["sites"]),
    )

    original_pair = (
        (
            ("ring_stations", width),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", 0),
        ),
        (
            ("ring_stations", width),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", _mask(width)),
        ),
    )
    original_rows_satisfied = all(
        _row_mask(
            dict(item)["A_mask"],
            dict(item)["B_mask"],
            dict(item)["refs_mask"],
            0,
            width,
        )
        == 0
        for item in original_pair
    )
    marked_match = marked_pair == FROZEN["FROZEN_MARKED_EDGE_WITNESS_PAIR"]
    original_match = original_pair == FROZEN["FROZEN_WITNESS_PAIR"]
    census_match = window_census == FROZEN["FROZEN_RADIUS1_WINDOW_CENSUS"]
    all_windows = (
        len(windows) == 9
        and all(row["observed_bit_differences"] == 0 for row in windows)
        and all(row["token_flip_distance"] > 1 for row in windows)
    )
    h_differs = dict(marked_pair[0])["h"] != dict(marked_pair[1])["h"]
    passed = (
        marked_match
        and original_match
        and census_match
        and all(row == 0 for row in marked_rows)
        and original_rows_satisfied
        and all_windows
        and h_differs
    )
    return passed, {
        "marked_pair": marked_pair,
        "marked_pair_matches_frozen": marked_match,
        "marked_pair_row_masks": marked_rows,
        "h_differs": h_differs,
        "original_pair_matches_frozen": original_match,
        "original_pair_rows_satisfied": original_rows_satisfied,
        "window_census": dict(window_census),
        "window_census_matches_frozen": census_match,
        "indistinguishable_windows": f"{sum(row['observed_bit_differences'] == 0 for row in windows)}/{len(windows)}",
    }


def _r1(a: int, b: int, width: int) -> tuple[int, int]:
    del width
    return b, a


def _r2(a: int, b: int, width: int) -> tuple[int, int]:
    return _previous_source_bits(b, width), _next_source_bits(a, width)


def _r(a: int, b: int, width: int) -> tuple[int, int]:
    middle_a, middle_b = _r1(a, b, width)
    return _r2(middle_a, middle_b, width)


def _one_row(a: int, b: int, refs: int, site: int, width: int) -> int:
    return (
        ((a >> site) & 1)
        ^ ((b >> site) & 1)
        ^ ((refs >> site) & 1)
        ^ ((refs >> ((site + 1) % width)) & 1)
    )


def _law_value(
    a: int,
    b: int,
    refs: int,
    site: int,
    width: int,
    law: tuple[tuple[str, int], ...],
) -> int:
    banks = {"A": a, "B": b, "ref": refs}
    value = 0
    for bank, offset in law:
        value ^= (banks[bank] >> ((site + offset) % width)) & 1
    return value


def _basis_law_failures(
    layer: Callable[[int, int, int], tuple[int, int]],
    width: int,
    law: tuple[tuple[str, int], ...],
) -> int:
    failures = 0
    for kind in ("A", "B", "ref"):
        for source in range(width):
            a = (1 << source) if kind == "A" else 0
            b = (1 << source) if kind == "B" else 0
            refs = (1 << source) if kind == "ref" else 0
            after_a, after_b = layer(a, b, width)
            for site in range(width):
                failures += _one_row(
                    after_a, after_b, refs, site, width
                ) != _law_value(a, b, refs, site, width, law)
    return failures


def _derived_offsets(
    layer: Callable[[int, int, int], tuple[int, int]], width: int
) -> frozenset[tuple[str, int]]:
    influences: set[tuple[str, int]] = set()
    for kind in ("A", "B", "ref"):
        for source in range(width):
            a = (1 << source) if kind == "A" else 0
            b = (1 << source) if kind == "B" else 0
            refs = (1 << source) if kind == "ref" else 0
            after_a, after_b = layer(a, b, width)
            if _one_row(after_a, after_b, refs, 0, width):
                signed = source if source <= width // 2 else source - width
                influences.add((kind, signed))
    return frozenset(influences)


def _to_tuple(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> site) & 1 for site in range(width))


def _from_tuple(bits: tuple[int, ...]) -> int:
    return sum(bit << site for site, bit in enumerate(bits))


def _k_cross_check(width: int) -> tuple[int, int]:
    program = tuple(("identity", 0, ()) for _ in range(width))
    cases = [
        (1 << site, 0) for site in range(width)
    ] + [
        (0, 1 << site) for site in range(width)
    ]
    mask = _mask(width)
    cases.extend(
        (
            (0, 0),
            (mask, 0),
            (0, mask),
            (mask, mask),
            (mask // 3, mask // 5),
            (
                int.from_bytes(sha256(f"R-A-{width}".encode()).digest(), "big")
                & mask,
                int.from_bytes(sha256(f"R-B-{width}".encode()).digest(), "big")
                & mask,
            ),
        )
    )
    failures = 0
    invariant_failures = 0
    for a, b in cases:
        _data, observed_a, observed_b = K.apply_controller_step(
            (),
            program,
            _to_tuple(a, width),
            _to_tuple(b, width),
        )
        expected_a, expected_b = _r(a, b, width)
        failures += (
            _from_tuple(observed_a) != expected_a
            or _from_tuple(observed_b) != expected_b
        )
        for h in (0, 1):
            invariant_failures += (
                (_token_parity(a, b) ^ h)
                != (_token_parity(expected_a, expected_b) ^ h)
            )
    return failures, invariant_failures


def r_law_recount() -> tuple[bool, dict[str, object]]:
    rings = tuple(row[2] for row in FROZEN["FROZEN_PROGRAM_CENSUS"])
    layers = (
        ("R1", _r1, FROZEN["FROZEN_R1_PULLBACK"]),
        ("R2", _r2, FROZEN["FROZEN_R2_PULLBACK"]),
        ("R", _r, FROZEN["FROZEN_R_PULLBACK"]),
    )
    derived = {
        name: tuple(sorted(_derived_offsets(layer, 11)))
        for name, layer, _law in layers
    }
    law_failures = {
        name: {
            width: _basis_law_failures(layer, width, law) for width in rings
        }
        for name, layer, law in layers
    }
    derived_match = all(
        frozenset(derived[name]) == frozenset(law)
        for name, _layer, law in layers
    )
    k_results = {width: _k_cross_check(width) for width in rings}

    permutation_proofs = {}
    for width in rings:
        outputs = set()
        single_output = True
        for rail in ("A", "B"):
            for source in range(width):
                a = 1 << source if rail == "A" else 0
                b = 1 << source if rail == "B" else 0
                out_a, out_b = _r(a, b, width)
                if out_a.bit_count() + out_b.bit_count() != 1:
                    single_output = False
                if out_a:
                    outputs.add(("A", (out_a & -out_a).bit_length() - 1))
                if out_b:
                    outputs.add(("B", (out_b & -out_b).bit_length() - 1))
        permutation_proofs[width] = single_output and len(outputs) == 2 * width

    counter = dict(FROZEN["FROZEN_R_COUNTEREXAMPLE"])
    after_a, after_b = _r(
        counter["A_before_mask"],
        counter["B_before_mask"],
        counter["ring_stations"],
    )
    observed_counterexample = (
        ("ring_stations", counter["ring_stations"]),
        ("A_before_mask", counter["A_before_mask"]),
        ("B_before_mask", counter["B_before_mask"]),
        ("refs_mask", counter["refs_mask"]),
        (
            "syndrome_before_mask",
            _row_mask(
                counter["A_before_mask"],
                counter["B_before_mask"],
                counter["refs_mask"],
                0,
                counter["ring_stations"],
            ),
        ),
        (
            "syndrome_after_mask",
            _row_mask(
                after_a,
                after_b,
                counter["refs_mask"],
                0,
                counter["ring_stations"],
            ),
        ),
    )
    counter_matches = (
        observed_counterexample == FROZEN["FROZEN_R_COUNTEREXAMPLE"]
    )
    passed = (
        derived_match
        and all(
            failures == 0
            for by_ring in law_failures.values()
            for failures in by_ring.values()
        )
        and all(result == (0, 0) for result in k_results.values())
        and all(permutation_proofs.values())
        and counter_matches
    )
    return passed, {
        "rings": rings,
        "derived_pullbacks": derived,
        "derived_match_frozen": derived_match,
        "basis_law_failures": law_failures,
        "K_cross_check_and_invariant_failures": k_results,
        "global_rail_permutation_proof": permutation_proofs,
        "token_parity_xor_static_h_invariant": all(
            result[1] == 0 for result in k_results.values()
        )
        and all(permutation_proofs.values()),
        "frozen_counterexample_reproduced": counter_matches,
    }


def _rooted_at_k(node: ast.AST) -> bool:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return isinstance(node, ast.Name) and node.id == "K"


def discipline() -> tuple[bool, dict[str, object]]:
    """Audit literal discipline and absence of writes through the K alias."""

    primary_tree = ast.parse(
        PRIMARY_PATH.read_text(encoding="utf-8"), filename=str(PRIMARY_PATH)
    )
    primary_nodes = _assignment_nodes(primary_tree)
    k_writes = []
    for node in ast.walk(primary_tree):
        if isinstance(node, (ast.Attribute, ast.Subscript)):
            if isinstance(node.ctx, (ast.Store, ast.Del)) and _rooted_at_k(node):
                k_writes.append((node.lineno, ast.unparse(node)))
        elif isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Name)
                and node.func.id in ("setattr", "delattr")
                and node.args
                and _rooted_at_k(node.args[0])
            ):
                k_writes.append((node.lineno, ast.unparse(node)))

    frozen_literal_failures = {}
    for name, node in primary_nodes.items():
        if name.startswith("FROZEN_"):
            try:
                _literal(node)
            except Exception as exc:
                frozen_literal_failures[name] = f"{type(exc).__name__}: {exc}"

    checker_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    checker_nodes = _assignment_nodes(checker_tree)
    checker_audit = _literal(checker_nodes["AUDIT_INPUT_PATHS"])
    checker_blocklist = _literal(checker_nodes["PRIMARY_IMPORT_BLOCKLIST"])
    direct_primary_imports = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            direct_primary_imports.extend(
                alias.name
                for alias in node.names
                if alias.name in PRIMARY_IMPORT_BLOCKLIST
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module in PRIMARY_IMPORT_BLOCKLIST
        ):
            direct_primary_imports.append(node.module)

    expected_inputs = (
        "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    )
    primary_loaded = any(
        name in sys.modules for name in PRIMARY_IMPORT_BLOCKLIST
    )
    passed = (
        not k_writes
        and not frozen_literal_failures
        and all(name in primary_nodes for name in REQUIRED_FROZEN_NAMES)
        and checker_audit == expected_inputs
        and checker_blocklist == PRIMARY_IMPORT_BLOCKLIST
        and not direct_primary_imports
        and not primary_loaded
    )
    return passed, {
        "primary_K_attribute_writes": k_writes,
        "primary_frozen_literal_failures": frozen_literal_failures,
        "primary_frozen_literal_count": sum(
            name.startswith("FROZEN_") for name in primary_nodes
        ),
        "checker_AUDIT_tuple": checker_audit,
        "checker_blocklist": checker_blocklist,
        "checker_direct_primary_imports": direct_primary_imports,
        "primary_present_in_sys_modules": primary_loaded,
    }


CERTIFICATES = (
    ("extraction", extraction),
    ("coboundary_refutation_recount", coboundary_refutation_recount),
    ("twist_theorem_recount", twist_theorem_recount),
    ("witness_recount", witness_recount),
    ("r_law_recount", r_law_recount),
    ("discipline", discipline),
)


def main() -> int:
    started = perf_counter()
    results: dict[str, bool] = {}
    details: dict[str, object] = {}
    for name, certificate in CERTIFICATES:
        try:
            passed, detail = certificate()
        except Exception as exc:
            passed = False
            detail = {
                "honest_exception": type(exc).__name__,
                "message": str(exc),
            }
        results[name] = bool(passed)
        details[name] = detail
        print(f"{'PASS' if passed else 'FAIL'} {name} :: {_compact(detail)}")

    runtime = perf_counter() - started
    within_timeout = runtime <= AUDIT_TIMEOUT_SEC
    all_pass = all(results.values()) and within_timeout
    passed_count = sum(results.values())
    summary = {
        "audit": "cycle728_holonomy_independent_check",
        "audit_inputs": AUDIT_INPUT_PATHS,
        "blocklist": PRIMARY_IMPORT_BLOCKLIST,
        "certificates": f"{passed_count}/{len(CERTIFICATES)}",
        "failed": tuple(name for name, passed in results.items() if not passed),
        "pass": all_pass,
        "runtime_seconds": round(runtime, 6),
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
        "within_timeout": within_timeout,
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    print(
        "CYCLE728_HOLONOMY_INDEPENDENT_CHECK_PASS"
        if all_pass
        else "CYCLE728_HOLONOMY_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
