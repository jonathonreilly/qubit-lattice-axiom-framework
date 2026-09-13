---
claim_id: native_positive_ward_scalar_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "Supplied infinite cubic pi-flux Gaussian CAR model: reconstructed all-parity impurity gap and an elementary rational certificate 7<h²alpha<330 for the complete 90-term bounded Ward scalar."
upstream_dependencies: []
runner: scripts/native_positive_ward_scalar_2026_09_13.py
---

# Positive native Ward scalar from elementary bounds

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

The bounded native Ward scalar defined below is strictly positive in the
supplied infinite cubic Gaussian model. An elementary certificate proves
7<h²alpha<330. Every scalar supplier is derived here from exact return counts;
no inherited numerical interval or high-precision oracle is required.
This is an author proposal with actual current-surface status conditional-support.
Independent source review and formal audit remain pending.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Analytical CAR and infinite-gap derivations with a finite rational error certificate for a supplied model."
trace_class: upstream_support
target_claim_id: native_infinite_star_node_reduction_note_2026-09-09
target_blocker_text: "Determine the sign of the complete native Ward scalar while retaining its source corrections and rigorous approximation error."
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Independently review the scalar unit and the separate physical Dirac-node identification; investigate the complete low-energy interacting theory."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## 1. Exact target, imports and obligation graph

**Theorem.** For the infinite cubic pi-flux CAR model specified in section 2,
for every h>0, the scalar alpha in (1.1) exists and satisfies 7<h²alpha<330.

Let A run over the 15 two-element subsets of the six center-incident legs.
Write D_A=H0+B_A, R_A=-D_A^-1, J_A=2i gamma(d_A), g=gamma(e0), and

    x_A=R_A Omega, v_A=R_A J_A R_A Omega,
    8alpha=Re[<x,T x>-<x,Tg v>].                         (1.1)

Here T_(C,A)=1 if A and C are disjoint and 0 otherwise. It acts on the
15-channel direct sum; g acts identically within each channel. Each row has
six entries, so ||T||=6, and ||g||=1. Equation(1.1) retains all 90 ordered pairs.
The gap proved in section 4 makes every term bounded. The reference energy
in every D_A is the original vacuum energy.

The physical identification of (1.1) with the original star's Dirac-node
coefficient is a separate source bridge, described in the review record.
The theorem here proves positivity of the explicitly defined bounded scalar.
It does not derive the chosen model or reference state from the framework
axioms. It gives no fixed-coupling phase, mass gap, empirical prediction or
completed TOE by itself.

| Input or obligation | Role | Provenance and status in this unit |
|---|---|---|
| Cubic pi-flux nearest-neighbor K, CAR and pure Gaussian Omega | Supplied model and reference | Defined explicitly in section 2; their selection as physical law is open |
| Elementary radial scalar bounds | Mathematical supplier | Proved here in section 3 from exact counts and a uniform tail |
| Infinite D_A>=h/4 | Resolvent-domain and error premise | Reconstructed here in section 4, including the energy normalization and form limit |
| Bounded Ward field and source identities | Algebraic reduction | Proved here in sections 5–6 |
| Moments and complete signed trial contractions | Finite coefficient identities | Explicit table/recurrence here and machine-readable polynomial data; re-derived by the algebra runner |
| Source errors and final positive interval | Decisive certificate | Rational arithmetic in section 7; different finite native implementations challenge the identities |
| Original star Dirac-node interpretation and full interacting consequence | Physical bridge outside this theorem | Remains separately conditional; no inherited numerical conclusion is promoted |

No new axiom or primitive is proposed. Standard CAR, Fock space, the spectral
theorem and finite-dimensional determinant identities are mathematical tools.
Their needed hypotheses are stated in the corresponding steps. The theorem
covers h>0 in the specified infinite model. It does not include h=0, a changed
flux/reference, finite-size sign extrapolation or an arbitrary interacting bath.
The strongest downstream missing step is control of the complete interacting
low-energy theory and its physical realization, beyond this bounded scalar.

## 2. Supplied native model and normalization

