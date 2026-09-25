---
claim_id: dynamics_clause_record_fields_keep_the_carved_majoranas_sublattice_symmetric_and_a_gapless_start_plus_a_time_reversal_odd_term_gives_a_chern_number_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Dangling-only fields on even-period compass carvings preserve a sublattice symmetry. An isolated negative bundle has vanishing Chern number on particle-hole-invariant planes. Leaf fields are an explicit exception to the content rule. Supplied finite band/content searches are numerical and restricted to their actual classes."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.py
---

# Dangling-field sublattice symmetry and finite Chern diagnostics

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional symmetry theorem with numerical controls; unaudited.

## Supplied setting

Use the compass bonds and constrained dangling fields on the explicit N16 and N20 patterns of the relaxed-carving construction. Their coordinates, gauge signs and field coefficients are fully specified in the primary runner. Dynamics, rank-one record compression, patterns, contents and any added three-spin term are supplied. Auxiliary Majorana variables have physical constraints `D_j=1`; band calculations alone are not statements about a projected spin phase or particle species.

## Sublattice theorem

Assign each c_j the parity of its cubic site and each dangling b_j^a the opposite parity. Every compass bond joins neighbouring sites and every dangling field joins b_j^a to c_j. Thus every quadratic coupling joins opposite classes, and the momentum-independent diagonal matrix S obeys `S H(k) S=-H(k)` for even-period cells. Odd-period cells require an enlarged cell or a momentum-shifting description. This argument holds for all allowed field magnitudes and gauge signs, not only the sampled momenta.

If the negative-energy bundle is isolated with constant rank, S identifies it with the positive-energy bundle and preserves its first Chern number. On a particle-hole-invariant plane k_a=0 or pi, complex conjugation and k->-k identify the same bundles with opposite Chern numbers; inversion of both plane coordinates preserves orientation. Consequently C_-=0 on those planes. An isolated bundle over the whole three-dimensional Brillouin torus has the same slice Chern number on homologous slices, giving the corresponding weak invariant zero. Flat zero modes may be excluded only while the negative bundle remains separated from them. No assertion about every possible node type or charge follows merely from a sampled band plot.

## Leaf exception

A leaf with only a c-axis bond can have a kept-axis field and remain quadratic: the physical identity `sigma^c=-i b^a b^b` uses its two dangling Majoranas. This joins the same class and breaks S. The runner compares the exact two-qubit matrix spectrum with a parity sector of the six-Majorana quadratic spectrum for20field choices. Thus dangling-only fields are sufficient for the symmetry, not a general characterization of all solvable record fields.

## Reproducible finite diagnostics

The runner keeps seven families:

1. Both networks,24 gauge assignments, random fields and momenta obey the sublattice identity.
2. Negative-band lattice Chern sums vanish on the six 0/pi planes for the chosen sectors. Sampled separations are about 0.618 and 1.437, with respectively 2 and 4 near-zero bands.
3. The leaf comparison verifies the physical-space identity above.
4. Add the supplied Kitaev corner pattern, whose quadratic image is `-i epsilon_abc u_im u_mk c_i c_k`. At kappa=0.05,0.2,1,4 the computations find two near-zero bands and zero Chern sums on the tested planes. Refined nonzero-band minima are respectively about(0.612,0.541,0.569,0.341) and(0.034,0.132,0.431,0.210). This discrete parameter sample is not a proof that a gap stays open along a connecting path.
5. Set N20 dangling fields to zero by hand. The c-only model has a near-zero minimum at kappa=0 and a refined minimum about 0.0528 at kappa=0.3; plane Chern sums are(1,0,0) on three tested slices per axis. The seven records touching all three axes prevent the **componentwise perpendicular-content construction**, not every possible cancellation of net fields from multiple records. No impossibility of all zero-net-field content assignments is asserted.
6. A bounded SAT search supplies 16 otherpatterns for which componentwise perpendicular contents do work. Eight sampled c-band models have near-zero nonflat energies. This is a search result, not a full geometric or gap classification.
7. For one seeded axis-valued content assignment on each pattern, the runner reduces weight-one/three covariant star terms. It separately reports the coefficient nullspace, the rank of its actual Pauli image and the number of same-class bilinears. Kernel directions acting as zero are not counted as nonzero free terms. This is a finite-content calculation with the stated support-local D-insertion criterion; it is not a universal no-go over continuous record contents, larger supports, other carvings or alternative representations.

The freeness routine tries physical-constraint insertions on the Pauli support and pairs kept-axis b variables into bonds. Its constructive successes are valid identities. Completeness outside that explicitly searched class is not supplied by its failure to find an image.

## Numerical and physical limits

Lattice Chern sums use a discretized link-variable method and must have nonsingular overlaps and a constant selected band count. Grid refinement supports numerical stability; it is not a certified global gap proof. Local minimizers and momentum grids provide upper bounds on a spectral minimum, not rigorous positive lower bounds. Here “near zero” uses the runner's declared numerical thresholds. Surface-mode, charged-matter and physical Weyl identifications are not derived. Historical external checks and exploratory wider scans remain recoverable on the source branch, without certification by this note.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_GAPPED_MAJORANA_FERMIONS_IN_A_STATIC_Z2_GAUGE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_GAPPED_MAJORANA_FERMIONS_IN_A_STATIC_Z2_GAUGE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_COVARIANCE_ALLOWS_THEM_AND_ON_THE_CUBE_CARVING_NONE_KEEPS_THE_MAJORANAS_FREE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_COVARIANCE_ALLOWS_THEM_AND_ON_THE_CUBE_CARVING_NONE_KEEPS_THE_MAJORANAS_FREE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.py](../scripts/dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.py). Paired evidence: [current output](../logs/runner-cache/dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.txt).

The auxiliary representation is the mathematical construction of [Kitaev](https://arxiv.org/abs/cond-mat/0506438), with its physical projection, not an adopted framework premise. Numerical topology uses [Fukui, Hatsugai and Suzuki](https://arxiv.org/abs/cond-mat/0503172) where applicable.


## No-Go Discipline Gate

This gate bounds the negative subclaims and does not award an audit grade.

### N1 — Alternative routes

- **ATTEMPTED — Change field axis.** A leaf kept-axis field remains quadratic and breaks the bipartition. The no-Chern argument requires the stated dangling-axis field class.
- **ATTEMPTED — Break the bipartition.** Add the supplied Kitaev pattern. Selected finite strengths retain zero sampled Chern numbers, not a proof for every strength.
- **ATTEMPTED — Remove fields.** The supplied zero-field model supports nonzero sampled Chern numbers. Failure of componentwise orthogonal records does not exclude cancellation of net fields.
- **ATTEMPTED — Change records.** Test one seeded axis-valued record assignment on each selected carving. These finite-cell images do not classify every record assignment.
- **ATTEMPTED — Increase star weight.** The companion higher-weight construction supplies a positive route. Weight-three image restrictions cannot exclude it.

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

A leaf kept-axis field remains quadratic and breaks the bipartition. The no-Chern argument requires the stated dangling-axis field class. The surviving result retains all listed hypotheses and leaves alternatives outside that scope open.

### N8 — Related work

The linked parent notes supply the adjacent covariance, record-compression and carving arguments. Their narrowed scopes govern their use here; historical independent-check narratives are not a current certificate.
