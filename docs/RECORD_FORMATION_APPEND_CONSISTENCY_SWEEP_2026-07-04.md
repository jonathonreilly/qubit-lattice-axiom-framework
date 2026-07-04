# Record Formation Consistency Sweep - 2026-07-04

Scope: classified the 182 files present in `INPUT_grep_hits.txt` and the 27 trimmed rows present in `INPUT_ledger_rows.json`. Counts below are for those input files/rows only; `docs/audit/data/axiom_premise_nodes.json` is listed as a known consequential mirror re-key but is not part of the 182-file input set.

## File Bucket Counts

| Bucket | Count |
|---|---:|
| FLIPS-VERDICT | 17 |
| RE-KEY | 10 |
| DISCLAIMER-TRUE | 136 |
| HISTORICAL | 9 |
| UNAFFECTED | 10 |
| NEEDS-SUPERVISOR | 0 |

## Ledger Row Bucket Counts

| Bucket | Count |
|---|---:|
| FLIPS-VERDICT | 1 |
| RE-KEY | 0 |
| DISCLAIMER-TRUE | 6 |
| HISTORICAL | 0 |
| UNAFFECTED | 20 |
| NEEDS-SUPERVISOR | 0 |

## FLIPS-VERDICT

1. `docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`
   - Flips: "The claim "Lattice, Quantum, and Record force record formation" does **not** hold unconditionally."
   - New statement: The direct no-go no longer holds as stated: the axioms would force occurrence-as-fact; the residual must narrow to formation rule/process/state/site/weight.
2. `scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py`
   - Flips: "VERDICT: record formation is NOT unconditionally forced by the Lattice/Quantum/Record baseline."
   - New statement: The runner target flips; it should test that rule/process/state/site/weight are not forced, not that occurrence itself is absent.
3. `docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md`
   - Flips: "Formally this is not a theorem: the empty history satisfies the axioms vacuously and carries no arrow (checked)."
   - New statement: Empty-history admissibility no longer follows if Records form; remaining residuals are low-entropy/single-chain/finite-history content and the specific realized formation rule.
4. `scripts/frontier_past_hypothesis_existence_reduction_append_only_2026_06_11.py`
   - Flips: "T5c the EMPTY history (w = epsilon) is structurally valid and carries no arrow -- non-emptiness ('at least one record is registered') is the explicit residual PRECONDITION, strictly weaker than any specialness claim and not derived here: formally vacuous-model-allowed, no-arrow when empty"
   - New statement: The non-emptiness residual is no longer a generic axiom gap; the check must be narrowed to special boundary/realized-history content.