Use real Majoranas gamma(f), with{gamma(f),gamma(g)}=2 f dot g. On Z³,
K_(r,r+e_a)=h(-1)^(sum_(b<a)r_b), K^T=-K, with all other entries zero.
Its positive one-particle frequency is omega=|iK|. In hopping units h=1,

    -K²=4 sum_a sin²k_a,
    <gamma(f)gamma(g)>=f dot g+i f dot K omega^-1 g.

These equations specify the pure free Gaussian reference Omega. The free
Hamiltonian H0 is normal ordered so H0 Omega=0 and
[H0,gamma(f)]=i gamma(Kf). Its one-particle frequency is bounded by 2sqrt3.
The Fock representation and the local-polynomial core used below are with
respect to this supplied reference. No impurity vacuum is assumed.

For each pair A, d_A has entry-K_(0,j) at its two selected neighbors and zero
elsewhere. Thus||d_A||²=2 in h=1 units and d_A dot e0=0. Set
B_A=i gamma(e0)gamma(d_A). This reverses exactly those two native bonds.
Perpendicular pairs form class P (12 pairs); opposite pairs form class O
(3 pairs). Finite approximants are fully antiperiodic even cubic tori tending
to infinity. The finite fixtures used by the runner are normalization and
identity checks; no measured finite-volume scalar is substituted into (1.1).

## 3. Elementary scalar suppliers

For X=4 sum_a sin²k_a, the distribution is X=6(1-Z), with
Z=(cos x+cos y+cos z)/3. Its law is symmetric. Let p_(2n)=E Z^(2n).
Equal positive/negative coordinate steps give

    p_(2n)=binom(2n,n) sum_(j=0)^n binom(n,j)²binom(2j,j)/36^n.

For Z>=0, Z^(2n)<=exp[-2n(1-Z)]. On[-pi,pi]^3,
1-Z>=2|x|²/(3pi²), by concavity of sine on[0,pi/2]. Translation by(pi,pi,pi)
exchanges the signs of Z. Twice the positive-part integral is therefore
bounded by the Gaussian integral on R³, giving

    p_(2n)<=3sqrt3 pi^(3/2)/(32 n^(3/2))<n^-3/2, n>=1.

The final strict constant follows from27(22/7)^3<1024 and pi<22/7.
One elementary proof of the latter is the positive integral
integral_0^1 x^4(1-x)^4/(1+x²) dx=22/7-pi, by polynomial division.
Thus for N256 the return tail is at most integral_256^infinity x^-3/2 dx=1/8.
Writing P_N=sum_(n=0)^N p_(2n), monotone convergence gives

    P_N/6 <= A0=E X^-1 <=(P_N+1/8)/6.                   (3.1)

For r=-1,1,3,5,7,9 and a=r/2, the averaged binomial series gives

    L_r=6^a sum_(n>=0) binom(a,2n)p_(2n).               (3.2)

After N=256 the coefficients have a fixed sign and decreasing absolute value.
For consecutive even indices their ratio is
(a-m)(a-m-1)/[(m+1)(m+2)], with m even and m>a; its absolute value is less
than 1 because a>=-1/2. Consequently the signed tail in(3.2) lies between
zero and binom(a,514)/8. Outward rational square roots enclose the prefactor.
The series interchange is justified by absolute summability: the binomial
coefficients are bounded for each fixed a, and sum p_(2n)<infinity; odd
absolute powers of Z are bounded by the preceding even powers. C0=L_-1.
All needed odd radial moments and inverse moments now have finite rational
certificates from the same fixed return count. The exact even moments are

    M_n=sum_(a+b+c=n) n!/(a!b!c!)
                    binom(2a,a)binom(2b,b)binom(2c,c).

No sampled momentum value is used to bound an infinite scalar.

## 4. Infinite impurity gap

Set h=1 here. On a finite fully antiperiodic even cubic torus, K is the actual
real skew nearest-neighbor pi-flux matrix, with one-particle frequencies at
most 2sqrt3 and no zero frequency. The free Fock Hamiltonian is the quadratic
operator(i/4)gamma^T K gamma with its vacuum energy E0=-Tr|iK|/4 subtracted.
For a two-leg set A take d_j=-K_(0j) on the two chosen neighbors and zero
elsewhere, a=e0, B_A=i gamma(a)gamma(d). This is precisely the bond-reversal
perturbation DeltaK=2(ad^T-da^T), not a new source or a mean-field defect.

