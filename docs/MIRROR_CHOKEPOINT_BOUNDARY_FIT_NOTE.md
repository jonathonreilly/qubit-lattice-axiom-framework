# Mirror Chokepoint Boundary Fit Note

**Date:** 2026-04-03  
**Status:** bounded finite-window certificate for the named dense boundary mirror card; no mirror-family theorem and no asymptotic law.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is pipeline-derived after independent review.

This note freezes one named finite parameter card from the mirror chokepoint
runner. The claim is intentionally bounded: the card is Born-clean,
gravity-positive, and decohering for `N = 40, 60, 80, 100`, reaches a
gravity-estimator validity wall at `N = 120`, and has a weak descriptive fit
on the four selected fit rows. The fit is not used to select the card or the
fit rows.

**Primary runner:** [`scripts/mirror_chokepoint_boundary_fit_certificate.py`](../scripts/mirror_chokepoint_boundary_fit_certificate.py)

**Companion replay runner:** [`scripts/mirror_chokepoint_joint.py`](../scripts/mirror_chokepoint_joint.py)

**Registered output:** [`logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt`](../logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt)

**Canonical archival log:** [`logs/2026-04-03-mirror-chokepoint-boundary-canonical-n60-r5p0.txt`](../logs/2026-04-03-mirror-chokepoint-boundary-canonical-n60-r5p0.txt)

## Setup

- strict layer-1 chokepoint connectivity
- `NPL_HALF = 60` (`120` total nodes per layer)
- `connect_radius = 5.0`
- `layer2_prob = 0.0`
- `k = 5.0`
- `16` seeds
- selected fit rows `N = 40, 60, 80, 100`
- gravity-estimator validity wall at `N = 120`

The registered certificate replays this literal command before applying any
fit:

```bash
python3 scripts/mirror_chokepoint_joint.py --npl-half 60 --connect-radius 5.0 --n-layers 40 60 80 100 120 --layer2-prob 0.0
```

The literal card is an admitted finite evaluation surface, not a parameter
choice derived from a mirror-family theorem. Its role is only to define the
bounded object being replayed. No observed target, fitted exponent, or
extrapolated purity threshold selects the card.

## Pre-fit Inclusion Firewall

The finite card is selected by the setup and the pre-fit inclusion gates, not
by the exponent. The gates are:

1. the replay header is `NPL_HALF=60 (total 120), k=5.0, 16 seeds`;
2. each selected mirror fit row has all `16` successful seeds;
3. each selected fit row has Born `|I3|/P < 1e-10`;
4. each selected fit row has `|k=0| <= 1e-12`;
5. each selected fit row has positive gravity with `gravity / SE > 2`;
6. each selected fit row has `pur_cl < 0.95`;
7. the `N = 120` mirror output has no valid gravity estimates because its
   field-free detector norms are below the implementation's `1e-30` validity
   threshold, so the row is excluded before fitting.

Only after those gates are fixed is the exponent computed from
`1 - pur_cl` on `N = 40, 60, 80, 100`.

## Gate-passing Finite Rows

The bounded boundary pocket is Born-clean, `k=0`-clean, gravity-positive, and
decohering through `N = 100`:

| N | `d_TV` | `pur_cl` | `S_norm` | gravity | gravity/SE | Born `|I3|/P` | `k=0` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 40 | `0.6884` | `0.8608±0.03` | `0.9850` | `+4.7499±0.666` | `7.13` | `<1e-10` | `0.00e+00` |
| 60 | `0.4791` | `0.8440±0.03` | `0.9953` | `+3.9733±0.473` | `8.40` | `<1e-10` | `0.00e+00` |
| 80 | `0.4291` | `0.8182±0.03` | `1.0029` | `+3.0551±0.672` | `4.55` | `<1e-10` | `0.00e+00` |
| 100 | `0.2308` | `0.9043±0.02` | `1.0058` | `+1.3089±0.570` | `2.30` | `<1e-10` | `0.00e+00` |

