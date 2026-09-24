---
claim_id: time_integrated_microscopic_cube_birth_variance_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Supplied compensated cube and actual original birth: a positive lower bound for the ordinary full-ensemble variance integrated over every fixed later interval, with explicit nonnegative unresolved remainders. No pointwise or sharp integral asymptotic, physical energy completion or native selection."
upstream_dependencies:
  - ordinary_microscopic_cube_energy_after_the_birth_layer_bounded_theorem_note_2026-09-24
  - actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/time_integrated_microscopic_cube_birth_variance_2026_09_24.py
---

# Continuing formation and integrated microscopic energy fluctuations

**Type:** bounded_theorem

**Status:** proposed_retained

In the supplied compensated cube, convergence of ordinary mean energy does
not control its fluctuations. After an actual original birth, the common
limiting model gives every fixed later time interval a positive probability
of a second birth. The
full-ensemble microscopic energy variance integrated over that interval has
a lower bound of order epsilon^-2, with coefficient tied to that probability.
The non-event part that converges to the common matter/field description
itself carries a large physical energy-vector norm.

The theorem is conditional on the supplied model, canonical input, original
instrument and joint scaling. It retains both matter and field after formation.
It neither selects those inputs nor identifies this Hamiltonian with a
conserved total energy of an apparatus. No pointwise variance divergence or
sharp asymptotic for the whole integral is inferred.

## 1. Target and parents

Retain the supplied compensated lambda=0 cube, integer spin S, C=S(S+1),
epsilon^2 C=delta/K and fixed delta,K,kappa>0. The actual canonical first
birth on edge 01 has one of the original normalized outputs phi_i. The
subsequent full original ensemble rho_i(t) includes a possible second birth.
The six-site example is not used: it cannot form that second pair.

On N=6 let

    H = delta epsilon^-4 h,
    h = W + epsilon T + epsilon^2 C_S,
    H_eff = H - i kappa Gamma_S/(2 epsilon^2),
    v(t) = exp(-it H_eff) phi_i.

Gamma_S is the original sum of marked j* j, not a replacement energy filter.
It is supported in grade W=1. The terminal N=8 Hamiltonian is exactly zero.
Consequently the full, unconditioned ensemble moments are

    m(t)=Tr(H rho_i(t))=<v(t),H v(t)>,
    M2(t)=Tr(H^2 rho_i(t))=||H v(t)||^2,
    Var_H rho_i(t)=M2(t)-m(t)^2.                           (1)

No division by no-event survival probability occurs.

Use the exact no-event low coordinate and weighted bounds from the ordinary
energy theorem in open PR #9057, at c234d47c9d99b7fd5590957ec08d9083877d25e6.
That is a provisional mathematical dependency, not retained audit authority.
Its parents provide the exact uniformly bounded Riesz intertwiners, actual
birth expansion, full original generator and common matter/field limit.

Write the limiting no-event low ket as

    u_i(t)=exp[t(-i H_rot-kappa Lambda/2)] beta_i,
    Lambda=sum_j B_j* B_j,
    B_j=j_j F_infinity P,
    H_rot=K D-delta Z_infinity* Z_infinity/2,
    beta_i=j_i F_infinity Omega/sqrt(b_i),     b_i=2,2,4.

Here Omega is the bare zero-field all-A-plus input in N=4; this last expression
is its leading normalized first-birth output in N=6. The B_j above act from
the N=6 low space to N=8 and describe the subsequent original marks.

Its survival probability S_i(t)=||u_i(t)||^2 is the no-second-birth
probability of the common effective ensemble. A first birth is already the
specified normalized initial condition. Define

    P_i(a,b)=S_i(a)-S_i(b).

This is the probability of a second birth during [a,b] in that effective
model. It is not a newly selected physical rate or apparatus.

The first conclusion, for every fixed 0<a<b<infinity, is

    liminf_(epsilon->0) epsilon^2
        integral_a^b Var_H rho_i(t) dt
        >= (kappa/2) P_i(a,b).                            (2)

The positive probability bound in Section 6 makes this coefficient strictly
positive on every such interval. Consequently, the integrated ordinary variance
is at least of order epsilon^-2.
No matching upper bound, pointwise asymptotic or finite-spin spectral gap is
asserted. Divergence of these integrals alone does not rule out pointwise
convergence along every possible sequence; concentration in time must not be
silently excluded. The conclusion is about this stated time-integrated metric.

