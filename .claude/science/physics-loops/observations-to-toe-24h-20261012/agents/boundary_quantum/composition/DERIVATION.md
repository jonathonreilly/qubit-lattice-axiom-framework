# Pair law: directional composition and a visibility-tolerant finite test

Exploratory mathematics for a setting-conditioned pair model. This document
does not adopt a premise, change audit status, or claim a unified theory.
Parameters and tests were frozen in `PRECOMPUTE_FREEZE.json`; the later
visibility extension was frozen separately before its numerical evaluation.

## Model and the additional realization being tested

The parent packet defines a uniform unit-vector reference measure with binary
responses A=sgn(a·λ), B=−sgn(b·λ), conditioned by exp[−k(a·b)AB]. It gives

\[
 E_k(a,b)=-f_k(a\cdot b),\qquad
 f_k(c)=\tanh\left[\operatorname{atanh}\left(\frac2\pi\arcsin c\right)+kc\right],
 \quad k\ge0,
\]

with endpoints f_k(±1)=±1. Its one-pair probabilities are
p(A,B|a,b)=[1+AB E_k(a,b)]/4 and have fair, setting-independent marginals.
The setting-conditioned reference measure is explicit; measurement
independence is not a premise. Pairwise no-signaling alone does not supply
one state and one family of composable measurement operators.

Suppose, additionally, that all these correlators have a common projective
Hilbert realization: Hermitian involutions A_a and B_b, commuting between
parties, and one normalized vector ψ. Purification covers mixed states.
Exact anticorrelation gives

\[
 \|(A_a+B_a)\psi\|^2=2+2E(a,a)=0.
\]

Thus B_aψ=−A_aψ. With v_a=A_aψ,

\[
 f_k(a\cdot b)=\operatorname{Re}\langle v_a,v_b\rangle,\qquad \|v_a\|=1.
\]

Every finite directional matrix G_ij=f_k(a_i·a_j) must therefore be PSD.
This is a necessary consequence of that realization. Failure does not rule
out every ontology or invalidate the normalized pair probabilities. Neither
PSD on a finite list nor PSD as an abstract kernel identifies actual spin
observables, physical dynamics, or a fixed-dimensional laboratory system.

For a continuous isotropic S² kernel, the standard Schoenberg criterion
requires nonnegative Legendre coefficients

\[
 a_\ell(k)=\frac{2\ell+1}{2}\int_{-1}^1f_k(c)P_\ell(c)\,dc.
\]