5. `docs/SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
   - Flips: "record formation is not forced (retained_no_go): 'at least one record exists' is NOT an axiom consequence, so no axis can be derived from it unconditionally"
   - New statement: Record existence becomes an axiom consequence; the no-go can still rest on missing time metric, rate, and registration-direction bridge.
6. `scripts/single_clock_axis_selection_check_2026_06_11.py`
   - Flips: "record formation is not forced (retained_no_go): 'at least one record exists' is NOT an axiom consequence, so no axis can be derived from it unconditionally"
   - New statement: The runner check should stop using non-existence as an axis obstacle and keep the axis/rate bridge obstacle.
7. `docs/OBSERVABLE_PRINCIPLE_P1_REGISTRATION_REALIZATION_PIN_CONSOLIDATION_NARROW_THEOREM_NOTE_2026-06-11.md`
   - Flips: "Record formation is not unconditionally forced | RR conditions on realization, does not force formation"
   - New statement: Generic occurrence is supplied; RR remains conditional only because the specific realization clause, record pattern, and clock window are still supplied.
8. `docs/RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md`
   - Flips: "record occurrence is derived from the axioms;"
   - New statement: The note can no longer use generic occurrence derivation as the forbidden overclaim; it should disclaim the activation probability, selection law, IID protocol, clock/rate, and every-trial/site occurrence.
9. `scripts/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.py`
   - Flips: "therefore record occurrence is derived"
   - New statement: The banned-string guard must be re-keyed or narrowed: generic occurrence is axiomatic, but the sparse IID occurrence kernel is not.
10. `docs/RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md`
   - Flips: "Record formation is **not unconditionally forced** by the axioms"
   - New statement: Generic formation is forced by the append; the note should say the specific instrument, strength, schedule, and rate are named admissions.
11. `scripts/frontier_record_instrument_composite_link_erasure_slaving_2026_06_09.py`
   - Flips: "Record formation is NOT unconditionally forced by the axioms"
   - New statement: Same narrowing as the source note: occurrence is supplied, but the flanking instruments and their parameters remain admitted.
12. `docs/RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md`
   - Flips: "Record formation is **not unconditionally forced** by the axioms"
   - New statement: Generic formation is supplied; the conditional theorem still admits the concrete instrument, rate, and background V.
13. `scripts/frontier_record_local_finite_atom_availability_2026_06_17.py`
   - Flips: "A5 retained no-go boundary keeps record formation unforced"
   - New statement: The dependency check should target unsupplied production/realization dynamics, not unforced occurrence.
14. `docs/COLOR_DEPOLARIZATION_SINGLE_FRAME_DEPHASING_INSUFFICIENCY_AND_MULTIFRAME_EXHIBIT_NARROW_THEOREM_NOTE_2026-06-09.md`
   - Flips: "records that record formation and instrument choice are not forced by the minimal axioms."
   - New statement: After the append, only the instrument choice, averaging weight, normalization, and rate remain unforced.
15. `scripts/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.py`
   - Flips: "record formation is not unconditionally forced (retained_no_go)."
   - New statement: After the append, this runner should say multi-frame/instrument admission is not forced; occurrence itself is.
16. `docs/COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`
   - Flips: "record formation and frame/instrument choice are not forced by the minimal axioms."
   - New statement: After the append, the frame/instrument choice remains open, while generic record formation does not.
17. `docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md`
   - Flips: "it "does not unconditionally force record formation"."
   - New statement: The theorem still conditions on a specified K1 neighbor-conditioned record stack, but the old generic-formation no-go citation must be narrowed.

## RE-KEY

- `docs/MINIMAL_AXIOMS_2026-06-29.md`: Record section opening: add `Records form.` as the opening paragraph.
- `docs/MINIMAL_AXIOMS_2026-06-29.md`: `context selection, measurement basis selection, Born weights, probability rules, update laws, decoherence mechanisms, and occurrence rules;`
- `docs/audit/data/axiom_premise_nodes.json`: Non-input consequential mirror: record clause gains `records form;` and `occurrence rule` becomes the new formation-rule wording.
- `docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md`: `It still supplies no context-selection rule, occurrence rule, weighting,`
- `docs/audit/AXIOM_MINIMALITY_POLICY.md`: `provide an occurrence rule, define probabilities,`
- `docs/audit/AXIOM_MINIMALITY_POLICY.md`: `normalization, probability, occurrence rule, update law,`
- `docs/audit/AXIOM_RESET_IMPACT_2026-06-29.md`: `probability, Born weights, occurrence rules, or update laws;`
- `docs/GENERATION_MODULI_SELECTOR_EXACT_CONSTRAINTS_BOUNDED_NOTE_2026-07-02.md`: `update laws, occurrence rules, source/action identification, P2/modulus`
- `docs/SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md`: `rules, update laws, decoherence mechanisms, and occurrence rules;`
- `docs/ai_methodology/skills/physics-loop/SKILL.md`: `persistence dynamics, occurrence rule, update law, time metric, within-sector`
- `docs/ai_methodology/skills/review-loop/SKILL.md`: `persistence dynamics, occurrence rules, update laws, time metric,`
- `scripts/audit_companion_minimal_axioms_clean_base_exact.py`: `does not import context selection, occurrence rules, sector generation,`
- `scripts/audit_companion_minimal_axioms_clean_base_exact.py`: `provide an occurrence rule, define probabilities`
- `scripts/audit_companion_minimal_axioms_clean_base_exact.py`: `Open gates outside axioms include context selection and occurrence rules`
- `scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py`: `It still supplies no context-selection rule, occurrence rule, weighting, normalization, probability, update law, measurement/decoherence dynamics, K/CPT structure, central-sector decomposition, source/action bridge, physical observable bridge, state-selection rule, law-domain derivation, or downstream theory consequence`

## NEEDS-SUPERVISOR

None.

## Appendix: Files

| File | Bucket | Justification |
|---|---|---|
| `docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; hit does not bear on the proposed Record-axiom append |
| `docs/ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md` | RE-KEY | classified from hit lines; exact old "occurrence rule" exclusion should become the new formation-rule wording |
| `docs/ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/ACPHILAMBDA_K1_STAGGERED_K_BLINDNESS_REAL_LIFT_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/ARROW_CPT_ORIENTATION_DO_NOT_SOURCE_CP_ODD_ACTION_COEFFICIENTS_NO_GO_NOTE_2026-06-08.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/AXIOM_CHANGE_PROPOSAL_2026-04-10.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/CHANNEL_SURFACE_CN_GROUNDING_PERIPHERAL_UNITARY_SUMMAND_BOUNDED_THEOREM_NOTE_2026-06-11.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/COLOR_DEPOLARIZATION_SINGLE_FRAME_DEPHASING_INSUFFICIENCY_AND_MULTIFRAME_EXHIBIT_NARROW_THEOREM_NOTE_2026-06-09.md` | FLIPS-VERDICT | scope citation says record formation and instrument choice are not forced; after append only instrument/weight/rate remain unsupplied |
| `docs/COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md` | FLIPS-VERDICT | scope citation says record formation and frame/instrument choice are not forced; after append only frame/instrument choice remains open |
| `docs/COLOR_SU3_RESTRICTED_TRANSPORT_PROFILE_2026-06-05.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/DECOHERENCE_DECISION_NOTE.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS_2026-06-02.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/GAUGE_WILSON_ISOTROPY_BOUNDARY_HYGIENE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/GENERATION_MODULI_SELECTOR_EXACT_CONSTRAINTS_BOUNDED_NOTE_2026-07-02.md` | RE-KEY | classified from hit lines; open-gates echo contains "occurrence rules" |
| `docs/GENERATION_PRIOR_STABILITY_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/LITERATURE_POSITIONING_NOTE.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/MINIMAL_AXIOMS_2026-06-04.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/MINIMAL_AXIOMS_2026-06-05.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | RE-KEY | Record section opening and open-gates occurrence-rules bullet are the source text being tested |
| `docs/N5_SINGLE_GENERATOR_CLOCK_EXCHANGE_INVARIANCE_NARROW_NO_GO_NOTE_2026-06-17.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/OBSERVABLE_PRINCIPLE_P1_REGISTRATION_REALIZATION_PIN_CONSOLIDATION_NARROW_THEOREM_NOTE_2026-06-11.md` | FLIPS-VERDICT | uses the retained no-go that RR does not force formation and that the realization class may be empty; append supplies occurrence-as-fact but not RR |
| `docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md` | DISCLAIMER-TRUE | classified from hit lines; formation rule remains unsupplied under the tested append |
| `docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md` | FLIPS-VERDICT | non-emptiness/at-least-one-record is named as non-derived residual; append supplies generic occurrence |
| `docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/POST_RECORD_PERSISTENT_RECORD_PRODUCTION_BRIDGE_PROTOTYPE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/POST_RECORD_TRANSITION_KERNEL_INTERFACE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md` | FLIPS-VERDICT | quotes the old no-go title and says it does not force formation; after append the specific K1 record stack remains supplied but generic occurrence is no longer open |
| `docs/RECORD_AXIOM_AUDIT_APPLICATION_MAP_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_COMPOSITION_BRIDGE_SEMIGROUP_POSITIVITY_SELECTION_BOUNDED_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_COUNT_BOUNDS_COMPOSITION_WORDS_FINITE_DIAL_BOUNDED_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md` | FLIPS-VERDICT | admission rationale says record formation is not forced; append leaves the named instrument/rate/V admitted but not generic occurrence |
| `docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_EQUAL_LETTER_STABLE_LOCATION_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md` | FLIPS-VERDICT | direct no-go says Lattice/Quantum/Record do not force record formation; append explicitly supplies that occurrence fact |
| `docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md` | FLIPS-VERDICT | admission rationale says record formation is not forced; append leaves which instrument/strength/schedule unsupplied but not generic occurrence |
| `docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md` | FLIPS-VERDICT | non-claim excludes record occurrence from axioms; append supplies generic occurrence, while activation/selection/IID remain supplied |
| `docs/RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_POINTER_CONTROLLED_COUPLING_FINITE_EXAMPLE_BOUNDED_THEOREM_NOTE_2026-06-15.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_SELECTOR_AUDIT_SIDECAR_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_TYPING_AUDIT_UNLOCK_MAP_2026-06-05.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md` | FLIPS-VERDICT | route A says at least one record is not an axiom consequence; append makes record occurrence an axiom consequence while axis/rate stay open |
| `docs/SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/STACK_SPECTRAL_TRANSCRIPTION_WEAK_REGISTRATION_FAITHFUL_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-11.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md` | RE-KEY | classified from hit lines; copied open-gates bullet contains "occurrence rules" |
| `docs/TELEPORTATION_FINITE_GAPPED_PREPARATION_PATH_SUPPORT_NOTE_2026-06-16.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/TELEPORTATION_NOISE_FAULT_CONTROLS_NOTE.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/THERMODYNAMIC_PH_QUANTITATIVE_CLAUSE_RECORD_BUDGET_LEDGER_BOUNDED_THEOREM_NOTE_2026-06-11.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md` | DISCLAIMER-TRUE | classified from hit lines; specific occurrence on this surface/step/lane remains unclaimed because which/where/weight are unsupplied |
| `docs/UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_HYGIENE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/YT_ZERO_IMPORT_BOUNDARY_RATIO_AUTHORITY_THEOREM_NOTE_2026-05-17.md` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `docs/ai_methodology/raw/prompts_session_1e4222c2_jonreilly.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/ai_methodology/raw/protocols.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/ai_methodology/raw/science_scaffolding.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/ai_methodology/skills/audit-loop/SKILL.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/ai_methodology/skills/physics-loop/SKILL.md` | RE-KEY | classified from hit lines; skill guardrail contains old "occurrence rule" wording |
| `docs/ai_methodology/skills/review-loop/SKILL.md` | RE-KEY | classified from hit lines; skill guardrail contains old "occurrence rules" wording |
| `docs/audit/AUDIT_LEDGER.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/audit/AXIOM_MINIMALITY_POLICY.md` | RE-KEY | policy text contains old occurrence-rule no-laundering language that should be re-keyed to formation rules |
| `docs/audit/AXIOM_RESET_IMPACT_2026-06-29.md` | RE-KEY | classified from hit lines; reset impact open-gate list contains "occurrence rules" |
| `docs/lanes/open_science/07_THERMALIZATION_KINETIC_THEORY_OPEN_LANE_2026-06-12.md` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `docs/work_history/repo/backlog/NATURE_BACKLOG_2026-04-10.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `docs/work_history/repo/backlog/REVIEW_HARDENING_BACKLOG.md` | HISTORICAL | classified from hit lines; pre-reset, archived, or superseded material; no live verdict change |
| `scripts/audit_companion_busch_povm_extension_deps_changed_hygiene_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_luders_rule_from_composition_consistency_deps_changed_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_minimal_axioms_clean_base_exact.py` | RE-KEY | runner needles old occurrence-rule/open-gate strings and will need mechanical string updates |
| `scripts/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_quark_lane3_bounded_companion_retention_firewall_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.py` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `scripts/audit_companion_yt_primitive_unit_source_action_physical_premise_no_go_hygiene_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `scripts/audit_companion_yt_ward_record_axiom_invariance_2026_06_04.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/born_rule_framework_bridge_check.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/channel_surface_cn_grounding_peripheral_summand_2026_06_11.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/emergent_barrier.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/frontier_arrow_from_record_formation_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_chirality_record_typing_interface_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.py` | FLIPS-VERDICT | runner prose uses old no-go to make every frame a named admission; append narrows that admission to instrument/weight/rate |
| `scripts/frontier_color_su3_restricted_transport_profile_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_dynamics_form_from_record_preservation_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/frontier_dynamics_sort_records_accumulate_2026_07_03.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_past_hypothesis_existence_reduction_append_only_2026_06_11.py` | FLIPS-VERDICT | runner check makes non-emptiness an explicit residual precondition; append supplies generic record occurrence |
| `scripts/frontier_post_record_arrow_orientation_firewall_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_post_record_clock_rate_interface_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_post_record_count_probability_firewall_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/frontier_post_record_persistent_record_production_bridge_prototype_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py` | RE-KEY | classified from hit lines; string needle contains old "occurrence rule" wording |
| `scripts/frontier_record_audit_application_map_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_composition_bridge_positivity_2026_07_02.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_count_bounds_composition_words_2026_07_02.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_dynamics_audit_gate_ladder_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_finite_alphabet_post_record_dynamics_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_formation_dynamics_constraint_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py` | FLIPS-VERDICT | runner verdict is the direct unconditional-formation no-go; append invalidates that target verdict |
| `scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/frontier_record_iid_typicality_firewall_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_instrument_composite_link_erasure_slaving_2026_06_09.py` | FLIPS-VERDICT | runner docstring says formation is not forced so every record instrument is admitted; append narrows the admission to specific instrument details |
| `scripts/frontier_record_instrument_kernel_interface_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_local_finite_atom_availability_2026_06_17.py` | FLIPS-VERDICT | runner check requires old no-go text that record formation remains unforced; append changes the target boundary |
| `scripts/frontier_record_markov_generator_embeddability_boundary_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_markov_generator_premise_classifier_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_production_interface_principle_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_production_kernel_boundary_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_production_residual_checklist_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_reset_sink_entropy_ledger_2026_06_05.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_record_unbounded_additivity_schema_2026_06_06.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/frontier_sm_gstar_higgs_sector_count_2026_05_29.py` | UNAFFECTED | classified from hit lines; hit is incidental or a different sense of occurrence/record, not the Record-axiom formation issue |
| `scripts/frontier_thermodynamic_ph_record_budget_ledger_2026_06_11.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/interference_decoherence_via_delay.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/interference_geometry_sweep.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/model_axiom_audit.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/observable_principle_p1_rr_consolidation_check_2026_06_11.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/realized_kinetic_branch_conditional_record_registration_2026_07_02.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/record_density_slows_lr_front_optical_metric_toy_2026_06_09.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/record_occurrence_thinned_iid_frequency_bridge_2026_07_01.py` | FLIPS-VERDICT | runner banned-string guard treats derived record occurrence as an overclaim; append makes generic occurrence axiomatic but not the sparse IID kernel |
| `scripts/record_pointer_controlled_coupling_finite_example_2026_06_15.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |
| `scripts/single_clock_axis_selection_check_2026_06_11.py` | FLIPS-VERDICT | runner check says at least one record is not an axiom consequence; append supplies occurrence but not axis/time metric |
| `scripts/stack_spectral_transcription_weak_registration_2026_06_11.py` | DISCLAIMER-TRUE | classified from hit lines; process/dynamics/production remains explicitly unsupplied after the append |
| `scripts/teleportation_finite_gapped_preparation_path_support_2026_06_16.py` | DISCLAIMER-TRUE | classified from hit lines; model-specific or conditional record-formation language, not a claim that the axioms supply the rule/process |

