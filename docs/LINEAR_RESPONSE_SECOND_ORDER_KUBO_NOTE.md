# Second-Order Kubo Extension — Finite Second-Order Null Replay (Binding)

**Date:** 2026-04-07 (scope narrowed 2026-05-17 and sharpened
2026-06-18: binding scope is the finite second-order null replay on
the named runner; the boundary-of-Taylor-expansion no-go is split out
for separate review)
**Status:** bounded negative on the finite second-order null replay
— adding the second-order term `½·kubo₂·s²` to the first-order Kubo
prediction does not improve the failing-family residuals on the
declared 44-family runner panel at the cached truncation order. The
broader Taylor-expansion-boundary / no-higher-order-rescue
interpretation is **not** in this note's binding scope without a
separate remainder / convergence / non-analyticity theorem.
**Claim type:** bounded_theorem

## Scope narrowing

A prior source repair path for this row was to either narrow the note
to the finite second-order null replay, or provide a remainder /
convergence / non-analyticity theorem or higher-order computation
covering the failing families.

This revision takes the narrowing option. The binding evidence of
this note is exactly the **finite second-order null replay** on the
44-family panel: at the cached truncation order, adding `½·kubo₂·s²`
to the first-order Kubo prediction does not change the linearity-
regime subset count (15/44), residual sums grow slightly rather than
shrink, and the named failing families (`G2_asym_z`, `H1_ring`,
`L1_longrange`, `OF9_stretched`, `K3_NL5`) either degrade, stay the
same, or improve only marginally.

The broader claim — that **no higher Taylor order can rescue the
failing families** (a no-go statement about all higher orders, not
just the second) — is **demoted to out-of-binding-scope**. Promoting
that no-go requires either a remainder / convergence / non-analyticity
theorem covering the failing families, or an explicit higher-order
computation. Neither is supplied here.

`claim_type` is demoted from `positive_theorem` to `bounded_theorem`
to reflect the narrowed binding scope.

**Scope boundary after narrowing (2026-06-18):**
Repo audit machinery remains the authority for any terminal status.
This source note now takes the narrowing route: the binding
claim is only the actually replayed finite computation — second-order
Kubo on the declared 44-family battery and four cached strengths,
with the residual / linearity-regime numbers documented in §Result.
The broader Taylor-boundary question is explicitly out of scope here.
A no-go for third or higher Taylor order, for another expansion
basepoint, or for non-perturbative treatments would require a separate
remainder / convergence / non-analyticity theorem or a separate
higher-order computation. The safe read of this note is therefore the
second-order replay and the three observed second-order pathology
categories (finite-size `K3_NL5`, structural cancellation `G2_asym_z`,
phase decorrelation `H1_ring` / `L1_longrange`), not an all-orders
Taylor no-go.

## Artifact chain

- [`scripts/linear_response_second_order_kubo.py`](../scripts/linear_response_second_order_kubo.py)
- [`logs/2026-04-07-linear-response-second-order-kubo.txt`](../logs/2026-04-07-linear-response-second-order-kubo.txt)

## Question

The first-order Kubo lane derived `d(cz)/ds` at s = 0 via a parallel
perturbation propagator `B_j = d(amp_j)/ds`. The range-of-validity lane
showed that on a strict linearity-regime subset (15/41 families,
selected without the F~M label), measured F~M is within 1.6% of 1.0.

The other 26/41 families fall outside the strict linear regime. They
have documented nonlinear ratio patterns:

- `G2_asym_z`: ratio flips sign 0.17 → 0.05 → −0.19 → −0.69
- `K3_NL5`: ratio ≈ 2 throughout (systematic factor of 2)
- `H1_ring`: ratio drifts 0.55 → 0.58 → 0.65 → 0.80
- `L1_longrange`: similar drifting pattern
- `OF9_stretched`: ratio crosses 1 from above

This lane tests whether **second-order Kubo** (the `s²` term in the
Taylor expansion at s = 0) explains those patterns.

