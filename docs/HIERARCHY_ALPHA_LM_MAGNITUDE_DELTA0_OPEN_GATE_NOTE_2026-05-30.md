# Hierarchy Alpha_LM Magnitude Delta-Zero Open Gate

**Date:** 2026-05-30 (2026-06-12: downstream Block04 mean-field feedback probe recorded as context-only route pruning)
**Claim type:** open_gate
**Status:** source note; downstream status is decided by independent review.
**Primary runner:** [`scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py`](../scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py)

## Result

This note isolates the magnitude content in the hierarchy substitution

```text
alpha_LM = alpha_bare / u_0,
alpha_LM^16 = alpha_bare^16 * u_0^-16.
```

The runner verifies three local facts.

1. With `g_bare = 1`, `alpha_bare = 1/(4 pi)`, so
   `alpha_bare^16 = (4 pi)^-16 = 2.586e-18`.
2. The exact Matsubara determinant and condensate-density forms checked here
   contain `u_0` but no explicit `alpha_bare`.
3. The triplet
   `alpha_bare`, `alpha_LM = alpha_bare/u_0`,
   `alpha_s = alpha_bare/u_0^2` is a constant-ratio geometric progression.
   In the corresponding `1/alpha` variables the equal-step test gives
   `Delta_2 / Delta_1 = u_0`, not `1`.

Thus the checked block observables do not by themselves supply the
`(4 pi)^-16` coupling-power magnitude.  A transport interpretation of that
constant-ratio progression remains an open gate on the current `delta = 0`
lattice baseline; the finite algebra here records the obstruction surface but
does not close the hierarchy formula.

## Boundary

This note does not derive `v`, does not close the hierarchy lane, and does not
approve a new axiom, primitive, or Tier-A admission.  It also does not claim
that every possible future mechanism is closed.

The exact boundary is narrower:

```text
block determinant / condensate forms checked here: u_0-only;
alpha_LM magnitude factor: carries alpha_bare^16 by algebraic relabeling;
transport source for that coupling-power magnitude on the current baseline:
open.
```

A future source could close this gate by deriving an explicit `alpha_bare`
dependence inside the relevant block observable, or by deriving a baseline-native
transport rule that supplies the same constant-ratio coupling-power magnitude.

## Sharpening record (2026-06-11 / 2026-06-12; gate unchanged, still open)

Two downstream probes (backticked context pointers; citation direction
is downstream -> this gate) sharpened the obstruction surface without
closing it:

- `HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_PROBE_NOTE_2026-06-11.md`
  — exact single taste-mode decimation on the minimal `2^4` block
  carries `m +- 2i u_0` per mode (magnitude `2 u_0` at `m = 0`) with
  exactly zero induced coupling shift on kept modes; the bare per-mode
  conversion target is `N = alpha_LM/(2 u_0) = 1/(8 pi u_0^2)`.
- `HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md`
  — over a declared dressed/undressed ratio normalization the per-mode
  factor is `u_0` and the gate's open content reduces exactly to ONE
  unsupplied transport rule: one factor
  `alpha_s = alpha_bare/u_0^2` (fact 3's third progression member)
  per taste decoupling.
- `HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_PROBE_NOTE_2026-06-11.md`
  — context-only route pruning, not a load-bearing dependency for this
  note: under declared mean-field link-feedback variants, feeding the
  exact induced action `-n_c n ln(2u)` into the link self-consistency
  gives a per-decoupling readout factor `R = O(1)` near `1`, about
  `9.7x` above the required `alpha_s = 0.1033038`; therefore ordinary
  mean-field link un-freezing is refuted as the supplier for the
  `alpha_s`-per-decoupling attachment rule.

The zero-induced-shift result forecloses quadratic-block-algebra
closure routes at frozen links. After Block04, the ordinary
mean-field link-feedback candidate is also pruned. Surviving routes run
through beyond-mean-field link fluctuations or exact one-link Haar
integrals at strong coupling, readout-side dressing of the Green-kernel
chain, or a non-link transport rule.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks pass.
```
