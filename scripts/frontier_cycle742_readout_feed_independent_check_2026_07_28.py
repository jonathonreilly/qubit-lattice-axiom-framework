#!/usr/bin/env python3
"""Independent bounded checker for the Cycle 742 archive readout feed."""
from __future__ import annotations

import ast
import json
import sys
from fractions import Fraction
from functools import cache
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693
import frontier_cycle741_physical_bank_renewal_2026_07_28 as N741


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/ARCHIVE_RECORD_READOUT_FEED_CYCLE742_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
BLOCKLIST = (
    "scripts/frontier_cycle742_archive_record_readout_feed_2026_07_28.py",
)

STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_PERMANENCE_WALL = (
    "byte preservation is proven, permanence is NOT; the locking mechanism "
    "remains the named W5 gap"
)
ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / BLOCKLIST[0]


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _primary_source_tree() -> tuple[str, ast.Module]:
    source = PRIMARY_PATH.read_text(encoding="utf-8")
    return source, ast.parse(source, filename=str(PRIMARY_PATH))


def _top_assignment(tree: ast.Module, name: str) -> ast.AST:
    values: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            values.append(node.value)
    if len(values) != 1:
        raise AssertionError(("top-level assignment census", name, len(values)))
    return values[0]


def _literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(_top_assignment(tree, name))


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def _dotted_name(node: ast.AST) -> str | None:
    parts: list[str] = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    parts.append(node.id)
    return ".".join(reversed(parts))


def _named_dict(function: ast.FunctionDef, name: str) -> ast.Dict:
    matches: list[ast.Dict] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            continue
        if isinstance(node.value, ast.Dict):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("dict assignment census", name, len(matches)))
    return matches[0]


def _dict_entry(node: ast.Dict, key: str) -> ast.AST:
    matches = tuple(
        value
        for raw_key, value in zip(node.keys, node.values)
        if isinstance(raw_key, ast.Constant) and raw_key.value == key
    )
    if len(matches) != 1:
        raise AssertionError(("dict key census", key, len(matches)))
    return matches[0]


def _check_condition(function: ast.FunctionDef, label: str) -> ast.AST:
    matches = tuple(
        node.args[1]
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "check"
        and len(node.args) >= 2
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == label
    )
    if len(matches) != 1:
        raise AssertionError(("check call census", label, len(matches)))
    return matches[0]


def _has_literal_comparison(
    node: ast.AST,
    left_text: str,
    operator_type: type[ast.cmpop],
    expected: object,
) -> bool:
    for comparison in ast.walk(node):
        if (
            isinstance(comparison, ast.Compare)
            and len(comparison.ops) == 1
            and isinstance(comparison.ops[0], operator_type)
            and len(comparison.comparators) == 1
            and ast.unparse(comparison.left) == left_text
            and isinstance(comparison.comparators[0], ast.Constant)
            and comparison.comparators[0].value == expected
        ):
            return True
    return False


