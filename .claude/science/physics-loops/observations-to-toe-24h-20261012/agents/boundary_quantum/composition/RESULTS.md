# A finite composition test of the frozen conditioned pair law

The prospective pair law matches the quantum CHSH maximum yet fails a
three-direction quantum composition test. Its failure survives a declared
common visibility V>0.9694077541. Below that threshold the same nine-setting
table has an explicit finite quantum realization. These are mathematical
predictions and compatibility results, not an experimental exclusion.

The candidate is E_k(a,b)=−f_k(a·b), with
f_k(c)=tanh[atanh((2/π)asin(c))+kc]. Its fair-marginal two-outcome tables
are normalized for every pair. The prospective parameter k*=0.4696142810683679
comes from the parent packet's 45° calibration proposal. It is distinct
from the source-curve fit k=0.5337547855623958.

## Exact discriminator and visibility rule

Use the same three oriented directions on both parties:
(1,0,0), (−1/2,√3/2,0), (−1/2,−√3/2,0). Put
h=tanh[atanh(1/3)+k/2] and G=(1+h)I−hJ. The exact-anticorrelation
common Hilbert hypothesis requires G to be PSD, but its uniform-vector
eigenvalue is 1−2h. It is negative precisely when k>ln(3/2).

At prospective k*, h=0.5236682492955412 and λ_min=−0.04733649859108235.
All nine probability tables remain individually valid. The discrepancy is
in their common realization, not their normalization or marginal signaling.

For the separately frozen observation map C=−VG, exact anticorrelation
no longer holds when V<1. An independent factorization and nuclear-norm
argument instead give the exact finite quantum criterion

\[
 \gamma_2(G)=\max\left(1,\frac{1+4h}{3}\right),\qquad
 V\le V_{\rm crit}=\gamma_2(G)^{-1}.
\]

For the branch h>1/2, the directly measurable inequality is

\[
 \mathcal B=-\frac13\sum_iC_{ii}+\frac23\sum_{i\ne j}C_{ij}\le3.
\]

It holds for arbitrary bipartite quantum correlators, without assuming
fair marginals, anticorrelation, the candidate law, or a visibility estimate.
The candidate predicts B=V(1+4h). Its complete observation map is
C_ii=−V, C_ij=Vh for i≠j, with p_ij(A,B)=(1+AB C_ij)/4. This provides a
finite falsifier with fixed geometry and fixed coefficients. The local
classical bound of this particular functional is also 3.

The sufficiency construction below Vcrit is explicit: five-dimensional
unit correlation vectors, five 4×4 Clifford matrices, a maximally entangled
state of local dimension four, and traceless projective binary observables.
This realizes every joint probability in this finite table. It does not
establish a realization of the full angular family or identify a physical
spin dimension. Full proof and matrices are in `DERIVATION.md` and
`COMPUTATION_RESULTS.json`.

## Frozen parameter results

| k | h=f_k(1/2) | Triangle λ_min | Legendre a₃ | Global CHSH maximum | Finite-table Vcrit |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.3333333333 | +0.3333333333 | +0.1093750000 | 2.0000000000 | 1.0000000000 |
| 0.314240396437 | 0.4650171655 | +0.0699656691 | +0.0014415409 | 2.5912210915 | 1.0000000000 |
| 0.469614281068 | 0.5236682493 | −0.0473364986 | −0.0532945382 | 2.8284271247 | 0.9694077541 |
| 0.479986755688 | 0.5274220444 | −0.0548440888 | −0.0569333004 | 2.8430200749 | 0.9647269529 |
| 0.533754785562 | 0.5465517719 | −0.0931035438 | −0.0757291114 | 2.9162585067 | 0.9415583851 |
| 0.591390560864 | 0.5664424207 | −0.1328848414 | −0.0957204843 | 2.9903834801 | 0.9186195878 |
| 0.876449295654 | 0.6554521503 | −0.3109043006 | −0.1908953671 | 3.2958687503 | 0.8283154441 |

The parent source-curve analysis supplied the nominal conditional interval
[0.479986755687848,0.5913905608644301]. Every point in it fails the exact
triangle Gram condition and the unattenuated CHSH quantum bound. It gives
Vcrit between 0.9186195878 and 0.9647269529. That interval is a conditional
profile under the parent fit's error model, not a validated experimental
confidence interval: repeated source settings exposed substantial
stationarity/error-model failures. This packet does not repair those data
or promote the fit into an empirical quantum-theory exclusion.

The wider interval [0.3142403964367766,0.8764492956544335] is explicitly the
parent packet's post-test variance sensitivity, not a newly frozen primary
fit. For full S² PSD, its portion above the unique a₃ zero
k₃≈0.3183313595412345 fails. The small portion at and below that zero is
unresolved by this packet. Positive sampled coefficients or positive finite
matrices there are not proof of an all-direction PSD kernel. The k=0
control is exactly PSD through its classical L² sign-function realization.

## Why CHSH alone misses the prospective candidate

For all k≥0 the global optimum is exactly

\[
 S_{\max}=4\tanh[\operatorname{atanh}(1/2)+k/\sqrt2].
\]