## 2. The exact low component carries microscopic energy variance

Let E_j be the exact Riesz projections of h_eff=epsilon^4 H_eff/delta near
j=0,1,2. Choose the parent's uniformly bounded invertible intertwiner J
from the bare grade spaces Pi_j to E_j, and write

    v(t)=sum_(j=0)^2 J_j a_j(t),
    J_j=J Pi_j,   dot a_j=K_j a_j.

All norms of J,J^-1 are uniformly bounded for small epsilon. In particular
J_0=P+epsilon F_S P+O(epsilon^2), and the grade-one parity refinement gives

    Gamma_S J_0 = epsilon Gamma_S F_S P+O(epsilon^3).       (3)

The constants are uniform in S. For the main limit, O(epsilon^2) in (3)
would already suffice: after multiplication by epsilon^-1 it is o(1).
Gamma_S P=0, and the derivative of the low spectral isometry is +F_S P
because T=-(F_S+F_S*) and the low/first-high gap is one. The additional
Hermitian-to-no-event intertwiner differs from identity by O(epsilon^3),
so it does not change that leading coefficient.

The weighted low theorem gives, on every fixed [0,T],

    sup_t ||w a_0(t)|| <= C_T,
    sup_t ||a_0(t)-u_i(t)|| ->0,
    K_0=-i K D + B_epsilon,
    sup_epsilon ||B_epsilon|| < infinity,                 (4)

where w=1+sum E_e^2 and |D|<=Cw. Thus sup_t ||K_0 a_0(t)|| is uniformly
bounded. This is a vector bound on the actual low trajectory, not the false
claim that the norm of the entire low Hamiltonian is uniformly bounded.

The exact intertwining identity H_eff J_0=i J_0 K_0 gives

    H J_0 a_0 = i J_0 K_0 a_0
                 + i kappa Gamma_S J_0 a_0/(2 epsilon^2).

Multiplying by epsilon and using (3),(4), bounded strong convergence of the
normalized spin shifts and compactness of the limiting trajectory yields

    epsilon H J_0 a_0(t)
        -> i(kappa/2) Gamma_infinity F_infinity u_i(t)     (5)

uniformly on [0,T] in the common physical word Hilbert space. The first
term is O(epsilon) in norm. The second term has the displayed limit because
Gamma_S F_S is uniformly bounded and converges strongly, and the input
trajectory converges uniformly. It follows that

    epsilon^2 ||H J_0 a_0(t)||^2
        -> (kappa^2/4)||Gamma_infinity F_infinity u_i(t)||^2 (6)

uniformly. This energy contribution comes from the difference between the
physical Hermitian Hamiltonian and the no-event generator. Removing the
initial fast Riesz component does not remove it.

## 3. Rapid relative phases control integrated cross terms

It remains essential to show that the other two Riesz components cannot
cancel (6) throughout the fixed interval. They are not mutually orthogonal
in the physical energy norm. Dropping their cross terms pointwise would be
invalid. The following exact Sylvester estimate controls their integrals.

Uniform cluster expansions and grading give

    K_j=-i delta epsilon^-4 j I+R_j,
    ||R_j||<=C epsilon^-2,                  j=0,1,2.       (7)

The exact dissipative full evolution is a contraction. Since E_j commutes
with it, the actual birth estimates and bounded intertwiner imply, for all
t>=0,

    ||a_0(t)||<=C,  ||a_1(t)||<=C epsilon,
    ||a_2(t)||<=C epsilon^2.                               (8)

The stronger O(epsilon^4) second-high estimate is unnecessary here.
From H_eff J_j=i J_j K_j and (3),

    ||H J_0||<=C epsilon^-2,
    ||H J_1||+||H J_2||<=C epsilon^-4.                    (9)

The first is an operator norm on the full low space: ||K_0||=O(epsilon^-2)
on the finite spin box, while the additional loss term has norm O(epsilon^-1).
The two high estimates also follow directly from ||H||=O(epsilon^-4).

For j<k put C_jk=(H J_j)* H J_k and solve

    K_j* Y_jk+Y_jk K_k=C_jk.                              (10)

On the rectangular operator space the left map is the scalar
i delta (j-k)epsilon^-4 times identity plus an operator of norm at most
C epsilon^-2. Its inverse exists by the norm-convergent Neumann series for
small epsilon, with norm at most C epsilon^4. This works uniformly in the
growing finite dimensions and requires no diagonalizability or dissipative
gap inside a cluster. Therefore

    ||Y_01||+||Y_02||<=C epsilon^-2,
    ||Y_12||<=C epsilon^-4.                              (11)

