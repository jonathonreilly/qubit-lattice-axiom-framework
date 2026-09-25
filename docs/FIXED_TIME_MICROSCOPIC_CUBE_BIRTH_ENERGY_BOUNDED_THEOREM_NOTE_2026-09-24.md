---
claim_id: fixed_time_microscopic_cube_birth_energy_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Conditional joint spin/scale limit for the original compensated cube and actual zero-field first birth:
  the birth-scaled mean vanishes after many fast times on bounded physical-time intervals, and the birth-scaled
  second moment and variance vanish uniformly for all later times.'
upstream_dependencies:
- actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- minimal_axioms
- rotor_cube_fast_energy_strong_decay_without_uniform_decay_bounded_theorem_note_2026-09-24
runner: scripts/fixed_time_microscopic_cube_birth_energy_2026_09_24.py
---

# Microscopic cube birth energy after the fast time scale

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

This is conditional mathematics for the explicitly supplied compensated quantum
cube, its original formation instrument and specified preparation. It does not
select a physical law or change the framework premises. The exact proof below
concerns the microscopic Hamiltonian and includes the possible second birth.

## Statement and supplied model

The cube has A={0,3,5,6}, B={1,2,4,7}, and A-to-B edges between binary vertices
that differ in one bit. Site charges are q=0,+1,-1 with hard-core occupancy.
Integer-spin fields E_e in [-S,S] obey div E=q-1_A. An outward charge-s hop on
an occupied-A/empty-B edge changes E_e to E_e-s and has amplitude
sqrt(1-E_e(E_e-s)/C), C=S(S+1). Its adjoint is the inward hop. Let F_a sum outward hops from a, F=sum_a F_a,
T=-(F+F^dagger), W=sum_(a in A)(1-n_a), and P=1_(W=0).

On this cube the supplied gated compensation is exactly

    C_S=P F^dagger F P + P(D/C)P,
    D(q,E)=sum_(a in A,b~a,q_b=0) E_ab(E_ab-q_a) on P.

It vanishes on every W>0 sector. The full microscopic Hamiltonian is

    H=delta epsilon^-4 h,    h=W+epsilon T+epsilon^2 C_S.

A resolved birth j_(e,s) on an empty edge creates charges (s,-s), changes E_e
to E_e+s and has amplitude sqrt(1-E_e(E_e+s)/C). A coherent edge mark is the
stipulated sum of its two resolved signs. The jumps in the original GKLS law
are L_j=sqrt(kappa)/epsilon j, with either all resolved marks or all coherent
edge marks. Spin-boundary moves have their actual zero amplitudes. No energy
filter or replacement of this instrument is introduced.

Let Omega have all A charges +1, B empty and E=0. U_epsilon is the canonical
positive-overlap rotation from P to the low spectral band of this Hamiltonian.
At time zero prepare the actual normalized first-mark output on edge 01,

    phi_i=j_i U_epsilon Omega/||j_i U_epsilon Omega||,

for i equal to resolved plus, resolved minus or coherent sum. rho_i(t) is the
complete subsequent GKLS ensemble, including the possible second birth. Fix
positive delta,K,kappa and take integer S->infinity with epsilon^2 C=delta/K.
Let a_epsilon>=0 satisfy a_epsilon/epsilon^2->infinity.

Write Pi_r=1_(W=r), B_i=j_i F Omega, R_i=-F_0 B_i, b_i=||B_i||^2 and
ell_i=||R_i||^2/b_i. The triples (b_i,||R_i||^2,ell_i) are (2,4,2),
(2,2,1) and (4,6,3/2); these zero-field vectors and coefficients are independent
of S>=1. On N=6,W=1 define G_S=Pi_1(FF^dagger-F^dagger F)Pi_1 and
Gamma_(1,S)=Pi_1(sum_j j^dagger j)Pi_1. Their rotor limits are G and Gamma_1.
They act on the full physical charge/integer-field space, with unit rotor shifts;
no individual Fourier fiber is used as a physical state.

