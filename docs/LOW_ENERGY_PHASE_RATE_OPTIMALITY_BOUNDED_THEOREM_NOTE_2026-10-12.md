---
claim_id: low_energy_phase_rate_optimality_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "At each fixed nonzero time, sharp uniform energy-weighted phase exponents c^(2/3) and actual-energy-bounded vector exponent c^(1/3), witnessed by spacing-dependent even low-band packets."
upstream_dependencies:
  - energy_transfer_correlation_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
runner: scripts/low_energy_phase_rate_optimality_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Determine the attainable uniform exponents for the global mean-energy low-phase comparison."
source_of_blocker_text: frontier_question
next_trace_action: "Complete exact assembly review and source integration; retain stated model and observation hypotheses."
conditional_surface_status: "Supplied massive free chain and chosen Fock representation; Current remains open_gate."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit conditional asymptotic upper and lower estimates for specified norms and matrix elements; no fixed-state or full-correlation optimality claim."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem

Status: conditional-support

Primary runner: [source identity and reconstruction only](../scripts/low_energy_phase_rate_optimality_identity_2026_10_12.py).
It executes zero mathematical predicates or scientific mutations and supplies
no mathematical, N5 or audit certificate.

**Publication review record:** The complete 81-line phase proof and complete
205-line source-exposed review are archived at hashes
`255d378681114973fb0c2bed0ddcfbcab668a256ff091f801f3d800989250042` and
`a78dea4566d2046c3cf1da57e2cff5e111d46e14bbed00edd01453e50935e610`.
The reviewer found no failed load-bearing step. This was a same-family,
source-exposed ordinary check, not a separately sealed derivation, a formal
proof or an audit. Root reports having read and accepted that scoped outcome.
Final publication assembly review and execution acceptance remain pending.
The source's final pending-check paragraph below preserves author chronology.

**Review clarifications, separate from the unchanged source:** Choose packet
half-width r>0 and fixed M>0 for the mean-energy witnesses. The assertion
Theta(c^(2/3)) for the scalar refers to its absolute magnitude; its leading
signed value is -M/(v k) c^(2/3)[1+o(1)] with the stated matched bra. Interpret
Delta_c as the nonnegative joint spectral multiplier, not an unqualified
difference of unbounded operators on different domains. The compact packet
supports make all witness domain statements direct.

# Root probe: sharp energy-constrained low-phase exponents

Provisional ordinary mathematics in the supplied free chain, 2026-10-12.
This extends the frozen root phase estimate, after exposure to the independently
sealed transfer core. That core supplies a fixed-momentum growing-time witness,
not the scale-dependent fixed-time construction below. No novelty, formal
verification or independent-review claim is attached to this new probe.

Fix m,v,mu>0 and one t!=0. On the common low one-particle space let
E(p)=sqrt(m^2+v^2 p^2), with the actual band energy e_c and its purely
auxiliary extension e_c=E off |p|<1/c. The exact parent identity is

    e_c-E = v^2 c^2 p^4 / [(1+sqrt(1-c^2 p^2))^2(e_c+E)].

Put k=(4 pi/(v |t|))^(1/3), p_c=k c^(-2/3). Then c p_c tends to zero,
E(p_c)/(v p_c) tends to one, and (e_c+E)/(2v p_c) tends to one. Therefore

    |t| (e_c(p_c)-E(p_c)) -> pi/2.

The same holds uniformly on the two fixed-width intervals
p=+p_c+x and p=-p_c+x, |x|<=r, for any fixed finite r. All these
intervals lie in the actual finite band for small c; no outside-band
comparison extension participates in the example.

Choose normalized compactly supported one-particle profiles with width r,
translate one to +p_c and the other to -p_c, and denote them u_c,v_c.
Their supports are disjoint for small c, so phi_c=u_c wedge v_c has norm
one. It has even fermion parity. On its two-particle momentum support,

    t[(e_c(p)+e_c(q))-(E(p)+E(q))] -> sgn(t) pi

uniformly, and H0/(2v p_c) ->1 uniformly, where H0=dGamma(E).
Let Hc=dGamma(e_c), Uc=exp(itHc), U0=exp(itH0). Thus

    ||(Uc-U0)phi_c|| ->2,
    <phi_c,(exp(it(Hc-H0))-1)phi_c> ->-2.

