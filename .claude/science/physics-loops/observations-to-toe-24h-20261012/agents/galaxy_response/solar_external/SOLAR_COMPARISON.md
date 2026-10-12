# Fixed galaxy response supplied with a QUMOND completion: Solar comparison

The fixed exponential response, supplied with the QUMOND field equation and the provisional galaxy calibration, predicts `Q2=2.88147e-26 s^-2` for the spherical Galactic-field conversion or `2.89416e-26 s^-2` for the stated disk approximation. Both exceed the unfitted Park et al. (2026) summary rectangle `[-2.0,5.2]e-27 s^-2`. Every point in the frozen, sampled parameter box also exceeds it. This is a conditional failure of this specific completion and comparison rule, not a new statistical exclusion, an exclusion of arbitrary nonlinear responses, or a completed galaxy-plus-Solar fit.

The initial derivation was frozen at **18:32:17Z**, the numerical contract/code at **18:46:44Z**, and the first numerical results at **18:46:45Z**, all on 2026-10-12. The parent's quadrupole results were first read after our numerical freeze. Primary target summaries were public and exposed before the protocol; the comparison is model development, not blind. No Solar target was used to fit the response, acceleration scale, or field conversion.

## Additional premises and mathematical response

The previously calibrated galaxy rule was `g_circ=g_bar/[1-exp(-sqrt(g_bar/a0))]`. It did **not** solve a nonspherical gravitational field equation. This block supplies the additional nonrelativistic completion

`laplacian Phi_N=4 pi G rho_b`,

`laplacian Phi=div[nu(|grad Phi_N|/a0) grad Phi_N]`,

`nu(y)=1/[1-exp(-sqrt(y))]`.

