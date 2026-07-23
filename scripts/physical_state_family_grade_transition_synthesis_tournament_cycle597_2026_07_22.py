#!/usr/bin/env python3
"""Cycle597: state-family grade-to-transition synthesis tournament."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
from math import floor
from pathlib import Path
import re
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_ti_innovation_bath_offgrid_history_tournament_cycle595_2026_07_22 as c595
import physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22 as c580

c592 = c595.c592
c587 = c595.c587
c577 = c595.c577
c552 = c595.c552
Gate = c587.Gate
Word = tuple[int, ...]

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_PATHS = {
    "Cycle595 runner": ROOT / "scripts/physical_ti_innovation_bath_offgrid_history_tournament_cycle595_2026_07_22.py",
    "Cycle595 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TI_INNOVATION_BATH_OFFGRID_HISTORY_TOURNAMENT_CYCLE595_NOTE_2026-07-22.md",
    "Cycle595 receipt": ROOT / "outputs/physical_ti_innovation_bath_offgrid_history_tournament_cycle595_receipt_2026_07_22.json",
    "Cycle595 cold": ROOT / "outputs/physical_ti_innovation_bath_offgrid_history_tournament_cycle595_cold_2026_07_22.txt",
    "Cycle592 runner": ROOT / "scripts/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22.py",
    "Cycle592 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md",
    "Cycle592 receipt": ROOT / "outputs/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_receipt_2026_07_22.json",
    "Cycle592 cold": ROOT / "outputs/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_cold_2026_07_22.txt",
    "Cycle580 runner": ROOT / "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
    "Cycle580 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md",
    "Cycle580 receipt": ROOT / "outputs/physical_l41_elementary_gate_layout_compiler_cycle580_receipt_2026_07_22.json",
    "Cycle580 cold": ROOT / "outputs/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.txt",
    "Cycle577 runner": ROOT / "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py",
    "Cycle577 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md",
    "Cycle577 receipt": ROOT / "outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_receipt_2026_07_22.json",
    "Cycle577 cold": ROOT / "outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.txt",
}
FROZEN = {
    "Cycle595 runner": "107fdaef7f2f834617bd695119569f0fc867768e64d695105e69107ef80d87d8",
    "Cycle595 note": "a6d852fdde7a90cb7bf2b11729d67828b03974e1248cbac7466353f13835f462",
    "Cycle595 receipt": "09eeeb4b2a2575a10a5030d75e29f6dd0346a7bbf248409531fb9825b1b005e6",
    "Cycle595 cold": "ecd3fb24ab1deee7395b914d708749bd924c6f1f3d5d177cd55228f4759f7216",
    "Cycle592 runner": "14d01e640eb1818c29aeb9f05313b2211e28e445d4798f3f6718d0b0fca0d62a",
    "Cycle592 note": "092f0bfc06f7a42d82ed10ade5f551bdb08ebe7040c8c2b8ba0b1b3ea1c971c7",
    "Cycle592 receipt": "edf069adbf58b66b30b6b9a66a85dd577b6c6c3170f833807dc57d59c8f14457",
    "Cycle592 cold": "cb2640da38cf7cb0a69e6351871d9a9ba93c712f6865d5055b0bd79f18acdc5c",
    "Cycle580 runner": "1f1acb34dc8976f5617319353e9591f64eae5cfe923a1dea736adfa792c4e718",
    "Cycle580 note": "47a6418c27965219ddc5d3c2a8bc39fd34aa6173d3d1c16e473a136113b9c787",
    "Cycle580 receipt": "9cf656c917ff738bc6d0d0e52dc8c251630aaedd86dd5a6b90dd4f7857cdbc1d",
    "Cycle580 cold": "890c68f44bf6cc563916304b51481def8aa3ad7009a6ecfe0b0a4cffc85cd7e6",
    "Cycle577 runner": "0876bc8888193606446b5fe07f1fdd8e3ddef3b313551739b81be3792c820aa7",
    "Cycle577 note": "7617ee877ca22986e0eacc09d08e14f6246cbc75b6443961c8626a1b5435f18c",
    "Cycle577 receipt": "f7e6bbc40a4d56ee115ba43ddbab7bee4aff05227b988a057adc4420f51941ed",
    "Cycle577 cold": "1c77d2ca4bf860482d3e55596c85e0983f32e755e7ceaac33ff0576a928c8a36",
}

# Every recursively imported local physical runner is independently byte-pinned.
# This is a conservative transitive import closure, not an inheritance of any
# scientific or review standing.
RUNTIME_PARENT_HASHES = {
    "physical_actual_member_admitted_history_law_tournament_train_cycle508_2026_07_20": "c02479ad564869b0a129b323997c35f3bb522f1db5c9f91c0c0718f31cca0c84",
    "physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21": "8f505d2de6476bdbc20f87a901e8be9fe46deda5b568c98d750977069a352e53",
    "physical_adjacent_two_star_order_character_preflight_cycle517_2026_07_21": "ad8b0c71840cbfa56aae3ae9da44eceec1cad7d84be06bab32604eb5f6fbb4a3",
    "physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21": "d2e0648558fb3031a200600b0643de28a5c8e695c35165a6905a6a99ff45255d",
    "physical_autonomous_local_member_law_cell_cycle552_2026_07_21": "123c9fe8a7a3802af2627e21dd1cee5a8dadfbe0b82b7862e64c7024be6adc7f",
    "physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22": "881e2c5a33217352a97df363f5c3dcd67980c2e672b59e072c6ecbc1cb0f27d1",
    "physical_autonomous_record_dual_front_rendezvous_nn_route_cycle353_2026_07_18": "d062a229d268ac54edebe664feed0e8dc70683b5e2dff3675f119d8204d901b9",
    "physical_autonomous_record_lineage_residue_nn_route_cycle352_2026_07_18": "83bfaba8d9d5f4e5507ee2d4a840be435d30c222af37542a5a19ad1d0f5ccdbb",
    "physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18": "a88b16a7af9938cda209537750ab9bfd58b16b0f3896c53419f3b030e8fbc19e",
    "physical_autonomous_record_payload_continuation_nn_route_cycle356_2026_07_18": "3921b1a28f55fdb5a3311e8496f8d2fe4d73a49e017ec5f0d03ef42e060bc677",
    "physical_autonomous_record_payload_faithful_close_nn_route_cycle361_2026_07_18": "cd4bbf4278e16e046fcc3d2a5e959b410ebeeb182428c32ebeb8cea96783d093",
    "physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21": "f31d207540efbf1541343c53552c947c77f2c984e705818786ac3c5f6d06eba2",
    "physical_born_menu_grade_interface_census_cycle381_2026_07_18": "9d33a422697bd67a8792e2b5f66911a3e1975f1fa00c076f09258de91c3bf714",
    "physical_born_proportional_quotient_auxiliary_cycle462_2026_07_19": "bc5ba26d8daa96d13f2d7ae2ec7aaa0d0d6a6b4f9b6ac7ea5684e5ad137aa42a",
    "physical_born_scaled_ray_split_merge_auxiliary_cycle454_2026_07_19": "09d9781ad3416bf8bd94917353661c1d222de115bc83691150be19fb4ae11ed2",
    "physical_born_short_rational_mixed_effect_auxiliary_cycle457_2026_07_19": "622407e8568143e3bbf3a74e21b964507dcd7f0d765afa81714488e970894a96",
    "physical_born_sparse_mixed_quotient_auxiliary_cycle466_2026_07_19": "e8cdc4af63e2567ace107f77390d4f72b1b0ce56b1624913356c56a0fea40406",
    "physical_born_support_eight_mixed_quotient_auxiliary_cycle471_2026_07_19": "792dc308187359c859a65432bdb3c585cd48528fe0f77e6919f0a3145386c32f",
    "physical_born_support_nine_mixed_quotient_auxiliary_cycle478_2026_07_19": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20": "d2836a9f46814fcab6387fa70f513bb5ec3403d29d30e080752c233484d4c98f",
    "physical_coherent_receiver_source_injection_cycle417_2026_07_18": "a359d119d97d74b6ff6d7eff495fd48d040ba41645ed90c472ffcd1fe05d5732",
    "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18": "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
    "physical_cycle269_coherent_cubic_pair_orbit_2026_07_17": "a5998584cdc19612c11c5b70399183ea3fa5c3f99d60f12aa989dbd3a87bbcd0",
    "physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17": "39c60c3ca2e7525a3a42f058df02a4b96e63f2bde6d54c042a5ec95a4ff3f9c6",
    "physical_cycle269_collision_safe_auxiliary_ports_2026_07_17": "03786effa03eae50930ca0bfa14c881276df8bd6bdba83b6d7a893cffe1fe747",
    "physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18": "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    "physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18": "0688e7db8b8490e525c0e1f1108474903e2ff40d278e185b6add54f8086f8110",
    "physical_cycle269_four_cell_star_cycle324_2026_07_18": "f2e07bf91e7a5b06c8037314798cb84cd6d747bc92fa6292c1759915fb91354d",
    "physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17": "3e970b2c84ebe891d36c132cd99d716ceb20b596cea89729f06ed8950c7a847c",
    "physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17": "cb6de428c5054ea9415a59bab75d36c693c65d8070df30a6a0bbc2a926f3f4e4",
    "physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17": "393de6368fe127a8d0e85b8a52a504585b53c09fb9ddfced5fe7b9079f26af92",
    "physical_cycle269_local_contact_intertwiner_2026_07_17": "ee42959d75bc09dfc7f1ce1ef4f19f50a2363b5d142efd8f5f8ebb20519bef3f",
    "physical_cycle269_local_fock_extension_cycle312_2026_07_18": "0aaab171ac23b28d8e6daa583e2e256bc872f971ec7f282898edea726d96ccd8",
    "physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18": "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    "physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17": "5c2030ef6a33906792307710a9fbfea02f0551574962c6e60cd04c42e5a62a36",
    "physical_cycle269_reference_relative_localized_pair_lift_2026_07_17": "95820817eaf883040aae96531f1afd4fe7a90569a43215d226cf44dce9a1cc09",
    "physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18": "4428d1f73ff315987edabd7f838a1c58414d0a982f0cd28656ddef3bd230d19f",
    "physical_cycle269_staggered_reservoir_catchup_2026_07_17": "5310ee8e19a55694f7a11ccf013c696b16cdb37961c5ade41ed316b27238bab1",
    "physical_cycle269_three_cell_multiedge_cycle319_2026_07_18": "faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb",
    "physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20": "93afe1600cb3fb8b7844729521b005ce62f957a128a6ffb9493a03a1d9932e96",
    "physical_cycle515_koszul_frame_bridge_cycle516_2026_07_20": "3c4318a84c661893932c8d41a90db36445f80cefd092a6a3fffb56cbf8abfa9c",
    "physical_delayed_dependency_admission_latch_cycle443_2026_07_19": "febfa320e566db01c50abd482352b6573daf6780a18414bef83a6529e960112b",
    "physical_detector_to_protected_record_formation_compiler_cycle433_2026_07_19": "53a8c2b97407b6444ad0c0bc2e4077419c9e74686bc309cbd1884066bdd378d3",
    "physical_deterministic_every_orbit_typed_append_cycle482_2026_07_19": "6b6f6242b407714e65b0b34abc34db1492d2dfd0984a308735281dfad8b21fda",
    "physical_effect_equivalence_normalized_grade_cycle321_2026_07_18": "77f46e3784274ee0dfafd610f2d9aca7a5edc836e94324b698689369574c4fd4",
    "physical_effect_functionality_protected_candidate_record_tournament_cycle436_2026_07_19": "e7e62dfba1a0b8afe9c5fb3e28371d45f07f85af0de0f50e8653b2b2fae67f46",
    "physical_endpoint_registration_process_route_cycle338_2026_07_18": "3d292cf8da5922d042281057e5a38edf4d020c02483f268970232c95aa4e7ab3",
    "physical_environment_export_realized_member_bridge_cycle334_2026_07_18": "ba27c3b6353f1ecb6f12d3b7feb4d5860a0acce85bbf58a0c2ad8bc90394d0ab",
    "physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19": "75a7f42ebbea25702474b8856413cbc2bd4c5e37d8d04b8ccf7e3b4d86f50262",
    "physical_event_to_append_commit_candidate_cycle326_2026_07_18": "8762609f9e9e85fb9311ed467bbc91fd5905f2ac5d160997555e8623c5e7f44c",
    "physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19": "dd3004fe92203651fd7fe732d1253d49379b52075bd88159fa7712154c0f8557",
    "physical_exhaustive_finite_grammar_overlap_installation_cycle398_2026_07_18": "af170225b321b508afe50b6718401426749e95c3312779b01e25ebfbb9d2690b",
    "physical_finite_born_exact_context_rank_recon_cycle448_2026_07_19": "cdaa13295194a81766191489e14ce20a35fe81fd26ef69e5c7377969ba7da478",
    "physical_finite_born_proof_basis_protected_packet_compiler_cycle440_2026_07_19": "ef0fff769dd5bcb0f2f0c4e05fc42ab5b69f3b45a670ab8d8a06bb156eab91cc",
    "physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18": "082d9619fada5a80a0214a10504b9f2496a604b01db5bdeffa25586be738b67b",
    "physical_fixed_program_carrier_two_use_cycle323_2026_07_18": "a7c709677344faf187aa223d79ea8e3ea5ea7ef4566ef951297a6a17d62a5511",
    "physical_form_occurrence_born_weight_firewall_cycle488_2026_07_20": "8102d64c485028dce3cf642ad48b2dca529d39b56e9563ad70dfe905924f4ba7",
    "physical_higher_outcome_overlap_menu_fixed_carrier_cycle394_2026_07_18": "720e56f03a2c5ddd3a009dc588205767a09337a88480f81882afd39bde76a39f",
    "physical_kraus_form_dephasing_bath_conveyor_cycle496_2026_07_20": "70b69e0dd63809e9c162ca95e0f453da58dd5b08bc2baf50c6458439b2a9949e",
    "physical_kraus_grade_repeated_history_law_tournament_cycle500_2026_07_20": "f94db1512fc8f2dd9298fefdf73162054b311810f66445c48f1a1d20931ad49f",
    "physical_kraus_record_lock_candidate_grade_formation_tournament_cycle502_2026_07_20": "6d93325cfa5ae438fa62db213127b03f7d8bb799c9a709726424f08c19c523b2",
    "physical_kraus_retained_carrier_record_binding_tournament_cycle505_2026_07_20": "8f7b95a9e164a6072de4bf95aa06c62f894ec8132fcff31ea31a61932767dea8",
    "physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22": "1f1acb34dc8976f5617319353e9591f64eae5cfe923a1dea736adfa792c4e718",
    "physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22": "0876bc8888193606446b5fe07f1fdd8e3ddef3b313551739b81be3792c820aa7",
    "physical_m64_reversible_event_sidecar_cycle314_2026_07_18": "c9fbdc70d1d80da008cf8ff3f43ebb158f54f6ba731b9ddc65e643f54f26618a",
    "physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18": "21fe83e141e6271d3fd6bee96320db3b365eede40af71a8d2a13097e6133c8c5",
    "physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18": "3caee29d02054a7aec31122b1053ab40a2265bb48384bba6fc925e9c457fee06",
    "physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19": "7ce3fa050d00e6cc1f6b0b2f21f487a9bf70add0a7f2ca3837c0be7ecb98b3a1",
    "physical_objective_member_record_bridge_tournament_cycle568_2026_07_22": "c07ef6ce6b633e804ae7dcfeec3a25cc78d0549d9c6124e4a76dc3a88e10e356",
    "physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21": "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
    "physical_outward_carrier_typed_prefix_cycle485_2026_07_19": "050c979de0f27073815309ad67635997f5c54b3344734b36e4f7fb3ab80ded7c",
    "physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22": "14d01e640eb1818c29aeb9f05313b2211e28e445d4798f3f6718d0b0fca0d62a",
    "physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21": "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    "physical_quadrupole_packet_width_bridge_cycle435_2026_07_19": "d0682c388411e3f2c4547e4703214ce70831382e12fe154da9a5349944a07ff7",
    "physical_quadrupole_receiver_candidate_packet_instrument_cycle439_2026_07_19": "bcfa1cfd94c01d20119ea5cd9fb61e535d0663033b51f0b22e3a9477f834c503",
    "physical_recoil_hard_core_field_bridge_cycle426_2026_07_19": "1001fc29d3e230ed55a0c973cdf5c598f75c72a6ee6b916a56eeddfdaa0a599e",
    "physical_record_actualization_law_program_tournament_cycle449_2026_07_19": "857febfb57c7b82559465ab0623ef15b5c392b87ceb323340e007c228df442ad",
    "physical_record_formation_link_genesis_counter_adapter_cycle368_2026_07_18": "c2e57bf1f09c78f871a6656b24d9ddb210a96ecf01d885d2d2cb8e7c9e52df6d",
    "physical_record_protected_capacity_export_adapter_cycle370_2026_07_18": "62e2d423999afaa4380d7392fee20f0cad492ade20f8af7f41ceb4547151ea02",
    "physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18": "22d5391c35b9b9d08c08bb44614fe24147181600df9a41a656fd5ea18950275a",
    "physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18": "4413c729325038deeebaac17d751b398e9e225e1c383cf80e80954df874231da",
    "physical_relational_actual_history_member_selection_cycle333_2026_07_18": "5c5e96ba6373c7ffb0dfb0905f37754d9c24262808b1ad6d43f160eb308ff51c",
    "physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22": "af0a0b4837781b2a03fc471c819ce4c6b95e4e4cc000c403fabe4ddb10f6b14c",
    "physical_reset_environment_record_occurrence_cycle483_2026_07_19": "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222",
    "physical_selected_seam_conditional_record_binder_cycle531_2026_07_21": "53ce534e112862b8a8b9427a1655c4803766e016ea289c410784d1c67d59f370",
    "physical_selected_seam_event_current_adapter_cycle526_2026_07_21": "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
    "physical_seven_overlap_menu_fixed_carrier_cycle390_2026_07_18": "8c24b68ba4f2a19c5a81d317a5e103152f0dd36dd78a5269a0333cbb12081c04",
    "physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18": "70d9c20fcbe9161c1a98c36c21b0370140ee785b32fa73eb4bd709c1eb983a95",
    "physical_signed_transverse_source_test_matter_prediction_cycle432_2026_07_19": "7e9a78895db3d1389f1cc119a51308c3a086d6bd7324ce49b8e8c615617f36c6",
    "physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18": "4fb41afc5067849689a958697d986962eab32ca6549199b046519e3bb48d8920",
    "physical_source_prediction_bridge_contract_cycle420_2026_07_19": "79eca68ca217277fa237d2420888b64ef7bfba801e8745925a8dfb14b7576d5c",
    "physical_source_response_actualization_law_tournament_cycle403_2026_07_18": "2cf352a051d50667168d3e6d72d4388d107784b37be692e38f17b4a0828f4987",
    "physical_source_response_record_counter_interface_cycle399_2026_07_18": "4d86e2323d25a73a5ee417b7fa674dcc5542a0f0363979dda330b0e7d30ce4f6",
    "physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19": "934f8bcda20d054e4a27f0710ff91da0f16ad0a27f7b6f5e50fa681a656c8c9a",
    "physical_strict_response_source_clock_metric_receiver_cycle416_2026_07_18": "ba99d29160f12d1133d9c5d8ec5a04f853ba20fb25f67d5f1b5f1473773f08c4",
    "physical_support_matcher_predecessor_controls_cycle329_2026_07_18": "2cf6370f72cd4025fcfba8f0edefff1c577ad2bf5c5b93f996ef23c5affbab0b",
    "physical_terminal_menu_member_law_tournament_cycle493_2026_07_20": "981a67e1bb4711c65fd1f24e7120f18dc0c92d051fa9accd4f962e49f1aa3a07",
    "physical_three_star_shared_parity_overlap_cycle520_2026_07_21": "22b00fd39fd07a04afb8776f4b97c31486ce4d2034617bd16aa170c263108b2b",
    "physical_ti_innovation_bath_offgrid_history_tournament_cycle595_2026_07_22": "107fdaef7f2f834617bd695119569f0fc867768e64d695105e69107ef80d87d8",
    "physical_transition_occurrence_close_tournament_cycle332_2026_07_18": "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
    "physical_two_block_recurrent_field_transport_cycle419_2026_07_19": "3c86a2ee58929b170b438920f917806cbe6f4bd113b6b617cafc6f84d15bb07b",
    "physical_typed_record_born_corpus_tournament_synthesis_cycle351_2026_07_18": "7912b5177f073abd5d06fd6206720582db2ebd1fe0cbb9d63afff8698cd53291",
    "physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18": "c9d3f14a9b3a741b297282e39b7cf7bb063f2480a032e990985f78a07e65a797",
    "physical_typed_record_scaled_projector_unpaired_corpus_route_cycle349_2026_07_18": "1698666d933113c1242c82ac5ce463b085e5236a1a56036dbdc0f8924fb0f5e2",
}
RUNTIME_PARENT_PATHS = {
    name: ROOT / "scripts" / f"{name}.py" for name in RUNTIME_PARENT_HASHES
}
EXPECTED_RUNTIME_PARENT_MANIFEST_SHA256 = "e407b4b1d71af6cbb9feed475bb204f2457ef129506b395a1393a0b970136fde"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


# This complete rule object is frozen before train or held input declarations.
# In particular, the 2-bit parameter grid, 6-bit transition address, and rotor
# constants are selected without any held parameter, precision, or corpus size.
SYNTHESIS_LAW = {
    "family": "three-M2 product states Z(p_L) tensor X(p_M) tensor Z(p_R), 0<=p_j<=1",
    "route_A": "Cycle577 Z-X-Z projector query using the Cycle580 encoded H/CNOT extraction block; four supplied copies",
    "route_B": {
        "parameter_fraction_bits": 2,
        "parameter_encoding": "four-bit unary threshold, nearest-grid half-up",
        "transition_bits": 6,
        "transition_addresses": 64,
        "rule": "all 4x4x4 microaddresses classified by the three unary parameter comparisons",
        "answer_rows": 0,
    },
    "route_C": {
        "rotor": "r_(n+1)=r_n+25 mod 64",
        "genesis": 9,
        "selection": "derived grade mask at r_n, never a host sampler",
        "worst_case_domain": "all 5^3 unary parameter words and all prefixes 1..64",
    },
    "occurrence_adapter": "fixed member = history mod 4; unchanged Cycle552 conditional occurrence",
}
SYNTHESIS_LAW_SHA256 = sha256(json.dumps(SYNTHESIS_LAW, sort_keys=True).encode()).hexdigest()
EXPECTED_SYNTHESIS_LAW_SHA256 = "9a2a6121730ad67c6049a42150a056687cc33fc6771897425fccb3d9e5b877b6"


@dataclass(frozen=True)
class Spec:
    name: str
    parameters: tuple[Fraction, Fraction, Fraction]
    corpus_size: int
    split: str


# Declared strictly after SYNTHESIS_LAW and its hash.
TRAIN_SPECS = (
    Spec("train_uniform", (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)), 128, "train"),
    Spec("train_basis_corner", (Fraction(1), Fraction(1), Fraction(1)), 96, "train"),
    Spec("train_asymmetric", (Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)), 160, "train"),
)
HELD_SPECS = (
    Spec("held_offgrid_7over11_4over9_5over13", (Fraction(7, 11), Fraction(4, 9), Fraction(5, 13)), 137, "held"),
    Spec("held_offgrid_11over17_13over19_17over23", (Fraction(11, 17), Fraction(13, 19), Fraction(17, 23)), 211, "held"),
)
SPECS = TRAIN_SPECS + HELD_SPECS
HELD_DECLARATION = {
    "points": tuple(tuple(str(value) for value in spec.parameters) for spec in HELD_SPECS),
    "physical_parameter_fraction_bits": 2,
    "transition_bits": 6,
    "sizes": tuple(spec.corpus_size for spec in HELD_SPECS),
}
HELD_SHA256 = sha256(json.dumps(HELD_DECLARATION, sort_keys=True).encode()).hexdigest()


def product_state(parameters: tuple[Fraction, Fraction, Fraction]) -> np.ndarray:
    if len(parameters) != 3 or any(value < 0 or value > 1 for value in parameters):
        raise ValueError("parameters leave the declared product-state cube")
    p_left, p_middle, p_right = (float(value) for value in parameters)
    minus = (c577.ZERO - c577.ONE) / np.sqrt(2.0)
    left = np.sqrt(p_left) * c577.ZERO + np.sqrt(1.0 - p_left) * c577.ONE
    middle = np.sqrt(p_middle) * c577.PLUS + np.sqrt(1.0 - p_middle) * minus
    right = np.sqrt(p_right) * c577.ZERO + np.sqrt(1.0 - p_right) * c577.ONE
    return c577.kron_all(left.reshape(-1, 1), middle.reshape(-1, 1), right.reshape(-1, 1)).reshape(-1)


def exact_product_grade(parameters: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, ...]:
    p_left, p_middle, p_right = parameters
    output = []
    for middle_sign, left_value, right_value in c577.HISTORIES:
        middle = p_middle if middle_sign == 1 else 1 - p_middle
        left = p_left if left_value == 0 else 1 - p_left
        right = p_right if right_value == 0 else 1 - p_right
        output.append(middle * left * right)
    return tuple(output)


def independent_grade(state: np.ndarray) -> np.ndarray:
    return c592.independent_grade_vector(state)


# Route A: exact coherent projector query and copied history-label register.
A_QUERY_NAMES = {
    "logical_H_open_decode", "logical_H_open_H", "logical_H_open_encode",
    "extract_X_middle", "extract_Z_left", "extract_Z_right",
    "logical_H_close_decode", "logical_H_close_H", "logical_H_close_encode",
}
A_QUERY = tuple(gate for gate in c580.ELEMENTARY_GATES if gate.name in A_QUERY_NAMES)
A_COPY = tuple(gate for gate in c580.ELEMENTARY_GATES if gate.role == "dephasing-copy")


def a_initial(state: np.ndarray) -> np.ndarray:
    encoded = c577.W3 @ state
    return np.kron(
        np.kron(np.kron(encoded, c577.ket(0, 64)), c577.ket(0, 8)),
        c577.ket(0, 8),
    ).reshape(-1, 1)


def register_distribution(state: np.ndarray, register: str) -> np.ndarray:
    tensor = state.reshape(64, 64, 8, 8)
    if register == "pointer":
        return np.sum(np.abs(tensor) ** 2, axis=(0, 1, 3)).reshape(8)
    if register == "copy":
        return np.sum(np.abs(tensor) ** 2, axis=(0, 1, 2)).reshape(8)
    raise ValueError("unknown Route-A register")


def route_a_controls() -> dict[str, object]:
    # Reconstruct the complete exact-pinned Cycle580 instrument and its inverse as
    # a shore check.  The state-query below uses only its exact pointer block;
    # using the full reset/contact instrument would overwrite the queried state.
    shore_initial = c580.initial_columns()
    shore_compiled = c580.apply_sequence(shore_initial, c580.ELEMENTARY_GATES)
    shore_target = c580.cycle577_target_columns()
    full_instrument_residual = float(np.linalg.norm(shore_compiled - shore_target))
    full_inverse_residual = float(np.linalg.norm(c580.inverse_sequence(shore_compiled, c580.ELEMENTARY_GATES) - shore_initial))
    del shore_initial, shore_compiled, shore_target

    rows = []
    maximum_query_residual = maximum_inverse_residual = maximum_copy_residual = 0.0
    maximum_expected_grade_residual = maximum_sector_mass_residual = 0.0
    maximum_boundary_leakage = 0.0
    maximum_active_query_deletion = maximum_active_copy_deletion = 0.0
    query_copies = 4
    for spec in SPECS:
        state = product_state(spec.parameters)
        exact = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        projector_grade = independent_grade(state)
        maximum_expected_grade_residual = max(maximum_expected_grade_residual, float(np.linalg.norm(projector_grade - exact)))
        initial = a_initial(state)
        queried = c580.apply_sequence(initial, A_QUERY)
        copied = c580.apply_sequence(queried, A_COPY)
        pointer = register_distribution(queried, "pointer")
        grade_copy = register_distribution(copied, "copy")
        maximum_query_residual = max(maximum_query_residual, float(np.linalg.norm(pointer - exact)))
        maximum_copy_residual = max(maximum_copy_residual, float(np.linalg.norm(grade_copy - exact)))
        recovered_query = c580.inverse_sequence(queried, A_QUERY)
        recovered_full = c580.inverse_sequence(copied, A_QUERY + A_COPY)
        maximum_inverse_residual = max(maximum_inverse_residual, float(np.linalg.norm(recovered_query - initial)), float(np.linalg.norm(recovered_full - initial)))
        maximum_boundary_leakage = max(
            maximum_boundary_leakage,
            c580.code_leakage(queried, c580.SYSTEM_PAIRS),
            c580.code_leakage(copied, c580.SYSTEM_PAIRS),
        )

        deleted_query = c580.apply_sequence(initial, tuple(g for g in A_QUERY + A_COPY if g.name != "extract_X_middle"))
        deleted_copy = c580.apply_sequence(initial, tuple(g for g in A_QUERY + A_COPY if g.name != "copy_middle_dephase"))
        maximum_active_query_deletion = max(maximum_active_query_deletion, float(np.linalg.norm(register_distribution(deleted_query, "copy") - exact, ord=1)))
        maximum_active_copy_deletion = max(maximum_active_copy_deletion, float(np.linalg.norm(register_distribution(deleted_copy, "copy") - exact, ord=1)))

        # Four independent supplied copies yield a coherent tuple register.
        # Its sector weights form a multinomial ledger; no sector is selected.
        expected_counts = np.zeros(8)
        sector_mass = 0.0
        supported_sector_count = 0
        for labels in product(range(8), repeat=query_copies):
            mass = float(np.prod(tuple(exact[label] for label in labels)))
            sector_mass += mass
            if mass > TOL:
                supported_sector_count += 1
            for label in labels:
                expected_counts[label] += mass / query_copies
        maximum_sector_mass_residual = max(maximum_sector_mass_residual, abs(sector_mass - 1.0), float(np.linalg.norm(expected_counts - exact)))
        rows.append({
            "name": spec.name, "split": spec.split,
            "exact_grade": tuple(float(x) for x in exact),
            "nonzero_single_query_sectors": int(np.sum(exact > TOL)),
            "supported_four_query_tuple_sectors": supported_sector_count,
            "maximum_single_component_empirical_variance": float(max(exact * (1.0 - exact) / query_copies)),
            "numeric_grade_word_or_objective_sector_derived": False,
        })

    frames = c577.c41.proper_cubic_rotations()
    edge_failures = 0
    two_site = tuple(gate for gate in A_QUERY + A_COPY if len(gate.qubits) == 2)
    for frame in frames:
        for gate in two_site:
            left_name, right_name = (c580.QUBIT_NAMES[index] for index in gate.qubits)
            left = frame @ np.asarray(c580.LAYOUT[left_name], dtype=int)
            right = frame @ np.asarray(c580.LAYOUT[right_name], dtype=int)
            edge_failures += int(sum(abs(int(a - b)) for a, b in zip(left, right)) != 1)

    result = {
        "route": "A coherent Cycle577-projector/Cycle580-pointer query",
        "complete_Cycle580_instrument_residual": full_instrument_residual,
        "complete_Cycle580_inverse_residual": full_inverse_residual,
        "query_elementary_gates": len(A_QUERY), "copy_CNOTs": len(A_COPY),
        "physical_M2_per_query_copy": 18,
        "supplied_identically_prepared_query_copies": query_copies,
        "physical_M2_per_four_query_batch": 18 * query_copies,
        "physical_M2_claim_basis": "exact-pinned Cycle577 dual-rail composition plus exact-pinned Cycle580 elementary layout",
        "primitive_composition_inherited_and_verified": True,
        "unverified_role_block_EG": None,
        "unverified_role_block_leakage": None,
        "unverified_role_block_layout": None,
        "maximum_projector_formula_residual": maximum_expected_grade_residual,
        "maximum_query_distribution_residual": maximum_query_residual,
        "maximum_copied_label_distribution_residual": maximum_copy_residual,
        "maximum_exact_inverse_residual": maximum_inverse_residual,
        "maximum_boundary_dual_rail_leakage": maximum_boundary_leakage,
        "four_query_sector_ledger_residual": maximum_sector_mass_residual,
        "active_query_gate_deletion_fixture_L1": maximum_active_query_deletion,
        "active_copy_gate_deletion_fixture_L1": maximum_active_copy_deletion,
        "all_coherent_sectors_preserved": True,
        "coherent_grade_register_is_objective_probability": False,
        "state_copy_preparation_or_no_cloning_derived": False,
        "proper_cubic_frames": len(frames),
        "all24_query_copy_edge_tests": len(frames) * len(two_site),
        "all24_query_copy_edge_failures": edge_failures,
        "rows": rows,
        "pass": max(full_instrument_residual, full_inverse_residual, maximum_expected_grade_residual,
                    maximum_query_residual, maximum_copy_residual, maximum_inverse_residual,
                    maximum_boundary_leakage, maximum_sector_mass_residual) < TOL
        and maximum_active_query_deletion > TOL and maximum_active_copy_deletion > TOL
        and edge_failures == 0 and len(frames) == 24,
    }
    check("Route A exactly queries and copies the Cycle577 grade distribution while preserving every coherent sector and supplied-copy import", result["pass"], result)
    return result


# Route B: one reversible product-family circuit, with no program selector and
# no per-state answer rows.  Each continuous parameter is rounded to a four-cell
# unary threshold; all 4^3 addresses then synthesize an exact denominator-64
# history mask by three literal comparisons.
B_PARAM_CELLS = 4
B_ADDRESS_COUNT = B_PARAM_CELLS**3
_b = [0]
B_PARAMETERS = tuple(take(_b, B_PARAM_CELLS) for _ in range(3))
B_WORK = take(_b, 1)[0]
B_MASK = tuple(take(_b, B_ADDRESS_COUNT) for _ in range(8))
B_WIDTH = _b[0]


def address_triple(address: int) -> tuple[int, int, int]:
    if address not in range(B_ADDRESS_COUNT):
        raise ValueError("microaddress leaves 4x4x4 domain")
    return address // 16, (address // 4) % 4, address % 4


def round_parameter(value: Fraction) -> int:
    if value < 0 or value > 1:
        raise ValueError("parameter leaves unit interval")
    return min(B_PARAM_CELLS, floor(value * B_PARAM_CELLS + Fraction(1, 2)))


def quantized_parameters(parameters: tuple[Fraction, Fraction, Fraction]) -> tuple[tuple[int, int, int], tuple[Fraction, Fraction, Fraction]]:
    if len(parameters) != 3:
        raise ValueError("parameter word must have exactly three entries")
    counts = tuple(round_parameter(value) for value in parameters)
    return counts, tuple(Fraction(value, B_PARAM_CELLS) for value in counts)


def build_b_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for address in range(B_ADDRESS_COUNT):
        left_index, middle_index, right_index = address_triple(address)
        for history, (middle_sign, left_value, right_value) in enumerate(c577.HISTORIES):
            literal_sites = (B_PARAMETERS[0][left_index], B_PARAMETERS[1][middle_index], B_PARAMETERS[2][right_index])
            invert = (left_value == 1, middle_sign == -1, right_value == 1)
            for slot, (site, needed) in enumerate(zip(literal_sites, invert)):
                if needed:
                    gates.append(Gate("X", (site,), f"B:mask:{history}:{address}:invert:{slot}:pre"))
            gates.append(Gate("TOFFOLI", (literal_sites[0], literal_sites[1], B_WORK), f"B:mask:{history}:{address}:and12"))
            gates.append(Gate("TOFFOLI", (B_WORK, literal_sites[2], B_MASK[history][address]), f"B:mask:{history}:{address}:write"))
            gates.append(Gate("TOFFOLI", (literal_sites[0], literal_sites[1], B_WORK), f"B:mask:{history}:{address}:unand12"))
            for slot, (site, needed) in reversed(tuple(enumerate(zip(literal_sites, invert)))):
                if needed:
                    gates.append(Gate("X", (site,), f"B:mask:{history}:{address}:invert:{slot}:post"))
    return tuple(gates)


B_SCHEDULE = build_b_schedule()


def prepare_b(parameters: tuple[Fraction, Fraction, Fraction]) -> Word:
    counts, _quantized = quantized_parameters(parameters)
    bits = [0] * B_WIDTH
    for sites, count in zip(B_PARAMETERS, counts):
        for index, site in enumerate(sites):
            bits[site] = int(index < count)
    return tuple(bits)


def validate_unary(bits: Word) -> None:
    if len(bits) != B_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Route-B word leaves binary domain")
    for sites in B_PARAMETERS:
        word = tuple(bits[site] for site in sites)
        if word != tuple(sorted(word, reverse=True)):
            raise ValueError("Route-B parameter is not unary monotone")
    if bits[B_WORK] != 0 or any(bits[site] for row in B_MASK for site in row):
        raise ValueError("Route-B work/mask target is not blank")


def history_for_address(counts: tuple[int, int, int], address: int) -> int:
    left_index, middle_index, right_index = address_triple(address)
    return 4 * int(middle_index >= counts[1]) + 2 * int(left_index >= counts[0]) + int(right_index >= counts[2])


def expected_mask(counts: tuple[int, int, int]) -> Word:
    return tuple(int(history_for_address(counts, address) == history) for history in range(8) for address in range(B_ADDRESS_COUNT))


def mask_from_b_output(bits: Word) -> Word:
    return tuple(bits[site] for row in B_MASK for site in row)


def mask_counts(mask: Word) -> tuple[int, ...]:
    if len(mask) != 8 * B_ADDRESS_COUNT:
        raise ValueError("grade mask has wrong width")
    return tuple(sum(mask[history * B_ADDRESS_COUNT:(history + 1) * B_ADDRESS_COUNT]) for history in range(8))


def route_b_controls() -> dict[str, object]:
    line = c587.static_line_compiler_controls(B_SCHEDULE, B_WIDTH)
    exhaustive_failures = inverse_failures = code_failures = 0
    for counts in product(range(5), repeat=3):
        parameters = tuple(Fraction(value, 4) for value in counts)
        source = prepare_b(parameters)
        validate_unary(source)
        output = c587.apply_schedule(source, B_SCHEDULE)
        exhaustive_failures += mask_from_b_output(output) != expected_mask(counts)
        exhaustive_failures += output[B_WORK] != 0
        inverse_failures += c587.apply_schedule(output, B_SCHEDULE, reverse=True) != source
        code_failures += int(any(bit not in (0, 1) for bit in output))

    rows = []
    maximum_exact_grade_residual = maximum_product_synthesis_residual = 0.0
    maximum_bound_violation = 0.0
    for spec in SPECS:
        source = prepare_b(spec.parameters)
        output = c587.apply_schedule(source, B_SCHEDULE)
        counts, quantized = quantized_parameters(spec.parameters)
        synthesized_counts = mask_counts(mask_from_b_output(output))
        synthesized = np.asarray(synthesized_counts, dtype=float) / B_ADDRESS_COUNT
        exact = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        quantized_exact = np.asarray(tuple(float(value) for value in exact_product_grade(quantized)))
        exact_from_projector = independent_grade(product_state(spec.parameters))
        maximum_exact_grade_residual = max(maximum_exact_grade_residual, float(np.linalg.norm(exact_from_projector - exact)))
        maximum_product_synthesis_residual = max(maximum_product_synthesis_residual, float(np.linalg.norm(synthesized - quantized_exact)))
        actual_l1 = float(np.linalg.norm(synthesized - exact, ord=1))
        parameter_l1_bound = float(2 * sum(abs(value - rounded) for value, rounded in zip(spec.parameters, quantized)))
        maximum_bound_violation = max(maximum_bound_violation, actual_l1 - parameter_l1_bound)
        rows.append({
            "name": spec.name, "split": spec.split,
            "parameters": tuple(str(value) for value in spec.parameters),
            "quantized_parameters": tuple(str(value) for value in quantized),
            "denominator64_counts": synthesized_counts,
            "target_to_synthesized_L1": actual_l1,
            "product_parameter_L1_bound": parameter_l1_bound,
        })

    # Active parameter-bit deletion changes the derived grade word; deleting
    # the whole parameter word is lawfully refused.  Neither control reads a
    # state-specific answer row.
    deletion_spec = HELD_SPECS[0]
    ideal_source = prepare_b(deletion_spec.parameters)
    ideal_output = c587.apply_schedule(ideal_source, B_SCHEDULE)
    deleted_source = list(ideal_source)
    active_site = next(site for sites in B_PARAMETERS for site in reversed(sites) if deleted_source[site])
    deleted_source[active_site] = 0
    deleted_output = c587.apply_schedule(tuple(deleted_source), B_SCHEDULE)
    parameter_bit_deletion_l1 = float(np.linalg.norm(
        np.asarray(mask_counts(mask_from_b_output(ideal_output))) / B_ADDRESS_COUNT
        - np.asarray(mask_counts(mask_from_b_output(deleted_output))) / B_ADDRESS_COUNT,
        ord=1,
    ))
    absent_refused = 0
    try:
        prepare_b(())  # type: ignore[arg-type]
    except ValueError:
        absent_refused = 1

    relevant_source = inspect.getsource(build_b_schedule) + inspect.getsource(prepare_b) + inspect.getsource(expected_mask)
    answer_table_reads = relevant_source.count("HISTORY_TABLE") + relevant_source.count("MEMBER_TABLE")
    result = {
        "route": "B reversible unary fixed-point product-family synthesizer",
        "parameter_fraction_bits": 2, "transition_bits": 6,
        "physical_M2": B_WIDTH,
        "physical_M2_claim_basis": "exact-pinned Cycle587 basis-state primitive compiler with recursively pinned Cycle523 Toffoli dependency",
        "primitive_composition_inherited_and_verified": True,
        "unverified_role_block_EG": None,
        "unverified_role_block_leakage": None,
        "unverified_role_block_layout": None,
        "logical_gate_count": len(B_SCHEDULE),
        "exhaustive_parameter_words": 125,
        "exhaustive_mask_failures": exhaustive_failures,
        "inverse_failures": inverse_failures,
        "binary_code_failures": code_failures,
        "maximum_projector_formula_residual": maximum_exact_grade_residual,
        "maximum_exact_quantized_product_synthesis_residual": maximum_product_synthesis_residual,
        "maximum_approximation_bound_violation": maximum_bound_violation,
        "parameter_bit_deletion_L1": parameter_bit_deletion_l1,
        "absent_parameter_word_refusals": absent_refused,
        "Cycle592_answer_table_reads": answer_table_reads,
        "program_selector_M2": 0,
        "state_specific_answer_rows": 0,
        "static_nearest_neighbor_compiler": line,
        "rows": rows,
        "pass": exhaustive_failures == inverse_failures == code_failures == 0
        and max(maximum_exact_grade_residual, maximum_product_synthesis_residual) < TOL
        and maximum_bound_violation < TOL and parameter_bit_deletion_l1 > TOL
        and absent_refused == 1 and answer_table_reads == 0 and line["pass"],
    }
    check("Route B uses one reversible fixed-point product rule over all 125 parameter words with no program selector or answer ROM", result["pass"], result)
    return result


# Route C: a deterministic +25 one-carrier rotor reads the derived Route-B
# grade mask.  A fresh blank archive packet is consumed per occurrence; no
# history word or random draw is supplied by the host.
ROTOR_INCREMENT = 25
ROTOR_GENESIS = 9
_c = [0]
C_A = take(_c, 64)
C_BUFFER = take(_c, 64)
C_MASK = tuple(take(_c, 64) for _ in range(8))
C_SELECT = tuple(take(_c, 64) for _ in range(8))
C_HISTORY = take(_c, 8)
C_ARCHIVE = take(_c, 8)
C_WIDTH = _c[0]


def build_c_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for history, address in product(range(8), range(64)):
        gates.append(Gate("TOFFOLI", (C_MASK[history][address], C_A[address], C_SELECT[history][address]), f"C:select:{history}:{address}"))
    for history, address in product(range(8), range(64)):
        gates.append(Gate("CNOT", (C_SELECT[history][address], C_HISTORY[history]), f"C:history:{history}:{address}:write"))
    for history in range(8):
        gates.append(Gate("CNOT", (C_HISTORY[history], C_ARCHIVE[history]), f"C:archive:{history}"))
    for history, address in reversed(tuple(product(range(8), range(64)))):
        gates.append(Gate("CNOT", (C_SELECT[history][address], C_HISTORY[history]), f"C:history:{history}:{address}:clear"))
    for history, address in reversed(tuple(product(range(8), range(64)))):
        gates.append(Gate("TOFFOLI", (C_MASK[history][address], C_A[address], C_SELECT[history][address]), f"C:unselect:{history}:{address}"))
    for address in range(64):
        gates.append(Gate("SWAP", (C_A[address], C_BUFFER[address]), f"C:onsite:{address}"))
    for address in range(64):
        gates.append(Gate("SWAP", (C_BUFFER[address], C_A[(address + ROTOR_INCREMENT) % 64]), f"C:cross:{address}"))
    return tuple(gates)


C_SCHEDULE = build_c_schedule()


def validate_grade_mask(mask: Word) -> None:
    if len(mask) != 512 or any(type(bit) is not int or bit not in (0, 1) for bit in mask):
        raise ValueError("Route-C grade mask leaves binary 8x64 domain")
    if any(sum(mask[history * 64 + address] for history in range(8)) != 1 for address in range(64)):
        raise ValueError("Route-C grade mask is not one history per address")


def prepare_c(mask: Word, address: int) -> Word:
    validate_grade_mask(mask)
    if address not in range(64):
        raise ValueError("Route-C carrier leaves 64-address ring")
    bits = [0] * C_WIDTH
    bits[C_A[address]] = 1
    for history in range(8):
        for microaddress in range(64):
            bits[C_MASK[history][microaddress]] = mask[history * 64 + microaddress]
    return tuple(bits)


def mask_history(mask: Word, address: int) -> int:
    validate_grade_mask(mask)
    return next(history for history in range(8) if mask[history * 64 + address])


def expected_c(mask: Word, address: int) -> Word:
    output = list(prepare_c(mask, (address + ROTOR_INCREMENT) % 64))
    output[C_ARCHIVE[mask_history(mask, address)]] = 1
    return tuple(output)


def grade_mask_for_parameters(parameters: tuple[Fraction, Fraction, Fraction]) -> Word:
    output = c587.apply_schedule(prepare_b(parameters), B_SCHEDULE)
    return mask_from_b_output(output)


def discrepancy_certificate(order: tuple[int, ...]) -> Fraction:
    maximum = Fraction(0)
    for parameter_counts in product(range(5), repeat=3):
        target = [0] * 8
        for address in range(64):
            target[history_for_address(parameter_counts, address)] += 1
        prefix = [0] * 8
        for length, address in enumerate(order, start=1):
            prefix[history_for_address(parameter_counts, address)] += 1
            maximum = max(maximum, *(abs(Fraction(prefix[h]) - Fraction(length * target[h], 64)) for h in range(8)))
    return maximum


def route_c_controls() -> dict[str, object]:
    line = c587.static_line_compiler_controls(C_SCHEDULE, C_WIDTH)
    rotor_order = tuple((ROTOR_GENESIS + ROTOR_INCREMENT * index) % 64 for index in range(64))
    natural_order = tuple(range(64))
    rotor_discrepancy = discrepancy_certificate(rotor_order)
    natural_discrepancy = discrepancy_certificate(natural_order)
    eg_failures = inverse_failures = interface_failures = mask_ledger_failures = 0
    rows = []
    maximum_budget_violation = 0.0
    for spec in SPECS:
        mask = grade_mask_for_parameters(spec.parameters)
        validate_grade_mask(mask)
        grade_counts = mask_counts(mask)
        counts, quantized = quantized_parameters(spec.parameters)
        mask_ledger_failures += grade_counts != tuple(int(64 * value) for value in exact_product_grade(quantized))
        for address in range(64):
            source = prepare_c(mask, address)
            output = c587.apply_schedule(source, C_SCHEDULE)
            eg_failures += output != expected_c(mask, address)
            inverse_failures += c587.apply_schedule(output, C_SCHEDULE, reverse=True) != source

        histories = tuple(mask_history(mask, (ROTOR_GENESIS + ROTOR_INCREMENT * index) % 64) for index in range(spec.corpus_size))
        empirical = np.asarray(tuple(histories.count(history) / spec.corpus_size for history in range(8)))
        quantized_grade = np.asarray(grade_counts, dtype=float) / 64.0
        target_grade = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        rotor_l1 = float(np.linalg.norm(empirical - quantized_grade, ord=1))
        approximation_l1 = float(np.linalg.norm(quantized_grade - target_grade, ord=1))
        total_l1 = float(np.linalg.norm(empirical - target_grade, ord=1))
        parameter_bound = float(2 * sum(abs(value - rounded) for value, rounded in zip(spec.parameters, quantized)))
        rotor_bound = float(8 * rotor_discrepancy / spec.corpus_size)
        total_bound = parameter_bound + rotor_bound
        maximum_budget_violation = max(maximum_budget_violation, total_l1 - total_bound, rotor_l1 - rotor_bound, approximation_l1 - parameter_bound)
        for history in set(histories):
            member = history % 4
            base = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=history)
            fields, _law = c552.snapshot_view(c552.physical_step(base), 0)
            interface_failures += int(fields[:3] != (1, 1, 1))
        rows.append({
            "name": spec.name, "split": spec.split, "corpus_size": spec.corpus_size,
            "denominator64_grade": tuple(float(x) for x in quantized_grade),
            "finite_rotor_frequency": tuple(float(x) for x in empirical),
            "rotor_to_grade_L1": rotor_l1,
            "grade_approximation_L1": approximation_l1,
            "frequency_to_target_L1": total_l1,
            "parameter_approximation_bound": parameter_bound,
            "rotor_discrepancy_bound": rotor_bound,
            "combined_L1_bound": total_bound,
        })

    deletion_mask = grade_mask_for_parameters(HELD_SPECS[0].parameters)
    deletion_address = ROTOR_GENESIS
    deletion_history = mask_history(deletion_mask, deletion_address)
    source = prepare_c(deletion_mask, deletion_address)
    ideal = c587.apply_schedule(source, C_SCHEDULE)
    deleted_select = c587.apply_schedule(source, C_SCHEDULE, delete_label=f"C:select:{deletion_history}:{deletion_address}")
    deleted_cross = c587.apply_schedule(source, C_SCHEDULE, delete_label=f"C:cross:{deletion_address}")
    select_deletion_residual = float(np.linalg.norm(np.asarray(deleted_select) - np.asarray(ideal)))
    rotor_deletion_residual = float(np.linalg.norm(np.asarray(deleted_cross) - np.asarray(ideal)))
    deleted_grade_refused = absent_grade_refused = 0
    broken = list(deletion_mask)
    broken[deletion_history * 64 + deletion_address] = 0
    try:
        prepare_c(tuple(broken), deletion_address)
    except ValueError:
        deleted_grade_refused = 1
    try:
        prepare_c((), deletion_address)
    except ValueError:
        absent_grade_refused = 1

    source_text = inspect.getsource(build_c_schedule) + inspect.getsource(prepare_c) + inspect.getsource(expected_c) + inspect.getsource(mask_history)
    host_sampler_tokens = sum(source_text.count(token) for token in ("random", "choice(", "HISTORY_TABLE", "MEMBER_TABLE"))
    result = {
        "route": "C deterministic +25 low-discrepancy physical rotor",
        "physical_M2_per_occurrence_fixture": C_WIDTH,
        "physical_M2_claim_basis": "exact-pinned Cycle587 basis-state primitive compiler with recursively pinned Cycle523 Toffoli dependency",
        "primitive_composition_inherited_and_verified": True,
        "unverified_role_block_EG": None,
        "unverified_role_block_leakage": None,
        "unverified_role_block_layout": None,
        "rotor_increment": ROTOR_INCREMENT, "rotor_genesis": ROTOR_GENESIS,
        "rotor_period": len(set(rotor_order)),
        "exhaustive_grade_words": 125, "exhaustive_prefixes_per_word": 64,
        "rotor_maximum_per_history_count_discrepancy": str(rotor_discrepancy),
        "natural_order_comparator_discrepancy": str(natural_discrepancy),
        "EG_failures": eg_failures, "inverse_failures": inverse_failures,
        "grade_mask_ledger_failures": mask_ledger_failures,
        "unchanged_Cycle552_interface_failures": interface_failures,
        "maximum_error_budget_violation": maximum_budget_violation,
        "active_select_deletion_residual": select_deletion_residual,
        "active_rotor_edge_deletion_residual": rotor_deletion_residual,
        "deleted_grade_word_refusals": deleted_grade_refused,
        "absent_grade_word_refusals": absent_grade_refused,
        "host_sampler_or_answer_table_tokens": host_sampler_tokens,
        "carrier_and_grade_mask_catalytically_preserved": True,
        "fresh_blank_archive_M2_per_occurrence": 8,
        "archive_packet_renewal_derived": False,
        "rotor_frequency_promoted_to_Born": False,
        "static_nearest_neighbor_compiler": line,
        "rows": rows,
        "pass": rotor_discrepancy == Fraction(67, 32) and natural_discrepancy == Fraction(16)
        and len(set(rotor_order)) == 64 and rotor_discrepancy < natural_discrepancy
        and not any((eg_failures, inverse_failures, mask_ledger_failures, interface_failures))
        and maximum_budget_violation < TOL and min(select_deletion_residual, rotor_deletion_residual) > TOL
        and deleted_grade_refused == absent_grade_refused == 1 and host_sampler_tokens == 0 and line["pass"],
    }
    check("Route C deterministically consumes the derived grade mask with an exhaustive discrepancy certificate and explicit approximation/resource budget", result["pass"], result)
    return result


def covariance_domain_controls() -> dict[str, object]:
    frames = c577.c41.proper_cubic_rotations()
    frame_failures = group_failures = frame_tests = 0
    for frame in frames:
        for member in range(4):
            source = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=member)
            framed, axis = c552.frame_word(source, 0, frame)
            expected, expected_axis = c552.frame_word(c552.physical_step(source), 0, frame)
            frame_failures += int(c552.physical_step(framed) != expected or axis != expected_axis)
            frame_tests += 1
    for left, right in product(frames, repeat=2):
        source = c552.prepare(0, 0, 0, 0, edge=1, plus=1, minus=0, K_position=0)
        for axis in range(3):
            _, axis1 = c552.frame_word(source, axis, right)
            _, axis2 = c552.frame_word(source, axis1, left)
            _, axisp = c552.frame_word(source, axis, left @ right)
            group_failures += axis2 != axisp
    malformed = (
        lambda: product_state((Fraction(-1), Fraction(1, 2), Fraction(1, 2))),
        lambda: prepare_b(()),
        lambda: prepare_b((Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))),
        lambda: address_triple(64),
        lambda: prepare_c((0,) * 512, 0),
        lambda: prepare_c(grade_mask_for_parameters(TRAIN_SPECS[0].parameters), 64),
    )
    refused = 0
    for action in malformed:
        try:
            action()
        except ValueError:
            refused += 1
    result = {
        "proper_cubic_frames": len(frames),
        "all24_member_tests": frame_tests, "all24_member_failures": frame_failures,
        "all576_axis_tests": len(frames) ** 2 * 3, "all576_axis_failures": group_failures,
        "malformed_domain_refusals": refused, "malformed_domain_total": len(malformed),
        "pass": len(frames) == 24 and frame_failures == group_failures == 0 and refused == len(malformed),
    }
    check("all24/all576 conditional-occurrence covariance and malformed-domain controls remain exact", result["pass"], result)
    return result


def dependency_discipline_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    runtime_observed = {name: file_sha(path) for name, path in RUNTIME_PARENT_PATHS.items()}
    runtime_mismatches = tuple(
        name for name, expected in RUNTIME_PARENT_HASHES.items()
        if runtime_observed.get(name) != expected
    )
    runtime_manifest_sha256 = sha256(json.dumps(runtime_observed, sort_keys=True).encode()).hexdigest()
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    body = " ".join(note.lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "state-family", "off-grid", "nearest-neighbor", "all 24", "all 576",
        "tested four-copy coherent grade register has no objective-probability derivation",
        "tested finite rotor frequencies have no born calibration",
        "executed finite gate schedules have no time interpretation",
        "counted finite blank-resource debits have no energy derivation",
        "tested eight-m2 archive packet has no framework-record qualification",
        "supplied / derived / open", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "status: fail", "n1 gate: fail", "no axiom pressure", "cycle-597-local",
        "16 exact-pinned shore surfaces", "104 recursively pinned runtime-dependency runners",
        "cycle 595 supplies deterministic 8-address orbit enumeration and equidistribution",
        "not stochastic mixing", "reduced i/8 is a reversible dilation", "lfsr route is a narrow falsifier",
        "role/qubit block physical m2 boundary", "null e-g/leakage/layout",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    declared = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", note)

    receipt_checks = {}
    for cycle in ("595", "592", "580", "577"):
        receipt = json.loads(FROZEN_PATHS[f"Cycle{cycle} receipt"].read_text(encoding="utf-8"))
        receipt_checks[f"Cycle{cycle}"] = {
            "runner": receipt.get("runner_sha256") == FROZEN[f"Cycle{cycle} runner"],
            "note": receipt.get("note_sha256") == FROZEN[f"Cycle{cycle} note"],
            "cold": receipt.get("cold_transcript_sha256") == FROZEN[f"Cycle{cycle} cold"],
            "verified": receipt.get("pass") is True
            and receipt.get("tests_passed") == receipt.get("tests_total"),
            "authority_audit": receipt.get("authority") == "none" and receipt.get("audit") == "unset",
        }
    direct_parent_checks = {
        "Cycle595_Cycle592_alias": c595.c592 is c592,
        "Cycle595_Cycle587_alias": c595.c587 is c587,
        "Cycle595_Cycle577_alias": c595.c577 is c577,
        "Cycle595_Cycle552_alias": c595.c552 is c552,
        "Cycle580_Cycle577_alias": c580.c577 is c577,
        "Cycle577_Cycle41_parent_present": hasattr(c577, "c41"),
        "Cycle523_primitive_parent_pinned": "physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21" in RUNTIME_PARENT_HASHES,
    }

    routes = (
        {"family": "coherent projector-query tuple register", "object": "Cycle577 projectors and Cycle580 extraction unitary", "mechanism": "four-copy coherent query sector weights", "honesty_marker": "ATTEMPTED", "search_status": "COUNTED", "terminal": "derive a reusable numeric grade without supplied identical copies or sector selection"},
        {"family": "reversible fixed-point product synthesizer", "object": "unary parameter registers and 4x4x4 microaddress mask", "mechanism": "reversible literal products", "honesty_marker": "ATTEMPTED", "search_status": "COUNTED", "terminal": "derive the parameter-register/state calibration and expand family/precision"},
        {"family": "deterministic lattice rotor", "object": "one-carrier 64-cycle and derived grade mask", "mechanism": "exhaustively bounded +25 discrepancy", "honesty_marker": "ATTEMPTED", "search_status": "COUNTED", "terminal": "derive Born calibration, actuality, and archive renewal"},
        {"family": "full quantum amplitude estimation", "object": "phase/kickback grade register", "mechanism": "controlled projector reflections", "honesty_marker": None, "search_status": "OPEN_UNTESTED_NOT_COUNTED", "terminal": "compile controlled reflections, phase arithmetic, copy supply, and error bound locally"},
        {"family": "renewable stochastic reservoir", "object": "stationary local bath transition kernel", "mechanism": "mixing invariant measure", "honesty_marker": None, "search_status": "OPEN_UNTESTED_NOT_COUNTED", "terminal": "derive kernel, invariant law, resource renewal, and actuality owner"},
        {"family": "adaptive physical tomography", "object": "renewable calibration corpus and estimator", "mechanism": "confidence-controlled state-family learning", "honesty_marker": None, "search_status": "OPEN_UNTESTED_NOT_COUNTED", "terminal": "derive independent trials, estimator dynamics, stopping rule, and Record semantics"},
    )
    qualifying = tuple(route for route in routes if route["honesty_marker"] == "ATTEMPTED")
    walls = (
        "state-to-parameter calibration", "state-family and precision coverage", "objective actuality",
        "Record permanence", "frequency-to-Born calibration", "resource renewal",
    )
    pair_reasons = {
        (walls[0], walls[1]): ("a state-to-unary calibration for one declared family does not prove coverage at wider precision or for nonproduct states", "a wider-family synthesis theorem does not identify which physical preparation owns a particular parameter word"),
        (walls[0], walls[2]): ("a calibrated parameter word remains coherent data and does not select an objective outcome", "an actuality owner does not derive the state-to-parameter calibration used by the synthesizer"),
        (walls[0], walls[3]): ("a preparation/parameter calibration does not form a permanent readable Record", "a Record medium does not calibrate the input state's unary parameter word"),
        (walls[0], walls[4]): ("a state-to-parameter map does not identify finite rotor counts with Born probability", "a Born calibration would not by itself construct the physical state-to-word encoder"),
        (walls[0], walls[5]): ("a calibrated parameter word does not regenerate spent query copies or archive packets", "resource renewal does not determine the input state's parameter calibration"),
        (walls[1], walls[2]): ("family/precision scaling preserves a conditional coherent family and does not select actuality", "objective selection at one output does not extend the arithmetic theorem to wider families or precision"),
        (walls[1], walls[3]): ("a scalable grade compiler does not supply permanence, readability, or protected admission", "a durable Record law does not extend the grade compiler's family or precision"),
        (walls[1], walls[4]): ("exact or approximate wider-family grades still lack a frequency-to-probability calibration", "a probability calibration does not synthesize grades for nonproduct states or higher precision"),
        (walls[1], walls[5]): ("a scalable arithmetic family can still consume unrenewed copies and archive blanks", "renewed resources do not prove state-family or precision coverage"),
        (walls[2], walls[3]): ("an objective selected event need not be durably retained, readable, or protected", "a permanent packet can preserve conditional data without selecting which candidate is actual"),
        (walls[2], walls[4]): ("actuality of one member does not calibrate its long-run frequencies to Born weights", "a Born-frequency theorem does not identify the framework owner that makes a candidate actual"),
        (walls[2], walls[5]): ("an actuality owner can still consume a finite nonrenewable stock", "a renewable bath or archive source does not select an objective outcome"),
        (walls[3], walls[4]): ("Record permanence/readability does not derive the probability measure governing Record frequencies", "a Born calibration does not construct protected, non-reentering, readable Records"),
        (walls[3], walls[5]): ("a durable finite Record does not regenerate the blank medium needed for unbounded use", "renewing blank medium does not establish Record admission, protection, or readability"),
        (walls[4], walls[5]): ("a frequency-to-Born calibration can hold conditionally while source/archive resources remain finite", "resource renewal does not identify deterministic rotor frequencies with Born probabilities"),
    }
    pairs = tuple({
        "pair": (left, right),
        "left_closes_right": False,
        "left_to_right_reason": pair_reasons[(left, right)][0],
        "right_closes_left": False,
        "right_to_left_reason": pair_reasons[(left, right)][1],
        "independent": True,
    } for left, right in combinations(walls, 2))
    hidden = (
        "four identically prepared input copies", "two-bit unary parameter/state calibration",
        "blank pointer/copy/work/mask/archive M2", "finite 64-address chart and rotor genesis",
        "Cycle552 conditional member/history interface", "finite corpus sizes and held preparations",
    )
    hidden_phrase_classifications = (
        {"hit": "canonical sorted hash-map manifest", "surface": "Cycle597 note:131", "classification": "NON_LOAD_BEARING_CONTEXT", "reason": "canonical modifies JSON key sorting for a byte manifest and supplies no physics premise"},
        {"hit": "preregistered", "surface": "Cycle592 immutable runner/note filenames and historical title", "classification": "NON_LOAD_BEARING_CONTEXT", "reason": "the token occurs in pinned filenames/title; the current law's actual pre-held hash is separately executable"},
        {"hit": "registered", "surface": "one immutable runtime dependency filename", "classification": "NON_LOAD_BEARING_CONTEXT", "reason": "module-name text carries no premise or claim weight"},
        {"hit": "quoted scan vocabulary", "surface": "Cycle597 note N3 checklist", "classification": "NON_LOAD_BEARING_META_SCAN", "reason": "the phrases are enumerated as audit targets rather than invoked as proof steps"},
    )
    residuals = (
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md:190-193",
            "prior_residual": "three state-specific ROM rows were author-supplied from three known grades, with held family and denominator generalization open",
            "current_residual": "state-specific answer rows are removed only on the declared two-bit quantized product-state family; the state-to-parameter calibration and wider family/precision remain open",
            "exact_match": True,
            "disposition": "closed only for the shared state-specific-row residual at declared fixed precision",
        },
    )
    dropped_residuals = (
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_TI_INNOVATION_BATH_OFFGRID_HISTORY_TOURNAMENT_CYCLE595_NOTE_2026-07-22.md:70-74",
            "prior_residual": "the fixed denominator-eight ROM refuses new labels and cannot exactly represent two off-grid grades",
            "current_residual": "Cycle597 supplies lawful quantized approximations for one product family but does not exactly synthesize continuous off-grid grades",
            "exact_match": False,
            "disposition": "dropped as an exact-closure witness; retained only as a partial-scope N8 echo",
        },
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md:21-29",
            "prior_residual": "Cycle577's bounded elementary gate/layout and full-unitary-extension obligation",
            "current_residual": "Cycle597 reuses the already-retired Cycle580 query sub-block and does not close a new gate/layout residual",
            "exact_match": False,
            "disposition": "dropped as a Cycle597 closure witness; retained as pinned construction authority",
        },
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md:53-60",
            "prior_residual": "pinned candidate weights are not derived Born probabilities and select no actual branch",
            "current_residual": "Cycle597 retains the same Born/actuality wall and closes neither residual",
            "exact_match": False,
            "disposition": "dropped as a closure witness; retained as a semantic boundary",
        },
    )
    rhetoric = (
        {
            "phrase": "the tested four-copy coherent grade register has no objective-probability derivation",
            "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM",
            "per_block": "TESTED: one 18-M2 query and one supplied four-copy 72-M2 batch preserve all coherent sectors and supply no objective numeric selector",
            "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM",
        },
        {
            "phrase": "the tested finite rotor frequencies have no Born calibration",
            "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM",
            "per_block": "TESTED: five finite train/held corpora plus all 125 fixed-grid grade words and 64 prefixes have only a conditional frequency/error theorem",
            "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM",
        },
        {
            "phrase": "the executed finite gate schedules have no time interpretation",
            "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM",
            "per_block": "TESTED: finite query, synthesis, routing, and rotor schedules carry no clock variable or duration map",
            "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM",
        },
        {
            "phrase": "the counted finite blank-resource debits have no energy derivation",
            "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM",
            "per_block": "TESTED: copy/work/mask/archive M2 counts are resource ledgers with no work, heat, stress, or generator map",
            "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM",
        },
        {
            "phrase": "the tested eight-M2 archive packet has no framework-Record qualification",
            "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM",
            "per_block": "TESTED: one finite archive packet is written reversibly without permanence, readability, protected admission, or independent actuality",
            "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM",
        },
    )
    partial = (
        {"candidate_path": "scripts/physical_state_family_grade_transition_synthesis_tournament_cycle597_2026_07_22.py", "status": "EXECUTED_NARROW_POSITIVE", "what_it_closes": "state-specific answer rows for one two-bit quantized product-state family"},
        {"candidate_path": "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py", "status": "EXACT_PINNED_PARENT_COMPONENT", "what_it_closes": "the projector/instrument representation needed by a future controlled-reflection construction, not the reflection or grade register itself"},
        {"candidate_path": "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py", "status": "EXACT_PINNED_PARENT_COMPONENT", "what_it_closes": "bounded elementary layout for the existing instrument/query block, not autonomous phase estimation"},
        {"candidate_path": "scripts/physical_controlled_projector_phase_estimation_grade_compiler_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_it_closes": "supplied four-copy sector inspection and the separate calibrated parameter word if controlled reflections, b-bit error, E-G, leakage, layout, and copy ledger are constructed"},
        {"candidate_path": "scripts/physical_renewable_archive_actuality_record_separation_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_it_closes": "finite archive renewal and separately typed actuality/Record obligations if a physical renewal and admission law is constructed"},
    )
    steelman = {
        "mechanism": "compile local controlled reflections of each exact Cycle577 history projector from the Cycle580 elementary grammar, run b-bit coherent amplitude estimation into a reusable grade register, and feed that register to scalable reversible threshold arithmetic and a separately renewable archive/actuality apparatus",
        "supporting_authority": (
            "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md:33-42",
            "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md:21-29",
            "scripts/physical_state_family_grade_transition_synthesis_tournament_cycle597_2026_07_22.py:535",
        ),
        "actionable_terminal": "construct and held-test b=3 and b=4 controlled-reflection circuits with exact E-G/inverse/leakage/all24 layout, a copy/source ledger, a quantitative phase-error theorem, no supplied state-specific parameter word, and an independently typed renewable actuality/Record owner",
        "openness": "the controlled-reflection and renewable-owner components are unbuilt, so this concrete route defeats every present broad no-go",
    }
    echo = (
        {"prior_wall": "Cycle577 Route-B elementary gate/layout and full-unitary extension", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md:405", "retired_status": "RETIRED_BY_CYCLE580", "retirement_mechanism": "literal support-two elementary decomposition and cubic nearest-neighbor layout", "applicability_here": "the same compile-and-verify mechanism is applicable to future controlled projector reflections, but no such reflection is yet built"},
        {"prior_wall": "Cycle580 autonomous in-state schedule/recurrence", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md:21-29", "retired_status": "OPEN", "retirement_mechanism": "none; compile-time order remains supplied", "applicability_here": "a phase-estimation candidate must expose its in-state control and renewal rather than inherit host order"},
        {"prior_wall": "Cycle592 author-supplied state-specific ROM rows", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md:190-193", "retired_status": "RETIRED_ONLY_FOR_CYCLE597_TWO_BIT_PRODUCT_FAMILY", "retirement_mechanism": "one row-free reversible literal-product rule over all 125 quantized parameter words", "applicability_here": "scale the same import-retirement shape with an explicit error theorem; do not generalize beyond the tested family"},
        {"prior_wall": "Cycle595 fixed denominator-eight off-grid refusal", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_TI_INNOVATION_BATH_OFFGRID_HISTORY_TOURNAMENT_CYCLE595_NOTE_2026-07-22.md:70-74", "retired_status": "PARTIAL_ONLY", "retirement_mechanism": "Cycle597 replaces refusal by a declared quantization plus approximation bound, not exact continuous synthesis", "applicability_here": "increase b and prove scalable local resource/error bounds; exact continuous closure remains unclaimed"},
        {"prior_wall": "Cycle592 actuality, Record, and fresh-resource renewal", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md:367-375", "retired_status": "OPEN", "retirement_mechanism": "none in Cycle597; finite reversible archive debit is only exposed", "applicability_here": "requires a separately typed renewable admission/Record construction and cannot be retired by arithmetic relabeling"},
    )
    discipline = {
        "Status": "FAIL",
        "artifact_status": "PASS_NARROWED_POSITIVE_ONLY",
        "N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5, "N1_gate": "FAIL",
        "N2_collapsed_walls": walls, "N2_pairwise": pairs,
        "N3_explicit_supplies": hidden,
        "N3_phrase_hit_classifications": hidden_phrase_classifications,
        "N3_hidden_conditions_promoted": 0,
        "N4_residual_matches": residuals,
        "N4_dropped_nonmatches": dropped_residuals,
        "N5_rhetoric_resolution_ledger": rhetoric,
        "N6_partial_closure_paths": partial,
        "N6_convention_only_closure_found": False,
        "N6_new_axiom_required": False,
        "N6_primitive_or_control_plane_claim": False,
        "N6_campaign_control_surface_rule": "NO_GO_LEDGER, primitive registry, axioms, policies, queues, and audit status are read-only by campaign instruction; the full checklist remains visible in the Cycle597 note",
        "N7_steelman": steelman, "N8_cross_cycle_echo": echo,
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
    }
    result = {
        "expected": FROZEN, "observed": observed,
        "runtime_parent_count": len(RUNTIME_PARENT_HASHES),
        "runtime_parent_hash_mismatches": runtime_mismatches,
        "runtime_parent_manifest_sha256": runtime_manifest_sha256,
        "expected_runtime_parent_manifest_sha256": EXPECTED_RUNTIME_PARENT_MANIFEST_SHA256,
        "receipt_checks": receipt_checks,
        "direct_parent_checks": direct_parent_checks,
        "synthesis_law_sha256": SYNTHESIS_LAW_SHA256,
        "expected_synthesis_law_sha256": EXPECTED_SYNTHESIS_LAW_SHA256,
        "held_declaration_sha256": HELD_SHA256,
        "note_missing": missing,
        "declared_runner_sha256": declared.group(1) if declared else None,
        "runner_sha256": file_sha(Path(__file__)),
        "discipline": discipline,
        "inventory": {
            "supplied": hidden,
            "derived": (
                "exact coherent projector-query distribution and inverse",
                "one row-free reversible denominator-64 product-family grade mask",
                "deterministic physical rotor with exhaustive finite discrepancy certificate",
                "explicit approximation plus rotor-frequency error budgets through conditional occurrence",
            ),
            "open": (
                "objective actuality and framework Record", "Born/probability calibration",
                "state-to-parameter ownership and family/precision scaling", "copy/archive renewal",
                "time, energy, source, stress, gravity, noise, and infinite-volume integration",
            ),
            "physical_M2_boundary": {
                "Route_A": "only exact-pinned Cycle577 dual-rail plus Cycle580 elementary-layout composition",
                "Route_B_C": "only exact-pinned Cycle587 basis-state compiler plus recursively pinned Cycle523 primitive dependency",
                "unverified_role_blocks_promoted_to_physical_M2": 0,
                "unverified_role_block_EG_leakage_layout": None,
            },
        },
        "pass": observed == FROZEN and SYNTHESIS_LAW_SHA256 == EXPECTED_SYNTHESIS_LAW_SHA256
        and not runtime_mismatches
        and runtime_manifest_sha256 == EXPECTED_RUNTIME_PARENT_MANIFEST_SHA256
        and len(RUNTIME_PARENT_HASHES) == 104
        and all(all(checks.values()) for checks in receipt_checks.values())
        and all(direct_parent_checks.values())
        and not missing and declared is not None and declared.group(1) == file_sha(Path(__file__))
        and discipline["Status"] == "FAIL"
        and len(qualifying) == 3 and sum(route["search_status"] == "OPEN_UNTESTED_NOT_COUNTED" for route in routes) == 3
        and len(pairs) == 15 and len(pair_reasons) == 15
        and len(hidden_phrase_classifications) == 4 and len(residuals) == 1 and len(dropped_residuals) == 3
        and len(rhetoric) == len(partial) == len(echo) == 5
        and not any((discipline["broad_no_go_claim"], discipline["minimum_content_claim"], discipline["shared_obstruction_claim"], discipline["axiom_pressure_claim"])),
    }
    check("exact shores, rule-before-held freeze, inventory, and full N1-N8 prevent state-family and Born overclaim", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_result: str = "one reversible row-free denominator-64 product-family grade synthesizer feeding a deterministic local rotor and unchanged conditional occurrence"
    objective_actuality: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    physical_time: None = None
    energy_or_source: None = None
    axiom_pressure: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle597 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c = route_c_controls()
        covariance = covariance_domain_controls()
        dependency = dependency_discipline_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["maximum_RSS_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "route_A": route_a, "route_B": route_b, "route_C": route_c,
            "covariance_domain": covariance, "dependency_discipline_inventory": dependency,
            "resources": resources, "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print(
        "authority=none; audit=unset; tested four-copy coherent grade register has no objective-probability derivation; "
        "tested finite rotor frequencies have no Born calibration; executed finite gate schedules have no time interpretation; "
        "counted finite blank-resource debits have no energy derivation; tested eight-M2 archive packet has no framework-Record qualification"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
