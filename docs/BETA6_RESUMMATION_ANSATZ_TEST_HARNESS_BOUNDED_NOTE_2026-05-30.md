# Beta=6 SU(3) Wilson Single-Plaquette Resummation-Ansatz Test Harness

**Date:** 2026-05-30
**Claim type:** bounded_theorem (methodology / verdict harness)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome for any cited claim_id; all statuses quoted
below are read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the dates stated.
**Primary runner:** [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)

## 0. Scope and what this note is for

This note documents a **test harness**, not a closure. It builds the
machinery that will **verdict** the two surviving-but-unproven analytic
continuation ansaetze for the beta=6 SU(3) Wilson single-plaquette lane the
moment the parallel exact-coefficient cycle supplies the connected
coefficients beyond the retained order-`beta^5` term.

The lane's open object and ruled-out catalog are recorded in the frontier
map [`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md).
That note identifies exactly one non-ruled-out (long-shot) analytic route —
**d-log-Pade resummation of the connected-shell series** — and a tadpole /
boosted-PT comparator, and names the binding constraint: there is no exact
connected-coefficient data beyond the order-`beta^5` term, and producing more
collides with the treewidth-29 infeasibility wall
(`su3_wigner_l3_treewidth_infeasible_2026-05-04`, `audited_conditional`
on 2026-05-29).

This harness is **independent of** that exact-coefficient computation. It is
the part that can be built now: a framework that, given the connected
coefficient series of

```text
Delta(beta) = P_full(beta) - P_1plaq(beta),    Delta(beta) = sum_{n>=5} d_n beta^n,
```

with `d_5 = 1/472392` retained and `d_6, d_7, ...` to-be-supplied, runs the
two tests below and reports a clear PASS/FAIL scorecard.

### What this note explicitly does NOT claim (honesty, non-negotiable)

- It does **not** close beta=6 and must not be read as doing so.
- `<P>(beta=6) ~= 0.594` (`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`,
  `P_inf = 0.59400 +/- 0.00037`; also quoted as 0.5934) is a **Monte-Carlo
  comparator**, **not** a derivation input. Nothing in the harness is fitted
  to it. The harness **tests** whether an ansatz fixed by the **low-order
  exact coefficients** independently reaches it — it does not tune to it.
- The only exact connected coefficient currently in the repo is the retained
  order-`beta^5` coefficient `d_5 = 1/472392`
  (`gauge_vacuum_plaquette_mixed_cumulant_audit_note`). `d_6, d_7` enter the
  harness only as parameters. Supplying them is the activation of the verdict.

## 1. The two ansaetze under test

### 1a. d-log-Pade resummation

Write `Delta(beta) = beta^5 * h(beta)` with `h` analytic and `h(0) = d_5`.
Form the logarithmic-derivative series `H(beta) = (log h)'(beta)`, build the
`[n/n]` Pade approximant of `H`, locate the nearest `beta`-plane singularity
(root of the Pade denominator), and integrate `H` back from `0` to `beta` to
recover `log h(beta) - log h(0)`, hence `Delta(beta)`. The route's conjectured
analytic structure (frontier note Section 4b) is a dominant **complex-pair**
branch point at `|beta_c| ~ 5.7` off the real axis — physically plausible for
SU(3) pure-gauge (smooth crossover near `beta ~ 5.7`, no genuine bulk
transition) but **unproven**.

### 1b. Tadpole-improved / boosted perturbation theory

The `u_0 = <P>^{1/4}` self-consistency (the `1/4` exponent is retained,
`u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17`). The boosted
coupling is `beta_eff = beta * u_0^4 = beta * <P>`. A boosted-coupling
continuation with a single nearest real boosting singularity `beta*` maps the
connected series onto a leading geometric tail, `d_{n+1}/d_n -> 1/beta*`.

## 2. Forward test (implied `<P>(6)` under each ansatz)

The harness computes `<P>(6) = P_1plaq(6) + Delta(6)` as a function of how many
connected coefficients are supplied, and reports convergence toward the 0.594
comparator and sensitivity to the next unknown coefficient.

- **Baseline (recomputed for self-consistency).** `P_1plaq(6) = 0.4225317396`
  via the retained order-3 dominant-weight recurrence
  `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`,
  `a_0=1, a_1=0, a_2=1/36`
  (`gauge_vacuum_plaquette_transfer_operator_character_recurrence_note`,
  `plaquette_v1_picard_fuchs_ode_note_2026-05-05`). The comparator-implied
  residual is `Delta(6)_target = 0.594 - 0.4225317396 ~= 0.1715` (a
  comparator-derived target, **not** a fit). The implicit boosted coupling
  that would reproduce the comparator is `beta_eff^can = P_1plaq^{-1}(0.5934)
  = 9.32617` (matches frontier note Section 7; this is a **read-off, not a
  derivation** of the value).

- **One connected term only (`d_5`).** `Delta(6) ~ d_5 * 6^5 = 0.016461`, so
  `<P>(6)_trunc ~= 0.43899` — about **10%** of the comparator gap. A single
  low-order term **cannot** reach 0.594; this is expected and is not a closure.

- **Tadpole / boosted-PT forward fixed points.** The self-consistent tadpole
  fixed point of the **bare single-plaquette series** alone,
  `u_0^4 = P_1plaq(beta * u_0^4)`, has only the **trivial** fixed point
  `P = 0`. The over-boost convention `beta_eff = beta / <P>` converges to
  `P = 0.6115` (in the crossover, convention-dependent — not a derivation of
  0.594), and the `z = 6` mean-field / Drouffe-Itzykson self-consistent branch
  reproduces the **already-ruled-out** `P_1plaq(31.5) = 0.8742` (frontier
  ledger item M4). **Finding:** boosting the single-plaquette series alone does
  **not** independently reach 0.594; a tadpole verdict therefore lives in the
  connected-coefficient **pattern** it implies, tested predictively (Section 3).

## 3. Predictive falsification test (the decisive one)

Given only the lower-order connected series, the harness computes what each
ansatz **predicts** for the next connected coefficient, written as a one-line
call so that comparing exact-vs-predicted is an immediate falsify-or-support
the moment the parallel cycle drops in the exact coefficient.

### 3a. Each ansatz's prediction from the currently-known series

With only `d_5 = 1/472392` known, **neither** ansatz makes a falsifiable
prediction for `d_6`. One connected coefficient cannot fix a non-trivial
continuation (the tadpole geometric ratio needs two contiguous coefficients;
a `[>=1/>=1]` d-log Pade re-expansion needs four). The harness reports this
honest null rather than fabricating a value. This is itself a finding: **the
exact `d_6` alone is not sufficient for the d-log-Pade predictive verdict**;
the activation thresholds are

| ansatz | contiguous exact coeffs needed | predicts |
|---|---|---|
| tadpole / geometric | 2 (`d_5, d_6`) | `d_7` |
| d-log-Pade | 4 (`d_5 .. d_8`) | `d_9` |

So the **first** new exact coefficient `d_6` immediately activates the
**tadpole/geometric** predictive verdict (the cheapest decisive falsifier),
while the **d-log-Pade** predictive verdict activates only after three further
orders.

### 3b. The one-line drop-in

The runner exposes a single drop-in point (`EXACT_HIGHER = {6: ..., 7: ...}`).
The moment the parallel cycle delivers an exact coefficient, add it, rerun,
and read the `SUPPORT` / `FALSIFY` line. The runner self-tests this path on
synthetic coefficients (Section 4c of the runner): it confirms the machinery
returns `SUPPORT` for a coefficient consistent with a pure single-pole
continuation (relative error ~`1e-61`) and `FALSIFY` for a coefficient that
deviates 50% from the predicted value (relative error `0.33`, outside the 5%
support window). The verdict is therefore wired and demonstrably live before
any physical coefficient lands.

## 4. Convergence behavior (controlled complex-pair proxy)

To certify the d-log-Pade **method** is sound when the singularity structure
cooperates, the harness reproduces the frontier-note proxy: a function with a
complex-conjugate-pair branch point at `beta = R e^{+-i theta}`,
`R = 5.7, theta = 0.55`, amplitude tuned so the proxy's `Delta(6) = 0.171`
(matching the physical `Delta(6) ~ 0.1715`). The closed form is the Gegenbauer
(ultraspherical) generating function, so its Taylor coefficients are
`C_n^{(1/2)}(cos theta) / R^n` in closed form, and `beta = 6` sits just
**beyond** the singular radius `|beta_c| ~ 5.7` (the bare Taylor sum diverges;
analytic continuation is mandatory — exactly the regime the resummation must
handle). On this proxy:

- The `[n/n]` d-log Pade **localizes the singularity**: `[10/10]` gives
  `|beta_c| = 5.6989` (true 5.7), `arg = 0.5497` (true 0.55) — a genuine
  off-axis complex pair.
- The **forward** reconstruction of `Delta(6)` converges monotonically:
  `[4/4] -> 8.2e-3`, `[6/6] -> 3.4e-3`, `[8/8] -> 1.4e-3`, `[10/10] -> 5.8e-4`
  (reproduces the frontier-note claim of `~1e-3` by `~[10/10]`).
- The **predictive** next-coefficient call sharpens with order: given `d_1..d_6`
  it predicts `d_7` to relative error `3.1e-3`; given `d_1..d_8`, `d_9` to
  `6.0e-4`; given `d_1..d_11`, `d_12` to `5.7e-7`.

This certifies only that the **method works on a function of the conjectured
analytic class**. It says nothing about whether the **physical** `Delta(beta)`
is of that class — that analyticity premise is unproven (frontier note
Section 4b) and is precisely what the predictive test against the exact
coefficients will probe.

## 5. Honest verdict status

- The d-log-Pade method is sound on a controlled complex-pair proxy.
- On the physical series, only **one** exact connected coefficient (`d_5`) is
  known — too few for either ansatz to make a falsifiable prediction, and a
  single term reaches only ~10% of the comparator gap. **Neither ansatz can be
  said to reach 0.594 yet;** asserting so would be fitting to the comparator,
  the exact circularity the no-go ledger warns against.
- Tadpole / boosted-PT of the bare single-plaquette series does not reach
  0.594 (it collapses to 0, or convention-dependent lands on the ruled-out
  0.611 / 0.8740).
- **Verdict status: PENDING** the exact `d_6` (and `d_7`, `d_8`). The
  predictive falsification is wired as a one-line drop-in. **This harness
  verdicts the route; it does not close beta=6.** `0.594` is a Monte-Carlo
  comparator, never a derivation input.

## 6. Reproduce

```text
python3 scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py
```

The runner prints a per-test PASS/FAIL scorecard (20 PASS / 0 FAIL at
submission) covering: the recomputed retained constants; the proxy singularity
localization and forward convergence; the proxy predictive next-coefficient
sharpening; the honest single-coefficient null on the physical series; the
tadpole fixed-point findings (trivial collapse and the ruled-out
Drouffe-Itzykson branch); the synthetic-coefficient self-test of the
SUPPORT/FALSIFY machinery; and the forward `<P>(6)` sensitivity band.

## 7. Key files

- [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)
- [`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- [`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md)
- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md)
- [`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
- [`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md)
- [`U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md`](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md)
- [`SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md`](SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md)

This note is a methodology / verdict harness and asserts no closure of the
beta=6 lane.
