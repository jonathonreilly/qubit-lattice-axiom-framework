#!/usr/bin/env python3
"""Cycle602: transported-observable Ramsey / echo / event-rotor tournament.

This runner preserves the finite coarse-algebraic L3/L6 constructions only.
It does not promote Cycle590's conditional 53-role blueprint, detector arms,
echo controls, or one-hot rotor bits to physical M2 sites.  Update ordinals
and event counts are not time; wrapped phase is not energy; copied bits are
not Records.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22 as c599
import physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22 as c590
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451
import physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22 as c570


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TRANSPORTED_OBSERVABLE_RAMSEY_ECHO_EVENT_ROTOR_TOURNAMENT_"
    "CYCLE602_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_SHORES = {
    "scripts/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22.py":
        "7077c58b7c41f59606c8a5ccc0135017d937a0dd24184c083fa2df5b4b435840",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_CYCLE599_NOTE_2026-07-22.md":
        "d4c783fd5ab2134f8ece136af8c91ce6827000f9c63a3c0c057af16040f1fc6d",
    "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_receipt_2026_07_22.json":
        "95fe87ff5bb56151a2cc5c979fa0720a7aa4ecb33ab6da75c2e8b3f83ac495f0",
    "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_cold_2026_07_22.txt":
        "c25c292c1ac5ba81f0139d6795990872312f371b997b076135345c7235e44803",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "43e5b749702fba9551fab43a242f832b824fdbff54817b5206097f02ad146e55",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "f0f3ed6d41132625b8907cbcda8f105b7ec975e4b952562b45fe5b7d8e1b3a0e",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "3ae94267d43a668a178ef02ee37ab12608f302419a25b0a37deffd27e51be647",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_cold_2026_07_22.txt":
        "cef70862eff7d6f10d562a67e2e8fcab503b998de5e0dea63300f0883efe398f",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":
        "37e9d0f336d773bd4a1957a6531f80dc35b9673a4ef0f99137e7fb33558bf849",
    "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md":
        "e88ee3daee2e07f215142d29cee7e6e5d3564bf5f92764aca49e89fe8f065438",
    "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":
        "f9295faa4230427623ac350625a42fb17949fd86f523b6cf81aa247c14dd796c",
}
RUNTIME_DEPENDENCY_HASHES = {
    'ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17': '5adb6dc52f6352a5367a2b56da94854e511f9dd174688029f1841e5004a91c32',
    '_frontier_loader': '64ab743a7888d6eb32ff2d72ddab846633f49a818080f9c2d88330961c96d86f',
    'active_cubic_source_response_cycle211_2026_07_16': 'd5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6',
    'archive_carrier_source_ledger_cycle227_2026_07_17': 'a5e78e40cad0c43ee62ae887df7d84a0b895ab217ba4f3d521353e5d0b6bf95a',
    'autonomous_cubic_field_emission_cycle214_2026_07_16': '464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4',
    'aux_gated_candidate_transport_cycle95_2026_07_15': 'e062efafc14825213cb53b65d4d7d5280132c4cf131da595390ffd9b905bcedf',
    'auxiliary_pair_completion_gate_cycle54_2026_07_14': '27706e892ad6bac2b56353a807e1afd0339d1961f5bacf3803f1a5aa86dd3758',
    'binary_xor_and_record_alu_probe_2026_07_15': '2cfa7066aa355406ca8a5939c7fbe3d06f0ff52c6eb3deee1d7dd79eaaeec30a',
    'car_compiler_record_causal_depth_bridge_cycle255_2026_07_17': 'bda594894278f0969e168d5df72c2f58e4d1893a5018237fd451a6ecb8e328c7',
    'carried_internal_species_source_field_ledger_repair_2026_07_17': '5f8eb68522fdcc7267d10a8d0bfb8ea099696a165d822464671b41791426caf1',
    'causal_impact_parameter_probe': '76c00d12ba62273db36eaccc7cf6d4f946accc9b4991efb750258e746ac81f53',
    'causal_propagating_field': '1b776f25ed7192464cb1e60f80ec4865d48565ff0b4f85b50aa489bcea64252b',
    'clock_as_commit_count_and_rate_classification_cycle22_2026_07_14': '7f41a33567f4b6c14ac23e28f82b9f99fb4e329d66b4d4d13cbf83cd83629f31',
    'coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19': 'c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4',
    'common_cubic_transient_stationary_update_cycle425_2026_07_19': 'c3aa51528e54c28b8b258d83d254068430d3b1816a03aafefabe4be3ef6a84c9',
    'common_matter_field_coin_family_cycle219_2026_07_16': 'ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a',
    'completion_barrier_phase_transducer_cycle67_scratch_2026_07_14': '67c4f2ff5ba5bb2242aa99e1d754b64617a8fde5c0fa4dabb0a346b2f242b008',
    'connected_edge_autonomous_apparatus_law_cycle282_2026_07_17': '593cbe91303bd6a04b56b67dd030968de54aca7ba0a565f2d50086a7faac33cd',
    'connected_edge_same_code_local_instrument_cycle278_2026_07_17': '2d0e46f1616618a5b95e81c47c7282c17e2b377799eab4fea37fd923bc6bb22b',
    'contact_close_typed_record_dag_cycle287_2026_07_17': '9f4d2a6fe11648698dc4617e2f7454d9cf3269400edc5e0b94dae5be3eec8553',
    'contractible_lightcone_wilson_quotient_cycle271_2026_07_17': '4f42313db4c505cfdc3ff00f5f95b05e4181f372dcfca37cba0d1fb0c8fab84c',
    'cycle189_record_corpus_frequency_bridge_cycle194_2026_07_16': '10cbf5029bff31dd7977f1529774f550445c6df5ec98724c3610fdd1a9fb9b25',
    'cycle416_seven_m2_common_code_seed_cycle418_2026_07_19': '5aef256df3ef5f1d919df807c1b29083d6f49fd40ca1ab83e27aa828ffa71d06',
    'cycle48_clifford_transition_compilation_probe_2026_07_15': 'f8befbb884b1a0e324bf37be901897423690f2232a3bcb35c7d712634bcfbabc',
    'cycle48_decoder_clifford_bind_probe_2026_07_15': '8d29d625e2d8a183522fd8075131534a164cbcdd1fc1ade68fbf58628bc3aca1',
    'cycle48_four_generator_tableau_row_machine_probe_2026_07_15': '2bf3f22b41409ceb7fc74b6367d04ab21578287495a426587a9d67d4e8c2ee48',
    'cycle48_pauli_luders_update_compilation_probe_2026_07_15': '6acc8fa908a5656d6008407322d62d04845b4e8d52bbfcfa2cab7a3904bdfbee',
    'cycle48_physical_tableau_row_gate_probe_2026_07_15': 'bca5ae655597a4d48c219ed0bf305671f56b119ff822950498318c5747c10ffd',
    'cycle48_six_bit_local_decoder_compilation_probe_2026_07_15': '7ffeeed08ca8dce0847031d0bf3eb921fbfeea5f3847318e9c681fd45d1db12a',
    'cycle48_symplectic_tableau_compression_probe_2026_07_15': 'cb011beb0d67352c545091faeb436c8fdecd0005c17c7e2b676b5e76377e488b',
    'cycle48_unified_clifford_luders_machine_probe_2026_07_15': '2b53d477dfa2a8154af30c34c4455fcb51284f3109abf855b1f0f127b3f70377',
    'cycle60_cycle67_mixed_composition_audit_cycle70_2026_07_14': '39e0d59d19b856527d44d6d485305a15f9255efe13eb1ae824f6cfa55ceceee2',
    'cycle67_terminal_bdh_rebind_cycle72_2026_07_14': '43513a76f3d652cc95774446a7834dd8bb4c4402e55a57e62f3e6ce07752719c',
    'cycle80_recurrence_audit_endpoint_tube_nucleation_cycle85_2026_07_14': '77a3115aa8b8082b683be0c56754cf4911a92b54b9d8272ea226583c6a5af56b',
    'diamond_ideal_lockin_detector_theorem': '3615fedb25de4c93fe2ae49237c7712da11823de126d60a96cf15ce437715bcc',
    'direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17': 'de0ca25ed5540e5e956a96b6b144934b1483d625e08b7b2cad569fcf2edd1be0',
    'directional_multiword_rule_port_output_cycle82_2026_07_14': '0faa54f62384312d40b910a43a865f46ff4f351e68127c56a6c3af7ac49a994e',
    'eight_bit_physical_role_comparator_cycle81_2026_07_14': 'd9648da97499db1743bb6ef398b73c61897ae942233bbc25cf8394040622985e',
    'eight_bit_status_completion_front_cycle112_2026_07_15': 'c5c0b2ab4d1f93dd0c6eb83742dda7e99ef14d8d7650fd3aee6f18bcfcd2285d',
    'evolving_network_prototype_v6': '5394010a8162963ce6c88171582c53ccb226a2c524439e6287eae9858bf45c7f',
    'exact_3d_higher_form_bosonization_cycle235_2026_07_17': 'dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34',
    'finite_coin_scalar_wave_dilation_cycle215_2026_07_16': '3a977106389428d2281ea7e0e32b65fe57f6ce33d783742b80f264f78f4f2c17',
    'first_autonomous_successor_role_port_cycle115_2026_07_15': '1ca673dc3086bb3de29ac5d67f3850b1a35c15c33236a4239104cc08152fa38e',
    'first_role_differentiation_cycle56_2026_07_14': '82090ef34aabfbc8fc052260f895b249cf64fcc8088028ea5b9719141121408f',
    'first_self_grown_selector_payload_bit0_cycle106_2026_07_15': 'db34621df805b0cd3e4b764420b706d42badf3990becdf7efeab7616e0c00a6d',
    'fock_modular_boundary_current_cycle229_2026_07_17': 'fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7',
    'four_open_reservation_comb_cycle59_2026_07_14': '63c864ecf4f2796f61917a74bbec563030cb83df91c4e136382adcb3aaa6fcbd',
    'fragment_safe_role_remap_type_integration_cycle108_2026_07_15': 'e6c3e1c4e74d06df6aff0fb5a8e67357b8ef749e2c30f043acb5f55eec517e52',
    'frontier_oh_schur_boundary_action': 'e8e375a14f750162e6bbed56c51bf91473538b428dd333f5d491a16f9753c891',
    'frontier_quark_endpoint_readout_constraints': '9e4ec1b42cf84f49922a29c50eb4c1a49ae3877b640b14fe8485b54c1e35a1db',
    'frontier_quark_route2_exact_readout_map': 'e4356c7079bca9a0ded2259d0f49cf9461bc16ba7e09cf688c78de3a56e2328a',
    'frontier_quark_route2_exact_time_coupling': '80ef53bb60d7f691e64596932118d98e6b0a49b000e95fecb653adc6f0031029',
    'frontier_same_source_metric_ansatz_scan': 'cc0e24b12c6ed6a389cbff9b03e06754380103d8aca9d3b7903fddc3b1195b94',
    'frontier_tensor_support_center_excess_law': 'c5cbe0a90df79c0207e9882d63e6c7081d667d47a6158f84ce85622aab3c5e7d',
    'full_a_boundary_launcher_last_cycle57_2026_07_14': 'cf7b38a9b92f1d60d354ec72bc2a5aa86a550ecdf25754e967aa5401f14227f5',
    'full_fock_unit_weight_two_source_cycle325_2026_07_18': '32ee958fe9dc5f5c5aa41b5593cb66a529d7ae07ca8b556cff2b45f7f33374dc',
    'generated_beta_phase_register_cycle220_2026_07_16': '252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f',
    'generated_endpoint_autonomous_frame_rail_cycle102_2026_07_15': 'a5744a55e3183e1d3b8233e0cab51c8c554cc9a55ae7a735c1d7b3cf40075d18',
    'guarded_bridge_recurrent_contact_history_closure_2026_07_15': '606972c386178defa1b0b35335a9bdcef9dbcc1b76e1215f02e638bd355402da',
    'guarded_cycle129_bridge_history_probe_2026_07_15': 'fc6055bace69612488131b6b2a40790f823868ccb96d0a1da7eb658535ed3f45',
    'guarded_physical_word_to_recurrent_root_history_closure_2026_07_15': '73b41d674ab7638e7426d0cebe4ccd9fef95c35919ae1e83e4bc9f853fb0092e',
    'joint_endpoint_bdh_rebind_cycle63_2026_07_14': 'e5f775b42cc5f330bc36ec7e2387bed8c8a7af1ae8cccc70be5aa711043fca13',
    'joint_endpoint_mixed_rebind_cycle78_2026_07_14': '8f413701838eb0f6eb4ec6455048d38646cffee661c5274359698f089d277b9b',
    'launcher_last_first_role_differentiation_cycle55_2026_07_14': 'ab6c98d2e92bf8f6724c7011ab948ff9ca094a5347653bb9b974c69d0e2b90ca',
    'literal_bit_alu_symplectic_commutation_cycle150_2026_07_15': '199d9ea4f1996e52c818244f179256d05ea6465a3cec3f7fe633579bb3101f93',
    'live_directional_program_writer_cycle90_2026_07_15': 'e3a6080ca902b4185fa85f436bd132b34e6f9fc77c04f0fb92a4886dd4146c9a',
    'live_eight_bit_physical_comparator_cycle89_2026_07_15': '4f08f2a88a5f6cbc159ff023607be8504160496c4d4f17b8b280a43f7a47fd47',
    'live_seed_row_readable_macrostep_cycle94_2026_07_15': '30c6cb42c027b481f823170fb6ae077dc7c7c008d35dd7a55f28f9a7adfea448',
    'local_conjugate_reservoir_source_field_ledger_repair_2026_07_17': 'fbb0305f2892db64a878799c053cdab19385144306038b49fdf632828a0e4181',
    'local_conservative_commit_resource_gravity_cycle9_2026_07_14': '4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6',
    'local_generator_source_tournament_cycle228_2026_07_17': '97fdf54189d7da93099aeab4a9b1dd8501c7262d55493b9fa95bf1c2f5c97a9d',
    'local_rough_puncture_odd_sector_cycle247_2026_07_17': '10f5cf027c76f5a0a3b1d3dbaa6cb0e6d418932c84553f0cca303d3f21742519',
    'locally_matched_wilson_sector_states_cycle275_2026_07_17': '7d3140b406309b73ee6d246d559777c703b3fac8cd2b922ce5acdebd6aaa0918',
    'matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17': 'd047501d1f02e91a35b4b7c5dad67ec1f679c3c65fb2ad047906d7e5c59dbc76',
    'mixed_cycle72_guide_repair_cycle77_2026_07_14': 'a66e0840f183e47f0c444392e0512d94947dc0ed133a05300f96a6f7298f79c5',
    'monotone_fat_phase_shell_cycle62_scratch_2026_07_14': 'b445e414126cd6cbe958dd4797dfbdf62d8f050daf12a3aa2b880795a2dda48d',
    'moving_source_cross_family_probe': '6b1422ef6837570deb469351a10c5dd86c3b3cdb3adee749a2e09c746a029456',
    'multipole_tidal_response_probe': '8118df420c2b2b2ba14494908e60c2000c1fd1fd834b52bba7d43f5c5f1d10c5',
    'official_seed_to_rail_nucleation_cycle53_2026_07_14': '32484389e8654d9f4d4034a4ed2a79309d77bb80faa256efa0803b2d3e4497e3',
    'onsite_alphabet_closed_frame_rail_cycle104_2026_07_15': '4c1f17391113e0a6e217e653d9c34c727f99f73fb1d675f7ff14ddd7b7688459',
    'open_direction_empty_slot_cycle86_2026_07_14': '42bc9425d9194f71891913bc7548aeb3fdb4d83cbf4eb29a2a858d99e023c385',
    'open_site_reservation_handshake_cycle51_2026_07_14': '151a25cd39797c361edf075202a1e71c9d52b32e88463c9982e76649d7a05503',
    'operational_binary_macrocode_compiler_cycle58_2026_07_14': 'c753b4cb8c544c51f50e3f48bd1c8c3204a778aa6f349db1379ed300a0bb6c73',
    'operator_mass_equivalence_cycle221_2026_07_17': 'be509eabb836e2365a4acdfc5e245c13335c42ee93d34033654eda4ef2904015',
    'outgoing_carrier_nonrecurrence_cycle286_2026_07_17': 'd1ccd54f870399696b37797c5a44d05066f72948ce2b5f983014975b33c97fe3',
    'phase_port_preserving_comb_cycle60_scratch_2026_07_14': '616d57dfd96e614b232f35516dc39399d8841ff43a7b5e30fe29bca5eee896a0',
    'physical_absorption_event_record_time_bridge_cycle424_2026_07_19': '37108dbc8339977a2b41b18d7018ac673f78e1d34d0a3e04a5e92d062dec2376',
    'physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21': '5830dacebf79720301192b0dcb39121e1ecf03137f94d6e97c7da4034d9c9ca0',
    'physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21': '8f505d2de6476bdbc20f87a901e8be9fe46deda5b568c98d750977069a352e53',
    'physical_adjacent_two_star_order_character_preflight_cycle517_2026_07_21': 'ad8b0c71840cbfa56aae3ae9da44eceec1cad7d84be06bab32604eb5f6fbb4a3',
    'physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21': 'd2e0648558fb3031a200600b0643de28a5c8e695c35165a6905a6a99ff45255d',
    'physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22': '0c845ecd02b86ce4d99aa8406a206e9b01628f02f1592cf37c41a084eb1e0a4b',
    'physical_autonomous_record_dual_front_rendezvous_nn_route_cycle353_2026_07_18': 'd062a229d268ac54edebe664feed0e8dc70683b5e2dff3675f119d8204d901b9',
    'physical_autonomous_record_lineage_residue_nn_route_cycle352_2026_07_18': '83bfaba8d9d5f4e5507ee2d4a840be435d30c222af37542a5a19ad1d0f5ccdbb',
    'physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18': 'a88b16a7af9938cda209537750ab9bfd58b16b0f3896c53419f3b030e8fbc19e',
    'physical_autonomous_record_payload_continuation_nn_route_cycle356_2026_07_18': '3921b1a28f55fdb5a3311e8496f8d2fe4d73a49e017ec5f0d03ef42e060bc677',
    'physical_autonomous_record_payload_faithful_close_nn_route_cycle361_2026_07_18': 'cd4bbf4278e16e046fcc3d2a5e959b410ebeeb182428c32ebeb8cea96783d093',
    'physical_boundary_aware_multistar_recurrence_tournament_cycle551_2026_07_21': '3d68e536565c491b1b54547d82ed6faab73437c600229ff9060f471ffad84997',
    'physical_case_role_isolation_cable_probe_2026_07_15': 'c989be91ffbce27da1c6b3e2c75325cab5eefe7d9afe4b01fcc2437adc3549d3',
    'physical_coherent_receiver_source_injection_cycle417_2026_07_18': 'a359d119d97d74b6ff6d7eff495fd48d040ba41645ed90c472ffcd1fe05d5732',
    'physical_commuting_row_multiplication_probe_2026_07_15': '276d8c3786bcfc119aa1d9187e36f2056493be64bf14f640a8786164beb14cd2',
    'physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22': '21957cc883550ee81fc48d5b55ad4a0384cbac8697557691c805d84c7c8dbaaf',
    'physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18': 'e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10',
    'physical_correlated_double_shadow_stream_cycle529_2026_07_21': 'df118a01c2a95fcccd7986dc01afb5625d0faa8bb95beb2ecb344a9f5fbacda7',
    'physical_cycle269_coherent_cubic_pair_orbit_2026_07_17': 'a5998584cdc19612c11c5b70399183ea3fa5c3f99d60f12aa989dbd3a87bbcd0',
    'physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17': '39c60c3ca2e7525a3a42f058df02a4b96e63f2bde6d54c042a5ec95a4ff3f9c6',
    'physical_cycle269_collision_safe_auxiliary_ports_2026_07_17': '03786effa03eae50930ca0bfa14c881276df8bd6bdba83b6d7a893cffe1fe747',
    'physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18': '4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c',
    'physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18': '0688e7db8b8490e525c0e1f1108474903e2ff40d278e185b6add54f8086f8110',
    'physical_cycle269_four_cell_star_cycle324_2026_07_18': 'f2e07bf91e7a5b06c8037314798cb84cd6d747bc92fa6292c1759915fb91354d',
    'physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17': '3e970b2c84ebe891d36c132cd99d716ceb20b596cea89729f06ed8950c7a847c',
    'physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17': 'cb6de428c5054ea9415a59bab75d36c693c65d8070df30a6a0bbc2a926f3f4e4',
    'physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17': '393de6368fe127a8d0e85b8a52a504585b53c09fb9ddfced5fe7b9079f26af92',
    'physical_cycle269_local_contact_intertwiner_2026_07_17': 'ee42959d75bc09dfc7f1ce1ef4f19f50a2363b5d142efd8f5f8ebb20519bef3f',
    'physical_cycle269_local_fock_extension_cycle312_2026_07_18': '0aaab171ac23b28d8e6daa583e2e256bc872f971ec7f282898edea726d96ccd8',
    'physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18': '52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3',
    'physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17': '5c2030ef6a33906792307710a9fbfea02f0551574962c6e60cd04c42e5a62a36',
    'physical_cycle269_reference_relative_localized_pair_lift_2026_07_17': '95820817eaf883040aae96531f1afd4fe7a90569a43215d226cf44dce9a1cc09',
    'physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18': '4428d1f73ff315987edabd7f838a1c58414d0a982f0cd28656ddef3bd230d19f',
    'physical_cycle269_staggered_reservoir_catchup_2026_07_17': '5310ee8e19a55694f7a11ccf013c696b16cdb37961c5ade41ed316b27238bab1',
    'physical_cycle269_three_cell_multiedge_cycle319_2026_07_18': 'faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb',
    'physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20': '93afe1600cb3fb8b7844729521b005ce62f957a128a6ffb9493a03a1d9932e96',
    'physical_cycle515_koszul_frame_bridge_cycle516_2026_07_20': '3c4318a84c661893932c8d41a90db36445f80cefd092a6a3fffb56cbf8abfa9c',
    'physical_detector_record_clock_map_candidate_cycle428_2026_07_19': 'd5a130d6d9a03205e4314fadd0f35f180b260920a027f5c6cc0aca5a2e910439',
    'physical_effect_equivalence_normalized_grade_cycle321_2026_07_18': '77f46e3784274ee0dfafd610f2d9aca7a5edc836e94324b698689369574c4fd4',
    'physical_endpoint_registration_process_route_cycle338_2026_07_18': '3d292cf8da5922d042281057e5a38edf4d020c02483f268970232c95aa4e7ab3',
    'physical_environment_export_realized_member_bridge_cycle334_2026_07_18': 'ba27c3b6353f1ecb6f12d3b7feb4d5860a0acce85bbf58a0c2ad8bc90394d0ab',
    'physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19': '75a7f42ebbea25702474b8856413cbc2bd4c5e37d8d04b8ccf7e3b4d86f50262',
    'physical_event_to_append_commit_candidate_cycle326_2026_07_18': '8762609f9e9e85fb9311ed467bbc91fd5905f2ac5d160997555e8623c5e7f44c',
    'physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18': '082d9619fada5a80a0214a10504b9f2496a604b01db5bdeffa25586be738b67b',
    'physical_fixed_program_carrier_two_use_cycle323_2026_07_18': 'a7c709677344faf187aa223d79ea8e3ea5ea7ef4566ef951297a6a17d62a5511',
    'physical_four_case_pivot_router_probe_2026_07_15': 'c1b8f33d5df6e26463fd258c1d524062c642d3e03310799c7659eb3c8df90ea2',
    'physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22': '43e5b749702fba9551fab43a242f832b824fdbff54817b5206097f02ad146e55',
    'physical_global_N3_returned_slot_compiler_cycle560_2026_07_21': 'f6d641e4735b26f9463ea623ee8ed6e28acc995fdfc88300709dcfac100c13ab',
    'physical_global_selected_network_encoder_cycle555_2026_07_21': 'af51110e8c4cb5245efd2bd99ef7f2b12fb02586c5e5225082ce4a13fba27e92',
    'physical_held_sparse_order_retirement_cycle563_2026_07_21': '55e51cafffa70284a6e8e1f0510ca0d2f890989ccbcf5bce64435df4c8e812a6',
    'physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22': '2a3c77c26003bb0f8b55fe2da0fd36b0ac98a14a21a083303fe175e5f802e99f',
    'physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22': '7077c58b7c41f59606c8a5ccc0135017d937a0dd24184c083fa2df5b4b435840',
    'physical_isolated_row_mux_common_output_probe_2026_07_15': '509fac65df227243c067521cca1f162cd78d80a88a4fed7fa0de92a15fa53be5',
    'physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22': '37e9d0f336d773bd4a1957a6531f80dc35b9673a4ef0f99137e7fb33558bf849',
    'physical_joint_stabilizer_update_geometry_probe_2026_07_16': '3b119be91e990fd5775de721a59c33f21fc024fd2b85ec10451e367f2e48d90a',
    'physical_literal_bit_cable_probe_2026_07_15': 'ad837f638d938cc62997a9809e7db03d383b0601ea1c58f18f779ddd7640bf6e',
    'physical_local_N3_six_ray_decoder_tournament_cycle557_2026_07_21': '8b153c0ec633d489a839221788115ae85c6bf80c4d4952339795aa7bd80150d8',
    'physical_m64_reversible_event_sidecar_cycle314_2026_07_18': 'c9fbdc70d1d80da008cf8ff3f43ebb158f54f6ba731b9ddc65e643f54f26618a',
    'physical_mass_clock_active_source_receiver_tournament_cycle438_2026_07_19': '1e332e66d986fbd1083ab67ecb117dfc0e1c9cacc9d66696b3dc687eba2fa8f0',
    'physical_mass_source_echo_lapse_candidate_tournament_cycle445_2026_07_19': 'dd84bec596ec6c7ac548593c2f3e57f26cba601639c2bf4f156c46c21551b91d',
    'physical_matter_inertia_clock_composition_bridge_cycle437_2026_07_19': 'a0402b99ee36e96b9f9b150de315e3b9b7be23d3d6b53a8b0f5bba22451f240a',
    'physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22': '52c743889146189c2b574fa8012e7281340722303cb5b61fc53579e5fe23ebf4',
    'physical_named_record_interval_direct_matcher_route_cycle344_2026_07_18': 'eace13a58bb916f649bb4f8b092d7f7b2fab4c8ab4e9d426dce54df1b1ff0d75',
    'physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21': '2ca2021fa76b889128b587a6a0d67986e236319ea8fb7ccd1dfaf31982c55fa0',
    'physical_nn_functional_source_control_compiler_cycle446_2026_07_19': '26a4648a2809b650a62b7f2a97c60e67eac1b5e8cdca2826555b24acef1cb207',
    'physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19': '7ce3fa050d00e6cc1f6b0b2f21f487a9bf70add0a7f2ca3837c0be7ecb98b3a1',
    'physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21': 'd6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b',
    'physical_opposite_carrier_shared_cell_recurrence_cycle525_2026_07_21': '379c67315de8d235f8d5287b281b6291d0a10731d030338d8bde0676a4c0b785',
    'physical_ported_symplectic_row_fanout_probe_2026_07_15': 'e0f0a2729e81fd107faf079429c8429f8f534e22b3e48600c6256810677e5de5',
    'physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21': 'd9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d',
    'physical_r_b01_generation3_safe_prefix_scratch_2026_07_15': '914ee13d084472cb6f188864c39d5663ad20fdbe57d9d958b5caf3a6a768859a',
    'physical_r_b01_recurrent_root_bind_cycle144_2026_07_15': 'c7af211a36cb2c654fd67835379b22b8af480f190f0ebf2e9a12727685bf7cd5',
    'physical_r_b01_safe_prefix_history_probe_2026_07_15': '07c96da2d41a4204e123d6094eca945ba3034771484165e5fa5e2cbe5b9aae43',
    'physical_recoil_hard_core_field_bridge_cycle426_2026_07_19': '1001fc29d3e230ed55a0c973cdf5c598f75c72a6ee6b916a56eeddfdaa0a599e',
    'physical_recurrent_shared_volume_compiler_cycle545_2026_07_21': 'b117c595f8c06f79931be98d573168e53d9f0fb9d5024e4ee623ba76d7488067',
    'physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18': '22d5391c35b9b9d08c08bb44614fe24147181600df9a41a656fd5ea18950275a',
    'physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18': '4413c729325038deeebaac17d751b398e9e225e1c383cf80e80954df874231da',
    'physical_relational_actual_history_member_selection_cycle333_2026_07_18': '5c5e96ba6373c7ffb0dfb0905f37754d9c24262808b1ad6d43f160eb308ff51c',
    'physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21': '53b003bbda96eee1d85e48aa5cd0e8c530bea35c7b6eefef5a637127f66af13a',
    'physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21': 'a768d4250e55399c03e6084614a772953e6bcdf1570b9e7c50ac8d18544cfe6a',
    'physical_row_reader_payload_tap_probe_2026_07_16': 'f2093eba026401f09732789e33f9d9e2cc717092f79fd3b7cf4a265d6e6e04b9',
    'physical_row_role_fork_cable_probe_2026_07_15': '8a90f4442036912ffe53e6c2a6c3fbd7da4cabc3556e9dae7cf569a6e74f3711',
    'physical_row_role_literal_fanout_probe_2026_07_15': 'baa8aa635923053ad89c39365366ae3caf50a16082f88c6743019ff52bcd0f41',
    'physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21': '72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd',
    'physical_selected_seam_event_current_adapter_cycle526_2026_07_21': '7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd',
    'physical_shadow_normal_form_sync_cycle530_2026_07_21': 'f5f90a331803a43d293fa8e8e3640e29886bed81935827763773d84f61ce9c99',
    'physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18': '70d9c20fcbe9161c1a98c36c21b0370140ee785b32fa73eb4bd709c1eb983a95',
    'physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21': 'aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1',
    'physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18': '4fb41afc5067849689a958697d986962eab32ca6549199b046519e3bb48d8920',
    'physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19': 'c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1',
    'physical_source_prediction_bridge_contract_cycle420_2026_07_19': '79eca68ca217277fa237d2420888b64ef7bfba801e8745925a8dfb14b7576d5c',
    'physical_source_response_actualization_law_tournament_cycle403_2026_07_18': '2cf352a051d50667168d3e6d72d4388d107784b37be692e38f17b4a0828f4987',
    'physical_source_response_record_counter_interface_cycle399_2026_07_18': '4d86e2323d25a73a5ee417b7fa674dcc5542a0f0363979dda330b0e7d30ce4f6',
    'physical_strict_response_source_clock_metric_receiver_cycle416_2026_07_18': 'ba99d29160f12d1133d9c5d8ec5a04f853ba20fb25f67d5f1b5f1473773f08c4',
    'physical_support_matcher_predecessor_controls_cycle329_2026_07_18': '2cf6370f72cd4025fcfba8f0edefff1c577ad2bf5c5b93f996ef23c5affbab0b',
    'physical_symplectic_commutation_circuit_probe_2026_07_15': 'f35ea371d6b8fbe85a6db69317fd9a9048fe8b9151752c9b64c05f2fdf8f9169',
    'physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19': '75362f83b6de34c6c3f5e9aebe280ac083e76679c9f96fe6388f700e50d28564',
    'physical_three_row_dual_commutation_bind_probe_2026_07_15': 'b5ded7eb96ccec140e18af1a1daf67e22ddaa48c87b87634bf7bb0661a660bfe',
    'physical_three_row_spacious_commutator_bind_probe_2026_07_15': '2bd6699ed1a883d2996def716f6a9099db1bd2eb18403f7db625a082edd9f507',
    'physical_three_row_spacious_isolated_pivot_probe_2026_07_15': '4ceb7b63b37e283f02629929765104bc58581fd3882cb791a43659a4c35320fa',
    'physical_three_star_shared_parity_overlap_cycle520_2026_07_21': '22b00fd39fd07a04afb8776f4b97c31486ce4d2034617bd16aa170c263108b2b',
    'physical_transition_occurrence_close_tournament_cycle332_2026_07_18': 'de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415',
    'physical_transport_bound_commuting_multiplier_probe_2026_07_15': 'a477a3ebccf30b452d29e627dea1c5eb6ea4f70a3872ed82bcb64f4d0c19754e',
    'physical_two_block_recurrent_field_transport_cycle419_2026_07_19': '3c86a2ee58929b170b438920f917806cbe6f4bd113b6b617cafc6f84d15bb07b',
    'physical_two_port_row_four_fork_probe_2026_07_15': '76127ff36150be954932647fa03689183254da114afaad593c8b25dbd40302b9',
    'physical_two_row_commutation_bind_probe_2026_07_15': 'a7bd6ee7c36a4ce06919525da1d0ca4baffa88f4ac88a666221bed920eb8e7a4',
    'post_cycle124_rail_attached_head_cycle122_graph_scratch': '1348cd4bef99921dfdfcc5048c5a650df294d4874b4ada977461cb3823d87afb',
    'post_cycle129_guarded_rail_bridge_graph_scratch': '8e602992d1a22ebf058a0e18bc9607bbb11e6c1361303ab756a32e8113b72dd5',
    'post_cycle131_outward_adapter_search_scratch': 'fd98d1ef19350fff173422022fa7b646e97faceb7ea81239a3cb554c5c755f12',
    'prebind_unary_role_history_census_2026_07_15': '2fb1d4971103aa1cb995ec4a7c95b252200a912b7c14b11550e2eaacb2f3e2b9',
    'proper_cubic_bound_object_equivalence_cycle210_2026_07_16': 'c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b',
    'proper_cubic_hard_core_many_field_vertex_cycle421_2026_07_19': '3bbfeb45288af8d59c64a630a6b2e43ae1f6be74e87f2373683176155aeac8e7',
    'r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15': '089941fb612987e71e92adbe0db4ae5ada42936c86611c0691ec3d16bb63d79f',
    'r_b00_port_to_zero_source_word_completion_cycle121_2026_07_15': 'f947fc3d154e768409dd5b285c96d6eb1fe28522ba51829a4405b2eb2fa8a839',
    'r_b01_word_retargeted_cycle121_writer_probe_2026_07_15': 'edb9c9244a7be78246df3e98add1faef9a076bfe42fc5c06f7b53f55b883e8ef',
    'r_b10_completion_to_r_b00_role_allocator_common_port_cycle119_2026_07_15': '23ed32cd651cd20939c56a7a8d276c553338155d4db3b9225ee7eea1f7e94b4f',
    'r_b10_port_to_zero_source_word_completion_cycle117_2026_07_15': 'b50d84d82c8a2054e5ccbd68927890bacc6168ac5b321a965c068d30c2acf217',
    'read_status_to_generated_rail_spine_cycle105_2026_07_15': '90a9bed29a3fbd73bea53d26ffd20bf30fb02d663dba54941305f860822f8a45',
    'record_defined_causal_depth_clock_cycle170_2026_07_16': '1542635ef85c7c8eee6be7b08245de0c6e3d406555b81b5dc5450bcc4d0e3927',
    'record_derived_coherent_carrier_decoder_cycle48_2026_07_14': '7d17e7925ee38b0ba95a758e2918008280092ed86fca3e32b9cbbcac339c358e',
    'recurrent_post_oz_payload_prototype_2026_07_15': '3ef608276e903a8b1e108056bd975e1146c73aebbf9ff6047a793d478eb59c11',
    'recurrent_r_b01_physical_writer_embedding_search_scratch_2026_07_15': '8259d07c8e31576afee40ec8991437aa11c113c043510e53af68742256a52001',
    'recurrent_socket_to_cycle129_downstream_interface_probe_2026_07_15': 'ef68b809f6fba435a44fcb3a38c7953737d1b327840fdda4390b1d70f98117c2',
    'relational_notched_rail_socket_prototype_2026_07_15': '613ec29da8e53f9008d5aabfa819cdb96093163272e6e783f175e346062dab86',
    'relational_notched_socket_rail_replacement_probe_2026_07_15': 'c959700797ba81b9a26115a6b11f3bd9d984ebce090bf9a454d0f34097b2401d',
    'relational_periodic_socket_emitter_search_scratch_2026_07_15': 'eee0ba030d6a7a3b60ed45f794cf0b161960e6cd89659430d06d3c326c910dcc',
    'retained_source_notched_rail_nucleation_cycle141_2026_07_15': 'e6d63819550223b0cf2e7c85bead1b7f6a11355856bb5f97856418a473644483',
    'retarded_cubic_mass_field_cycle213_2026_07_16': '472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86',
    'self_extending_frame_cage_rail_cycle52_2026_07_14': 'eba3890d556f38c84af8e51723e23d55f3b3024e820221c9cfd1c2c43a141b45',
    'self_writing_append_only_bell_front_cycle14_2026_07_14': 'afd52a3947d583bf813bf9f582d61c982abb37b5c55fc1e3cbfed5356a5016e6',
    'seven_bit_physical_role_comparator_cycle75_2026_07_14': '0a371532a8319bc1a8b64bd08a7813ea41ecfb862ed1ed7fe60160bb95e8b2c7',
    'spacious_and_xor_streaming_commutator_probe_2026_07_15': '243508b49df2aa3a47b0fe5eab32d978d0d8187afcfc8ef74c499e5ae6b6a989',
    'spatial_car_contact_seam_form_factor_cycle230_2026_07_17': 'b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae',
    'spatial_compiler_derived_causal_time_bridge_cycle243_2026_07_17': '1ff4826b2a3c4a5fe839e868b14dcbf36924b8351259505025399a3c0abecbda',
    'stationary_dressed_reservoir_shifted_green_profile_2026_07_17': 'f711429d255c872bab5fd296cfc9ce662d3adb4e17f3a97915ffc152caa30d83',
    'status_gated_typed_payload_handoff_cycle109_2026_07_15': 'af8747c41b24bca982ca26ae25c61a5e43ac65ed782686a3fc761640467416f0',
    'stochastic_record_history_actuality_semantics_cycle27_2026_07_14': '35791d8610ca498116bf49cde1ddcdd3ac36ba9ef639380e4b577d1116e945a4',
    'streaming_parity_to_pivot_router_probe_2026_07_15': '4ce55bd2137b4fe7003dfd5b221f1d2d0ae27699ebed58a5ce0e9a547301af17',
    'strict_nn_record_law_compiler_cycle43_2026_07_14': 'a69749eadcec8e38e02171a33fbe7cb81e45bee27f6aeca596d6b60809c7dea8',
    'three_phase_recurrent_append_tube_cycle80_2026_07_14': '3cc9de0975458f91aefd648ba91f77b6841339baab2e14619d7cfc44c2a80d2d',
    'total_status_serial_reject_selector_cycle93_2026_07_15': '81b89aac7fff79d09cf3a896b466740d665540b333359ce4c02fb97edbb7fd91',
    'two_block_qle2_many_field_transport_cycle423_2026_07_19': '6963a3f9611c4581858ef68b093b0c75fb1851b18a83eee510ab83413737c39a',
    'two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18': '4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75',
    'virtual_exchange_green_kernel_cycle216_2026_07_16': '9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011',
    'wilson_subsystem_sector_free_compiler_cycle269_2026_07_17': 'c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35',
    'zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15': '35efacfe864be1faa92bfa6c6644a3cda4532e10f15ceaf2e2f0a990e4e26a88',
    'zero_source_relational_first_harness_cycle101_2026_07_15': '5e53f1ebd979b8b07a4341041901f34acd54edcde25dc826a6fc34da464352c6',
}
RUNTIME_DEPENDENCY_PATHS = {name: ROOT / "scripts" / f"{name}.py" for name in RUNTIME_DEPENDENCY_HASHES}
EXPECTED_RUNTIME_DEPENDENCY_MANIFEST_SHA256 = 'b5c68885d243018aec66fa7e0a9bc367f18941c3965dca35959f465992681227'

# Frozen before any train or held output is evaluated.
FROZEN_LAW = {
    "Route_A": {
        "detector_channels": ("onsite_A2", "one_update_transported_A2"),
        "aggregate_coefficients": (1, 1),
        "train": {"L": 3, "q": (1, 2, 3, 4)},
        "held": {"L": 6, "q": (1, 2, 3, 4, 5, 6)},
        "held_contact_deletion_q": 6,
    },
    "Route_B": {
        "path": "actual beta=-0.3,g=0.37",
        "reference": "same free law with g=0",
        "branch_field": "one scalar selector role bit per coarse cell with logical equality checks",
        "train": {"L": 3, "q": (1, 2, 3, 4)},
        "held": {"L": 6, "q": (1, 2, 3, 4, 5, 6)},
    },
    "Route_C": {
        "rotor_modulus": 4,
        "root_position": 0,
        "root_binder": 1,
        "prefixes": (1, 2, 4, 5, 8, 13, 21),
    },
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()

CAUSAL_TIME_COMPARISON = {
    "source": "PR #5557 Cycles610-612 comparison surface only",
    "runtime_imported_or_pinned": False,
    "executed_by_Cycle602": False,
    "back_credit_to_Cycle602": False,
    "Cycle610": "later proper-cubic compiler work; no retroactive physical-M2 status for Cycle602",
    "Cycle611": "later matter/source response work; no Cycle602 source-response law",
    "Cycle612_3_to_4_delay": "rate-compatible association only; not implemented here",
    "Cycle612_5_to_4_advance": "requires a count/event edit and is a different mechanism; not implemented here",
    "proper_time_or_lapse_implemented": False,
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def shore_and_time_firewall() -> dict[str, object]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    runtime_observed = {name: file_sha(path) for name, path in RUNTIME_DEPENDENCY_PATHS.items()}
    runtime_mismatches = tuple(
        name for name, expected in RUNTIME_DEPENDENCY_HASHES.items()
        if runtime_observed.get(name) != expected
    )
    runtime_manifest = sha256(json.dumps(runtime_observed, sort_keys=True).encode()).hexdigest()
    receipts = {}
    for cycle, path in {
        "Cycle599": "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_receipt_2026_07_22.json",
        "Cycle590": "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json",
        "Cycle570": "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json",
    }.items():
        receipt = json.loads((ROOT / path).read_text(encoding="utf-8"))
        number = cycle.removeprefix("Cycle")
        runner_path = next(name for name in FROZEN_SHORES if f"cycle{number}_" in name.lower() and name.startswith("scripts/"))
        note_path = next(name for name in FROZEN_SHORES if f"cycle{number}_" in name.lower() and name.endswith(".md"))
        checks = {
            "runner_bound": receipt.get("runner_sha256") == FROZEN_SHORES[runner_path],
            "note_bound": receipt.get("note_sha256") == FROZEN_SHORES[note_path],
            "pass": receipt.get("pass") is True,
            "authority_audit": receipt.get("authority") == "none" and receipt.get("audit") == "unset",
        }
        if cycle == "Cycle599":
            checks["cold_bound"] = receipt.get("cold_transcript_sha256") == FROZEN_SHORES[
                "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_cold_2026_07_22.txt"
            ]
            checks["narrow_no_go_boundary"] = receipt.get("no_go_discipline", {}).get("Status") == "FAIL"
            checks["author_not_accepted"] = receipt.get("author_accepted") is False
        receipts[cycle] = checks
    condition = (
        observed == FROZEN_SHORES and len(FROZEN_SHORES) == 13
        and not runtime_mismatches and len(RUNTIME_DEPENDENCY_HASHES) == 233
        and runtime_manifest == EXPECTED_RUNTIME_DEPENDENCY_MANIFEST_SHA256
        and all(all(checks.values()) for checks in receipts.values())
        and not CAUSAL_TIME_COMPARISON["runtime_imported_or_pinned"]
        and not CAUSAL_TIME_COMPARISON["back_credit_to_Cycle602"]
    )
    result = {
        "observed": observed,
        "exact_pinned_surfaces": len(FROZEN_SHORES),
        "runtime_dependency_count": len(RUNTIME_DEPENDENCY_HASHES),
        "runtime_dependency_hash_mismatches": runtime_mismatches,
        "runtime_dependency_manifest_sha256": runtime_manifest,
        "expected_runtime_dependency_manifest_sha256": EXPECTED_RUNTIME_DEPENDENCY_MANIFEST_SHA256,
        "receipt_checks": receipts,
        "Cycle590_status_used_here": "conditional coarse-algebraic 53-role blueprint only; not strict physical",
        "causal_time_comparison": CAUSAL_TIME_COMPARISON,
        "frozen_law_sha256": FROZEN_LAW_SHA256,
    }
    check("Cycle599/C590/C451/C570 shores and the complete repo-local runtime closure are byte exact", condition, result)
    return result


def coarse_support(amplitude: np.ndarray) -> set[int]:
    sites: set[int] = set()
    for left, right in np.argwhere(abs(amplitude) > 1e-12):
        sites.add(int(left) // 6)
        sites.add(int(right) // 6)
    return sites


def transported_detector(length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, object]:
    source = c599.local_a2_source(length)
    walk = c590.one_particle_walk(length)
    transported = c590.full_update(source, walk)
    if abs(np.vdot(source, transported)) > TOL:
        raise ValueError("onsite and one-update channels are not orthogonal")
    detector = source + transported
    detector /= np.linalg.norm(detector)
    return source, transported, detector, walk


def route_a_transported_observable() -> dict[str, object]:
    print("\nROUTE A — FIXED-COARSE ONSITE PLUS TRANSPORTED A2 OBSERVABLE")
    rows = []
    maximum_inverse = maximum_norm = maximum_antisymmetry = 0.0
    minimum_visibility = np.inf
    held_cache = None
    for split in ("train", "held"):
        spec = FROZEN_LAW["Route_A"][split]
        length = spec["L"]
        source, transported, detector, walk = transported_detector(length)
        origin = complex(np.vdot(detector, source))
        state = source.copy()
        words = []
        for q in spec["q"]:
            state = c590.full_update(state, walk)
            onsite = complex(np.vdot(source, state))
            shifted = complex(np.vdot(transported, state))
            aggregate = complex(np.vdot(detector, state))
            visibility = float(abs(aggregate))
            minimum_visibility = min(minimum_visibility, visibility)
            words.append({
                "law_applications_not_time": q,
                "onsite_channel": onsite,
                "transported_channel": shifted,
                "aggregate": aggregate,
                "visibility_amplitude": visibility,
                "phase_word_defined": visibility > SIGNAL,
                "principal_phase_difference": float(np.angle(aggregate / origin)) if visibility > SIGNAL else None,
            })
        restored = state.copy()
        for _ in spec["q"]:
            restored = c590.inverse_full_update(restored, walk)
        maximum_inverse = max(maximum_inverse, float(np.linalg.norm(restored - source)))
        maximum_norm = max(maximum_norm, abs(float(np.linalg.norm(state)) - 1))
        maximum_antisymmetry = max(maximum_antisymmetry, float(np.linalg.norm(state + state.T)))
        support = coarse_support(source + transported)
        support_coordinates = tuple(c590.site_tuple(site, length) for site in sorted(support))
        row = {
            "split": split,
            "length": length,
            "words": words,
            "detector_coarse_cells": len(support),
            "detector_cells": support_coordinates,
            "detector_periodic_radius": 1,
            "pair_support_diameter": 2,
            "channel_orthogonality_residual": float(abs(np.vdot(source, transported))),
        }
        rows.append(row)
        if split == "held":
            held_cache = (source, transported, detector, walk, state, row)
    assert held_cache is not None
    source, transported, detector, walk, held_state, held_row = held_cache

    deleted = source.copy()
    for _ in FROZEN_LAW["Route_A"]["held"]["q"]:
        deleted = c590.full_update(deleted, walk, coupling=0.0)
    held_deleted_state_signal = float(np.linalg.norm(held_state - deleted))
    held_deleted_word_signal = float(abs(np.vdot(detector, held_state) - np.vdot(detector, deleted)))

    # The actual Cycle230 contact factorization is checked directly at the
    # new source, including an L6 periodic-seam translation.
    free_once = walk @ ((walk @ source.T).T)
    contact_factorization = float(np.linalg.norm(
        c590.full_update(source, walk)
        - c599.c230.contact_pair_step(np.asarray(free_once), 6, c590.CONTACT)
    ))
    translated_source = c599.translate_pair(source, 6, (-1, 0, 0))
    seam_translation = float(np.linalg.norm(
        c590.full_update(translated_source, walk)
        - c599.translate_pair(c590.full_update(source, walk), 6, (-1, 0, 0))
    ))
    mass_species = c590.c219.common_species(c590.BETA)
    mass_residual = abs(c590.c219.rest_mass(mass_species) - mass_species.analytic_mass)

    frames = c590.c210.proper_cubic_frames()
    covariance = []
    word_covariance = []
    held_aggregate = complex(np.vdot(detector, held_state))
    for frame in frames:
        rotated_source = c590.rotate_amplitude(source, frame, 6)
        rotated_transported = c590.rotate_amplitude(transported, frame, 6)
        rotated_detector = c590.rotate_amplitude(detector, frame, 6)
        rotated_state = c590.rotate_amplitude(held_state, frame, 6)
        covariance.append(float(np.linalg.norm(c590.full_update(rotated_source, walk) - rotated_transported)))
        word_covariance.append(float(abs(np.vdot(rotated_detector, rotated_state) - held_aggregate)))

    # Algebraic factorization only.  No physical pulse, detector, placement,
    # leakage test, or primitive product is executed by Cycle602.
    synthesis_attempt = {
        "transported_channel_factorization": "apply the coarse inverse update algebraically, then contract with the onsite A2 bra",
        "single_fixed_aggregate_evaluated": True,
        "both_channels_physically_emitted_under_one_rule": False,
        "q_dependent_selector": False,
        "simultaneous_nondemolition_controlled_inverse_synthesized": False,
        "onsite_A2_pulse_readout_primitive_layout_synthesized": False,
        "physical_EG": None,
        "physical_placement": None,
        "physical_leakage": None,
        "physical_primitive_product": None,
    }
    result = {
        "executed_layer": "fixed-coarse logical N=2 antisymmetric arrays on L3/L6",
        "interpretation": "coarse-algebraic transported A2 observable; not a physical detector or Ramsey device",
        "rows": rows,
        "minimum_frozen_visibility": minimum_visibility,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_norm_residual": maximum_norm,
        "maximum_antisymmetry_residual": maximum_antisymmetry,
        "held_contact_deletion_state_signal": held_deleted_state_signal,
        "held_contact_deletion_word_signal": held_deleted_word_signal,
        "Cycle230_contact_factorization_residual": contact_factorization,
        "held_axis_seam_translation_residual": seam_translation,
        "one_particle_mass_residual": mass_residual,
        "proper_cubic_frames": len(frames),
        "paired_frames": len(frames) ** 2,
        "maximum_all24_update_covariance_residual": max(covariance),
        "maximum_all24_word_covariance_residual": max(word_covariance),
        "Cycle590_conditional_roles_per_coarse_cell": 53,
        "Cycle590_53_role_blueprint_promoted_to_strict_physical": False,
        "strict_physical_M2_count": None,
        "detector_physical_M2_count": None,
        "physical_EG": None,
        "physical_placement": None,
        "physical_leakage": None,
        "physical_primitive_product": None,
        "bounded_readout_coarse_radius": 1,
        "synthesis_attempt": synthesis_attempt,
        "global_N_le_3_cutoff_locally_enforced": False,
        "runtime_parity_or_q_selector": False,
        "route_disposition": "positive fixed finite coarse-algebraic observable family only",
    }
    condition = (
        minimum_visibility > SIGNAL and maximum_inverse < TOL and maximum_norm < TOL
        and maximum_antisymmetry < TOL and held_deleted_state_signal > SIGNAL
        and held_deleted_word_signal > SIGNAL and contact_factorization < TOL
        and seam_translation < TOL and mass_residual < TOL
        and max(covariance + word_covariance) < TOL and len(frames) == 24
        and all(word["phase_word_defined"] for row in rows for word in row["words"])
    )
    result["pass"] = bool(condition)
    check("Route A's fixed two-channel coarse observable defines a nonzero phase word at every frozen q without a parity selector", condition, result)
    return result


def route_b_contact_reference_echo() -> dict[str, object]:
    print("\nROUTE B — COARSE CONTACT / DECLARED-FREE REFERENCE ECHO")
    rows = []
    minimum_visibility = np.inf
    maximum_inverse = 0.0
    held_deletion = 0.0
    for split in ("train", "held"):
        spec = FROZEN_LAW["Route_B"][split]
        length = spec["L"]
        source = c599.local_a2_source(length)
        walk = c590.one_particle_walk(length)
        actual = reference = source.copy()
        words = []
        for q in spec["q"]:
            actual = c590.full_update(actual, walk)
            reference = c590.full_update(reference, walk, coupling=0.0)
            echo = complex(np.vdot(reference, actual))
            minimum_visibility = min(minimum_visibility, float(abs(echo)))
            words.append({
                "law_applications_not_time": q,
                "contact_relative_echo": echo,
                "visibility_amplitude": float(abs(echo)),
                "principal_phase_difference": float(np.angle(echo)),
                "phase_word_defined": abs(echo) > SIGNAL,
            })
        restored_actual = actual.copy()
        restored_reference = reference.copy()
        for _ in spec["q"]:
            restored_actual = c590.inverse_full_update(restored_actual, walk)
            # inverse of the free-only law
            left = walk.conj().T @ restored_reference
            restored_reference = np.asarray((walk.conj().T @ left.T).T)
        maximum_inverse = max(
            maximum_inverse,
            float(np.linalg.norm(restored_actual - source)),
            float(np.linalg.norm(restored_reference - source)),
        )
        if split == "held":
            held_deletion = float(abs(np.vdot(reference, actual) - 1))
        rows.append({"split": split, "length": length, "words": words})
    held_cells = 6**3
    branch_interface = {
        "matter_sector": "one N=2 dimer in a direct-sum path label; not two simultaneous dimers",
        "N4_or_four_CAR_domain_invoked": False,
        "reference_channel": "declared g=0 free channel",
        "reference_independent_genesis": False,
        "selector_role_bits_per_coarse_cell": 1,
        "held_selector_role_bits": held_cells,
        "nearest_neighbor_selector_equality_checks": 3 * held_cells,
        "local_selector_checks_enforced_by_update": False,
        "controlled_contact_code_space_operator": "local selector=1 applies contact, selector=0 applies identity",
        "controlled_contact_primitive_gate_and_layout_synthesized": False,
        "physical_EG": None,
        "physical_placement": None,
        "physical_leakage": None,
        "physical_primitive_product": None,
        "physical_status": "null; coarse algebraic echo only",
    }
    result = {
        "executed_layer": "coarse algebraic N=2 contact-on/contact-off overlap on L3/L6",
        "interpretation": "Loschmidt-style algebraic echo; not a physical pulse, branch device, detector, or clock",
        "rows": rows,
        "minimum_frozen_echo_visibility": minimum_visibility,
        "maximum_inverse_residual": maximum_inverse,
        "held_contact_deletion_echo_signal": held_deletion,
        "branch_interface": branch_interface,
        "proper_cubic_covariance_executed_here": False,
        "proper_cubic_frames_checked_here": 0,
        "runtime_q_selector": False,
        "physical_EG": None,
        "physical_placement": None,
        "physical_leakage": None,
        "physical_primitive_product": None,
        "route_disposition": "positive fixed finite coarse-algebraic echo only",
    }
    condition = (
        minimum_visibility > SIGNAL and maximum_inverse < TOL and held_deletion > SIGNAL
        and all(word["phase_word_defined"] for row in rows for word in row["words"])
        and not branch_interface["N4_or_four_CAR_domain_invoked"]
    )
    result["pass"] = bool(condition)
    check("Route B gives a nonzero finite contact-relative echo without silently expanding to N4", condition, result)
    return result


@dataclass(frozen=True)
class RotorLayout:
    fields: dict[str, tuple[int, ...]]
    width: int

    def field(self, name: str) -> tuple[int, ...]:
        return self.fields[name]


def rotor_layout(prefix: int) -> RotorLayout:
    fields = {}
    cursor = 0

    def take(name: str, width: int) -> None:
        nonlocal cursor
        fields[name] = tuple(range(cursor, cursor + width))
        cursor += width

    take("root.rotor", 4)
    take("root.binder", 1)
    take("root.valid", 1)
    for cell in range(1, prefix + 1):
        take(f"cell{cell}.opportunity", 1)
        take(f"cell{cell}.rotor", 4)
        take(f"cell{cell}.carry", 1)
        take(f"cell{cell}.binder", 1)
        take(f"cell{cell}.valid", 1)
        take(f"cell{cell}.predecessor", 1)
    return RotorLayout(fields, cursor)


def rotor_initial(prefix: int, malformed: str | None = None) -> tuple[RotorLayout, tuple[int, ...]]:
    layout = rotor_layout(prefix)
    bits = [0] * layout.width
    bits[layout.field("root.rotor")[0]] = 1
    bits[layout.field("root.binder")[0]] = 1
    bits[layout.field("root.valid")[0]] = 1
    for cell in range(1, prefix + 1):
        bits[layout.field(f"cell{cell}.opportunity")[0]] = 1
    if malformed == "origin":
        bits[layout.field("root.rotor")[0]] = 0
    elif malformed == "binder":
        bits[layout.field("root.binder")[0]] = 0
    elif malformed == "opportunity":
        bits[layout.field("cell1.opportunity")[0]] = 0
    elif malformed is not None:
        raise ValueError("unknown malformed rotor word")
    return layout, tuple(bits)


def rotor_validate(layout: RotorLayout, bits: tuple[int, ...], prefix: int) -> None:
    if sum(bits[index] for index in layout.field("root.rotor")) != 1:
        raise ValueError("rotor origin leaves Q1")
    if bits[layout.field("root.binder")[0]] != 1:
        raise ValueError("charged binder is absent")
    if bits[layout.field("root.valid")[0]] != 1:
        raise ValueError("root event is invalid")
    for cell in range(1, prefix + 1):
        if bits[layout.field(f"cell{cell}.opportunity")[0]] != 1:
            raise ValueError("local event opportunity is absent")


def rotor_schedule(layout: RotorLayout, prefix: int) -> tuple[c570.Gate, ...]:
    gates = []
    for cell in range(1, prefix + 1):
        previous = "root" if cell == 1 else f"cell{cell - 1}"
        for index, (source, target) in enumerate(zip(layout.field(f"{previous}.rotor"), layout.field(f"cell{cell}.rotor"))):
            gates.append(c570.Gate("CNOT", (source, target), f"cell{cell}:rotor-copy-{index}"))
        gates.append(c570.Gate("CNOT", (layout.field(f"{previous}.binder")[0], layout.field(f"cell{cell}.binder")[0]), f"cell{cell}:binder-copy"))
        gates.append(c570.Gate("CNOT", (layout.field(f"cell{cell}.opportunity")[0], layout.field(f"cell{cell}.valid")[0]), f"cell{cell}:valid"))
        gates.append(c570.Gate("CNOT", (layout.field(f"{previous}.valid")[0], layout.field(f"cell{cell}.predecessor")[0]), f"cell{cell}:predecessor"))
        control = layout.field(f"cell{cell}.opportunity")[0]
        rotor = layout.field(f"cell{cell}.rotor")
        carry = layout.field(f"cell{cell}.carry")[0]
        label = f"cell{cell}:event-rotor"
        gates.append(c570.Gate("TOFFOLI", (control, rotor[-1], carry), f"{label}:wrap-carry"))
        gates.extend(
            c570.Gate("FREDKIN", (control, rotor[index], rotor[index + 1]), f"{label}:rotate-{index}")
            for index in reversed(range(len(rotor) - 1))
        )
    return tuple(gates)


def rotor_decode(layout: RotorLayout, bits: tuple[int, ...], prefix: int) -> dict[str, object]:
    carries = 0
    rows = []
    for cell in range(1, prefix + 1):
        rotor = tuple(bits[index] for index in layout.field(f"cell{cell}.rotor"))
        binder = bits[layout.field(f"cell{cell}.binder")[0]]
        valid = bits[layout.field(f"cell{cell}.valid")[0]]
        predecessor = bits[layout.field(f"cell{cell}.predecessor")[0]]
        if sum(rotor) != 1 or binder != 1 or valid != 1 or predecessor != 1:
            raise ValueError("rotor leaves the local one-hot/binder code")
        carry = bits[layout.field(f"cell{cell}.carry")[0]]
        carries += carry
        rows.append({"cell": cell, "rotor": rotor.index(1), "carry": carry, "binder": binder})
    extensive = 4 * carries + rows[-1]["rotor"] if rows else 0
    return {"rows": rows, "extensive_event_count_not_time": extensive}


def route_c_reversible_one_hot_rotor() -> dict[str, object]:
    print("\nROUTE C — REVERSIBLE ONE-HOT ALGEBRAIC ROTOR")
    rows = {}
    maximum_support = 0
    for prefix in FROZEN_LAW["Route_C"]["prefixes"]:
        layout, initial = rotor_initial(prefix)
        rotor_validate(layout, initial, prefix)
        schedule = rotor_schedule(layout, prefix)
        physical = c570.run_schedule(initial, schedule)
        decoded = rotor_decode(layout, physical, prefix)
        restored = c570.run_schedule(physical, schedule, reverse=True)

        clock_layout, clock_initial = c570.initial_word(prefix)
        clock_physical = c570.run_schedule(clock_initial, c570.joint_schedule(clock_layout, prefix))
        endpoints = c570.decode_endpoints(clock_layout, clock_physical, prefix)
        maximum_support = max(maximum_support, *(len(gate.sites) for gate in schedule))
        rows[prefix] = {
            "split": "held" if prefix in c570.HELD_PREFIXES else "train",
            "rotor_event_count_not_time": decoded["extensive_event_count_not_time"],
            "Cycle570_endpoint_totals": c570.endpoint_totals(endpoints),
            "inverse_exact": restored == initial,
            "local_code_checks": all(row["binder"] == 1 for row in decoded["rows"]),
        }

    # Exact 3:4/4:4/5:4 matcher shore remains separate from the rotor count.
    matcher = {}
    for probe in (3, 4, 5):
        interval = c451.interval_for_positions(2, 6, 2 + probe)
        matcher[f"{probe}:4"] = None if interval is None else str(interval.probe_over_reference)

    layout, initial = rotor_initial(5)
    schedule = rotor_schedule(layout, 5)
    physical = c570.run_schedule(initial, schedule)
    binder_deleted = c570.run_schedule(initial, schedule, delete_label="cell3:binder-copy")
    carry_deleted = c570.run_schedule(initial, schedule, delete_label="cell4:event-rotor:wrap-carry")
    deletion_visible = 0
    for word in (binder_deleted, carry_deleted):
        try:
            decoded = rotor_decode(layout, word, 5)
            deletion_visible += int(decoded["extensive_event_count_not_time"] != 5)
        except ValueError:
            deletion_visible += 1
    malformed_rejections = 0
    for label in ("origin", "binder", "opportunity"):
        try:
            malformed_layout, malformed = rotor_initial(2, malformed=label)
            rotor_validate(malformed_layout, malformed, 2)
        except ValueError:
            malformed_rejections += 1

    result = {
        "executed_layer": "reversible Boolean one-hot rotor and binder-role schedule",
        "interpretation": "algebraic rotor sidecar; not a physical M2 placement, event, Record, or clock",
        "rows": rows,
        "Cycle451_matcher": matcher,
        "deletion_controls_visible": deletion_visible,
        "malformed_rejections": malformed_rejections,
        "maximum_gate_arity_bits": maximum_support,
        "root_algebraic_bits": 6,
        "algebraic_bits_per_prefix_cell": 9,
        "proper_cubic_covariance_executed_here": False,
        "proper_cubic_frames_checked_here": 0,
        "rotor_and_binder_frame_action_supplied": "scalar internal role assignment",
        "local_one_hot_binder_code": "binder role bit=1 and rotor one-hot weight=1",
        "local_code_preserved": True,
        "gauge_group_field_or_Gauss_generator_derived": False,
        "global_charge_conservation_claimed": False,
        "algebraic_gate_alphabet": ("CNOT", "TOFFOLI", "FREDKIN"),
        "bounded_algebraic_routing_grammar": "inherited Cycle570 reversible bit routing within a logical cell and predecessor boundary",
        "phase_origin": "supplied root rotor K0 plus occupied binder",
        "phase_origin_genesis_derived": False,
        "matter_q_to_event_count_map_derived": False,
        "event_count_called_time": False,
        "candidate_event_called_Record": False,
        "physical_EG": None,
        "physical_placement": None,
        "physical_leakage": None,
        "physical_primitive_product": None,
        "route_disposition": "positive reversible finite-prefix algebraic rotor only",
    }
    condition = (
        all(row["rotor_event_count_not_time"] == prefix and row["inverse_exact"] and row["local_code_checks"]
            for prefix, row in rows.items())
        and matcher == {"3:4": "3/4", "4:4": "1", "5:4": "5/4"}
        and deletion_visible == 2 and malformed_rejections == 3 and maximum_support <= 3
    )
    result["pass"] = bool(condition)
    check("Route C reversibly propagates a one-hot algebraic rotor with deletion and malformed-word controls", condition, result)
    return result


def line_ref(function) -> str:
    return f"{Path(inspect.getsourcefile(function) or '').name}:{inspect.getsourcelines(function)[1]}"


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict[str, object]:
    alternatives = (
        {
            "object_formulation": "fixed-coarse onsite plus transported A2 covector",
            "mechanism_invariant": "one-update transported observable orbit with fixed equal coefficients",
            "terminal_obligation": "nonzero finite L3/L6 coherent word without a q selector",
            "honesty_marker": "ATTEMPTED",
            "search_status": "COUNTED",
            "disposition": "positive finite coarse-algebraic family; no physical detector",
        },
        {
            "object_formulation": "single N=2 branch with contact-on/contact-off references",
            "mechanism_invariant": "Loschmidt-style overlap under matched coarse updates",
            "terminal_obligation": "finite interaction-sensitive echo",
            "honesty_marker": "ATTEMPTED",
            "search_status": "COUNTED",
            "disposition": "positive finite coarse-algebraic echo; no physical branch control",
        },
        {
            "object_formulation": "reversible one-hot rotor with binder and predecessor role bits",
            "mechanism_invariant": "fixed CNOT/TOFFOLI/FREDKIN Boolean permutation",
            "terminal_obligation": "finite-prefix rollover and inverse with deletion sensitivity",
            "honesty_marker": "ATTEMPTED",
            "search_status": "COUNTED",
            "disposition": "positive algebraic rotor; not a physical event/clock device",
        },
        {
            "object_formulation": "literal physical-M2 pulse/detector/readout block",
            "mechanism_invariant": "primitive E/G product with placement and code-space leakage bound",
            "terminal_obligation": "physical transported-observable Ramsey device",
            "honesty_marker": None,
            "search_status": "OPEN_UNTESTED_NOT_COUNTED",
            "disposition": "open",
        },
        {
            "object_formulation": "autonomously prepared physical echo reference",
            "mechanism_invariant": "locally stabilized path label and independent reference genesis",
            "terminal_obligation": "physical interaction-conditioned comparison",
            "honesty_marker": None,
            "search_status": "OPEN_UNTESTED_NOT_COUNTED",
            "disposition": "open",
        },
        {
            "object_formulation": "causal endpoint/predecessor interval with Record admission",
            "mechanism_invariant": "deletion-sensitive occurrence and calibrated interval association",
            "terminal_obligation": "proper-time-capable realized clock comparison",
            "honesty_marker": None,
            "search_status": "OPEN_UNTESTED_NOT_COUNTED",
            "disposition": "open; later Cycles610-612 give comparison facts without back-credit",
        },
    )
    qualifying = tuple(route for route in alternatives if route["honesty_marker"] == "ATTEMPTED")
    walls = {
        "transported detector primitive composition": {
            "type": "PHYSICAL_COMPILATION",
            "obligation": "literal physical-M2 E/G, placement, leakage and primitive product for preparation and transported readout",
        },
        "echo control primitive composition": {
            "type": "PHYSICAL_COMPILATION",
            "obligation": "literal local path-control E/G and constraint enforcement for the contact-on/off echo",
        },
        "autonomous state and origin genesis": {
            "type": "GENESIS",
            "obligation": "autonomous preparation of the A2 state, echo reference, root rotor and binder role",
        },
        "matter-to-causal-interval association": {
            "type": "ASSOCIATION",
            "obligation": "a physical law associating one matter interrogation with endpoint/predecessor interval data",
        },
        "Record actuality": {
            "type": "ACTUALITY",
            "obligation": "framework-owned occurrence, permanence, readability and admission",
        },
        "local number-domain enforcement": {
            "type": "DOMAIN_LOCALITY",
            "obligation": "bounded local enforcement of the global N<=3 compiler promise",
        },
        "universal proper-time calibration": {
            "type": "CALIBRATION",
            "obligation": "empirical cross-device equivalence and continuum unit map",
        },
    }
    directional = tuple({
        "pair": (left, right),
        "left_wall_type": walls[left]["type"],
        "right_wall_type": walls[right]["type"],
        "left_closes_right": False,
        "left_to_right_reason": f'{walls[left]["obligation"]} does not construct {walls[right]["obligation"]}',
        "right_closes_left": False,
        "right_to_left_reason": f'{walls[right]["obligation"]} does not construct {walls[left]["obligation"]}',
        "independent": True,
        "collapsed": False,
    } for left, right in combinations(walls, 2))
    residuals = (
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_CYCLE599_NOTE_2026-07-22.md:147-172",
            "prior_residual": "fixed coarse A2 recurrence has odd-checkpoint zero visibility and lacks a primitive Ramsey interface",
            "current_residual": "fixed transported A2 covector supplies nonzero finite q=1..4/q=1..6 words while physical interface fields stay null",
            "scope_match": True,
            "exact_match": True,
            "current_witness": line_ref(route_a_transported_observable),
            "current_numeric_residual": route_a["maximum_inverse_residual"],
        },
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md:126-141",
            "prior_residual": "conditional logical macro identity is not a physical M2 update and lacks physical E/G, leakage and primitive composition",
            "current_residual": "Cycle602 calls the coarse array update only and preserves null physical fields",
            "scope_match": True,
            "exact_match": True,
            "current_witness": line_ref(route_b_contact_reference_echo),
            "current_numeric_residual": route_b["maximum_inverse_residual"],
        },
        {
            "witness": "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py:357-375",
            "prior_residual": "reversible finite Boolean gate interpreter with deletion support",
            "current_residual": "Cycle602 executes that interpreter on a new one-hot rotor schedule and checks exact inverse/deletions",
            "scope_match": True,
            "exact_match": True,
            "current_witness": line_ref(route_c_reversible_one_hot_rotor),
            "current_numeric_residual": 0.0 if all(row["inverse_exact"] for row in route_c["rows"].values()) else 1.0,
        },
    )
    dropped_residuals = (
        {
            "witness": "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md:23-60",
            "prior_residual": "Cycle570's claimed physical endpoint/accumulator semantics",
            "current_residual": "Cycle602 executes only the Boolean run_schedule helper and a host-side ratio comparison",
            "scope_match": False,
            "exact_match": False,
            "disposition": "dropped as physical, event, clock, or proper-time evidence",
        },
    )
    rhetoric = (
        {"phrase": "the executed update ordinal is not promoted to time", "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM", "per_block": "TESTED: q labels index finite coarse matrix products only", "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM"},
        {"phrase": "the reported principal phase is not promoted to energy", "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM", "per_block": "TESTED: no generator-to-energy or empirical unit map is executed", "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM"},
        {"phrase": "the 53-role Cycle590 blueprint is not promoted to strict physical M2", "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM", "per_block": "TESTED: physical E/G, placement, leakage and primitive-product fields are null", "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM"},
        {"phrase": "the one-hot rotor bit word is not promoted to a Record", "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM", "per_block": "TESTED: no occurrence, permanence, readability or admission law is executed", "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM"},
        {"phrase": "the contact echo visibility is not promoted to probability", "per_element": "UNTESTED_NO_NEGATIVE_CLAIM", "per_site": "UNTESTED_NO_NEGATIVE_CLAIM", "per_mode": "UNTESTED_NO_NEGATIVE_CLAIM", "per_block": "TESTED: overlap magnitude is a coherent diagnostic without selection or frequency calibration", "lattice_wide": "UNTESTED_NO_NEGATIVE_CLAIM"},
    )
    partial = (
        {"candidate_path": "scripts/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_2026_07_22.py", "status": "EXECUTED_NARROW_COARSE_ALGEBRAIC_POSITIVE", "what_it_closes": "finite L3/L6 transported-observable, echo and reversible-rotor diagnostics only"},
        {"candidate_path": "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py", "status": "EXACT_PINNED_CONDITIONAL_PARENT", "what_it_closes": "coarse/logical parent identities, not Cycle602 physical detector or echo composition"},
        {"candidate_path": "scripts/physical_transported_A2_detector_primitive_compiler_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_it_closes": "physical pulse/readout E/G, placement, leakage, primitive product and all24 layout"},
        {"candidate_path": "scripts/physical_autonomous_echo_reference_compiler_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_it_closes": "autonomous constrained branch/reference genesis and controlled-contact primitive product"},
        {"candidate_path": "scripts/physical_matter_clock_causal_interval_composition_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_it_closes": "matter-to-endpoint association, deletion-sensitive interval and Record admission without Cycle610-612 back-credit"},
    )
    steelman = {
        "mechanism": "compile the fixed seven-cell transported A2 covector as a bounded physical-M2 Naimark/readout block, compose it with a literal primitive realization of the conditional Cycle590 macro, autonomously prepare the reference branch, then attach its nonzero word to a deletion-sensitive endpoint/predecessor interval",
        "supporting_authority": (
            "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_CYCLE599_NOTE_2026-07-22.md:147-172",
            "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md:126-141",
            line_ref(route_a_transported_observable),
        ),
        "actionable_terminal": "construct and execute held L6 physical E/G/inverse/leakage/placement and primitive-product certificates for state preparation, transported readout and echo control, then demonstrate an autonomous association with a reversible deletion-sensitive causal interval",
        "openness": "this concrete route is unattempted and defeats any broad no-go, minimum-content, shared-obstruction or axiom-pressure claim",
    }
    echo = (
        {"prior_wall": "Cycle590 conditional logical macro is not a physical M2 primitive product", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md:126-141", "retired_status": "NOT_RETIRED", "retirement_mechanism": "none in Cycle602", "applicability_here": "compile literal detector/echo E/G, placement and leakage before physical promotion"},
        {"prior_wall": "Cycle599 fixed onsite A2 readout has odd-checkpoint zero visibility", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_RAMSEY_CLOCK_STRICT_M2_TIME_BRIDGE_TOURNAMENT_CYCLE599_NOTE_2026-07-22.md:147-172", "retired_status": "RETIRED_AT_FINITE_COARSE_OBSERVABLE_SCOPE", "retirement_mechanism": "one-update transported covector with fixed equal coefficients", "applicability_here": "does not retire physical detector or clock obligations"},
        {"prior_wall": "Cycle451 ratios are matched candidate words rather than a universal clock law", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md", "retired_status": "OPEN", "retirement_mechanism": "none in Cycle602", "applicability_here": "3:4/4:4/5:4 remain host-side comparisons"},
        {"prior_wall": "Cycle570 reversible prefix schedule is not proper time", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md:18-20,55-60", "retired_status": "OPEN_AT_CYCLE602_INTERFACE", "retirement_mechanism": "Boolean rotor inverse only", "applicability_here": "prefix and rotor counts remain non-time indices"},
        {"prior_wall": "Cycle610 later proper-cubic physical compiler work", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "retired_status": "COMPARISON_ONLY_NO_BACK_CREDIT", "retirement_mechanism": "not imported, pinned or executed by Cycle602", "applicability_here": "cannot retroactively physicalize the C590 53-role blueprint or Cycle602 detector"},
        {"prior_wall": "Cycle611 later matter/source response work", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_VARIATION_CURRENT_STRESS_COMPENSATOR_SOURCE_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md", "retired_status": "COMPARISON_ONLY_NO_BACK_CREDIT", "retirement_mechanism": "not imported, pinned or executed by Cycle602", "applicability_here": "Cycle602 derives no source-to-echo response, lapse or gravity law"},
        {"prior_wall": "Cycle612 conditional causal-interval comparison", "citation": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md:46-82", "retired_status": "COMPARISON_ONLY_NO_BACK_CREDIT", "retirement_mechanism": "3:4 delay is rate-compatible association; 5:4 advance requires count/event edit and is a different mechanism", "applicability_here": "neither response is implemented and no proper-time claim follows"},
    )
    gate = {
        "Status": "FAIL",
        "artifact_status": "PASS_NARROWED_COARSE_ALGEBRAIC_POSITIVE_ONLY",
        "N1_routes": alternatives,
        "N1_qualifying": len(qualifying),
        "N1_required": 5,
        "N1_gate": "FAIL",
        "N2_collapsed_walls": tuple({"wall": name, **spec} for name, spec in walls.items()),
        "N2_directional_wall_independence": directional,
        "N3_explicit_supplies": (
            "beta=-0.3, contact=0.37, finite L3/L6 periodic tori and boundary rules",
            "local A2 source, one-update transported covector, equal aggregate coefficients and q interrogation lists",
            "contact-off reference branch, logical selector roles and noiseless coherent overlap evaluation",
            "root one-hot rotor, binder/predecessor roles, blank bits and Cycle570 Boolean gate interpreter",
            "Cycle451 matcher positions and 3:4/4:4/5:4 ratio labels",
        ),
        "N3_phrase_hit_classifications": (
            {"hit": "registered", "surface": "runtime closure filename physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18", "classification": "NON_LOAD_BEARING_FILENAME", "reason": "the module key supplies no physics premise"},
            {"hit": "registered", "surface": "Cycle602 N3 classification row and note N3 explanation", "classification": "NON_LOAD_BEARING_META_SCAN", "reason": "these self-referential occurrences document the audit target rather than supply a proof step"},
        ),
        "N3_hidden_conditions_promoted": 0,
        "N4_exact_residual_matches": residuals,
        "N4_dropped_nonmatches": dropped_residuals,
        "N5_rhetoric_resolution_ledger": rhetoric,
        "N6_partial_closure_paths": partial,
        "N6_convention_only_closure_found": False,
        "N6_new_axiom_required": False,
        "N6_control_plane_edit": False,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echo,
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
    }
    condition = (
        gate["Status"] == "FAIL" and len(qualifying) == 3
        and sum(route["search_status"] == "OPEN_UNTESTED_NOT_COUNTED" for route in alternatives) == 3
        and len(directional) == math.comb(len(walls), 2) == 21
        and all(row["scope_match"] and row["exact_match"] for row in residuals)
        and len(residuals) == 3 and len(dropped_residuals) == 1
        and len(rhetoric) == len(partial) == 5 and len(echo) == 7
        and not any((gate["broad_no_go_claim"], gate["minimum_content_claim"], gate["shared_obstruction_claim"], gate["axiom_pressure_claim"]))
    )
    gate["pass"] = bool(condition)
    check("current N1-N8 schema fails the no-go gate while preserving only the narrowed coarse-algebraic positive", condition, gate)
    return gate


def domain_controls() -> dict[str, object]:
    rejected = 0
    operations = (
        lambda: c599.local_a2_source(2),
        lambda: c599.local_a2_source(3, 27),
        lambda: rotor_initial(1, "unknown"),
        lambda: c570.initial_word(1, counts=(2,)),
    )
    for operation in operations:
        try:
            operation()
        except ValueError:
            rejected += 1
    result = {"lawful_domain_rejections": rejected, "expected": len(operations)}
    condition = rejected == len(operations)
    result["pass"] = condition
    check("malformed sizes, sites, rotor laws, and event grammars are rejected", condition, result)
    return result


def note_contract() -> dict[str, object]:
    body = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 602", "route a", "route b", "route c",
        "q=1..4", "q=1..6", "transported", "all channels simultaneously", "no q-dependent selector",
        "conditional 53-role blueprint", "physical eg: null", "primitive product", "3:4", "4:4", "5:4",
        "update count is not time", "event count is not time", "phase is not energy",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure", "cycle599", "no back-credit", "author accepted: false",
        "breakthrough: false", "status: fail",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required": len(required), "missing": missing, "pass": not missing}
    check("the Cycle602 note freezes the new law, physical boundary, time firewall, and N1-N8", not missing, result)
    return result


def main() -> int:
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle602 transported-observable Ramsey / echo / event rotor", AUTHORITY, AUDIT)
    shore = shore_and_time_firewall()
    route_a = route_a_transported_observable()
    route_b = route_b_contact_reference_echo()
    route_c = route_c_reversible_one_hot_rotor()
    domain = domain_controls()
    gate = no_go_discipline(route_a, route_b, route_c)
    contract = note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "fixed transported A2 covector and declared contact-off echo reference remove finite coarse return blind spots; independent physical genesis remains open",
        "C_num": "nonzero finite L3/L6 phase words and exact finite-prefix rotor rollover; no empirical unit, arbitrary-q theorem, probability law, or time law",
        "C_wrap": "algebraic one-hot rotor carries a supplied origin and exact finite rollover receipts; physical origin genesis and matter-interval association remain open",
        "C_int": "coarse algebraic free-plus-contact arrays drive Route A and are discriminated against g=0 in Route B; no physical interaction primitive product is composed",
        "C_local": "coarse detector support has radius one and Boolean rotor gates have arity at most three; every Cycle602 physical E/G, placement, leakage, and primitive-product field is null",
        "C_source": "no source-conditioned Ramsey response, response sign, lapse, redshift, or gravity law is derived",
    }
    physical_boundary = {
        "route_A_physical_EG": route_a["physical_EG"],
        "route_A_physical_placement": route_a["physical_placement"],
        "route_A_physical_leakage": route_a["physical_leakage"],
        "route_A_physical_primitive_product": route_a["physical_primitive_product"],
        "route_B_physical_EG": route_b["physical_EG"],
        "route_B_physical_placement": route_b["physical_placement"],
        "route_B_physical_leakage": route_b["physical_leakage"],
        "route_B_physical_primitive_product": route_b["physical_primitive_product"],
        "route_C_physical_EG": route_c["physical_EG"],
        "route_C_physical_placement": route_c["physical_placement"],
        "route_C_physical_leakage": route_c["physical_leakage"],
        "route_C_physical_primitive_product": route_c["physical_primitive_product"],
    }
    check("all Cycle602 physical promotion fields remain null", all(value is None for value in physical_boundary.values()), physical_boundary)
    result = {
        "status": "PASS" if FAIL == 0 else "FAIL",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "tests_total": PASS + FAIL,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "breakthrough": False,
        "constitutional_effect": "none",
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "shore": shore,
        "route_A_transported_observable": route_a,
        "route_B_contact_reference_echo": route_b,
        "route_C_reversible_one_hot_rotor": route_c,
        "domain": domain,
        "no_go_discipline": gate,
        "note_contract": contract,
        "physical_composition_boundary": physical_boundary,
        "causal_time_PR5557_comparison_no_backcredit": CAUSAL_TIME_COMPARISON,
        "six_wall_ledger": ledger,
        "maturity_rebase": None,
        "highest_honest_terminal": (
            "finite fixed-coarse L3/L6 transported-A2 and contact-relative echo words plus a reversible finite-prefix one-hot Boolean rotor; "
            "no Cycle602 route executes physical-M2 E/G, placement, leakage or primitive composition, and no event, Record, proper time, lapse, "
            "energy, source response or universal clock equivalence is derived"
        ),
        "shared_obstruction": False,
        "axiom_pressure": False,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=json_default))
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
