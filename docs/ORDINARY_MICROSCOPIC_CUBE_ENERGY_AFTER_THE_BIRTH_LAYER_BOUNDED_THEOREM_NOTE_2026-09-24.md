---
claim_id: ordinary_microscopic_cube_energy_after_the_birth_layer_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Conditional supplied compensated cube and actual zero-field first birth: ordinary full-ensemble mean
  energy converges after a lower endpoint much larger than epsilon^(6/5); matched high mean and full variance scales
  hold only on growing fast times with epsilon*tau tending to zero. No fixed-positive-time unscaled variance limit
  or physical reservoir selection.'
upstream_dependencies:
- actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- minimal_axioms
- sharp_actual_rotor_cube_energy_tail_bounded_theorem_note_2026-09-24
runner: scripts/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py
---

# Ordinary microscopic cube energy after the birth layer

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

Under the supplied compensated cube dynamics, the ordinary full-ensemble mean
energy converges to the common matter/field rotor energy at positive physical
times. More precisely, convergence is uniform on [a_epsilon,T] whenever
T is fixed and a_epsilon/epsilon^(6/5) tends to infinity. The original formation
instrument and possible second birth remain in the calculation.

Three new estimates make this possible: weighted rotor decay controls a growing
fast-time comparison; an exact local birth cancellation suppresses the second
high band; weighted low-cluster bounds permit the unbounded electric expectation.
The final section identifies the order epsilon^(6/5) birth-energy layer and
large variance on its shrinking-time window. It proves no ordinary variance
limit at fixed positive physical time. All dynamics and preparation hypotheses
are supplied; no physical law, reservoir or axiom is selected.

## Supplied model and first ordinary-energy conclusion

Use the supplied lambda=0 compensated cube and the notation of the actual-birth
parent. In particular

    H = delta epsilon^-4 h,
    h = W + epsilon T + epsilon^2 C_S,
    C_S = P F*F P + P(D/C)P,   C=S(S+1),
    epsilon^2 C = delta/K,   delta,K,kappa > 0 fixed.

Integer S tends to infinity. On P, D is the nonnegative diagonal electric
polynomial D(q,E)=sum_(a in A,b~a,q_b=0) E_ab(E_ab-q_a), of degree two in
the twelve fields. Here A={0,3,5,6}, B={1,2,4,7}, edges join binary vertices
that differ in one bit, W counts empty A sites, P=1_(W=0), and T=-(F+F*).
The original finite-spin hops, birth marks and Gauss constraint are those
of the actual-birth parent. The effective marks below are B_j=P j_j F P,
with P understood in the corresponding number sectors.
The first mark is on edge 01, from the canonical zero-field N=4 preparation.
The three actual normalized outputs are phi_i. Their leading P vectors are
beta_i=B_i/sqrt(b_i), where b_i=2,2,4. The complete original subsequent
ensemble is rho_i(t), including the possible second birth. The terminal N=8
Hamiltonian is exactly zero in this supplied model.

Define Z=Pi2 T Pi1 T P and M=P F*F P. The rotor low Hamiltonian and original
effective birth loss in the N=6 P sector are

    H_rot = K D - delta Z_inf* Z_inf/2,
    Gamma_B,inf = sum_j B_j,inf* B_j,inf,
    psi_i(t) = exp[t(-i H_rot-kappa Gamma_B,inf/2)] beta_i.

Here D is its self-adjoint diagonal realization on the common physical word
space; the remaining operators are bounded finite sums of physical shifts.
The resulting full effective ensemble has energy

    E_rot,i(t) = <psi_i(t), H_rot psi_i(t)>,

because its terminal sector also has zero energy. No survival normalization
is taken. First, for each finite T>0, we prove

    sup_(epsilon <= t <= T)
        |Tr(H rho_i(t))-E_rot,i(t)| -> 0.                         (1)

