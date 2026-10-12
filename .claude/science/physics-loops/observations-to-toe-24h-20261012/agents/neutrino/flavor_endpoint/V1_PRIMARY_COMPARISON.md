# Independent V1 endpoint-flavor check and pinned primary comparisons

The one-parameter endpoint hypothesis does not reproduce the solar angle,
atmospheric angle or either fixed mass-gap ratio in the pinned fitted summaries.
This is a conditional summary-level failure of this supplied physical
identification. It is not a newly calculated experimental exclusion significance,
a change to the axioms/audit standing, or a blind prediction. Root's numerical
results and code were not consulted before this independent initial result was
frozen at 2026-10-12T18:00:01.945425Z. Public approximate targets were already
known; all source exposure and calibration roles are recorded in the protocols.

The matrix, flavor assignment, normal ordering, standard coherent propagation
and standard matter potential are physical premises. With ordered roots of

\[
P_3(x)=x^3-3(s+2)x^2+3(s+1)(s+2)x-s(s+1)(s+2),
\]

an eigenvector with electron component one is

\[
v(x)=\left(1,{s-x\over\sqrt{s}},
 {x^2-2(s+1)x+s(s+1)\over\sqrt{2s(s+1)}}\right)^T.
\]

Normalize its square norm to get \(U_{ei}^2=w_i\). Then
\(s_{13}^2=w_3\), \(s_{12}^2=w_2/(1-w_3)\), and
\(s_{23}^2=w_3(s-x_3)^2/[s(1-w_3)]\). The standard rephasing-invariant
cosine extracted from \(|U_{\mu1}|^2\) is +1, so this assignment fixes
\(\delta_{CP}=0\), not an unspecified choice between 0 and pi; \(J_{CP}=0\).

Only the Daya Bay fitted amplitude 0.0851±0.0024 selects s. The central result is
s=2.185966563400368, x=(1.040067936665203,3.492775752475005,8.025056001060898).
The electron weights are (0.572990021392132,0.405262004217797,0.021747974390071).
For \(m_i^2=m_0^2+A x_i^p\), A>0, define
\(r_{31}=\Delta m^2_{21}/\Delta m^2_{31}\),
\(r_{32}=\Delta m^2_{21}/\Delta m^2_{32}=r_{31}/(1-r_{31})\).

| V1 output | Central | Daya Bay central ±1.96 quoted errors propagated |
|---|---:|---:|
| s | 2.18596656 | [2.04665556,2.32896730] |
| sin²theta12 | 0.41427157 | [0.40315408,0.42488030] |
| sin²theta23 | 0.34674866 | [0.34186798,0.35149064] |
| r31, p=1 | 0.35113987 | [0.34828874,0.35390449] |
| r31, p=2 | 0.17558085 | [0.17099129,0.18010277] |
| r32, p=1 | 0.54116420 | [0.53442184,0.54775879] |
| r32, p=2 | 0.21297522 | [0.20625995,0.21966506] |

These bands are diagnostic calibrations, not complete confidence intervals for
the conditional model. Across 1001 logarithmically spaced s in [0.01,10], the
calibration amplitude increased monotonically and the recurrence eigenvectors
agreed with `numpy.linalg.eigh` to 9.99e-16. Maximum eigen residual was
8.88e-15. Numerical monotonicity is not a uniqueness proof outside that search.

Primary observations and their conditioning are as follows. Every value below
is a fitted standard-family summary, not a raw observation. The independent
target roles apply to model selection here, not statistical independence of the
underlying published constraints.

