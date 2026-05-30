# Rescaled NN Lattice C_arm Coherent-Saddle Support Note

**Date:** 2026-05-10
**Claim type:** bounded_theorem (leading coherent-saddle support for the
slit-detector arm-width constant; direct deterministic blocked-slit sigma
check now included in the primary runner, with max residual 1.96% against
the phase-corrected L2 saddle on the checked grid)
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:** [`scripts/lattice_nn_rescaled_C_arm_derivation.py`](../scripts/lattice_nn_rescaled_C_arm_derivation.py)
**Upstream harness:** [`scripts/lattice_nn_deterministic_rescale.py`](../scripts/lattice_nn_deterministic_rescale.py)
**Upstream harness note:** [`docs/LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md`](LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md)
**Diagnostic comparator:** companion PR #968 reports a four-point fit
`sigma_arm(h) = C_arm h^alpha` with `C_arm = 2.7107`,
`alpha = 0.5256`, R^2 = 0.9996 on `h <= 0.25`. Those numbers are used
here as a comparison target only, not as audit authority.

**Upstream bridge diagnostics (added 2026-05-11 in response to the
`audited_conditional` verdict on this row; each is itself a
`bounded_theorem` source note, not a retained-grade theorem):**

- [`docs/NN_LATTICE_RESCALED_FULL_KERNEL_IDENTIFICATION_NOTE_2026-05-10.md`](NN_LATTICE_RESCALED_FULL_KERNEL_IDENTIFICATION_NOTE_2026-05-10.md)
  — runner-backed identification of the field-free no-slit kernel
  `A(y_s -> y_d; h)`. Translation invariance is verified to machine
  precision on the checked refinement window. Its L1/L2 anchoring comparison
  is context only in this note; the repaired load-bearing bridge is the
  primary runner's direct blocked-slit sigma check below.
- **2026-05-26 direct blocked-slit check in the primary runner** —
  `scripts/lattice_nn_rescaled_C_arm_derivation.py` now imports the actual
  field-free blocked-slit propagation function
  `measure_arm_distribution(...)`, measures `sigma_arm(h)` directly at
  `h = 0.25, 0.125, 0.0625, 0.03125`, and verifies the phase-corrected L2
  saddle against those measured widths without using the diagnostic fit as a
  premise. The max residual is `1.96%`; all checked Born residuals are
  below `1e-10`.
- `docs/NN_LATTICE_RESCALED_C_ARM_NNLO_SADDLE_NOTE_2026-05-10.md`
  (see-also cross-reference; backticked to break cycle-0205 in the
  citation graph. The NNLO-saddle companion's own §"Companion work"
  table cites this LO derivation note as the load-bearing predecessor
  in the saddle expansion (`alpha_LO = 0.5000`, `C_arm_LO = 2.4855`);
  that direction is the load-bearing one. The forward pointer here is
  navigation to the refinement note, not a derivation input.)
  — closed-form finite-slit-aperture NNLO correction: complex-Gaussian
  truncated convolution `psi_det(y) ~ exp(-y^2/(4 alpha_total))
  [erf(u_b) - erf(u_a)]`. NNLO predicts `alpha_eff = 0.5247`,
  `|Delta alpha| = 0.0009` vs empirical `0.5256` (96% of LO gap closed under
  the fitted comparison). Per-h sigma_arm matches PR #968 to <= 0.3% across
  the fit window.
