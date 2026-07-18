#!/usr/bin/env python3
"""Factorized Peres--Mermin reference census with an explicit host firewall.

This is the lightweight predecessor to a fully routed physical geometry.  It
enumerates every two-qubit stabilizer basis, Peres--Mermin context, compatible
measurement order, and candidate sign history.  Two implementations are kept
deliberately separate:

* the oracle uses the compact tableau algebra;
* the factorized evaluator consumes only retained physical truth tables and
  role decoders.

The factorized evaluator does not prove that the corresponding devices have
already been jointly routed.  It proves the finite interface semantics that
the later routed construction must realize without host-supplied products,
commutation bits, membership bits, updates, or parity answers.

The imported component tables were populated by their predecessor modules
from algebraic reference values before this script installs its dynamic
firewall.  The firewall therefore certifies composition after those tables
exist; it is not a certificate of oracle-free component-table synthesis.
"""

from __future__ import annotations

import ast
import inspect
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import wraps
from itertools import permutations, product
from pathlib import Path
from typing import Callable, Optional

import binary_xor_and_record_alu_probe_2026_07_15 as alu
import cycle48_symplectic_tableau_compression_probe_2026_07_15 as tableau
import factorized_commuting_signed_membership_probe_2026_07_16 as old_membership
import physical_commuting_row_multiplication_probe_2026_07_15 as mult
import physical_four_case_pivot_router_probe_2026_07_15 as pivot
import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as joint
import physical_row_role_literal_fanout_probe_2026_07_15 as fanout
import physical_symplectic_commutation_circuit_probe_2026_07_15 as commute
import total_status_serial_reject_selector_cycle93_2026_07_15 as status


Row = tuple[int, int, int, int, int]
Basis = tuple[Row, Row]
ContextRows = tuple[Row, Row, Row]
Order = tuple[int, int, int]
Bits = tuple[int, int, int]

PLUS_II: Row = (0, 0, 0, 0, 0)
MINUS_II: Row = (0, 0, 0, 0, 1)
ROWS: tuple[Row, ...] = tuple(product((0, 1), repeat=5))  # type: ignore[assignment]
ORDERS: tuple[Order, ...] = tuple(permutations(range(3)))  # type: ignore[assignment]
BIT_TRIPLES: tuple[Bits, ...] = tuple(product((0, 1), repeat=3))  # type: ignore[assignment]
SIGNED_MEASUREMENTS = tuple(
    (
        measurement_id,
        outcome_bit,
        tableau.measurement_row(measurement_id, outcome_bit),
    )
    for measurement_id in range(15)
    for outcome_bit in (0, 1)
)

PM_CONTEXTS = (
    ("R1", (11, 2, 14), 0),
    ("R2", (0, 3, 4), 0),
    ("R3", (12, 6, 9), 0),
    ("C1", (11, 0, 12), 0),
    ("C2", (2, 3, 6), 0),
    ("C3", (14, 4, 9), 1),
)

H0 = status.H0
H1 = status.H1
ROLE_BIT = {H0: 0, H1: 1}

PASS = 0
FAIL = 0
PROVENANCE: Counter[str] = Counter()
FORBIDDEN_CALL_COUNTS: Counter[str] = Counter()
FORBIDDEN_CALL_ORDER = (
    "tableau.symplectic",
    "tableau.multiply_commuting",
    "tableau.tableau_measure",
    "pivot.pivot_rows",
    "old_membership.membership_bits",
)
GEOMETRY_REPRESENTATIVES: dict[
    tuple[tuple[str, str, str], int, int, int],
    tuple[int, int, int, int, Bits],
] = {}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


