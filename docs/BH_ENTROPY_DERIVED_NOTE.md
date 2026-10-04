# Bekenstein-Hawking Entropy Finite-Lattice Companion

**Date:** 2026-07-11
**Claim type:** open_gate
**Status:** open finite numerical companion; no retained black-hole entropy
derivation or all-`L` coefficient theorem is claimed
**Audit-status authority:** independent audit lane only
**Primary runner:**
[`scripts/frontier_bh_entropy_derived.py`](../scripts/frontier_bh_entropy_derived.py)

## Scope

This note records reproducible finite-lattice calculations for a half-filled
nearest-neighbor free-fermion carrier. It compares a Gaussian subsystem
correlation entropy with

```text
S_max = |dA| log chi_eff
```

and with the Bekenstein-Hawking comparison coefficient `1/4`. It does not
derive that normalization from the four axioms—Lattice, Qubit, Admissibility,
and Record—and it does not identify the carrier observable with physical
black-hole entropy.

The paired
[`BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md`](BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md)
now classifies the asymptotic issue as an open gate. In particular, the exact
two-dimensional geometric Widom integral `1/6` is not silently promoted to the
coefficient of the mixed zero-mode prescription used by these finite runs.

## Corrigendum (2026-09-30)

**What was misleading.** The "Reproduced Finite Results" section below quotes
the two-dimensional linear-in-`1/L` intercept `0.2492` (the runner prints it as
`0.3%` from `1/4`) and says its closeness to `1/4` is evidence against
declaring the finite data inconsistent with `1/4`. The finite data do not
support that reading, for two reasons.

1. **The mixed zero-mode prescription adds an `O(L)` term.** An even-`L` open
   square has exactly `L` zero modes, the same number as the boundary sites
   `|dA| = L`. `C = 1(H<0) + (1/2)1(H=0)` gives each of them occupation `1/2`
   (global entropy `L ln 2`). On the left half this adds
   `S_mixed - S_pure = 0.1946 L - 0.103` (fit on `L >= 16`) relative to a pure
   half-filled Slater state (a real orthogonal Haar-random half of the zero space, mean of six
   draws), which is the same order as the area term the ratio reads. At
   `L = 40`: `r = 0.2697` mixed, `0.2177` pure half-filled and `0.2184` with
   the zero modes left empty, so the pure state removes `50%` of the excess
   over `1/6`. At `L = 64`: `0.2570` mixed against `0.2107` pure (the earlier
   `scripts/probe_bh_rt_ratio_asymptotic.py`, whose lowest-`N/2` state is also
   pure, gives `0.2107` there). The rank `chi_eff` is `L` for the mixed and
   pure states (`L - 1` with the zero modes empty), so the denominators agree.
   The raw `r(64)` being within `2.8%` of `1/4` is therefore partly a
   zero-mode effect of the mixed state.
2. **The `1/L` intercept depends on the prescription, and the finite data do
   not fix the fit form.** On the runner's sizes `L = 6..48` the
   linear-in-`1/L` intercept is `0.2492` (mixed), `0.2078` (pure) and `0.2008`
   (empty zero modes), and for the mixed state it drifts with the fit window
   (`0.2472`, `0.2416`, `0.2374` for `L >= 6, 16, 32`). Every state's `r(L)`
   is still falling at `L = 64` (and at `L = 96` in the pure-state probe). On
   `L >= 24` the `c + a/ln L` form fits the mixed data better than `c + b/L`
   (maximum residual `1.2e-4` against `7.8e-4`), but for the pure and empty
   states the two forms fit about equally well (residuals `2e-4` to `7e-4`) while
   extrapolating to different intercepts (`0.15` and `0.20`).

**Corrected statement.** The finite data do not show that the asymptotic
coefficient is `1/4`, and the `0.2492` intercept is not evidence for it: with
a pure half-filled state neither fit form reaches `1/4`. Fits
`r = c + a/ln L` on `L >= 16` to `L >= 40` give `c = 0.147` to `0.158` for the
mixed, empty and pure states (the probe's two-parameter fits to `L = 96` give
`0.150` to `0.160`); this is near the exact geometric value `1/6` and more
than `35%` below `1/4`. That is a fit-form-dependent finite-size indication,
not a proof: the linear-in-`1/L` fits give `0.20` to `0.25`, the probe's
three-parameter fits `c + a/ln L + b/L` are unstable (`c` from `0.12` to
`0.19` across windows), and the limit of `r(L)` for either prescription stays
an open gate (Open Gates 2 below). The three-dimensional `1/L` intercept
`0.0644` was not re-examined under other prescriptions here.

