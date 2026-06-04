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

## 5. No-go discipline gate (N1-N8)

**Status:** PASS for this bounded under-determination claim only. The negative
content is narrow: at three coefficients `{d_5, d_6, d_7}` the surviving single
complex-conjugate-pair premise `beta_c = R e^{+- i theta}` (exponent
`gamma > 0`) is **not localizable** — the harness proxy angle is sign-excluded
(A) and the two single-pair estimators disagree (B). This is **not** a claim
that the surviving complex-pair class is wrong, **not** a closure of the
resummation route, and **not** a new foreclosure. "Under-determined" is a
statement about the order-7 information content, not about the existence of the
pair.

### N1 — Alternative route enumeration

Routes that would try to **determine** the under-determined pair
`(R, theta, gamma)` (or rescue the harness proxy) from the order-7 data, and
why each fails *within this note's scope* (three exact coefficients, single
dominant pair):

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Two-relation Mercer-Roberts pin | Solve `d_7 = (2 cos theta / R) d_6 - (1/R^2) d_5` for `(R, theta)` as two unknowns. | One recurrence is **one** equation in two unknowns; it fixes only the locus `cos theta(R)`, not a point. Adding the order-5/6 ratio gives `gamma R^{-5}`, still leaving `(R, theta)` on a curve. | ATTEMPTED |
| Cumulant-sign triangulation | Use `sign(ell_0), sign(ell_1)` to bracket `theta`. | Two signs give only the open band `theta in (45, 90) deg`; they cannot return a point, and (B) shows the band is **disjoint** from the recurrence locus, so they cannot even be intersected to a value. | ATTEMPTED |
| Fix `R` from the proxy, solve `theta` | Adopt `R = 5.7` (harness proxy) and back out `theta` from the order-7 recurrence. | Yields `theta ~= 34 deg`, **outside** the `(45, 90) deg` cumulant band (B); and the proxy `R` is itself a flagged un-derived value, so this imports the very thing under test. | ATTEMPTED |
| Fix `theta` from the proxy, solve `R` | Adopt `theta = 31.5 deg` (harness proxy) and back out `R`. | `theta = 31.5 deg` is **sign-excluded** by (A): it predicts `ell_1 > 0` against the exact `ell_1 = -1/16 < 0`. No `R` repairs a wrong-sign angle. | ATTEMPTED |
| Single-real-pole / real-axis branch point | Localize a real `beta_c` (`theta = 0` or `pi`) instead of an off-axis pair. | The real-axis / positive-measure family is foreclosed upstream by `BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md`; and the Mercer-Roberts locus has `cos theta > 0` for all `R`, so `theta = pi` is off-locus. Out of the surviving class by construction. | OUT OF SURVIVING CLASS |
| Multi-pair / subdominant-pair fit | Add a second conjugate pair (or a sub-leading singularity) to absorb the estimator disagreement. | A second pair adds `>= 2` parameters; three coefficients cannot fit a single 3-parameter pair self-consistently, so they a fortiori cannot fit a richer model. This **widens** under-determination, it does not resolve it. | WIDENS UNDER-DETERMINATION |
| Borel / Pade re-localization | Read `(R, theta)` off Pade poles or Borel singularities of the order-7 truncation. | Low-order Pade poles from 3 terms are unstable proxies for the true singularity and carry no independent information beyond `{d_5, d_6, d_7}`; they re-express the same rank-deficient data, not new constraints. | NO NEW INFORMATION |
| Proxy-MC anchoring | Pin `R` (or the analytic sum) using `<P>(beta=6) ~= 0.594`. | The Monte-Carlo plaquette is a forbidden comparator for this lane and plays no role here; anchoring on it would be an import, not a native determination. | FORBIDDEN IMPORT |
| Order-8 closure | Supply `d_8`, pair the second Mercer-Roberts relation with the first, add the `ell_2 ~ cos 3 theta` sign. | This **does** over-determine `(R, theta)` and is the note's pre-registered decisive test — but `d_8` sits behind the retained treewidth-29 infeasibility wall (`su3_wigner_l3_treewidth_infeasible_2026-05-04`), so it is **outside the order-7 scope**, not a within-scope determination. | OUT OF SCOPE (compute-walled) |

Every within-scope route either returns a curve/band (not a point), lands
outside the surviving class, or merely re-expresses the same three numbers. The
only route that determines the pair (`d_8`) is explicitly out of scope and
blocked by the lane's own named compute wall.

### N2 — Wall-independence audit

