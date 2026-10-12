# Sphere quantum visibility and a degree-three correlation test

Date: 2026-10-12.
Claim type: bounded_theorem
Status: conditional-support
Audit authority remains the independent audit lane.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: supply and test an apparatus map for the proposed correlation statistic
conditional_surface_status: measurable normal separable tensor quantum model and specified candidate law
hypothetical_axiom_status: candidate angular law explored without adopting a framework premise
admitted_observation_status: no measured data or visibility fitted in this result
claim_type_reason: harmonic realization criterion and a certified prospective statistic
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Primary runner: [sphere_quantum_visibility_reflection_2026_10_12.py](../scripts/sphere_quantum_visibility_reflection_2026_10_12.py).
Its [canonical cache](../logs/runner-cache/sphere_quantum_visibility_reflection_2026_10_12.txt)
records actual execution and source identities. The complete mathematics
needed by the runner is given here; it imports no other repository runner.

## Target, premises and observation-first role

**Target.** For a real continuous isotropic function on the sphere, characterize
its realization as a common-visibility binary quantum correlation, and
construct a bounded statistic with a certified expectation for a specified
alternative angular law.

The observed success of quantum correlations motivates reconstructing the
whole setting family rather than matching a few angles. This note supplies
a mathematical test and a possible measurement design. It does not evaluate
experimental counts, adopt the alternative law, or identify a microscopic
theory of everything. No novelty priority is asserted.

| Supplied item | Provenance and role | Physical question left open |
|---|---|---|
| One normal state on separable tensor Hilbert spaces; measurable local binary observables | Explicit ordinary quantum comparison model | Application to a particular source and readout |
| Sphere of settings with normalized area measure; isotropic target kernel | Mathematical domain; isotropy is needed only for the realization criterion and candidate evaluation | Calibration of actual directions |
| The angular law below, its exact parameter, and visibilities 0.9, 0.95, 1 | Mathematical candidate choices fixed before its certificate; no data fit | Whether a physical preparation realizes this law |
| Fresh joint settings independent of the source conditionally on the past; one local observable map across sampling branches | Explicit premises of the trial bound | Randomness, leakage, detection and trial inclusion |
| Conditional alternative mean on every trial | Additional premise for the alternative error guarantee | Stability of an actual preparation |
| Harmonics, Hilbert-Schmidt inequalities, Clifford matrices, Taylor and Hoeffding bounds | Mathematical tools; needed normalizations and constructions are supplied below | No new physical premise follows from these tools |

No registered framework axiom or primitive is used as a mathematical premise.
The dependency chain is quantum vector factorization -> trace norm and harmonic
spectrum -> necessity; signed Clifford sectors -> sufficiency. Independently,
vector factorization -> harmonic reflection -> bounded statistic; analytic
derivative bounds -> rational quadrature certificate -> candidate expectation;
coefficient sampling -> conditional concentration. The mathematical steps are
proved below. The strongest missing downstream obligation is an apparatus
model that justifies the same observables and the conditional trial premises.
It is separate from the mathematical theorem, not a terminal lemma used in it.

## 1. Exact common-visibility criterion

Let f be real and continuous on [-1,1], with Legendre coefficients

\[
a_l={2l+1\over2}\int_{-1}^1 f(c)P_l(c)\,dc.
\]

For 0<V<=1, one normal state and measurable projective binary local
observables on separable tensor Hilbert spaces, with fair local marginals and
correlation C(a,b)=-V f(a dot b) for every a,b in S2, exist **if and only if**

\[
V\sum_{l=0}^{\infty}|a_l|\le1. \tag{1}
\]

The sum may be infinite. At V=0 an uncorrelated fair construction always
exists. Countably infinite local dimension is allowed; finite energy or
finite entanglement is not promised.

### Necessity

Purify a normal state using a separable ancilla and write
u(a)=(A(a) tensor I)psi, v(b)=(I tensor B(b))psi. In the realification of
the Hilbert space, C(a,b)=u(a) dot v(b) and both norms are one. Binary POVM
contractions give the same argument with norms at most one. Weak operator
measurability gives strong vector measurability in this separable setting.

For normalized area mu, the integral maps U h=integral u(a)h(a)dmu(a) and
W h=integral v(b)h(b)dmu(b) are Hilbert-Schmidt with squared norms at most
one. Expanding in a countable orthonormal basis of the vector space, scalar
Parseval and Tonelli give ||U||_2^2=integral||u||^2. Thus the correlation
operator T=U*W is trace class and ||T||_1<=||U||_2||W||_2<=1.

With normalized sphere measure the addition theorem gives the eigenvalue
-V a_l/(2l+1), repeated 2l+1 times. Its trace norm is the left side of (1).
Summability is therefore a consequence of realization, not an assumption in
this direction. Fair marginals were unnecessary for the bound.

### Sufficiency

