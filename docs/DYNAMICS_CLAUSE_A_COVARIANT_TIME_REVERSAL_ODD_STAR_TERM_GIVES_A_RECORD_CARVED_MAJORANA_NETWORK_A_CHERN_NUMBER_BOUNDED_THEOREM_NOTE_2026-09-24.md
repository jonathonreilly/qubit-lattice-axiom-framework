---
claim_id: dynamics_clause_a_covariant_time_reversal_odd_star_term_gives_a_record_carved_majorana_network_a_chern_number_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "A supplied19-site pattern and record assignment admit a selected covariant odd star operator with a constructively checked quadratic image. Finite numerical band, slab, perturbation and node diagnostics are preserved with no certified global gap, exhaustive node count or physical particle identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.py
---

# Covariant star terms with a quadratic image: finite Majorana band diagnostics

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional finite construction and numerical band evidence; unaudited.

## Supplied model

Use Pauli compass bonds of coefficient 1 on the following periodic 19-site subset of a 4 x 4 x 4 cell:

`(0,0,0),(0,0,1),(0,1,0),(0,1,3),(0,2,3),(1,0,1),(1,0,2),(1,1,2),(1,1,3),(1,3,1),(2,1,2),(2,2,1),(2,2,2),(2,3,0),(2,3,1),(3,0,0),(3,2,3),(3,3,0),(3,3,3)`.

Its 22 nearest-neighbour bonds have at most one of each axis type at each site. The quotient graph is connected with displacement rank 3 and cycle rank 4. Their difference is a quotient-homology kernel dimension; it does not count all cycles of the infinite lift. Each of the 13 missing bond axes supplies a dangling Majorana.

Every record points along the last coordinate axis, in x/y/z order, on which it touches no unrecorded site. Give that unit vector sign `(-1)^(x+y+z)`. Every individual record-field contribution then vanishes. The pattern and contents are supplied and need not themselves be covariant. The compass Hamiltonian and the star operator below are fully soldered proper-cubic covariant. No ingredient is adopted as an axiom or inferred as the unique formation outcome.

## Covariant construction

The odd-weight Pauli strings on a site and its six neighbours carry a signed permutation action of the 24 proper cubic rotations. An orbit contributes one invariant sum when its stabilizer has consistent signs; otherwise it contributes zero. This finite orbit algorithm counts 37 terms at weights 1 and 3 and 325 at weights 1,3,5,7, placing fields at the centre. The neighbour radial field is a telescoping lattice sum, not another nonzero periodic bulk term.

Compression replaces each recorded factor by its specified component. In the auxiliary Clifford representation, `sigma^a=i b^a c`, `D=b^x b^y b^z c=1`, and a kept bond pairs b variables into `u_jk=i b_j^a b_k^a`. Constraint insertion and anticommutation signs give the constructive quadratic images in the runner. Physical spin spectra require the D=1 projection and its parity restrictions. The runner tests bond normalization and spectra of12three-site and30small tree examples; those controls do not identify arbitrary auxiliary states as physical.

Reduce the covariant orbit sums on this fixed pattern. In the runner's orbit-coordinate Euclidean metric, project the orbit of

`sigma^x_(+x) sigma^y_(-x) sigma^y_(+y) sigma^z_(-y) sigma^z_(+z)`

onto the nullspace of the nonquadratic reduced rows, then normalize its largest orbit coefficient to magnitude 1. This defines the supplied term; the projection metric is a modeling choice. The reported coefficient nullspace has dimension 41, with five active directions. The chosen term uses 23 orbits of weights 5 and 7. Its image consists of 27Kitaev corner patterns and one dangling-axis x field at(2,2,2). Statements about these dimensions are finite linear-algebra results, not a claim that the support-local freeness search covers every possible representation.

