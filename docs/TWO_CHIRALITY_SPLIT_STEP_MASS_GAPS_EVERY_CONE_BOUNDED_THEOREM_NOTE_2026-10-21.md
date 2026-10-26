---
claim_id: two_chirality_split_step_mass_gaps_every_cone_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Exact spectra at the original zero-cone points of a supplied folded single-particle walk; separate finite zone scans and six dispersion samples, without a continuous-zone gap theorem."
upstream_dependencies: []
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A downstream physical consumer is not yet known; a continuous-zone gap proof is absent."
source_of_blocker_text: review_loop
reachability_to_target: "Cone-point identities do not establish a full-zone gap or physical lattice realization."
conditional_surface_status: "Exact original-cone spectra under the supplied walk and coin; finite evidence elsewhere."
hypothetical_axiom_status: "none adopted; model choices are supplied conditions"
admitted_observation_status: "none"
claim_type_reason: "Explicit conditional cone-point proof, with numerical illustrations separately scoped."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: "Conditional algebraic support; downstream consumer not yet known."
next_trace_action: "If a full-zone claim is pursued, prove a continuous-zone bound or preserve a counterexample."
runner: scripts/two_chirality_split_step_mass_gaps_every_cone_2026_10_21.py
---

# Exact original-cone spectra and finite scans for a supplied split-step walk

Claim type: bounded_theorem.
Primary runner: `scripts/two_chirality_split_step_mass_gaps_every_cone_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), with zero premise weight, and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are context only. Neither derives this walk.

## Supplied model and imports

The carrier is the linear single-particle space l²(Z³) tensor C⁴, with two two-component blocks called L and R. It is not a tensor-product qubit lattice. Set U_L(k) = S_z S_y S_x, S_i = cos(k_i) I - i sigma_i sin(k_i), and U_R(k) = U_L(-k). A tick first applies exp(-i[m + M(-1)^(x+y+z)] beta), with beta exchanging L and R, then applies the block walk. Staggering folds (k,k+Q), Q=pi(1,1,1), into an eight-dimensional sector. Ordering, carrier, Pauli matrices, block reversal, coin, dimensionless real angles and finite sampling choices are supplied mathematical definitions; no physical provenance or bridge is established.

## Exact original-cone theorem

Write a(k) = tr(U_L)/2 = cx cy cz + sx sy sz. For fixed x,y,

    a(k) <= sqrt(cx² cy² + sx² sy²) <= 1.

Equality in the second inequality requires (cx²,cy²)=(1,1) or (0,0); equality in the first fixes z and the product sign. Thus U_L=I precisely at four integer-pi points with cosine product +1 and four half-integer-pi points with sine product +1, modulo 2pi. Direct differentiation of the Pauli coefficients gives local Weyl velocity determinants +1 and -1 respectively. Chirality here means the sign of that determinant. Momentum reversal reflects these sets and reverses the determinant signs. L and R therefore share the four integer-pi points with opposite chirality; Q maps the unshared L points to the unshared R points.

In the folded basis let rho act on (k,k+Q), tau on (L,R), and suppress spin identity. U_L(k+Q)=-U_L(k). The commuting coin generators are A=tau_x and B=rho_x tau_x, so U=D exp(-imA) exp(-iMB).

At a shared cone, D=rho_z. In a tau_x=t sector, U=exp(-itm) rho_z exp(-itM rho_x). The last two factors square to I and have eigenvalues ±1. The spectrum is therefore ±exp(±im), with original shared cone-point gap dist(m,pi Z), independent of M.

At an unshared L cone, D=rho_z tau_z; it anticommutes with A and commutes with B. In a B=b sector, U=exp(-ibM) D exp(-imA), whose last factors again square to I. Its spectrum is ±exp(±iM), with gap dist(M,pi Z), independent of m. The unshared R cone gives the same spectrum.

Consequently M=0 leaves eigenvalue +1 at the unshared points for this specified coin. Both m and M outside pi Z remove +1 at every original zero-cone point. Nonzero angles alone are insufficient: resonant multiples of pi have zero gap. Continuity gives a positive gap in some neighborhood of each such point, but neither excludes new zeros elsewhere nor supplies a continuous-zone minimum. This is not a statement about all possible mass modifications.

## Separate finite illustrations

The runner's 40³ cone scan illustrates the classification; the proof above supplies completeness. On the supplied 25³ zone grid, minimum absolute eigenphase agrees within the stated tolerance with .05 for (m,M)=(.05,.5) and .02 for (.02,1). A finite mesh minimum is only an upper bound on the continuous-zone infimum; no full-zone positive lower bound is proved.

At exactly m=.02, M=.5, the runner compares sqrt(m²+cos(M)²|k|²) with the lowest absolute eigenphase at |k|=.02 and .04 along normalized (1,0,0), (1,1,0), (1,1,1): six samples agree within 1.5%. This is a finite directional comparison, not uniform dispersion or isotropy. Preserve the contrasting M=1, m=.02, k=.04(1,1,1)/sqrt(3) case: eigenphase .0287692287470575 versus comparator .0294462651411395, a 2.299% discrepancy. Fixed nonzero m can have direction-dependent curvature.

Every complete ordered shift changes all three position coordinates by odd integers; x-y and x-z modulo 2 are invariant, while the onsite coin preserves position. This yields four invariant sublattice classes for this supplied walk, without identifying physical species.

## Review record and scope

The original global-gap and uniform-dispersion wording is narrowed to the exact cone-point identities and explicitly finite scans. The original source remains recoverable at PR9840 head 0b32ff7a72da28fb40c691010dea793042be1bf9. No matter content, tensor-product one-qubit realization, exact cubic covariance, physical mass value or audit status is established. The continuous-zone proof and physical identification remain open.