If (1) holds, absolute summability and |P_l|<=1 give uniform convergence of
the Legendre series. Completeness in L2 and continuity identify its sum with
f everywhere. A real normalized harmonic feature w_l(a) has unit norm and
inner product P_l(a dot b).

For l>=1, use 2l+1 traceless Hermitian Clifford generators in dimension
d_l=2^l. Explicitly, for j=1,...,l they are
Z^(tensor(j-1)) tensor X tensor I^(tensor(l-j)),
Z^(tensor(j-1)) tensor Y tensor I^(tensor(l-j)), and Z^(tensor l).
Their anticommutation makes w_l(a) dot Gamma a binary projective observable.
On a maximally entangled sector choose

\[
A_l(a)=w_l(a)\cdot\Gamma,
\qquad B_l(b)=-\operatorname{sign}(a_l)[w_l(b)\cdot\Gamma]^T.
\]

The identity <Phi_d|A tensor B|Phi_d>=Tr(AB^T)/d yields correlation
-sign(a_l)P_l and zero marginals. For l=0 use a two-dimensional Pauli-Z
sector with this sign rule; a one-dimensional observable would not be fair.

Give sector l probability V|a_l|. Assign the remainder 1-V sum|a_l| to a
separate product state |+x> tensor |+x> measured by Z on each side. On
countable local direct sums, the superposition of matching sector states
with the square roots of these probabilities is normalized. Block-diagonal
observables eliminate cross-sector terms. This is one normal vector state
and one setting family for the whole sphere. Strong continuity follows by
finite-block continuity and a uniformly bounded squared tail.

If f(1)=1 and the absolute sum is finite, then
sum|a_l|=1+2 sum_(a_l<0)|a_l|. Its reciprocal is the criterion's critical
visibility. Evaluating that reciprocal requires control of the full absolute
tail; the candidate evaluation below uses only a_3.