For the two-sided weighted operator, simultaneous multiplication on this
support gives

    ||(H0+mu)^(-1/2)(Uc-U0)(H0+mu)^(-1/2)||
      >= (1+o(1))/(v p_c).

One can either take the essential supremum on this positive-measure support
or normalize a vector after applying (H0+mu)^(1/2) to phi_c. The oscillatory
common U0 phase does not change the operator norm. The root upper estimate
is O(c^(2/3)); this lower bound is a positive constant times c^(2/3).
The exponent is therefore sharp for this uniform weighted norm at each
fixed nonzero time. No optimal leading constant is asserted.

There is also an actual-energy-bounded even-state test. Fix M>0 and put

    h_c=<phi_c,Hc phi_c> ~ 2v p_c,
    eta_c=M/h_c,
    Psi_c=sqrt(1-eta_c)Omega+sqrt(eta_c)phi_c,

for small c when eta_c<1. Then ||Psi_c||=1 and <Psi_c,Hc Psi_c>=M,
while <Psi_c,H0 Psi_c><=M. The vacuum is annihilated by Uc-U0, so

    ||(Uc-U0)Psi_c|| ~ 2 sqrt(M/(2v p_c)) = Theta(c^(1/3)).

Consequently the energy-constrained vector exponent c^(1/3) cannot be
improved uniformly over such states. To test the two-sided scalar estimate,
take Phi_c=U0 Psi_c, which has the same norm and both energy expectations
because H0 and Hc commute. Then

    <Phi_c,(Uc-U0)Psi_c>
      =eta_c <phi_c,(exp(it(Hc-H0))-1)phi_c>
      ~ -2 M/(2v p_c) = Theta(c^(2/3)).

These are scale-dependent states and matrix-element vectors. They do not
claim a slow rate for every fixed smooth local observable, a fixed density,
or the full correlation theorem. They distinguish a global mean-energy
resource bound from a fixed compact-momentum/particle window, where the
earlier O(c^2) phase estimate remains valid. At t=0 every discrepancy is
zero. Infinite-time, massless, thermal-density and interacting claims are
outside scope.

Pending independent checks: the uniform scaling expansion, the weighted
norm lower bound and the even-state normalization. This file is a source
probe only; no scientific runner, Lean certificate or audit was executed.


## Publication dependency and quantifier record

The [energy-controlled correlation note](ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
section 7, supplies the exact global upper phase estimates and their energy
weight conventions. [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the actual low-band dispersion and chosen representation embedding.
The correlation note's Concrete and Local Even imports supply the full Fock
and real CAR conventions transitively. These links give two direct dependency
edges for this companion, with no cyclic dependence: the correlation theorem
does not use this sharpness source.

For k=(4 pi/(v |t|))^(1/3), the reviewed calculation gives on both translated
packet supports e_c-E=pi/(2|t|)+O(c^(2/3)), uniformly. The weighted norm is at
least [1+o(1)] c^(2/3)/(v k), including on the even restriction; the earlier
upper bound has the same exponent. The actual-energy-M vector discrepancy is
2 sqrt(M/(2v k)) c^(1/3)[1+o(1)], and the matched two-vector scalar has absolute
magnitude M c^(2/3)/(v k)[1+o(1)]. These are conditional asymptotic existence
statements, not an optimal leading constant.

The witnesses depend on spacing, their momenta escape to infinity while
remaining in the actual low band, and their pair occupation tends to zero.
They leave the fixed ordinary smooth-cell, fixed-state and complete-correlation
rates open. Compact momentum/particle windows retain their stronger phase
estimate. At t=0 the discrepancy is zero; M=0 gives only the vacuum in this
massive representation. No uniform large-time, massless or interacting result
is asserted.

The complete original source is unchanged between this wrapper's header and
appendix; PUBLICATION_EDITS.json reconstructs it exactly. The completed review
is fully archived with its chronology. Final assembly review remains pending.
The [No-Go Discipline Gate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/3679df3c7901b4660f5d9e9d69023e2e82772a83/.claude/science/physics-loops/toe-energy-correlations-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps formal negative-packet N1/N5 readiness pending. The explicit witnesses
are positive scoped constructions; no unrestricted route exhaustion or packet
PASS is claimed. There is no audit, Lean or retained-status claim.
