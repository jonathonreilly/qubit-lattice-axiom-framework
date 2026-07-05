# Plaquette MC Certification Protocol — the Measurement-Fallback Design: Exact Precision Targets for a 5-Decimal `<P>` Certificate at `beta = 6` (the Single Highest-Stakes Number in the Lane), a Smoke-Calibrated Statistics Budget, PRE-REGISTERED Decision Bands That Can FALSIFY the Bounded Match, and the Stage-2 Staircase Flat-Cost Measurement Design (Design-Only)

**Date:** 2026-06-11 (block13 of the DELTA0/hierarchy measurement wave)
**Claim type:** meta — meta/protocol
**Claim boundary (declared up front):** exactly three grades of content,
none of which certifies a plaquette value or changes any status:
(M1, `bounded_theorem`-grade) the precision-target arithmetic is EXACT
(Fraction arithmetic where stated) over the declared literals of the
honest-status note and the B1 license — half-steps, relative targets,
the elasticity `-4` propagation, and the F4 separation geometry;
(M2, diagnostic) the smoke-scale finite-MC run is a STATISTICS-BUDGET
CALIBRATION only — `sigma_P`, `tau_int`, and per-sweep wall-clock
measured at `L = 4` with declared fixed seed; the smoke `<P>` estimate
is a fenced finite-volume diagnostic, NOT comparable to the
infinite-volume `0.5934` target, and certifies NOTHING about the value;
(M3/M4, protocol design) the numbered Stage-1 protocol with its
pre-registration block, and the Stage-2 design. **No value
certification is performed; no status change to the plaquette note; the
B1 license is unchanged by this row.**
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane.
**Primary runner:** [`scripts/frontier_plaquette_mc_certification_protocol_smoke_2026_06_11.py`](../scripts/frontier_plaquette_mc_certification_protocol_smoke_2026_06_11.py)

## 0. Setting: why a measurement-fallback protocol, and why now

The plaquette authority
([`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md))
licenses the canonical `<P> = 0.5934` at `beta = 6` downstream only as
an admitted comparison/reuse number "unless a separate retained MC
certificate or analytic beta=6 closure is supplied". Every constant of
the hierarchy lane consumes that license: `u_0`, `alpha_LM`,
`alpha_s = 0.1033038`, `K`, the `v_cand` readout (elasticity `-4`), and
the entire `Delta_S = 2.270081` action-cost decomposition of the DELTA0
campaign. This block designs **exactly the certificate the escape
clause names** — the MC half of the fallback (the analytic `beta = 6`
closure remains the other route).

The stakes are sharper than a generic error-bar upgrade, and the
honest-status note's F4 anti-tuning certificate
([`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md))
says exactly why: the plaquette value that would zero the fenced
comparator residual is `<P>_needed = 0.5934379`, which differs from the
licensed `0.5934` by `+3.79e-5` — **LESS than the 4-decimal rounding
half-step `5e-5`**. The licensed grid cannot even encode the
difference. A certification at 5 decimals is therefore DECISIVE
territory: the certified value either lands on `0.59344` (the
comparator residual moves INSIDE the B1 readout) or on `0.59340`/away
(the residual survives and its attribution to the B2 Planck anchor
becomes the unique surviving assignment at quoted precisions). This is
the single highest-stakes number in the lane, and this protocol handles
it the only honest way available: **the decision bands are
pre-registered below, declared BEFORE any production sweep is run**, so
that the F4 anti-tuning certificate stays meaningful whatever the
measurement returns. The production measurement **can FALSIFY the
bounded match — that is its scientific value.**

