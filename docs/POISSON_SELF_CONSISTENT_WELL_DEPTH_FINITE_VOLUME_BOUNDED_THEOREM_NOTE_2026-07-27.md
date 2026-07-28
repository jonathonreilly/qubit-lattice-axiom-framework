# Finite-volume self-consistent localization and absolute-well-depth model comparisons on a supplied four-operator family

**Date:** 2026-07-27
**Status:** bounded support proposed for independent audit; not an audit verdict
**Type:** bounded_theorem
**Primary runner:** [`scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py`](../scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py)
**Cached runner output:** [`logs/runner-cache/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.txt`](../logs/runner-cache/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.txt)

Independent audit is required before the repository may assign retained grade.

## Exact target

On the listed finite lattices and couplings, compare two diagnostics for a
self-consistent eigenstate-density source across the supplied operator family
`{poisson, biharmonic, screened, local}`:

1. the RMS extent of the normalized density;
2. the absolute well depth
   `D_N = -min(V)` under the Dirichlet convention `V = 0` at the boundary.

For each finite sequence, compare the equal-parameter descriptive models
`a + c/M` and `a + b M`, where `M = N - 2` is the interior width.
R14 additionally reports the additive-reference-independent shell contrast

```text
C_N = mean(V; 9 <= r < 10) - mean(V; 4 <= r < 5).
```

This target is finite and computational. It does not assert that either model
is the true asymptotic expansion, that an infinite-volume limit exists or
fails to exist, or that `D_N` is a physical binding energy.

## Construction

The source is the density of the lowest eigenstate of the field that density
itself sources:

```text
H = -t A + V,
H psi_0 = E_0 psi_0,
rho = |psi_0|^2,
Op phi = s g rho,
V = phi <= 0.
```

`A` is the Dirichlet nearest-neighbor graph Laplacian constructed by
[`frontier_self_consistent_field_equation.py`](../scripts/frontier_self_consistent_field_equation.py).
`Op` runs over the four supplied operators. The sign `s` is chosen once per
operator from the first field solve so every comparison receives a
non-positive well. That is an explicit comparison convention, not a derived
physical sign rule.

The source is normalized by the eigensolver. It is not the propagated,
layer-normalized density used by the contextual parent
`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`.

## Finite claim ledger

| ID | Finite claim | Support and boundary |
|---|---|---|
| thesis | The tested finite sequences produce converged self-consistent states. At the scored couplings, Poisson (`g=50`) and screened Poisson (`g=100`) prefer `a+c/M` for absolute well depth, biharmonic (`g=10`) prefers `a+b M`, and the local zero-start sweep is discontinuous. | R0, R3-R12, R14. This is a finite-range model comparison under supplied conventions, not a limit theorem or uniqueness result. |
| R0 | Every scored operator produces a non-positive well under the per-operator sign convention. | All solves must converge and `max(V) <= 10^-12`. |
| R3 | Poisson extent increments fall by more than two orders of magnitude and end below `10^-3` on the two tested sequences. | `g=20`, `N=12..52`; `g=50`, `N=12..48`. No limit is inferred. |
| R4 | At `g=50`, the full depth sequence prefers `a+c/M` (`rss=5.21e-4`) to `a+b M` (`rss=2.31e-2`). The `g=20` depth sequence is inconclusive: the full sequence prefers `a+c/M`, while its last four sizes prefer the linear model. | The contradictory `g=20` tail is retained explicitly rather than averaged away. |
| R5 | At `g=10`, the biharmonic extent stays in `2.6725..2.9127` while its absolute depth runs `0.7874 -> 3.7835`; `a+b M` has `rss=1.61e-3` versus `6.72e-1` for `a+c/M`. | Six converged boxes, `N=12..32`; no divergence theorem is claimed. |
| R6-R7 | The observed biharmonic linear trend also appears for a prescribed normalized Gaussian, both with Dirichlet boundaries and on a periodic torus with the zero mode removed. | These controls remove the nonlinear fixed point and then the Dirichlet wall. They support a kernel attribution only for the implemented finite protocols. |
| R8 | The identical `V=0`-start local-operator protocol jumps from extent `0.0245` to `7.5743` across the size sweep. | This does not prove fixed-`N` bistability; it shows only that the sampled sweep does not exhibit a smooth continuation. |
| R9 | On the tested screened-Poisson sequence, the extent spread is `1.1e-5` and the depth sequence prefers `a+c/M`. | `mu^2=0.25`, `g=100`, `N=12..28`. |
| R10-R12 | Outside the localized source, replacing its density by a point source in the already supplied field solver changes the Poisson field median by about `10^-4` at odd interior width; the even/odd control strongly reduces the larger even-width residual when the point source is aligned with the centroid. | This is a localization/multipole-replacement check. It is not the transfer propagator's susceptibility and does not close the parent row's response-kernel bridge. |
| R14 | Over `N=24,32,40`, the biharmonic shell contrast `C_N` prefers `a+c/M`, while its absolute well depths prefer `a+b M`. | The separation depends on the Dirichlet-zero absolute-potential reference and does not apply to this fixed-window contrast. |

## Imports and support classification

| Input | Classification | Role |
|---|---|---|
| Dirichlet nearest-neighbor `A` and the four-operator menu | explicit supplied construction | Defines the finite comparison surface; it is not claimed to follow from the minimal axioms. |
| `t=1` | explicit normalization convention | Only ratios such as `g/t` are meaningful in the finite model. |
| `g` | scanned model parameter | No value is fit to observation. |
| `mu^2=0.25` | explicit supplied parameter | Defines the one screened-Poisson sequence. |
| per-operator source sign | explicit comparison convention | Makes every well non-positive; it is not a physical selector. |
| Dirichlet boundary value `V=0` | explicit boundary/reference condition | Gives meaning to the absolute depth `D_N`. |
| `eigsh(..., which="SA")` and sparse LU | numerical method | Every scored fixed point must satisfy the runner's convergence predicate. |

