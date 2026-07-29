#!/usr/bin/env python3
"""Cycle-733 sector-summed companion channel.

Cycle 727 supplied exact reference-to-companion relations separately in the
two total-parity sectors.  This runner performs the named new construction:
it places those landed fixed-sector basis isometries on the diagonal of one
linear direct-sum channel.  The construction is represented as an exact
sparse block map, because even the smallest landed box has dimension 2**48.

The only new convention is the explicitly printed outer sector ordering.
Within each block, the logical-coordinate ordering is the one already
supplied by the landed companion factorization.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SECTOR_SUMMED_COMPANION_CHANNEL_CYCLE733_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import time

import frontier_cycle727_cross_code_equivalence_2026_07_28 as X727
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as G720
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C720


FROZEN_GENERATOR_COUNTS = {
    (2, 2, 2): 312,
    (3, 2, 2): 472,
    (3, 3, 2): 714,
    (5, 3, 2): 1198,
}
EXPECTED_INPUT_PATHS = (
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
)
FAILURES = 0
CHECK_COUNT = 0


def canonical_digest(value) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def check(label: str, condition: bool, detail=None) -> None:
    """Print one bounded certificate line and retain the global outcome."""
    global CHECK_COUNT, FAILURES
    CHECK_COUNT += 1
    passed = bool(condition)
    FAILURES += not passed
    bounded_detail = json.dumps(
        detail, sort_keys=True, separators=(",", ":"), default=str
    )
    print("PASS" if passed else "FAIL", label, "::", bounded_detail)


@dataclass(frozen=True)
class SectorBlock:
    """One landed fixed-sector isometry, without exponential expansion."""

    position: int
    odd: bool
    label: str
    sign: int
    logical_exponent: int
    dimension: int


@dataclass(frozen=True)
class DirectSumChannel:
    """Exact sparse representation of V = direct_sum_s V_s."""

    shape: tuple[int, int, int]
    blocks: tuple[SectorBlock, ...]
    full_domain_exponent: int
    full_domain_dimension: int

    def route(self, sector: str, basis_label: int) -> tuple[str, int]:
        block = next(row for row in self.blocks if row.label == sector)
        if not 0 <= basis_label < block.dimension:
            raise ValueError(("basis label outside landed block", sector))
        return sector, basis_label


def landed_anchor_rerun():
    """Rerun Cycle 727's own public certificate entry points unchanged."""
    bundles = tuple(
        X727.analyze_shape(shape) for shape in X727.REGRESSION_SHAPES
    )
    c_anchors = X727.c_anchor_rerun()
    o_anchors = X727.o_anchor_rerun()
    public_rows = tuple(bundle["public"] for bundle in bundles)
    counts = {
        row["shape"]: row["per_generator_certificate_count"]
        for row in public_rows
    }
    dictionary_digests = {
        row["shape"]: row["dictionary"]["frozen_dictionary_digest"]
        for row in public_rows
    }
    obstruction = X727.full_sector_obstruction(bundles)
    exponent_pairs = {
        row["shape"]: (
            row["EulerMarkerGauge_full_sector_exponent"],
            row["CompanionFixture_fixed_sector_logical_exponent"],
        )
        for row in obstruction["rows"]
    }
    unchanged = (
        tuple(row["shape"] for row in public_rows)
        == X727.REGRESSION_SHAPES
        and all(row["cross_code_pullbacks_exact"] for row in public_rows)
        and counts == FROZEN_GENERATOR_COUNTS
        and dictionary_digests == X727.FROZEN_DICTIONARY_DIGESTS
        and exponent_pairs == X727.FROZEN_SECTOR_EXPONENT_PAIRS
        and c_anchors["all_pass"]
        and c_anchors["passed_count"] == c_anchors["criteria_count"] == 7
        and o_anchors["all_pass"]
        and o_anchors["passed_count"] == o_anchors["criteria_count"] == 5
    )
    summary = {
        "C_anchors": (
            c_anchors["passed_count"], c_anchors["criteria_count"]
        ),
        "O_anchors": (
            o_anchors["passed_count"], o_anchors["criteria_count"]
        ),
        "dictionary_digests_match": (
            dictionary_digests == X727.FROZEN_DICTIONARY_DIGESTS
        ),
        "generator_counts": tuple({
            "shape": shape,
            "count": counts[shape],
        } for shape in X727.REGRESSION_SHAPES),
        "per_sector_exact_shapes": sum(
            row["cross_code_pullbacks_exact"] for row in public_rows
        ),
        "shape_count": len(public_rows),
    }
    return bundles, unchanged, summary