Let A_L(s)=<a,(s²-K²)^-1 a> and G_(2,L)(s) be the Green entry
between the center and its same-axis two-step translate in the displayed
gauge. Put D_L(s)=A_L(s)-G_(2,L)(s). Coordinate symmetry gives s²A_L+6D_L=1. On the center and normalized signed
neighbor sum, the two-by-two resolvent is

    [[s A_L,-sqrt2 D_L],[sqrt2 D_L,s B_L]],
    B_L=A_L for perpendicular pairs, B_L=D_L for opposite pairs.

The matrix determinant lemma therefore gives the exact ratios

    d_O=1-(8/9)(1-z)²,
    d_P=(1+2z)²/9+8s²A_L², z=s²A_L.                    (4.1)

Both are at least 1/9. Pairing positive and negative skew frequencies and
integrating log[(s²+b²)/(s²+a²)] gives pi(b-a), hence the finite Fock minimum
relative to the original vacuum is

    DeltaE_(A,L)=-(1/(2pi)) integral_0^infinity log d_(A,L)(s) ds.

There is no omitted vacuum-energy constant or parity division. Restricting a
physical parity sector can only increase this all-parity lower bound.

For each s>0, AP Riemann sums converge to A(s). The following uniform bounds
justify the energy-shift limit without importing a finite inverse-square bound.
Near zero, d>=1/9, d_O<=1 and d_P<=1+8/s², since 0<=s²A_L<=1 and A_L<=s^-2.
Thus |log d| is dominated by log9+log(1+8/s²), an integrable function near 0.
For s>=4 put u=s², w=1-uA_L. Then 0<=w<=6/u and
0<=6/u-w=E[X²/(u(u+X))]<=42/u² (the local moments are6,42 for all sufficiently
large even tori). Expanding (4.1) gives

    |d_P-1|<=168/u²+288/u³<=186/u²,
    |d_O-1|<=32/u².

Because d>=1/9, |log d|<=9|d-1|. These uniform s^-4 bounds supply domination
at infinity. This establishes DeltaE_(A,L)->DeltaE_A with the same integral
and infinite Green entry, independently of the older finite-gap theorem.

It remains to show DeltaE_A>1/4, using elementary inequalities. Cauchy-Schwarz
and EX=6,EX²=42 give 1-s²A(s)>=6/(s²+7). The opposite determinant then yields

    g=(8/9)(1-s²A)²>=32/(s²+7)²,
    DeltaE_O >= (1/sqrt7)(4/7+40/343) >177/686>1/4.

Keep g+g²/2 in -log(1-g). The required integrals are
integral_0^infinity (s²+a²)^-2 ds=pi/(4a³) and
integral_0^infinity (s²+a²)^-4 ds=5pi/(32a^7), obtained by
s=a tan(theta) and the cosine-power recurrence. Finally sqrt7<8/3,
so 1/sqrt7>3/8 and (3/8)(4/7+40/343)=177/686.

For P, (3.1) supplies A0<=17/60; this loose bound is verified from the same
finite return sum. With a0=17/60 define

    P(y)=1/9+(4a0/9+8a0²)y²+(4a0²/9)y^4, w(y)=1-P(y).

On 0<=y<=1, d_P(y)<=P(y)<1. For u=s²>=1/3, monotonicity in A and the
Cauchy-Schwarz bound give d_P<=1-(24-8/u)/(u+7)²<=1. These ranges cover all
s>=0, so every omitted part of the negative logarithm is nonnegative. Retain
12 positive logarithm powers on[0,1] and lower rectangles on[1,20]:

    DeltaE_P >= (7/44) sum_(n=1)^12 (1/n) integral_0^1 w(y)^n dy
      +(7/44) sum_(j=16)^319 (1/16)
            [24-8/(j/16)²]/[((j+1)/16)²+7]² >1/4.       (4.2)

This is a finite rational inequality, since 1/(2pi)>7/44. The rectangle
numerator is evaluated at its increasing left endpoint and the denominator
at its increasing right endpoint. No monotonicity of their ratio is assumed.

Finally, for every finite local CAR polynomial O,

    <O Omega_L,D_(A,L) O Omega_L>
       =<O* [H0,O]>_L+<O* B_A O>_L
       >=DeltaE_(A,L)<O*O>_L.

