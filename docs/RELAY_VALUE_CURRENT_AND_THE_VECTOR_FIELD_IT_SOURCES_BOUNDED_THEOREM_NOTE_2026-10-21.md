---
claim_id: relay_value_current_and_the_vector_field_it_sources_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional link-count continuity and polynomial divergence identity for a supplied homogeneous second-order vector ansatz, with explicitly normalized nonzero-momentum static solution and nonzero-exchange coupling implication."
upstream_dependencies: []
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Physical charge assignments, field selection and lattice dynamics remain open; downstream consumer not yet known."
source_of_blocker_text: review_loop
reachability_to_target: "Continuity and imposed off-shell divergence identity do not select a unique physical field theory."
conditional_surface_status: "Exact conditional counting and polynomial algebra; finite packet illustration."
hypothetical_axiom_status: "none adopted"
admitted_observation_status: "none"
claim_type_reason: "Explicit event-counting proof and supplied-ansatz coefficient calculation with domains."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: "Conditional algebraic support; downstream consumer not yet known."
next_trace_action: "Justify any physical charge or field-selection bridge independently before using it."
runner: scripts/relay_value_current_and_the_vector_field_it_sources_2026_10_21.py
---

# Supplied value-current continuity and vector-operator identity

Claim type: bounded_theorem.
Primary runner: `scripts/relay_value_current_and_the_vector_field_it_sources_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), with zero premise weight, and [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are context only. Neither supplies the read-once/stepping clauses previously attributed to the register. The minimal axioms permit continuous possibility domains; discrete record outcomes or discrete charges do not follow. A finite charge menu is an optional supplied model, not a deduction.

## Conditional value-current identity

Supply labelled relays with fixed carried real values q, no creation or destruction, and one link traversed per tick. Define density at a site as the sum of carried values present, and oriented link current as the sum crossing per tick. Every outgoing event removes exactly its q at the departure and adds it at the arrival; summing gives density change = inflow - outflow identically. The same identity holds in expectation by linearity, including signed unequal fixed q. No read-once or charge-quantization premise is inferred.

The separate numerical illustration supplies Born-style expected weights from a six-direction unitary coin and periodic shift, constant q=1, packet width 3, phase .4 x, seed 4 and coin angle .3. It checks six ticks on 24³ sites. Local coin norm preservation makes outgoing expected value equal current density, and the shift gives incoming expected value at the next tick. Agreement to rounding is a finite check, not a derivation of a realized relay process. No comparison with an unbound record-source model is asserted.

## Supplied vector ansatz and identity

Consider the supplied linear, translation-invariant, constant-coefficient, homogeneous second-order Lorentz-covariant ansatz, with eta=diag(-1,1,1,1):

    O(A)_n = a k² A_n + b k_n (k.A).

Impose the off-shell polynomial identity k.O(A)=0 for every k,A, so the field equation introduces no additional divergence constraint on A. Direct contraction gives (a+b) k²(k.A); the identity therefore fixes b=-a. The overall scale a remains arbitrary, including the zero operator. For a nonzero response one must separately require a!=0; normalization a=1 is supplied. Pure-gauge A=k xi is annihilated by this family.

Conserved source alone does not impose that off-shell identity. For example adding -m² A gives divergence -m²(k.A); with m!=0 a conserved source instead requires k.A=0. This is a constraint on solutions, not an exclusion of massive vector theories. No uniqueness over all compatible field theories is claimed.

## Normalized static particular solution

Supply a=1, b=-1, k0=0, source convention O_0=-q and O_i=0, Coulomb gauge sum_i k_i A_i=0, and nonzero spatial momentum. Then O_0=|k|² A_0 gives the covariant component A_0=-q/|k|², and O_i=|k|² A_i gives A_i=0. This is the selected rational particular solution, without homogeneous additions. For general nonzero a the component is -q/(a|k|²). At |k|=0 a nonzero q is incompatible with these equations; the zero operator cannot source nonzero q either. An inverse-Fourier 1/r potential additionally requires continuum infinite-space boundary conditions and Fourier normalization, which the runner does not establish.

## Nonzero-exchange implication

Supply two component currents whose divergences are J and -J, and impose conservation of their weighted source e1 J1+e2 J2. Then (e1-e2)J=0. For nonzero J this implies e1=e2; at J=0 arbitrary e1,e2 satisfy it. Along exchange-connected species this condition propagates equality within that specified exchange model; disconnected sectors and additional current contributions lie outside it. No universal physical coupling value follows.

## Review record and scope

Original PR9843 head 2a72b995a79c426be91c45573e57a956686a18e4 preserves the false discrete-outcome and register attributions and missing domains. They are withdrawn or explicitly narrowed here. All relay rules, values, expected weights, walk/packet, continuum ansatz, off-shell identity, sign conventions and normalization are supplied choices. No physical gauge group, charge spectrum, vector response on lattice links, lattice field dynamics, empirical identification or audit status is established.