Stage 2 (the per-rung staircase flat-cost measurement contrastable with
the action-cost note's flat `Delta_S = 2.270081` prediction) is
specified at design level only (§4) and stays design-only pending
Stage 1.

## 1. M1 — precision-target derivation (exact arithmetic; runner Section M1)

All arithmetic exact (Fraction) over the declared literals; every line
recomputed by the runner.

- **4-decimal (license) grade.** To certify `<P>` at the B1 license
  grade the total error budget (statistical + finite-volume systematic,
  at the declared `z = 2` coverage) must be below the rounding
  half-step `5e-5`; relative `5e-5 / 0.5934 = 1/11868 = 8.4260e-5`
  (the honest-status note quotes `8.43e-5`). Through the exact
  sensitivity `d ln v_cand / d ln <P> = -4` this is the honest-status
  B1 resolution window `4/11868 = 1/2967 = 3.3704e-4 = 0.0337%` on
  `v_cand` — reproduced exactly.
- **5-decimal (decisive) grade.** Total error `< 5e-6`: relative
  `8.4260e-6`, inducing `0.0034%` on `v_cand` — **BELOW the B2
  attribution scale `0.0255%`** (ratio `~7.6`), while the 4-decimal
  window `0.0337%` is above it. Only the 5-decimal grade can resolve
  the residual attribution.
- **F4 separation geometry (exact).** `<P>_needed - 0.5934 = +3.79e-5
  < 5e-5`: the 4-decimal grid rounds `<P>_needed` back to the licensed
  `0.5934` (no admissible tuning — the F4 certificate). At 5 decimals
  the question separates: `round(0.5934379, 5) = 0.59344`, and
  `0.59344 - 0.59340 = 4e-5` = **EIGHT 5-decimal half-steps**. A
  5-decimal certificate cannot straddle the two answers.

**Decision-grade table (M1):**

| Grade | Total error | Relative on `<P>` | Induced window on `v_cand` | What it decides |
| --- | --- | --- | --- | --- |
| 4-decimal | `< 5e-5` | `8.4260e-5` | `0.0337%` | the B1 license itself: does the certified value round to `0.5934`? (confirm -> license upgraded to MC certificate; refute -> license BROKEN) |
| 5-decimal | `< 5e-6` | `8.4260e-6` | `0.0034%` | F4 / residual attribution: `0.59344` (residual re-attributed to B1's 4th-decimal rounding) vs `0.59340` (residual confirmed NOT from B1; B2 attribution decisive) |

## 2. M2 — statistics budget from smoke (diagnostic; runner Section M2)

**Machinery reuse.** The runner imports
[`scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`](../scripts/frontier_plaquette_self_consistency_finite_mc_repair.py)
and reuses its update algorithm — Metropolis with projected
near-identity SU(3) proposals — adapted to a vectorized full-lattice
checkerboard sweep (staple-based local `Delta_S`). Reuse fidelity is
checked, not assumed: the batched SU(3) projection reproduces the
module's `project_su3` element-wise (`< 1e-12`); the vectorized average
plaquette matches the module's `average_plaquette` on an `L = 2` random
configuration (`< 1e-12`); and the staple identity
`sum Re Tr[U_mu A_mu] = 4 sum_P Re Tr U_P` validates the local action
difference (`< 1e-10`).

**Smoke chain (declared, deterministic):** `L = 4`, `beta = 6`, cold
start, proposal spread `eps = 0.20`, 2 hits/link/sweep, seed
`20260611`, 500 thermalization + 2500 measurement sweeps; Madras-Sokal
windowed `tau_int` with the automatic window (`c = 5`, declared);
thermalization detected by the declared two-part criterion
(cold-start transient cut: first-sweep `P > mean + 10 sigma_P`;
post-cut halves agree within `5x` combined error).

**HONESTY FENCE (load-bearing for this note's claim boundary):** the
smoke numbers CALIBRATE the budget; they CERTIFY NOTHING about the
value. The smoke `<P>` estimate at `L = 4` is a finite-volume
diagnostic, fenced, NOT comparable to `0.5934`, which is the
infinite-volume target. The runner checks (as a PASS) that the smoke
error of mean is ABOVE certification grade.

**Measured at smoke scale (this machine, this implementation; recorded
live by the runner — the numbers below are the reference run's,
indicative only; wall-clock is machine-dependent):**

| Quantity | Reference-run value |
| --- | --- |
| `<P>_smoke(L=4)` | `0.59601 +/- 0.00078` (fenced diagnostic) |
| `sigma_P` (per-configuration) | `0.007624` |
| `tau_int` (plaquette) | `13.1` sweeps (window `W = 66`) |
| `t_sweep(L=4)` | `~6.7 ms` (vectorized numpy, single core) |

**Certification budget (computed by the runner from the measured
values; `N_indep = (z sigma_P / target)^2` at `z = 2`;
`sweeps = N_indep x 2 tau_int`):**

- 4-decimal grade: `N_indep ~ 9.3e4`, `~2.4e6` sweeps;
- 5-decimal grade: exactly `100x` more — `N_indep ~ 9.3e6`, `~2.4e8`
  sweeps.

**Declared cost-scaling model:** per-sweep work scales with the link
count, `t_sweep(L) = t_sweep(4) x (L/4)^4`. Two projections are
printed, both declared: the **conservative envelope** holds `sigma_P`
and `tau_int` at their `L = 4` values (an upper bound, since the
per-configuration variance of an intensive average falls with volume);
the **variance-scaling refinement** applies `sigma_P^2 ~ 1/L^4`
(short-ranged connected plaquette correlations at `beta = 6`), under
which `N_indep` falls by `(L/4)^4` and the total wall-clock is
approximately `L`-independent at `~ the L = 4 figure` (`tau_int` still
held fixed — declared assumption, to be measured in situ at production).
Reference-run projections (this pure-Python implementation, single
core; production codes — compiled Cabibbo-Marinari heatbath +
overrelaxation — are conventionally 2-3 orders of magnitude faster per
link and have smaller `tau_int`; that remark is context, not a measured
claim):

| `L` | `t_sweep` (model) | 4-decimal [conservative \| refined] | 5-decimal [conservative \| refined] |
| --- | --- | --- | --- |
| 8 | `~0.11 s` | `~72 h` \| `~4.5 h` | `~7.2e3 h` \| `~4.5e2 h` |
| 16 | `~1.7 s` | `~1.2e3 h` \| `~4.5 h` | `~1.2e5 h` \| `~4.5e2 h` |
| 24 | `~8.7 s` | `~5.9e3 h` \| `~4.5 h` | `~5.9e5 h` \| `~4.5e2 h` |
| 32 | `~27 s` | `~1.9e4 h` \| `~4.5 h` | `~1.9e6 h` \| `~4.5e2 h` |

**Feasibility readout (honest):** at the refined model the 4-decimal
grade is hours-scale per volume even in this reference implementation;
the 5-decimal grade is `~450 h` per volume here, i.e. it requires
either a compiled production code or modest parallelism — standard,
not exotic. The conservative envelope at `L = 32` makes the same point
in reverse: a naive fixed-variance reading would be prohibitive, which
is why the scaling model is declared rather than implied.

**Finite-volume extrapolation plan (declared):** certify the
infinite-volume value by the ansatz `<P>_L = <P>_inf + c L^-4` at fixed
`beta = 6` over `L in {8, 12, 16, 24, 32}` (5 points, 2 fit
parameters). The parent plaquette note has no finite-volume series of
its own (its runner is an `L = 2, 3` observable diagnostic), so the
ansatz is declared here: leading periodic finite-volume corrections to
an intensive gluonic observable fall as the inverse 4-volume; the fit
quality requirement and the `L = 24 -> 32` stability requirement are in
the protocol (§3, step 6). If the `L^-4` fit fails its quality gate,
the certificate is NOT issued (no ansatz-shopping after the fact).

## 3. M3 — Stage-1 protocol specification (the design deliverable)

Numbered and executable. Machine requirements follow from §2's
projections; every analysis choice is declared here, before any
production run.

1. **Implementation.** A compiled SU(3) code (Cabibbo-Marinari heatbath
   + overrelaxation mixture) OR this runner's vectorized Metropolis as
   the reference implementation. REQUIREMENT: two algorithmically
   independent update codes must agree on `<P>_L(beta = 6)` at `L = 8`
   within combined `2 sigma` before production statistics are collected
   (algorithm cross-validation gate).
2. **Surfaces.** `beta = 6` exactly (Wilson single-plaquette action,
   periodic boundaries, the plaquette note's normalization
   `P = Re Tr U_P / 3`); `L in {8, 12, 16, 24, 32}`.
3. **Machine requirement (from §2).** 4-decimal grade: single
   workstation, days-scale (refined model, any implementation grade).
   5-decimal grade: compiled code on a single node OR `O(100)`-core
   embarrassingly parallel replica streams (independent seeds, declared
   in advance) — `~5e2 h` reference-implementation-equivalent per
   volume.
4. **Thermalization/measurement split.** Per volume: paired cold and
   hot starts; discard `>= 20 tau_int` (measured in situ) or until the
   declared two-part criterion of §2 passes, whichever is later; the
   cold/hot pair must agree within combined `2 sigma` (start-state
   gate). Measure `P` every sweep.
5. **Error analysis (declared).** Madras-Sokal `tau_int` with `c = 5`
   automatic windowing; blocking/jackknife with block length
   `>= 4 tau_int`; the quoted statistical error is
   `max(jackknife, naive x sqrt(2 tau_int))`. Replica streams (if used)
   combined only after a per-stream stationarity pass.
6. **Finite-volume extrapolation.** Fit `<P>_L = <P>_inf + c L^-4`
   over the five volumes; require acceptable fit quality (declared
   gate: correlated `chi^2/dof < 2`) AND `|<P>_32 - <P>_24|` below the
   target grade; the certificand is `<P>_inf` with the FV systematic
   (fit-parameter error plus the `L = 24 -> 32` shift) added to the
   budget IN FULL.
7. **Grades.** Grade-4 certificate: total budget (stat + FV, `z = 2`)
   `< 5e-5`. Grade-5 certificate: `< 5e-6`. The grade attained is part
   of the certificate; a Grade-4 run does NOT adjudicate the F4
   question and must say so.
8. **Pre-registration.** The decision bands below are frozen as of this
   note's date, BEFORE any production sweep exists. Any post-hoc band
   adjustment voids the certificate's anti-tuning meaning.
9. **Reporting.** Certified `<P>_inf`, full error budget, grade, band
   verdict, seeds, and code provenance — supplied to the plaquette note
   as the "separate retained MC certificate" its escape clause names;
   the plaquette note's status change is then the audit lane's call,
   not this protocol's.

### Pre-registration block (decision bands; declared BEFORE any production sweep)

Let `d := <P>_inf(certified) - 0.5934` with the certificate at the
stated grade. **Explicit warning, part of the registration: this
measurement can FALSIFY the bounded match — that is its scientific
value.** The bands partition the axis (`5e-6 < 5e-5 < 1e-4 = 2 x
half-step`, exact):

- **Band A (license confirmed): `|d| <= 5e-5`.** The certified value
  rounds to `0.5934`: the B1 license is upgraded from admitted reuse
  number to MC certificate at 4 decimals. Re-audit triggers fire across
  the lane (every B1 consumer re-cites the certificate; the
  honest-status note's own trigger — "the plaquette lane re-licenses
  `<P>` at different precision" — fires; all 4-decimal values
  unchanged).
- **Band B (decisive sub-bands; requires Grade-5):** within Band A, at
  `sigma_total <= 5e-6`:
  - **Band B-i: `|<P>_inf - 0.5934379| <= 1e-5`** (lands on
    `0.59344`): F4 becomes decisive — the fenced comparator residual
    (`~0.0255%` on `v_cand`, elasticity `-4 x` the offset, exactly) is
    re-attributed from the B2 Planck anchor to B1's 4th-decimal
    rounding; the honest-status B2-attribution paragraph and the
    class-D comparator framing must be re-audited.
  - **Band B-ii: `|<P>_inf - 0.59340| <= 1e-5`** (stays on the licensed
    center): the residual is confirmed NOT from B1; the B2 attribution
    becomes the unique surviving assignment at quoted precisions, and
    the comparator's last word passes — per the honest-status note's
    own sentence — to the Planck lane.
  - **Band B-iii** (elsewhere inside Band A): partial re-attribution;
    both windows recomputed at the certified center; no decisive call.
- **Band C (license broken, moderate): `5e-5 < |d| <= 1e-4`.** The
  certified value no longer rounds to `0.5934`: the B1 license is
  BROKEN. `v_cand` moves by `-4 x d / 0.5934` (between `0.0337%` and
  `0.0674%` — the Band-C minimum displacement is exactly `2x` the B1
  window). B1 is re-licensed at the certified value and the full
  consumer list (below) recomputes; 4-decimal constants change in the
  last digit.
- **Band D (license broken, decisive): `|d| > 1e-4`.** The bounded
  match is in falsification territory: the `v_cand` readout moves by
  elasticity `-4 x` a deviation larger than its own input-resolution
  window, the comparator residual changes sign or scale, and the F4
  anti-tuning certificate is VOID at the old center. **What re-opens
  (enumerated):** the honest-status T1 constants (`u_0`, `alpha_LM`,
  `alpha_s = 0.1033038`, `K = 2.017224e-17`) and its C1 readout
  `v_cand`; the F4 certificate and both resolution windows; the entire
  DELTA0 action-cost surface (`Delta_S = 2.270081` per rung, the rung
  `2.400553`, the 16-rung budget `38.4422` — every block01-block10
  constant consuming B1); the YT-P2 retained per-rung cross-check; the
  Higgs-note B2 insensitivity certificate; the `alpha_s` scale label
  `mu = v`; the observable-principle readout. (Each re-opens for
  recomputation at the certified value; whether any survives is the
  recomputation's outcome, not this protocol's prediction.)

A certificate that lands in ANY band is a scientific success: A/B
upgrade or sharpen the lane's most-consumed number; C/D would be the
framework's first measured strike against the bounded match — exactly
what a pre-registered measurement is for.

## 4. M4 — Stage 2: the staircase flat-cost measurement (design only)

The action-cost note
([`HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_NOTE_2026-06-11.md))
predicts (as T4's testable consequence) a FLAT per-rung transport cost
`Delta_S = 2.270081`, independent of the threshold index `k`, with a
declared kill criterion (any measured `k`-dependence eliminates the
formulation). What a Stage-2 measurement would need:

- **Observable family 1 — spectral flow of the staggered operator
  under blocking.** Track the low spectrum of the staggered Dirac
  operator across successive factor-2 blocking steps; per-threshold
  decouplings appear as eigenvalue-density depletions, and the per-rung
  cost is read as the log-ratio of effective couplings between
  consecutive blocking steps. The flat-`Delta_S` prediction is a
  zero-drift line; any drift is T4's kill criterion firing.
- **Observable family 2 — per-threshold condensate shares.**
  Taste-projected condensate decomposition across the Hamming staircase
  `(1,4,6,4,1)`: each threshold's share of the condensate against the
  equal-cost prediction.
- **Why it is strictly harder (multi-scale).** Stage 1 is a single-`beta`
  pure-gauge scalar observable. Stage 2 spans 16 rungs of `2.4006`
  each — `~38.4` e-folds of scale: no single lattice covers it, so the
  measurement requires a step-scaling recursion (per-step matched
  lattices with per-step continuum extrapolation) plus fermionic
  measurements — orders of magnitude beyond Stage 1 in both cost and
  systematic exposure.
- **Status: design-only pending Stage 1.** No Stage-2 computation
  exists in this block, and none is scheduled by it: Stage 1 is the
  gate (it certifies the very number every Stage-2 constant consumes).

## 5. What this note does NOT claim

- It does NOT certify, derive, measure, or update `<P> = 0.5934` at any
  grade: the Stage-1 certification is NOT performed; the smoke run is a
  budget calibration whose `<P>` estimate is a fenced `L = 4`
  finite-volume diagnostic, never compared to the canonical value.
- It does NOT change the status of the plaquette note or the B1
  license: `0.5934` remains an admitted reuse number until a
  pre-registered production run lands a retained certificate (or the
  analytic closure route lands), and the status call is the audit
  lane's.
- It does NOT predict which decision band the production measurement
  will land in, and it does NOT treat the F4 geometry as evidence for
  any band (the geometry is exact arithmetic; the landing is an open
  empirical question — including the falsifying bands C/D).
- It does NOT claim the projected wall-clocks are measured facts beyond
  the reference machine and implementation: the cost model and the
  variance-scaling refinement are DECLARED scaling assumptions, to be
  re-measured in situ at production (and the compiled-code speedup
  remark is context, not a measurement).
- It does NOT perform, schedule, or cost Stage 2 beyond design level
  (design-only pending Stage 1), and it does NOT add content to the
  action-cost note's T4 (whose kill criterion it merely cites as the
  Stage-2 contrast).
- It does NOT consume any PDG quantity as load-bearing: the single
  PDG-derived scale touched (the comparator-residual `~0.0255%` that
  the F4 offset reproduces under elasticity `-4`) lives in the fenced
  class-D check and in Band B-i's description only.
- It does NOT introduce any new axiom, primitive, fitted coefficient,
  or vocabulary (all targets, elasticities, and literals are quoted
  from the cited authorities and verified on disk).

## 6. Re-audit triggers

Re-audit this note if: a production run lands in ANY pre-registered
band (the band verdict supersedes this note's open status and fires the
band's enumerated consequences); the plaquette note's license language
or the honest-status note's F4/window literals change (M1's exact
arithmetic consumes them); the action-cost note's `Delta_S = 2.270081`
or its T4 kill criterion changes (Stage-2 contrast); the analytic
`beta = 6` closure route lands first (the fallback's priority
inverts); or the reuse module
`frontier_plaquette_self_consistency_finite_mc_repair.py` changes its
update algorithm (M2's reuse-fidelity surface).

## 7. Dependencies (one-hop, load-bearing)

- [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  — the B1 license and the escape clause ("unless a separate retained
  MC certificate or analytic beta=6 closure is supplied") whose MC
  branch this protocol designs; also the finite-observable theorem that
  makes `<P>_L(beta)` a well-defined certifiable number, and the reused
  runner machinery
  ([`scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`](../scripts/frontier_plaquette_self_consistency_finite_mc_repair.py)).
- [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
  — the exact elasticity `-4`, the B1 4-decimal license grade and its
  `0.0337%` window, the F4 anti-tuning target `0.5934379`, and the B2
  attribution scale `0.0255%` that M1's decision table is built from
  (literals verified on disk by the runner).
- [`HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_NOTE_2026-06-11.md)
  — the Stage-2 target: the flat per-rung `Delta_S = 2.270081`
  staircase prediction and its `k`-independence kill criterion (literal
  verified on disk by the runner).

Context file pointers (backticked; non-load-bearing):
`COMPLETE_PREDICTION_CHAIN_2026_04_15.md`,
`HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md`,
`HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_NOTE_2026-06-11.md`,
`YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md`,
`HIGGS_MASS_FROM_AXIOM_NOTE.md`, `ALPHA_S_DERIVED_NOTE.md`,
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`,
`SCALE_REFERENCE_PRIMITIVE_NOTE.md`.

**No-promotion statement:** this note does not promote, demote, or set
the audit status of any dependency. The independent audit lane is the
only status authority.

## Verification

Run:

```bash
python3 scripts/frontier_plaquette_mc_certification_protocol_smoke_2026_06_11.py
```

Expected result (deterministic: fixed seeds `20260611` /
`2026061101` / `2026061102`, numpy Generator; no network; total runtime
well under 120 s on the reference machine — the `L = 4` smoke chain,
~25 s, dominates; exit code 0):

```text
Breakdown: A=10 B=6 C=9 D=2 RESIDUAL=3
TOTAL: PASS=27 FAIL=0
```

with exactly three `RESIDUAL (declared-open):` lines (R1: the Stage-1
certification is NOT performed — the pre-registered bands await a
production run; R2: Stage 2 is design-only pending Stage 1; R3: the
plaquette note's status is unchanged — `0.5934` remains an admitted
reuse number until the certificate lands). The smoke `<P>` line is
printed inside a fenced DIAGNOSTIC block, never as a comparison to
`0.5934`; the terminal VERDICT states that the precision-target
arithmetic is exact, that the smoke run calibrates and certifies
nothing, that the bands are pre-registered before any production run,
and that the production measurement can FALSIFY the bounded match.

Baseline non-disturbance (the reused machinery still passes):

```bash
PYTHONPATH=scripts python3 scripts/frontier_plaquette_self_consistency_finite_mc_repair.py  # TOTAL: PASS=24 FAIL=0
```
