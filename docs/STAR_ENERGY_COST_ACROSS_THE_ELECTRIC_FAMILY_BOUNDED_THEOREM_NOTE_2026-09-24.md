---
claim_id: star_energy_cost_across_the_electric_family_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - local_electric_completions_and_postbirth_field_phase_bounded_theorem_note_2026-09-24
  - exact_microscopic_energy_at_a_star_birth_bounded_theorem_note_2026-09-24
  - finite_time_star_energy_and_supply_bound_bounded_theorem_note_2026-09-24
runner: scripts/star_energy_cost_across_the_electric_family_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Star birth energy across the local electric family

Personal conditional bridge calculation, 2026-09-24; independent reconstruction
pending. The positive terminal-field completion is a different question from the
microscopic energy carried by the original formation channel. This exact star
calculation relates them without changing that channel or selecting lambda.

## 1. Same supplied family, common finite-energy preparation

Use the physical star A={0}, B={1,2,3}, div E=q-1_A, with integer S>=1. The
Gauss constraint gives E_0b=-q_b. On this entire sixteen-state physical sector,
D_ext=0 because every active outward edge ends at an empty leaf with E=0.
The previously supplied electric family is

`C_S^lambda=C_S+lambda(E2-D_ext)/[S(S+1)]`, `0<=lambda<=1`.

At `epsilon² S(S+1)=delta/K`, its full microscopic Hamiltonian is exactly

`H_lambda=H_0+K lambda E2`,

where H_0 is the positive square Hamiltonian in the original exact-star note.
Since E2 is the number of occupied leaves, it obeys

`E2|_(N=1)=W`, `E2|_(N=3)=2I+W`.

In particular the addition is bounded by 3K on this entire physical space.
All original resolved/coherent j and their epsilon scaling are retained.

Choose the same explicit preparation for every lambda:

`psi=(g+epsilon Fg)/sqrt(a)`, `a=1+3epsilon²`.

It has zero H_0 energy, but it is not an exact eigenstate of H_lambda for
lambda>0. Its actual initial energy is

`E_initial(lambda)=3K lambda epsilon²/a`.                       (1)

It tends to zero. Thus the preparation does not hide a divergent initial energy
supply. No assertion of exact low-cluster preparation for the changed law is
needed. The initial density still approaches gg* in trace norm.

## 2. Exact actual-output moments

The unchanged marks give precisely the same immediate normalized states v as
in the exact-star note. Every such state lies in the N=3 P space, so E2 v=2v.
Although H_0 and E2 do not commute on the full space,

`H_lambda v=H_0 v+2K lambda v`.

Consequently its mean and variance are exactly

`mean(H_lambda)=c delta/epsilon²+2K lambda`,

`Var(H_lambda)=c delta² epsilon^-6 [1+(3-c)epsilon²]`,            (2)

where c=2 for a plus resolved mark, c=1 for a minus resolved mark, and c=3/2
for a coherent edge mark. The lambda addition changes the mean by a scalar on
the immediate output but leaves this variance unchanged. This argument uses the
norm of H_lambda v, so it retains the entire high-energy spectral contribution.
It does not assume that the new spectrum still has only the two old energies.

The total initial intensity is still `12kappa/a`. The initial full GKLS energy
derivative is

`d mean(H_lambda)/dt|0 = 18kappa delta/(epsilon² a)+12kappa K lambda/a`. (3)

Here the gain is `18kappa delta/(epsilon²a)+24kappa K lambda/a`, and the
loss contribution is `-12kappa K lambda/a`. For lambda>0 the loss-energy term
cannot be omitted by carrying over the old zero-energy-eigenstate argument.
The Hamiltonian contribution to its own energy remains zero.

## 3. Exact finite-time relation and its asymptotic

The no-event state again remains in span(g,s), s=Fg/sqrt(3). Its two-by-two
generator is the earlier G plus `-iK lambda diag(0,1)`. Write this G_lambda,
`v_lambda(t)=exp(tG_lambda)ell`, and `P_b,lambda(t)=1-||v_lambda(t)||²`.
Each possible first mark still produces the same normalized output with the
same instantaneous relative mark weights. No second microscopic birth is
possible. Subsequent N=3 evolution conserves its H_lambda energy. Therefore