The notation epsilon as a time is in the model's fixed time units; multiplying
that lower endpoint by any fixed positive time constant changes no exponent.
In particular the same conclusion holds on every [t0,T], t0>0. The proof below
does not claim convergence of unscaled second moments or variance at fixed
positive physical time, and does not identify a physical recipient or supplier
of the lost/birth energy.

## 1. A weighted rotor semigroup estimate

Let L(theta)=-i delta G(theta)-kappa P_bright be the complete 96-dimensional
fast rotor fiber. The sharp-tail theorem supplies its analytic block form

    G = [[0,Q*],[Q,B]],
    ||exp(tau L(theta))|| <= C exp[-c sigma_min(Q(theta))^2 tau],
    sigma_min(Q(theta))^2 >= c1 sum_j sin(theta_j)^2.              (2)

It also establishes that Q is deficient at exactly eight sign phases. Both
constants here are positive and uniform on the five-torus. They need not be
optimal. All remaining phases have full column rank. Let r be any fixed
finite-support physical input, including each actual r_i=R_i/sqrt(b_i).

We claim, writing w=1+sum_e E_e^2 on physical words,

    ||w exp(tau L) r|| <= C_r (1+tau)^(-1/4),  tau>=0.             (3)

This is an H^2 Fourier estimate, not a bound for arbitrary normalizable inputs.
The chord coordinates are five fields; the other seven fields are affine
integer-linear functions of these coordinates and the finite charge label.
Thus the graph norm of w is equivalent to the vector-valued Fourier H^2 norm.

Here is a proof that does not choose individual eigenvalue branches. At a
deficient phase theta0 let K0=ker Q(theta0), viewed in the dark subspace.
Then ker L(theta0)=K0 and K0 is reducing: L and L* both vanish there. Every
other eigenvalue has strictly negative real part. Indeed an imaginary-axis
eigenvector must have zero bright part by the norm derivative, and its dark
equation then gives eigenvalue zero and Qd=0. Contractivity excludes a Jordan
chain at zero. Choose a small fixed contour about zero, excluding the stable
spectrum, and the analytic Riesz projection R(h), h=theta-theta0.

An analytic bounded invertible map U(h), U(0)=I, identifies R(h) with K0 and
its complementary projection with K0-perp. The two exactly separated blocks
of U(h)^-1 L(theta0+h) U(h) are A(h) and C(h). On the slow block,

    A(0)=0,             partial_j A(0)=0.                        (4)

For the derivative, the similarity-derivative terms vanish after projection
onto K0 because L(0) vanishes on it from both sides. The remaining term is
P_K0 L'_j(0) P_K0, which is zero because the dark-dark block of L(theta)
vanishes identically. This holds also at multiplicity two and four points.
Consequently ||A'(h)||<=C|h| and ||A''(h)||<=C locally.

The exact block semigroup inherits from (2) and bounded U,U^-1 the estimate

    ||exp(tau A(h))|| <= C exp(-c |h|^2 tau).                    (5)

Shrinking the neighborhood keeps the complementary spectrum strictly stable.
Its matrix exponential and its first two phase derivatives are bounded by
C(1+tau^2)exp(-c2 tau), uniformly locally. One way to see uniformity is a
fixed stable spectral contour for the bounded family and its differentiated
resolvent. No diagonalizability is required.

Duhamel differentiation of the exact exponential in (5) gives

    ||partial_j exp(tau A)|| <= C tau |h| exp(-c |h|^2 tau),
    ||partial_j partial_k exp(tau A)||
       <= C(tau+tau^2 |h|^2) exp(-c |h|^2 tau).                  (6)

Each integrand is a product of two or three semigroups whose time arguments
sum to tau; hence its exponential factor remains exp(-c |h|^2 tau).
Multiplication by the smooth U,R and input Fourier polynomial adds only
lower derivatives with bounded coefficients. A smooth partition of unity
around the eight deficient phases and their complement is legitimate; its
derivatives have fixed bounds. Away from those phases, compactness and full
column rank give a uniform stable exponential bound for L and its derivatives.

