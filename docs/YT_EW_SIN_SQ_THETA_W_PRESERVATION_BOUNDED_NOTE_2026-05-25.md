# Weinberg Angle Preservation Under K_EW Bounded Note

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/yt_ew_sin_sq_theta_w_preservation_runner.py`](../scripts/yt_ew_sin_sq_theta_w_preservation_runner.py)

## Claim

Given the `K_EW` correction in
[`yt_ew_color_projection_theorem`](YT_EW_COLOR_PROJECTION_THEOREM.md) —
namely `g_a -> K_EW(kappa_EW) * g_a` applied universally for
`a` in `{Y, 1, 2}` — the Weinberg angle ratio

```text
sin^2(theta_W) = g_Y^2 / (g_Y^2 + g_2^2)
```

is invariant under any value of `kappa_EW`. This is the
multiplicative-universality consequence of the parent theorem's correction
structure; the universal factor `K_EW(kappa_EW)` cancels identically in
the numerator and denominator of the ratio.

This bounded proof-walk uses only:

- multiplicative universality of `K_EW` (the same factor multiplies
  `g_Y`, `g_1`, and `g_2`, cited from the parent theorem);
- cancellation of a common non-zero multiplicative factor in the
  numerator and denominator of a ratio;
- the formal scalar ratio `s^2 = g_Y^2 / (g_Y^2 + g_2^2)` from the
  defined finite-dimensional algebra in
  [`ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md).

The cited theorem does not identify this ratio with a physical weak angle or
select electroweak couplings. Such an identification is an additional premise
of this note's SM interpretation and is not supplied by the algebraic ratio.

This note isolates the `kappa_EW`-independent multiplicative-universality
consequence of
[`yt_ew_color_projection_theorem`](YT_EW_COLOR_PROJECTION_THEOREM.md)
(which is `audited_conditional`). The `kappa_EW = 0` derivation remains
open per the parent's verdict and the cited
[`ew_current_matching_rule_open_gate_note_2026-05-03`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md).

This note makes no claim about the numerical value of `kappa_EW` itself,
nor about the unconditional `9/8` (or any other) projection on individual
`g_a`. It is a bounded proof-walk of an algebraic cancellation; it does
not add a new axiom, a new repo-wide theory class, or a retained status
claim.

## Proof-Walk

| Step | Load-bearing input | New axiom? |
|---|---|---|
| State the parent correction: `g_a -> K_EW(kappa_EW) * g_a` for `a` in `{Y, 1, 2}` | parent theorem `yt_ew_color_projection_theorem` (audited_conditional) — multiplicative universality across EW couplings | no |
| State the formal ratio `s^2 = g_Y^2 / (g_Y^2 + g_2^2)` | defined `C^2` quadratic-form theorem; physical weak-angle interpretation remains separate | no |
| Substitute the parent correction into the ratio | `sin^2(theta_W)' = (K_EW g_Y)^2 / ((K_EW g_Y)^2 + (K_EW g_2)^2)` | no |
| Factor `K_EW^2` from numerator and denominator | exact-rational algebra; `K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)` is non-zero for all real `kappa_EW` not equal to `-8`, in particular for `kappa_EW = 0` (the named matching condition) | no |
| Cancel the common `K_EW^2` factor | `sin^2(theta_W)' = g_Y^2 / (g_Y^2 + g_2^2) = sin^2(theta_W)` | no |
| Conclude `kappa_EW`-independence | algebraic invariance, no value of `kappa_EW` chosen | no |

The checked proof path does not cite the Wilson plaquette action,
staggered phases, Brillouin-zone labels, link unitaries, lattice scale,
`u_0`, a Monte Carlo measurement, or a fitted observational value. It
does not derive `kappa_EW` or `K_EW(0) = 9/8`.

## Exact Arithmetic Check

With `K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)` at `N_c = 3` (from the
parent theorem), substituting `g_Y -> K_EW g_Y` and `g_2 -> K_EW g_2`
into the SM Weinberg ratio gives

```text
sin^2(theta_W)' = (K_EW g_Y)^2 / ((K_EW g_Y)^2 + (K_EW g_2)^2)
                = K_EW^2 g_Y^2 / (K_EW^2 (g_Y^2 + g_2^2))
                = g_Y^2 / (g_Y^2 + g_2^2)
                = sin^2(theta_W).
```

The runner repeats this with symbolic `g_Y`, `g_2`, `kappa_EW` and
verifies `sympy.simplify(sin_sq_after - sin_sq_before) == 0` over the
rational extension. It also evaluates at the connected-trace
specialization `kappa_EW = 0` (giving `K_EW = 9/8`) and at a
counterfactual `kappa_EW = 1` (giving `K_EW = 1`) to confirm the
identity is genuinely `kappa_EW`-independent and not a coincidence at a
single value.

## Dependencies

- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  for the `K_EW(kappa_EW)` form and the multiplicative-universality
  structure `g_a -> K_EW * g_a` for `a` in `{Y, 1, 2}` (parent is
  `audited_conditional`; the `K_EW` algebraic form is exact rational
  arithmetic at `N_c = 3`).
- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  for the formal identity `s^2 = g_Y^2 / (g_Y^2 + g_2^2)` only. It does not
  supply the physical SM or weak-angle identification used conditionally here.
- [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
  for the open gate that `kappa_EW = 0` is not derived in the parent
  theorem; this note does not close that gate.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This note does not close:

- the `kappa_EW = 0` specialization itself (named open in the parent
  and in the cited matching-rule gate);
- the unconditional `9/8` individual-coupling projection on `g_Y`, `g_1`,
  or `g_2` (still inherits the parent's `audited_conditional` status);
- the numerical value of `sin^2(theta_W)` at `M_Z` or at the EW scale `v`
  (depends on running, matching, and retained-coupling systematics
  downstream of this proof-walk);
- any parent theorem/status promotion of `yt_ew_color_projection_theorem`;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/yt_ew_sin_sq_theta_w_preservation_runner.py
```

Expected:

```text
TOTAL: PASS=1 FAIL=0
VERDICT: bounded proof-walk passes; sin^2(theta_W) is invariant under
the multiplicative-universality K_EW(kappa_EW) correction.
```