This is the established [QUMOND construction](https://arxiv.org/abs/0911.5464v2), here used as a candidate premise. We do not derive it from the galaxy rotation table or provide a relativistic completion. Transfer of the galaxy-fitted a0 into this PDE remains provisional. The source is a point Sun in a constant Newtonian external field, and the solution contains no independently adjustable harmonic tidal term.

For `Phi_N=-GM/r-g_Ne z`, use `rM=sqrt(GM/a0)`, `x=r/rM`, `c=cos(theta)`, `eta=g_Ne/a0`. The gradient in acceleration units and its modulus are

`u=n/x^2-eta e_z`, `v=sqrt(x^-4+eta^2-2 eta c/x^2)`.

The phantom-source divergence is

`D=div_x[(nu(v)-1)u]=nu'(v)[v^2-3(x^-2-eta c)^2]/(v x^3)`.

The regular near-Sun anomalous potential is defined with the Cassini sign:

`delta Phi=-(Q2/2)[z^2-r^2/3]`,

`Hzz=-2Q2/3`, `Hxx=Hyy=Q2/3`.

The independently derived dimensionless response `F=Q2*rM/a0` has two equivalent forms, with `P2=(3c^2-1)/2`, `w=1/x`, and `v=sqrt(w^4+eta^2-2 eta w^2 c)`:

`F=(3/2) integral dw dc P2(c) nu'(v) [v^2-3(w^2-eta c)^2] w^2/v`,

`F=(9/4) integral dw dc (nu(v)-1) [w^2(3c^2-1)+eta(3c-5c^3)]`.

Both integrations cover `0<w<infinity`, `-1<c<1`. The second angular polynomial has zero angular mean; subtracting any c-independent value of nu stabilizes the integral without changing it. With the published plus-cross-term convention, `F=-3q/2`. The physical scaling is `Q2=a0^(3/2) F(eta)/sqrt(GM)`.

The integrable zero-field saddle is at `w=sqrt(eta),c=1`. We resolve it by splitting w there and using `c=1-u^2`. No saddle volume or divergent value is clipped. The high-acceleration exponential tail makes the local anomalous source tiny, but the distant nonspherical source still creates a harmonic quadrupole. Suppression of `nu-1` at Saturn alone therefore does not suppress Q2. Spherical symmetry at eta=0 and nu=1 give exact zero controls.

## Frozen data roles and conversion assumptions

The primary fixed galaxy acceleration is `a0=7.658058668049826e-11 m/s^2`; the fixed-global-M/L control is `8.533673475349299e-11`. The development envelope `[7.65,8.70]e-11` spans reported calibration alternatives, **not** their full observational or PDE uncertainty. Distances, inclinations and per-galaxy stellar mass-to-light nuisance parameters were not freely refit in that preceding packet.

[Gaia EDR3/Klioner et al.](https://arxiv.org/abs/2012.02036v1), Table 2, gives the Solar-system acceleration magnitude `(2.32 +/- 0.16)e-10 m/s^2`; the uncertainty is explicitly a bootstrap **1-sigma** estimate. Its Galactic direction is `l=358.9 +/- 4.1 degrees`, `b=-3.3 +/- 4.6 degrees`. This block adopts `[2.00,2.64]e-10` as a magnitude rectangle, fixes the axis toward the Galactic center, and does not marginalize direction or component covariance. The measurement is relative to remote quasars; identifying the entire magnitude with a uniform local Galactic field is an additional approximation.

The conversion to the Newtonian background is not fixed by a locally uniform QUMOND boundary. We carry two declared parent-galaxy prescriptions:

`g_e/a0=eta nu(eta)` (spherical),

`g_e/a0=eta nu(sqrt(eta^2+s_b^2))`, `s_b=2 pi G Sigma_b/a0` (disk approximation).

The latter is the approximation in [Park et al. (2026), Eq. (12)](https://arxiv.org/abs/2602.17884v2). Sigma is adopted as `47 M_sun/pc^2`, with development range `[41,53]`, using twice the `3 M_sun/pc^2` uncertainty adopted there from Bland-Hawthorn & Gerhard's synthesis. This is not an independent surface-density likelihood or an exact Milky Way PDE solution. Both maps have unique positive roots: `d[eta nu(sqrt(eta^2+s_b^2))]/deta = nu+(eta^2/v)nu' >= nu+v nu' > nu/2 > 0`, since `-d ln nu/d ln v = sqrt(v)/[2(exp(sqrt(v))-1)] < 1/2`.

Fixed constants are `GM_sun=1.32712440018e20 m^3/s^2`, `AU=149597870700 m`, and `pc=AU*648000/pi`. In Sigma units of Solar masses per square parsec, `G Sigma=GM_sun*Sigma/pc^2`.

## Numerical results and independent comparison

The Gauss-Legendre orders 64,128,256 and cutoffs 40,60 are retained in the first frozen result. At the seven nonzero diagnostic eta values, the two forms agree within `2.94e-11` relative at order 256. Their slowest 128-to-256 change is below `8.84e-10` relative. The exact IBP tail bound beyond cutoff 60 is below `3.48e-22` in F for eta<=10; this is a tail bound, not a certified bound on the quadrature discretization error.

| eta_N | F=Q2*rM/a0 | Hzz*rM/a0 |
|---:|---:|---:|
|0.5|0.139411966033|-0.092941310689|
|1|0.254825263127|-0.169883508751|
|1.5|0.353205464436|-0.235470309624|
|2|0.438074892424|-0.292049928282|
|3|0.576018353464|-0.384012235642|
|5|0.761488620955|-0.507659080637|
|10|0.938849074978|-0.625899383319|

The parent's independently frozen Hessian-parts quadrature agrees within `5.32e-12` relative at the four common initial eta values. Its direct-density quadrature agrees within `2.73e-9`, consistent with its separate refinement series. Its provisional `QPhi=+3Hzz/2` label has the **opposite** sign to the observational Q2; the raw Hessian comparison resolves this without convention ambiguity. The parent result SHA256 is `c61e2f8966deb6b9f9fa5db998679f2656fe30afcc22b936655c3830ad1a5772`.

At central Gaia magnitude:

| Galaxy calibration | Conversion | eta_N | g_e/g_Ne | Q2 (10^-27 s^-2) |
|---|---|---:|---:|---:|
| Primary free global M/L | Spherical |2.382266044|1.271683496|28.81471848|
| Primary free global M/L | Disk, Sigma47 |2.397663167|1.263517100|28.94160986|
| Fixed global M/L | Spherical |2.074784874|1.310324588|30.77727371|
| Fixed global M/L | Disk, Sigma47 |2.090185762|1.300669865|30.93988518|

The disk approximation changes the primary prediction by `+0.4404%`. For the predeclared grid of 9 a0 values, 17 acceleration values, and 5 Sigma values (plus the spherical alternative), all 918 points were evaluated. The sampled spherical envelope is `[25.19133229,34.94080952]e-27 s^-2`; the sampled disk envelope is `[25.33656445,35.09160900]e-27`. All sampled adjacent differences increase with a0, g_e and, for the disk prescription, Sigma. Selected endpoint results checked at doubled order agree below `6e-13` relative. This does not prove global extrema between grid points, and the box is not a confidence region.

After the first numerical freeze, a publication normalization control at `a0=1.02e-10` reproduced Park's exposed spherical/disk examples as `3.38727755e-26` and `3.41122715e-26 s^-2`, which round to its `3.387e-26` and `3.411e-26` values. They played no role in choosing the candidate parameters or accepting the initial numerical result.

## Observable and conditional conclusion

[Park et al. (2026), Table I](https://arxiv.org/abs/2602.17884v2), reports `Q2=(1.6 +/- 1.8)e-27 s^-2` (1 sigma) from a simultaneous 792-parameter least-squares ephemeris fit using DE440 data and Cassini ranging through August 2017. The acceleration template is `delta a=Q2[(e dot r)e-r/3]`. We use its summary estimate; we did not reconstruct the nuisance covariance or refit the ranging data. The earlier [Hees et al. (2014)](https://arxiv.org/abs/1402.6950v2) result `Q2=(3 +/- 3)e-27 s^-2` is a historical control with overlapping observations, not an independent likelihood factor. This dynamical quadrupole differs from Cassini 2003's fitted Shapiro gamma.

Under the fixed premises, the primary prediction and every sampled box point fail the frozen summary-compatibility rule. The smallest sampled Q2 is 4.84 times the primary rectangle's positive upper edge, so the two declared background-conversion approximations do not reconcile this candidate. We do not translate that ratio into a sigma significance or posterior probability. The comparison assumes the completion enters the usual Solar ephemeris through this Newtonian anomalous potential; unconstrained relativistic modifications, a freely added tidal field, or screening are different models.

The consequential remaining gap is the **algebraic galaxy rule to disk PDE calibration**, followed by an exact Galactic background solution and orientation treatment. These can be investigated as separately declared models. They cannot be silently counted as included uncertainties in this packet. No retained/adopted physical claim, formal audit verdict, or universal MOND exclusion is made.

## Evidence and source pins

Runtime root: `/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/galaxy_response/solar_external/`.

- `initial_derivation_freeze.json`: independent derivation hash `08c26d654cf448a62ef47fad2bcb0d44b78d5710fcfd89a049eb89d093ad47af`.
- `numerical_contract_freeze.json`: protocol and code before first quadrupole calculation.
- `initial_numerical_results.json`: SHA256 `e6e2a70ae6e709121d9cb1822cb858a4d1c26d8fff79f5d963da2bcb76a63906`; both forms, all refinements, versions.
- `physical_comparison_results.json`: SHA256 `47e971f94c72c3d95d1ebceef2ecde412bee195087f30df9748a2fac03e9817d`; all 918 box rows, central predictions and parent comparison. Unit-explicit Q2 output is in inverse seconds squared.
- `solar_quadrupole_comparison.png` and `.pdf`: full prediction/summary display, visually checked. Model-box shading and observational-summary shading have different meanings.
- `inputs/source_manifest.json`: exact URLs, byte counts, download times and PDF hashes. Text extraction and selected rendered pages are retained; equations and uncertainty labels were checked against rendered pages.

| Primary document | Exact version | SHA256 |
|---|---|---|
| Park et al. |2602.17884v2, revised2026-07-28|`143b0aa0ebb7755175fd93c54b7e0127fb0171c20987297ea8f51e0d1511b638`|
| Hees et al. historical fit |1402.6950v2|`cdba1abaa49844e6c16d762ba561f33c6935e583f915571837330fd485bf4ef3`|
| Hees et al. response integral |1510.01369v1|`7931b315b086b04d67fa307c722effd3ac50c7a10adb7370f6a70d5c863832a8`|
| Gaia/Klioner et al. |2012.02036v1|`fe837894aeae91e89f59c0509b9ad4227a523f43a43674c023e5415d7ba5f700`|

The Hees 2014 PDF's later rendering date and the Hees 2016 PDF's 2022 compiled header are not new science versions. The already pinned Milgrom 2010 QUMOND PDF remains in the parent galaxy runtime `inputs/Milgrom2010_0911.5464v2.pdf`, SHA256 `203057e0596d8b0e7da2a2af900a84f530f40dd16f372bc9115a2941ba7fcc40`. The field equation and diagnostic integral are known constructions; independence here concerns derivation/check provenance, not novelty.
