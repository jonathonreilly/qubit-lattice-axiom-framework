#!/usr/bin/env python3
"""Candidate assembly, sixteenth edition: the source-linked graph from the axioms
to the eleven preserved targets, with results as AND nodes, route choices as
OR nodes, and the exact minimal decision sets of every target.

TOE derivation campaign by underdetermination witnesses and its next-steps
continuation.  The graph is supplied structure assembled from cited
results; the theorems are its verified properties: well-formedness,
acyclicity with a negative control, source linking on disk, and the exact
minimal decision sets under AND/OR semantics.  No completion percentage and
no physical identification.  Changes from the first edition: nearest-
neighbour locality is Admissibility text (its decision group is withdrawn);
the clock group becomes the order-law group without its order-blind
candidate; roles can be supplied or registered by formation; the photon
route runs through the static reading or through formation.  Third edition:
registered frames (open PR 8676) give soldering an alternative, coordinate
letters with an order law, in both formation routes.  Fourth edition: the
static route needs a frame source as well (open PR #8679): soldered vertex
records with supplied roles, or coordinate letters with roles read from labels.
Fifth edition: the formed photon route reaches the uniform ice measure only
through a coordinator (open PR #8686), formed ice is otherwise directed (open
PR #8687), and the letters may be fixed or relational (open PR #8691).  Sixth
edition: a positive static rule selects the equal-time Coulomb law (open PR
#8698), and formed flux moves as a persistent walk (open PR #8701).  Seventh
edition: single-site formation reaches the uniform ice measure beyond one top
cell only with plan letters (two planar squares, open PR #8715; two adjacent
cubes, open PR #8719; plans, open PR #8686); finite joint cell units reach
rows but not blocks, in the plane and in three dimensions (open PR #8720);
and relational spirals are rigid on the lattice and under the static reading
but amplified by the sweep (open PR #8717).  Eighth edition: beyond rows,
exact joint formation needs units unbounded along an axis formed as a chain,
so the joint-unit route needs an order law as well (open PR #8720), and the
static spiral is locally rigid in the full nonlinear relations (open PR
#8724).  Ninth edition: the landed torus ice measure has no local formation
order (open PR #8727), every linear ice sweep rule moves flux as a damped or
rigid Markov walk (open PR #8726), and seven relational letters carry the
frame (open PR #8729); the minimal sets are unchanged.  Tenth edition: no
planar window of two to five squares admits a single-site order (open PR
#8735), under local formation multi-qubit units leave relational first
formations a fair coin (open PR #8731), under the static reading with its
fixed octant relational frames with Sidon angles are globally rigid,
carrying the frame but no role pattern (open PR #8743), that rigidity needs
a global octant (open PR #8744), and layer units form uniform ice on
infinite prisms in the zero-flux sector (open PR #8740), whose flux sectors
carry a Gaussian stiffness (open PR #8746); the minimal sets are unchanged.
Eleventh edition: relational letters in alternating pairs record the role
pattern under the static reading away from the side-4 torus (open PR
#8750), and four-angle cycles record it on the landed ice torus (open PR
#8752), so with relational letters only, as under possibility covariance,
gravity's one unsoldered set becomes {alphabet, reading}; under the sweep
reading the cycle letters record no role pattern (open PR #8756), so that
route needs the static reading.  Twelfth edition: that route needs no
supplied octant.  Under the rotation-covariant rule the cycle letters record
their octant on the landed torus (open PR #8854), strong cycle letters record
the frame and the roles on every window (open PR #8856), and strong letters
are generic (open PR #8857); the minimal sets are unchanged.  Thirteenth
edition: thirty-five of the cited pull requests have landed, so thirty-eight
nodes now link to their landed notes and thirteen stay open.  The photon
lane joins record dynamics.  By row transfer the flux stiffness is Gaussian
on the square cross-section (open PR #8859).  The zero-flux layer chain is
gapless, its gap falling as the smallest transverse wavenumber (open PR
#8864), and its branch has the dispersion of a massless nearest-neighbour
lattice field (open PR #8869).  The unit link field fixes one stiffness for
the flux cost and the correlations (open PR #8871), and test defects
interact through the lattice Green's function at that stiffness (open PR
#8875).  The minimal sets are unchanged.  Fourteenth edition: ten more cited
pull requests have landed, among them the first-edition inputs 8637, 8641
and 8646 and the photon-lane results 8859 and 8864, so ten more nodes link
to their landed notes and five stay open.  On cubic tori to side 24 the
winding stiffness and the correlations carry the sum-rule stiffness, with a
long-wavelength value 0.5% above 1/3 (open PR #8881), and the static photon
has two degenerate transverse polarizations with one stiffness (open PR
#8890).  The minimal sets are unchanged.  Fifteenth edition: the layer
vacuum is a Gaussian flux functional, so the layer-unit law is local
transfer times a 1/r flux interaction (open PR #8896); at the RK point of
the supplied Hamiltonian the photon's single-mode bound is quadratic (open
PR #8905); worms sample test-defect pairs exactly, and the pair free energy
follows the Green function on tori (open PR #8913); and uniform ice carries
the lattice Green function only in its charged sector, with short-ranged
neutral scalar records, which answers the design note's seam for this
measure and narrows gravity's input (open PR #8918).  The first three join
record dynamics, the last feeds gravity; the minimal sets are unchanged.
Sixteenth edition: the static photon stiffens in a background flux and
saturation leaves square ice (open PR #8928); the unit-field sum rule is
ten times closer for three-dimensional ice than for square ice (open PR
#8930); in a flux sector the photon's rise is wavenumber-independent and a
second branch crosses below it (open PR #8949); and test-defect pairs follow
the charge-squared law with a core correction (open PR #8951).  All four
join record dynamics; the minimal sets are unchanged.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import os
import sys

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


D = "docs/"
L = "landed"
OP = "open"
NODES = {
    "AX": ("source", D + "MINIMAL_AXIOMS_2026-06-29.md"),
    "PRIM": ("source", "premise registry: scale_reference, kinetic_isotropy, realized_state"),
    "ORDER_LAW": (L, D + "ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "BINARY_ORDER_BLIND": (L, D + "FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "HANDED_CENSUS": (L, D + "ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "READABILITY": (L, D + "ADMISSIBILITY_READABILITY_CONTINUUM_ALPHABET_FISHER_RANK_AND_FORMATION_ORDER_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "COMPOSITION_ZEROS": (L, D + "COMPOSITION_LAW_SELECTION_GRADED_ZEROS_ORDER_BLIND_RULES_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "GAUSS_SUPPORT": (L, D + "COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "SOLDER_CENSUS": (L, D + "POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "ROLES_NNN": (L, D + "THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md"),
    "REPEAT_CERT_SELECTS": (L, D + "COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md"),
    "BORN_PRICE": (L, D + "THE_BORN_PRICE_WORDINGS_HOMOGENEITY_IS_PAYABLE_ON_THE_CONTINUUM_LAW_AS_IT_STANDS_THE_COLLINEAR_MENUS_NEED_A_SCALE_READING_RULE_THE_FOUR_OUTCOME_MENU_PAYS_WITH_NO_CLAUSE_AND_NONE_REMOVES_THE_FAIR_COIN_BOUNDED_NOTE_2026-09-05.md"),
    "GLUED_HIERARCHY": (L, D + "A_HIERARCHY_OF_NEIGHBOURHOOD_CONDITIONS_GLUED_BREAKABLE_AND_FREE_RECORD_GROUPS_UNDER_SHIFTING_TICKS_BOUNDED_THEOREM_NOTE_2026-09-03.md"),
    "CUBIC_ICE_RK": (L, D + "SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md"),
    "GRAVITY_BOUNDARIES": (L, D + "LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "FAIR_COIN_ANTIPARALLEL": (L, D + "MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "SOLDERED_SPLIT": (L, D + "MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "AFFINE_REDUCTION": (L, D + "MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "CLOCK_INVISIBILITY": (L, D + "CLOCK_AND_RATE_COVARIANT_EXPONENTIAL_RACES_RECORD_LEVEL_INVISIBILITY_FOR_ORDER_BLIND_RULES_AND_CLOCK_SENSITIVE_HOLE_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "HOLE_READS_CLOCK": (L, D + "CLOCK_AND_RATE_COVARIANT_EXPONENTIAL_RACES_RECORD_LEVEL_INVISIBILITY_FOR_ORDER_BLIND_RULES_AND_CLOCK_SENSITIVE_HOLE_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "BLOCK_CHAIN_EQUALITY": (L, D + "FORMATION_UNIT_SEQUENTIAL_VS_JOINT_COVARIANT_SETS_BLOCK_CHAIN_EQUALITY_PRODUCT_FILL_VISIBILITY_AND_GLUED_UNIT_HOLE_DISSOLUTION_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "UNIT_DIAL": (L, D + "FORMATION_UNIT_SEQUENTIAL_VS_JOINT_COVARIANT_SETS_BLOCK_CHAIN_EQUALITY_PRODUCT_FILL_VISIBILITY_AND_GLUED_UNIT_HOLE_DISSOLUTION_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "KERNEL_MISMATCH": (L, D + "RECORD_DYNAMICS_FINISHED_RECORD_CORRELATORS_AGAINST_PROPAGATION_KERNELS_NEAREST_NEIGHBOUR_SENTENCE_EXCLUDES_LONG_RANGE_PAIRS_AND_GLUED_SUPPORT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "NN_EXCLUSION": (L, D + "RECORD_DYNAMICS_FINISHED_RECORD_CORRELATORS_AGAINST_PROPAGATION_KERNELS_NEAREST_NEIGHBOUR_SENTENCE_EXCLUDES_LONG_RANGE_PAIRS_AND_GLUED_SUPPORT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "CODE_RIGIDITY": (L, D + "RECORD_DYNAMICS_FINISHED_RECORD_CORRELATORS_AGAINST_PROPAGATION_KERNELS_NEAREST_NEIGHBOUR_SENTENCE_EXCLUDES_LONG_RANGE_PAIRS_AND_GLUED_SUPPORT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "ORDER_BLIND_RANGE": (L, D + "ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "UNSOLDERED_CONSTANCY": (L, D + "ORDER_BLIND_FORMATION_WITH_ZEROS_AND_HOLES_NEVER_FAILING_UNSOLDERED_RULES_ARE_CONSTANT_AND_HOLE_RULES_HAVE_PAIR_FORM_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "PAIR_FORM_HOLES": (L, D + "ORDER_BLIND_FORMATION_WITH_ZEROS_AND_HOLES_NEVER_FAILING_UNSOLDERED_RULES_ARE_CONSTANT_AND_HOLE_RULES_HAVE_PAIR_FORM_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "ORDER_VISIBLE": (L, D + "HOLES_AS_UNRECORDED_SITES_UNSOLDERED_ORDER_BLIND_RULES_ARE_CONSTANT_AND_THE_FORMATION_ORDER_IS_VISIBLE_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "ICE_FORMATION": (L, D + "ICE_SUPPORT_UNDER_NEAREST_NEIGHBOUR_FORMATION_VERTEX_BOUND_SOLDERED_VERTEX_RECORDS_ORDER_DEPENDENT_DEFECTS_AND_UNIFORM_ICE_ONLY_BY_CONDITIONING_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "STAR_BROADCAST": (L, D + "STAR_CONSTRAINTS_UNDER_NEAREST_NEIGHBOUR_FORMATION_UNSOLDERED_BROADCAST_BOUNDS_AND_SOLDERED_REGISTRATION_OF_THE_PARITY_ROLE_SKELETON_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "ROLES_REGISTERED": (L, D + "STAR_CONSTRAINTS_UNDER_NEAREST_NEIGHBOUR_FORMATION_UNSOLDERED_BROADCAST_BOUNDS_AND_SOLDERED_REGISTRATION_OF_THE_PARITY_ROLE_SKELETON_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "ORDER_LAW_FRONTS": (L, D + "ORDER_LAWS_FOR_EXTENDED_SOLDERED_SUPPORTS_INDEPENDENT_CLOCKS_NUCLEATE_AT_POSITIVE_DENSITY_AND_SWEEPS_HAVE_NO_FIRST_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "SOLDER_MENU": (L, D + "THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "FRAME_REGISTRATION": (L, D + "REGISTERED_FRAMES_COORDINATE_LABELS_SWEEP_RIGIDITY_CORNER_PRICE_AND_SOLDERED_EMULATION_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "STATIC_ICE_RECORDS": (L, D + "STATIC_ICE_MEASURE_NEAREST_NEIGHBOUR_ADMISSIBILITY_NEEDS_A_FRAME_SOURCE_SOLDERED_VERTEX_RECORDS_OR_COORDINATE_LETTERS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "UNIFORM_ICE_COORDINATION": (L, D + "UNIFORM_ICE_BY_FORMATION_THE_SQUARE_LOOP_OBSTRUCTION_THE_PLAQUETTE_COORDINATOR_AND_PLANS_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "DIRECTED_ICE": (L, D + "DIRECTED_ICE_SWEEP_FORMATION_MAKES_ICE_CORRELATIONS_CAUSAL_FLUX_PROPAGATES_AS_A_DIRECTED_RANDOM_WALK_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "RELATIONAL_FRAMES": (L, D + "RELATIONAL_FRAMES_IN_ONE_QUBIT_SPIRAL_RECORDS_UNDER_POSSIBILITY_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "COULOMB_SELECTION": (L, D + "COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "FLUX_TRANSPORT": (L, D + "FORMED_FLUX_AS_A_PERSISTENT_WALK_STRAIGHT_CONTINUATION_GIVES_BALLISTIC_THEN_DIFFUSIVE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "TWO_SQUARES_NO_ORDER": (L, D + "UNIFORM_ICE_BY_FORMATION_TWO_PLANAR_SQUARES_ADMIT_NO_LOCAL_ORDER_AND_ONE_CUBE_NEEDS_ITS_CUBE_SITE_BOUNDED_THEOREM_NOTE_2026-09-22.md"),
    "TWO_CUBES_NO_ORDER": (L, D + "UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "SPIRAL_RIGIDITY": (L, D + "RELATIONAL_SPIRAL_FRAMES_ARE_RIGID_ON_THE_LATTICE_AND_UNDER_THE_STATIC_READING_BUT_FLEXIBLE_AND_AMPLIFIED_UNDER_THE_SWEEP_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "JOINT_CELL_UNITS": (L, D + "UNIFORM_ICE_BY_JOINT_CELL_UNITS_ROWS_YES_THE_TWO_BY_TWO_BLOCK_NO_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "STATIC_SPIRAL_RIGIDITY": (L, D + "RELATIONAL_SPIRAL_FRAMES_ARE_LOCALLY_RIGID_UNDER_THE_STATIC_READING_NONLINEAR_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "LINEAR_SWEEP_TRANSPORT": (L, D + "FORMED_FLUX_TRANSPORT_FOR_EVERY_LINEAR_ICE_SWEEP_RULE_IS_A_MARKOV_WALK_DAMPED_OR_RIGID_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "TORUS_NO_ORDER": (L, D + "THE_LANDED_TORUS_UNIFORM_ICE_MEASURE_ADMITS_NO_LOCAL_FORMATION_ORDER_EVEN_WITH_EVERY_COORDINATOR_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "FINITE_RELATIONAL_LETTERS": (L, D + "RELATIONAL_SPIRAL_LETTERS_WITH_FINITELY_MANY_VALUES_SEVEN_SUFFICE_AND_ARE_THE_FEWEST_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "POLYOMINO_NO_ORDER": (L, D + "UNIFORM_ICE_BY_SINGLE_SITES_NO_PLANAR_WINDOW_OF_TWO_TO_FIVE_SQUARES_ADMITS_A_LOCAL_FORMATION_ORDER_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "UNIT_FAIR_COIN": (L, D + "RELATIONAL_LETTERS_FORMED_BY_MULTI_QUBIT_UNITS_EVERY_SINGLE_FACE_ATTACHMENT_IS_AT_BEST_A_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "STATIC_GLOBAL_RIGIDITY": (L, D + "RELATIONAL_LETTERS_UNDER_THE_STATIC_READING_ARE_GLOBALLY_RIGID_EXACTLY_FOR_SIDON_ANGLE_SETS_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "LAYER_UNITS_PRISMS": (L, D + "UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "GLOBAL_OCTANT": (L, D + "RELATIONAL_LETTERS_STATIC_RIGIDITY_NEEDS_A_GLOBAL_OCTANT_SITE_AND_LINE_ORIENTATIONS_LEAVE_THE_LETTERS_FLEXIBLE_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "FLUX_STIFFNESS": (L, D + "UNIFORM_ICE_LAYER_TRANSFER_FLUX_SECTORS_CARRY_A_GAUSSIAN_STIFFNESS_INVERSE_IN_THE_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "PAIR_LETTER_ROLES": (L, D + "RELATIONAL_LETTERS_IN_ALTERNATING_PAIRS_RECORD_THE_ROLE_PATTERN_UNDER_THE_STATIC_READING_BUT_NOT_ON_THE_SIDE_FOUR_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "CYCLE_LETTER_ROLES": (L, D + "RELATIONAL_LETTERS_IN_FOUR_ANGLE_CYCLES_RECORD_THE_ROLE_PATTERN_ON_THE_LANDED_ICE_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "SWEEP_NO_ROLES": (L, D + "RELATIONAL_CYCLE_LETTERS_UNDER_THE_SWEEP_READING_RECORD_NO_ROLE_PATTERN_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "OCTANT_RECORDED": (L, D + "RELATIONAL_CYCLE_LETTERS_RECORD_THEIR_OCTANT_UNDER_THE_ROTATION_COVARIANT_STATIC_RULE_ON_THE_LANDED_ICE_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "FOLDED_ROLES": (L, D + "STRONG_CYCLE_LETTERS_RECORD_FRAME_AND_ROLES_UNDER_THE_ROTATION_COVARIANT_RULE_ON_EVERY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "GENERIC_LETTERS": (L, D + "STRONG_CYCLE_LETTERS_ARE_GENERIC_EVERY_OBSTRUCTION_IS_A_NONTRIVIAL_ANGLE_RELATION_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "ROW_TRANSFER_SQUARE": (L, D + "UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "GAPLESS_CHAIN": (L, D + "UNIFORM_ICE_ZERO_FLUX_LAYER_CHAIN_GAP_CLOSES_AS_THE_SMALLEST_TRANSVERSE_WAVENUMBER_BOUNDED_THEOREM_NOTE_2026-09-23.md"),
    "MASSLESS_BRANCH": (OP, "open PR #8869 (the layer transfer's branch has the dispersion of a massless nearest-neighbour lattice field)"),
    "ONE_STIFFNESS": (OP, "open PR #8871 (the unit link field fixes one stiffness for the flux cost and the correlations)"),
    "TEST_DEFECT_COULOMB": (OP, "open PR #8875 (test defects interact through the lattice Green's function at the flux-cost stiffness)"),
    "WINDING_STIFFNESS": (OP, "open PR #8881 (on cubic tori to side 24 the winding stiffness and the correlations carry the sum-rule stiffness)"),
    "TWO_POLARIZATIONS": (OP, "open PR #8890 (the static photon has two degenerate transverse polarizations with one stiffness)"),
    "LAYER_VACUUM": (OP, "open PR #8896 (the layer vacuum is a Gaussian flux functional, so the layer-unit law carries a 1/r flux interaction)"),
    "RK_SOFT_PHOTON": (OP, "open PR #8905 (at the RK point of the supplied Hamiltonian the photon's single-mode bound is quadratic)"),
    "WORM_DEFECT_PAIRS": (OP, "open PR #8913 (worms sample test-defect pairs exactly; the pair free energy follows the Green function on tori)"),
    "GREEN_CHARGED_SECTOR": (OP, "open PR #8918 (uniform ice carries the lattice Green function in its charged sector; neutral scalar records are short-ranged)"),
    "NONLINEAR_PHOTON": (OP, "open PR #8928 (the static photon stiffens in a background flux, and saturation leaves square ice)"),
    "DIMENSION_CONTRAST": (OP, "open PR #8930 (the unit-field sum rule is ten times closer for three-dimensional ice than for square ice)"),
    "FLUX_QUANTA_SHIFT": (OP, "open PR #8949 (in a flux sector the photon's rise is wavenumber-independent and a second branch crosses below it)"),
    "CHARGE_SQUARED": (OP, "open PR #8951 (test-defect pairs follow the charge-squared law with a core correction)"),
    "DEC_SOLDER": ("decision", "recorded in SOLDER_CENSUS and SOLDER_MENU"),
    "DEC_MIRROR": ("decision", "recorded in HANDED_CENSUS"),
    "DEC_ALPHABET": ("decision", "recorded in READABILITY, ROLES_REGISTERED, FRAME_REGISTRATION, STATIC_ICE_RECORDS and UNIFORM_ICE_COORDINATION"),
    "DEC_GRADING": ("decision", "recorded in COMPOSITION_ZEROS"),
    "DEC_ROLES": ("decision", "recorded in GAUSS_SUPPORT and ROLES_NNN"),
    "DEC_AFFINITY": ("decision", "recorded in AFFINE_REDUCTION"),
    "DEC_MENU_SUPPLIER": ("decision", "recorded in AFFINE_REDUCTION"),
    "DEC_REPEAT_CERT": ("decision", "recorded in AFFINE_REDUCTION and REPEAT_CERT_SELECTS"),
    "DEC_ORDER_LAW": ("decision", "recorded in HOLE_READS_CLOCK and ORDER_LAW_FRONTS"),
    "DEC_UNIT": ("decision", "recorded in UNIT_DIAL"),
    "DEC_RULE": ("decision", "recorded in ORDER_LAW and ORDER_VISIBLE"),
    "DEC_READING": ("decision", "recorded in ORDER_BLIND_RANGE and PAIR_FORM_HOLES"),
    "ROLES_SOURCE": ("choice", "supplied roles, roles registered by formation, or roles read from static coordinate or relational pair letters"),
    "PHOTON_ROUTE": ("choice", "static reading with the landed ice measure, or formation"),
    "STATIC_ICE_ROUTE": ("route", "static reading, the landed uniform ice measure, and a static frame source"),
    "STATIC_FRAME_SOURCE": ("choice", "soldered vertex records, or coordinate letters under the static reading"),
    "STATIC_LETTERS_ROUTE": ("route", "coordinate letters make the static ice records nearest-neighbour"),
    "ROLES_STATIC_LETTERS": ("route", "roles read from static coordinate letters"),
    "ROLES_PAIR_LETTERS": ("route", "roles read from static relational letters: pairs away from the side-4 torus, four-angle cycles on it, strong cycles on every window under the rotation-covariant rule"),
    "FORMED_ICE_ROUTE": ("route", "formation of the ice support (soldered or registered frame)"),
    "REGISTERED_FRAME_ROUTE": ("route", "coordinate letters with an order law register the lattice frame"),
    "FRAME_SOURCE": ("choice", "soldering, or a frame registered by coordinate letters"),
    "LETTER_SCHEME": ("choice", "fixed coordinate letters, or relational spiral letters under possibility covariance"),
    "ORDER_OR_UNIT": ("choice", "single sites with an order law, or joint formation units"),
    "SINGLE_SITE_ROUTE": ("route", "single-site formation with an order law; plan letters beyond one top cell"),
    "JOINT_UNIT_ROUTE": ("route", "joint formation units; beyond rows, units unbounded along an axis formed as a chain by an order law"),
    "T_FORMATION_LAW": ("target", "design note: formation law"),
    "T_MENUS": ("target", "design note: possibility domain and menus"),
    "T_HANDEDNESS": ("target", "design note: handedness"),
    "T_BORN": ("target", "design note: Born weights"),
    "T_READABILITY": ("target", "design note: readability"),
    "T_CLOCK_RATE": ("target", "design note: clock/rate"),
    "T_FORMATION_UNIT": ("target", "design note: formation unit"),
    "T_RECORD_DYNAMICS": ("target", "design note: record dynamics"),
    "T_MATTER": ("target", "design note: matter/composition"),
    "T_GAUGE": ("target", "design note: support/gauge structure"),
    "T_GRAVITY": ("target", "design note: downstream gravity"),
}
CANDIDATES = {
    "DEC_SOLDER": ["trivial action (unsoldered)", "sign twist", "axis soldering", "full soldering (the three Cl(3,0) generators are the lattice axes)"],
    "DEC_MIRROR": ["covariance under improper rotations", "mirror sense as registered content", "parity fix clause"],
    "DEC_ALPHABET": ["continuum Bloch alphabet", "finite orbit alphabet", "eight axis-labelled role letters",
                     "coordinate letters (Z_4^3 labels with tags)",
                     "relational spiral letters (Bloch sphere, possibility covariance; seven values suffice, PR #8729, landed)",
                     "plan letters carrying a window configuration (PR #8686, landed)"],
    "DEC_GRADING": ["graded composition", "ordinary composition with a supplied encoding"],
    "DEC_ROLES": ["window extension", "sector clause", "supplied next-nearest-neighbour role pattern"],
    "DEC_AFFINITY": ["affinity/mixture-linearity in the neighbour state", "leave the non-affine class open"],
    "DEC_MENU_SUPPLIER": ["own value", "second neighbour", "lattice axis"],
    "DEC_REPEAT_CERT": ["same-label repeat certainty", "flipped-label certainty (anti-Born)"],
    "DEC_ORDER_LAW": ["independent identical clocks", "eagerness (count) clock", "value clock",
                      "front-like law with no first formation", "time as record count"],
    "DEC_UNIT": ["single-site unit", "covariant set with product fill", "covariant set with block-chain fill", "support-aligned glued units",
                 "units unbounded along an axis, formed as a chain (PR #8720, landed)"],
    "DEC_RULE": ["order-sensitive nearest-neighbour rule", "soldered order-blind rule of nearest-neighbour reach", "support rule with holes"],
    "DEC_READING": ["formation reading of the distribution sentence", "static reading of the distribution sentence"],
}
WITHDRAWN = {"DEC_LOCALITY": "nearest-neighbour locality is Admissibility text (PR #8646, landed)",
             "order-blind physical rule": "excluded under the unsoldered reading by the text (PRs #8663, #8664, #8666, landed)"}
EDGES = [("AX", n) for n, (k, p) in NODES.items() if k in (L, OP)] + [
    ("PRIM", "ORDER_LAW"), ("PRIM", "ORDER_VISIBLE"), ("PRIM", "ORDER_LAW_FRONTS"),
    ("STAR_BROADCAST", "ROLES_REGISTERED"), ("FRAME_SOURCE", "ROLES_REGISTERED"),
    ("DEC_SOLDER", "FRAME_SOURCE"), ("REGISTERED_FRAME_ROUTE", "FRAME_SOURCE"),
    ("FRAME_REGISTRATION", "LETTER_SCHEME"), ("RELATIONAL_FRAMES", "LETTER_SCHEME"),
    ("LETTER_SCHEME", "REGISTERED_FRAME_ROUTE"), ("DEC_ALPHABET", "REGISTERED_FRAME_ROUTE"),
    ("DEC_ORDER_LAW", "REGISTERED_FRAME_ROUTE"),
    ("DEC_ORDER_LAW", "ROLES_REGISTERED"), ("DEC_ALPHABET", "ROLES_REGISTERED"),
    ("DEC_ROLES", "ROLES_SOURCE"), ("ROLES_REGISTERED", "ROLES_SOURCE"),
    ("CUBIC_ICE_RK", "STATIC_ICE_ROUTE"), ("DEC_READING", "STATIC_ICE_ROUTE"),
    ("STATIC_ICE_RECORDS", "STATIC_ICE_ROUTE"), ("STATIC_FRAME_SOURCE", "STATIC_ICE_ROUTE"), ("COULOMB_SELECTION", "STATIC_ICE_ROUTE"),
    ("DEC_SOLDER", "STATIC_FRAME_SOURCE"), ("STATIC_LETTERS_ROUTE", "STATIC_FRAME_SOURCE"),
    ("STATIC_ICE_RECORDS", "STATIC_LETTERS_ROUTE"), ("DEC_ALPHABET", "STATIC_LETTERS_ROUTE"),
    ("STATIC_ICE_RECORDS", "ROLES_STATIC_LETTERS"), ("DEC_READING", "ROLES_STATIC_LETTERS"),
    ("DEC_ALPHABET", "ROLES_STATIC_LETTERS"), ("ROLES_STATIC_LETTERS", "ROLES_SOURCE"),
    ("ICE_FORMATION", "FORMED_ICE_ROUTE"), ("FRAME_SOURCE", "FORMED_ICE_ROUTE"), ("UNIFORM_ICE_COORDINATION", "FORMED_ICE_ROUTE"), ("ORDER_OR_UNIT", "FORMED_ICE_ROUTE"),
    ("SINGLE_SITE_ROUTE", "ORDER_OR_UNIT"), ("JOINT_UNIT_ROUTE", "ORDER_OR_UNIT"),
    ("DEC_UNIT", "JOINT_UNIT_ROUTE"), ("JOINT_CELL_UNITS", "JOINT_UNIT_ROUTE"), ("DEC_ORDER_LAW", "JOINT_UNIT_ROUTE"),
    ("DEC_ORDER_LAW", "SINGLE_SITE_ROUTE"), ("DEC_ALPHABET", "SINGLE_SITE_ROUTE"),
    ("TWO_SQUARES_NO_ORDER", "SINGLE_SITE_ROUTE"), ("TWO_CUBES_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("SPIRAL_RIGIDITY", "RELATIONAL_FRAMES"), ("STATIC_SPIRAL_RIGIDITY", "RELATIONAL_FRAMES"),
    ("FINITE_RELATIONAL_LETTERS", "RELATIONAL_FRAMES"), ("TORUS_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("LINEAR_SWEEP_TRANSPORT", "T_RECORD_DYNAMICS"), ("POLYOMINO_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("UNIT_FAIR_COIN", "RELATIONAL_FRAMES"), ("STATIC_GLOBAL_RIGIDITY", "RELATIONAL_FRAMES"),
    ("LAYER_UNITS_PRISMS", "JOINT_UNIT_ROUTE"), ("GLOBAL_OCTANT", "RELATIONAL_FRAMES"),
    ("FLUX_STIFFNESS", "JOINT_UNIT_ROUTE"),
    ("PAIR_LETTER_ROLES", "ROLES_PAIR_LETTERS"), ("DEC_READING", "ROLES_PAIR_LETTERS"), ("DEC_ALPHABET", "ROLES_PAIR_LETTERS"),
    ("CYCLE_LETTER_ROLES", "ROLES_PAIR_LETTERS"), ("SWEEP_NO_ROLES", "ROLES_PAIR_LETTERS"),
    ("OCTANT_RECORDED", "ROLES_PAIR_LETTERS"), ("FOLDED_ROLES", "ROLES_PAIR_LETTERS"), ("GENERIC_LETTERS", "ROLES_PAIR_LETTERS"),
    ("ROW_TRANSFER_SQUARE", "T_RECORD_DYNAMICS"), ("GAPLESS_CHAIN", "T_RECORD_DYNAMICS"), ("MASSLESS_BRANCH", "T_RECORD_DYNAMICS"),
    ("ONE_STIFFNESS", "T_RECORD_DYNAMICS"), ("TEST_DEFECT_COULOMB", "T_RECORD_DYNAMICS"),
    ("WINDING_STIFFNESS", "T_RECORD_DYNAMICS"), ("TWO_POLARIZATIONS", "T_RECORD_DYNAMICS"),
    ("LAYER_VACUUM", "T_RECORD_DYNAMICS"), ("RK_SOFT_PHOTON", "T_RECORD_DYNAMICS"), ("WORM_DEFECT_PAIRS", "T_RECORD_DYNAMICS"),
    ("GREEN_CHARGED_SECTOR", "T_GRAVITY"),
    ("NONLINEAR_PHOTON", "T_RECORD_DYNAMICS"), ("DIMENSION_CONTRAST", "T_RECORD_DYNAMICS"),
    ("FLUX_QUANTA_SHIFT", "T_RECORD_DYNAMICS"), ("CHARGE_SQUARED", "T_RECORD_DYNAMICS"),
    ("ROLES_PAIR_LETTERS", "ROLES_SOURCE"),
    ("STATIC_ICE_ROUTE", "PHOTON_ROUTE"), ("FORMED_ICE_ROUTE", "PHOTON_ROUTE"),
    ("ORDER_LAW", "T_FORMATION_LAW"), ("ORDER_VISIBLE", "T_FORMATION_LAW"), ("UNSOLDERED_CONSTANCY", "T_FORMATION_LAW"),
    ("BINARY_ORDER_BLIND", "T_FORMATION_LAW"), ("DEC_RULE", "T_FORMATION_LAW"), ("DEC_ORDER_LAW", "T_FORMATION_LAW"),
    ("SOLDER_CENSUS", "T_MENUS"), ("FAIR_COIN_ANTIPARALLEL", "T_MENUS"), ("SOLDERED_SPLIT", "T_MENUS"),
    ("DEC_SOLDER", "T_MENUS"), ("DEC_MENU_SUPPLIER", "T_MENUS"),
    ("HANDED_CENSUS", "T_HANDEDNESS"), ("DEC_MIRROR", "T_HANDEDNESS"), ("DEC_SOLDER", "T_HANDEDNESS"),
    ("AFFINE_REDUCTION", "T_BORN"), ("BORN_PRICE", "T_BORN"), ("REPEAT_CERT_SELECTS", "T_BORN"),
    ("DEC_AFFINITY", "T_BORN"), ("DEC_REPEAT_CERT", "T_BORN"), ("DEC_MENU_SUPPLIER", "T_BORN"),
    ("READABILITY", "T_READABILITY"), ("DEC_ALPHABET", "T_READABILITY"),
    ("CLOCK_INVISIBILITY", "T_CLOCK_RATE"), ("HOLE_READS_CLOCK", "T_CLOCK_RATE"), ("ORDER_VISIBLE", "T_CLOCK_RATE"),
    ("PAIR_FORM_HOLES", "T_CLOCK_RATE"), ("ORDER_LAW_FRONTS", "T_CLOCK_RATE"), ("DEC_ORDER_LAW", "T_CLOCK_RATE"),
    ("BLOCK_CHAIN_EQUALITY", "T_FORMATION_UNIT"), ("UNIT_DIAL", "T_FORMATION_UNIT"),
    ("GLUED_HIERARCHY", "T_FORMATION_UNIT"), ("DEC_UNIT", "T_FORMATION_UNIT"),
    ("KERNEL_MISMATCH", "T_RECORD_DYNAMICS"), ("NN_EXCLUSION", "T_RECORD_DYNAMICS"), ("CODE_RIGIDITY", "T_RECORD_DYNAMICS"),
    ("ORDER_BLIND_RANGE", "T_RECORD_DYNAMICS"), ("PHOTON_ROUTE", "T_RECORD_DYNAMICS"), ("DIRECTED_ICE", "T_RECORD_DYNAMICS"), ("FLUX_TRANSPORT", "T_RECORD_DYNAMICS"),
    ("COMPOSITION_ZEROS", "T_MATTER"), ("DEC_GRADING", "T_MATTER"),
    ("GAUSS_SUPPORT", "T_GAUGE"), ("ROLES_NNN", "T_GAUGE"), ("GLUED_HIERARCHY", "T_GAUGE"), ("ROLES_SOURCE", "T_GAUGE"),
    ("GRAVITY_BOUNDARIES", "T_GRAVITY"), ("T_RECORD_DYNAMICS", "T_GRAVITY"), ("T_GAUGE", "T_GRAVITY"),
    ("HOLE_READS_CLOCK", "T_GRAVITY"),
]
OPEN_EDGES = {
    "T_GRAVITY": ["record-statistic bridge from a supported source to a curvature response (unproved; uniform ice carries the lattice Green function only in its charged sector, and its neutral scalar records are short-ranged, open PR #8918)",
                  "continuum bridge (unproved; on the computed prisms the uniform ice flux behaves as one massless Gaussian lattice field with its stiffness fixed by the unit link field and lattice-Coulomb test charges, PRs #8859 and #8864, landed, and open PRs #8869, #8871, #8875; on tori to side 24 the long-wavelength stiffness is c = 0.335, within 0.5% of the sum-rule 1/3, with two degenerate polarizations, open PRs #8881, #8890; test-defect pairs follow the Green function on tori out to r = 8, open PR #8913, and the charge-squared law, open PR #8951; the photon is nonlinear at finite flux, open PRs #8928, #8949; its near-Gaussian form is three-dimensional, square ice missing the sum rule by 4.6%, open PR #8930)"],
    "T_RECORD_DYNAMICS": ["photon dynamics rests on the landed quantum Hamiltonian (supplied bridge; the equal-time law is selected by a positive static rule, PR #8698, landed; linear sweep rules move flux by a linear transfer, damped when strictly positive and rigid for permutations, with mixed cases beyond both, PR #8726, landed; at the RK point of the supplied Hamiltonian the single-mode bound is quadratic, 2 n_f K |s|^2 with 2 n_f K = 0.346, open PR #8905)",
                          "defect densities of front-like order laws on large windows (not computed)",
                          "first-formation orders beyond corner growth, broadcast and the designed order (not classified)",
                          "exact formation of the uniform ice measure by layer units with an infinite cross-section, or by single sites on planar windows beyond five squares or three-dimensional windows beyond two cubes (single sites not searched; finite cell units fail around blocks and chains of units work, PR #8720, landed; layer units are exact on every infinite prism in the zero-flux sector, PR #8740, landed, and their law is local transfer times the Gaussian vacuum functional, within 0.24% on the 4 x 4 prism, whose kernel is a 1/r flux interaction in the layer, open PR #8896; no planar window of two to five squares and no pair of adjacent cubes admits a single-site order, PRs #8715, #8719, #8735, landed)"],
    "T_MATTER": ["record/role bridge to physical fermions (unconstructed, per the support-rule note)"],
}
TARGET_BRIEF = ["formation law", "possibility domain and menus", "handedness", "Born weights", "readability",
                "clock/rate", "formation unit", "record dynamics", "matter/composition",
                "support/gauge structure", "downstream gravity"]
PARENTS = {}
for u, v in EDGES:
    PARENTS.setdefault(v, []).append(u)


def minimise(fam):
    fam = {frozenset(s) for s in fam}
    return {s for s in fam if not any(t < s for t in fam)}


def decision_sets(node, memo=None, parents=None):
    """Minimal decision sets under AND (results, routes, targets) and OR (choices)."""
    memo = {} if memo is None else memo
    parents = PARENTS if parents is None else parents
    if node in memo:
        return memo[node]
    kind = NODES[node][0]
    if kind == "decision":
        out = {frozenset([node])}
    elif kind == "choice":
        out = set()
        for p in parents.get(node, ()):
            out |= decision_sets(p, memo, parents)
        out = minimise(out)
    else:
        out = {frozenset()}
        for p in parents.get(node, ()):
            out = minimise({a | b for a in out for b in decision_sets(p, memo, parents)})
    memo[node] = out
    return out


def topo_order(nodes, parents):
    order, seen, done = [], set(), set()

    def visit(n):
        if n in done:
            return True
        if n in seen:
            return False
        seen.add(n)
        for p in parents.get(n, ()):
            if not visit(p):
                return False
        done.add(n)
        order.append(n)
        return True
    try:
        ok = all(visit(n) for n in nodes)
    except RecursionError:
        return False, order
    return ok, order


print("== 1. Well-formedness and source linking ==")
kinds = {k: sum(1 for n, (kk, p) in NODES.items() if kk == k) for k in ("source", L, OP, "decision", "choice", "route", "target")}
check("node ledger: 2 sources, 61 landed, 13 open, 12 decision groups, 6 choices, 8 routes, 11 targets",
      kinds == {"source": 2, L: 61, OP: 13, "decision": 12, "choice": 6, "route": 8, "target": 11} and len(NODES) == 113)
check("every edge endpoint is declared; no edge enters a source or a decision; target edges go to targets",
      all(u in NODES and v in NODES for u, v in EDGES)
      and all(NODES[v][0] not in ("source", "decision") for u, v in EDGES)
      and all(NODES[v][0] == "target" for u, v in EDGES if NODES[u][0] == "target"))
check("every landed node's provenance is a note path present on this revision of the repository",
      all(p.startswith(D) and os.path.exists(p) for n, (k, p) in NODES.items() if k == L))
check("every open node names a campaign pull request; the withdrawn locality group is absent",
      all(p.startswith("open PR #8") for n, (k, p) in NODES.items() if k == OP) and "DEC_LOCALITY" not in NODES)
check("decision groups carry >= 2 recorded candidates; the order-law group no longer lists an order-blind rule",
      set(CANDIDATES) == {n for n, (k, p) in NODES.items() if k == "decision"}
      and all(len(c) >= 2 for c in CANDIDATES.values())
      and not any("order-blind physical rule" in c for c in CANDIDATES["DEC_ORDER_LAW"]),
      f"{sum(len(c) for c in CANDIDATES.values())} recorded candidate clauses in 12 groups")
check("the eleven targets are exactly the design note's preserved list",
      [NODES[n][1].replace("design note: ", "") for n in NODES if NODES[n][0] == "target"] == TARGET_BRIEF)

print()
print("== 2. Acyclicity and minimal decision sets ==")
ACYC, ORD = topo_order(list(NODES), PARENTS)
check("the graph is acyclic over all 113 nodes, and the same sorter rejects a two-node cycle",
      ACYC and len(ORD) == 113 and topo_order(("a", "b"), {"a": ["b"], "b": ["a"]})[0] is False)
SETS = {t: decision_sets(t) for t in NODES if NODES[t][0] == "target"}
fmt = lambda fam: " | ".join(sorted("{" + ",".join(sorted(x.replace("DEC_", "") for x in s)) + "}" for s in fam))
EXPECT_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"})}
check("gravity has exactly four minimal decision sets: every formation set holds the order law, every static set the reading",
      SETS["T_GRAVITY"] == EXPECT_GRAVITY
      and all(("DEC_ORDER_LAW" in s) != ("DEC_READING" in s) for s in SETS["T_GRAVITY"]), fmt(SETS["T_GRAVITY"]))
NOLAYER = {k: [q for q in v if not (k == "JOINT_UNIT_ROUTE" and q == "DEC_ORDER_LAW")] for k, v in PARENTS.items()}
SEVENTH_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without the layer order, gravity's sets return to the seventh edition's",
      decision_sets("T_GRAVITY", parents=NOLAYER) == SEVENTH_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOLAYER)))
check("single-site formation of the uniform measure needs plan letters, so soldering with an order law alone no longer reaches gravity",
      decision_sets("SINGLE_SITE_ROUTE") == {frozenset({"DEC_ORDER_LAW", "DEC_ALPHABET"})}
      and frozenset({"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"}) not in SETS["T_GRAVITY"],
      "single-site route: " + fmt(decision_sets("SINGLE_SITE_ROUTE")))
NOPLAN = {k: [q for q in v if not (k == "SINGLE_SITE_ROUTE" and q == "DEC_ALPHABET")] for k, v in NOLAYER.items()}
SIXTH_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without the layer order and the plan letters, gravity's sets return to the sixth edition's five",
      decision_sets("T_GRAVITY", parents=NOPLAN) == SIXTH_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOPLAN)))
check("every minimal set of gravity contains a frame source: soldering or the alphabet",
      all("DEC_SOLDER" in s or "DEC_ALPHABET" in s for s in SETS["T_GRAVITY"]),
      "the static route's supplied Hamiltonian remains an open edge")
NOSTAT = {k: [q for q in v if q not in ("STATIC_ICE_RECORDS", "STATIC_FRAME_SOURCE", "ROLES_STATIC_LETTERS", "ROLES_PAIR_LETTERS")]
          for k, v in NOPLAN.items()}
OLD_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without those and the static frame source, gravity's sets return to the third edition's",
      decision_sets("T_GRAVITY", parents=NOSTAT) == OLD_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOSTAT)))
PC = {k: list(v) for k, v in PARENTS.items()}
PC["LETTER_SCHEME"] = []
PC["ROLES_SOURCE"] = [p for p in PARENTS["ROLES_SOURCE"] if p not in ("ROLES_REGISTERED", "ROLES_STATIC_LETTERS")]
PC_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_READING"}, {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_ALPHABET", "DEC_ORDER_LAW", "DEC_ROLES", "DEC_SOLDER"})}
check("control: with relational letters only, as under possibility covariance, gravity's one unsoldered minimal set is {alphabet, reading}",
      decision_sets("T_GRAVITY", parents=PC) == PC_GRAVITY
      and {s for s in PC_GRAVITY if "DEC_SOLDER" not in s} == {frozenset({"DEC_ALPHABET", "DEC_READING"})},
      fmt(decision_sets("T_GRAVITY", parents=PC)) + "; fixed letters are unavailable and relational letters have no first "
      "formation (PRs 8691, 8731, landed), so the letter scheme is empty; registered roles need fixed parity letters, and "
      "relational letters record the role pattern: pairs away from the side-4 torus (PR #8750, landed), four-angle cycles on it "
      "(PR #8752, landed)")
PC0 = {k: list(v) for k, v in PC.items()}
PC0["ROLES_SOURCE"] = [p for p in PC["ROLES_SOURCE"] if p != "ROLES_PAIR_LETTERS"]
PC0_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_ALPHABET", "DEC_ORDER_LAW", "DEC_ROLES", "DEC_SOLDER"})}
check("control: with single-angle relational letters only, the unsoldered set is {alphabet, reading, roles}",
      decision_sets("T_GRAVITY", parents=PC0) == PC0_GRAVITY,
      fmt(decision_sets("T_GRAVITY", parents=PC0)) + "; a single-angle static record carries no role pattern (PR #8743, landed)")
check("record dynamics: a frame source in every set (static or formed; soldering or letters)",
      SETS["T_RECORD_DYNAMICS"] == {frozenset({"DEC_READING", "DEC_SOLDER"}), frozenset({"DEC_READING", "DEC_ALPHABET"}),
                                    frozenset({"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW"}), frozenset({"DEC_ALPHABET", "DEC_ORDER_LAW"})},
      fmt(SETS["T_RECORD_DYNAMICS"]))
check("gauge: supplied roles, or roles read from coordinate letters under formation or the static reading",
      SETS["T_GAUGE"] == {frozenset({"DEC_ROLES"}), frozenset({"DEC_ALPHABET", "DEC_ORDER_LAW"}),
                          frozenset({"DEC_ALPHABET", "DEC_READING"})},
      fmt(SETS["T_GAUGE"]))
check("the formed photon route passes through the coordinator result; directed ice feeds record dynamics; letters are fixed or relational",
      "UNIFORM_ICE_COORDINATION" in PARENTS["FORMED_ICE_ROUTE"] and "DIRECTED_ICE" in PARENTS["T_RECORD_DYNAMICS"]
      and set(PARENTS["LETTER_SCHEME"]) == {"FRAME_REGISTRATION", "RELATIONAL_FRAMES"}
      and NODES["LETTER_SCHEME"][0] == "choice"
      and "COULOMB_SELECTION" in PARENTS["STATIC_ICE_ROUTE"] and "FLUX_TRANSPORT" in PARENTS["T_RECORD_DYNAMICS"]
      and {"TWO_SQUARES_NO_ORDER", "TWO_CUBES_NO_ORDER", "DEC_ALPHABET", "DEC_ORDER_LAW"} <= set(PARENTS["SINGLE_SITE_ROUTE"])
      and "SPIRAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"] and "JOINT_CELL_UNITS" in PARENTS["JOINT_UNIT_ROUTE"]
      and "DEC_ORDER_LAW" in PARENTS["JOINT_UNIT_ROUTE"] and "STATIC_SPIRAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"]
      and "FINITE_RELATIONAL_LETTERS" in PARENTS["RELATIONAL_FRAMES"] and "TORUS_NO_ORDER" in PARENTS["SINGLE_SITE_ROUTE"]
      and "LINEAR_SWEEP_TRANSPORT" in PARENTS["T_RECORD_DYNAMICS"] and "POLYOMINO_NO_ORDER" in PARENTS["SINGLE_SITE_ROUTE"]
      and "UNIT_FAIR_COIN" in PARENTS["RELATIONAL_FRAMES"] and "STATIC_GLOBAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"]
      and "LAYER_UNITS_PRISMS" in PARENTS["JOINT_UNIT_ROUTE"] and "GLOBAL_OCTANT" in PARENTS["RELATIONAL_FRAMES"]
      and "FLUX_STIFFNESS" in PARENTS["JOINT_UNIT_ROUTE"] and "PAIR_LETTER_ROLES" in PARENTS["ROLES_PAIR_LETTERS"]
      and "CYCLE_LETTER_ROLES" in PARENTS["ROLES_PAIR_LETTERS"] and "SWEEP_NO_ROLES" in PARENTS["ROLES_PAIR_LETTERS"]
      and all(n in PARENTS["ROLES_PAIR_LETTERS"] for n in ("OCTANT_RECORDED", "FOLDED_ROLES", "GENERIC_LETTERS")),
      "the window results carry plan letters into single-site formation, the unit results carry the layer order into joint units, and the spiral, letter and multi-qubit unit results join the relational letters")
PHOTON_LANE = ("ROW_TRANSFER_SQUARE", "GAPLESS_CHAIN", "MASSLESS_BRANCH", "ONE_STIFFNESS", "TEST_DEFECT_COULOMB",
               "WINDING_STIFFNESS", "TWO_POLARIZATIONS", "LAYER_VACUUM", "RK_SOFT_PHOTON", "WORM_DEFECT_PAIRS",
               "NONLINEAR_PHOTON", "DIMENSION_CONTRAST", "FLUX_QUANTA_SHIFT", "CHARGE_SQUARED")
NOPH = {k: [q for q in v if q not in PHOTON_LANE] for k, v in PARENTS.items()}
check("the photon-lane results feed record dynamics only and change no minimal set",
      all([v for u, v in EDGES if u == n] == ["T_RECORD_DYNAMICS"] for n in PHOTON_LANE)
      and all(decision_sets(t, parents=NOPH) == SETS[t] for t in SETS),
      "a massless Gaussian lattice field with a fixed stiffness and lattice-Coulomb test charges on the computed prisms supports the photon route without adding a decision")
NOSEAM = {k: [q for q in v if q != "GREEN_CHARGED_SECTOR"] for k, v in PARENTS.items()}
check("the seam result feeds gravity only and changes no minimal set",
      [v for u, v in EDGES if u == "GREEN_CHARGED_SECTOR"] == ["T_GRAVITY"]
      and all(decision_sets(t, parents=NOSEAM) == SETS[t] for t in SETS),
      "uniform ice carries the Green function only in its charged sector; gravity's scalar input is not among its neutral records")
check("formation law {rule, order law}; clock/rate {order law}; no target is decision-free",
      SETS["T_FORMATION_LAW"] == {frozenset({"DEC_RULE", "DEC_ORDER_LAW"})}
      and SETS["T_CLOCK_RATE"] == {frozenset({"DEC_ORDER_LAW"})}
      and all(frozenset() not in fam for fam in SETS.values()))
check("every decision group appears in some target's minimal sets; open edges are declared",
      {d for fam in SETS.values() for s in fam for d in s} == {n for n in NODES if NODES[n][0] == "decision"}
      and sum(len(v) for v in OPEN_EDGES.values()) == 7)

print()
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