**Theorem.** For every fixed finite T with a_epsilon<=T eventually,

    sup_[a_epsilon,T] |epsilon^2 Tr(H rho_i(t))/delta| ->0,

and, without a finite upper-time restriction,

    sup_(t>=a_epsilon) epsilon^6 Tr(H^2 rho_i(t))/delta^2 ->0,
    sup_(t>=a_epsilon) epsilon^6 Var_rho_i(t)(H)/delta^2 ->0.

In particular the statements hold uniformly on every fixed [t0,T] with t0>0.
At birth the scaled mean and variance tend to ell_i=2,1,3/2, respectively.
The theorem supplies disappearance of those leading scales after many fast
times. Boundedness or convergence of the unscaled energy and variance, a decay
rate, and physical heat or work accounting remain open.

## Exact original no-event representation

In N=6 the full no-event propagator at physical time is

    K_e(t)=exp[-i delta epsilon^-4 h_eff t],
    h_eff=W+epsilon T+epsilon^2(C_S-i kappa Gamma/(2 delta)),
    Gamma=sum_j j^dagger j >=0.

It is a contraction for every t>=0, exactly: d||K_e(t)v||^2/dt
=-kappa epsilon^-2 <K_e(t)v,Gamma K_e(t)v> <=0.
After the next birth N=8 and W=T=C_S=Gamma=0. Therefore, with v(t)=K_e(t)phi_i,

    Tr(H^m rho_i(t)) = delta^m epsilon^-4m <v(t),h^m v(t)>, m=1,2.

This is an unnormalized no-event vector representing full ensemble energy moments.
It is not conditioning away the second birth or renormalizing survival probability.

## A monotonic bound for exact spectral clusters

Use fixed contours around W grades r=0,1,2. Let P_r be the orthogonal spectral
projectors of h and E_r the Riesz projectors of h_eff. Uniformly in S and small
epsilon the uniform bounded perturbations and integer gaps give

    ||E_r-P_r|| <= c epsilon^3,
    ||E_r|| <= 1+c epsilon,        [E_r,K_e(t)]=0.

The first estimate follows because the imaginary perturbation is epsilon^2 times
Gamma, and [Gamma,W]=0: its nominal second-order contour term has only double
poles and integrates to zero. The remaining resolvent Neumann series is uniformly
O(epsilon^3). This is the projector identity in the compact-fast-time parent.

Even though E_r is not orthogonal, E_r v(t)=K_e(t-s)E_r v(s). Contraction therefore
gives the exact inequality

    ||E_r v(t)|| <= ||E_r v(s)||,   t>=s>=0.                 (A)

No claim that the Hermitian band weight ||P_r v(t)||^2 is monotone is used.
The parent output expansion and compact-fast-time evolution give, for fixed tau,

    epsilon^-2 ||E_1 v(epsilon^2 tau)||^2 -> f_i(tau),
    ||E_2 phi_i|| = O(epsilon^2),
    f_i(tau)=||exp[tau(-i delta G-kappa Gamma_1/2)] R_i||^2/b_i.

All initial estimates are uniform in S. The parent proves the first limit on
compact tau intervals, and the rotor-tail theorem proves f_i(tau)->0 as tau->infinity.
For any fixed tau and all small enough epsilon, epsilon^2 tau<a_epsilon. Applying (A)
then the projector comparison, uniformly for every t>=a_epsilon, gives

    limsup_joint sup_[a_epsilon,infinity) epsilon^-2 ||P_1 v(t)||^2 <= f_i(tau),
    sup_[0,infinity) epsilon^-2 ||P_2 v(t)||^2 = O(epsilon^2).

For the first inequality, the O(epsilon^3) difference produces O(epsilon^2)
after squaring and dividing by epsilon^2, because (A) also bounds E_1 v by O(epsilon).
The corresponding P_2 correction is smaller. Let tau tend to infinity only AFTER
taking the limsup. Hence

    sup_[a_epsilon,infinity) epsilon^-2 sum_(r=1,2) ||P_r v(t)||^2 ->0.   (B)

This uses no growing-time perturbation expansion, no finite-spin spectral-gap
claim and no assumption of uniform rotor decay over inputs.