Differentiate <a_j(t),Y_jk a_k(t)> and use (10). Exactly,

    integral_a^b <H J_j a_j(t),H J_k a_k(t)> dt
       = [<a_j(t),Y_jk a_k(t)>]_a^b.                     (12)

Combining (8),(11), these three integrals are respectively
O(epsilon^-1), O(1), O(epsilon^-1). All vanish after multiplication by
epsilon^2. There is no replacement of the actual fast propagator by its
rotor limit at a growing time.

The diagonal high-component squared norms are nonnegative. Expanding (1),
integrating and applying (6),(12) thus gives

    liminf epsilon^2 integral_a^b M2(t) dt
      >= (kappa^2/4) integral_a^b
                     ||Gamma_infinity F_infinity u_i(t)||^2 dt. (13)

This is a lower bound; the high diagonal terms need not have a limit and
are not discarded from an equality.

## 4. Relation to the second birth and to variance

On the rotor N=6 cube, Gamma_infinity=2 P_bright: an active state has exactly
one vacant A and one vacant B joined by an edge, with two original resolved
orientations of unit shift norm. The original coherent/resolved descriptions
have the same complete loss. Other grades and opposite vacancies have zero
loss. In particular

    Gamma_infinity^2=2 Gamma_infinity,
    Lambda=P F_infinity* Gamma_infinity F_infinity P,
    ||Gamma_infinity F_infinity u||^2=2<u,Lambda u>.       (14)

The effective no-event norm satisfies

    dS_i/dt=-kappa <u_i,Lambda u_i>.

Inserting (14) into (13) gives the right-hand side of (2). The ordinary
mean-energy theorem proves m(t) converges uniformly to the bounded common
matter/field energy on every fixed [a,b] with a>0. Hence

    epsilon^2 integral_a^b m(t)^2 dt ->0,

and (2) follows for the full ensemble variance. This last subtraction is
why the theorem is stated away from the initial t=0 birth layer.

The exact integer root word calculation gives, for each of plus, minus and
coherent beta_i,

    <beta_i,Lambda beta_i>=8,
    ||Gamma_infinity F_infinity beta_i||^2=16.             (15)

It constructs j_i F Omega, then every original j_j F beta_i, and verifies
the equality with the complete Gamma loss. Thus S_i'(0)=-8 kappa, and the
low-component coefficient (6) at t=0 is 4 kappa^2. These exact author word
coefficients were separately reconstructed in POST.
Continuity alone gives positivity on sufficiently early intervals. Section 6
gives the additional global rotor argument needed for every fixed interval.

## 5. Two identities retain the unresolved contribution

