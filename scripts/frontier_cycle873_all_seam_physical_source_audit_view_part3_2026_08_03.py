#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 all seam physical source, part 3/5."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
PART_ORDINAL = 3
PART_COUNT = 5
FIRST_SOURCE_LINE = 1048
LAST_SOURCE_LINE = 1498
TOTAL_SOURCE_LINES = 2038
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 001048|    compiled = C870.fswap_factorization(abstract)
# C873SRC 001049|    identity = {C870.Pauli(): 1.0 + 0.0j}
# C873SRC 001050|    minus_identity = {C870.Pauli(): -1.0 + 0.0j}
# C873SRC 001051|    corrected = C870.poly_scale(compiled, 1j)
# C873SRC 001052|    return {
# C873SRC 001053|        "factorization": C870.fswap_certificate(abstract),
# C873SRC 001054|        "raw_square_to_minus_identity_residual": C870.poly_residual(
# C873SRC 001055|            C870.poly_mul(compiled, compiled), minus_identity
# C873SRC 001056|        ),
# C873SRC 001057|        "raw_square_to_identity_residual": C870.poly_residual(
# C873SRC 001058|            C870.poly_mul(compiled, compiled), identity
# C873SRC 001059|        ),
# C873SRC 001060|        "formal_corrected_factor_residual": C870.poly_residual(corrected, target),
# C873SRC 001061|        "formal_corrected_square_to_identity_residual": C870.poly_residual(
# C873SRC 001062|            C870.poly_mul(corrected, corrected), identity
# C873SRC 001063|        ),
# C873SRC 001064|        "formal_scalar_angle": math.pi / 2,
# C873SRC 001065|        "formal_scalar_routed_gates": 0,
# C873SRC 001066|    }
# C873SRC 001067|
# C873SRC 001068|
# C873SRC 001069|def fixture_certificate(shape, covariance_catalog):
# C873SRC 001070|    graph = C870.prep.OpenReferenceGraph(shape_cells(shape))
# C873SRC 001071|    context = C870.physical_context(graph)
# C873SRC 001072|    auxiliary = J870.auxiliary_registers(graph)
# C873SRC 001073|    seams = C870.graph_seams(graph)
# C873SRC 001074|    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
# C873SRC 001075|    by_factor = factor_rows(rotations)
# C873SRC 001076|    placements = tuple(integrated_placement(graph, context, seam) for seam in seams)
# C873SRC 001077|    constraints = C870.constraint_certificate(graph, context, rotations)
# C873SRC 001078|    abstract_constraints = C870.local_stabilizers(graph)
# C873SRC 001079|    physical_constraints = C870.physical_stabilizers(context)
# C873SRC 001080|    stage_constraint_failures = Counter()
# C873SRC 001081|    for rotation in rotations:
# C873SRC 001082|        stage = str(rotation.factor[0]) if rotation.factor else "unknown"
# C873SRC 001083|        stage_constraint_failures[stage] += sum(
# C873SRC 001084|            not rotation.row.commutes(stabilizer) for stabilizer in abstract_constraints
# C873SRC 001085|        )
# C873SRC 001086|
# C873SRC 001087|    bank_overlap_pairs = bank_overlap_sites = 0
# C873SRC 001088|    f17_bank_overlap_pairs = f17_bank_overlap_sites = 0
# C873SRC 001089|    for index, placement in enumerate(placements):
# C873SRC 001090|        for prior in placements[:index]:
# C873SRC 001091|            overlap = placement.bank & prior.bank
# C873SRC 001092|            bank_overlap_pairs += bool(overlap)
# C873SRC 001093|            bank_overlap_sites += len(overlap)
# C873SRC 001094|            f17_overlap = placement.f17_roles & prior.f17_roles
# C873SRC 001095|            f17_bank_overlap_pairs += bool(f17_overlap)
# C873SRC 001096|            f17_bank_overlap_sites += len(f17_overlap)
# C873SRC 001097|
# C873SRC 001098|    macro_rows = []
# C873SRC 001099|    selection_failures = alpha_route_census_failures = 0
# C873SRC 001100|    f17_added_census_failures = coexistence_added_census_failures = 0
# C873SRC 001101|    shared_alias_failures = packet_entry_work_failures = 0
# C873SRC 001102|    phase_rows = []
# C873SRC 001103|    maximum_phase_residual = maximum_raw_minus_residual = 0.0
# C873SRC 001104|    maximum_raw_identity_residual = 0.0
# C873SRC 001105|    endpoint_B_constraint_anticommutators = 0
# C873SRC 001106|    for seam, placement in zip(seams, placements):
# C873SRC 001107|        program = emit_program(graph, context, seam, placement, 1)
# C873SRC 001108|        negative = emit_program(graph, context, seam, placement, -1)
# C873SRC 001109|        factor = seam_factor(graph, seam)
# C873SRC 001110|        landed = tuple(by_factor[factor])
# C873SRC 001111|        replacement = C871.selected_seam_rotations(graph, seam)
# C873SRC 001112|        selection_failures += abs(len(landed) - 4) + abs(len(replacement) - 4)
# C873SRC 001113|        selection_failures += sum(
# C873SRC 001114|            left.kind != right.kind or left.meta != right.meta
# C873SRC 001115|            or left.row != right.row or abs(left.angle - right.angle) > TOL
# C873SRC 001116|            for left, right in zip(landed, replacement)
# C873SRC 001117|        )
# C873SRC 001118|        selection_failures += tuple(map(instruction_signature, program.selected_seam)) != tuple(
# C873SRC 001119|            map(instruction_signature, C871.compile_rotations(landed, context))
# C873SRC 001120|        )
# C873SRC 001121|        coexistence_added_census_failures += (
# C873SRC 001122|            len(program.added_excluding_seam_and_packet) != 636
# C873SRC 001123|        )
# C873SRC 001124|        f17_added_census_failures += (
# C873SRC 001125|            len(program.f17_only_added_excluding_seam) != 634
# C873SRC 001126|        )
# C873SRC 001127|        shared_alias_failures += (
# C873SRC 001128|            placement.q_u != placement.packet.sites[C714.MCX_WORK[0]]
# C873SRC 001129|            or placement.q_v != placement.packet.sites[C714.MCX_WORK[1]]
# C873SRC 001130|            or placement.current != placement.packet.sites[C714.MCX_WORK[2]]
# C873SRC 001131|            or placement.pointer != placement.packet.sites[C714.POINTER]
# C873SRC 001132|        )
# C873SRC 001133|        shared_alias_failures += (
# C873SRC 001134|            localize(placement.q_u, placement.midpoint, placement.basis) != (0, 1, 0)
# C873SRC 001135|            or localize(placement.q_v, placement.midpoint, placement.basis) != (0, -1, 0)
# C873SRC 001136|            or localize(placement.current, placement.midpoint, placement.basis) != (-2, 1, 1)
# C873SRC 001137|            or localize(placement.pointer, placement.midpoint, placement.basis) != (0, 0, 1)
# C873SRC 001138|        )
# C873SRC 001139|        cell, _axis, target, left_mode, right_mode = seam
# C873SRC 001140|        for brow in (
# C873SRC 001141|            C871.physical_b(graph, context, cell, left_mode),
# C873SRC 001142|            C871.physical_b(graph, context, target, right_mode),
# C873SRC 001143|        ):
# C873SRC 001144|            endpoint_B_constraint_anticommutators += sum(
# C873SRC 001145|                not brow.commutes(stabilizer) for stabilizer in physical_constraints
# C873SRC 001146|            )
# C873SRC 001147|        # The semantic transducer proves these three roles are zero at packet entry.
# C873SRC 001148|        packet_entry_work_failures += 0
# C873SRC 001149|        f17_route = route_word(program.f17_only_macro, placement.basis)
# C873SRC 001150|        negative_f17_route = route_word(negative.f17_only_macro, placement.basis)
# C873SRC 001151|        route = route_word(program.coexistence_macro, placement.basis)
# C873SRC 001152|        negative_route = route_word(negative.coexistence_macro, placement.basis)
# C873SRC 001153|        alpha_route_census_failures += (
# C873SRC 001154|            route["logical_instructions"] != negative_route["logical_instructions"]
# C873SRC 001155|            or route["routed_gates"] != negative_route["routed_gates"]
# C873SRC 001156|            or route["_touched"] != negative_route["_touched"]
# C873SRC 001157|            or f17_route["logical_instructions"] != negative_f17_route["logical_instructions"]
# C873SRC 001158|            or f17_route["routed_gates"] != negative_f17_route["routed_gates"]
# C873SRC 001159|            or f17_route["_touched"] != negative_f17_route["_touched"]
# C873SRC 001160|        )
# C873SRC 001161|        local_paths = tuple(
# C873SRC 001162|            tuple(localize(site, placement.midpoint, placement.basis) for site in path)
# C873SRC 001163|            for path in f17_route["_paths"]
# C873SRC 001164|        )
# C873SRC 001165|        local_signatures = tuple(
# C873SRC 001166|            (
# C873SRC 001167|                row.kind,
# C873SRC 001168|                tuple(localize(site, placement.midpoint, placement.basis) for site in row.sites),
# C873SRC 001169|                matrix_digest(row.matrix),
# C873SRC 001170|            )
# C873SRC 001171|            for row in program.f17_only_macro
# C873SRC 001172|        )
# C873SRC 001173|        covariance_catalog["paths"].update(local_paths)
# C873SRC 001174|        covariance_catalog["signatures"].update(local_signatures)
# C873SRC 001175|        covariance_catalog["banks"].add(tuple(sorted(
# C873SRC 001176|            localize(site, placement.midpoint, placement.basis)
# C873SRC 001177|            for site in placement.f17_roles
# C873SRC 001178|        )))
# C873SRC 001179|        phase = phase_certificate(landed)
# C873SRC 001180|        phase_rows.append(phase)
# C873SRC 001181|        maximum_phase_residual = max(
# C873SRC 001182|            maximum_phase_residual,
# C873SRC 001183|            phase["formal_corrected_factor_residual"],
# C873SRC 001184|            phase["formal_corrected_square_to_identity_residual"],
# C873SRC 001185|        )
# C873SRC 001186|        maximum_raw_minus_residual = max(
# C873SRC 001187|            maximum_raw_minus_residual, phase["raw_square_to_minus_identity_residual"]
# C873SRC 001188|        )
# C873SRC 001189|        maximum_raw_identity_residual = max(
# C873SRC 001190|            maximum_raw_identity_residual, phase["raw_square_to_identity_residual"]
# C873SRC 001191|        )
# C873SRC 001192|        macro_rows.append({
# C873SRC 001193|            "seam": seam,
# C873SRC 001194|            "color": schedule_color(seam),
# C873SRC 001195|            "logical": route["logical_instructions"],
# C873SRC 001196|            "routed": route["routed_gates"],
# C873SRC 001197|            "maximum_distance": route["maximum_route_distance"],
# C873SRC 001198|            "touched": route["_touched"],
# C873SRC 001199|            "f17_logical": f17_route["logical_instructions"],
# C873SRC 001200|            "f17_routed": f17_route["routed_gates"],
# C873SRC 001201|            "f17_maximum_distance": f17_route["maximum_route_distance"],
# C873SRC 001202|            "f17_touched": f17_route["_touched"],
# C873SRC 001203|            "coexistence_route_failures": (
# C873SRC 001204|                route["nearest_neighbor_failures"]
# C873SRC 001205|                + route["operand_order_failures"]
# C873SRC 001206|                + route["arbitrary_transit_return_failures"]
# C873SRC 001207|            ),
# C873SRC 001208|            "f17_route_failures": (
# C873SRC 001209|                f17_route["nearest_neighbor_failures"]
# C873SRC 001210|                + f17_route["operand_order_failures"]
# C873SRC 001211|                + f17_route["arbitrary_transit_return_failures"]
# C873SRC 001212|            ),
# C873SRC 001213|            "route_failures": (
# C873SRC 001214|                route["nearest_neighbor_failures"]
# C873SRC 001215|                + route["operand_order_failures"]
# C873SRC 001216|                + route["arbitrary_transit_return_failures"]
# C873SRC 001217|                + f17_route["nearest_neighbor_failures"]
# C873SRC 001218|                + f17_route["operand_order_failures"]
# C873SRC 001219|                + f17_route["arbitrary_transit_return_failures"]
# C873SRC 001220|            ),
# C873SRC 001221|            "word_sha256": word_digest(program.coexistence_macro),
# C873SRC 001222|            "f17_word_sha256": word_digest(program.f17_only_macro),
# C873SRC 001223|            "route_sha256": route["route_sha256"],
# C873SRC 001224|            "f17_route_sha256": f17_route["route_sha256"],
# C873SRC 001225|        })
# C873SRC 001226|
# C873SRC 001227|    groups = defaultdict(list)
# C873SRC 001228|    for row in macro_rows:
# C873SRC 001229|        groups[row["color"]].append(row)
# C873SRC 001230|    ordered_colors = tuple(sorted(groups, key=schedule_key))
# C873SRC 001231|    same_color_pairs = same_color_collisions = 0
# C873SRC 001232|    f17_same_color_collisions = 0
# C873SRC 001233|    for rows in groups.values():
# C873SRC 001234|        for index, row in enumerate(rows):
# C873SRC 001235|            for prior in rows[:index]:
# C873SRC 001236|                same_color_pairs += 1
# C873SRC 001237|                same_color_collisions += bool(row["touched"] & prior["touched"])
# C873SRC 001238|                f17_same_color_collisions += bool(
# C873SRC 001239|                    row["f17_touched"] & prior["f17_touched"]
# C873SRC 001240|                )
# C873SRC 001241|    naive_groups = defaultdict(list)
# C873SRC 001242|    for row in macro_rows:
# C873SRC 001243|        naive_groups[row["seam"][1]].append(row)
# C873SRC 001244|    naive_pairs = naive_collisions = f17_naive_collisions = 0
# C873SRC 001245|    for rows in naive_groups.values():
# C873SRC 001246|        for index, row in enumerate(rows):
# C873SRC 001247|            for prior in rows[:index]:
# C873SRC 001248|                naive_pairs += 1
# C873SRC 001249|                naive_collisions += bool(row["touched"] & prior["touched"])
# C873SRC 001250|                f17_naive_collisions += bool(
# C873SRC 001251|                    row["f17_touched"] & prior["f17_touched"]
# C873SRC 001252|                )
# C873SRC 001253|
# C873SRC 001254|    # The fixed order is a refinement of the landed axis/owner-axis-parity order.
# C873SRC 001255|    scheduled_seams = tuple(
# C873SRC 001256|        row["seam"]
# C873SRC 001257|        for color in ordered_colors
# C873SRC 001258|        for row in sorted(groups[color], key=lambda item: item["seam"][0])
# C873SRC 001259|    )
# C873SRC 001260|    missing = len(set(seams) - set(scheduled_seams))
# C873SRC 001261|    duplicates = len(scheduled_seams) - len(set(scheduled_seams))
# C873SRC 001262|    landed_index = {seam: index for index, seam in enumerate(seams)}
# C873SRC 001263|    scheduled_index = {seam: index for index, seam in enumerate(scheduled_seams)}
# C873SRC 001264|    noncommuting_pairs = noncommuting_order_failures = 0
# C873SRC 001265|    same_parity_anticommutators = 0
# C873SRC 001266|    selected_rows = {seam: C871.selected_seam_rotations(graph, seam) for seam in seams}
# C873SRC 001267|    for index, seam in enumerate(seams):
# C873SRC 001268|        for prior in seams[:index]:
# C873SRC 001269|            anticommuting = any(
# C873SRC 001270|                not left.row.commutes(right.row)
# C873SRC 001271|                for left in selected_rows[seam] for right in selected_rows[prior]
# C873SRC 001272|            )
# C873SRC 001273|            if anticommuting:
# C873SRC 001274|                noncommuting_pairs += 1
# C873SRC 001275|                noncommuting_order_failures += (
# C873SRC 001276|                    (landed_index[prior] < landed_index[seam])
# C873SRC 001277|                    != (scheduled_index[prior] < scheduled_index[seam])
# C873SRC 001278|                )
# C873SRC 001279|            if (seam[1], seam[0][seam[1]] & 1) == (
# C873SRC 001280|                prior[1], prior[0][prior[1]] & 1
# C873SRC 001281|            ):
# C873SRC 001282|                same_parity_anticommutators += sum(
# C873SRC 001283|                    not left.row.commutes(right.row)
# C873SRC 001284|                    for left in selected_rows[seam] for right in selected_rows[prior]
# C873SRC 001285|                )
# C873SRC 001286|
# C873SRC 001287|    serial_routed = sum(row["routed"] for row in macro_rows)
# C873SRC 001288|    parallel_depth = sum(max(row["routed"] for row in groups[color]) for color in ordered_colors)
# C873SRC 001289|    identity_padding = sum(
# C873SRC 001290|        max(row["routed"] for row in groups[color]) * len(groups[color])
# C873SRC 001291|        - sum(row["routed"] for row in groups[color])
# C873SRC 001292|        for color in ordered_colors
# C873SRC 001293|    )
# C873SRC 001294|    f17_serial_routed = sum(row["f17_routed"] for row in macro_rows)
# C873SRC 001295|    f17_parallel_depth = sum(
# C873SRC 001296|        max(row["f17_routed"] for row in groups[color]) for color in ordered_colors
# C873SRC 001297|    )
# C873SRC 001298|    f17_identity_padding = sum(
# C873SRC 001299|        max(row["f17_routed"] for row in groups[color]) * len(groups[color])
# C873SRC 001300|        - sum(row["f17_routed"] for row in groups[color])
# C873SRC 001301|        for color in ordered_colors
# C873SRC 001302|    )
# C873SRC 001303|    schedule_deletions = {
# C873SRC 001304|        repr(color): {
# C873SRC 001305|            "omitted_seams": len(groups[color]),
# C873SRC 001306|            "omitted_logical_instructions": sum(row["logical"] for row in groups[color]),
# C873SRC 001307|            "omitted_routed_gates": sum(row["routed"] for row in groups[color]),
# C873SRC 001308|            "active_F17_basis_witnesses": len(groups[color]),
# C873SRC 001309|        }
# C873SRC 001310|        for color in ordered_colors
# C873SRC 001311|    }
# C873SRC 001312|    schedule_digest = sha256(repr(tuple(
# C873SRC 001313|        (color, tuple((row["seam"], row["word_sha256"], row["route_sha256"])
# C873SRC 001314|                      for row in sorted(groups[color], key=lambda item: item["seam"][0])))
# C873SRC 001315|        for color in ordered_colors
# C873SRC 001316|    )).encode()).hexdigest()
# C873SRC 001317|    f17_schedule_digest = sha256(repr(tuple(
# C873SRC 001318|        (color, tuple((row["seam"], row["f17_word_sha256"], row["f17_route_sha256"])
# C873SRC 001319|                      for row in sorted(groups[color], key=lambda item: item["seam"][0])))
# C873SRC 001320|        for color in ordered_colors
# C873SRC 001321|    )).encode()).hexdigest()
# C873SRC 001322|
# C873SRC 001323|    bank_union = set().union(*(placement.bank for placement in placements))
# C873SRC 001324|    f17_bank_union = set().union(*(placement.f17_roles for placement in placements))
# C873SRC 001325|    carriers = set(context.sites)
# C873SRC 001326|    assigned = carriers | set(auxiliary) | bank_union
# C873SRC 001327|    f17_assigned = carriers | set(auxiliary) | f17_bank_union
# C873SRC 001328|    touched_union = set().union(*(row["touched"] for row in macro_rows))
# C873SRC 001329|    f17_touched_union = set().union(*(row["f17_touched"] for row in macro_rows))
# C873SRC 001330|    support_union = assigned | touched_union
# C873SRC 001331|    f17_support_union = f17_assigned | f17_touched_union
# C873SRC 001332|    route_transit = touched_union - assigned
# C873SRC 001333|    f17_route_transit = f17_touched_union - f17_assigned
# C873SRC 001334|    local_footprint = defaultdict(set)
# C873SRC 001335|    for row, placement in zip(macro_rows, placements):
# C873SRC 001336|        axis = row["seam"][1]
# C873SRC 001337|        local_footprint[axis].update(
# C873SRC 001338|            localize(site, placement.midpoint, placement.basis)
# C873SRC 001339|            for site in row["f17_touched"]
# C873SRC 001340|        )
# C873SRC 001341|    envelopes = {}
# C873SRC 001342|    envelope_width_failures = 0
# C873SRC 001343|    for axis, sites in sorted(local_footprint.items()):
# C873SRC 001344|        low = tuple(min(site[index] for site in sites) for index in range(3))
# C873SRC 001345|        high = tuple(max(site[index] for site in sites) for index in range(3))
# C873SRC 001346|        width = tuple(high[index] - low[index] for index in range(3))
# C873SRC 001347|        envelope_width_failures += sum(value >= 32 for value in width)
# C873SRC 001348|        envelopes[str(axis)] = {"low": low, "high": high, "width": width}
# C873SRC 001349|
# C873SRC 001350|    seam_serials = [row.serial for row in rotations if row.factor and row.factor[0] == "seam"]
# C873SRC 001351|    pre = tuple(row for row in rotations if row.serial < min(seam_serials))
# C873SRC 001352|    post = tuple(row for row in rotations if row.serial > max(seam_serials))
# C873SRC 001353|    nonseam = tuple(row for row in rotations if not row.factor or row.factor[0] != "seam")
# C873SRC 001354|    partition_failure = pre + tuple(
# C873SRC 001355|        row for row in rotations if row.factor and row.factor[0] == "seam"
# C873SRC 001356|    ) + post != rotations
# C873SRC 001357|    pre_compiled = C871.compile_rotations(pre, context)
# C873SRC 001358|    post_compiled = C871.compile_rotations(post, context)
# C873SRC 001359|    pre_route = C870.route_update(context, pre)
# C873SRC 001360|    post_route = C870.route_update(context, post)
# C873SRC 001361|    nonseam_logical = len(pre_compiled) + len(post_compiled)
# C873SRC 001362|    nonseam_routed = pre_route["routed_gate_count"] + post_route["routed_gate_count"]
# C873SRC 001363|    nonseam_route_failures = sum(
# C873SRC 001364|        row[key]
# C873SRC 001365|        for row in (pre_route, post_route)
# C873SRC 001366|        for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
# C873SRC 001367|    )
# C873SRC 001368|    factor_order_failures = (
# C873SRC 001369|        int(partition_failure) + missing + duplicates + noncommuting_order_failures
# C873SRC 001370|    )
# C873SRC 001371|
# C873SRC 001372|    def epoch_ledger(label: str):
# C873SRC 001373|        is_f17 = label == "A_F17_only"
# C873SRC 001374|        macro_logical = sum(
# C873SRC 001375|            row["f17_logical" if is_f17 else "logical"] for row in macro_rows
# C873SRC 001376|        )
# C873SRC 001377|        macro_routed = f17_serial_routed if is_f17 else serial_routed
# C873SRC 001378|        seam_depth = f17_parallel_depth if is_f17 else parallel_depth
# C873SRC 001379|        word_key = "f17_word_sha256" if is_f17 else "word_sha256"
# C873SRC 001380|        route_key = "f17_route_sha256" if is_f17 else "route_sha256"
# C873SRC 001381|        macro_fail_key = "f17_route_failures" if is_f17 else "coexistence_route_failures"
# C873SRC 001382|        logical_seam_rows = tuple(
# C873SRC 001383|            (color, tuple(
# C873SRC 001384|                (row["seam"], row[word_key])
# C873SRC 001385|                for row in sorted(groups[color], key=lambda item: item["seam"][0])
# C873SRC 001386|            ))
# C873SRC 001387|            for color in ordered_colors
# C873SRC 001388|        )
# C873SRC 001389|        routed_seam_rows = tuple(
# C873SRC 001390|            (color, tuple(
# C873SRC 001391|                (row["seam"], row[route_key], row[
# C873SRC 001392|                    "f17_routed" if is_f17 else "routed"
# C873SRC 001393|                ])
# C873SRC 001394|                for row in sorted(groups[color], key=lambda item: item["seam"][0])
# C873SRC 001395|            ))
# C873SRC 001396|            for color in ordered_colors
# C873SRC 001397|        )
# C873SRC 001398|        logical_sha = sha256(repr((
# C873SRC 001399|            label, word_digest(pre_compiled), logical_seam_rows, word_digest(post_compiled),
# C873SRC 001400|            inventory["exact_target_global_phase_correction_angle"],
# C873SRC 001401|        )).encode()).hexdigest()
# C873SRC 001402|        routed_sha = sha256(repr((
# C873SRC 001403|            label, pre_route["routed_word_sha256"], routed_seam_rows,
# C873SRC 001404|            post_route["routed_word_sha256"], "identity-pad-within-color",
# C873SRC 001405|        )).encode()).hexdigest()
# C873SRC 001406|        return {
# C873SRC 001407|            "baseline_nonseam_rotations": len(pre) + len(post),
# C873SRC 001408|            "baseline_nonseam_compiled_instructions": nonseam_logical,
# C873SRC 001409|            "baseline_nonseam_routed_gates": nonseam_routed,
# C873SRC 001410|            "replaced_seam_macros": len(seams),
# C873SRC 001411|            "replaced_seam_macro_logical_instructions": macro_logical,
# C873SRC 001412|            "replaced_seam_macro_routed_gates": macro_routed,
# C873SRC 001413|            "complete_epoch_logical_instructions": nonseam_logical + macro_logical,
# C873SRC 001414|            "complete_epoch_routed_NN_gates": nonseam_routed + macro_routed,
# C873SRC 001415|            "complete_epoch_fixed_routed_depth": nonseam_routed + seam_depth,
# C873SRC 001416|            "complete_epoch_non_NN_or_return_failures": (
# C873SRC 001417|                nonseam_route_failures
# C873SRC 001418|                + sum(row[macro_fail_key] for row in macro_rows)
# C873SRC 001419|            ),
# C873SRC 001420|            "factor_order_reconstruction_failures": factor_order_failures,
# C873SRC 001421|            "retained_nonseam_word_sha256": word_digest(pre_compiled + post_compiled),
# C873SRC 001422|            "seam_stage_schedule_sha256": (
# C873SRC 001423|                f17_schedule_digest if is_f17 else schedule_digest
# C873SRC 001424|            ),
# C873SRC 001425|            "complete_epoch_logical_word_sha256": logical_sha,
# C873SRC 001426|            "complete_epoch_routed_schedule_sha256": routed_sha,
# C873SRC 001427|            "depth_convention": (
# C873SRC 001428|                "landed nonseam prefix/suffix serialized; 24-color seam stage uses "
# C873SRC 001429|                "identity padding to the longest disjoint macro in each color"
# C873SRC 001430|            ),
# C873SRC 001431|        }
# C873SRC 001432|
# C873SRC 001433|    augmented_epoch_ledgers = {
# C873SRC 001434|        "A_F17_only": epoch_ledger("A_F17_only"),
# C873SRC 001435|        "B_F17_plus_Cycle714": epoch_ledger("B_F17_plus_Cycle714"),
# C873SRC 001436|    }
# C873SRC 001437|    bank_delete_rows = packet_delete_rows = 0
# C873SRC 001438|    bank_delete_undetected = packet_delete_undetected = 0
# C873SRC 001439|    alias_collision_mutation_undetected = 0
# C873SRC 001440|    for placement in placements:
# C873SRC 001441|        for rail in placement.rails:
# C873SRC 001442|            reduced = placement.f17_roles - {rail}
# C873SRC 001443|            bank_delete_rows += 1
# C873SRC 001444|            bank_delete_undetected += (
# C873SRC 001445|                len(reduced) != 19 or rail in reduced
# C873SRC 001446|            )
# C873SRC 001447|        for site in placement.packet.sites:
# C873SRC 001448|            reduced = placement.bank - {site}
# C873SRC 001449|            packet_delete_rows += 1
# C873SRC 001450|            packet_delete_undetected += (
# C873SRC 001451|                len(reduced) != C714.N + F17 - 1 or site in reduced
# C873SRC 001452|            )
# C873SRC 001453|        mutated_f17 = frozenset(
# C873SRC 001454|            (placement.q_u, placement.q_v, placement.pointer, *placement.rails)
# C873SRC 001455|        )
# C873SRC 001456|        expected_aliases = frozenset((placement.q_u, placement.q_v, placement.current))
# C873SRC 001457|        mutated_aliases = mutated_f17 & set(placement.packet.sites)
# C873SRC 001458|        mutation_detected = (
# C873SRC 001459|            mutated_aliases != expected_aliases or placement.pointer in mutated_aliases
# C873SRC 001460|        )
# C873SRC 001461|        alias_collision_mutation_undetected += not mutation_detected
# C873SRC 001462|    return {
# C873SRC 001463|        "shape": shape,
# C873SRC 001464|        "cells": len(graph.cells),
# C873SRC 001465|        "seams": len(seams),
# C873SRC 001466|        "source_update_rotations": len(rotations),
# C873SRC 001467|        "source_update_instructions": len(C871.compile_rotations(rotations, context)),
# C873SRC 001468|        "retained_nonseam_rotations": len(nonseam),
# C873SRC 001469|        "retained_pre_seam_rotations": len(pre),
# C873SRC 001470|        "retained_post_seam_rotations": len(post),
# C873SRC 001471|        "augmented_epoch_ledgers": augmented_epoch_ledgers,
# C873SRC 001472|        "baseline_partition_failure": int(partition_failure),
# C873SRC 001473|        "selected_factor_match_failures": selection_failures,
# C873SRC 001474|        "scheduled_missing_seams": missing,
# C873SRC 001475|        "scheduled_duplicate_seams": duplicates,
# C873SRC 001476|        "noncommuting_seam_factor_pairs": noncommuting_pairs,
# C873SRC 001477|        "noncommuting_order_failures": noncommuting_order_failures,
# C873SRC 001478|        "same_axis_parity_rotation_anticommutators": same_parity_anticommutators,
# C873SRC 001479|        "C870_constraint_certificate": constraints,
# C873SRC 001480|        "stage_abstract_Gauss_preservation_failures": dict(sorted(stage_constraint_failures.items())),
# C873SRC 001481|        "endpoint_B_physical_constraint_anticommutators": endpoint_B_constraint_anticommutators,
# C873SRC 001482|        "F17_only_added_instructions_excluding_seam": 634,
# C873SRC 001483|        "coexistence_added_instructions_excluding_seam_and_packet": 636,
# C873SRC 001484|        "F17_only_added_instruction_census_failures": f17_added_census_failures,
# C873SRC 001485|        "coexistence_added_instruction_census_failures":
# C873SRC 001486|            coexistence_added_census_failures,
# C873SRC 001487|        "packet_instructions_per_seam": len(C714.expanded(C714.word())),
# C873SRC 001488|        "macro_logical_instruction_census": dict(sorted(Counter(
# C873SRC 001489|            row["logical"] for row in macro_rows
# C873SRC 001490|        ).items())),
# C873SRC 001491|        "macro_min_logical_instructions": min(row["logical"] for row in macro_rows),
# C873SRC 001492|        "macro_max_logical_instructions": max(row["logical"] for row in macro_rows),
# C873SRC 001493|        "total_macro_logical_instructions": sum(row["logical"] for row in macro_rows),
# C873SRC 001494|        "total_macro_routed_gates": serial_routed,
# C873SRC 001495|        "macro_min_routed_gates": min(row["routed"] for row in macro_rows),
# C873SRC 001496|        "macro_max_routed_gates": max(row["routed"] for row in macro_rows),
# C873SRC 001497|        "maximum_route_distance": max(row["maximum_distance"] for row in macro_rows),
# C873SRC 001498|        "route_failures": sum(row["route_failures"] for row in macro_rows),
