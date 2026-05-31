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