Cancellation must hold on the infinite periodic operator, not just after independently folding all sites into one cell. The runner checks the chosen term by aggregating unwrapped Pauli supports modulo a **single common cell translation**, retaining relative offsets. Every surviving support must have a quadratic image. Rational reconstruction checks exact cancellation for the integer reduction rows; floating-point residuals alone are not called exact. The 12 other dangling b variables remain decoupled in this constructed quadratic model.

## Band calculations and their scope

All following values are numerical diagnostics of the supplied auxiliary quadratic Hamiltonian. The 16 translation-invariant cell gauge assignments are compared using the stated momentum grid; they do not exhaust arbitrary spatial flux patterns. Negative bands are selected separately from exact decoupled zero modes.

| Test | Observed result in the supplied calculation |
|---|---|
| Compass plus lambda times the projected term | At lambda 1,2,4, eight lowest sampled sectors;12 decoupled zero modes; refined nonzero-band minima about 0.0190,0.0351,0.0174; tested plane Chern sums(-1,0,0) |
| Finite slab |12 cells open along z, k_x=1,121 values of k_y; localized states show opposite signed crossings on the two surfaces at energies±0.01 |
| Added independent dangling fields | Four specified all-axis draws yield opposite Chern sums for the original bands and bands grown from the zeros, summing to 0 on the tested planes; two near-zero modes remain |
| Two-axis field examples | One specified pair retains total C_x=-1 with 10 zero modes; another gives 0 |
| Change coupling and signs | Sampled minima approach zero at lambda 0.5 and 10; positive minima are found at 0.9 and 8; removing the constructed field closes the sampled/refined separation; lambda reversal and uniform record signs reverse the displayed Chern sum |
| Another active direction | The explicit supplied five coefficients(-1.928,-1.492,4.792,-0.488,-0.316) define a numerical model in the sign-fixed singular-vector basis. A24 seed search finds a particle-hole pair of middle-band near-touchings, with lattice Berry flux approximately-1 and+1 and approximately linear splitting at two displacement scales |

The added dangling-field calculations hold the reduced star term fixed. Arbitrarily changing physical record contents would also change that term. Therefore these perturbations are separately supplied quadratic-model modifications, not a proof that one record tilt produces the entire tested Hamiltonian. The separate generic-content calculation is a finite test of one specified content assignment.

For the node example the two observed momenta are near(5.172,6.197,6.074) and its negative modulo 2 pi, at energies near∓0.0071. The lower ten coupled bands, rather than all negative-energy bands inside the small pockets, define its monopole and slice sums. A finite grid and local optimization do not prove that these are the only nodes or that a globally positive gap exists elsewhere. No exact node count, protected low-energy particle species, physical U(1) charge, or neutral-Weyl identification is claimed.

A positive refined minimum is an upper bound on the true spectral minimum. Chern sums on finitely many slices and meshes are numerical evidence; a continuum topological phase theorem additionally needs an isolated smooth bundle and certified gap control. Slab crossings in a finite window do not establish an exact count of all surface branches. The stated zero-mode decoupling is a property of the auxiliary operator, not by itself a physical spin ground-state degeneracy count.

## Reproduction and deferred work

The primary runner defines the full coordinate, orbit, projection, Hamiltonian, gauge, grid, optimizer and random-seed conventions. It retains all nine calculation families and checks overlap nonsingularity. The selected projected term is checked with offset-preserving support aggregation; the singular-vector node example remains a numerical model whose coordinates and invariants must be reproduced on the executing numerical stack.