In five dimensions the squared L2 norm of the right side of the second
estimate in (6) is bounded, for tau>=1, by a constant times

    tau^2 integral_R5 (1+tau |h|^2)^2 exp(-2c tau |h|^2) dh
        = O(tau^(2-5/2)) = O(tau^-1/2).

The zeroth and first derivatives are smaller. The bounded interval 0<=tau<=1
is controlled by bounded analytic generator derivatives. Taking the square
root proves (3). In particular ||exp(tau L)r||<=C(1+tau)^(-5/4) also follows
from the sharp tail parent.

## 2. Weighted spin-to-rotor comparison on growing fast times

Embed each spin box into the common physical word Hilbert space, with chi_S
its orthogonal projection. Every normalized spin hop is a weighted rotor
shift inside the box, with zero amplitude at the boundary and zero extension
outside. The elementary bound 1-sqrt(1-x)<=x for 0<=x<=1 gives

    ||(F_S-F_inf)u|| <= C2/C ||w u||.                            (7)

For an input outside the box at least one field has |E_e|>=S+1, so its
indicator is also bounded by a constant times w/C. This accounts for the
extension, rather than only comparing interior coefficients. Charge labels
are finite. A single shift changes fields by at most one, and therefore
||w F_inf w^-1|| and ||w F_S w^-1|| have common finite bounds. Adjoint shifts
and each birth mark have the same properties. The finite polynomial formulas
for G_1,S and Gamma_1,S then give

    ||(L_S-L)u|| <= C3/C ||w u||,                             (8)
    L_S=-i delta G_1,S-kappa Gamma_1,S/2,

where L_S is zero extended. Each telescoping product uses (7) and the stated
weighted shift bounds. The original resolved and coherent losses coincide,
as their two sign ranges on a given edge are orthogonal.

Use the actual-birth parent's exact analytic intertwiner J_e=S_e V_e from
the W grades to the no-event spectral clusters. It obeys uniform ordinary
bounds on J_e and J_e^-1, and the exact full propagator is a contraction.
After removal of the scalar phase, the grade-one block generator in fast
time has the exact form

    A_e,1 = L_S + epsilon^2 R_e,1,     sup||R_e,1||<infinity.     (9)

All its semigroups have a common all-time bound, inherited by similarity from
the microscopic contraction. Extend this block by zero outside chi_S; that
extension has semigroup identity outside and the same common bound. Since
C^-1=K epsilon^2/delta, (8)-(9) imply

    ||(A_e,1-L)u|| <= C4 epsilon^2 ||w u||.                      (10)

Duhamel, using the bounded exact block semigroup on the left and the rotor
semigroup on the input, and then (3), gives for every tau>=0

    ||[exp(tau A_e,1)-exp(tau L)]r_i||
      <= C epsilon^2 integral_0^tau (1+s)^(-1/4) ds
      <= C epsilon^2(1+tau)^(3/4).                              (11)

All generators in this fast comparison are bounded; the weighted estimate
is applied only to the displayed smooth input evolution. This is a quantitative
growing-time estimate, not a substitution into the earlier
compact-time theorem.

The actual grade-one coordinate is epsilon r_i+O(epsilon^3) uniformly in S,
and its error is propagated with the common all-time bound. At tau=epsilon^-1
(physical time t=epsilon), the rotor amplitude and the error (11) are both
O(epsilon^(5/4)). Thus

    ||E_1 v(epsilon)||=O(epsilon^(9/4)),                         (12)

where v(t) is the full unnormalized N=6 no-event vector and E_1 its exact
commuting Riesz projector. Exact contraction and commutation imply the same
bound for every t>=epsilon. The Hermitian projector P_1 satisfies
||P_1-E_1||=O(epsilon^3), so its band contribution to the ordinary energy is

    |<P_1 v,H P_1 v>| <= C epsilon^-4 ||P_1 v||^2
                       =O(epsilon^(1/2)), t>=epsilon.           (13)

## 3. The second high band has an extra birth cancellation

