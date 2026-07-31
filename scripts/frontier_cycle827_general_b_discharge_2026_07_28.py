#!/usr/bin/env python3
"""Cycle 827: symbolic general-b discharge of the Cycle-817 template gap.

This stdlib-only runner treats the Cycle-817 and Cycle-823 primaries as inert
bytes/text/AST.  It extracts Cycle-823 v2's exact constructor-signature
certificate, formalizes its fixed-b decision as P(b), and proves P(b) for all
integer b>=3 (and every Cycle-817 capacity C>=b) from Cycle-740's affine table
identities.  No blocklisted primary is imported or executed.
"""
from __future__ import annotations

import ast
import base64
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import perf_counter
import zlib


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = "scripts/frontier_cycle827_general_b_discharge_2026_07_28.py"

PRIMARY_817 = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py"
)
PRIMARY_823 = (
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py"
)
PRIMARY_740 = (
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py"
)
CONSTRUCTOR_719 = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
MAPPER_719 = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
)
FINALIZER_719 = (
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py"
)

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py",
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

# Only the 817/823 pair is the mandated executable blocklist.  In fact this
# runner imports no repository module at all; all six inputs are inert.
BLOCKLIST = (
    "frontier_cycle817_general_b_sector_theorem_2026_07_28",
    "frontier_cycle823_hypothesis_discharge_2026_07_28",
)
BLOCKED_DYNAMIC_CALLS = frozenset(
    ("__import__", "compile", "eval", "exec", "run_module", "run_path")
)

EXPECTED_PROVENANCE = {
    PRIMARY_817: {
        "sha256":
            "469a0af17b19bb6a35ac5356b5c143f6027af05c412f92a5b349f09c0452c7a4",
        "blob": "01045658578074e6d3c496ff09b3169381596728",
    },
    PRIMARY_823: {
        "sha256":
            "ecc213e98a7ad2ff673ac486c155fd728847f5978632f8d1bc37a02173ead5b0",
        "blob": "5529b4c3754915157b8a2b210443a3c7e5ab3730",
    },
    PRIMARY_740: {
        "sha256":
            "be1d0af8a7dae03b8eff414c1a88ec21fc04c3e92984569a15324b5da2c0fdd3",
        "blob": "523df5a77342d2eaa9a3a78d9d9997a94145baeb",
    },
    CONSTRUCTOR_719: {
        "sha256":
            "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
        "blob": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    },
    MAPPER_719: {
        "sha256":
            "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "blob": "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    },
    FINALIZER_719: {
        "sha256":
            "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
        "blob": "97cc3de7b95e341326c404047a321dbe2c825eda",
    },
}

SOURCE_WIDTH = 41
BANK_WIDTH = 131
LINK_AUX_WIDTH = 191
LINK_WIDTH = 2 * LINK_AUX_WIDTH
SOURCE_ANCHOR_SUPPORT = (0, SOURCE_WIDTH + BANK_WIDTH)
CROSS_PREDECESSOR_OFFSET = 1
ARITY = {"X": 1, "CNOT": 2, "TOF": 3}
PAIR_TEMPLATE_KIND = {
    "handoff_forward": "handoff",
    "relay_latch": "relay",
    "relay_swap": "relay",
    "relay_unlatch": "relay",
    "handoff_return": "handoff",
}
TEMPLATE_NAMES = (
    "source",
    "bank_packet",
    "cross",
    "handoff_forward",
    "relay_latch",
    "relay_swap",
    "relay_unlatch",
    "handoff_return",
    "finalizer",
)
REPRODUCTION_BANKS = tuple(range(3, 12))
ACCESSIBLE_PROOF_BANKS = tuple(range(3, 15))

