# Frozen precomparison derivation: full-ensemble early energy growth

This is an independent discovery calculation, not formal review/audit or a
retained-status claim. Prior supplier/cutoff work is disclosed exposure. Before
this text was written, only the root CONTRACT and the actual landed input
identities were read for this target; no root volume-power proof, constants,
REPORT or implementation was read. The source identity file records that
boundary. The following construction is a connected local Dyson expansion,
rather than a differential inequality for the current's time derivative.

## Result at the supplied-model scope

Use exactly the source30a9461 common law, Omega and ONE complete original
instrument from the contract. Put

    p0 = 123744 kappa delta,
    lambda = 5184 delta + 160 kappa,
    a = 16641 lambda,
    C_* = 241920 kappa K + 12165120 kappa delta,
    t0 = min{1/(2a), p0/(480 C_* a)},
    c = p0/2 = 61872 kappa delta.

These quantities are finite, strictly positive and independent of L for the
stated positive parameters. The derivation below gives, for every even L>=24
and 0<=t<=t0, for the full trace-one original GKSL ensemble including all
later births,

    <p_a>_rho(t) >= p0/2   for each A center a,
    Tr(h rho_L(t)) - <Omega,h Omega> >= c N t.

Here p_a is the complete adjoint-dissipator energy current from all original
marks at center a, including both loss terms. Its expectation is defined by
the actual unbounded-energy form, justified below. There is no first-event
survival factor, no conditioned trajectory and no replacement record map.
At K=delta=kappa=1, this conservative choice gives

    t0 = 1289/5516759566540800 ~= 2.3365165446357267e-13.

The initial p0 is an IMPORT from the exact landed first-birth source, applied
at Omega; its complete original-instrument power is123744*kappa*delta*N.
Translation invariance equates the N center contributions. This note does not
recompute the source's855 magnetic coefficients. Everything needed to turn
that initial identity into a volume-uniform all-birth interval is proved here.
The carrier, couplings, continuous-time GKSL law, state and readout remain
supplied inputs, not framework/foundation selections.

## 1. Local tensor law and bounded center generators

Place each A charge at its A site and each B charge plus its six incoming
integer links at its B site. Use the A-occupied hard-core tensor product as
an ambient local space, and then restrict to the invariant Gauss/total-charge
sector. A global constraint projector is never used as a nonlocal interaction.
Complete magnetic/jump words preserve the actual constraint. The field product
cutoffs commute with it. The same argument works for both original complete
instruments, separately; the coherent B_++B_- is never split into hidden signs.

Write h=K D+A with

    D = sum_e d_e,
    d_ab=(1-n_b)E_ab(E_ab-q_a),
    A=sum_{unordered distance-two A pairs} A_ac,
    A_ac=-2 delta (F_c F_a P)^*(F_c F_a P).

All d_e mutually commute and are diagonal, supported at the adjacent A/B
cells. Integer fields and q_a=+/-1 give d_e>=0. Each A_ac is supported on its
two complete stars. It has total rotor-shift length at most4. A birth B_m has
shift length at most2; Gamma_a=kappa sum_{m at a}B_m^*B_m has shift length at
most4. These are full words; no intermediate F is individually field-clipped.

For o occupied B neighbors, F has outgoing incidence6-o and inverse incidence
o+1, so ||F||^2 <= (6-o)(o+1)<=12. For either complete original instrument,

    Gamma_a = 2 kappa (5-o) F_a^*F_a

on the input-o block. The cross-sign term vanishes because the final A signs
are orthogonal. Thus the respective o=0,...,5 norm bounds in units kappa are
60,80,72,48,20,0; o=6 also gives0. In every later sector,

    ||Gamma_a|| <= 80 kappa,
    ||A_ac|| <= 288 delta.

There are18 distance-two A neighbors. Define A_a=(1/2)sum_c A_ac. Then
sum_a A_a=A, ||A_a||<=2592 delta, and A_a is supported in the cell ball B_3(a).
The individual jump stars are in B_1(a).

