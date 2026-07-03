# Fixed-`g_bare` Interacting Existence Target: IR Gap Reframing

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Scope:** bounded reframing of the interacting-existence target on the fixed
`g_bare=1` lattice. It does not prove the IR theory exists and does not solve the
standard `a -> 0` continuum Yang-Mills construction problem.
**Primary runner:**
[`scripts/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.py`](../scripts/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.py)
**Runner cache:**
[`logs/runner-cache/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.txt`](../logs/runner-cache/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.txt)

## Summary

The useful result is a target clarification:

- the retained-bounded `g_bare=1` / `beta=6` Wilson-surface convention is a
  fixed nonzero bare coupling, not a zero-coupling endpoint;
- therefore this repo's fixed-`g_bare` interacting-existence target should be
  stated as a fixed-lattice IR gap/clustering target, with the pure-gauge
  `Delta_gauge(beta=6)>0` problem still open.

This is a reframing/support theorem, not an existence theorem.

The 2026-06-09 repair removes the previous standard-RG diagnostic from the
load-bearing packet. No standard RG formula, no two-loop coefficient, no
asymptotic-scaling formula, and no dimensional-transmutation estimate are used
as support for this narrowed claim. Textbook continuum-limit language is
context only; the narrowed content is the framework-native fixed-surface target
clarification.

## Inputs

- [`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md) supplies the
  retained-bounded `g_bare=1`, `beta=6` Wilson-surface convention.
- [`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md`](INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
  isolates the retained-bounded matter-sector gap floor and records the
  pure-gauge `beta=6` gap as open.
- No RG/asymptotic-scaling authority is a dependency of this restricted packet.

## Runner Result

The runner reports `TOTAL: PASS=16 FAIL=0`.

It verifies:

1. The current audit ledger records `G_BARE_DERIVATION_NOTE.md` as
   `retained_bounded`, `audited_clean`, and `bounded_theorem`.
2. The current audit ledger records
   `INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md`
   as retained-bounded and keeps `Delta_gauge(beta=6)>0` open.
3. On the fixed Wilson surface, `beta = 2 N_c / g_bare^2` gives `beta=6` for
   `N_c=3`, `g_bare=1`.
4. `g_bare=1` is fixed and nonzero; this note does not take a zero-coupling
   endpoint.
5. The source note contains the narrowed-scope markers and no longer carries the
   old two-loop/asymptotic-scaling diagnostic strings as load-bearing claims.

## Reframing

This framework's fixed `g_bare=1` lattice does not take a zero-coupling limit in
this note. On that fixed lattice, the live existence target is fixed-lattice IR
gap/clustering and transfer-matrix control at `beta=6`.

The open input is exactly the one already isolated by the interacting transfer
note: the pure-gauge `Delta_gauge(beta=6)>0` gap, plus the coupled spectral
control needed to lift the matter-sector floor to the full interacting theory;
the pure-gauge gap remains open.

## Boundaries

- This note does not prove `Delta_gauge(beta=6)>0`, full interacting
  `Delta_T>0`, clustering, OS reconstruction, or any continuum `a -> 0` limit.
- It does not claim that asymptotic freedom, two-loop running, or standard
  asymptotic scaling proves a nonperturbative continuum theory exists. Those
  standard RG diagnostics are not load-bearing in this narrowed packet.
- It does not treat the scale-reference primitive, Planck units, or a physical
  scale assignment as a bounded-status source.
- It does not create a new axiom, primitive, action, measure, selector, or audit
  verdict.

## Safe Wording

Use:

> On the retained-bounded `g_bare=1` Wilson surface, the repo is not taking the
> zero-coupling endpoint. The interacting-existence target is therefore the
> fixed-lattice IR gap/clustering problem at `beta=6`; the pure-gauge gap remains
> open.

Do not use:

> The framework has proven interacting QFT existence, solved standard continuum
> Yang-Mills, or derived the continuum limit from asymptotic freedom.
