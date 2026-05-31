# Beta=6 SU(3) Plaquette Complex-Pair Premise Under-Determination at Three Coefficients

**Date:** 2026-05-30
**Claim type:** bounded
**Status:** premise-sharpening proposal. This note adds no axiom, no fitted
input, and no audit verdict. It neither proves nor forecloses the surviving
complex-conjugate-pair analyticity premise; it records that three exact
coefficients do not localize it.
**Status authority:** independent audit lane only. This source note does not
quote, set, or predict an audit outcome for any cited claim_id.
**Primary runner:** [`scripts/frontier_beta6_complex_pair_underdetermination.py`](../scripts/frontier_beta6_complex_pair_underdetermination.py)
**Closure outcome:** none. This is a premise-sharpening of the surviving
resummation branch. It is NOT a closure of the resummation route or of beta=6,
and it does NOT add a new foreclosure.

## 0. Object being scoped

The infinite-volume connected plaquette series at the framework point is

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n.
```

The moment-positivity no-go
`BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md`
(a sibling review-loop proposal, cited by name pending its landing on main, so
no citation-graph edge is asserted here) foreclosed the positive-measure /
real-axis-branch-cut continuation family and left the **off-axis
complex-conjugate-pair class** as the sole surviving resummation candidate. The resummation test harness
[`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
pins that surviving class with a **hard-coded proxy singularity point**

```text
R_proxy = 5.7,   theta_proxy = 0.55 rad = 31.5 deg,
```

flagged in that harness as a controlled proxy, not a derived value. This note
asks the narrow question the harness leaves open: do the framework's **own**
exact coefficients support that proxy point, or localize the surviving pair at
all? The answer, in exact arithmetic, is no on both counts.

This note keeps the lane's `A_min` and forbidden-import list fixed. No fitted
`beta_eff`, perturbative beta-function derivation, lattice Monte-Carlo
plaquette, or PDG comparator is used; the Monte-Carlo comparator
`<P>(beta=6) ~= 0.594`
(`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`) plays no role here.

## 1. Inputs (exact, on-main)

The three lowest exact connected-cumulant coefficients of `Delta(beta)` are
taken verbatim from main (same values as the moment-positivity no-go):

| coefficient | exact value | source note (claim_id) |
|---|---|---|
| `d_5` | `1/472392 = 4/18^5` | [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) (`gauge_vacuum_plaquette_mixed_cumulant_audit_note`) |
| `d_6` | `7/5668704 = 42/18^6` | [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md) (`beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30`) |
| `d_7` | `5/17006112 = 180/18^7` | [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md) (`beta6_plaquette_d7_coefficient_and_tadpole_verdict_bounded_note_2026-05-30`) |

Status authority for each cited claim_id is the independent audit lane
(`rows[<claim_id>]['effective_status']` in `docs/audit/data/audit_ledger.json`);
this note quotes the **values** only. The exact values are independently
re-checked by exact rational arithmetic in the runner.

## 2. The two exact cumulants

Write `Delta(beta) = d_5 beta^5 (1 + a_1 beta + a_2 beta^2 + ...)` with
`a_1 = d_6/d_5`, `a_2 = d_7/d_5`. The first two cumulants of the normalized
log-series `log( Delta(beta) / (d_5 beta^5) )` are exact rationals:

```text
ell_0 = kappa_1 = a_1               = d_6/d_5                  = 7/12,
ell_1 = kappa_2 = 2 a_2 - a_1^2     = 2(d_7/d_5) - (d_6/d_5)^2 = -1/16.
```

(`d_7/d_5 = 5/36`; `2*(5/36) - (7/12)^2 = 40/144 - 49/144 = -9/144 = -1/16`.
Both reproduced by a sympy `log`-series expansion in the runner.)

For a **single dominant complex-conjugate pair** `beta_c = R e^{+- i theta}`
with algebraic exponent `gamma > 0`, the exact cumulants are

```text
kappa_k = 2 gamma (k-1)! R^{-k} cos(k theta),
```

so `sign(ell_0) = sign(cos theta)` and `sign(ell_1) = sign(cos 2 theta)`. These
signs depend only on `theta` (since `gamma, R > 0`), which is what makes the
two statements below robust.

## 3. Statement (premise-sharpening, two exact consequences)

> **(A) The harness proxy angle is excluded by an exact sign, independently of
> `R` and `gamma`.** `ell_1 = -1/16 < 0` forces `cos 2 theta < 0`, i.e.
> `theta > 45 deg` (with `ell_0 > 0` giving `cos theta > 0`, i.e.
> `theta < 90 deg`, the single-pair cumulant band is `theta in (45, 90) deg`).
> The harness proxy `theta_proxy = 31.5 deg` gives `cos(2 * 31.5 deg) > 0`,
> which **predicts `ell_1 > 0`** — the opposite sign to the exact `ell_1 < 0`.
> The proxy angle is therefore inconsistent with the framework's own exact
> coefficients.
>
> **(B) The surviving pair is not localizable at three coefficients.** The
> Mercer-Roberts single-pair recurrence
> `d_7 = (2 cos theta / R) d_6 - (1/R^2) d_5`, evaluated on the harness radius
> `R = 5.7`, forces `theta ~= 34 deg` — below `45 deg`, hence **outside** the
> cumulant-sign band `(45, 90) deg` of (A). The two single-pair estimators are
> mutually inconsistent at three coefficients, so `{d_5, d_6, d_7}` do not even
> obey a single-pair recurrence at orders 5-7: the pair is not localizable
> (let alone confirmed) from three coefficients.