Conjugate by the electric unitary:

    O^I(t)=exp(i K D t) O exp(-i K D t).

Because all d_e commute, every d_e commuting with O cancels from this
conjugation exactly. Only electric edges meeting supp O need be included.
Therefore supp O^I lies in the ONE-step cell halo of supp O. There is no
iterated electric propagation. Conjugation changes neither operator norm
nor rotor-shift range. The time-dependent center adjoint generator

    G_a(t)(O) = i[A_a^I(t),O]
      + kappa sum_{m at a} B_m^I(t)^* O B_m^I(t)
      - (1/2){Gamma_a^I(t),O}

has support U_a subset B_4(a) and norm <=lambda on bounded operators.
Indeed the gain CP map has norm ||Gamma_a||, and the anticommutator has norm
at most ||Gamma_a||. Both are included. The interaction-picture density
satisfies rho_I'=sum_a G_a(t)_* rho_I. No scalar event-rate substitution occurs.

If U_a is disjoint from supp O, G_a(t)(O)=0 EXACTLY. This uses the cancellation
of gain against the actual anticommutator. Gain alone would violate this
identity even on I, and would destroy the connected expansion below.

## 2. Product boxes and polynomial local-current bounds

First work at fixed finite L in the finite product field box |E_e|<=R.
Compress the WHOLE magnetic pair term A_ac,R=Pi_R A_ac Pi_R and each original
B_m,R=Pi_R B_m Pi_R. Define Gamma_a,R from B_m,R, not by compressing Gamma_a.
The electric D_R is its diagonal restriction. The finite box is a CPTP GKSL
law with the original labels; its total energy identity is ordinary finite
matrix differentiation. The above norm/support/shift bounds survive uniformly
in R: in particular Gamma_a,R<=Pi_R Gamma_a Pi_R. The electric one-step halo
remains exact. All subsequent projection estimates hold also when s>R, by
interpreting the inner field projection as its intersection with this box.

Let P_s project onto |E_e|<=s for all fields of this finite volume, and let
p_a,R be the center energy current

    p_a,R = kappa sum_{m at a} B_m,R^* h_R B_m,R
                         - (1/2){Gamma_a,R,h_R}.

Terms of h_R whose tensor supports miss the root star cancel, including loss.
Exactly36 electric edges meet that star. Magnetic pairs with intersecting
support have an endpoint among the root and its18 distance-two A neighbors;
there are264 such unordered pairs. Every such support is in B_5(a). Hence
supp p_a,R subset B_5(a), and supp p_a,R^I(t) subset B_6(a).
The sparse check independently enumerates these actual whole-star counts.

On field cap s, each birth image has cap at most s+2. The relevant electric
sum is bounded there by36 K(s+2)(s+3), since |E(E-q)|<=|E|(|E|+1).
The gain CP norm and anticommutator bound therefore give

    ||P_s p_a,R^I(t) P_s|| <= C(s),
    C(s)=5760 kappa K (s+2)(s+3) + 12165120 kappa delta.

The magnetic coefficient is2*80*264*288. This is a compressed unbounded-form
estimate, not a bound on the full infinite-rotor current. It is uniform in
volume, R and t. Electric conjugation commutes with P_s, so the same bound
holds in the interaction picture without differentiating its field phases.

For any finite-field-core observable O, the local generator obeys the useful
restriction estimate

    ||P_s G_a(t)(O) P_s||
        <= lambda ||P_(s+4) O P_(s+4)||.                 (1)

For the commutator and loss pieces, every operator multiplying either side of
O shifts fields by at most4. For the gain, B shifts by at most2 and the CP
norm is <=80kappa. Insert the larger projection next to each factor to prove
(1). It works for arbitrary signs of O and for nonpositive Dyson coefficients.
No assertion that rho itself has bounded fields is made.

## 3. Connected adjoint Dyson expansion and its majorant

The cell balls in the three-dimensional nearest-neighbor graph have

    |B_4|=129,       |B_6|=377.

