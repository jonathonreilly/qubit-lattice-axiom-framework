# Native record compatibility: exact local algebra, Markov test, and a surviving domain

**Status:** conditional-support; author discovery, not formal review or audit.
**Claim type:** bounded_theorem. **Trace:** frontier_discovery, partial compatibility discrimination rather than a framework record construction.

The supplied native H0 has a trivial strictly local conserved-operator algebra on the full carrier. A separate result excludes repairing a common sharp site-marker interpretation by arbitrary finite-rate GKSL noise while keeping H0: a specific four-site pair transfer couples two incomparable marker patterns, and the no-event loss cannot cancel both directions. There is also an actual extensive invariant memory domain of the same H0, with a concrete additional guarded-birth instrument. These results resolve the declared conditional tests; they do not exclude permanent records in every possible realization of the axioms.

The complete proofs are in frozen DERIVATION.md, SHA `f0cb650ccfc0520e779539f0804bfc38b73ed71176972be7fac0462c5e62639b`. They retain the actual five pair components, density stabilizer, physical M2 factors and positive mu,tau. The main source is `docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md` at main `fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7`, SHA `7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0`. No prior spectral, scattering or thermodynamic asymptotic theorem is needed to prove the new algebraic results.

## What was resolved

For the actual local Hamiltonian,

    {finite-support O : [H0,O]=0} = C I.

The proof isolates the unique outside three-ladder coefficient of a four-collinear-site mobility term. It is `-(2tau/3)[b_v,O]` at an extremal support site, and the conjugate isolates `b_v^dagger`. Removing successive boundary planes proves the assertion for all finite supports, arbitrary operator coherences and the full state carrier. It is not a particle-sector computation or an assumption that O commutes separately with every summand. On tori the support and the stated collar must be unaliased. Global conserved quantities and genuinely infinite-tail operators are not included. Adding `-nu N` does not change the proof.

For the separate irreversible test, let `P_x=|1_r><1_r|` in one common, arbitrary supplied qubit basis. Ask that a state with an already formed marker at x remain supported in P_x for all future times, while allowing empty sites to form markers. An added finite-dimensional GKSL dissipator is unrestricted in strength, number conservation and spatial range, but the Hamiltonian part remains H0. Invariance forces each loss-of-marker jump block to vanish and also forces the corresponding block of

    K=-i H0-(1/2)sum_j L_j^dagger L_j

to vanish. Both directions between incomparable bit patterns are forbidden; Hermiticity then forces their Hamiltonian matrix element to be zero. The actual patterns `1010` and `0101` on four consecutive axial sites instead have

    |H_mn|=(2tau/3)[t^4+(1-t)^4]>=tau/12,

for some t in [0,1] determined by the common basis. The proof retains possible no-event cancellation before ruling it out for this pair. It also treats Lindblad gauge freedom: under the hypothetical persistence condition, every jump and adjoint has zero matrix element on this incomparable pair, so identity shifts and jump mixing cannot conceal the nonzero witness in a different Hamiltonian representation.

The all-state hypothesis is a clear sufficient domain for the test, but the proof exposes a smaller necessary domain condition. It already contradicts persistence if the SAME semigroup admits both of those two pure product configurations as formed-record preparations, with identical product spectators, and preserves their already occupied marker sites. For one such initial vector n, positivity first forces every `L_j n` to preserve its occupied sites; the offdiagonal derivative then gives K_mn=0. The other input gives K_nm=0. No assumption about all superpositions is needed for this two-input witness. A restricted record-admissible domain can avoid the test, but it must genuinely exclude at least one of the two tested configurations or change another named condition. In the original occupation basis these are ordinary translated bare two-particle pairs of the native model.

## A positive counterexample to broadening the conclusion

Let C_ind be the span of occupation configurations independent in the actual eighteen-neighbor pair graph. Every collective pair annihilator and pair gradient kills this subspace, as does V3, so

    H0|C_ind = mu N|C_ind.

All occupation bits are exactly stable there. The choices on `(3Z)^3` alone give dimension `2^(V/27)` on suitable tori. This is an extensive exact memory subspace on the actual qubits, not merely the vacuum or N=1 exception. Each nonvacuum fixed-N vector costs mu N energy. It therefore does not by itself identify the low-energy collective pair medium as readable memory. More concretely, for `0<nu<mu` it cannot contain a grand ground state: its `H0-nu N` energy is nonnegative, whereas the actual landed density-onset trial gives strictly negative grand ground energy.

The separately supplied range-two jump

    J_x=sqrt(gamma) b_x^dagger product_(y~_G x)(1-n_y)

keeps C_ind invariant under a GKSL law with the SAME H0. Its trajectories only add previously absent compatible sites; every old occupation remains fixed. This provides a one-content write-once marker process on the restricted domain. It adds the basis, Markov/Born instrument, rate and observation rule. It is not the axioms' unspecified nearest-neighbor Admissibility law, does not turn an absent site's value into an allowed readout, and does not supply distinct readable contents or a physical clock. On the unrestricted carrier it fails the persistence requirement, as the preceding theorem requires.

The physical remaining obligation is therefore precise: specify and establish a record-admissible state domain, content/instrument map and permanence mechanism that also preserves the intended collective low-energy physics. Asking for this whole missing map without new mechanism is target-equivalent to the original bridge. The present result supplies a test any full-carrier sharp realization must pass and a concrete restricted-domain alternative, not the full map.