`E_total,lambda(t)=E_no,lambda(t)`
`                +[3delta/(2epsilon²)+2K lambda] P_b,lambda(t)`,     (4)

`E_no,lambda(t)=<v_lambda(t),H1,lambda v_lambda(t)> >=0`.

Positivity follows from H_0>=0 and K lambda E2>=0. This is an exact finite-time
identity for both instruments.

The scaled characteristic polynomial of G_lambda is

`epsilon⁴ z²+[i delta a+2kappa epsilon²+iK lambda epsilon⁴]z`
`             +i6kappa delta-3delta K lambda epsilon²=0`.

The root continuous from -6kappa is

`z_s=-6kappa+[18kappa-i(12kappa²/delta+3K lambda)]epsilon²`
`                    +O(epsilon⁴)`.

In the old orthonormal low/high coordinates, its low diagonal entry is
`-6kappa/a-i3K lambda epsilon²/a`. The off-diagonal entry is
`2sqrt(3)kappa/(epsilon a)+i sqrt(3)K lambda epsilon/a`; the large imaginary
high diagonal remains of order epsilon^-4. The same eigenvector argument as in
the finite-time star note gives high amplitude O_T(epsilon³), low amplitude
`exp(-6kappa t)+O_T(epsilon²)`, and therefore

`P_b,lambda(t)=1-exp(-12kappa t)+O_T(epsilon²)`,

`E_no,lambda(t)=O_T(epsilon²)`.

For each fixed lambda in [0,1], fixed positive K,delta,kappa and each fixed t>0,

`epsilon² E_total,lambda(t) -> (3delta/2)[1-exp(-12kappa t)]`,       (5)

or `E_total,lambda(t)/[S(S+1)] -> (3K/2)[1-exp(-12kappa t)]`.
The leading cost is the same throughout this family. This is a finite-star
statement, not a general-graph uniform theorem.

## 4. Consequence for a proposed energy account

For an additional proposed energy-conserving dilation with nonnegative
reservoir energy, reproduction of the microscopic system energy requires

`E_R(0) >= E_total,lambda(t)-E_initial(lambda)`
` >= [3delta/(2epsilon²)+2K lambda] P_b,lambda(t)-3K lambda epsilon²/a`. (6)

A bounded interaction allowance changes the left side to E_R(0)+2||V|| under
the conservation hypothesis stated in the preceding finite-time note. These are
resource inequalities under explicit extra assumptions, not a construction of
that dilation and not a prohibition on resources growing with S.

The electric completion can change target postbirth phases while leaving this
microscopic resource scaling intact. It therefore does not by itself supply an
energy source for the original birth instrument. This conclusion does not
reject the family as a supplied effective model or select a member. A reservoir,
additional microscopic degrees of freedom, changed energy law or controlled
moment approximation would have to be stated and examined separately.

## 5. Evidence and limits

The standalone symbolic control reuses the pinned root star matrices and checks
(1)-(3), the new two-by-two polynomial and its slow root through epsilon².
The analytic symmetry and eigenvector argument supply (4)-(5); a finite collection
of epsilon values is not used to infer them. The output variance is checked
from complete twelve-dimensional Hamiltonian action. The reuse is recorded as
author consistency evidence, not independent review.

The conditional common target on this star is zero in N=1 and 2K lambda in
N=3; its energy is finite. This does not identify its energy moments with those
of the microscopic Hamiltonian. The star has no cycle and can form only once.
No general cube leakage coefficient, infinite-volume result, autonomous
reservoir, empirical particle law, native selection or audit status is claimed.


## Attributed uniform-family proof contribution

The following mathematical argument was authored in the submission’s electric-robustness reconstruction packet. It is retained as proof source and reviewed on its content; the packet’s label confers no audit or review authority. Its uniform-in-lambda estimate is used by the supplied battery and clock constructions. In this section ell=lambda K, d=1+3epsilon², Omega=delta epsilon^-4, and the no-event state is alpha*g+beta*Fg/sqrt(3).

