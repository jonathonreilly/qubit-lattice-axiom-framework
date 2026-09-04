---
claim_id: emergent_3d_fermion_one_qubit_superlattice_existence
claim_type: bounded_theorem
claim_scope: "Finite declared-model result: exact Pauli calculations verify Bravyi-Kitaev superfast-encoding relations, stabilizer ranks, bounded string-operator syndromes, and fermionic-sign diagnostics on the named open cubic blocks and tori; a separate 5x5x5 diagonal marker constraint has the enumerated finite-torus zero sets; a separate 2D Pauli rule has the reported finite charge-class sign table; and a bounded unit-cube census has the reported representative counts, common-zero witnesses, and finite-window mobility counts. These results do not construct one framework Admissibility law, couple the marker sectors to the fixed BKSF embedding, supply state preparation or dynamics, or establish an infinite-volume particle or phase."
upstream_dependencies: []
runner: scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py
---

# Finite BKSF fermionic-sign checks and a separate superlattice marker census

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification and dependency closure. This source sets no audit verdict.
**Primary runner:**
[`scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py`](../scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.txt`](../logs/runner-cache/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.txt)

This note retains exact finite computations and separates them from their physical interpretation. It studies four declared objects: a fixed-coordinate BKSF encoding, a diagonal marker constraint, a two-dimensional Pauli rule, and a bounded three-dimensional unit-cube census. The runner does not assemble those objects into one framework law.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite Pauli, rank, constraint-propagation, finite-field, and bounded-window computations with explicit physical and framework boundaries."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independently audit the finite computations and their declared import boundaries."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The machine-bound target is the conjunction of runner groups `A` through `F`:

1. `A`-`C`: finite BKSF relations, stabilizer ranks, Pauli support and syndrome identities, three closed `A_ij` string circuits, two finite fermionic-sign diagnostics, and finite controls.
2. `D`: exact zero-set cylinders for one separately declared marker constraint on seven named tori; four template-separation calculations; an operator/constraint support-footprint census; and a finite seven-bit pattern census.
3. `E`: commutation, two torus ranks, a finite-window charge quotient, T-junction signs, and a mutual-sign table for the declared 2D rule.
4. `F`: exhaustive unit-cube pattern counts under the declared equivalence, explicit finite-field common zeros for the 21 one-pattern representatives, and a `2x2x2`/margin-`3` mobility calculation for 21 one-pattern and 423 two-pattern representatives.

Every executed predicate uses integer or `F2`/`Z4` arithmetic, finite-field arithmetic, exhaustive enumeration, or exhaustive constraint propagation. The clearance test uses an integer squared-distance comparison. No floating-point witness, SAT solver, or external solver enters the executable result.

## Imported methods and support

The following imports are load-bearing for names or interpretations, but not framework premises:

- **BKSF construction.** The definitions of the edge operators and their interpretation as an encoding of an even fermionic algebra are imported from Setia, Bravyi, Mezzacapo, and Whitfield, [“Superfast encodings for fermionic quantum simulation”](https://arxiv.org/abs/1810.05274). The runner redeclares the operators and checks the finite Pauli identities; it does not derive the encoding from the local qubits.
- **Fermionic-sign diagnostic.** The use of the three-string reordering sign as a statistics diagnostic is imported from Levin and Wen, [“Fermions, strings, and gauge fields in lattice spin models”](https://arxiv.org/abs/cond-mat/0302460). The runner computes the finite operator signs. Calling `-1` “fermionic” is the operational interpretation supplied by that method, not an independently derived thermodynamic statement.
- **Polynomial/module notation.** The translation-invariant Pauli representation by Laurent-polynomial modules follows Haah, [“Commuting Pauli Hamiltonians as maps between free modules”](https://arxiv.org/abs/1204.1063). This note retains only the runner's bounded pattern census and explicit common-zero evaluations; the original general depth/no-particle conclusion is not retained.
- **Controls.** “2D toric-code epsilon” labels the explicit finite Pauli control implemented by `TC2D`. The other three-dimensional `+1` control is only the commuting-X-string construction the runner executes; it is not a checked 3D toric-code charge.

There are no observational values, fitted constants, accepted framework premises, Jordan-Wigner strings, graded tensor products, or imported numerical tables. The standard literature methods above are not recomputed from first principles, so the result is not a zero-input derivation.

## Declared finite models

### Fixed-coordinate BKSF model

The ambient fine lattice has one qubit at every available fine site. A coarse vertex `v` is placed at `2v`, and the qubit for its positive coarse edge in direction `a` is placed at `2v+e_a`. Only those coarse-edge-role qubits participate in the BKSF operators. The other fine-site roles are not additional encoding qubits.

At each coarse vertex the direction order is

```text
-x < -y < -z < +x < +y < +z.
```

For an oriented edge `(i,j)`, the runner constructs

```text
A_ij = X_(ij) times the ordered incident-edge Z strings,
A_ji = -A_ij,
B_i  = product of incident-edge Z operators,
S_f  = the phase-corrected ordered product of A operators around face f.
```

The two Pauli components of the formal hopping expression are `A_ij B_i` and `A_ij B_j`. The runner never represents their scalar coefficients, so its exact claims concern their Pauli supports, commutators, syndromes, and string-product phases.

The finite identity `prod_i B_i=I` imposes a global parity relation. On a finite periodic connected graph, an endpoint type therefore occurs with a compensating endpoint rather than as an isolated single excitation. The sign calculations probe the local endpoint type using open-block strings.

### Separate marker constraint

The marker construction uses the same fine-coordinate set but is logically separate from the BKSF model. For an axis `a`, it declares a period-`(4,2,2)` value template:

```text
all-even corner:  (s[a] // 2) mod 2
one-odd edge:     free
two-odd face:     0
three-odd centre: 1
```

There are 16 translates for each of three axis orientations, hence 48 templates. At every site, the marker penalty reads pinned offsets in a `5x5x5` window; if no template matches it adds one contribution, and each matching template with a pinned centre contributes when the centre disagrees.

The marker's 48 translated/oriented sectors are not coupled to the BKSF embedding. In particular, the runner does not condition the fixed coarse-edge operators on which translated marker sector is realised. The construction therefore is not one assembled translation-covariant Hamiltonian or one nearest-neighbour Admissibility rule.

### Homogeneous finite diagnostic models

The 2D rule is the one-pattern Pauli rule `IXZZXIIII` on the displayed four-site support. Its charge classes are a quotient of syndromes in declared finite windows. The 3D census uses one qubit per translation cell and generator supports within the unit cube. Its equivalence is only common cubic vertex maps, common onsite Clifford relabellings, and exchange of the two displayed patterns; no generator-row operation or wider support class is included.

## Finite results

### A. Encoding identities and ranks

- BKSF relations `R0`-`R4` and `prod_i B_i=I` hold on open and periodic `3x3x3` coarse blocks.
- With face stabilizers alone, the open `3x3x3` and `4x4x4` blocks give `V/n/k = 27/54/26` and `64/144/63`.
- On coarse tori `3^3`, `4^3`, and `3x3x4`, face-only ranks give `k=29,66,38`; adjoining three displayed noncontractible Wilson loops gives `k=26,63,35`; adjoining every `B_i` to the face set gives `k=3` in each of those three tested cases. Equality across these cases is not an all-size scaling result and does not distinguish a phase or foliated order.

### B. Finite transport-operator checks

On the open `5x5x5` coarse block, the two components associated with each positive-axis edge have a union of 11 fine sites, all fixed coarse-edge sites, and `L_infinity` radius 2 about the edge midpoint. The three axes have the same checked union size and radius; their Pauli weights and strings need not be identical.

All 144,000 `(component, face)` pairs commute, and every `A_ij` has exactly the two endpoint `B` syndromes. Three closed products of `A_ij` string representatives are expressible in the face-stabilizer span with residual phase `+1`. These are not products of the full hopping sums.

### C. Finite sign diagnostics

On the open `7x7x7` coarse block, the imported Levin-Wen T-junction formula returns `-1` for 10 declared leg geometries, including noncoplanar and rerouted cases. Reordering the same three pairwise string representatives returns `-1` for four declared triangle geometries. These are finite operator-algebra witnesses; they do not by themselves prove adiabatic exchange, a gap, deconfined quasiparticles, a thermodynamic limit, or a phase.

The bound-pair construction returns `+1`, the separate 3D commuting-X-string construction returns `+1`, and the explicit 2D toric-code epsilon control returns `-1`. A bare X string anticommutes with 18 BKSF face stabilizers in the displayed case.

### D. Marker and support censuses

- On the `4x4x4` torus, exhaustive branch-and-propagate enumeration returns 48 pairwise-inconsistent zero-penalty cylinders, exactly the declared sectors, with 24 free bits each. The zero-set cardinality is therefore `48 * 2^24`.
- On `8x4x4`, it returns the 48 declared cylinders with 48 free bits. On `5x4x4`, `4x5x4`, and `7x4x4`, it returns zero cylinders.
- For the declared template-separation criterion, a `3x3x3` window leaves two unseparated pin-pairs, a seven-site star leaves 29, and `5x5x5` leaves zero across all 48 templates. Each of the eight period-2 value assignments leaves an unseparated pair at each tested odd cubic side length `3,5,7,9`. This is minimality only within that criterion and those declared template families.
- The footprint census contains 16 displayed BKSF/hop objects and 31 actual marker-penalty contributions: 30 pinned-centre contributions plus the no-template contribution. Four supports fit a seven-site star. The other 43 are assigned explicit 6-connected hulls, the largest using 125 hubs. Since any finite support can be connected by added hubs, this is a support diagnostic, not a locality or nearest-neighbour factorization theorem.
- Across the 48 declared marker sectors and all free-bit fillings, the finite corner-centred star census realises all 128 seven-bit patterns and adjacent pairs realise all four two-bit patterns. This finite equality is not extended to possibility-state rules or general admissibility constraints.

### E. Two-dimensional rule

For `IXZZXIIII`, all translates within interaction reach commute. The runner obtains `k(6)=k(8)=2` and three nontrivial classes in its declared finite syndrome quotient. Their finite T-junction signs are `+1` in 12 geometries, `+1` in 12, and `-1` in 18. The mutual-sign table has `+1` on the diagonal and `-1` off diagonal. The toric-code/anyon reading is imported physical interpretation; the exact retained content is the finite rank, quotient, and sign calculation.

### F. Unit-cube three-dimensional census

The exhaustive loop excludes the identity and finds 1,011 self-commuting patterns among the `4^8-1` nonidentity Pauli patterns, 735 with support at least four. Under the declared equivalence, it reports 21 one-pattern representatives at support at least four, 28 at support at least one, and 423 mutually commuting two-pattern representatives.

For each of the 21 one-pattern representatives, the runner evaluates both Laurent polynomials at nonzero coordinates over `GF(2)` or `GF(4)` and exhibits a common zero, establishing that each displayed two-generator Laurent ideal is proper. Empty polynomial components are evaluated as zero; `(0,0,0)` is never used as a Laurent-torus witness.

In the declared `2x2x2` generator-cell block with margin 3, the 21 representatives distribute as `0:10, 1:5, 2:2, 3:4` by the number of coordinate axes for which some nontrivial cluster is mobile in that window. The simultaneous-intersection calculation returns zero representatives with one cluster mobile along all three axes. The analogous calculation returns zero among the 423 two-pattern representatives. These are exhaustive outputs for that finite window and representative set, not a classification of arbitrary supports, larger windows, phases, or non-stabilizer models.

## Operational meaning and claim boundary

- **Fermion.** Here the word refers only to the `-1` value of the imported Levin-Wen/reordered-string operational diagnostic for the displayed endpoint operators. It does not assert a continuum fermion, relativistic field, spin representation, canonical anticommutation relations for physical site operators, or a thermodynamic quasiparticle.
- **Emergent.** The computation does not derive the BKSF structure dynamically. BKSF is chosen as an encoded even-fermion algebra. “Emergent” is therefore not part of the retained theorem.
- **One qubit per site.** The ambient construction places at most one qubit on each fine site; BKSF actively uses the fixed coarse-edge subset. Eight fine sites per coarse-cell volume is geometric bookkeeping, not an active-qubit cost, density theorem, or minimum.
- **Locality and covariance.** BKSF operators are finite-support operators in a coordinate-fixed embedding. The marker constraint directly reads a `5x5x5` window. Marker symmetrisation includes three orientations, but the runner does not test covariance of the ordered BKSF operators under proper cubic rotations or select/couple one of the 48 marker sectors. No nearest-neighbour framework rule is supplied.
- **Gauge/stabilizer assumptions.** Face stabilizers, Wilson loops, the fixed global parity sector, and the imported encoding are declared inputs. Their finite ranks are computed; their physical realization and preparation are not.
- **Finite versus thermodynamic.** Every assertion is confined to the named blocks, tori, windows, templates, and representatives. There is no `L`-independent theorem, infinite-volume limit, gap estimate, stability theorem, or deconfinement calculation.
- **Formation and records.** No update law, state preparation, sector-selection probability, measurement/Born bridge, Record mapping, or formation rate is present.

## Proof-obligation disposition

The runner closes the finite linear-algebra, Pauli, enumeration, finite-field, and constraint-propagation obligations listed above. The physical bridge from finite signs to a fermionic interpretation is explicitly imported and limited. The original claims that a single covariant Admissibility law forms the marker pattern and a 3D fermion, and that one qubit per homogeneous cell universally excludes such matter, are withdrawn. The retained zero counts are outputs of explicitly bounded exhaustive sets and are not used to foreclose other constructions.

## Executable claim block

```text
model_relation: fixed-coordinate BKSF checks and marker constraint are separate declared models
ambient_resource: at most one qubit per fine site; BKSF uses only fixed coarse-edge sites
A: finite relations and ranks on the named open blocks and three named tori
B: exact Pauli support/commutator/syndrome checks; three closed A-string circuits
C: finite T-junction and reordered-string signs with explicitly scoped controls
D: finite marker zero-set cylinders; odd-window template separation; support and bit-pattern censuses
E: finite 2D commutation, rank, quotient, T-junction, and mutual-sign results
F: 1011 of 4^8-1 nonidentity patterns; 735 support>=4; 21/28 one-pattern and 423 two-pattern representatives under the declared equivalence; common zeros over GF(2) or GF(4); bounded mobility outputs
physical_interpretation: imported and limited to an operational fermionic-sign diagnostic
framework_law_formation_infinite_volume_phase_claims: absent
runner_result: PASS=24 FAIL=0 required
```

## Review record

Hard landing conditions are a fresh paired runner/cache result with `PASS=24 FAIL=0`, exact cache SHA binding, a current citation-graph manifest entry, clean pipeline and strict audit lint/readiness checks, an independent finite recomputation, and decisive fail-closed mutations. Independent audit remains a separate lane; this note does not set or apply its verdict.
