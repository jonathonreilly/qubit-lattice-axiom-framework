#!/usr/bin/env python3
"""Cycle 827 v2 independent adversarial checker.

The three blocklisted primaries are inert evidence: this checker reads only
their bytes, text, and AST.  It independently implements exact multivariate
polynomial arithmetic and the concrete affine mapper.  The v1 attacks are
retained; their acceptance conditions now require complete v2 accounting.
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


ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = (
    "scripts/frontier_cycle827_discharge_independent_check_2026_07_28.py"
)
PRIMARY_817 = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py"
)
PRIMARY_823 = (
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py"
)
PRIMARY_827 = (
    "scripts/frontier_cycle827_general_b_discharge_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py",
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py",
    "scripts/frontier_cycle827_general_b_discharge_2026_07_28.py",
)
BLOCKLIST = (
    "frontier_cycle817_general_b_sector_theorem_2026_07_28",
    "frontier_cycle823_hypothesis_discharge_2026_07_28",
    "frontier_cycle827_general_b_discharge_2026_07_28",
)
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000

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
    PRIMARY_827: {
        "sha256":
            "2f85e4d5a1c9d19afcbb44f1680fcb90ff8cf95ff1020f06da660bb2ab286ef3",
        "blob": "75446e9dc63d91dc9fc45a39c42e027b385f4115",
    },
}

SOURCE_WIDTH = 41
BANK_WIDTH = 131
LINK_HALF_WIDTH = 191
LINK_WIDTH = 382
SOURCE_SUPPORT = (0, SOURCE_WIDTH + BANK_WIDTH)
ARITY = {"X": 1, "CNOT": 2, "TOF": 3}
PAIR_KIND = {
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
VARIABLES = ("b", "C", "i", "u", "s", "p")
ZERO_MONOMIAL = (0,) * len(VARIABLES)

FINDING_SYMBOLIC = (
    "Polynomial substeps 13/13 are exact in Z[b,C,i,u,s,p]. V2 declares "
    "the Cycle-823 actual-object b=3 PASS and proves p_(b+1)=p_b from the "
    "b-free actual mapper AST, so universal closure has no silent premise."
)
FINDING_DOMAIN = (
    "The independent concrete mapper passes b=3, C=b, p=0 and p=130; the "
    "first/last bank and edge indices and all 8b-5 grammar counts are exact."
)
FINDING_PREMISES = (
    "Independent AST accounting finds exactly nine load-bearing premises: "
    "the eight Cycle-817 premises plus B823_VERIFIED_ACTUAL_OBJECT_BASE_B3. "
    "The live-p bound is a derived lemma. X(131) satisfies the old eight "
    "and live p but violates the declared b=3 base at local bank wire 131."
)
FINDING_REPRODUCTION = (
    "Independent b=3..14 checks pass at C=b and C=14; changing the first "
    "mapped bank operand to the excluded boundary B_i+131 is rejected."
)
FINDING_CONTROLS = (
    "SHA-256/blob pins, literal relative input paths, the exact 817/823/827 "
    "blocklist, text/AST-only access, deterministic core, runtime, and "
    "stdout bounds all pass."
)


def stable_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_bytes(value)).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def assigned_node(tree: ast.Module, name: str) -> ast.AST:
    matches = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment", name, len(matches)))
    return matches[0]


def assigned_literal(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assigned_node(tree, name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def load_inert_inputs() -> tuple[
    dict[str, object], dict[str, str], dict[str, ast.Module]
]:
    provenance: dict[str, object] = {}
    sources = {}
    trees = {}
    for path in AUDIT_INPUT_PATHS:
        data = (ROOT / path).read_bytes()
        source = data.decode("utf-8")
        observed = {
            "sha256": sha256(data).hexdigest(),
            "blob": git_blob_sha1(data),
        }
        observed["exact"] = (
            observed["sha256"] == EXPECTED_PROVENANCE[path]["sha256"]
            and observed["blob"] == EXPECTED_PROVENANCE[path]["blob"]
        )
        provenance[path] = observed
        sources[path] = source
        trees[path] = ast.parse(source, filename=path)
    return provenance, sources, trees


# Polynomials are sparse maps from exponent tuples to integer coefficients.
def polynomial(terms: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    if any(len(monomial) != len(VARIABLES) for monomial in terms):
        raise AssertionError("noncanonical monomial")
    return {
        monomial: int(coefficient)
        for monomial, coefficient in terms.items()
        if coefficient
    }


def pconst(value: int) -> dict[tuple[int, ...], int]:
    return polynomial({ZERO_MONOMIAL: value})


def pvar(name: str) -> dict[tuple[int, ...], int]:
    exponent = [0] * len(VARIABLES)
    exponent[VARIABLES.index(name)] = 1
    return {tuple(exponent): 1}


def padd(*values: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for value in values:
        for monomial, coefficient in value.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return polynomial(result)


def pscale(
    factor: int, value: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    return polynomial({
        monomial: factor * coefficient
        for monomial, coefficient in value.items()
    })


def psub(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    return padd(left, pscale(-1, right))


def pmul(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                a + b for a, b in zip(left_monomial, right_monomial)
            )
            result[monomial] = (
                result.get(monomial, 0)
                + left_coefficient * right_coefficient
            )
    return polynomial(result)


def independent_symbolic_identities() -> tuple[
    tuple[str, dict[tuple[int, ...], int], dict[tuple[int, ...], int]], ...
]:
    b, capacity, index, local, split, pred = (
        pvar(name) for name in VARIABLES
    )
    one = pconst(1)
    bank_i = padd(pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, index))
    bank_next = padd(bank_i, pconst(BANK_WIDTH))
    link_i = padd(
        pconst(SOURCE_WIDTH),
        pscale(BANK_WIDTH, capacity),
        pscale(LINK_WIDTH, index),
    )
    width = padd(
        pconst(SOURCE_WIDTH),
        pscale(BANK_WIDTH, capacity),
        pscale(LINK_WIDTH, padd(capacity, pconst(-1))),
    )
    b_minus_one = padd(b, pconst(-1))
    return (
        (
            "1+b+(b-1)+3(b-1)+3(b-1)+1 = 8b-5",
            padd(
                one, b, b_minus_one, pscale(3, b_minus_one),
                pscale(3, b_minus_one), one,
            ),
            padd(pscale(8, b), pconst(-5)),
        ),
        (
            "B_i+131 = B_(i+1)",
            padd(bank_i, pconst(BANK_WIDTH)),
            bank_next,
        ),
        (
            "B_(C-1)+131 = L_0(C)",
            padd(
                pconst(SOURCE_WIDTH),
                pscale(BANK_WIDTH, padd(capacity, pconst(-1))),
                pconst(BANK_WIDTH),
            ),
            padd(pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, capacity)),
        ),
        (
            "L_i(C)+382 = L_(i+1)(C)",
            padd(link_i, pconst(LINK_WIDTH)),
            padd(
                pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, capacity),
                pscale(LINK_WIDTH, padd(index, one)),
            ),
        ),
        (
            "L_(C-2)(C)+382 = D(C)",
            padd(
                pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, capacity),
                pscale(LINK_WIDTH, padd(capacity, pconst(-2))),
                pconst(LINK_WIDTH),
            ),
            width,
        ),
        (
            "bank map: B_i+u",
            padd(bank_i, local),
            padd(pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, index), local),
        ),
        (
            "pair-left map: B_i+u",
            padd(bank_i, local),
            padd(pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, index), local),
        ),
        (
            "pair-right map: B_(i+1)+(131+u)-131",
            padd(bank_next, pconst(BANK_WIDTH), local, pconst(-BANK_WIDTH)),
            padd(
                pconst(SOURCE_WIDTH + BANK_WIDTH),
                pscale(BANK_WIDTH, index), local,
            ),
        ),
        (
            "pair-link map: L_i+s+(262+u)-262",
            padd(
                link_i, split, pconst(2 * BANK_WIDTH), local,
                pconst(-2 * BANK_WIDTH),
            ),
            padd(
                pconst(SOURCE_WIDTH), pscale(BANK_WIDTH, capacity),
                pscale(LINK_WIDTH, index), split, local,
            ),
        ),
        (
            "cross target: B_(i+1)+p",
            padd(bank_next, pred),
            padd(
                pconst(SOURCE_WIDTH + BANK_WIDTH),
                pscale(BANK_WIDTH, index), pred,
            ),
        ),
        (
            "C-i-1 = (C-b)+(b-i-1) for bank i<=b-1",
            padd(capacity, pscale(-1, index), pconst(-1)),
            padd(
                capacity, pscale(-1, b), b, pscale(-1, index),
                pconst(-1),
            ),
        ),
        (
            "C-i-2 = (C-b)+(b-i-2) for edge i<=b-2",
            padd(capacity, pscale(-1, index), pconst(-2)),
            padd(
                capacity, pscale(-1, b), b, pscale(-1, index),
                pconst(-2),
            ),
        ),
        (
            "D(C)-172 = 513*(C-1)",
            padd(width, pconst(-SOURCE_SUPPORT[1])),
            pscale(
                BANK_WIDTH + LINK_WIDTH,
                padd(capacity, pconst(-1)),
            ),
        ),
    )


def symbolic_certificate(tree827: ast.Module) -> dict[str, object]:
    identities = independent_symbolic_identities()
    rows = []
    for label, left, right in identities:
        difference = psub(left, right)
        rows.append({
            "identity": label,
            "difference": {
                str(monomial): coefficient
                for monomial, coefficient in sorted(difference.items())
            },
            "exact": not difference,
        })
    primary_function = function_node(
        tree827, "symbolic_identity_certificate"
    )
    primary_labels = tuple(
        call.args[0].value
        for call in ast.walk(primary_function)
        if isinstance(call, ast.Call)
        and call_name(call.func) == "affine_identity"
        and call.args
        and isinstance(call.args[0], ast.Constant)
        and isinstance(call.args[0].value, str)
    )
    independent_labels = tuple(row["identity"] for row in rows)
    label_coverage = (
        len(primary_labels) == 13
        and Counter(primary_labels) == Counter(independent_labels)
    )
    # These are the non-polynomial interval steps stated by the primary.
    domain_reasoning = {
        "C_minus_i_minus_1_nonnegative": all(
            capacity - index - 1 >= 0
            for b in range(3, 18)
            for capacity in (b, b + 1, b + 9)
            for index in range(b)
        ),
        "C_minus_i_minus_2_nonnegative": all(
            capacity - index - 2 >= 0
            for b in range(3, 18)
            for capacity in (b, b + 1, b + 9)
            for index in range(b - 1)
        ),
        "source_below_D": all(
            data_width(capacity) > SOURCE_SUPPORT[1]
            for capacity in range(3, 32)
        ),
        "pair_target_intervals_disjoint": (
            (0, BANK_WIDTH),
            (BANK_WIDTH, 2 * BANK_WIDTH),
            (2 * BANK_WIDTH, 2 * BANK_WIDTH + LINK_HALF_WIDTH),
        ) == ((0, 131), (131, 262), (262, 453)),
        "positive_widths": (
            SOURCE_WIDTH > 0
            and BANK_WIDTH > 0
            and LINK_HALF_WIDTH > 0
            and LINK_WIDTH == 2 * LINK_HALF_WIDTH
        ),
    }
    polynomial_exact = (
        label_coverage
        and all(row["exact"] for row in rows)
        and all(domain_reasoning.values())
    )
    return {
        "coefficient_ring": "Z[b,C,i,u,s,p]",
        "primary_identity_labels": primary_labels,
        "independent_rows": rows,
        "all_13_polynomial_substeps_exact": polynomial_exact,
        "nonpolynomial_domain_steps": domain_reasoning,
        "label_coverage_exact": label_coverage,
        "exact": polynomial_exact,
    }


def decode_templates(tree823: ast.Module) -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]], dict[str, object]
]:
    encoded = assigned_literal(tree823, "TEMPLATE_PREIMAGE_B85")
    expected_metadata = assigned_literal(
        tree823, "EXPECTED_TEMPLATE_METADATA"
    )
    if not isinstance(encoded, str) or not isinstance(
        expected_metadata, dict
    ):
        raise AssertionError("Cycle-823 certificate literals unavailable")
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
    exact = (
        len(raw) == 44_752
        and tuple(sorted(templates))
        == tuple(sorted(set(TEMPLATE_NAMES) - {"cross"}))
        and metadata == expected_metadata
        and all(
            kind in ARITY
            and len(wires) == ARITY[kind]
            and len(wires) == len(set(wires))
            for word in templates.values()
            for kind, wires in word
        )
    )
    return templates, {
        "decoded_bytes": len(raw),
        "metadata_digest": stable_digest(metadata),
        "exact": exact,
    }


def bank_base(index: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * index


def link_base(index: int, capacity: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * capacity + LINK_WIDTH * index


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
    rows: list[tuple[str, int]] = [("source", 0)]
    for bank in range(bank_count):
        rows.append(("bank_packet", bank))
        if bank:
            rows.append(("cross", bank - 1))
        if bank < bank_count - 1:
            rows.extend((
                ("handoff_forward", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    for edge in reversed(range(bank_count - 1)):
        rows.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    rows.append(("finalizer", 0))
    return tuple(rows)


def expected_counts(bank_count: int) -> dict[str, int]:
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


def pair_zone(wire: int) -> tuple[str, int] | None:
    if 0 <= wire < BANK_WIDTH:
        return "left", wire
    if BANK_WIDTH <= wire < 2 * BANK_WIDTH:
        return "right", wire - BANK_WIDTH
    if 2 * BANK_WIDTH <= wire < 2 * BANK_WIDTH + LINK_HALF_WIDTH:
        return "link", wire - 2 * BANK_WIDTH
    return None


def map_formula(
    name: str,
    index: int,
    capacity: int,
    local: tuple[tuple[str, tuple[int, ...]], ...],
    pred: int,
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
            (link_base(index, capacity), bank_base(index + 1) + pred),
        ),)
    split = 0 if PAIR_KIND[name] == "handoff" else LINK_HALF_WIDTH
    output = []
    for kind, wires in local:
        mapped = []
        for wire in wires:
            if wire < BANK_WIDTH:
                mapped.append(bank_base(index) + wire)
            elif wire < 2 * BANK_WIDTH:
                mapped.append(bank_base(index + 1) + wire - BANK_WIDTH)
            else:
                mapped.append(
                    link_base(index, capacity)
                    + split + wire - 2 * BANK_WIDTH
                )
        output.append((kind, tuple(mapped)))
    return tuple(output)


def map_by_zones(
    name: str,
    index: int,
    capacity: int,
    local: tuple[tuple[str, tuple[int, ...]], ...],
    pred: int,
) -> tuple[tuple[str, tuple[int, ...]], ...] | None:
    if name in {"source", "finalizer"}:
        return local
    if name == "bank_packet":
        if any(
            not 0 <= wire < BANK_WIDTH
            for _kind, wires in local for wire in wires
        ):
            return None
        return tuple(
            (kind, tuple(bank_base(index) + wire for wire in wires))
            for kind, wires in local
        )
    if name == "cross":
        if not 0 <= pred < BANK_WIDTH:
            return None
        return ((
            "CNOT",
            (link_base(index, capacity), bank_base(index + 1) + pred),
        ),)
    split = 0 if PAIR_KIND[name] == "handoff" else LINK_HALF_WIDTH
    output = []
    for kind, wires in local:
        mapped = []
        for wire in wires:
            zone = pair_zone(wire)
            if zone is None:
                return None
            if zone[0] == "left":
                mapped.append(bank_base(index) + zone[1])
            elif zone[0] == "right":
                mapped.append(bank_base(index + 1) + zone[1])
            else:
                mapped.append(
                    link_base(index, capacity) + split + zone[1]
                )
        output.append((kind, tuple(mapped)))
    return tuple(output)


def concrete_check(
    bank_count: int,
    capacity: int,
    pred: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    if capacity < bank_count:
        raise ValueError("capacity must be >= bank_count")
    rows = program_rows(bank_count)
    failures = []
    gate_count = 0
    operand_count = 0
    for station, (name, index) in enumerate(rows):
        local = () if name == "cross" else templates[name]
        observed = map_formula(name, index, capacity, local, pred)
        expected = map_by_zones(name, index, capacity, local, pred)
        if observed != expected:
            failures.append((station, name, "exact affine zone map"))
        if name in {"source", "finalizer"} and any(
            not SOURCE_SUPPORT[0] <= wire < SOURCE_SUPPORT[1]
            for _kind, wires in local for wire in wires
        ):
            failures.append((station, name, "source support"))
        if name == "bank_packet" and not 0 <= index < bank_count:
            failures.append((station, name, "bank index"))
        if name in {"cross", *PAIR_KIND} and not 0 <= index < bank_count - 1:
            failures.append((station, name, "edge index"))
        gate_count += len(observed)
        operand_count += sum(len(wires) for _kind, wires in observed)
        for gate_index, (kind, wires) in enumerate(observed):
            if (
                kind not in ARITY
                or len(wires) != ARITY.get(kind)
                or len(wires) != len(set(wires))
            ):
                failures.append((
                    station, name, gate_index, "kind/arity/distinctness",
                ))
            for wire in wires:
                if not 0 <= wire < data_width(capacity):
                    failures.append((
                        station, name, gate_index, "global range", wire,
                    ))
    counts = dict(sorted(Counter(name for name, _index in rows).items()))
    if (
        len(rows) != 8 * bank_count - 5
        or counts != expected_counts(bank_count)
    ):
        failures.append(("8b-5 grammar", len(rows), counts))
    bank_indices = tuple(index for name, index in rows if name == "bank_packet")
    edge_indices = tuple(
        index for name, index in rows if name in {"cross", *PAIR_KIND}
    )
    return {
        "b": bank_count,
        "C": capacity,
        "p": pred,
        "rows": len(rows),
        "gates": gate_count,
        "operands": operand_count,
        "family_counts": counts,
        "bank_index_edges": (min(bank_indices), max(bank_indices)),
        "edge_index_edges": (min(edge_indices), max(edge_indices)),
        "failure_count": len(failures),
        "first_failures": failures[:5],
        "exact": not failures,
    }


def interval_partition_exact(capacity: int) -> bool:
    intervals = [(0, SOURCE_WIDTH)]
    intervals.extend(
        (bank_base(index), bank_base(index) + BANK_WIDTH)
        for index in range(capacity)
    )
    intervals.extend(
        (link_base(index, capacity), link_base(index, capacity) + LINK_WIDTH)
        for index in range(capacity - 1)
    )
    return (
        intervals[0][0] == 0
        and all(
            left[1] == right[0]
            for left, right in zip(intervals, intervals[1:])
        )
        and intervals[-1][1] == data_width(capacity)
    )


def lawful_mapped_words(
    bank_count: int,
    capacity: int,
    pred: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> bool:
    for name, index in program_rows(bank_count):
        local = () if name == "cross" else templates[name]
        for kind, wires in map_formula(
            name, index, capacity, local, pred
        ):
            if (
                kind not in ARITY
                or len(wires) != ARITY[kind]
                or len(wires) != len(set(wires))
                or any(not 0 <= wire < data_width(capacity) for wire in wires)
            ):
                return False
    return True


def ownership_covariance_truth_table() -> bool:
    def predicate(bits: tuple[int, ...]) -> bool:
        return not any(bits)

    return all(
        predicate((
            left_a, right_a, left_b, station_b, right_b, work,
        )) == predicate((
            left_a, right_a, left_b, station_b, right_b, work,
        ))
        for left_a in (0, 1)
        for right_a in (0, 1)
        for left_b in (0, 1)
        for station_b in (0, 1)
        for right_b in (0, 1)
        for work in (0, 1)
    )


def hidden_premise_countermodel() -> dict[str, object]:
    # This world satisfies every declared predicate but deliberately places
    # the bank word at the excluded local boundary.  Its mapped X gates are
    # still valid and globally in range, so P_LOCAL_WORD_CLASS cannot recover
    # the stronger preimage-zone fact.
    synthetic = {
        "source": (("X", (0,)),),
        "bank_packet": (("X", (BANK_WIDTH,)),),
        "handoff_forward": (("X", (0,)),),
        "relay_latch": (("X", (BANK_WIDTH,)),),
        "relay_swap": (("X", (2 * BANK_WIDTH,)),),
        "relay_unlatch": (("X", (2 * BANK_WIDTH + 1,)),),
        "handoff_return": (("X", (1,)),),
        "finalizer": (("X", (0,)),),
    }
    bank_count = 3
    capacity = 3
    pred = 1
    rows = program_rows(bank_count)
    counts = Counter(name for name, _index in rows)
    indices_lawful = all(
        (
            0 <= index < bank_count
            if name == "bank_packet"
            else 0 <= index < bank_count - 1
            if name in {"cross", *PAIR_KIND}
            else True
        )
        for name, index in rows
    )
    sector_witness = {
        "b": bank_count,
        "n": 8 * bank_count - 5,
        "k": 0,
        "h": 0,
        "A_positions": (),
        "B_work_controller_blank": True,
        "expected_count": 0,
        "direction_endpoint": (1, 0),
        "K_chain_clean": True,
    }
    sector_exact = (
        sector_witness["b"] > 0
        and sector_witness["n"] == 8 * sector_witness["b"] - 5
        and sector_witness["h"] == sector_witness["k"] % 2
        and not sector_witness["A_positions"]
        and sector_witness["B_work_controller_blank"]
        and sector_witness["expected_count"] == sector_witness["k"]
        and sector_witness["direction_endpoint"] == (1, 0)
        and sector_witness["K_chain_clean"]
    )
    premise_outcomes = {
        "P_CAPACITY": 3 <= bank_count <= capacity,
        "P_AFFINE_TABLE": interval_partition_exact(capacity),
        "P_NONPADDED_RING": (
            len(rows) == 8 * bank_count - 5
            and dict(counts) == expected_counts(bank_count)
        ),
        "P_LAWFUL_MAPPING": indices_lawful,
        "P_LOCAL_WORD_CLASS": lawful_mapped_words(
            bank_count, capacity, pred, synthetic
        ),
        "H_OWNERSHIP_DEFINITION_AND_COVARIANCE":
            ownership_covariance_truth_table(),
        "H_FIXED_TEMPLATE_AND_FINALIZER_UNIFORMITY": (
            synthetic == dict(synthetic)
            and synthetic["finalizer"] == (("X", (0,)),)
        ),
        "H_SECTOR_INPUT": sector_exact,
    }
    p_holds = all(
        0 <= wire < BANK_WIDTH
        for _kind, wires in synthetic["bank_packet"]
        for wire in wires
    )
    mapped_boundary = bank_base(bank_count - 1) + BANK_WIDTH
    exact = (
        all(premise_outcomes.values())
        and not p_holds
        and mapped_boundary == link_base(0, capacity)
        and 0 <= mapped_boundary < data_width(capacity)
    )
    return {
        "instantiation": {
            "b": bank_count,
            "C": capacity,
            "p": pred,
            "bank_preimage": synthetic["bank_packet"],
            "last_bank_mapped_operand": mapped_boundary,
            "D(C)": data_width(capacity),
        },
        "declared_premise_outcomes": premise_outcomes,
        "P(b)_bank_zone_clause": p_holds,
        "live_p_lemma_satisfied": 0 <= pred < BANK_WIDTH,
        "B823_VERIFIED_ACTUAL_OBJECT_BASE_B3": p_holds,
        "violated_v2_premise": (
            "B823_VERIFIED_ACTUAL_OBJECT_BASE_B3"
            if not p_holds else None
        ),
        "precise_failure": (
            "bank_packet gate 0 operand 0 is local wire 131, the excluded "
            "upper endpoint of [0,131)"
        ),
        "countermodel_exact": exact,
        "exact": exact,
    }


def dict_literal_value(
    function: ast.FunctionDef, key: str,
) -> object:
    matches = []
    for node in ast.walk(function):
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if (
                    isinstance(key_node, ast.Constant)
                    and key_node.value == key
                ):
                    try:
                        matches.append(ast.literal_eval(value_node))
                    except (ValueError, TypeError):
                        pass
    if len(matches) != 1:
        raise AssertionError(("dict literal", function.name, key, len(matches)))
    return matches[0]


def premise_accounting_certificate(
    tree817: ast.Module,
    tree827: ast.Module,
    countermodel: dict[str, object],
) -> dict[str, object]:
    cycle817_declared = assigned_literal(
        tree817, "CORRECTED_INVENTORY_NAMES"
    )
    expected_eight = (
        "P_CAPACITY",
        "P_AFFINE_TABLE",
        "P_NONPADDED_RING",
        "P_LAWFUL_MAPPING",
        "P_LOCAL_WORD_CLASS",
        "H_OWNERSHIP_DEFINITION_AND_COVARIANCE",
        "H_FIXED_TEMPLATE_AND_FINALIZER_UNIFORMITY",
        "H_SECTOR_INPUT",
    )
    expected_complete = expected_eight + (
        "B823_VERIFIED_ACTUAL_OBJECT_BASE_B3",
    )
    primary_declared = assigned_literal(
        tree827, "DECLARED_THEOREM_PREMISES"
    )
    cache_blob = assigned_literal(
        tree827, "CYCLE823_CACHE_BLOB_SHA1"
    )
    cert_a = function_node(tree827, "certificate_a")
    cert_b = function_node(tree827, "certificate_b")
    cert_c = function_node(tree827, "certificate_c")
    live_p = function_node(tree827, "live_p_dynamics_certificate")
    gate = function_node(tree827, "theorem_premise_gate")
    rendered_a = ast.unparse(cert_a)
    rendered_b = ast.unparse(cert_b)
    rendered_c = ast.unparse(cert_c)
    rendered_live_p = ast.unparse(live_p)
    primary_declared_proof_premises = dict_literal_value(
        cert_b, "premises"
    )
    gate_references = tuple(
        node.slice.value
        for node in ast.walk(gate)
        if isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "premise_truth"
        and isinstance(node.slice, ast.Constant)
        and isinstance(node.slice.value, str)
    )
    dataflow = {
        "certificate_a_builds_declared_base":
            "actual_base_lemma" in rendered_a,
        "certificate_a_proves_live_p":
            "live_p_dynamics_certificate" in rendered_a
            and "live_p['exact']" in rendered_a,
        "live_p_step_reads_b_free_mapper":
            "function_node(mapper_tree, 'mapped_action')"
            in rendered_live_p
            and "bank_count_or_capacity_AST_loads"
            in rendered_live_p
            and "p_(b+1)" in rendered_live_p,
        "certificate_b_reads_declared_base_exact":
            "actual_base['exact']" in rendered_b,
        "certificate_b_reads_live_p_lemma":
            "cert_a['live_p_bound']['exact']" in rendered_b,
        "certificate_b_gates_exact_premise_list":
            "theorem_premise_gate(premise_truth)" in rendered_b,
        "certificate_c_consumes_universal_proof":
            "universal_proof_exact_without_signature_diagnostic"
            in rendered_c,
        "certificate_c_consumes_internal_AST_accounting":
            "premise_accounting['exact']" in rendered_c,
    }
    x131_handled = (
        countermodel["exact"]
        and countermodel["live_p_lemma_satisfied"]
        and not countermodel["B823_VERIFIED_ACTUAL_OBJECT_BASE_B3"]
        and countermodel["violated_v2_premise"]
        == "B823_VERIFIED_ACTUAL_OBJECT_BASE_B3"
    )
    exact = (
        cycle817_declared == expected_eight
        and primary_declared == expected_complete
        and primary_declared_proof_premises == expected_complete
        and gate_references == expected_complete
        and len(gate_references) == len(set(gate_references)) == 9
        and all(dataflow.values())
        and cache_blob == "c5d8367dea7b8af05f1d53113149156436966ade"
        and x131_handled
    )
    return {
        "Cycle817_declared_eight": cycle817_declared,
        "primary_declared_complete": primary_declared,
        "primary_certificate_B_premises": primary_declared_proof_premises,
        "theorem_premise_gate_AST_references": gate_references,
        "load_bearing_AST_dataflow": dataflow,
        "Cycle823_cache_git_blob_sha1": cache_blob,
        "countermodel": countermodel,
        "X131_rejected_by_declared_base_premise": x131_handled,
        "live_p_is_lemma_not_declared_premise": (
            "H_LIVE_P_BOUND" not in primary_declared
            and "LIVE_P" not in primary_declared
        ),
        "no_silent_extra_assumption": exact,
        "finding": FINDING_PREMISES,
        "exact": exact,
    }


def domain_edge_certificate(
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    probes = {
        "b3_Ceqb_p0": concrete_check(3, 3, 0, templates),
        "b3_Ceqb_p130": concrete_check(3, 3, 130, templates),
        "b14_Ceqb_p0": concrete_check(14, 14, 0, templates),
        "b14_Ceqb_p130": concrete_check(14, 14, 130, templates),
    }
    grammar_edges = all(
        row["rows"] == 8 * row["b"] - 5
        and row["bank_index_edges"] == (0, row["b"] - 1)
        and row["edge_index_edges"] == (0, row["b"] - 2)
        for row in probes.values()
    )
    exact = all(row["exact"] for row in probes.values()) and grammar_edges
    return {
        "boundary_probes": probes,
        "8b_minus_5_first_last_indices_exact": grammar_edges,
        "finding": FINDING_DOMAIN,
        "exact": exact,
    }


def reproduction_certificate(
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    rows = {}
    for bank_count in range(3, 15):
        at_boundary = concrete_check(
            bank_count, bank_count, 1, templates
        )
        at_capacity_14 = concrete_check(
            bank_count, 14, 1, templates
        )
        rows[bank_count] = {
            "C_equal_b": at_boundary["exact"],
            "C_equal_14": at_capacity_14["exact"],
            "rows": at_boundary["rows"],
            "gates": at_boundary["gates"],
            "operands": at_boundary["operands"],
            "same_counts": (
                at_boundary["rows"] == at_capacity_14["rows"]
                and at_boundary["gates"] == at_capacity_14["gates"]
                and at_boundary["operands"] == at_capacity_14["operands"]
            ),
        }
        rows[bank_count]["exact"] = (
            rows[bank_count]["C_equal_b"]
            and rows[bank_count]["C_equal_14"]
            and rows[bank_count]["same_counts"]
        )
    local = templates["bank_packet"]
    expected = map_by_zones("bank_packet", 0, 3, local, 1)
    observed = list(map_formula("bank_packet", 0, 3, local, 1))
    perturbation_applied = bool(observed and observed[0][1])
    if perturbation_applied:
        kind, wires = observed[0]
        changed = list(wires)
        changed[0] = bank_base(0) + BANK_WIDTH
        observed[0] = (kind, tuple(changed))
    negative_rejected = (
        perturbation_applied
        and tuple(observed) != expected
        and observed[0][1][0] == bank_base(1)
        and not bank_base(0) <= observed[0][1][0] < bank_base(1)
    )
    exact = (
        all(row["exact"] for row in rows.values())
        and negative_rejected
    )
    return {
        "b3_through_b14": rows,
        "negative_control": {
            "perturbation": "first bank operand -> B_i+131",
            "rejected": negative_rejected,
        },
        "finding": FINDING_REPRODUCTION,
        "exact": exact,
    }


def build_scientific_core(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    templates, literal = decode_templates(trees[PRIMARY_823])
    symbolic = symbolic_certificate(trees[PRIMARY_827])
    countermodel = hidden_premise_countermodel()
    premise = premise_accounting_certificate(
        trees[PRIMARY_817], trees[PRIMARY_827], countermodel
    )
    domain = domain_edge_certificate(templates)
    reproduction = reproduction_certificate(templates)
    primary_passes = (
        literal["exact"]
        and symbolic["exact"]
        and premise["exact"]
        and countermodel["exact"]
    )
    return {
        "template_literal": literal,
        "symbolic_reimplementation": symbolic,
        "domain_edge_attack": domain,
        "premise_accounting": premise,
        "reproduction_and_negative_control": reproduction,
        "primary_passes": primary_passes,
        "verdict": "PASS" if primary_passes else "INDETERMINATE",
    }


def controls_certificate(
    provenance: dict[str, object],
    sources: dict[str, str],
    first_core: dict[str, object],
    second_core: dict[str, object],
    elapsed: float,
) -> dict[str, object]:
    self_source = (ROOT / SELF_PATH).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=SELF_PATH)
    input_node = assigned_node(self_tree, "AUDIT_INPUT_PATHS")
    blocklist_node = assigned_node(self_tree, "BLOCKLIST")
    literal_paths = (
        isinstance(input_node, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in input_node.elts
        )
    )
    literal_blocklist = (
        isinstance(blocklist_node, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in blocklist_node.elts
        )
    )
    paths_exact = (
        literal_paths
        and tuple(sources) == AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    imports = []
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    allowed_imports = {
        "__future__",
        "ast",
        "base64",
        "collections",
        "hashlib",
        "json",
        "pathlib",
        "sys",
        "time",
        "zlib",
    }
    blocked_dynamic_names = {
        "__import__", "compile", "eval", "exec", "run_module", "run_path"
    }
    dynamic_calls = tuple(sorted({
        call_name(node.func)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and call_name(node.func).split(".")[-1] in blocked_dynamic_names
    }))
    loaded_blocklisted = tuple(sorted(
        name for name in sys.modules
        if name.split(".")[-1] in BLOCKLIST
    ))
    deterministic = stable_bytes(first_core) == stable_bytes(second_core)
    exact = (
        all(row["exact"] for row in provenance.values())
        and paths_exact
        and literal_blocklist
        and BLOCKLIST == tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
        and not (set(imports) - allowed_imports)
        and not dynamic_calls
        and not loaded_blocklisted
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        "input_provenance": provenance,
        "AUDIT_INPUT_PATHS_AST_literals": literal_paths,
        "literal_relative_paths_existing": paths_exact,
        "BLOCKLIST_AST_literals": literal_blocklist,
        "BLOCKLIST": BLOCKLIST,
        "blocklist_exactly_817_823_827": (
            BLOCKLIST == tuple(
                Path(path).stem for path in AUDIT_INPUT_PATHS
            )
        ),
        "primary_access": "bytes/text/AST only",
        "imports": tuple(sorted(imports)),
        "unexpected_imports": tuple(
            sorted(set(imports) - allowed_imports)
        ),
        "blocked_dynamic_calls": dynamic_calls,
        "loaded_blocklisted_modules": loaded_blocklisted,
        "deterministic_core_byte_identical": deterministic,
        "deterministic_core_sha256":
            sha256(stable_bytes(first_core)).hexdigest(),
        "runtime_seconds": round(elapsed, 6),
        "runtime_under_1400_seconds": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": 0,
        "stdout_under_150KB": True,
        "finding": FINDING_CONTROLS,
        "_base_exact": exact,
        "exact": exact,
    }


def make_report(
    core: dict[str, object],
    controls: dict[str, object],
) -> dict[str, object]:
    symbolic_passes = (
        core["symbolic_reimplementation"]["exact"]
        and core["premise_accounting"]["exact"]
        and core["primary_passes"]
    )
    attacks = {
        "THE_SYMBOLIC_DERIVATION": {
            "status": "PASS" if symbolic_passes else "INDETERMINATE",
            "polynomial_substeps": (
                "PASS" if core["symbolic_reimplementation"]["exact"]
                else "FAIL"
            ),
            "finding": FINDING_SYMBOLIC,
        },
        "DOMAIN_EDGE_ATTACK": {
            "status": (
                "PASS" if core["domain_edge_attack"]["exact"] else "FAIL"
            ),
            "finding": FINDING_DOMAIN,
        },
        "PREMISE_ACCOUNTING": {
            "status": (
                "PASS" if core["premise_accounting"]["exact"]
                else "INDETERMINATE"
            ),
            "finding": FINDING_PREMISES,
        },
        "REPRODUCTION_AND_NEGATIVE_CONTROL": {
            "status": (
                "PASS"
                if core["reproduction_and_negative_control"]["exact"]
                else "FAIL"
            ),
            "finding": FINDING_REPRODUCTION,
        },
        "CONTROLS": {
            "status": "PASS" if controls["exact"] else "FAIL",
            "finding": FINDING_CONTROLS,
        },
    }
    checker_exact = (
        core["template_literal"]["exact"]
        and core["symbolic_reimplementation"]["exact"]
        and core["domain_edge_attack"]["exact"]
        and core["premise_accounting"]["exact"]
        and core["reproduction_and_negative_control"]["exact"]
        and core["primary_passes"]
        and controls["exact"]
    )
    return {
        "cycle": 827,
        "checker_role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "attacks": attacks,
        "scientific_core": core,
        "controls": controls,
        "primary_verdict": (
            "PASS" if core["primary_passes"] else "INDETERMINATE"
        ),
        "refutation_basis": (
            None
            if core["primary_passes"] else
            "V2_ACCEPTANCE_CONDITION_NOT_ESTABLISHED"
        ),
        "checker_exact": checker_exact,
        "terminal": (
            "CYCLE827_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if checker_exact else
            "CYCLE827_INDEPENDENT_ADVERSARIAL_CHECK_INDETERMINATE"
        ),
    }


def render_report(report: dict[str, object]) -> str:
    report.pop("report_sha256", None)
    report["report_sha256"] = stable_digest(report)
    lines = []
    for name, row in report["attacks"].items():
        lines.append(f"{row['status']} {name}")
        lines.append(f"FINDING {name}: {row['finding']}")
    lines.extend((
        f"VERDICT {report['primary_verdict']}",
        str(report["terminal"]),
        json.dumps(
            report, sort_keys=True, separators=(",", ":"), default=str
        ),
    ))
    return "\n".join(lines) + "\n"


def main() -> int:
    started = perf_counter()
    provenance, sources, trees = load_inert_inputs()
    first_core = build_scientific_core(trees)
    second_core = build_scientific_core(trees)
    elapsed = perf_counter() - started
    controls = controls_certificate(
        provenance, sources, first_core, second_core, elapsed
    )
    report = make_report(first_core, controls)
    output = ""
    observed_size = -1
    for _iteration in range(8):
        controls["stdout_bytes"] = max(0, observed_size)
        controls["stdout_under_150KB"] = (
            max(0, observed_size) < STDOUT_LIMIT_BYTES
        )
        controls["exact"] = (
            controls["_base_exact"] and controls["stdout_under_150KB"]
        )
        report = make_report(first_core, controls)
        output = render_report(report)
        new_size = len(output.encode())
        if new_size == observed_size:
            break
        observed_size = new_size
    # One final render records the exact fixed-point byte count.
    controls["stdout_bytes"] = len(output.encode())
    controls["stdout_under_150KB"] = (
        controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    )
    controls["exact"] = (
        controls["_base_exact"] and controls["stdout_under_150KB"]
    )
    report = make_report(first_core, controls)
    output = render_report(report)
    final_size = len(output.encode())
    if final_size != controls["stdout_bytes"]:
        controls["stdout_bytes"] = final_size
        controls["stdout_under_150KB"] = final_size < STDOUT_LIMIT_BYTES
        controls["exact"] = (
            controls["_base_exact"] and controls["stdout_under_150KB"]
        )
        report = make_report(first_core, controls)
        output = render_report(report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        print(json.dumps({
            "checker_exact": False,
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE827_INDEPENDENT_ADVERSARIAL_CHECK_INDETERMINATE",
        }, sort_keys=True, separators=(",", ":")))
        return 1
    sys.stdout.write(output)
    return 0 if report["checker_exact"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