def extraction() -> dict[str, object]:
    """Extract Cycle 742's declarations without importing or executing it."""
    _source, tree = _primary_source_tree()
    audit_node = _top_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_paths = ast.literal_eval(audit_node)
    audit_literal_tuple = isinstance(audit_node, ast.Tuple) and all(
        isinstance(item, ast.Constant) and isinstance(item.value, str)
        for item in audit_node.elts
    )

    embed_function = _function(tree, "embed_archive")
    record_calls = tuple(
        node
        for node in ast.walk(embed_function)
        if isinstance(node, ast.Call)
        and _dotted_name(node.func) == "R693.Record"
    )
    if len(record_calls) != 1:
        raise AssertionError(("R693.Record constructor census", len(record_calls)))
    record_keywords = {
        keyword.arg: keyword.value
        for keyword in record_calls[0].keywords
        if keyword.arg is not None
    }
    content_node = record_keywords.get("content")
    site_node = record_keywords.get("site")
    content_shape = (
        isinstance(site_node, ast.Name)
        and site_node.id == "site"
        and isinstance(content_node, ast.Tuple)
        and len(content_node.elts) == 4
        and all(isinstance(item, ast.Call) for item in content_node.elts)
        and all(
            _dotted_name(item.func) == "R693.F"
            for item in content_node.elts
            if isinstance(item, ast.Call)
        )
        and isinstance(content_node.elts[0], ast.Call)
        and len(content_node.elts[0].args) == 1
        and isinstance(content_node.elts[0].args[0], ast.Name)
        and content_node.elts[0].args[0].id == "bit"
        and all(
            isinstance(item, ast.Call)
            and len(item.args) == 1
            and isinstance(item.args[0], ast.Constant)
            and item.args[0].value == 0
            for item in content_node.elts[1:]
        )
    )

    sites_function = _function(tree, "archive_sites")
    site_tuples = tuple(
        node
        for node in ast.walk(sites_function)
        if isinstance(node, ast.Tuple)
        and len(node.elts) == 3
        and any(
            isinstance(part, ast.Constant) and part.value == 11
            for part in ast.walk(node)
        )
    )
    site_schema_3d = len(site_tuples) == 1

    main_function = _function(tree, "main")
    embedding_dict = _named_dict(main_function, "embedding")
    content_scalars = ast.literal_eval(
        _dict_entry(embedding_dict, "record_content_scalars")
    )
    site_dimension = ast.literal_eval(
        _dict_entry(embedding_dict, "record_site_dimension")
    )
    zero_fitted = ast.literal_eval(
        _dict_entry(embedding_dict, "zero_fitted_parameters")
    )

    embedding_condition = _check_condition(
        main_function, "B_embedding_exact_909_site_schema_roundtrip"
    )
    declared_sizes = (
        _has_literal_comparison(
            embedding_condition, "N741.ARCHIVE_SLOTS", ast.Eq, 3
        )
        and _has_literal_comparison(
            embedding_condition, "N741.RECORD_WIDTH", ast.Eq, 303
        )
        and _has_literal_comparison(
            embedding_condition, "N741.ARCHIVE_WIDTH", ast.Eq, 909
        )
    )

    reproduction_condition = _check_condition(
        main_function,
        "C_readout_reproduces_four_archived_payloads_all_three_generations",
    )
    declared_three_generations = _has_literal_comparison(
        reproduction_condition, "len(generation_rows)", ast.Eq, 3
    )
    declared_four_payloads = _has_literal_comparison(
        reproduction_condition, "row['packets_read']", ast.Eq, 4
    )
    packet_match_all_call = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "all"
        and len(node.args) == 1
        and ast.unparse(node.args[0]) == "row['packet_byte_matches']"
        for node in ast.walk(reproduction_condition)
    )
    reproduction_census = (
        12
        if declared_three_generations
        and declared_four_payloads
        and packet_match_all_call
        else 0
    )

    boundary_dict = _named_dict(main_function, "boundary")
    permanence_value = ast.literal_eval(
        _dict_entry(boundary_dict, "record_permanence_claimed")
    )
    junction_value_node = _dict_entry(
        boundary_dict, "junction_feed_achieved"
    )
    boundary_condition = _check_condition(
        main_function, "F_honest_boundary_keys"
    )
    junction_required_true = _has_literal_comparison(
        boundary_condition,
        "boundary['junction_feed_achieved']",
        ast.Is,
        True,
    )
    permanence_required_false = _has_literal_comparison(
        boundary_condition,
        "boundary['record_permanence_claimed']",
        ast.Is,
        False,
    )
    permanence_wall = _literal_assignment(tree, "PERMANENCE_WALL")
    r693_anchor = _literal_assignment(tree, "R693_SHA256")

    passed = (
        audit_literal_tuple
        and audit_paths == AUDIT_INPUT_PATHS
        and content_shape
        and site_schema_3d
        and content_scalars == 4
        and site_dimension == 3
        and zero_fitted is True
        and declared_sizes
        and reproduction_census == 12
        and permanence_value is False
        and isinstance(junction_value_node, ast.Call)
        and junction_required_true
        and permanence_required_false
        and permanence_wall == EXPECTED_PERMANENCE_WALL
        and isinstance(r693_anchor, str)
        and len(r693_anchor) == 64
    )
    return {
        "pass": passed,
        "audit_tuple_literal": audit_literal_tuple,
        "audit_input_paths": audit_paths,
        "embedding": {
            "archive_records": 909,
            "archive_slots": 3,
            "record_width": 303,
            "record_site_dimension": site_dimension,
            "record_content": "(Fraction(bit),0,0,0)",
            "record_content_scalars": content_scalars,
            "zero_fitted_parameters": zero_fitted,
        },
        "reproduction_census": {
            "declared": reproduction_census,
            "expected": 12,
        },
        "boundary": {
            "junction_feed_achieved": junction_required_true,
            "record_permanence_claimed": permanence_value,
            "permanence_boundary": permanence_wall,
        },
        "r693_anchor_sha256": r693_anchor,
    }


