# Controlled components and second-birth bounds for the actual first output

Primary-author conditional corollary, 2026-09-23. This argument is written
before its new controls and independent reconstruction. It uses the checked
prepared-sector theorem at AUTHOR_SEAL
dfc55f6eac748bb11130fe3a8e5544194c6babd810c0c06d45e177c56c72df7e and
independent FINAL 4bbbdcf3fa5a12181ccaf4e9ad09ec5dfb82fe4a078d5256ccad67caedf10cfe.
It derives consequences for an unselected actual output without assuming
that its complementary component has a full state or waiting-law limit.

## 1. Setup

Use the supplied eight-site spin ring, K,delta,kappa>0,
eta=K S(S+1)=delta/epsilon². In the six-record P space let F be the
physical rotor H2=-4 flat projection and J its compact isometry. Write
h_F=K D_F+delta H4_F and

 U_S(t)=exp[-it(eta(H2_S+4I)+delta H4_S-i Gamma_S/2)],
 V(t)=J exp(-2 kappa t) exp(-it h_F) J† on F H6.

The centered scalar phase has no effect on probabilities. Use a common
rotor-space extension of the physical finite-spin contractions as in the
prepared proof. We will use, uniformly on each compact time interval,

 U_S(t) F -> V(t) F,       U_S(t)† F -> V(t)† F           (1)

strongly. The first is the checked theorem. The second follows by applying
exactly its weighted-core/crossing-corrector argument with the sign of the
Hamiltonian reversed. The loss keeps its negative no-event sign, so the
adjoint propagator is still a contraction. The flat Hamiltonian becomes
-h_F, selfadjoint on the same f² domain; weighted-core bounds and transverse
crossings are unchanged. The residual powers and density extension still
apply. This sign reversal is an analytic extension of the checked proof,
not an inference that arbitrary strong limits automatically pass to adjoints.

Let psi be any fixed actual normalized first-mark rotor output from a
normalizable initial field, for either stipulated instrument. Its flat
weight is exactly 1/2 by the checked complete output spectrum. Put

 phi=F psi,     chi=(I-F)psi,     ||phi||²=||chi||²=1/2.

For the zero-circulation initial all-A-plus state, the normalized finite-spin
first output equals this compact psi exactly for every sufficiently large S:
its hop and birth use different initially zero-field links, each of amplitude
one. More generally the conclusions below allow physical initial psi_S->psi.

## 2. A fixed part of the actual survival, without a projection operation

The adjoint limit in (1) implies

 sup_(0<=t<=T) |<U_S(t)phi,U_S(t)chi>| ->0.              (2)

To see this, U_S phi approaches V phi. Also U_S† V(t)phi approaches
V(t)† V(t)phi=exp(-4 kappa t)phi. Strong convergence in (1), uniform for
each fixed vector and t, is uniform over the compact set
{V(t)phi:0<=t<=T}: approximate that set by a finite net and use the common
contraction bound. Pairing with chi proves (2). The same argument works
with convergent embedded initial vectors by contraction.

Consequently the true unselected six-record survival obeys

 S_S(t)=1/2 exp(-4 kappa t)+q_S(t)+o_T(1),               (3)
 q_S(t)=||U_S(t)chi||²,     0<=q_S(t)<=1/2,

uniformly on compact times. No F projection is performed during the actual
evolution. The decomposition is a statement about scalar probabilities,
not a trace-norm assertion that the full quantum state becomes a classical
mixture. No convergence of q_S is being assumed.

In particular,

 limsup_(S->infinity) S_S(t)
       <= [1+exp(-4 kappa t)]/2,                       (4)

with the corresponding uniform compact-time one-sided bound. This gives
at least one half of the prepared-clock formation probability inside the
actual first-output process, without identifying the remaining waiting law.

## 3. Exact finite-spin loss bound and compactness of the unresolved clock

For each P charge word, a next birth is possible only when the two vacant
B sites are adjacent on their four-cycle. Then their common A site is unique.
It can hop to either empty B neighbor and form on the other edge. A fixed
resolved mark and final word/field uniquely recover the initial word/field.
Thus every resolved B†B is diagonal in the physical charge/field basis.

Each hop weight is at most one. At a physical unused birth link with field E,

 g_(S,+)(E)²+g_(S,-)(E)²=2[1-E²/(S(S+1))] <=2.

The two old-hop destinations therefore give

 0<=Gamma_S<=4 kappa I.                                (5)

This holds on the complete physical six-record P space, including spin
boundaries, and on the bounded common-space extension with clipped amplitudes.
For an unphysical integer E the displayed sum identity is replaced by the
bound that each clipped squared amplitude lies between zero and one; (5)
still follows. No negative unphysical squared amplitude is used.
Both instruments have the same loss by the newborn-pattern orthogonality
already checked in the prepared-sector comparison.