All operators on the right are local, and their Gaussian correlations converge
by bounded AP Riemann sums (the finitely many Dirac nodes have measure zero).
The limiting inequality holds on local polynomial vectors. These form a core:
finite-particle truncations are a core for dGamma(omega), local one-particle
approximations are dense, and the free generator is bounded on each fixed
particle-number sector. B_A is bounded. Closing the form gives D_A>=1/4
in the infinite original-vacuum representation. This route uses neither an
impurity ground vector nor a presumed nonzero overlap of two vacua.

## 5. Ward field and complete covariance table

For w_A=6K^-1d_A, the bounds in section 3 show w_A belongs to l². The real
bounded CAR field W_A=gamma(w_A) has W_A²=||w_A||²I. Cubic magnetic symmetry
(or the radial table below) gives w_A(0)=2, and w_A dot d_A=0. Indeed the six
single-leg sources sum to K e0; applying the Fourier inverse returns e0, and
the six equal center contributions each supply one sixth. Therefore

    [H0,W_A]=3J_A, [W_A,B_A]=2J_A,
    [W_A,D_A]=-J_A, [W_A,R_A]=-R_A J_A R_A,
    v_A=R_A W_A Omega-W_A R_A Omega.                     (5.0)

The inverse commutator is bounded because D_A>=1/4. The last identity keeps
the full square-summable source tail; it does not treat a generalized zero
mode as a vacuum annihilator. The polynomial vectors lie in the required
operator domains: H0 has bounded one-particle frequency and each such vector
has finite particle number, including W_A Omega.

Write O_n Omega=D_A^n Omega, with O_0=I and

    O_(n+1)=[H0,O_n]+B_A O_n.

The W-source obeys the analogous recurrence from initial operator W_A.
The identity [H0,W_A]=3J_A reduces its first free action to a local source.
Higher actions can be represented as one W field times local CAR words
plus local words, using [W_A,B_A]=2J_A. Products with two W fields may use
W_A²=||W_A||²I, but cross contractions with one W must be retained.

Here is the finite covariance table, derived from the actual
bipartite dispersion rather than a fitted Gaussian bank. Set h=1 for this
table, write a=e0, d=d_A, a_j=K^j a, d_j=K^j d and let w denote the REAL
coefficient vector of W (thus w=6K^-1 d and K w=6d). Define

    M_n=E omega^(2n), L_r=E omega^r,
    D_n=2M_n (P), or M_(n+1)/3 (O),
    F_r=2L_r (P), or L_(r+2)/3 (O).

M_0=1. Let <gamma(f)gamma(g)>=f dot g+i kappa(f,g). For i+j=2n,

    a_i dot a_j=(-1)^(i+n) M_n,
    d_i dot d_j=(-1)^(i+n) D_n,
    kappa(a_i,d_j)=(-1)^(i+n+1) L_(2n+1)/3.

For i+j=2n+1,

    a_i dot d_j=(-1)^(i+n+1) M_(n+1)/3,
    kappa(a_i,a_j)=(-1)^(i+n+1) L_(2n+1),
    kappa(d_i,d_j)=(-1)^(i+n+1) F_(2n+1).

The parity-complementary entries vanish; swap Euclidean arguments
symmetrically and kappa arguments antisymmetrically. These formulas use
K*=-K, -K²=omega²I in each doubled cell, and the six equal signed leg
contributions. Perpendicular-neighbor cross entries vanish by cell parity;
the opposite-neighbor difference contributes a radial power shift.

The extra Ward vector has entries

    w dot a_(2n)=2(-1)^n M_n,
    w dot d_(2n+1)=-6(-1)^n D_n,
    kappa(w,a_(2n+1))=-2(-1)^n L_(2n+1),
    kappa(w,d_(2n))=-6(-1)^n F_(2n-1),
    ||w||²=72 E omega^-2 (P), or 12 (O).                  (5.1)

Again the other parities vanish. The only new nonlocal scalar types are
A0=E omega^-2 and C0=E omega^-1, both finite in three dimensions. For
example the first W-source moments reduce to

    m0_W=||w||²,
    m1_W=(L1/3)||w||²+12 F_(-1).                         (5.2)

