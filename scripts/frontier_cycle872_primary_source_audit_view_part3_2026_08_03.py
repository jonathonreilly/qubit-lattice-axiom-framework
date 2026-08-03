#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 primary source, part 3/4."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
PART_ORDINAL = 3
PART_COUNT = 4
FIRST_SOURCE_LINE = 971
LAST_SOURCE_LINE = 1455
TOTAL_SOURCE_LINES = 1940
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "c1b32ef8e2a870128b7081a88b920b85c84123d04f98a165bfc7225dcfc716e4"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 000971|                dirty["endpoint_alias_failures"] += path_index in (0, len(path) - 1)
# C872SRC 000972|                dirty["same_color_failures"] += color(seam) == color(seams[other])
# C872SRC 000973|                dirty["label_return_failures"] += labels[path_index] != path_index
# C872SRC 000974|                dirty["dirty_basis_rows"] += 2
# C872SRC 000975|                dirty["dirty_basis_failures"] += 2 * (labels[path_index] != path_index)
# C872SRC 000976|
# C872SRC 000977|    naive_pairs = fine_pairs = 0
# C872SRC 000978|    for index, left in enumerate(seams):
# C872SRC 000979|        for right in seams[:index]:
# C872SRC 000980|            if coarse_color(left) == coarse_color(right):
# C872SRC 000981|                naive_pairs += bool(footprints[left] & footprints[right])
# C872SRC 000982|            if color(left) == color(right):
# C872SRC 000983|                fine_pairs += bool(footprints[left] & footprints[right])
# C872SRC 000984|
# C872SRC 000985|    tags = tuple(factor[0] for factor, _rows in factors)
# C872SRC 000986|    first_seam = tags.index("seam")
# C872SRC 000987|    last_seam = len(tags) - 1 - tuple(reversed(tags)).index("seam")
# C872SRC 000988|    expected_phase = -math.pi * len(seams) / 2
# C872SRC 000989|    return {
# C872SRC 000990|        "length": length,
# C872SRC 000991|        "cells": len(graph.cells),
# C872SRC 000992|        "seams": len(seams),
# C872SRC 000993|        "actual_update_rotations": len(rotations),
# C872SRC 000994|        "actual_factor_macros": len(factors),
# C872SRC 000995|        "actual_seam_factors": len(actual_seams),
# C872SRC 000996|        "actual_seam_rotations": sum(len(rows) for _factor, rows in actual_seams),
# C872SRC 000997|        "augmented_instructions": sum(map(len, words)),
# C872SRC 000998|        "augmented_instruction_range": (min(map(len, words)), max(map(len, words))),
# C872SRC 000999|        "used_packet_M2_per_seam": C714.N,
# C872SRC 001000|        "retained_spatial_current_M2_per_seam": 1,
# C872SRC 001001|        "total_resource_M2_per_seam": C714.N + 1,
# C872SRC 001002|        "packet_bank_radius": max(placement.radius for placement in placements),
# C872SRC 001003|        "total_resource_radius": max(
# C872SRC 001004|            max(placement.radius for placement in placements),
# C872SRC 001005|            max(map(abs, SPATIAL_CURRENT_LOCAL)),
# C872SRC 001006|        ),
# C872SRC 001007|        "used_packet_union_M2": len(used_packet_union),
# C872SRC 001008|        "used_resource_union_M2": len(used_resource_union),
# C872SRC 001009|        "packet_bank_pair_overlap_pairs": packet_pair_overlaps,
# C872SRC 001010|        "resource_bank_pair_overlap_pairs": resource_pair_overlaps,
# C872SRC 001011|        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
# C872SRC 001012|        "spatial_output_geometry_failures": spatial_geometry,
# C872SRC 001013|        "route_policy": (
# C872SRC 001014|            "declared coframe-returned replacement for the augmented seam stage; "
# C872SRC 001015|            "landed Manhattan route retained outside that stage"
# C872SRC 001016|        ),
# C872SRC 001017|        "retained_seam_route_reconciliation": dict(route_reconciliation),
# C872SRC 001018|        "binding_failures": dict(binding_failures),
# C872SRC 001019|        "commuting_transpositions": len(inversions),
# C872SRC 001020|        "certified_coarse_macro_pairs": len(coarse_pairs),
# C872SRC 001021|        "commutation_failures": dict(commute_failures),
# C872SRC 001022|        "maximum_polynomial_commutator_residual": maximum_poly_residual,
# C872SRC 001023|        "active_colors": len(grouped),
# C872SRC 001024|        "lockstep_schedule_key": (
# C872SRC 001025|            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
# C872SRC 001026|            "on remaining axes in ascending global-axis order"
# C872SRC 001027|        ),
# C872SRC 001028|        "emitted_physical_stream_order": "exact Cycle870 serial factor order",
# C872SRC 001029|        "identity_padding_slots": padding,
# C872SRC 001030|        "same_layer_gate_pairs": same_layer_pairs,
# C872SRC 001031|        "same_layer_support_collisions": same_layer_collisions,
# C872SRC 001032|        "same_color_footprint_collisions": footprint_collisions,
# C872SRC 001033|        "fixed_color_schedule_routed_depth": fixed_depth,
# C872SRC 001034|        "first_forward_swap_deletion_detections": deletions,
# C872SRC 001035|        "dirty_spectator": {
# C872SRC 001036|            **dict(dirty),
# C872SRC 001037|            "ordered_macro_bank_pairs": len(macro_bank_pairs),
# C872SRC 001038|        },
# C872SRC 001039|        "coarse_six_color_collision_control": naive_pairs,
# C872SRC 001040|        "fine_24_color_collision_count": fine_pairs,
# C872SRC 001041|        "seam_stage_contiguity_failure": any(
# C872SRC 001042|            tag != "seam" for tag in tags[first_seam:last_seam + 1]
# C872SRC 001043|        ),
# C872SRC 001044|        "stage_order_failure": (
# C872SRC 001045|            any(tag == "contact" for tag in tags[:first_seam])
# C872SRC 001046|            or any(tag in ("coin", "reverse") for tag in tags[last_seam + 1 :])
# C872SRC 001047|        ),
# C872SRC 001048|        "expected_seam_phase": expected_phase,
# C872SRC 001049|        "observed_seam_phase": inventory["compiled_relative_phase_breakdown"]["seam_FSWAP"],
# C872SRC 001050|        "seam_phase_failure": abs(
# C872SRC 001051|            inventory["compiled_relative_phase_breakdown"]["seam_FSWAP"] - expected_phase
# C872SRC 001052|        ) > C871.TOL,
# C872SRC 001053|        "full_update_relative_phase_unchanged": inventory[
# C872SRC 001054|            "compiled_relative_to_target_global_phase_angle"
# C872SRC 001055|        ],
# C872SRC 001056|    }
# C872SRC 001057|
# C872SRC 001058|
# C872SRC 001059|def held_schedule_fixture(length: int):
# C872SRC 001060|    """Held geometry/schedule stress for the declared coframe replacement."""
# C872SRC 001061|    graph = C870.prep.OpenReferenceGraph(cells(length))
# C872SRC 001062|    context = C870.physical_context(graph)
# C872SRC 001063|    seams = C870.graph_seams(graph)
# C872SRC 001064|    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
# C872SRC 001065|    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
# C872SRC 001066|    resource_banks = tuple(resource_bank(placement) for placement in placements)
# C872SRC 001067|    blocked = set(context.sites) | J870.auxiliary_registers(graph)
# C872SRC 001068|    words = tuple(
# C872SRC 001069|        flatten(candidate_segments(graph, context, seam, placement))
# C872SRC 001070|        for seam, placement in zip(seams, placements)
# C872SRC 001071|    )
# C872SRC 001072|    footprints = {
# C872SRC 001073|        seam: footprint(word, placement.basis)
# C872SRC 001074|        for seam, word, placement in zip(seams, words, placements)
# C872SRC 001075|    }
# C872SRC 001076|    routed_depth = {}
# C872SRC 001077|    for seam, word, placement in zip(seams, words, placements):
# C872SRC 001078|        depth = 0
# C872SRC 001079|        for instruction in word:
# C872SRC 001080|            if len(instruction.sites) == 1:
# C872SRC 001081|                depth += 1
# C872SRC 001082|            else:
# C872SRC 001083|                path = C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 001084|                depth += 2 * len(path) - 3
# C872SRC 001085|        routed_depth[seam] = depth
# C872SRC 001086|    grouped = defaultdict(list)
# C872SRC 001087|    for seam in seams:
# C872SRC 001088|        grouped[color(seam)].append(seam)
# C872SRC 001089|    fine_pairs = fine_collisions = 0
# C872SRC 001090|    for members in grouped.values():
# C872SRC 001091|        for index, left in enumerate(members):
# C872SRC 001092|            for right in members[:index]:
# C872SRC 001093|                fine_pairs += 1
# C872SRC 001094|                fine_collisions += bool(footprints[left] & footprints[right])
# C872SRC 001095|    coarse_collisions = sum(
# C872SRC 001096|        bool(footprints[left] & footprints[right])
# C872SRC 001097|        for index, left in enumerate(seams) for right in seams[:index]
# C872SRC 001098|        if coarse_color(left) == coarse_color(right)
# C872SRC 001099|    )
# C872SRC 001100|    packet_pair_overlaps = sum(
# C872SRC 001101|        bool(set(left.sites) & set(right.sites))
# C872SRC 001102|        for index, left in enumerate(placements) for right in placements[:index]
# C872SRC 001103|    )
# C872SRC 001104|    resource_pair_overlaps = sum(
# C872SRC 001105|        bool(left & right)
# C872SRC 001106|        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
# C872SRC 001107|    )
# C872SRC 001108|    offset_min = [math.inf] * 3
# C872SRC 001109|    offset_max = [-math.inf] * 3
# C872SRC 001110|    for seam, placement in zip(seams, placements):
# C872SRC 001111|        for site in footprints[seam]:
# C872SRC 001112|            for axis in range(3):
# C872SRC 001113|                offset_min[axis] = min(offset_min[axis], site[axis] - placement.midpoint[axis])
# C872SRC 001114|                offset_max[axis] = max(offset_max[axis], site[axis] - placement.midpoint[axis])
# C872SRC 001115|    return {
# C872SRC 001116|        "length": length,
# C872SRC 001117|        "cells": len(graph.cells),
# C872SRC 001118|        "seams": len(seams),
# C872SRC 001119|        "used_packet_M2_per_seam": C714.N,
# C872SRC 001120|        "retained_spatial_current_M2_per_seam": 1,
# C872SRC 001121|        "total_resource_M2_per_seam": C714.N + 1,
# C872SRC 001122|        "used_packet_union_M2": len(set().union(*(set(row.sites) for row in placements))),
# C872SRC 001123|        "used_resource_union_M2": len(set().union(*resource_banks)),
# C872SRC 001124|        "packet_bank_pair_overlap_pairs": packet_pair_overlaps,
# C872SRC 001125|        "resource_bank_pair_overlap_pairs": resource_pair_overlaps,
# C872SRC 001126|        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
# C872SRC 001127|        "spatial_output_geometry_failures": {
# C872SRC 001128|            "duplicate_output_sites": len(spatial_sites) - len(set(spatial_sites)),
# C872SRC 001129|            "packet_aliases": sum(
# C872SRC 001130|                site in set().union(*(set(row.sites) for row in placements))
# C872SRC 001131|                for site in spatial_sites
# C872SRC 001132|            ),
# C872SRC 001133|            "native_aux_collisions": sum(site in blocked for site in spatial_sites),
# C872SRC 001134|        },
# C872SRC 001135|        "active_colors": len(grouped),
# C872SRC 001136|        "lockstep_schedule_key": (
# C872SRC 001137|            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
# C872SRC 001138|            "on remaining axes in ascending global-axis order"
# C872SRC 001139|        ),
# C872SRC 001140|        "same_color_macro_pairs": fine_pairs,
# C872SRC 001141|        "same_color_footprint_support_collisions": fine_collisions,
# C872SRC 001142|        "coarse_six_color_collision_control": coarse_collisions,
# C872SRC 001143|        "fixed_color_schedule_routed_depth": sum(
# C872SRC 001144|            max(routed_depth[seam] for seam in members) for members in grouped.values()
# C872SRC 001145|        ),
# C872SRC 001146|        "macro_routed_depth_range": (
# C872SRC 001147|            min(routed_depth.values()), max(routed_depth.values())
# C872SRC 001148|        ),
# C872SRC 001149|        "footprint_offset_min": offset_min,
# C872SRC 001150|        "footprint_offset_max": offset_max,
# C872SRC 001151|        "route_policy": "declared coframe-returned replacement",
# C872SRC 001152|    }
# C872SRC 001153|
# C872SRC 001154|
# C872SRC 001155|def semantic_direction_certificate():
# C872SRC 001156|    rows = tuple(product((0, 1), repeat=12))
# C872SRC 001157|    counts = Counter()
# C872SRC 001158|    failures = Counter()
# C872SRC 001159|    lawful_pairs = set()
# C872SRC 001160|    for pointer, binder, actuality, admissibility, law, fresh, causal in product(
# C872SRC 001161|        (0, 1), repeat=7
# C872SRC 001162|    ):
# C872SRC 001163|        controls = (pointer, binder, actuality, admissibility, law, fresh)
# C872SRC 001164|        after = C714.apply_semantic(
# C872SRC 001165|            C714.initial(9, 12, causal, controls), C714.word()
# C872SRC 001166|        )
# C872SRC 001167|        expected = (
# C872SRC 001168|            pointer & binder & actuality & admissibility & law & fresh & causal
# C872SRC 001169|        )
# C872SRC 001170|        counts["exact_packet_equation_rows"] += 1
# C872SRC 001171|        failures["exact_packet_equation"] += after[C714.PORIENT] != expected
# C872SRC 001172|        failures["exact_packet_ORIENT_return"] += after[C714.ORIENT] != causal
# C872SRC 001173|    for axis in range(3):
# C872SRC 001174|        left, right = 2 * axis + 1, 6 + 2 * axis
# C872SRC 001175|        for source in rows:
# C872SRC 001176|            target, _phase = C704.GAUSS.target_fswap_action(source, left, right)
# C872SRC 001177|            pre_left, pre_right = source[left], source[right]
# C872SRC 001178|            post_left, post_right = target[left], target[right]
# C872SRC 001179|            pointer = pre_left ^ pre_right
# C872SRC 001180|            u_to_v = pointer & post_right
# C872SRC 001181|            v_to_u = pointer & post_left
# C872SRC 001182|            wrong = pointer & post_left
# C872SRC 001183|            du = pre_left ^ post_left
# C872SRC 001184|            dv = pre_right ^ post_right
# C872SRC 001185|            failures["pointer"] += pointer != (du | dv)
# C872SRC 001186|            failures["one_hot"] += (u_to_v ^ v_to_u) != pointer or u_to_v + v_to_u > 1
# C872SRC 001187|            failures["scratch"] += (du ^ post_left ^ post_right) != 0
# C872SRC 001188|            failures["scratch"] += (dv ^ post_left ^ post_right) != 0
# C872SRC 001189|            failures["current_decode"] += (
# C872SRC 001190|                2 * u_to_v - pointer != u_to_v - v_to_u
# C872SRC 001191|                or u_to_v - v_to_u != post_right - pre_right
# C872SRC 001192|            )
# C872SRC 001193|            for causal in (0, 1):
# C872SRC 001194|                counts["rows"] += 1
# C872SRC 001195|                counts["moving"] += pointer
# C872SRC 001196|                counts["u_to_v"] += u_to_v
# C872SRC 001197|                counts["v_to_u"] += v_to_u
# C872SRC 001198|                counts["wrong_side_detected"] += pointer and wrong != u_to_v
# C872SRC 001199|                # Deleting the seam makes post=pre, hence du=dv=pointer=0
# C872SRC 001200|                # in the actual comparator grammar and spatial output zero.
# C872SRC 001201|                counts["seam_deletion_detected"] += (
# C872SRC 001202|                    (0, 0) != (pointer, u_to_v)
# C872SRC 001203|                )
# C872SRC 001204|                lawful_pairs.add((u_to_v, causal))
# C872SRC 001205|
# C872SRC 001206|                # The added M2 site begins blank and retains the spatial bit.
# C872SRC 001207|                spatial_before = 0
# C872SRC 001208|                spatial_after = spatial_before ^ (pointer & post_right)
# C872SRC 001209|                failures["spatial_output"] += spatial_after != u_to_v
# C872SRC 001210|                counts["dirty_spatial_input_detected"] += (
# C872SRC 001211|                    (1 ^ (pointer & post_right)) != u_to_v
# C872SRC 001212|                )
# C872SRC 001213|
# C872SRC 001214|                # Cycle714 ORIENT is a supplied causal coordinate.  The packet
# C872SRC 001215|                # emits its enabled causal projection and returns ORIENT.
# C872SRC 001216|                enabled_controls = (pointer, 1, 1, 1, 1, 1)
# C872SRC 001217|                before = C714.initial(9, 12, causal, enabled_controls)
# C872SRC 001218|                after = C714.apply_semantic(before, C714.word())
# C872SRC 001219|                failures["causal_packet_projection"] += (
# C872SRC 001220|                    after[C714.PORIENT] != pointer & causal
# C872SRC 001221|                )
# C872SRC 001222|                failures["causal_ORIENT_return"] += after[C714.ORIENT] != causal
# C872SRC 001223|                failures["work_return"] += any(
# C872SRC 001224|                    after[index] for index in C714.MCX_WORK + C714.ENABLE_WORK
# C872SRC 001225|                )
# C872SRC 001226|
# C872SRC 001227|                # Mutation: XOR the spatial result into the supplied causal
# C872SRC 001228|                # ORIENT, reproducing the forbidden overloaded construction.
# C872SRC 001229|                damaged = C714.initial(
# C872SRC 001230|                    9, 12, causal ^ u_to_v, (pointer, 1, 1, 1, 1, 1)
# C872SRC 001231|                )
# C872SRC 001232|                damaged_after = C714.apply_semantic(damaged, C714.word())
# C872SRC 001233|                counts["ORIENT_overload_detected"] += (
# C872SRC 001234|                    damaged_after[C714.PORIENT] != pointer & causal
# C872SRC 001235|                )
# C872SRC 001236|
# C872SRC 001237|    initial = C714.initial(9, 12, 1, (1, 1, 1, 1, 1, 1))
# C872SRC 001238|    first = C714.apply_semantic(initial, C714.word())
# C872SRC 001239|    reused = C714.apply_semantic(first, C714.word())
# C872SRC 001240|    reuse_difference = sum(a != b for a, b in zip(first, reused))
# C872SRC 001241|    return {
# C872SRC 001242|        **dict(counts),
# C872SRC 001243|        "failure_census": dict(failures),
# C872SRC 001244|        "packet_reuse_without_reset_changed_bits": reuse_difference,
# C872SRC 001245|        "packet_reuse_without_reset_detected": reuse_difference > 0,
# C872SRC 001246|        "spatial_causal_pairs": tuple(sorted(lawful_pairs)),
# C872SRC 001247|        "spatial_current_decode": "j_e = 2*r_u_to_v - pointer = r_u_to_v-r_v_to_u",
# C872SRC 001248|        "spatial_output_register": "one separate retained M2 per seam",
# C872SRC 001249|        "exact_packet_equation": (
# C872SRC 001250|            "PORIENT = POINTER AND BINDER AND ACTUAL AND ADMISS AND LAW AND FRESH AND ORIENT"
# C872SRC 001251|        ),
# C872SRC 001252|        "enabled_domain_simplification": (
# C872SRC 001253|            "with BINDER=ACTUAL=ADMISS=LAW=FRESH=1 only, PORIENT=POINTER AND ORIENT"
# C872SRC 001254|        ),
# C872SRC 001255|        "output_type": "spatial direction / unit-weight number-resource current",
# C872SRC 001256|        "causal_orientation": (
# C872SRC 001257|            "supplied and retained in ORIENT; PORIENT carries the fully enabled projection"
# C872SRC 001258|        ),
# C872SRC 001259|    }
# C872SRC 001260|
# C872SRC 001261|
# C872SRC 001262|def continuity_certificate():
# C872SRC 001263|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 001264|    seams = C870.graph_seams(graph)
# C872SRC 001265|    cell_rows = graph.cells
# C872SRC 001266|    cell_index = {cell: index for index, cell in enumerate(cell_rows)}
# C872SRC 001267|    endpoint_index = {}
# C872SRC 001268|    endpoint_cell = []
# C872SRC 001269|    for seam in seams:
# C872SRC 001270|        for key in ((seam[0], seam[3]), (seam[2], seam[4])):
# C872SRC 001271|            if key not in endpoint_index:
# C872SRC 001272|                endpoint_index[key] = len(endpoint_index)
# C872SRC 001273|                endpoint_cell.append(cell_index[key[0]])
# C872SRC 001274|
# C872SRC 001275|    failures = Counter()
# C872SRC 001276|    patterns = 0
# C872SRC 001277|    for currents in product((-1, 0, 1), repeat=len(seams)):
# C872SRC 001278|        occupation = [0] * len(endpoint_index)
# C872SRC 001279|        for seam, current in zip(seams, currents):
# C872SRC 001280|            u = endpoint_index[(seam[0], seam[3])]
# C872SRC 001281|            v = endpoint_index[(seam[2], seam[4])]
# C872SRC 001282|            if current > 0:
# C872SRC 001283|                occupation[u] = 1
# C872SRC 001284|            elif current < 0:
# C872SRC 001285|                occupation[v] = 1
# C872SRC 001286|        before = [0] * len(cell_rows)
# C872SRC 001287|        for endpoint, bit in enumerate(occupation):
# C872SRC 001288|            before[endpoint_cell[endpoint]] += bit
# C872SRC 001289|        observed_current = []
# C872SRC 001290|        for seam in seams:
# C872SRC 001291|            u = endpoint_index[(seam[0], seam[3])]
# C872SRC 001292|            v = endpoint_index[(seam[2], seam[4])]
# C872SRC 001293|            pre_v = occupation[v]
# C872SRC 001294|            occupation[u], occupation[v] = occupation[v], occupation[u]
# C872SRC 001295|            observed_current.append(occupation[v] - pre_v)
# C872SRC 001296|        after = [0] * len(cell_rows)
# C872SRC 001297|        for endpoint, bit in enumerate(occupation):
# C872SRC 001298|            after[endpoint_cell[endpoint]] += bit
# C872SRC 001299|        divergence = [0] * len(cell_rows)
# C872SRC 001300|        for seam, current in zip(seams, observed_current):
# C872SRC 001301|            divergence[cell_index[seam[0]]] -= current
# C872SRC 001302|            divergence[cell_index[seam[2]]] += current
# C872SRC 001303|        failures["current_pattern"] += tuple(observed_current) != currents
# C872SRC 001304|        failures["cell_continuity"] += any(
# C872SRC 001305|            after[index] - before[index] != divergence[index]
# C872SRC 001306|            for index in range(len(cell_rows))
# C872SRC 001307|        )
# C872SRC 001308|        failures["global_number"] += sum(after) != sum(before)
# C872SRC 001309|        patterns += 1
# C872SRC 001310|
# C872SRC 001311|    # Both stationary endpoint columns project to j=0 and zero occupation delta.
# C872SRC 001312|    stationary_rows = (((0, 0), (0, 0)), ((1, 1), (1, 1)))
# C872SRC 001313|    stationary_failures = sum(
# C872SRC 001314|        (post_v - pre_v) != 0 or (sum(post) - sum(pre)) != 0
# C872SRC 001315|        for pre, post in stationary_rows for pre_v, post_v in ((pre[1], post[1]),)
# C872SRC 001316|    )
# C872SRC 001317|
# C872SRC 001318|    frames = C871.proper_frames()
# C872SRC 001319|    frame_rows = frame_failures = 0
# C872SRC 001320|    product_rows = product_failures = 0
# C872SRC 001321|    for seam in seams:
# C872SRC 001322|        owner, axis, target = seam[0], seam[1], seam[2]
# C872SRC 001323|        for frame in frames:
# C872SRC 001324|            target_axis, sign = C871.signed_axis(frame, axis)
# C872SRC 001325|            moved_owner = C871.matvec(frame, owner)
# C872SRC 001326|            moved_target = C871.matvec(frame, target)
# C872SRC 001327|            canonical_owner, canonical_target = (
# C872SRC 001328|                (moved_owner, moved_target) if sign > 0
# C872SRC 001329|                else (moved_target, moved_owner)
# C872SRC 001330|            )
# C872SRC 001331|            for current in (-1, 0, 1):
# C872SRC 001332|                transformed = sign * current
# C872SRC 001333|                observed = {
# C872SRC 001334|                    moved_owner: -current,
# C872SRC 001335|                    moved_target: current,
# C872SRC 001336|                }
# C872SRC 001337|                expected = {
# C872SRC 001338|                    canonical_owner: -transformed,
# C872SRC 001339|                    canonical_target: transformed,
# C872SRC 001340|                }
# C872SRC 001341|                frame_rows += 1
# C872SRC 001342|                frame_failures += observed != expected or target_axis not in range(3)
# C872SRC 001343|        for left in frames:
# C872SRC 001344|            for right in frames:
# C872SRC 001345|                intermediate_axis, sign_right = C871.signed_axis(right, axis)
# C872SRC 001346|                _final_axis, sign_left = C871.signed_axis(left, intermediate_axis)
# C872SRC 001347|                _product_axis, sign_product = C871.signed_axis(left @ right, axis)
# C872SRC 001348|                for current in (-1, 0, 1):
# C872SRC 001349|                    product_rows += 1
# C872SRC 001350|                    product_failures += sign_left * sign_right * current != sign_product * current
# C872SRC 001351|    return {
# C872SRC 001352|        "shape": (2, 2, 2),
# C872SRC 001353|        "seams": len(seams),
# C872SRC 001354|        "endpoint_modes": len(endpoint_index),
# C872SRC 001355|        "current_patterns": patterns,
# C872SRC 001356|        "covered_full_occupation_columns": 4 ** len(seams),
# C872SRC 001357|        "stationary_equivalence_rows": len(stationary_rows),
# C872SRC 001358|        "stationary_equivalence_failures": stationary_failures,
# C872SRC 001359|        "failure_census": dict(failures),
# C872SRC 001360|        "proper_frames": len(frames),
# C872SRC 001361|        "frame_rows": frame_rows,
# C872SRC 001362|        "frame_failures": frame_failures,
# C872SRC 001363|        "ordered_frame_products": len(frames) ** 2,
# C872SRC 001364|        "product_rows": product_rows,
# C872SRC 001365|        "product_failures": product_failures,
# C872SRC 001366|        "identity": "Delta N_x = sum_in j_e - sum_out j_e",
# C872SRC 001367|        "current": "j_e = n_v_post - n_v_pre = r_u_to_v - r_v_to_u",
# C872SRC 001368|        "type": "unit-weight conserved number/resource current",
# C872SRC 001369|        "not_claimed": (
# C872SRC 001370|            "energy", "mass", "source density", "occurrence", "gravity"
# C872SRC 001371|        ),
# C872SRC 001372|        "coupling_and_scale": "supplied",
# C872SRC 001373|    }
# C872SRC 001374|
# C872SRC 001375|
# C872SRC 001376|def color_covariance_certificate():
# C872SRC 001377|    def encode(axis, owner):
# C872SRC 001378|        return (
# C872SRC 001379|            axis, owner[axis] & 1,
# C872SRC 001380|            *(owner[index] & 1 for index in range(3) if index != axis),
# C872SRC 001381|        )
# C872SRC 001382|
# C872SRC 001383|    def decode(row):
# C872SRC 001384|        axis, axial, *remaining = row
# C872SRC 001385|        iterator = iter(remaining)
# C872SRC 001386|        owner = tuple(axial if index == axis else next(iterator) for index in range(3))
# C872SRC 001387|        return axis, owner
# C872SRC 001388|
# C872SRC 001389|    colors = tuple(
# C872SRC 001390|        encode(axis, owner)
# C872SRC 001391|        for axis in range(3) for owner in product((0, 1), repeat=3)
# C872SRC 001392|    )
# C872SRC 001393|    frames = C871.proper_frames()
# C872SRC 001394|
# C872SRC 001395|    def action(row, frame):
# C872SRC 001396|        axis, owner = decode(row)
# C872SRC 001397|        target_axis, sign = C871.signed_axis(frame, axis)
# C872SRC 001398|        moved = C871.matvec(frame, owner)
# C872SRC 001399|        if sign < 0:
# C872SRC 001400|            moved = C871.add(moved, C871.matvec(frame, C871.unit(axis)))
# C872SRC 001401|        return encode(target_axis, moved)
# C872SRC 001402|
# C872SRC 001403|    bijection_failures = 0
# C872SRC 001404|    for frame in frames:
# C872SRC 001405|        bijection_failures += len({action(row, frame) for row in colors}) != len(colors)
# C872SRC 001406|    product_failures = 0
# C872SRC 001407|    for left in frames:
# C872SRC 001408|        for right in frames:
# C872SRC 001409|            product_failures += sum(
# C872SRC 001410|                action(action(row, right), left) != action(row, left @ right)
# C872SRC 001411|                for row in colors
# C872SRC 001412|            )
# C872SRC 001413|    return {
# C872SRC 001414|        "colors": len(colors),
# C872SRC 001415|        "proper_frames": len(frames),
# C872SRC 001416|        "bijection_failures": bijection_failures,
# C872SRC 001417|        "ordered_frame_products": len(frames) ** 2,
# C872SRC 001418|        "product_rows": len(colors) * len(frames) ** 2,
# C872SRC 001419|        "product_failures": product_failures,
# C872SRC 001420|    }
# C872SRC 001421|
# C872SRC 001422|
# C872SRC 001423|def used_epoch_passive_covariance():
# C872SRC 001424|    """Passive representation law for the used 59+1-site words/routes."""
# C872SRC 001425|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 001426|    context = C870.physical_context(graph)
# C872SRC 001427|    seams = C870.graph_seams(graph)
# C872SRC 001428|    representatives = tuple(next(seam for seam in seams if seam[1] == axis) for axis in range(3))
# C872SRC 001429|    frames = C871.proper_frames()
# C872SRC 001430|    counts = Counter()
# C872SRC 001431|    for seam in representatives:
# C872SRC 001432|        placement = C871.packet_placement(graph, context, seam)
# C872SRC 001433|        word = flatten(candidate_segments(graph, context, seam, placement))
# C872SRC 001434|        signatures = tuple(sorted(
# C872SRC 001435|            set(map(C871.instruction_signature, word)), key=repr
# C872SRC 001436|        ))
# C872SRC 001437|        paths = tuple(sorted(set(
# C872SRC 001438|            C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 001439|            for instruction in word if len(instruction.sites) == 2
# C872SRC 001440|        ), key=repr))
# C872SRC 001441|        for frame in frames:
# C872SRC 001442|            moved_basis = tuple(C871.matvec(frame, row) for row in placement.basis)
# C872SRC 001443|            for path in paths:
# C872SRC 001444|                observed = C871.coframe_path(
# C872SRC 001445|                    C871.matvec(frame, path[0]), C871.matvec(frame, path[-1]), moved_basis
# C872SRC 001446|                )
# C872SRC 001447|                counts["frame_path_rows"] += 1
# C872SRC 001448|                counts["frame_path_failures"] += observed != C871.transform_path(path, frame)
# C872SRC 001449|        for left in frames:
# C872SRC 001450|            for right in frames:
# C872SRC 001451|                composed = left @ right
# C872SRC 001452|                for signature in signatures:
# C872SRC 001453|                    counts["signature_product_rows"] += 1
# C872SRC 001454|                    counts["signature_product_failures"] += (
# C872SRC 001455|                        C871.transform_signature(
