# Beta=6 SU(3) Plaquette Connected-Cumulant Moment-Positivity No-Go

**Date:** 2026-05-30
**Claim type:** no_go
**Status:** formal no-go proposal. This note adds no axiom, no fitted input,
and no audit verdict. The independent audit lane sets audit and effective
status.
**Status authority:** independent audit lane only. This source note does not
quote, set, or predict an audit outcome for any cited claim_id.
**Primary runner:** [`scripts/frontier_beta6_cumulant_moment_positivity.py`](../scripts/frontier_beta6_cumulant_moment_positivity.py)
**Closure outcome:** B, formal no-go. It retires ONE branch of the resummation
harness's unproven analyticity premise (the positive-measure / real-axis
branch-cut branch) as a negative theorem. It is NOT a closure of the
resummation route or of beta=6.

## 0. Object being scoped

The infinite-volume connected plaquette series at the framework point is

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n,
   P_full  = <(1/3) Re Tr U_{p0}>_Wilson,
   P_1plaq = the single-plaquette-in-isolation expectation.
```

The resummation test harness
[`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
rests on an **unproven analyticity premise** for `Delta(beta)`: that its
dominant singularity is an off-axis complex-conjugate pair near
`|beta_c| ~ 5.7` with no real branch point at `beta_r < 6` (research map
[`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md),
Section 4b). That premise has a real-axis sibling branch — the family in which
`Delta(beta)` is the Laplace/Stieltjes transform of a **positive** spectral
measure on the real axis (a real branch cut / a sum of real-axis poles with
positive residues). This note forecloses that sibling branch, and only that
branch, using the framework's **own** exact connected-cumulant coefficients.

This note keeps the lane's `A_min` and forbidden-import list fixed. No fitted
`beta_eff`, perturbative beta-function derivation, lattice Monte-Carlo
plaquette, or PDG comparator is used; the Monte-Carlo comparator
`<P>(beta=6) ~= 0.594`
(`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`) plays no role here.

## 1. Inputs (exact, on-main)

The three lowest exact connected-cumulant coefficients of `Delta(beta)` are
taken verbatim from main:

| coefficient | exact value | source note (claim_id) |
|---|---|---|
| `d_5` | `1/472392 = 4/18^5` | [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) (`gauge_vacuum_plaquette_mixed_cumulant_audit_note`) |
| `d_6` | `7/5668704 = 7/(3*18^5)` | [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md) (`beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30`) |
| `d_7` | `5/17006112 = 5/(9*18^5)` | [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md) (`beta6_plaquette_d7_coefficient_and_tadpole_verdict_bounded_note_2026-05-30`) |

Status authority for each cited claim_id is the independent audit lane
(`rows[<claim_id>]['effective_status']` in
`docs/audit/data/audit_ledger.json`); this note quotes the **values** only,
not the audit statuses. (`d_5`'s source carried `retained` on 2026-05-30; the
`d_6`/`d_7` source notes are review-loop proposals whose status the audit lane
sets.) The two new coefficient notes were verified to be on main before this
note was drafted; these exact values were independently re-checked by exact
rational arithmetic in the runner.

## 2. Theorem (the no-go)

> **Claim.** The window `{d_5, d_6, d_7}` of the framework's own connected
> plaquette cumulants is **not** a Hamburger (hence not a Stieltjes) moment
> sequence. Consequently `Delta(beta) = sum_k d_k beta^k` is **not** the
> Laplace/Stieltjes transform of a positive measure on the real axis: the
> positive-measure / real-axis-branch-cut analytic-continuation family for the
> beta=6 plaquette resummation is foreclosed.

**Proof (exact-rational).** A necessary condition for any real sequence
`{c_k}` to be a Hamburger moment sequence `c_k = integral t^k d mu(t)` with
`mu >= 0` is that every Hankel matrix `[c_{i+j}]` be positive semidefinite, so
every principal minor is `>= 0` (Hamburger's theorem; Stieltjes positivity is
strictly stronger and implies the Hamburger condition). Take the centered 2x2
Hankel window built from the three coefficients,

```text
H = [[d_5, d_6],
     [d_6, d_7]],      det H = d_5 d_7 - d_6^2.
```

In exact rationals,

```text
d_5 d_7 - d_6^2 = (1/472392)(5/17006112) - (7/5668704)^2
               = -29 / 32134205039616
               < 0.
```

A single **negative** 2x2 minor falsifies positive semidefiniteness of `H`,
so `{d_5, d_6, d_7}` violates the Hamburger necessary condition and cannot be
the moment window of any positive real-axis measure. A function whose Taylor
coefficients fail the Hamburger positivity condition is not a Laplace/Stieltjes
transform of a positive measure on the real axis. QED.

**Integer (per-shell) witness.** Because `d_5 = 4/18^5` (four closed cube
shells through the marked plaquette, each carrying the single-plaquette SU(3)
character normalization `18`), the geometric per-shell rescaling
`m_n := d_n * 18^n` clears denominators to the clean integers

```text
m_5 = d_5 * 18^5 = 4,
m_6 = d_6 * 18^6 = 42,
m_7 = d_7 * 18^7 = 180.
```

The weights `s_n = 18^n` are **geometric** (`s_5 s_7 = s_6^2 = 18^12`), so the
diagonal congruence preserves the sign of the 2x2 minor exactly:

```text
m_5 m_7 - m_6^2 = 4 * 180 - 42^2 = -1044 = 18^12 (d_5 d_7 - d_6^2) < 0.
```

The integer witness `-1044` carries the identical strict negativity; the
no-go does not depend on any floating-point evaluation.

## 3. Precise scope (what survives — honesty, non-negotiable)

This no-go forecloses **only** the positive-measure / real-axis-branch-cut
continuation family. It does **not** refute the resummation harness's
complex-conjugate-pair premise:

- **The off-axis complex-pair class survives.** A complex-conjugate pair of
  singularities is **generically non-Stieltjes** — its associated coefficient
  sequence is not a positive-measure moment sequence — so a negative Hankel
  minor is exactly what that class predicts and is **consistent** with it. The
  off-axis complex-pair continuation candidate (the harness's
  `[n/n]` d-log-Pade route, research map Route 1) is therefore **not** touched
  by this result.
- **No closure is claimed.** This note does not assert `P(6)`, does not posit a
  closed boosting form, does not reuse any target-fit exponent, and does not
  close the resummation route or beta=6.

**Consequence for the program.** The resummation harness's unproven analyticity
premise had two branches; this note retires one of them. The surviving
resummation long-shot is now narrowed to the **off-axis complex-conjugate-pair
class alone**. A genuine closure along that surviving branch still requires the
independent dynamical input the lane already lacks (an analytic proof that
`Delta(beta)` is of the conjectured complex-pair class, plus enough exact
high-order connected coefficients to drive the predictive `d-log-Pade` test —
both blocked by the retained treewidth-29 infeasibility wall
`su3_wigner_l3_treewidth_infeasible_2026-05-04`).

This is complementary to, and independent of, the order-7 single-ratio
geometric/tadpole falsification in
[`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
(`d_7/d_6 = 5/21 != d_6/d_5 = 7/12`): that result rules out a single real
geometric tail; this result rules out the entire positive-measure / real-axis
branch-cut class. Together they leave the off-axis complex-pair class as the
sole surviving resummation candidate.

## 4. Audit consequence

This note proposes a no-go claim for independent audit-lane review. Review-loop
does not apply the verdict. The audit ledger row should seed with
`claim_type = no_go` and remain unaudited until the audit lane ratifies it. The
load-bearing content is the exact-rational sign of a 2x2 Hankel minor of three
on-main coefficients, reproduced by the companion runner.

```yaml
claim: beta6_plaquette_cumulant_moment_positivity_no_go
closure_proposal: no_go
foreclosed_class: positive_measure_real_axis_branch_cut_continuation
surviving_class: off_axis_complex_conjugate_pair_continuation
resummation_route_status: not_closed
beta6_status: not_closed
forbidden_imports_used: false
audit_status_authority: independent audit lane only
```

## No-go discipline gate (N1-N8)

**Status:** PASS for the narrow positive-measure / real-axis-branch-cut
foreclosure only. The claim being closed is **not** a closure of the
beta=6 plaquette lane, **not** a refutation of the off-axis
complex-conjugate-pair resummation premise, and **not** an assertion about
`P(6)`. It is the single exact-rational statement that the framework's own
window `{d_5, d_6, d_7}` is not a Hamburger (hence not a Stieltjes) moment
sequence, so `Delta(beta)` is not the Laplace/Stieltjes transform of a
positive measure on the real axis.

### N1 - Alternative route enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Direct positive-measure fit | Exhibit a positive `mu >= 0` on the real axis with `d_k = integral t^k d mu(t)` reproducing `{d_5, d_6, d_7}`. | Hamburger's theorem makes Hankel-PSD necessary; the 2x2 minor `d_5 d_7 - d_6^2 = -29/32134205039616 < 0` falsifies PSD, so no such `mu` exists. | ATTEMPTED |
| Rescale denominators to dodge the sign | Clear the `18^n` denominators (per-shell integers `m_n`) hoping the rescaled window is a moment sequence. | The weights `s_n = 18^n` are geometric (`s_5 s_7 = s_6^2 = 18^12`); a geometric diagonal congruence preserves the minor sign exactly: `m_5 m_7 - m_6^2 = -1044 < 0`. | ATTEMPTED |
| Shift/recentre the window | Use a non-centred Hankel block (e.g. start at `d_5` vs a shifted origin) to obtain a PSD minor. | A genuine Hamburger sequence requires **every** principal minor `>= 0`; finding one negative 2x2 minor anywhere in `[c_{i+j}]` already falsifies positivity, and translation of the moment variable cannot repair a strictly negative determinant. | ATTEMPTED |
| Stieltjes (half-line) instead of Hamburger | Argue the measure lives on `[0, infinity)` so a weaker condition applies. | Stieltjes positivity is **strictly stronger** than Hamburger; if the Hamburger condition already fails, the Stieltjes condition fails a fortiori. | ATTEMPTED |
| Sign-flip / alternating reinterpretation | Read `Delta(-beta)` or `(-1)^n d_n` as the moment sequence to flip the offending sign. | The 2x2 minor is invariant under `d_n -> (-1)^n d_n` (it multiplies `d_5, d_7` by `(-1)` and `d_6` by `+1`, leaving `d_5 d_7 - d_6^2` unchanged); the negativity is sign-convention-robust. | ATTEMPTED |
| Off-axis complex-conjugate-pair continuation | Continue `Delta(beta)` via a complex-pair singularity (d-log-Pade, research-map Route 1). | This class is **generically non-Stieltjes**: a negative Hankel minor is exactly what it predicts, so it is **consistent** with — not refuted by — this result; left open as the surviving candidate, not closed here. | NOT ATTEMPTED (out of scope) |

### N2 - Wall-independence audit

The collapsed wall set for this no-go has **one** wall: the strict
negativity of the single 2x2 Hankel minor `d_5 d_7 - d_6^2 < 0` of the
framework's own exact coefficients. The integer-witness restatement
(`m_5 m_7 - m_6^2 = -1044`) is **not** an independent wall — it is the same
determinant pushed through a sign-preserving geometric congruence, supplied
as a floating-point-free witness of the identical fact. What could change
the verdict: a corrected exact value for any of `d_5, d_6, d_7` on main that
flipped the minor's sign. None of the three coefficient values is asserted
here to be audit-final; this note quotes them as on-main inputs and the
audit lane retains authority over their statuses. If a coefficient were
revised, this no-go would have to be recomputed — but within the quoted
values the wall is a single exact inequality, not a stack of independent
walls.

### N3 - Hidden-wall scan

No rhetorical phrase ("foreclosed", "no-go", "positive measure",
"branch cut") is used as a hidden retained input. The explicit
load-bearing inputs are exactly three, and nothing else:

1. The three exact rational coefficients `d_5 = 1/472392`,
   `d_6 = 7/5668704`, `d_7 = 5/17006112` (quoted by **value** from their
   on-main source notes; re-checked by exact rational arithmetic in the
   runner).
2. Hamburger's theorem: a real sequence is a moment sequence of a positive
   measure **only if** every Hankel principal minor is `>= 0` (textbook
   moment-problem fact, not a framework axiom).
3. The elementary inclusion that Stieltjes positivity implies the Hamburger
   condition (so Hamburger failure forecloses the half-line case too).

The phrase "the framework's own coefficients" is descriptive of input
provenance, not a load-bearing dynamical premise; the treewidth-29
infeasibility wall is mentioned only to characterise the surviving branch's
separate blocker and is **not** used to prove this no-go.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md` (`d_7/d_6 = 5/21 != d_6/d_5 = 7/12`) | A single **real geometric** tail (one-ratio progression) for `Delta(beta)`. | The entire **positive-measure / real-axis branch-cut** class (all positive `mu` on the real axis, not just geometric tails). | partial — strictly broader here; the geometric-tail falsification is a special case, used as a **complementary** companion, not as a load-bearing premise of this Hankel result. |
| `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md` (`d_5`) | (positive coefficient source) | Supplies the exact `d_5` value only. | value-only input, not a refutation witness — not load-bearing as a no-go residual. |
| `BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md` (analyticity premise, two branches) | The premise's positive-measure / real-axis sibling branch. | Exactly that sibling branch (and **only** it). | yes — the foreclosed object is precisely one of the harness's two enumerated branches. |

Non-matching or value-only witnesses are explicitly marked not load-bearing
for the no-go.

### N5 - Rhetoric audit

The broad words in this note are scoped as follows. "Foreclosed" /
"no-go" attach **only** to the positive-measure / real-axis-branch-cut
continuation family — not to beta=6, not to the resummation route, not to
the off-axis complex-pair class. "Not a moment sequence" / "positivity
violated" refer to the **Hamburger Hankel-PSD** condition on the specific
window `{d_5, d_6, d_7}`, not to any statement that `Delta(beta)` is
ill-defined, non-analytic, or sign-indefinite as a series. An over-broad
reading — "the beta=6 plaquette has no analytic continuation" or "the
resummation program is dead" — is **disclaimed**: a complex-conjugate-pair
continuation is generically non-Stieltjes and remains the live surviving
candidate. The result says one branch of an unproven premise is retired,
nothing more.

### N6 - Partial-closure path scan

Non-axiom partial-closure paths that remain open after this note (none is a
new axiom or import):

- Prove `Delta(beta)` is of the off-axis complex-conjugate-pair class
  analytically (would re-route, not contradict, this result).
- Extend the exact connected-coefficient window beyond `d_7` to drive the
  predictive d-log-Pade test on the surviving branch (currently blocked by
  the retained treewidth-29 infeasibility wall
  `su3_wigner_l3_treewidth_infeasible_2026-05-04` — an existing wall, not a
  new axiom).
- Supply the independent dynamical input the lane already lacks for a
  genuine beta=6 closure.

Each path is a continuation of existing work within the lane's fixed
`A_min` and forbidden-import list; none introduces a selector, mechanism,
or axiom.

### N7 - Steelman

The strongest objection: "A finite three-coefficient window cannot
foreclose an infinite-measure family — Hamburger's theorem characterises
**full** infinite sequences, and any finite truncation `{c_0, ..., c_N}`
that is Hankel-PSD extends to a genuine moment sequence (the truncated
Hamburger moment problem is solvable iff the finite Hankel matrix is PSD).
So a finite window cannot, in general, rule the measure out." The reply:
the truncated-moment-problem solvability theorem is a **sufficiency**
statement for PSD windows; the **necessity** direction is unconditional —
**any** subsequence-minor of a true moment sequence must be `>= 0`, because
the Hankel form of a positive measure is PSD on every finite coordinate
subspace. A strictly **negative** centred 2x2 minor is therefore an
unconditional certificate that **no** positive-measure extension exists,
finite window or not. The steelman correctly blocks the converse
over-reading (a PSD window would **not** prove a positive measure exists),
but it does not touch the scoped negative claim, which rides only on
necessity.

### N8 - Cross-cycle echo

The repo's recurrent negative-claim failure mode is to test **one
representative object** (one expression, one ratio, one continuation
ansatz) and then declare the **whole lane** closed. This note avoids that
echo structurally: (i) it foreclosing exactly **one** of the two
enumerated branches of the harness's analyticity premise and names the
surviving branch explicitly in the theorem, the scope section, and the YAML
(`surviving_class: off_axis_complex_conjugate_pair_continuation`); (ii) it
states up front that the complex-pair class is *consistent* with a negative
Hankel minor, pre-empting any slide from "real-axis branch foreclosed" to
"resummation dead"; and (iii) it records `resummation_route_status:
not_closed` and `beta6_status: not_closed` as machine-readable scope guards.
The claim boundary is the positive-measure / real-axis branch-cut family,
and nothing wider.

## 5. Runner

Run:

```bash
python3 scripts/frontier_beta6_cumulant_moment_positivity.py
```

Expected summary:

```text
SCORECARD: PASS=17 FAIL=0
```

The runner computes `d_5 d_7 - d_6^2` and `m_5 m_7 - m_6^2` in exact
`Fraction`/sympy `Rational` arithmetic, asserts both are strictly negative,
checks the integer-rescaling identity `m_5 m_7 - m_6^2 = 18^12 (d_5 d_7 - d_6^2)`,
and asserts the scope guard (positive-measure class foreclosed;
complex-conjugate-pair class survives).

## 6. Key files

- [`scripts/frontier_beta6_cumulant_moment_positivity.py`](../scripts/frontier_beta6_cumulant_moment_positivity.py)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)

This note is a formal no-go and asserts no closure of the beta=6 lane.