## The derivation

For path P from source to detector node j with phase factor `T_P` and
perturbation factor `Q_P = Σ_edges (L_e / r_e)`:

```
amp_j(s) = Σ_paths T_P · exp(−i s k Q_P)

A_j = amp_j(0)         = Σ T_P
B_j = (d amp_j/ds)|₀   = −ik Σ T_P Q_P
C_j = (d² amp_j/ds²)|₀ = −k² Σ T_P Q_P²
```

The recurrence for `C_j` follows from expanding `(Q_{P_i} + L_e / r_e)²`
along each incoming edge. With `g_e = −ik · L_e / r_e`:

```
C_j = Σ_{i→j} [C_i + 2·g_e·B_i + g_e²·A_i] · exp(ikL) · w · h²/L²
```

All three propagators (A, B, C) run in a single pass — same path-sum
structure, same O(edges) cost.

The second-order prediction for the centroid response is:

```
predicted_delta_cz(s) ≈ kubo₁ · s + (1/2) · kubo₂ · s²

where
  kubo₁ = (d cz/ds)|₀  via A and B
  kubo₂ = (d² cz/ds²)|₀  via A, B, and C (chain rule):
        = (N₂ − 2·kubo₁·T₁ − cz₀·T₂) / T₀
```

with `N₁, N₂, T₁, T₂` the corresponding numerator/total derivatives
expressed via `2 Re[A* B]`, `2 Re[A* C] + 2 |B|²`, etc.

## Result

### Linearity regime (max |ratio − 1| < 0.10 at all 4 strengths)

| Selection | Count |
| --- | ---: |
| First-order Kubo only | **15/44** |
| First + second-order Kubo | **15/44** |
| **Growth** | **+0 families** |

The strict linearity regime does **not grow** with the second-order
extension. None of the failing families are brought into the linear
regime by adding the `s²` term.

### Aggregate residuals at s = 0.008

| Order | sum \|residual\| | median \|residual\| |
| --- | ---: | ---: |
| First-order only | 5.6090 | 0.003385 |
| First + second-order | 5.7221 | 0.003258 |

Sum of absolute residuals **grows** by 2% with the second-order term.
Median residual barely improves. The second-order term does not
provide a consistent reduction in the prediction error across the
44-family set.

### Per-family pathology

The six families with documented nonlinear ratio patterns:

| Family | kubo₁ | kubo₂ | 1st-order ratios | 2nd-order ratios | verdict |
| --- | ---: | ---: | --- | --- | --- |
| `G1_asym_y` | +2.69 | +6.14 | 1.25 → 1.29 | 1.25 → 1.27 | tiny improvement |
| `G2_asym_z` | +0.31 | −26.0 | 0.17 → −0.69 | 0.18 → **−1.04** | **worse at large s** |
| `H1_ring` | −2.12 | −60.8 | 0.55 → 0.80 | 0.54 → 0.72 | slightly better |
| `K3_NL5` | +0.27 | +0.08 | 2.12 → 1.89 | 2.12 → 1.89 | **no change** |
| `L1_longrange` | −1.36 | −57.3 | 0.59 → 0.70 | 0.58 → 0.60 | mixed |
| `OF9_stretched` | −0.05 | +3.64 | 1.27 → 1.03 | 1.33 → **1.50** | **worse** |

## Three observed second-order pathology categories

The failing families fall into three distinct nonlinear regimes,
**none** of which is fixed by the implemented second-order term:

### 1. Finite-size / boundary cases — `K3_NL5`

`K3_NL5` has NL = 5 (only 5 layers). The Kubo expansion assumes the
propagator has reached an asymptotic regime where the path-sum
structure is well-defined. With only 5 layers, the propagator is
dominated by boundary effects and never enters that regime.
`kubo₂ = 0.08` is essentially zero — the second-order correction
is negligible — but the measured ratio sits at ~2 throughout. At the
computed order the factor of 2 looks like a finite-size offset rather
than a second-order Taylor correction; whether some higher Taylor order
recovers it is not established here (no third-or-higher-order
computation is supplied). The computed second-order correction does not
move the family into the linearity regime.

