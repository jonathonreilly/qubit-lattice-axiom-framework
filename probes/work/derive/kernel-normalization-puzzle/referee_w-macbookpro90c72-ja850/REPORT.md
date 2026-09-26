# Referee: kernel-normalization-puzzle a1

Attempt `w-jonathonsmac4f50-j00a2`. This script does not import that attempt. The formation runs were not repeated.

## Verdicts

**N1.** In `probes/lib/formation_levelplane.py` the axes `t1, t2` are built from the initial direction before the time loop. The sphere branch then records `s·t1` and `s·t2`, and the spectrum is the average of the two squared Fourier components. The calibration is `σ² = A(nβ)/(nβ)` with `n = dim + 1` on the backward stencil and `n = 2 dim + 1` on the symmetric one. A three-dimensional backward plane therefore has `n = 4`, not `3`.

**N2.** For two independent centred Gaussians of variance `v`, `⟨(θ²)^m⟩ = (2v)^m m!` through `m = 4`. The radial integral of `sin²θ` has the expansion

`E[sin²θ]/T = 1 − (2/3)T + (4/15)T² − (8/105)T³ + O(T⁴)`,

where `T = 2v`. The quadratic polynomial in the attempt is the truncation of this expansion. It is not an identity for the exact expectation.

**N3.** `A(κ) = 1 − 1/κ + 2/(e^{2κ}−1)`, so `β · (2/3) · A(3β)/(3β) = (2/9) A(3β)`, which tends to `2/9`. At `T = σ² = A(3β)/(3β)` the linear deficit is `0.09259` at `β = 2` and `0.00913` at `β = 24`. The attempt's own stdout prints these values. Its summary instead says `0.0300` and `0.00309`.

The quadratic ratio at those two couplings is `0.9126` and `0.9909`. The quoted backward table, `0.95–0.99` at `β = 2..6`, lies above `0.9126`. With `T ≥ σ²` this Gaussian factor would push the ratio even lower, so it is too large to be the whole measured ratio. The same linear deficit at `β = 2` remains above `0.07` for `n = 4` and above `0.04` for `n = 7`.

The factor is below 1, so it still does not produce the quoted values above 1.

## What stays open

The Gaussian hypothesis, the shell weight `W`, and the three unpriced candidates were not derived. The quoted table was not remeasured.

## Result

HIT: confirmed as a corrected partial. The lab-frame ratio is `1 − (2/3)T + (4/15)T² − (8/105)T³ + O(T⁴)`. At `T = A(3β)/(3β)` the deficit is `0.09259` at `β = 2` and `0.00913` at `β = 24`, not the stated `0.030` and `0.0031`.