Historical independent-check narratives, wider searches, doubled-cell comparisons and the 4095 field-subset map in the submitted branch remain preserved there for further review. They are not promoted to current certificates here. In particular, unrestricted gauge minimization, certified gap bounds, a physical projection/degeneracy analysis, representation-independent freeness, and physical matter identification remain open.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_GAPPED_MAJORANA_FERMIONS_IN_A_STATIC_Z2_GAUGE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_GAPPED_MAJORANA_FERMIONS_IN_A_STATIC_Z2_GAUGE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_COVARIANCE_ALLOWS_THEM_AND_ON_THE_CUBE_CARVING_NONE_KEEPS_THE_MAJORANAS_FREE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_COVARIANCE_ALLOWS_THEM_AND_ON_THE_CUBE_CARVING_NONE_KEEPS_THE_MAJORANAS_FREE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORD_FIELDS_KEEP_THE_CARVED_MAJORANAS_SUBLATTICE_SYMMETRIC_AND_A_GAPLESS_START_PLUS_A_TIME_REVERSAL_ODD_TERM_GIVES_A_CHERN_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORD_FIELDS_KEEP_THE_CARVED_MAJORANAS_SUBLATTICE_SYMMETRIC_AND_A_GAPLESS_START_PLUS_A_TIME_REVERSAL_ODD_TERM_GIVES_A_CHERN_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.py](../scripts/dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.py). Paired evidence: [current output](../logs/runner-cache/dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.txt).

The auxiliary representation is the mathematical construction of [Kitaev](https://arxiv.org/abs/cond-mat/0506438), with its physical projection, not an adopted framework premise. Numerical topology uses [Fukui, Hatsugai and Suzuki](https://arxiv.org/abs/cond-mat/0503172) where applicable.


## No-Go Discipline Gate

This gate bounds the negative subclaims and does not award an audit grade.

### N1 — Alternative routes

- **ATTEMPTED — Unwrap cancellations.** Aggregate Pauli strings modulo one common cell translation. The selected term survives this stronger test; independent site folding is insufficient by itself.
- **ATTEMPTED — Change record signs.** Uniform record signs reverse the sampled handedness. The record pattern is part of the supplied construction.
- **ATTEMPTED — Add quadratic fields.** Specified all-axis perturbations transfer opposite Chern number into formerly zero bands; selected pairs preserve it. This does not classify all field directions.
- **ATTEMPTED — Vary coefficient.** Selected coupling values and a second active direction produce different numerical band diagnostics. A finite search does not prove a complete phase diagram or node count.
- **ATTEMPTED — Project to spins.** The auxiliary construction and finite Clifford checks do not select a physical gauge sector, many-body state, charged particle, or emergent spacetime.

Successful counterroutes narrow the claim; they are not relabelled as failed physical alternatives.

### N2 — Conditional structure

The supplied dynamics, representation, record pattern and preparation assumptions are joint hypotheses. No independence count of physical obstructions is asserted.

### N3 — Hidden assumptions

The compass Hamiltonian and Majorana representation are supplied mathematics. The axioms do not select them, their gauge sector, physical state or readout. Numerical rank tolerances and finite grids remain explicit limitations.

### N4 — Residual matching

Companion results contribute only their linked conditional identities. Their finite calculations do not close an additional universal formation or dynamics problem.

### N5 — Resolution

- `per_element:` Pauli compression, signed group actions and declared Clifford identities are the element-level checks.
- `per_site:` Local supports and explicit carving-site constraints are checked only under the supplied record rules.
- `per_mode:` Finite Bloch grids and stated optimizers are diagnostics; no certified global band gap is inferred.
- `per_block:` Named finite cells and covariance coefficient spaces are checked with their explicit size and support restrictions.
- `lattice_wide:` General lattice conclusions rely only on displayed conditional arguments; finite searches do not certify physical emergence.

### N6 — Partial closure

The stated model gives conditional conclusions without adding an axiom. No necessity of new physical axioms is established by failure inside this restricted model.

### N7 — Strongest counter-route

Aggregate Pauli strings modulo one common cell translation. The selected term survives this stronger test; independent site folding is insufficient by itself. The surviving result retains all listed hypotheses and leaves alternatives outside that scope open.

### N8 — Related work

The linked parent notes supply the adjacent covariance, record-compression and carving arguments. Their narrowed scopes govern their use here; historical independent-check narratives are not a current certificate.