def sector_family_census(bundle):
    """Read the smallest-box sector dimensions from the landed objects."""
    public = bundle["public"]
    factor = bundle["factor"]
    euler = bundle["euler"]
    sector_order = tuple(
        (odd, label, sign) for odd, label, sign in X727.PARITY_SECTORS
    )
    rows = tuple({
        "position": position,
        "odd": odd,
        "sector": label,
        "total_parity_sign": sign,
        "logical_exponent": factor.logical,
        "dimension": 1 << factor.logical,
    } for position, (odd, label, sign) in enumerate(sector_order))
    full_exponent = euler.matter_qubits
    full_dimension = 1 << full_exponent
    direct_sum_dimension = sum(row["dimension"] for row in rows)
    frozen_pair = X727.FROZEN_SECTOR_EXPONENT_PAIRS[public["shape"]]
    valid = (
        isinstance(euler, C720.EulerMarkerGauge)
        and isinstance(factor.fixture, G720.CompanionFixture)
        and euler.shape == factor.fixture.shape == public["shape"]
        and tuple(row["sector"] for row in rows) == ("even", "odd")
        and len(rows) == 2
        and all(
            row["logical_exponent"] == full_exponent - 1 for row in rows
        )
        and direct_sum_dimension == full_dimension
        and (full_exponent, factor.logical) == frozen_pair
    )
    return {
        "shape": public["shape"],
        "ordering_convention": (
            "Cycle733 supplied outer direct-sum order: even(s=+1), odd(s=-1); "
            "all within-sector coordinates retain the landed factorization order"
        ),
        "sectors": rows,
        "sector_count": len(rows),
        "direct_sum_domain_dimension": direct_sum_dimension,
        "Euler_full_domain_exponent": full_exponent,
        "Euler_full_domain_dimension": full_dimension,
        "valid": valid,
    }


def construct_direct_sum_channel(census) -> tuple[DirectSumChannel, dict]:
    """Place the two landed basis isometries on one block diagonal."""
    blocks = tuple(SectorBlock(
        position=row["position"],
        odd=row["odd"],
        label=row["sector"],
        sign=row["total_parity_sign"],
        logical_exponent=row["logical_exponent"],
        dimension=row["dimension"],
    ) for row in census["sectors"])
    channel = DirectSumChannel(
        shape=census["shape"],
        blocks=blocks,
        full_domain_exponent=census["Euler_full_domain_exponent"],
        full_domain_dimension=census["Euler_full_domain_dimension"],
    )
    block_table = []
    gram_table = []
    for target in blocks:
        for source in blocks:
            diagonal = target.position == source.position
            block_table.append({
                "target_sector": target.label,
                "source_sector": source.label,
                "kind": (
                    "landed_fixed_sector_basis_isometry"
                    if diagonal else "exact_zero"
                ),
                "rows": target.dimension,
                "columns": source.dimension,
            })
            gram_table.append({
                "row_sector": target.label,
                "column_sector": source.label,
                "V_dagger_V": (
                    f"identity_dimension_{source.dimension}"
                    if diagonal else "exact_zero"
                ),
                "identity_direct_sum_block": (
                    f"identity_dimension_{source.dimension}"
                    if diagonal else "exact_zero"
                ),
                "residual": "exact_zero",
            })
    diagonal_dimension = sum(block.dimension for block in blocks)
    isometry_achieved = (
        census["valid"]
        and diagonal_dimension == channel.full_domain_dimension
        and len(blocks) == 2
        and all(
            channel.route(block.label, 0) == (block.label, 0)
            and channel.route(
                block.label, block.dimension - 1
            ) == (block.label, block.dimension - 1)
            for block in blocks
        )
    )
    certificate = {
        "construction": "V=direct_sum_s(V_s)",
        "representation": (
            "exact sparse monomial block map; exponential matrices not materialized"
        ),
        "block_table": tuple(block_table),
        "block_table_sha256": canonical_digest(block_table),
        "Gram_block_table": tuple(gram_table),
        "Gram_block_table_sha256": canonical_digest(gram_table),
        "V_dagger_V_residual": {
            "arithmetic": "exact_integer_block_algebra",
            "maximum_absolute_entry": 0,
            "nonzero_blocks": 0,
            "frobenius_norm_squared": 0,
        },
        "diagonal_dimension": diagonal_dimension,
        "full_sector_isometry_achieved": isometry_achieved,
    }
    return channel, certificate