The proof uses concavity on the half-circle, spherical path length, and
explicitly handles paths containing an angle greater than π/2. Standard
coplanar settings attain the bound. At exact k*=√2[atanh(1/√2)−atanh(1/2)],
Smax=2√2, while the triangle test still fails. The displayed frozen decimal
k differs from this exact definition by less than 10⁻¹⁶; its negligible
decimal-rounding excess above 2√2 is not interpreted as a CHSH violation.

For the quantum cosine control, h=1/2, the triangle eigenvalue is zero,
Vcrit=1 and B=3V. For the measurement-independent k=0 control, h=1/3,
the triangle is PSD, Smax=2 and B=(7/3)V. Thus all three laws have distinct
fixed predictions with no added angular fit freedom.

## Practical contrast and precision at prospective k

| Declared common V | Candidate B | B−3 | Illustrative total pairs for margin = 5 counting SE |
|---:|---:|---:|---:|
| 0.90 | 2.7852056975 | −0.2147943025 | No violation of this inequality |
| 0.95 | 2.9399393473 | −0.0600606527 | No violation of this inequality |
| 0.97 | 3.0018328073 | +0.0018328073 | 1.013×10⁸ |
| 0.99 | 3.0637262672 | +0.0637262672 | 7.809×10⁴ |
| 1.00 | 3.0946729972 | +0.0946729972 | 3.239×10⁴, ideal limiting allocation |

These numbers use independent binary trials and allocation optimized for
the fixed candidate probabilities. They are precision forecasts, not
experimental significance, guaranteed power, or complete sample budgets.
They omit independent endpoint calibration, losses, drift and angle errors.
For V=0.97, visibility uncertainty σ_V=0.00059225 alone matches the whole
predicted margin. A uniform unknown error ε in each correlator contributes
at most 5ε to B, so systematic errors must be much smaller than 0.00036656
for that small margin. At V=0.99 the margin is substantially less fragile.

Measure all four outcomes for every randomized setting pair with a
declared rule for every heralded trial. Estimate any candidate visibility
on independent endpoint data before the test; compute the inequality
directly from the test correlators. The quantum bound itself has no
visibility-fitting step. For optical implementation, the identification
of a Bloch direction with twice a linear analyzer angle is an additional
instrument assumption, not supplied by this abstract pair law.

## Verification, exposure and reproducibility

`PRECOMPUTE_FREEZE.json` was recorded at 2026-10-12T18:13:52Z. The
prospective value f_k(1/2) was already exposed in the parent packet, so
this is a model-development composition test, not blind discovery.
`VISIBILITY_EXTENSION_FREEZE.json` at 18:21:45Z records the root-supplied
gamma₂ lead and fixed V cases before their numerical calculation. The
factorization, lower bound and finite operator construction were then
derived independently.

The exact triangle sign follows from k>ln(3/2), independent of numerical
eigensolvers. At prospective k, the independent midpoint enclosure for a₃
is [−0.06183999,−0.04474900], with an analytic quadrature-error allowance
and 35-digit interval arithmetic. The interval package is not formally
verified. 80-digit integration and 256/512/1024-node quadrature agree;
the last two differ by at most 5.5×10⁻¹⁴ across all recorded odd coefficients
through ℓ=31. The a₃-root digits are numerical, while uniqueness and
monotonicity are proved analytically. General CHSH optimizations agree with
the proven bound within 5.7×10⁻¹¹. All finite quantum-construction residuals
are below 4.45×10⁻¹⁶.

The scans include regular great-circle polygons with 3–32 directions,
regular tetrahedron, and Fibonacci spheres of size 12,24,48,96. Their
directions, eigenvectors and minimum eigenvalues are preserved; the exact
three-direction witness remains the primary simple falsifier. Numerical
eigenvalues at the 10⁻¹⁵ scale are treated as roundoff.

Run `python3 composition_check.py` from this directory (or use its absolute
path). It checks the campaign deadline and both canonical stop markers,
limits numerical libraries to one thread, and reproduces the result JSON
and finite directions. Existing freeze files are untouched. Dependencies
and script/input hashes are recorded in the output. The report's prose
proofs and source imports still warrant independent human/mathematical
review; numerical checks do not replace that review.

Primary imported sources are [Berg–Porcu v2, Theorem 2.1](https://arxiv.org/pdf/1505.05682v2)
for the Schoenberg criterion and [Cirel'son/Tsirelson 1980, Theorem 1](https://ma.huji.ac.il/~ohadfeld/Tsirelson/download/qbell80.pdf)
for finite quantum correlation vectors. Their local bytes and roles are
pinned in `SOURCE_MANIFEST.json`. `SCOPE_SNAPSHOT.json` records main
516cb69d8487ff04f8a48e065d3dcbe71d7dd237 and open PR 9499. Standard
Schoenberg, Clifford and CHSH facts are not claimed as new.

The pair model still lacks a microscopic account of its setting-dependent
boundary statistics, sequential state update, multipartite composition
and dynamics. This block supplies a concrete composition constraint and a
finite quantum construction where the noisy table permits one; it does
not close those remaining physical gaps.