### 2. Structural cancellation — `G2_asym_z`

`G2_asym_z` has broken Z2 in the measurement axis. The first-order
linear term is very small (`kubo₁ = 0.31`, vs ~5 for healthy families),
so the response is dominated by destructive interference cancelling
the leading term. The second-order term `kubo₂ = −26.0` is large in
magnitude but in the wrong sign regime: at s = 0.008 the corrected
prediction overshoots from −0.69 to **−1.04**. This finite replay
therefore shows that the second-order term worsens the declared
large-strength diagnostic for this family; it does not prove a
third-or-higher-order obstruction.

### 3. Phase decorrelation — `H1_ring`, `L1_longrange`

Both have large `|kubo₂|` (~−60) and ratio patterns that drift
smoothly with s in a way the second-order term does not resolve. The structural drift
(from 0.55 to 0.80 for `H1_ring`, from 0.59 to 0.70 for `L1_longrange`)
is consistent with **path-phase decorrelation**: paths with very
different lengths contribute to the response with random relative
phases. Closing the physical diagnosis would require a
non-perturbative path-sum treatment, a different expansion basepoint,
or an explicit higher-order/remainder theorem; this note supplies only
the second-order replay.

## What this finite replay supports

This is a **clean second-order negative** with a finite binding scope:

- The first-order Kubo derivation works on the **linearity regime**:
  15 / 41 families where the linear term dominates at the checked
  strengths (the measured-vs-linear ratio stays within the 10 % band at
  all four strengths). On these, F~M ≈ 1 (mean |F~M − 1| =
  0.0069) and gravity sign is correctly predicted. Whether the
  higher-order Taylor corrections remain small beyond the computed
  second order is not established here.
- The second-order Kubo extension does **not** generalize the
  derivation to the other 26 / 41 families at the checked order and
  strengths.
- The remaining failing families are best treated as open follow-up
  targets: finite-size corrections for `K3_NL5`, a controlled
  cancellation analysis for `G2_asym_z`, non-perturbative path-phase
  analysis for the decorrelation cases, or an explicit
  higher-order/remainder theorem.

## What stands

The first-order Kubo lane and the linearity-regime range-of-validity
lane are **unaffected** by this negative. They derive:

- Gravity sign: 42/44 sign agreement, r = 0.97 correlation across all
  44 families (true-Kubo lane)
- F~M ≈ 1: 15/15 families in the strict linearity regime, mean
  |F~M − 1| = 0.0069 (range-of-validity lane)

Those sibling positives stand or fall under their own source notes and
independent review status. This lane (second-order Kubo) does not
extend them, but it also does not undermine them.

## Frontier map adjustment (Update 7)

| Row | Update 6+ (after range-of-validity) | This lane |
| --- | --- | --- |
| Compact underlying principle | first-order Kubo derives sign + F~M on linear regime | **bounded**: second-order replay does not extend the 15 / 41 linearity reach |
| Theory compression | first-order derived; second-order open | **second-order does NOT extend the derivation; structural treatment needed for failing families** |
| Strength against harshest critique | analytic expression on linear regime | unchanged |

## Honest read

This is a **negative** but a clean and informative one. It says:

- The implemented second-order Kubo replay has a finite reach:
  it does not extend the linearity-regime subset already characterized
  by the first-order/range-of-validity lane.
- This note does not rule out third or higher Taylor terms, a different
  expansion basepoint, or a controlled non-perturbative treatment.
- The remaining derivation work must be **structurally different**:
  either finite-size corrections, full non-perturbative path-sum, or
  a different analytic framework such as expansion around a different
  basepoint or transfer-matrix spectral analysis.

It does **not** invalidate the first-order Kubo derivation. It tells
us where that derivation reaches and where it ends.

