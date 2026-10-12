# Finite source profiles with a positive common scalar spectrum

This block supplies a concrete discriminator that is absent in the point-source calculation: a broad positive mediator spectrum can make different exterior heights respond to different mixtures of a layered source. The supplied model has three independent source rows at Earth surface, a representative satellite altitude and the Sun at 1 AU. A vector retuned to cancel two rows leaves a calculable third response. The effect falls rapidly with increasing mediator range, and independent source rows do not by themselves identify the full quadratic coupling inverse.

These are conditional theoretical results, not experimental exclusions. No scalar instrument template, ephemeris normalization or observational likelihood is supplied in this block. The source profiles, geometry and coupling assumptions are not precision geophysical or nuclear inferences.

## Frozen model and source data

[MODEL_FREEZE.json](MODEL_FREEZE.json) was written at 2026-10-12T17:34:18.714390 UTC before computing the finite-profile responses. It fixes:

- A common positive gamma measure with s=1: dν_ell(μ)=ell exp(-ell μ)dμ for inverse range μ≥0. It integrates to one. Every mode has the same composition coupling direction d=(g,x,e), with its positive modal weight.
- ell=10^7,10^9,10^11,10^13 m.
- Earth radius R=6.371e6 m; core radius .55R; core mass fraction .32 in Fe; mantle mass fraction .68 in SiO2. Density is constant separately within each layer. This is an explicit supplied model.
- Earth field radii R and R+710000 m. The latter is a representative satellite position, not the actual mission trajectory or an orbit-fit reconstruction.
- Solar radius scale 6.957e8 m and field radius 149597870700 m. The original BS05(OP) and BS05(AGS,OP) mass/radius/abundance tables are integrated in mass coordinate. Fe and O proxies for the unresolved metal remainder give four source variants.
- The same leading material charge approximations as the massless block. Mixture masses, atomic/nuclear response approximations and input hashes are recorded in the code and results.

The exactly massless scalar and this gamma spectrum are different comparison models. The massless coupling vector is held fixed as a test vector; it is not assumed to remain calibrated under a new mediator measure.