The loose old estimate ||E_2 phi_i||=O(epsilon^2) is insufficient for ordinary
energy. A stronger estimate follows from the actual birth algebra.

For a birth j centered at A site a, outward hops F_c commute with j for c!=a.
For disjoint sites this is direct. If they share the birth B endpoint, both
orders vanish by hard-core occupancy. Outward operators F_c commute with one
another for the same reason, and F_a^2=0. These identities include finite-spin
amplitudes; no same-link opposite shift is interchanged in this argument.

The leading grade-r part of the canonical N=4 low column is
epsilon^r F^r Omega/r!. Compensation, normalization and backtracking need
at least two additional powers to change this minimal outward coefficient.
The grade-two row of the N=6 high projector has the leading blocks

    Pi2 E_2 Pi0 = epsilon^2 F^2/2 + O(epsilon^4),
    Pi2 E_2 Pi1 = -epsilon F + O(epsilon^3),
    Pi2 E_2 Pi2 = Pi2 + O(epsilon^2).                            (14)

These are the direct resolvent terms with denominators 2-0 and 2-1.
The grade-diagonal imaginary epsilon^2 loss does not change the displayed
minimal coefficients. The order-epsilon^3 grade-two numerator after the
actual birth is consequently

    j F^3 Omega/6 - F j F^2 Omega/2 + F^2 j F Omega/2.             (15)

It vanishes: it is the cubic coefficient of exp(-epsilon F) j exp(epsilon F)
on Omega, where j Omega=0. All remote commuting F_c cancel from this expression,
and exp(-epsilon F_a) j exp(epsilon F_a) is a polynomial of degree at most two
because F_a^2=0. This proof applies separately to both signs and hence to their
coherent sum.

W parity makes the grade-two numerator an odd analytic function of epsilon.
Indeed Xi=(-1)^W gives Xi_6 j=-j Xi_4, the canonical column has the usual
Xi parity, and E_2(-epsilon)=Xi_6 E_2(epsilon) Xi_6. Its first possible power
is epsilon^3 by grade counting; after (15) the next is epsilon^5. The actual
mark norm is epsilon sqrt(b_i)(1+O(epsilon^2)), with b_i bounded away from zero.
The exact E_2 range is a uniformly bounded graph over Pi2. Uniform analytic
remainders therefore prove

    ||E_2 phi_i||=O(epsilon^4).                                 (16)

Contraction preserves (16) at all later times. The same O(epsilon^3)
Hermitian/Riesz projector comparison then gives

    |<P_2 v,H P_2 v>|=O(epsilon^2),  t>=0.                       (17)

The finite S=1 control exactly cancels the integer coefficient (15) for all
three marks and rejects an altered middle coefficient. Refined contour
calculations at four epsilon values are consistent with (16). Those controls
are not the uniform proof and do not by themselves test the joint limit.

## 4. Weighted low-block control and its ordinary energy limit

Uniform weighted analyticity is needed; ordinary density convergence alone
does not settle the expectation of the unbounded limiting electric energy.
Here the original finite graph supplies that additional control.

On each physical sector put w=1+sum E_e^2. The finite-hop operators T,j and
their adjoints have uniform norms after conjugation by w. W and all its grade
projections commute with w. So does Q_S=D/C, which is uniformly bounded on
the spin box. Consequently C_S, Gamma and their adjoints have common weighted
bounds. Every resolvent Neumann series about W, the canonical projection
polar series and the intertwiner/inverse series converge for a common small
epsilon in both the ordinary and weighted operator norms. This proves all
cluster expansions, including their remainders, in the weighted algebra.
For the canonical polar formula, the adjoint factors are controlled as well,
by the same property for the generating operators; no unbounded conjugation
is silently commuted through an adjoint.

The exact no-event low coordinate a_0=Pi0 J_e^-1 v has physical-time generator

    A_e,0 = -i K D -i delta H4_S -kappa Gamma_B,S/2
                    +epsilon^2 R_e,0,
    H4_S = -Z_S*Z_S/2 -(M_S Q_S+Q_S M_S)/2,                      (18)