## Actual source and prior comparison

The current minimal axiom memo, primitive registry/classification and all three registered primitive sources were freshly read before premise judgments. Approved units, kinetic-form isotropy and pointwise realized-state specialization retain their grants. None is treated as an unapproved import. Their actual grants do not select this basis, tensor-product quantum state model, Hamiltonian, GKSL law, Born readout, rate or record encoding. Record permanence is current axiom content; a site-fixed sharp-projector/full-carrier implementation is an additional condition.

The closest July record-observable normal-form note already proves freezing when all recordable rank-one frames span M2 and already separates a finite-unitary blank/record obstruction. That is prior art and is not repackaged as the present result. The new step instead concerns this actual H0, one arbitrary finite-support operator, and one common sharp basis even with arbitrary dissipative repair. The current cubic-response note also warns against identifying a Hamiltonian, strict tick and record-forming instrument. The old site-tagged permanence note explicitly leaves migrating semantics open; its now-superseded additive-readout quotation is not a premise. The branch-correlator erosion note concerns a different functional and is not evidence against durable records.

Earlier native stability work had an instantaneous occupation/coherence ambiguity and a timed phase-to-occupation protocol. Neither classified permanent local observables or made that Born protocol an actual record law. Refreshed open native PR9401 `ea3d4f62` and PR9413 `d6197654` explicitly retain the record-observable boundary. Their relevant current law/scope sections were inspected; their full spectral/thermodynamic proofs are not new premises here. Open apparatus PR9397 `72e8656d` supplies clocks and record banks on an enlarged carrier for a different rotor law, so it is not a native same-H0 exception. SOURCE_BINDINGS records exact current heads, actual read scopes, main source identities and the bounded prior search. No exhaustive literature-priority claim is made.

## Proof and computation separation

CONTRACT and DERIVATION were frozen with code identity before the sole scientific control. The runner independently expands the five literal collective templates with exact rational coefficients; it imports no previous builder. It streamed 99,125 terms and found exactly the two asserted four-site words, coefficient `(mu:0,tau:-2/3)`, and the unique boundary annihilation/creation factors. Three literal basis matrix elements matched the derived formula; the balanced basis attained `-tau/12`. Setting mobility to zero removes this witness. Exact H0 action on vacuum and independent-set configurations with one, two and four particles gave mu N, while a graph-edge pair gave 21 nonzero output words and violated that restricted eigenvector formula.

The first run exited zero with no failure or retry: 2.319249 CPU seconds, 2.323393292 wall seconds, 21,233,664 bytes peak RSS, one thread. The declared envelope was 30 CPU seconds, 90 wall seconds, 150 MiB. Deadline/STOP and shared slot guards were observed. These finite controls corroborate the coefficient and domain construction; they do not compute an arbitrary-support commutant or prove general Markov invariance. Those assertions are the analytic arguments above. No author source, authority surface, branch, PR or audit state was changed.

## Scope stress test and no-go discipline

This is a scoped conditional compatibility result with an explicit positive escape, not a universal no-record packet. The required N-gate answers are retained here without claiming packet PASS.

- **N1, real approach families:** actual local-operator boundary extraction, Markov invariant-subspace/no-event analysis, and restricted physical-domain construction were attempted. Arbitrary site-dependent frames, infinite-tail encodings and non-Markov/history implementations remain unclassified; they are not invented failed routes. Fewer than five excluded approach families means the selected five-family no-go submission schema is not satisfied. No no-go PR or packet PASS is requested.
- **N2:** the theorems use different explicit class hypotheses, not an asserted list of independent walls. Removing all-state persistence admits the displayed code; allowing a changed Hamiltonian, nonlocal observable, or different record semantics changes the question. No pairwise logical independence or wall count is asserted.
- **N3:** all supplied carrier, basis, clock, quantum expectation, GKSL, full-domain and sharp-readout conditions are explicit. The constructive jump is added dynamics; it is not disguised as an axiom-derived rate. The actual Hamiltonian and its tensor placements are unchanged in every calculation.
- **N4:** the earlier spanning-frame theorem and temporal readout witness are prior comparisons, not witnesses against this new quantified class. The current Record wording controls the premise reading; removed finite additivity and old availability wording are not imported.
- **N5:** the commutant result covers one-site through every fixed finite block on the full carrier. It does not cover global or quasi-local charges, thermodynamic state-dependent memory, or all possible record instruments. The GKSL result concerns common sharp site markers and the stated preparation domain, not every meaning of permanence.
- **N6:** choosing a constrained domain or a different operational record realization may close part of the physical bridge without a new axiom. The existing approved primitives remain available within their actual grants. There is no claim that a new primitive is necessary.
- **N7:** the strongest counterargument is constructive: the actual independent-set code and guarded-birth law preserve markers extensively while keeping H0. This defeats any unrestricted statement that this Hamiltonian has no possible permanent-memory realization. It lies outside the all-state tests and leaves its low-energy/Admissibility/readout identification unproved.
- **N8:** earlier native fixed-readout ambiguities did not exclude temporal protocols; the new work preserves that escape and goes further by testing exact permanence. July's distinction between site-tagged and migrating records remains live. No closure of those broader alternatives is inferred.

The decisive results and their escapes are frozen for focused independent reconstruction. No downstream scientific reuse is authorized by the author run alone.
