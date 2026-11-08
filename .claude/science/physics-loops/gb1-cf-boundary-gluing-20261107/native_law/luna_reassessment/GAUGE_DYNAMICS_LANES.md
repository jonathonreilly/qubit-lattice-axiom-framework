# Gauge, dynamics, circuit, and finite-range lane triage

## Scope and source identity

This is a read-only triage of the GAUGE / DYNAMICS / CIRCUIT / finite-range implementation lanes, excluding record-law lanes and the new GB1-CF branch proofs as requested. It is not an audit verdict or a new theory.

- Pinned main source: f5af11cd0102cfd0b51aef0911f600130bf5beb1 (all main citations below use this revision; blob SHAs identify the cited file bytes).
- Assigned worktree: branch physics-loop/gb1-cf-pair-20261107, HEAD 985f174411be88e0cb7e826f0df8f2ad3c16ea35.
- The pinned Admissibility text is at docs/MINIMAL_AXIOMS_2026-06-29.md:55-62 (blob bc23300becfe4e4db57153c0e94cfcdf2338da71); its premise-node entry is docs/audit/data/axiom_premise_nodes.json:11-25 (blob b93959cca4f7e26c673cdccbe601e50c3cb93daa). The authorized two-phrase replacement would remove the explicit nearest-neighbor restriction on the Admissibility distribution's dependence. It does not specify a dynamics law, gate set, tick, Hamiltonian, probability values, or intermediate-state constraint.
- Six docs added on the current GB1-CF branch relative to the pin were excluded as findings. They are the SU2_*2026-11-07/08 notes and scope checks, including the neighborhood-propagation/record-readout files.

**Triage result:** zero confirmed narrow source issues in this slice. Two lead-verification candidates below are places a downstream consumer could overread; neither cited source itself makes the broader inference. Conditional nearest-neighbor results remain valid on their stated hypotheses, and broadening Admissibility does not make them false.

## Lead-verification candidates

### 1. Graph-Dirac requirements could be read as a universal implementation gate

**Grade:** lead-verification candidate; no source error confirmed.

**Source:** docs/GRAPH_DIRAC_REQUIREMENTS_2026-04-10.md:20-38,126-141,169-181,215-226; pinned-main commit f5af11cd0102cfd0b51aef0911f600130bf5beb1, file blob da9dd754cd1391c437d0a8b8163a12bf79e24e7c.

**Restrictive assumption and inference:** This requirements memo is for preserving the retained staggered operator on candidate graph families. It assumes nearest-neighbor hopping/stepwise transport (:22-25,91-95), says the transport law must be “nearest-neighbor or uniformly local” (:126-135), and marks graphs whose edges destroy nearest-neighbor locality incompatible with that operator (:169-181); its future-harness checklist asks whether the update stays nearest-neighbor (:215-226). Read narrowly, this excludes graph families that fail the retained operator's locality, orientation, or parity conditions. It does not establish that every physical update or circuit must be a single hop. The explicit “or uniformly local” already leaves a finite-range route open, though the note does not define that term.

**Effect of neighborhood wording:** It broadens the Admissibility law's allowed dependence. It does not change the support of this specified staggered hopping operator, select a transport law, or promote this memo to a physical locality theorem. Whether a particular finite-range construction counts as the same staggered operator remains to be checked.

**Mediated counterroute to test:** Compile a radius-two transport stencil on the same bipartite, oriented graph into a finite sequence of ordinary nearest-neighbor gates (with routed workspace if needed). Compare its exact or controlled effective one-step operator with the target staggered Bloch symbol and current/flux observables. If the effective operator changes the target, the memo's operator-specific exclusion stands.

**Unresolved physical conditions:** The axioms do not identify a gate sequence with physical transport, provide a clock or control schedule, select the staggered operator, or supply a gauge/readout bridge. “Uniformly local” needs an explicit metric/range definition before it can be used as a theorem hypothesis.

### 2. Tensor-electric freeze is a single-step obstruction, not a circuit no-go

**Grade:** lead-verification candidate; the source is correctly scoped. Verify only any downstream use as a general obstruction.

**Source:** docs/DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md:17-45,51-68,70-99,108-138; pinned-main commit f5af11cd0102cfd0b51aef0911f600130bf5beb1, file blob fc571724d7822ec5fbb0fdbcf962d025f57d9edb.

