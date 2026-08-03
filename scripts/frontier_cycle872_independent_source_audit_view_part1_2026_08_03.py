#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 independent source, part 1/2."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 2
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 532
TOTAL_SOURCE_LINES = 1064
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "2350243e16aeb39a6a0f20b9a036468c82e541477e206566664c1103fa145523"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 000001|#!/usr/bin/env python3
# C872SRC 000002|"""Independent Cycle 872 checker.
# C872SRC 000003|
# C872SRC 000004|This file does not import the primary runner.  It reconstructs every macro
# C872SRC 000005|from the actual Cycle870 factor inventory and checks a compact independent
# C872SRC 000006|acceptance surface with alternative enumeration code.
# C872SRC 000007|"""
# C872SRC 000008|
# C872SRC 000009|from __future__ import annotations
# C872SRC 000010|
# C872SRC 000011|import argparse
# C872SRC 000012|import ast
# C872SRC 000013|from collections import Counter, defaultdict
# C872SRC 000014|from hashlib import sha256
# C872SRC 000015|from itertools import groupby, product
# C872SRC 000016|import json
# C872SRC 000017|import math
# C872SRC 000018|import os
# C872SRC 000019|from pathlib import Path
# C872SRC 000020|import sys
# C872SRC 000021|
# C872SRC 000022|import numpy as np
# C872SRC 000023|
# C872SRC 000024|
# C872SRC 000025|PACKAGE_ROOT = Path(__file__).resolve().parents[1]
# C872SRC 000026|
# C872SRC 000027|
# C872SRC 000028|def discover_source_root():
# C872SRC 000029|    supplied = os.environ.get("CYCLE872_SOURCE_ROOT")
# C872SRC 000030|    candidates = [Path(supplied)] if supplied else []
# C872SRC 000031|    for start in (Path.cwd(), PACKAGE_ROOT):
# C872SRC 000032|        candidates.extend((start, *start.parents))
# C872SRC 000033|    marker = "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
# C872SRC 000034|    for candidate in candidates:
# C872SRC 000035|        resolved = candidate.resolve()
# C872SRC 000036|        if (resolved / marker).is_file():
# C872SRC 000037|            return resolved
# C872SRC 000038|    raise RuntimeError(
# C872SRC 000039|        "Cycle872 upstream repository not found; run from its root or set "
# C872SRC 000040|        "CYCLE872_SOURCE_ROOT"
# C872SRC 000041|    )
# C872SRC 000042|
# C872SRC 000043|
# C872SRC 000044|SOURCE_ROOT = discover_source_root()
# C872SRC 000045|sys.path.insert(0, str(SOURCE_ROOT / "scripts"))
# C872SRC 000046|
# C872SRC 000047|import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
# C872SRC 000048|import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
# C872SRC 000049|import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
# C872SRC 000050|import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
# C872SRC 000051|import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
# C872SRC 000052|
# C872SRC 000053|
# C872SRC 000054|PRIMARY_MODULE = "frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03"
# C872SRC 000055|NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
# C872SRC 000056|DEFAULT_RECEIPT = PACKAGE_ROOT / "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json"
# C872SRC 000057|EXPECTED_NOTE_SHA256 = "dd218e18d3a24506b11db9fdbad909f899187eeda5bf579a2b1a984afd10c8f7"
# C872SRC 000058|EXPECTED_INPUT_SHA256 = {
# C872SRC 000059|    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
# C872SRC 000060|    "scripts/active_cubic_source_response_cycle211_2026_07_16.py": "d5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6",
# C872SRC 000061|    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py": "a5e78e40cad0c43ee62ae887df7d84a0b895ab217ba4f3d521353e5d0b6bf95a",
# C872SRC 000062|    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py": "464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4",
# C872SRC 000063|    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
# C872SRC 000064|    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py": "3a977106389428d2281ea7e0e32b65fe57f6ce33d783742b80f264f78f4f2c17",
# C872SRC 000065|    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py": "fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7",
# C872SRC 000066|    "scripts/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.py": "2d9618ab1c50448f4bd611826c3f265bb8985878a5d76d01d3b78d793d3635d0",
# C872SRC 000067|    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py": "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
# C872SRC 000068|    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py": "781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e",
# C872SRC 000069|    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
# C872SRC 000070|    "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py": "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
# C872SRC 000071|    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py": "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a",
# C872SRC 000072|    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py": "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
# C872SRC 000073|    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py": "b42ea07c1ed671b9cbab38bc38eba6f8166fe65be52295941a95e3ed75049abf",
# C872SRC 000074|    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py": "f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3",
# C872SRC 000075|    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py": "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
# C872SRC 000076|    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py": "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
# C872SRC 000077|    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py": "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
# C872SRC 000078|    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py": "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
# C872SRC 000079|    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py": "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
# C872SRC 000080|    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py": "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
# C872SRC 000081|    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
# C872SRC 000082|    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py": "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
# C872SRC 000083|    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py": "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
# C872SRC 000084|    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py": "94f0fbd1212e210d0e073c3a80cdc2f92afa3c9807f981bd220625a67e8d94a0",
# C872SRC 000085|    "scripts/frontier_full128_code_projectors_2026_07_24.py": "f561714d036c8c7568b1772110303d6c0da11c6d73c9df3bdcbae2db632f5b44",
# C872SRC 000086|    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py": "ecae9048b4ee2d257315072cb7120335109f362fa7007573c46a82a1f0ed4195",
# C872SRC 000087|    "scripts/frontier_full128_cycle_encoder_2026_07_24.py": "17eca725b72943d8804147dd800be044ffaa80dc209588adb37ae6543d0fa935",
# C872SRC 000088|    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py": "b446ace0856b45108ae0ed4ed35614961ae3b69bf20d12132981f54809966afb",
# C872SRC 000089|    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py": "05cb2f6083cf6c4307c04284632e991b7fd7378cbd2a4eb08a52d5e3c7ae6b99",
# C872SRC 000090|    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py": "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
# C872SRC 000091|    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py": "4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6",
# C872SRC 000092|    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py": "97fdf54189d7da93099aeab4a9b1dd8501c7262d55493b9fa95bf1c2f5c97a9d",
# C872SRC 000093|    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py": "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8",
# C872SRC 000094|    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py": "67aa2435d66fb34b6734cc564a82ac839525139fdc9e8c347dc1b2277d08b40b",
# C872SRC 000095|    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py": "ef6805e691a1ddd303a96f7cabd7000517e0cf33d5b1c577b20c2cbbf29aca23",
# C872SRC 000096|    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py": "4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6",
# C872SRC 000097|    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
# C872SRC 000098|    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py": "a9786cf68a9c669e7e7fe310a00ab9912aa404689651682ccfe3045a06e357f1",
# C872SRC 000099|    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py": "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b",
# C872SRC 000100|    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py": "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
# C872SRC 000101|    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py": "472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86",
# C872SRC 000102|    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
# C872SRC 000103|    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py": "9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011",
# C872SRC 000104|}
# C872SRC 000105|EXPECTED_FIXTURES = {
# C872SRC 000106|    2: {
# C872SRC 000107|        "cells": 8, "seams": 12, "rotations": 1392, "factors": 324,
# C872SRC 000108|        "instructions": 10920, "schedule_depth": 74912,
# C872SRC 000109|        "six_collisions": 12, "fine_collisions": 0,
# C872SRC 000110|        "packet_union": 708, "resource_union": 720,
# C872SRC 000111|        "route_differences": 540, "dirty_pairs": 46,
# C872SRC 000112|    },
# C872SRC 000113|    3: {
# C872SRC 000114|        "cells": 27, "seams": 54, "rotations": 4752, "factors": 1107,
# C872SRC 000115|        "instructions": 49644, "schedule_depth": 173040,
# C872SRC 000116|        "six_collisions": 72, "fine_collisions": 0,
# C872SRC 000117|        "packet_union": 3186, "resource_union": 3240,
# C872SRC 000118|        "route_differences": 2752, "dirty_pairs": 281,
# C872SRC 000119|    },
# C872SRC 000120|    4: {
# C872SRC 000121|        "cells": 64, "seams": 144, "schedule_depth": 184848,
# C872SRC 000122|        "six_collisions": 216, "fine_collisions": 0,
# C872SRC 000123|        "packet_union": 8496, "resource_union": 8640,
# C872SRC 000124|    },
# C872SRC 000125|    5: {
# C872SRC 000126|        "cells": 125, "seams": 300, "schedule_depth": 186816,
# C872SRC 000127|        "six_collisions": 480, "fine_collisions": 0,
# C872SRC 000128|        "packet_union": 17700, "resource_union": 18000,
# C872SRC 000129|    },
# C872SRC 000130|}
# C872SRC 000131|EXPECTED_PHYSICAL_STREAM = {
# C872SRC 000132|    "length": 2,
# C872SRC 000133|    "native_rotations": 1392,
# C872SRC 000134|    "native_factors": 324,
# C872SRC 000135|    "unrouted_bound_instructions": 26768,
# C872SRC 000136|    "physical_local_gates": 220920,
# C872SRC 000137|    "matrix_registry_entries": 77,
# C872SRC 000138|    "first_forward_swap_deletion_detections": 18440,
# C872SRC 000139|    "factor_manifest_sha256": "653f27706716823d46d8c9395aed8cd55ab4c1750bf8ee12285fcd85771b2878",
# C872SRC 000140|    "label_insensitive_instruction_binding_sha256": "c03fbd9503bcfda2cabb319f48ccb83d93db9b53f8c5aa7dd51859bdc1fff629",
# C872SRC 000141|    "normalized_physical_gate_sha256": "a178a1f221afd8fe8ad8aacac1cd61024f94c11eb5fe58eb75defa4d674e97b1",
# C872SRC 000142|    "matrix_registry_sha256": "e2f7cf72a9bb1288db9f3d89f4677d4f77625cc23c4f6790c22cb268cfebf091",
# C872SRC 000143|}
# C872SRC 000144|SPATIAL_CURRENT_LOCAL = (0, 0, 3)
# C872SRC 000145|
# C872SRC 000146|
# C872SRC 000147|def sha(path: Path) -> str:
# C872SRC 000148|    return sha256(path.read_bytes()).hexdigest()
# C872SRC 000149|
# C872SRC 000150|
# C872SRC 000151|def cells(length):
# C872SRC 000152|    return tuple(product(range(length), repeat=3))
# C872SRC 000153|
# C872SRC 000154|
# C872SRC 000155|def fine(seam):
# C872SRC 000156|    owner, axis = seam[0], seam[1]
# C872SRC 000157|    return (
# C872SRC 000158|        axis, owner[axis] & 1,
# C872SRC 000159|        *(owner[index] & 1 for index in range(3) if index != axis),
# C872SRC 000160|    )
# C872SRC 000161|
# C872SRC 000162|
# C872SRC 000163|def coarse(seam):
# C872SRC 000164|    return seam[1], seam[0][seam[1]] & 1
# C872SRC 000165|
# C872SRC 000166|
# C872SRC 000167|def spatial_current_site(placement):
# C872SRC 000168|    site = placement.midpoint
# C872SRC 000169|    for coefficient, direction in zip(SPATIAL_CURRENT_LOCAL, placement.basis):
# C872SRC 000170|        site = tuple(
# C872SRC 000171|            site[index] + coefficient * direction[index] for index in range(3)
# C872SRC 000172|        )
# C872SRC 000173|    return site
# C872SRC 000174|
# C872SRC 000175|
# C872SRC 000176|def resource_bank(placement):
# C872SRC 000177|    return frozenset((*placement.sites, spatial_current_site(placement)))
# C872SRC 000178|
# C872SRC 000179|
# C872SRC 000180|def independent_import_certificate():
# C872SRC 000181|    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
# C872SRC 000182|    imported = []
# C872SRC 000183|    for node in ast.walk(tree):
# C872SRC 000184|        if isinstance(node, ast.Import):
# C872SRC 000185|            imported.extend(alias.name for alias in node.names)
# C872SRC 000186|        elif isinstance(node, ast.ImportFrom) and node.module:
# C872SRC 000187|            imported.append(node.module)
# C872SRC 000188|    return {
# C872SRC 000189|        "imported_modules": tuple(sorted(imported)),
# C872SRC 000190|        "primary_imported": any(PRIMARY_MODULE in row for row in imported),
# C872SRC 000191|    }
# C872SRC 000192|
# C872SRC 000193|
# C872SRC 000194|def provenance():
# C872SRC 000195|    observed = {label: sha(SOURCE_ROOT / label) for label in EXPECTED_INPUT_SHA256}
# C872SRC 000196|    return {
# C872SRC 000197|        "input_sha256": observed,
# C872SRC 000198|        "literal_dependency_pin_count": len(EXPECTED_INPUT_SHA256),
# C872SRC 000199|        "dependency_surface": (
# C872SRC 000200|            "complete local Python import closure plus dynamically loaded Cycle870 "
# C872SRC 000201|            "placement and Cycle610/611 modules"
# C872SRC 000202|        ),
# C872SRC 000203|        "pin_failures": {
# C872SRC 000204|            label: (expected, observed[label])
# C872SRC 000205|            for label, expected in EXPECTED_INPUT_SHA256.items()
# C872SRC 000206|            if observed[label] != expected
# C872SRC 000207|        },
# C872SRC 000208|        "note_sha256": sha(PACKAGE_ROOT / NOTE),
# C872SRC 000209|        "note_pin_failure": sha(PACKAGE_ROOT / NOTE) != EXPECTED_NOTE_SHA256,
# C872SRC 000210|        "checker_sha256": sha(Path(__file__)),
# C872SRC 000211|    }
# C872SRC 000212|
# C872SRC 000213|
# C872SRC 000214|def independent_segments(
# C872SRC 000215|    graph, context, seam, placement, actual_rows, *, wrong_side=False,
# C872SRC 000216|    delete_seam=False,
# C872SRC 000217|):
# C872SRC 000218|    cell, _axis, target, left_mode, right_mode = seam
# C872SRC 000219|    left = C871.physical_b(graph, context, cell, left_mode)
# C872SRC 000220|    right = C871.physical_b(graph, context, target, right_mode)
# C872SRC 000221|    du = placement.sites[C714.MCX_WORK[0]]
# C872SRC 000222|    dv = placement.sites[C714.MCX_WORK[1]]
# C872SRC 000223|    pointer = placement.sites[C714.POINTER]
# C872SRC 000224|    spatial = spatial_current_site(placement)
# C872SRC 000225|    pre = C871.extract_b(left, context, du, "check_pre_l") + C871.extract_b(
# C872SRC 000226|        right, context, dv, "check_pre_r"
# C872SRC 000227|    )
# C872SRC 000228|    seam_word = C871.compile_rotations(actual_rows, context)
# C872SRC 000229|    if delete_seam:
# C872SRC 000230|        seam_word = ()
# C872SRC 000231|    post = C871.extract_b(left, context, du, "check_post_l") + C871.extract_b(
# C872SRC 000232|        right, context, dv, "check_post_r"
# C872SRC 000233|    )
# C872SRC 000234|    endpoint_or = (
# C872SRC 000235|        C871.cnot(du, pointer, "check_or"), C871.cnot(dv, pointer, "check_or")
# C872SRC 000236|    ) + C871.toffoli_word(du, dv, pointer, "check_or_tof_")
# C872SRC 000237|    clean = (
# C872SRC 000238|        C871.extract_b(left, context, du, "check_clean_l")
# C872SRC 000239|        + C871.extract_b(right, context, du, "check_clean_r")
# C872SRC 000240|        + C871.extract_b(left, context, dv, "check_clean_l")
# C872SRC 000241|        + C871.extract_b(right, context, dv, "check_clean_r")
# C872SRC 000242|    )
# C872SRC 000243|    direction_b = left if wrong_side else right
# C872SRC 000244|    direction = (
# C872SRC 000245|        C871.extract_b(direction_b, context, du, "check_direction_load")
# C872SRC 000246|        + C871.toffoli_word(pointer, du, spatial, "check_direction_tof_")
# C872SRC 000247|        + C871.extract_b(direction_b, context, du, "check_direction_unload")
# C872SRC 000248|    )
# C872SRC 000249|    return {
# C872SRC 000250|        "pre": pre,
# C872SRC 000251|        "seam": seam_word,
# C872SRC 000252|        "post": post,
# C872SRC 000253|        "or": endpoint_or,
# C872SRC 000254|        "clean": clean,
# C872SRC 000255|        "spatial_direction_write": direction,
# C872SRC 000256|        "packet": C871.packet_word(placement),
# C872SRC 000257|    }
# C872SRC 000258|
# C872SRC 000259|
# C872SRC 000260|def independent_macro(graph, context, seam, placement, actual_rows):
# C872SRC 000261|    segments = independent_segments(graph, context, seam, placement, actual_rows)
# C872SRC 000262|    return tuple(
# C872SRC 000263|        instruction for word in segments.values() for instruction in word
# C872SRC 000264|    ), segments["seam"]
# C872SRC 000265|
# C872SRC 000266|
# C872SRC 000267|def canonical_json_bytes(value):
# C872SRC 000268|    return (
# C872SRC 000269|        json.dumps(value, sort_keys=True, separators=(",", ":"), default=float)
# C872SRC 000270|        + "\n"
# C872SRC 000271|    ).encode()
# C872SRC 000272|
# C872SRC 000273|
# C872SRC 000274|def matrix_payload(matrix):
# C872SRC 000275|    array = np.asarray(matrix, dtype=complex)
# C872SRC 000276|    return {
# C872SRC 000277|        "shape": tuple(map(int, array.shape)),
# C872SRC 000278|        "row_major_complex_float_hex": tuple(
# C872SRC 000279|            (float(value.real).hex(), float(value.imag).hex())
# C872SRC 000280|            for value in array.reshape(-1)
# C872SRC 000281|        ),
# C872SRC 000282|        "cycle655_rounded_matrix_sha256": C870.c707.c655.matrix_digest(array),
# C872SRC 000283|    }
# C872SRC 000284|
# C872SRC 000285|
# C872SRC 000286|def matrix_key(matrix):
# C872SRC 000287|    return sha256(canonical_json_bytes(matrix_payload(matrix))).hexdigest()
# C872SRC 000288|
# C872SRC 000289|
# C872SRC 000290|def independent_physical_stream_check():
# C872SRC 000291|    """Reconstruct the L2 full factor/stage/routed-gate ledger independently."""
# C872SRC 000292|    graph = C870.prep.OpenReferenceGraph(cells(2))
# C872SRC 000293|    context = C870.physical_context(graph)
# C872SRC 000294|    seams = C870.graph_seams(graph)
# C872SRC 000295|    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
# C872SRC 000296|    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 000297|    factors = tuple(
# C872SRC 000298|        (tuple(factor), tuple(group))
# C872SRC 000299|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 000300|    )
# C872SRC 000301|    seam_lookup = {
# C872SRC 000302|        ("seam", index, seam[0], seam[1], seam[2]): (seam, placements[index])
# C872SRC 000303|        for index, seam in enumerate(seams)
# C872SRC 000304|    }
# C872SRC 000305|    failures = Counter()
# C872SRC 000306|    registry = {}
# C872SRC 000307|    instructions = []
# C872SRC 000308|    gates = []
# C872SRC 000309|    factor_manifest = []
# C872SRC 000310|    deletion_detections = 0
# C872SRC 000311|
# C872SRC 000312|    def register(matrix):
# C872SRC 000313|        key = matrix_key(matrix)
# C872SRC 000314|        payload = matrix_payload(matrix)
# C872SRC 000315|        failures["matrix_digest_collision"] += key in registry and registry[key] != payload
# C872SRC 000316|        registry[key] = payload
# C872SRC 000317|        return key
# C872SRC 000318|
# C872SRC 000319|    def emit(factor_index, factor, stage, segment, rotation_serial,
# C872SRC 000320|             instruction, route_policy, basis):
# C872SRC 000321|        nonlocal deletion_detections
# C872SRC 000322|        serial = len(instructions)
# C872SRC 000323|        if len(instruction.sites) == 1:
# C872SRC 000324|            path = tuple(instruction.sites)
# C872SRC 000325|        elif route_policy == "landed_global_axis_manhattan_returned":
# C872SRC 000326|            path = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
# C872SRC 000327|        else:
# C872SRC 000328|            path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000329|        failures["arity"] += len(instruction.sites) not in (1, 2)
# C872SRC 000330|        failures["endpoints"] += (
# C872SRC 000331|            not path
# C872SRC 000332|            or path[0] != instruction.sites[0]
# C872SRC 000333|            or path[-1] != instruction.sites[-1]
# C872SRC 000334|        )
# C872SRC 000335|        gate_start = len(gates)
# C872SRC 000336|        source_matrix = register(instruction.matrix)
# C872SRC 000337|        if len(instruction.sites) == 1:
# C872SRC 000338|            gates.append({
# C872SRC 000339|                "serial": len(gates), "factor_index": factor_index,
# C872SRC 000340|                "instruction_serial": serial, "role": "active_one_site",
# C872SRC 000341|                "sites": instruction.sites, "matrix": source_matrix,
# C872SRC 000342|            })
# C872SRC 000343|        else:
# C872SRC 000344|            labels = list(path)
# C872SRC 000345|            swap_matrix = register(C870.c707.c655.SWAP)
# C872SRC 000346|            for route_index in range(len(path) - 2):
# C872SRC 000347|                sites = (path[route_index], path[route_index + 1])
# C872SRC 000348|                gates.append({
# C872SRC 000349|                    "serial": len(gates), "factor_index": factor_index,
# C872SRC 000350|                    "instruction_serial": serial, "role": "swap_forward",
# C872SRC 000351|                    "sites": sites, "matrix": swap_matrix,
# C872SRC 000352|                })
# C872SRC 000353|                labels[route_index], labels[route_index + 1] = (
# C872SRC 000354|                    labels[route_index + 1], labels[route_index]
# C872SRC 000355|                )
# C872SRC 000356|            failures["operands"] += tuple(labels[-2:]) != instruction.sites
# C872SRC 000357|            gates.append({
# C872SRC 000358|                "serial": len(gates), "factor_index": factor_index,
# C872SRC 000359|                "instruction_serial": serial, "role": "active_two_site",
# C872SRC 000360|                "sites": (path[-2], path[-1]), "matrix": source_matrix,
# C872SRC 000361|            })
# C872SRC 000362|            for route_index in reversed(range(len(path) - 2)):
# C872SRC 000363|                sites = (path[route_index], path[route_index + 1])
# C872SRC 000364|                gates.append({
# C872SRC 000365|                    "serial": len(gates), "factor_index": factor_index,
# C872SRC 000366|                    "instruction_serial": serial, "role": "swap_return",
# C872SRC 000367|                    "sites": sites, "matrix": swap_matrix,
# C872SRC 000368|                })
# C872SRC 000369|                labels[route_index], labels[route_index + 1] = (
# C872SRC 000370|                    labels[route_index + 1], labels[route_index]
# C872SRC 000371|                )
# C872SRC 000372|            failures["spectator_return"] += labels != list(path)
# C872SRC 000373|            if len(path) > 2:
# C872SRC 000374|                damaged = list(path)
# C872SRC 000375|                for route_index in range(1, len(path) - 2):
# C872SRC 000376|                    damaged[route_index], damaged[route_index + 1] = (
# C872SRC 000377|                        damaged[route_index + 1], damaged[route_index]
# C872SRC 000378|                    )
# C872SRC 000379|                for route_index in reversed(range(len(path) - 2)):
# C872SRC 000380|                    damaged[route_index], damaged[route_index + 1] = (
# C872SRC 000381|                        damaged[route_index + 1], damaged[route_index]
# C872SRC 000382|                    )
# C872SRC 000383|                deletion_detections += damaged != list(path)
# C872SRC 000384|        gate_stop = len(gates)
# C872SRC 000385|        failures["NN"] += sum(
# C872SRC 000386|            len(row["sites"]) == 2 and C870.c707.c655.l1(*row["sites"]) != 1
# C872SRC 000387|            for row in gates[gate_start:gate_stop]
# C872SRC 000388|        )
# C872SRC 000389|        failures["one_active"] += sum(
# C872SRC 000390|            row["role"].startswith("active") for row in gates[gate_start:gate_stop]
# C872SRC 000391|        ) != 1
# C872SRC 000392|        instructions.append({
# C872SRC 000393|            "serial": serial,
# C872SRC 000394|            "factor_index": factor_index,
# C872SRC 000395|            "factor": factor,
# C872SRC 000396|            "stage": stage,
# C872SRC 000397|            "segment": segment,
# C872SRC 000398|            "rotation_serial": rotation_serial,
# C872SRC 000399|            "kind": instruction.kind,
# C872SRC 000400|            "unrouted_sites": instruction.sites,
# C872SRC 000401|            "unrouted_matrix": source_matrix,
# C872SRC 000402|            "route_policy": route_policy,
# C872SRC 000403|            "path": path,
# C872SRC 000404|            "gate_serial_start": gate_start,
# C872SRC 000405|            "gate_serial_stop_exclusive": gate_stop,
# C872SRC 000406|        })
# C872SRC 000407|
# C872SRC 000408|    for factor_index, (factor, factor_rotations) in enumerate(factors):
# C872SRC 000409|        stage = str(factor[0])
# C872SRC 000410|        instruction_start = len(instructions)
# C872SRC 000411|        gate_start = len(gates)
# C872SRC 000412|        route_policy = (
# C872SRC 000413|            "augmented_seam_local_coframe_returned"
# C872SRC 000414|            if stage == "seam" else "landed_global_axis_manhattan_returned"
# C872SRC 000415|        )
# C872SRC 000416|        if stage == "seam":
# C872SRC 000417|            seam, placement = seam_lookup[factor]
# C872SRC 000418|            segments = independent_segments(
# C872SRC 000419|                graph, context, seam, placement, factor_rotations
# C872SRC 000420|            )
# C872SRC 000421|            for segment, word in segments.items():
# C872SRC 000422|                if segment == "seam":
# C872SRC 000423|                    actual = []
# C872SRC 000424|                    for rotation in factor_rotations:
# C872SRC 000425|                        rotation_word = C870.c707.compile_pauli_rotation(
# C872SRC 000426|                            C870.physical_lift(rotation.row, context),
# C872SRC 000427|                            context.sites, rotation.angle,
# C872SRC 000428|                        )
# C872SRC 000429|                        actual.extend(rotation_word)
# C872SRC 000430|                        for instruction in rotation_word:
# C872SRC 000431|                            emit(
# C872SRC 000432|                                factor_index, factor, stage, segment, rotation.serial,
# C872SRC 000433|                                instruction, route_policy, placement.basis,
# C872SRC 000434|                            )
# C872SRC 000435|                    failures["seam_word"] += (
# C872SRC 000436|                        C871.word_sha256(tuple(actual)) != C871.word_sha256(word)
# C872SRC 000437|                    )
# C872SRC 000438|                else:
# C872SRC 000439|                    for instruction in word:
# C872SRC 000440|                        emit(
# C872SRC 000441|                            factor_index, factor, stage, segment, None,
# C872SRC 000442|                            instruction, route_policy, placement.basis,
# C872SRC 000443|                        )
# C872SRC 000444|        else:
# C872SRC 000445|            for rotation in factor_rotations:
# C872SRC 000446|                for instruction in C870.c707.compile_pauli_rotation(
# C872SRC 000447|                    C870.physical_lift(rotation.row, context),
# C872SRC 000448|                    context.sites, rotation.angle,
# C872SRC 000449|                ):
# C872SRC 000450|                    emit(
# C872SRC 000451|                        factor_index, factor, stage, "landed_factor", rotation.serial,
# C872SRC 000452|                        instruction, route_policy, None,
# C872SRC 000453|                    )
# C872SRC 000454|        factor_manifest.append({
# C872SRC 000455|            "factor_index": factor_index,
# C872SRC 000456|            "factor": factor,
# C872SRC 000457|            "stage": stage,
# C872SRC 000458|            "native_rotation_serials": tuple(row.serial for row in factor_rotations),
# C872SRC 000459|            "replacement": "augmented_seam_macro" if stage == "seam" else "identity",
# C872SRC 000460|            "route_policy": route_policy,
# C872SRC 000461|            "instruction_serial_start": instruction_start,
# C872SRC 000462|            "instruction_serial_stop_exclusive": len(instructions),
# C872SRC 000463|            "physical_gate_serial_start": gate_start,
# C872SRC 000464|            "physical_gate_serial_stop_exclusive": len(gates),
# C872SRC 000465|        })
# C872SRC 000466|
# C872SRC 000467|    failures["factor_sequence"] += tuple(
# C872SRC 000468|        row["factor"] for row in factor_manifest
# C872SRC 000469|    ) != tuple(factor for factor, _rows in factors)
# C872SRC 000470|    failures["rotation_coverage"] += tuple(
# C872SRC 000471|        serial for row in factor_manifest for serial in row["native_rotation_serials"]
# C872SRC 000472|    ) != tuple(row.serial for row in rotations)
# C872SRC 000473|    failures["gate_serial"] += any(
# C872SRC 000474|        row["serial"] != index for index, row in enumerate(gates)
# C872SRC 000475|    )
# C872SRC 000476|    failures["stage_order"] += tuple(dict.fromkeys(
# C872SRC 000477|        row["stage"] for row in factor_manifest
# C872SRC 000478|    )) != ("coin", "reverse", "seam", "contact")
# C872SRC 000479|    gate_stages = Counter(
# C872SRC 000480|        factor_manifest[row["factor_index"]]["stage"] for row in gates
# C872SRC 000481|    )
# C872SRC 000482|    result = {
# C872SRC 000483|        "length": 2,
# C872SRC 000484|        "native_rotations": len(rotations),
# C872SRC 000485|        "native_factors": len(factors),
# C872SRC 000486|        "unrouted_bound_instructions": len(instructions),
# C872SRC 000487|        "physical_local_gates": len(gates),
# C872SRC 000488|        "matrix_registry_entries": len(registry),
# C872SRC 000489|        "first_forward_swap_deletion_detections": deletion_detections,
# C872SRC 000490|        "deletion_control_scope": (
# C872SRC 000491|            "delete the first forward SWAP of every nontrivial returned route; "
# C872SRC 000492|            "not exhaustive over arbitrary SWAP positions"
# C872SRC 000493|        ),
# C872SRC 000494|        "factor_stage_census": dict(Counter(row["stage"] for row in factor_manifest)),
# C872SRC 000495|        "physical_gate_stage_census": dict(gate_stages),
# C872SRC 000496|        "factor_manifest_sha256": sha256(canonical_json_bytes(
# C872SRC 000497|            tuple(factor_manifest)
# C872SRC 000498|        )).hexdigest(),
# C872SRC 000499|        "instruction_binding_sha256": sha256(canonical_json_bytes(
# C872SRC 000500|            tuple(instructions)
# C872SRC 000501|        )).hexdigest(),
# C872SRC 000502|        "label_insensitive_instruction_binding_sha256": sha256(
# C872SRC 000503|            canonical_json_bytes(tuple(
# C872SRC 000504|                {key: value for key, value in row.items() if key != "kind"}
# C872SRC 000505|                for row in instructions
# C872SRC 000506|            ))
# C872SRC 000507|        ).hexdigest(),
# C872SRC 000508|        "instruction_label_scope": (
# C872SRC 000509|            "compiler kind strings intentionally excluded; all semantic binding fields retained"
# C872SRC 000510|        ),
# C872SRC 000511|        "normalized_physical_gate_sha256": sha256(canonical_json_bytes(
# C872SRC 000512|            tuple(gates)
# C872SRC 000513|        )).hexdigest(),
# C872SRC 000514|        "matrix_registry_sha256": sha256(canonical_json_bytes(
# C872SRC 000515|            dict(sorted(registry.items()))
# C872SRC 000516|        )).hexdigest(),
# C872SRC 000517|        "native_factor_sha256": C870.factor_digest(rotations),
# C872SRC 000518|        "failure_census": dict(failures),
# C872SRC 000519|    }
# C872SRC 000520|    result["expected_mismatches"] = {
# C872SRC 000521|        key: (expected, result.get(key))
# C872SRC 000522|        for key, expected in EXPECTED_PHYSICAL_STREAM.items()
# C872SRC 000523|        if result.get(key) != expected
# C872SRC 000524|    }
# C872SRC 000525|    return result
# C872SRC 000526|
# C872SRC 000527|
# C872SRC 000528|def path_metrics(word, basis):
# C872SRC 000529|    depth = deletion = returns = operands = 0
# C872SRC 000530|    footprint = set()
# C872SRC 000531|    for instruction in word:
# C872SRC 000532|        if len(instruction.sites) == 1:
