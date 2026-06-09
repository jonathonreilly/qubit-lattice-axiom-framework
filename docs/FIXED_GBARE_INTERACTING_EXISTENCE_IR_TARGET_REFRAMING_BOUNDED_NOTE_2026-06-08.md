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
  fixed nonzero bare coupling, not the standard `g_bare -> 0` continuum endpoint;
- standard asymptotic-scaling arithmetic says the `a -> 0` endpoint is reached
  only in the weak-coupling limit;
- therefore this repo's fixed-`g_bare` interacting-existence target should be
  stated as a fixed-lattice IR gap/clustering target, with the pure-gauge
  `Delta_gauge(beta=6)>0` problem still open.

This is a reframing/support theorem, not an existence theorem.

## Inputs

- [`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md) supplies the
  retained-bounded `g_bare=1`, `beta=6` Wilson-surface convention.
- [`QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02.md`](QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02.md)
  supplies the retained-bounded one-loop full-SM SU(3) coefficient `b_3=7`.
- [`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md`](INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
  isolates the retained-bounded matter-sector gap floor and records the
  pure-gauge `beta=6` gap as open.
- The two-loop coefficient `b_1=26`, the asymptotic-scaling formula, and the
  dimensional-transmutation estimate are standard RG method inputs evaluated in
  the runner; they are not claimed as newly derived framework primitives.

## Runner Result

The runner reports `TOTAL: PASS=14 FAIL=0`.

It verifies:

1. `b_0=7` and `b_1=26` for the full-SM SU(3) instance under the stated standard
   RG formulas, with `b_0>0`.
2. In the perturbative asymptotic-scaling formula, `a(g)` decreases toward zero
   as `g -> 0`; this is the standard UV-continuum endpoint.
3. A non-asymptotically-free sign control runs in the opposite direction under
   the same diagnostic.
4. `g_bare=1` gives `beta=6` and is not `g_bare=0`; the runner's
   two-loop/one-loop diagnostic places it at a finite scaling-onset coupling,
   not deep in the asymptotic regime.
5. The fixed bare coupling gives a finite dimensional-transmutation scale in
   the runner's one-loop estimate, `mu_conf/mu_lattice ~= 3e-5`.

## Reframing

The standard constructive continuum problem asks for an interacting
`a -> 0` limit. This framework's fixed `g_bare=1` lattice does not take that
limit in this note. On that fixed lattice, the live existence target is IR:
mass gap, clustering, and transfer-matrix control at `beta=6`.

The open input is exactly the one already isolated by the interacting transfer
note: the pure-gauge `Delta_gauge(beta=6)>0` gap, plus the coupled spectral
control needed to lift the matter-sector floor to the full interacting theory.

## Boundaries

- This note does not prove `Delta_gauge(beta=6)>0`, full interacting
  `Delta_T>0`, clustering, OS reconstruction, or any continuum `a -> 0` limit.
- It does not claim that asymptotic freedom by itself proves a nonperturbative
  continuum theory exists; it uses AF/sign arithmetic only as the standard
  weak-coupling scaling diagnostic.
- It does not treat the scale-reference primitive, Planck units, or a physical
  scale assignment as a bounded-status source.
- It does not create a new axiom, primitive, action, measure, selector, or audit
  verdict.

## Safe Wording

Use:

> On the retained-bounded `g_bare=1` Wilson surface, the repo is not taking the
> standard `g_bare -> 0` UV-continuum endpoint. The interacting-existence target
> is therefore the fixed-lattice IR gap/clustering problem at `beta=6`; the
> pure-gauge gap remains open.

Do not use:

> The framework has proven interacting QFT existence, solved standard continuum
> Yang-Mills, or derived the continuum limit from asymptotic freedom.