def _own_archive_sites() -> tuple[tuple[int, int, int], ...]:
    wire_sites = tuple(
        N741.K.M.R12.full_wire_layout()["wire_sites"]
    )
    return tuple(
        (
            wire_sites[wire][0],
            wire_sites[wire][1] + 11 * (slot + 1),
            wire_sites[wire][2],
        )
        for slot in range(N741.ARCHIVE_SLOTS)
        for wire in N741.RECORD_WIRES
    )


def _flatten_archive(
    archives: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    return tuple(bit for slot in archives for bit in slot)


def _split_archive(
    flat: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    if len(flat) != N741.ARCHIVE_WIDTH:
        raise ValueError(("archive width", len(flat)))
    return tuple(
        flat[
            slot * N741.RECORD_WIDTH:
            (slot + 1) * N741.RECORD_WIDTH
        ]
        for slot in range(N741.ARCHIVE_SLOTS)
    )


def _own_embed(
    archives: tuple[tuple[int, ...], ...],
) -> tuple[R693.Record, ...]:
    if len(archives) != N741.ARCHIVE_SLOTS:
        raise ValueError(("archive slots", len(archives)))
    if any(len(slot) != N741.RECORD_WIDTH for slot in archives):
        raise ValueError("archive slot width")
    flat = _flatten_archive(archives)
    if any(bit not in (0, 1) for bit in flat):
        raise ValueError("archive is not binary")
    zero = Fraction(0)
    return tuple(
        R693.Record(
            site=site,
            content=(Fraction(bit), zero, zero, zero),
        )
        for site, bit in zip(_own_archive_sites(), flat)
    )


def _own_extract(
    records: tuple[R693.Record, ...],
) -> tuple[tuple[int, ...], ...]:
    sites = _own_archive_sites()
    if len(records) != len(sites):
        raise ValueError(("record census", len(records)))
    zero = Fraction(0)
    bits: list[int] = []
    for expected_site, record in zip(sites, records):
        if (
            not isinstance(record.site, tuple)
            or len(record.site) != 3
            or record.site != expected_site
        ):
            raise ValueError(("record site", expected_site, record.site))
        if (
            not isinstance(record.content, tuple)
            or len(record.content) != 4
            or record.content[1:] != (zero, zero, zero)
            or record.content[0] not in (zero, Fraction(1))
        ):
            raise ValueError(("record content", record.content))
        bits.append(int(record.content[0]))
    return _split_archive(tuple(bits))


def _own_record_image(data: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(data[wire] for wire in N741.RECORD_WIRES)


def _own_payloads(
    banks: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(bank[wire] for wire in N741.K.A.cell(cell)["payload"])
        for bank in banks
        for cell in range(N741.K.A.BANK_CELLS)
    )


@cache
def _generation_fixtures() -> tuple[dict[str, object], ...]:
    word = N741.renewal_word()
    data = N741.GENESIS_STATE
    archives = (N741.ZERO_ARCHIVE_SLOT,) * N741.ARCHIVE_SLOTS
    rows: list[dict[str, object]] = []
    for generation, directions in enumerate(
        N741.GENERATION_DIRECTIONS, start=1
    ):
        exhausted, fill = N741.fill_generation(data, directions)
        banks, _links = N741.K.M.unpack_state(
            exhausted, N741.FIXTURE_BANKS
        )
        source_payloads = _own_payloads(banks)
        image = _own_record_image(exhausted)
        expected_archives = (image,) + archives[:-1]
        combined = N741.pack_combined(exhausted, archives)
        renewed = N741.K.A.apply_semantic(combined, word)
        data, archives = N741.split_combined(renewed)
        rows.append({
            "generation": generation,
            "archives": archives,
            "source_payloads": source_payloads,
            "n741_run_exact": (
                fill["violation_count"] == 0
                and fill["packet_count"] == N741.CAPACITY_ORBITS
                and data == N741.GENESIS_STATE
                and archives == expected_archives
                and len(source_payloads) == 4
            ),
        })
    return tuple(rows)


def embedding_roundtrip_recount() -> dict[str, object]:
    """Round-trip N741 generation 1 through an independently coded schema."""
    first = _generation_fixtures()[0]
    archives = first["archives"]
    if not isinstance(archives, tuple):
        raise TypeError("generation archive type")
    records = _own_embed(archives)
    recovered = _own_extract(records)
    sites = tuple(record.site for record in records)
    original_bytes = bytes(_flatten_archive(archives))
    recovered_bytes = bytes(_flatten_archive(recovered))
    operating_sites = set(
        N741.K.M.R12.full_wire_layout()["assigned_sites"]
    )
    passed = (
        first["n741_run_exact"] is True
        and len(records) == N741.ARCHIVE_WIDTH == 909
        and len(sites) == len(set(sites)) == 909
        and all(len(site) == 3 for site in sites)
        and not (set(sites) & operating_sites)
        and recovered == archives
        and recovered_bytes == original_bytes
    )
    return {
        "pass": passed,
        "generation": 1,
        "records_embedded": len(records),
        "unique_3d_sites": len(set(sites)),
        "byte_count": len(original_bytes),
        "byte_identical": recovered_bytes == original_bytes,
        "archive_sha256": sha256(original_bytes).hexdigest(),
        "n741_run_exact": first["n741_run_exact"],
    }


def _readout_bits(
    records: tuple[R693.Record, ...],
) -> tuple[int, ...]:
    values = tuple(
        R693.record_readout((record,)) for record in records
    )
    if any(value not in (Fraction(0), Fraction(1)) for value in values):
        raise ValueError("R693 readout left the declared bit image")
    return tuple(int(value) for value in values)


def readout_recount() -> dict[str, object]:
    """Recount all archived packet bytes through R693's public readout."""
    _source, tree = _primary_source_tree()
    pinned_sha = _literal_assignment(tree, "R693_SHA256")
    r693_path = Path(R693.__file__).resolve()
    sha_before = _sha256(r693_path)
    generation_rows: list[dict[str, object]] = []
    matches_total = 0
    comparisons_total = 0
    all_exact = True

    for fixture in _generation_fixtures():
        archives = fixture["archives"]
        expected_payloads = fixture["source_payloads"]
        if not isinstance(archives, tuple):
            raise TypeError("generation archive type")
        if not isinstance(expected_payloads, tuple):
            raise TypeError("source payload type")
        records = _own_embed(archives)
        flat = _readout_bits(records)
        read_archives = _split_archive(flat)
        restored = list(N741.GENESIS_STATE)
        for wire, bit in zip(
            N741.RECORD_WIRES, read_archives[0]
        ):
            restored[wire] = bit
        read_banks, _read_links = N741.K.M.unpack_state(
            tuple(restored), N741.FIXTURE_BANKS
        )
        observed_payloads = _own_payloads(read_banks)
        matches = tuple(
            bytes(observed) == bytes(expected)
            for observed, expected in zip(
                observed_payloads, expected_payloads
            )
        )
        comparisons_total += len(matches)
        matches_total += sum(matches)
        aggregate_exact = (
            R693.record_readout(records)
            == sum(
                (R693.record_readout((record,)) for record in records),
                Fraction(0),
            )
        )
        row_exact = (
            fixture["n741_run_exact"] is True
            and len(records) == 909
            and read_archives == archives
            and len(observed_payloads) == len(expected_payloads) == 4
            and len(matches) == 4
            and all(matches)
            and aggregate_exact
        )
        all_exact = all_exact and row_exact
        generation_rows.append({
            "generation": fixture["generation"],
            "records_read": len(records),
            "payload_comparisons": len(matches),
            "payload_matches": sum(matches),
            "aggregate_exact": aggregate_exact,
            "exact": row_exact,
        })

    sha_after = _sha256(r693_path)
    anchor_unchanged = (
        isinstance(pinned_sha, str)
        and sha_before == pinned_sha
        and sha_after == sha_before
    )
    passed = (
        len(generation_rows) == 3
        and comparisons_total == 12
        and matches_total == 12
        and all_exact
        and anchor_unchanged
    )
    return {
        "pass": passed,
        "generation_rows": tuple(generation_rows),
        "payload_reproduction": f"{matches_total}/{comparisons_total}",
        "r693_public_entry_point": "record_readout",
        "r693_sha256_before": sha_before,
        "r693_sha256_after": sha_after,
        "r693_pinned_sha256": pinned_sha,
        "r693_anchor_unchanged": anchor_unchanged,
    }


def _root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _target_leaves(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(
            leaf for item in node.elts for leaf in _target_leaves(item)
        )
    return (node,)


def _assignment_leaves(tree: ast.AST) -> tuple[ast.AST, ...]:
    leaves: list[ast.AST] = []
    for node in ast.walk(tree):
        raw_targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            raw_targets = tuple(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            raw_targets = (node.target,)
        elif isinstance(node, ast.Delete):
            raw_targets = tuple(node.targets)
        for target in raw_targets:
            leaves.extend(_target_leaves(target))
    return tuple(leaves)


def _no_write_audit(tree: ast.Module) -> dict[str, object]:
    module_attribute_targets = tuple(
        ast.unparse(target)
        for target in _assignment_leaves(tree)
        if isinstance(target, (ast.Attribute, ast.Subscript))
        and _root_name(target) in {"R693", "N741"}
    )
    module_mutators = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"setattr", "delattr"}
        and node.args
        and _root_name(node.args[0]) in {"R693", "N741"}
    )
    filesystem_mutator_names = {
        "chmod",
        "mkdir",
        "rename",
        "replace",
        "rmdir",
        "touch",
        "unlink",
        "write_bytes",
        "write_text",
    }
    filesystem_mutators = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in filesystem_mutator_names
    )
    write_mode_opens: list[str] = []
    for node in ast.walk(tree):
        if (
            not isinstance(node, ast.Call)
            or _dotted_name(node.func) not in {"open", "Path.open"}
        ):
            continue
        mode_nodes = tuple(
            keyword.value for keyword in node.keywords
            if keyword.arg == "mode"
        )
        if len(node.args) >= 2:
            mode_nodes += (node.args[1],)
        modes = tuple(
            item.value
            for item in mode_nodes
            if isinstance(item, ast.Constant)
            and isinstance(item.value, str)
        )
        if any(any(flag in mode for flag in "wax+") for mode in modes):
            write_mode_opens.append(ast.unparse(node))
    passed = (
        not module_attribute_targets
        and not module_mutators
        and not filesystem_mutators
        and not write_mode_opens
    )
    return {
        "pass": passed,
        "R693_N741_attribute_targets": module_attribute_targets,
        "R693_N741_setattr_delattr": module_mutators,
        "filesystem_mutator_calls": filesystem_mutators,
        "write_mode_open_calls": tuple(write_mode_opens),
    }


def controls_recount() -> dict[str, object]:
    """Exercise bit corruption, empty inputs, and the primary's no-write AST."""
    final_fixture = _generation_fixtures()[-1]
    final_archives = final_fixture["archives"]
    if not isinstance(final_archives, tuple):
        raise TypeError("final archive type")
    records = _own_embed(final_archives)
    baseline = _readout_bits(records)
    corrupted_flat = list(_flatten_archive(final_archives))
    corruption_index = 0
    corrupted_flat[corruption_index] ^= 1
    corrupted_archives = _split_archive(tuple(corrupted_flat))
    corrupted_records = _own_embed(corrupted_archives)
    corrupted = _readout_bits(corrupted_records)
    changed_indices = tuple(
        index
        for index, (left, right) in enumerate(
            zip(baseline, corrupted)
        )
        if left != right
    )
    aggregate_changed = (
        R693.record_readout(records)
        != R693.record_readout(corrupted_records)
    )

    blank_archives = (
        N741.ZERO_ARCHIVE_SLOT,
    ) * N741.ARCHIVE_SLOTS
    blank_records = _own_embed(blank_archives)
    blank_bits = _readout_bits(blank_records)
    blank_archive_empty = (
        len(blank_records) == 909
        and not any(blank_bits)
        and R693.record_readout(blank_records) == Fraction(0)
    )
    absent_archive_empty = R693.record_readout(()) == Fraction(0)

    _source, primary_tree = _primary_source_tree()
    no_write = _no_write_audit(primary_tree)
    passed = (
        changed_indices == (corruption_index,)
        and aggregate_changed
        and blank_archive_empty
        and absent_archive_empty
        and no_write["pass"] is True
    )
    return {
        "pass": passed,
        "corruption_index": corruption_index,
        "changed_indices": changed_indices,
        "aggregate_readout_changed": aggregate_changed,
        "blank_909_record_archive_reads_zero": blank_archive_empty,
        "absent_archive_reads_zero": absent_archive_empty,
        "primary_no_write_ast": no_write,
    }


def _subscript_key(node: ast.AST) -> object:
    if not isinstance(node, ast.Subscript):
        return None
    try:
        return ast.literal_eval(node.slice)
    except (ValueError, TypeError, SyntaxError):
        return None


def discipline() -> dict[str, object]:
    """Audit this checker and the primary's exact permanence boundary."""
    source, primary_tree = _primary_source_tree()
    self_source = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=__file__)

    self_attribute_targets = tuple(
        ast.unparse(target)
        for target in _assignment_leaves(self_tree)
        if isinstance(target, ast.Attribute)
    )
    self_attribute_mutators = tuple(
        ast.unparse(node)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"setattr", "delattr"}
    )
    blocked_module = Path(BLOCKLIST[0]).stem
    imported_modules = tuple(
        node.names[0].name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for _alias in (node.names[0],)
    ) + tuple(
        node.module or ""
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom)
    )
    dynamic_blocked_imports = tuple(
        ast.unparse(node)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and _dotted_name(node.func) in {"__import__", "importlib.import_module"}
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == blocked_module
    )
    blocklist_clean = (
        blocked_module not in imported_modules
        and blocked_module not in sys.modules
        and not dynamic_blocked_imports
        and BLOCKLIST
        == (
            "scripts/frontier_cycle742_archive_record_readout_feed_2026_07_28.py",
        )
    )

    self_audit_node = _top_assignment(self_tree, "AUDIT_INPUT_PATHS")
    self_audit_literal = (
        isinstance(self_audit_node, ast.Tuple)
        and ast.literal_eval(self_audit_node) == AUDIT_INPUT_PATHS
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in self_audit_node.elts
        )
    )

    permanence_wall = _literal_assignment(
        primary_tree, "PERMANENCE_WALL"
    )
    claimed_dict_values = tuple(
        value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Dict)
        for key, value in zip(node.keys, node.values)
        if isinstance(key, ast.Constant)
        and key.value == "record_permanence_claimed"
    )
    claimed_comparison_values = tuple(
        comparator.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Compare)
        and _subscript_key(node.left) == "record_permanence_claimed"
        for comparator in node.comparators
        if isinstance(comparator, ast.Constant)
    )
    claimed_key_lines = tuple(
        line.strip()
        for line in source.splitlines()
        if "record_permanence_claimed" in line
    )
    no_permanence_claim = (
        bool(claimed_dict_values)
        and all(
            isinstance(value, ast.Constant) and value.value is False
            for value in claimed_dict_values
        )
        and bool(claimed_comparison_values)
        and all(value is False for value in claimed_comparison_values)
        and claimed_key_lines
        and all("True" not in line for line in claimed_key_lines)
    )
    permanence_verbatim = permanence_wall == EXPECTED_PERMANENCE_WALL

    passed = (
        not self_attribute_targets
        and not self_attribute_mutators
        and blocklist_clean
        and self_audit_literal
        and no_permanence_claim
        and permanence_verbatim
    )
    return {
        "pass": passed,
        "self_attribute_write_targets": self_attribute_targets,
        "self_setattr_delattr_calls": self_attribute_mutators,
        "blocklist": BLOCKLIST,
        "blocklist_clean": blocklist_clean,
        "audit_tuple_pure_literal": self_audit_literal,
        "record_permanence_claimed": False,
        "record_permanence_key_lines": claimed_key_lines,
        "no_permanence_claim_anywhere": no_permanence_claim,
        "permanence_boundary_verbatim": permanence_verbatim,
        "permanence_boundary": permanence_wall,
    }


