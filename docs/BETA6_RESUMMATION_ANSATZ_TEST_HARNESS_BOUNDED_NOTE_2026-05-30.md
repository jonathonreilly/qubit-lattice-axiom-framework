# Beta=6 SU(3) Wilson Single-Plaquette Resummation-Ansatz Test Harness

**Date:** 2026-05-30; 2026-06-07 current-coefficient refresh; 2026-06-07
conditional-coefficient scope repair; 2026-06-08 coefficient-source packet
repair.
**Claim type:** bounded_theorem (methodology / test harness)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome for any cited claim_id; all statuses quoted
below are read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the dates stated.
**Primary runner:** [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)

## 0. Scope and what this note is for

This note documents a **test harness**, not a closure. It builds and now runs
the machinery that tests the two remaining unproven analytic continuation
ansaetze for the beta=6 SU(3) Wilson single-plaquette lane against the current
supplied connected-coefficient packet.

### 2026-06-07 audit-scope repair

The current auditable claim is intentionally narrower than a retained
coefficient-packet theorem:

- **Claim supported here:** conditional-on-supplied-coefficients harness
  arithmetic. Given the exact `d_6..d_11` values supplied by the paired
  coefficient source packet, the runner checks the d-log-Pade and
  tadpole/geometric test mechanics, their FALSIFY/SUPPORT classifications, the
  proxy-method sanity checks, and the forward comparator diagnostics.
- **Not claimed here:** a retained derivation of the `d_6..d_11` coefficient
  packet, a retained beta=6 value, or a retained closure of the analytic
  continuation route.
- **Non-load-bearing context:** the beta=6 research map and the Monte-Carlo
  plaquette value are comparator/context surfaces only. They do not supply a
  load-bearing derivation input for this claim.
- **Audit boundary:** if a later review wants more than conditional harness
  arithmetic, it must supply a retained-grade one-hop coefficient-packet
  authority for exact `d_6..d_11` or inline a derivation of those coefficients.

### 2026-06-08 coefficient-source packet repair

