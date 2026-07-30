#!/usr/bin/env python3
"""Finite-box pullback analysis and explicit supply predicates."""

from __future__ import annotations

from frontier_cycle727_cross_code_pullback_core_2026_07_28 import *


def analyze_shape(shape: tuple[int, int, int]) -> dict[str, object]:
    """Compute every signed pullback and all five orthogonal audits."""
    reference = C.CellEdgeGauge.build(shape)
    euler = C.EulerMarkerGauge.build(shape)
    companion = M.CompanionFixture.build(shape)
    generators, dictionary = common_dictionary(reference, companion)
    cell_orientation = reference_orientation(reference, generators)
    euler_orientation = reference_orientation(euler, generators)
    factor = O.build_factorization(companion)
    mask_gauge = (1 << factor.gauge) - 1
    mask_center = (1 << factor.center) - 1
    generator_certificates = []
    pullbacks: dict[tuple[str, str, str], list[Pauli]] = {}
    sector_targets: dict[tuple[str, str], list[Pauli]] = {}
    full_reference_pullbacks: dict[tuple[str, str], list[Pauli]] = {}
    localities: dict[str, list[dict[str, object]]] = {
        family: [] for family in FAMILIES
    }

    for index, (
        generator,
        cell_decoded,
        euler_decoded,
    ) in enumerate(zip(
        generators,
        cell_orientation["decoded_rows"],
        euler_orientation["decoded_rows"],
    )):
        _cell_generator, cell_logical, cell_leakage, cell_supply = cell_decoded
        _euler_generator, euler_logical, euler_leakage, euler_supply = (
            euler_decoded
        )
        cell_pullback = A.apply_images(
            cell_orientation["images"], cell_logical, reference.matter_qubits
        )
        euler_pullback = A.apply_images(
            euler_orientation["images"], euler_logical, euler.matter_qubits
        )
        full_reference_pullbacks.setdefault(
            (generator.family, "CellEdgeGauge"), []
        ).append(cell_pullback)
        full_reference_pullbacks.setdefault(
            (generator.family, "EulerMarkerGauge"), []
        ).append(euler_pullback)
        _companion_even, companion_coordinates = companion_signed_pullback(
            factor, generator.companion_physical, False
        )
        companion_gauge_v = (
            companion_coordinates.v_mask >> factor.logical
        ) & mask_gauge
        companion_gauge_w = (
            companion_coordinates.w_mask >> factor.logical
        ) & mask_gauge
        center_mask = (
            companion_coordinates.w_mask
            >> (factor.logical + factor.gauge)
        ) & mask_center
        local_center_mask = center_mask & ((1 << (factor.center - 1)) - 1)
        parity_coordinate = (
            center_mask >> (factor.center - 1)
        ) & 1
        locality = locality_row(reference, companion, generator)
        localities[generator.family].append(locality)
        sectors = {}
        for odd, sector, sector_sign in PARITY_SECTORS:
            target_sector = fixed_sector_target(
                factor, generator.target, odd
            )
            cell_sector_pullback = fixed_sector_target(
                factor, cell_pullback, odd
            )
            euler_sector_pullback = fixed_sector_target(
                factor, euler_pullback, odd
            )
            companion_pullback, _coordinates = companion_signed_pullback(
                factor, generator.companion_physical, odd
            )
            for surface, row in (
                ("CellEdgeGauge", cell_sector_pullback),
                ("EulerMarkerGauge", euler_sector_pullback),
                ("CompanionFixture", companion_pullback),
            ):
                pullbacks.setdefault(
                    (generator.family, surface, sector), []
                ).append(row)
            sector_targets.setdefault(
                (generator.family, sector), []
            ).append(target_sector)
            signed_rows = {
                "target_fixed_sector": pauli_key(target_sector),
                "CellEdgeGauge_full": pauli_key(cell_pullback),
                "CellEdgeGauge_fixed_sector": pauli_key(
                    cell_sector_pullback
                ),
                "EulerMarkerGauge_full": pauli_key(euler_pullback),
                "EulerMarkerGauge_fixed_sector": pauli_key(
                    euler_sector_pullback
                ),
                "CompanionFixture_fixed_sector": pauli_key(
                    companion_pullback
                ),
            }
            sectors[sector] = {
                "sector_sign": sector_sign,
                "signed_rows_digest": json_digest(signed_rows),
                "rank_bits": {
                    "target": int(bool(
                        target_sector.x | target_sector.z
                    )),
                    "CellEdgeGauge": int(bool(
                        cell_sector_pullback.x | cell_sector_pullback.z
                    )),
                    "EulerMarkerGauge": int(bool(
                        euler_sector_pullback.x | euler_sector_pullback.z
                    )),
                    "CompanionFixture": int(bool(
                        companion_pullback.x | companion_pullback.z
                    )),
                },
                "phase_agreement": {
                    "CellEdgeGauge": (
                        cell_sector_pullback.phase == target_sector.phase
                    ),
                    "EulerMarkerGauge": (
                        euler_sector_pullback.phase == target_sector.phase
                    ),
                    "CompanionFixture": (
                        companion_pullback.phase == target_sector.phase
                    ),
                },
                "coordinate_agreement": {
                    "CellEdgeGauge": (
                        cell_sector_pullback.x == target_sector.x
                        and cell_sector_pullback.z == target_sector.z
                    ),
                    "EulerMarkerGauge": (
                        euler_sector_pullback.x == target_sector.x
                        and euler_sector_pullback.z == target_sector.z
                    ),
                    "CompanionFixture": (
                        companion_pullback.x == target_sector.x
                        and companion_pullback.z == target_sector.z
                    ),
                },
                "gauge_leakage": {
                    "CellEdgeGauge_nonmatter_v_mask": cell_leakage,
                    "EulerMarkerGauge_nonmatter_v_mask": euler_leakage,
                    "CompanionFixture_gauge_v_mask": companion_gauge_v,
                    "CompanionFixture_gauge_w_mask": companion_gauge_w,
                },
                "center_parity_supply": {
                    "CellEdgeGauge_constraint_w_mask": cell_supply,
                    "CellEdgeGauge_parity": "retained_not_supplied",
                    "EulerMarkerGauge_constraint_w_mask": euler_supply,
                    "EulerMarkerGauge_parity": (
                        "both_sectors_in_one_root_free_register"
                    ),
                    "CompanionFixture_local_center_mask": local_center_mask,
                    "CompanionFixture_parity_coordinate": parity_coordinate,
                    "CompanionFixture_parity": (
                        f"externally_supplied_s={sector_sign:+d}"
                    ),
                },
            }
        generator_certificates.append({
            "index": index,
            "family": generator.family,
            "label": generator.label,
            "signed_target": pauli_key(generator.target),
            "locality": locality,
            "sectors": sectors,
        })

    family_tables = {}
    for family in FAMILIES:
        selected = tuple(
            row for row in generators if row.family == family
        )
        targets = tuple(row.target for row in selected)
        full_target_rank = gf2_rank(
            row.symplectic(companion.matter_qubits) for row in targets
        )
        full_reference_ranks = {
            surface: gf2_rank(
                row.symplectic(companion.matter_qubits)
                for row in full_reference_pullbacks[(family, surface)]
            )
            for surface in ("CellEdgeGauge", "EulerMarkerGauge")
        }
        sector_tables = {}
        for _odd, sector, _sector_sign in PARITY_SECTORS:
            target_rank = gf2_rank(
                row.symplectic(companion.matter_qubits)
                for row in sector_targets[(family, sector)]
            )
            ranks = {
                surface: gf2_rank(
                    row.symplectic(companion.matter_qubits)
                    for row in pullbacks[(family, surface, sector)]
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            family_records = tuple(
                row for row in generator_certificates
                if row["family"] == family
            )
            phase_failures = {
                surface: sum(
                    not row["sectors"][sector]["phase_agreement"][surface]
                    for row in family_records
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            coordinate_failures = {
                surface: sum(
                    not row["sectors"][sector]["coordinate_agreement"][surface]
                    for row in family_records
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            leakage_totals = {
                key: sum(
                    int(row["sectors"][sector]["gauge_leakage"][key]).bit_count()
                    for row in family_records
                )
                for key in (
                    "CellEdgeGauge_nonmatter_v_mask",
                    "EulerMarkerGauge_nonmatter_v_mask",
                    "CompanionFixture_gauge_v_mask",
                    "CompanionFixture_gauge_w_mask",
                )
            }
            center_counts = {
                "CellEdgeGauge_constraint_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CellEdgeGauge_constraint_w_mask"
                    ])
                    for row in family_records
                ),
                "EulerMarkerGauge_constraint_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "EulerMarkerGauge_constraint_w_mask"
                    ])
                    for row in family_records
                ),
                "CompanionFixture_local_center_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CompanionFixture_local_center_mask"
                    ])
                    for row in family_records
                ),
                "CompanionFixture_parity_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CompanionFixture_parity_coordinate"
                    ])
                    for row in family_records
                ),
            }
            sector_tables[sector] = {
                "target_rank": target_rank,
                "pullback_ranks": ranks,
                "rank_agreement": all(
                    rank == target_rank for rank in ranks.values()
                ),
                "phase_failures": phase_failures,
                "coordinate_failures": coordinate_failures,
                "gauge_leakage_bit_totals": leakage_totals,
                "center_parity_supply_counts": center_counts,
                "center_parity_classification": {
                    "CellEdgeGauge": (
                        "constraint rows are +1 supplies; total matter parity "
                        "is retained because the root Gauss row is omitted"
                    ),
                    "EulerMarkerGauge": (
                        "marker/equality/Gauss rows are +1 supplies; both "
                        "matter-parity sectors remain in one register"
                    ),
                    "CompanionFixture": (
                        "local center signs are fixed and total parity is the "
                        f"external sector label s={+1 if sector == 'even' else -1:+d}"
                    ),
                },
            }
        family_tables[family] = {
            "generator_count": len(selected),
            "ordered_label_digest": json_digest(
                tuple(row.label for row in selected)
            ),
            "signed_target_digest": signed_digest(targets),
            "full_sector_target_rank": full_target_rank,
            "full_sector_reference_pullback_ranks": full_reference_ranks,
            "sectors": sector_tables,
            "locality_census": family_locality_census(
                tuple(localities[family])
            ),
        }

    reference_constraint_rows = tuple(
        row.symplectic(reference.qubits)
        for row in reference.w_rows[reference.matter_qubits :]
    )
    euler_constraint_rows = tuple(
        row.symplectic(euler.qubits)
        for row in euler.w_rows[euler.matter_qubits :]
    )
    reference_total_parity = Pauli(
        z=(1 << reference.matter_qubits) - 1
    ).symplectic(reference.qubits)
    euler_total_parity = Pauli(
        z=(1 << euler.matter_qubits) - 1
    ).symplectic(euler.qubits)
    physical_total_parity = Pauli(
        z=(1 << companion.matter_qubits) - 1
    )
    target_total_parity = Pauli(
        z=(1 << companion.matter_qubits) - 1
    )
    supply_count_table = {
        family: {
            sector: family_tables[family]["sectors"][sector][
                "center_parity_supply_counts"
            ]
            for _odd, sector, _sign in PARITY_SECTORS
        }
        for family in FAMILIES
    }
    supply_count_digest = json_digest(supply_count_table)
    supply_predicates = {
        "CellEdgeGauge_stabilizer_rank_exact": (
            gf2_rank(reference_constraint_rows)
            == reference.qubits - reference.matter_qubits
        ),
        "EulerMarkerGauge_stabilizer_rank_exact": (
            gf2_rank(euler_constraint_rows)
            == euler.qubits - euler.matter_qubits
        ),
        "CellEdgeGauge_total_parity_retained": not gf2_in_span(
            reference_total_parity, reference_constraint_rows
        ),
        "EulerMarkerGauge_total_parity_retained": not gf2_in_span(
            euler_total_parity, euler_constraint_rows
        ),
        "CellEdgeGauge_omits_one_root_Gauss_row": (
            len(reference.gauss) == len(reference.cells) - 1
        ),
        "EulerMarkerGauge_has_all_Gauss_rows": (
            len(euler.gauss) == len(euler.cells)
        ),
        "EulerMarkerGauge_marker_count_is_odd": (
            len(euler.marker_objects) & 1
        ) == 1,
        "CompanionFixture_center_split_exact": (
            factor.center == factor.local_center_rank + 1
        ),
        "CompanionFixture_physical_parity_coordinate_exact": (
            factor.physical_w[
                factor.logical + factor.gauge + factor.center - 1
            ] == physical_total_parity
        ),
        "CompanionFixture_target_parity_coordinate_exact": (
            factor.target_w[factor.logical] == target_total_parity
        ),
        "supply_masks_within_declared_coordinates": all(
            row["sectors"][sector]["center_parity_supply"][
                "CellEdgeGauge_constraint_w_mask"
            ] < (1 << len(reference_constraint_rows))
            and row["sectors"][sector]["center_parity_supply"][
                "EulerMarkerGauge_constraint_w_mask"
            ] < (1 << len(euler_constraint_rows))
            and row["sectors"][sector]["center_parity_supply"][
                "CompanionFixture_local_center_mask"
            ] < (1 << factor.local_center_rank)
            and row["sectors"][sector]["center_parity_supply"][
                "CompanionFixture_parity_coordinate"
            ] in (0, 1)
            for row in generator_certificates
            for _odd, sector, _sign in PARITY_SECTORS
        ),
        "supply_counts_sector_independent": all(
            supply_count_table[family]["even"]
            == supply_count_table[family]["odd"]
            for family in FAMILIES
        ),
        "supply_count_digest_frozen": (
            supply_count_digest == FROZEN_SUPPLY_COUNT_DIGESTS[shape]
        ),
    }
    rank_exact = all(
        table["sectors"][sector]["rank_agreement"]
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    phase_exact = all(
        not any(table["sectors"][sector]["phase_failures"].values())
        and not any(table["sectors"][sector]["coordinate_failures"].values())
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    zero_gauge_leakage = all(
        not any(
            table["sectors"][sector][
                "gauge_leakage_bit_totals"
            ].values()
        )
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    locality_certified = all(
        table["locality_census"]["maximum_semantic_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 1
        )
        and table["locality_census"]["maximum_companion_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 1
        )
        and table["locality_census"]["maximum_reference_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 3
        )
        for family, table in family_tables.items()
    )
    supply_classified = all(supply_predicates.values())
    exact = (
        rank_exact
        and phase_exact
        and zero_gauge_leakage
        and locality_certified
        and supply_classified
        and not cell_orientation["coordinate_system_inconsistent"]
        and not euler_orientation["coordinate_system_inconsistent"]
        and cell_orientation["augmented_contradictions"] == 0
        and euler_orientation["augmented_contradictions"] == 0
        and cell_orientation["phase_contradictions"] == 0
        and euler_orientation["phase_contradictions"] == 0
        and cell_orientation["replay_failures"] == 0
        and euler_orientation["replay_failures"] == 0
        and factor.phase_contradictions == 0
    )
    public = {
        "shape": shape,
        "cells": len(reference.cells),
        "oriented_edges": len(reference.edges),
        "dictionary": dictionary,
        "dictionary_match": {
            "identical_cells": reference.cells == companion.cells,
            "identical_oriented_edges": reference.edges == companion.edges,
            "identical_matter_mode_count": (
                reference.matter_qubits == companion.matter_qubits
            ),
        },
        "reference_orientations": {
            "CellEdgeGauge": {
                key: value for key, value in cell_orientation.items()
                if key not in ("images", "decoded_rows")
            },
            "EulerMarkerGauge": {
                key: value for key, value in euler_orientation.items()
                if key not in ("images", "decoded_rows")
            },
        },
        "companion_factorization": {
            "logical_qubits": factor.logical,
            "gauge_pairs": factor.gauge,
            "center_signs_including_parity": factor.center,
            "local_center_rank": factor.local_center_rank,
            "phase_rank": factor.phase_rank,
            "phase_contradictions": factor.phase_contradictions,
        },
        "separate_certificates": {
            "rank_agreement": rank_exact,
            "phase_agreement": phase_exact,
            "zero_gauge_leakage": zero_gauge_leakage,
            "center_parity_supply_classified": supply_classified,
            "locality_census_certified": locality_certified,
        },
        "supply_certificate": {
            "predicates": supply_predicates,
            "count_table": supply_count_table,
            "count_table_sha256": supply_count_digest,
            "frozen_count_table_sha256": FROZEN_SUPPLY_COUNT_DIGESTS[shape],
        },
        "family_tables": family_tables,
        "per_generator_certificate_count": len(generator_certificates),
        "per_generator_certificates": tuple({
            "index": row["index"],
            "family": row["family"],
            "label": row["label"],
            "certificate_digest": json_digest(row),
        } for row in generator_certificates),
        "per_generator_certificate_digest": json_digest(
            generator_certificates
        ),
        "per_family_generator_certificate_digests": {
            family: json_digest(tuple(
                row for row in generator_certificates
                if row["family"] == family
            ))
            for family in FAMILIES
        },
        "cross_code_pullbacks_exact": exact,
    }
    return {
        "public": public,
        "factor": factor,
        "euler": euler,
        "generators": generators,
    }