**Restrictive assumption and inference:** The theorem supplies commuting tensor-electric slots and a vector stencil; it proves freeze for nearest-neighbor two-site generators that commute with every row (:19-45). Separately, exact Smith factors obstruct static integer and odd-modulus moves supported in one closed neighborhood (:51-68). These implications support “no move in this specified one-step class.” The note does not prove that a product of gates, a larger finite-range update, or a time-dependent circuit cannot return to the constraint sector.

**Counterevidence retained in the same source:** It exhibits an explicit ten-slot planar kernel move on nine sites, with doubled-coordinate extent (0,4,4) (:70-83), and states that box-free minimal support and native finite-qubit realization remain open (:85-99,131-138). Those boundaries must travel with any citation to the one-neighborhood obstruction.

**Effect of neighborhood wording:** No change to this conditional theorem: its matrix/stencil hypotheses and exact one-step result remain as proved. A broader Admissibility neighborhood could make a wider local dependency eligible, but does not supply the tensor model or authorize a gate/control protocol.

**Mediated counterroute to test:** Starting from the displayed planar kernel vector, construct a finite sequence of locally supported reversible updates whose composite preserves all rows and reaches the vector. Check the full constrained subspace, boundary conditions, and every transition. Run both variants: require code/gauge preservation at every intermediate time, and require it only at the endpoint. The latter is not ruled out unless continuous intermediate preservation is independently authorized.

**Unresolved physical conditions:** The tensor slots, stencil, and constraint sector are supplied model data. The axioms supply no physical identification for them, no local gate set, and no rule saying whether Gauss constraints must hold during a control sequence or only at its endpoints.

## Counterevidence and conditional results to preserve

- docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md:19-40,367-388 (blob a47f425bcf0e36ce06f45bc4bb9df02cba9e1e41) proves a finite-range Lieb-Robinson lemma for supplied interactions of bounded support diameter and overlap weight. Its displayed action includes nearest-neighbor matter hops and elementary plaquette terms of diameter two. It separately says finite range of the exact logarithm is only an unsatisfied conditional antecedent; do not turn this into either a general dynamical claim or a nearest-shell restriction.
- docs/COHERENT_BINARY_K_ADMISSION_BOUNDED_THEOREM_NOTE_2026-10-14.md:110-114,240-244,302-314 (blob c2cf25fd9edb41b262a30af5fcb0f70cd7344404) gives a supplied finite circuit with 29,489,403 nearest-neighbor physical gates. It explicitly permits temporary departure from constraint sector K and requires no intermediate-time preservation. It is conditional on supplied clean workspace, addressed gates, external schedule, drift removal, and final flag readout; it does not derive such controls from Admissibility.
- docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:80-124,140-184 (blob 96e9a173b8f853e31a72cbbde5625fe5c206d5f1) distinguishes kinematic link-connection covariance from gauging selection, action, and dynamics; it labels the latter as open rather than a locality no-go. Neighborhood wording alone closes none of these bridges.
- The tensor-electric theorem above is itself a valid conditional single-generator / single-neighborhood result. Do not rewrite it as false; do not promote it to a no-go on mediated updates.

## Search and verification limits

Required python3 scripts/lab_ops.py preflight returned preflight: go; it reported “model floor: no target named, no floor checked.” No model/effort telemetry beyond that was available here. The preflight itself checked whether origin was reachable; no other network, literature, numerical, or runner job was used.

The initial case-insensitive rg scan over the pinned docs snapshot used the requested locality/gauge/circuit terms; its full output is /tmp/luna_gauge_rg_f5_full.txt (16,583 hit lines), and only the first 100 lines were inspected as discovery output. Follow-up bounded phrase scans and their full logs are /tmp/luna_gauge_restrictive_full.txt, /tmp/luna_gauge_section_terms_full.txt, /tmp/luna_nn_restrictions.txt, /tmp/luna_intermediate_symmetry.txt, /tmp/luna_circuit_nn.txt, /tmp/luna_finite_range_dismissals.txt, /tmp/luna_exact_restrictive_main_full.txt, and /tmp/luna_intermediate_code_full.txt. Those searches were broad lexical filters, not exhaustive semantic review of every matching note. Complete claim sections and premises were read for the two leads and the counterevidence listed above; record-law lanes and the six branch-added SU2 docs were outside this pass. No source, axiom, audit/status file, or prompt was changed.