The audit blocker for this row was not a mathematical sign error in the harness;
it was that the exact `d_6..d_11` packet was visible to the harness as local
values rather than as a source-verifiable one-hop packet. This repair wires the
harness to the exact coefficient runner
[`scripts/frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py)
and checks the paired cache
[`logs/runner-cache/frontier_beta6_d11_coefficient_2026_06_04.txt`](../logs/runner-cache/frontier_beta6_d11_coefficient_2026_06_04.txt)
for a fresh source SHA, `SCORECARD: PASS=9 FAIL=0`, and the exact values through
`d_11`.

This closes the source-packet/provenance defect for the harness. It does not
turn the harness into a retained coefficient theorem and does not close
`beta=6`; coefficient retention and beta=6 closure remain separate audit
questions.

The lane's open object and blocked-route catalog are recorded in the research
map [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md).
That note identifies exactly one not-yet-blocked (long-shot) analytic route -
**d-log-Pade resummation of the connected-shell series** — and a tadpole /
boosted-PT comparator. The original 2026-05-30 version was pending because no
connected-coefficient data beyond the retained order-`beta^5` term was wired into
the harness. The current repo has since supplied rational `d_6..d_11` values in
the beta6 coefficient source packet, so this refresh consumes that packet and
records the live SUPPORT/FALSIFY outcomes conditional on it.

This harness is **downstream of but not a replacement for** the exact-coefficient
computation. It evaluates the connected coefficient series of

```text
Delta(beta) = P_full(beta) - P_1plaq(beta),    Delta(beta) = sum_{n>=5} d_n beta^n,
```

with `d_5 = 1/472392` retained and `d_6..d_11` loaded from the paired source
packet, runs the two tests below, and reports a clear PASS/FAIL scorecard.

### What this note explicitly does NOT claim (honesty, non-negotiable)

- It does **not** close beta=6 and must not be read as doing so.
- `<P>(beta=6) ~= 0.594` (`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`,
  `P_inf = 0.59400 +/- 0.00037`; also quoted as 0.5934) is a **Monte-Carlo
  comparator**, **not** a derivation input. Nothing in the harness is fitted
  to it. The harness **tests** whether an ansatz fixed by the **low-order
  supplied coefficients** independently reaches it — it does not tune to it.
- The supplied connected coefficients consumed by the harness are
  `d_5 = 1/472392`, `d_6 = 7/5668704`, `d_7 = 5/17006112`,
  `d_8 = 5/272097792`, `d_9 = -2035/264479053824`,
  `d_10 = -10483/5289581076480`, and
  `d_11 = -13/3967185807360`. The harness now loads these values from the
  paired coefficient source runner and verifies the d11 cache freshness. This
  packet activates the test; this note does not derive the packet or close
  beta=6.

## 1. The two ansaetze under test

### 1a. d-log-Pade resummation

Write `Delta(beta) = beta^5 * h(beta)` with `h` analytic and `h(0) = d_5`.
Form the logarithmic-derivative series `H(beta) = (log h)'(beta)`, build the
`[n/n]` Pade approximant of `H`, locate the nearest `beta`-plane singularity
(root of the Pade denominator), and integrate `H` back from `0` to `beta` to
recover `log h(beta) - log h(0)`, hence `Delta(beta)`. The route's conjectured
analytic structure (research map Section 4b) is a dominant **complex-pair**
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
  = 9.32617` (matches research map Section 7; this is a **read-off, not a
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
  reproduces the **already-blocked** `P_1plaq(31.5) = 0.8742` (research-map
  ledger item M4). **Finding:** boosting the single-plaquette series alone does
  **not** independently reach 0.594; a tadpole test outcome therefore lives in the
  connected-coefficient **pattern** it implies, tested predictively (Section 3).

## 3. Predictive falsification test (the decisive one)

Given a lower-order connected series, the harness computes what each ansatz
**predicts** for the next connected coefficient and compares that prediction
against the next supplied coefficient. This refresh uses the supplied
`d_5..d_11` packet.

### 3a. Activation thresholds and current supplied-coefficient outcomes

With only `d_5 = 1/472392`, **neither** ansatz made a falsifiable prediction
for `d_6`. One connected coefficient cannot fix a non-trivial continuation
(the tadpole geometric ratio needs two contiguous coefficients; a
`[>=1/>=1]` d-log Pade re-expansion needs four). That historical null remains
as a regression check. The activation thresholds are

| ansatz | contiguous supplied coeffs needed | predicts |
|---|---|---|
| tadpole / geometric | 2 (`d_5, d_6`) | `d_7` |
| d-log-Pade | 4 (`d_5 .. d_8`) | `d_9` |

The current supplied packet activates both tests. The runner reports:

- **tadpole / geometric:** `d_5,d_6 -> d_7` predicts
  `7.2032926e-7`, while supplied `d_7 = 2.9401194e-7`, relative error `1.45`.
  This is a FALSIFY result under the 5% window.
- **d-log-Pade earliest activation:** `d_5..d_8 -> d_9` predicts
  `-1.0534861e-8`, while supplied `d_9 = -7.6943711e-9`, relative error
  `0.3692`. This is also a FALSIFY result.
- **d-log-Pade stability:** the intermediate `d_10` check is narrowly inside
  the 5% window, but the full-current `d_5..d_10 -> d_11` check predicts
  `-1.8277392e-11`, while supplied `d_11 = -3.2768821e-12`, relative error
  `4.578`. The correct interpretation is instability, not closure.

### 3b. Current supplied coefficient packet

The runner's `SUPPLIED_HIGHER_COEFFS` packet is:

```python
{
    6: "7/5668704",
    7: "5/17006112",
    8: "5/272097792",
    9: "-2035/264479053824",
    10: "-10483/5289581076480",
    11: "-13/3967185807360",
}
```

The runner still self-tests the comparison path on synthetic coefficients: it
returns `SUPPORT` for a coefficient consistent with a pure single-pole
continuation and `FALSIFY` for a coefficient that deviates 50% from the
predicted value. The live physical packet uses the same comparison path.

## 4. Convergence behavior (controlled complex-pair proxy)

To certify the d-log-Pade **method** is sound when the singularity structure
cooperates, the harness reproduces the research-map proxy: a function with a
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
  (reproduces the research-map claim of `~1e-3` by `~[10/10]`).
- The **predictive** next-coefficient call sharpens with order: given `d_1..d_6`
  it predicts `d_7` to relative error `3.1e-3`; given `d_1..d_8`, `d_9` to
  `6.0e-4`; given `d_1..d_11`, `d_12` to `5.7e-7`.

This certifies only that the **method works on a function of the conjectured
analytic class**. It says nothing about whether the **physical** `Delta(beta)`
is of that class — that analyticity premise is unproven (research map
Section 4b) and is precisely what the predictive test against the supplied
coefficients probes inside this conditional harness.

## 5. Honest test status

- The d-log-Pade method is sound on a controlled complex-pair proxy.
- On the physical series, supplied `d_5..d_11` are now consumed. The old
  `PENDING d_6` state is retired.
- The tadpole/geometric ansatz is falsified conditional on the supplied
  coefficients.
- The d-log-Pade ansatz is unstable rather than converged: `d_9` and `d_11`
  falsify while `d_10` narrowly supports. This is not clean convergence to
  `0.5934` or `0.594`.
- Tadpole / boosted-PT of the bare single-plaquette series does not reach
  0.594 (it collapses to 0, or convention-dependent lands on the blocked
  0.611 / 0.8740).
- **Current test status:** simple tadpole/geometric FALSIFY; d-log-Pade
  instability/no-closure. **This harness evaluates the route; it does not
  close beta=6.** `0.594` is a Monte-Carlo comparator, never a derivation
  input.

## 6. Reproduce

```text
python3 scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py
```

The runner prints a per-test PASS/FAIL scorecard (`PASS=30 FAIL=0` after the
2026-06-08 source-packet repair) covering: coefficient-source/cache provenance;
the recomputed retained constants; the proxy singularity
localization and forward convergence; the proxy predictive next-coefficient
sharpening; the historical single-coefficient null on the physical series; the
supplied `d_5..d_11` predictive FALSIFY/SUPPORT comparisons; the
tadpole fixed-point findings (trivial collapse and the blocked
Drouffe-Itzykson branch); the synthetic-coefficient self-test of the
SUPPORT/FALSIFY machinery; and the forward `<P>(6)` sensitivity band.

## 7. Key files

- [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)
- [`logs/runner-cache/frontier_beta6_resummation_ansatz_test_2026_05_30.txt`](../logs/runner-cache/frontier_beta6_resummation_ansatz_test_2026_05_30.txt)
- [`scripts/frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py)
- [`logs/runner-cache/frontier_beta6_d11_coefficient_2026_06_04.txt`](../logs/runner-cache/frontier_beta6_d11_coefficient_2026_06_04.txt)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)
- [`BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_TWOCUBE_CLOSED_FORM_BOUNDED_NOTE_2026-06-04.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- [`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md)
- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md)
- [`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
- [`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md)
- [`U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md`](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md)
- [`SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md`](SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md)

This note is a methodology / test harness and asserts no closure of the
beta=6 lane.
