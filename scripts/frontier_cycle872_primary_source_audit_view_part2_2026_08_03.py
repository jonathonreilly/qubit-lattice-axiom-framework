#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 primary source, part 2/4."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
PART_ORDINAL = 2
PART_COUNT = 4
FIRST_SOURCE_LINE = 486
LAST_SOURCE_LINE = 970
TOTAL_SOURCE_LINES = 1940
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "c1b32ef8e2a870128b7081a88b920b85c84123d04f98a165bfc7225dcfc716e4"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 000486|                        )
# C872SRC 000487|                        actual.extend(rotation_word)
# C872SRC 000488|                        for instruction in rotation_word:
# C872SRC 000489|                            emit_instruction(
# C872SRC 000490|                                factor_index, factor, stage, segment, rotation.serial,
# C872SRC 000491|                                instruction, route_policy, placement.basis,
# C872SRC 000492|                            )
# C872SRC 000493|                    failures["seam_segment_actual_word"] += (
# C872SRC 000494|                        C871.word_sha256(tuple(actual)) != C871.word_sha256(segment_word)
# C872SRC 000495|                    )
# C872SRC 000496|                else:
# C872SRC 000497|                    for instruction in segment_word:
# C872SRC 000498|                        emit_instruction(
# C872SRC 000499|                            factor_index, factor, stage, segment, None,
# C872SRC 000500|                            instruction, route_policy, placement.basis,
# C872SRC 000501|                        )
# C872SRC 000502|        else:
# C872SRC 000503|            for rotation in factor_rotations:
# C872SRC 000504|                rotation_word = C870.c707.compile_pauli_rotation(
# C872SRC 000505|                    C870.physical_lift(rotation.row, context),
# C872SRC 000506|                    context.sites,
# C872SRC 000507|                    rotation.angle,
# C872SRC 000508|                )
# C872SRC 000509|                for instruction in rotation_word:
# C872SRC 000510|                    emit_instruction(
# C872SRC 000511|                        factor_index, factor, stage, "landed_factor",
# C872SRC 000512|                        rotation.serial, instruction, route_policy, None,
# C872SRC 000513|                    )
# C872SRC 000514|        factor_manifest.append({
# C872SRC 000515|            "factor_index": factor_index,
# C872SRC 000516|            "factor": factor,
# C872SRC 000517|            "stage": stage,
# C872SRC 000518|            "native_rotation_serials": tuple(row.serial for row in factor_rotations),
# C872SRC 000519|            "replacement": "augmented_seam_macro" if stage == "seam" else "identity",
# C872SRC 000520|            "route_policy": route_policy,
# C872SRC 000521|            "instruction_serial_start": instruction_start,
# C872SRC 000522|            "instruction_serial_stop_exclusive": len(instructions),
# C872SRC 000523|            "physical_gate_serial_start": gate_start,
# C872SRC 000524|            "physical_gate_serial_stop_exclusive": len(gates),
# C872SRC 000525|        })
# C872SRC 000526|
# C872SRC 000527|    expected_factor_sequence = tuple(factor for factor, _rows in factors)
# C872SRC 000528|    observed_factor_sequence = tuple(row["factor"] for row in factor_manifest)
# C872SRC 000529|    failures["factor_sequence"] += observed_factor_sequence != expected_factor_sequence
# C872SRC 000530|    failures["factor_count"] += len(factor_manifest) != len(factors)
# C872SRC 000531|    failures["rotation_coverage"] += tuple(
# C872SRC 000532|        serial
# C872SRC 000533|        for row in factor_manifest
# C872SRC 000534|        for serial in row["native_rotation_serials"]
# C872SRC 000535|    ) != tuple(row.serial for row in rotations)
# C872SRC 000536|    failures["instruction_serial"] += any(
# C872SRC 000537|        row.serial != index for index, row in enumerate(instructions)
# C872SRC 000538|    )
# C872SRC 000539|    failures["physical_gate_serial"] += any(
# C872SRC 000540|        row.serial != index for index, row in enumerate(gates)
# C872SRC 000541|    )
# C872SRC 000542|    failures["factor_binding"] += sum(
# C872SRC 000543|        row.factor_index != instruction.factor_index
# C872SRC 000544|        for instruction in instructions
# C872SRC 000545|        for row in gates[instruction.gate_start:instruction.gate_stop]
# C872SRC 000546|    )
# C872SRC 000547|    failures["NN_support"] += sum(
# C872SRC 000548|        len(row.sites) == 2 and C870.c707.c655.l1(*row.sites) != 1
# C872SRC 000549|        for row in gates
# C872SRC 000550|    )
# C872SRC 000551|    failures["gate_arity"] += sum(len(row.sites) not in (1, 2) for row in gates)
# C872SRC 000552|    failures["stage_order"] += tuple(dict.fromkeys(
# C872SRC 000553|        row["stage"] for row in factor_manifest
# C872SRC 000554|    )) != ("coin", "reverse", "seam", "contact")
# C872SRC 000555|    failures["landed_nonseam_route_policy"] += sum(
# C872SRC 000556|        row["stage"] != "seam"
# C872SRC 000557|        and row["route_policy"] != "landed_global_axis_manhattan_returned"
# C872SRC 000558|        for row in factor_manifest
# C872SRC 000559|    )
# C872SRC 000560|    failures["seam_route_policy"] += sum(
# C872SRC 000561|        row["stage"] == "seam"
# C872SRC 000562|        and row["route_policy"] != "augmented_seam_local_coframe_returned"
# C872SRC 000563|        for row in factor_manifest
# C872SRC 000564|    )
# C872SRC 000565|    return PhysicalEpochStream(
# C872SRC 000566|        length, rotations, inventory, factors, tuple(factor_manifest),
# C872SRC 000567|        tuple(instructions), tuple(gates), registry, dict(failures),
# C872SRC 000568|        deletion_detections,
# C872SRC 000569|    )
# C872SRC 000570|
# C872SRC 000571|
# C872SRC 000572|def physical_stream_certificate(stream: PhysicalEpochStream) -> dict[str, object]:
# C872SRC 000573|    payload = physical_stream_payload(stream)
# C872SRC 000574|    payload_bytes = canonical_json_bytes(payload)
# C872SRC 000575|    gate_payload = tuple(serialize_physical_gate(row) for row in stream.gates)
# C872SRC 000576|    instruction_payload = tuple(
# C872SRC 000577|        serialize_bound_instruction(row) for row in stream.instructions
# C872SRC 000578|    )
# C872SRC 000579|    semantic_instruction_payload = tuple(
# C872SRC 000580|        {key: value for key, value in row.items() if key != "kind"}
# C872SRC 000581|        for row in instruction_payload
# C872SRC 000582|    )
# C872SRC 000583|    stage_factors = Counter(row["stage"] for row in stream.factor_manifest)
# C872SRC 000584|    stage_gates = Counter(
# C872SRC 000585|        stream.factor_manifest[row.factor_index]["stage"] for row in stream.gates
# C872SRC 000586|    )
# C872SRC 000587|    route_roles = Counter(row.role for row in stream.gates)
# C872SRC 000588|    return {
# C872SRC 000589|        "length": stream.length,
# C872SRC 000590|        "cells": stream.length ** 3,
# C872SRC 000591|        "native_rotations": len(stream.native_rotations),
# C872SRC 000592|        "native_factors": len(stream.native_factors),
# C872SRC 000593|        "augmented_seam_factors": stage_factors["seam"],
# C872SRC 000594|        "factor_stage_census": dict(stage_factors),
# C872SRC 000595|        "physical_gate_stage_census": dict(stage_gates),
# C872SRC 000596|        "unrouted_bound_instructions": len(stream.instructions),
# C872SRC 000597|        "physical_local_gates": len(stream.gates),
# C872SRC 000598|        "physical_gate_role_census": dict(route_roles),
# C872SRC 000599|        "matrix_registry_entries": len(stream.matrix_registry),
# C872SRC 000600|        "matrix_registry_sha256": sha256(canonical_json_bytes(
# C872SRC 000601|            dict(sorted(stream.matrix_registry.items()))
# C872SRC 000602|        )).hexdigest(),
# C872SRC 000603|        "factor_manifest_sha256": sha256(canonical_json_bytes(
# C872SRC 000604|            stream.factor_manifest
# C872SRC 000605|        )).hexdigest(),
# C872SRC 000606|        "instruction_binding_sha256": sha256(canonical_json_bytes(
# C872SRC 000607|            instruction_payload
# C872SRC 000608|        )).hexdigest(),
# C872SRC 000609|        "label_insensitive_instruction_binding_sha256": sha256(
# C872SRC 000610|            canonical_json_bytes(semantic_instruction_payload)
# C872SRC 000611|        ).hexdigest(),
# C872SRC 000612|        "instruction_label_scope": (
# C872SRC 000613|            "kind strings are diagnostic compiler labels; independent comparison "
# C872SRC 000614|            "uses the label-insensitive binding digest over factors, rotations, "
# C872SRC 000615|            "segments, sites, exact matrices, paths, and gate ranges"
# C872SRC 000616|        ),
# C872SRC 000617|        "normalized_physical_gate_sha256": sha256(canonical_json_bytes(
# C872SRC 000618|            gate_payload
# C872SRC 000619|        )).hexdigest(),
# C872SRC 000620|        "serialized_stream_sha256": sha256(payload_bytes).hexdigest(),
# C872SRC 000621|        "serialized_stream_bytes": len(payload_bytes),
# C872SRC 000622|        "construction_failure_census": stream.construction_failures,
# C872SRC 000623|        "first_forward_swap_deletion_detections": stream.deletion_detections,
# C872SRC 000624|        "deletion_control_scope": (
# C872SRC 000625|            "delete the first forward SWAP of every nontrivial returned route; "
# C872SRC 000626|            "not exhaustive over arbitrary SWAP positions"
# C872SRC 000627|        ),
# C872SRC 000628|        "native_factor_sha256": C870.factor_digest(stream.native_rotations),
# C872SRC 000629|        "factor_order": "exact Cycle870 serial factor order",
# C872SRC 000630|        "nonseam_route": "landed C707/C655 global-axis Manhattan returned route",
# C872SRC 000631|        "seam_route": "declared Cycle872 local-coframe returned replacement",
# C872SRC 000632|        "spectator_statement": (
# C872SRC 000633|            "identity label permutation with intended operands at every active gate; "
# C872SRC 000634|            "therefore exact on arbitrary dirty or entangled spectator states"
# C872SRC 000635|        ),
# C872SRC 000636|        "execution_scope": (
# C872SRC 000637|            "exact local gate matrices plus global serial composition/order; "
# C872SRC 000638|            "no global statevector or global matrix execution"
# C872SRC 000639|        ),
# C872SRC 000640|    }
# C872SRC 000641|
# C872SRC 000642|
# C872SRC 000643|def routed_macro_gate_payload(word, basis) -> tuple[dict[str, object], ...]:
# C872SRC 000644|    output = []
# C872SRC 000645|    for instruction_serial, instruction in enumerate(word):
# C872SRC 000646|        source_matrix = matrix_key(instruction.matrix)
# C872SRC 000647|        if len(instruction.sites) == 1:
# C872SRC 000648|            output.append({
# C872SRC 000649|                "instruction_serial": instruction_serial,
# C872SRC 000650|                "role": "active_one_site",
# C872SRC 000651|                "sites": instruction.sites,
# C872SRC 000652|                "matrix": source_matrix,
# C872SRC 000653|            })
# C872SRC 000654|            continue
# C872SRC 000655|        path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000656|        swap_matrix = matrix_key(C870.c707.c655.SWAP)
# C872SRC 000657|        for index in range(len(path) - 2):
# C872SRC 000658|            output.append({
# C872SRC 000659|                "instruction_serial": instruction_serial,
# C872SRC 000660|                "role": "swap_forward",
# C872SRC 000661|                "sites": (path[index], path[index + 1]),
# C872SRC 000662|                "matrix": swap_matrix,
# C872SRC 000663|            })
# C872SRC 000664|        output.append({
# C872SRC 000665|            "instruction_serial": instruction_serial,
# C872SRC 000666|            "role": "active_two_site",
# C872SRC 000667|            "sites": (path[-2], path[-1]),
# C872SRC 000668|            "matrix": source_matrix,
# C872SRC 000669|        })
# C872SRC 000670|        for index in reversed(range(len(path) - 2)):
# C872SRC 000671|            output.append({
# C872SRC 000672|                "instruction_serial": instruction_serial,
# C872SRC 000673|                "role": "swap_return",
# C872SRC 000674|                "sites": (path[index], path[index + 1]),
# C872SRC 000675|                "matrix": swap_matrix,
# C872SRC 000676|            })
# C872SRC 000677|    return tuple(output)
# C872SRC 000678|
# C872SRC 000679|
# C872SRC 000680|def physical_macro_mutation_certificate() -> dict[str, object]:
# C872SRC 000681|    """Digest actual coframe-routed canonical and damaged seam macros."""
# C872SRC 000682|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 000683|    context = C870.physical_context(graph)
# C872SRC 000684|    seams = C870.graph_seams(graph)
# C872SRC 000685|    canonical = []
# C872SRC 000686|    wrong_side = []
# C872SRC 000687|    seam_deleted = []
# C872SRC 000688|    for seam in seams:
# C872SRC 000689|        placement = C871.packet_placement(graph, context, seam)
# C872SRC 000690|        canonical.append(routed_macro_gate_payload(
# C872SRC 000691|            flatten(candidate_segments(graph, context, seam, placement)),
# C872SRC 000692|            placement.basis,
# C872SRC 000693|        ))
# C872SRC 000694|        wrong_side.append(routed_macro_gate_payload(
# C872SRC 000695|            flatten(candidate_segments(
# C872SRC 000696|                graph, context, seam, placement, wrong_side=True
# C872SRC 000697|            )),
# C872SRC 000698|            placement.basis,
# C872SRC 000699|        ))
# C872SRC 000700|        seam_deleted.append(routed_macro_gate_payload(
# C872SRC 000701|            flatten(candidate_segments(
# C872SRC 000702|                graph, context, seam, placement, delete_seam=True
# C872SRC 000703|            )),
# C872SRC 000704|            placement.basis,
# C872SRC 000705|        ))
# C872SRC 000706|    nn_failures = sum(
# C872SRC 000707|        len(gate["sites"]) == 2 and C870.c707.c655.l1(*gate["sites"]) != 1
# C872SRC 000708|        for family in (canonical, wrong_side, seam_deleted)
# C872SRC 000709|        for macro in family for gate in macro
# C872SRC 000710|    )
# C872SRC 000711|    return {
# C872SRC 000712|        "shape": (2, 2, 2),
# C872SRC 000713|        "seams": len(seams),
# C872SRC 000714|        "canonical_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000715|            tuple(canonical)
# C872SRC 000716|        )).hexdigest(),
# C872SRC 000717|        "wrong_side_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000718|            tuple(wrong_side)
# C872SRC 000719|        )).hexdigest(),
# C872SRC 000720|        "seam_deleted_routed_macro_sha256": sha256(canonical_json_bytes(
# C872SRC 000721|            tuple(seam_deleted)
# C872SRC 000722|        )).hexdigest(),
# C872SRC 000723|        "wrong_side_digest_detections": sum(
# C872SRC 000724|            left != right for left, right in zip(canonical, wrong_side)
# C872SRC 000725|        ),
# C872SRC 000726|        "seam_deletion_digest_detections": sum(
# C872SRC 000727|            left != right for left, right in zip(canonical, seam_deleted)
# C872SRC 000728|        ),
# C872SRC 000729|        "NN_failures": nn_failures,
# C872SRC 000730|        "semantic_supported_rows": "reported in spatial_direction",
# C872SRC 000731|    }
# C872SRC 000732|
# C872SRC 000733|
# C872SRC 000734|def route_word(word, basis):
# C872SRC 000735|    output = []
# C872SRC 000736|    deletion_detected = 0
# C872SRC 000737|    for instruction_index, instruction in enumerate(word):
# C872SRC 000738|        if len(instruction.sites) == 1:
# C872SRC 000739|            output.append(("ACTIVE:" + instruction.kind, instruction.sites, instruction_index))
# C872SRC 000740|            continue
# C872SRC 000741|        path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000742|        forward = [
# C872SRC 000743|            ("SWAP_FORWARD", (path[index], path[index + 1]), instruction_index)
# C872SRC 000744|            for index in range(len(path) - 2)
# C872SRC 000745|        ]
# C872SRC 000746|        active = [("ACTIVE:" + instruction.kind, (path[-2], path[-1]), instruction_index)]
# C872SRC 000747|        backward = [
# C872SRC 000748|            ("SWAP_RETURN", (path[index], path[index + 1]), instruction_index)
# C872SRC 000749|            for index in reversed(range(len(path) - 2))
# C872SRC 000750|        ]
# C872SRC 000751|        output.extend(forward + active + backward)
# C872SRC 000752|        if forward:
# C872SRC 000753|            labels = list(range(len(path)))
# C872SRC 000754|            # Delete the first forward SWAP but retain the gate and full return.
# C872SRC 000755|            for index in range(1, len(path) - 2):
# C872SRC 000756|                labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000757|            for index in reversed(range(len(path) - 2)):
# C872SRC 000758|                labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000759|            deletion_detected += labels != list(range(len(path)))
# C872SRC 000760|    return tuple(output), deletion_detected
# C872SRC 000761|
# C872SRC 000762|
# C872SRC 000763|def footprint(word, basis):
# C872SRC 000764|    output = set()
# C872SRC 000765|    for instruction in word:
# C872SRC 000766|        if len(instruction.sites) == 1:
# C872SRC 000767|            output.update(instruction.sites)
# C872SRC 000768|        else:
# C872SRC 000769|            output.update(C871.coframe_path(*instruction.sites, basis))
# C872SRC 000770|    return output
# C872SRC 000771|
# C872SRC 000772|
# C872SRC 000773|def returned_path_labels(path):
# C872SRC 000774|    labels = list(range(len(path)))
# C872SRC 000775|    for index in range(len(path) - 2):
# C872SRC 000776|        labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000777|    operands = tuple(labels[-2:])
# C872SRC 000778|    for index in reversed(range(len(path) - 2)):
# C872SRC 000779|        labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000780|    return operands, tuple(labels)
# C872SRC 000781|
# C872SRC 000782|
# C872SRC 000783|def schedule_order(seams):
# C872SRC 000784|    output = []
# C872SRC 000785|    for coarse in tuple(dict.fromkeys(map(coarse_color, seams))):
# C872SRC 000786|        members = tuple(seam for seam in seams if coarse_color(seam) == coarse)
# C872SRC 000787|        for fine in sorted(set(map(color, members))):
# C872SRC 000788|            output.extend(seam for seam in members if color(seam) == fine)
# C872SRC 000789|    return tuple(output)
# C872SRC 000790|
# C872SRC 000791|
# C872SRC 000792|def epoch_fixture(length: int):
# C872SRC 000793|    graph = C870.prep.OpenReferenceGraph(cells(length))
# C872SRC 000794|    context = C870.physical_context(graph)
# C872SRC 000795|    seams = C870.graph_seams(graph)
# C872SRC 000796|    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
# C872SRC 000797|    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
# C872SRC 000798|    resource_banks = tuple(resource_bank(placement) for placement in placements)
# C872SRC 000799|    blocked = set(context.sites) | J870.auxiliary_registers(graph)
# C872SRC 000800|    segments = tuple(
# C872SRC 000801|        candidate_segments(graph, context, seam, placement)
# C872SRC 000802|        for seam, placement in zip(seams, placements)
# C872SRC 000803|    )
# C872SRC 000804|    words = tuple(map(flatten, segments))
# C872SRC 000805|    used_packet_union = set().union(*(set(placement.sites) for placement in placements))
# C872SRC 000806|    used_resource_union = set().union(*resource_banks)
# C872SRC 000807|    packet_pair_overlaps = sum(
# C872SRC 000808|        bool(set(left.sites) & set(right.sites))
# C872SRC 000809|        for index, left in enumerate(placements) for right in placements[:index]
# C872SRC 000810|    )
# C872SRC 000811|    resource_pair_overlaps = sum(
# C872SRC 000812|        bool(left & right)
# C872SRC 000813|        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
# C872SRC 000814|    )
# C872SRC 000815|    spatial_geometry = {
# C872SRC 000816|        "duplicate_output_sites": len(spatial_sites) - len(set(spatial_sites)),
# C872SRC 000817|        "packet_aliases": sum(site in used_packet_union for site in spatial_sites),
# C872SRC 000818|        "native_aux_collisions": sum(site in blocked for site in spatial_sites),
# C872SRC 000819|    }
# C872SRC 000820|    routes = {}
# C872SRC 000821|    deletions = 0
# C872SRC 000822|    footprints = {}
# C872SRC 000823|    for seam, placement, word in zip(seams, placements, words):
# C872SRC 000824|        routes[seam], detected = route_word(word, placement.basis)
# C872SRC 000825|        deletions += detected
# C872SRC 000826|        footprints[seam] = footprint(word, placement.basis)
# C872SRC 000827|
# C872SRC 000828|    route_reconciliation = Counter()
# C872SRC 000829|    for placement, candidate in zip(placements, segments):
# C872SRC 000830|        for instruction in candidate["seam"]:
# C872SRC 000831|            if len(instruction.sites) != 2:
# C872SRC 000832|                continue
# C872SRC 000833|            replacement = C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 000834|            landed = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
# C872SRC 000835|            replacement_operands, replacement_return = returned_path_labels(replacement)
# C872SRC 000836|            landed_operands, landed_return = returned_path_labels(landed)
# C872SRC 000837|            route_reconciliation["retained_two_site_instructions"] += 1
# C872SRC 000838|            route_reconciliation["path_differences"] += replacement != landed
# C872SRC 000839|            route_reconciliation["endpoint_failures"] += (
# C872SRC 000840|                replacement[0] != landed[0]
# C872SRC 000841|                or replacement[-1] != landed[-1]
# C872SRC 000842|                or replacement[0] != instruction.sites[0]
# C872SRC 000843|                or replacement[-1] != instruction.sites[1]
# C872SRC 000844|            )
# C872SRC 000845|            route_reconciliation["replacement_operand_failures"] += (
# C872SRC 000846|                replacement_operands != (0, len(replacement) - 1)
# C872SRC 000847|            )
# C872SRC 000848|            route_reconciliation["landed_operand_failures"] += (
# C872SRC 000849|                landed_operands != (0, len(landed) - 1)
# C872SRC 000850|            )
# C872SRC 000851|            route_reconciliation["replacement_return_failures"] += (
# C872SRC 000852|                replacement_return != tuple(range(len(replacement)))
# C872SRC 000853|            )
# C872SRC 000854|            route_reconciliation["landed_return_failures"] += (
# C872SRC 000855|                landed_return != tuple(range(len(landed)))
# C872SRC 000856|            )
# C872SRC 000857|            route_reconciliation["replacement_routed_gates"] += 2 * len(replacement) - 3
# C872SRC 000858|            route_reconciliation["landed_routed_gates"] += 2 * len(landed) - 3
# C872SRC 000859|
# C872SRC 000860|    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 000861|    factors = tuple(
# C872SRC 000862|        (factor, tuple(group))
# C872SRC 000863|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 000864|    )
# C872SRC 000865|    actual_seams = tuple((factor, rows) for factor, rows in factors if factor[0] == "seam")
# C872SRC 000866|    binding_failures = Counter()
# C872SRC 000867|    physical_rows = {}
# C872SRC 000868|    logical_polys = {}
# C872SRC 000869|    packet_sites = {}
# C872SRC 000870|    endpoint_modes = {}
# C872SRC 000871|    for seam_index, (seam, placement, candidate) in enumerate(zip(seams, placements, segments)):
# C872SRC 000872|        expected = ("seam", seam_index, seam[0], seam[1], seam[2])
# C872SRC 000873|        selected = tuple(rows for factor, rows in actual_seams if factor == expected)
# C872SRC 000874|        binding_failures["selection"] += len(selected) != 1
# C872SRC 000875|        if len(selected) == 1:
# C872SRC 000876|            binding_failures["four_rotations"] += len(selected[0]) != 4
# C872SRC 000877|            actual_word = C871.compile_rotations(selected[0], context)
# C872SRC 000878|            binding_failures["compiled_word"] += (
# C872SRC 000879|                C871.word_sha256(actual_word) != C871.word_sha256(candidate["seam"])
# C872SRC 000880|            )
# C872SRC 000881|        cell, _axis, target, left_mode, right_mode = seam
# C872SRC 000882|        u = graph.vertex_index[(cell, left_mode)]
# C872SRC 000883|        v = graph.vertex_index[(target, right_mode)]
# C872SRC 000884|        logical = (
# C872SRC 000885|            graph.B(u), graph.B(v),
# C872SRC 000886|            *C870.seam_hop_rows(graph, cell, left_mode, target, right_mode),
# C872SRC 000887|        )
# C872SRC 000888|        physical_rows[seam] = tuple(C870.physical_lift(row, context) for row in logical)
# C872SRC 000889|        logical_polys[seam] = C870.fswap_polynomial(logical)
# C872SRC 000890|        packet_sites[seam] = resource_bank(placement)
# C872SRC 000891|        endpoint_modes[seam] = {(cell, left_mode), (target, right_mode)}
# C872SRC 000892|
# C872SRC 000893|    scheduled = schedule_order(seams)
# C872SRC 000894|    position = {seam: index for index, seam in enumerate(scheduled)}
# C872SRC 000895|    inversions = tuple(
# C872SRC 000896|        (left, right)
# C872SRC 000897|        for index, left in enumerate(seams) for right in seams[index + 1 :]
# C872SRC 000898|        if position[left] > position[right]
# C872SRC 000899|    )
# C872SRC 000900|    coarse_pairs = tuple(
# C872SRC 000901|        (left, right)
# C872SRC 000902|        for index, left in enumerate(seams) for right in seams[index + 1 :]
# C872SRC 000903|        if coarse_color(left) == coarse_color(right)
# C872SRC 000904|    )
# C872SRC 000905|    commute_failures = Counter()
# C872SRC 000906|    maximum_poly_residual = 0.0
# C872SRC 000907|    for left, right in coarse_pairs:
# C872SRC 000908|        commute_failures["endpoint_overlap"] += bool(endpoint_modes[left] & endpoint_modes[right])
# C872SRC 000909|        commute_failures["packet_overlap"] += bool(packet_sites[left] & packet_sites[right])
# C872SRC 000910|        commute_failures["physical_anticommutators"] += sum(
# C872SRC 000911|            not a.commutes(b) for a in physical_rows[left] for b in physical_rows[right]
# C872SRC 000912|        )
# C872SRC 000913|        residual = C870.poly_residual(
# C872SRC 000914|            C870.poly_mul(logical_polys[left], logical_polys[right]),
# C872SRC 000915|            C870.poly_mul(logical_polys[right], logical_polys[left]),
# C872SRC 000916|        )
# C872SRC 000917|        maximum_poly_residual = max(maximum_poly_residual, residual)
# C872SRC 000918|        commute_failures["polynomial"] += residual > C871.TOL
# C872SRC 000919|    commute_failures["inversion_outside_class"] = sum(
# C872SRC 000920|        coarse_color(left) != coarse_color(right) for left, right in inversions
# C872SRC 000921|    )
# C872SRC 000922|
# C872SRC 000923|    grouped = defaultdict(list)
# C872SRC 000924|    for seam in seams:
# C872SRC 000925|        grouped[color(seam)].append(seam)
# C872SRC 000926|    padding = same_layer_pairs = same_layer_collisions = footprint_collisions = 0
# C872SRC 000927|    fixed_depth = 0
# C872SRC 000928|    for members in grouped.values():
# C872SRC 000929|        depth = max(len(routes[seam]) for seam in members)
# C872SRC 000930|        fixed_depth += depth
# C872SRC 000931|        padded = {
# C872SRC 000932|            seam: routes[seam] + (None,) * (depth - len(routes[seam]))
# C872SRC 000933|            for seam in members
# C872SRC 000934|        }
# C872SRC 000935|        padding += sum(depth - len(routes[seam]) for seam in members)
# C872SRC 000936|        for index, left in enumerate(members):
# C872SRC 000937|            footprint_collisions += sum(
# C872SRC 000938|                bool(footprints[left] & footprints[right]) for right in members[:index]
# C872SRC 000939|            )
# C872SRC 000940|        for layer in range(depth):
# C872SRC 000941|            active = [padded[seam][layer] for seam in members if padded[seam][layer] is not None]
# C872SRC 000942|            for index, gate in enumerate(active):
# C872SRC 000943|                for prior in active[:index]:
# C872SRC 000944|                    same_layer_pairs += 1
# C872SRC 000945|                    same_layer_collisions += bool(set(gate[1]) & set(prior[1]))
# C872SRC 000946|
# C872SRC 000947|    bank_at = {}
# C872SRC 000948|    for bank_index, bank in enumerate(resource_banks):
# C872SRC 000949|        for site in bank:
# C872SRC 000950|            bank_at[site] = bank_index
# C872SRC 000951|    dirty = Counter()
# C872SRC 000952|    macro_bank_pairs = set()
# C872SRC 000953|    for macro_index, (seam, placement, word) in enumerate(zip(seams, placements, words)):
# C872SRC 000954|        for instruction in word:
# C872SRC 000955|            if len(instruction.sites) != 2:
# C872SRC 000956|                continue
# C872SRC 000957|            path = C871.coframe_path(*instruction.sites, placement.basis)
# C872SRC 000958|            labels = list(range(len(path)))
# C872SRC 000959|            for index in range(len(path) - 2):
# C872SRC 000960|                labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000961|            dirty["operand_failures"] += labels[-2:] != [0, len(path) - 1]
# C872SRC 000962|            for index in reversed(range(len(path) - 2)):
# C872SRC 000963|                labels[index], labels[index + 1] = labels[index + 1], labels[index]
# C872SRC 000964|            dirty["path_return_failures"] += labels != list(range(len(path)))
# C872SRC 000965|            for path_index, site in enumerate(path):
# C872SRC 000966|                other = bank_at.get(site)
# C872SRC 000967|                if other is None or other == macro_index:
# C872SRC 000968|                    continue
# C872SRC 000969|                macro_bank_pairs.add((macro_index, other))
# C872SRC 000970|                dirty["site_incidences"] += 1
