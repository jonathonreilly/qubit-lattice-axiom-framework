#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 local constraints source, part 2/3."""

TARGET_SOURCE = "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 3
FIRST_SOURCE_LINE = 530
LAST_SOURCE_LINE = 994
TOTAL_SOURCE_LINES = 1092
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "70d7362a2f534bd94b5b421f38e0c0509483ed8c1962b83f21f790b4c1dcb685"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000530|        )
# C873SRC 000531|    }
# C873SRC 000532|    failures = (
# C873SRC 000533|        sum(value > TOL for value in commutators.values())
# C873SRC 000534|        + sum(value > TOL for value in unitarity.values())
# C873SRC 000535|        + int(np.linalg.norm(reconstructed - coin) > TOL)
# C873SRC 000536|        + sum(value == 0 for value in onsite_census.values())
# C873SRC 000537|        + int(hostile <= 1.0e-3)
# C873SRC 000538|    )
# C873SRC 000539|    return {
# C873SRC 000540|        "basis_occupation_columns": 64,
# C873SRC 000541|        "matter_clock": "diag(omega^N_x) on all six-mode occupation words",
# C873SRC 000542|        "link_action": "identity for all three onsite stages",
# C873SRC 000543|        "physical_target_bridge": (
# C873SRC 000544|            "pinned Cycle870 emitted-word intertwiners supply the physical-to-target "
# C873SRC 000545|            "step; this certificate executes the target-to-F17-star commutators"
# C873SRC 000546|        ),
# C873SRC 000547|        "coin_schedule_gates": len(coin_gates),
# C873SRC 000548|        "coin_schedule_reconstruction_residual": float(
# C873SRC 000549|            np.linalg.norm(reconstructed - coin)
# C873SRC 000550|        ),
# C873SRC 000551|        "live_L2_onsite_rotation_census": onsite_census,
# C873SRC 000552|        "star_clock_commutator_residuals": commutators,
# C873SRC 000553|        "unitarity_residuals": unitarity,
# C873SRC 000554|        "bare_occupation_flip_control_commutator": hostile,
# C873SRC 000555|        "failures": int(failures),
# C873SRC 000556|    }
# C873SRC 000557|
# C873SRC 000558|
# C873SRC 000559|def object_a_preservation_certificate(fixtures_for_transport):
# C873SRC 000560|    all_seams = sum(len(edges) for _vertices, edges, _faces in fixtures_for_transport)
# C873SRC 000561|    all_plaquettes = sum(len(faces) for _vertices, _edges, faces in fixtures_for_transport)
# C873SRC 000562|    seam_rows = star_failures = onehot_failures = 0
# C873SRC 000563|    plaquette_commutator_failures = 0
# C873SRC 000564|    for _seam in range(all_seams):
# C873SRC 000565|        for alpha in (-1, 1):
# C873SRC 000566|            family_sign = alpha
# C873SRC 000567|            for a, b in product((0, 1), repeat=2):
# C873SRC 000568|                for label in range(F17):
# C873SRC 000569|                    for rest_u, rest_v in product(range(6), repeat=2):
# C873SRC 000570|                        before = (
# C873SRC 000571|                            (rest_u + a + family_sign * label) % F17,
# C873SRC 000572|                            (rest_v + b - family_sign * label) % F17,
# C873SRC 000573|                        )
# C873SRC 000574|                        after_label = (label + alpha * (a - b)) % F17
# C873SRC 000575|                        after = (
# C873SRC 000576|                            (rest_u + b + family_sign * after_label) % F17,
# C873SRC 000577|                            (rest_v + a - family_sign * after_label) % F17,
# C873SRC 000578|                        )
# C873SRC 000579|                        seam_rows += 1
# C873SRC 000580|                        star_failures += before != after
# C873SRC 000581|                        onehot_failures += not (0 <= after_label < F17)
# C873SRC 000582|                    for plaquette_step in (-1, 1):
# C873SRC 000583|                        left = (label + plaquette_step + alpha * (a - b)) % F17
# C873SRC 000584|                        right = (label + alpha * (a - b) + plaquette_step) % F17
# C873SRC 000585|                        plaquette_commutator_failures += left != right
# C873SRC 000586|    operator_pairs = operator_rows = operator_failures = 0
# C873SRC 000587|    for _vertices, edges, faces in fixtures_for_transport:
# C873SRC 000588|        edge_index = {edge: index for index, edge in enumerate(edges)}
# C873SRC 000589|        for seam_edge in edges:
# C873SRC 000590|            seam_index = edge_index[seam_edge]
# C873SRC 000591|            for face in faces:
# C873SRC 000592|                boundary = np.zeros(len(edges), dtype=np.int64)
# C873SRC 000593|                for edge, coefficient in plaquette_boundary(face).items():
# C873SRC 000594|                    boundary[edge_index[edge]] = coefficient
# C873SRC 000595|                operator_pairs += 1
# C873SRC 000596|                for current in (-1, 0, 1):
# C873SRC 000597|                    seam_shift = np.zeros(len(edges), dtype=np.int64)
# C873SRC 000598|                    seam_shift[seam_index] = current
# C873SRC 000599|                    operator_rows += 1
# C873SRC 000600|                    operator_failures += not np.array_equal(
# C873SRC 000601|                        (seam_shift + boundary) % F17,
# C873SRC 000602|                        (boundary + seam_shift) % F17,
# C873SRC 000603|                    )
# C873SRC 000604|    onsite = onsite_stage_star_clock_certificate()
# C873SRC 000605|    return {
# C873SRC 000606|        "all_seams": all_seams,
# C873SRC 000607|        "all_plaquettes": all_plaquettes,
# C873SRC 000608|        "seam_star_basis_rows": seam_rows,
# C873SRC 000609|        "seam_star_preservation_failures": star_failures,
# C873SRC 000610|        "seam_one_hot_label_failures": onehot_failures,
# C873SRC 000611|        "seam_plaquette_translation_commutator_rows": all_seams * 2 * 4 * F17 * 2,
# C873SRC 000612|        "seam_plaquette_translation_commutator_failures": plaquette_commutator_failures,
# C873SRC 000613|        "all_seam_all_plaquette_operator_pairs": operator_pairs,
# C873SRC 000614|        "all_seam_all_plaquette_current_rows": operator_rows,
# C873SRC 000615|        "all_seam_all_plaquette_commutator_failures": operator_failures,
# C873SRC 000616|        "onsite_stage_preservation": onsite,
# C873SRC 000617|        "onsite_stage_preservation_failures": onsite["failures"],
# C873SRC 000618|        "full_augmented_epoch_constraint_preservation_failures": (
# C873SRC 000619|            star_failures + onehot_failures + plaquette_commutator_failures
# C873SRC 000620|            + operator_failures + onsite["failures"]
# C873SRC 000621|        ),
# C873SRC 000622|    }
# C873SRC 000623|
# C873SRC 000624|
# C873SRC 000625|def fixture_certificate(shape):
# C873SRC 000626|    graph = C870.prep.OpenReferenceGraph(shape_cells(shape))
# C873SRC 000627|    context = C870.physical_context(graph)
# C873SRC 000628|    vertices = tuple(graph.cells)
# C873SRC 000629|    edges = graph_edges(graph)
# C873SRC 000630|    faces = plaquettes(shape)
# C873SRC 000631|    incidence, boundary = chain_matrices(vertices, edges, faces)
# C873SRC 000632|    incidence_rank = matrix_rank_mod(incidence)
# C873SRC 000633|    boundary_rank = matrix_rank_mod(boundary)
# C873SRC 000634|    cycle_rank = len(edges) - incidence_rank
# C873SRC 000635|    boundary_squared_failures = int(np.count_nonzero((incidence @ boundary) % F17))
# C873SRC 000636|    placements = placement_map(graph, context)
# C873SRC 000637|
# C873SRC 000638|    f17_banks = tuple(placement.f17_roles for placement in placements.values())
# C873SRC 000639|    pair_overlap_sites = sum(
# C873SRC 000640|        len(bank & prior)
# C873SRC 000641|        for index, bank in enumerate(f17_banks)
# C873SRC 000642|        for prior in f17_banks[:index]
# C873SRC 000643|    )
# C873SRC 000644|    carrier_aux = set(context.sites) | set(J870.auxiliary_registers(graph))
# C873SRC 000645|    bank_carrier_aux_collisions = sum(len(bank & carrier_aux) for bank in f17_banks)
# C873SRC 000646|    onehot_radius_failures = onehot_path_failures = 0
# C873SRC 000647|    onehot_geometries = []
# C873SRC 000648|    for placement in placements.values():
# C873SRC 000649|        onehot_radius_failures += max(
# C873SRC 000650|            max(map(abs, INT.localize(site, placement.midpoint, placement.basis)))
# C873SRC 000651|            for site in placement.rails
# C873SRC 000652|        ) > 2
# C873SRC 000653|        onehot_path_failures += sum(
# C873SRC 000654|            l1(left, right) != 1
# C873SRC 000655|            for left, right in zip(placement.rails, placement.rails[1:])
# C873SRC 000656|        )
# C873SRC 000657|        onehot_geometries.append(support_geometry(placement.rails, placement.midpoint))
# C873SRC 000658|
# C873SRC 000659|    plaquette_supports = []
# C873SRC 000660|    word_failures = layer_collisions = deletion_undetected = 0
# C873SRC 000661|    word_hash = sha256()
# C873SRC 000662|    for face in faces:
# C873SRC 000663|        word, layers = plaquette_swap_word(face, placements)
# C873SRC 000664|        support = set(site for _edge, _coefficient, pair in word for site in pair)
# C873SRC 000665|        center = add(scale(16, face[0]), scale(8, unit(face[1])), scale(8, unit(face[2])))
# C873SRC 000666|        geometry = support_geometry(support, center)
# C873SRC 000667|        plaquette_supports.append(geometry)
# C873SRC 000668|        word_failures += len(word) != 64
# C873SRC 000669|        word_failures += geometry["M2"] != 68
# C873SRC 000670|        word_failures += sum(l1(*pair) != 1 for _edge, _coefficient, pair in word)
# C873SRC 000671|        for layer in layers:
# C873SRC 000672|            sites = [site for _edge, _coefficient, pair in layer for site in pair]
# C873SRC 000673|            layer_collisions += len(sites) != len(set(sites))
# C873SRC 000674|        for edge, coefficient in plaquette_boundary(face).items():
# C873SRC 000675|            full = tuple(
# C873SRC 000676|                (label + coefficient) % F17 for label in range(F17)
# C873SRC 000677|            )
# C873SRC 000678|            for omitted in range(16):
# C873SRC 000679|                damaged = tuple(
# C873SRC 000680|                    int(math.log2(INT.apply_unary(1 << label, coefficient, omitted)))
# C873SRC 000681|                    for label in range(F17)
# C873SRC 000682|                )
# C873SRC 000683|                deletion_undetected += damaged == full
# C873SRC 000684|        word_hash.update(repr((face, word)).encode())
# C873SRC 000685|
# C873SRC 000686|    star_supports = []
# C873SRC 000687|    star_constraint_failures = 0
# C873SRC 000688|    physical_stabilizers = C870.physical_stabilizers(context)
# C873SRC 000689|    star_clock_rows = []
# C873SRC 000690|    star_clock_hash = sha256()
# C873SRC 000691|    standard_basis = (unit(0), unit(1), unit(2))
# C873SRC 000692|    for cell in vertices:
# C873SRC 000693|        matter = set()
# C873SRC 000694|        for mode in range(6):
# C873SRC 000695|            row = C871.physical_b(graph, context, cell, mode)
# C873SRC 000696|            matter.update(C871.z_support(row, context))
# C873SRC 000697|            star_constraint_failures += sum(
# C873SRC 000698|                not row.commutes(stabilizer)
# C873SRC 000699|                for stabilizer in physical_stabilizers
# C873SRC 000700|            )
# C873SRC 000701|        incident = tuple(
# C873SRC 000702|            edge for edge in edges if edge[0] == cell or edge_head(edge) == cell
# C873SRC 000703|        )
# C873SRC 000704|        link_sites = set().union(*(set(placements[edge].rails) for edge in incident))
# C873SRC 000705|        support = matter | link_sites
# C873SRC 000706|        star_supports.append({
# C873SRC 000707|            "degree": len(incident),
# C873SRC 000708|            "matter_M2": len(matter),
# C873SRC 000709|            "link_rail_M2": len(link_sites),
# C873SRC 000710|            **support_geometry(support, scale(16, cell)),
# C873SRC 000711|        })
# C873SRC 000712|        clock_word, _incident = star_clock_word(
# C873SRC 000713|            graph, context, cell, edges, placements, 1
# C873SRC 000714|        )
# C873SRC 000715|        negative_clock_word, _ = star_clock_word(
# C873SRC 000716|            graph, context, cell, edges, placements, -1
# C873SRC 000717|        )
# C873SRC 000718|        clock_route = INT.route_word(clock_word, standard_basis)
# C873SRC 000719|        negative_route = INT.route_word(negative_clock_word, standard_basis)
# C873SRC 000720|        route_failures = sum(
# C873SRC 000721|            clock_route[key] for key in (
# C873SRC 000722|                "nearest_neighbor_failures", "operand_order_failures",
# C873SRC 000723|                "arbitrary_transit_return_failures",
# C873SRC 000724|            )
# C873SRC 000725|        )
# C873SRC 000726|        route_failures += sum(
# C873SRC 000727|            negative_route[key] for key in (
# C873SRC 000728|                "nearest_neighbor_failures", "operand_order_failures",
# C873SRC 000729|                "arbitrary_transit_return_failures",
# C873SRC 000730|            )
# C873SRC 000731|        )
# C873SRC 000732|        alpha_route_mismatch = (
# C873SRC 000733|            clock_route["logical_instructions"] != negative_route["logical_instructions"]
# C873SRC 000734|            or clock_route["routed_gates"] != negative_route["routed_gates"]
# C873SRC 000735|            or clock_route["_touched"] != negative_route["_touched"]
# C873SRC 000736|        )
# C873SRC 000737|        star_clock_rows.append({
# C873SRC 000738|            "logical": len(clock_word),
# C873SRC 000739|            "routed": clock_route["routed_gates"],
# C873SRC 000740|            "maximum_distance": clock_route["maximum_route_distance"],
# C873SRC 000741|            "route_failures": route_failures,
# C873SRC 000742|            "alpha_route_mismatch": int(alpha_route_mismatch),
# C873SRC 000743|            "link_clock_phase_gates": sum(
# C873SRC 000744|                row.kind == "F17_star_link_clock_phase" for row in clock_word
# C873SRC 000745|            ),
# C873SRC 000746|            "matter_axis_RZ_gates": sum(row.kind == "axis_RZ" for row in clock_word),
# C873SRC 000747|        })
# C873SRC 000748|        star_clock_hash.update(repr(tuple(
# C873SRC 000749|            INT.instruction_signature(row) for row in clock_word
# C873SRC 000750|        )).encode())
# C873SRC 000751|
# C873SRC 000752|    plaquette_dependency = len(faces) - boundary_rank
# C873SRC 000753|    fixed_divergence_dimension = F17 ** cycle_rank
# C873SRC 000754|    plus_one_dimension = F17 ** (cycle_rank - boundary_rank)
# C873SRC 000755|    return {
# C873SRC 000756|        "shape": shape,
# C873SRC 000757|        "vertices": len(vertices),
# C873SRC 000758|        "oriented_links": len(edges),
# C873SRC 000759|        "plaquettes": len(faces),
# C873SRC 000760|        "physical_unary_link_M2": F17 * len(edges),
# C873SRC 000761|        "Object_A_total_bank_M2_including_three_clean_work_per_link": 20 * len(edges),
# C873SRC 000762|        "incidence_rank_mod17": incidence_rank,
# C873SRC 000763|        "expected_connected_incidence_rank": len(vertices) - 1,
# C873SRC 000764|        "independent_link_star_constraints_at_fixed_matter": incidence_rank,
# C873SRC 000765|        "global_star_compatibility": "sum_x(g_x-N_x)=0 mod17",
# C873SRC 000766|        "cycle_space_rank": cycle_rank,
# C873SRC 000767|        "plaquette_boundary_rank_mod17": boundary_rank,
# C873SRC 000768|        "plaquette_dependency_count": plaquette_dependency,
# C873SRC 000769|        "boundary_of_boundary_nonzero_entries": boundary_squared_failures,
# C873SRC 000770|        "fixed_star_divergence_link_sector_dimension": fixed_divergence_dimension,
# C873SRC 000771|        "uniform_cycle_plus_one_sector_dimension": plus_one_dimension,
# C873SRC 000772|        "unique_uniform_cycle_state_in_each_consistent_fixed_star_sector":
# C873SRC 000773|            plus_one_dimension == 1,
# C873SRC 000774|        "one_hot_constraint": {
# C873SRC 000775|            "per_link_physical_support_M2": F17,
# C873SRC 000776|            "maximum_Linf_radius": max(row["Linf_radius"] for row in onehot_geometries),
# C873SRC 000777|            "maximum_L1_radius": max(row["L1_radius"] for row in onehot_geometries),
# C873SRC 000778|            "maximum_L1_diameter": max(row["L1_diameter"] for row in onehot_geometries),
# C873SRC 000779|            "radius_failures": onehot_radius_failures,
# C873SRC 000780|            "rail_path_NN_failures": onehot_path_failures,
# C873SRC 000781|        },
# C873SRC 000782|        "star_constraint": {
# C873SRC 000783|            "definition": (
# C873SRC 000784|                "A_x=omega^(N_x+alpha[sum_out ell-sum_in ell]), alpha in {-1,+1}; "
# C873SRC 000785|                "P_{g,x}=17^-1 sum_t omega^(-tg) A_x^t"
# C873SRC 000786|            ),
# C873SRC 000787|            "maximum_degree": max(row["degree"] for row in star_supports),
# C873SRC 000788|            "maximum_physical_support_M2": max(row["M2"] for row in star_supports),
# C873SRC 000789|            "maximum_matter_support_M2": max(row["matter_M2"] for row in star_supports),
# C873SRC 000790|            "maximum_link_rail_support_M2": max(row["link_rail_M2"] for row in star_supports),
# C873SRC 000791|            "maximum_Linf_radius": max(row["Linf_radius"] for row in star_supports),
# C873SRC 000792|            "maximum_L1_radius": max(row["L1_radius"] for row in star_supports),
# C873SRC 000793|            "maximum_L1_diameter": max(row["L1_diameter"] for row in star_supports),
# C873SRC 000794|            "encoded_matter_constraint_anticommutators": star_constraint_failures,
# C873SRC 000795|            "emitted_star_clock_word": {
# C873SRC 000796|                "minimum_logical_instructions": min(row["logical"] for row in star_clock_rows),
# C873SRC 000797|                "maximum_logical_instructions": max(row["logical"] for row in star_clock_rows),
# C873SRC 000798|                "minimum_routed_gates": min(row["routed"] for row in star_clock_rows),
# C873SRC 000799|                "maximum_routed_gates": max(row["routed"] for row in star_clock_rows),
# C873SRC 000800|                "maximum_route_distance": max(row["maximum_distance"] for row in star_clock_rows),
# C873SRC 000801|                "route_or_alpha_census_failures": sum(
# C873SRC 000802|                    row["route_failures"] + row["alpha_route_mismatch"]
# C873SRC 000803|                    for row in star_clock_rows
# C873SRC 000804|                ),
# C873SRC 000805|                "maximum_link_clock_phase_gates": max(
# C873SRC 000806|                    row["link_clock_phase_gates"] for row in star_clock_rows
# C873SRC 000807|                ),
# C873SRC 000808|                "matter_axis_RZ_gates_per_star": tuple(sorted(set(
# C873SRC 000809|                    row["matter_axis_RZ_gates"] for row in star_clock_rows
# C873SRC 000810|                ))),
# C873SRC 000811|                "formal_zero_site_scalar_angle": 6 * math.pi / F17,
# C873SRC 000812|                "all_star_clock_words_sha256": star_clock_hash.hexdigest(),
# C873SRC 000813|            },
# C873SRC 000814|        },
# C873SRC 000815|        "plaquette_shift": {
# C873SRC 000816|            "logical_link_support": 4,
# C873SRC 000817|            "physical_support_M2": 68,
# C873SRC 000818|            "physical_SWAP_gates": 64,
# C873SRC 000819|            "parallel_depth": 16,
# C873SRC 000820|            "clean_ancilla_M2": 0,
# C873SRC 000821|            "maximum_Linf_radius": max(row["Linf_radius"] for row in plaquette_supports),
# C873SRC 000822|            "maximum_L1_radius": max(row["L1_radius"] for row in plaquette_supports),
# C873SRC 000823|            "maximum_L1_diameter": max(row["L1_diameter"] for row in plaquette_supports),
# C873SRC 000824|            "word_or_NN_failures": word_failures,
# C873SRC 000825|            "parallel_layer_site_collisions": layer_collisions,
# C873SRC 000826|            "individual_SWAP_deletions_tested": 64 * len(faces),
# C873SRC 000827|            "undetected_individual_SWAP_deletions": deletion_undetected,
# C873SRC 000828|            "all_plaquette_words_sha256": word_hash.hexdigest(),
# C873SRC 000829|        },
# C873SRC 000830|        "bank_pair_overlap_sites": pair_overlap_sites,
# C873SRC 000831|        "bank_carrier_aux_collision_sites": bank_carrier_aux_collisions,
# C873SRC 000832|        "star_plaquette_commutator_exponent_nonzero_entries": boundary_squared_failures,
# C873SRC 000833|        "constraint_commutation": {
# C873SRC 000834|            "one_hot_with_star_reason":
# C873SRC 000835|                "the one-hot projector and star clock are diagonal in link occupation",
# C873SRC 000836|            "one_hot_with_plaquette_reason":
# C873SRC 000837|                "the executed cyclic-shift word preserves every rail Hamming sector",
# C873SRC 000838|            "star_with_star_reason": "all star clocks are diagonal",
# C873SRC 000839|            "plaquette_with_plaquette_reason":
# C873SRC 000840|                "all plaquette generators are products of commuting link translations",
# C873SRC 000841|            "star_with_plaquette_failures": boundary_squared_failures,
# C873SRC 000842|        },
# C873SRC 000843|    }, (vertices, edges, faces)
# C873SRC 000844|
# C873SRC 000845|
# C873SRC 000846|def collect_failures(report):
# C873SRC 000847|    failures = []
# C873SRC 000848|    if not report["provenance"]["expected_base_is_ancestor_of_head"]:
# C873SRC 000849|        failures.append("expected base is not an ancestor of HEAD")
# C873SRC 000850|    if report["provenance"]["integration_runner_sha256"] != EXPECTED_INTEGRATION_SHA256:
# C873SRC 000851|        failures.append("integration runner hash")
# C873SRC 000852|    unary = report["one_hot_algebra"]
# C873SRC 000853|    for key in (
# C873SRC 000854|        "one_hot_mapping_failures", "all_sector_Hamming_weight_failures",
# C873SRC 000855|        "all_sector_inverse_failures", "P1_commutator_failures",
# C873SRC 000856|    ):
# C873SRC 000857|        if unary[key]:
# C873SRC 000858|            failures.append(f"one-hot:{key}")
# C873SRC 000859|    clock = report["clock_primitive"]
# C873SRC 000860|    for key in ("matter_clock_phase_residual", "link_clock_phase_residual"):
# C873SRC 000861|        if clock[key] > TOL:
# C873SRC 000862|            failures.append(f"clock:{key}")
# C873SRC 000863|    single = report["single_plaquette_uniform"]
# C873SRC 000864|    for key in (
# C873SRC 000865|        "uniform_normalization_residual", "uniform_shift_residual",
# C873SRC 000866|        "nontrivial_power_identity_failures",
# C873SRC 000867|    ):
# C873SRC 000868|        if single[key] > TOL:
# C873SRC 000869|            failures.append(f"single plaquette:{key}")
# C873SRC 000870|    if single["uniform_plus_one_sector_dimension"] != 1:
# C873SRC 000871|        failures.append("single plaquette uniqueness")
# C873SRC 000872|    if abs(single["uniform_shift_overlap"][0] - 1.0) > TOL or abs(
# C873SRC 000873|        single["uniform_shift_overlap"][1]
# C873SRC 000874|    ) > TOL:
# C873SRC 000875|        failures.append("single plaquette uniform overlap")
# C873SRC 000876|    if any(abs(value) > TOL for value in single["basis_link_shift_overlap"]):
# C873SRC 000877|        failures.append("single plaquette basis overlap control")
# C873SRC 000878|    for fixture in report["fixtures"]:
# C873SRC 000879|        prefix = str(tuple(fixture["shape"]))
# C873SRC 000880|        for key in (
# C873SRC 000881|            "boundary_of_boundary_nonzero_entries", "bank_pair_overlap_sites",
# C873SRC 000882|            "bank_carrier_aux_collision_sites",
# C873SRC 000883|            "star_plaquette_commutator_exponent_nonzero_entries",
# C873SRC 000884|        ):
# C873SRC 000885|            if fixture[key]:
# C873SRC 000886|                failures.append(f"{prefix}:{key}")
# C873SRC 000887|        if fixture["incidence_rank_mod17"] != fixture["expected_connected_incidence_rank"]:
# C873SRC 000888|            failures.append(f"{prefix}:incidence rank")
# C873SRC 000889|        if fixture["plaquette_boundary_rank_mod17"] != fixture["cycle_space_rank"]:
# C873SRC 000890|            failures.append(f"{prefix}:plaquette span")
# C873SRC 000891|        if fixture["uniform_cycle_plus_one_sector_dimension"] != 1:
# C873SRC 000892|            failures.append(f"{prefix}:uniform uniqueness")
# C873SRC 000893|        for section, keys in {
# C873SRC 000894|            "one_hot_constraint": ("radius_failures", "rail_path_NN_failures"),
# C873SRC 000895|            "star_constraint": ("encoded_matter_constraint_anticommutators",),
# C873SRC 000896|            "plaquette_shift": (
# C873SRC 000897|                "word_or_NN_failures", "parallel_layer_site_collisions",
# C873SRC 000898|                "undetected_individual_SWAP_deletions",
# C873SRC 000899|            ),
# C873SRC 000900|        }.items():
# C873SRC 000901|            for key in keys:
# C873SRC 000902|                if fixture[section][key]:
# C873SRC 000903|                    failures.append(f"{prefix}:{section}:{key}")
# C873SRC 000904|        if fixture["star_constraint"]["emitted_star_clock_word"][
# C873SRC 000905|            "route_or_alpha_census_failures"
# C873SRC 000906|        ]:
# C873SRC 000907|            failures.append(f"{prefix}:star clock route")
# C873SRC 000908|    frame = report["proper_frame_transport"]
# C873SRC 000909|    for key in (
# C873SRC 000910|        "boundary_equivariance_failures", "edge_orientation_label_failures",
# C873SRC 000911|        "edge_product_failures", "plaquette_product_failures", "label_product_failures",
# C873SRC 000912|        "physical_NN_gate_frame_failures", "physical_gate_product_failures",
# C873SRC 000913|        "physical_star_support_frame_failures",
# C873SRC 000914|        "physical_star_support_product_failures",
# C873SRC 000915|    ):
# C873SRC 000916|        if frame[key]:
# C873SRC 000917|            failures.append(f"frame:{key}")
# C873SRC 000918|    preserve = report["Object_A_preservation"]
# C873SRC 000919|    for key in (
# C873SRC 000920|        "seam_star_preservation_failures", "seam_one_hot_label_failures",
# C873SRC 000921|        "seam_plaquette_translation_commutator_failures",
# C873SRC 000922|        "all_seam_all_plaquette_commutator_failures",
# C873SRC 000923|        "onsite_stage_preservation_failures",
# C873SRC 000924|        "full_augmented_epoch_constraint_preservation_failures",
# C873SRC 000925|    ):
# C873SRC 000926|        if preserve[key]:
# C873SRC 000927|            failures.append(f"Object A:{key}")
# C873SRC 000928|    return failures
# C873SRC 000929|
# C873SRC 000930|
# C873SRC 000931|def json_safe(value):
# C873SRC 000932|    if isinstance(value, dict):
# C873SRC 000933|        return {
# C873SRC 000934|            key if isinstance(key, str | int | float | bool) or key is None else repr(key):
# C873SRC 000935|            json_safe(item)
# C873SRC 000936|            for key, item in value.items()
# C873SRC 000937|        }
# C873SRC 000938|    if isinstance(value, tuple | list | set | frozenset):
# C873SRC 000939|        return [json_safe(item) for item in value]
# C873SRC 000940|    if isinstance(value, np.generic):
# C873SRC 000941|        return value.item()
# C873SRC 000942|    return value
# C873SRC 000943|
# C873SRC 000944|
# C873SRC 000945|def main(output: Path = OUT) -> int:
# C873SRC 000946|    base_is_ancestor = subprocess.run(
# C873SRC 000947|        (
# C873SRC 000948|            "git", "merge-base", "--is-ancestor",
# C873SRC 000949|            EXPECTED_BASE_COMMIT, "HEAD",
# C873SRC 000950|        ),
# C873SRC 000951|        cwd=ROOT,
# C873SRC 000952|        check=False,
# C873SRC 000953|    ).returncode == 0
# C873SRC 000954|    fixture_rows = []
# C873SRC 000955|    transports = []
# C873SRC 000956|    for shape in SHAPES:
# C873SRC 000957|        fixture, transport = fixture_certificate(shape)
# C873SRC 000958|        fixture_rows.append(fixture)
# C873SRC 000959|        transports.append(transport)
# C873SRC 000960|    single_plaquette = single_plaquette_uniform_certificate()
# C873SRC 000961|    report = {
# C873SRC 000962|        "status": "pending",
# C873SRC 000963|        "name": "Cycle873 physical-M2 F17 open-box local constraints",
# C873SRC 000964|        "provenance": {
# C873SRC 000965|            "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 000966|            "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 000967|            "integration_runner": str(INTEGRATION_PATH.relative_to(ROOT)),
# C873SRC 000968|            "integration_runner_sha256": digest(INTEGRATION_PATH),
# C873SRC 000969|            "pinned_source_sha256": {
# C873SRC 000970|                path: digest(ROOT / path) for path in INT.SOURCE_PATHS
# C873SRC 000971|            },
# C873SRC 000972|        },
# C873SRC 000973|        "constraint_algebra": {
# C873SRC 000974|            "one_hot": "P1_e=sum_k |1_k><1_k|; Q_e=I-P1_e",
# C873SRC 000975|            "star": (
# C873SRC 000976|                "A_x=omega^(N_x+alpha div ell), alpha in {-1,+1}, omega=exp(2*pi*i/17), "
# C873SRC 000977|                "with a selected eigenvalue/projector per supplied consistent sector"
# C873SRC 000978|            ),
# C873SRC 000979|            "plaquette": (
# C873SRC 000980|                "S_p=product_e X_e^(boundary coefficient); S_p^17=I; "
# C873SRC 000981|                "the +1 sector is invariant under every plaquette translation"
# C873SRC 000982|            ),
# C873SRC 000983|            "commutation_reason": (
# C873SRC 000984|                "incidence times plaquette boundary is zero mod17; label translations "
# C873SRC 000985|                "are abelian and preserve every unary Hamming sector"
# C873SRC 000986|            ),
# C873SRC 000987|        },
# C873SRC 000988|        "sparse_plaquette_gate_word": {
# C873SRC 000989|            "rail_local_offsets": INT.RAIL_LOCAL_OFFSETS,
# C873SRC 000990|            "positive_link_shift_SWAP_pairs": tuple(
# C873SRC 000991|                (index, index + 1) for index in range(15, -1, -1)
# C873SRC 000992|            ),
# C873SRC 000993|            "negative_link_shift_SWAP_pairs": tuple(
# C873SRC 000994|                (index, index + 1) for index in range(16)
