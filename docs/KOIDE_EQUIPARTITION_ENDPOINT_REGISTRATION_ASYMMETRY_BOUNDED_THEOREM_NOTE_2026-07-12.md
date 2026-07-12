# Equipartition Endpoints Are Registration-Asymmetric on the Tied First-Order Section — the `r = 1` Positive Branch Is Forced to `(3a,0,0)`, While `r = 1/2` Has an Open Three-Distinct Positive Sector with `Q = 2/3`; Allowing Signs Restores `r = 1` Non-Degeneracy but Unpins `Q` (Bounded Theorem, rhalf block 12)

**Date:** 2026-07-12
**Claim type:** bounded_theorem (exact tied-section positivity-window and
endpoint registration-compatibility asymmetry, conditional on explicitly
named unadopted identification elements). This source note does not set or
predict an audit outcome, adopt any premise, derive either equipartition
endpoint, or edit any audit-lane-owned registry or data file.
**Primary runner:**
[`scripts/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.py`](../scripts/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.txt`](../logs/runner-cache/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.txt)
(SCORECARD: PASS=23, FAIL=0)

> **CLAIMED (bounded and conditional):** on block 10's K-tied circulant,
> the nonnegative-spectrum phase set has nonempty interior exactly for
> `r < 1`. At the two landed fork endpoints, the positive branch is
> registration-asymmetric: `r = 1` permits only the phase points with
> spectrum `(3a,0,0)`, hence violates the same named three-distinct-value
> comparator used in block 10, whereas `r = 1/2` has the nonempty open sector
> `0 < |theta| < pi/12 (mod 2pi/3)` with three distinct positive values and
> `Q = 2/3` identically. If signs are instead allowed and
> `sqrt(m_k) = |lambda_k|`, `r = 1` regains non-degenerate patterns but `Q`
> becomes phase-dependent. Every record-facing statement is conditional on
> the named identification and branch elements below.
>
> **NOT CLAIMED:** a derivation or adoption of `r = 1/2`, a rejection of the
> `r = 1` algebraic endpoint outside the named registration conditions, a
> discharge of the equipartition/dial residual, an empirical comparison, a
> premise promotion, or an audit-status change.

## Role and exact boundary

Block 9 landed the two equipartition cells without choosing between them:
per-real-mode equipartition gives `r = 1`, while per-outcome-cell
equipartition gives `r = 1/2`. Block 10 forces K-reality into the measure at
its declared bounded grade and selects the K-tied branch over its all-real
competitor only after consuming a **named non-degeneracy element**: the
registered pattern has three distinct values. That element is a
comparator/premise, labeled and never thresholded.

This block asks the next exact question: once on that tied section, can both
equipartition endpoints support the registered pattern that block 10's branch
selection requires?

Take

```text
a > 0,        b = |b| exp(i theta),        r = |b|^2/a^2 >= 0,
lambda_k = a + 2|b| cos(theta + 2pi k/3),  k = 0,1,2.
```

The spectrum is real on the tie. The readout interpretation is **not**
supplied by the minimal Record axiom and is **not** supplied by the bounded
R-D anatomy note. This note therefore declares, without adopting, its own
bridge/modeling element

```text
B_sqrt:  sqrt(m_k) = lambda_k for each registered member,
```

together with the positive-branch convention

```text
B_plus:  lambda_k >= 0 for every k.
```

Only under `B_sqrt + B_plus` may the signed spectral sums below be read as
the mass-ratio functional

```text
Q = (sum_k lambda_k^2)/(sum_k lambda_k)^2.
```

The sign-allowed alternative is treated separately in T4; it uses
`m_k = lambda_k^2` and therefore `sqrt(m_k) = |lambda_k|`.

## T1 — exact positivity window for general `r`

Define the reduced phase distance

```text
delta(theta) = dist(theta, (2pi/3) Z),      0 <= delta <= pi/3.
```

Shifting `theta` by `2pi/3` only permutes the three eigenvalues, and reflection
of the reduced phase also only permutes their ordering. For
`0 <= delta <= pi/3`, the cosine multiset can be written as

```text
{ cos(delta), cos(2pi/3 + delta), cos(2pi/3 - delta) }.
```

The two gaps above `cos(2pi/3 + delta)` are exactly

```text
cos(delta)          - cos(2pi/3 + delta)
  = (3/2)cos(delta) + (sqrt(3)/2)sin(delta) >= 0,

cos(2pi/3 - delta) - cos(2pi/3 + delta)
  = sqrt(3) sin(delta) >= 0.
```

Therefore (runner checks 5-8)

```text
min_k cos(theta + 2pi k/3)
  = -cos(pi/3 - delta),

lambda_min(theta)
  = a - 2|b| cos(pi/3 - delta).
```

This decreases monotonically as `delta` runs from `0` to `pi/3`; its best and
worst values are `a-|b|` and `a-2|b|`. For `r > 0`, the exact condition is

```text
lambda_k >= 0 for all k
  iff min_k cos(theta + 2pi k/3) >= -1/(2sqrt(r))
  iff 1 - 2sqrt(r) cos(pi/3-delta) >= 0.
```

For `1/4 <= r <= 1`, let

```text
alpha(r) = pi/3 - arccos(1/(2sqrt(r))).
```

The complete phase classification is:

| range | nonnegative phase set | strictly positive phase set |
|---|---|---|
| `r = 0` | every phase | every phase |
| `0 < r < 1/4` | every phase | every phase |
| `r = 1/4` | every phase | `delta < pi/3` |
| `1/4 < r < 1` | `delta <= alpha(r)` | `delta < alpha(r)` |
| `r = 1` | `delta = 0` | empty |
| `r > 1` | empty | empty |

Equivalently in `(a,|b|)` coordinates:

- `a >= 2|b|`: every phase is nonnegative;
- `|b| < a < 2|b|`: closed windows of half-width
  `pi/3 - arccos(a/(2|b|))` surround `theta = 0 (mod 2pi/3)`;
- `a = |b|`: only those center points remain;
- `a < |b|`: no phase is nonnegative.

Thus the nonnegative phase set has **nonempty interior iff `r < 1`**. The
separate non-degeneracy statement is also exact. For `|b| > 0`, the product
of pairwise spectral differences is (runner check 16)

```text
(lambda_0-lambda_1)(lambda_0-lambda_2)(lambda_1-lambda_2)
  = -6sqrt(3)|b|^3 sin(3theta).
```

Hence the three values are distinct exactly when
`theta != 0 (mod pi/3)`. A strictly positive, three-distinct phase sector
therefore exists **iff `0 < r < 1`**. At `r = 0` all three values equal `a`;
at `r = 1` positivity leaves only a degenerate center point.

### The two endpoint windows

At `r = 1/2`, `|b| = a/sqrt(2)` and

```text
alpha(1/2) = pi/3 - arccos(1/sqrt(2)) = pi/12.
```

Thus nonnegativity holds exactly for
`delta <= pi/12`; the boundary `delta = pi/12` has one exact zero. The open
interior `delta < pi/12` is strictly positive, and deleting the collision
point `delta = 0` leaves the nonempty open, three-distinct sector

```text
0 < delta(theta) < pi/12.
```

Choosing the representative nearest `theta = 0`, this is
`0 < |theta| < pi/12 (mod 2pi/3)`.

At `r = 1`, `|b| = a` and `alpha(1) = 0`: the window degenerates to the
measure-zero point set `theta = 0 (mod 2pi/3)`.

> **T1.** The tied circulant has a genuinely open nonnegative phase window
> exactly for `r < 1`; it has a positive, non-degenerate window exactly for
> `0 < r < 1`. The `r = 1/2` half-width is exactly `pi/12`, while the `r = 1`
> phase set is zero-width.

## T2 — the per-real-mode endpoint is registration-incompatible on the positive branch

At `r = 1`, T1 forces `theta = 0 (mod 2pi/3)`. After the harmless spectral
permutation induced by the phase representative,

```text
(lambda_0, lambda_1, lambda_2) = (3a, 0, 0),
(m_0,      m_1,      m_2)      = (9a^2, 0, 0).
```

The two doublet members are equal, both before and after squaring. Therefore
the registered pattern has at most two distinct values and fails block 10's
same named element

```text
ND_3: the registered pattern has three distinct values.
```

`ND_3` is used only at its declared grade: a labeled comparator/premise, with
no threshold and no numerical data comparison.

> **T2.** Conditional on block 10's tied-section result, `B_sqrt`, `B_plus`,
> and the same named `ND_3` element, the per-real-mode endpoint `r = 1`
> cannot host a non-degenerate nonnegative registered spectrum at all. This
> is a registration-compatibility result, not a derivation that algebraically
> forbids `r = 1` outside those conditions.

## T3 — the per-outcome-cell endpoint hosts a registrable sector

The two trace identities are phase-free (runner checks 2-4):

```text
sum_k lambda_k   = 3a,
sum_k lambda_k^2 = 3a^2 + 6|b|^2.
```

On `B_sqrt + B_plus`, they give

```text
Q = (sum_k m_k)/(sum_k sqrt(m_k))^2
  = (sum_k lambda_k^2)/(sum_k lambda_k)^2
  = (3a^2 + 6|b|^2)/(9a^2)
  = (1 + 2r)/3.
```

At `r = 1/2`, this is identically

```text
Q = 2/3,
```

independently of `theta`. By T1, every phase in
`0 < delta(theta) < pi/12` has three distinct positive `lambda_k`. Squaring
preserves their distinctness because they are positive, so the registered
`m_k` also satisfy `ND_3`. This is a nonempty open registrable sector, not a
single fitted phase.

> **T3.** Conditional on `B_sqrt`, `B_plus`, and `ND_3`, the
> per-outcome-cell endpoint `r = 1/2` hosts a nonempty open non-degenerate
> positive sector, and `Q = 2/3` everywhere on it. This **does not derive
> `r = 1/2`**. It proves only that the already-landed `r = 1/2` fork endpoint
> has a registrable non-degenerate sector while the `r = 1` endpoint has none
> on the positive branch.

## T4 — allowing signs restores `r = 1` non-degeneracy but unpins `Q`

Consider instead the explicitly different branch

```text
B_abs:  m_k = lambda_k^2,       sqrt(m_k) = |lambda_k|,
```

with no requirement that every `lambda_k` be nonnegative. Then

```text
Q_abs(theta)
  = (sum_k lambda_k^2)/(sum_k |lambda_k|)^2.
```

At `r = 1`, the numerator remains the phase-free value `9a^2`, but the
absolute-value denominator is not the signed trace `3a`. Normalize `a = 1`,
which leaves `Q_abs` unchanged. At the exact non-degenerate point
`theta = pi/6`,

```text
lambda = (1+sqrt(3), 1-sqrt(3), 1),
m      = (4+2sqrt(3), 4-2sqrt(3), 1),

sum |lambda_k| = 1 + 2sqrt(3),
Q_abs(pi/6)    = 9/(13+4sqrt(3)) ~= 0.4516.
```

All three `m_k` are distinct. A second exact non-degenerate point is
`theta = pi/12`, where

```text
lambda = (
  1 + (sqrt(6)+sqrt(2))/2,
  1 - sqrt(2),
  1 - (sqrt(6)-sqrt(2))/2
),

sign(lambda)       = (+,-,+),
sum |lambda_k|     = 1 + 2sqrt(2),
Q_abs(pi/12)       = 9/(9+4sqrt(2)).
```

The three squared values are again distinct, and

```text
9/(13+4sqrt(3)) != 9/(9+4sqrt(2)).
```

Thus fixing `r = 1` fixes the quadratic numerator but not the absolute-value
denominator. The phase remains a live input, so the per-real-mode law alone
selects no value of `Q` on `B_abs`.

> **T4.** On the sign-allowed branch, the `r = 1` endpoint regains
> non-degenerate registered spectra, but `Q` is phase-dependent. Within the
> two endpoints of the landed equipartition fork, the per-real-mode law
> therefore either violates `ND_3` (`B_plus`) or pins no `Q` (`B_abs`). The
> per-outcome-cell endpoint is the unique fork endpoint compatible with both
> a non-degenerate registered pattern and a pinned `Q`, **conditional on**
> the tied-section result, the branch-appropriate identification
> (`B_sqrt + B_plus` or `B_abs`), and `ND_3`. This conditional compatibility
> does not choose or derive the endpoint.

## Source grades and the R-D boundary

Only the four bounded sources authorized for this block are used.

- **Block 9 — bounded theorem, no adoption/status authority.**
  [`KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`](KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  supplies the landed two-cell equipartition arithmetic and the real tied
  spectrum. It explicitly leaves the `r = 1` versus `r = 1/2` binary open.
- **Block 10 — bounded theorem, no adoption/status authority.**
  [`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  supplies the tied-section branch result at its declared grade and names
  `ND_3` as a comparator/premise, labeled and never thresholded. It also says
  the per-cell equipartition/dial law remains untouched.
- **Minimal axioms — current axiom memo, not a spectral bridge.**
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says that
  only records are readable and scalar readout is additive over disjoint
  records. Its Qualification requires a derivation, bridge, admission, or
  approved primitive registration for further structure. It does not map a
  circulant eigenvalue to a registered mass.
- **R-D anatomy — source proposal, independent audit required.** Read once
  from
  `origin/main:docs/RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`.
  Its own status says **“source proposal; independent audit required”** and
  that it does not adopt R-D, fix `r`, or provide status authority. What it
  actually carries is the supplied singlet/doublet projector surface, the
  conditional bookkeeping `(p_s,p_d) = (a^2,2|b|^2)`, idempotent pinching,
  the agreement-conditioned map `r -> 2r^2`, its inverse, and the unresolved
  independent-composition statistics atom. It **does not carry**
  `sqrt(m_k) = lambda_k`, a per-member spectral-to-mass map, or the
  nonnegative-eigenvalue branch. `B_sqrt`, `B_plus`, and the alternative
  `B_abs` are therefore this note's own explicitly unadopted modeling
  elements; they are not laundered through R-D or Record.

## Residual Atoms

1. **`B_sqrt`, the spectral square-root identification** —
   `sqrt(m_k) = lambda_k` per registered member. This note's own declared
   bridge/modeling element; unadopted and load-bearing for T2-T3.
2. **The branch convention** — `B_plus` requires all `lambda_k >= 0` and
   permits the signed trace in `Q`; `B_abs` instead registers
   `m_k = lambda_k^2` and uses `|lambda_k|`. Neither branch is adopted here.
3. **`ND_3`, the non-degeneracy element** — the registered pattern has three
   distinct values. Inherited from block 10 at exactly its comparator/premise
   grade, labeled and never thresholded; no numerical dataset is consumed.
4. **The equipartition/dial-point law** — per-real-mode versus
   per-outcome-cell equipartition remains the unresolved selector between
   `r = 1` and `r = 1/2`. This note reshapes the endpoints' conditional
   registration compatibility and does not discharge the selector.
5. **The K-tied section** — consumed only at block 10's declared bounded
   grade and conditional on that note's own supplied elements. This note does
   not independently derive the tie or enlarge its scope.
6. **The `C_3` circulant spectral model** — inherited from block 9 as the
   declared probe coupling, not derived here as a physical mass operator.
7. **The R-D statistics atom** — independent composition of repeated
   registration on the conditional weight bookkeeping remains unresolved;
   this note neither uses nor discharges it.

## What This Does Not Claim

- **Not** a derivation, adoption, or empirical selection of `r = 1/2` or
  `r = 1`. The equipartition/dial residual survives intact.
- **Not** an unconditional record-layer prediction. T2-T4 are conditional on
  the explicitly named identification, branch, non-degeneracy, and tied-
  section elements at their declared grades.
- **Not** a claim that the minimal Record axiom or the R-D source supplies a
  spectral-to-mass identification; neither does.
- **Not** a thresholded notion of non-degeneracy and not a fitted phase. The
  condition is exact pairwise inequality, and the T3 sector is open.
- **Not** a universal exclusion of the per-real-mode endpoint. The theorem is
  the branch dichotomy: it is incompatible with `ND_3` on `B_plus`, while on
  `B_abs` it supports `ND_3` but does not determine `Q`.
- **Not** a claim beyond the K-tied three-member circulant and the two landed
  equipartition endpoints. Other spectral carriers, record maps, or endpoint
  families are outside scope.
- **Not** a premise promotion, registry edit, audit verdict, or effective-
  status change. Independent audit remains required.

## Reprove-and-cite ledger

- **Reproven here (runner, exact SymPy):** phase permutation under
  `theta -> theta+2pi/3`; the phase-free trace and squared-trace identities;
  conditional `Q = (1+2r)/3`; the reduced-sector cosine ordering and exact
  minimum envelope; its monotonicity and the best/worst minima; the complete
  `(a,|b|)` and `r` positivity-window classification; the exact boundary
  half-width and its endpoints; the `r = 0` special case; the `pi/12`
  half-width and zero boundary at `r = 1/2`; the pairwise-difference product
  and exact degeneracy locus; `Q = 2/3` at `r = 1/2`; the zero-width
  `(3a,0,0)` spectrum and registered doublet degeneracy at `r = 1`; the
  `theta = pi/6` sign-branch spectrum, squared pattern, and exact `Q`; the
  second non-degenerate `theta = pi/12` sign-branch point and its different
  exact `Q`.
- **Cited at declared grade:** block 9's two equipartition cells and tied
  spectrum; block 10's tied-section result, named `ND_3` element, and
  surviving dial residual; the minimal Record/Qualification boundary; the
  R-D anatomy note's proposed status, conditional bookkeeping, exact flow
  anatomy, and unresolved statistics atom.
- **Declared here, not cited as landed:** `B_sqrt`, `B_plus`, and `B_abs`.

## Verification

```bash
python3 scripts/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.py
python3 scripts/precompute_audit_runners.py --push-mode none --force \
  --runners scripts/frontier_equipartition_endpoint_registration_asymmetry_2026_07_12.py
```

Expected: 23 numbered `[PASS]` lines, four declared-open `RESIDUAL` lines,
then `TOTAL: PASS=23 FAIL=0` and the conditional verdict. Exit code 0 iff
`FAIL=0`.

**Independent audit required.** This note asserts no effective-status change.