For the physical sequence, (5) gives the exact survival lower bound
S_S(t)>=exp(-4 kappa t). It also makes the complementary functions q_S
nonincreasing and uniformly Lipschitz, with |q_S'|<=2 kappa and q_S(0)=1/2
when chi lies in the physical spin box. Compact flat and actual-output seeds
have this property for all sufficiently large S. General convergent embeddings
inherit the conclusions by approximation; the common clipped extension obeys
the same bound.

Arzela--Ascoli and a diagonal extraction supply compact-time subsequential
limits q with q(0)=1/2, 1/2 exp(-4 kappa t)<=q(t)<=1/2.
Every such survival limit has the component displayed in (3).
This does not prove a unique residual clock or rule out a defective tail.

## 4. Finite electric-window observables of the actual output

Let R_N=J 1_(|f|<=N) J†. This is a finite-rank projection inside F,
with fixed N independent of S. Equation (1) gives

 sup_(t<=T) ||R_N U_S(t)chi|| ->0.                       (6)

Indeed each of its finitely many frame coefficients is the pairing of chi
with U_S† acting on a fixed flat vector. The prepared convergence then yields

 R_N |U_S(t)psi><U_S(t)psi| R_N
   -> R_N |V(t)phi><V(t)phi| R_N                        (7)

in trace norm, uniformly on compact times. The same conclusion holds for
mixed first outputs by trace-class approximation. Compact operators supported
on F follow by finite-rank approximation.

Thus finite electric-window statistics inside the flat sector retain the
derived electric/H4 evolution as an observable component of the actual
unselected first output. No additional state selection is needed to establish
the expectation values in (7). The projection describes the specified
observable; this does not establish a local apparatus that measures it.

Replacing R_N by F, taking N with S, using an unbounded electric moment, or
claiming full-state trace convergence is not justified by this argument.
Complementary probability can occupy flat vectors at circulation of order S;
the new unprepared numerical probes motivate retaining this distinction.

## 5. A microscopic unconditioned two-birth bound from the original state

Now start at four records, all A plus and all B empty, with all electric
links zero. For every integer S>=1, the target pre-first no-event dynamics
on this particular input is scalar:

 H2_S=-8,     H4_S=24,     Gamma_first=16 kappa.          (8)

There are eight one-hop paths and twenty distinct grade-two outputs, each
with two path orders and unit amplitude. Their Grams are 8 and 80, so
H4=8²-80/2=24. Four hops cannot wind the eight-site ring. Every resolved
first mark has Gram one and every coherent edge mark Gram two on this input.
Its first clock is therefore exactly Exp(16 kappa), with the fixed normalized
outputs covered above. This finite-spin statement uses the zero-field input;
it is not claimed for an arbitrary finite-spin field.

Let P8,S(t) be the target probability that both further records pairs have
formed by t, so all eight sites are occupied. Integrating over the first
time and its finite mark set, (4) and (5) imply

 B(t)=1/2-(2/3)exp(-4 kappa t)+(1/6)exp(-16 kappa t),

 sup_(t<=T) [B(t)-P8,S(t)]_+ ->0,
 P8,S(t)<=2B(t)  for every S>=1 and t>=0.                (9)

The lower bound is the positive convolution of
16 kappa exp(-16 kappa s) with
[1-exp(-4 kappa(t-s))]/2. The upper bound uses the exact hazard bound (5).
No second-clock limit was assumed to take that convolution.
Both bounds are nonnegative because their integral representation is positive.

The inherited microscopic-to-target trace-density error is O(epsilon)
uniformly in S on a fixed graph and fixed time interval. The projection onto
eight occupied sites is bounded. Therefore the same limiting lower bound
and upper bound up to O(epsilon) hold for the unconditioned microscopic
number probability under the joint scaling. This is a deterministic original
initial-state result, not a theorem obtained by conditioning a microscopic
trajectory on its first random mark.

## 6. Scope and verification plan

The proof extends the prepared theorem's adjoint core argument explicitly,
then uses contractions, finite-rank observables, a local exact loss count
and an exact first-sector path count. Planned independent checks should
target the adjoint implication, the physical-box extension, the finite-spin
loss identity and the first-clock convolution, rather than fitting q_S.

Completed author controls verify the finite-spin first-sector path weights
and the diagonal loss bound on full physical P spaces for S=1,2,4,8, and
check the count convolution symbolically. Complete saved unprepared spin
propagations at S=64,96,128,192 corroborate (2), (6) and the observable
distinction. At S=192, t=1.2, K=.4, delta=.7, kappa=.3, the |f|<=2 flat-window
density differs from its predicted component by about 2.06e-4 in trace norm;
the complementary probability in that window is about 1.24e-8. These data
are not a generic-state or monotone convergence certificate. No extrapolated
semiclassical process or full complementary limit is imported here.

This is a finite ring with at most two formations from the stated original
state. It does not establish indefinite production, local measurement
implementation, a spatial field phase, finite-resource completion, native
quantum-law selection or an empirical/TOE identification.
