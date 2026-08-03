#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 all seam physical source, part 2/5."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 5
FIRST_SOURCE_LINE = 564
LAST_SOURCE_LINE = 1047
TOTAL_SOURCE_LINES = 2038
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000564|            after_g = (
# C873SRC 000565|                (after_a + family_sign * after_label) % F17,
# C873SRC 000566|                (after_b - family_sign * after_label) % F17,
# C873SRC 000567|            )
# C873SRC 000568|            gauss += before_g != after_g
# C873SRC 000569|            source = next(iter(initial))
# C873SRC 000570|            coherent[source] = 1.0 / normalization
# C873SRC 000571|            target, amplitude = next(iter(expected.items()))
# C873SRC 000572|            coherent_expected[target] = coherent_expected.get(target, 0.0j) + amplitude / normalization
# C873SRC 000573|    coherent_observed = execute_semantic(coherent, rows)
# C873SRC 000574|    return {
# C873SRC 000575|        "alpha": alpha,
# C873SRC 000576|        "typed_family": "G=n+div(ell)" if alpha == 1 else "G=n-div(ell)",
# C873SRC 000577|        "lawful_columns": 4 * F17,
# C873SRC 000578|        "basis_failures": failures,
# C873SRC 000579|        "scratch_cleanup_failures": scratch,
# C873SRC 000580|        "pointer_failures": pointer_failures,
# C873SRC 000581|        "pointer_boundary": "F17-only macro leaves the non-bank pointer spectator unchanged",
# C873SRC 000582|        "typed_G_failures": gauss,
# C873SRC 000583|        "distinct_output_columns": len(outputs),
# C873SRC 000584|        "coherent_forward_residual_with_formal_seam_scalar": state_distance(
# C873SRC 000585|            coherent_observed, coherent_expected
# C873SRC 000586|        ),
# C873SRC 000587|        "coherent_inverse_residual": state_distance(
# C873SRC 000588|            execute_semantic(coherent_observed, inverse), coherent
# C873SRC 000589|        ),
# C873SRC 000590|        "raw_compiled_seam_global_phase": [0.0, -1.0],
# C873SRC 000591|        "raw_normalized_state_residual_to_exact_target": math.sqrt(2.0),
# C873SRC 000592|        "formal_zero_site_seam_correction_angle": math.pi / 2,
# C873SRC 000593|    }
# C873SRC 000594|
# C873SRC 000595|
# C873SRC 000596|def semantic_mutation_certificate():
# C873SRC 000597|    labels = (
# C873SRC 000598|        "delete_plus_shift", "delete_minus_shift", "delete_cleanup", "delete_seam",
# C873SRC 000599|    )
# C873SRC 000600|    output = {}
# C873SRC 000601|    for mutation in labels:
# C873SRC 000602|        changed = dirty = 0
# C873SRC 000603|        for a, b in product((0, 1), repeat=2):
# C873SRC 000604|            for label in range(F17):
# C873SRC 000605|                initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
# C873SRC 000606|                expected = semantic_target(a, b, label, 1)
# C873SRC 000607|                observed = execute_semantic(
# C873SRC 000608|                    initial,
# C873SRC 000609|                    semantic_operations(1, mutation, include_pointer=False),
# C873SRC 000610|                )
# C873SRC 000611|                changed += state_distance(observed, expected) > TOL
# C873SRC 000612|                dirty += any(
# C873SRC 000613|                    any(key[index] for index in (2, 3, 4))
# C873SRC 000614|                    for key in observed
# C873SRC 000615|                )
# C873SRC 000616|        output[mutation] = {"changed_columns": changed, "dirty_columns": dirty}
# C873SRC 000617|    return {
# C873SRC 000618|        "component_mutations": output,
# C873SRC 000619|        "inactive_component_mutations": tuple(
# C873SRC 000620|            label for label, row in output.items()
# C873SRC 000621|            if not row["changed_columns"] and not row["dirty_columns"]
# C873SRC 000622|        ),
# C873SRC 000623|    }
# C873SRC 000624|
# C873SRC 000625|
# C873SRC 000626|def persistent_recurrence_certificate():
# C873SRC 000627|    rows = tuple(
# C873SRC 000628|        row for row in semantic_operations(1, include_pointer=False)
# C873SRC 000629|    )
# C873SRC 000630|    two_epoch_failures = two_epoch_work_failures = 0
# C873SRC 000631|    coexistence_reuse_pointer_failures = 0
# C873SRC 000632|    multi_epoch_failures = 0
# C873SRC 000633|    for a, b in product((0, 1), repeat=2):
# C873SRC 000634|        for label in range(F17):
# C873SRC 000635|            initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
# C873SRC 000636|            once = execute_semantic(initial, rows)
# C873SRC 000637|            twice = execute_semantic(once, rows)
# C873SRC 000638|            two_epoch_failures += state_distance(twice, initial) > TOL
# C873SRC 000639|            two_epoch_work_failures += any(
# C873SRC 000640|                any(key[index] for index in (2, 3, 4)) for key in twice
# C873SRC 000641|            )
# C873SRC 000642|            current = initial
# C873SRC 000643|            ca, cb, current_label = a, b, label
# C873SRC 000644|            for epoch in range(1, 9):
# C873SRC 000645|                current = execute_semantic(current, rows)
# C873SRC 000646|                current_label = (current_label + (ca - cb)) % F17
# C873SRC 000647|                ca, cb = cb, ca
# C873SRC 000648|                expected = semantic_target(a, b, label, 1) if epoch == 1 else {
# C873SRC 000649|                    (ca, cb, 0, 0, 0, current_label, 0):
# C873SRC 000650|                    (-1.0 if (a == b == 1 and epoch & 1) else 1.0) + 0.0j
# C873SRC 000651|                }
# C873SRC 000652|                # For double occupancy the CAR sign alternates each FSWAP.
# C873SRC 000653|                if epoch == 1:
# C873SRC 000654|                    expected = {
# C873SRC 000655|                        (ca, cb, 0, 0, 0, current_label, 0):
# C873SRC 000656|                        (-1.0 if a == b == 1 else 1.0) + 0.0j
# C873SRC 000657|                    }
# C873SRC 000658|                multi_epoch_failures += state_distance(current, expected) > TOL
# C873SRC 000659|
# C873SRC 000660|            # The coexistence word retains p in the packet pointer.  Reusing the
# C873SRC 000661|            # same packet without blanking makes the second XOR erase p.
# C873SRC 000662|            full_once = execute_semantic(
# C873SRC 000663|                initial, semantic_operations(1, include_pointer=True)
# C873SRC 000664|            )
# C873SRC 000665|            full_twice = execute_semantic(
# C873SRC 000666|                full_once, semantic_operations(1, include_pointer=True)
# C873SRC 000667|            )
# C873SRC 000668|            if a ^ b:
# C873SRC 000669|                coexistence_reuse_pointer_failures += all(key[6] == 0 for key in full_twice)
# C873SRC 000670|    return {
# C873SRC 000671|        "F17_only_two_epoch_columns": 4 * F17,
# C873SRC 000672|        "F17_only_two_epoch_failures": two_epoch_failures,
# C873SRC 000673|        "F17_only_two_epoch_work_cleanup_failures": two_epoch_work_failures,
# C873SRC 000674|        "F17_only_eight_epoch_rows": 8 * 4 * F17,
# C873SRC 000675|        "F17_only_eight_epoch_failures": multi_epoch_failures,
# C873SRC 000676|        "coexistence_second_epoch_without_packet_blank_detected_columns":
# C873SRC 000677|            coexistence_reuse_pointer_failures,
# C873SRC 000678|        "object_A_boundary": (
# C873SRC 000679|            "persistent F17 rails; q_u/q_v/current return clean; no Cycle714/612 packet output"
# C873SRC 000680|        ),
# C873SRC 000681|        "object_B_boundary": (
# C873SRC 000682|            "unchanged Cycle714 packet retained; a fresh blank packet/reset remains supplied "
# C873SRC 000683|            "for every invocation"
# C873SRC 000684|        ),
# C873SRC 000685|    }
# C873SRC 000686|
# C873SRC 000687|
# C873SRC 000688|def packet_join_certificate():
# C873SRC 000689|    cases = failures = inverse_failures = work_failures = pointer_failures = 0
# C873SRC 000690|    # Seven supplied-control patterns: all admitted plus each non-pointer control
# C873SRC 000691|    # individually disabled.  Pointer itself is exhaustively supplied by a,b.
# C873SRC 000692|    other_controls = ((1, 1, 1, 1, 1),) + tuple(
# C873SRC 000693|        tuple(0 if index == omitted else 1 for index in range(5))
# C873SRC 000694|        for omitted in range(5)
# C873SRC 000695|    )
# C873SRC 000696|    for a, b in product((0, 1), repeat=2):
# C873SRC 000697|        pointer = a ^ b
# C873SRC 000698|        for rotor in range(16):
# C873SRC 000699|            for head in range(64):
# C873SRC 000700|                for orientation in (0, 1):
# C873SRC 000701|                    for rest in other_controls:
# C873SRC 000702|                        before = C714.initial(
# C873SRC 000703|                            rotor, head, orientation, (pointer, *rest)
# C873SRC 000704|                        )
# C873SRC 000705|                        observed = C714.apply_semantic(before, C714.word())
# C873SRC 000706|                        expected = C714.independent_expected(before)
# C873SRC 000707|                        cases += 1
# C873SRC 000708|                        failures += observed != expected
# C873SRC 000709|                        work_failures += any(
# C873SRC 000710|                            observed[index]
# C873SRC 000711|                            for index in C714.ENABLE_WORK + C714.MCX_WORK
# C873SRC 000712|                        )
# C873SRC 000713|                        pointer_failures += observed[C714.POINTER] != pointer
# C873SRC 000714|                        restored = C714.apply_semantic(
# C873SRC 000715|                            observed, tuple(reversed(C714.word()))
# C873SRC 000716|                        )
# C873SRC 000717|                        inverse_failures += restored != before
# C873SRC 000718|    return {
# C873SRC 000719|        "blank_packet_join_cases": cases,
# C873SRC 000720|        "independent_packet_failures": failures,
# C873SRC 000721|        "packet_inverse_failures": inverse_failures,
# C873SRC 000722|        "packet_work_cleanup_failures": work_failures,
# C873SRC 000723|        "retained_pointer_failures": pointer_failures,
# C873SRC 000724|        "shared_roles": {
# C873SRC 000725|            "F17_q_u": C714.MCX_WORK[0],
# C873SRC 000726|            "F17_q_v": C714.MCX_WORK[1],
# C873SRC 000727|            "F17_serial_current": C714.MCX_WORK[2],
# C873SRC 000728|            "retained_pointer": C714.POINTER,
# C873SRC 000729|        },
# C873SRC 000730|        "expanded_packet_instructions": len(C714.expanded(C714.word())),
# C873SRC 000731|        "Toffoli_primitive_residual": C714.toffoli_residual(),
# C873SRC 000732|    }
# C873SRC 000733|
# C873SRC 000734|
# C873SRC 000735|def swap_rail(mask: int, rail: int) -> int:
# C873SRC 000736|    if ((mask >> rail) & 1) != ((mask >> (rail + 1)) & 1):
# C873SRC 000737|        mask ^= (1 << rail) | (1 << (rail + 1))
# C873SRC 000738|    return mask
# C873SRC 000739|
# C873SRC 000740|
# C873SRC 000741|def apply_unary(mask: int, direction: int, deleted_edge: int | None = None):
# C873SRC 000742|    order = range(15, -1, -1) if direction > 0 else range(16)
# C873SRC 000743|    for rail in order:
# C873SRC 000744|        if rail != deleted_edge:
# C873SRC 000745|            mask = swap_rail(mask, rail)
# C873SRC 000746|    return mask
# C873SRC 000747|
# C873SRC 000748|
# C873SRC 000749|def unary_projector_certificate():
# C873SRC 000750|    mapping = inverse = weight = projector_commutator = 0
# C873SRC 000751|    unlawful_preserved = 0
# C873SRC 000752|    for direction in (-1, 1):
# C873SRC 000753|        for mask in range(1 << F17):
# C873SRC 000754|            observed = apply_unary(mask, direction)
# C873SRC 000755|            weight += observed.bit_count() != mask.bit_count()
# C873SRC 000756|            projector_commutator += (observed.bit_count() == 1) != (mask.bit_count() == 1)
# C873SRC 000757|            inverse += apply_unary(observed, -direction) != mask
# C873SRC 000758|            unlawful_preserved += mask.bit_count() != 1 and observed.bit_count() == mask.bit_count()
# C873SRC 000759|        for label in range(F17):
# C873SRC 000760|            mapping += apply_unary(1 << label, direction) != 1 << ((label + direction) % F17)
# C873SRC 000761|    edge_deletions = {}
# C873SRC 000762|    for direction in (-1, 1):
# C873SRC 000763|        for edge in range(16):
# C873SRC 000764|            edge_deletions[f"{direction:+d}:{edge}"] = sum(
# C873SRC 000765|                apply_unary(1 << label, direction, edge)
# C873SRC 000766|                != apply_unary(1 << label, direction)
# C873SRC 000767|                for label in range(F17)
# C873SRC 000768|            )
# C873SRC 000769|    unlawful = (1 << F17) - F17
# C873SRC 000770|    return {
# C873SRC 000771|        "constraint": "Q=I-P1, with P1=sum_k |1_k><1_k| on this fixed 17-M2 bank",
# C873SRC 000772|        "constraint_support_M2": F17,
# C873SRC 000773|        "projector_rank": F17,
# C873SRC 000774|        "exhaustive_masks_per_direction": 1 << F17,
# C873SRC 000775|        "one_hot_mapping_failures": mapping,
# C873SRC 000776|        "all_sector_Hamming_weight_failures": weight,
# C873SRC 000777|        "all_sector_inverse_failures": inverse,
# C873SRC 000778|        "P1_commutator_failures": projector_commutator,
# C873SRC 000779|        "unlawful_sector_rows_also_preserved_by_dynamics": unlawful_preserved,
# C873SRC 000780|        "deleted_Q_unlawful_columns_admitted": unlawful,
# C873SRC 000781|        "deleted_Q_vacuum_admitted": True,
# C873SRC 000782|        "deleted_Q_double_hot_columns_admitted": math.comb(F17, 2),
# C873SRC 000783|        "deleted_Fredkin_changed_one_hot_rows": edge_deletions,
# C873SRC 000784|        "inactive_deleted_Fredkins": tuple(
# C873SRC 000785|            label for label, count in edge_deletions.items() if count == 0
# C873SRC 000786|        ),
# C873SRC 000787|        "enforcement_boundary": (
# C873SRC 000788|            "P1/Q is an explicit bounded-bank projector, but its initialization or "
# C873SRC 000789|            "enforcement is supplied/open and contributes no gates or physical-energy claim"
# C873SRC 000790|        ),
# C873SRC 000791|    }
# C873SRC 000792|
# C873SRC 000793|
# C873SRC 000794|def computational_basis_path_history_witness():
# C873SRC 000795|    # A -> C on an elementary plaquette has two two-hop one-particle paths.
# C873SRC 000796|    # Every edge is read in its positive coordinate orientation and alpha=+1.
# C873SRC 000797|    a, b, c, d = (0, 0), (1, 0), (1, 1), (0, 1)
# C873SRC 000798|    edges = ((a, b), (b, c), (a, d), (d, c))
# C873SRC 000799|    upper = {edge: int(edge in ((a, b), (b, c))) for edge in edges}
# C873SRC 000800|    lower = {edge: int(edge in ((a, d), (d, c))) for edge in edges}
# C873SRC 000801|
# C873SRC 000802|    def divergence(labels):
# C873SRC 000803|        output = {site: 0 for site in (a, b, c, d)}
# C873SRC 000804|        for (left, right), label in labels.items():
# C873SRC 000805|            output[left] += label
# C873SRC 000806|            output[right] -= label
# C873SRC 000807|        return {site: value % F17 for site, value in output.items()}
# C873SRC 000808|
# C873SRC 000809|    upper_div, lower_div = divergence(upper), divergence(lower)
# C873SRC 000810|    initial_n = {a: 1, b: 0, c: 0, d: 0}
# C873SRC 000811|    final_n = {a: 0, b: 0, c: 1, d: 0}
# C873SRC 000812|    initial_div = {site: 0 for site in initial_n}
# C873SRC 000813|    initial_g = {site: (initial_n[site] + initial_div[site]) % F17 for site in initial_n}
# C873SRC 000814|    upper_g = {site: (final_n[site] + upper_div[site]) % F17 for site in final_n}
# C873SRC 000815|    lower_g = {site: (final_n[site] + lower_div[site]) % F17 for site in final_n}
# C873SRC 000816|    # Product unary basis states are orthogonal if any link label differs.
# C873SRC 000817|    field_inner_product = int(tuple(upper.values()) == tuple(lower.values()))
# C873SRC 000818|    same_divergence = upper_div == lower_div
# C873SRC 000819|    return {
# C873SRC 000820|        "one_particle_paths": ((a, b, c), (a, d, c)),
# C873SRC 000821|        "upper_link_labels": tuple(upper[edge] for edge in edges),
# C873SRC 000822|        "lower_link_labels": tuple(lower[edge] for edge in edges),
# C873SRC 000823|        "upper_divergence": upper_div,
# C873SRC 000824|        "lower_divergence": lower_div,
# C873SRC 000825|        "same_endpoint_divergence": same_divergence,
# C873SRC 000826|        "upper_G_matches_initial": upper_g == initial_g,
# C873SRC 000827|        "lower_G_matches_initial": lower_g == initial_g,
# C873SRC 000828|        "joint_F17_history_inner_product": field_inner_product,
# C873SRC 000829|        "matter_endpoint_inner_product": 1,
# C873SRC 000830|        "matter_reduced_interference_cross_term_relative_to_untracked_field":
# C873SRC 000831|            field_inner_product,
# C873SRC 000832|        "fixed_Gauss_sector_identifies_or_erases_closed_circulation": False,
# C873SRC 000833|        "integrated_landed_mass_dispersion_fixture_executed": False,
# C873SRC 000834|        "spectrum_boundary": (
# C873SRC 000835|            "for supplied computational-basis link initialization, the witness does not "
# C873SRC 000836|            "by itself support inheritance of the landed matter-only mass/dispersion fixture: "
# C873SRC 000837|            "alternative paths occupy orthogonal divergence-free F17 circulations inside "
# C873SRC 000838|            "the same endpoint G sector.  This is a route-local diagnostic, not an "
# C873SRC 000839|            "obstruction claim: the uniform +1 cycle-space sector constructed separately "
# C873SRC 000840|            "identifies those translations"
# C873SRC 000841|        ),
# C873SRC 000842|    }
# C873SRC 000843|
# C873SRC 000844|
# C873SRC 000845|def signed_transport_certificate():
# C873SRC 000846|    frames = C871.proper_frames()
# C873SRC 000847|    rows = failures = family_failures = 0
# C873SRC 000848|    omitted_swap = omitted_rail = wrong_polarity_flip = 0
# C873SRC 000849|    product_rows = product_failures = 0
# C873SRC 000850|
# C873SRC 000851|    def move(axis, state, frame):
# C873SRC 000852|        target_axis, sign = C871.signed_axis(frame, axis)
# C873SRC 000853|        a, b, label, alpha, family_sign = state
# C873SRC 000854|        if sign < 0:
# C873SRC 000855|            a, b, label = b, a, (-label) % F17
# C873SRC 000856|        return target_axis, (a, b, label, alpha, family_sign), sign
# C873SRC 000857|
# C873SRC 000858|    for axis in range(3):
# C873SRC 000859|        for frame in frames:
# C873SRC 000860|            _target_axis, sign = C871.signed_axis(frame, axis)
# C873SRC 000861|            for alpha in (-1, 1):
# C873SRC 000862|                family_sign = alpha
# C873SRC 000863|                for a, b in product((0, 1), repeat=2):
# C873SRC 000864|                    for label in range(F17):
# C873SRC 000865|                        state = (a, b, label, alpha, family_sign)
# C873SRC 000866|                        _moved_axis, moved, _ = move(axis, state, frame)
# C873SRC 000867|                        ma, mb, ml, malpha, ms = moved
# C873SRC 000868|                        before_g = ((a + family_sign * label) % F17,
# C873SRC 000869|                                    (b - family_sign * label) % F17)
# C873SRC 000870|                        moved_g = ((ma + ms * ml) % F17, (mb - ms * ml) % F17)
# C873SRC 000871|                        expected_g = before_g if sign > 0 else before_g[::-1]
# C873SRC 000872|                        family_failures += moved_g != expected_g
# C873SRC 000873|                        after = (b, a, (label + alpha * (a - b)) % F17, alpha, family_sign)
# C873SRC 000874|                        _after_axis, moved_after, _ = move(axis, after, frame)
# C873SRC 000875|                        observed_after = (
# C873SRC 000876|                            mb, ma, (ml + malpha * (ma - mb)) % F17,
# C873SRC 000877|                            malpha, ms,
# C873SRC 000878|                        )
# C873SRC 000879|                        rows += 1
# C873SRC 000880|                        failures += observed_after != moved_after
# C873SRC 000881|                        if sign < 0:
# C873SRC 000882|                            no_swap = (a, b, (-label) % F17, alpha, family_sign)
# C873SRC 000883|                            no_rail = (b, a, label, alpha, family_sign)
# C873SRC 000884|                            wrong_flip = (b, a, (-label) % F17, -alpha, -family_sign)
# C873SRC 000885|                            omitted_swap += no_swap != moved
# C873SRC 000886|                            omitted_rail += no_rail != moved
# C873SRC 000887|                            wrong_polarity_flip += wrong_flip != moved
# C873SRC 000888|        for right in frames:
# C873SRC 000889|            right_axis, right_sign = C871.signed_axis(right, axis)
# C873SRC 000890|            for left in frames:
# C873SRC 000891|                _left_axis, left_sign = C871.signed_axis(left, right_axis)
# C873SRC 000892|                direct = left @ right
# C873SRC 000893|                for alpha in (-1, 1):
# C873SRC 000894|                    for a, b in product((0, 1), repeat=2):
# C873SRC 000895|                        for label in range(F17):
# C873SRC 000896|                            state = (a, b, label, alpha, alpha)
# C873SRC 000897|                            middle_axis, middle, _ = move(axis, state, right)
# C873SRC 000898|                            final_axis, sequential, _ = move(middle_axis, middle, left)
# C873SRC 000899|                            direct_axis, direct_state, direct_sign = move(axis, state, direct)
# C873SRC 000900|                            product_rows += 1
# C873SRC 000901|                            product_failures += (final_axis, sequential) != (direct_axis, direct_state)
# C873SRC 000902|                            product_failures += direct_sign != left_sign * right_sign
# C873SRC 000903|    return {
# C873SRC 000904|        "proper_frames": len(frames),
# C873SRC 000905|        "ordered_frame_products": len(frames) ** 2,
# C873SRC 000906|        "signed_law_rows": rows,
# C873SRC 000907|        "signed_law_failures": failures,
# C873SRC 000908|        "typed_family_transport_failures": family_failures,
# C873SRC 000909|        "negative_frame_endpoint_swap_omission_detected_rows": omitted_swap,
# C873SRC 000910|        "negative_frame_rail_k_to_minus_k_omission_detected_rows": omitted_rail,
# C873SRC 000911|        "negative_frame_spurious_alpha_family_flip_detected_rows": wrong_polarity_flip,
# C873SRC 000912|        "polarity_normalization_rule": (
# C873SRC 000913|            "after canonical endpoint reversal: (a,b,k)->(b,a,-k), while supplied "
# C873SRC 000914|            "alpha and the matched family sign stay fixed (s*alpha=1 mod17)"
# C873SRC 000915|        ),
# C873SRC 000916|        "ordered_product_state_rows": product_rows,
# C873SRC 000917|        "ordered_product_failures": product_failures,
# C873SRC 000918|    }
# C873SRC 000919|
# C873SRC 000920|
# C873SRC 000921|def route_word(word: tuple[Instruction, ...], basis):
# C873SRC 000922|    logical_one = logical_two = routed = maximum_distance = 0
# C873SRC 000923|    nearest = operand = returned = 0
# C873SRC 000924|    touched: set[Coord] = set()
# C873SRC 000925|    paths = []
# C873SRC 000926|    route_hash = sha256()
# C873SRC 000927|    for instruction in word:
# C873SRC 000928|        if len(instruction.sites) == 1:
# C873SRC 000929|            logical_one += 1
# C873SRC 000930|            routed += 1
# C873SRC 000931|            touched.add(instruction.sites[0])
# C873SRC 000932|            route_hash.update(repr(instruction_signature(instruction)).encode())
# C873SRC 000933|            continue
# C873SRC 000934|        logical_two += 1
# C873SRC 000935|        left, right = instruction.sites
# C873SRC 000936|        path = C871.coframe_path(left, right, basis)
# C873SRC 000937|        paths.append(path)
# C873SRC 000938|        distance = len(path) - 1
# C873SRC 000939|        maximum_distance = max(maximum_distance, distance)
# C873SRC 000940|        nearest += sum(l1(a, b) != 1 for a, b in zip(path, path[1:]))
# C873SRC 000941|        labels = list(path)
# C873SRC 000942|        for index in range(len(path) - 2):
# C873SRC 000943|            labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C873SRC 000944|        operand += labels[-2:] != [left, right]
# C873SRC 000945|        for index in reversed(range(len(path) - 2)):
# C873SRC 000946|            labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C873SRC 000947|        returned += labels != list(path)
# C873SRC 000948|        routed += 2 * distance - 1
# C873SRC 000949|        touched.update(path)
# C873SRC 000950|        route_hash.update((instruction.kind + repr(path) + matrix_digest(instruction.matrix)).encode())
# C873SRC 000951|    return {
# C873SRC 000952|        "logical_instructions": len(word),
# C873SRC 000953|        "logical_one_site": logical_one,
# C873SRC 000954|        "logical_two_site": logical_two,
# C873SRC 000955|        "routed_gates": routed,
# C873SRC 000956|        "maximum_route_distance": maximum_distance,
# C873SRC 000957|        "nearest_neighbor_failures": nearest,
# C873SRC 000958|        "operand_order_failures": operand,
# C873SRC 000959|        "arbitrary_transit_return_failures": returned,
# C873SRC 000960|        "touched_coordinates": len(touched),
# C873SRC 000961|        "route_sha256": route_hash.hexdigest(),
# C873SRC 000962|        "_touched": touched,
# C873SRC 000963|        "_paths": tuple(paths),
# C873SRC 000964|    }
# C873SRC 000965|
# C873SRC 000966|
# C873SRC 000967|def structural_route_deletion_certificate(maximum_distance: int):
# C873SRC 000968|    tested = undetected = forward = central = reverse = 0
# C873SRC 000969|    full_operand = full_return = 0
# C873SRC 000970|    for distance in range(1, maximum_distance + 1):
# C873SRC 000971|        swaps = tuple(range(distance - 1))
# C873SRC 000972|        word = tuple(("forward", index) for index in swaps) + (("gate", -1),) + tuple(
# C873SRC 000973|            ("reverse", index) for index in reversed(swaps)
# C873SRC 000974|        )
# C873SRC 000975|        labels = list(range(distance + 1))
# C873SRC 000976|        gate_operands = None
# C873SRC 000977|        for kind, index in word:
# C873SRC 000978|            if kind == "gate":
# C873SRC 000979|                gate_operands = tuple(labels[-2:])
# C873SRC 000980|            else:
# C873SRC 000981|                labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C873SRC 000982|        full_operand += gate_operands != (0, distance)
# C873SRC 000983|        full_return += labels != list(range(distance + 1))
# C873SRC 000984|        for omitted in range(len(word)):
# C873SRC 000985|            labels = list(range(distance + 1))
# C873SRC 000986|            gate_seen = False
# C873SRC 000987|            gate_operands = None
# C873SRC 000988|            for index, (kind, site) in enumerate(word):
# C873SRC 000989|                if index == omitted:
# C873SRC 000990|                    continue
# C873SRC 000991|                if kind == "gate":
# C873SRC 000992|                    gate_seen = True
# C873SRC 000993|                    gate_operands = tuple(labels[-2:])
# C873SRC 000994|                else:
# C873SRC 000995|                    labels[site], labels[site + 1] = labels[site + 1], labels[site]
# C873SRC 000996|            detected = (
# C873SRC 000997|                not gate_seen or gate_operands != (0, distance)
# C873SRC 000998|                or labels != list(range(distance + 1))
# C873SRC 000999|            )
# C873SRC 001000|            tested += 1
# C873SRC 001001|            undetected += not detected
# C873SRC 001002|            forward += word[omitted][0] == "forward"
# C873SRC 001003|            central += word[omitted][0] == "gate"
# C873SRC 001004|            reverse += word[omitted][0] == "reverse"
# C873SRC 001005|    return {
# C873SRC 001006|        "path_distances": maximum_distance,
# C873SRC 001007|        "structural_symbolic_deletions": tested,
# C873SRC 001008|        "forward_SWAP_deletions": forward,
# C873SRC 001009|        "central_interaction_deletions": central,
# C873SRC 001010|        "return_SWAP_deletions": reverse,
# C873SRC 001011|        "undetected_structural_deletions": undetected,
# C873SRC 001012|        "full_operand_failures": full_operand,
# C873SRC 001013|        "full_arbitrary_register_return_failures": full_return,
# C873SRC 001014|        "qualification": (
# C873SRC 001015|            "symbolic arbitrary-register routing structure, not a claim that every "
# C873SRC 001016|            "literal primitive deletion changes every supplied reachable state"
# C873SRC 001017|        ),
# C873SRC 001018|    }
# C873SRC 001019|
# C873SRC 001020|
# C873SRC 001021|def schedule_color(seam):
# C873SRC 001022|    cell, axis, _target, _left, _right = seam
# C873SRC 001023|    return (axis, cell[0] & 1, cell[1] & 1, cell[2] & 1)
# C873SRC 001024|
# C873SRC 001025|
# C873SRC 001026|def schedule_key(color):
# C873SRC 001027|    axis, x, y, z = color
# C873SRC 001028|    residues = (x, y, z)
# C873SRC 001029|    return axis, residues[axis], residues[(axis + 1) % 3], residues[(axis + 2) % 3]
# C873SRC 001030|
# C873SRC 001031|
# C873SRC 001032|def factor_rows(rotations):
# C873SRC 001033|    output = defaultdict(list)
# C873SRC 001034|    for row in rotations:
# C873SRC 001035|        if row.factor and row.factor[0] == "seam":
# C873SRC 001036|            output[row.factor].append(row)
# C873SRC 001037|    return output
# C873SRC 001038|
# C873SRC 001039|
# C873SRC 001040|def seam_factor(graph, seam):
# C873SRC 001041|    index = C870.graph_seams(graph).index(seam)
# C873SRC 001042|    return ("seam", index, seam[0], seam[1], seam[2])
# C873SRC 001043|
# C873SRC 001044|
# C873SRC 001045|def phase_certificate(rows):
# C873SRC 001046|    abstract = tuple(row.row for row in rows)
# C873SRC 001047|    target = C870.fswap_polynomial(abstract)