It is also sufficient for an abstract PSD isotropic kernel when the usual
convergent expansion conditions hold. Here f is odd, so all even coefficients
vanish. The accessible primary source used for this imported fact is
[Berg–Porcu, v2, Theorem 2.1 and Eq. (18)](https://arxiv.org/pdf/1505.05682v2),
which states Schoenberg's theorem and identifies the S² polynomials as
Legendre polynomials. The original 1942 full text was not retrieved.

## Exact three-direction witness and complete probability table

Fix oriented unit directions

\[
 a_1=(1,0,0),\quad a_2=(-1/2,\sqrt3/2,0),\quad
 a_3=(-1/2,-\sqrt3/2,0).
\]

Every distinct pair has dot product −1/2. Write

\[
 h=f_k(1/2)=\tanh[\operatorname{atanh}(1/3)+k/2].
\]

Then G=(1+h)I−hJ, with J the all-ones 3×3 matrix. Its eigenvalues are
1+h, 1+h, 1−2h. The exact normalized witness is w=(1,1,1)/√3:

\[
 w^T G w=1-2h<0\quad\Longleftrightarrow\quad
 k>2[\operatorname{atanh}(1/2)-\operatorname{atanh}(1/3)]
 =\log(3/2).
\]

At k=0.4696142810683679, h=0.523668249295541176… and the negative
eigenvalue is −0.047336498591082352…. This statement uses the frozen finite
decimal k. If k is instead defined by exact 45° quantum calibration, its
value differs by less than 10⁻¹⁶ and the witness has the same strict sign.

The nine setting pairs all have valid distributions. For i=j, E_ij=−1,
so p(++ )=p(−−)=0 and p(+−)=p(−+)=1/2. For i≠j, E_ij=h, so
p(++ )=p(−−)=(1+h)/4 and p(+−)=p(−+)=(1−h)/4. At the prospective k,
these off-diagonal probabilities are 0.380917062323885294… and
0.119082937676114706…. The same formula completely specifies all nine
tables, including both outcome labels, without a fitted angle or visibility.

The regular tetrahedron gives another exact witness: its four off-diagonal
dots are −1/3 and the uniform eigenvalue is 1−3f_k(1/3). Its threshold is
k=3[atanh(1/3)−atanh((2/π)asin(1/3))]≈0.3802595033613354.
The equilateral triple is retained for the simple noise-tolerant test below;
it is not claimed to be the most sensitive possible finite geometry.

## Legendre obstruction and explicit numerical-error treatment

The ℓ=3 coefficient is strictly decreasing for all k≥0. Indeed,

\[
 a_3'(k)=7\int_0^1 r(c)w(c)\,dc,\quad
 r(c)=cP_3(c),\quad w(c)=1-f_k(c)^2.
\]

The function r is negative below c*=√(3/5), positive above it, and
∫₀¹r(c)dc=0. Since f_k is strictly increasing and nonnegative on [0,1], w
is strictly decreasing. Subtracting w(c*) inside the integral makes the
integrand strictly negative away from the zeroes. Therefore a₃′<0.
Integration by parts gives a₃(0)=7/64; dominated convergence gives
lim_{k→∞} a₃(k)=−7/8. There is exactly one zero k₃, defined by the integral,
numerically k₃≈0.3183313595412345. The displayed digits are a numerical
location, not a formal root enclosure. For every k>k₃ the S² PSD condition
fails, including some k for which the three-direction witness is positive.

For independent numerical checking, write θ=acos(c), g(θ)=f_k(cos θ).
Then a₃=7∫₀^{π/2}g(θ)P₃(cos θ)sin θ dθ. On this interval,
|g′|≤2/π+k, |P₃|≤1 and |P₃′|≤6, hence the derivative of this integrand
before the factor 7 is bounded by 2/π+k+7. A composite midpoint rule with
N panels has absolute error at most

\[
 \frac{7(2/\pi+k+7)(\pi/2)^2}{4N}.
\]

The script evaluates the sum using `mpmath.iv` at 35 decimal digits, adds
this analytic error, and expands converted binary64 endpoints outward.
The interval backend is not formally verified. At the prospective k,
N=4096 gives [−0.0618399857555876,−0.0447490048281473], well separated
from zero. Independent 80-digit integration gives a₃=−0.0532945381868694.
256/512/1024-node Gauss–Legendre integration after the θ substitution agrees
for every odd coefficient through ℓ=31; the maximum 512-to-1024 change over
the frozen k cases is 5.5×10⁻¹⁴. Agreement alone is not a proof of the sign
of an arbitrarily small coefficient. No positive-k PSD conclusion is made
from finitely many positive coefficients or finite numerical matrices.

At k=0 the baseline is rigorously PSD: f₀(a·b) is the L² inner product of
the two sign functions sgn(a·λ), sgn(b·λ) under the uniform reference
measure. Numerical polygon eigenvalues around −2×10⁻¹⁵ at k=0 are
roundoff, not a violation. The widened post-test sensitivity interval's
segment below k₃ is left unresolved for full S² PSD.

## Global CHSH optimum, including angles beyond π/2

Set a=2/π, u=1−aθ and
g(θ)=tanh[atanh(u)+k cos θ] for 0≤θ≤π/2. It decreases, obeys g≥u≥0,
and is concave. On the open interval, direct differentiation gives

\[
 \frac{g''}{1-g^2}=
 \frac{2a^2(u-g)}{(1-u^2)^2}
 -\frac{4gak\sin\theta}{1-u^2}
 -2gk^2\sin^2\theta-k\cos\theta\le0.
\]

Continuity extends concavity to the endpoints. The full-angle extension
decreases on [0,π] and satisfies g(π−θ)=−g(θ).

For arbitrary four unit settings, consider the geodesic path
a₁→b₀→a₀→b₁→−a₁. Its four lengths t_i lie in [0,π] and sum to at least
π by the spherical triangle inequality. The CHSH expression
f(a₀·b₀)+f(a₁·b₀)+f(a₀·b₁)−f(a₁·b₁) equals Σ_i g(t_i). Since g
decreases, reducing lengths to a total π can only increase this sum; the
reduced lengths need not correspond to realizable settings for an upper
bound.

If all reduced lengths are ≤π/2, concavity gives Σg(t_i)≤4g(π/4). Otherwise
exactly one length z exceeds π/2. The other three sum to π−z=3α with
0≤α<π/6. Concavity for those three and odd reflection give

\[
 \sum_i g(t_i)\le3g(\alpha)-g(3\alpha).
\]

Its derivative with respect to α is 3[g′(α)−g′(3α)]≥0, again by
concavity. It is therefore at most 3g(π/6). Finally,
π/4=(3/4)(π/6)+(1/4)(π/2) and g(π/2)=0 imply
3g(π/6)≤4g(π/4). This covers the negative fourth-term cases as well as the
first quadrant.

Coplanar settings a₀=0°, a₁=90°, b₀=45°, b₁=−45° attain equality.
Reversing both Alice settings reverses the expression because f is odd.
Thus the global absolute optimum for every k≥0 is exactly

\[
 S_{\max}(k)=4f_k(1/\sqrt2)
 =4\tanh[\operatorname{atanh}(1/2)+k/\sqrt2].
\]

The exact prospective calibration
k*=√2[atanh(1/√2)−atanh(1/2)]≈0.4696142810683678 gives Smax=2√2.
The negative three-direction Gram witness therefore survives even when
every CHSH test of this unattenuated family respects the quantum CHSH
bound. General five-parameter numerical optimizations independently
approach the analytic maximum within 5.7×10⁻¹¹ for all frozen k cases;
those optimizations are checks, not the global proof.

## Common visibility: an actual finite bipartite quantum criterion

The separately declared observation map is C=−VG, 0≤V≤1. It has
diagonal correlations −V and off-diagonal correlations Vh. This is a
common contrast model, not a value fitted after the test. When V<1,
exact anticorrelation is absent and the previous same-vector Gram
argument cannot be imposed on G.

Instead define γ₂(M) as the infimum of max_i||x_i|| max_j||y_j|| over real
factorizations M_ij=x_i·y_j. For a 3×3 quantum correlator table, unit
correlation vectors are necessary. This standard characterization appears
in [Cirel'son/Tsirelson (1980), Theorem 1, pp. 93–94](https://ma.huji.ac.il/~ohadfeld/Tsirelson/download/qbell80.pdf).
The relevant pages were read from the pinned original PDF. Sufficiency for
this particular table is constructed explicitly below, rather than assumed
from a finite Gram condition.

For any factorization M=XYᵀ,
||M||_*≤||X||_F||Y||_F≤3 max_i||x_i|| max_j||y_j||. The first inequality
follows by the orthogonal dual representation of the nuclear norm and
Frobenius Cauchy–Schwarz. Thus γ₂(M)≥||M||_*/3.

For h>1/2, put P=J/3. Then

\[
 G=(1+h)(I-P)+(1-2h)P,\qquad
 |G|=(1+h)(I-P)+(2h-1)P,
\]
\[
 S=\operatorname{sign}(G)=I-2P,\quad S^TS=I,\qquad
 t=|G|_{ii}=\frac{1+4h}{3}.
\]

Let L=|G|^{1/2}, X=L and Y=SL. Then XYᵀ=G and every row of both
factors has squared norm t. This attains the nuclear lower bound exactly:

\[
 \gamma_2(G)=t,\qquad
 C=-VG\text{ is quantum-feasible on these nine setting pairs}
 \Longleftrightarrow V\le V_{\rm crit}=\frac3{1+4h}.
\]

For h≤1/2, G is PSD with unit diagonal, so γ₂(G)=1 and all 0≤V≤1 pass
this finite criterion. In general Vcrit=1/max[1,(1+4h)/3]. These are finite
table claims; feasibility here does not establish a realization of the
candidate on every direction or sequential/multipartite experiments.

Here is a physical operator construction for the finite table whenever
Vt≤1. Take r=√(1−Vt) and five-dimensional unit vectors

\[
 x_i=(\sqrt V L_{i\cdot},r,0),\quad
 y_j=(\sqrt V (SL)_{j\cdot},0,r).
\]

Then x_i·y_j=VG_ij. For h≤1/2 use S=I, L=G^{1/2}, t=1.
Choose the five anticommuting Hermitian 4×4 matrices

\[
 \Gamma=(\sigma_x\otimes I,\sigma_y\otimes I,
 \sigma_z\otimes\sigma_x,\sigma_z\otimes\sigma_y,
 \sigma_z\otimes\sigma_z).
\]

On the maximally entangled state |Φ₄⟩=(1/2)Σ_{r=1}⁴|r,r⟩ set
A_i=x_i·Γ and B_j=−(y_j·Γ)ᵀ. Their squares are I, individual expectations
are zero, and ⟨A_i⊗B_j⟩=Tr(A_i B_jᵀ)/4=−x_i·y_j=−VG_ij. Thus all
fair-marginal joint probabilities are realized. The script constructs
these actual matrices and verifies the square, trace and correlation
identities. Its largest binary64 residual in the frozen feasible cases is
4.45×10⁻¹⁶. Local dimension four is a sufficient construction, not a
minimality claim or a claim that the experimental spin itself has that
dimension.

## Directly measurable nine-setting inequality

With the fixed coefficient matrix S=I−2J/3, define

\[
 \mathcal B(C)=-\sum_{ij}S_{ij}C_{ij}
 =-\frac13\sum_i C_{ii}+\frac23\sum_{i\ne j}C_{ij}.
\]

For any quantum correlation vectors, |B|≤||X||_F||SY||_F≤3 because S
is orthogonal. This uses neither exact anticorrelation, fair marginals,
the candidate model, nor a visibility estimate. It applies to binary
bounded observables in the stated bipartite quantum setting. Its local
deterministic bound is also 3: maximizing over one party's signs gives
Σ_i|(Sb)_i|, which is 3 for three equal signs and 7/3 for a two-plus-one
pattern. Enumeration of all 64 sign assignments verifies this.

The candidate predicts B=V(1+4h). It violates the quantum bound exactly
when V>Vcrit in the h>1/2 branch. The complete candidate probabilities are

\[
 E_{ii}=-V,\quad E_{i\ne j}=Vh,\qquad
 p_{ij}(A,B)=\frac{1+AB E_{ij}}4.
\]

Record all four joint outcomes for each randomized setting pair, with a
declared treatment of every heralded trial. The spin directions are the
three fixed oriented directions above. For linear polarization with the
usual Bloch-angle doubling, one implementation has analyzer angles
0°,60°,120°; that instrument identification and its readout calibration
must be established experimentally. No normalization of selected
coincidence counts is silently treated as an event-ready binary trial.

The candidate comparison can calibrate V on separate endpoint data before
testing the nine tables. Application of the inequality directly to the
measured correlators does not require estimating V. It is a test of the
finite common quantum model against the stated setting-conditioned pair
law, not an experimental exclusion made by this theoretical packet.

## Counting forecast and calibration sensitivity

For independent binary trials with n per setting, the sampling variance is

\[
 \operatorname{Var}(\widehat{\mathcal B})
 =\frac{(1-V^2)+8(1-V^2h^2)}{3n}.
\]

For a total N, optimal fixed allocation in the known candidate model gives

\[
 \operatorname{Var}_{\min}(\widehat{\mathcal B})
 =\frac{[\sqrt{1-V^2}+4\sqrt{1-V^2h^2}]^2}{N}.
\]

These follow by summing independent cell variances and minimizing
Σw_ij²(1−E_ij²)/n_ij at fixed Σn_ij=N. For V=1, the ideal diagonal
variance is zero; a real test still needs finite endpoint verification and
systematic control, so the algebraic allocation is a limiting forecast.
Solving margin/SE=5 is an illustrative precision target, not a test power
calculation or an observed significance. It omits calibration data,
drift, angle errors, loss and allocation uncertainty.

At the prospective k, V=0.97 gives B−3=0.00183280727 and requires about
1.013×10⁸ optimally allocated pairs under those idealized assumptions.
At V=0.99, B−3=0.06372626721 and the analogous number is 7.809×10⁴.
Prediction uncertainty from independent visibility uncertainty is
σ_B=(1+4h)σ_V; at V=0.97 a σ_V of 0.00059225 alone equals the entire
margin. If every measured correlator has an unknown systematic error
bounded by ε, then |δB|≤5ε exactly. The small 0.97-visibility margin
therefore demands errors far below ε=0.00036656. There is no fitted
visibility or angle adjustment after inspecting these tests.

## Source and claim scope

The mathematical inputs about spherical kernels, correlation vectors,
Clifford realizations and the quantum CHSH bound are established results,
not novelty claims. The independent work here applies them to the frozen
one-parameter conditioned pair law, derives its global CHSH maximum, and
retains a simple finite discriminator with an explicit visibility map.
The current-main/open-PR scope snapshot is `SCOPE_SNAPSHOT.json`; main
already contains CHSH and tensor-carrier analyses. Source versions, bytes
and retrieval roles are recorded in `SOURCE_MANIFEST.json`.

This finite Hilbert construction below threshold supplies a mathematical
composition for nine settings. It does not supply the alternative model's
microscopic boundary dynamics, measurement-setting causal mechanism,
sequential state update, multipartite composition, source interactions,
or connection to gravitation. Those remain additional scientific work.