## What to attack next

1. **Born preservation derivation** — the Born condition `|I₃|/P < 1e-10`
   in the battery is a direct consequence of propagator linearity in
   the sources. This is a one-line proof that adds a third battery
   condition to the derivation column. Cheap and clean.
2. **Experimental prediction card for wave-retardation** — the
   physics flagship lane that's closest to a lab claim. Different
   scorecard column entirely.
3. **Non-perturbative path-sum analysis** for the failing families —
   structurally bigger than the Kubo lane; would need a new
   computational framework.

Of the three, (1) is the smallest and most certain to add a result.
(2) is the highest-leverage column move. (3) is the deepest but most
expensive.

## Bottom line

> "Adding the second-order Kubo term `½·kubo₂·s²` to the first-order
> prediction does not extend the derivation past the linearity regime.
> The strict linearity-regime subset stays at 15/44 (zero growth), the
> aggregate residual at s=0.008 actually grows by 2%, and the documented
> failing families (`G2_asym_z`, `H1_ring`, `K3_NL5`, `L1_longrange`,
> `OF9_stretched`) either get worse, stay the same, or improve only
> marginally with the second-order correction. At this checked order,
> the failing families fall into three observed pathology categories:
> finite-size effects,
> destructive cancellation of the linear term, and path-phase
> decorrelation. This note does not supply an all-orders Taylor no-go;
> it only shows that the implemented second-order correction fails to
> extend the first-order linearity-regime subset."

## Citation chain and source repair boundary

The prior source repair path flagged that the note extrapolated its
finite computation into a boundary claim about the Taylor-expansion
approach and higher Taylor orders without a convergence/no-go theorem.
The cited authority chain on this row is registered explicitly below so
the one-hop edges from the source note to its load-bearing inputs are
visible. Non-load-bearing baseline anchors are kept as plain text and
are not graph dependencies.

