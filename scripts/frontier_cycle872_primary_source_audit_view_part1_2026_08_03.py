#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 872 primary source, part 1/4."""

TARGET_SOURCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 4
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 485
TOTAL_SOURCE_LINES = 1940
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "c1b32ef8e2a870128b7081a88b920b85c84123d04f98a165bfc7225dcfc716e4"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C872SRC 000001|#!/usr/bin/env python3
# C872SRC 000002|"""Cycle 872 bounded construction: one all-seam spatial packet epoch.
# C872SRC 000003|
# C872SRC 000004|This runner writes one deterministic receipt.  It claims one bounded update
# C872SRC 000005|epoch on supplied clean own-bank inputs.  It does not derive causal
# C872SRC 000006|orientation or later-epoch bank renewal.
# C872SRC 000007|"""
# C872SRC 000008|
# C872SRC 000009|from __future__ import annotations
# C872SRC 000010|
# C872SRC 000011|import argparse
# C872SRC 000012|from collections import Counter, defaultdict
# C872SRC 000013|from dataclasses import dataclass, field
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
# C872SRC 000028|def discover_source_root() -> Path:
# C872SRC 000029|    supplied = os.environ.get("CYCLE872_SOURCE_ROOT")
# C872SRC 000030|    candidates = []
# C872SRC 000031|    if supplied:
# C872SRC 000032|        candidates.append(Path(supplied))
# C872SRC 000033|    for start in (Path.cwd(), PACKAGE_ROOT):
# C872SRC 000034|        candidates.extend((start, *start.parents))
# C872SRC 000035|    marker = "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
# C872SRC 000036|    for candidate in candidates:
# C872SRC 000037|        resolved = candidate.resolve()
# C872SRC 000038|        if (resolved / marker).is_file():
# C872SRC 000039|            return resolved
# C872SRC 000040|    raise RuntimeError(
# C872SRC 000041|        "Cycle872 upstream repository not found; run from its root or set "
# C872SRC 000042|        "CYCLE872_SOURCE_ROOT"
# C872SRC 000043|    )
# C872SRC 000044|
# C872SRC 000045|
# C872SRC 000046|SOURCE_ROOT = discover_source_root()
# C872SRC 000047|sys.path.insert(0, str(SOURCE_ROOT / "scripts"))
# C872SRC 000048|
# C872SRC 000049|import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
# C872SRC 000050|import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
# C872SRC 000051|import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
# C872SRC 000052|import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
# C872SRC 000053|import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
# C872SRC 000054|import physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22 as C612
# C872SRC 000055|
# C872SRC 000056|
# C872SRC 000057|NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
# C872SRC 000058|DEFAULT_RECEIPT = PACKAGE_ROOT / "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json"
# C872SRC 000059|EXPECTED_NOTE_SHA256 = "dd218e18d3a24506b11db9fdbad909f899187eeda5bf579a2b1a984afd10c8f7"
# C872SRC 000060|EXPECTED_INPUT_SHA256 = {
# C872SRC 000061|    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
# C872SRC 000062|    "scripts/active_cubic_source_response_cycle211_2026_07_16.py": "d5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6",
# C872SRC 000063|    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py": "a5e78e40cad0c43ee62ae887df7d84a0b895ab217ba4f3d521353e5d0b6bf95a",
# C872SRC 000064|    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py": "464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4",
# C872SRC 000065|    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
# C872SRC 000066|    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py": "3a977106389428d2281ea7e0e32b65fe57f6ce33d783742b80f264f78f4f2c17",
# C872SRC 000067|    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py": "fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7",
# C872SRC 000068|    "scripts/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.py": "2d9618ab1c50448f4bd611826c3f265bb8985878a5d76d01d3b78d793d3635d0",
# C872SRC 000069|    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py": "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
# C872SRC 000070|    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py": "781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e",
# C872SRC 000071|    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
# C872SRC 000072|    "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py": "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
# C872SRC 000073|    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py": "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a",
# C872SRC 000074|    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py": "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
# C872SRC 000075|    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py": "b42ea07c1ed671b9cbab38bc38eba6f8166fe65be52295941a95e3ed75049abf",
# C872SRC 000076|    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py": "f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3",
# C872SRC 000077|    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py": "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
# C872SRC 000078|    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py": "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
# C872SRC 000079|    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py": "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
# C872SRC 000080|    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py": "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
# C872SRC 000081|    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py": "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
# C872SRC 000082|    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py": "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
# C872SRC 000083|    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
# C872SRC 000084|    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py": "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
# C872SRC 000085|    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py": "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
# C872SRC 000086|    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py": "94f0fbd1212e210d0e073c3a80cdc2f92afa3c9807f981bd220625a67e8d94a0",
# C872SRC 000087|    "scripts/frontier_full128_code_projectors_2026_07_24.py": "f561714d036c8c7568b1772110303d6c0da11c6d73c9df3bdcbae2db632f5b44",
# C872SRC 000088|    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py": "ecae9048b4ee2d257315072cb7120335109f362fa7007573c46a82a1f0ed4195",
# C872SRC 000089|    "scripts/frontier_full128_cycle_encoder_2026_07_24.py": "17eca725b72943d8804147dd800be044ffaa80dc209588adb37ae6543d0fa935",
# C872SRC 000090|    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py": "b446ace0856b45108ae0ed4ed35614961ae3b69bf20d12132981f54809966afb",
# C872SRC 000091|    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py": "05cb2f6083cf6c4307c04284632e991b7fd7378cbd2a4eb08a52d5e3c7ae6b99",
# C872SRC 000092|    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py": "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
# C872SRC 000093|    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py": "4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6",
# C872SRC 000094|    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py": "97fdf54189d7da93099aeab4a9b1dd8501c7262d55493b9fa95bf1c2f5c97a9d",
# C872SRC 000095|    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py": "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8",
# C872SRC 000096|    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py": "67aa2435d66fb34b6734cc564a82ac839525139fdc9e8c347dc1b2277d08b40b",
# C872SRC 000097|    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py": "ef6805e691a1ddd303a96f7cabd7000517e0cf33d5b1c577b20c2cbbf29aca23",
# C872SRC 000098|    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py": "4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6",
# C872SRC 000099|    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
# C872SRC 000100|    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py": "a9786cf68a9c669e7e7fe310a00ab9912aa404689651682ccfe3045a06e357f1",
# C872SRC 000101|    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py": "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b",
# C872SRC 000102|    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py": "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
# C872SRC 000103|    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py": "472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86",
# C872SRC 000104|    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
# C872SRC 000105|    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py": "9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011",
# C872SRC 000106|}
# C872SRC 000107|
# C872SRC 000108|Coord = tuple[int, int, int]
# C872SRC 000109|SPATIAL_CURRENT_LOCAL = (0, 0, 3)
# C872SRC 000110|
# C872SRC 000111|
# C872SRC 000112|@dataclass(frozen=True)
# C872SRC 000113|class BoundInstruction:
# C872SRC 000114|    serial: int
# C872SRC 000115|    factor_index: int
# C872SRC 000116|    factor: tuple[object, ...]
# C872SRC 000117|    stage: str
# C872SRC 000118|    segment: str
# C872SRC 000119|    rotation_serial: int | None
# C872SRC 000120|    instruction: object = field(repr=False, compare=False)
# C872SRC 000121|    route_policy: str
# C872SRC 000122|    path: tuple[Coord, ...]
# C872SRC 000123|    gate_start: int
# C872SRC 000124|    gate_stop: int
# C872SRC 000125|
# C872SRC 000126|
# C872SRC 000127|@dataclass(frozen=True)
# C872SRC 000128|class ExecutablePhysicalGate:
# C872SRC 000129|    serial: int
# C872SRC 000130|    factor_index: int
# C872SRC 000131|    instruction_serial: int
# C872SRC 000132|    role: str
# C872SRC 000133|    sites: tuple[Coord, ...]
# C872SRC 000134|    matrix: np.ndarray = field(repr=False, compare=False)
# C872SRC 000135|
# C872SRC 000136|
# C872SRC 000137|@dataclass(frozen=True)
# C872SRC 000138|class PhysicalEpochStream:
# C872SRC 000139|    length: int
# C872SRC 000140|    native_rotations: tuple[object, ...]
# C872SRC 000141|    native_inventory: dict[str, object]
# C872SRC 000142|    native_factors: tuple[tuple[tuple[object, ...], tuple[object, ...]], ...]
# C872SRC 000143|    factor_manifest: tuple[dict[str, object], ...]
# C872SRC 000144|    instructions: tuple[BoundInstruction, ...]
# C872SRC 000145|    gates: tuple[ExecutablePhysicalGate, ...]
# C872SRC 000146|    matrix_registry: dict[str, dict[str, object]]
# C872SRC 000147|    construction_failures: dict[str, int]
# C872SRC 000148|    deletion_detections: int
# C872SRC 000149|
# C872SRC 000150|
# C872SRC 000151|def file_sha256(path: Path) -> str:
# C872SRC 000152|    return sha256(path.read_bytes()).hexdigest()
# C872SRC 000153|
# C872SRC 000154|
# C872SRC 000155|def cells(length: int) -> tuple[Coord, ...]:
# C872SRC 000156|    return tuple(product(range(length), repeat=3))
# C872SRC 000157|
# C872SRC 000158|
# C872SRC 000159|def color(seam) -> tuple[int, int, int, int]:
# C872SRC 000160|    owner, axis = seam[0], seam[1]
# C872SRC 000161|    remaining = tuple(owner[index] & 1 for index in range(3) if index != axis)
# C872SRC 000162|    return axis, owner[axis] & 1, *remaining
# C872SRC 000163|
# C872SRC 000164|
# C872SRC 000165|def coarse_color(seam) -> tuple[int, int]:
# C872SRC 000166|    return seam[1], seam[0][seam[1]] & 1
# C872SRC 000167|
# C872SRC 000168|
# C872SRC 000169|def spatial_current_site(placement) -> Coord:
# C872SRC 000170|    """The retained spatial-current output, separate from causal ORIENT."""
# C872SRC 000171|    site = placement.midpoint
# C872SRC 000172|    for coefficient, direction in zip(SPATIAL_CURRENT_LOCAL, placement.basis):
# C872SRC 000173|        site = C871.add(site, C871.scale(coefficient, direction))
# C872SRC 000174|    return site
# C872SRC 000175|
# C872SRC 000176|
# C872SRC 000177|def resource_bank(placement) -> frozenset[Coord]:
# C872SRC 000178|    return frozenset((*placement.sites, spatial_current_site(placement)))
# C872SRC 000179|
# C872SRC 000180|
# C872SRC 000181|def provenance_certificate():
# C872SRC 000182|    observed = {
# C872SRC 000183|        label: file_sha256(SOURCE_ROOT / label)
# C872SRC 000184|        for label in EXPECTED_INPUT_SHA256
# C872SRC 000185|        if (SOURCE_ROOT / label).is_file()
# C872SRC 000186|    }
# C872SRC 000187|    return {
# C872SRC 000188|        "declared_inputs": tuple(EXPECTED_INPUT_SHA256),
# C872SRC 000189|        "literal_dependency_pin_count": len(EXPECTED_INPUT_SHA256),
# C872SRC 000190|        "dependency_surface": (
# C872SRC 000191|            "complete local Python import closure plus dynamically loaded Cycle870 "
# C872SRC 000192|            "placement and Cycle610/611 modules"
# C872SRC 000193|        ),
# C872SRC 000194|        "input_sha256": observed,
# C872SRC 000195|        "missing_inputs": tuple(
# C872SRC 000196|            label for label in EXPECTED_INPUT_SHA256 if label not in observed
# C872SRC 000197|        ),
# C872SRC 000198|        "pin_failures": {
# C872SRC 000199|            label: {"expected": expected, "observed": observed.get(label)}
# C872SRC 000200|            for label, expected in EXPECTED_INPUT_SHA256.items()
# C872SRC 000201|            if observed.get(label) != expected
# C872SRC 000202|        },
# C872SRC 000203|        "theorem_note": NOTE,
# C872SRC 000204|        "theorem_note_sha256": file_sha256(PACKAGE_ROOT / NOTE),
# C872SRC 000205|        "theorem_note_pin_failure": (
# C872SRC 000206|            file_sha256(PACKAGE_ROOT / NOTE) != EXPECTED_NOTE_SHA256
# C872SRC 000207|        ),
# C872SRC 000208|        "runner_sha256": file_sha256(Path(__file__)),
# C872SRC 000209|    }
# C872SRC 000210|
# C872SRC 000211|
# C872SRC 000212|def candidate_segments(graph, context, seam, placement, *, wrong_side=False,
# C872SRC 000213|                       delete_seam=False, seam_rotations=None):
# C872SRC 000214|    cell, _axis, target, left_mode, right_mode = seam
# C872SRC 000215|    left_b = C871.physical_b(graph, context, cell, left_mode)
# C872SRC 000216|    right_b = C871.physical_b(graph, context, target, right_mode)
# C872SRC 000217|    du = placement.sites[C714.MCX_WORK[0]]
# C872SRC 000218|    dv = placement.sites[C714.MCX_WORK[1]]
# C872SRC 000219|    pointer = placement.sites[C714.POINTER]
# C872SRC 000220|    spatial = spatial_current_site(placement)
# C872SRC 000221|    pre = (
# C872SRC 000222|        C871.extract_b(left_b, context, du, "endpoint_pre_left_B")
# C872SRC 000223|        + C871.extract_b(right_b, context, dv, "endpoint_pre_right_B")
# C872SRC 000224|    )
# C872SRC 000225|    seam_word = C871.compile_rotations(
# C872SRC 000226|        C871.selected_seam_rotations(graph, seam)
# C872SRC 000227|        if seam_rotations is None else seam_rotations,
# C872SRC 000228|        context,
# C872SRC 000229|    )
# C872SRC 000230|    if delete_seam:
# C872SRC 000231|        seam_word = ()
# C872SRC 000232|    post = (
# C872SRC 000233|        C871.extract_b(left_b, context, du, "endpoint_post_left_B")
# C872SRC 000234|        + C871.extract_b(right_b, context, dv, "endpoint_post_right_B")
# C872SRC 000235|    )
# C872SRC 000236|    endpoint_or = (
# C872SRC 000237|        C871.cnot(du, pointer, "endpoint_OR_CNOT"),
# C872SRC 000238|        C871.cnot(dv, pointer, "endpoint_OR_CNOT"),
# C872SRC 000239|    ) + C871.toffoli_word(du, dv, pointer, "endpoint_OR_Toffoli_")
# C872SRC 000240|    clean = (
# C872SRC 000241|        C871.extract_b(left_b, context, du, "endpoint_clean_left_B")
# C872SRC 000242|        + C871.extract_b(right_b, context, du, "endpoint_clean_right_B")
# C872SRC 000243|        + C871.extract_b(left_b, context, dv, "endpoint_clean_left_B")
# C872SRC 000244|        + C871.extract_b(right_b, context, dv, "endpoint_clean_right_B")
# C872SRC 000245|    )
# C872SRC 000246|    direction_b = left_b if wrong_side else right_b
# C872SRC 000247|    direction = (
# C872SRC 000248|        C871.extract_b(direction_b, context, du, "spatial_direction_B_load")
# C872SRC 000249|        + C871.toffoli_word(pointer, du, spatial, "spatial_direction_Toffoli_")
# C872SRC 000250|        + C871.extract_b(direction_b, context, du, "spatial_direction_B_unload")
# C872SRC 000251|    )
# C872SRC 000252|    return {
# C872SRC 000253|        "pre": pre,
# C872SRC 000254|        "seam": seam_word,
# C872SRC 000255|        "post": post,
# C872SRC 000256|        "or": endpoint_or,
# C872SRC 000257|        "clean": clean,
# C872SRC 000258|        "spatial_direction_write": direction,
# C872SRC 000259|        "packet": C871.packet_word(placement),
# C872SRC 000260|    }
# C872SRC 000261|
# C872SRC 000262|
# C872SRC 000263|def flatten(segments):
# C872SRC 000264|    return tuple(row for segment in segments.values() for row in segment)
# C872SRC 000265|
# C872SRC 000266|
# C872SRC 000267|def canonical_json_bytes(value) -> bytes:
# C872SRC 000268|    return (
# C872SRC 000269|        json.dumps(value, sort_keys=True, separators=(",", ":"), default=float)
# C872SRC 000270|        + "\n"
# C872SRC 000271|    ).encode()
# C872SRC 000272|
# C872SRC 000273|
# C872SRC 000274|def matrix_payload(matrix: np.ndarray) -> dict[str, object]:
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
# C872SRC 000286|def matrix_key(matrix: np.ndarray) -> str:
# C872SRC 000287|    return sha256(canonical_json_bytes(matrix_payload(matrix))).hexdigest()
# C872SRC 000288|
# C872SRC 000289|
# C872SRC 000290|def serialize_bound_instruction(row: BoundInstruction) -> dict[str, object]:
# C872SRC 000291|    instruction = row.instruction
# C872SRC 000292|    return {
# C872SRC 000293|        "serial": row.serial,
# C872SRC 000294|        "factor_index": row.factor_index,
# C872SRC 000295|        "factor": row.factor,
# C872SRC 000296|        "stage": row.stage,
# C872SRC 000297|        "segment": row.segment,
# C872SRC 000298|        "rotation_serial": row.rotation_serial,
# C872SRC 000299|        "kind": instruction.kind,
# C872SRC 000300|        "unrouted_sites": instruction.sites,
# C872SRC 000301|        "unrouted_matrix": matrix_key(instruction.matrix),
# C872SRC 000302|        "route_policy": row.route_policy,
# C872SRC 000303|        "path": row.path,
# C872SRC 000304|        "gate_serial_start": row.gate_start,
# C872SRC 000305|        "gate_serial_stop_exclusive": row.gate_stop,
# C872SRC 000306|    }
# C872SRC 000307|
# C872SRC 000308|
# C872SRC 000309|def serialize_physical_gate(row: ExecutablePhysicalGate) -> dict[str, object]:
# C872SRC 000310|    return {
# C872SRC 000311|        "serial": row.serial,
# C872SRC 000312|        "factor_index": row.factor_index,
# C872SRC 000313|        "instruction_serial": row.instruction_serial,
# C872SRC 000314|        "role": row.role,
# C872SRC 000315|        "sites": row.sites,
# C872SRC 000316|        "matrix": matrix_key(row.matrix),
# C872SRC 000317|    }
# C872SRC 000318|
# C872SRC 000319|
# C872SRC 000320|def physical_stream_payload(stream: PhysicalEpochStream) -> dict[str, object]:
# C872SRC 000321|    return {
# C872SRC 000322|        "schema": "cycle872-executable-local-gate-stream-v1",
# C872SRC 000323|        "length": stream.length,
# C872SRC 000324|        "composition_order": (
# C872SRC 000325|            "ascending physical-gate serial; each listed local matrix left-multiplies "
# C872SRC 000326|            "the state after the preceding gate"
# C872SRC 000327|        ),
# C872SRC 000328|        "local_basis": (
# C872SRC 000329|            "one-site |0>,|1>; two-site little-endian |00>,|10>,|01>,|11> "
# C872SRC 000330|            "with first listed site as local bit zero"
# C872SRC 000331|        ),
# C872SRC 000332|        "semantic_scope": (
# C872SRC 000333|            "exact local matrices and global serial composition/order certificate; "
# C872SRC 000334|            "no global statevector or global matrix was constructed"
# C872SRC 000335|        ),
# C872SRC 000336|        "formal_zero_site_global_phase_correction_angle": stream.native_inventory[
# C872SRC 000337|            "exact_target_global_phase_correction_angle"
# C872SRC 000338|        ],
# C872SRC 000339|        "factor_manifest": stream.factor_manifest,
# C872SRC 000340|        "instruction_bindings": tuple(
# C872SRC 000341|            serialize_bound_instruction(row) for row in stream.instructions
# C872SRC 000342|        ),
# C872SRC 000343|        "physical_gates": tuple(serialize_physical_gate(row) for row in stream.gates),
# C872SRC 000344|        "matrix_registry": dict(sorted(stream.matrix_registry.items())),
# C872SRC 000345|    }
# C872SRC 000346|
# C872SRC 000347|
# C872SRC 000348|def build_physical_epoch_stream(length: int) -> PhysicalEpochStream:
# C872SRC 000349|    """Materialize one complete, serial, locally executable physical epoch."""
# C872SRC 000350|    graph = C870.prep.OpenReferenceGraph(cells(length))
# C872SRC 000351|    context = C870.physical_context(graph)
# C872SRC 000352|    seams = C870.graph_seams(graph)
# C872SRC 000353|    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
# C872SRC 000354|    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
# C872SRC 000355|    factors = tuple(
# C872SRC 000356|        (tuple(factor), tuple(group))
# C872SRC 000357|        for factor, group in groupby(rotations, key=lambda row: row.factor)
# C872SRC 000358|    )
# C872SRC 000359|    seam_lookup = {
# C872SRC 000360|        ("seam", index, seam[0], seam[1], seam[2]): (seam, placements[index])
# C872SRC 000361|        for index, seam in enumerate(seams)
# C872SRC 000362|    }
# C872SRC 000363|    registry: dict[str, dict[str, object]] = {}
# C872SRC 000364|    instructions: list[BoundInstruction] = []
# C872SRC 000365|    gates: list[ExecutablePhysicalGate] = []
# C872SRC 000366|    factor_manifest: list[dict[str, object]] = []
# C872SRC 000367|    failures = Counter()
# C872SRC 000368|    deletion_detections = 0
# C872SRC 000369|
# C872SRC 000370|    def register(matrix) -> str:
# C872SRC 000371|        key = matrix_key(matrix)
# C872SRC 000372|        payload = matrix_payload(matrix)
# C872SRC 000373|        failures["matrix_digest_collision"] += key in registry and registry[key] != payload
# C872SRC 000374|        registry[key] = payload
# C872SRC 000375|        return key
# C872SRC 000376|
# C872SRC 000377|    def emit_instruction(
# C872SRC 000378|        factor_index: int,
# C872SRC 000379|        factor: tuple[object, ...],
# C872SRC 000380|        stage: str,
# C872SRC 000381|        segment: str,
# C872SRC 000382|        rotation_serial: int | None,
# C872SRC 000383|        instruction,
# C872SRC 000384|        route_policy: str,
# C872SRC 000385|        basis,
# C872SRC 000386|    ) -> None:
# C872SRC 000387|        nonlocal deletion_detections
# C872SRC 000388|        instruction_serial = len(instructions)
# C872SRC 000389|        failures["unsupported_instruction_arity"] += len(instruction.sites) not in (1, 2)
# C872SRC 000390|        if len(instruction.sites) == 1:
# C872SRC 000391|            path = tuple(instruction.sites)
# C872SRC 000392|        elif route_policy == "landed_global_axis_manhattan_returned":
# C872SRC 000393|            path = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
# C872SRC 000394|        else:
# C872SRC 000395|            path = C871.coframe_path(*instruction.sites, basis)
# C872SRC 000396|        failures["route_endpoint"] += (
# C872SRC 000397|            not path
# C872SRC 000398|            or path[0] != instruction.sites[0]
# C872SRC 000399|            or path[-1] != instruction.sites[-1]
# C872SRC 000400|        )
# C872SRC 000401|        gate_start = len(gates)
# C872SRC 000402|        register(instruction.matrix)
# C872SRC 000403|        if len(instruction.sites) == 1:
# C872SRC 000404|            gates.append(ExecutablePhysicalGate(
# C872SRC 000405|                len(gates), factor_index, instruction_serial, "active_one_site",
# C872SRC 000406|                instruction.sites, instruction.matrix,
# C872SRC 000407|            ))
# C872SRC 000408|        elif len(instruction.sites) == 2:
# C872SRC 000409|            labels = list(path)
# C872SRC 000410|            for route_index in range(len(path) - 2):
# C872SRC 000411|                sites = (path[route_index], path[route_index + 1])
# C872SRC 000412|                gates.append(ExecutablePhysicalGate(
# C872SRC 000413|                    len(gates), factor_index, instruction_serial, "swap_forward",
# C872SRC 000414|                    sites, C870.c707.c655.SWAP,
# C872SRC 000415|                ))
# C872SRC 000416|                register(C870.c707.c655.SWAP)
# C872SRC 000417|                labels[route_index], labels[route_index + 1] = (
# C872SRC 000418|                    labels[route_index + 1], labels[route_index]
# C872SRC 000419|                )
# C872SRC 000420|            active_sites = (path[-2], path[-1])
# C872SRC 000421|            failures["active_operand_binding"] += tuple(labels[-2:]) != instruction.sites
# C872SRC 000422|            gates.append(ExecutablePhysicalGate(
# C872SRC 000423|                len(gates), factor_index, instruction_serial, "active_two_site",
# C872SRC 000424|                active_sites, instruction.matrix,
# C872SRC 000425|            ))
# C872SRC 000426|            for route_index in reversed(range(len(path) - 2)):
# C872SRC 000427|                sites = (path[route_index], path[route_index + 1])
# C872SRC 000428|                gates.append(ExecutablePhysicalGate(
# C872SRC 000429|                    len(gates), factor_index, instruction_serial, "swap_return",
# C872SRC 000430|                    sites, C870.c707.c655.SWAP,
# C872SRC 000431|                ))
# C872SRC 000432|                labels[route_index], labels[route_index + 1] = (
# C872SRC 000433|                    labels[route_index + 1], labels[route_index]
# C872SRC 000434|                )
# C872SRC 000435|            failures["spectator_permutation_return"] += labels != list(path)
# C872SRC 000436|            if len(path) > 2:
# C872SRC 000437|                damaged = list(path)
# C872SRC 000438|                for route_index in range(1, len(path) - 2):
# C872SRC 000439|                    damaged[route_index], damaged[route_index + 1] = (
# C872SRC 000440|                        damaged[route_index + 1], damaged[route_index]
# C872SRC 000441|                    )
# C872SRC 000442|                for route_index in reversed(range(len(path) - 2)):
# C872SRC 000443|                    damaged[route_index], damaged[route_index + 1] = (
# C872SRC 000444|                        damaged[route_index + 1], damaged[route_index]
# C872SRC 000445|                    )
# C872SRC 000446|                deletion_detections += damaged != list(path)
# C872SRC 000447|        gate_stop = len(gates)
# C872SRC 000448|        active = tuple(
# C872SRC 000449|            row for row in gates[gate_start:gate_stop] if row.role.startswith("active")
# C872SRC 000450|        )
# C872SRC 000451|        failures["active_gate_count"] += len(active) != 1
# C872SRC 000452|        if len(active) == 1:
# C872SRC 000453|            failures["active_matrix_binding"] += (
# C872SRC 000454|                matrix_key(active[0].matrix) != matrix_key(instruction.matrix)
# C872SRC 000455|            )
# C872SRC 000456|        instructions.append(BoundInstruction(
# C872SRC 000457|            instruction_serial, factor_index, factor, stage, segment,
# C872SRC 000458|            rotation_serial, instruction, route_policy, path, gate_start, gate_stop,
# C872SRC 000459|        ))
# C872SRC 000460|
# C872SRC 000461|    for factor_index, (factor, factor_rotations) in enumerate(factors):
# C872SRC 000462|        stage = str(factor[0])
# C872SRC 000463|        instruction_start = len(instructions)
# C872SRC 000464|        gate_start = len(gates)
# C872SRC 000465|        route_policy = (
# C872SRC 000466|            "augmented_seam_local_coframe_returned"
# C872SRC 000467|            if stage == "seam" else "landed_global_axis_manhattan_returned"
# C872SRC 000468|        )
# C872SRC 000469|        if stage == "seam":
# C872SRC 000470|            seam_binding = seam_lookup.get(factor)
# C872SRC 000471|            failures["seam_factor_lookup"] += seam_binding is None
# C872SRC 000472|            if seam_binding is None:
# C872SRC 000473|                continue
# C872SRC 000474|            seam, placement = seam_binding
# C872SRC 000475|            candidate = candidate_segments(
# C872SRC 000476|                graph, context, seam, placement, seam_rotations=factor_rotations
# C872SRC 000477|            )
# C872SRC 000478|            for segment, segment_word in candidate.items():
# C872SRC 000479|                if segment == "seam":
# C872SRC 000480|                    actual = []
# C872SRC 000481|                    for rotation in factor_rotations:
# C872SRC 000482|                        rotation_word = C870.c707.compile_pauli_rotation(
# C872SRC 000483|                            C870.physical_lift(rotation.row, context),
# C872SRC 000484|                            context.sites,
# C872SRC 000485|                            rotation.angle,
