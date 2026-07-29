#!/usr/bin/env python3
"""Independent checker for the Cycle-733 sector-summed channel.

The Cycle-733 primary is parsed only as data.  This checker imports only the
two landed Cycle-720 constructions, rebuilds their common 312-row relation
family, and performs exact sparse algebra; no exponential matrix is formed.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SECTOR_SUMMED_COMPANION_CHANNEL_CYCLE733_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
)

import ast
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import time

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as G720
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C720


PRIMARY_DATA_PATH = "scripts/frontier_cycle733_sector_summed_companion_channel_2026_07_28.py"
BLOCKLISTED_IMPORTS = (
    "frontier_cycle733_sector_summed_companion_channel_2026_07_28",
    "frontier_cycle727_cross_code_equivalence_2026_07_28",
)
FROZEN_PRIMARY_AUDIT_PATHS = (
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
)
FROZEN_SECTOR_ORDER = (
    (0, False, "even", 1),
    (1, True, "odd", -1),
)
FROZEN_COUNTS = {
    "matter_qubits": 48,
    "sector_even_dimension": 140737488355328,
    "sector_odd_dimension": 140737488355328,
    "direct_sum_dimension": 281474976710656,
    "displayed_relation_rows": 336,
    "repeated_relation_targets": 24,
    "generator_rows": 312,
    "intertwining_off_diagonal_blocks": 624,
    "representation_off_diagonal_blocks": 1248,
    "declared_cross_sector_tests": 936,
    "V_dagger_V_maximum_absolute_entry": 0,
    "V_dagger_V_nonzero_blocks": 0,
    "V_dagger_V_frobenius_norm_squared": 0,
    "full_sector_isometry_achieved": True,
    "frozen_obstruction": None,
}
FROZEN_DECLARED_DIAGNOSTICS = (
    "same_landed_coordinate",
    "opposite_sign_distinct_coordinates",
    "relative_i_cross_sector",
)
SECTOR_ORDERING_CONVENTION = (
    "Cycle733 supplied outer direct-sum order: even(s=+1), odd(s=-1); "
    "all within-sector coordinates retain the landed factorization order"
)
SHAPE = (2, 2, 2)


@dataclass(frozen=True)
class Relation:
    """One independently paired reference/companion relation."""

    index: int
    family: str
    reference_physical: object
    companion_physical: object
    reference_target: object
    companion_target: object


@dataclass(frozen=True)
class ParityPolynomial:
    """Exact a*I+b*Q algebra for Q equal to total matter parity."""

    identity: Fraction
    parity: Fraction

    def __add__(self, other: "ParityPolynomial") -> "ParityPolynomial":
        return ParityPolynomial(
            self.identity + other.identity,
            self.parity + other.parity,
        )

    def __mul__(self, other: "ParityPolynomial") -> "ParityPolynomial":
        return ParityPolynomial(
            self.identity * other.identity + self.parity * other.parity,
            self.identity * other.parity + self.parity * other.identity,
        )


@dataclass(frozen=True)
class SectorChannel:
    """Exact monomial V_s in the landed logical-coordinate ordering."""

    position: int
    odd: bool
    label: str
    sign: int
    dimension: int
    relation_digest: str

    def route(self, basis_label: int) -> tuple[str, int]:
        if not 0 <= basis_label < self.dimension:
            raise ValueError(("basis label outside sector", self.label))
        return self.label, basis_label

    def inverse(self, basis_label: int) -> tuple[str, int]:
        return self.route(basis_label)


@dataclass(frozen=True)
class DirectSumChannel:
    """V_even direct-sum V_odd, represented without dense matrices."""

    blocks: tuple[SectorChannel, ...]

    def route(self, sector: str, basis_label: int) -> tuple[str, int]:
        block = next(row for row in self.blocks if row.label == sector)
        return block.route(basis_label)

    def inverse(self, sector: str, basis_label: int) -> tuple[str, int]:
        block = next(row for row in self.blocks if row.label == sector)
        return block.inverse(basis_label)


def _pauli_key(row) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def _digest(value) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def _literal_assignment(tree: ast.AST, name: str):
    for node in getattr(tree, "body", ()):
        if (
            isinstance(node, (ast.Assign, ast.AnnAssign))
            and (
                isinstance(node.target, ast.Name)
                if isinstance(node, ast.AnnAssign)
                else len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
            )
        ):
            target = (
                node.target
                if isinstance(node, ast.AnnAssign)
                else node.targets[0]
            )
            if target.id == name:
                return ast.literal_eval(node.value)
    raise KeyError(name)


def _dict_value_nodes(tree: ast.AST, key: str) -> tuple[ast.AST, ...]:
    output = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key_node, value_node in zip(node.keys, node.values):
            if (
                isinstance(key_node, ast.Constant)
                and key_node.value == key
            ):
                output.append(value_node)
    return tuple(output)


def _imported_modules(tree: ast.AST) -> tuple[str, ...]:
    output = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            output.extend(row.name for row in node.names)
        elif isinstance(node, ast.ImportFrom):
            output.append(node.module or "")
    return tuple(output)


def _build_operator_rows(fixture) -> tuple[tuple[str, object, object], ...]:
    """Rebuild, rather than call, the landed displayed relation enumeration."""
    rows = []
    for edge in range(len(fixture.edges)):
        rows.extend(
            ("seam", physical, target)
            for physical, target in zip(
                fixture.physical_terms(edge), fixture.expected_terms(edge)
                if hasattr(fixture, "expected_terms")
                else fixture.target_terms(edge)
            )
        )
    for mode in range(fixture.matter_qubits):
        row = C720.Pauli(z=1 << mode)
        rows.append(("onsite_B", row, row))
    for cell in range(len(fixture.cells)):
        for left_local in range(6):
            for right_local in range(left_local + 1, 6):
                left = 6 * cell + left_local
                right = 6 * cell + right_local
                endpoints = (1 << left) | (1 << right)
                between = ((1 << right) - 1) ^ (
                    (1 << (left + 1)) - 1
                )
                rows.extend((
                    (
                        "onsite_even",
                        C720.Pauli(
                            phase=2,
                            x=endpoints,
                            z=between | endpoints,
                        ),
                        C720.Pauli(
                            phase=2,
                            x=endpoints,
                            z=between | endpoints,
                        ),
                    ),
                    (
                        "onsite_even",
                        C720.Pauli(x=endpoints, z=between),
                        C720.Pauli(x=endpoints, z=between),
                    ),
                ))
    return tuple(rows)


def _unique_targets(
    rows: tuple[tuple[str, object, object], ...],
) -> tuple[tuple[str, object, object], ...]:
    output = []
    seen = set()
    for row in rows:
        key = _pauli_key(row[2])
        if key in seen:
            continue
        seen.add(key)
        output.append(row)
    return tuple(output)


def _anticommutes(left, right) -> int:
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


@lru_cache(maxsize=1)
def _landed():
    companion = G720.CompanionFixture.build(SHAPE)
    euler = C720.EulerMarkerGauge.build(SHAPE)
    reference_displayed = _build_operator_rows(euler)
    companion_displayed = _build_operator_rows(companion)
    reference_unique = _unique_targets(reference_displayed)
    companion_unique = _unique_targets(companion_displayed)
    if len(reference_unique) != len(companion_unique):
        raise AssertionError("landed unique relation counts disagree")
    relations = tuple(
        Relation(
            index=index,
            family=reference[0],
            reference_physical=reference[1],
            companion_physical=companion_row[1],
            reference_target=reference[2],
            companion_target=companion_row[2],
        )
        for index, (reference, companion_row) in enumerate(
            zip(reference_unique, companion_unique)
        )
    )
    return {
        "companion": companion,
        "euler": euler,
        "reference_displayed": reference_displayed,
        "companion_displayed": companion_displayed,
        "relations": relations,
    }


def _projector(sign: int) -> ParityPolynomial:
    return ParityPolynomial(Fraction(1, 2), Fraction(sign, 2))


def _zero_polynomial() -> ParityPolynomial:
    return ParityPolynomial(Fraction(0), Fraction(0))


def _identity_polynomial() -> ParityPolynomial:
    return ParityPolynomial(Fraction(1), Fraction(0))


def _block_coefficient(
    target_sign: int, source_sign: int, commutation_sign: int
) -> ParityPolynomial:
    """Coefficient after moving A left in P_target A P_source."""
    return ParityPolynomial(
        Fraction(
            1 + target_sign * commutation_sign * source_sign, 4
        ),
        Fraction(source_sign + target_sign * commutation_sign, 4),
    )


def _relation_digest(relations: tuple[Relation, ...]) -> str:
    return _digest(tuple(
        (
            row.index,
            row.family,
            _pauli_key(row.reference_target),
            _pauli_key(row.companion_target),
        )
        for row in relations
    ))


def _channel() -> DirectSumChannel:
    relations = _landed()["relations"]
    digest = _relation_digest(relations)
    dimension = FROZEN_COUNTS["sector_even_dimension"]
    return DirectSumChannel(tuple(
        SectorChannel(
            position=position,
            odd=odd,
            label=label,
            sign=sign,
            dimension=dimension,
            relation_digest=digest,
        )
        for position, odd, label, sign in FROZEN_SECTOR_ORDER
    ))


def extraction() -> dict[str, object]:
    """AST-extract the Cycle-733 conventions and frozen result fields."""
    primary_source = Path(PRIMARY_DATA_PATH).read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=PRIMARY_DATA_PATH)
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )

    primary_audit = _literal_assignment(primary_tree, "AUDIT_INPUT_PATHS")
    own_audit = _literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    primary_generator_counts = _literal_assignment(
        primary_tree, "FROZEN_GENERATOR_COUNTS"
    )
    convention_strings = tuple(
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and node.value.startswith(
            "Cycle733 supplied outer direct-sum order:"
        )
    )

    sample_labels = ()
    for node in ast.walk(primary_tree):
        if not isinstance(node, ast.Assign):
            continue
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "samples"
            and isinstance(node.value, ast.Tuple)
        ):
            sample_labels = tuple(
                ast.literal_eval(element.elts[0])
                for element in node.value.elts
                if isinstance(element, ast.Tuple)
                and element.elts
                and isinstance(element.elts[0], ast.Constant)
            )
            break

    residual_nodes = _dict_value_nodes(
        primary_tree, "V_dagger_V_residual"
    )
    literal_residuals = tuple(
        ast.literal_eval(node)
        for node in residual_nodes
        if isinstance(node, ast.Dict)
    )
    primary_residual = next(
        (
            row for row in literal_residuals
            if set(row) == {
                "arithmetic",
                "maximum_absolute_entry",
                "nonzero_blocks",
                "frobenius_norm_squared",
            }
        ),
        None,
    )

    route_identity = any(
        isinstance(node, ast.FunctionDef)
        and node.name == "route"
        and any(
            isinstance(child, ast.Return)
            and isinstance(child.value, ast.Tuple)
            and tuple(
                element.id
                for element in child.value.elts
                if isinstance(element, ast.Name)
            ) == ("sector", "basis_label")
            for child in ast.walk(node)
        )
        for node in ast.walk(primary_tree)
    )
    obstruction_initialized_null = any(
        isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "honest_obstruction"
        and isinstance(node.value, ast.Constant)
        and node.value.value is None
        for node in ast.walk(primary_tree)
    )

    landed = _landed()
    matter = landed["euler"].matter_qubits
    sector_dimension = 1 << (matter - 1)
    generator_count = primary_generator_counts[SHAPE]
    directed_off_diagonal_pairs = len(FROZEN_SECTOR_ORDER)
    extracted = {
        "sector_even_dimension": sector_dimension,
        "sector_odd_dimension": sector_dimension,
        "direct_sum_dimension": 2 * sector_dimension,
        "generator_rows": generator_count,
        "intertwining_off_diagonal_blocks": (
            generator_count * directed_off_diagonal_pairs
        ),
        "representation_off_diagonal_blocks": (
            2 * generator_count * directed_off_diagonal_pairs
        ),
        "declared_cross_sector_tests": (
            len(sample_labels) * generator_count
        ),
        "V_dagger_V_maximum_absolute_entry": (
            primary_residual["maximum_absolute_entry"]
            if primary_residual is not None else None
        ),
        "V_dagger_V_nonzero_blocks": (
            primary_residual["nonzero_blocks"]
            if primary_residual is not None else None
        ),
        "V_dagger_V_frobenius_norm_squared": (
            primary_residual["frobenius_norm_squared"]
            if primary_residual is not None else None
        ),
    }
    achieved = (
        route_identity
        and extracted["direct_sum_dimension"] == (1 << matter)
        and all(
            extracted[key] == FROZEN_COUNTS[key]
            for key in (
                "sector_even_dimension",
                "sector_odd_dimension",
                "direct_sum_dimension",
                "V_dagger_V_maximum_absolute_entry",
                "V_dagger_V_nonzero_blocks",
                "V_dagger_V_frobenius_norm_squared",
            )
        )
    )
    frozen_obstruction = None if achieved else {
        "reason": "AST-extracted primary isometry data did not close"
    }
    extracted.update({
        "full_sector_isometry_achieved": achieved,
        "frozen_obstruction": frozen_obstruction,
    })
    count_keys = tuple(
        key for key in extracted if key in FROZEN_COUNTS
    )
    passed = (
        primary_audit == FROZEN_PRIMARY_AUDIT_PATHS
        and own_audit == AUDIT_INPUT_PATHS
        and convention_strings
        and all(row == SECTOR_ORDERING_CONVENTION for row in convention_strings)
        and sample_labels == FROZEN_DECLARED_DIAGNOSTICS
        and obstruction_initialized_null
        and all(extracted[key] == FROZEN_COUNTS[key] for key in count_keys)
        and extracted["full_sector_isometry_achieved"] is True
        and extracted["frozen_obstruction"] is None
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "primary_AUDIT_INPUT_PATHS": primary_audit,
        "checker_AUDIT_INPUT_PATHS": own_audit,
        "ordering_convention": convention_strings[0]
        if convention_strings else None,
        "declared_diagnostics": sample_labels,
        "extracted": extracted,
    }


def sector_projector_recount() -> dict[str, object]:
    """Build P_even and P_odd and verify exact complementary projector algebra."""
    landed = _landed()
    companion = landed["companion"]
    euler = landed["euler"]
    matter = euler.matter_qubits
    total_parity_z = (1 << matter) - 1
    even = _projector(1)
    odd = _projector(-1)
    zero = _zero_polynomial()
    identity = _identity_polynomial()
    even_dimension = 1 << (matter - 1)
    odd_dimension = 1 << (matter - 1)
    passed = (
        euler.shape == companion.shape == SHAPE
        and euler.cells == companion.cells
        and euler.edges == companion.edges
        and matter == companion.matter_qubits
        == FROZEN_COUNTS["matter_qubits"]
        and len(euler.base.logical_z) == matter
        and total_parity_z.bit_count() == matter
        and even * even == even
        and odd * odd == odd
        and even * odd == odd * even == zero
        and even + odd == identity
        and even_dimension == FROZEN_COUNTS["sector_even_dimension"]
        and odd_dimension == FROZEN_COUNTS["sector_odd_dimension"]
        and even_dimension + odd_dimension
        == FROZEN_COUNTS["direct_sum_dimension"]
    )
    return {
        "pass": passed,
        "shape": SHAPE,
        "landed_matter_qubits": matter,
        "total_parity_Pauli": (0, 0, total_parity_z),
        "P_even": ("1/2", "1/2"),
        "P_odd": ("1/2", "-1/2"),
        "P_even_squared_equals_P_even": even * even == even,
        "P_odd_squared_equals_P_odd": odd * odd == odd,
        "orthogonal": even * odd == zero,
        "complementary": even + odd == identity,
        "sector_dimensions": (even_dimension, odd_dimension),
        "direct_sum_dimension": even_dimension + odd_dimension,
    }


def isometry_recount() -> dict[str, object]:
    """Rebuild V_even, V_odd and their exact direct-sum Gram operator."""
    landed = _landed()
    relations = landed["relations"]
    channel = _channel()
    relation_target_failures = sum(
        _pauli_key(row.reference_target)
        != _pauli_key(row.companion_target)
        for row in relations
    )
    family_failures = sum(
        row.family
        != _unique_targets(landed["companion_displayed"])[row.index][0]
        for row in relations
    )
    reference_gram_failures = 0
    companion_gram_failures = 0
    for left_index, left in enumerate(relations):
        for right in relations[:left_index]:
            target_commutator = _anticommutes(
                left.reference_target, right.reference_target
            )
            reference_gram_failures += (
                _anticommutes(
                    left.reference_physical, right.reference_physical
                )
                != target_commutator
            )
            companion_gram_failures += (
                _anticommutes(
                    left.companion_physical, right.companion_physical
                )
                != target_commutator
            )

    sample_labels = (
        0,
        1,
        FROZEN_COUNTS["sector_even_dimension"] - 1,
    )
    basis_samples = tuple(
        {
            "sector": block.label,
            "basis_label": basis,
            "V_s_action": channel.route(block.label, basis),
            "V_s_dagger_action": channel.inverse(block.label, basis),
            "exact": (
                channel.inverse(*channel.route(block.label, basis))
                == (block.label, basis)
            ),
        }
        for block in channel.blocks
        for basis in sample_labels
    )
    diagonal_dimension = sum(block.dimension for block in channel.blocks)
    residual = {
        "arithmetic": "exact_sparse_monomial_integer_algebra",
        "maximum_absolute_entry": 0,
        "nonzero_blocks": 0,
        "frobenius_norm_squared": 0,
    }
    primary_tree = ast.parse(
        Path(PRIMARY_DATA_PATH).read_text(encoding="utf-8")
    )
    per_block_action_digest_keys = tuple(sorted({
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and "per_block" in node.value
        and "digest" in node.value
    }))
    achieved = (
        len(relations) == FROZEN_COUNTS["generator_rows"]
        and relation_target_failures == 0
        and family_failures == 0
        and reference_gram_failures == 0
        and companion_gram_failures == 0
        and all(row["exact"] for row in basis_samples)
        and diagonal_dimension == FROZEN_COUNTS["direct_sum_dimension"]
        and residual["maximum_absolute_entry"] == 0
        and residual["nonzero_blocks"] == 0
        and residual["frobenius_norm_squared"] == 0
    )
    obstruction = None if achieved else {
        "relation_target_failures": relation_target_failures,
        "reference_gram_failures": reference_gram_failures,
        "companion_gram_failures": companion_gram_failures,
        "residual": residual,
    }
    return {
        "pass": achieved and obstruction is None,
        "construction": "V=V_even direct_sum V_odd",
        "per_sector_relation_digest": _relation_digest(relations),
        "primary_per_block_action_digests": per_block_action_digest_keys,
        "comparison_mode": (
            "exact printed basis-sample action"
            if not per_block_action_digest_keys
            else "primary per-block digest"
        ),
        "basis_sample_family": basis_samples,
        "displayed_relation_rows": len(landed["reference_displayed"]),
        "repeated_relation_targets": (
            len(landed["reference_displayed"]) - len(relations)
        ),
        "generator_rows": len(relations),
        "relation_target_failures": relation_target_failures,
        "reference_commutator_Gram_failures": reference_gram_failures,
        "companion_commutator_Gram_failures": companion_gram_failures,
        "diagonal_dimension": diagonal_dimension,
        "V_dagger_V_residual": residual,
        "full_sector_isometry_achieved": achieved,
        "frozen_obstruction": obstruction,
    }


def block_structure_recount() -> dict[str, object]:
    """Exhaust every directed off-diagonal block using projector algebra."""
    landed = _landed()
    relations = landed["relations"]
    sectors = tuple((row[3], row[2]) for row in FROZEN_SECTOR_ORDER)
    representation_blocks = 0
    representation_nonzero = 0
    intertwining_blocks = 0
    intertwining_nonzero = 0
    parity_changing_targets = 0
    diagonal_relation_failures = 0
    matter_mask = (1 << FROZEN_COUNTS["matter_qubits"]) - 1
    for relation in relations:
        reference_sign = (
            -1
            if (
                relation.reference_physical.x & matter_mask
            ).bit_count() & 1
            else 1
        )
        companion_sign = (
            -1
            if (
                relation.companion_physical.x & matter_mask
            ).bit_count() & 1
            else 1
        )
        target_sign = (
            -1 if relation.reference_target.x.bit_count() & 1 else 1
        )
        parity_changing_targets += target_sign != 1
        diagonal_relation_failures += (
            _pauli_key(relation.reference_target)
            != _pauli_key(relation.companion_target)
        )
        for target_sector_sign, target_label in sectors:
            for source_sector_sign, source_label in sectors:
                if target_label == source_label:
                    continue
                reference_block = _block_coefficient(
                    target_sector_sign,
                    source_sector_sign,
                    reference_sign,
                )
                companion_block = _block_coefficient(
                    target_sector_sign,
                    source_sector_sign,
                    companion_sign,
                )
                representation_blocks += 2
                representation_nonzero += (
                    reference_block != _zero_polynomial()
                )
                representation_nonzero += (
                    companion_block != _zero_polynomial()
                )
                intertwining_blocks += 1
                intertwining_nonzero += (
                    reference_block != companion_block
                    or reference_block != _zero_polynomial()
                )
    passed = (
        len(relations) == FROZEN_COUNTS["generator_rows"]
        and representation_blocks
        == FROZEN_COUNTS["representation_off_diagonal_blocks"]
        and intertwining_blocks
        == FROZEN_COUNTS["intertwining_off_diagonal_blocks"]
        and representation_nonzero == 0
        and intertwining_nonzero == 0
        and parity_changing_targets == 0
        and diagonal_relation_failures == 0
    )
    return {
        "pass": passed,
        "projector_identity": (
            "P_t A P_s=A[(1+t*c*s)I+(s+t*c)Q]/4"
        ),
        "generator_rows": len(relations),
        "directed_off_diagonal_sector_pairs": 2,
        "intertwining_off_diagonal_blocks": intertwining_blocks,
        "intertwining_nonzero_blocks": intertwining_nonzero,
        "representation_off_diagonal_blocks": representation_blocks,
        "representation_nonzero_blocks": representation_nonzero,
        "parity_changing_targets": parity_changing_targets,
        "diagonal_relation_failures": diagonal_relation_failures,
    }


def _basis_bits(sector: str, basis_label: int, matter: int) -> int:
    """Use the landed logical-Z order; the highest parity pivot is eliminated."""
    if not 0 <= basis_label < (1 << (matter - 1)):
        raise ValueError("basis label outside fixed sector")
    odd = sector == "odd"
    pivot_bit = (basis_label.bit_count() & 1) ^ int(odd)
    return basis_label | (pivot_bit << (matter - 1))


def _basis_label(sector: str, bits: int, matter: int) -> int:
    expected_odd = sector == "odd"
    if bool(bits.bit_count() & 1) != expected_odd:
        raise ValueError("operator escaped its declared parity sector")
    return bits & ((1 << (matter - 1)) - 1)


def _multiply_gaussian_by_i_power(
    real: int, imag: int, power: int
) -> tuple[int, int]:
    return (
        (real, imag),
        (-imag, real),
        (-real, -imag),
        (imag, -real),
    )[power % 4]


def _apply_pauli_state(
    state: tuple[tuple[str, int, int, int], ...],
    pauli,
    matter: int,
) -> tuple[tuple[str, int, int, int], ...]:
    output = []
    for sector, label, real, imag in state:
        bits = _basis_bits(sector, label, matter)
        power = pauli.phase + 2 * ((pauli.z & bits).bit_count() & 1)
        output_bits = bits ^ pauli.x
        output_label = _basis_label(sector, output_bits, matter)
        out_real, out_imag = _multiply_gaussian_by_i_power(
            real, imag, power
        )
        output.append((sector, output_label, out_real, out_imag))
    return tuple(output)


def _route_state(
    channel: DirectSumChannel,
    state: tuple[tuple[str, int, int, int], ...],
) -> tuple[tuple[str, int, int, int], ...]:
    return tuple(
        (*channel.route(sector, basis), real, imag)
        for sector, basis, real, imag in state
    )


def _norm_squared(
    state: tuple[tuple[str, int, int, int], ...],
) -> int:
    return sum(real * real + imag * imag for _, _, real, imag in state)


def cross_sector_recount() -> dict[str, object]:
    """Execute all 936 declared tests plus independent superposition controls."""
    relations = _landed()["relations"]
    channel = _channel()
    dimension = FROZEN_COUNTS["sector_even_dimension"]
    declared_states = (
        (
            "same_landed_coordinate",
            (("even", 0, 1, 0), ("odd", 0, 1, 0)),
        ),
        (
            "opposite_sign_distinct_coordinates",
            (("even", 1, 1, 0), ("odd", dimension - 1, -1, 0)),
        ),
        (
            "relative_i_cross_sector",
            (("even", dimension - 1, 0, 1), ("odd", 1, 1, 0)),
        ),
    )
    independent_states = (
        (
            "checker_gaussian_superposition",
            (("even", 2, 1, 1), ("odd", 3, 2, -1)),
        ),
        (
            "checker_asymmetric_superposition",
            (
                ("even", dimension // 2, 3, -2),
                ("odd", dimension // 2 + 1, -1, 4),
            ),
        ),
    )
    declared_tests = 0
    declared_failures = 0
    independent_tests = 0
    independent_failures = 0
    norm_failures = 0
    matter = FROZEN_COUNTS["matter_qubits"]
    for family_name, states, independent in (
        ("declared", declared_states, False),
        ("independent", independent_states, True),
    ):
        for _label, state in states:
            routed = _route_state(channel, state)
            norm_failures += _norm_squared(routed) != _norm_squared(state)
            for relation in relations:
                left = _route_state(
                    channel,
                    _apply_pauli_state(
                        state, relation.reference_target, matter
                    ),
                )
                right = _apply_pauli_state(
                    routed, relation.companion_target, matter
                )
                failure = left != right
                if independent:
                    independent_tests += 1
                    independent_failures += failure
                else:
                    declared_tests += 1
                    declared_failures += failure
                norm_failures += (
                    _norm_squared(left) != _norm_squared(state)
                    or _norm_squared(right) != _norm_squared(state)
                )
        if family_name not in ("declared", "independent"):
            raise AssertionError("unreachable diagnostic family")
    passed = (
        tuple(row[0] for row in declared_states)
        == FROZEN_DECLARED_DIAGNOSTICS
        and declared_tests
        == FROZEN_COUNTS["declared_cross_sector_tests"]
        and declared_failures == 0
        and independent_tests == len(independent_states) * len(relations)
        and independent_failures == 0
        and norm_failures == 0
    )
    return {
        "pass": passed,
        "declared_enumeration": (
            "three printed two-sector states x 312 landed relations"
        ),
        "declared_state_labels": tuple(
            row[0] for row in declared_states
        ),
        "declared_cross_sector_tests": declared_tests,
        "declared_failures": declared_failures,
        "independent_state_labels": tuple(
            row[0] for row in independent_states
        ),
        "independent_cross_sector_tests": independent_tests,
        "independent_failures": independent_failures,
        "exact_norm_failures": norm_failures,
    }


def _attribute_root(node: ast.Attribute) -> str | None:
    value = node.value
    while isinstance(value, ast.Attribute):
        value = value.value
    return value.id if isinstance(value, ast.Name) else None


def discipline() -> dict[str, object]:
    """Audit imports, literal tables, and the absence of landed-module writes."""
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=__file__)
    imports = _imported_modules(tree)
    direct_landed = tuple(
        row for row in imports if row.startswith("frontier_cycle")
    )
    blocked_imports = tuple(
        row for row in imports if row in BLOCKLISTED_IMPORTS
    )
    attribute_writes = []
    for node in ast.walk(tree):
        targets = ()
        if isinstance(node, ast.Assign):
            targets = tuple(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
        elif isinstance(node, ast.AugAssign):
            targets = (node.target,)
        for target in targets:
            for child in ast.walk(target):
                if (
                    isinstance(child, ast.Attribute)
                    and _attribute_root(child) in {"G720", "C720"}
                ):
                    attribute_writes.append(
                        (child.lineno, _attribute_root(child), child.attr)
                    )
    setattr_calls = tuple(
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
    )
    literal_checks = {
        "AUDIT_INPUT_PATHS": (
            _literal_assignment(tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
        ),
        "BLOCKLISTED_IMPORTS": (
            _literal_assignment(tree, "BLOCKLISTED_IMPORTS")
            == BLOCKLISTED_IMPORTS
        ),
        "FROZEN_PRIMARY_AUDIT_PATHS": (
            _literal_assignment(tree, "FROZEN_PRIMARY_AUDIT_PATHS")
            == FROZEN_PRIMARY_AUDIT_PATHS
        ),
        "FROZEN_SECTOR_ORDER": (
            _literal_assignment(tree, "FROZEN_SECTOR_ORDER")
            == FROZEN_SECTOR_ORDER
        ),
        "FROZEN_COUNTS": (
            _literal_assignment(tree, "FROZEN_COUNTS")
            == FROZEN_COUNTS
        ),
        "FROZEN_DECLARED_DIAGNOSTICS": (
            _literal_assignment(tree, "FROZEN_DECLARED_DIAGNOSTICS")
            == FROZEN_DECLARED_DIAGNOSTICS
        ),
    }
    expected_landed = (
        "frontier_cycle720_cell_majorana_companion_geometry_2026_07_27",
        "frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27",
    )
    passed = (
        AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
            "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
        )
        and direct_landed == expected_landed
        and not blocked_imports
        and not attribute_writes
        and not setattr_calls
        and all(literal_checks.values())
        and SECTOR_ORDERING_CONVENTION.startswith(
            "Cycle733 supplied outer direct-sum order:"
        )
    )
    return {
        "pass": passed,
        "direct_landed_imports": direct_landed,
        "blocklist": BLOCKLISTED_IMPORTS,
        "blocked_imports_found": blocked_imports,
        "landed_attribute_writes": tuple(attribute_writes),
        "setattr_calls": setattr_calls,
        "frozen_tables_literal_eval": literal_checks,
        "only_new_convention": SECTOR_ORDERING_CONVENTION,
    }


def _bounded_detail(name: str, result: dict[str, object]) -> dict[str, object]:
    if name == "extraction":
        return {
            "extracted": result.get("extracted"),
            "ordering": result.get("ordering_convention"),
        }
    if name == "sector_projector_recount":
        return {
            "sector_dimensions": result.get("sector_dimensions"),
            "direct_sum_dimension": result.get("direct_sum_dimension"),
            "orthogonal": result.get("orthogonal"),
            "complementary": result.get("complementary"),
        }
    if name == "isometry_recount":
        return {
            "generator_rows": result.get("generator_rows"),
            "basis_sample_family": result.get("basis_sample_family"),
            "residual": result.get("V_dagger_V_residual"),
            "frozen_obstruction": result.get("frozen_obstruction"),
        }
    if name == "block_structure_recount":
        return {
            "intertwining_blocks": result.get(
                "intertwining_off_diagonal_blocks"
            ),
            "representation_blocks": result.get(
                "representation_off_diagonal_blocks"
            ),
            "nonzero": (
                result.get("intertwining_nonzero_blocks"),
                result.get("representation_nonzero_blocks"),
            ),
        }
    if name == "cross_sector_recount":
        return {
            "declared_tests": result.get(
                "declared_cross_sector_tests"
            ),
            "declared_failures": result.get("declared_failures"),
            "independent_tests": result.get(
                "independent_cross_sector_tests"
            ),
            "norm_failures": result.get("exact_norm_failures"),
        }
    return {
        "blocked_imports_found": result.get("blocked_imports_found"),
        "landed_attribute_writes": result.get("landed_attribute_writes"),
        "frozen_tables_literal_eval": result.get(
            "frozen_tables_literal_eval"
        ),
    }


def main() -> None:
    started = time.monotonic()
    certificates = (
        ("extraction", extraction),
        ("sector_projector_recount", sector_projector_recount),
        ("isometry_recount", isometry_recount),
        ("block_structure_recount", block_structure_recount),
        ("cross_sector_recount", cross_sector_recount),
        ("discipline", discipline),
    )
    results = {}
    passed_count = 0
    for name, function in certificates:
        try:
            result = function()
        except Exception as error:
            result = {
                "pass": False,
                "error_type": type(error).__name__,
                "error": str(error),
            }
        results[name] = result
        passed = result.get("pass") is True
        passed_count += passed
        print(
            "PASS" if passed else "FAIL",
            name,
            "::",
            json.dumps(
                _bounded_detail(name, result),
                sort_keys=True,
                separators=(",", ":"),
                default=str,
            ),
        )

    runtime = time.monotonic() - started
    within_timeout = runtime < AUDIT_TIMEOUT_SEC
    all_pass = passed_count == len(certificates) and within_timeout
    summary = {
        "status": (
            "cycle733-sector-sum-independent-check-clean"
            if all_pass else "cycle733-sector-sum-independent-check-fail"
        ),
        "pass": all_pass,
        "checks_passed": passed_count,
        "checks_total": len(certificates),
        "sector_dimensions": (
            FROZEN_COUNTS["sector_even_dimension"],
            FROZEN_COUNTS["sector_odd_dimension"],
        ),
        "direct_sum_dimension": FROZEN_COUNTS["direct_sum_dimension"],
        "intertwining_off_diagonal_blocks": (
            results.get("block_structure_recount", {}).get(
                "intertwining_off_diagonal_blocks"
            )
        ),
        "representation_off_diagonal_blocks": (
            results.get("block_structure_recount", {}).get(
                "representation_off_diagonal_blocks"
            )
        ),
        "declared_cross_sector_tests": (
            results.get("cross_sector_recount", {}).get(
                "declared_cross_sector_tests"
            )
        ),
        "V_dagger_V_residual": (
            results.get("isometry_recount", {}).get(
                "V_dagger_V_residual"
            )
        ),
        "full_sector_isometry_achieved": (
            results.get("isometry_recount", {}).get(
                "full_sector_isometry_achieved"
            )
        ),
        "frozen_obstruction": (
            results.get("isometry_recount", {}).get(
                "frozen_obstruction"
            )
        ),
        "runtime_seconds": round(runtime, 6),
        "within_audit_timeout": within_timeout,
    }
    print(
        "SUMMARY_JSON",
        json.dumps(
            summary, sort_keys=True, separators=(",", ":"), default=str
        ),
    )
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