Equation (5.2) follows directly from H0W Omega=3J Omega,
W B_A W=||w||² B_A+2J W and WJ=-JW. Its positivity is consistent with
D_A>=1/4. It is not obtained by normalizing W Omega to unit norm.

## 6. Separate source trials and the signed nominal

For real quadratics p_A,q_A choose

    xhat_A=-p_A(D_A)Omega, yhat_A=-q_A(D_A)W_A Omega,
    vhat_A=yhat_A-W_A xhat_A.

From[D,W]=J and the original-vacuum identity

    (DJ+JD)Omega=-2gamma(Kd)Omega

one obtains

    vhat=W(p-q)(D)Omega-q1 J Omega+2q2 gamma(Kd)Omega.     (6.1)

To check the vacuum identity, J B=4g, B J=-4g and H0 J Omega=-2gamma(Kd)Omega.
The asserted anticommutator is not a full operator identity on arbitrary
states. The nonlocal W(p-q) term in(6.1) is essential when the two polynomials
differ; it is retained in every contraction and source norm.

For two channels let n=|A intersect C| and let m count opposite leg matches.
Radial translation and coordinate-parity symmetry give

    d_A dot f(-K²)d_C=(n-m) E f(X)+(m/6) E[X f(X)].

Same-leg entries contribute E f(X), perpendicular entries vanish, and an
opposite leg contributes-E[cos(2k_a)f(X)]=E[Xf(X)]/6-Ef(X). It follows that

    w_A dot w_C=36[(n-m)A0+m/6],
    kappa(w_A,d_C)=-6[(n-m)C0+m L1/6],
    w_A dot Kd_C=-6n, kappa(w_A,Kd_C)=0,
    w_A dot e0=2, kappa(w_A,K e0)=-2L1,
    kappa(w_A,w_C)=0.

The other parities vanish. Self pairs have n=2 and m=0(P) or 2(O). Together
with section 5 these formulas fix all contractions on the eight fields
w_A,w_C,e0,K e0,d_A,Kd_A,d_C,Kd_C. Wick's rule then determines the complete
signed nominal N=Re[<xhat,T xhat>-<xhat,Tg vhat>] and the two trial norms.

The five ordered disjoint classes (A,C,m) have multiplicities
(O,O,0):6, (O,P,0):12, (P,O,0):12, (P,P,2):12, (P,P,1):48.
The [trial polynomial table](../.claude/science/physics-loops/native-positive-ward-scalar-20260913/TRIAL_FORMULAS.json)
contains each class kernel, both trial norms and their fully summed nominal.
Its p,r denote outer P,O coefficients and q,u denote Ward-source P,O
coefficients. The algebra runner re-derives each entry and checks the complete
sum. The native covariance checker contracts every actual ordered pair using
a separate implementation. No individual-class positivity is presumed.

## 7. Rational error certificate and positive sign

For either source psi=Omega or W_A Omega let r=(I-Dp(D))psi, replacing p by
q for the Ward source. Spectral calculus gives

    ||D^-1 r||²<=<r,Q(D)r>

whenever Q(x)>=x^-2 on[1/4,infinity). Use the same explicit quartic for all
four source errors:

    x²Q(x)-1=(x-1/4)(x-4)²(x-8)²(19x+4)/1024.           (7.1)

The right side is nonnegative on the required interval. The numerator is
divisible by x², so Q is genuinely a polynomial of degree 4. A quadratic trial
therefore requires moments only through 10. Convolving(1,-p0,-p1,-p2) with
itself and with Q gives the squared-error bound directly from the displayed
moment formulas, with the whole coefficient of A0 and C0 collected before
interval substitution. The Ward source is not divided by its norm.

Fix these rational coefficients. They were rounded once to three decimals
from earlier trial choices before this elementary evaluation; neither their
optimality nor an old numerical scalar is a premise of the certificate.

| Class | p0 | p1 | p2 | q0 | q1 | q2 |
|---|---:|---:|---:|---:|---:|---:|
| P |3091/1000|-663/500|3/20|1973/1000|-487/500|1/8|
| O |707/250|-559/500|117/1000|1719/1000|-97/125|19/200|

