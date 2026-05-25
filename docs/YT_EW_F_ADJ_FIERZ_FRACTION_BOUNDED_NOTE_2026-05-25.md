# y_t EW F_adj Fierz-Fraction Bounded Note

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/yt_ew_f_adj_fierz_runner.py`](../scripts/yt_ew_f_adj_fierz_runner.py)

## Claim

Given the retained Fierz channel-count authority
[`ew_current_fierz_channel_decomposition_note_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
(decoration-level authority supplying the SU(N_c) Fierz channel-count for
quark-current decompositions), the adjoint Fierz fraction is

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9   at N_c = 3.
```

This note isolates the exact-rational-arithmetic half of
[`yt_ew_color_projection_theorem`](YT_EW_COLOR_PROJECTION_THEOREM.md)
(which is audited_conditional on `kappa_EW`). The `kappa_EW = 0`
derivation and the unconditional `9/8` projection remain conditional per
the parent's verdict.

The proof-walk uses only:

1. The cited channel-count from the Fierz authority (singlet count `1`,
   adjoint count `N_c^2 - 1`, total channel-count `N_c^2`).
2. Rational arithmetic: `(N_c^2 - 1) / N_c^2 = 1 - 1/N_c^2`, evaluated at
   N_c = 3.

This is a bounded proof-walk that isolates the exact rational arithmetic
step. It does not add a new axiom, a new repo-wide theory class, or a
retained status claim. It makes **no claim** about `kappa_EW`, the
lattice-current readout, the disconnected coefficient, or the
unconditional `9/8` projection — those remain conditional per the parent
`yt_ew_color_projection_theorem`.

## Proof-Walk

| Step | Load-bearing input | Conditional on `kappa_EW`? |
|---|---|---|
| State Fierz channel-count: singlet `1`, adjoint `N_c^2 - 1`, total `N_c^2` | cited Fierz channel-count authority | no |
| Algebraic rearrangement: `(N_c^2 - 1) / N_c^2 = 1 - 1/N_c^2` | rational arithmetic | no |
| Specialize at N_c = 3: `1 - 1/9 = 8/9` | rational arithmetic | no |

The checked proof path cites only the Fierz channel-count authority and
rational arithmetic. It does not cite a lattice-current matching rule, a
disconnected coefficient, an OZI suppression argument, or any continuum
observational input.

## Exact Arithmetic Check

The cited Fierz authority supplies channel-counts `singlet = 1` and
`adjoint = N_c^2 - 1` with total `N_c^2`. The adjoint fraction is

```text
F_adj = (N_c^2 - 1) / N_c^2
      = 1 - 1/N_c^2.
```

Specializing at N_c = 3:

```text
F_adj = 1 - 1/9 = 8/9.
```

The runner repeats this calculation with `sympy.Rational` and checks the
algebraic rearrangement step independently.

## Dependencies

- [`ew_current_fierz_channel_decomposition_note_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  for the Fierz channel-count (decoration-level authority supplying the
  singlet count `1`, adjoint count `N_c^2 - 1`, total `N_c^2`).
- [`yt_ew_color_projection_theorem`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  for the parent theorem whose exact-rational-arithmetic half this note
  isolates. The parent remains audited_conditional on `kappa_EW`.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This note does not close:

- the `kappa_EW = 0` derivation (lattice-current disconnected coefficient);
- the unconditional `9/8` projection in the parent
  `yt_ew_color_projection_theorem`;
- the lattice-current matching rule (which channel the physical EW current
  couples to);
- any continuum-limit numerical claim such as a mass or coupling value;
- any follow-on proof-walk for other algebraic bookkeeping notes;
- any parent theorem/status promotion.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/yt_ew_f_adj_fierz_runner.py
```

Expected:

```text
TOTAL: PASS=2 FAIL=0
VERDICT: bounded proof-walk passes; F_adj = (N_c^2 - 1)/N_c^2 = 8/9 at
N_c = 3 is exact rational arithmetic from the cited Fierz channel-count.
```
