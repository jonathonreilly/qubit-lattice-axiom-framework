---
claim_id: actual_cube_birth_apparatus_coherence_and_energy_range_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional finite apparatus for one original selected cube birth at fixed amplitude: probability-weighted energetic Fisher and frequency-range bounds at subnormalized error o(epsilon^3), with a sharp one-input state-preparation relaxation and bounded mean. No full-instrument or continuous-process sufficiency, physical selector or retained no-go."
upstream_dependencies:
  - actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/actual_cube_birth_apparatus_coherence_and_energy_range_2026_09_24.py
---

# Apparatus coherence and energy range for one actual cube birth

**Type:** bounded_theorem

**Status:** proposed_retained

An actual birth in the supplied compensated cube has a small, high-energy
component. Its energy variance alone does not determine what an apparatus
must supply. This note bounds two initial resources: energetic Fisher
information and the range of coherent energy frequencies. The success
probability and the input's own coherence are included throughout.

The lower bounds apply to a conserving realization of the selected output
on the stated canonical input. An explicit preloaded-state swap reaches the
leading coefficients for this one-input relaxation with error O(epsilon^4)
and bounded mean energy above its true ground. That construction generally
fails to implement the original mark on other inputs. It therefore supplies
a sharp comparison for this weak task, not a physical formation mechanism.

All claims are conditional on the supplied microscopic model and implementation
class. This is partial narrowing of resource accounting; no physical-process
no-go or formal retained audit status is claimed. The original resolved or
coherent formation mark remains the target, without an added energy filter.

## 1. Exact operational target and scope

Use the actual cube with A={0,3,5,6}, B={1,2,4,7}, integer spin S, C=S(S+1),
epsilon^2 C=delta/K, and fixed positive delta,K. The supplied lambda=0 Hamiltonian is

    H=delta epsilon^-4 (W+epsilon T+epsilon^2 C_S).

The cube compensation and canonical cluster rotation U are precisely those of
the main local-compensation and bounded-target sources. Omega has charges 1_A
and zero fields. The actual input is psi=U Omega in N=4. For one specified edge
(0,1), choose one original mark j_i: resolved plus, resolved minus, or coherent.

Fix a positive strength alpha independent of epsilon, small enough that the
chosen marked CP operation can be an outcome of an instrument for every S:

    rho -> alpha^2 j_i rho j_i*.

For example alpha^2 sup_S ||sum_j j_j*j_j||<=1 suffices if all original marks
are included. Uniform boundedness follows from the fixed graph and normalized
integer-spin shifts. Other outcomes of the realizing instrument are unrestricted.
In particular, this argument does not require choosing a square-root no-event
completion and does not identify that completion with exact GKLS no-event motion.

On psi the target selected output is

    omega_i = p_i |phi_i><phi_i|,
    p_i=alpha^2 ||j_i psi||^2,
    phi_i=j_i psi/||j_i psi||.                              (1)

No energy-band measurement is added to the actual formation mark. Spectral
projections used below only define a mathematical witness for this same output.

The apparatus R may include a reservoir, clock, program and all other energy
references. Initially it is independent of psi, in an arbitrary finite-dimensional
state sigma_R. Its additive energy is H_R. Blank outcome flags have zero energy
and no initial correlation with the input. The implementation is a unitary V
commuting exactly with H+H_R, followed by flag readout and discarding inaccessible
degrees of freedom. More general covariant channels give the same conclusion.
All nonstationary auxiliary resources must be counted in R; an external phase
reference cannot be supplied without accounting for it.

Conservation here means the stated additive system-plus-apparatus energy.
Conservation of a different interacting total Hamiltonian, with a persistent
interaction-energy term, does not by itself imply this covariance hypothesis.
Such implementations require separate accounting; they are not excluded here.

Let sigma_i be the implemented subnormalized selected output on this input, and
assume only

    ||sigma_i-omega_i||_1 <= eta_epsilon.                    (2)

The comparison is unconditional: it includes success probability. It is weaker
than requiring a uniform instrument-channel approximation on every input. No
normalized rare-event error is inferred without its probability factor.