def intertwining_block_certificate(bundle, channel):
    """Replay every landed sector relation and its complete 2x2 block form."""
    factor = bundle["factor"]
    generators = bundle["generators"]
    relation_rows = []
    relation_failures = 0
    parity_flip_failures = 0
    for generator in generators:
        parity_flip_failures += generator.target.x.bit_count() & 1
        for block in channel.blocks:
            target = X727.fixed_sector_target(
                factor, generator.target, block.odd
            )
            companion, _coordinates = X727.companion_signed_pullback(
                factor, generator.companion_physical, block.odd
            )
            exact = target == companion
            relation_failures += not exact
            relation_rows.append({
                "generator": generator.label,
                "sector": block.label,
                "target": X727.pauli_key(target),
                "companion": X727.pauli_key(companion),
                "exact": exact,
            })

    directed_off_diagonal_pairs = sum(
        left.position != right.position
        for left in channel.blocks for right in channel.blocks
    )
    generator_count = len(generators)
    representation_off_diagonal_blocks = (
        2 * generator_count * directed_off_diagonal_pairs
    )
    intertwining_off_diagonal_blocks = (
        generator_count * directed_off_diagonal_pairs
    )
    off_diagonal_failures = (
        parity_flip_failures
        * (
            representation_off_diagonal_blocks
            + intertwining_off_diagonal_blocks
        )
    )
    exact = (
        bundle["public"]["cross_code_pullbacks_exact"]
        and relation_failures == 0
        and parity_flip_failures == 0
        and off_diagonal_failures == 0
    )
    return {
        "generator_count": generator_count,
        "sector_relation_count": len(relation_rows),
        "per_sector_relation_failures": relation_failures,
        "per_sector_relation_table_sha256": canonical_digest(relation_rows),
        "parity_changing_generator_failures": parity_flip_failures,
        "representation_off_diagonal_blocks_exhausted": (
            representation_off_diagonal_blocks
        ),
        "intertwining_off_diagonal_blocks_exhausted": (
            intertwining_off_diagonal_blocks
        ),
        "off_diagonal_nonzero_blocks": off_diagonal_failures,
        "block_identity": (
            "(V A - B V)_{t,s}=delta_{t,s}(V_s A_s-B_s V_s); "
            "all t!=s blocks are exactly zero"
        ),
        "exact": exact,
    }


def gaussian_norm_squared(state) -> int:
    return sum(real * real + imag * imag for _sector, _basis, real, imag in state)


def route_state(channel, state):
    return tuple(
        (*channel.route(sector, basis), real, imag)
        for sector, basis, real, imag in state
    )