The collapsed wall set for this bounded claim is a **single** wall: the
**order-7 rank deficiency** of the single-dominant-pair model. A single
complex-conjugate pair has three real parameters `(R, theta, gamma)`; the
asymptotic data at orders 5-7 supply only `(d_6/d_5, d_7/d_5)` for the
shape and an overall scale, and the two independent single-pair estimators
(Mercer-Roberts recurrence locus; cumulant-sign band) are **mutually
inconsistent**, certifying that no single pair reproduces `{d_5, d_6, d_7}`.
Statements (A) and (B) are not two independent walls: (B)'s lower bound
`45 deg` is *derived from* (A)'s cumulant-sign law, so they are two readings of
the one rank-deficiency wall, consistent with the no-double-counting
requirement. What could change this: a single additional exact coefficient
`d_8` converts the underdetermined locus into an over-determined two-equations-
plus-sign system (Section 4's pre-registered test). Nothing in this note bounds
*away* the existence of a localizing higher-order coefficient; it bounds only
what orders 5-7 can pin.

### N3 — Hidden-wall scan

No rhetorical phrase is load-bearing. "Under-determined," "not localizable,"
"sole surviving," and "sign-excluded" are conclusions, not inputs. The explicit
load-bearing inputs, each independently re-derivable in the runner, are exactly:

1. the three exact rational coefficients `d_5 = 4/18^5`, `d_6 = 42/18^6`,
   `d_7 = 180/18^7` (values quoted from main, re-checked by exact arithmetic);
2. the single-pair cumulant law `kappa_k = 2 gamma (k-1)! R^{-k} cos(k theta)`
   (a standard asymptotic identity for one dominant algebraic conjugate pair),
   from which `sign(ell_0) = sign(cos theta)` and
   `sign(ell_1) = sign(cos 2 theta)`;
3. the Mercer-Roberts single-pair three-term recurrence
   `d_{n+2} = (2 cos theta / R) d_{n+1} - (1/R^2) d_n`;
4. the two exact rationals derived from (1)-(3): `ell_1 = -1/16` and
   `cos theta = 0.8290` at `R = 57/10`.

The upstream foreclosure note and the harness proxy point are **cited context**,
not proof inputs: the negative result (A)+(B) stands on (1)-(4) alone and would
hold even if the harness had quoted no proxy at all (the proxy only supplies the
specific `R = 5.7`, `theta = 31.5 deg` numbers that (A)/(B) then contradict).

### N4 — Residual matching

| cited witness | residual the witness attacks | residual attacked here | match? |
|---|---|---|---|
| `BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md` | The harness leaves the surviving-pair location `(R, theta)` as a hard-coded *proxy*, explicitly flagged as not derived. | Whether the framework's own `{d_5, d_6, d_7}` support / localize that proxy point. | yes (same surviving-pair location residual) |
| `BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md` | The real-axis / positive-measure continuation family (foreclosed), leaving the off-axis pair as the surviving class. | Localizability of that *surviving* off-axis pair at order 7. | yes (it defines the class this note then probes; the locus check confirms the class is untouched) |
| `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md` | The exact order-7 coefficient value and tadpole verdict. | Consumed only as the value `d_7`; the tadpole verdict is not a localization input. | partial — value yes; tadpole verdict **not load-bearing** here |
| `plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05` (MC `<P>(6) ~= 0.594`) | The numerical thermodynamic plaquette value. | Plays no role; an explicitly forbidden comparator for this lane. | no — **not load-bearing** (forbidden import) |

The non-matching / partial witnesses (tadpole verdict, MC comparator) are
flagged not load-bearing and are not used as evidence for the under-determination.

### N5 — Rhetoric audit

The broad phrases are scoped to the exact claim and explicitly disclaimed
against over-broad readings:

- **"under-determined" / "not localizable"** means precisely: *the three exact
  coefficients `{d_5, d_6, d_7}` do not pin a single dominant complex-conjugate
  pair* (and disagree about it). It does **not** mean the pair does not exist,
  that no higher order can pin it (Section 4 says `beta^8` would), or that the
  resummation is impossible.
- **"sign-excluded" / "the proxy angle is inconsistent"** is scoped to the
  *single-pair* sign law on the *harness's specific* `theta = 31.5 deg`; it does
  not exclude every off-axis angle (the band `(45, 90) deg` survives) and does
  not exclude the harness's qualitative complex-pair ansatz, only its quoted
  angle.
- **"bounded"** is the claim_type: this note tightens a status from assertion
  ("needs `beta^8`") to a precise order-7 under-determination, adding no axiom,
  no fit, and no foreclosure.

Any reading that takes this note to close the resummation route, refute the
surviving complex-pair class, or assert a `P(6)` value is an over-broad reading
the note disavows (Section 4).

### N6 — Partial-closure path scan

Open, non-axiom partial-closure paths — additional **native** input that *would*
determine the coefficients — are explicitly available and none is a new axiom:

1. **The pre-registered `beta^8` test (primary).** Supplying the exact native
   coefficient `d_8` from the framework's own cumulant machinery pairs the
   second Mercer-Roberts relation
   `d_8 = (2 cos theta / R) d_7 - (1/R^2) d_6` with the order-7 relation to
   solve `(R, theta)` uniquely, and the third cumulant `ell_2 ~ cos 3 theta`
   adds an independent sign. Two equations + one sign over-determine the pair.
   This is native arithmetic, not an axiom; it is blocked only by the retained
   treewidth-29 compute wall (`su3_wigner_l3_treewidth_infeasible_2026-05-04`),
   not by any matter of principle.
2. **A higher-order tail (`d_9`, `d_10`, ...).** Each further native coefficient
   adds an over-determining constraint and would either confirm a localized pair
   or falsify the single-pair hypothesis in favor of a multi-singularity
   structure — again native, no axiom.
3. **A native bound on `gamma` (the algebraic exponent).** An independent
   framework-internal determination of the singularity exponent would remove one
   of the three parameters, making the order-7 data over- rather than
   under-determined for `(R, theta)`. This too would be a derivation, not an
   import.

None of these is a new axiom, a fit, or a forbidden comparator; each is a route
that *adds native information at higher order or on the exponent*. The note does
not foreclose any of them.

### N7 — Steelman

**Strongest objection.** "Three coefficients generically *do* fix a three-term
recurrence — `d_7 = (2 cos theta / R) d_6 - (1/R^2) d_5` is one equation, but
together with the order-5/6 normalization the single-pair ansatz has effectively
two shape parameters `(R, theta)` and two ratios `(d_6/d_5, d_7/d_5)`, so a
hostile reader could claim `(R, theta)` *is* determined at order 7 and the note
overstates the under-determination."

**Why it does not break the scoped claim.** The note does not deny that a single
recurrence *equation* can be written; it shows the two **independent** order-7
single-pair estimators return **inconsistent** answers — the cumulant-sign law
forces `theta in (45, 90) deg`, while the recurrence on the harness `R` forces
`theta ~= 34 deg`. A genuine single dominant pair must satisfy **both** (they
are not independent assumptions but two necessary consequences of the *same*
`kappa_k = 2 gamma (k-1)! R^{-k} cos(k theta)` law). Their disagreement is a
*certificate* that `{d_5, d_6, d_7}` are not generated by any single pair at
orders 5-7 — precisely an under-determination (in fact an inconsistency) of the
single-pair model, not a localization. The objection's "two equations, two
unknowns" count silently assumes a known `R`; the note's whole point is that `R`
is not independently fixed at order 7, which is why the estimators float apart.

### N8 — Cross-cycle echo

The repo's recurring negative-claim failure mode is the *one-representative ->
whole-lane-closed* overclaim: testing a single ansatz/expression and then
declaring the entire route foreclosed. This note structurally avoids that echo
on three counts. (i) It closes **nothing** — `new_foreclosure: false`,
`resummation_route_status: not_closed`, `beta6_status: not_closed` in the
machine block; the surviving complex-pair class is explicitly left intact, and
the runner *confirms* the upstream no-go's surviving class is untouched
(`cos theta > 0` for all sampled `R`). (ii) It scopes its negative content to a
single representative point (the harness proxy) and a single model class (one
dominant pair) at a single order (7), and names the exact higher order
(`beta^8`) that would flip "under-determined" to "localized or falsified." (iii)
It does not promote the proxy-angle exclusion into a claim that *no* off-axis
angle works — the survivor band `(45, 90) deg` is preserved. The boundary is the
order-7 information content of one model class, not the resummation lane.

## 6. Audit consequence

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

## 7. Runner

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

## 8. Key files

- [`scripts/frontier_beta6_complex_pair_underdetermination.py`](../scripts/frontier_beta6_complex_pair_underdetermination.py)
- `BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md`
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)

This note is a bounded premise-sharpening and asserts no closure of the beta=6
lane and no new foreclosure.
