# Physical parity versus old charge gauge

Bounded derivation and fixed-parameter numerical check. No new calibration, target splitting fit, target-based selection, or author-source edits. Andreev parameters are the successful calibration solution with minimum declared calibration cost (starttau=.2); cosine parameters are the frozen baseline in the same JSON. This does not reassess their fits or establish a physical device/TOE conclusion.

## Exact mapping

All coefficients below use the numerical energy/cycle-frequency GHz convention. Let delta=G²/(4EC Omega), s=1−delta. Starting with
Hphys(q)=4EC(n−q)²+V(phi)+Omega a†a+G(n−q)(a+a†),
substitute the real oscillator displacement a=b+Gq/Omega. The linear oscillator term becomes G n(b+b†). The remaining charge terms are4EC n²−8EC q s n+4EC q²s. Completing the charge square gives

Hphys(q) = Hold(q'=s q; b) + 4EC q² delta(1−delta) I.

Thus the proposed sign and q' mapping are correct. The scalar is positive for0<delta<1. Exact corresponding eigenvalue gaps are unchanged by the displacement and scalar. The equality is unitary equivalence in the full oscillator Hilbert space; an oscillator Fock truncation is not exactly displacement invariant.

Omega>0 and EC>0 with4EC Omega>G² ensure a positive quadratic charge/oscillator form and bounded-below stable problem for bounded periodic V. The algebraic substitution itself is formal beyond that stability range, but it should not be used there to infer a stable spectrum or envelope. The supplied cosine/Andreev potential commutes with the oscillator displacement, so its particular Fourier shape does not affect the identity.

Physical charge periodicity is q→q+1 via integer charge translation. Physical parity comparison q→q+.5 therefore maps to old offsets q'→q'+s/2, not q'→q'+.5. In particular physical endpoints0,.5 correspond to old0,s/2. Conversely the old endpoints0,.5 correspond to physical0,1/(2s). At these frozen fits s≈.993762, so the old upper endpoint slightly overshoots the physical half-charge extremum. Old gaps viewed as functions of q' have period s under the combined charge translation/displacement. Their periodicity is not1 when interpreted literally with the fixed G n coupling and no compensating shift.

For the real even potentials here, physical gaps are even in q and symmetric about.5. Hence the old-versus-physical endpoint difference is second order in the small displacement from the extremum. This does not justify treating a general old q'→q'+.5 comparison as an exact physical parity pair. A general envelope computation should use physical q,q+.5 or their correctly mapped old coordinates.

## Independent numeric check

The preserved scripts construct the real potential from4096 phase samples with its independently normalized first harmonic, project into the charge basis, then diagonalize the full charge⊗photon Hamiltonian. They implement both G n X and G(n−q)X directly and identify j0..6 by bare-device overlaps. No author model function is imported. Initial cutoff is charge−22..22,16 photons; a second run uses−26..26,20 photons. Physical q=0,.25,.5,.75,1, old q'=0,.5, and the mapped oldhalf endpoint are checked for both frozen parameter sets.

|model|delta|physical endpoint f06 dispersion Hz|old endpoint dispersion Hz|old mean−physical mean Hz|
|---|---|---|---|---|
|Andreev|0.006237410609|3464585.004380|3464247.573138|-168.715619|
|cosine|0.006238412249|544476.842126|544423.883973|-26.479075|

The mapping's f06 gap and ground-energy scalar checks agree within.00011Hz at the first cutoff. Physical period1 and q=.25/.75 reflection are numerically reproduced. Minimum selected bare overlap exceeds.9704; labels are unique. Increasing cutoffs changes tested physical f06 values by less than.000437Hz (Andreev) and.000189Hz (cosine); endpoint-mean corrections remain−168.71569Hz and−26.47905Hz. These decimal differences indicate numerical consistency, not experimental precision or a rigorous infinite-cutoff bound.

Accordingly this specific endpoint-convention correction changes f06 dispersion by roughly337.4Hz and53.0Hz, about0.0097% of the physical endpoint dispersion in each model. It is small against the3.465MHz/.5445MHz dispersion scale of these frozen models. It is not exactly zero and should be included when defining physical parity envelopes. This limited comparison does not claim insignificance against every possible measurement precision, validate the original mean-offset measurement interpretation, or certify an entire continuous envelope.

Changing the model convention while retaining fitted parameters is a diagnostic, not a recalibration. The existing calibration was performed under the old definition; this review does not silently substitute the mapped physical model into its prior residual claims. Physical parity occupation/preparation and the relation of endpoint averages to measured centers remain separate experimental assumptions.

## SHA256 identities

- `../ens-independent-cavity/model.py`: `6129a23fe0d9cb6cf1b0862702650e13c6a607d0cb6f0208042247a9e53c6090`
- `../ens-independent-cavity/calibration.json`: `a29d0a620d69f34aea0df124e94a7438206ccc6efe0970f815aca2549d99a284`
- `independent_parity_gauge_check.py`: `59527e476f8b075799dee13681215ee867c82499b236959c84fbccd75136444a`
- `independent_parity_gauge_results.json`: `1828bb5b83d20221ad5ad4dc7959366ae076b01ceae2b14bc73c29c5c015dec3`
- `independent_parity_gauge_check.log`: `82104b883a9460256f057d444ab73d9780d39a6cae4a5b512fa75d7bbfa9ce56`
- `independent_parity_gauge_fine_check.py`: `bbc7c5aac5dfae96623cfc1429aa32cfba75ffbb062b18de84e3d54322e9e7c5`
- `independent_parity_gauge_fine_results.json`: `8b1cf0160d9c90d7cce6af768ffda37bdb40f6a5f6a37872cd45e9b75911e141`
- `independent_parity_gauge_fine_check.log`: `c0ad8d853ccc36c74ab21ea2ebc4e6208c4ecffd40be76357b808c07aa7c800e`