## Appendix: Ledger Rows

| Claim ID | Bucket | Justification |
|---|---|---|
| `acphilambda_occurrence_clock_composition_delta_blindness_2026-07-02` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `acphilambda_species_bridge_realized_state_decomposition_note_2026-06-11` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `arrow_from_record_formation_past_hypothesis_residual_note_2026-06-05` | DISCLAIMER-TRUE | trimmed scope admits past-hypothesis residual, not record-production process; append does not supply the boundary condition |
| `darwinism_bridge_residual_local_observability_open_gate_note_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_note_2026-06-07` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `koide_review_guard_note_2026-04-24` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `persistent_record_as_kraus_operator_note_2026-05-20` | DISCLAIMER-TRUE | trimmed chain excludes deriving W from persistent-record dynamics, still unsupplied |
| `post_record_persistent_record_production_bridge_prototype_2026-06-06` | DISCLAIMER-TRUE | trimmed scope says supplied bridge, not derivation of production law/kernel |
| `post_record_production_dynamics_needed_row_map_2026-06-06` | DISCLAIMER-TRUE | trimmed meta scope maps rows and makes no dynamics claim |
| `record_dephasing_broadcast_interface_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_dynamics_audit_gate_ladder_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_dynamics_koide_dial_firewall_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_formation_controlled_copy_write_isometry_theorem_note_2026-06-18` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06` | FLIPS-VERDICT | trimmed row title/no-go says minimal axioms do not unconditionally force record formation; append supplies occurrence-as-fact |
| `record_formation_pointer_non_demolition_dynamics_constraint_bounded_theorem_note_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_formation_to_kraus_isometry_bridge_2026-06-06` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_local_observability_decoder_criterion_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_occurrence_thinned_iid_frequency_bridge_2026-07-01` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_pointer_broadcast_circuit_interface_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_prerecord_instrument_kernel_gate_2026-06-06` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_production_interface_principle_2026-06-06` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_production_kernel_boundary_2026-06-06` | DISCLAIMER-TRUE | trimmed scope says grammar does not determine production kernel/law/rate/prior; append supplies none |
| `record_production_residual_checklist_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_selective_instrument_atom_criterion_2026-06-05` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `record_unbounded_finite_additivity_schema_2026-06-06` | DISCLAIMER-TRUE | trimmed scope says it does not derive record production, still true |
| `stack_spectral_transcription_weak_registration_faithful_limit_bounded_theorem_note_2026-06-11` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
| `teleportation_measurement_record_note` | UNAFFECTED | classified from trimmed fields only; metadata/path wording has no supplied-vs-unsupplied occurrence claim |
