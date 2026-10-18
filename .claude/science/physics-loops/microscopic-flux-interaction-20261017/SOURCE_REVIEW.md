# Microscopic flux-interaction focused source review

Disposition: PASS for the stated conditional-support route test. No material correction required. This is not a formal audit, retention decision or integration/landing PASS.

Reviewed: complete note, complete primary runner, actual declared upstream Pauli definition prefix (geometry, labels, incident edges, Pauli phases, A/B/R definitions and cycles), complete primary output and loop pack, supplied independent mathematical review, and independently implemented syndrome reconstruction. Base: fa841753c1a6296e5ad45518375660b0f1004769. Primary note and runner hashes were recorded at entry. The author then added the constructive density-interaction witness in section 4; I reread the complete final note and confirm that addition in this same session. The primary runner remains unchanged. No repository edits, audits, commits, pushes or merges by this reviewer.

## Material conclusions

The specified source class is explicit: an actual quadratic fermion lift preserving central loop/repetition constraints, F of those constraints only, and decoupled spectators. The note correctly excludes arbitrary products of corner charges from that class; mutual charge commutation does not make charge products harmless quadratic penalties. It also explicitly declines to claim construction or locality verification of the full C19 fine-site lift. Results are conditional on that lift, not derived for every C19 completion or every one-qubit Hamiltonian.

The exact Pauli centrality enumeration supports [H,P]=0 for the declared generated algebra. Every loop is a Hermitian involution. Because loops are products of checked hopping generators, centrality with all generators also supplies loop mutual commutation. The algebraic implication PHQ=0 is exact; finite penalty denominators cannot restore a missing transition numerator. The direct-sum fixture illustrates this consequence and is correctly not presented as a 3072-qubit Hilbert-space diagonalization.

The syndrome proof is valid for all times whenever both H and rho commute with each conserved loop. Conjugation of the trace multiplies it by the product of the two syndrome signs. Any mismatch forces both ordered correlations, hence their commutator, to vanish. Loop independence is unnecessary. Stationarity is unnecessary for the stated cancellation, although it would be needed for a usual frequency-only equilibrium susceptibility. The note claims the cancellation, not the latter extra assumption.

Independent geometry reconstruction confirms 1536 singleton classes and 768 repetition-half pairs, no empty single-Z syndromes, and periodic coarse-cell diameter one. The two-Z neutral products therefore equal repetition operators. This restriction concerns these probes only. The text explicitly leaves neutral higher composites, other observables, coherent off-sector preparations and altered Hamiltonians open; it does not infer absence of a neutral scalar from charged-probe immobility.

CAR bilinear commutator closure, additive free many-body spectra within an admitted parity sector, and the one-particle Schur complement are correct. They preclude an independent quartic vertex generated merely by eliminating free one-particle bands. They do not imply arbitrary prepared states are Gaussian or exclude free particle-hole poles, statistical correlations from sector mixtures, arbitrary many-body projections, or new interactions. Those caveats are retained. The spectator statement is read as Hamiltonian/evolution factorization, not a claim that every initially entangled density operator is a product.

The added family H_V=H+V sum_edges n_i n_j is a valid constructive underdetermination witness. Density products vanish on vacuum and one-particle sectors, preserve charge-permuting graph symmetries and constraints, and have positive nonzero trace on the two-particle sector for V>0. Thus one-particle dispersion and source-vertex checks cannot select V, including V=0. No value is adopted. This strengthens the stated limitation without becoming a global no-go.

The negative result is limited to named mechanisms and quantified hypotheses. It is not a physical no-go theorem. Listed route comparisons are actual algebraic/scope tests, not an exhaustive search over microscopic completions. No physical premise is retired and no cosmological coupling is claimed.

## Verification

- Executed an exact copy of primary runner plus declared input in a separate temporary tree: 14/14 controls passed; generated result.json byte-identical to submitted output.
- Independently checked that all 2624 loop Paulis satisfy the Hermitian-involution phase relation.
- Read and executed the independent edge-incidence syndrome reconstruction. It does not call original A, loop_op, Pauli multiplication, commutator, edge_qubits or INC for its reconstruction; subsequent comparison matches every loop X support and exactly identifies the syndrome classes with onsite edges/repetition pairs.
- Manually verified the PHQ projector identity, trace-conjugation selection rule, CAR closure, Schur sign/order, and density-density positive control interpretation.
- Numerical fixture errors and the added quartic shift reproduce. These remain diagnostics of general identities, not a corner-model many-body spectrum or empirical test.

Later combined mechanical gates and exact-current-main preservation are not performed by this source reviewer. The source verdict is bound to the identities below.

The three added mutation controls corrupt a flux-preserving hop set, the Schur sign and the fermionic commutator. Recorded failures are respectively loop_hop, exact_high_band_elimination and bilinear_commutator_closure; source inspection confirms those controls exercise the intended formulas. Portable independent reconstruction is now included in outputs.

The author replaced the mutation checker's absolute Python path with sys.executable; this portability correction was inspected and confirmed. Relocated execution of the final repository independent checker passes and reproduces independent.json byte-for-byte.

## SHA-256 identities

```text
e9410c6459abbd94cbffcc7cfc2de816af02f7fb9881e073486efa117cfb6c1d  .claude/science/physics-loops/microscopic-flux-interaction-20261017/CLAIM_STATUS_CERTIFICATE.md
c81c2477958e1ecf48b7cf52a0063136e4e427f582dfebae6d8ee979f1c353f5  .claude/science/physics-loops/microscopic-flux-interaction-20261017/HANDOFF.md
0f7c533d141dcb2dbbc5ecd6d495869ad90596aeb08d4f6f3d8dc1877a1c06d9  .claude/science/physics-loops/microscopic-flux-interaction-20261017/INDEPENDENT_MATH.md
9d7763d59bfaf1a618b10b47f463a6b08ae434356bf478f6266d2c71ee916871  .claude/science/physics-loops/microscopic-flux-interaction-20261017/INDEPENDENT_PROBES.md
42bde1b8108d0c4b79424b1762ac3293d80a3573931847a51da8cfd5850f083f  .claude/science/physics-loops/microscopic-flux-interaction-20261017/STATE.yaml
3549c4b7b4b68117bd1ecdff94c3684f226ce1fcce5f98b7c1043e3095afdbfd  .claude/science/physics-loops/microscopic-flux-interaction-20261017/TRACE_GATE.md
2187816f2a9d5a34f433511c154c13b39b7346a613af50a9099daf8f84619de6  docs/MICROSCOPIC_FLUX_INTERACTION_NOTE_2026-10-17.md
90828f661436c1bf124c4d13f8991ca78f12a2c7ea84873dbaece31537bfbdd4  outputs/microscopic_flux_interaction/independent.json
4c2e390b2988284e394a32e3100299baf7bac9db42a28dd299b74ee4a49685ba  outputs/microscopic_flux_interaction/independent_check.py
c18123812b25e2c11b4ee7a6f51d29ce843afeb6568f8f12efaf68d2a701bcba  outputs/microscopic_flux_interaction/mutation_check.py
f37b0e813e556bafc8068195475c00d804971bec4658bf7536677e1502780fa3  outputs/microscopic_flux_interaction/mutations.json
b6aafeb6f84b4133ea918d4997824eb64acb5c037c60c28b0efb18e85de1d8be  outputs/microscopic_flux_interaction/result.json
0e60313a17d8198dfaae11f5387394ca991c6308f8b746b05272b40cf906333a  scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py
2cf991823adbcf6f77e49131d9aefc4670a766a14a09b68038eb30d57925e8b0  scripts/microscopic_flux_interaction.py
```