Let E_A and Y_A be the respective certified inverse-error bounds. By(5.0),

    ||v_A-vhat_A||<=Y_A+||W_A||E_A,
    E²=12 E_P²+3 E_O²,
    F²=12(Y_P+||W_P||E_P)²+3(Y_O+||W_O||E_O)².

If a>=||xhat|| and b>=||vhat||, expanding the direct and mixed terms of (1.1)
and using||T||=6 gives

    |8alpha-N|<=6[E(2a+E+b+F)+aF].                       (7.2)

Both the E² and EF contributions remain. The standard-library rational
runner computes the moments, all four source errors, trial norms and complete
nominal using only the elementary scalar intervals. It verifies

    a<1871/200, b<2724/125,
    E<1473/1000, F<1761/125,
    1345<N<1347.

With these coarse bounds the right side of(7.2) is exactly 1286.244234<1287.
It follows that 7<alpha<330 at h=1. In general D=h D1, R=h^-1 R1,
J=h J1 and W is dimensionless; hence alpha=h^-2 alpha1 and

    7 < h²alpha < 330.                                  (7.3)

The sharper author enclosure is approximately[7.40692207,329.05339815].
Equation(7.3) is the primary claim. The [frozen witness](../.claude/science/physics-loops/native-positive-ward-scalar-20260913/WITNESS.json)
contains only the displayed rational choices. The [moment table](../.claude/science/physics-loops/native-positive-ward-scalar-20260913/MOMENT_FORMULAS.json)
is a finite mathematical expression table, re-derived from the Clifford
recurrence during verification. A positive nominal alone would not prove(7.3).

## 8. Verification and review record

The primary runner directly imports all three helpers. Its declared input
closure includes the source note, the formula tables, witness and helpers.
The arithmetic path uses standard-library rational arithmetic; the algebra
path independently regenerates the symbolic coefficient tables. The native
path constructs actual finite AP covariance and Fock objects to challenge
the identities, including source normalization and the retained W(p-q) term.
The L16 Fock calculation uses the 13-mode span of the actual positive-frequency
source vectors. That span contains all field derivatives required before the
fifth D action, so its moment comparisons do not truncate those finite tests.

Eight actual source mutations were also executed and rejected: return-count
normalization, radial frequency powers, the free Ward commutator, the W(p-q)
term, the positive gap tail, the native Fock defect, the trace-energy factor
and interval cross products. Raw mutant sources and outputs are preserved in
the [mutation record](../.claude/science/physics-loops/native-positive-ward-scalar-20260913/mutations/RESULTS.json).

These are different implementations by the same author. They are not an
independent source-review or audit verdict. The finite checks do not prove
the infinite gap by extrapolation: its determinant, domination and form-core
arguments are the analytical proof in section 4. Mechanical source/cache
validation likewise grants no retained status.

Discovery provenance is recorded in the [source manifest](../.claude/science/physics-loops/native-positive-ward-scalar-20260913/SOURCE_MANIFEST.json).
The complete first common-polynomial failures, later separate-source result,
refused fixtures and conditioning corrections are preserved on campaign
branch `physics-loop/toe-local-formation-20260912` at `a23c4a74f2` and its
ancestors. The earlier stronger numerical interval used inherited scalar
certificates. This unit replaces that numerical dependency with section 3;
those old numerical files are not read by the public proof runner.

The named downstream consumer is
`native_infinite_star_node_reduction_note_2026-09-09`. It is a separately
conditional interpretation source, not an upstream premise of this scalar
theorem. The native object and physical motivation were studied in revisions
`a814da6cc1178ac015914c9088fc04b2e635963e` (third-order star),
`64c1efc6984b16cf95c61e7ac148add85d741606` (infinite node reduction) and
`4f0964492f54b5160b79ff39b60c4b8a4a77f09b` (bounded Ward field). These are
provenance and separately conditional interpretation sources, not inherited
numerical premises. If the separately reviewed Dirac-node reduction identifies
its node coefficient with (1.1), this sign certificate excludes its zero case.
Any complete-sixth infrared consequence additionally needs its full
coefficient decomposition, and an interacting phase requires further control.

Independent review of the final source, the combined current-main integration
pipeline, strict lint and changed-evidence gates remain hard conditions before
landing. The author proposes this bounded theorem and does not land it or
write audit-owned verdict/status fields. No editable prompt, axiom or primitive
is changed by this unit.
