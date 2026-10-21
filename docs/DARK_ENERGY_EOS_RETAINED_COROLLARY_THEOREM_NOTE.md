# Dark-energy EOS on a supplied stationary vacuum sector

**Date:** 2026-04-18; source scope corrected 2026-10-21
**Status:** conditional source corollary; audit status is owned by the independent audit pipeline.
**Script:** `scripts/frontier_dark_energy_eos_retained_corollary.py`

## Supplied premises

This note uses the following source assumptions, not independently retained framework conclusions:

1. A chosen `S³` geometric carrier and spectral identity `lambda_1(S³_R)=3/R²`, from [S3 general R](S3_GENERAL_R_DERIVATION_NOTE.md) and [S3 cap](S3_CAP_UNIQUENESS_NOTE.md).
2. Identification of the vacuum cosmological constant with that eigenvalue, `Lambda=3/R²`, as in [spectral-gap identity](COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md).
3. A stationary vacuum curvature radius `R>0`, with `dR/dt=0`, and constant c and G. R here is the vacuum curvature scale, not the evolving FRW scale factor `a_sc(t)`. The [discrete assembly](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md) and [smooth solution-class note](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md) are conditional source models.
4. A positive, separately conserved vacuum component on an expanding or contracting FRW background (`H!=0`), with the continuity equation supplied by the [continuum-model note](UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md).

At the reviewed source revision `f24d17d97d372df977476e4a69674577f31af575`, this row and all six named upstream rows are unaudited in the ledger. Source prose cannot promote them. The [current axioms](MINIMAL_AXIOMS_2026-06-29.md) do not by themselves supply the vacuum identification, stationary sector or FRW dynamics.

## Conditional corollary

Use energy density (not mass density):

```text
rho_Lambda = c^4 Lambda/(8 pi G) = 3 c^4/(8 pi G R²) > 0.
```

With R fixed, `d rho_Lambda/dt=0`. The separately conserved FRW continuity equation is

```text
d rho/dt + 3 H (1+w) rho = 0.
```

For `H!=0` this gives `w=-1`. It also gives the constant CPL parameters `w_0=-1, w_a=0` on this entire fixed sector. If H vanishes identically, the continuity equation alone does not determine w. Energy exchange with another component would change the premise and invalidate this inference.

If the correction model from [dark-energy EOS](DARK_ENERGY_EOS_NOTE.md) is additionally supplied,

```text
Lambda_eff = (3/R²) [1 - (l_P/R)²/4],
```

fixed R and l_P make this a constant shift. Where the effective energy density remains positive, the same continuity argument applies. This note does not derive that correction or replace a constant by an arbitrarily small time-dependent drift.

## What remains open

The calculation is a standard conditional FRW consequence. It does not derive the stationary vacuum sector, its identification with the observed dark-energy component, a value of R or Lambda, matter-content matching, or an observational precision. The [cosmology-scale note](COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md) and [numerical Lambda result](COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md) remain separate source questions.

A measured departure from w=-1 would challenge the joint use of this stationary, separately conserved vacuum as the observed component; it would not isolate which supplied premise fails. No current observational bound or guaranteed number of decimal places is asserted here.

## Source correction and reproduction

The original promotion narrative and proposed publication row are recoverable at source revision `f24d17d97d372df977476e4a69674577f31af575`. They are not current authority. This correction changes no ledger verdict or publication-table status. Those generated or independently owned surfaces require their own review.

```bash
python3 scripts/frontier_dark_energy_eos_retained_corollary.py
```

The runner checks the fixed-parameter conditional algebra and explicit premise-failure controls. Such checks do not derive the cosmological identification or grant retained status.