where R_e,0 and its w-conjugate have uniform bounds. Formula (18) follows
from the actual-birth parent low expansion, the canonical compensated H4
formula, and C_1=0. Its initial coordinate obeys

    a_0(0)->beta_i,       sup ||w a_0(0)||<infinity.               (19)

To verify the second fact, expand j U_e Omega in the weighted norm. Its
zeroth term vanishes and its leading term is epsilon B_i; the denominator
is bounded below by c epsilon. The near-identity intertwiners are bounded
in the same weighted norm. This is a fixed finite-support preparation, not
a moving high-flux family.

Write A_e,0=-i K D+B_e. On the spin box both B_e and w B_e w^-1 are uniformly
bounded. Outside the box extend the generator by -i K D and B_e by zero.
This extension leaves every embedded physical finite-spin trajectory unchanged.
The interaction picture of the diagonal unitary exp(-itKD), which commutes
with w, and the bounded perturbation series give

    sup_(0<=t<=T) ||w a_0(t)|| <= exp(C T) ||w a_0(0)||.           (20)

Thus a common weighted bound holds for every finite physical-time interval.
The limiting bounded part is B_inf=-i delta H4_inf-kappa Gamma_B,inf/2,
with H4_inf=-Z_inf*Z_inf/2. Indeed the normalized shifts converge strongly,
Q_S->0 strongly, and the epsilon^2 remainder tends to zero in ordinary norm.
Finite products preserve strong convergence because their norms are common.
The bounded perturbation/Dyson series about the same exp(-itKD), termwise
strong convergence and uniform tail bounds prove

    sup_(0<=t<=T) ||a_0(t)-psi_i(t)|| ->0.                        (21)

The limiting evolution has the same weighted bound by the same series or
by lower semicontinuity of the closed weight. Since |D|<=Cw, both ||D a_0||
and ||D psi_i|| are uniformly bounded. Self-adjointness then gives the
explicit expectation estimate

    |<a_0,D a_0>-<psi_i,D psi_i>|
       <= ||a_0-psi_i|| (||D a_0||+||D psi_i||).                 (22)

It tends to zero uniformly. Bounded strong convergence of H4_S, with the
compact continuous limiting path, similarly passes its expectation.

For the microscopic energy the Hermitian low coordinate is
y_0=Pi0 V_e* v, while a_0 uses J_e=S_e V_e. The ordinary comparison
S_e-I=O(epsilon^3) implies ||y_0-a_0||=O(epsilon^3), uniformly for all t>=0.
The exact Hermitian low Hamiltonian is

    H_e,low = K D +delta H4_S +epsilon^2 R_e,H,
    ||H_e,low||=O(epsilon^-2),                                 (23)

where the last bound uses ||D||=O(C) inside the spin box. Therefore replacing
y_0 by a_0 changes its expectation by only O(epsilon), even without any
weighted estimate for the full microscopic high vector. This avoids assuming
control of a rapidly spreading high component in (20). Combining (18)-(23)
proves ordinary low-energy convergence uniformly on [0,T].

## 5. Assembly and limits

The full ensemble energy equals <v,Hv> because the N=8 Hamiltonian vanishes.
Hermitian spectral separation makes this the sum of the three band energies,
without cross terms. Equations (13), (17), and the low-energy limit prove (1).
The high contribution is bounded by O(sqrt(epsilon)) for all t>=epsilon;
only the low-energy convergence uses a fixed upper time T.

This does not give an unscaled variance limit at fixed positive time. The established high norm
bound alone allows a large second moment because squaring H changes its
epsilon power. It also does not select lambda=0, the compensation, original
Markov instrument, canonical preparation, physical time or a reservoir.
Changing any of those, taking a volume limit, or moving the input to large
flux requires a new argument. No new axiom or retained audit status is used.

## 6. Relative growing-time moments and the sharper birth layer