Each nonlinear solve starts the eigensolver from a deterministic uniform
vector and then warm-starts it from the preceding ground state. The principal
finite sequences use a `10^-10` fixed-point update threshold. The matched
point-source rows use `2*10^-9`, above the approximately `1.2*10^-9`
odd-centred numerical floor and far below the reported field-ratio precision.

No measured value, literature constant, observational comparator, probability
rule, readout bridge, or framework primitive enters the finite claims. The
primitive-registry check finds no use of the scale-reference,
kinetic-isotropy, or realized-state primitives.

## Proof-obligation boundary

The finite data do not prove the asymptotics of the nonlinear Dirichlet
problem. In particular:

- a lower RSS among two selected two-parameter models is not a proof of a
  limit or divergence;
- the `g=20` Poisson tail demonstrates why that distinction matters;
- the physical self-consistent energy functional is not specified, so
  `-min(V)` is not called binding energy;
- the matched point-source comparison reuses the selected field solver and
  therefore cannot derive that solver from the parent transfer propagator.

An infinite-volume theorem would need independent control of the discrete
Green-function asymptotics and of the nonlinear fixed-point branch. Those are
open obligations, not routine continuations of this note.

## No-Go Discipline N1-N8

The narrow negative content is only this: on the stated finite protocols,
biharmonic absolute well depth prefers the linear model, while the
fixed-window difference does not. No claim is made that every route or every
infinite-volume biharmonic construction fails.

### N1 — Alternative routes

| Route family | Marker | Result |
|---|---|---|
| finite-range/tail sensitivity | ATTEMPTED | The `g=20` Poisson full-range and tail-only fits prefer different models, so R4 records that sequence as inconclusive. |
| boundary topology | ATTEMPTED | The prescribed-source torus retains the finite linear trend through `N=96`. |
| nonlinear versus prescribed source | ATTEMPTED | Removing self-consistency retains the finite trend. |
| potential reference | ATTEMPTED | Referencing a fixed radial window succeeds in removing the separation; R14 narrows the claim to absolute depth. |
| source profile | ATTEMPTED | Both the self-consistent density and a prescribed Gaussian show the finite trend. |
| source-sign convention | ATTEMPTED | Each operator receives a non-positive well; the result is explicitly conditional on this convention. |
| larger finite range | ATTEMPTED | The periodic prescribed-source sequence extends to `N=96`; it still does not prove an infinite-volume statement. |

These families differ in object, boundary, nonlinearity, observable, source,
sign convention, or terminal asymptotic test; they are not merely different
phrasings of one run.

### N2 — Wall independence

The collapsed conditions are W1 finite four-operator menu, W2 one-particle
source, W3 finite boxes plus the two-model menu, W4 Dirichlet-zero absolute
potential reference, and W5 per-operator sign normalization.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| W1/W2 | no | no | yes |
| W1/W3 | no | no | yes |
| W1/W4 | no | no | yes |
| W1/W5 | no | no | yes |
| W2/W3 | no | no | yes |
| W2/W4 | no | no | yes |
| W2/W5 | no | no | yes |
| W3/W4 | no | no | yes |
| W3/W5 | no | no | yes |
| W4/W5 | no | no | yes |

### N3 — Hidden-wall scan

The construction, sign normalization, model menu, boundary reference,
couplings, and finite size ranges are explicit above. No “standard”,
“natural,” or “by construction” phrase supplies an unlisted physical premise.

### N4 — Residual matching

No prior negative result is used as proof of the finite model preferences.
The parent row is contextual motivation only; its missing susceptibility
bridge is expressly not claimed closed here. Accordingly there is no
cross-note witness count to inflate or residual to conflate.

### N5 — Rhetoric audit

The comparison is tested per operator, per listed coupling, on finite boxes,
for Dirichlet and periodic prescribed-source controls, and for absolute depth
versus a fixed-window difference. It is not tested in other dimensions, for
all source profiles, for multi-particle sources, for every branch, or for all
local operators. The claim is restricted to the tested resolutions.

### N6 — Partial-closure scan

Changing the potential reference to a fixed radial window is a non-axiomatic
reframing, and it succeeds. R14 therefore prevents a broader claim about local
fields. No new axiom or primitive is proposed.

### N7 — Steelman

The absolute potential is reference-dependent, the two fit families are a
small model menu, and the largest available sizes can reverse an all-size fit,
as the `g=20` Poisson control does. A biharmonic model may therefore have a
finite fixed-window potential contrast on the tested boxes even when the
Dirichlet-zero absolute depth grows with the box. This objection lands. The
note keeps only the finite absolute-depth model comparison and makes no no-go
or limit claim.

### N8 — Cross-cycle echo

The repository search found no retained prior wall that can be imported to
close this finite comparison, and the closest in-flight sibling is not used as
authority. The current runner instead tests the fixed-window contrast directly
in R14, and that test causes the narrowing recorded above.

**No-Go Discipline result: PASS for the narrowed finite statement.**

## What this does not do

- It does not repair or requeue `self_consistency_forces_poisson_note`; the
  transfer-propagator susceptibility bridge remains open.
- It does not consume any open sibling branch or compose a two-gate selector.
- It does not prove an infinite-volume limit, operator uniqueness, physical
  self-binding, or a physical binding energy.
- It does not apply or predict an audit verdict.

## Verification

```bash
python3 scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py
```

The runner first verifies that the imported parent module matches its committed
blob, then requires every scored fixed point and every thesis dependency to
PASS.