P_DEFINITION = {
    "name": "P(b)",
    "domain": (
        "integer b>=3; universally for every integer capacity C>=b"
    ),
    "property": (
        "the Cycle-817/823 actual constructor preimages have fixed "
        "source/finalizer support [0,172), bank support [0,131), pair "
        "support split as [0,131)/[131,262)/[262,453), cross predecessor "
        "offset 1 in [0,131), and a b-independent finalizer; the 8b-5 row "
        "grammar uses bank indices 0..b-1 and edge indices 0..b-2; under "
        "B_i=41+131i and L_i(C)=41+131C+382i every mapped operand is the "
        "corresponding exact zone translation, hence is distinct and lies "
        "in [0,D(C)) with D(C)=41+131C+382(C-1)"
    ),
    "equivalence_to_gap": (
        "P(b) is exactly H_TEMPLATE_PREIMAGE_ZONE_CLASS on the actual "
        "Cycle-817 constructor families, with the row/index and affine "
        "mapping obligations made explicit."
    ),
}


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return sha1(header + data).hexdigest()


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def assigned_node(tree: ast.Module, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def assigned_literal(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assigned_node(tree, name))


def function_fragments(
    tree: ast.Module,
    name: str,
    fragments: tuple[str, ...],
) -> dict[str, object]:
    node = function_node(tree, name)
    rendered = ast.unparse(node)
    matches = {fragment: fragment in rendered for fragment in fragments}
    return {
        "function": name,
        "span": (node.lineno, node.end_lineno),
        "fragments": matches,
        "exact": all(matches.values()),
    }


def load_inert_packet() -> tuple[
    dict[str, object], dict[str, str], dict[str, ast.Module]
]:
    sources: dict[str, str] = {}
    rows: dict[str, object] = {}
    for path in AUDIT_INPUT_PATHS:
        absolute = ROOT / path
        data = absolute.read_bytes()
        sources[path] = data.decode("utf-8")
        observed = {
            "bytes": len(data),
            "sha256": sha256(data).hexdigest(),
            "blob": git_blob_sha1(data),
        }
        expected = EXPECTED_PROVENANCE[path]
        observed["expected_sha256"] = expected["sha256"]
        observed["expected_blob"] = expected["blob"]
        observed["exact"] = (
            observed["sha256"] == expected["sha256"]
            and observed["blob"] == expected["blob"]
        )
        rows[path] = observed
    trees = {
        path: ast.parse(source, filename=path)
        for path, source in sources.items()
    }
    return {
        "rows": rows,
        "all_sha256_and_blob_pins_exact":
            all(bool(row["exact"]) for row in rows.values()),
        "exact": all(bool(row["exact"]) for row in rows.values()),
    }, sources, trees


def decode_823_templates(tree823: ast.Module) -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    dict[str, object],
]:
    encoded = assigned_literal(tree823, "TEMPLATE_PREIMAGE_B85")
    expected_metadata = assigned_literal(
        tree823, "EXPECTED_TEMPLATE_METADATA"
    )
    if not isinstance(encoded, str) or not isinstance(
        expected_metadata, dict
    ):
        raise AssertionError("Cycle-823 template certificate is not literal")
    raw = zlib.decompress(base64.b85decode(encoded.encode()))
    decoded = json.loads(raw)
    templates = {
        str(name): tuple(
            (str(kind), tuple(int(wire) for wire in wires))
            for kind, wires in word
        )
        for name, word in decoded.items()
    }
    metadata = {
        name: {
            "digest": stable_digest(word),
            "gates": len(word),
            "operands": sum(len(wires) for _kind, wires in word),
        }
        for name, word in templates.items()
    }
    gates_exact = all(
        kind in ARITY
        and len(wires) == ARITY[kind]
        and len(wires) == len(set(wires))
        for word in templates.values()
        for kind, wires in word
    )
    exact = (
        len(raw) == 44_752
        and tuple(sorted(templates))
        == tuple(sorted(name for name in TEMPLATE_NAMES if name != "cross"))
        and metadata == expected_metadata
        and gates_exact
    )
    return templates, {
        "decoded_bytes": len(raw),
        "template_metadata": metadata,
        "gate_kind_arity_distinctness_exact": gates_exact,
        "exact": exact,
    }