Write f_i(tau)=||exp(tau L)r_i||^2, with c(1+tau)^(-5/2)<=f_i<=C(1+tau)^(-5/2).
The weighted Duhamel estimate gives, in the exact first
high coordinate after its scalar phase is removed,

    ||a_1(epsilon^2 tau)/epsilon-exp(tau L)r_i||
       <= C epsilon^2[1+(1+tau)^(3/4)].                          (A)

The O(epsilon^3) actual-output remainder is included here and propagated with
the exact block's common all-time norm bound. Its constants are independent of
tau and S in the stated joint sequence. Since the rotor amplitude is at least
c(1+tau)^(-5/4), the relative amplitude error is bounded by

    C epsilon^2(1+tau)^2.                                     (B)

Thus for any growing tau_e with epsilon tau_e->0, this relative error tends
to zero. The Hermitian first-high coordinate differs from a_1 by O(epsilon^3)
in ordinary norm, giving another relative error bounded by
C epsilon^2(1+tau)^(5/4), which also tends to zero. The high Hamiltonian block
is delta epsilon^-4[I+O(epsilon^2)], uniformly in S. Consequently along every
such sequence,

    E_high,1(epsilon^2 tau_e)
       = delta epsilon^-2 f_i(tau_e) [1+o(1)],                  (C)
    M2_high,1(epsilon^2 tau_e)
       = delta^2 epsilon^-6 f_i(tau_e) [1+o(1)].                (D)

These are relative statements about band contributions, not a relative
statement for the total mean, which can cross zero. They are uniform along
families whose maximum epsilon(1+tau) tends to zero.

The second-high contribution is O(epsilon^2) to the mean and O(epsilon^-2)
to the second moment by the preceding argument's improved E2 birth suppression
and Hermitian/Riesz comparison. The low second moment is uniformly O(1) on
fixed bounded physical-time intervals: in the exact low coordinate, ||D a_0||
is uniformly bounded, so ||H_low a_0|| is uniformly bounded. Replacing a_0 by
the Hermitian coordinate costs at most O(epsilon^-2)*O(epsilon^3)=O(epsilon)
in this energy-vector norm. This is stronger than applying the norm of H_low^2
directly to the coordinate density difference.

Since tau_e=o(epsilon^-1), f_i(tau_e)>=c(1+tau_e)^(-5/2) implies that (D)
dominates O(epsilon^-2). The squared mean is negligible relative to (D):

    mean^2 / [epsilon^-6 f_i(tau_e)]
       <= C[epsilon^2 f_i(tau_e)+epsilon^6/f_i(tau_e)] ->0.

Here the low mean is bounded and the second high mean vanishes. Therefore
the same relative asymptotic as (D) holds for the FULL unscaled variance in
this growing-fast-time window. This still says nothing about variance at a
fixed positive physical time, for which tau=t/epsilon^2 is outside the window.

### The ordinary mean's initial-layer scale

Equation (C) and the two-sided tail imply

    E_high,1 = Theta(epsilon^-2 tau_e^-5/2),

for tau_e->infinity, epsilon tau_e->0. The crossover to order-one high energy
is tau_e of order epsilon^(-4/5), or physical time of order epsilon^(6/5).
No asymptotic prefactor is asserted because the rotor theorem supplies only
a two-sided order bound.

In particular:

1. If t_e/epsilon^2->infinity and t_e/epsilon^(6/5)->0, the ordinary mean
   diverges to +infinity. The bounded low mean cannot cancel its positive
   diverging first-high-band contribution.
2. At t_e=x epsilon^(6/5) for fixed x>0, the high mean stays bounded above and
   below by positive multiples of x^(-5/2). The variance is of order
   epsilon^-4 times such an x-dependent positive factor.
3. If a_e/epsilon^(6/5)->infinity, a_e<=T eventually, ordinary energy converges
   uniformly on [a_e,T] to the common rotor energy.