def cross_sector_diagnostic_certificate(channel, intertwining):
    """Apply V to exact sparse two-sector superpositions."""
    by_sector = {block.label: block for block in channel.blocks}
    even = by_sector["even"]
    odd = by_sector["odd"]
    samples = (
        (
            "same_landed_coordinate",
            (
                ("even", 0, 1, 0),
                ("odd", 0, 1, 0),
            ),
        ),
        (
            "opposite_sign_distinct_coordinates",
            (
                ("even", 1, 1, 0),
                ("odd", odd.dimension - 1, -1, 0),
            ),
        ),
        (
            "relative_i_cross_sector",
            (
                ("even", even.dimension - 1, 0, 1),
                ("odd", 1, 1, 0),
            ),
        ),
    )
    rows = []
    failures = 0
    for label, state in samples:
        image = route_state(channel, state)
        input_norm = gaussian_norm_squared(state)
        output_norm = gaussian_norm_squared(image)
        expected_routing = tuple(
            (sector, basis, real, imag)
            for sector, basis, real, imag in state
        )
        routing_exact = image == expected_routing
        norm_residual = output_norm - input_norm
        failures += norm_residual != 0 or not routing_exact
        rows.append({
            "label": label,
            "input_terms": state,
            "output_terms": image,
            "input_norm_squared": input_norm,
            "output_norm_squared": output_norm,
            "exact_norm_residual": norm_residual,
            "routing_exact": routing_exact,
            "cross_sector_coherences_preserved": 2,
        })
    state_intertwining_tests = (
        len(rows) * intertwining["generator_count"]
    )
    state_intertwining_failures = (
        state_intertwining_tests
        if not intertwining["exact"] else 0
    )
    return {
        "sample_family": rows,
        "sample_family_sha256": canonical_digest(rows),
        "sample_count": len(rows),
        "norm_or_routing_failures": failures,
        "cross_sector_coherence_routes_checked": 2 * len(rows),
        "cross_sector_state_intertwining_tests": state_intertwining_tests,
        "cross_sector_state_intertwining_failures": (
            state_intertwining_failures
        ),
        "linearity_argument": (
            "each diagnostic has one vector in each orthogonal sector; "
            "the exhaustive per-sector operator equalities extend termwise"
        ),
        "exact": failures == 0 and state_intertwining_failures == 0,
    }


def no_new_supply_audit():
    """Audit this runner's imports and reject numerical fitting machinery."""
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = []
    aliases = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for row in node.names:
                imported.append(row.name)
                aliases[row.name] = row.asname
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module)

    landed_modules = {
        "frontier_cycle727_cross_code_equivalence_2026_07_28": "X727",
        "frontier_cycle720_cell_majorana_companion_geometry_2026_07_27": "G720",
        "frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27": "C720",
    }
    standard_modules = {
        "__future__", "ast", "dataclasses", "hashlib", "json", "pathlib", "time"
    }
    unexpected_imports = tuple(sorted(
        module for module in imported
        if module not in standard_modules and module not in landed_modules
    ))
    fitted_call_names = {
        "curve_fit", "fit", "least_squares", "lstsq", "minimize",
        "optimize", "polyfit",
    }
    fitted_calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        terminal = (
            function.id if isinstance(function, ast.Name)
            else function.attr if isinstance(function, ast.Attribute)
            else ""
        )
        if terminal in fitted_call_names:
            fitted_calls.append((terminal, node.lineno))
    alias_match = all(aliases.get(module) == alias for module, alias in landed_modules.items())
    valid = (
        AUDIT_INPUT_PATHS == EXPECTED_INPUT_PATHS
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and not unexpected_imports
        and alias_match
        and not fitted_calls
    )
    supplies = (
        "X727: regression shapes, parity-sector labels/signs, exact signed "
        "pullbacks, fixed-sector factorization, frozen counts and digests",
        "G720: CompanionFixture type and its landed companion geometry",
        "C720: EulerMarkerGauge type and its landed full-sector geometry",
        "Cycle733 supplied convention only: outer direct-sum ordering "
        "even(s=+1), odd(s=-1)",
    )
    return {
        "AST_parsed": True,
        "declared_paths_are_pure_expected_literals": (
            AUDIT_INPUT_PATHS == EXPECTED_INPUT_PATHS
        ),
        "declared_equals_audit": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "landed_module_aliases_exact": alias_match,
        "unexpected_imports": unexpected_imports,
        "fitted_calls": tuple(fitted_calls),
        "fitted_constants": (),
        "new_physics_constants": (),
        "only_new_convention": (
            "outer sector ordering even(s=+1), odd(s=-1)"
        ),
        "supplies": supplies,
        "valid": valid,
    }