| Cited authority | File / log | Role on this row |
|---|---|---|
| Active runner | [`scripts/linear_response_second_order_kubo.py`](../scripts/linear_response_second_order_kubo.py) | computes the third parallel propagator `C_j = d^2(amp_j)/ds^2` at s = 0 via the same path-sum recurrence, evaluates `kubo_2 = d^2(cz)/ds^2|_0`, runs four battery strengths `s in {0.001, 0.002, 0.004, 0.008}`, and writes the per-family residual / ratio table cited in §Result |
| Frozen runner output | [`logs/2026-04-07-linear-response-second-order-kubo.txt`](../logs/2026-04-07-linear-response-second-order-kubo.txt) | preserves the linearity-regime count (15/44 first-order vs 15/44 first+second-order), the aggregate residual (5.6090 vs 5.7221), and the per-family kubo_1 / kubo_2 / ratio rows for the six families enumerated in the per-family pathology table |
| Audit-lane runner cache | [`logs/runner-cache/linear_response_second_order_kubo.txt`](../logs/runner-cache/linear_response_second_order_kubo.txt) | runner-cache copy referenced by the audit-lane replay verifying the second-order null result |
| Sibling first-order Kubo runner | [`scripts/linear_response_true_kubo.py`](../scripts/linear_response_true_kubo.py) | the literal first-order `<z*deltaH>_0` computation cited in §"What stands"; its closure is the input under which §"What this closes" defends the bounded 15/44 linearity reach |
| Sibling first-order Kubo log | [`logs/2026-04-07-linear-response-true-kubo.txt`](../logs/2026-04-07-linear-response-true-kubo.txt) | preserved log for the sibling [`docs/LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](LINEAR_RESPONSE_TRUE_KUBO_NOTE.md) |
| Generator inputs | `scripts/universality_classifier.py`, `scripts/independent_generators_heldout.py`, `scripts/global_coherence_off_scaffold.py` | the same three import surfaces enumerating the 26 swept + 9 scaffolded + 9 off-scaffold families used by the runner |
| Repo baseline anchor | `MINIMAL_AXIOMS_2026-05-03.md` (plain-text, non-citation baseline reference) | `unaudited` / `meta` repo-baseline terminology anchor for the linear path-sum architecture; not a mathematical input to the second-order replay |

The source repair path is to either (i) **narrow the source claim** to
the computed second-order null result on the 44-family battery, or
(ii) **add a theorem or computation bounding the Taylor remainder or
demonstrating non-convergence / non-analyticity** for the failing
families. This source text implements path (i): the
§"What this finite replay supports", §"Honest read", and §"Bottom
line" sections now make a strictly second-order statement and
withdraw the all-orders extrapolation.

Path (ii) remains open. A third-or-higher-order computation or an
analytic remainder/non-analyticity theorem is not supplied here. The
safe read is the second-order replay (computed §Result) plus the
three observed pathology categories (finite-size, structural
cancellation, phase decorrelation) seen by that replay — not an
all-orders Taylor no-go. The acknowledged residual is the absence of
a theorem covering Taylor orders beyond two; everything else (the
second-order recurrence, the kubo_1 / kubo_2 numbers, and the zero
growth of the strict linearity-regime subset) is supported by the
listed cited authorities.

This rigorization edit does not promote terminal status, edit generated
audit surfaces, or add the missing convergence theorem. It only narrows
the citable source claim to the finite second-order replay.

## Scope-narrowing repair (2026-06-20)

This dated revision implements the source-side narrowing route for the
re-audit flag *"scope_too_broad: remove or segregate the residual
all-orders Taylor / no-higher-order language in the conclusion sections,
or add a retained remainder / non-analyticity / higher-order computation
covering the failing families."* It removes/segregates the residual
language — it does **not** add the remainder/non-analyticity computation
(path (ii) above remains open). No derived value changes; only the
prose/print scope is narrowed to the computed second order.

Residual overbroad phrasings narrowed in the conclusion sections:

- **§"Three observed second-order pathology categories" → finite-size
  case `K3_NL5`.** Before: *"The factor of 2 is a finite-size offset,
  not a Taylor-series correction."* This categorically asserted the
  offset is unreachable by any Taylor order (an all-orders claim).
  After: *"At the computed order the factor of 2 looks like a
  finite-size offset rather than a second-order Taylor correction;
  whether some higher Taylor order recovers it is not established here
  (no third-or-higher-order computation is supplied)."* The claim is now
  scoped to the computed second order, with higher orders explicitly
  marked open.

- **§"What this finite replay supports" → linearity-regime bullet.**
  Before: *"15 / 41 families where the linear term dominates and the
  higher-order Taylor corrections are small."* The clause "the
  higher-order Taylor corrections are small" asserts about all higher
  Taylor orders, none of which is computed beyond the second. After: the
  regime is defined by the **observed** measured-vs-linear ratio staying
  within the 10 % band at the four checked strengths, and a sentence
  explicitly marks whether higher-order corrections remain small beyond
  the computed second order as *not established here*.

Runner narrowing (per the audit instruction "if a runner check asserts
the overbroad all-orders claim, narrow it to the computed-orders
statement"): the executed NULL-branch verdict string in
`scripts/linear_response_second_order_kubo.py` previously printed
*"Failing families need either much higher orders or a different
framework."* — an assertion about higher-order behavior the runner does
not compute. It now prints a strictly computed-second-order statement
that the failing families are not brought into the linearity regime at
the computed second order, with higher orders / a different framework
marked *not established here (not computed)*. No numeric output, no
derived value, and no PASS/FAIL accounting changed (the runner has no
PASS/FAIL gate to alter).

The safe read after this repair is exactly the finite second-order
replay (computed §Result) plus the three observed second-order pathology
categories. The all-orders Taylor question remains explicitly open.

**Status authority:** the independent audit lane on origin/main is the
sole authority for the terminal/effective status of this row. This
source-side edit narrows the citable claim only; it does not author or
alter any audit grade or verdict.