The conditional bound is

    liminf_(epsilon->0) epsilon^4 F_(H_R)(sigma_R)
          >= 4 alpha^2 delta^2 r_i,                       (3)

provided eta_epsilon=o(epsilon^3), where r_i=4,2,6 for plus, minus, coherent.
This is an initial apparatus requirement, not a claim of an exact minimum or
that this much coherence is consumed or returned. It leaves other outcomes free.

## 2. Finite-dimensional Fisher identities used here

F_H(rho) is the symmetric-logarithmic-derivative Fisher information for the
parameter family exp(-itH)rho exp(itH). If rho=sum_a lambda_a |a><a|, then

    F_H(rho)=2 sum_(a,b;lambda_a+lambda_b>0)
        (lambda_a-lambda_b)^2/(lambda_a+lambda_b) |H_ab|^2. (4)

This standard energetic-coherence quantity is reviewed, for example, in
[Marvian, arXiv:2112.04694](https://arxiv.org/pdf/2112.04694v1), equation(2) and the properties following it. Only
these finite-dimensional identities are used, not that paper's iid conversion
or periodicity theorems. The following short derivation makes the precise
needed hypotheses explicit.

The use of energetic coherence as an implementation resource is established
prior work, including [Tajima, Shiraishi and Saito, arXiv:1906.04076](https://arxiv.org/abs/1906.04076). Its additive
conservation setup and unitary-control bounds give relevant context. Its
optimal unitary-operation cost theorem is not applied to the present heralded
one-input target. The model-specific content here is the actual birth
coefficient, its probability weight, the diverging energy scale and the
explicit approximation-sensitive witness. No new general coherence principle
or priority over that machinery is claimed.

For dotrho=-i[H,rho], the symmetric logarithmic derivative L solves
dotrho=(rho L+L rho)/2 on the support. Its variational form is

    F(rho,dotrho)=sup_(X=X*) [2 Tr(dotrho X)-Tr(rho X^2)].   (5)

It follows by completing the square in the real seminorm Tr(rho X^2); evaluating
in the eigenbasis gives (4), including zero eigenvalues. For a parameter-independent
CPTP map E, Kadison's inequality E*(X^2)>=E*(X)^2 and (5) prove
F(E rho,E dotrho)<=F(rho,dotrho). For a covariant channel, E dotrho is the output
time derivative. An energy-conserving unitary and partial trace therefore obey
this monotonicity relative to the corresponding additive energies.

On product inputs, the logarithmic derivative is L_A tensor I+I tensor L_B.
Each has zero mean, so Fisher information is additive. For a pure state it is
four times energy variance. More generally (4), using
(lambda_a-lambda_b)^2/(lambda_a+lambda_b)<=lambda_a+lambda_b,
and invariance under H -> H-cI, gives

    F_H(rho)<=4 Var_rho(H).                               (6)

For a zero-energy classical flag with time-independent probabilities, block
diagonality in (5) gives F(sum_j p_j rho_j tensor |j><j|)=sum_j p_j F_H(rho_j).
The probabilities are independent of the time-translation parameter because
the flag energy is zero and the output time action leaves each block invariant.
These are statements about rotating the entire input, including its apparatus;
the target marked map itself need not be covariant on the system alone.

Finally, restricting (5) to a scalar multiple of any Hermitian A and optimizing
the scalar gives

    F_H(rho)>=|Tr(rho i[H,A])|^2/Tr(rho A^2),               (7)

when the denominator is positive. Subtracting the mean of A can sharpen it,
but is unnecessary. This uncentered version is convenient for a rare flag.

The implementation hypotheses imply

    F_H(psi)+F_(H_R)(sigma_R) >= F_(H tensor I_flag)(output). (8)

No assumption of reservoir purity, a thermal form, commensurate energies,
catalyst return or an uncorrelated final reservoir is required.

## 3. The actual input has uniformly bounded Fisher information

The bounded compensation theorem gives the exact canonical low Hamiltonian

    U* H U|_P = delta epsilon^-2 (D/C) + delta H4_S + O(epsilon^2),

with ||H4_S|| and the remainder coefficient uniformly bounded at fixed graph.
The local compensation identity supplies C_0=M+D/C on the N=4 input sector.
On zero fields, D Omega=0 exactly. Since U is the exact spectral isometry,

    ||H psi|| = ||(U*HU)Omega|| = O(1),
    F_H(psi)=4 Var_psi(H)=O(1),                            (9)

uniformly along the joint scaling. This does not assert that psi is a zero-energy
eigenstate or that H is nonnegative. A scalar energy shift changes none of the
Fisher quantities. We use h_epsilon=||H-c_epsilon I||=O(epsilon^-4) on the relevant
finite physical sectors whenever a norm bound is needed below.

## 4. Actual birth coefficients and an exact phase witness

The actual-fast-time parent, at time zero, supplies the uniform expansions

    ||j_i psi||^2 = b_i epsilon^2+O(epsilon^4),
    ||P_1^H phi_i|| = epsilon sqrt(r_i/b_i)+O(epsilon^3),
    ||P_0^H phi_i|| = 1+O(epsilon^2),
    ||P_2^H phi_i|| = O(epsilon^2),

with (b_i,r_i)=(2,4),(2,2),(4,6). The projectors here are the exact Hermitian
Hamiltonian clusters in N=6. Their energies satisfy

    H|_(P_1^H) = delta epsilon^-4 I+O(epsilon^-2),
    ||H|_(P_0^H)||=O(epsilon^-2).                         (10)

Set x=P_0^H phi_i, y=P_1^H phi_i, l=||x||, u=||y||, a=x/l, b=y/u. They are
orthogonal and l,u are positive for small epsilon. The Hermitian operator

    A_i=i(|b><a|-|a><b|)

has norm one, A_i^2=|a><a|+|b><b|, and vanishing mean on phi_i. It acts only in
the selected flag block of the full output. Since the projectors reduce H,

    |Tr(omega_i i[H,A_i])|
        = 2 p_i l u |<b,Hb>-<a,Ha>| =: d_i,
    Tr(omega_i A_i^2)=p_i(l^2+u^2)=:v_i.                 (11)

This equality does not require a or b to be exact energy eigenvectors. Components
of H a orthogonal to a in its cluster, and of H b orthogonal to b, have zero
overlap with the corresponding component of phi_i. Equations (1),(10) imply

    d_i=2 alpha^2 delta sqrt(b_i r_i) epsilon^-1[1+O(epsilon^2)],
    v_i=alpha^2 b_i epsilon^2[1+O(epsilon^2)].             (12)

For the realized output, (2), ||A_i||=1 and
||[H,A_i]||<=2h_epsilon give

    |Tr(sigma_i i[H,A_i])| >= [d_i-2h_epsilon eta_epsilon]_+,
    Tr(sigma_i A_i^2)<=v_i+eta_epsilon.

Apply (7) to the entire flagged output and (8) to obtain the exact finite-model
inequality

    F_(H_R)(sigma_R) >=
       [d_i-2h_epsilon eta_epsilon]_+^2/(v_i+eta_epsilon)
       -F_H(psi).                                         (13)

If eta_epsilon=o(epsilon^3), the derivative correction is o(epsilon^-1) and
the denominator correction is o(epsilon^2). Substituting (9),(12) proves (3).
The constants are respectively 16,8,24 times alpha^2 delta^2. This lower bound
is obtained from one original mark alone and does not count a separate physical
energy-band measurement. Other outcome coherences can require additional resources.

For exact matching, the flagged pure-state identity also yields the familiar
lower bound 4 p_i Var_H(phi_i)-F_H(psi). The robust witness (13) is needed because
Fisher information or variance cannot be passed through a mere small trace error
uniformly when the microscopic energy norm diverges.

## 5. Why the error scale and the resource distinction matter

Let Pinch_H be pinching into the three exact N=6 energy clusters, not into every
energy eigenvalue. On the selected target branch its leading removed coherence
is between x and y. The trace norm of that rank-two off-diagonal block is
2p_i l u, while terms involving the grade-two amplitude contribute O(epsilon^4).
Consequently

    ||omega_i-Pinch_H(omega_i)||_1
       =2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^4).      (14)

The pinched branch has only O(1) Fisher information after accounting for its
probability. For the low component, its canonical coordinate is beta_i+O(epsilon^2)
with (D/C)beta_i=0, so its energy-vector norm is O(1). Within either high cluster
subtract its scalar center; the remaining norm is O(epsilon^-2). The respective
branch probabilities are O(epsilon^2), O(epsilon^4), O(epsilon^6). Equation (6)
then gives weighted low/high contributions O(epsilon^2), O(1), O(epsilon^2).
Complete the missing probability with any stationary state in a different flag.
This full comparison output has O(1) Fisher information while its selected branch
is only O(epsilon^3) away from the target.

Thus an unspecified O(epsilon^3) or merely vanishing trace error cannot support
the same divergent resource conclusion. This is a limitation of the state-error
premise, not a construction of a covariant apparatus realizing that pinched target.
No optimal approximation threshold or attainable minimum is claimed.

For a stationary apparatus F_(H_R)(sigma_R)=0, and (13) specializes to a
test of whether the bounded input coherence supplies the selected-output
witness. A high-variance energy-diagonal reservoir also has zero Fisher
information. A nonstationary clock or external phase control is a different
resource and must be counted in R before evaluating the inequality. This is
resource accounting for the stated operation, not a general bath-selection
or physical-process impossibility conclusion.

Equation (6) also implies Var_(sigma_R)(H_R)=Omega(epsilon^-4), hence an energy
standard deviation at least of order epsilon^-2. This is not a mean energy cost.
Only if the resource has a further supplied spectral range 0<=H_R<=Lambda_R I
can one infer

    Lambda_R <H_R> >= Var(H_R) >= F_(H_R)(sigma_R)/4.        (15)

No assumption about Lambda_R is derived here. Large rare-energy tails, correlated
final resources, reusable references and other implementations remain possible
within the bounds. There is no conclusion that every bath needs a divergent
mean energy or that a unique reservoir is selected.

## 6. Relation to the original continuous dynamics

The normalized selected output in (1) is exactly the original actual birth
state. The strength alpha is a specified operational premise. It must not be
silently interpreted as a fixed physical timestep of the GKLS model.
For the parent's collision instrument alpha^2=kappa tau/epsilon^2, the same
finite inequality applies, with leading selected-branch term proportional to
kappa tau epsilon^-6. Establishing a simultaneous continuous-time approximation
requires its own tau-dependent error bound; taking tau of order epsilon^2 does
not make the large-H splitting error small. None is assumed in (3).

An exact marked continuum process with resolved event times, coarse bins, or
interventions is a different operational target. Integrating unknown event times
can dephase precisely the high-frequency coherences measured here. This note
does not transfer (3) to every such process without proof. It provides a scoped
test for a conserving implementation of the actual marked operation at stated
strength and accuracy. Physical time, bath preparation, spatial locality,
compensation selection, other electric completions and empirical predictions
remain open. No new axiom or retained status is introduced.

## 7. A finite frequency-support lemma

For a finite Hamiltonian H with spectral projectors Pi_E, decompose an operator
X into its Bohr-frequency components

    X_nu = sum_(E-E'=nu) Pi_E X Pi_E'.

Under time translation X_nu acquires the phase exp(-it nu). Distinct finitely
many frequencies are linearly independent: multiplying by exp(it mu) and
taking the long-time Cesaro average isolates X_mu. Hence a covariant linear
map maps the nu component only into the same output frequency. This follows
directly by applying that average to the covariance equation; no periodicity,
integer spectrum or infinite-dimensional limit is assumed.

For a positive state sigma_R define its coherence bandwidth

    B_R=max{|E-E'|: Pi_E sigma_R Pi_E' is nonzero},

with B_R=0 for a stationary state. Always B_R<=diam(spec H_R). The spectral
diameter alone need not say which frequencies occur or with what amplitude.
Classical populations of arbitrarily separated levels do not increase B_R.

If a system input rho is supported in an energy interval of width B_in, its
frequencies have absolute value at most B_in. The product rho tensor sigma_R
therefore has frequencies only within [-(B_in+B_R),B_in+B_R]. A unitary conserving
H+H_R, a partial trace, and zero-energy flag readout all preserve covariance.
Consequently every selected subnormalized output sigma_i has no matrix element
between output energy sets separated by more than B_in+B_R. Degeneracies and
arbitrary final system-resource correlations do not change this argument.

Only a necessary frequency condition is proved. A large enough bandwidth does
not guarantee the individual resonances or their amplitudes needed by a target.

## 8. Application to the actual birth

The exact N=4 low cluster supporting psi=U Omega has width

    B_in=O(epsilon^-2).

This uses the uniform finite-graph bounds on D/C and H4_S in the bounded-target
parent. It does not approximate psi by a bare, noninvariant low-sector vector.
In N=6 let P_0 and P_1 be the same exact Hermitian spectral clusters as in the
Fisher argument above. Their ordered energy separation is

    G_epsilon=min spec(H|P_1)-max spec(H|P_0)
             =delta epsilon^-4+O(epsilon^-2).

Use x=P_0 phi_i, y=P_1 phi_i, l=||x||, u=||y||, a=x/l and b=y/u.
If B_in+B_R<G_epsilon, the lemma gives P_1 sigma_i P_0=0. The Hermitian test

    Q_i=|a><b|+|b><a|,   ||Q_i||=1

has zero expectation in sigma_i and expectation 2p_i l u in the target omega_i.
Trace-norm duality gives the exact finite-model lower error

    ||sigma_i-omega_i||_1 >= 2p_i l u.                       (R1)

Since 2p_i l u=2alpha^2 sqrt(b_i r_i)epsilon^3[1+O(epsilon^2)], an implementation
with eta_epsilon=o(epsilon^3) must eventually satisfy B_R>=G_epsilon-B_in.
In particular,

    liminf epsilon^4 B_R >= delta,
    liminf epsilon^4 diam(spec H_R) >= delta.               (R2)

The conclusion concerns initial coherence frequencies and energy range. It
does not say that the mean energy is of order epsilon^-4. Neither a mere large
classical variance nor a coherent state supported only on low frequencies
satisfies the missing high-frequency requirement. Scalar energy shifts leave
the statement unchanged. The entire apparatus, including clocks, is counted.

## 9. A one-input state-preparation relaxation

The original lower bound assumes only the selected output on one particular
input. This weak requirement admits a simple positive realization that makes
its limitations clear. Preload the desired output state into an apparatus with
a matching Hamiltonian and transfer it by an energy-conserving swap. This uses
the answer as a supplied resource state. It is a state-preparation construction,
not a derivation of the original j_i operation on other inputs.

Let P_4 denote the exact N=4 low spectral subspace and define the invariant
system subspace

    D = ran(P_4) direct-sum ran(P_0) direct-sum ran(P_1).

The direct sums separate the charge sectors. Define the normalized truncated
birth vector phi_01=(x+y)/sqrt(l^2+u^2), keeping the original success probability
p_i. Since ||P_2 phi_i||=O(epsilon^2),

    ||p_i |phi_01><phi_01|-omega_i||_1
       =2p_i ||P_2 phi_i||=O(epsilon^4)=o(epsilon^3).        (R3)

There are precisely the three relevant N=6 clusters. The equality uses the
pure-state trace distance and orthogonal projection, without changing the
physical formation mark in the target.

Take one zero-energy two-valued flag F and a replica R of D tensor F. Its
Hamiltonian is H_R=(H|D-E_min I) tensor I_F, where E_min=min spec(H|D). Choose
a ground eigenvector e_min in D and prepare

    sigma_R = p_i |phi_01><phi_01| tensor |1><1|
              +(1-p_i)|e_min><e_min| tensor |0><0|.          (R4)

On (D tensor F) tensor R, use the ordinary swap. On the orthogonal system
complement, use identity. The invariant D decomposition makes this a global
unitary on the full system-plus-resource space. The swap commutes with the
additive energy because the two Hamiltonians agree up to the scalar E_min;
the identity complement also commutes. A system input psi tensor a blank flag
is in D tensor F, so the final accessible state is exactly (R4), with the
resource holding the old input. All discarded correlations and energy flows
are accounted for by this unitary. Flag readout is permitted and stationary.

For this one-input target the apparatus Fisher information is exactly

    F_R(sigma_R)=4p_i Var_H(phi_01),
    epsilon^4 F_R(sigma_R) -> 4alpha^2 delta^2 r_i.          (R5)

To check the coefficient directly, the high-cluster probability in phi_01 is
epsilon^2 r_i/b_i+O(epsilon^4), its gap is delta epsilon^-4+O(epsilon^-2),
and its internal spectral width is O(epsilon^-2). The low normalized component
has energy-vector norm O(1). The squared mean is O(epsilon^-4), subleading to
the conditional leading second moment delta^2(r_i/b_i)epsilon^-6. Multiplying
by 4p_i proves (R5). Combining with the robust lower bound above proves
asymptotic equality of the leading Fisher coefficient for this relaxed target.
It does not prove attainability or optimality for the entire marked operation.

The spectrum of H_R has diameter

    Lambda_R=delta epsilon^-4+O(epsilon^-2).                (R6)

Indeed D has only its two low clusters and the first high cluster. The lower
edge stays bounded: in either low sector, the exact canonical Hamiltonian is
delta epsilon^-2 D_S/C+delta H4_S+O(epsilon^2), with D_S nonnegative and H4_S
uniformly bounded. Thus E_min>=-O(1); a zero-field low input supplies an O(1)
Rayleigh quotient and E_min<=O(1). The first high-cluster edges satisfy the
stated delta epsilon^-4+O(epsilon^-2) estimates. This is a bounded-below fact,
not an assertion that the unshifted microscopic Hamiltonian is nonnegative.

The chosen failure state is exactly at the apparatus ground. In the success
state the high probability is epsilon^2 r_i/b_i+O(epsilon^4), while its energy
is delta epsilon^-4+O(epsilon^-2); the low component contributes O(1).
The mean apparatus energy above its true ground is consequently

    Tr(H_R sigma_R)=alpha^2 delta r_i+O(epsilon^2).          (R7)

This finite limiting mean coexists with Fisher information of order epsilon^-4
and spectral diameter of order epsilon^-4. It explicitly exhibits the rare
high-energy alternative that invalidates an inference of divergent mean energy
from Fisher information alone. The preparation of (R4), its spatial realization
and the mechanism that might select it are all supplied, not solved.

## 10. What is and is not sharp

For the stated one-input relaxation with error o(epsilon^3), the leading Fisher
coefficient and energy-range coefficient are jointly attained by the explicit
truncated-output swap construction. It retains the exact target success
probability and incurs only O(epsilon^4) selected-state error. Exact target
state preparation at an arbitrarily tighter prescribed tolerance is not
established by this truncated construction. The attainment statement concerns
the class of error sequences o(epsilon^3), using this particular O(epsilon^4)
sequence. Exact target
state preparation can instead preload the full phi_i; the additional cluster
enlarges the available energy range and does not change the leading Fisher
coefficient. No optimal mean-energy theorem is inferred from (R7).

The swap outputs (R4) on every input in D, so it generally fails the original
map rho -> alpha^2 j_i rho j_i* on any other input. It is therefore only a sharp
comparison for the one-input resource obstruction. A uniformly accurate
conserving instrument, a continuing apparatus, the original continuous
generator, robust record storage and physically selected resources remain
different proof obligations. No physical law, reservoir or new axiom is chosen.

The frequency-support lemma is elementary finite-dimensional covariance
machinery. The contribution is its application to the exact actual-birth
clusters, alongside the deliberately limited constructive comparison and
its energy accounting. No new general resource principle is claimed.

## 11. Verification and limits of finite evidence

A separate checker sealed a reconstruction before release of the root Fisher
argument. It reconstructed the actual input and birth coefficients directly
from primitive words, used a distinct commutator witness for robustness, and
independently exhibited a conserving full-system swap and pinched comparison.
Released-source POST checked the phase witness, frequency-support lemma and
restricted-subspace swap, with separate finite matrix constructions. No
material mathematical repair was identified within the stated finite-apparatus
one-input scope. The frequency/range supplement is a POST comparison, not a
blind PRE reconstruction. Final source bindings and their precise scope are
recorded in the review packet; none is a retained audit verdict.

The self-contained author runner checks the weighted phase witness and noise,
finite conserving mixed-resource processing, complete S=1 microscopic input
and all three original marks, missing-frequency output blocks, and a conserving
preloaded-state swap. The actual-cube scaled Fisher coefficients at epsilon=.03
are about .16084, .08049 and .24137 for alpha=.1, delta=1, toward .16,.08,.24.
The input Fisher value is about 196.66. These fixed-S controls do not prove the
joint large-spin limit. The cube matrix definitions are explicitly reused
author definitions included in the runner, not independent code or a runtime
dependency on another publication.

The finite frequency control has apparatus spectral diameter 200 and variance
about 3394.79 but coherent bandwidth 1. It produces a high-energy population
about .231 while its forbidden high/low coherence is exactly zero in the
computed matrix. The separate swap toy has mean energy .04 at every sampled
epsilon while its Fisher information and gap grow. These examples test the
distinctions in the proof; they are not cube apparatus simulations or evidence
that nature prepares the stipulated resource.

The first author cube run produced two SciPy dtype future warnings, with no
failed assertion. It is preserved separately. Explicit float diagonal dtype
removed those warnings without changing formulas, tolerances or scientific
values. The final primary and independent controls are floating consistency
checks, not interval certificates. The written proofs carry the quantifiers.

## Imports and attribution

- [Actual fast-time cube birth](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md): the original mark, actual canonical preparation, exact cluster support, probabilities and leading energetic birth coordinates.
- [Bounded compensation target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md): uniform canonical low Hamiltonian and high-cluster expansions under the supplied joint scaling.
- [Local compensation and common matter/field limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): nonnegative D, zero-field input and birth identities, without a field-only postbirth substitution.

Energetic-coherence resource inequalities are established machinery. The
finite-dimensional inequalities are proved explicitly here; no iid optimal-cost
or general unitary-control theorem is imported for a heralded one-input target.
The model-specific coefficients, error scale, frequency range and limited
constructive comparison are the present applications. No general priority
claim is made.

## No-Go Discipline Gate

The committed [N1-N8 checklist](../.claude/science/physics-loops/actual-birth-coherence-20260924/NO_GO_DISCIPLINE_CHECKLIST.md)
records real attack families and positive escapes, the collapsed resource
relations, hidden-premise and prior-residual checks, and the remaining formal
packet limitation. It does not invent prior retained authority or claim a
negative-packet PASS. This is a proposed conditional quantitative result and
constructive one-input comparison. No prior open physical formation route is
declared closed. The primary cache carries the stated finite N5 resolution
certificate. Formal audit and complete landing gates remain separate.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/actual_cube_birth_apparatus_coherence_and_energy_range_2026_09_24.py
```

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: actual_cube_birth_apparatus_coherence_and_energy_range_bounded_theorem_note_2026-09-24
target_blocker_text: "The large actual birth-energy variance alone does not specify required apparatus coherence, frequency range or mean-energy cost."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Transfer resource accounting to the original continuous marked process and a physically specified, sustainable apparatus."
conditional_surface_status: "Supplied compensated cube and canonical input, fixed marked amplitude, finite apparatus, exact additive-energy covariance, zero-energy flag readout and explicit approximation metric."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite Fisher and frequency-support inequalities give quantitative necessary resources, and a restricted conserving swap reaches the leading coefficients for the one-input relaxation."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