The following strengthening originated in the independent PRE and was then
read and checked by the root. It is not attributed to the earlier frozen root
derivation. For any solution x'=-iHx-alpha Gamma_S x, alpha=kappa/(2epsilon^2),
the exact identity Hx=i(x'+alpha Gamma_S x) gives

    ||Hx||^2=||x'||^2+alpha^2||Gamma_S x||^2
                         +alpha d<x,Gamma_S x>/dt.        (16)

The ordinary-energy parent supplies, uniformly for t>=epsilon,
z_1=E_1 v=O(epsilon^(9/4)), and uniformly for t>=0,
z_2=E_2 v=O(epsilon^4). On any fixed [a,b] with a>0, these imply
z_1+z_2=o(epsilon). With (3)-(5),

    Gamma_S v/epsilon -> Gamma_infinity F_infinity u_i,
    <v,Gamma_S v>=O(epsilon^2),

uniformly on that interval. Applying (16) to v, integrating, subtracting
the bounded mean square and using (14) yields

    epsilon^2 integral_a^b Var_H rho_i dt
       -epsilon^2 integral_a^b ||v'(t)||^2 dt
       -> (kappa/2)[S_i(a)-S_i(b)].                        (17)

Uniform low convergence and the high bounds also imply ||v(t)||^2->S_i(t).
Since the exact microscopic second-birth probability is p2,epsilon=1-||v||^2,
one can equivalently replace the limiting survival difference in (17) by
p2,epsilon(b)-p2,epsilon(a), with an o(1) remainder. This is the probability
increment of the full original ensemble, without conditioning again at a.
The derivative term is nonnegative and is not shown to vanish.

There is also a remainder in terms of the first high Riesz component:

    epsilon^2 integral_a^b Var_H rho_i dt
       -epsilon^2 integral_a^b ||H E_1 v(t)||^2 dt
       -> (kappa/2)[S_i(a)-S_i(b)].                        (18)

To verify (18), put u_low=J_0 a_0 and M_r=sup_[a,b]||z_r||. Remove the
scalar phase omega_r=delta r epsilon^-4 by q_r=exp(i omega_r t)z_r.
The exact cluster estimate gives ||q_r'||<=C epsilon^-2 M_r. The weighted
trajectory gives ||u_low'||<=C, ||H u_low||<=C epsilon^-1, and the loose
bound ||(H u_low)'||<=C epsilon^-4. One integration by parts then gives

    |integral_a^b <H u_low,H z_r> dt|
       <= C M_r [epsilon^-1+(b-a)(epsilon^-4+epsilon^-3)]. (19)

Here the integrand with its fast phase removed has norm at most
C epsilon^-5 M_r and derivative norm at most
C(epsilon^-8+epsilon^-7)M_r. Multiplication by 1/omega_r proves (19).
With M_1=O(epsilon^(9/4)) and M_2=O(epsilon^4), its epsilon^2-scaled
terms are O(epsilon^(1/4)) and O(epsilon^2). Also ||H z_2||=O(1),
||H z_1||=O(epsilon^(-7/4)), so the scaled second-high diagonal and
high/high cross terms vanish. Combining these with (6),(14) and the bounded
mean proves (18). These estimates give the coarse integral upper bound
O(epsilon^(-7/2)); they do not identify a sharp exponent.

Equations (17) and (18) are alternatives. Each exposes a nonnegative
unresolved remainder. Setting either remainder to zero would claim more
than the estimates prove. Their lower inequality independently checks the
Sylvester argument, whose weaker initial high bounds already suffice for (2).

## 6. Uniform rotor loss on the physical low space

This local-star argument originated in the sealed independent PRE. The root
reviewed its direct-sum and charge-cover steps before including it here.
In N=6,P there are two vacant B sites, all four A sites occupied, five
positive charges and one negative charge. Every B-vacancy pair has exactly
two common A neighbors. Call them active centers for that word.

Let F_a be the part of F_infinity P that moves a charge out of A vertex a.
Let P_a project onto P words whose two vacant B sites both neighbor a. Only
these inputs can contribute to P_bright F_a P. Different a have different
vacant A sites after F_a, so the loss separates exactly:

    Lambda=2 sum_a F_a* P_bright F_a,
    sum_a P_a=2 I.                                            (20)

For a local block, freeze all electric links outside the three-edge star
at a, and all matter charges outside that star. Gauss at each B leaf then
determines its incident star field uniquely from the leaf charge and the
frozen external fields. Gauss at a is preserved by the fixed local total
charge. Thus the following finite local matrices describe direct summands
of the complete physical rotor operator. No single Fourier phase or field
truncation is substituted for a physical state.

If the negative charge is outside the star, its two occupied local sites
both have positive charge. Label an input by the one occupied B leaf and
an output by the one vacant B leaf. The unsigned local hop matrix is

    A_plus = [[0,1,1],[1,0,1],[1,1,0]],
    A_plus* A_plus=I+J_3,

with eigenvalues 1,1,4. If the negative charge lies inside the star, the
local occupied charges are opposite. There are six inputs (occupied leaf,
sign at a) and six outputs (positive leaf, negative leaf). Each output has
two positive unit-amplitude preimages. The squared singular values are
0,1,1,3,3,4. Thus, denoting by P_a,out the active inputs with the negative
charge outside that star,

    P_a,out <= F_a* P_bright F_a <= 4 P_a.                      (21)

For any B-vacancy pair the two active centers have disjoint pairs of
occupied local sites: each pair consists of its A center and its third,
occupied B neighbor. The single negative charge belongs to at most one
of those pairs. Hence it is outside at least one active star, and

    sum_a P_a,out >= I.

Combining this fact with (20)-(21) proves 2 I <= Lambda <= 16 I on the entire
physical rotor N=6,P Hilbert space. The possible kernel in an individual
opposite-charge local block therefore causes no global zero mode for Lambda. No analogous
uniform finite-spin lower bound is assumed at the spin boundary.

The survival equation now gives

    -16 kappa S_i <= S_i' <= -2 kappa S_i,
    exp(-16 kappa t) <= S_i(t) <= exp(-2 kappa t).

Using S_i(b)<=exp(-2 kappa(b-a)) S_i(a) and
S_i(a)>=exp(-16 kappa a) gives the explicit estimate

    (kappa/2)[S_i(a)-S_i(b)]
      >= (kappa/2) exp(-16 kappa a)
                   [1-exp(-2 kappa(b-a))] > 0.            (22)

Thus the lower variance-integral coefficient is
strictly positive on every nonempty fixed interval after birth, for each
of the three supplied actual marks.

## 7. Verification, provenance and unresolved physics

The personal Sylvester proof was frozen before the separately sealed PRE was
read. The PRE independently recovered the same lower bound and supplied the
exact derivative identity, explicit high remainder and uniform rotor loss
bound. The root reviewed those enhancements; their origin is retained here.
Released-source POST checked the complete frozen root proof, its operator-norm
Sylvester bound and original loss factors. It independently reconstructed the
actual words and exercised a nonnormal rectangular Sylvester problem, including
a failed missing-adjoint alternative. No material discrepancy was found within
the specified conditional scope. This is selective independent checking, not
retained audit authority or a fresh certification of every transitive parent.

The self-contained author runner includes exact integer original-birth words,
the local same/opposite-charge Gram spectra and complete charge-label cover,
a three-grade toy with exact spectral time integrals, and full S=1 actual-cube
low Riesz controls. The physical-star direct-sum argument carries the rotor
operator quantifier; the small matrices alone do not. The actual-cube matrix
definitions are explicitly reused from the earlier author runner, included
here rather than imported at runtime, and are not independent evidence.

For kappa=.7 and toy interval [.2,.8], the scaled integrated variance is about
.15119 at epsilon=.03, toward .150326, while the wrong use of H_eff for the
low squared-energy observable gives about .000204. All spectral cross terms
and the mean square are included. This toy is not the actual cube.
In the full S=1 cube at epsilon=.02, the three scaled low second moments are
about 2.2563,2.1508,2.2036 versus 1.96; their vector errors remain about
.554,.447,.503. The energy-weighted 32-to-48-point contour refinement residual
is about 1.4e-11. These are finite floating consistency controls, not interval
certificates or numerical proof of the joint spin limit.

The exact low Riesz component is oblique to the Hermitian energy bands. Its
large physical energy-vector norm does not contradict bounded energy moments
inside the exact Hermitian low band. Replacing H by the no-event generator,
dropping cross terms pointwise, or extrapolating a rotor tail to growing fast
time would change or overstate the argument. Those shortcuts are not used.

All variance identities use the original full ensemble and the lambda=0
zero-energy terminal sector. No survival normalization or field-only limit is
inserted. Changing the Hamiltonian, instrument, initial state, positive rate
or joint scaling requires a new argument. In particular the six-site example
cannot form a second pair and does not supply this cube theorem.

The integrated result does not imply a pointwise variance limit or divergence
at every selected time; concentration and interference in time remain possible.
The sharp integral remainder is open. Canonical preparation, compensation,
Markovian time and the formation instrument remain supplied. A physically
selected reservoir, heat/work accounting, conserved interacting total energy,
local sustained apparatus and empirical predictions are unresolved. No new
axiom, broad formation impossibility or TOE completion is asserted.

## Imported sources

- [Ordinary energy beyond the birth layer](ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md): weighted low trajectory, actual high Riesz bounds and bounded ordinary mean on fixed later intervals. This is the explicit provisional parent in PR #9057.
- [Actual fast-time cube birth](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md): original preparation, marks, fast generator and exact cluster structure.
- [Bounded compensation target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md): uniform graded expansions and supplied joint scaling.
- [Common local compensation limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): common matter/field target and original effective marks.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/time_integrated_microscopic_cube_birth_variance_2026_09_24.py
```

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: time_integrated_microscopic_cube_birth_variance_bounded_theorem_note_2026-09-24
target_blocker_text: "Ordinary mean convergence leaves later accumulated microscopic energy fluctuations uncontrolled."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Determine the surviving first-high integral and physical apparatus energy accounting, keeping pointwise variance open."
conditional_surface_status: "Supplied compensated cube, canonical actual first birth, complete original instrument, fixed positive parameters and joint spin scaling; provisional ordinary-energy parent."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An exact low-component identity and integrated interference estimates relate a positive variance lower bound to the second-birth probability; a physical-star rotor bound makes it positive on every fixed later interval."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
