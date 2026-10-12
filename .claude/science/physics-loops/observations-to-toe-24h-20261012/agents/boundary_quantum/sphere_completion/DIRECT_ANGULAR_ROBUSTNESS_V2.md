# Direction error and correlation bias for the reflection statistic

Direct parent derivation, October 12, 2026. This is a prospective measurement
design calculation, not an analysis of any apparatus or new data. It uses
the checked reflection statement in DIRECT_REFLECTION_WITNESS_V2.md and
the rational result DIRECT_REFLECTION_RESULT.json. The candidate and
visibility remain unchanged; no tolerance is estimated from measurements.

## Signed-measure stability

For normalized sphere measure mu, the statistic is

    B(C)=-integral C(a,a)dmu(a)
         +14 double_integral P3(a dot b)C(a,b)dmu(a)dmu(b).

Its coefficient measure has total variation

    J=1+14*(1/2)*integral_-1^1 |P3(c)|dc=111/20.

The diagonal measure and area-product measure are mutually singular. Therefore
for any two bounded measurable correlations with uniform difference at most
epsilon, |B(C)-B(D)|<=J epsilon. If their diagonal difference is bounded
by epsilon0 and their product-almost-everywhere difference by epsilon1, the
stronger statement is epsilon0+(91/20)epsilon1. Product-almost-everywhere
control alone cannot replace the separate diagonal bound.

This is the operator norm of the functional on arbitrary bounded measurable
functions: choosing the error sign separately on the diagonal and off it
attains the total-variation bound. No claim of attainability within the
restricted quantum or candidate family is intended.

## Candidate angular modulus

Let F(theta)=f_k(cos theta) on [0,pi], with k=k*>0 from the reflection
certificate. On the first half interval set u=1-2theta/pi,
t=tanh(k cos theta), F=(u+t)/(1+ut). Both partial derivatives F_u,F_t
are nonnegative and at most one, giving

    |dF/dtheta| <= 2/pi+k = L.

Oddness of f means F(pi-theta)=-F(theta), so the same bound holds on the
second half. Continuity at the endpoints and midpoint proves global
Lipschitz continuity. In fact |F'(pi/2)|=2/pi+k, so this is the exact
global Lipschitz constant. This proof does not replace the candidate with
its small-angle or linear approximation.

If actual directions a',b' differ from labels a,b by geodesic angles at
most delta_A,delta_B, the spherical triangle inequality gives

    |distance(a',b')-distance(a,b)| <= delta_A+delta_B.

Consequently the candidate correlation C=-V F(distance) changes pointwise
by at most V L(delta_A+delta_B). Mixtures obey the same bound when the
direction errors obey it almost surely. An additional absolute correlation
error epsilon gives

    |B_actual-B_ideal| <= J [V L(delta_A+delta_B)+epsilon] = b.

The diagonal is included, even though the candidate has an angular cusp
there. Ignoring that term would overstate tolerance. A sharper optional
bound for equal deltas with 2delta<=pi/2 is

    b_angle <= V[1-F(2delta)]+(91/10)V L delta,

because F is decreasing and a',b' are at separation at most 2delta when
their intended labels agree. The accompanying numerical table deliberately
uses the simpler conservative uniform bound, not this optional improvement.

## Why calibration alone need not raise the quantum bound

For deterministic local maps a->a'(a) and b->b'(b), replace the observable
families by A'(a)=A(a'(a)) and B'(b)=B(b'(b)). They are still common binary
quantum maps on the same state, so the ideal label-sampled bound |B|<=1
remains exact, however inaccurate the labels are. Local stochastic setting
maps can likewise be averaged to Hermitian contractions if their classical
kernels depend only on the local label and past, are source-independent
conditionally on the past, and the two arms jitter independently given the
past. The contraction form of the reflection proof then applies on the same
conditional source state. A source-correlated calibration model requires
explicit calibration registers or another appropriate conditional state;
separate averaging on the original state alone is not justified.

The herald and included-trial decision precede the fresh sampling branch
and setting choice. Retention conditional on the fresh settings is not
covered, even without outcome-based selection. The same local map must be
used in both sampling branches. An error rule
depending on the other party's fresh setting, an exposed branch flag, source
selection by settings, or outcome-conditioned trial inclusion is not covered
by this argument. These are substantive apparatus premises. If an additional
systematic error also shifts the quantum statistic, its separately justified
null allowance must be subtracted from the candidate gap as well; it cannot
be charged only to the candidate.

## Fixed illustrative error budget and sample counts

Take the already certified ideal gap Delta0=B_lower(.95)-1 and L_upper
from the exact k and pi intervals. For equal angular bounds delta and an
extra candidate-side error epsilon, use

    Delta_eff = Delta0-J[2 V L_upper delta+epsilon].

Freeze delta in {0,1/2000,1/1000,1/500,1/250} radians and epsilon in
{0,1/1000}. These are stipulated examples, not inferred instrument specs.
For positive Delta_eff the same conservative conditional two-error bound is
N=ceil(40 J^2/Delta_eff^2), threshold 1+Delta_eff/2. The alternative must
satisfy its lower conditional mean on every included trial, and the
comparison's quantum conditional bound must remain at most one. No finite
sample assertion is made for a nonpositive effective gap.

The pure-angle strict-positive threshold is
delta<Delta0/(2JV L_upper). This is a sufficient certified tolerance for the
coarse bound, not an optimized achievable angle or a necessity theorem.
All computations below use Fraction endpoints and preserve nonpositive gaps.
No real experiment, detection model, or actual angular distribution is claimed.

## Source continuity

Version 2 explicitly supplies source-independent local jitter kernels for
separate averaging and requires heralding/inclusion before fresh settings.
These are premise clarifications from independent review; the original
source-bound rational calculation is unchanged and remains preserved.