## Low-band energy and strong tightness

Let U be the canonical Hermitian cluster rotation; ||U-I||=O(epsilon), and

    Pi0 U^dagger h U Pi0 = epsilon^2 Q_S+epsilon^4 H4_S+O(epsilon^6),
    Q_S=D/C >=0,  C=S(S+1),  sup_S ||Q_S||<infinity.

Here Q_S is extended by zero outside the physical spin box and outside Pi0.
On the common rotor word space Q_S converges strongly to zero: this is immediate
on every finite-support word (D is fixed, C->infinity), then on all vectors by
its common norm bound. It does NOT converge to zero in operator norm.

The actual phi_i differs by O(epsilon) in norm from beta_i=B_i/sqrt(b_i), a
fixed finite-support P vector. GKLS contraction, the uniform microscopic target
theorem and the common compensated rotor density limit imply

    sup_[0,T] ||rho_i(t)-rho_rot,i(t)||_1 ->0               (C)

under the canonical zero extension, with initial |beta_i><beta_i| on N=6.
Taking the N=6 corner, sigma_i(t)=|v(t)><v(t)|, preserves this convergence.
The limit is a continuous trace-class path. Strong convergence Q_S->0, its
uniform bound and finite-rank approximation give Tr(Q_S sigma_rot,i(t))->0
uniformly on [0,T]; compactness of the continuous path makes this uniform.
Equation (C) then gives

    sup_[0,T] <v(t),Q_S v(t)> ->0.                         (D)

Moving v into canonical low coordinates changes this expectation by O(epsilon),
using ||U-I||=O(epsilon), Q_S=Pi0 Q_S Pi0 and ||v||<=1. Thus the scaled low-band
mean tends uniformly to zero. This use of density convergence is legitimate
only because Q_S has a uniform norm bound; it is not density convergence
applied to H, whose norm diverges as epsilon^-4.

## Assembly of the two moments

The high Hermitian bands have uniformly bounded h and h^2. Their contributions
to epsilon^-2 <v,h v> and epsilon^-2 <v,h^2 v> vanish by (B). In the low band,
epsilon^-2 h equals Q_S+O(epsilon^2), so (D) proves the mean assertion. Its
squared operator satisfies ||epsilon^-2 h_low^2||=O(epsilon^2), proving the
second-moment assertion without an unbounded low-field moment assumption.
Finally 0<=Var(H)<=Tr(H^2 rho) proves the variance assertion. The Hamiltonian
need not be positive; the low part is bounded below by -O(epsilon^4) in h,
and the first conclusion uses absolute value and the explicit low-band bound.

## Limits and next question

The order-of-limits issue is addressed by the exact commuting-cluster inequality,
not by substituting tau=t/epsilon^2 in a compact-tau formula. The mean conclusion
is uniform on [a_epsilon,T] whenever a_epsilon/epsilon^2
tends to infinity and T is fixed. The second-moment and variance conclusions are
uniform for all t>=a_epsilon: their low-band bound uses only the common operator
bound on Q_S and exact contraction, so it needs no finite-time density limit.
All statements use the zero-field prepared input, lambda=0, fixed cube and positive
fixed parameters.
Moving high-flux input families, changing lambda, growth of graph size, individual
survival-conditioned energies, an unscaled mean/variance limit, a quantitative
rate and a physical reservoir remain open. The second birth and matter sector
have remained in the full ensemble throughout.

## Proof obligations and evidence boundary

| Obligation | Source and disposition |
| --- | --- |
| Exact terminal zero Hamiltonian and canonical actual-output coefficients | Supplied-model parent, with its original instrument and preparation |
| Uniform Riesz projectors and their third-order comparison | Parent contour argument restated above |
| All-time contraction of each exact no-event component | Proved here by commutation and the semigroup property |
| Strong rotor decay for the fixed high component | Conditional rotor-tail theorem; its charge-hop rank certificate was separately reconstructed for this check |
| Uniform density limit for the compensated model | Conditional microscopic target and common field/record limit; used only against uniformly bounded Q_S |
| Uniform vanishing of the two scaled moments | Proved above by spectral separation and the low-band estimate |