These vector and Clifford ingredients are standard; the primary background
is [Tsirelson, Quantum analogues of the Bell inequalities](https://www.mathnet.ru/eng/znsl4332).
The full argument and the infinite-dimensional construction needed here are
given above rather than imported from a citation.

## 2. A reflection statistic

For any common quantum correlation C, with no isotropy or fairness premise,
let Pi_3 be the orthogonal projection onto degree-three spherical harmonics.
Its kernel is 7 P_3(a dot b), where P_3(c)=(5c^3-3c)/2. The operator
S=I-2 Pi_3 is an isometry on vector-valued L2(mu). Hence

\[
\begin{split}
B(C)&=-\int C(a,a)d\mu(a)
 +14\iint P_3(a\cdot b)C(a,b)d\mu(a)d\mu(b),\\
|B(C)|&=|\langle u,Sv\rangle|\le1. \tag{2}
\end{split}
\]

The diagonal term is the actual common-setting measurement. It is not an
assertion that an arbitrary product-L2 kernel has a trace given by its
diagonal. The vector maps supply its bounded measurable diagonal directly.
For an isotropic candidate, B(-Vf)=V[f(1)-2a_3]; setting f(1)=1 gives
V(1-2a_3). This expectation needs no absolute-tail premise.

Controls distinguish the diagonal: the cosine has B=V; the normalized
polynomial (1+eta)P_1-eta P_3 gives V(1+2eta), while P_1-eta P_3 gives
V(1+eta). They are distinct test functions.

## 3. Specified candidate and rational certificate

For -1<c<1 define

\[
f_k(c)=\tanh\{\operatorname{atanh}[(2/\pi)\arcsin c]+kc\},\quad
f_k(\pm1)=\pm1,
\qquad
k_* = \sqrt2[\operatorname{atanh}(1/\sqrt2)-\operatorname{atanh}(1/2)]. \tag{3}
\]

This continuous odd bounded candidate was chosen mathematically to give
f_k(1/sqrt2)=1/sqrt2; that equality is calibration to a stipulated angle,
not a successful experimental prediction. The parameter differs from any
prior fit to exposed public fringe data. No such data enters this certificate.

Use theta in [0,pi/2], u=1-2theta/pi, t=tanh(k cos theta), and
g=(u+t)/(1+ut). Oddness and substitution give

\[
a_3(k)=7\int_0^{\pi/2}g(\theta)P_3(\cos\theta)\sin\theta\,d\theta. \tag{4}
\]

On 0<=u,t<=1, direct differentiation gives
g_u=(1-t^2)/(1+ut)^2, g_t=(1-u^2)/(1+ut)^2,
g_uu=-2t(1-t^2)/(1+ut)^3, g_tt=-2u(1-u^2)/(1+ut)^3,
and g_ut=-2(u+t)/(1+ut)^3. Therefore their absolute bounds are 1,1,2,2,4.
For 0<=k<=1/2, |t'|<=k, |t''|<=k+2k^2 and 2/pi<2/3 give
|g'|<=7/6 and |g''|<=91/18.
For H=P_3(cos theta)sin theta, |H|<=1, |H'|<=7, and

\[
H''=P_3''(c)\sin^3\theta-3P_3'(c)\sin\theta\cos\theta-P_3(c)\sin\theta
\]

has absolute bound 25 using |P_3''|<=15, |P_3'|<=6 and
|sin theta cos theta|<=1/2. Thus |(gH)''|<=835/18<48. The denominator
1+ut>=1 also establishes endpoint smoothness in this parametrization.

The 2048-panel composite midpoint error is at most

\[
{7\,48(\pi/2)^3\over24(2048)^2}
 < {7\,48(11/7)^3\over24(2048)^2}
 = {1331\over102760448}. \tag{5}
\]

The runner evaluates all midpoints with outward fixed-point rational
intervals at scale 10^40. Addition is exact at this scale; multiplication
uses four corners with floor/ceiling; division uses four rational corners
and requires a positive denominator. Horner evaluation propagates inclusion.

The pi bracket is Machin's 16 atan(1/5)-4 atan(1/239), bounded by adjacent
alternating partial sums with 50 and 12 terms. The tangent identity and its
angle in (0,pi/2) fix the branch. Integer square root brackets sqrt2.
For 0<=x<1, the 140-term atanh series has nonnegative tail at most
x^281/[281(1-x^2)]. Together these enclose the same exact k_* in (0,1/2).
Sine through degree 25 and cosine through degree 24 use respective
remainders +/-2^27/27! and +/-2^26/26! on [0,2]. Exponential through
degree 24 uses remainder [0,3/25!] on [0,1); e<3 follows from its series.
Every midpoint satisfies the domains. The exact midpoint u cancels pi.
The full rational endpoints appear in the cache; outward decimal summaries are

\[
-0.053307319061055 < a_3(k_*) < -0.053281414152582. \tag{6}
\]

In particular, (2)-(6) give B(-0.95f_k)>1.0512346868899072. At visibility
0.9 the certified interval is below 1; this alone gives no full-realization
conclusion. A separate high-precision quadrature is only a numerical control.
The continuum certificate does not certify an arbitrary rounded finite
implementation or an actual apparatus.

## 4. Prospective trial sampling and conditional error bounds

The primitive 5c^4/8-3c^2/4 at the roots 0 and +/-sqrt(3/5) gives
integral_-1^1 |P_3(c)|dc=13/20. The total absolute weight in (2) is
J=1+14(13/40)=111/20. For every included heralded trial choose:

1. With probability 20/111, uniform a and b=a, recording Z=-J AB.
2. With probability 91/111, uniform a, relative c of density
   (20/13)|P_3(c)| and uniform relative azimuth, recording
   Z=J sign(P_3(c))AB.

Direct substitution gives E Z=B and |Z|<=J. Each local marginal of the
settings is uniform in each branch. The source is independent of the fresh
**joint** setting choice conditionally on past trials. Both branches use
the same local map for a given direction; no branch flag may let the devices
retune it. Correlation between the two settings is intentional. Zero-density
roots may receive either sign. Selecting coincidences or allowing setting
leakage would require a new analysis.

Under the quantum comparison model each conditional mean is at most one.
The conditional range has width 2J; Hoeffding's exponential moment bound and
iteration over the past give
Pr(mean Z>=1+epsilon)<=exp[-N epsilon^2/(2J^2)]. Under the alternative
assume E[Z_i|past]>=1+Delta on **each** included trial. An iid stable
candidate is sufficient; an unconditional average alone is not this premise.
The same conditional moment argument supplies the lower-tail bound. With
threshold 1+Delta/2, both errors are at most .01 when

\[
N\ge {8J^2\ln100\over\Delta^2}. \tag{7}
\]

Using the certified lower gap and the exact coarse bound ln100<5 gives
N=469373 at V=.95 and N=108502 at V=1. The latter logarithm bound follows
from the positive partial sum of e^5 through degree 11 exceeding 100.
These are sufficient conservative counts, not a measured power analysis or
an optimized test. Direction uncertainty, finite resolution, source drift,
detection and included-trial definitions remain apparatus inputs.

## Verification and review boundary

Run `python3 scripts/sphere_quantum_visibility_reflection_2026_10_12.py`;
`--json` emits the same deterministic checks as JSON and writes no files.
The runner declares a 120-second timeout and the paired note as an integrity
input. It recomputes (6), checks the signed finite Clifford construction,
the polynomial spectrum and reflection controls, and the sampling constants.
Its rational computation supports (6); finite floating controls supplement
the proofs of (1) and (2) without replacing them.

The direct author's two source arguments and independent checks are preserved
in the originating campaign at commit 28e1edd109c96910227cfcda8c8a3221d0d6ea0d.
This self-contained version carries the corrected conditional-mean premise;
the old whole-sphere parameter classification, resource theorem and finite
300-setting numerical candidate are separate work and are not inputs here.
The final portable source receives its own affected-source independent review.
No formal audit verdict, physical premise adoption, empirical exclusion or
established TOE follows from a runner or reviewer passing these tests.
