---
claim_id: dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_gapped_majorana_fermions_in_a_static_z2_gauge_field_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Supplied relaxed compass patterns have a quadratic auxiliary Majorana representation with physical projection still required. Explicit finite spectra and momentum scans are numerical diagnostics. The 16-site infinite lift has an explicit28-edge cycle and is not a tree; quotient cycle-rank subtraction does not prove pure gauge or a global gap."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.py
---

# Relaxed compass carvings: quadratic Majorana representation and finite diagnostics

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional algebra and numerical finite diagnostics; unaudited.

## Supplied model and algebra

Set the Pauli-bond compass coefficient K=1, with positive-K rescaling understood. Every unrecorded site keeps at most one unrecorded neighbour per axis. A record is perpendicular to each axis on which its unrecorded neighbour keeps a bond. Thus record compression leaves

`H = sum_{(j,k,a)} sigma_j^a sigma_k^a + sum_{(j,a) dangling} h_{j,a} sigma_j^a`.

The explicit 16- and20-site periodic patterns and all nearest-neighbour edges are defined by N16, N20 and the coordinate construction in the primary runner. Records use `(1,sqrt(2),sqrt(3))`, with constrained components set to zero and the remainder normalized. Every surviving dangling-axis field is the sum of its two record contributions. These inputs are supplied, not framework-selected.

In the enlarged Clifford representation use `sigma_j^a=i b_j^a c_j`, with physical constraints `D_j=b_j^x b_j^y b_j^z c_j=1`, and `u_jk=i b_j^a b_k^a`. Each kept bond becomes `-i u_jk c_j c_k` in this convention. A dangling field is `i h b_j^a c_j`. The even bond variables commute mutually and with these terms, so fixing them leaves a quadratic operator. Projection onto all D_j=1 must still be imposed to recover physical spin states: an arbitrary auxiliary Fock vacuum need not survive projection. The finite spin-spectrum comparisons below test their actual cases, not a general assertion that unconstrained vacuum minimization always gives the physical spectrum.

A kept-axis field generally fails to commute with that bond variable in this representation. This is a sufficient solvability construction, not a necessary criterion. In particular a leaf with its sole bond along c admits `sigma^c=-i b^a b^b` on the physical space, using its two dangling Majoranas. The original universal exclusion of kept-axis fields is therefore not retained.

## Periodic topology: the lift is not a tree

Both displayed quotient graphs are connected and have displacement rank three. The20-site graph has23edges, cycle rank4 and14dangling axes. The16-site graph has18edges, cycle rank3 and12dangling axes. The differences `beta1-3` are1and0. They count the kernel dimension of the quotient graph's real homology displacement map. They do **not** count every cycle of the infinite periodic lift.

For example, the 16-site lift has the following simple 28-edge cycle, whose coordinates are ordinary integers; consecutive vertices, including the last and first, are nearest neighbours:

`(4,-3,2),(4,-3,1),(4,-2,1),(3,-2,1),(3,-1,1),(3,-1,2),(3,0,2),(3,0,3),(2,0,3),(2,1,3),(1,1,3),(1,1,2),(0,1,2),(0,0,2),(-1,0,2),(-1,-1,2),(-1,-1,1),(-1,-2,1),(0,-2,1),(0,-3,1),(0,-3,2),(1,-3,2),(1,-3,3),(2,-3,3),(2,-4,3),(3,-4,3),(3,-4,2),(4,-4,2)`.

Every vertex reduces modulo 4 to N16. This directly refutes the submitted tree claim. Algebraically, a commutator of two winding walks can close in the abelian periodic cover even though neither is in the linear kernel of the quotient-cycle displacement map. Equal energies for the sampled translation-invariant gauge assignments do not prove that arbitrary gauge assignments on this lift are pure gauge.

## Finite spectral evidence

The primary runner retains the supplied calculations, now interpreted as floating-point diagnostics:

| Calculation | Submitted numerical value or tested scope |
|---|---|
| N20 physical-spin lowest Ritz value versus auxiliary minimum | about -26.0373871085;16 spanning-tree gauge classes |
| N16 spin versus auxiliary minimum | about -20.1928732905; all 2^18 bond-sign assignments |
| N16 cycle-basis operators | commute with the supplied dangling-field Hamiltonian; a tested kept-axis perturbation breaks some |
| N20 translation-invariant sectors | sampled per-cell energies about -26.036648 and -25.92526 |
| N20 momentum scan | two near-zero bands and smallest sampled nonzero absolute energy about 0.61787 on 16^3 points |
| N20 bond-sign perturbations | in the specified repeated 2 x 2 x 2 construction,32 flips cost about 0.11139 and 152 have energy change below tolerance |
| N20 doubled cells | tested x/y/z doublings give no lower sampled energy density |
| N16 translation-invariant sectors | eight sampled averages agree within tolerance; four near-zero bands and sampled separation about 1.437 |
| SAT catalogue |2500 solutions supply nine distinct three-direction components; up to eight are scanned numerically |

Seeded Lanczos with residual checks supports the displayed low eigenpairs, without certifying all multiplicities or a thermodynamic gap. A sampled momentum minimum is an upper bound on the true minimum; calling it a gap requires further control between samples. Likewise no lower energy in finitely many sectors or supercells establishes a global flux minimizer. Bond-flip costs are computed for the stated periodic perturbation, not an isolated infinite-volume excitation. Zero-energy auxiliary bands alone are not a count of physical spin ground-state degeneracy after projection.

## Boundary and continuation

The exact retained argument is the conditional quadratic representation and the explicit graph/cycle verification. Numerical tables remain reproducible diagnostics. No physical fermion species, topological order, global ground sector, uniform gap, localized-mode basis or extensive spin degeneracy is established. The source branch preserves the submitted exploratory scans and historical independent-check narrative for follow-up; those reports are not new evidence supplied by this review.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_ZERO_FIELD_CARVINGS_ARE_CUBES_AND_TUBES_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_ZERO_FIELD_CARVINGS_ARE_CUBES_AND_TUBES_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.py](../scripts/dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.py). Paired evidence: [current output](../logs/runner-cache/dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.txt).

The auxiliary representation is the mathematical construction of [Kitaev](https://arxiv.org/abs/cond-mat/0506438), with its physical projection, not an adopted framework premise. Numerical topology uses [Fukui, Hatsugai and Suzuki](https://arxiv.org/abs/cond-mat/0503172) where applicable.


## No-Go Discipline Gate

This gate bounds the negative subclaims and does not award an audit grade.

### N1 — Alternative routes

- **ATTEMPTED — Unwrap the graph.** Construct a simple 28-edge cycle on the infinite N16 lift. This defeats the original tree and pure-gauge inference.
- **ATTEMPTED — Change field axis.** The companion leaf example keeps a kept-axis field quadratic. The dangling-axis condition is sufficient, not necessary.
- **ATTEMPTED — Change gauge period.** Compare doubled cells and periodically repeated flips. Those finite searches leave arbitrary gauge patterns unresolved.
- **ATTEMPTED — Resolve momentum.** Use stated grids above zero bands. Positive grid minima do not certify a positive continuum gap.
- **ATTEMPTED — Project auxiliary states.** Finite spin energy comparisons survive, but auxiliary flat-band counts alone do not prove a physical spin degeneracy.

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

Construct a simple 28-edge cycle on the infinite N16 lift. This defeats the original tree and pure-gauge inference. The surviving result retains all listed hypotheses and leaves alternatives outside that scope open.

### N8 — Related work

The linked parent notes supply the adjacent covariance, record-compression and carving arguments. Their narrowed scopes govern their use here; historical independent-check narratives are not a current certificate.