def bank_base(index: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * index


def link_base(index: int, capacity: int) -> int:
    return (
        SOURCE_WIDTH
        + BANK_WIDTH * capacity
        + LINK_WIDTH * index
    )


def data_width(capacity: int) -> int:
    return (
        SOURCE_WIDTH
        + BANK_WIDTH * capacity
        + LINK_WIDTH * (capacity - 1)
    )


def program_rows(bank_count: int) -> tuple[tuple[str, int], ...]:
    if (
        isinstance(bank_count, bool)
        or not isinstance(bank_count, int)
        or bank_count < 3
    ):
        raise ValueError("bank_count must be an integer >=3")
    prefix: list[tuple[str, int]] = [("source", 0)]
    for bank in range(bank_count):
        prefix.append(("bank_packet", bank))
        if bank:
            prefix.append(("cross", bank - 1))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff_forward", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    reverse: list[tuple[str, int]] = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    return tuple(prefix + reverse + [("finalizer", 0)])


def pair_zone(wire: int) -> tuple[str, int] | None:
    if 0 <= wire < BANK_WIDTH:
        return "left_bank", wire
    if BANK_WIDTH <= wire < 2 * BANK_WIDTH:
        return "right_bank", wire - BANK_WIDTH
    if (
        2 * BANK_WIDTH
        <= wire
        < 2 * BANK_WIDTH + LINK_AUX_WIDTH
    ):
        return "link_half", wire - 2 * BANK_WIDTH
    return None


def map_by_740_formula(
    name: str,
    index: int,
    capacity: int,
    local: tuple[tuple[str, tuple[int, ...]], ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if name in {"source", "finalizer"}:
        return local
    if name == "bank_packet":
        return tuple(
            (kind, tuple(bank_base(index) + wire for wire in wires))
            for kind, wires in local
        )
    if name == "cross":
        return ((
            "CNOT",
            (
                link_base(index, capacity),
                bank_base(index + 1) + CROSS_PREDECESSOR_OFFSET,
            ),
        ),)
    split = (
        0 if PAIR_TEMPLATE_KIND[name] == "handoff"
        else LINK_AUX_WIDTH
    )
    output = []
    for kind, wires in local:
        mapped = []
        for wire in wires:
            if wire < BANK_WIDTH:
                mapped.append(bank_base(index) + wire)
            elif wire < 2 * BANK_WIDTH:
                mapped.append(
                    bank_base(index + 1) + wire - BANK_WIDTH
                )
            else:
                mapped.append(
                    link_base(index, capacity)
                    + split
                    + wire
                    - 2 * BANK_WIDTH
                )
        output.append((kind, tuple(mapped)))
    return tuple(output)


def map_by_p_zones(
    name: str,
    index: int,
    capacity: int,
    local: tuple[tuple[str, tuple[int, ...]], ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if name in {"source", "finalizer"}:
        return local
    if name == "bank_packet":
        return tuple(
            (kind, tuple(bank_base(index) + wire for wire in wires))
            for kind, wires in local
        )
    if name == "cross":
        return ((
            "CNOT",
            (
                link_base(index, capacity),
                bank_base(index + 1) + CROSS_PREDECESSOR_OFFSET,
            ),
        ),)
    split = (
        0 if PAIR_TEMPLATE_KIND[name] == "handoff"
        else LINK_AUX_WIDTH
    )
    output = []
    for kind, wires in local:
        mapped = []
        for wire in wires:
            zone = pair_zone(wire)
            if zone is None:
                mapped.append(-1)
            elif zone[0] == "left_bank":
                mapped.append(bank_base(index) + zone[1])
            elif zone[0] == "right_bank":
                mapped.append(bank_base(index + 1) + zone[1])
            else:
                mapped.append(
                    link_base(index, capacity) + split + zone[1]
                )
        output.append((kind, tuple(mapped)))
    return tuple(output)


def expected_family_counts(bank_count: int) -> dict[str, int]:
    return {
        "source": 1,
        "bank_packet": bank_count,
        "cross": bank_count - 1,
        "handoff_forward": bank_count - 1,
        "relay_latch": bank_count - 1,
        "relay_swap": 2 * (bank_count - 1),
        "relay_unlatch": bank_count - 1,
        "handoff_return": bank_count - 1,
        "finalizer": 1,
    }


def decide_p_instance(
    bank_count: int,
    capacity: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    finalizer_independent: bool,
    *,
    perturb: bool = False,
) -> dict[str, object]:
    if (
        isinstance(capacity, bool)
        or not isinstance(capacity, int)
        or capacity < bank_count
    ):
        raise ValueError("capacity must be an integer >= bank_count")
    rows = program_rows(bank_count)
    failures: list[dict[str, object]] = []
    failure_count = 0
    gates = 0
    operands = 0
    perturbed = False

    def fail(**row: object) -> None:
        nonlocal failure_count
        failure_count += 1
        if len(failures) < 12:
            failures.append(row)

    for station, (name, index) in enumerate(rows):
        local = () if name == "cross" else templates[name]
        observed = list(map_by_740_formula(name, index, capacity, local))
        expected = map_by_p_zones(name, index, capacity, local)
        if perturb and not perturbed and name == "bank_packet" and observed:
            kind, wires = observed[0]
            changed = list(wires)
            changed[0] = bank_base(index) + BANK_WIDTH
            observed[0] = (kind, tuple(changed))
            perturbed = True
        mapped = tuple(observed)
        gates += len(mapped)
        operands += sum(len(wires) for _kind, wires in mapped)
        if mapped != expected:
            fail(
                b=bank_count,
                C=capacity,
                station=station,
                family=name,
                detail="exact affine zone identity",
                observed_digest=stable_digest(mapped),
                expected_digest=stable_digest(expected),
            )
        if name == "bank_packet" and not 0 <= index < bank_count:
            fail(
                b=bank_count, C=capacity, station=station, family=name,
                detail="bank index", observed=index,
                expected=(0, bank_count),
            )
        if (
            name not in {"source", "bank_packet", "finalizer"}
            and not 0 <= index < bank_count - 1
        ):
            fail(
                b=bank_count, C=capacity, station=station, family=name,
                detail="edge index", observed=index,
                expected=(0, bank_count - 1),
            )
        for gate_index, (kind, wires) in enumerate(mapped):
            if (
                kind not in ARITY
                or len(wires) != ARITY.get(kind)
                or len(wires) != len(set(wires))
            ):
                fail(
                    b=bank_count, C=capacity, station=station, family=name,
                    gate=gate_index, detail="kind/arity/distinctness",
                    observed=(kind, wires),
                )
            for operand_index, wire in enumerate(wires):
                if not 0 <= wire < data_width(capacity):
                    fail(
                        b=bank_count, C=capacity, station=station,
                        family=name, gate=gate_index,
                        operand=operand_index, detail="global data range",
                        observed=wire, expected=(0, data_width(capacity)),
                    )

    counts = dict(sorted(Counter(name for name, _ in rows).items()))
    expected_counts = expected_family_counts(bank_count)
    if (
        len(rows) != 8 * bank_count - 5
        or counts != expected_counts
    ):
        fail(
            b=bank_count, C=capacity, detail="8b-5 row grammar",
            observed=(len(rows), counts),
            expected=(8 * bank_count - 5, expected_counts),
        )
    if not finalizer_independent:
        fail(
            b=bank_count, C=capacity, detail="finalizer independence",
            observed=False, expected=True,
        )
    if perturb and not perturbed:
        fail(
            b=bank_count, C=capacity, detail="negative perturbation applied",
            observed=False, expected=True,
        )
    exact = failure_count == 0
    return {
        "b": bank_count,
        "C": capacity,
        "n": 8 * bank_count - 5,
        "rows": len(rows),
        "gates": gates,
        "operands": operands,
        "family_counts": counts,
        "failure_count": failure_count,
        "failures": failures,
        "perturbed": perturb,
        "P(b)": "PASS" if exact else "FAIL",
        "exact": exact,
    }


def main() -> int:
    """Scaffold entry point; completed certificates are added incrementally."""
    started = perf_counter()
    source_inputs, _sources, trees = load_inert_packet()
    templates, literal = decode_823_templates(trees[PRIMARY_823])
    probe = decide_p_instance(3, 12, templates, True)
    elapsed = perf_counter() - started
    exact = source_inputs["exact"] and literal["exact"] and probe["exact"]
    report = {
        "cycle": 827,
        "phase": "SCAFFOLD",
        "source_inputs": source_inputs,
        "literal_templates": literal,
        "probe": probe,
        "runtime_seconds": round(elapsed, 6),
        "runner_exact": exact,
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