Torus identification can only lower these cardinalities. The initial current
support has at most377 cells. After j nonzero center operations its support
has at most377+129j cells. A fixed cell can lie in U_a for at most129 center
positions a (using all parity sites as a safe upper bound). Therefore the
number of potentially nonzero ordered center strings of length l is at most

    product_(j=0)^(l-1) 129(377+129j)
      <= 16641^l (l+2)!/2.                             (2)

No torus Hilbert dimension or global event rate enters (2). Repeated centers
are included; this is not a self-avoiding-walk estimate. The bound follows
from377<=3*129, so the rising factorial is bounded by(3)_l.

At fixed R all adjoint Dyson expansions are ordinary norm-convergent finite
matrix series. Apply them to p_a,R^I(t), with its t fixed, and take the Omega
expectation. Equation(1), starting from P_0 Omega=Omega, bounds every length-l
term by lambda^l C(4l). The electric phase has Omega as a zero-eigenvalue
vector, so the length-zero term is <Omega,p_a,R Omega>=p0 for R>=8, for all t.
This last equality is the exact source initial-power identity; the R>=8
allowance keeps every relevant complete low-order word inside the box.

The ordered time simplex has volume t^l/l!. From(2), for z=a t<1,

    |Tr(p_a,R rho_R(t))-p0|
       <= sum_(l>=1) binom(l+2,2) C(4l) z^l.           (3)

This is a bound on the FULL original ensemble. Every later jump and all
Hamiltonian/loss insertions occur in the Dyson coefficients. Adjoint ordering
reverses the time labels but changes neither the support count nor the norm
bound. The time-dependent electric phases have been kept exactly.

For l>=1, (4l+2)(4l+3)<=42 l^2, hence C(4l)<=C_* l^2. Elementary generating
function differentiation gives the exact identity

    sum_(l>=1) binom(l+2,2) l^2 z^l
      = (z d/dz)^2 (1-z)^(-3)
      = 3 z(1+3z)/(1-z)^5.

For0<=z<=1/2 this is at most240 z. Consequently

    |Tr(p_a,R rho_R(t))-p0| <= 240 C_* a t              (4)

uniformly in R>=8 and L. The proposed t0 makes the right side <=p0/2.
The two magnetic/current geometry radii must not be confused with their
one-step electric halos; using radii3 and5 after conjugation would be wrong.

## 4. Uniform local moments before removing the cutoff

The same expansion also provides genuine local electric moment bounds. Take
O=E_e^(2p), p a positive integer. It is diagonal and supported on the B cell
carrying that edge, so O^I=O and its initial expectation is0. The connected
count starts with one cell; it is bounded by16641^l l!, because
1+129j<=129(j+1). The compressed observable on field cap4l has norm(4l)^(2p).
Thus, uniformly in finite L and R,

    Tr(E_e^(2p) rho_R(t))
        <= 4^(2p) sum_(l>=1) l^(2p) (a t)^l,  a t<1.  (5)

For a t<=1/2, convenient explicit consequences are

    <E_e^2> <=192 a t,
    <E_e^4> <=76800 a t.

These follow from z(1+z)/(1-z)^3 and
z(1+11z+11z^2+z^3)/(1-z)^5, respectively. They precede the limit R->infinity
and are independent of volume. Higher even moments follow from the same
absolutely convergent series. They are not inferred from trace convergence.

## 5. Removing R, identifying the unbounded law, and integrating energy

Here the order of limits is explicit: fix any finite L, remove R using weighted
estimates, prove the energy identity, and then note that (4)-(5) and t0,c do not
depend on L. No interchange with an infinite-volume limit is used.

For completeness, a fixed-volume weighted construction identifies the target
process directly. Define W=1+sum_e |E_e|. The diagonal electric flow preserves
W. Each A or Gamma term has total field-shift length <=4; each birth has <=2.
On trace class, the summed interaction-picture bounded perturbation has norm
at most N lambda. Its length-n density Dyson coefficient rho^(n)(t) obeys

    ||rho^(n)(t)||_1 <= (N lambda t)^n/n!,
    rho^(n)(t)=P_{W<=1+4n} rho^(n)(t) P_{W<=1+4n}.