| Source and exact version | Quantity and interval definition | Conditioning and access |
|---|---|---|
| [Daya Bay 2211.14988v1](https://arxiv.org/abs/2211.14988v1), calibration | sin²(2theta13)=.0851±.0024 | Standard survival law; sin²theta12=.307±.013 and delta21=(7.53±.18)e-5 eV², paper p5. This imports solar-sector information. No arbitrary-law grid use. |
| [JUNO 2511.14593v1](https://arxiv.org/abs/2511.14593v1), 18 Nov2025; matching [Nature June2026 article](https://doi.org/10.1038/s41586-026-10538-z) | NO sin²theta12=.3092±.0087; delta21=(7.50±.12)e-5 eV². One-dimensional frequentist profile errors from CNP chi². | Earth matter included; detector/background/flux covariance and the Daya Bay 2D theta13–delta31 constraint enter. Daya Bay supplies reference spectra too. Raw detector data/code are not public; publisher Fig4 grid is public. |
| [SK solar 2312.12907v2](https://arxiv.org/abs/2312.12907v2), 20 Feb2024, PRD109092001 | All-solar sin²theta12=.306±.013, delta21=(6.10 +.95/−.81)e-5 eV², SecVII D/Fig47. Excludes KamLAND from this quoted all-solar result. | SK+SNO+Borexino+radiochemical chi²; three-flavor correction to matter survival and reactor sin²theta13=.0218±.0007. The approximation is ordering-insensitive, not a distinct NO likelihood. No final two-parameter covariance matrix was supplied in the inspected summary. |
| [T2K+NOvA 2510.19888v2](https://arxiv.org/abs/2510.19888v2), 24 Oct2025; [Nature Table3](https://www.nature.com/articles/s41586-025-09599-3/tables/3) | NO theta23 highest-posterior points .561 and .470, 68.27% HPD set [.522,.582] union [.462,.486]; delta32=2.43(+.04/−.03)e-3 eV². | Bayesian marginalization conditional on NO; flat deltaCP/sin²theta23/delta32; solar Gaussian priors .307±.013 and (7.53±.18)e-5. Publisher theta13 prior=(2.18±.07)e-2. Posteriors are available on inquiry in the article; no inquiry was made. |
| [NOvA 2509.04361v2](https://arxiv.org/abs/2509.04361v2), 9 Mar2026, TableS1, PRL136011802 | NO **without reactor constraint**: theta23 HPD=.547, 1sigma set [.465,.509] union [.517,.562]; delta32 HPD=2.431e-3, [2.392,2.467]e-3 eV². | Marginalized Bayesian HPD; other oscillation parameters fixed PDG2023. With 1D Daya Bay constraint the theta23 set is [.484,.566], delta32 [2.397,2.467]e-3. [Public data release](https://novaexperiment.fnal.gov/data-releases/) exists; these are separate fit variants, not independent measurements. |
| [T2K 2506.05889v3](https://arxiv.org/abs/2506.05889v3), 30 Dec2025, PRL135261801 | NO theta23=.559(+.018/−.078), delta32=2.506(+.039/−.052)e-3 eV²; frequentist constant-delta-chi² Fig5, delta32 smeared for simulated-data studies. | Reactor prior sin²theta13=(2.20±.07)e-2; Gaussian solar priors as above; matter density2.6g/cm³. [No-reactor MCMC chains](https://doi.org/10.5281/zenodo.17312780) are public. The quoted errors are not Bayesian HPD errors. |

Version traps: the T2K+NOvA arXiv v2 PDF p17 visibly prints ±.007 inside
the theta13 prior parentheses, whereas publisher Methods prints ±.07. The
publisher number is recorded here; no code-level resolution is claimed.
NOvA v1/search snippets reverse the abstract's asymmetric theta23 errors;
v2 and its explicit TableS1 are used. The rounded NOvA abstract also mixes a
theta23 presentation with different inference summaries, so TableS1 governs the
Bayesian comparison. None of the accelerator measurements should be combined
as independent of the joint analysis that includes their earlier data.

The publisher JUNO grid is a 100×100 profile surface over sin²theta12 in
[.26,.36] and delta21 in [6.9,8.1]e-5 eV². Its sampled minimum is .003 above
the continuous minimum. Subtracting that sampled minimum and linearly
interpolating the one-dimensional profiles gives theta12 intervals
[.300459,.317918] at delta-chi²=1, [.292166,.326431] at3.84145882,
and [.283200,.335809] at9. Sample-grid and interpolation errors are not folded
into an experimental likelihood. Independent local quadratic fits with windows
3,5,8 points around the minimum give correlation −.22052 to−.22128. For the
middle window, in coordinate order (delta21/e-5eV², sin²theta12), the approximate
covariance is [[.01368067,−.000225729],[−.000225729,.0000763190]]. This is our
local Gaussian diagnostic derived from the release, not an experiment-published
covariance matrix or a covariance across experiments.

The full V1 theta12 band is above both the JUNO diagnostic delta-chi²=9
profile interval and the release's upper grid boundary. We therefore assign
**no chi² value, sigma separation or exclusion level to V1**. The theta23 band
also misses every listed primary interval, including NOvA with no reactor
constraint. From JUNO delta21 and the joint accelerator delta32 reported
one-error ranges, the endpoint rectangle gives r31 in [.0290117,.0307730]
and r32 in [.0298785,.0317500], far from either fixed-map band. This rectangle
is not a joint confidence region; covariance and shared priors remain uncombined.
The result is a failed forward compatibility screen, without a fitted p or a
silent reassignment of flavors. CP=0 remains within the joint NO three-sigma
deltaCP interval; CP alone is not the decisive failure here.

There is no statistical independence claim between the calibration and targets.
Daya Bay uses solar inputs overlapping the information in solar/global fits.
The SK solar fit uses a reactor theta13 constraint that includes Daya Bay
information. JUNO directly includes the same Daya Bay oscillation constraint and
reference flux. The joint accelerator fit uses a PDG reactor prior containing
earlier Daya Bay information, plus the same solar priors. The latest NOvA
no-reactor variant removes the direct theta13 constraint but still fixes the
solar sector; it is the cleaner atmospheric cross-check. Its beam events are
different observations, yet its conditioned fitted summary is not the full
likelihood of a V1 model with theta12≈.414 and a large solar/atmospheric gap
ratio. A rigorous test would fit the candidate jointly to likelihoods with those
conditions consistently released, counting shared reactor/solar inputs once.

Any strictly increasing positive map f(J) preserves these eigenvectors. Thus
variable p, exponential or shifted mass maps can fit a gap ratio only by adding
mass-map freedom; they cannot repair either mixing angle. A common additive
mass-squared offset changes no gap. This is a useful exact limitation, not a
fit. No auxiliary map was selected in this V1 packet.

Reproduction: run `independent_v1.py --out <runtime>/independent_v1_results.json`,
then `compare_v1.py --grid <Fig4 CSV> --v1 <that JSON> --out <comparison JSON>`.
Inputs, URLs and SHA256 values are in runtime `inputs/manifest_v1.json`,
`inputs/manifest_supplement.json`, and `inputs/manifest_latest_accelerator.json`;
the grid hash is 5b5e7e223b093f14b7960e4542adca1f842881066765b360de3ffa5ae4c426c1.
The exact reports/code/results are sealed by `V1_DELIVERY_FREEZE.json`.
All calculations are subsecond and numerical threads are capped at one.

A source-pin search for Laguerre/Jacobi-endpoint flavor language found unrelated
Laguerre oscillator modes and endpoint flavor algebra in main; it supplies no
physical generation-to-Laguerre bridge for this candidate. No novelty claim for
Jacobi quadrature, the spectral theorem or the diagonalization is made. The
next useful candidate is an explicitly separate boundary-defect hypothesis,
subject to infinite-operator positivity and a changed scalar measure, as derived
in `BOUNDARY_ADMISSIBILITY.md`.