The strongest remaining energy question is a bound or limit for the unscaled
microscopic mean and variance at fixed positive time. This proof does not end
at that stronger assertion or use it as a premise. The zero-rate endpoint,
moving high-flux inputs, changing electric completion, other graphs and volume
limits require separate arguments.

The primary runner enumerates the complete physical spin-one N=4,6,8 spaces,
uses the actual canonical preparation, and checks contour refinement, the
non-Hermitian projector comparison, grade identification on the actual outputs,
commutation and decreasing component norms.
It computes microscopic first and second moments at three finite epsilon values
and fixed physical-time samples. These are finite numerical consistency checks;
they do not certify a spin-to-infinity or infinite-time limit. Its matrix
construction reuses selected definitions from a previous independent cube
builder and is fully included in the primary runner. This reuse is explicit;
the new primary computation is an author control, not an independent derivation.

A separate three-state dissipative example has increasing orthogonal high-band
weight and decreasing oblique component norm. A two-state density family has
trace distance 2/n from its limit and energy n under diag(0,n^2). These are
explicit finite examples used to distinguish the estimates in this proof.

Run:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fixed_time_microscopic_cube_birth_energy_2026_09_24.py
```

## Imports

The Hamiltonian, compensation, spin-link realization, GKLS instrument, scale
relation and canonical zero-field preparation are supplied model hypotheses.
A native derivation or physical selection of them is not established here.

- [Actual cube birth on the fast time scale](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the actual output, terminal sector and uniform cluster estimates.
- [Strong rotor decay](ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies decay for each fixed normalizable high input, with its complete physical Fourier representation.
- [Common compensated field/record limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies strong trace-class convergence for the complete supplied dynamics.
- [Bounded compensation target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the uniform microscopic approximation and canonical low Hamiltonian coefficient.

All four imports retain their conditional mathematical hypotheses. No retained
audit grade is inferred from their presence on main or from this independent check.

## Review record — historical author provenance

The root authored and sealed the first argument before releasing it to a separate
checker. The checker reconstructed the fixed-time result and exact supporting
rotor paths before author disclosure; PRE.md is sealed by SHA-256
1681b7333d6244bcad00b8b287b6fd0e621c466a0d1b61d0c53295edd1576e58.
It also identified the moving-lower-endpoint and all-future moment refinements,
which the root reconstructed directly from the same uniform inequalities.
Released-source comparison and final publication checks are recorded in the
committed review packet. This is scientific checking, not a formal audit verdict.

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: fixed_time_microscopic_cube_birth_energy_bounded_theorem_note_2026-09-24
target_blocker_text: "The compact-fast-time energy result and sequential rotor decay did not control microscopic energy at fixed positive physical time."
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Bound the unscaled energy and variance while retaining the finite-spin dynamics and the original formation instrument."
conditional_surface_status: "Supplied finite cube quantum model, compensation, scale relation, marks and preparation."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The joint-limit conclusion is proved under explicit supplied-model hypotheses; no physical law is selected."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Landing-review boundary and No-Go Discipline Gate

N1: the supplied compensated cube, zero-field first-mark preparation, positive fixed parameters and stated joint scaling. N2: other preparations, models and scalings remain open. N3: compensation, quantum dynamics and the instrument are supplied mathematical hypotheses. N4: the linked parents retain their exact domains and order of limits. N5: finite spin-one numerics corroborate the argument; they do not execute the joint or infinite-time limits. N6: unscaled energy, moving high-field states and physical energy accounting remain separate. N7: trace-norm convergence alone cannot control an unbounded energy; the proof instead uses the uniformly bounded D/C. N8: strong rotor decay is converted using an exact commuting-cluster contraction, not a growing-time substitution.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive this supplied dynamical model.

Historical author seals and comparisons are provenance only. Review does not apply an audit verdict or retained grade. The complete original packet remains recoverable at PR #9038's frozen head. Fresh finite controls execute in a temporary output directory and print their scientific results into the canonical capture.