- `docs/NN_LATTICE_RESCALED_C_ARM_ALPHA_CONSTRAINED_REFIT_NOTE_2026-05-10.md` (back-reference, not load-bearing on this derivation — the refit note is a downstream *diagnostic-fit artifact* that consumes this derivation's `C_arm_analytic = 2.4855` as upstream authority. Backticked to break length-2 cycle `cycle-0011` in `docs/audit/data/cycle_inventory.json`; citation graph direction is *refit → this derivation*.)
  — diagnostic-fit artifact at the audit boundary: under `alpha = 1/2`
  constrained fitting (the geodesic-scaling prediction), the per-h estimator
  `C_arm(h) = sigma_arm(h) / sqrt(h)` recovers the analytic value
  pointwise on the checked grid with residual `0.504%` at h=0.03125 and
  `0.268%` at h=0.015625.

See the "2026-05-11 audit-repair addendum" section near the end of this
note for the consolidated repair statement and the corrected length-
anchoring interpretation.

## Claim

The companion fitted constant

```text
C_arm_numeric = 2.7107
```

is approximated by a coherent path-integral saddle on the rescaled NN
harness's per-step lateral characteristic function. The bounded closed
form tested here is

```text
C_arm^2(h)  =  L_eff  *  |a_pm(h)|^2  /  [ Re(a_pm(h) * conj(a_0(h)))  +  2 |a_pm(h)|^2 ]
```

with

- `a_0(h)   = exp(i k h) / sqrt(FANOUT)` — per-step amplitude for `diy = 0`;
- `a_pm(h)  = c * exp(i k h sqrt(2)) / sqrt(2 * FANOUT)` — per-step amplitude
  for `diy = +/- 1`, where `c = exp(-BETA * pi^2 / 16)`;
- `L_eff   = L_2 = 2 L_total / 3` — the slit-to-detector propagation length,
  set by the geometry of the harness (slit plane at layer `nl // 3`).

In the `h -> 0` leading-saddle limit the formula collapses to the
harness-fixed geodesic constant

```text
C_arm_analytic  =  sqrt(  L_2 / ( sqrt(2)/c  +  2 )  )
                =  2.4855
```

with `BETA = 0.8`, `k = 5.0`, `L_total = 40` matching the harness. The residual
versus the diagnostic fit is

```text
( C_arm_analytic  -  C_arm_numeric ) / C_arm_numeric  =  -8.31%
```

inside the 10% bounded comparison band. Per-h cross-checks with the full
coherent formula (retaining the `cos(k h (sqrt(2) - 1))` phase term)
match the diagnostic fit to better than 2.5% on all four fit points.
This is bounded analytic support at the harness-fixed parameters, not
exact derivation of the fitted constant and not status promotion for the
companion fit.

## Imported Authorities

| Authority | Role |
|---|---|
| [`docs/LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md`](LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md) | freezes the deterministic-rescale schedule, the per-step factor `step_scale = h / sqrt(FANOUT)`, and the harness parameters `BETA = 0.8`, `k = 5`, `L_total = 40`, `FANOUT = 3` used here as inputs |
| [`scripts/lattice_nn_deterministic_rescale.py`](../scripts/lattice_nn_deterministic_rescale.py) | provides the per-edge amplitude `f(diy; h)` and the slit-plane geometry (`bl = nl // 3`) used to set `L_eff = L_2 = 2 L_total / 3` |

This note is a bounded closed-form support note. It does not introduce a
new axiom, does not modify any retained theorem family, and does not
promote any status row.

## Derivation

### 1. Per-step amplitude

The harness's per-edge factor on the deterministic-rescale lane is

```text
f(diy; h)  =  step_scale  *  exp(i k L)  *  exp(-BETA * theta^2)  /  L
```

with `step_scale = h / sqrt(FANOUT)`, `L = h * sqrt(1 + diy^2)`, and
`theta = atan2(|diy|, 1)`. For the three NN edges this evaluates to

```text
f(0; h)    =  exp(i k h)              /  sqrt(FANOUT)        =  a_0(h)
f(+/-1; h) =  c * exp(i k h sqrt(2))  /  sqrt(2 * FANOUT)    =  a_pm(h)
```

with `c = exp(-BETA pi^2 / 16) = 0.61050` at `BETA = 0.8`. Note both factors
are h-independent in magnitude — `step_scale * 1/L` cancels h. The h-dependence
sits entirely in the per-step phase.

### 2. Lateral characteristic function

Sum the per-step amplitude over `diy` weighted by `exp(i q h diy)`:

```text
g(q; h)  =  a_0(h)  +  a_pm(h) * exp(i q h)  +  a_pm(h) * exp(-i q h)
        =  a_0(h)  +  2 a_pm(h) * cos(q h).
```

The path amplitude over `N = L_total / h` edges in lateral momentum is

```text
G_N(q; h)  =  g(q; h)^N
```

and the position amplitude on the detector is

```text
A_N(y)  =  (1 / 2 pi)  integral  dq  g(q; h)^N  exp(- i q y).
```

### 3. Saddle-point expansion

`g(q; h)` is even in q (since `a_+ = a_- = a_pm`), so its first q-derivative
at `q = 0` vanishes. The Taylor expansion to order `q^2` is

```text
g(q; h)  =  g(0; h)  -  a_pm(h) * (q h)^2  +  O((q h)^4).
```

Taking the logarithm:

```text
log( g(q; h) / g(0; h) )  =  - r(h) * (q h)^2  +  O(q^4),
                with  r(h)  =  a_pm(h) / g(0; h)   (complex in general).
```

Hence

```text
g(q; h)^N  =  g(0; h)^N  *  exp( - N r(h) (q h)^2  +  O(q^4) ).
```

This is the saddle-point equation: `g(q)^N` is a complex Gaussian centered at
`q = 0` with complex covariance `1 / (2 N r h^2)`.

### 4. Position distribution as a real Gaussian

Fourier-transform the complex Gaussian:

```text
A_N(y)  =  g(0)^N  *  ( 1 / sqrt(4 pi N r h^2) )  *  exp( - y^2 / (4 N r h^2) ).
```

The position distribution is `|A_N(y)|^2`, which is a real Gaussian:

```text
|A_N(y)|^2  =  |g(0)|^(2N) / |4 pi N r h^2|  *  exp( - Re( y^2 / (2 N r h^2) ) ).
```

`Re(1 / r) = Re(r) / |r|^2`, so

```text
|A_N(y)|^2  proportional to  exp( - y^2 * Re(r) / (2 N h^2 |r|^2 ) )
```

with variance

```text
sigma_arm^2  =  N h^2 |r|^2 / Re(r)  =  L_total * h * |r(h)|^2 / Re(r(h)).
```

Substituting `r = a_pm / g(0)` and using
`Re(a_pm / g(0)) = Re(a_pm * conj(g(0))) / |g(0)|^2`:

```text
sigma_arm^2  =  L_total * h  *  |a_pm|^2 / Re( a_pm * conj(g(0)) )
            =  L_total * h  *  |a_pm|^2 / [ Re(a_pm * conj(a_0))  +  2 |a_pm|^2 ].
```

This is exactly `sigma_arm^2 = C_arm^2 * h` with

```text
C_arm^2(h)  =  L_total  *  |a_pm|^2 / [ Re(a_pm * conj(a_0))  +  2 |a_pm|^2 ].
```

### 5. The `h -> 0` (geodesic) limit

`a_pm * conj(a_0) = (c / sqrt(2 FANOUT)) * (1 / sqrt(FANOUT)) * exp(i k h (sqrt(2) - 1))`,
so

```text
Re( a_pm * conj(a_0) )  =  ( c / FANOUT * sqrt(2) )  *  cos( k h (sqrt(2) - 1) ).
```

In the continuum limit the cosine -> 1 and the phase factor drops out. With
`|a_pm|^2 = c^2 / (2 FANOUT)`:

```text
C_arm^2  =  L_total  *  ( c^2 / (2 FANOUT) )
        / [ ( c / (FANOUT * sqrt(2)) )  +  ( c^2 / FANOUT ) ]
       =  L_total  /  ( sqrt(2) / c  +  2 ).
```

This is the parameter-free closed form for `C_arm` in the geodesic limit.

### 6. Slit-plane geometry: `L_eff = L_2 = 2 L_total / 3`

The harness places the slit plane at layer `bl = nl // 3` (see
`measure_full(...)` in `scripts/lattice_nn_deterministic_rescale.py`, line
123). The source-to-slit distance is `L_1 = L_total / 3`; the slit-to-detector
distance is `L_2 = 2 L_total / 3`. The "per-arm distribution on the detector"
is computed by propagating from the source with one slit blocked (the function
`pa = propagate(...)` with `blocked | set(sb)`), so the wave is forced through
the open slit at `y = SLIT_Y = 3.0`.

For the rescaled NN harness at the fit range `h <= 0.25`, the natural
source-to-slit transverse spread is `sigma_1 = sqrt(L_1 h r) ~ 0.4 - 0.9` for
`r = 0.2317` and `h in [0.0625, 0.25]`. This is smaller than the slit
half-width (1.0) but not negligibly so: the slit transmits the natural tail of
the source wave that lies within the slit window. After the slit, the surviving
amplitude continues for `L_2` and broadens with the same per-step
characteristic function `g(q; h)`. The per-arm width on the detector is
therefore set by `L_2`, not `L_total`.

Mechanically, the slit imposes a position constraint at `y = SLIT_Y` that
re-anchors the centroid. The post-slit propagation then gives the
standard saddle-point spread over `L_2`; finite slit-aperture corrections
remain part of the bounded residual, not an exact closure claim.

The closed form, with this length identification, is

```text
C_arm_analytic^2  =  L_2  /  ( sqrt(2)/c  +  2 ),    L_2 = 2 L_total / 3.
```

### 7. Closed-form reduction

With harness parameters frozen,

```text
c                   =  exp(-0.8 * pi^2 / 16)               =  0.61050
sqrt(2)/c           =  1.41421 / 0.61050                   =  2.31649
denominator         =  sqrt(2)/c + 2                       =  4.31649
L_2                 =  2 * 40 / 3                          =  26.667
C_arm_analytic^2    =  26.667 / 4.31649                    =  6.178
C_arm_analytic      =  sqrt(6.178)                         =  2.4855
```

Residual versus the diagnostic fit:

```text
( C_arm_analytic  -  C_arm_numeric ) / C_arm_numeric
   =  ( 2.4855  -  2.7107 ) / 2.7107
   =  -8.31%
```

inside the 10% bounded comparison band.

### 8. Per-h cross-check with the leading phase correction

Retaining the `exp(i k h (sqrt(2) - 1))` phase factor in `a_pm * conj(a_0)`,
the full coherent formula is

```text
C_arm^2(h)  =  L_2  /  [ ( sqrt(2)/c ) * cos( k h (sqrt(2) - 1) )  +  2 ].
```

Evaluated at the four fit points:

| `h` | `C_arm(h)` | `sigma_pred(h) = C_arm(h) sqrt(h)` | `sigma_fit(h) = 2.7107 h^0.5256` | reldiff |
|---|---:|---:|---:|---:|
| 0.0625 | 2.4911 | 0.6228 | 0.6312 | -1.34% |
| 0.1250 | 2.5081 | 0.8867 | 0.9087 | -2.42% |
| 0.1875 | 2.5367 | 1.0984 | 1.1245 | -2.32% |
| 0.2500 | 2.5778 | 1.2889 | 1.3081 | -1.47% |

All four points agree with the diagnostic fit to within 2.5%. The fitted
`alpha = 0.5256 > 1/2` is recovered: `C_arm(h)` increases with h because
`cos(k h (sqrt(2)-1)) < 1` for h > 0, which shrinks the denominator and
inflates `sigma_arm` faster than `sqrt(h)`. The geodesic exponent
`alpha = 1/2` is exact only in the strict `h -> 0` limit.

### 9. Direct blocked-slit sigma check (2026-05-26)

The primary runner now checks the closed-form phase-corrected L2 saddle
against the actual deterministic blocked-slit propagation rather than only
against the historical diagnostic fit. It imports
`measure_arm_distribution(...)` from
`scripts/lattice_nn_rescaled_continuum_identification.py`, which constructs
the field-free two-slit geometry, blocks the opposite slit for each arm, and
computes the detector arm widths directly.

The direct propagation check gives:

| h | nodes | measured sigma | phase-corrected L2 prediction | reldiff | Born |
|---:|---:|---:|---:|---:|---:|
| 0.25000 | 25,921 | 1.3147 | 1.2889 | -1.96% | 4.62e-16 |
| 0.12500 | 103,041 | 0.8984 | 0.8867 | -1.30% | 3.21e-16 |
| 0.06250 | 410,881 | 0.6282 | 0.6228 | -0.87% | 2.06e-15 |
| 0.03125 | 1,640,961 | 0.4416 | 0.4396 | -0.44% | 1.21e-15 |

The max direct blocked-slit residual is `1.96%`, and the max Born residual
is `2.06e-15`. This is the load-bearing audit repair for the blocked-slit
width bridge: the runner now measures `sigma_arm(h)` from the actual
blocked-slit propagation and compares it to the phase-corrected L2 saddle.
The diagnostic fit constants remain historical comparators, not premises of
the direct check.

## Cross-validation table

Closed-form and direct-check residuals at the harness-fixed parameters:

| Estimate | Formula | Value | Residual vs 2.7107 |
|---|---|---:|---:|
| Incoherent random walk | `sqrt(L_total * Var(diy_eff))` | 3.2955 | +21.57% |
| Coherent, `L = L_total` | `sqrt(L_total / (sqrt(2)/c + 2))` | 3.0441 | +12.30% |
| **Coherent, `L = L_2`** | `sqrt((2/3) L_total / (sqrt(2)/c + 2))` | **2.4855** | **-8.31%** |
| Coherent, `L = L_2`, with phase correction | per-h table above | matches each h to <= 2.5% | bounded comparison |
| Direct blocked-slit propagation | measured `sigma_arm(h)` vs phase-corrected L2 prediction | max residual 1.96% | bounded bridge check |

The incoherent estimate is a sharp upper bound: it ignores phase interference
between paths with different total `Sigma diy_i`, which destructively interfere
in the lateral random walk and suppress variance growth. The coherent estimate
restores this by Fourier-transforming the per-step amplitude rather than
squared-amplitude.

The post-slit length `L_2 = 2 L_total / 3` rather than `L_total` is the
geometric statement that the slit re-anchors the per-arm centroid; the
spreading is set by what happens after the slit, not by the full source-to-
detector transit.

## Reproducibility

Run

```text
python3 scripts/lattice_nn_rescaled_C_arm_derivation.py
```

to print all stages: incoherent estimate, phase-coherence diagnostic,
saddle-point coherent formula, h -> 0 limit, per-h cross-check, and the
direct deterministic blocked-slit sigma check. The closed-form stages depend
only on `BETA`, `K_PHYS`, `PHYS_L`, `FANOUT` taken from the upstream harness
script, and the slit-plane fraction `1/3` taken from `bl = nl // 3` in
`measure_full(...)`. The direct check then calls the actual field-free
blocked-slit propagation function `measure_arm_distribution(...)` from
`scripts/lattice_nn_rescaled_continuum_identification.py`.

## Bounded scope

This note derives the leading coherent-saddle `C_arm` formula from the
harness parameters and the slit-plane geometry. It does not:

- prove `alpha = 1/2` is exact at finite h (the cosine phase term raises the
  effective exponent to `0.5256` in the fit window, recovered by the formula);
- promote any retained-theorem-family row;
- close PR #968 or promote the companion diagnostic fit;
- claim derivation of `sigma_arm` outside the rescaled NN harness or away from
  the deterministic-rescale lane (the formula uses harness-specific `c`,
  `FANOUT = 3`, `L_total = 40`, slit at `nl // 3`).

The `8.3%` residual at the strict `h -> 0` saddle is consistent with sub-leading
non-Gaussian corrections to the saddle (the `O((q h)^4)` term dropped in step
3) and with finite-slit-aperture corrections that we have not closed
analytically. Both are sub-leading at the four fit points used.

## 2026-05-11 audit-repair addendum

The 2026-05-10 audit verdict on this row was `audited_conditional` with the
following load-bearing concern, quoted from the auditor's `repair_target`:

> add a retained bridge theorem or deterministic runner deriving the arm
> width from the actual blocked-slit propagation, and supply/audit the
> diagnostic fit artifact as a direct dependency.

The retained-bridge-theorem branch of the auditor's `or` is still not claimed
by this source note. The repair is the other branch: the primary runner now
performs the deterministic blocked-slit measurement directly. The no-slit
full-kernel comparison, NNLO saddle note, and alpha-constrained refit note
remain useful context, but they are not load-bearing substitutes for the
direct check.

**1. Direct deterministic blocked-slit check.** The primary runner now calls
the actual field-free blocked-slit propagation function
`measure_arm_distribution(...)` and checks the measured arm width against the
phase-corrected L2 saddle:

| h | measured sigma | L2 prediction | residual |
|---:|---:|---:|---:|
| 0.25000 | 1.3147 | 1.2889 | -1.96% |
| 0.12500 | 0.8984 | 0.8867 | -1.30% |
| 0.06250 | 0.6282 | 0.6228 | -0.87% |
| 0.03125 | 0.4416 | 0.4396 | -0.44% |

This is the repair for the audit-stated blocker: `sigma_arm(h)` is now derived
from actual blocked-slit propagation inside the primary runner, and the
diagnostic fit is not an input to that direct comparison.

**2. No-slit kernel and L1/L2 comparison demoted to context.** The
full-kernel identification note
(`NN_LATTICE_RESCALED_FULL_KERNEL_IDENTIFICATION_NOTE_2026-05-10`)
still numerically identifies the field-free no-slit kernel
`A(y_s -> y_d; h)` on its checked grid. Its L1/L2 comparison remains a
useful diagnostic of possible slit interpretations, but this note no longer
treats that comparison as the load-bearing length-anchoring proof. The
load-bearing bridge is the direct blocked-slit table above, which checks the
L2 phase-corrected saddle against the actual slit geometry.

**3. Diagnostic-fit artifact kept as comparator only.** The alpha-constrained
refit note (`NN_LATTICE_RESCALED_C_ARM_ALPHA_CONSTRAINED_REFIT_NOTE_2026-05-10`)
provides a useful view of the same measured widths under the geodesic
`alpha = 1/2` estimator:

| h | C_arm(h) | residual vs `2.4855` |
|---|---:|---:|
| 0.250   | 2.6294 | +5.788% |
| 0.125   | 2.5412 | +2.240% |
| 0.0625  | 2.5128 | +1.097% |
| 0.03125 | 2.4981 | +0.504% |
| 0.015625 | 2.4922 | +0.268% |

The residual halves under each refinement and asymptotes to the analytic
value. The original 8.3% residual was a fit-protocol artefact: a
two-parameter `(C, alpha)` fit lets `alpha` drift to `0.5256` to absorb
the cosine phase correction, which then over-inflates `C` by the
observed factor `2.7107 / 2.4855 = 1.0906`.

**Net effect on this row's claim.** The load-bearing repair is now a primary
runner check: direct blocked-slit widths match the phase-corrected L2 saddle
within `1.96%` on the checked grid. This addendum records a packet for
independent audit; it does not mark the conditional verdict resolved and does
not promote the row's status. The remaining bounded-scope caveats
(harness-fixed `BETA, k, L_total, FANOUT, SLIT_Y`, observable subspace,
field-free single-source) are intrinsic and not addressed by this addendum.

## Status

This source note is a bounded closed-form derivation plus direct blocked-slit
runner proposal. The audit lane sets the effective status after independent
review of the runner, the derivation steps, and the slit-plane length
identification.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `nn_lattice_rescaled_c_arm_nnlo_saddle_note_2026-05-10`
  (downstream consumer; backticked to break cycle-0011. Citation direction
  is *saddle → this derivation*, see the cross-reference in the §"Inputs"
  block above.)
- `nn_lattice_rescaled_c_arm_alpha_constrained_refit_note_2026-05-10`
  (downstream consumer; backticked to break cycle-0012. Citation direction
  is *refit → this derivation*, see line 44 above.)