def _safe_certificate(name: str, function: object) -> dict[str, object]:
    try:
        if not callable(function):
            raise TypeError(("certificate is not callable", name))
        result = function()
        if not isinstance(result, dict):
            raise TypeError(("certificate result type", name))
        if "pass" not in result:
            raise KeyError(("certificate missing pass", name))
        return result
    except Exception as error:
        return {
            "pass": False,
            "error_type": type(error).__name__,
            "error": str(error),
        }


def main() -> int:
    started = perf_counter()
    certificates = (
        ("extraction", extraction),
        ("embedding_roundtrip_recount", embedding_roundtrip_recount),
        ("readout_recount", readout_recount),
        ("controls_recount", controls_recount),
        ("discipline", discipline),
    )
    results: dict[str, dict[str, object]] = {}
    for name, function in certificates:
        results[name] = _safe_certificate(name, function)

    passed_count = sum(
        result.get("pass") is True for result in results.values()
    )
    failed_count = len(results) - passed_count
    elapsed = perf_counter() - started
    summary: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "blocklist": BLOCKLIST,
        "certificates": results,
        "checks_passed": passed_count,
        "checks_failed": failed_count,
        "pass": failed_count == 0,
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE742_READOUT_FEED_INDEPENDENT_CHECK_PASS"
            if failed_count == 0
            else "CYCLE742_READOUT_FEED_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    summary["report_sha256"] = sha256(
        json.dumps(summary, sort_keys=True, default=str).encode()
    ).hexdigest()

    lines = tuple(
        (
            f"{'PASS' if results[name].get('pass') is True else 'FAIL'} "
            f"{name} :: "
            f"{json.dumps(results[name], sort_keys=True, default=str)}"
        )
        for name, _function_object in certificates
    )
    final_json = json.dumps(
        summary, sort_keys=True, separators=(",", ":"), default=str
    )
    output = (
        "\n".join(lines)
        + "\nSUMMARY_JSON "
        + final_json
        + f"\nRESULT {passed_count} {failed_count} "
        + f"elapsed {elapsed:.3f} s\n"
        + summary["terminal"]
        + "\n"
    )
    output_bytes = len(output.encode())
    if output_bytes >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(
            "FAIL stdout_under_150KB :: "
            + json.dumps({
                "limit_bytes": STDOUT_LIMIT_BYTES,
                "observed_bytes": output_bytes,
            }, sort_keys=True)
            + "\nRESULT 0 1\n"
            + "CYCLE742_READOUT_FEED_INDEPENDENT_CHECK_HONEST_FAIL\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
