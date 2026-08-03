#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 independent source, part 3/4."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py"
PART_ORDINAL = 3
PART_COUNT = 4
FIRST_SOURCE_LINE = 941
LAST_SOURCE_LINE = 1396
TOTAL_SOURCE_LINES = 1546
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "02c3f321ba5ef1dce723ed04bd83919839648fd89202f607b6cc680645a97734"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000941|        carriers_aux = set(context.sites) | set(auxiliary)
# C873SRC 000942|        rail_carrier_aux_collisions = sum(
# C873SRC 000943|            len(set(bank) & carriers_aux) for bank in rails.values()
# C873SRC 000944|        )
# C873SRC 000945|        star_support_max = 0
# C873SRC 000946|        for cell_index, cell in enumerate(graph.vertices):
# C873SRC 000947|            matter = set()
# C873SRC 000948|            for mode in range(6):
# C873SRC 000949|                matter.update(C871.z_support(
# C873SRC 000950|                    C871.physical_b(physical_graph, context, cell, mode), context
# C873SRC 000951|                ))
# C873SRC 000952|            incident = tuple(
# C873SRC 000953|                edge for edge, (tail, head, _axis) in enumerate(graph.edges)
# C873SRC 000954|                if tail == cell_index or head == cell_index
# C873SRC 000955|            )
# C873SRC 000956|            support = matter | set().union(*(set(rails[edge]) for edge in incident))
# C873SRC 000957|            star_support_max = max(star_support_max, len(support))
# C873SRC 000958|
# C873SRC 000959|        rows.append({
# C873SRC 000960|            "shape": dims,
# C873SRC 000961|            "vertices": len(graph.vertices),
# C873SRC 000962|            "oriented_links": len(graph.edges),
# C873SRC 000963|            "plaquettes": graph.faces.shape[1],
# C873SRC 000964|            "incidence_rank_mod17": incidence_rank,
# C873SRC 000965|            "cycle_space_rank": cycle_rank,
# C873SRC 000966|            "plaquette_boundary_rank_mod17": face_rank,
# C873SRC 000967|            "plaquette_dependency_count": graph.faces.shape[1] - face_rank,
# C873SRC 000968|            "boundary_of_boundary_nonzero_entries": boundary_squared,
# C873SRC 000969|            "fixed_divergence_dimension": F17 ** cycle_rank,
# C873SRC 000970|            "uniform_plus_one_dimension": F17 ** (cycle_rank - face_rank),
# C873SRC 000971|            "onehot_path_failures": onehot_path_failures,
# C873SRC 000972|            "rail_pair_overlap_sites": rail_overlap_sites,
# C873SRC 000973|            "rail_carrier_aux_collision_sites": rail_carrier_aux_collisions,
# C873SRC 000974|            "plaquette_support_M2": plaquette_support_max,
# C873SRC 000975|            "plaquette_word_or_NN_failures": plaquette_word_failures,
# C873SRC 000976|            "plaquette_layer_collisions": layer_collisions,
# C873SRC 000977|            "maximum_star_support_M2": star_support_max,
# C873SRC 000978|        })
# C873SRC 000979|    frames = C871.proper_frames()
# C873SRC 000980|    return {
# C873SRC 000981|        "fixtures": rows,
# C873SRC 000982|        "proper_frames": len(frames),
# C873SRC 000983|        "ordered_frame_products": len(frames) ** 2,
# C873SRC 000984|        "plaquette_SWAP_deletions_tested": deletion_tests,
# C873SRC 000985|        "undetected_plaquette_SWAP_deletions": deletion_undetected,
# C873SRC 000986|        "characterization_boundary": (
# C873SRC 000987|            "one-hot/star/plaquette ranks and emitted sparse shifts characterize a "
# C873SRC 000988|            "preserved code space; autonomous preparation/enforcement is not tested"
# C873SRC 000989|        ),
# C873SRC 000990|    }
# C873SRC 000991|
# C873SRC 000992|
# C873SRC 000993|def supplied_background(graph, particle_number, convention="ordered_prefix"):
# C873SRC 000994|    field = np.zeros(len(graph.vertices), dtype=np.int64)
# C873SRC 000995|    if convention == "ordered_prefix":
# C873SRC 000996|        field[:particle_number] = -1
# C873SRC 000997|    elif convention == "first_anchor":
# C873SRC 000998|        field[0] = -particle_number
# C873SRC 000999|    elif convention == "last_anchor":
# C873SRC 001000|        field[-1] = -particle_number
# C873SRC 001001|    else:
# C873SRC 001002|        raise ValueError(convention)
# C873SRC 001003|    field %= F17
# C873SRC 001004|    if int(field.sum()) % F17 != (-particle_number) % F17:
# C873SRC 001005|        raise AssertionError("background compatibility")
# C873SRC 001006|    return FixedStarBackground(
# C873SRC 001007|        convention, particle_number, tuple(map(int, field))
# C873SRC 001008|    )
# C873SRC 001009|
# C873SRC 001010|
# C873SRC 001011|def matter_q(graph, bits, background):
# C873SRC 001012|    n = np.array([(bits >> i) & 1 for i in range(len(graph.vertices))], dtype=np.int64)
# C873SRC 001013|    if int(n.sum()) != background.particle_number:
# C873SRC 001014|        raise AssertionError("fixed-number background")
# C873SRC 001015|    q = (n + np.asarray(background.field, dtype=np.int64)) % F17
# C873SRC 001016|    if int(q.sum()) % F17:
# C873SRC 001017|        raise AssertionError("nonzero total Gauss word")
# C873SRC 001018|    return q
# C873SRC 001019|
# C873SRC 001020|
# C873SRC 001021|def affine_state(graph, bits, generators, background):
# C873SRC 001022|    base = solve_mod(
# C873SRC 001023|        graph.incidence, matter_q(graph, bits, background)
# C873SRC 001024|    ); beta = generators.shape[1]
# C873SRC 001025|    amp = 1 / math.sqrt(F17 ** beta); out = {}
# C873SRC 001026|    for coeff in product(range(F17), repeat=beta):
# C873SRC 001027|        link = (base + generators @ np.asarray(coeff, dtype=np.int64)) % F17
# C873SRC 001028|        out[(bits, tuple(map(int, link)))] = amp
# C873SRC 001029|    return out
# C873SRC 001030|
# C873SRC 001031|
# C873SRC 001032|def six_mode_count_certificate():
# C873SRC 001033|    rows = incidence_failures = star_failures = range_failures = 0
# C873SRC 001034|    minus_rows = sign_failures = 0
# C873SRC 001035|    wrong_sign_controls = omitted_shift_controls = 0
# C873SRC 001036|    for a, b, spectator_u, spectator_v, ell in product(
# C873SRC 001037|        (0, 1), (0, 1), range(6), range(6), range(F17)
# C873SRC 001038|    ):
# C873SRC 001039|        rows += 1
# C873SRC 001040|        n_u, n_v = a + spectator_u, b + spectator_v
# C873SRC 001041|        out_u, out_v = n_u - a + b, n_v - b + a
# C873SRC 001042|        current = a - b
# C873SRC 001043|        out_ell = (ell + current) % F17
# C873SRC 001044|        incidence_failures += (
# C873SRC 001045|            ((-current) % F17, current % F17)
# C873SRC 001046|            != ((out_u - n_u) % F17, (out_v - n_v) % F17)
# C873SRC 001047|        )
# C873SRC 001048|        before_g = ((-ell - n_u) % F17, (ell - n_v) % F17)
# C873SRC 001049|        after_g = (
# C873SRC 001050|            (-out_ell - out_u) % F17,
# C873SRC 001051|            (out_ell - out_v) % F17,
# C873SRC 001052|        )
# C873SRC 001053|        star_failures += before_g != after_g
# C873SRC 001054|        range_failures += not all(
# C873SRC 001055|            0 <= value <= 6 for value in (n_u, n_v, out_u, out_v)
# C873SRC 001056|        )
# C873SRC 001057|        sign = -1 if (a, b) == (1, 1) else 1
# C873SRC 001058|        minus_rows += sign == -1
# C873SRC 001059|        sign_failures += sign != (-1 if a == b == 1 else 1)
# C873SRC 001060|        if a != b:
# C873SRC 001061|            wrong_sign_controls += (
# C873SRC 001062|                (current % F17, (-current) % F17)
# C873SRC 001063|                != ((out_u - n_u) % F17, (out_v - n_v) % F17)
# C873SRC 001064|            )
# C873SRC 001065|            omitted_shift_controls += before_g != (
# C873SRC 001066|                (-ell - out_u) % F17,
# C873SRC 001067|                (ell - out_v) % F17,
# C873SRC 001068|            )
# C873SRC 001069|    return {
# C873SRC 001070|        "rows": rows,
# C873SRC 001071|        "alpha_normalization": "+1",
# C873SRC 001072|        "FSWAP_minus_11_rows": minus_rows,
# C873SRC 001073|        "incidence_failures": incidence_failures,
# C873SRC 001074|        "fixed_background_or_star_invariance_failures": star_failures,
# C873SRC 001075|        "occupation_range_failures": range_failures,
# C873SRC 001076|        "FSWAP_sign_failures": sign_failures,
# C873SRC 001077|        "wrong_incidence_sign_detected_rows": wrong_sign_controls,
# C873SRC 001078|        "omitted_link_shift_detected_rows": omitted_shift_controls,
# C873SRC 001079|        "notation": (
# C873SRC 001080|            "a,b are selected seam bits; n_u=a+s_u and n_v=b+s_v are "
# C873SRC 001081|            "total six-mode occupations with s_u,s_v in 0..5; this is the "
# C873SRC 001082|            "alpha=+1 global affine normalization and does not instantiate an "
# C873SRC 001083|            "alpha=-1 global encoder"
# C873SRC 001084|        ),
# C873SRC 001085|    }
# C873SRC 001086|
# C873SRC 001087|
# C873SRC 001088|def augmented_edge(graph, state, edge, raw=False):
# C873SRC 001089|    u, v, _axis = graph.edges[edge]; out = {}
# C873SRC 001090|    for (bits, link_tuple), amp in state.items():
# C873SRC 001091|        a, b = (bits >> u) & 1, (bits >> v) & 1; moved = bits; phase = 1
# C873SRC 001092|        if a != b: moved ^= (1 << u) | (1 << v)
# C873SRC 001093|        if a == b == 1: phase = -1
# C873SRC 001094|        link = list(link_tuple); link[edge] = (link[edge] + a - b) % F17
# C873SRC 001095|        scalar = -1j if raw else 1
# C873SRC 001096|        key = (moved, tuple(link)); out[key] = out.get(key, 0j) + scalar * phase * amp
# C873SRC 001097|    return out
# C873SRC 001098|
# C873SRC 001099|
# C873SRC 001100|def repeated_factor_certificate():
# C873SRC 001101|    plaquette = open_box((2, 2, 1)); cube = open_box((2, 2, 2))
# C873SRC 001102|    pgen = nullspace_mod(plaquette.incidence)
# C873SRC 001103|    direct = []; raw_direct = []; background_residuals = []
# C873SRC 001104|    for bits in range(1 << len(plaquette.vertices)):
# C873SRC 001105|        backgrounds = tuple(
# C873SRC 001106|            supplied_background(plaquette, bits.bit_count(), convention)
# C873SRC 001107|            for convention in ("ordered_prefix", "first_anchor", "last_anchor")
# C873SRC 001108|        )
# C873SRC 001109|        for edge in range(len(plaquette.edges)):
# C873SRC 001110|            background = backgrounds[0]
# C873SRC 001111|            initial = affine_state(plaquette, bits, pgen, background)
# C873SRC 001112|            observed = augmented_edge(plaquette, initial, edge)
# C873SRC 001113|            u, v, _ = plaquette.edges[edge]; moved = bits
# C873SRC 001114|            if ((bits >> u) & 1) != ((bits >> v) & 1): moved ^= (1 << u) | (1 << v)
# C873SRC 001115|            phase = -1 if ((bits >> u) & 1) == ((bits >> v) & 1) == 1 else 1
# C873SRC 001116|            expected = {
# C873SRC 001117|                key: phase * amp
# C873SRC 001118|                for key, amp in affine_state(
# C873SRC 001119|                    plaquette, moved, pgen, background
# C873SRC 001120|                ).items()
# C873SRC 001121|            }
# C873SRC 001122|            direct.append(state_distance(observed, expected))
# C873SRC 001123|            raw_direct.append(state_distance(augmented_edge(plaquette, initial, edge, raw=True), expected))
# C873SRC 001124|            for variant in backgrounds:
# C873SRC 001125|                variant_initial = affine_state(plaquette, bits, pgen, variant)
# C873SRC 001126|                variant_expected = {
# C873SRC 001127|                    key: phase * amp
# C873SRC 001128|                    for key, amp in affine_state(
# C873SRC 001129|                        plaquette, moved, pgen, variant
# C873SRC 001130|                    ).items()
# C873SRC 001131|                }
# C873SRC 001132|                background_residuals.append(state_distance(
# C873SRC 001133|                    augmented_edge(plaquette, variant_initial, edge),
# C873SRC 001134|                    variant_expected,
# C873SRC 001135|                ))
# C873SRC 001136|    edge_lookup = {(plaquette.vertices[u], plaquette.vertices[v]): e for e, (u, v, _) in enumerate(plaquette.edges)}
# C873SRC 001137|    v00, v10, v01, v11 = (0,0,0), (1,0,0), (0,1,0), (1,1,0)
# C873SRC 001138|    sequence = (edge_lookup[(v00,v10)], edge_lookup[(v10,v11)], edge_lookup[(v01,v11)], edge_lookup[(v00,v01)])
# C873SRC 001139|    repeated = []; repeated_raw = []
# C873SRC 001140|    for bits in range(1 << len(plaquette.vertices)):
# C873SRC 001141|        background = supplied_background(plaquette, bits.bit_count())
# C873SRC 001142|        initial = affine_state(plaquette, bits, pgen, background); observed = initial; raw = initial; moved = bits; phase = 1
# C873SRC 001143|        for edge in sequence:
# C873SRC 001144|            u, v, _ = plaquette.edges[edge]; a, b = (moved >> u) & 1, (moved >> v) & 1
# C873SRC 001145|            if a != b: moved ^= (1 << u) | (1 << v)
# C873SRC 001146|            if a == b == 1: phase *= -1
# C873SRC 001147|            observed = augmented_edge(plaquette, observed, edge); raw = augmented_edge(plaquette, raw, edge, raw=True)
# C873SRC 001148|        expected = {
# C873SRC 001149|            key: phase * amp
# C873SRC 001150|            for key, amp in affine_state(
# C873SRC 001151|                plaquette, moved, pgen, background
# C873SRC 001152|            ).items()
# C873SRC 001153|        }
# C873SRC 001154|        repeated.append(state_distance(observed, expected)); repeated_raw.append(state_distance(raw, expected))
# C873SRC 001155|    # Exhaust the L2 local incidence law and 36-factor recurrence algebraically.
# C873SRC 001156|    direct_l2 = incidence_failures = repeat_failures = 0; raw_phase = (-1j) ** 36
# C873SRC 001157|    repeat_sequence = tuple(range(len(cube.edges))) * 3
# C873SRC 001158|    for bits in range(1 << len(cube.vertices)):
# C873SRC 001159|        background = supplied_background(cube, bits.bit_count())
# C873SRC 001160|        q0 = matter_q(cube, bits, background)
# C873SRC 001161|        for edge, (u, v, _axis) in enumerate(cube.edges):
# C873SRC 001162|            moved = bits; a, b = (bits >> u) & 1, (bits >> v) & 1
# C873SRC 001163|            if a != b: moved ^= (1 << u) | (1 << v)
# C873SRC 001164|            current = np.zeros(len(cube.edges), dtype=np.int64); current[edge] = a - b
# C873SRC 001165|            incidence_failures += not np.array_equal(cube.incidence @ current % F17, (matter_q(cube, moved, background) - q0) % F17)
# C873SRC 001166|            direct_l2 += 1
# C873SRC 001167|        moved = bits; accumulated = np.zeros(len(cube.edges), dtype=np.int64)
# C873SRC 001168|        for edge in repeat_sequence:
# C873SRC 001169|            u, v, _ = cube.edges[edge]; a, b = (moved >> u) & 1, (moved >> v) & 1
# C873SRC 001170|            if a != b: moved ^= (1 << u) | (1 << v)
# C873SRC 001171|            accumulated[edge] = (accumulated[edge] + a - b) % F17
# C873SRC 001172|        repeat_failures += not np.array_equal(cube.incidence @ accumulated % F17, (matter_q(cube, moved, background) - q0) % F17)
# C873SRC 001173|    return {
# C873SRC 001174|        "plaquette_direct_columns": len(direct), "plaquette_single_factor_corrected_max_residual": max(direct),
# C873SRC 001175|        "supplied_background_variant_columns": len(background_residuals),
# C873SRC 001176|        "supplied_background_variant_max_residual": max(background_residuals),
# C873SRC 001177|        "fixed_star_background_boundary": (
# C873SRC 001178|            "q_g(n)=n+g is checked at fixed supplied g for ordered-prefix, "
# C873SRC 001179|            "first-anchor, and last-anchor diagnostic fields; g selection/genesis "
# C873SRC 001180|            "and full affine-encoder frame/product/translation covariance remain open"
# C873SRC 001181|        ),
# C873SRC 001182|        "plaquette_single_raw_factor_residual": max(raw_direct),
# C873SRC 001183|        "plaquette_four_factor_columns": len(repeated), "plaquette_four_factor_corrected_max_residual": max(repeated),
# C873SRC 001184|        "plaquette_four_raw_factor_max_residual": max(repeated_raw), "plaquette_raw_phase": [((-1j)**4).real, ((-1j)**4).imag],
# C873SRC 001185|        "open_L2_direct_cases": direct_l2, "open_L2_incidence_failures": incidence_failures,
# C873SRC 001186|        "open_L2_repeated_factor_count": len(repeat_sequence), "open_L2_repeated_words": 1 << len(cube.vertices),
# C873SRC 001187|        "open_L2_repeated_uniform_intertwiner_failures": repeat_failures,
# C873SRC 001188|        "open_L2_raw_36_factor_phase": [raw_phase.real, raw_phase.imag],
# C873SRC 001189|        "open_L2_one_seam_stage_raw_phase": [((-1j)**len(cube.edges)).real, ((-1j)**len(cube.edges)).imag],
# C873SRC 001190|        "open_box_one_seam_stage_raw_phases": [
# C873SRC 001191|            {
# C873SRC 001192|                "shape": dims,
# C873SRC 001193|                "seams": len(open_box(dims).edges),
# C873SRC 001194|                "phase": [
# C873SRC 001195|                    ((-1j) ** len(open_box(dims).edges)).real,
# C873SRC 001196|                    ((-1j) ** len(open_box(dims).edges)).imag,
# C873SRC 001197|                ],
# C873SRC 001198|            }
# C873SRC 001199|            for dims in ((2, 2, 2), (3, 3, 3), (3, 2, 2))
# C873SRC 001200|        ],
# C873SRC 001201|        "open_L2_cycle_rank": nullspace_mod(cube.incidence).shape[1],
# C873SRC 001202|    }
# C873SRC 001203|
# C873SRC 001204|
# C873SRC 001205|def ring_affine_state(cell, mode, length=5):
# C873SRC 001206|    # q = n - delta_0; incidence is head-minus-tail on e_i:i->i+1.
# C873SRC 001207|    q = np.zeros(length, dtype=np.int64); q[cell] += 1; q[0] -= 1; q %= F17
# C873SRC 001208|    incidence = np.zeros((length, length), dtype=np.int64)
# C873SRC 001209|    for edge in range(length): incidence[edge, edge] = -1; incidence[(edge + 1) % length, edge] = 1
# C873SRC 001210|    base = solve_mod(incidence, q); amp = 1 / math.sqrt(F17)
# C873SRC 001211|    return {(cell, mode, tuple(map(int, (base + t) % F17))): amp for t in range(F17)}
# C873SRC 001212|
# C873SRC 001213|
# C873SRC 001214|def ring_coin(state, coin):
# C873SRC 001215|    out = {}
# C873SRC 001216|    for (cell, mode, links), amp in state.items():
# C873SRC 001217|        for target in range(6):
# C873SRC 001218|            value = coin[target, mode]
# C873SRC 001219|            if abs(value): out[(cell, target, links)] = out.get((cell, target, links), 0j) + value * amp
# C873SRC 001220|    return out
# C873SRC 001221|
# C873SRC 001222|
# C873SRC 001223|def ring_reverse(state):
# C873SRC 001224|    reverse = (1, 0, 3, 2, 5, 4)
# C873SRC 001225|    return {(cell, reverse[mode], links): amp for (cell, mode, links), amp in state.items()}
# C873SRC 001226|
# C873SRC 001227|
# C873SRC 001228|def ring_seams(state, length=5):
# C873SRC 001229|    # x seams are the actual Cycle870 left-mode 1 / right-mode 0 factors.
# C873SRC 001230|    # The unit-period y/z quotient supplies their p_y=p_z=0 partner swaps.
# C873SRC 001231|    out = {}
# C873SRC 001232|    for (cell, mode, links_tuple), amp in state.items():
# C873SRC 001233|        links = list(links_tuple)
# C873SRC 001234|        if mode == 1:  # left endpoint on edge cell, moves to its head as mode 0
# C873SRC 001235|            links[cell] = (links[cell] + 1) % F17; target = ((cell + 1) % length, 0)
# C873SRC 001236|        elif mode == 0:  # right endpoint of edge cell-1, moves to its tail as mode 1
# C873SRC 001237|            edge = (cell - 1) % length; links[edge] = (links[edge] - 1) % F17; target = (edge, 1)
# C873SRC 001238|        elif mode in (2, 3, 4, 5):
# C873SRC 001239|            target = (cell, mode ^ 1)  # cancels the onsite reverse at p_y=p_z=0
# C873SRC 001240|        key = (*target, tuple(links)); out[key] = out.get(key, 0j) + amp
# C873SRC 001241|    return out
# C873SRC 001242|
# C873SRC 001243|
# C873SRC 001244|def inner(left, right):
# C873SRC 001245|    return sum(np.conj(value) * right.get(key, 0j) for key, value in left.items())
# C873SRC 001246|
# C873SRC 001247|
# C873SRC 001248|def independent_fock_lift(one_particle):
# C873SRC 001249|    """Independent exterior-power lift on all 64 six-mode words."""
# C873SRC 001250|    one_particle = np.asarray(one_particle, dtype=complex)
# C873SRC 001251|    occupied = tuple(
# C873SRC 001252|        tuple(mode for mode in range(6) if bits >> mode & 1)
# C873SRC 001253|        for bits in range(64)
# C873SRC 001254|    )
# C873SRC 001255|    output = np.zeros((64, 64), dtype=complex)
# C873SRC 001256|    for source, source_modes in enumerate(occupied):
# C873SRC 001257|        for target, target_modes in enumerate(occupied):
# C873SRC 001258|            if len(source_modes) != len(target_modes):
# C873SRC 001259|                continue
# C873SRC 001260|            output[target, source] = (
# C873SRC 001261|                1.0 if not source_modes else np.linalg.det(
# C873SRC 001262|                    one_particle[np.ix_(target_modes, source_modes)]
# C873SRC 001263|                )
# C873SRC 001264|            )
# C873SRC 001265|    return output
# C873SRC 001266|
# C873SRC 001267|
# C873SRC 001268|def independent_onsite_star_preservation(coin, reverse_matrix, coupling):
# C873SRC 001269|    """Check the onsite targets against the order-17 matter clock.
# C873SRC 001270|
# C873SRC 001271|    This is deliberately separate from the Cycle873 local-constraint core.
# C873SRC 001272|    The pinned Cycle870 checker supplies the physical-word/target bridge; this
# C873SRC 001273|    routine exhausts the additional target/star-clock obligation.
# C873SRC 001274|    """
# C873SRC 001275|    occupations = np.asarray([bits.bit_count() for bits in range(64)])
# C873SRC 001276|    clock = np.diag(np.exp(2j * math.pi * occupations / F17))
# C873SRC 001277|    contact_diagonal = np.exp(
# C873SRC 001278|        1j * coupling * occupations * (occupations - 1) / 2
# C873SRC 001279|    )
# C873SRC 001280|    targets = {
# C873SRC 001281|        "coin": independent_fock_lift(coin),
# C873SRC 001282|        "reverse": independent_fock_lift(reverse_matrix),
# C873SRC 001283|        "contact": np.diag(contact_diagonal).astype(complex),
# C873SRC 001284|    }
# C873SRC 001285|    targets["composed_onsite_epoch"] = (
# C873SRC 001286|        targets["contact"] @ targets["reverse"] @ targets["coin"]
# C873SRC 001287|    )
# C873SRC 001288|    commutators = {
# C873SRC 001289|        name: clean_float(float(np.linalg.norm(matrix @ clock - clock @ matrix)))
# C873SRC 001290|        for name, matrix in targets.items()
# C873SRC 001291|    }
# C873SRC 001292|    unitarity = {
# C873SRC 001293|        name: clean_float(float(np.linalg.norm(
# C873SRC 001294|            matrix.conj().T @ matrix - np.eye(64)
# C873SRC 001295|        )))
# C873SRC 001296|        for name, matrix in targets.items()
# C873SRC 001297|    }
# C873SRC 001298|    hostile = np.zeros((64, 64), dtype=complex)
# C873SRC 001299|    for bits in range(64):
# C873SRC 001300|        hostile[bits ^ 1, bits] = 1.0
# C873SRC 001301|    hostile_commutator = float(np.linalg.norm(hostile @ clock - clock @ hostile))
# C873SRC 001302|    return {
# C873SRC 001303|        "basis_occupation_columns": 64,
# C873SRC 001304|        "star_clock_commutator_residuals": commutators,
# C873SRC 001305|        "unitarity_residuals": unitarity,
# C873SRC 001306|        "bare_occupation_flip_control_commutator": hostile_commutator,
# C873SRC 001307|        "contact_one_particle_target_residual": clean_float(max(
# C873SRC 001308|            abs(contact_diagonal[bits] - 1.0)
# C873SRC 001309|            for bits in range(64) if bits.bit_count() == 1
# C873SRC 001310|        )),
# C873SRC 001311|        "physical_target_bridge": (
# C873SRC 001312|            "pinned Cycle870 emitted-word intertwiners plus this independent "
# C873SRC 001313|            "64-column target/star-clock check"
# C873SRC 001314|        ),
# C873SRC 001315|    }
# C873SRC 001316|
# C873SRC 001317|
# C873SRC 001318|def recurrence_dispersion_certificate(C870, C871, C219, C210):
# C873SRC 001319|    species = C219.common_species(float(C870.c230.BETA)); coin = np.asarray(species.coin, dtype=complex)
# C873SRC 001320|    gates = C871.coin_schedule(); reconstructed = np.eye(6, dtype=complex)
# C873SRC 001321|    for gate in gates:
# C873SRC 001322|        embedded = np.eye(6, dtype=complex)
# C873SRC 001323|        embedded[np.ix_(gate.modes, gate.modes)] = gate.matrix
# C873SRC 001324|        reconstructed = embedded @ reconstructed
# C873SRC 001325|    reverse_matrix = np.eye(6, dtype=complex)
# C873SRC 001326|    for left, right in ((0, 1), (2, 3), (4, 5)):
# C873SRC 001327|        helper = C870.reverse_helper(left, right)
# C873SRC 001328|        for a, b in ((left, helper), (right, helper), (left, helper)):
# C873SRC 001329|            swap = np.eye(6, dtype=complex); swap[a, a] = swap[b, b] = 0; swap[a, b] = swap[b, a] = 1
# C873SRC 001330|            reverse_matrix = swap @ reverse_matrix
# C873SRC 001331|    l2graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
# C873SRC 001332|    l2rotations, phase_inventory = C870.build_update(l2graph, gates)
# C873SRC 001333|    factor_stage_order = tuple(dict.fromkeys(row.factor[0] for row in l2rotations))
# C873SRC 001334|    length = 5; encoded = [ring_affine_state(cell, mode, length) for cell in range(length) for mode in range(6)]
# C873SRC 001335|    observed_columns = []
# C873SRC 001336|    for source in encoded:
# C873SRC 001337|        observed_columns.append(ring_seams(ring_reverse(ring_coin(source, coin)), length))
# C873SRC 001338|    compressed = np.asarray([[inner(encoded[row], observed_columns[col]) for col in range(6*length)] for row in range(6*length)])
# C873SRC 001339|    # Direct periodic one-particle target: stream after the actual Cycle219 coin.
# C873SRC 001340|    native = np.zeros_like(compressed)
# C873SRC 001341|    directions = np.asarray(C210.DIRECTIONS)
# C873SRC 001342|    for cell in range(length):
# C873SRC 001343|        for source_mode in range(6):
# C873SRC 001344|            for target_mode in range(6):
# C873SRC 001345|                target_cell = (cell + int(directions[target_mode, 0])) % length
# C873SRC 001346|                native[target_cell * 6 + target_mode, cell * 6 + source_mode] += coin[target_mode, source_mode]
# C873SRC 001347|    intertwiner_residuals = []
# C873SRC 001348|    for col in range(6*length):
# C873SRC 001349|        expected = {}
# C873SRC 001350|        for row in range(6*length):
# C873SRC 001351|            coefficient = native[row, col]
# C873SRC 001352|            if abs(coefficient):
# C873SRC 001353|                for key, value in encoded[row].items(): expected[key] = expected.get(key, 0j) + coefficient * value
# C873SRC 001354|        intertwiner_residuals.append(state_distance(observed_columns[col], expected))
# C873SRC 001355|    fourier_residuals = []; block_unitarity = []
# C873SRC 001356|    for n in range(length):
# C873SRC 001357|        momentum = 2 * math.pi * n / length
# C873SRC 001358|        F = np.zeros((6*length, 6), dtype=complex)
# C873SRC 001359|        for cell in range(length):
# C873SRC 001360|            for mode in range(6): F[cell*6+mode, mode] = np.exp(1j * momentum * cell) / math.sqrt(length)
# C873SRC 001361|        block = F.conj().T @ compressed @ F
# C873SRC 001362|        bloch = np.diag(np.exp(-1j * (C210.DIRECTIONS @ np.array((momentum,0.0,0.0))))) @ coin
# C873SRC 001363|        fourier_residuals.append(float(np.linalg.norm(block - bloch)))
# C873SRC 001364|        block_unitarity.append(float(np.linalg.norm(block.conj().T @ block - np.eye(6))))
# C873SRC 001365|
# C873SRC 001366|    def branch_phase(momentum):
# C873SRC 001367|        bloch = np.diag(np.exp(-1j * (C210.DIRECTIONS @ np.asarray(momentum)))) @ coin
# C873SRC 001368|        values, vectors = np.linalg.eig(bloch); overlaps = np.abs(vectors.conj().T @ C210.UNIFORM)
# C873SRC 001369|        return float(np.angle(values[int(np.argmax(overlaps))]))
# C873SRC 001370|    step = 1e-4; rest_phase = branch_phase(np.zeros(3)); curvature = np.zeros((3,3))
# C873SRC 001371|    for i in range(3):
# C873SRC 001372|        d = np.zeros(3); d[i] = step
# C873SRC 001373|        curvature[i,i] = (branch_phase(d) - 2*rest_phase + branch_phase(-d)) / step**2
# C873SRC 001374|        for j in range(i):
# C873SRC 001375|            pp=np.zeros(3); pm=np.zeros(3); mp=np.zeros(3); mm=np.zeros(3)
# C873SRC 001376|            pp[i]=pp[j]=step; pm[i]=step; pm[j]=-step; mp[i]=-step; mp[j]=step; mm[i]=mm[j]=-step
# C873SRC 001377|            curvature[i,j]=curvature[j,i]=(branch_phase(pp)-branch_phase(pm)-branch_phase(mp)+branch_phase(mm))/(4*step**2)
# C873SRC 001378|    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
# C873SRC 001379|    contact = C870.contact_semantics()
# C873SRC 001380|    onsite_star = independent_onsite_star_preservation(
# C873SRC 001381|        coin, reverse_matrix, float(C870.c230.COUPLING)
# C873SRC 001382|    )
# C873SRC 001383|    eight_step_encoded_native_residual = float(np.linalg.norm(
# C873SRC 001384|        np.linalg.matrix_power(compressed, 8)
# C873SRC 001385|        - np.linalg.matrix_power(native, 8)
# C873SRC 001386|    ))
# C873SRC 001387|    return {
# C873SRC 001388|        "beta": float(C870.c230.BETA), "coin_schedule_gates": len(gates),
# C873SRC 001389|        "coin_schedule_reconstruction_residual": float(np.linalg.norm(reconstructed - coin)),
# C873SRC 001390|        "C870_factor_stage_order": factor_stage_order,
# C873SRC 001391|        "onsite_reverse_helper_permutation_residual": float(np.linalg.norm(reverse_matrix - C210.REVERSE)),
# C873SRC 001392|        "L2_compiled_relative_to_target_phase_angle": phase_inventory["compiled_relative_to_target_global_phase_angle"],
# C873SRC 001393|        "L2_formal_global_correction_angle": phase_inventory["exact_target_global_phase_correction_angle"],
# C873SRC 001394|        "ring_length": length, "encoded_joint_columns": len(encoded), "F17_terms_per_encoded_column": F17,
# C873SRC 001395|        "coin_reverse_seam_contact_intertwiner_max_residual": clean_float(max(intertwiner_residuals)),
# C873SRC 001396|        "compressed_native_matrix_residual": float(np.linalg.norm(compressed - native)),