**Proof.** (A) is the sign of one exact rational, `ell_1 = -1/16 < 0`, against
`cos(2 theta_proxy) = cos(1.10 rad) = +0.45 > 0`; the single-pair sign law
`sign(ell_1) = sign(cos 2 theta)` is `gamma`- and `R`-independent. (B) is the
exact-rational value `cos theta = R (d_7 + d_5/R^2) / (2 d_6) = 0.8290` at
`R = 57/10`, giving `theta = 34.0 deg < 45 deg`; the cumulant band lower bound
`45 deg` is from (A). Both are reproduced in exact `Fraction`/`sympy` arithmetic
by the runner. QED.

## 4. Precise scope (what survives — honesty, non-negotiable)

- **This neither proves nor forecloses the surviving complex-pair premise.** The
  off-axis complex-pair class remains the sole surviving resummation candidate
  exactly as the moment-positivity no-go left it. (Indeed the Mercer-Roberts
  locus has `cos theta > 0` for **all** `R > 0`, so a real-negative-axis
  singularity at `theta = pi` is *not* on the locus — these three coefficients
  do **not** contradict the existing no-go's surviving-class statement, and no
  scope-correction to that note is proposed.)
- **What is tightened.** The surviving premise is real but **under-determined**
  at the available order: the harness's specific proxy point `(R, theta) =
  (5.7, 31.5 deg)` is not data-supported (its `theta` is sign-excluded by (A)),
  and no single complex pair is consistent with all three coefficients (B). The
  "needs `beta^8`" status of the lane is thereby upgraded from an assertion to a
  precise under-determination statement.
- **No closure is claimed.** This note asserts no `P(6)`, posits no closed
  boosting form, reuses no target-fit exponent, and closes neither the
  resummation route nor beta=6.

**Pre-registered decisive test (`beta^8`).** When the order-8 connected
coefficient `d_8` becomes available, the second Mercer-Roberts relation
`d_8 = (2 cos theta / R) d_7 - (1/R^2) d_6` pairs with the order-7 relation to
pin `(R, theta)` uniquely, and the third cumulant `ell_2 = kappa_3 =
4 gamma R^{-3} cos 3 theta` supplies an independent sign constraint
(`~ cos 3 theta`). Two relations in two unknowns plus a sign over-determine the
pair: this is the test that converts "under-determined" into either a localized
pair or a falsification. `d_8` sits at/behind the retained treewidth-29
infeasibility wall (`su3_wigner_l3_treewidth_infeasible_2026-05-04`), so the
decisive test remains blocked by the same compute wall the lane already names.

## 5. Audit consequence

This note proposes a bounded premise-sharpening for independent audit-lane
review. Review-loop does not apply a verdict. The load-bearing content is the
sign of one exact rational cumulant (`ell_1 = -1/16`) and one exact rational
recurrence value (`cos theta = 0.8290` at `R = 5.7`), reproduced by the
companion runner.

```yaml
claim: beta6_plaquette_complex_pair_underdetermination
closure_proposal: none
result: proxy_angle_sign_excluded_and_single_pair_not_localizable_at_three_coefficients
surviving_class: off_axis_complex_conjugate_pair_continuation   # unchanged
new_foreclosure: false
resummation_route_status: not_closed
beta6_status: not_closed
forbidden_imports_used: false
decisive_test: beta8_second_mercer_roberts_relation_plus_ell2_sign  # blocked by treewidth-29 wall
audit_status_authority: independent audit lane only
```

## 6. Runner

```bash
python3 scripts/frontier_beta6_complex_pair_underdetermination.py
```

Expected summary:

```text
SCORECARD: PASS=19 FAIL=0
```

The runner computes `ell_0 = 7/12` and `ell_1 = -1/16` in exact `Fraction`
arithmetic (and re-derives both from a `sympy` `log`-series), certifies the
proxy-angle sign exclusion (A), certifies the Mercer-Roberts locus value
`theta ~= 34 deg < 45 deg` and the estimator disagreement (B), confirms the
locus stays at `cos theta > 0` for all sampled `R > 0` (so the existing no-go's
surviving class is untouched), and records the well-posedness of the
pre-registered `beta^8` test.

## 7. Key files

- [`scripts/frontier_beta6_complex_pair_underdetermination.py`](../scripts/frontier_beta6_complex_pair_underdetermination.py)
- `BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md`
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)

This note is a bounded premise-sharpening and asserts no closure of the beta=6
lane and no new foreclosure.
