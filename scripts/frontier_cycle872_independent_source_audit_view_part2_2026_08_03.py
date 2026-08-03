#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 independent source, part 2/2."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 2
FIRST_SOURCE_LINE = 533
LAST_SOURCE_LINE = 1064
TOTAL_SOURCE_LINES = 1064
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "2350243e16aeb39a6a0f20b9a036468c82e541477e206566664c1103fa145523"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 000533|            depth += 1
# C872SRC 000534|            footprint.update(instruction.sites)
# C872SRC 000535|            continue
# C872SRC 000536|        path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000537|        depth += 2 * len(path) - 3
# C872SRC 000538|        footprint.update(path)
# C872SRC 000539|        labels = list(range(len(path)))
# C872SRC 000540|        for index in range(len(path) - 2):
# C872SRC 000541|            labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000542|        operands += labels[-2:] != [0, len(path) - 1]
# C872SRC 000543|        for index in reversed(range(len(path) - 2)):
# C872SRC 000544|            labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000545|        returns += labels != list(range(len(path)))
# C872SRC 000546|        if len(path) > 2:
# C872SRC 000547|            damaged = list(range(len(path)))
# C872SRC 000548|            for index in range(1, len(path) - 2):
# C872SRC 000549|                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
# C872SRC 000550|            for index in reversed(range(len(path) - 2)):
# C872SRC 000551|                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
# C872SRC 000552|            deletion += damaged != list(range(len(path)))
# C872SRC 000553|    return depth, footprint, deletion, operands, returns
# C872SRC 000554|
# C872SRC 000555|
# C872SRC 000556|def independent_routed_macro_payload(word, basis):
# C872SRC 000557|    output = []
# C872SRC 000558|    for serial, instruction in enumerate(word):
# C872SRC 000559|        source_matrix = matrix_key(instruction.matrix)
# C872SRC 000560|        if len(instruction.sites) == 1:
# C872SRC 000561|            output.append({
# C872SRC 000562|                "instruction_serial": serial, "role": "active_one_site",
# C872SRC 000563|                "sites": instruction.sites, "matrix": source_matrix,
# C872SRC 000564|            })
# C872SRC 000565|            continue
# C872SRC 000566|        path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000567|        swap_matrix = matrix_key(C870.c707.c655.SWAP)
# C872SRC 000568|        for index in range(len(path) - 2):
# C872SRC 000569|            output.append({
# C872SRC 000570|                "instruction_serial": serial, "role": "swap_forward",
# C872SRC 000571|                "sites": (path[index], path[index + 1]), "matrix": swap_matrix,
# C872SRC 000572|            })
# C872SRC 000573|        output.append({
# C872SRC 000574|            "instruction_serial": serial, "role": "active_two_site",
# C872SRC 000575|            "sites": (path[-2], path[-1]), "matrix": source_matrix,
# C872SRC 000576|        })
# C872SRC 000577|        for index in reversed(range(len(path) - 2)):
# C872SRC 000578|            output.append({
# C872SRC 000579|                "instruction_serial": serial, "role": "swap_return",
# C872SRC 000580|                "sites": (path[index], path[index + 1]), "matrix": swap_matrix,
# C872SRC 000581|            })
# C872SRC 000582|    return tuple(output)
# C872SRC 000583|
# C872SRC 000584|
# C872SRC 000585|def independent_macro_mutations():
# C872SRC 000586|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 000587|    context = C870.physical_context(graph)
# C872SRC 000588|    seams = C870.graph_seams(graph)
# C872SRC 000589|    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 000590|    factor_map = {
# C872SRC 000591|        factor: tuple(group)
# C872SRC 000592|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 000593|        if factor[0] == "seam"
# C872SRC 000594|    }
# C872SRC 000595|    families = {"canonical": [], "wrong_side": [], "seam_deleted": []}
# C872SRC 000596|    for index, seam in enumerate(seams):
# C872SRC 000597|        placement = C871.packet_placement(graph, context, seam)
# C872SRC 000598|        factor = ("seam", index, seam[0], seam[1], seam[2])
# C872SRC 000599|        rows = factor_map[factor]
# C872SRC 000600|        for label, options in (
# C872SRC 000601|            ("canonical", {}),
# C872SRC 000602|            ("wrong_side", {"wrong_side": True}),
# C872SRC 000603|            ("seam_deleted", {"delete_seam": True}),
# C872SRC 000604|        ):
# C872SRC 000605|            segments = independent_segments(
# C872SRC 000606|                graph, context, seam, placement, rows, **options
# C872SRC 000607|            )
# C872SRC 000608|            word = tuple(
# C872SRC 000609|                instruction for segment in segments.values() for instruction in segment
# C872SRC 000610|            )
# C872SRC 000611|            families[label].append(independent_routed_macro_payload(word, placement.basis))
# C872SRC 000612|    return {
# C872SRC 000613|        "seams": len(seams),
# C872SRC 000614|        "canonical_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000615|            tuple(families["canonical"])
# C872SRC 000616|        )).hexdigest(),
# C872SRC 000617|        "wrong_side_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000618|            tuple(families["wrong_side"])
# C872SRC 000619|        )).hexdigest(),
# C872SRC 000620|        "seam_deleted_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000621|            tuple(families["seam_deleted"])
# C872SRC 000622|        )).hexdigest(),
# C872SRC 000623|        "wrong_side_digest_detections": sum(
# C872SRC 000624|            left != right for left, right in zip(
# C872SRC 000625|                families["canonical"], families["wrong_side"]
# C872SRC 000626|            )
# C872SRC 000627|        ),
# C872SRC 000628|        "seam_deletion_digest_detections": sum(
# C872SRC 000629|            left != right for left, right in zip(
# C872SRC 000630|                families["canonical"], families["seam_deleted"]
# C872SRC 000631|            )
# C872SRC 000632|        ),
# C872SRC 000633|    }
# C872SRC 000634|
# C872SRC 000635|
# C872SRC 000636|def fixture(length, full):
# C872SRC 000637|    graph = C870.prep.OpenReferenceGraph(cells(length))
# C872SRC 000638|    context = C870.physical_context(graph)
# C872SRC 000639|    seams = C870.graph_seams(graph)
# C872SRC 000640|    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
# C872SRC 000641|    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
# C872SRC 000642|    resource_banks = tuple(resource_bank(placement) for placement in placements)
# C872SRC 000643|    blocked = set(context.sites) | J870.auxiliary_registers(graph)
# C872SRC 000644|    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 000645|    factors = tuple(
# C872SRC 000646|        (factor, tuple(group))
# C872SRC 000647|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 000648|    )
# C872SRC 000649|    factor_map = {
# C872SRC 000650|        factor: rows for factor, rows in factors if factor[0] == "seam"
# C872SRC 000651|    }
# C872SRC 000652|    words = []
# C872SRC 000653|    seam_words = []
# C872SRC 000654|    binding_failures = 0
# C872SRC 000655|    for index, (seam, placement) in enumerate(zip(seams, placements)):
# C872SRC 000656|        key = ("seam", index, seam[0], seam[1], seam[2])
# C872SRC 000657|        rows = factor_map.get(key, ())
# C872SRC 000658|        binding_failures += len(rows) != 4
# C872SRC 000659|        word, seam_word = independent_macro(graph, context, seam, placement, rows)
# C872SRC 000660|        words.append(word)
# C872SRC 000661|        seam_words.append(seam_word)
# C872SRC 000662|
# C872SRC 000663|    metrics = [path_metrics(word, placement.basis) for word, placement in zip(words, placements)]
# C872SRC 000664|    depths = {seam: metrics[index][0] for index, seam in enumerate(seams)}
# C872SRC 000665|    footprints = {seam: metrics[index][1] for index, seam in enumerate(seams)}
# C872SRC 000666|    deletion = sum(row[2] for row in metrics)
# C872SRC 000667|    route_failures = sum(row[3] + row[4] for row in metrics)
# C872SRC 000668|    groups = defaultdict(list)
# C872SRC 000669|    for seam in seams:
# C872SRC 000670|        groups[fine(seam)].append(seam)
# C872SRC 000671|    schedule_depth = sum(max(depths[seam] for seam in members) for members in groups.values())
# C872SRC 000672|    fine_collisions = sum(
# C872SRC 000673|        bool(footprints[left] & footprints[right])
# C872SRC 000674|        for index, left in enumerate(seams) for right in seams[:index]
# C872SRC 000675|        if fine(left) == fine(right)
# C872SRC 000676|    )
# C872SRC 000677|    six_collisions = sum(
# C872SRC 000678|        bool(footprints[left] & footprints[right])
# C872SRC 000679|        for index, left in enumerate(seams) for right in seams[:index]
# C872SRC 000680|        if coarse(left) == coarse(right)
# C872SRC 000681|    )
# C872SRC 000682|    packet_union = set().union(*(set(row.sites) for row in placements))
# C872SRC 000683|    resource_union = set().union(*resource_banks)
# C872SRC 000684|    packet_overlaps = sum(
# C872SRC 000685|        bool(set(left.sites) & set(right.sites))
# C872SRC 000686|        for index, left in enumerate(placements) for right in placements[:index]
# C872SRC 000687|    )
# C872SRC 000688|    resource_overlaps = sum(
# C872SRC 000689|        bool(left & right)
# C872SRC 000690|        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
# C872SRC 000691|    )
# C872SRC 000692|    spatial_geometry_failures = (
# C872SRC 000693|        len(spatial_sites) - len(set(spatial_sites))
# C872SRC 000694|        + sum(site in packet_union for site in spatial_sites)
# C872SRC 000695|        + sum(site in blocked for site in spatial_sites)
# C872SRC 000696|    )
# C872SRC 000697|
# C872SRC 000698|    route_difference = reconcile_failures = 0
# C872SRC 000699|    for seam_word, placement in zip(seam_words, placements):
# C872SRC 000700|        for instruction in seam_word:
# C872SRC 000701|            if len(instruction.sites) != 2:
# C872SRC 000702|                continue
# C872SRC 000703|            replacement = C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 000704|            landed = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
# C872SRC 000705|            route_difference += replacement != landed
# C872SRC 000706|            reconcile_failures += (
# C872SRC 000707|                replacement[0] != landed[0] or replacement[-1] != landed[-1]
# C872SRC 000708|            )
# C872SRC 000709|
# C872SRC 000710|    bank_at = {
# C872SRC 000711|        site: bank for bank, resources in enumerate(resource_banks) for site in resources
# C872SRC 000712|    }
# C872SRC 000713|    dirty_pairs = set()
# C872SRC 000714|    dirty_failures = 0
# C872SRC 000715|    if full:
# C872SRC 000716|        for macro, (seam, placement, word) in enumerate(zip(seams, placements, words)):
# C872SRC 000717|            for instruction in word:
# C872SRC 000718|                if len(instruction.sites) != 2:
# C872SRC 000719|                    continue
# C872SRC 000720|                path = C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 000721|                for path_index, site in enumerate(path):
# C872SRC 000722|                    other = bank_at.get(site)
# C872SRC 000723|                    if other is None or other == macro:
# C872SRC 000724|                        continue
# C872SRC 000725|                    dirty_pairs.add((macro, other))
# C872SRC 000726|                    dirty_failures += path_index in (0, len(path) - 1)
# C872SRC 000727|                    dirty_failures += fine(seam) == fine(seams[other])
# C872SRC 000728|
# C872SRC 000729|    result = {
# C872SRC 000730|        "length": length,
# C872SRC 000731|        "cells": len(graph.cells),
# C872SRC 000732|        "seams": len(seams),
# C872SRC 000733|        "rotations": len(rotations),
# C872SRC 000734|        "factors": len(factors),
# C872SRC 000735|        "instructions": sum(map(len, words)),
# C872SRC 000736|        "binding_failures": binding_failures,
# C872SRC 000737|        "schedule_depth": schedule_depth,
# C872SRC 000738|        "fine_collisions": fine_collisions,
# C872SRC 000739|        "six_collisions": six_collisions,
# C872SRC 000740|        "packet_union": len(packet_union),
# C872SRC 000741|        "resource_union": len(resource_union),
# C872SRC 000742|        "packet_overlaps": packet_overlaps,
# C872SRC 000743|        "resource_overlaps": resource_overlaps,
# C872SRC 000744|        "spatial_geometry_failures": spatial_geometry_failures,
# C872SRC 000745|        "first_forward_swap_deletion_detections": deletion,
# C872SRC 000746|        "route_failures": route_failures,
# C872SRC 000747|        "route_differences": route_difference,
# C872SRC 000748|        "route_reconciliation_failures": reconcile_failures,
# C872SRC 000749|        "dirty_pairs": len(dirty_pairs),
# C872SRC 000750|        "dirty_failures": dirty_failures,
# C872SRC 000751|        "used_packet_M2_per_seam": C714.N,
# C872SRC 000752|        "retained_spatial_current_M2_per_seam": 1,
# C872SRC 000753|        "total_resource_M2_per_seam": C714.N + 1,
# C872SRC 000754|        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
# C872SRC 000755|        "lockstep_schedule_key": (
# C872SRC 000756|            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
# C872SRC 000757|            "on remaining axes in ascending global-axis order"
# C872SRC 000758|        ),
# C872SRC 000759|        "route_policy": "coframe replacement in augmented seam stage",
# C872SRC 000760|    }
# C872SRC 000761|    expected = EXPECTED_FIXTURES[length]
# C872SRC 000762|    result["expected_mismatches"] = {
# C872SRC 000763|        key: (expected_value, result.get(key))
# C872SRC 000764|        for key, expected_value in expected.items()
# C872SRC 000765|        if result.get(key) != expected_value
# C872SRC 000766|    }
# C872SRC 000767|    return result
# C872SRC 000768|
# C872SRC 000769|
# C872SRC 000770|def direction_check():
# C872SRC 000771|    failures = Counter()
# C872SRC 000772|    counts = Counter()
# C872SRC 000773|    pairs = set()
# C872SRC 000774|    for pointer, binder, actuality, admissibility, law, fresh, causal in product(
# C872SRC 000775|        (0, 1), repeat=7
# C872SRC 000776|    ):
# C872SRC 000777|        controls = (pointer, binder, actuality, admissibility, law, fresh)
# C872SRC 000778|        after = C714.apply_semantic(
# C872SRC 000779|            C714.initial(9, 12, causal, controls), C714.word()
# C872SRC 000780|        )
# C872SRC 000781|        counts["exact_packet_equation_rows"] += 1
# C872SRC 000782|        failures["exact_packet_equation"] += after[C714.PORIENT] != (
# C872SRC 000783|            pointer & binder & actuality & admissibility & law & fresh & causal
# C872SRC 000784|        )
# C872SRC 000785|    for axis in range(3):
# C872SRC 000786|        left, right = 2 * axis + 1, 6 + 2 * axis
# C872SRC 000787|        for source in product((0, 1), repeat=12):
# C872SRC 000788|            target, _phase = C704.GAUSS.target_fswap_action(source, left, right)
# C872SRC 000789|            pointer = source[left] ^ source[right]
# C872SRC 000790|            uv = pointer & target[right]
# C872SRC 000791|            vu = pointer & target[left]
# C872SRC 000792|            failures["one_hot"] += (uv ^ vu) != pointer
# C872SRC 000793|            failures["current_decode"] += 2 * uv - pointer != uv - vu
# C872SRC 000794|            for causal in (0, 1):
# C872SRC 000795|                pairs.add((uv, causal))
# C872SRC 000796|                counts["rows"] += 1
# C872SRC 000797|                counts["moving"] += pointer
# C872SRC 000798|                counts["wrong_side"] += pointer and vu != uv
# C872SRC 000799|                counts["seam_deletion"] += (0, 0) != (pointer, uv)
# C872SRC 000800|                spatial = pointer & target[right]
# C872SRC 000801|                failures["spatial_output"] += spatial != uv
# C872SRC 000802|                counts["dirty_spatial"] += (1 ^ spatial) != uv
# C872SRC 000803|                before = C714.initial(
# C872SRC 000804|                    9, 12, causal, (pointer, 1, 1, 1, 1, 1)
# C872SRC 000805|                )
# C872SRC 000806|                after = C714.apply_semantic(before, C714.word())
# C872SRC 000807|                failures["causal_projection"] += (
# C872SRC 000808|                    after[C714.PORIENT] != pointer & causal
# C872SRC 000809|                )
# C872SRC 000810|                failures["causal_return"] += after[C714.ORIENT] != causal
# C872SRC 000811|                damaged = C714.initial(
# C872SRC 000812|                    9, 12, causal ^ uv, (pointer, 1, 1, 1, 1, 1)
# C872SRC 000813|                )
# C872SRC 000814|                damaged_after = C714.apply_semantic(damaged, C714.word())
# C872SRC 000815|                counts["ORIENT_overload"] += (
# C872SRC 000816|                    damaged_after[C714.PORIENT] != pointer & causal
# C872SRC 000817|                )
# C872SRC 000818|    once = C714.apply_semantic(C714.initial(9, 12, 1), C714.word())
# C872SRC 000819|    twice = C714.apply_semantic(once, C714.word())
# C872SRC 000820|    return {
# C872SRC 000821|        **dict(counts), "failure_census": dict(failures),
# C872SRC 000822|        "spatial_causal_pairs": tuple(sorted(pairs)),
# C872SRC 000823|        "reuse_changed_bits": sum(a != b for a, b in zip(once, twice)),
# C872SRC 000824|    }
# C872SRC 000825|
# C872SRC 000826|
# C872SRC 000827|def continuity_check():
# C872SRC 000828|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 000829|    seams = C870.graph_seams(graph)
# C872SRC 000830|    index = {cell: row for row, cell in enumerate(graph.cells)}
# C872SRC 000831|    failures = 0
# C872SRC 000832|    patterns = 0
# C872SRC 000833|    for currents in product((-1, 0, 1), repeat=len(seams)):
# C872SRC 000834|        direct = [0] * len(graph.cells)
# C872SRC 000835|        incidence = [0] * len(graph.cells)
# C872SRC 000836|        for seam, current in zip(seams, currents):
# C872SRC 000837|            pre_u, pre_v = (
# C872SRC 000838|                (1, 0) if current == 1 else (0, 1) if current == -1 else (0, 0)
# C872SRC 000839|            )
# C872SRC 000840|            post_u, post_v = pre_v, pre_u
# C872SRC 000841|            direct[index[seam[0]]] += post_u - pre_u
# C872SRC 000842|            direct[index[seam[2]]] += post_v - pre_v
# C872SRC 000843|            incidence[index[seam[0]]] -= current
# C872SRC 000844|            incidence[index[seam[2]]] += current
# C872SRC 000845|        failures += direct != incidence or sum(direct) != 0
# C872SRC 000846|        patterns += 1
# C872SRC 000847|    frame_failures = product_failures = 0
# C872SRC 000848|    frames = C871.proper_frames()
# C872SRC 000849|    for seam in seams:
# C872SRC 000850|        for frame in frames:
# C872SRC 000851|            _axis, sign = C871.signed_axis(frame, seam[1])
# C872SRC 000852|            for current in (-1, 0, 1):
# C872SRC 000853|                moved = sign * current
# C872SRC 000854|                frame_failures += abs(moved) != abs(current)
# C872SRC 000855|        for left in frames:
# C872SRC 000856|            for right in frames:
# C872SRC 000857|                intermediate, sr = C871.signed_axis(right, seam[1])
# C872SRC 000858|                _final, sl = C871.signed_axis(left, intermediate)
# C872SRC 000859|                _product, sp = C871.signed_axis(left @ right, seam[1])
# C872SRC 000860|                for current in (-1, 0, 1):
# C872SRC 000861|                    product_failures += sl * sr * current != sp * current
# C872SRC 000862|    return {
# C872SRC 000863|        "patterns": patterns,
# C872SRC 000864|        "covered_columns": 4 ** len(seams),
# C872SRC 000865|        "continuity_failures": failures,
# C872SRC 000866|        "frame_rows": len(seams) * len(frames) * 3,
# C872SRC 000867|        "frame_failures": frame_failures,
# C872SRC 000868|        "product_rows": len(seams) * len(frames) ** 2 * 3,
# C872SRC 000869|        "product_failures": product_failures,
# C872SRC 000870|    }
# C872SRC 000871|
# C872SRC 000872|
# C872SRC 000873|def allocator_check():
# C872SRC 000874|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 000875|    context = C870.physical_context(graph)
# C872SRC 000876|    seam = C870.graph_seams(graph)[0]
# C872SRC 000877|    midpoint = C871.seam_midpoint(seam[0], seam[1])
# C872SRC 000878|    basis = C871.local_coframe(seam[1])
# C872SRC 000879|    blocked = set(context.sites) | J870.auxiliary_registers(graph)
# C872SRC 000880|    def physical(local):
# C872SRC 000881|        output = midpoint
# C872SRC 000882|        for coefficient, direction in zip(local, basis):
# C872SRC 000883|            output = C871.add(output, C871.scale(coefficient, direction))
# C872SRC 000884|        return output
# C872SRC 000885|    available = {
# C872SRC 000886|        row for row in product(range(-3, 4), repeat=3) if physical(row) not in blocked
# C872SRC 000887|    }
# C872SRC 000888|    def rotate(row):
# C872SRC 000889|        a, b, c = row
# C872SRC 000890|        return a, -c, b
# C872SRC 000891|    seen = set()
# C872SRC 000892|    orbits = []
# C872SRC 000893|    for row in sorted(available):
# C872SRC 000894|        if row in seen:
# C872SRC 000895|            continue
# C872SRC 000896|        orbit = []
# C872SRC 000897|        current = row
# C872SRC 000898|        for _ in range(4):
# C872SRC 000899|            orbit.append(current)
# C872SRC 000900|            current = rotate(current)
# C872SRC 000901|        orbit = frozenset(orbit)
# C872SRC 000902|        seen.update(orbit)
# C872SRC 000903|        if len(orbit) == 4 and orbit <= available:
# C872SRC 000904|            orbits.append(orbit)
# C872SRC 000905|    reflect = lambda orbit: frozenset((-a, b, -c) for a, b, c in orbit)
# C872SRC 000906|    fixed = sorted((row for row in orbits if reflect(row) == row), key=repr)
# C872SRC 000907|    paired = []
# C872SRC 000908|    used = set(fixed)
# C872SRC 000909|    for orbit in sorted(orbits, key=repr):
# C872SRC 000910|        if orbit in used:
# C872SRC 000911|            continue
# C872SRC 000912|        partner = reflect(orbit)
# C872SRC 000913|        pair = tuple(sorted((orbit, partner), key=repr))
# C872SRC 000914|        paired.append(pair)
# C872SRC 000915|        used.update(pair)
# C872SRC 000916|    paired.sort(key=repr)
# C872SRC 000917|    selected = tuple(fixed[:5]) + tuple(row for pair in paired[:27] for row in pair)
# C872SRC 000918|    selected_set = set(selected)
# C872SRC 000919|    sites = frozenset(site for orbit in selected for site in orbit)
# C872SRC 000920|    failures = 0
# C872SRC 000921|    products = 0
# C872SRC 000922|    frames = C871.proper_frames()
# C872SRC 000923|    def matrix(axis, frame):
# C872SRC 000924|        target, _sign = C871.signed_axis(frame, axis)
# C872SRC 000925|        return target, np.asarray(
# C872SRC 000926|            np.column_stack(C871.local_coframe(target)).T
# C872SRC 000927|            @ frame @ np.column_stack(C871.local_coframe(axis)), dtype=int
# C872SRC 000928|        )
# C872SRC 000929|    for axis in range(3):
# C872SRC 000930|        for frame in frames:
# C872SRC 000931|            _target, transform = matrix(axis, frame)
# C872SRC 000932|            failures += frozenset(
# C872SRC 000933|                tuple(map(int, transform @ np.asarray(site))) for site in sites
# C872SRC 000934|            ) != sites
# C872SRC 000935|            failures += any(
# C872SRC 000936|                frozenset(tuple(map(int, transform @ np.asarray(site))) for site in orbit)
# C872SRC 000937|                not in selected_set for orbit in selected
# C872SRC 000938|            )
# C872SRC 000939|        for left in frames:
# C872SRC 000940|            for right in frames:
# C872SRC 000941|                intermediate, mr = matrix(axis, right)
# C872SRC 000942|                final, ml = matrix(intermediate, left)
# C872SRC 000943|                product_axis, mp = matrix(axis, left @ right)
# C872SRC 000944|                products += 1
# C872SRC 000945|                failures += final != product_axis or not np.array_equal(ml @ mr, mp)
# C872SRC 000946|    return {
# C872SRC 000947|        "status": "separate geometric candidate",
# C872SRC 000948|        "used_by_epoch": False,
# C872SRC 000949|        "available_orbits": len(orbits),
# C872SRC 000950|        "selected_registers": len(selected),
# C872SRC 000951|        "M2_per_seam": len(sites),
# C872SRC 000952|        "frames": len(frames),
# C872SRC 000953|        "products": products,
# C872SRC 000954|        "failures": failures,
# C872SRC 000955|    }
# C872SRC 000956|
# C872SRC 000957|
# C872SRC 000958|def mass_contact_check():
# C872SRC 000959|    inherited = C871.inherited_matter_certificate()
# C872SRC 000960|    return {
# C872SRC 000961|        "scope": (
# C872SRC 000962|            "inherited unchanged Cycle870/Cycle871 factor fixtures; not a new "
# C872SRC 000963|            "integrated-epoch spectrum"
# C872SRC 000964|        ),
# C872SRC 000965|        "mass": inherited["mass_fixture_pass"],
# C872SRC 000966|        "contact": inherited["contact_fixture_pass"],
# C872SRC 000967|        "mass_difference": abs(
# C872SRC 000968|            inherited["one_particle"]["analytic_mass"]
# C872SRC 000969|            - inherited["one_particle"]["rest_mass"]
# C872SRC 000970|        ),
# C872SRC 000971|        "contact_residual": inherited["contact"]["maximum_residual_up_to_global_phase"],
# C872SRC 000972|    }
# C872SRC 000973|
# C872SRC 000974|
# C872SRC 000975|def build_report():
# C872SRC 000976|    report = {
# C872SRC 000977|        "schema": "cycle872-all-seam-spatial-packet-independent-v1",
# C872SRC 000978|        "status": "pending",
# C872SRC 000979|        "independence": independent_import_certificate(),
# C872SRC 000980|        "provenance": provenance(),
# C872SRC 000981|        "physical_epoch_stream": independent_physical_stream_check(),
# C872SRC 000982|        "physical_macro_mutations": independent_macro_mutations(),
# C872SRC 000983|        "fixtures": [fixture(length, length in (2, 3)) for length in (2, 3, 4, 5)],
# C872SRC 000984|        "direction": direction_check(),
# C872SRC 000985|        "continuity": continuity_check(),
# C872SRC 000986|        "four_rail_candidate": allocator_check(),
# C872SRC 000987|        "mass_contact": mass_contact_check(),
# C872SRC 000988|        "scope": (
# C872SRC 000989|            "one clean-own-bank epoch using a 59-site packet plus separate retained spatial-current "
# C872SRC 000990|            "M2 per seam and a declared coframe replacement route; four-rail allocation is separate; "
# C872SRC 000991|            "causal ORIENT and later reset remain supplied"
# C872SRC 000992|        ),
# C872SRC 000993|    }
# C872SRC 000994|    failures = []
# C872SRC 000995|    if report["independence"]["primary_imported"]:
# C872SRC 000996|        failures.append("primary imported")
# C872SRC 000997|    if report["provenance"]["pin_failures"] or report["provenance"]["note_pin_failure"]:
# C872SRC 000998|        failures.append("provenance")
# C872SRC 000999|    stream = report["physical_epoch_stream"]
# C872SRC 001000|    if any(stream["failure_census"].values()) or stream["expected_mismatches"]:
# C872SRC 001001|        failures.append("physical epoch stream")
# C872SRC 001002|    if stream["first_forward_swap_deletion_detections"] <= 0:
# C872SRC 001003|        failures.append("physical stream deletion")
# C872SRC 001004|    mutations = report["physical_macro_mutations"]
# C872SRC 001005|    if any((
# C872SRC 001006|        mutations["wrong_side_digest_detections"] != mutations["seams"],
# C872SRC 001007|        mutations["seam_deletion_digest_detections"] != mutations["seams"],
# C872SRC 001008|    )):
# C872SRC 001009|        failures.append("physical macro mutations")
# C872SRC 001010|    for row in report["fixtures"]:
# C872SRC 001011|        if row["expected_mismatches"]:
# C872SRC 001012|            failures.append(f"L{row['length']} expected mismatch")
# C872SRC 001013|        if any(row[key] for key in (
# C872SRC 001014|            "binding_failures", "packet_overlaps", "resource_overlaps",
# C872SRC 001015|            "spatial_geometry_failures", "route_failures",
# C872SRC 001016|            "route_reconciliation_failures", "fine_collisions",
# C872SRC 001017|        )):
# C872SRC 001018|            failures.append(f"L{row['length']} fixture failure")
# C872SRC 001019|        if row["six_collisions"] <= 0 or row["first_forward_swap_deletion_detections"] <= 0:
# C872SRC 001020|            failures.append(f"L{row['length']} inactive control")
# C872SRC 001021|        if row["length"] in (2, 3) and row["dirty_failures"]:
# C872SRC 001022|            failures.append(f"L{row['length']} dirty")
# C872SRC 001023|    if any(report["direction"]["failure_census"].values()):
# C872SRC 001024|        failures.append("direction")
# C872SRC 001025|    if any((
# C872SRC 001026|        report["direction"]["wrong_side"] != 12288,
# C872SRC 001027|        report["direction"]["dirty_spatial"] != 24576,
# C872SRC 001028|        report["direction"]["ORIENT_overload"] != 6144,
# C872SRC 001029|        report["direction"]["seam_deletion"] != 12288,
# C872SRC 001030|        len(report["direction"]["spatial_causal_pairs"]) != 4,
# C872SRC 001031|    )):
# C872SRC 001032|        failures.append("direction controls")
# C872SRC 001033|    if report["direction"]["reuse_changed_bits"] <= 0:
# C872SRC 001034|        failures.append("reuse control")
# C872SRC 001035|    if any(report["continuity"][key] for key in (
# C872SRC 001036|        "continuity_failures", "frame_failures", "product_failures"
# C872SRC 001037|    )):
# C872SRC 001038|        failures.append("continuity")
# C872SRC 001039|    if report["four_rail_candidate"]["failures"]:
# C872SRC 001040|        failures.append("allocator")
# C872SRC 001041|    if not report["mass_contact"]["mass"] or not report["mass_contact"]["contact"]:
# C872SRC 001042|        failures.append("mass/contact")
# C872SRC 001043|    report["failures"] = failures
# C872SRC 001044|    report["status"] = "pass" if not failures else "fail"
# C872SRC 001045|    return report
# C872SRC 001046|
# C872SRC 001047|
# C872SRC 001048|def main():
# C872SRC 001049|    parser = argparse.ArgumentParser()
# C872SRC 001050|    parser.add_argument("--output", type=Path, default=DEFAULT_RECEIPT)
# C872SRC 001051|    args = parser.parse_args()
# C872SRC 001052|    report = build_report()
# C872SRC 001053|    args.output.parent.mkdir(parents=True, exist_ok=True)
# C872SRC 001054|    args.output.write_text(
# C872SRC 001055|        json.dumps(report, indent=2, sort_keys=True, default=float) + "\n",
# C872SRC 001056|        encoding="utf-8",
# C872SRC 001057|    )
# C872SRC 001058|    print("CYCLE872_ALL_SEAM_SPATIAL_PACKET_INDEPENDENT_PASS" if report["status"] == "pass"
# C872SRC 001059|          else "CYCLE872_ALL_SEAM_SPATIAL_PACKET_INDEPENDENT_FAIL")
# C872SRC 001060|    return 0 if report["status"] == "pass" else 1
# C872SRC 001061|
# C872SRC 001062|
# C872SRC 001063|if __name__ == "__main__":
# C872SRC 001064|    raise SystemExit(main())