@dataclass
class FailureBook:
    totals: Counter[str] = field(default_factory=Counter)
    samples: dict[str, list[object]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def add(self, category: str, detail: object) -> None:
        self.totals[category] += 1
        if len(self.samples[category]) < 10:
            self.samples[category].append(detail)

    @property
    def total(self) -> int:
        return sum(self.totals.values())


@dataclass(frozen=True)
class StageResult:
    c1: int
    c2: int
    member: int
    support: int
    updated: Basis
    stage_type: str


@dataclass(frozen=True)
class CheckerResult:
    unsigned_product: Row
    unsigned_sign: int
    scalar_parity: int
    full_product: Row
    binds: tuple[int, int, int]
    unsigned_sources: tuple[int, int, int]
    unsigned_identity: int
    parity_ok: int
    full_ok: int


@dataclass(frozen=True)
class TranscriptResult:
    support_prefix: tuple[int, int, int]
    first_reject: Optional[int]
    final_generators: Basis
    checker: CheckerResult
    terminal: int
    stage_types: tuple[str, str, str]


@dataclass(frozen=True)
class OracleResult:
    support: bool
    first_reject: Optional[int]
    final_group: Optional[tuple[Row, Row, Row]]
    probabilities: tuple[float, ...]
    weight: Optional[Fraction]


@dataclass
class PrimitiveTables:
    boolean: dict[tuple[int, int, int], int] = field(default_factory=dict)
    status: dict[tuple[int, int, int], int] = field(default_factory=dict)
    row_bits: dict[Row, tuple[int, int, int, int, int]] = field(
        default_factory=dict
    )
    equality4: dict[tuple[Row, Row], int] = field(default_factory=dict)
    equality5: dict[tuple[Row, Row], int] = field(default_factory=dict)
    commutation: dict[tuple[Row, Row], int] = field(default_factory=dict)
    products: dict[tuple[Row, Row], Row] = field(default_factory=dict)
    stages: dict[tuple[Row, Row, Row], StageResult] = field(
        default_factory=dict
    )
    checkers: dict[
        tuple[ContextRows, ContextRows],
        CheckerResult,
    ] = field(default_factory=dict)


def lookup(kind: str, table: dict, key):
    PROVENANCE[kind] += 1
    return table[key]


def install_dynamic_firewall() -> None:
    targets = (
        (tableau, "symplectic", "tableau.symplectic"),
        (tableau, "multiply_commuting", "tableau.multiply_commuting"),
        (tableau, "tableau_measure", "tableau.tableau_measure"),
        (pivot, "pivot_rows", "pivot.pivot_rows"),
        (old_membership, "membership_bits", "old_membership.membership_bits"),
    )
    for module, attribute, label in targets:
        original = getattr(module, attribute)

        @wraps(original)
        def counted(*args, __original=original, __label=label, **kwargs):
            FORBIDDEN_CALL_COUNTS[__label] += 1
            return __original(*args, **kwargs)

        setattr(module, attribute, counted)


def firewall_snapshot() -> tuple[int, ...]:
    return tuple(FORBIDDEN_CALL_COUNTS[label] for label in FORBIDDEN_CALL_ORDER)


def static_firewall_failures() -> tuple[object, ...]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_names = {
        "symplectic",
        "multiply_commuting",
        "tableau_measure",
        "pivot_rows",
        "membership_bits",
        "group_key",
        "STATE_GENERATORS",
        "BRANCH",
    }
    failures: list[object] = []
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not (
            node.name.startswith("physical_")
            or node.name == "factorized_transcript"
        ):
            continue
        for child in ast.walk(node):
            if isinstance(child, ast.Name) and child.id in forbidden_names:
                failures.append((node.name, "forbidden-name", child.id))
            if (
                isinstance(child, ast.Attribute)
                and child.attr in forbidden_names
            ):
                failures.append((node.name, "forbidden-attribute", child.attr))
            if (
                isinstance(child, ast.BinOp)
                and isinstance(child.op, (ast.BitXor, ast.BitAnd, ast.BitOr))
            ):
                failures.append((node.name, "host-bit-operation"))
            if (
                node.name.startswith("physical_equal")
                and isinstance(child, ast.Compare)
                and any(
                    isinstance(operator, (ast.In, ast.NotIn, ast.Eq, ast.NotEq))
                    for operator in child.ops
                )
            ):
                failures.append((node.name, "host-equality-operation"))
    return tuple(failures)


# ---------------------------------------------------------------------------
# Factorized physical-table evaluator.
# ---------------------------------------------------------------------------


def physical_row_bits_uncached(
    row: Row,
) -> tuple[int, int, int, int, int]:
    bits = []
    for bit_index in range(5):
        role = lookup(
            "reader",
            fanout.CANONICAL_TABLE,
            fanout.local(row, bit_index),
        )
        bits.append(ROLE_BIT[role])
    return tuple(bits)  # type: ignore[return-value]


def physical_alu_uncached(left: int, right: int, operation: int) -> int:
    role = lookup(
        "alu",
        alu.CANONICAL_TABLE,
        alu.alu_local(left, right, operation),
    )
    return ROLE_BIT[role]


def physical_xor(left: int, right: int, tables: PrimitiveTables) -> int:
    return tables.boolean[(left, right, 0)]


def physical_and(left: int, right: int, tables: PrimitiveTables) -> int:
    return tables.boolean[(left, right, 1)]


def physical_or(left: int, right: int, tables: PrimitiveTables) -> int:
    first = physical_xor(left, right, tables)
    second = physical_and(left, right, tables)
    return physical_xor(first, second, tables)


def physical_not(value: int, tables: PrimitiveTables) -> int:
    return physical_xor(value, 1, tables)


def physical_and_chain(
    values: tuple[int, ...],
    tables: PrimitiveTables,
) -> int:
    result = 1
    for value in values:
        result = physical_and(result, value, tables)
    return result


def physical_parity4_uncached(
    values: tuple[int, int, int, int],
) -> int:
    records = {
        site: alu.bit(value)
        for site, value in zip(commute.TERMS, values, strict=True)
    }
    records.update({site: commute.FRAME for site in commute.FRAMES})
    signature = commute.c53.canonical_signature(
        commute.c53.local_signature(records, commute.CENTER)
    )
    return ROLE_BIT[lookup("parity", commute.PARITY_TABLE, signature)]


def physical_symplectic_uncached(
    left: Row,
    right: Row,
    tables: PrimitiveTables,
) -> int:
    left_bits = tables.row_bits[left]
    right_bits = tables.row_bits[right]
    terms = (
        physical_and(left_bits[0], right_bits[2], tables),
        physical_and(left_bits[2], right_bits[0], tables),
        physical_and(left_bits[1], right_bits[3], tables),
        physical_and(left_bits[3], right_bits[1], tables),
    )
    return physical_parity4_uncached(terms)


def physical_multiply_uncached(
    left: Row,
    right: Row,
) -> Optional[Row]:
    signature = mult.local(left, right)
    role = mult.CANONICAL_TABLE.get(signature)
    if role is None:
        return None
    PROVENANCE["multiply"] += 1
    return mult.five.ROLE_ROW[role]


def physical_status_step_uncached(
    previous: int,
    candidate: int,
    reference: int,
) -> int:
    records = {
        (-1, 1, 0): alu.bit(previous),
        (0, 0, 0): alu.bit(candidate),
        (0, 2, 0): alu.bit(reference),
        (0, 1, 1): H0,
        (0, 1, -1): H1,
    }
    signature = status.c53.canonical_signature(
        status.c53.local_signature(records, (0, 1, 0))
    )
    return ROLE_BIT[lookup("status", status.STATUS_TABLE, signature)]


def physical_equal_bits(
    candidate_bits: tuple[int, int, int, int, int],
    reference_bits: tuple[int, int, int, int, int],
    width: int,
    tables: PrimitiveTables,
) -> int:
    current = 1
    for bit_index in range(width):
        current = tables.status[
            (current, candidate_bits[bit_index], reference_bits[bit_index])
        ]
    return current


def physical_case_role(c1: int, c2: int):
    return lookup("case", pivot.CASE_TABLE, pivot.case_local(c1, c2))


def physical_joint_route_uncached(
    c1: int,
    c2: int,
    g1: Row,
    g2: Row,
    measured: Row,
    product_row: Row,
) -> Basis:
    case_role = physical_case_role(c1, c2)
    selector1 = lookup(
        "selector",
        joint.INTEGRATED_SELECTOR_TABLE,
        joint.integrated_selector_local(case_role, 2),
    )
    selector2 = lookup(
        "selector",
        joint.INTEGRATED_SELECTOR_TABLE,
        joint.integrated_selector_local(case_role, 3),
    )
    branch_index = {
        pivot.SEL_L1_G1: 0,
        pivot.SEL_L1_P: 1,
        pivot.SEL_L2_G2: 0,
        pivot.SEL_L2_P: 1,
        pivot.SEL_L2_PRODUCT: 2,
    }
    candidates1 = (g1, measured)
    candidates2 = (g2, measured, product_row)
    selected1 = candidates1[branch_index[selector1]]
    selected2 = candidates2[branch_index[selector2]]
    output1 = lookup(
        "gate",
        joint.INTEGRATED_GATE_TABLE,
        joint.integrated_gate_local(
            selector1,
            mult.five.ROW_ROLE[selected1],
            branch_index[selector1],
            2,
        ),
    )
    output2 = lookup(
        "gate",
        joint.INTEGRATED_GATE_TABLE,
        joint.integrated_gate_local(
            selector2,
            mult.five.ROW_ROLE[selected2],
            branch_index[selector2],
            3,
        ),
    )
    return mult.five.ROLE_ROW[output1], mult.five.ROLE_ROW[output2]


def physical_stage_uncached(
    generators: Basis,
    measured: Row,
    tables: PrimitiveTables,
) -> StageResult:
    g1, g2 = generators
    c1 = tables.commutation[(g1, measured)]
    c2 = tables.commutation[(g2, measured)]
    product_row = tables.products[(g2, g1)]
    updated = physical_joint_route_uncached(
        c1,
        c2,
        g1,
        g2,
        measured,
        product_row,
    )
    equalities = (
        tables.equality5[(measured, g1)],
        tables.equality5[(measured, g2)],
        tables.equality5[(measured, product_row)],
    )
    member = physical_or(
        physical_or(equalities[0], equalities[1], tables),
        equalities[2],
        tables,
    )
    anti = physical_or(c1, c2, tables)
    support = physical_or(anti, member, tables)
    if anti:
        stage_type = "A" + str(c1) + str(c2)
    elif member:
        stage_type = "D+"
    else:
        stage_type = "D-"
    return StageResult(c1, c2, member, support, updated, stage_type)


def physical_checker_uncached(
    ordered_unsigned_rows: ContextRows,
    ordered_signed_rows: ContextRows,
    tables: PrimitiveTables,
) -> CheckerResult:
    unsigned_first = tables.products[
        (ordered_unsigned_rows[0], ordered_unsigned_rows[1])
    ]
    unsigned_product = tables.products[
        (unsigned_first, ordered_unsigned_rows[2])
    ]
    full_first = tables.products[
        (ordered_signed_rows[0], ordered_signed_rows[1])
    ]
    full_product = tables.products[(full_first, ordered_signed_rows[2])]
    signs = (
        tables.row_bits[ordered_signed_rows[0]][4],
        tables.row_bits[ordered_signed_rows[1]][4],
        tables.row_bits[ordered_signed_rows[2]][4],
    )
    scalar_parity = physical_xor(
        physical_xor(signs[0], signs[1], tables),
        signs[2],
        tables,
    )
    binds = (
        tables.equality4[(ordered_signed_rows[0], ordered_unsigned_rows[0])],
        tables.equality4[(ordered_signed_rows[1], ordered_unsigned_rows[1])],
        tables.equality4[(ordered_signed_rows[2], ordered_unsigned_rows[2])],
    )
    unsigned_sources = (
        physical_not(tables.row_bits[ordered_unsigned_rows[0]][4], tables),
        physical_not(tables.row_bits[ordered_unsigned_rows[1]][4], tables),
        physical_not(tables.row_bits[ordered_unsigned_rows[2]][4], tables),
    )
    unsigned_identity = tables.equality4[(unsigned_product, PLUS_II)]
    unsigned_sign = tables.row_bits[unsigned_product][4]
    parity_ok = tables.status[(1, scalar_parity, unsigned_sign)]
    full_ok = tables.equality5[(full_product, PLUS_II)]
    return CheckerResult(
        unsigned_product,
        unsigned_sign,
        scalar_parity,
        full_product,
        binds,
        unsigned_sources,
        unsigned_identity,
        parity_ok,
        full_ok,
    )


def factorized_transcript(
    initial_basis: Basis,
    ordered_unsigned_rows: ContextRows,
    ordered_signed_rows: ContextRows,
    tables: PrimitiveTables,
) -> TranscriptResult:
    generators = initial_basis
    prefix = 1
    prefixes = []
    stage_types = []
    first_reject = None
    for step_index, measured in enumerate(ordered_signed_rows, 1):
        stage = tables.stages[(generators[0], generators[1], measured)]
        prefix = physical_and(prefix, stage.support, tables)
        prefixes.append(prefix)
        stage_types.append(stage.stage_type)
        if first_reject is None and prefix == 0:
            first_reject = step_index
        generators = stage.updated
    checker = tables.checkers[
        (ordered_unsigned_rows, ordered_signed_rows)
    ]
    terminal_inputs = (
        prefix,
        *checker.binds,
        *checker.unsigned_sources,
        checker.unsigned_identity,
        checker.parity_ok,
        checker.full_ok,
    )
    terminal = physical_and_chain(terminal_inputs, tables)
    return TranscriptResult(
        tuple(prefixes),  # type: ignore[arg-type]
        first_reject,
        generators,
        checker,
        terminal,
        tuple(stage_types),  # type: ignore[arg-type]
    )


# ---------------------------------------------------------------------------
# Independent tableau oracle.
# ---------------------------------------------------------------------------


def oracle_transcript(
    initial_basis: Basis,
    measurement_ids: tuple[int, int, int],
    order: Order,
    bits: Bits,
) -> OracleResult:
    generators = initial_basis
    probabilities = []
    for step_index, slot in enumerate(order, 1):
        probability, target = tableau.tableau_measure(
            generators,
            measurement_ids[slot],
            bits[slot],
        )
        probabilities.append(float(probability))
        if probability == 0:
            return OracleResult(
                False,
                step_index,
                None,
                tuple(probabilities),
                None,
            )
        generators = tableau.STATE_GENERATORS[target]
    random_steps = sum(probability == 0.5 for probability in probabilities)
    return OracleResult(
        True,
        None,
        tableau.group_key(*generators),
        tuple(probabilities),
        Fraction(1, 2**random_steps),
    )


def oracle_products(
    ordered_unsigned_rows: ContextRows,
    ordered_signed_rows: ContextRows,
) -> tuple[Row, int, Row]:
    unsigned_product = tableau.multiply_commuting(
        tableau.multiply_commuting(
            ordered_unsigned_rows[0],
            ordered_unsigned_rows[1],
        ),
        ordered_unsigned_rows[2],
    )
    full_product = tableau.multiply_commuting(
        tableau.multiply_commuting(
            ordered_signed_rows[0],
            ordered_signed_rows[1],
        ),
        ordered_signed_rows[2],
    )
    scalar_parity = sum(row[4] for row in ordered_signed_rows) % 2
    return unsigned_product, scalar_parity, full_product


def build_host_domain():
    bases_by_state = tuple(
        tuple(tableau.all_bases(state_id))
        for state_id in range(60)
    )
    context_rows = tuple(
        tuple(
            tableau.measurement_row(measurement_id, 1)
            for measurement_id in measurement_ids
        )
        for _label, measurement_ids, _expected_sign in PM_CONTEXTS
    )
    return bases_by_state, context_rows


def build_primitive_tables(
    bases_by_state: tuple[tuple[Basis, ...], ...],
    context_rows: tuple[ContextRows, ...],
) -> PrimitiveTables:
    tables = PrimitiveTables()
    for left, right, operation in product((0, 1), repeat=3):
        tables.boolean[(left, right, operation)] = physical_alu_uncached(
            left,
            right,
            operation,
        )
    for previous, candidate, reference in product((0, 1), repeat=3):
        tables.status[(previous, candidate, reference)] = (
            physical_status_step_uncached(previous, candidate, reference)
        )
    for row in ROWS:
        tables.row_bits[row] = physical_row_bits_uncached(row)
    for candidate in ROWS:
        for reference in ROWS:
            candidate_bits = tables.row_bits[candidate]
            reference_bits = tables.row_bits[reference]
            tables.equality4[(candidate, reference)] = physical_equal_bits(
                candidate_bits,
                reference_bits,
                4,
                tables,
            )
            tables.equality5[(candidate, reference)] = physical_equal_bits(
                candidate_bits,
                reference_bits,
                5,
                tables,
            )
            tables.commutation[(candidate, reference)] = (
                physical_symplectic_uncached(candidate, reference, tables)
            )
            product_row = physical_multiply_uncached(candidate, reference)
            if product_row is not None:
                tables.products[(candidate, reference)] = product_row
    for state_bases in bases_by_state:
        for g1, g2 in state_bases:
            for _measurement_id, _outcome_bit, measured in SIGNED_MEASUREMENTS:
                tables.stages[(g1, g2, measured)] = physical_stage_uncached(
                    (g1, g2),
                    measured,
                    tables,
                )
    for context_index, unsigned_rows in enumerate(context_rows):
        _label, measurement_ids, _expected_sign = PM_CONTEXTS[context_index]
        for order in ORDERS:
            ordered_unsigned = tuple(
                unsigned_rows[slot] for slot in order
            )
            for bits in BIT_TRIPLES:
                signed_rows = tuple(
                    tableau.measurement_row(measurement_id, bits[slot])
                    for slot, measurement_id in enumerate(measurement_ids)
                )
                ordered_signed = tuple(signed_rows[slot] for slot in order)
                key = (ordered_unsigned, ordered_signed)
                tables.checkers[key] = physical_checker_uncached(
                    ordered_unsigned,  # type: ignore[arg-type]
                    ordered_signed,  # type: ignore[arg-type]
                    tables,
                )
    return tables


def stage_preflight(
    bases_by_state: tuple[tuple[Basis, ...], ...],
    tables: PrimitiveTables,
    failures: FailureBook,
) -> Counter[str]:
    census: Counter[str] = Counter()
    for state_id, state_bases in enumerate(bases_by_state):
        for basis_index, basis in enumerate(state_bases):
            for measurement_id, outcome_bit, measured in SIGNED_MEASUREMENTS:
                stage = tables.stages[(basis[0], basis[1], measured)]
                probability, target = tableau.tableau_measure(
                    basis,
                    measurement_id,
                    outcome_bit,
                )
                census["attempt"] += 1
                census["support" if stage.support else "reject"] += 1
                anti = bool(stage.c1 or stage.c2)
                census["anticommuting" if anti else "commuting"] += 1
                if not anti:
                    census["member" if stage.member else "opposite"] += 1
                if bool(stage.support) != bool(probability):
                    failures.add(
                        "stage-support",
                        (
                            state_id,
                            basis_index,
                            measurement_id,
                            outcome_bit,
                            stage,
                            probability,
                        ),
                    )
                if probability:
                    physical_group = tableau.group_key(*stage.updated)
                    oracle_group = tableau.group_key(
                        *tableau.STATE_GENERATORS[target]
                    )
                    if physical_group != oracle_group:
                        failures.add(
                            "stage-update",
                            (
                                state_id,
                                basis_index,
                                measurement_id,
                                outcome_bit,
                                physical_group,
                                oracle_group,
                            ),
                        )
    return census


def checker_preflight(
    context_rows: tuple[ContextRows, ...],
    tables: PrimitiveTables,
    failures: FailureBook,
) -> Counter[str]:
    census: Counter[str] = Counter()
    unsigned_products = Counter()
    for context_index, unsigned_rows in enumerate(context_rows):
        _label, measurement_ids, _expected_sign = PM_CONTEXTS[context_index]
        for order in ORDERS:
            ordered_unsigned = tuple(
                unsigned_rows[slot] for slot in order
            )
            first_checker = None
            for bits in BIT_TRIPLES:
                signed_rows = tuple(
                    tableau.measurement_row(measurement_id, bits[slot])
                    for slot, measurement_id in enumerate(measurement_ids)
                )
                ordered_signed = tuple(signed_rows[slot] for slot in order)
                checker = tables.checkers[
                    (ordered_unsigned, ordered_signed)
                ]
                if first_checker is None:
                    first_checker = checker
                    unsigned_products[checker.unsigned_product] += 1
                census["attempt"] += 1
                census[
                    "parity_equal"
                    if checker.parity_ok
                    else "parity_different"
                ] += 1
                census[
                    "full_plus"
                    if checker.full_product == PLUS_II
                    else "full_minus"
                ] += 1
                if not (
                    checker.binds == (1, 1, 1)
                    and checker.unsigned_sources == (1, 1, 1)
                    and checker.unsigned_identity == 1
                ):
                    failures.add(
                        "checker-input-contract",
                        (context_index, order, bits, checker),
                    )
    census["unsigned_plus"] = unsigned_products[PLUS_II]
    census["unsigned_minus"] = unsigned_products[MINUS_II]
    return census


def compact_result_signature(
    physical: TranscriptResult,
    physical_group: Optional[tuple[Row, Row, Row]],
):
    return (
        physical.support_prefix[-1],
        physical.checker.unsigned_product,
        physical.checker.scalar_parity,
        physical.checker.full_product,
        physical.terminal,
        physical_group,
    )


def run_exhaustive(
    bases_by_state: tuple[tuple[Basis, ...], ...],
    context_rows: tuple[ContextRows, ...],
    tables: PrimitiveTables,
    failures: FailureBook,
):
    global GEOMETRY_REPRESENTATIVES
    global_census: Counter[object] = Counter()
    context_census: dict[str, Counter[object]] = {
        label: Counter() for label, _ids, _sign in PM_CONTEXTS
    }
    context_order_census: dict[tuple[str, int], Counter[str]] = {
        (label, order_index): Counter()
        for label, _ids, _sign in PM_CONTEXTS
        for order_index in range(len(ORDERS))
    }
    basis_comparisons = 0
    order_comparisons = 0
    stage_shapes = set()
    combined_shapes = set()
    GEOMETRY_REPRESENTATIVES = {}

    for state_id, state_bases in enumerate(bases_by_state):
        basis_reference = {}
        for basis_index, basis in enumerate(state_bases):
            for context_index, unsigned_rows in enumerate(context_rows):
                label, measurement_ids, expected_unsigned_sign = (
                    PM_CONTEXTS[context_index]
                )
                order_reference = {}
                for order_index, order in enumerate(ORDERS):
                    ordered_unsigned = tuple(
                        unsigned_rows[slot] for slot in order
                    )
                    for bits in BIT_TRIPLES:
                        signed_rows = tuple(
                            tableau.measurement_row(
                                measurement_id,
                                bits[slot],
                            )
                            for slot, measurement_id in enumerate(
                                measurement_ids
                            )
                        )
                        ordered_signed = tuple(
                            signed_rows[slot] for slot in order
                        )
                        oracle = oracle_transcript(
                            basis,
                            measurement_ids,
                            order,
                            bits,
                        )
                        before = firewall_snapshot()
                        physical = factorized_transcript(
                            basis,
                            ordered_unsigned,  # type: ignore[arg-type]
                            ordered_signed,  # type: ignore[arg-type]
                            tables,
                        )
                        after = firewall_snapshot()
                        key = (
                            state_id,
                            basis_index,
                            context_index,
                            order_index,
                            bits,
                        )
                        if before != after:
                            failures.add(
                                "dynamic-firewall",
                                (key, before, after),
                            )

                        oracle_unsigned, oracle_q, oracle_full = (
                            oracle_products(
                                ordered_unsigned,  # type: ignore[arg-type]
                                ordered_signed,  # type: ignore[arg-type]
                            )
                        )
                        physical_group = (
                            tableau.group_key(*physical.final_generators)
                            if physical.support_prefix[-1]
                            else None
                        )

                        checker = physical.checker
                        if checker.binds != (1, 1, 1):
                            failures.add("binding", (key, checker.binds))
                        if checker.unsigned_sources != (1, 1, 1):
                            failures.add(
                                "unsigned-source",
                                (key, checker.unsigned_sources),
                            )
                        if checker.unsigned_product != oracle_unsigned:
                            failures.add(
                                "unsigned-product",
                                (
                                    key,
                                    checker.unsigned_product,
                                    oracle_unsigned,
                                ),
                            )
                        if checker.unsigned_product[:4] != PLUS_II[:4]:
                            failures.add(
                                "unsigned-nonidentity",
                                (key, checker.unsigned_product),
                            )
                        if checker.unsigned_sign != expected_unsigned_sign:
                            failures.add(
                                "unsigned-context-sign",
                                (
                                    key,
                                    checker.unsigned_sign,
                                    expected_unsigned_sign,
                                ),
                            )
                        if checker.scalar_parity != oracle_q:
                            failures.add(
                                "scalar-parity",
                                (
                                    key,
                                    checker.scalar_parity,
                                    oracle_q,
                                ),
                            )
                        if checker.full_product != oracle_full:
                            failures.add(
                                "full-product",
                                (
                                    key,
                                    checker.full_product,
                                    oracle_full,
                                ),
                            )
                        expected_full = (
                            PLUS_II
                            if checker.parity_ok
                            else MINUS_II
                        )
                        if checker.full_product != expected_full:
                            failures.add(
                                "full-parity-relation",
                                (
                                    key,
                                    checker.full_product,
                                    expected_full,
                                ),
                            )
                        if physical.first_reject != oracle.first_reject:
                            failures.add(
                                "first-reject",
                                (
                                    key,
                                    physical.first_reject,
                                    oracle.first_reject,
                                ),
                            )
                        if bool(physical.support_prefix[-1]) != oracle.support:
                            failures.add(
                                "support",
                                (
                                    key,
                                    physical.support_prefix,
                                    oracle,
                                ),
                            )
                        if bool(physical.terminal) != oracle.support:
                            failures.add(
                                "terminal",
                                (key, physical.terminal, oracle.support),
                            )
                        if oracle.support:
                            if physical_group != oracle.final_group:
                                failures.add(
                                    "final-group",
                                    (
                                        key,
                                        physical_group,
                                        oracle.final_group,
                                    ),
                                )
                            if (
                                len(oracle.probabilities) != 3
                                or oracle.probabilities[2] != 1.0
                            ):
                                failures.add(
                                    "third-deterministic",
                                    (key, oracle.probabilities),
                                )

                        signature = compact_result_signature(
                            physical,
                            physical_group,
                        )
                        basis_key = (context_index, order_index, bits)
                        if basis_index == 0:
                            basis_reference[basis_key] = signature
                        else:
                            basis_comparisons += 1
                            if basis_reference[basis_key] != signature:
                                failures.add(
                                    "basis-invariance",
                                    (
                                        key,
                                        basis_reference[basis_key],
                                        signature,
                                    ),
                                )
                        order_key = bits
                        if order_index == 0:
                            order_reference[order_key] = signature
                        else:
                            order_comparisons += 1
                            if order_reference[order_key] != signature:
                                failures.add(
                                    "order-invariance",
                                    (
                                        key,
                                        order_reference[order_key],
                                        signature,
                                    ),
                                )

                        global_census["attempt"] += 1
                        context_census[label]["attempt"] += 1
                        context_order_census[(label, order_index)][
                            "attempt"
                        ] += 1
                        support_name = (
                            "supported" if oracle.support else "rejected"
                        )
                        global_census[support_name] += 1
                        context_census[label][support_name] += 1
                        context_order_census[(label, order_index)][
                            support_name
                        ] += 1
                        if oracle.first_reject is not None:
                            global_census[
                                ("first_reject", oracle.first_reject)
                            ] += 1
                        relation = (
                            "q_equal_u"
                            if checker.parity_ok
                            else "q_different_u"
                        )
                        global_census[relation] += 1
                        context_census[label][relation] += 1
                        if checker.parity_ok and oracle.support:
                            global_census["q_equal_u_supported"] += 1
                            context_census[label][
                                "q_equal_u_supported"
                            ] += 1
                        if checker.parity_ok and not oracle.support:
                            global_census["q_equal_u_rejected"] += 1
                            context_census[label][
                                "q_equal_u_rejected"
                            ] += 1
                        if not checker.parity_ok and oracle.support:
                            global_census["q_different_u_supported"] += 1
                        global_census[
                            "unsigned_plus"
                            if checker.unsigned_product == PLUS_II
                            else "unsigned_minus"
                        ] += 1
                        global_census[
                            "full_plus"
                            if checker.full_product == PLUS_II
                            else "full_minus"
                        ] += 1
                        global_census["terminal_h1"] += physical.terminal
                        if oracle.support:
                            global_census[
                                "supported_unsigned_plus"
                                if checker.unsigned_product == PLUS_II
                                else "supported_unsigned_minus"
                            ] += 1
                            global_census[
                                "supported_full_plus"
                                if checker.full_product == PLUS_II
                                else "supported_full_minus"
                            ] += 1
                            global_census["third_deterministic"] += int(
                                oracle.probabilities[2] == 1.0
                            )
                            global_census[("weight", oracle.weight)] += 1
                            context_census[label][
                                ("weight", oracle.weight)
                            ] += 1

                        stage_shapes.add(physical.stage_types)
                        combined_shape = (
                            physical.stage_types,
                            checker.unsigned_sign,
                            checker.parity_ok,
                            physical.support_prefix[-1],
                        )
                        combined_shapes.add(combined_shape)
                        GEOMETRY_REPRESENTATIVES.setdefault(
                            combined_shape,
                            key,
                        )

    return (
        global_census,
        context_census,
        context_order_census,
        basis_comparisons,
        order_comparisons,
        stage_shapes,
        combined_shapes,
    )


def geometry_representatives():
    return tuple(
        (shape, GEOMETRY_REPRESENTATIVES[shape])
        for shape in sorted(GEOMETRY_REPRESENTATIVES)
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    failures = FailureBook()

    print("STATIC AND DYNAMIC FIREWALL")
    static_failures = static_firewall_failures()
    check(
        "factorized functions contain no direct forbidden oracle calls or "
        "direct host bit operators",
        not static_failures,
        static_failures[:10],
    )
    expected_signature = (
        "initial_basis",
        "ordered_unsigned_rows",
        "ordered_signed_rows",
        "tables",
    )
    actual_signature = tuple(
        inspect.signature(factorized_transcript).parameters
    )
    check(
        "factorized public signature contains rows and tables only",
        actual_signature == expected_signature,
        actual_signature,
    )
    install_dynamic_firewall()
    bases_by_state, context_rows = build_host_domain()
    check(
        "host enumerates 60 states and 360 ordered bases",
        len(bases_by_state) == 60
        and all(len(state_bases) == 6 for state_bases in bases_by_state)
        and sum(map(len, bases_by_state)) == 360,
        (len(bases_by_state), sum(map(len, bases_by_state))),
    )

    print("\nPHYSICAL-TABLE CACHE BUILD")
    before_build = firewall_snapshot()
    tables = build_primitive_tables(bases_by_state, context_rows)
    after_build = firewall_snapshot()
    check(
        "cache assembly makes zero direct forbidden oracle calls after "
        "component import",
        before_build == after_build,
        (before_build, after_build),
    )
    cache_sizes = (
        len(tables.row_bits),
        len(tables.equality4),
        len(tables.equality5),
        len(tables.commutation),
        len(tables.products),
        len(tables.stages),
        len(tables.checkers),
    )
    check(
        "factorized cache sizes are exact",
        cache_sizes == (32, 1_024, 1_024, 1_024, 544, 10_800, 288),
        cache_sizes,
    )
    check(
        "all physical primitive kinds are exercised",
        set(PROVENANCE)
        >= {
            "reader",
            "alu",
            "parity",
            "multiply",
            "status",
            "case",
            "selector",
            "gate",
        }
        and all(PROVENANCE[kind] > 0 for kind in (
            "reader",
            "alu",
            "parity",
            "multiply",
            "status",
            "case",
            "selector",
            "gate",
        )),
        dict(PROVENANCE),
    )

    print("\nSINGLE-STAGE PREFLIGHT")
    stage_census = stage_preflight(bases_by_state, tables, failures)
    expected_stage = {
        "attempt": 10_800,
        "support": 9_720,
        "reject": 1_080,
        "anticommuting": 8_640,
        "commuting": 2_160,
        "member": 1_080,
        "opposite": 1_080,
    }
    check(
        "all 10,800 factorized stages match the tableau oracle",
        all(stage_census[key] == value for key, value in expected_stage.items())
        and not failures.totals["stage-support"]
        and not failures.totals["stage-update"],
        (dict(stage_census), failures.samples.get("stage-support", [])[:1]),
    )

    print("\nCHECKER PREFLIGHT")
    checker_census = checker_preflight(context_rows, tables, failures)
    expected_checker = {
        "attempt": 288,
        "parity_equal": 144,
        "parity_different": 144,
        "full_plus": 144,
        "full_minus": 144,
        "unsigned_plus": 30,
        "unsigned_minus": 6,
    }
    check(
        "all 288 independent checker cases have corrected semantics",
        all(
            checker_census[key] == value
            for key, value in expected_checker.items()
        )
        and not failures.totals["checker-input-contract"],
        dict(checker_census),
    )

    print("\nFULL 103,680-TRANSCRIPT CENSUS")
    (
        global_census,
        context_census,
        context_order_census,
        basis_comparisons,
        order_comparisons,
        stage_shapes,
        combined_shapes,
    ) = run_exhaustive(bases_by_state, context_rows, tables, failures)

    expected_global = {
        "attempt": 103_680,
        "supported": 38_880,
        "rejected": 64_800,
        ("first_reject", 1): 10_368,
        ("first_reject", 2): 15_552,
        ("first_reject", 3): 38_880,
        "q_equal_u": 51_840,
        "q_different_u": 51_840,
        "q_equal_u_supported": 38_880,
        "q_equal_u_rejected": 12_960,
        "q_different_u_supported": 0,
        "unsigned_plus": 86_400,
        "unsigned_minus": 17_280,
        "full_plus": 51_840,
        "full_minus": 51_840,
        "terminal_h1": 38_880,
        "supported_unsigned_plus": 32_400,
        "supported_unsigned_minus": 6_480,
        "supported_full_plus": 38_880,
        "supported_full_minus": 0,
        "third_deterministic": 38_880,
        ("weight", Fraction(1, 4)): 27_648,
        ("weight", Fraction(1, 2)): 10_368,
        ("weight", Fraction(1, 1)): 864,
    }
    check(
        "global support, parity, product, and weight census is exact",
        all(
            global_census[key] == value
            for key, value in expected_global.items()
        ),
        {
            str(key): global_census[key]
            for key in expected_global
        },
    )

    context_failures = []
    for label, _measurement_ids, _expected_sign in PM_CONTEXTS:
        observed = context_census[label]
        expected = {
            "attempt": 17_280,
            "supported": 6_480,
            "rejected": 10_800,
            "q_equal_u": 8_640,
            "q_different_u": 8_640,
            "q_equal_u_supported": 6_480,
            "q_equal_u_rejected": 2_160,
            ("weight", Fraction(1, 4)): 4_608,
            ("weight", Fraction(1, 2)): 1_728,
            ("weight", Fraction(1, 1)): 144,
        }
        if any(observed[key] != value for key, value in expected.items()):
            context_failures.append(
                (
                    label,
                    {
                        str(key): observed[key]
                        for key in expected
                    },
                )
            )
    check(
        "each of six contexts has the exact same support census",
        not context_failures,
        context_failures[:2],
    )

    context_order_failures = []
    for key, observed in context_order_census.items():
        expected = {
            "attempt": 2_880,
            "supported": 1_080,
            "rejected": 1_800,
        }
        if any(observed[name] != value for name, value in expected.items()):
            context_order_failures.append((key, dict(observed)))
    check(
        "all 36 context-order cells have 2,880/1,080/1,800",
        not context_order_failures,
        context_order_failures[:2],
    )

    print("\nINVARIANCE, SHAPES, AND FIREWALL CLOSE")
    check(
        "basis invariance has 17,280 classes and 86,400 comparisons",
        basis_comparisons == 86_400
        and not failures.totals["basis-invariance"],
        (
            basis_comparisons,
            failures.samples.get("basis-invariance", [])[:1],
        ),
    )
    check(
        "order invariance has 17,280 classes and 86,400 comparisons",
        order_comparisons == 86_400
        and not failures.totals["order-invariance"],
        (
            order_comparisons,
            failures.samples.get("order-invariance", [])[:1],
        ),
    )
    check(
        "38 stage shapes and 76 future-geometry representative keys are "
        "exposed",
        len(stage_shapes) == 38
        and len(combined_shapes) == 76
        and len(geometry_representatives()) == 76,
        (len(stage_shapes), len(combined_shapes)),
    )
    check(
        "no transcript mismatch crossed the physical/oracle boundary",
        failures.total == 0,
        {
            "totals": dict(failures.totals),
            "samples": dict(failures.samples),
        },
    )
    check(
        "old host-supplied membership path was never called",
        FORBIDDEN_CALL_COUNTS["old_membership.membership_bits"] == 0,
        dict(FORBIDDEN_CALL_COUNTS),
    )
    print("REPRESENTATIVE_COUNT", len(geometry_representatives()))
    for shape, key in geometry_representatives():
        print("REPRESENTATIVE", shape, key)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "PERES_MERMIN_FACTORIZED_REFERENCE_CENSUS"
        if FAIL == 0
        else "OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