## Controlled fixed-positive-time singular scaling

Here is a direct uniform estimate from (11). It avoids applying a P-initialized
effective theorem to the partly W=1 initial state. Put

    gamma=2kappa epsilon^-2, q=ell-i gamma,
    z(t)=beta(t)-sqrt(3)epsilon alpha(t),
    w=Omega d+q.

The exact equations and initial condition are

    i alpha'=-sqrt(3)Omega epsilon z,
    i z'=w z+sqrt(3)epsilon q alpha,
    z(0)=0.                                          (15)

No-event contractivity implies |alpha(t)|<=1. Duhamel followed by one
integration by parts in its scalar fast exponential yields, for any T,

    sup_(0<=t<=T)|z(t)| <= 2A_epsilon
                              +B_epsilon sup_(0<=t<=T)|z(t)|,
    A_epsilon=sqrt(3)epsilon |q|/|w|,
    B_epsilon=A_epsilon sqrt(3)Omega epsilon/gamma.    (16)

Indeed the integration-by-parts boundary terms are bounded by two, and the
remaining convolution of |alpha'| is bounded by its supremum divided by gamma.
Since ell belongs to [0,K], |w|>=Omega d, giving uniformly in lambda

    A_epsilon=O(epsilon^3), B_epsilon=O(epsilon^2).

For sufficiently small epsilon, B_epsilon<1, so (16) proves
`sup_t |z(t)|=O(epsilon^3)`, with constants independent of T. Also
beta=sqrt(3)epsilon alpha+O(epsilon^3)=O(epsilon). The positivity factorization
(4) now gives the actual no-event energy bound

    E_1(t)=Omega|z(t)|^2+ell|beta(t)|^2=O(epsilon^2).   (17)

This bound is stronger than trace-norm convergence and directly controls
the potentially large microscopic observable on the no-event part.

Survival obeys the exact relation

    p_1'=-4kappa epsilon^-2 |beta|^2.

Using p_1=d|alpha|^2+O(epsilon^4) and
|beta|^2=3epsilon^2|alpha|^2+O(epsilon^4), one gets

    p_1'=-(12kappa/d)p_1+O(epsilon^2), p_1(0)=1,
    p_1(t)=exp(-12kappa t)+O_T(epsilon^2)              (18)

on every fixed finite interval, uniformly in lambda in [0,1]. Equations
(13), (17) and (18) establish

    <H>_t=(3delta/(2epsilon^2))(1-exp(-12kappa t))+O_T(1),
    epsilon^2 <H>_t -> (3delta/2)(1-exp(-12kappa t)),
    <H>_t/[S(S+1)] -> (3K/2)(1-exp(-12kappa t)).        (19)

For every fixed positive t the last coefficient is strictly positive. The
initial mean from (6) tends to zero. The limits and error bounds are uniform
throughout the stipulated electric family; choosing lambda as a resource-
dependent value in [0,1] does not remove the leading divergence.

The underlying physical Hilbert space here remains sixteen-dimensional and
all fields remain in {-1,0,1}. The singular energy comes from the microscopic
couplings and the post-event state, not from a high-field input escaping a
spin box. Consequently an O(1) electric correction ell E2 cannot remove the
order-S(S+1) mean energy requirement or the leading marked variance.
A qualitative limiting density by itself would not have supplied (19).



## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [local_electric_completions_and_postbirth_field_phase_bounded_theorem_note_2026-09-24](LOCAL_ELECTRIC_COMPLETIONS_AND_POSTBIRTH_FIELD_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [exact_microscopic_energy_at_a_star_birth_bounded_theorem_note_2026-09-24](EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [finite_time_star_energy_and_supply_bound_bounded_theorem_note_2026-09-24](FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8923, frozen head `191ad04ad48d64c55d31c34521caec68444bfa64`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/star_energy_cost_across_the_electric_family_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
