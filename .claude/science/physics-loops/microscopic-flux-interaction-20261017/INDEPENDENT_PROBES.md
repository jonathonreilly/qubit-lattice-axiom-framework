# Independent flux-selection and elimination review

Reviewed root `scripts/microscopic_flux_interaction.py` and the actual source `scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py` in `/private/tmp/scalar-environment-20261017`, on the stated new branch/base. No repository files changed.

Independent code: `/private/tmp/microscopic-independent.py`; output `/private/tmp/microscopic-independent.json`.

## Independent actual-code syndrome reconstruction

Loaded the actual upstream geometry and cycle sequences, then reconstructed each cycle's X support solely from its traversed graph edges: onsite edges contribute their one local qubit; cross-site edges contribute their two repetition halves; XOR along the loop gives its support. This path did not call A, loop_op, Pauli multiplication, symplectic commutator, edge_qubits or INC. Transposed that loop-edge incidence matrix to obtain each physical Z probe's syndrome. Only afterward compared all reconstructed supports with original loop_op X supports; every row agrees.

Exact L4 results:
-3072 physical qubits;
-2624 listed loop operators;
-2304 distinct Z syndromes;
-1536 singleton classes and768 classes of size2;
-no empty Z syndrome;
-max periodic coarse-site L1 diameter1.

The classes are exactly the1536 onsite-edge qubits individually plus the768 repeated cross-site edge pairs. Thus the claimed diameter bound is correct and has an explicit structural interpretation. This is an exact finite L4 enumeration; an all-size claim would need a separate combinatorial proof.

## Selection-rule proof

For each conserved Hermitian loop involution W, suppose [H,W]=0 and [rho,W]=0. A Pauli O_i has W O_i W=(-1)^s_i(W) O_i. Conservation implies the same equation for O_i(t). Trace cyclicity and rho invariance give

Tr[rho O_i(t)O_j]=(-1)^[s_i(W)+s_j(W)] Tr[rho O_i(t)O_j].

If any loop syndrome bit differs, the correlation vanishes. The reverse-ordered term obeys the same equation, so the retarded commutator response also vanishes. Neither equal time nor a pure flux sector is required; any loop-block-diagonal rho works. Stationarity [rho,H]=0 is needed for the usual time-translation-invariant susceptibility interpretation, not for this cancellation at fixed times. Equal syndromes are necessary, not sufficient, for a nonzero correlation. Generator dependencies and duplicate loops do not invalidate the proof or necessary comparison.

For the actual single-Z probes this proves that distinct syndrome classes have zero two-point response at all times. Their nonempty syndromes also make their one-point means zero in the allowed states, so connected and full two-point functions coincide.

Crucial scope: this does NOT exclude flux-neutral composites, hopping/density bilinears, higher-point strings whose net syndrome cancels, states coherent between loop sectors, or dynamics containing explicit flux-changing terms. In particular, a neutral collective scalar could live in syndrome0, and the tested individual Z probes do not rule it out. Do not translate the result into a general absence of scalar propagation.

## Flux penalties and band elimination

If P projects onto any common conserved flux sector and Q=1-P, then [H,P]=0 implies PHQ=PH(1-P)=HP(1-P)=0. Consequently increasing a diagonal flux penalty cannot induce virtual cross-sector interactions through PHQ(E-QHQ)^-1QHP: that expression is exactly zero. This is conditioned on exact conserved sectors; adding flux-changing electric terms changes the hypothesis. Root's direct-sum fixture illustrates the algebra but does not independently test all sectors of the3072-qubit model; the general proof plus actual centrality checks carry that argument.

For a genuinely quadratic fermion Hamiltonian, eliminating a one-particle high-band block by the Schur complement produces an energy-dependent quadratic kernel H_LL+H_LH(z-H_HH)^-1H_HL. Gaussian integration preserves Gaussianity, so this operation does not create a fundamental quartic interaction. It does not say there are no poles: the Schur kernel has high-band resolvent singularities, the full projected propagator retains accessible free eigenmode poles, and bilinear correlators have particle-hole transitions. Low-energy expansions require spectral separation and must retain their range of validity. A fluctuating auxiliary field can be introduced formally, but its identification as a new autonomous physical scalar does not follow.

The supplied explicit density-density positive control usefully shows departure from additive two-particle free spectra. It is a new interaction premise, not something the band elimination has generated. A thermal sum over conserved flux sectors can also lead to statistical effective correlations when sectors are traced out; the PHQ proof rules out dynamical virtual transitions, not every possible static coarse-grained functional.

No material flaw found in the narrow selection rule, finite syndrome enumeration, or conditioned quadratic-elimination statements. Avoid expanding them into a universal no-interaction/no-free-pole/no-collective-scalar theorem.