`N = 120` is the gravity-estimator validity wall for this card. `11/16` seeds
return a row, but none of those eleven rows has both detector norms above the
implementation threshold `1e-30`. The companion initializes gravity to zero
and only evaluates the centroid displacement after both norm gates pass, so
its displayed `+0.0000±0.000` is a default sentinel, not measured zero
gravity. The primary certificate reconstructs the norms and requires `0/11`
valid gravity evaluations before excluding the row. No physical gravity value
is claimed at `N = 120`.

## Canonical Decoherence Fit

Fit on the selected fit rows only, using `1 - pur_cl`. With
`x_i = log(N_i)` and `y_i = log(1 - pur_cl(N_i))`, ordinary least squares gives
`y = log(A) + alpha x`, hence `1 - pur_cl = A N^alpha`:

```text
(1 - pur_cl) = 0.3901 × N^(-0.245)
R² = 0.126
```

The registered certificate computes the OLS result at full arithmetic
precision from the displayed four-decimal `pur_cl` inputs:

```text
A = 0.3900585585
alpha = -0.2453900421
R² = 0.1258401054
```

The resulting illustrative extrapolations are:

```text
pur_cl = 0.95 at N = 4.321958e3
pur_cl = 0.99 at N = 3.048489e6
```

The selected values are non-monotone and the fit quality is poor. The
extrapolations are therefore only arithmetic consequences of the weak
four-point summary; they are not predictions and are not evidence for an
asymptotic law.

## Closure Chain

1. The primary certificate runner replays the companion mirror runner on the
   fixed dense boundary command.
2. The pre-fit inclusion gates certify the mirror rows `N = 40, 60, 80, 100`
   as Born-clean, `k=0`-clean, gravity-positive with `gravity / SE > 2`, and
   decohering with `pur_cl < 0.95`.
3. The `N = 120` mirror output contains eleven default gravity zeros but zero
   valid gravity evaluations; it is an estimator-validity wall and is excluded
   from gravity claims and from the fit.
4. Ordinary least-squares regression on `log(1 - pur_cl)` versus `log(N)` for
   the four selected fit rows gives the quoted `A`, `alpha`, and `R²`.
5. The note makes no claim beyond this finite replay and post-inclusion
   descriptive fit.

## Assumption and Artifact Boundary

| Item | Role | Class | Load-bearing disposition |
|---|---|---|---|
| Fixed dense card and seed schedule | Defines the finite object | admitted finite evaluation surface | Explicitly scoped; no family-selection claim |
| Live rows at `N = 40, 60, 80, 100` | Supplies the bounded metrics | computed runner output | Replayed by the primary certificate and frozen in its registered cache |
| `N = 120` detector-norm validity threshold | Distinguishes evaluated gravity from the companion's zero sentinel | admitted implementation threshold (`1e-30`) | Reconstructed per returned seed; `0/11` gravity evaluations are valid |
| Frozen displayed row values | Regression expectations for transcription drift | computed-output regression fixture | Checked only after live replay; not an observational or fit selector |
| Gates fixed before regression | Selects the four fit rows and estimator-invalid row | certificate logic | Checked before `alpha` or `R²` is computed |
| OLS formulas | Produces `A`, `alpha`, and `R²` | exact arithmetic on computed rows | Recomputed in the certificate |
| Observations or external comparators | None | non-input | Not used |

There are no one-hop note dependencies in the load-bearing chain. The
companion replay runner is executable implementation used by the primary
certificate, while the archival log is corroborating history and is not an
independent proof input.

So the safe statement is:

- **mirror boundary pocket on the named card:** yes, through `N = 100`
- **canonical exponent fit:** `alpha = -0.245`, weak
- **gravity-estimator validity wall on the named card:** `N = 120`; gravity unresolved, not zero
- **bounded or asymptotic family law:** no