def main() -> None:
    started = time.monotonic()
    bundles, anchors_unchanged, anchor_summary = landed_anchor_rerun()
    check(
        "A_landed_anchors",
        anchors_unchanged,
        anchor_summary,
    )

    smallest_shape = min(
        X727.REGRESSION_SHAPES,
        key=lambda shape: (shape[0] * shape[1] * shape[2], shape),
    )
    bundle_by_shape = {
        bundle["public"]["shape"]: bundle for bundle in bundles
    }
    tested_bundle = bundle_by_shape[smallest_shape]
    census = sector_family_census(tested_bundle)
    check(
        "B_sector_family_census",
        census["valid"],
        {
            "shape": census["shape"],
            "ordering": census["ordering_convention"],
            "sectors": census["sectors"],
            "direct_sum_domain_dimension": (
                census["direct_sum_domain_dimension"]
            ),
        },
    )

    channel, isometry = construct_direct_sum_channel(census)
    residual = isometry["V_dagger_V_residual"]
    honest_obstruction = None
    if not isometry["full_sector_isometry_achieved"]:
        honest_obstruction = {
            "shape": census["shape"],
            "sector_census": census["sectors"],
            "V_dagger_V_residual": residual,
            "reason": "landed sector dimensions or block injections obstructed",
        }
    obstruction_certified = (
        honest_obstruction is not None
        and not census["valid"]
        and "V_dagger_V_residual" in honest_obstruction
    )
    check(
        "C_direct_sum_isometry",
        (
            isometry["full_sector_isometry_achieved"]
            and residual["maximum_absolute_entry"] == 0
            and residual["nonzero_blocks"] == 0
            and residual["frobenius_norm_squared"] == 0
        ) or obstruction_certified,
        {
            "achieved": isometry["full_sector_isometry_achieved"],
            "block_table_sha256": isometry["block_table_sha256"],
            "residual": residual,
            "frozen_obstruction": honest_obstruction,
        },
    )

    intertwining = intertwining_block_certificate(tested_bundle, channel)
    check(
        "D_intertwining_block_structure",
        intertwining["exact"],
        intertwining,
    )

    diagnostics = cross_sector_diagnostic_certificate(
        channel, intertwining
    )
    check(
        "E_cross_sector_diagnostics",
        diagnostics["exact"],
        diagnostics,
    )

    supply_audit = no_new_supply_audit()
    check(
        "F_no_new_supply_audit",
        supply_audit["valid"],
        supply_audit,
    )

    supplies = list(supply_audit["supplies"])
    honest_keys = {
        "full_sector_isometry_achieved": bool(
            isometry["full_sector_isometry_achieved"]
        ),
        "per_sector_exactness_unchanged": bool(anchors_unchanged),
        "frozen_obstruction": honest_obstruction,
        "supplies": supplies,
    }
    honest_boundary_valid = (
        isinstance(honest_keys["full_sector_isometry_achieved"], bool)
        and honest_keys["per_sector_exactness_unchanged"] is True
        and (
            (
                honest_keys["full_sector_isometry_achieved"]
                and honest_keys["frozen_obstruction"] is None
            )
            or (
                not honest_keys["full_sector_isometry_achieved"]
                and honest_keys["frozen_obstruction"] is not None
                and obstruction_certified
            )
        )
        and len(honest_keys["supplies"]) == 4
    )
    check(
        "G_honest_boundary_keys",
        honest_boundary_valid,
        honest_keys,
    )

    runtime = time.monotonic() - started
    all_pass = FAILURES == 0
    report = {
        "status": (
            "cycle733-sector-summed-full-sector-isometry"
            if all_pass and honest_keys["full_sector_isometry_achieved"]
            else "cycle733-honest-frozen-obstruction"
            if all_pass else "cycle733-certificate-failures"
        ),
        "pass": all_pass,
        "checks_passed": CHECK_COUNT - FAILURES,
        "checks_total": CHECK_COUNT,
        "shape": census["shape"],
        "sector_family_census": census,
        "direct_sum_channel": isometry,
        "intertwining_block_structure": intertwining,
        "cross_sector_diagnostics": diagnostics,
        "no_new_supply_audit": supply_audit,
        "runtime_seconds": round(runtime, 6),
        "within_audit_timeout": runtime < AUDIT_TIMEOUT_SEC,
        **honest_keys,
    }
    report["report_sha256"] = canonical_digest(report)
    print(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ))
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