For the third assertion, choose a comparison time tau_e that tends to infinity,
satisfies tau_e epsilon^(4/5)->infinity and epsilon tau_e->0, and obeys
epsilon^2 tau_e<=a_e. Such a choice exists because a_e/epsilon^(6/5)->infinity;
for example, with L_e=a_e/epsilon^(6/5), take

    tau_e = epsilon^(-4/5) min(sqrt(L_e),epsilon^(-1/10)).

Both entries in the minimum diverge; their minimum is eventually at most L_e,
and epsilon tau_e<=epsilon^(1/10)->0. At this comparison time (C) tends to zero.
Exact commuting-cluster contraction extends the norm bound to every later
time, while the O(epsilon^3) Hermitian/Riesz error contributes O(epsilon^2)
ordinary high energy. The low convergence is uniform on [0,T], and the second
high mean vanishes uniformly. This proves the third assertion without ever
substituting fixed laboratory time into (A)'s relative window.


## Evidence and independent comparison

The primary runner includes the earlier personal physical-matrix definitions
explicitly and declares their provenance; it reads no scientific files at
execution. It checks the exact primitive dark block and dark kernels at the
eight exceptional phases, detects a spurious linear dark term, and tests
finite-spin quadratic-weight boundary controls with a failing linear-weight
variant. It also builds the complete spin-one spaces, checks the actual birth
cancellation and an altered coefficient, and refines the second-band Riesz
action for three actual marks at four epsilon values. These finite controls do not prove
the uniform Sobolev estimate, growing-time comparison or limiting theorem.
Those claims are established by the written arguments above.

A separate checker reconstructed the ordinary-energy limit before receiving
the root proof. Its PRE used a different exact physical-word program for all
36 edge/sign/coherent first marks and an exponential-weight low-domain argument.
The released-source comparison additionally checks the stronger exact second
Riesz-band estimate and the growing-time refinement. Reports and immutable
source bindings are recorded in the review packet. Scientific checking does
not confer retained audit status.

Run:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py
```

## Imports

- [Sharp rotor tail](SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the complete physical Fourier generator, uniform fiber bound, exact exceptional set, and two-sided actual-input tail.
- [Actual birth on the fast time scale](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the model, canonical output coefficients, uniform exact cluster coordinates, low no-event coefficient and terminal-zero identity.
- [Bounded compensation target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the canonical Hermitian low coefficient and the analytic rotation convention.

Every imported statement retains its conditional model hypotheses. No density
limit is used as a substitute for the new weighted energy argument. This note
is a continuation of the fifth campaign's scaled-energy and sharp-tail results;
formal retained status belongs to the separate audit path.

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: ordinary_microscopic_cube_energy_after_the_birth_layer_bounded_theorem_note_2026-09-24
target_blocker_text: "The disappearance of birth-rescaled moments did not establish ordinary microscopic mean energy or control growing fast-time comparisons."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Determine fixed-positive-time unscaled fluctuations and physical supply/selection while retaining the original instrument."
conditional_surface_status: "Supplied lambda=0 compensated cube, actual canonical zero-field first birth, original marks, joint spin scaling and fixed positive parameters."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Weighted analytic estimates and an exact local cancellation prove an ordinary mean limit and bounded mesoscopic moment statements under explicit model hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Landing-review boundary and No-Go Discipline Gate

N1: the fixed compensated cube, specified zero-field first marks and joint scaling. N2: other preparations, graphs and dynamical choices remain open. N3: the Hamiltonian, compensation and instrument are supplied. N4: the linked sharp rotor tail and microscopic cluster results retain their stated domains. N5: finite controls check local cancellation, weights and projector examples; the analytic weighted-domain argument supplies the quantified limit. N6: ordinary mean convergence and relative variance in the shrinking-time window do not establish a fixed-positive-time variance limit. N7: the low electric expectation requires the proved weighted bound, not trace convergence alone. N8: the epsilon^(6/5) layer uses a growing-time comparison with epsilon*tau tending to zero and later exact contraction, not an unrestricted substitution.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Historical author checks remain provenance only. The full original packet remains recoverable at PR #9057's frozen head. No audit verdict or retained grade is applied.