The primary BS05 files are preserved from the [Bahcall solar model export](https://www.sns.ias.edu/~jnb/SNdata/Export/BS2005/). Their original source/version and hashes remain in the parent composition manifest. They are old source models used for explicit sensitivity tests, not a current probabilistic solar uncertainty model.

## Exact exterior shell response

The independently derived angular Yukawa average for shell radius a and r>a is

    <exp(-μ distance)/distance>
      =exp(-μr)/r * sinh(μa)/(μa).

Integrating the frozen positive measure gives potential and force factors relative to GM/r and GM/r²:

    P_ell(r,a)=ell/(2a) ln[(ell+r+a)/(ell+r-a)],
    F_ell(r,a)=P_ell(r,a)+ell*r/[(ell+r)^2-a²].

At a=0 these become ell/(ell+r) and ell(ell+2r)/(ell+r)^2. For an arbitrary spherical composition profile q(a),

    W_P(r)=∫(dM/M) P_ell(r,a) q(a),
    W_F(r)=∫(dM/M) F_ell(r,a) q(a).

The point-test scalar acceleration divided by bare metric GM/r² is (q_test·d)(W_F·d). The source row includes its form factor W_F[0]; that normalization must not be discarded when quoting an acceleration. The normalized composition row is W_F/W_F[0].

An annual clock effect caused by changing source distance differentiates the potential, so it uses W_F. A static scalar clock shift uses W_P. [DERIVATION.md](DERIVATION.md) gives the calculation and conventions. Direct angular integration, gamma integration, a radial derivative check and the point limit agree with the closed formulas.

For ell=10^7 m, the Earth surface, satellite and solar force form factors W_F[0] are .886795, .862749 and .000133679 respectively. The Earth effective core mass fraction changes from .310698 at the surface to .311370 at satellite height, although its actual mass fraction remains .32. Different modal ranges weight the source layers differently.

## Fixed vector versus a new two-row cancellation

Take the massless double-source-null direction from the earlier block, normalized to x=.1. Its high-precision reconstruction is

    d0=(-.0000549667665158667142, .1, .0146708062435234729).

The original stored double-precision vector is also retained and evaluated separately. Its massless source contractions have rounding residuals -5.27e-21 (Earth) and 1.04e-21 (Sun); high precision is needed when the new effect becomes exceptionally small.

For each ell, **hold d0 fixed**, then separately construct a new vector with x=.1 that nulls the satellite and solar force rows. The table uses the high-precision massless representative for the fixed-vector column. Each scalar acceleration product is dimensionless, normalized to the bare metric source acceleration, for the TiAlV/PtRh contrast.

| ell (m) | Fixed d0: satellite Ti/Pt product | Retuned satellite+Sun vector: surface Ti/Pt product | Determinant of normalized surface/satellite/Sun rows |
|---:|---:|---:|---:|
| 1e7 | 2.35527e-12 | 1.91002e-13 | -1.07516e-10 |
| 1e9 | 4.67424e-16 | 2.15351e-20 | -1.08926e-17 |
| 1e11 | 4.67551e-20 | 2.23196e-28 | -1.12891e-25 |
| 1e13 | 4.67551e-24 | 2.23276e-36 | -1.12932e-33 |

Thus the massless vector is not an exact null of the new extended-source model. The retuned vector is a different vector for each ell and each choice of two rows; it is not a single vector surviving every mediator choice. At ell=10^7 m, the satellite+Sun retune is

    d=(-.0000550215687098283179, .1, .0147560382400114722),

and its surface source contraction is -7.51578e-9, while its two selected force-source contractions vanish to the working precision. The opposite retune, canceling surface+Sun and testing satellite, is also recorded.

The row rank is three for all four supplied models. Column scaling by the earlier coupling-box half widths (.001,.1,.1) gives condition numbers approximately 2.96e5, 2.94e12, 2.84e20 and 2.84e28. These values state the scaling convention and show why exact rank is not a practical precision claim. Model/source uncertainty and real measurement errors cannot be replaced by arbitrary-precision arithmetic.

## Why a spectrum matters

[RANK_LEMMA.md](RANK_LEMMA.md) gives a bounded proof, not just a numerical observation. For separated core/mantle radial supports, define their positive modal form factors C(μ), M(μ), and c(μ)=C/(C+M). The function c decreases with μ. The effective force core fraction satisfies

    f'(r)=Cov_r[c(μ), -μ²r/(1+μr)]>0

for a positive spectral measure with genuine width. Both functions in the covariance decrease with μ. Consequently two external radii have different material weights. If S is the normalized solar row,

    det[E(r1),E(r2),S]
      =[f(r1)-f(r2)] det[q_Fe,q_SiO2,S].

The second determinant is about 1.600015e-7 for the nominal inputs, and remains nonzero in the four supplied solar variants. This factorization independently agrees with the direct three-row determinant.

A single Yukawa mass gives proportional exterior source rows at all radii: its exterior field factor separates from a radius-independent source form factor. A point source, spatially constant composition or a massless-only spectrum also removes this discriminator. Finite radius alone is not the mechanism; a radial composition profile and modal width are both needed here.

For gamma s=1 at large ell, the first height-dependent composition effect scales as ell^-4:

    f(r1)-f(r2)
     =-.32*.68*R²[(1-.55²)/(1-.55³)](r2²-r1²)/ell^4
       +O(ell^-5).

The leading ell^-2 profile bias is common to both radii. At ell=10^13 m the computed height contrast divided by this leading asymptote is .99999636. This explains the rapid loss of practical discrimination as the spectrum approaches the massless limit.

## Joint clock response from the same field

After the initial profile calculation, [EXTENSION_FREEZE.json](EXTENSION_FREEZE.json) specified an additional derived response: the change of the locally measured Yb E3/E2 ratio between the two frozen Earth heights. It is not blind evidence. With supplied bare metric GM_E=3.986004418e14 m³/s² and c=299792458 m/s,

    Δln R_E3E2=6.95 e (GM_E/c²)
                  [W_P(r_alt)·d/r_alt-W_P(R)·d/R].

For the same satellite+Sun retuned vectors, this gives 2.71421e-20, 3.19335e-27, 3.31166e-35 and 3.31287e-43 across the four ell values. For the fixed massless representative, the corresponding first value is 7.00215e-19. These use the same couplings and source profile as the force calculation, with no separate clock-fit parameter. The universal metric contribution cancels in the local ratio; no practical clock sensitivity or empirical exclusion is claimed.

## What remains degenerate

Three independent source rows eliminate a simultaneous nonzero **source-charge** null in three coupling dimensions. They do not eliminate every null of the quadratic observables. A further exact family, constructed after inspecting the source-rank result, is

    x=.1,
    e=-(ΔQme_TiPt/ΔQem_TiPt)x,
    g=-(W_Sun,me*x+W_Sun,em*e)/W_Sun,0.

The Ti/Pt test contrast then vanishes at every Earth height, and the Sun source contraction vanishes. Thus both Earth Ti/Pt channels, solar annual E3/E2 and solar Be/Al all vanish. The same family gives a nonzero Earth-surface Be/Al scalar product: 5.52390e-11, 6.22978e-11, 6.22998e-11 and 6.22998e-11. A second Earth test-material contrast would therefore probe this remaining family. [contrast_null_results.json](contrast_null_results.json) preserves it rather than hiding this alternate cancellation.

A purely universal direction (g,0,0) also remains invisible to composition differences and these clock ratios. Distance-dependent gravity can test that direction. A complete inverse calculation must combine independent source rows, material contrasts and other gravitational responses; source rank alone is insufficient.

## Uncertainty and reproduction

The four solar model variants are kept distinct. A nominal vector is first held fixed when the source model changes; a separately retuned vector is then printed. At ell=10^7 m, the surface Ti/Pt response of the satellite+Sun retunes spans 1.88749e-13–2.01070e-13 across those variants. This is a stress range, not a confidence interval. Earth density/radius layering and atomic/nuclear charge errors have no calibrated uncertainty distribution here. Solar mesh quadrature has no continuum resolution error bound. These limitations prevent precision empirical coupling bounds.

[source_profiles.py](source_profiles.py) generated [results_80dps.json](results_80dps.json) and [results_60dps.json](results_60dps.json). The determinants agree to more than 23 relative decimal places; the 10^13 m determinant agrees to about 34. Both runs took under four seconds with one BLAS/OpenMP thread. [response_checks.py](response_checks.py) verifies the material determinant factorization, large-ell asymptote and height-clock transfer. [contrast_null.py](contrast_null.py) checks the additional null family. Every executable checks the immutable runtime deadline and both JSON and extensionless stop markers before running. No detached process, commit, push, PR or shared campaign-state edit was made.

Example from this directory:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
      python3 source_profiles.py \
      --source-dir /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/composition \
      --output /path/to/new-results.json --dps 80

These are author checks; independent scientific review remains the coordinator's responsibility. The useful next step is a joint response study with actual orbit/height templates and a second Earth test-material contrast, or an independently calibrated scalar fluctuation probe, while preserving the fixed-vector versus retuned-vector distinction.