**What still stands.** The finite numbers the runner prints, the exact
two-dimensional Widom integral `1/6`, the scope statements and the open gates
are unchanged, and `scripts/frontier_bh_entropy_derived.py` is not modified
(its printed "Deviation from 1/4: 0.3%" line is superseded by this section).

**Evidence.** `scripts/frontier_bh_entropy_zero_mode_pure_vs_mixed_2026_09_30.py`
(expected `PASS=11 FAIL=0`) builds the eigenbasis analytically from the open
chain sine modes, reproduces the mixed `S_corr` of
`scripts/frontier_bh_entropy_rt_ratio_widom.py` to `2e-14` at
`L = 8, 16, 24`, and prints the three prescriptions side by side. These are
same-family checks by the author; no independent referee has reviewed them.

## State Prescription

At half filling the `N/2` spectral cut can cross a degenerate eigenspace.
Selecting an arbitrary subset of eigenvectors would make the result depend on
the diagonalizer's basis. The runner instead occupies the whole Fermi-level
eigenspace with the common fractional weight needed for `Tr(C)=N/2`.

For the particle-hole-symmetric cases in the current grids this reduces to

```text
C = 1(H<0) + (1/2)1(H=0).
```

The resulting global state is generally mixed. The reported `S_corr` is the
Gaussian entropy of the restricted correlation matrix, not a claimed
pure-state entanglement entropy.

## Reproduced Finite Results

The current runner reports:

- two-dimensional finite boundary fit: `R^2 = 0.999010`;
- three-dimensional finite boundary fit: `R^2 = 0.996339`;
- mean finite comparison ratio `S_corr/(|dA| log chi_eff)`:
  `0.3143` in 2D and `0.1249` in 3D;
- two-dimensional `1/L` diagnostic intercept: `0.2492`;
- three-dimensional `1/L` diagnostic intercept: `0.0644`;
- monotone entropy decrease for the sampled positive `g/r` onsite potential at
  `g >= 0.5`;
- exact cancellation of duplicate-copy factors under the runner's explicitly
  independent-copy construction. This is a bookkeeping identity, not a
  species-universality, Hilbert-dimension, or bond-dimension result.

The fit intercepts are model-dependent finite-size summaries. The 2D
`1/L` intercept being close to `1/4` is evidence against declaring the finite
data inconsistent with `1/4`; the separate `c+a/log L` fit in the Widom runner
favors a value near `1/6`. Neither fit is an all-`L` theorem.
See the Corrigendum above: the `1/L` intercept depends on the zero-mode
prescription and is not evidence for `1/4`.

## Imported And Conventional Inputs

- nearest-neighbor free-fermion Hamiltonian and open boundary conditions;
- the basis-invariant mixed half-filling prescription;
- the Bekenstein-Hawking `1/4` value as an external comparison target;
- the positive `g/r` onsite-potential profile used by the diagnostic; its sign,
  normalization, and coupling to this fermion carrier are selected diagnostic
  inputs, not a derived gravitational bridge;
- `t=1` in the nearest-neighbor Hamiltonians, the `10^-6` SVD tolerance, the
  finite size grids, and the selected fit windows/forms;
- the SI constants (`G`, `c`, `l_P`, and `M_sun`) and benchmark masses used
  only in the frozen-star comparison table;
- the convention identifying the counted lattice boundary with the area
  comparator and the separately supplied `1/4` normalization in that table.

These are explicit external or conventional inputs to this diagnostic. The
four-axiom baseline is used only as the framework boundary against which those
inputs are disclosed.

## Open Gates

1. Derive or explicitly supply as a conditional a physical state selection and entropy
   observable for the intended black-hole carrier.
2. Prove the mixed-state and threshold-rank asymptotics, rather than selecting
   a finite fit family.
3. Derive the physical bridge from the lattice comparison to area in Planck
   units and to the Bekenstein-Hawking observable.

## Reproduction

```bash
python3 scripts/frontier_bh_entropy_derived.py
```

Expected current summary: `CHECKS PASSED: 4/4`. This is runner accounting for
the declared finite checks, not an independent audit verdict.