The corresponding finite-box coefficient has the same bounds. Consequently
for every fixed integer p and fixed T,

    sum_n ||W^p rho^(n)(t) W^p||_1
      <= sum_n (1+4n)^(2p) (N lambda T)^n/n! < infinity

uniformly for0<=t<=T, and the same estimate holds for all product boxes.
Every fixed-order coefficient stabilizes exactly once R>=4n+8. This guard
also contains the internal birth excursions in Gamma_R; compressing Gamma
instead would not establish the same finite cutoff law. Conjugation by D_R
and D is identical on these complete contained field words. Dominated
convergence therefore gives weighted trace convergence for every fixed p,
uniformly on compact time intervals, not merely trace-norm convergence.

The limiting trace-class Dyson solution is unique for the integral equation
with the original bounded interaction-picture generator. Positivity and trace
one follow from the CPTP finite-box limits. Returning from the electric
interaction picture gives exactly the original h and original complete mark
GKSL law. The generator uses each original gain map throughout; tracing its
labels for this energy observable does not replace the marked process or its
coherence. Fixed-volume marked-history convergence can equivalently be obtained
by inserting label copies in the same finite-word expansion; no selected sign
or Poisson count is substituted.

At fixed volume, h is K D plus a bounded operator of norm<=2592delta N and is
self-adjoint on Dom D. On the finite-field core, D is bounded by a constant
times W^2. The current is a finite sum of degree-at-most-two field polynomials
times finite shifts and bounded hard-core words. The weighted convergence
above therefore makes its quadratic-form expectation and the actual h mean
well defined; all moments needed here are finite. No self-adjoint current
extension or trace-only energy limit is assumed.

In more detail, current coefficients are locally bounded by C(s) on each
finite-field cap. Their global fixed-volume finite-word expression has a
W^2-relative bound uniform in R. Low-order current expectations coincide for
R>=4n+8 and their Dyson tails have the same polynomial-times-factorial fixed-N
majorant. Thus the current limits agree with the actual original-current form
on the limiting state. Alternatively (3) is a summable local majorant and its
coefficients stabilize, giving the same limit and continuity directly.

For each finite box the EXACT identity, with Hamiltonian commutator canceled,
is

    Tr(h_R rho_R(t))-<Omega,h_R Omega>
       = integral_0^t sum_a Tr(p_a,R rho_R(s)) ds.

The left side converges in the weighted topology; h_R is the compression of
h, so its expectation on the supported rho_R is the actual h form there.
The right side converges by (3)-(4) for the stated interval. Therefore

    Tr(h rho(t))-<Omega,h Omega>
       = integral_0^t sum_a Tr(p_a rho(s)) ds
       >= (p0/2) N t.

This proves the claimed volume-uniform early interval under the supplied
model assumptions, including all later births and the exact loss current.
It makes no late-time sign, permanent-record, heat/work or native-selection
claim. A supplier ledger needs its separate interaction/controller accounting;
that is not used in this argument.

## 6. Evidence, limits and comparison boundary

The local sparse check used no author root code/report. It enumerated19 active
centers,264 unordered magnetic pairs,36 electric edges, the radius5 current
support and radius6 electric halo, and129/377 ball cardinalities. It verifies
all six occupation incidence coefficients,32 exact connected-count/series
coefficients, the explicit rational unit-parameter choice, and undercounting
controls. It used approximately0.456 CPU seconds and20.3MB peak RSS, within
the initial30CPU/150MB price. No full torus or large Hilbert matrix was built.

These checks are finite discriminators, not substitutes for the operator/domain
proof. The initial power is the explicitly linked landed theorem input. The
new all-birth/volume-uniform extension has no intentionally omitted terminal
lemma in this PRE argument, but remains an independent discovery derivation
awaiting adversarial comparison; it is not a formal PASS or audit outcome.

Root proof/constants/REPORT were not read before this PRE was frozen. Any
subsequent comparison must preserve these bytes and record later corrections
separately.
