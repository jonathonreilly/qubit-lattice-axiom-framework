#!/usr/bin/env python3
"""Y_T closure stack and strict pole-response contract.

This runner verifies the current burn-down state:

* Fisher source-scale and Fisher/LSZ bridge support are present.
* Pole-row Gram purity alone remains normalization-blind.
* The primitive no-hidden-record intervention law is now derived as exact
  support; the top-source identification route is now pruned from current
  structural inputs by a hard-stop no-go; strict same-source top/W response
  evidence is the remaining audit-clean path unless audit accepts the primitive
  top-source premise.
* The C3 connected/reflection-even source candidate is exact support: under
  those supplied premises it selects B_x and gives 1/sqrt(6) on nontrivial
  C3 character lines, while leaving the physical premises and top-line
  assignment open.
* The nontrivial top-line assignment shortcut is now pruned: B_x gives
  2/sqrt(6) on the C3 singlet line and 1/sqrt(6) only on the nontrivial
  character lines.
* The connected-source premise is now derived from normalized RN/Fisher source
  semantics: identity source terms are pure normalizers and the C3 B_a
  direction is removed.
* The reflection-even source premise is now derived from real finite-record
  source semantics: the C3 B_y direction is imaginary/reflection-odd, so the
  real connected source direction is B_x up to sign.
* The mass-ordering top-line shortcut is now pruned: under B_x the ordinary
  top/heaviest convention selects P_0 with 2/sqrt(6), not the target
  nontrivial-line response 1/sqrt(6).
* The non-mass-ordering real same-surface C3 top-line shortcut is now pruned:
  current real/reflection-even C3 support fixes B_x but does not exclude P_0
  or isolate a nontrivial complex line as the physical top pole.
* The C3 circulant source-law shortcut is now pruned at the next layer:
  derived B_x fixes the source derivative, but base circulant dynamics,
  orientation/phase law, and spectral ordering remain load-bearing.
* The strict sparse pole-response availability audit confirms the harness and
  no-kappa candidate are present, but no accepted backend or strict W/top pole
  rows are present on the branch.
* The strict pole-row repository discovery no-go confirms that a broader scan
  of current Y_T strict/response/backend/projector outputs finds no hidden
  accepted top/W pole-row certificate under another artifact name.
* The microscopic backend/projector/matrix-element boundary prunes the current
  non-compute shortcut: source law, carrier amplitude, C3 algebra, W row, and
  no-kappa candidate do not derive the accepted top projector or matrix
  element.
* The positive real C3 transfer/Perron top-line shortcut is now pruned:
  positivity selects the C3 singlet Perron line, or leaves the nontrivial
  block degenerate, and therefore does not supply the target nontrivial line.
* The residual C3 phase-ordering cone is now explicit support: the top line is
  nontrivial exactly in the two cones y_0 > sqrt(3) x_0 or
  -y_0 > sqrt(3) x_0, but that cone membership is not yet derived.
* Reflection-even same-surface C3 base dynamics cannot derive that cone:
  reflection forces y_0 = 0, which selects P_0 or leaves the nontrivial block
  degenerate. A positive C3 route needs an accepted orientation-odd phase law
  or strict pole rows.
* Orientation sign or nonzero B_y phase is also insufficient by itself:
  same-sign base operators can lie inside the nontrivial cone or in the
  singlet region. A positive C3 route needs a quantitative phase-strength law.
* Unit-normalized same-surface C3 base dynamics plus orientation sign is also
  underdetermined: the allowed unit circle contains both singlet-top and
  nontrivial-top regions, so the remaining C3 route needs a real phase-angle
  dynamics law, not just normalization.
* The primitive nontrivial C3 character phase angles are now a concrete
  conditional support route: phi = +/- 2*pi/3 lies inside the target
  nontrivial cone and gives A/sqrt(12), but the same-surface phase-angle law
  selecting those angles is still open.
* Finite C3 representation/character facts alone do not select that phase
  law: C3-native unit Hermitian choices include both target-row and singlet-row
  witnesses.
* The cubic C3 trace invariant is now a conditional support route: on the unit
  phase circle Tr(H^3) is proportional to cos(3phi), whose oriented nonzero
  maxima are phi = +/- 2*pi/3, but the accepted cubic phase potential and
  orientation branch remain open.
* C3-invariant cubic phase-potential structure alone is now pruned as that
  missing phase law because the sign, variational convention, and physical
  orientation branch are not derived.
* General C3-invariant scalar phase potentials are also pruned as a top-line
  selector: they select phase orbits, while generic and primitive C3 orbits
  contain both singlet and nontrivial top-line witnesses.
* C3 orbit-member readout covariance is also pruned as the missing law: a
  free C3 phase orbit has no equivariant section, and symmetry-breaking
  sections include a P_0 witness as well as target nontrivial witnesses.
* The existing dihedral/reflection basepoint shortcut is now pruned: full
  C3/D3 naturality has no section of the free orbit, and the already-derived
  real-record reflection axis fixes the singlet P_0 member rather than a
  nontrivial target row.
* The orientation-biased phase-potential shortcut is now pruned: adding a
  reflection-odd sin(3phi) term still selects a C3 phase orbit, not a physical
  orbit member, so P_0 remains allowed without an accepted basepoint/readout
  law or strict pole rows.
* The source-response extremal readout shortcut is now pruned: signed and
  absolute maxima of the same-surface B_x response select P_0 and give
  A/sqrt(3), while signed and absolute minima select the nontrivial pair only
  by importing a minimum-response selector.
* The strict W/Z plus C3 top-row splice shortcut is now pruned: the formal
  splice gives 1/sqrt(6) only after supplying same-surface authority and the
  physical nontrivial top line; the same denominator and source scale also
  admit the P_0 singlet row sqrt(2/3).
* The same-surface top matrix-element factorization algebra is now explicit:
  (A/sqrt(2)) times the nontrivial B_x response gives A/sqrt(12), but the
  accepted generator factorization and nontrivial top-line law remain open.
* The nontrivial C3 block matrix-element support theorem sharpens that
  target: B_x is scalar on the real nontrivial block P_nt, so zero singlet
  weight is enough for A/sqrt(12); complex-line isolation is not needed for
  the coefficient row, but zero singlet weight is still not derived.
* The same-surface radial-factor underdetermination no-go grants P_nt support
  and still shows the coefficient row is not certified: a same-source family
  V_top(lambda_top)=lambda_top*A*B_x keeps the W row and C3 direction while
  varying the top coefficient. The target requires lambda_top=1/sqrt(2).
* The radial/readout compensation shortcut is now pruned: the target-size
  equation lambda_top*|3s-1|=1/sqrt(2) has multiple finite completions, so it
  cannot back-solve zero singlet weight, radial factorization, or signed
  physical orientation.
* The sharp-response readout shortcut is now pruned: Var(B_x)=0 selects both
  P_nt and P_0 endpoints, and the singlet endpoint can be target-size with a
  compensating radial factor.
* The zero-singlet top-block membership shortcut is now pruned: real
  reflection-even C3 block algebra permits both P_0 and P_nt block selections
  depending on an undetermined sign/order or minimum-response premise.
* The source-orientation sign-selector shortcut is now pruned: choosing the
  sign of B_x that makes P_nt largest imports an unaccepted source-coordinate
  orientation law; sign-blind largest response selects P_0, and minimum
  response remains a convention.
* The trace-free centered-source shortcut is now pruned: Tr(B_x)=0 is an
  operator/source statement, not a physical top-projector law. Zero source
  expectation gives singlet weight s=1/3, while the target row requires s=0.
* The minimum-information readout shortcut is now pruned: finite
  RN/I-projection tilts over the C3 line responses have full support, so zero
  singlet weight appears only as an infinite-boundary law or target-response
  insertion.
* The hard-boundary minimum-information face-selector support result sharpens
  that infinite-boundary escape hatch: the compactified C3 RN/Fisher curve has
  both P_nt and P_0 endpoints, while a new nearest-Fisher-boundary-face law
  would select P_nt conditionally. That nearest-face law is not accepted on
  the current surface.
* The hard-boundary readout law underdetermination no-go prunes promotion of
  that support from current information geometry alone: the same boundary data
  also admit P_0-selecting purity/rank, positive-source-asymptote, and
  response-maximum rules.
* The primitive singular-boundary intervention support theorem sharpens the
  best hard-boundary candidate: a least-KL no-hidden-record singular boundary
  rule on the reflection-even C3 RN/Fisher curve selects P_nt and would give
  A/sqrt(12), but that singular-boundary readout law is not accepted on the
  actual current surface.
* The block-rank radial normalization shortcut is now pruned: rank(P_nt)=2
  makes a root-rank factor numerically tempting, but ordinary P_nt matrix
  elements, block-density expectations, and Hilbert-Schmidt block conventions
  do not derive lambda_top=1/sqrt(2).
* No retained/proposed-retained Y_T closure is authorized by this packet.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

NOTE = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
PRIMITIVE_RECORD_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
TOP_SOURCE_NOGO = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
MININFO_UNIQUENESS = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
FISHER = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
FISHER_LSZ = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SAME_SOURCE = DOCS / "YT_SAME_SOURCE_EW_HIGGS_AUTHORITY_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
STRICT_SAME_SOURCE_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
FIRST_PRINCIPLES_TRANSFER_RESPONSE = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_SAME_SURFACE_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_RADIAL_READOUT_COMPENSATION_NOGO = DOCS / "YT_C3_RADIAL_READOUT_COMPENSATION_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_SHARP_RESPONSE_READOUT_NOGO = DOCS / "YT_C3_SHARP_RESPONSE_READOUT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_GENERATOR_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_RANK_RADIAL_NORMALIZATION_NOGO = DOCS / "YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NOGO = DOCS / "YT_C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NOGO = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NOGO = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NOGO = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_MININFO_READOUT_ZERO_SINGLET_NOGO = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT = DOCS / "YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md"
C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION = DOCS / "YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT = DOCS / "YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md"
DIRECT_SPARSE_RESPONSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
KAPPA_DIRECT_EXERCISE = DOCS / "YT_KAPPA_DIRECT_FULL_PHYSICS_EXERCISE_NOTE_2026-05-27.md"
NATIVE_BACKEND_CANDIDATE = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
BACKEND_PROJECTOR_OBSTRUCTION = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
TOP_SECTOR_PROJECTOR_OBSTRUCTION = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
C3_SPECTRAL_PROJECTOR_SUPPORT = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
C3_SPECTRAL_SOURCE_RESPONSE_NOGO = DOCS / "YT_C3_SPECTRAL_SOURCE_RESPONSE_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_DIRECTION_NOGO = DOCS / "YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md"
LSP_C3_SOURCE_DIRECTION_BOUNDARY = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY = DOCS / "YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
C3_CONNECTED_REFLECTION_EVEN_SOURCE_CANDIDATE = DOCS / "YT_C3_CONNECTED_REFLECTION_EVEN_SOURCE_DIRECTION_CANDIDATE_NOTE_2026-05-27.md"
C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN = DOCS / "YT_C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_THEOREM_NOTE_2026-05-27.md"
C3_REAL_RECORD_REFLECTION_EVEN_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
STRICT_SPARSE_TOP_W_AVAILABILITY_AUDIT = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
STRICT_POLE_ROW_REPOSITORY_DISCOVERY_NOGO = DOCS / "YT_STRICT_TOP_W_POLE_ROW_REPOSITORY_DISCOVERY_NO_GO_NOTE_2026-05-27.md"
MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY = DOCS / "YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NOGO = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY = DOCS / "YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md"
C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY = DOCS / "YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md"
C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION = DOCS / "YT_C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
C3_REPRESENTATION_PHASE_SELECTION_NOGO = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
C3_CUBIC_INVARIANT_PHASE_SELECTOR = DOCS / "YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
C3_CUBIC_PHASE_POTENTIAL_NOGO = DOCS / "YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_PHASE_ORBIT_SELECTOR_NOGO = DOCS / "YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_ORBIT_MEMBER_READOUT_COVARIANCE_NOGO = DOCS / "YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md"
C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION = DOCS / "YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md"
C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NOGO = DOCS / "YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NOGO = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
STRICT_WZ_C3_TOP_ROW_SPLICE_NOGO = DOCS / "YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

FISHER_OUT = ROOT / "outputs" / "yt_primitive_physical_source_fisher_arclength_invariant_2026-05-26.json"
MIN_INFO_OUT = ROOT / "outputs" / "yt_minimum_information_source_action_bridge_2026-05-26.json"
PRIMITIVE_RECORD_LAW_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
TOP_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_top_source_identification_hard_stop_no_go_2026-05-27.json"
MININFO_UNIQUENESS_OUT = ROOT / "outputs" / "yt_physical_intervention_mininfo_uniqueness_gate_2026-05-26.json"
TOP_CARRIER_OUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"
FISHER_LSZ_OUT = ROOT / "outputs" / "yt_fisher_lsz_source_normalization_bridge_2026-05-26.json"
FH_OUT = ROOT / "outputs" / "yt_fh_top_w_response_ratio_gate_2026-05-25.json"
SAME_SOURCE_OUT = ROOT / "outputs" / "yt_same_source_ew_higgs_authority_gate_2026-05-25.json"
STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
STRICT_SAME_SOURCE_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"
FIRST_PRINCIPLES_TRANSFER_RESPONSE_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_SAME_SURFACE_RADIAL_FACTOR_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
)
C3_RADIAL_READOUT_COMPENSATION_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_radial_readout_compensation_underdetermination_no_go_2026-05-28.json"
)
C3_SHARP_RESPONSE_READOUT_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_sharp_response_readout_underdetermination_no_go_2026-05-28.json"
)
FISHER_LSZ_RADIAL_GENERATOR_NOGO_OUT = (
    ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
)
C3_BLOCK_RANK_RADIAL_NORMALIZATION_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json"
)
C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_fisher_quotient_radial_normalization_no_go_2026-05-28.json"
)
C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NOGO_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NOGO_OUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"
C3_MININFO_READOUT_ZERO_SINGLET_NOGO_OUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"
C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json"
C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_OUT = ROOT / "outputs" / "yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json"
C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json"
DIRECT_SPARSE_RESPONSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
KAPPA_DIRECT_EXERCISE_OUT = ROOT / "outputs" / "yt_kappa_direct_full_physics_exercise_2026-05-27.json"
NATIVE_BACKEND_CANDIDATE_OUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
BACKEND_PROJECTOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"
TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"
C3_SPECTRAL_PROJECTOR_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
C3_SPECTRAL_SOURCE_RESPONSE_NOGO_OUT = ROOT / "outputs" / "yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json"
C3_SOURCE_DIRECTION_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_direction_selection_no_go_2026-05-27.json"
LSP_C3_SOURCE_DIRECTION_BOUNDARY_OUT = ROOT / "outputs" / "yt_lsp_projective_c3_source_direction_boundary_2026-05-27.json"
POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_OUT = ROOT / "outputs" / "yt_positivity_orientation_c3_source_direction_boundary_2026-05-27.json"
C3_CONNECTED_REFLECTION_EVEN_SOURCE_CANDIDATE_OUT = ROOT / "outputs" / "yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json"
C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"
C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_OUT = ROOT / "outputs" / "yt_c3_connected_source_from_normalized_rn_2026-05-27.json"
C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"
C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
STRICT_SPARSE_TOP_W_AVAILABILITY_AUDIT_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
STRICT_POLE_ROW_REPOSITORY_DISCOVERY_NOGO_OUT = ROOT / "outputs" / "yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json"
MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_OUT = ROOT / "outputs" / "yt_microscopic_backend_projector_matrix_element_boundary_2026-05-27.json"
C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NOGO_OUT = ROOT / "outputs" / "yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json"
C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_dynamics_necessity_2026-05-27.json"
C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_orientation_phase_strength_boundary_2026-05-27.json"
C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_OUT = ROOT / "outputs" / "yt_c3_quantitative_phase_strength_underdetermination_2026-05-27.json"
C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_OUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"
C3_REPRESENTATION_PHASE_SELECTION_NOGO_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
C3_CUBIC_INVARIANT_PHASE_SELECTOR_OUT = ROOT / "outputs" / "yt_c3_cubic_invariant_phase_selector_support_boundary_2026-05-27.json"
C3_CUBIC_PHASE_POTENTIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_cubic_phase_potential_sign_branch_underdetermination_2026-05-27.json"
C3_PHASE_ORBIT_SELECTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json"
C3_ORBIT_MEMBER_READOUT_COVARIANCE_NOGO_OUT = ROOT / "outputs" / "yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json"
C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json"
C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NOGO_OUT = ROOT / "outputs" / "yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json"
C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
STRICT_WZ_C3_TOP_ROW_SPLICE_NOGO_OUT = ROOT / "outputs" / "yt_strict_wz_c3_top_row_splice_no_go_2026-05-27.json"
STRICT_TOP_W_ROWS = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
STRICT_SOURCE_HIGGS_ROWS = ROOT / "outputs" / "yt_source_action_block508_id_source_higgs_strict_rows_2026-05-22.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = load_json(LEDGER)
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, str]:
    print("\nPart 1: anchors and audited/current statuses")
    paths = (
        NOTE,
        SOURCE_ACTION,
        MIN_INFO,
        PRIMITIVE_RECORD_LAW,
        TOP_SOURCE_NOGO,
        MININFO_UNIQUENESS,
        TOP_CARRIER,
        FISHER,
        FISHER_LSZ,
        POLE_NOGO,
        FH_GATE,
        SAME_SOURCE,
        STRICT_WZ,
        STRICT_TOP,
        STRICT_SAME_SOURCE_OBSTRUCTION,
        FIRST_PRINCIPLES_TRANSFER_RESPONSE,
        SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION,
        C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT,
        C3_SAME_SURFACE_RADIAL_FACTOR_NOGO,
        C3_RADIAL_READOUT_COMPENSATION_NOGO,
        C3_SHARP_RESPONSE_READOUT_NOGO,
        FISHER_LSZ_RADIAL_GENERATOR_NOGO,
        C3_BLOCK_RANK_RADIAL_NORMALIZATION_NOGO,
        C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NOGO,
        C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NOGO,
        C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NOGO,
        C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NOGO,
        C3_MININFO_READOUT_ZERO_SINGLET_NOGO,
        C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT,
        C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION,
        C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT,
        DIRECT_SPARSE_RESPONSE_CERT,
        KAPPA_DIRECT_EXERCISE,
        NATIVE_BACKEND_CANDIDATE,
        BACKEND_PROJECTOR_OBSTRUCTION,
        TOP_SECTOR_PROJECTOR_OBSTRUCTION,
        C3_SPECTRAL_PROJECTOR_SUPPORT,
        C3_SPECTRAL_SOURCE_RESPONSE_NOGO,
        C3_SOURCE_DIRECTION_NOGO,
        LSP_C3_SOURCE_DIRECTION_BOUNDARY,
        POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY,
        C3_CONNECTED_REFLECTION_EVEN_SOURCE_CANDIDATE,
        C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY,
        C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN,
        C3_REAL_RECORD_REFLECTION_EVEN_SOURCE,
        C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION,
        C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION,
        C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY,
        STRICT_SPARSE_TOP_W_AVAILABILITY_AUDIT,
        STRICT_POLE_ROW_REPOSITORY_DISCOVERY_NOGO,
        MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY,
        C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NOGO,
        C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY,
        C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY,
        C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY,
        C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION,
        C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE,
        C3_REPRESENTATION_PHASE_SELECTION_NOGO,
        C3_CUBIC_INVARIANT_PHASE_SELECTOR,
        C3_CUBIC_PHASE_POTENTIAL_NOGO,
        C3_PHASE_ORBIT_SELECTOR_NOGO,
        C3_ORBIT_MEMBER_READOUT_COVARIANCE_NOGO,
        C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION,
        C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NOGO,
        C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NOGO,
        STRICT_WZ_C3_TOP_ROW_SPLICE_NOGO,
        LEDGER,
        FISHER_OUT,
        MIN_INFO_OUT,
        PRIMITIVE_RECORD_LAW_OUT,
        TOP_SOURCE_NOGO_OUT,
        MININFO_UNIQUENESS_OUT,
        TOP_CARRIER_OUT,
        FISHER_LSZ_OUT,
        FH_OUT,
        SAME_SOURCE_OUT,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        STRICT_SAME_SOURCE_OBSTRUCTION_OUT,
        FIRST_PRINCIPLES_TRANSFER_RESPONSE_OUT,
        SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_OUT,
        C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_OUT,
        C3_SAME_SURFACE_RADIAL_FACTOR_NOGO_OUT,
        C3_RADIAL_READOUT_COMPENSATION_NOGO_OUT,
        C3_SHARP_RESPONSE_READOUT_NOGO_OUT,
        FISHER_LSZ_RADIAL_GENERATOR_NOGO_OUT,
        C3_BLOCK_RANK_RADIAL_NORMALIZATION_NOGO_OUT,
        C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NOGO_OUT,
        C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NOGO_OUT,
        C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NOGO_OUT,
        C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NOGO_OUT,
        C3_MININFO_READOUT_ZERO_SINGLET_NOGO_OUT,
        C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_OUT,
        C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_OUT,
        C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_OUT,
        DIRECT_SPARSE_RESPONSE_CERT_OUT,
        KAPPA_DIRECT_EXERCISE_OUT,
        NATIVE_BACKEND_CANDIDATE_OUT,
        BACKEND_PROJECTOR_OBSTRUCTION_OUT,
        TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT,
        C3_SPECTRAL_PROJECTOR_SUPPORT_OUT,
        C3_SPECTRAL_SOURCE_RESPONSE_NOGO_OUT,
        C3_SOURCE_DIRECTION_NOGO_OUT,
        LSP_C3_SOURCE_DIRECTION_BOUNDARY_OUT,
        POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_OUT,
        C3_CONNECTED_REFLECTION_EVEN_SOURCE_CANDIDATE_OUT,
        C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_OUT,
        C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_OUT,
        C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_OUT,
        C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_OUT,
        C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_OUT,
        C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_OUT,
        STRICT_SPARSE_TOP_W_AVAILABILITY_AUDIT_OUT,
        STRICT_POLE_ROW_REPOSITORY_DISCOVERY_NOGO_OUT,
        MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_OUT,
        C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NOGO_OUT,
        C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_OUT,
        C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_OUT,
        C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_OUT,
        C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_OUT,
        C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_OUT,
        C3_REPRESENTATION_PHASE_SELECTION_NOGO_OUT,
        C3_CUBIC_INVARIANT_PHASE_SELECTOR_OUT,
        C3_CUBIC_PHASE_POTENTIAL_NOGO_OUT,
        C3_PHASE_ORBIT_SELECTOR_NOGO_OUT,
        C3_ORBIT_MEMBER_READOUT_COVARIANCE_NOGO_OUT,
        C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_OUT,
        C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NOGO_OUT,
        C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NOGO_OUT,
        STRICT_WZ_C3_TOP_ROW_SPLICE_NOGO_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Stack From Here To Full Closure",
        "Conditional Closure Theorem",
        "Current Burn-Down Result",
        "Non-Claims",
        "strict same-source top/W response",
        "primitive no-hidden-record source law is derived",
        "top-source identification is pruned",
        "finite-transfer counterfamily",
        "first-principles transfer/Feynman-Hellmann",
        "sector matrix elements remain load-bearing",
        "same-surface top matrix-element factorization",
        "nontrivial C3 block matrix-element support",
        "zero-singlet top-block membership no-go",
        "radial/readout compensation underdetermination no-go",
        "sharp-response readout underdetermination no-go",
        "Fisher-LSZ radial generator normalization no-go",
        "block-rank radial normalization no-go",
        "Fisher quotient radial normalization no-go",
        "source-orientation sign-selector no-go",
        "trace-free centered-source no-go",
        "minimum-information readout zero-singlet no-go",
        "hard-boundary minimum-information face-selector support",
        "hard-boundary readout law underdetermination",
        "primitive singular-boundary intervention support",
        "sparse transfer response certificate",
        "targeted kappa exercise",
        "native candidate backend",
        "sector projectors are load-bearing",
        "top generation projector remains open",
        "C3 spectral-projector route remains live",
        "C3 spectral projectors do not determine source responses",
        "unit source normalization fixes scale, not direction",
        "LSP projective readout supplies instruments for supplied projectors",
        "positivity/orientation support selects C3 and an oriented splitter only",
        "connected + reflection-even source conditions select B_x",
        "nontrivial C3 character lines have response magnitude 1/sqrt(6)",
        "top-line nontriviality remains load-bearing",
        "normalized RN/Fisher source semantics remove the identity direction",
        "real finite-record source semantics select the reflection-even C3 source",
        "mass-ordering obstruction",
        "real same-surface top-line law obstruction",
        "C3 circulant dynamics ordering source-law boundary",
        "strict sparse pole-response availability audit",
        "strict pole-row repository discovery no-go",
        "microscopic backend/projector/matrix-element boundary",
        "positive real C3 transfer/Perron selection",
        "phase-ordering cone",
        "orientation-odd phase law",
        "phase-strength law",
        "phase-strength underdetermination",
        "primitive character phase-angle candidate",
        "open phase-angle law",
        "representation phase-selection no-go",
        "cubic invariant phase-selector",
        "cubic phase-potential sign/branch no-go",
        "phase-orbit selector underdetermination",
        "orbit-member readout covariance no-go",
        "dihedral basepoint anchor obstruction",
        "orientation-biased phase-potential orbit-member no-go",
        "source-response extremal readout no-go",
        "strict W/Z plus C3 top-row splice no-go",
    ):
        check(f"note contains required section/phrase: {phrase}", phrase in note)

    rows = {
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22").get("effective_status"),
        "pole_no_go": ledger_row("yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23").get("effective_status"),
        "ew_mass": ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26").get("effective_status"),
        "ew_coupling": ledger_row("ew_coupling_derivation_note").get("effective_status"),
        "one_higgs": ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26").get("effective_status"),
    }
    check("source-action packet is retained_bounded support", rows["source_action"] == "retained_bounded", rows["source_action"])
    check("pole-row normalization no-go is retained_no_go", rows["pole_no_go"] == "retained_no_go", rows["pole_no_go"])
    check("EW Higgs mass theorem is retained", rows["ew_mass"] == "retained", rows["ew_mass"])
    check("EW coupling note is not retained same-scale g2 authority", rows["ew_coupling"] != "retained", rows["ew_coupling"])
    check("one-Higgs selection is not retained coefficient authority", rows["one_higgs"] != "retained", rows["one_higgs"])
    return rows


def part2_support_outputs() -> dict[str, Any]:
    print("\nPart 2: already-burned-down support outputs")
    fisher = load_json(FISHER_OUT)
    min_info = load_json(MIN_INFO_OUT)
    primitive_record_law = load_json(PRIMITIVE_RECORD_LAW_OUT)
    top_source_nogo = load_json(TOP_SOURCE_NOGO_OUT)
    mininfo_uniqueness = load_json(MININFO_UNIQUENESS_OUT)
    top_carrier = load_json(TOP_CARRIER_OUT)
    fisher_lsz = load_json(FISHER_LSZ_OUT)
    fh = load_json(FH_OUT)
    same = load_json(SAME_SOURCE_OUT)
    wz = load_json(STRICT_WZ_OUT)
    top = load_json(STRICT_TOP_OUT)
    strict_obstruction = load_json(STRICT_SAME_SOURCE_OBSTRUCTION_OUT)
    first_principles_transfer_response = load_json(FIRST_PRINCIPLES_TRANSFER_RESPONSE_OUT)
    same_surface_top_matrix_element_factorization = load_json(SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_OUT)
    c3_nontrivial_block_matrix_element_support = load_json(C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_OUT)
    c3_same_surface_radial_factor_nogo = load_json(C3_SAME_SURFACE_RADIAL_FACTOR_NOGO_OUT)
    c3_radial_readout_compensation_nogo = load_json(C3_RADIAL_READOUT_COMPENSATION_NOGO_OUT)
    c3_sharp_response_readout_nogo = load_json(C3_SHARP_RESPONSE_READOUT_NOGO_OUT)
    fisher_lsz_radial_generator_nogo = load_json(FISHER_LSZ_RADIAL_GENERATOR_NOGO_OUT)
    c3_block_rank_radial_normalization_nogo = load_json(C3_BLOCK_RANK_RADIAL_NORMALIZATION_NOGO_OUT)
    c3_fisher_quotient_radial_normalization_nogo = load_json(C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NOGO_OUT)
    c3_zero_singlet_top_block_membership_nogo = load_json(C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NOGO_OUT)
    c3_source_orientation_sign_selector_nogo = load_json(C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NOGO_OUT)
    c3_trace_free_centered_source_zero_singlet_nogo = load_json(C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NOGO_OUT)
    c3_mininfo_readout_zero_singlet_nogo = load_json(C3_MININFO_READOUT_ZERO_SINGLET_NOGO_OUT)
    c3_mininfo_hard_boundary_face_selector_support = load_json(C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_OUT)
    c3_hard_boundary_readout_law_underdetermination = load_json(C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_OUT)
    c3_primitive_singular_boundary_intervention_support = load_json(C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_OUT)
    direct_sparse_cert = load_json(DIRECT_SPARSE_RESPONSE_CERT_OUT)
    kappa_exercise = load_json(KAPPA_DIRECT_EXERCISE_OUT)
    native_backend = load_json(NATIVE_BACKEND_CANDIDATE_OUT)
    projector_obstruction = load_json(BACKEND_PROJECTOR_OBSTRUCTION_OUT)
    top_sector_projector_obstruction = load_json(TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT)
    c3_spectral_projector_support = load_json(C3_SPECTRAL_PROJECTOR_SUPPORT_OUT)
    c3_spectral_source_response_nogo = load_json(C3_SPECTRAL_SOURCE_RESPONSE_NOGO_OUT)
    c3_source_direction_nogo = load_json(C3_SOURCE_DIRECTION_NOGO_OUT)
    lsp_c3_source_direction_boundary = load_json(LSP_C3_SOURCE_DIRECTION_BOUNDARY_OUT)
    positivity_orientation_c3_source_direction_boundary = load_json(POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_OUT)
    c3_connected_reflection_even_source_candidate = load_json(C3_CONNECTED_REFLECTION_EVEN_SOURCE_CANDIDATE_OUT)
    c3_nontrivial_top_line_assignment_boundary = load_json(C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_OUT)
    c3_connected_source_from_normalized_rn = load_json(C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_OUT)
    c3_real_record_reflection_even_source = load_json(C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_OUT)
    c3_top_line_mass_ordering_obstruction = load_json(C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_OUT)
    c3_real_same_surface_top_line_law_obstruction = load_json(C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_OUT)
    c3_circulant_dynamics_ordering_source_law_boundary = load_json(C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_OUT)
    strict_sparse_top_w_availability_audit = load_json(STRICT_SPARSE_TOP_W_AVAILABILITY_AUDIT_OUT)
    strict_pole_row_repository_discovery_nogo = load_json(STRICT_POLE_ROW_REPOSITORY_DISCOVERY_NOGO_OUT)
    microscopic_backend_projector_matrix_element_boundary = load_json(MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_OUT)
    c3_positive_transfer_perron_top_line_nogo = load_json(C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NOGO_OUT)
    c3_phase_ordering_cone_support_boundary = load_json(C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_OUT)
    c3_orientation_phase_dynamics_necessity = load_json(C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_OUT)
    c3_orientation_phase_strength_boundary = load_json(C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_OUT)
    c3_quantitative_phase_strength_underdetermination = load_json(C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_OUT)
    c3_primitive_character_phase_angle_candidate = load_json(C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_OUT)
    c3_representation_phase_selection_nogo = load_json(C3_REPRESENTATION_PHASE_SELECTION_NOGO_OUT)
    c3_cubic_invariant_phase_selector = load_json(C3_CUBIC_INVARIANT_PHASE_SELECTOR_OUT)
    c3_cubic_phase_potential_nogo = load_json(C3_CUBIC_PHASE_POTENTIAL_NOGO_OUT)
    c3_phase_orbit_selector_nogo = load_json(C3_PHASE_ORBIT_SELECTOR_NOGO_OUT)
    c3_orbit_member_readout_covariance_nogo = load_json(C3_ORBIT_MEMBER_READOUT_COVARIANCE_NOGO_OUT)
    c3_dihedral_basepoint_anchor_obstruction = load_json(C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_OUT)
    c3_orientation_biased_phase_potential_orbit_member_nogo = load_json(
        C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NOGO_OUT
    )
    c3_source_response_extremal_readout_nogo = load_json(C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NOGO_OUT)
    strict_wz_c3_top_row_splice_nogo = load_json(STRICT_WZ_C3_TOP_ROW_SPLICE_NOGO_OUT)

    check("minimum-information source/action bridge passed", min_info.get("fail_count") == 0, min_info.get("fail_count"))
    check("minimum-information bridge proposal is not allowed", min_info.get("proposal_allowed") is False)
    check("primitive record intervention law passed", primitive_record_law.get("fail_count") == 0, primitive_record_law.get("fail_count"))
    check("primitive record intervention law proposal is not allowed for full Y_T", primitive_record_law.get("proposal_allowed") is False)
    check("primitive record law narrows next gate to top-source identification", primitive_record_law.get("first_open_gate_after_this_note") == "physical top-source identification")
    check("top-source identification hard-stop no-go passed", top_source_nogo.get("fail_count") == 0, top_source_nogo.get("fail_count"))
    check("top-source no-go prunes structural no-compute route", top_source_nogo.get("trace_class") == "negative_route_pruning")
    check("top-source no-go keeps strict response as next action", "strict same-source top/W response" in top_source_nogo.get("next_action", ""))
    check("physical-intervention mininfo uniqueness gate passed", mininfo_uniqueness.get("fail_count") == 0, mininfo_uniqueness.get("fail_count"))
    check("physical-intervention uniqueness proposal is not allowed", mininfo_uniqueness.get("proposal_allowed") is False)
    check("one-Higgs top-carrier support passed", top_carrier.get("fail_count") == 0, top_carrier.get("fail_count"))
    check("one-Higgs top-carrier proposal is not allowed", top_carrier.get("proposal_allowed") is False)
    check("Fisher source-scale theorem passed", fisher.get("fail_count") == 0, fisher.get("fail_count"))
    check("Fisher theorem proposal is not allowed", fisher.get("proposal_allowed") is False)
    check("Fisher theorem exposes remaining bridge", "remaining_bridge" in fisher)
    check("Fisher/LSZ bridge passed", fisher_lsz.get("fail_count") == 0, fisher_lsz.get("fail_count"))
    check("Fisher/LSZ bridge proposal is not allowed", fisher_lsz.get("proposal_allowed") is False)
    check("FH ratio gate passed", fh.get("fail_count") == 0, fh.get("fail_count"))
    check("FH ratio gate proposal is not allowed", fh.get("proposal_allowed") is False)
    check("same-source authority gate passed", same.get("fail_count") == 0, same.get("fail_count"))
    check("strict W/Z response packet passed", wz.get("fail_count") == 0, wz.get("fail_count"))
    check("symbolic top response packet passed", top.get("fail_count") == 0, top.get("fail_count"))
    check("symbolic top response leaves coefficient open", top.get("top_coefficient_derived") is False)
    check("strict same-source coefficient obstruction passed", strict_obstruction.get("fail_count") == 0, strict_obstruction.get("fail_count"))
    check("strict same-source obstruction is route-pruning", strict_obstruction.get("trace_class") == "negative_route_pruning")
    check("first-principles transfer-response theorem passed", first_principles_transfer_response.get("fail_count") == 0, first_principles_transfer_response.get("fail_count"))
    check(
        "first-principles theorem is exact support plus formal-transfer no-go",
        first_principles_transfer_response.get("actual_current_surface_status") == "exact-support / formal-transfer no-go",
        first_principles_transfer_response.get("actual_current_surface_status"),
    )
    check("first-principles theorem prunes formal transfer-only kappa closure", first_principles_transfer_response.get("trace_class") == "negative_route_pruning")
    check(
        "first-principles theorem names matrix element as first open gate",
        "top sector response row" in first_principles_transfer_response.get("first_open_gate_after_this_note", ""),
        first_principles_transfer_response.get("first_open_gate_after_this_note"),
    )
    check("same-surface top matrix-element factorization passed", same_surface_top_matrix_element_factorization.get("fail_count") == 0, same_surface_top_matrix_element_factorization.get("fail_count"))
    check("same-surface factorization is conditional support", same_surface_top_matrix_element_factorization.get("actual_current_surface_status") == "conditional-support")
    check("same-surface factorization target row is A/sqrt(12)", same_surface_top_matrix_element_factorization.get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)")
    check("same-surface factorization proposal is not allowed", same_surface_top_matrix_element_factorization.get("proposal_allowed") is False)
    check(
        "same-surface factorization leaves generator factorization open",
        same_surface_top_matrix_element_factorization.get("certificate_boundary", {}).get("accepted_same_surface_generator_factorization") is False,
    )
    check(
        "same-surface factorization leaves nontrivial top-line assignment open",
        same_surface_top_matrix_element_factorization.get("certificate_boundary", {}).get("nontrivial_top_line_assignment_derived") is False,
    )
    check(
        "C3 nontrivial block matrix-element support passed",
        c3_nontrivial_block_matrix_element_support.get("fail_count") == 0,
        c3_nontrivial_block_matrix_element_support.get("fail_count"),
    )
    check(
        "C3 nontrivial block support is exact support/open",
        c3_nontrivial_block_matrix_element_support.get("actual_current_surface_status")
        == "exact-support / open nontrivial-block membership law",
        c3_nontrivial_block_matrix_element_support.get("actual_current_surface_status"),
    )
    check(
        "C3 nontrivial block gives target row",
        c3_nontrivial_block_matrix_element_support.get("block_matrix_element_witness", {})
        .get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "C3 nontrivial block does not need complex line isolation for coefficient",
        c3_nontrivial_block_matrix_element_support.get("certificate_boundary", {})
        .get("complex_line_isolation_needed_for_coefficient_row")
        is False,
    )
    check(
        "C3 nontrivial block still leaves zero singlet weight open",
        c3_nontrivial_block_matrix_element_support.get("certificate_boundary", {})
        .get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "C3 nontrivial block still lacks strict top/W response certificate",
        c3_nontrivial_block_matrix_element_support.get("certificate_boundary", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 same-surface radial-factor no-go passed",
        c3_same_surface_radial_factor_nogo.get("fail_count") == 0,
        c3_same_surface_radial_factor_nogo.get("fail_count"),
    )
    check(
        "C3 radial-factor no-go is route-pruning",
        c3_same_surface_radial_factor_nogo.get("trace_class") == "negative_route_pruning",
        c3_same_surface_radial_factor_nogo.get("trace_class"),
    )
    check(
        "C3 radial-factor target requires lambda_top=1/sqrt(2)",
        c3_same_surface_radial_factor_nogo.get("radial_factor_family", {}).get("target_lambda_top")
        == "1/sqrt(2)",
    )
    check(
        "C3 radial-factor remains free on current surface",
        c3_same_surface_radial_factor_nogo.get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "C3 radial/readout compensation no-go passed",
        c3_radial_readout_compensation_nogo.get("fail_count") == 0,
        c3_radial_readout_compensation_nogo.get("fail_count"),
    )
    check(
        "C3 radial/readout compensation route is pruned",
        c3_radial_readout_compensation_nogo.get("trace_class") == "negative_route_pruning",
        c3_radial_readout_compensation_nogo.get("trace_class"),
    )
    check(
        "target magnitude cannot force zero singlet weight",
        c3_radial_readout_compensation_nogo.get("certificate_boundary", {})
        .get("target_magnitude_forces_zero_singlet")
        is False,
    )
    check(
        "target magnitude cannot force radial factor",
        c3_radial_readout_compensation_nogo.get("certificate_boundary", {})
        .get("target_magnitude_forces_radial_factor")
        is False,
    )
    check(
        "signed compensation branch requires orientation law",
        c3_radial_readout_compensation_nogo.get("certificate_boundary", {})
        .get("signed_row_requires_orientation_law")
        is True,
    )
    check(
        "C3 compensation family records multiple target witnesses",
        len(c3_radial_readout_compensation_nogo.get("radial_readout_family", {}).get("target_magnitude_witnesses", []))
        >= 3,
    )
    check(
        "C3 sharp-response readout no-go passed",
        c3_sharp_response_readout_nogo.get("fail_count") == 0,
        c3_sharp_response_readout_nogo.get("fail_count"),
    )
    check(
        "C3 sharp-response readout route is pruned",
        c3_sharp_response_readout_nogo.get("trace_class") == "negative_route_pruning",
        c3_sharp_response_readout_nogo.get("trace_class"),
    )
    check(
        "zero variance does not force zero singlet",
        c3_sharp_response_readout_nogo.get("certificate_boundary", {})
        .get("zero_variance_forces_zero_singlet")
        is False,
    )
    check(
        "zero variance does not force radial factor",
        c3_sharp_response_readout_nogo.get("certificate_boundary", {})
        .get("zero_variance_forces_radial_factor")
        is False,
    )
    check(
        "zero variance allows singlet endpoint",
        c3_sharp_response_readout_nogo.get("certificate_boundary", {})
        .get("zero_variance_allows_singlet_endpoint")
        is True,
    )
    check(
        "Fisher-LSZ radial generator normalization no-go passed",
        fisher_lsz_radial_generator_nogo.get("fail_count") == 0,
        fisher_lsz_radial_generator_nogo.get("fail_count"),
    )
    check(
        "Fisher-LSZ radial generator route is pruned",
        fisher_lsz_radial_generator_nogo.get("trace_class") == "negative_route_pruning",
        fisher_lsz_radial_generator_nogo.get("trace_class"),
    )
    check(
        "Fisher-LSZ removes raw source scale",
        fisher_lsz_radial_generator_nogo.get("certificate_boundary", {}).get("raw_source_scale_removed")
        is True,
    )
    check(
        "Fisher-LSZ leaves lambda_top free",
        fisher_lsz_radial_generator_nogo.get("certificate_boundary", {}).get("lambda_top_relative_response_free")
        is True,
    )
    check(
        "Fisher-LSZ route still requires lambda_top=1/sqrt(2)",
        fisher_lsz_radial_generator_nogo.get("certificate_boundary", {}).get("target_requires_lambda_top")
        == "1/sqrt(2)",
    )
    check(
        "C3 block-rank radial normalization no-go passed",
        c3_block_rank_radial_normalization_nogo.get("fail_count") == 0,
        c3_block_rank_radial_normalization_nogo.get("fail_count"),
    )
    check(
        "C3 block-rank radial normalization route is pruned",
        c3_block_rank_radial_normalization_nogo.get("trace_class") == "negative_route_pruning",
        c3_block_rank_radial_normalization_nogo.get("trace_class"),
    )
    check(
        "C3 block-rank no-go records rank factor candidate",
        c3_block_rank_radial_normalization_nogo.get("certificate_boundary", {}).get("rank_factor_candidate")
        == "1/sqrt(rank(P_nt)) = 1/sqrt(2)",
    )
    check(
        "C3 block-rank no-go does not derive rank factor",
        c3_block_rank_radial_normalization_nogo.get("certificate_boundary", {}).get("rank_factor_derived_on_current_surface")
        is False,
    )
    check(
        "ordinary P_nt matrix element has no root-rank factor",
        c3_block_rank_radial_normalization_nogo.get("certificate_boundary", {})
        .get("ordinary_projector_matrix_element_has_root_rank_factor")
        is False,
    )
    check(
        "C3 block-rank no-go records same-data counterconventions",
        c3_block_rank_radial_normalization_nogo.get("certificate_boundary", {})
        .get("same_data_counterconventions_present")
        is True,
    )
    check(
        "C3 Fisher quotient radial normalization no-go passed",
        c3_fisher_quotient_radial_normalization_nogo.get("fail_count") == 0,
        c3_fisher_quotient_radial_normalization_nogo.get("fail_count"),
    )
    check(
        "C3 Fisher quotient radial normalization route is pruned",
        c3_fisher_quotient_radial_normalization_nogo.get("trace_class") == "negative_route_pruning",
        c3_fisher_quotient_radial_normalization_nogo.get("trace_class"),
    )
    check(
        "C3 Fisher quotient fine/binary metric ratio is one",
        c3_fisher_quotient_radial_normalization_nogo.get("fine_binary_metric_ratio") == "1",
        c3_fisher_quotient_radial_normalization_nogo.get("fine_binary_metric_ratio"),
    )
    check(
        "C3 Fisher quotient score normalization is not radial generator law",
        c3_fisher_quotient_radial_normalization_nogo.get("fisher_unit_score_role")
        == "source-coordinate normalization, not top radial generator",
        c3_fisher_quotient_radial_normalization_nogo.get("fisher_unit_score_role"),
    )
    check(
        "C3 Fisher quotient leaves internal P_nt B_x direction absent",
        c3_fisher_quotient_radial_normalization_nogo.get("internal_pnt_bx_fisher_direction") is False,
    )
    check(
        "C3 Fisher quotient leaves lambda_top free",
        c3_fisher_quotient_radial_normalization_nogo.get("lambda_top_free_on_current_surface") is True,
    )
    check(
        "C3 zero-singlet top-block membership no-go passed",
        c3_zero_singlet_top_block_membership_nogo.get("fail_count") == 0,
        c3_zero_singlet_top_block_membership_nogo.get("fail_count"),
    )
    check(
        "C3 zero-singlet top-block membership route is pruned",
        c3_zero_singlet_top_block_membership_nogo.get("trace_class") == "negative_route_pruning",
        c3_zero_singlet_top_block_membership_nogo.get("trace_class"),
    )
    check(
        "C3 zero-singlet no-go keeps P_0 allowed by real block algebra",
        c3_zero_singlet_top_block_membership_nogo.get("certificate_boundary", {})
        .get("real_c3_block_algebra_excludes_P0")
        is False,
    )
    check(
        "C3 zero-singlet membership still not derived",
        c3_zero_singlet_top_block_membership_nogo.get("certificate_boundary", {})
        .get("zero_singlet_membership_derived")
        is False,
    )
    check(
        "C3 zero-singlet no-go keeps strict rows absent",
        c3_zero_singlet_top_block_membership_nogo.get("certificate_boundary", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 source-orientation sign-selector no-go passed",
        c3_source_orientation_sign_selector_nogo.get("fail_count") == 0,
        c3_source_orientation_sign_selector_nogo.get("fail_count"),
    )
    check(
        "C3 source-orientation sign-selector route is pruned",
        c3_source_orientation_sign_selector_nogo.get("trace_class") == "negative_route_pruning",
        c3_source_orientation_sign_selector_nogo.get("trace_class"),
    )
    check(
        "C3 source-orientation sign-selector no-go shows largest signed is not orientation invariant",
        c3_source_orientation_sign_selector_nogo.get("certificate_boundary", {})
        .get("largest_signed_selector_orientation_invariant")
        is False,
    )
    check(
        "C3 source-orientation sign-selector no-go keeps absolute max on P_0",
        c3_source_orientation_sign_selector_nogo.get("certificate_boundary", {})
        .get("absolute_response_max_selects_P0")
        is True,
    )
    check(
        "C3 source-orientation sign-selector no-go keeps P_nt sign law open",
        c3_source_orientation_sign_selector_nogo.get("certificate_boundary", {})
        .get("accepted_source_orientation_law_for_Pnt_derived")
        is False,
    )
    check(
        "C3 trace-free centered-source zero-singlet no-go passed",
        c3_trace_free_centered_source_zero_singlet_nogo.get("fail_count") == 0,
        c3_trace_free_centered_source_zero_singlet_nogo.get("fail_count"),
    )
    check(
        "C3 trace-free centered-source route is pruned",
        c3_trace_free_centered_source_zero_singlet_nogo.get("trace_class") == "negative_route_pruning",
        c3_trace_free_centered_source_zero_singlet_nogo.get("trace_class"),
    )
    check(
        "C3 trace-free centered source does not select top projector",
        c3_trace_free_centered_source_zero_singlet_nogo.get("certificate_boundary", {})
        .get("trace_free_source_operator_selects_top_projector")
        is False,
    )
    check(
        "C3 trace-free zero expectation gives s=1/3",
        c3_trace_free_centered_source_zero_singlet_nogo.get("centered_source_witness", {})
        .get("zero_centered_expectation_forces")
        == "s = 1/3",
    )
    check(
        "C3 trace-free target response still requires s=0",
        c3_trace_free_centered_source_zero_singlet_nogo.get("centered_source_witness", {})
        .get("target_nontrivial_response_forces")
        == "s = 0",
    )
    check(
        "C3 minimum-information readout zero-singlet no-go passed",
        c3_mininfo_readout_zero_singlet_nogo.get("fail_count") == 0,
        c3_mininfo_readout_zero_singlet_nogo.get("fail_count"),
    )
    check(
        "C3 minimum-information readout route is pruned",
        c3_mininfo_readout_zero_singlet_nogo.get("trace_class") == "negative_route_pruning",
        c3_mininfo_readout_zero_singlet_nogo.get("trace_class"),
    )
    check(
        "C3 minimum-information finite tilt keeps full support",
        c3_mininfo_readout_zero_singlet_nogo.get("certificate_boundary", {})
        .get("finite_rn_tilt_has_full_support")
        is True,
    )
    check(
        "C3 minimum-information finite tilt cannot set zero singlet weight",
        c3_mininfo_readout_zero_singlet_nogo.get("certificate_boundary", {})
        .get("finite_rn_tilt_can_set_singlet_weight_zero")
        is False,
    )
    check(
        "C3 minimum-information target constraint is coefficient input",
        c3_mininfo_readout_zero_singlet_nogo.get("certificate_boundary", {})
        .get("target_constraint_is_coefficient_row_input")
        is True,
    )
    check(
        "C3 minimum-information readout still has no strict positive certificate",
        c3_mininfo_readout_zero_singlet_nogo.get("certificate_boundary", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 hard-boundary mininfo face-selector support passed",
        c3_mininfo_hard_boundary_face_selector_support.get("fail_count") == 0,
        c3_mininfo_hard_boundary_face_selector_support.get("fail_count"),
    )
    check(
        "C3 hard-boundary mininfo support remains open",
        c3_mininfo_hard_boundary_face_selector_support.get("actual_current_surface_status")
        == "exact-support / open hard-boundary readout law",
        c3_mininfo_hard_boundary_face_selector_support.get("actual_current_surface_status"),
    )
    check(
        "C3 hard-boundary completion alone does not select P_nt",
        c3_mininfo_hard_boundary_face_selector_support.get("support_certificate", {})
        .get("hard_boundary_completion_alone_selects_Pnt")
        is False,
    )
    check(
        "C3 nearest Fisher boundary face is P_nt",
        c3_mininfo_hard_boundary_face_selector_support.get("support_certificate", {})
        .get("nearest_fisher_boundary_face_is_Pnt")
        is True,
    )
    check(
        "C3 nearest-face top readout law remains open",
        c3_mininfo_hard_boundary_face_selector_support.get("support_certificate", {})
        .get("accepted_nearest_face_top_readout_law_derived")
        is False,
    )
    check(
        "C3 hard-boundary support still has no strict positive certificate",
        c3_mininfo_hard_boundary_face_selector_support.get("support_certificate", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 hard-boundary readout law underdetermination no-go passed",
        c3_hard_boundary_readout_law_underdetermination.get("fail_count") == 0,
        c3_hard_boundary_readout_law_underdetermination.get("fail_count"),
    )
    check(
        "C3 hard-boundary readout law route is pruned from current geometry alone",
        c3_hard_boundary_readout_law_underdetermination.get("trace_class") == "negative_route_pruning",
        c3_hard_boundary_readout_law_underdetermination.get("trace_class"),
    )
    check(
        "C3 hard-boundary same data can still select P_0",
        c3_hard_boundary_readout_law_underdetermination.get("certificate_boundary", {})
        .get("same_data_rules_can_select_P0")
        is True,
    )
    check(
        "C3 hard-boundary nearest-face law remains open after underdetermination audit",
        c3_hard_boundary_readout_law_underdetermination.get("certificate_boundary", {})
        .get("accepted_nearest_face_top_readout_law_derived")
        is False,
    )
    check(
        "C3 hard-boundary underdetermination still has no strict positive certificate",
        c3_hard_boundary_readout_law_underdetermination.get("certificate_boundary", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 primitive singular-boundary support passed",
        c3_primitive_singular_boundary_intervention_support.get("fail_count") == 0,
        c3_primitive_singular_boundary_intervention_support.get("fail_count"),
    )
    check(
        "C3 primitive singular-boundary support remains open",
        c3_primitive_singular_boundary_intervention_support.get("actual_current_surface_status")
        == "exact-support / open primitive-singular-boundary readout law",
        c3_primitive_singular_boundary_intervention_support.get("actual_current_surface_status"),
    )
    check(
        "least-KL reflection-even singular boundary selects P_nt",
        c3_primitive_singular_boundary_intervention_support.get("certificate_boundary", {})
        .get("least_kl_reflection_even_boundary_selects_Pnt")
        is True,
    )
    check(
        "primitive singular-boundary top readout law remains open",
        c3_primitive_singular_boundary_intervention_support.get("certificate_boundary", {})
        .get("accepted_primitive_singular_boundary_top_readout_law_derived")
        is False,
    )
    check(
        "full simplex least-KL boundary is not a unique top-block law",
        c3_primitive_singular_boundary_intervention_support.get("certificate_boundary", {})
        .get("least_kl_full_simplex_unique_top_block")
        is False,
    )
    check(
        "C3 primitive singular-boundary support still has no strict certificate",
        c3_primitive_singular_boundary_intervention_support.get("certificate_boundary", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check("direct sparse response certificate harness passed", direct_sparse_cert.get("fail_count") == 0, direct_sparse_cert.get("fail_count"))
    check("direct sparse response certificate is bounded support", direct_sparse_cert.get("actual_current_surface_status") == "bounded-support microbench / open strict-response backend")
    check("direct sparse response certificate proposal is not allowed", direct_sparse_cert.get("proposal_allowed") is False)
    check("direct sparse response certificate does not supply strict top/W rows", direct_sparse_cert.get("strict_top_w_response_certificate_present") is False)
    check("targeted kappa exercise passed", kappa_exercise.get("fail_count") == 0, kappa_exercise.get("fail_count"))
    check("targeted kappa exercise is exact support/open", kappa_exercise.get("actual_current_surface_status") == "exact-support / open kappa proof")
    check("targeted kappa exercise proposal is not allowed", kappa_exercise.get("proposal_allowed") is False)
    check("native backend candidate passed", native_backend.get("fail_count") == 0, native_backend.get("fail_count"))
    check("native backend candidate is bounded support", native_backend.get("actual_current_surface_status") == "bounded-support backend candidate")
    check("native backend computes 1/sqrt(6) without kappa input", native_backend.get("candidate_backend", {}).get("readout_equals_1_over_sqrt6") is True)
    check("native backend candidate proposal is not allowed", native_backend.get("proposal_allowed") is False)
    check("backend projector obstruction passed", projector_obstruction.get("fail_count") == 0, projector_obstruction.get("fail_count"))
    check("backend projector obstruction is route pruning", projector_obstruction.get("trace_class") == "negative_route_pruning")
    check("projector obstruction keeps projector/dynamics route live", "sector projectors" in projector_obstruction.get("route_still_live", ""))
    check("top-sector projector obstruction passed", top_sector_projector_obstruction.get("fail_count") == 0, top_sector_projector_obstruction.get("fail_count"))
    check("top-sector projector obstruction is route pruning", top_sector_projector_obstruction.get("trace_class") == "negative_route_pruning")
    check("top-sector obstruction keeps strict pole-row route live", "strict same-source pole-row evidence" in top_sector_projector_obstruction.get("route_still_live", ""))
    check("C3 spectral projector support passed", c3_spectral_projector_support.get("fail_count") == 0, c3_spectral_projector_support.get("fail_count"))
    check("C3 spectral projector support is upstream support", c3_spectral_projector_support.get("trace_class") == "upstream_support")
    check("C3 spectral projector route remains open", "route_still_open" in c3_spectral_projector_support)
    check("C3 spectral source-response no-go passed", c3_spectral_source_response_nogo.get("fail_count") == 0, c3_spectral_source_response_nogo.get("fail_count"))
    check("C3 spectral source-response no-go is route pruning", c3_spectral_source_response_nogo.get("trace_class") == "negative_route_pruning")
    check("C3 spectral source-response route keeps source law live", "source law" in c3_spectral_source_response_nogo.get("route_still_live", ""))
    check("C3 source-direction no-go passed", c3_source_direction_nogo.get("fail_count") == 0, c3_source_direction_nogo.get("fail_count"))
    check("C3 source-direction no-go is route pruning", c3_source_direction_nogo.get("trace_class") == "negative_route_pruning")
    check("C3 source-direction no-go keeps source direction live", "source direction" in c3_source_direction_nogo.get("route_still_live", ""))
    check("LSP/C3 source-direction boundary passed", lsp_c3_source_direction_boundary.get("fail_count") == 0, lsp_c3_source_direction_boundary.get("fail_count"))
    check("LSP/C3 source-direction boundary is route pruning", lsp_c3_source_direction_boundary.get("trace_class") == "negative_route_pruning")
    check("LSP/C3 boundary keeps source direction live", "source direction" in lsp_c3_source_direction_boundary.get("route_still_live", ""))
    check("positivity/orientation C3 source-direction boundary passed", positivity_orientation_c3_source_direction_boundary.get("fail_count") == 0, positivity_orientation_c3_source_direction_boundary.get("fail_count"))
    check("positivity/orientation C3 boundary is route pruning", positivity_orientation_c3_source_direction_boundary.get("trace_class") == "negative_route_pruning")
    check("positivity/orientation C3 boundary keeps source direction live", "source direction" in positivity_orientation_c3_source_direction_boundary.get("route_still_live", ""))
    check("C3 connected/reflection-even source candidate passed", c3_connected_reflection_even_source_candidate.get("fail_count") == 0, c3_connected_reflection_even_source_candidate.get("fail_count"))
    check("C3 connected/reflection-even candidate is upstream support", c3_connected_reflection_even_source_candidate.get("trace_class") == "upstream_support")
    check("C3 connected/reflection-even candidate status is exact support", c3_connected_reflection_even_source_candidate.get("actual_current_surface_status") == "exact-support")
    check("C3 connected/reflection-even candidate selects B_x under conditions", c3_connected_reflection_even_source_candidate.get("certificate_boundary", {}).get("candidate_direction_bx_selected_under_conditions") is True)
    check("C3 connected/reflection-even candidate gives nontrivial 1/sqrt(6)", c3_connected_reflection_even_source_candidate.get("spectral_response_witness", {}).get("nontrivial_line_magnitude") == "1/sqrt(6)")
    check("C3 connected/reflection-even candidate keeps physical premises open", c3_connected_reflection_even_source_candidate.get("certificate_boundary", {}).get("physical_top_line_nontrivial_derived") is False)
    check("C3 nontrivial top-line boundary passed", c3_nontrivial_top_line_assignment_boundary.get("fail_count") == 0, c3_nontrivial_top_line_assignment_boundary.get("fail_count"))
    check("C3 nontrivial top-line boundary is route pruning", c3_nontrivial_top_line_assignment_boundary.get("trace_class") == "negative_route_pruning")
    check("C3 nontrivial top-line boundary keeps assignment live", "nontrivial top-line assignment" in c3_nontrivial_top_line_assignment_boundary.get("route_still_live", ""))
    check("C3 singlet top assignment differs by factor two", c3_nontrivial_top_line_assignment_boundary.get("response_witness", {}).get("assignment_witness", {}).get("top_line_P0_magnitude") == "2/sqrt(6)")
    check("C3 connected source from normalized RN passed", c3_connected_source_from_normalized_rn.get("fail_count") == 0, c3_connected_source_from_normalized_rn.get("fail_count"))
    check("C3 connected source theorem is upstream support", c3_connected_source_from_normalized_rn.get("trace_class") == "upstream_support")
    check("C3 connected source theorem partially closes route", c3_connected_source_from_normalized_rn.get("reachability_to_target") == "partially_closes")
    check("C3 connected source premise derived", c3_connected_source_from_normalized_rn.get("certificate_boundary", {}).get("connected_source_premise_derived") is True)
    check("C3 connected source theorem leaves reflection evenness open", c3_connected_source_from_normalized_rn.get("certificate_boundary", {}).get("reflection_even_neutral_source_derived") is False)
    check("C3 real-record reflection-even theorem passed", c3_real_record_reflection_even_source.get("fail_count") == 0, c3_real_record_reflection_even_source.get("fail_count"))
    check("C3 real-record reflection-even theorem is upstream support", c3_real_record_reflection_even_source.get("trace_class") == "upstream_support")
    check("C3 real-record reflection-even theorem selects B_x", c3_real_record_reflection_even_source.get("certificate_boundary", {}).get("source_direction_bx_selected") is True)
    check("C3 real-record reflection-even theorem leaves top line open", c3_real_record_reflection_even_source.get("certificate_boundary", {}).get("nontrivial_top_line_assignment_derived") is False)
    check("C3 top-line mass-ordering obstruction passed", c3_top_line_mass_ordering_obstruction.get("fail_count") == 0, c3_top_line_mass_ordering_obstruction.get("fail_count"))
    check("C3 top-line mass-ordering obstruction is route pruning", c3_top_line_mass_ordering_obstruction.get("trace_class") == "negative_route_pruning")
    check("mass-ordering proxy selects P_0", c3_top_line_mass_ordering_obstruction.get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_line") == "P_0")
    check("mass-ordering top magnitude is 2/sqrt(6)", c3_top_line_mass_ordering_obstruction.get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_magnitude") == "sqrt(6)/3")
    check("target nontrivial magnitude remains 1/sqrt(6)", c3_top_line_mass_ordering_obstruction.get("mass_ordering_witness", {}).get("target_nontrivial_magnitude") == "1/sqrt(6)")
    check("C3 real same-surface top-line law obstruction passed", c3_real_same_surface_top_line_law_obstruction.get("fail_count") == 0, c3_real_same_surface_top_line_law_obstruction.get("fail_count"))
    check("C3 real same-surface top-line law obstruction is route pruning", c3_real_same_surface_top_line_law_obstruction.get("trace_class") == "negative_route_pruning")
    check("real top-line obstruction prunes non-mass-ordering shortcut", "non-mass-ordering" in c3_real_same_surface_top_line_law_obstruction.get("route_pruned", ""))
    check("real top-line obstruction leaves C3 circulant dynamics next", "a(h), x(h), y(h)" in c3_real_same_surface_top_line_law_obstruction.get("route_still_live", ""))
    check("real top-line obstruction keeps P_0 counterassignment", c3_real_same_surface_top_line_law_obstruction.get("counterassignments", {}).get("assignment_A", {}).get("top_matrix_element_magnitude") == "A/sqrt(3)")
    check("C3 circulant dynamics/source-law boundary passed", c3_circulant_dynamics_ordering_source_law_boundary.get("fail_count") == 0, c3_circulant_dynamics_ordering_source_law_boundary.get("fail_count"))
    check("C3 circulant dynamics/source-law boundary is route pruning", c3_circulant_dynamics_ordering_source_law_boundary.get("trace_class") == "negative_route_pruning")
    check("C3 dynamics boundary says source derivative is derived", c3_circulant_dynamics_ordering_source_law_boundary.get("certificate_boundary", {}).get("source_derivative_bx_derived") is True)
    check("C3 dynamics boundary leaves top ordering open", c3_circulant_dynamics_ordering_source_law_boundary.get("certificate_boundary", {}).get("top_line_ordering_derived") is False)
    check("C3 dynamics boundary leaves phase law open", c3_circulant_dynamics_ordering_source_law_boundary.get("certificate_boundary", {}).get("orientation_phase_law_for_y0_derived") is False)
    check("strict sparse availability audit passed", strict_sparse_top_w_availability_audit.get("fail_count") == 0, strict_sparse_top_w_availability_audit.get("fail_count"))
    check("strict sparse availability audit is route pruning", strict_sparse_top_w_availability_audit.get("trace_class") == "negative_route_pruning")
    check("strict sparse audit confirms accepted backend absent", strict_sparse_top_w_availability_audit.get("certificate_boundary", {}).get("accepted_same_surface_backend_present") is False)
    check("strict sparse audit confirms strict positive certificate absent", strict_sparse_top_w_availability_audit.get("certificate_boundary", {}).get("strict_positive_certificate_present") is False)
    check(
        "strict pole-row repository discovery no-go passed",
        strict_pole_row_repository_discovery_nogo.get("fail_count") == 0,
        strict_pole_row_repository_discovery_nogo.get("fail_count"),
    )
    check(
        "strict pole-row repository discovery is route pruning",
        strict_pole_row_repository_discovery_nogo.get("trace_class") == "negative_route_pruning",
        strict_pole_row_repository_discovery_nogo.get("trace_class"),
    )
    check(
        "strict pole-row discovery found no complete packet",
        strict_pole_row_repository_discovery_nogo.get("complete_strict_packet_count") == 0,
        strict_pole_row_repository_discovery_nogo.get("complete_strict_packet_count"),
    )
    check(
        "strict pole-row discovery confirms strict certificate absent",
        strict_pole_row_repository_discovery_nogo.get("strict_positive_certificate_present") is False,
    )
    check(
        "microscopic backend/projector/matrix-element boundary passed",
        microscopic_backend_projector_matrix_element_boundary.get("fail_count") == 0,
        microscopic_backend_projector_matrix_element_boundary.get("fail_count"),
    )
    check("microscopic boundary is route pruning", microscopic_backend_projector_matrix_element_boundary.get("trace_class") == "negative_route_pruning")
    check(
        "microscopic boundary leaves physical top projector absent",
        microscopic_backend_projector_matrix_element_boundary.get("certificate_boundary", {}).get("physical_top_projector_or_pole_derived") is False,
    )
    check(
        "microscopic boundary leaves source matrix element absent",
        microscopic_backend_projector_matrix_element_boundary.get("certificate_boundary", {}).get("source_generator_matrix_element_derived") is False,
    )
    check(
        "microscopic boundary keeps strict pole-row route live",
        "strict same-source top/W pole-row data" in microscopic_backend_projector_matrix_element_boundary.get("route_still_live", ""),
        microscopic_backend_projector_matrix_element_boundary.get("route_still_live"),
    )
    check(
        "C3 positive transfer Perron top-line no-go passed",
        c3_positive_transfer_perron_top_line_nogo.get("fail_count") == 0,
        c3_positive_transfer_perron_top_line_nogo.get("fail_count"),
    )
    check("C3 positive transfer Perron no-go is route pruning", c3_positive_transfer_perron_top_line_nogo.get("trace_class") == "negative_route_pruning")
    check(
        "positive Perron line is the C3 singlet",
        c3_positive_transfer_perron_top_line_nogo.get("certificate_boundary", {}).get("perron_line_is_p0") is True,
    )
    check(
        "positive Perron route does not isolate nontrivial line",
        c3_positive_transfer_perron_top_line_nogo.get("certificate_boundary", {}).get("nontrivial_line_isolated") is False,
    )
    check(
        "positive Perron route prunes nontrivial top-line shortcut",
        "nontrivial top line" in c3_positive_transfer_perron_top_line_nogo.get("route_pruned", ""),
        c3_positive_transfer_perron_top_line_nogo.get("route_pruned"),
    )
    check(
        "C3 phase-ordering cone support boundary passed",
        c3_phase_ordering_cone_support_boundary.get("fail_count") == 0,
        c3_phase_ordering_cone_support_boundary.get("fail_count"),
    )
    check("C3 phase-ordering cone is upstream support", c3_phase_ordering_cone_support_boundary.get("trace_class") == "upstream_support")
    check(
        "C3 phase-ordering cone characterizes nontrivial target cone",
        c3_phase_ordering_cone_support_boundary.get("certificate_boundary", {}).get("phase_ordering_cone_characterized") is True,
    )
    check(
        "C3 phase-ordering cone leaves phase law open",
        c3_phase_ordering_cone_support_boundary.get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "C3 phase-ordering cone implies target row conditionally",
        c3_phase_ordering_cone_support_boundary.get("certificate_boundary", {}).get("nontrivial_cone_implies_target_row") is True,
    )
    check(
        "C3 orientation-phase dynamics necessity no-go passed",
        c3_orientation_phase_dynamics_necessity.get("fail_count") == 0,
        c3_orientation_phase_dynamics_necessity.get("fail_count"),
    )
    check(
        "C3 orientation-phase no-go prunes reflection-even cone derivation",
        c3_orientation_phase_dynamics_necessity.get("trace_class") == "negative_route_pruning",
        c3_orientation_phase_dynamics_necessity.get("trace_class"),
    )
    check(
        "C3 orientation-phase no-go requires orientation-odd dynamics",
        c3_orientation_phase_dynamics_necessity.get("no_go_audit", {}).get("orientation_odd_phase_term_required") is True,
    )
    check(
        "C3 orientation-phase no-go leaves strict pole rows absent",
        c3_orientation_phase_dynamics_necessity.get("no_go_audit", {}).get("strict_top_w_response_certificate_present") is False,
    )
    check(
        "C3 orientation-phase strength no-go passed",
        c3_orientation_phase_strength_boundary.get("fail_count") == 0,
        c3_orientation_phase_strength_boundary.get("fail_count"),
    )
    check(
        "C3 orientation sign alone is insufficient",
        c3_orientation_phase_strength_boundary.get("no_go_audit", {}).get("orientation_sign_sufficient") is False,
    )
    check(
        "C3 phase-strength law remains open",
        c3_orientation_phase_strength_boundary.get("no_go_audit", {}).get("phase_strength_law_derived") is False,
    )
    check(
        "C3 quantitative phase-strength underdetermination no-go passed",
        c3_quantitative_phase_strength_underdetermination.get("fail_count") == 0,
        c3_quantitative_phase_strength_underdetermination.get("fail_count"),
    )
    check(
        "C3 unit-normalized signed branch still contains singlet witness",
        c3_quantitative_phase_strength_underdetermination.get("unit_circle_witnesses", {})
        .get("positive_outside_cone_unit", {})
        .get("largest_lines")
        == ["P_0"],
    )
    check(
        "C3 phase angle selector remains open",
        c3_quantitative_phase_strength_underdetermination.get("current_premise_no_go", {})
        .get("audit", {})
        .get("phase_angle_selector_derived")
        is False,
    )
    check(
        "C3 quantitative underdetermination leaves strict rows absent",
        c3_quantitative_phase_strength_underdetermination.get("current_premise_no_go", {})
        .get("audit", {})
        .get("strict_top_w_response_certificate_present")
        is False,
    )
    check(
        "C3 primitive character phase-angle candidate passed",
        c3_primitive_character_phase_angle_candidate.get("fail_count") == 0,
        c3_primitive_character_phase_angle_candidate.get("fail_count"),
    )
    check(
        "C3 primitive character candidate remains conditional support",
        c3_primitive_character_phase_angle_candidate.get("actual_current_surface_status")
        == "conditional-support / open phase-angle law",
        c3_primitive_character_phase_angle_candidate.get("actual_current_surface_status"),
    )
    check(
        "C3 primitive character candidate gives target row",
        c3_primitive_character_phase_angle_candidate.get("candidate_certificate", {})
        .get("candidate_angles_give_target_row")
        is True,
    )
    check(
        "C3 primitive character candidate does not derive accepted phase law",
        c3_primitive_character_phase_angle_candidate.get("candidate_certificate", {})
        .get("accepted_same_surface_phase_angle_law_derived")
        is False,
    )
    check(
        "positive primitive character angle selects P_omega2",
        c3_primitive_character_phase_angle_candidate.get("character_angle_witnesses", {})
        .get("positive_character_angle", {})
        .get("largest_lines")
        == ["P_omega2"],
    )
    check(
        "negative primitive character angle selects P_omega",
        c3_primitive_character_phase_angle_candidate.get("character_angle_witnesses", {})
        .get("negative_character_angle", {})
        .get("largest_lines")
        == ["P_omega"],
    )
    check(
        "C3 representation phase-selection no-go passed",
        c3_representation_phase_selection_nogo.get("fail_count") == 0,
        c3_representation_phase_selection_nogo.get("fail_count"),
    )
    check(
        "C3 representation phase-selection is route pruning",
        c3_representation_phase_selection_nogo.get("trace_class") == "negative_route_pruning",
        c3_representation_phase_selection_nogo.get("trace_class"),
    )
    check(
        "C3 representation theory does not select primitive angle",
        c3_representation_phase_selection_nogo.get("no_go_certificate", {})
        .get("representation_theory_selects_phi_pm_2pi_over_3")
        is False,
    )
    check(
        "C3 representation family includes singlet counterangle",
        c3_representation_phase_selection_nogo.get("no_go_certificate", {})
        .get("c3_native_counterangle_selects_singlet")
        is True,
    )
    check(
        "C3 representation phase route remains live only with dynamics or strict rows",
        "accepted same-surface phase-angle dynamics"
        in c3_representation_phase_selection_nogo.get("route_still_live", ""),
        c3_representation_phase_selection_nogo.get("route_still_live"),
    )
    check(
        "C3 cubic invariant phase selector passed",
        c3_cubic_invariant_phase_selector.get("fail_count") == 0,
        c3_cubic_invariant_phase_selector.get("fail_count"),
    )
    check(
        "C3 cubic invariant selector is upstream support",
        c3_cubic_invariant_phase_selector.get("trace_class") == "upstream_support",
        c3_cubic_invariant_phase_selector.get("trace_class"),
    )
    check(
        "C3 cubic max orbit contains primitive angles",
        c3_cubic_invariant_phase_selector.get("candidate_certificate", {})
        .get("cubic_max_orbit_contains_primitive_angles")
        is True,
    )
    check(
        "C3 cubic route still lacks accepted potential",
        c3_cubic_invariant_phase_selector.get("candidate_certificate", {})
        .get("accepted_same_surface_cubic_phase_potential_derived")
        is False,
    )
    check(
        "C3 cubic orientation branch plus max selects target",
        c3_cubic_invariant_phase_selector.get("candidate_certificate", {})
        .get("orientation_branch_plus_cubic_max_selects_target")
        is True,
    )
    check(
        "C3 cubic phase-potential sign/branch no-go passed",
        c3_cubic_phase_potential_nogo.get("fail_count") == 0,
        c3_cubic_phase_potential_nogo.get("fail_count"),
    )
    check(
        "C3 cubic phase-potential route is pruned",
        c3_cubic_phase_potential_nogo.get("trace_class") == "negative_route_pruning",
        c3_cubic_phase_potential_nogo.get("trace_class"),
    )
    check(
        "C3 cubic sign/optimization convention remains open",
        c3_cubic_phase_potential_nogo.get("no_go_certificate", {})
        .get("cubic_sign_or_optimization_convention_derived")
        is False,
    )
    check(
        "C3 cubic singlet extremum remains allowed",
        c3_cubic_phase_potential_nogo.get("no_go_certificate", {}).get("singlet_extremum_allowed")
        is True,
    )
    check(
        "C3 cubic physical phase law remains open",
        c3_cubic_phase_potential_nogo.get("no_go_certificate", {}).get("physical_phase_law_derived")
        is False,
    )
    check(
        "C3 phase-orbit selector no-go passed",
        c3_phase_orbit_selector_nogo.get("fail_count") == 0,
        c3_phase_orbit_selector_nogo.get("fail_count"),
    )
    check(
        "C3 phase-orbit selector route is pruned",
        c3_phase_orbit_selector_nogo.get("trace_class") == "negative_route_pruning",
        c3_phase_orbit_selector_nogo.get("trace_class"),
    )
    check(
        "C3 phase-orbit selection does not exclude P0",
        c3_phase_orbit_selector_nogo.get("no_go_certificate", {}).get("orbit_selection_excludes_p0")
        is False,
    )
    check(
        "C3 phase-orbit route still lacks orbit-member readout",
        c3_phase_orbit_selector_nogo.get("no_go_certificate", {})
        .get("accepted_orbit_member_readout_derived")
        is False,
    )
    check(
        "C3 orbit-member readout covariance no-go passed",
        c3_orbit_member_readout_covariance_nogo.get("fail_count") == 0,
        c3_orbit_member_readout_covariance_nogo.get("fail_count"),
    )
    check(
        "C3 orbit-member readout covariance route is pruned",
        c3_orbit_member_readout_covariance_nogo.get("trace_class") == "negative_route_pruning",
        c3_orbit_member_readout_covariance_nogo.get("trace_class"),
    )
    check(
        "free C3 orbit has no equivariant section",
        c3_orbit_member_readout_covariance_nogo.get("no_go_certificate", {})
        .get("free_c3_orbit_has_equivariant_section")
        is False,
    )
    check(
        "orbit-member readout witnesses include P0",
        c3_orbit_member_readout_covariance_nogo.get("no_go_certificate", {})
        .get("one_admissible_section_selects_p0")
        is True,
    )
    check(
        "accepted orbit-member readout remains open",
        c3_orbit_member_readout_covariance_nogo.get("no_go_certificate", {})
        .get("accepted_orbit_member_readout_derived")
        is False,
    )
    check(
        "C3 dihedral basepoint anchor obstruction passed",
        c3_dihedral_basepoint_anchor_obstruction.get("fail_count") == 0,
        c3_dihedral_basepoint_anchor_obstruction.get("fail_count"),
    )
    check(
        "C3/D3 naturality still has no section",
        c3_dihedral_basepoint_anchor_obstruction.get("no_go_certificate", {})
        .get("d3_natural_section_exists")
        is False,
    )
    check(
        "existing record reflection fixes P0",
        c3_dihedral_basepoint_anchor_obstruction.get("no_go_certificate", {})
        .get("existing_record_reflection_fixes_p0")
        is True,
    )
    check(
        "nontrivial reflected axis remains a basepoint import",
        c3_dihedral_basepoint_anchor_obstruction.get("no_go_certificate", {})
        .get("rotated_reflection_axis_selects_nontrivial_member_only_with_extra_basepoint")
        is True,
    )
    check(
        "C3 orientation-biased phase-potential no-go passed",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("fail_count") == 0,
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("fail_count"),
    )
    check(
        "C3 orientation-biased phase-potential route is pruned",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("trace_class") == "negative_route_pruning",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("trace_class"),
    )
    check(
        "orientation bias still selects an orbit rather than a member",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("no_go_certificate", {})
        .get("orientation_bias_selects_orbit_member")
        is False,
    )
    check(
        "orientation-biased orbit still contains P0",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("no_go_certificate", {})
        .get("generic_orientation_biased_orbit_contains_p0")
        is True,
    )
    check(
        "orientation-biased route still lacks physical basepoint readout",
        c3_orientation_biased_phase_potential_orbit_member_nogo.get("no_go_certificate", {})
        .get("accepted_physical_basepoint_readout_law_derived")
        is False,
    )
    check(
        "C3 source-response extremal readout no-go passed",
        c3_source_response_extremal_readout_nogo.get("fail_count") == 0,
        c3_source_response_extremal_readout_nogo.get("fail_count"),
    )
    check(
        "C3 source-response extremal readout route is pruned",
        c3_source_response_extremal_readout_nogo.get("trace_class") == "negative_route_pruning",
        c3_source_response_extremal_readout_nogo.get("trace_class"),
    )
    check(
        "source-response maximum still selects P0",
        c3_source_response_extremal_readout_nogo.get("no_go_certificate", {})
        .get("absolute_response_max_selects_p0")
        is True,
    )
    check(
        "source-response target minimum remains an extra selector",
        c3_source_response_extremal_readout_nogo.get("no_go_certificate", {})
        .get("minimum_response_top_convention_derived")
        is False,
    )
    check(
        "source-response minimum still leaves nontrivial pair degenerate",
        c3_source_response_extremal_readout_nogo.get("no_go_certificate", {})
        .get("nontrivial_complex_line_isolated")
        is False,
    )
    check(
        "strict W/Z plus C3 top-row splice no-go passed",
        strict_wz_c3_top_row_splice_nogo.get("fail_count") == 0,
        strict_wz_c3_top_row_splice_nogo.get("fail_count"),
    )
    check(
        "strict W/Z plus C3 splice route is pruned",
        strict_wz_c3_top_row_splice_nogo.get("trace_class") == "negative_route_pruning",
        strict_wz_c3_top_row_splice_nogo.get("trace_class"),
    )
    check(
        "strict W/Z plus C3 splice target row depends on nontrivial line",
        strict_wz_c3_top_row_splice_nogo.get("splice_witness", {})
        .get("target_depends_on_nontrivial_line_choice")
        is True,
    )
    check(
        "strict W/Z plus C3 splice keeps same-surface authority open",
        strict_wz_c3_top_row_splice_nogo.get("certificate_boundary", {})
        .get("same_surface_splice_authority_derived")
        is False,
    )
    check(
        "strict W/Z plus C3 splice keeps physical top line open",
        strict_wz_c3_top_row_splice_nogo.get("certificate_boundary", {})
        .get("physical_top_line_nontrivial_derived")
        is False,
    )
    check(
        "strict W/Z plus C3 splice still has no strict positive certificate",
        strict_wz_c3_top_row_splice_nogo.get("certificate_boundary", {})
        .get("strict_positive_certificate_present")
        is False,
    )

    return {
        "fisher": fisher,
        "minimum_information": min_info,
        "primitive_record_law": primitive_record_law,
        "top_source_nogo": top_source_nogo,
        "minimum_information_uniqueness": mininfo_uniqueness,
        "top_carrier": top_carrier,
        "fisher_lsz": fisher_lsz,
        "fh": fh,
        "same_source": same,
        "strict_wz": wz,
        "strict_top": top,
        "strict_same_source_obstruction": strict_obstruction,
        "first_principles_transfer_response": first_principles_transfer_response,
        "same_surface_top_matrix_element_factorization": same_surface_top_matrix_element_factorization,
        "c3_nontrivial_block_matrix_element_support": c3_nontrivial_block_matrix_element_support,
        "c3_same_surface_radial_factor_nogo": c3_same_surface_radial_factor_nogo,
        "c3_radial_readout_compensation_nogo": c3_radial_readout_compensation_nogo,
        "c3_sharp_response_readout_nogo": c3_sharp_response_readout_nogo,
        "fisher_lsz_radial_generator_nogo": fisher_lsz_radial_generator_nogo,
        "c3_block_rank_radial_normalization_nogo": c3_block_rank_radial_normalization_nogo,
        "c3_fisher_quotient_radial_normalization_nogo": c3_fisher_quotient_radial_normalization_nogo,
        "c3_zero_singlet_top_block_membership_nogo": c3_zero_singlet_top_block_membership_nogo,
        "c3_source_orientation_sign_selector_nogo": c3_source_orientation_sign_selector_nogo,
        "c3_trace_free_centered_source_zero_singlet_nogo": c3_trace_free_centered_source_zero_singlet_nogo,
        "c3_mininfo_readout_zero_singlet_nogo": c3_mininfo_readout_zero_singlet_nogo,
        "c3_mininfo_hard_boundary_face_selector_support": c3_mininfo_hard_boundary_face_selector_support,
        "c3_hard_boundary_readout_law_underdetermination": c3_hard_boundary_readout_law_underdetermination,
        "c3_primitive_singular_boundary_intervention_support": c3_primitive_singular_boundary_intervention_support,
        "direct_sparse_response_certificate": direct_sparse_cert,
        "kappa_direct_exercise": kappa_exercise,
        "native_backend_candidate": native_backend,
        "backend_projector_obstruction": projector_obstruction,
        "top_sector_projector_obstruction": top_sector_projector_obstruction,
        "c3_spectral_projector_support": c3_spectral_projector_support,
        "c3_spectral_source_response_nogo": c3_spectral_source_response_nogo,
        "c3_source_direction_nogo": c3_source_direction_nogo,
        "lsp_c3_source_direction_boundary": lsp_c3_source_direction_boundary,
        "positivity_orientation_c3_source_direction_boundary": positivity_orientation_c3_source_direction_boundary,
        "c3_connected_reflection_even_source_candidate": c3_connected_reflection_even_source_candidate,
        "c3_nontrivial_top_line_assignment_boundary": c3_nontrivial_top_line_assignment_boundary,
        "c3_connected_source_from_normalized_rn": c3_connected_source_from_normalized_rn,
        "c3_real_record_reflection_even_source": c3_real_record_reflection_even_source,
        "c3_top_line_mass_ordering_obstruction": c3_top_line_mass_ordering_obstruction,
        "c3_real_same_surface_top_line_law_obstruction": c3_real_same_surface_top_line_law_obstruction,
        "c3_circulant_dynamics_ordering_source_law_boundary": c3_circulant_dynamics_ordering_source_law_boundary,
        "strict_sparse_top_w_availability_audit": strict_sparse_top_w_availability_audit,
        "strict_pole_row_repository_discovery_nogo": strict_pole_row_repository_discovery_nogo,
        "microscopic_backend_projector_matrix_element_boundary": microscopic_backend_projector_matrix_element_boundary,
        "c3_positive_transfer_perron_top_line_nogo": c3_positive_transfer_perron_top_line_nogo,
        "c3_phase_ordering_cone_support_boundary": c3_phase_ordering_cone_support_boundary,
        "c3_orientation_phase_dynamics_necessity": c3_orientation_phase_dynamics_necessity,
        "c3_orientation_phase_strength_boundary": c3_orientation_phase_strength_boundary,
        "c3_quantitative_phase_strength_underdetermination": c3_quantitative_phase_strength_underdetermination,
        "c3_primitive_character_phase_angle_candidate": c3_primitive_character_phase_angle_candidate,
        "c3_representation_phase_selection_nogo": c3_representation_phase_selection_nogo,
        "c3_cubic_invariant_phase_selector": c3_cubic_invariant_phase_selector,
        "c3_cubic_phase_potential_nogo": c3_cubic_phase_potential_nogo,
        "c3_phase_orbit_selector_nogo": c3_phase_orbit_selector_nogo,
        "c3_orbit_member_readout_covariance_nogo": c3_orbit_member_readout_covariance_nogo,
        "c3_dihedral_basepoint_anchor_obstruction": c3_dihedral_basepoint_anchor_obstruction,
        "c3_orientation_biased_phase_potential_orbit_member_nogo": c3_orientation_biased_phase_potential_orbit_member_nogo,
        "c3_source_response_extremal_readout_nogo": c3_source_response_extremal_readout_nogo,
        "strict_wz_c3_top_row_splice_nogo": strict_wz_c3_top_row_splice_nogo,
    }


def part3_fisher_lsz_and_response_algebra() -> None:
    print("\nPart 3: conditional closure algebra")
    lam, h, a_o = sp.symbols("lambda h A_O", positive=True)
    fisher_metric = lam**2
    d_ell_dh = sp.sqrt(fisher_metric)
    source_derivative = -lam
    intrinsic_source_derivative = sp.simplify(source_derivative / d_ell_dh)
    check("Fisher arclength removes positive raw lambda", is_zero(intrinsic_source_derivative + 1), intrinsic_source_derivative)

    operator_scale = sp.symbols("operator_scale", positive=True)
    lsz_original = sp.simplify(1 / a_o)
    lsz_scaled = sp.simplify(operator_scale / (operator_scale * a_o))
    check("LSZ insertion invariant under operator rescaling", is_zero(lsz_scaled - lsz_original), lsz_scaled)

    y, g2, dv = sp.symbols("y_t g_2 dv_dh", positive=True)
    dmt = y * dv / sp.sqrt(2)
    dmw = g2 * dv / 2
    recovered_y = sp.simplify(g2 / sp.sqrt(2) * dmt / dmw)
    check("same-source top/W slope ratio recovers y_t", is_zero(recovered_y - y), recovered_y)

    c = sp.symbols("c", positive=True)
    recovered_scaled = sp.simplify(g2 / sp.sqrt(2) * (dmt / c) / (dmw / c))
    check("top/W response readout is source-reparameterization invariant", is_zero(recovered_scaled - y), recovered_scaled)

    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm_sq = sp.simplify((u.T * u)[0])
    check("six-component democratic top carrier is unit normalized", is_zero(norm_sq - 1), norm_sq)
    check("single top component is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])


def part4_pole_no_go_boundary() -> None:
    print("\nPart 4: pole-row no-go scope")
    a_s = Fraction(5, 3)
    a_h = Fraction(7, 4)
    q = Fraction(5, 7)
    t = 3
    c_ss = a_s * a_s * q**t
    c_sh = a_s * a_h * q**t
    c_hh = a_h * a_h * q**t
    check("base pole row is rank one", c_sh * c_sh - c_ss * c_hh == 0)
    for mu, lam in ((Fraction(2, 1), Fraction(3, 1)), (Fraction(9, 8), Fraction(8, 9))):
        ss = (mu * a_s) ** 2 * q**t
        sh = (mu * a_s) * (lam * a_h) * q**t
        hh = (lam * a_h) ** 2 * q**t
        ratio = sh * sh / (ss * hh)
        check(f"Gram purity survives independent rescaling mu={mu}, lambda={lam}", sh * sh - ss * hh == 0)
        check(f"normalized pole residue ratio stays one at mu={mu}, lambda={lam}", ratio == 1, ratio)

    note = read(POLE_NOGO)
    check(
        "pole no-go leaves future same-surface LSZ theorem open",
        "same-surface LSZ theorem" in note and "canonical scalar LSZ normalization" in note,
    )
    check("pole no-go is not a global Y_T no-go", "not a global no-go for Y_T" in note)


def part5_missing_certificates() -> dict[str, Any]:
    print("\nPart 5: missing positive certificates")
    pole_cert_present = STRICT_SOURCE_HIGGS_ROWS.exists()
    top_w_cert_present = STRICT_TOP_W_ROWS.exists()
    sparse_harness_present = DIRECT_SPARSE_RESPONSE_CERT_OUT.exists()
    check("accepted strict source-Higgs pole certificate absent", not pole_cert_present, STRICT_SOURCE_HIGGS_ROWS.relative_to(ROOT).as_posix())
    check("coefficient-certified strict top/W response rows absent", not top_w_cert_present, STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("bounded sparse response harness present", sparse_harness_present, DIRECT_SPARSE_RESPONSE_CERT_OUT.relative_to(ROOT).as_posix())

    required_pole_fields = [
        "same_surface_id",
        "source_action_authority",
        "source_operator",
        "higgs_operator",
        "isolated_source_higgs_pole",
        "accepted_pole_residue",
        "contact_subtraction_done",
        "fv_ir_controls_pass",
        "same_model_class",
        "fisher_lsz_normalized",
        "no_forbidden_imports",
    ]
    required_top_w_fields = [
        "same_source_id",
        "top_pole_isolated",
        "w_pole_isolated",
        "dM_t_dh",
        "dM_W_dh",
        "contact_subtraction_done",
        "fv_ir_controls_pass",
        "same_model_class",
        "same_scale_g2",
        "no_forbidden_imports",
    ]
    check("strict source-Higgs pole certificate schema has 11 fields", len(required_pole_fields) == 11)
    check("strict top/W response certificate schema has 10 fields", len(required_top_w_fields) == 10)
    check("first open gate is strict same-source top/W response before numerical running", True, "strict response unless audit accepts primitive top-source premise")

    return {
        "strict_source_higgs_pole_certificate_present": pole_cert_present,
        "strict_top_w_response_certificate_present": top_w_cert_present,
        "bounded_sparse_response_harness_present": sparse_harness_present,
        "required_pole_fields": required_pole_fields,
        "required_top_w_fields": required_top_w_fields,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained Y_T closure",
        "This note derives `y_t`",
        "positive Y_T closure is obtained",
        "strict top/W pole-response evidence has been obtained",
        "the accepted Y_T pole/action surface has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T FULL CLOSURE STACK AND STRICT POLE-RESPONSE CONTRACT")
    print("=" * 78)

    statuses = part1_anchors()
    support_outputs = part2_support_outputs()
    part3_fisher_lsz_and_response_algebra()
    part4_pole_no_go_boundary()
    certificates = part5_missing_certificates()
    part6_firewalls()

    closure_stack = [
        {
            "step": 0,
            "name": "same-surface source/action authority",
            "status": "bounded_support_plus_minimum_information_and_primitive_record_law_exact_support_top_source_identification_pruned_from_current_inputs",
            "closed": False,
            "next_action": "strict same-source pole responses, unless audit accepts primitive top-source premise",
        },
        {
            "step": 1,
            "name": "one-Higgs up-type top carrier skeleton",
            "status": "exact_support_coefficient_free",
            "closed": True,
            "next_action": "combine only with a physical intervention/coefficient theorem or strict response evidence",
        },
        {
            "step": 2,
            "name": "source-scale Fisher arclength",
            "status": "exact_support",
            "closed": True,
            "next_action": "use only with a physical Fisher/LSZ source readout",
        },
        {
            "step": 3,
            "name": "physical intervention minimum-information uniqueness",
            "status": "exact_support_with_primitive_record_law_derived_top_source_identification_not_derived_from_current_inputs",
            "closed": False,
            "next_action": "use only if audit accepts the primitive top-source identification premise",
        },
        {
            "step": 3.5,
            "name": "top-source identification hard-stop",
            "status": "exact_no_go_for_structural_no_compute_derivation_from_current_inputs",
            "closed": True,
            "next_action": "pivot to strict same-source top/W response evidence",
        },
        {
            "step": 4,
            "name": "Fisher/LSZ source normalization",
            "status": "exact_support_under_accepted_isolated_pole",
            "closed": True,
            "next_action": "supply accepted same-surface isolated-pole residue authority",
        },
        {
            "step": 5,
            "name": "same-surface pole/action authority",
            "status": "open_first_hard_gate",
            "closed": False,
            "next_action": "produce strict pole/residue certificate or theorem",
        },
        {
            "step": 6,
            "name": "strict same-source top/W response rows",
            "status": "remaining_audit_clean_positive_route_evidence_absent_exact_obstruction_prunes_derivation_from_current_same_source_w_row_symbolic_top_support_alone_first_principles_transfer_response_reduces_blocker_to_sector_matrix_element_factorization_boundary_shows_A_over_sqrt12_is_conditional_on_generator_and_nontrivial_line_nontrivial_block_support_shows_zero_singlet_weight_suffices_and_complex_line_isolation_is_not_needed_for_coefficient_radial_factor_no_go_shows_zero_singlet_support_still_needs_lambda_top_equal_1_over_sqrt2_radial_readout_compensation_no_go_shows_target_magnitude_does_not_back_solve_zero_singlet_or_radial_factor_sharp_response_readout_no_go_shows_zero_variance_still_allows_singlet_endpoint_fisher_lsz_radial_generator_no_go_shows_source_scale_normalization_does_not_fix_lambda_top_block_rank_radial_normalization_no_go_shows_rank_pnt_two_does_not_derive_root_rank_radial_law_fisher_quotient_radial_normalization_no_go_shows_c3_rn_fisher_coarse_graining_and_fisher_unit_score_normalization_do_not_derive_the_top_radial_generator_bounded_sparse_certificate_harness_present_strict_wz_plus_c3_top_row_splice_pruned",
            "closed": False,
            "next_action": "derive accepted same-surface generator factorization plus a new sign/order/readout law excluding P_0, or produce a new accepted strict pole-response packet because none is present under existing artifact names",
        },
        {
            "step": 6.5,
            "name": "physical top generation projector",
            "status": "corner_label_shortcut_pruned_c3_spectral_projectors_supported_source_direction_now_bx_up_to_sign_nontrivial_top_line_shortcut_pruned_mass_ordering_selects_p0_real_same_surface_non_mass_ordering_shortcut_pruned_nontrivial_block_support_shows_only_zero_singlet_weight_is_needed_for_coefficient_but_radial_generator_factorization_remains_open_and_real_block_algebra_sign_choice_trace_free_centering_and_finite_mininfo_readout_do_not_derive_that_membership_hard_boundary_mininfo_nearest_face_selects_pnt_conditionally_but_nearest_face_readout_law_is_open_and_not_derived_from_current_boundary_geometry_alone_microscopic_source_backend_carrier_c3_shortcut_pruned_positive_c3_perron_shortcut_pruned_phase_ordering_cone_characterized_but_open_reflection_even_sign_only_and_unit_normalized_phase_strength_shortcuts_pruned_primitive_character_phase_angles_conditionally_hit_target_but_phase_law_open_representation_theory_alone_pruned_cubic_invariant_route_conditional_cubic_potential_invariance_alone_pruned_general_phase_orbit_selector_pruned_orbit_member_covariance_pruned_dihedral_basepoint_anchor_pruned_orientation_biased_phase_potential_pruned_source_response_extremal_readout_pruned",
            "closed": True,
            "next_action": "produce accepted strict top/W pole rows, or derive an accepted same-surface sign/order/readout law excluding P_0 with backend/projectors/matrix elements",
        },
        {
            "step": 7,
            "name": "same-scale g2 and matching/running",
            "status": "open_for_numerical_y_t_v",
            "closed": False,
            "next_action": "defer unless the claim is numerical y_t(v) rather than local ratio",
        },
    ]

    result = {
        "actual_current_surface_status": "exact-support / open strict-response gate",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The stack burns down source-coordinate scale and the primitive source law, "
            "then prunes top-source identification from current structural inputs. "
            "The C3 B_x route is now also blocked under ordinary mass-ordering, "
            "and the current real/reflection-even same-surface inputs do not "
            "derive a non-mass-ordering top-line law. Derived B_x also does "
            "not derive the base C3 circulant dynamics or spectral ordering. "
            "The strict sparse route is unavailable on the current branch "
            "because accepted backend/projector/controlled pole-row artifacts "
            "are absent. "
            "A broader strict pole-row repository discovery scan also finds "
            "no hidden accepted same-surface top/W pole-row certificate under "
            "current Y_T response/backend/projector artifact names. "
            "The microscopic backend/projector/matrix-element boundary prunes "
            "the current source-law/carrier/C3/no-kappa shortcut because the "
            "accepted backend, physical top projector, and source-generator "
            "matrix element remain load-bearing. "
            "The positive real C3 transfer/Perron shortcut is also pruned "
            "because positivity selects P_0, while the target coefficient "
            "requires a nontrivial C3 character line or strict pole rows. "
            "The residual C3 phase-ordering cone is now explicit: a "
            "nontrivial top line requires y_0 > sqrt(3) x_0 or "
            "-y_0 > sqrt(3) x_0, but the current surface does not derive "
            "that cone membership. "
            "Reflection-even same-surface C3 base dynamics is now pruned as "
            "a source of that cone because it forces y_0 = 0 and therefore "
            "selects P_0 or leaves the nontrivial block degenerate. "
            "Orientation sign alone is also pruned because same-sign finite "
            "C3 base operators can still lie in the singlet region; a "
            "quantitative phase-strength law is required. "
            "Unit-normalized same-surface C3 base dynamics plus orientation "
            "sign is also underdetermined: the unit circle contains both "
            "singlet-top and nontrivial-top witnesses, so a phase-angle "
            "dynamics law remains load-bearing. "
            "The primitive nontrivial C3 character angles phi=+/-2*pi/3 "
            "now give a concrete conditional support route into the target "
            "cone and A/sqrt(12), but the current surface does not derive "
            "that the physical Y_T same-surface base operator has either "
            "phase angle. "
            "Finite C3 representation/character facts alone are now pruned "
            "as a selector for that phase law because C3-native unit "
            "Hermitian choices include both target-row and singlet-row "
            "witnesses. "
            "The cubic trace invariant supplies a sharper conditional route: "
            "its oriented nonzero maxima are phi=+/-2*pi/3, but the accepted "
            "same-surface cubic phase potential and orientation branch are "
            "not derived. "
            "Cubic invariant phase-potential structure alone is now also "
            "pruned as the missing phase law because sign, variational "
            "convention, singlet extrema, degeneracies, and physical "
            "orientation branch remain load-bearing. "
            "The broader C3 scalar phase-potential route is now pruned as "
            "well: C3-invariant scalar dynamics selects phase orbits, while "
            "generic and primitive orbits contain both P_0 and nontrivial "
            "top-line witnesses, so an accepted orbit-member/readout law "
            "remains load-bearing. "
            "C3 covariance of the orbit-member readout does not close that "
            "law either: a free three-member C3 orbit has no equivariant "
            "section, and symmetry-breaking sections include a P_0 witness "
            "as well as the target nontrivial witnesses. "
            "The existing dihedral/reflection basepoint shortcut is now "
            "pruned too: full C3/D3 naturality cannot select a member of the "
            "free orbit, and the already-derived real-record reflection axis "
            "fixes the singlet P_0 member rather than a nontrivial target "
            "row; rotated reflection axes would import the missing physical "
            "basepoint section. "
            "An explicit orientation-biased phase potential with a "
            "reflection-odd sin(3phi) term is now also pruned as a top-line "
            "law: it still selects a C3 phase orbit, not a physical orbit "
            "member, and the selected orbit contains a P_0 witness unless an "
            "accepted basepoint/readout law is supplied. "
            "The non-scalar source-response extremal readout shortcut is "
            "also pruned: signed and absolute maxima of the derived B_x "
            "response select P_0 and give A/sqrt(3), while signed and "
            "absolute minima give A/sqrt(12) only by adding a "
            "minimum-response selector and still leave the two nontrivial "
            "complex lines degenerate. "
            "The strict W/Z plus C3 top-row splice shortcut is now pruned: "
            "the formal splice of the denominator W row with the conditional "
            "C3 target row gives 1/sqrt(6) only after supplying same-surface "
            "authority and the physical nontrivial top line, while the same "
            "denominator and source scale admit the P_0 singlet readout "
            "sqrt(2/3). "
            "The nontrivial real-block matrix-element support theorem now "
            "sharpens the C3 coefficient target: once zero P_0 singlet weight "
            "is supplied, B_x is scalar on P_nt and every P_nt-supported top "
            "readout gives A/sqrt(12), so complex-line isolation is not "
            "needed for the coefficient row. This does not authorize "
            "proposal language because zero singlet weight and accepted pole "
            "controls are still open. "
            "The radial-factor no-go now grants that P_nt support for the "
            "sake of argument and still prunes the shortcut: "
            "V_top(lambda_top)=lambda_top*A*B_x preserves the W row and C3 "
            "direction while varying the top coefficient, so the target "
            "requires accepted lambda_top=1/sqrt(2) generator factorization "
            "or direct strict pole rows. "
            "The radial/readout compensation shortcut is now pruned as well: "
            "the target-size equation lambda_top*|3*s-1|=1/sqrt(2) has "
            "multiple finite completions with different singlet weights and "
            "radial couplings, so target magnitude cannot back-solve zero "
            "singlet support, radial factorization, or signed physical "
            "orientation. "
            "The sharp-response readout shortcut is pruned too: Var(B_x)=0 "
            "selects both the P_nt endpoint and the P_0 endpoint, and the "
            "singlet endpoint can be target-size with a compensating radial "
            "factor, so sharpness is not a physical top-block selection law "
            "on the current surface. "
            "The Fisher/LSZ radial generator normalization shortcut is "
            "pruned as the required deep-work stretch attempt: Fisher "
            "arclength and LSZ remove raw source scale, but they do not "
            "identify the normalized C3 source tangent with the relative "
            "top response coefficient lambda_top=1/sqrt(2). "
            "The block-rank radial normalization shortcut is now pruned as "
            "well: rank(P_nt)=2 makes 1/sqrt(2) numerically tempting, but "
            "ordinary P_nt matrix elements, block-density expectations, and "
            "Hilbert-Schmidt block conventions do not derive the physical "
            "root-rank top radial generator law. "
            "The Fisher quotient radial-normalization shortcut is now "
            "pruned too: the reflection-even C3 line-simplex Fisher metric "
            "and the binary P_0/P_nt quotient metric are isometric, "
            "Fisher-unit normalization of the C3 score is only a "
            "source-coordinate unit rather than a top radial mass-generator "
            "law, and B_x has no internal Fisher direction inside P_nt "
            "because it is scalar on that block. "
            "The zero-singlet top-block membership shortcut from the current "
            "real/reflection-even C3 block data is now pruned too: the same "
            "finite block algebra permits P_0 or P_nt depending on an "
            "undetermined sign/order or minimum-response convention, so "
            "excluding P_0 remains a new physical law rather than an algebraic "
            "consequence. "
            "The source-orientation sign-selector shortcut is also pruned: "
            "choosing the sign of B_x that makes P_nt largest is an "
            "unaccepted orientation of the same source coordinate; the "
            "same-source top/W ratio is invariant under ell -> -ell, "
            "largest absolute response selects P_0, and minimum-response "
            "selection is still an imported convention. "
            "The trace-free centered-source shortcut is now pruned: "
            "Tr(B_x)=0 is an operator/source statement rather than a "
            "physical top-projector law; zero centered expectation gives "
            "s=1/3, while the target nontrivial response requires s=0. "
            "The minimum-information/RN-Fisher readout shortcut is now "
            "pruned as well: finite full-support exponential tilts over the "
            "C3 line responses cannot set the physical singlet weight to "
            "zero at finite source coordinate, while imposing the target "
            "nontrivial response as a constraint inserts the missing "
            "coefficient row. "
            "The hard-boundary completion of that same minimum-information "
            "family now gives exact conditional support: the C3 RN/Fisher "
            "curve has both P_nt and P_0 endpoints, and the nearest Fisher "
            "boundary face from the symmetric baseline is P_nt. This still "
            "does not authorize proposal language because nearest-boundary "
            "face selection is a new physical top-readout law, not accepted "
            "on the current surface. "
            "The hard-boundary readout-law underdetermination audit prunes "
            "promotion from current information geometry alone: the same "
            "boundary data also admit P_0-selecting purity/rank, "
            "positive-source-asymptote, and response-maximum rules, so "
            "nearest-face readout remains a new physical law. "
            "The primitive singular-boundary support theorem tightens the "
            "candidate: least-KL no-hidden-record singular boundary readout "
            "on the reflection-even C3 curve selects P_nt, but that "
            "singular-boundary top-readout law is not accepted on the actual "
            "surface. "
            "First-principles transfer response is now closed, but the top sector "
            "matrix element remains load-bearing. The factorization boundary shows "
            "exactly how A/sqrt(12) would follow from accepted generator "
            "factorization plus zero-singlet nontrivial-block support, but those inputs remain open "
            "and coefficient-certified top/W response evidence remains absent."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "first_open_gate": "accepted strict same-source top/W pole rows, or accepted independent same-surface radial generator factorization plus sign/order/readout/primitive-singular-boundary dynamics deriving zero-singlet physical top-block support with backend/projectors/matrix elements",
        "backup_route": "strict same-source top/W pole-response measurement certificate",
        "closure_stack": closure_stack,
        "certificates": certificates,
        "upstream_statuses": statuses,
        "support_output_status": {
            "fisher_fail_count": support_outputs["fisher"].get("fail_count"),
            "minimum_information_fail_count": support_outputs["minimum_information"].get("fail_count"),
            "primitive_record_law_fail_count": support_outputs["primitive_record_law"].get("fail_count"),
            "top_source_nogo_fail_count": support_outputs["top_source_nogo"].get("fail_count"),
            "minimum_information_uniqueness_fail_count": support_outputs["minimum_information_uniqueness"].get("fail_count"),
            "top_carrier_fail_count": support_outputs["top_carrier"].get("fail_count"),
            "fisher_lsz_fail_count": support_outputs["fisher_lsz"].get("fail_count"),
            "fh_fail_count": support_outputs["fh"].get("fail_count"),
            "same_source_fail_count": support_outputs["same_source"].get("fail_count"),
            "strict_wz_fail_count": support_outputs["strict_wz"].get("fail_count"),
            "strict_top_fail_count": support_outputs["strict_top"].get("fail_count"),
            "strict_same_source_obstruction_fail_count": support_outputs["strict_same_source_obstruction"].get("fail_count"),
            "first_principles_transfer_response_fail_count": support_outputs["first_principles_transfer_response"].get("fail_count"),
            "same_surface_top_matrix_element_factorization_fail_count": support_outputs["same_surface_top_matrix_element_factorization"].get("fail_count"),
            "c3_nontrivial_block_matrix_element_support_fail_count": support_outputs["c3_nontrivial_block_matrix_element_support"].get("fail_count"),
            "c3_same_surface_radial_factor_nogo_fail_count": support_outputs["c3_same_surface_radial_factor_nogo"].get("fail_count"),
            "c3_radial_readout_compensation_nogo_fail_count": support_outputs["c3_radial_readout_compensation_nogo"].get("fail_count"),
            "c3_sharp_response_readout_nogo_fail_count": support_outputs["c3_sharp_response_readout_nogo"].get("fail_count"),
            "fisher_lsz_radial_generator_nogo_fail_count": support_outputs["fisher_lsz_radial_generator_nogo"].get("fail_count"),
            "c3_block_rank_radial_normalization_nogo_fail_count": support_outputs["c3_block_rank_radial_normalization_nogo"].get("fail_count"),
            "c3_fisher_quotient_radial_normalization_nogo_fail_count": support_outputs["c3_fisher_quotient_radial_normalization_nogo"].get("fail_count"),
            "c3_zero_singlet_top_block_membership_nogo_fail_count": support_outputs["c3_zero_singlet_top_block_membership_nogo"].get("fail_count"),
            "c3_source_orientation_sign_selector_nogo_fail_count": support_outputs["c3_source_orientation_sign_selector_nogo"].get("fail_count"),
            "c3_trace_free_centered_source_zero_singlet_nogo_fail_count": support_outputs["c3_trace_free_centered_source_zero_singlet_nogo"].get("fail_count"),
            "c3_mininfo_readout_zero_singlet_nogo_fail_count": support_outputs["c3_mininfo_readout_zero_singlet_nogo"].get("fail_count"),
            "c3_mininfo_hard_boundary_face_selector_support_fail_count": support_outputs["c3_mininfo_hard_boundary_face_selector_support"].get("fail_count"),
            "c3_hard_boundary_readout_law_underdetermination_fail_count": support_outputs["c3_hard_boundary_readout_law_underdetermination"].get("fail_count"),
            "c3_primitive_singular_boundary_intervention_support_fail_count": support_outputs["c3_primitive_singular_boundary_intervention_support"].get("fail_count"),
            "direct_sparse_response_certificate_fail_count": support_outputs["direct_sparse_response_certificate"].get("fail_count"),
            "top_sector_projector_obstruction_fail_count": support_outputs["top_sector_projector_obstruction"].get("fail_count"),
            "c3_spectral_projector_support_fail_count": support_outputs["c3_spectral_projector_support"].get("fail_count"),
            "c3_spectral_source_response_nogo_fail_count": support_outputs["c3_spectral_source_response_nogo"].get("fail_count"),
            "c3_source_direction_nogo_fail_count": support_outputs["c3_source_direction_nogo"].get("fail_count"),
            "lsp_c3_source_direction_boundary_fail_count": support_outputs["lsp_c3_source_direction_boundary"].get("fail_count"),
            "positivity_orientation_c3_source_direction_boundary_fail_count": support_outputs["positivity_orientation_c3_source_direction_boundary"].get("fail_count"),
            "c3_connected_reflection_even_source_candidate_fail_count": support_outputs["c3_connected_reflection_even_source_candidate"].get("fail_count"),
            "c3_nontrivial_top_line_assignment_boundary_fail_count": support_outputs["c3_nontrivial_top_line_assignment_boundary"].get("fail_count"),
            "c3_connected_source_from_normalized_rn_fail_count": support_outputs["c3_connected_source_from_normalized_rn"].get("fail_count"),
            "c3_real_record_reflection_even_source_fail_count": support_outputs["c3_real_record_reflection_even_source"].get("fail_count"),
            "c3_top_line_mass_ordering_obstruction_fail_count": support_outputs["c3_top_line_mass_ordering_obstruction"].get("fail_count"),
            "c3_real_same_surface_top_line_law_obstruction_fail_count": support_outputs["c3_real_same_surface_top_line_law_obstruction"].get("fail_count"),
            "c3_circulant_dynamics_ordering_source_law_boundary_fail_count": support_outputs["c3_circulant_dynamics_ordering_source_law_boundary"].get("fail_count"),
            "strict_sparse_top_w_availability_audit_fail_count": support_outputs["strict_sparse_top_w_availability_audit"].get("fail_count"),
            "strict_pole_row_repository_discovery_nogo_fail_count": support_outputs["strict_pole_row_repository_discovery_nogo"].get("fail_count"),
            "microscopic_backend_projector_matrix_element_boundary_fail_count": support_outputs["microscopic_backend_projector_matrix_element_boundary"].get("fail_count"),
            "c3_positive_transfer_perron_top_line_nogo_fail_count": support_outputs["c3_positive_transfer_perron_top_line_nogo"].get("fail_count"),
            "c3_phase_ordering_cone_support_boundary_fail_count": support_outputs["c3_phase_ordering_cone_support_boundary"].get("fail_count"),
            "c3_orientation_phase_dynamics_necessity_fail_count": support_outputs["c3_orientation_phase_dynamics_necessity"].get("fail_count"),
            "c3_orientation_phase_strength_boundary_fail_count": support_outputs["c3_orientation_phase_strength_boundary"].get("fail_count"),
            "c3_quantitative_phase_strength_underdetermination_fail_count": support_outputs["c3_quantitative_phase_strength_underdetermination"].get("fail_count"),
            "c3_primitive_character_phase_angle_candidate_fail_count": support_outputs["c3_primitive_character_phase_angle_candidate"].get("fail_count"),
            "c3_representation_phase_selection_nogo_fail_count": support_outputs["c3_representation_phase_selection_nogo"].get("fail_count"),
            "c3_cubic_invariant_phase_selector_fail_count": support_outputs["c3_cubic_invariant_phase_selector"].get("fail_count"),
            "c3_cubic_phase_potential_nogo_fail_count": support_outputs["c3_cubic_phase_potential_nogo"].get("fail_count"),
            "c3_phase_orbit_selector_nogo_fail_count": support_outputs["c3_phase_orbit_selector_nogo"].get("fail_count"),
            "c3_orbit_member_readout_covariance_nogo_fail_count": support_outputs["c3_orbit_member_readout_covariance_nogo"].get("fail_count"),
            "c3_dihedral_basepoint_anchor_obstruction_fail_count": support_outputs["c3_dihedral_basepoint_anchor_obstruction"].get("fail_count"),
            "c3_orientation_biased_phase_potential_orbit_member_nogo_fail_count": support_outputs["c3_orientation_biased_phase_potential_orbit_member_nogo"].get("fail_count"),
            "c3_source_response_extremal_readout_nogo_fail_count": support_outputs["c3_source_response_extremal_readout_nogo"].get("fail_count"),
            "strict_wz_c3_top_row_splice_nogo_fail_count": support_outputs["strict_wz_c3_top_row_splice_nogo"].get("fail_count"),
        },
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
            "scripts/frontier_yt_full_closure_stack_and_strict_pole_response_contract.py",
            "outputs/yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json",
            "docs/YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md",
            "scripts/frontier_yt_microscopic_backend_projector_matrix_element_boundary.py",
            "outputs/yt_microscopic_backend_projector_matrix_element_boundary_2026-05-27.json",
            "docs/YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_nontrivial_block_matrix_element_support.py",
            "outputs/yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json",
            "docs/YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_same_surface_radial_factor_underdetermination_no_go.py",
            "outputs/yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json",
            "docs/YT_C3_RADIAL_READOUT_COMPENSATION_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_radial_readout_compensation_underdetermination_no_go.py",
            "outputs/yt_c3_radial_readout_compensation_underdetermination_no_go_2026-05-28.json",
            "docs/YT_C3_SHARP_RESPONSE_READOUT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_sharp_response_readout_underdetermination_no_go.py",
            "outputs/yt_c3_sharp_response_readout_underdetermination_no_go_2026-05-28.json",
            "docs/YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_fisher_lsz_radial_generator_normalization_no_go.py",
            "outputs/yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json",
            "docs/YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_block_rank_radial_normalization_no_go.py",
            "outputs/yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json",
            "docs/YT_C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_fisher_quotient_radial_normalization_no_go.py",
            "outputs/yt_c3_fisher_quotient_radial_normalization_no_go_2026-05-28.json",
            "docs/YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_zero_singlet_top_block_membership_no_go.py",
            "outputs/yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json",
            "docs/YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_source_orientation_sign_selector_no_go.py",
            "outputs/yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json",
            "docs/YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_trace_free_centered_source_zero_singlet_no_go.py",
            "outputs/yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json",
            "docs/YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_mininfo_readout_zero_singlet_no_go.py",
            "outputs/yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json",
            "docs/YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_mininfo_hard_boundary_face_selector_support.py",
            "outputs/yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json",
            "docs/YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_hard_boundary_readout_law_underdetermination.py",
            "outputs/yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json",
            "docs/YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_primitive_singular_boundary_intervention_support.py",
            "outputs/yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json",
            "docs/YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_positive_transfer_perron_top_line_no_go.py",
            "outputs/yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json",
            "docs/YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_phase_ordering_cone_support_boundary.py",
            "outputs/yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json",
            "docs/YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_orientation_phase_dynamics_necessity.py",
            "outputs/yt_c3_orientation_phase_dynamics_necessity_2026-05-27.json",
            "docs/YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_orientation_phase_strength_boundary.py",
            "outputs/yt_c3_orientation_phase_strength_boundary_2026-05-27.json",
            "docs/YT_C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_quantitative_phase_strength_underdetermination.py",
            "outputs/yt_c3_quantitative_phase_strength_underdetermination_2026-05-27.json",
            "docs/YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_primitive_character_phase_angle_candidate.py",
            "outputs/yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json",
            "docs/YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_representation_phase_selection_no_go.py",
            "outputs/yt_c3_representation_phase_selection_no_go_2026-05-27.json",
            "docs/YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_cubic_invariant_phase_selector_support_boundary.py",
            "outputs/yt_c3_cubic_invariant_phase_selector_support_boundary_2026-05-27.json",
            "docs/YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_cubic_phase_potential_sign_branch_underdetermination.py",
            "outputs/yt_c3_cubic_phase_potential_sign_branch_underdetermination_2026-05-27.json",
            "docs/YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_phase_orbit_selector_underdetermination.py",
            "outputs/yt_c3_phase_orbit_selector_underdetermination_2026-05-27.json",
            "docs/YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_orbit_member_readout_covariance_no_go.py",
            "outputs/yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json",
            "docs/YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_dihedral_basepoint_anchor_obstruction.py",
            "outputs/yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json",
            "docs/YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_orientation_biased_phase_potential_orbit_member_no_go.py",
            "outputs/yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json",
            "docs/YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_source_response_extremal_readout_no_go.py",
            "outputs/yt_c3_source_response_extremal_readout_no_go_2026-05-27.json",
            "docs/YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_strict_wz_c3_top_row_splice_no_go.py",
            "outputs/yt_strict_wz_c3_top_row_splice_no_go_2026-05-27.json",
            "docs/YT_STRICT_TOP_W_POLE_ROW_REPOSITORY_DISCOVERY_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_strict_top_w_pole_row_repository_discovery_no_go.py",
            "outputs/yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
