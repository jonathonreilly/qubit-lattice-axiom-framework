# SU(3) Beta=6 Lattice-Units Gap Conditional Reduction Diagnostic

**Date:** 2026-06-09
**Claim type:** open_gate / conditional fixed-lattice reduction
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py`](../scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py)
**Runner cache:**
[`logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt`](../logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt)

## 2026-06-12 audit firewall: reduction, not beta=6 gap theorem

The audited missing bridge is the actual physics wall: this packet does not
prove the no-second-order-bulk-critical-point premise on the 4D `SU(3)`
fundamental-Wilson axis through `beta=6`, nor does it supply a retained
small-beta transfer-matrix/positive-gap bridge all the way to that point. It
also does not make the framework's Lattice axiom supply a Wilson action,
coupling convention, transfer matrix, or all-coupling confinement theorem.

The source status is therefore **open-gate conditional reduction**. The
runner-checked content is useful but narrow: if the named no-critical-point
premise and standard fixed-lattice Wilson/gap setting are supplied, then a
zero lattice-units gap at `beta=6` would require a divergent correlation
length, so the supplied premise implies a positive fixed-lattice gap. This
firewall adds no new axiom, no Tier-A admission, and no audit-status change.

## Summary

This note narrows the fixed-lattice `SU(3)` gap question at the framework's
`beta=6` bare-coupling convention to one explicit premise:

```text
No second-order bulk critical point occurs on the 4D SU(3)
fundamental-Wilson axis in 0 < beta <= 6.
```

If that premise is granted, then the fixed-spacing lattice-units `0++` gap at
`beta=6` is positive. The reason is simple: in infinite volume the gap is
`m(beta)=1/xi(beta)`, so a zero gap at or before `beta=6` is exactly a divergent
correlation length on that Wilson axis. A first-order bulk jump does not by
itself close the gap because the correlation length remains finite on both
sides.

The premise is not proven here. Monte Carlo literature supports it as a
comparator: the 4D `SU(3)` fundamental Wilson axis shows a finite crossover
near `beta ~= 5.5`, not a volume-scaling divergence. The constructive proof of
that no-critical-point premise remains the open Balaban-class / RG-control
problem.

## Runner-Checked Content

The runner checks only bounded diagnostics around this reduction:

- exact `SU(3)` Weyl-measure class quadrature for one-plaquette class functions;
- the small-`beta` character-norm convention `u(beta)/beta -> 1/18`;
- positivity of the leading strong-coupling single-plaquette coefficient in the
  standard strong-coupling window, as a diagnostic tied to the cited
  convergent character expansion;
- monotone weakening of the leading coefficient toward weaker coupling;
- a finite positive-kernel illustration of the Perron-Frobenius mechanism;
- the non-perturbative weak-coupling scale being invisible to all checked
  perturbative orders;
- the leading strong-coupling extrapolation missing the `beta=6` comparator
  window by a large factor;
- guardrails that keep the note conditional and fixed-lattice only.

`TOTAL: PASS=10 FAIL=0`.

## Conditional Reduction

Let `m(beta)` denote the infinite-volume lattice-units `0++` gap for the pure
`SU(3)` fundamental-Wilson system at fixed lattice spacing.

Assume:

```text
There is no second-order bulk critical point on the SU(3)
fundamental-Wilson axis for 0 < beta <= 6.
```

Then `m(6) > 0`, conditional on the standard strong-coupling existence of a
positive lattice-units gap at small `beta` and the absence of any intervening
correlation-length divergence.

This is a reduction theorem, not an unconditional mass-gap theorem. It isolates
the one premise that would still have to be proven to make the fixed-lattice
`beta=6` statement unconditional.

## What This Does Not Claim

- Not an unconditional `beta=6` gap.
- Not a physical-units or continuum mass-gap theorem, and not a Clay-problem
  result.
- Not a `Lambda_QCD`, observed-spectrum, or Planck-scale statement.
- Not an import of a physical scale through the scale-reference primitive.
- Not an axiom, primitive, or Tier-A admission.
- Not a claim that the lattice axiom supplies the Wilson action, gauge weight,
  transfer matrix, or coupling convention.
- Not an all-coupling confinement proof.
- Not an audit verdict or status promotion.

## Comparator Status

The following numbers are comparators only and are not derivation inputs:

- finite crossover near `beta ~= 5.5` in 4D `SU(3)` fundamental-Wilson studies;
- `a sqrt(sigma) ~= 0.22`, equivalently `sigma a^2 ~= 0.048`, at `beta=6`;
- `m_0++ a ~= 0.8` at `beta=6`.

These comparators make the premise empirically plausible and falsifiable, but
they do not prove it inside the framework.

## Reprove-and-Cite Ledger

- **Runner-checked here:** the Weyl-measure quadrature, the small-`beta`
  normalization check, the leading coefficient diagnostics, the positive-kernel
  Perron-Frobenius illustration, the weak-side non-analyticity check, and the
  strong-side breakdown comparison.
- **Cited rather than reproven here:** the convergent strong-coupling
  character/cluster expansion and gap at sufficiently small `beta`, the
  transfer-matrix construction for compact lattice gauge theory, the Monte
  Carlo crossover evidence on the `SU(3)` Wilson axis, and the Balaban-class
  constructive route.

## Dependencies

- [FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md](FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md)
  supplies the fixed-lattice gauge-existence scope this note is reducing.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) supplies only
  the repo's axiom boundary. It does not supply the Wilson action, the
  no-critical-point premise, or a physical scale.

## Honest Auditor Read

Audit this as a conditional fixed-lattice reduction plus supporting diagnostics.
The durable claim is:

```text
If the 4D SU(3) fundamental-Wilson axis has no second-order bulk critical point
for 0 < beta <= 6, then the fixed-spacing lattice-units gap at beta=6 is
positive.
```

The open item is exactly the proof of that no-critical-point premise. Comparator
evidence can motivate the premise, but it does not turn the conditional result
into an unconditional one.

## 2026-06-15 audit-unlock residual certificate

This row is re-opened only as a conditional reduction. The runner supplies
bounded one-plaquette, strong-coupling, positive-kernel toy, and comparator
guardrail checks; those are diagnostics, not a proof of the physical Wilson
axis gap.

The exact missing object is a framework-native theorem ruling out a
second-order bulk critical point on the relevant 4D SU(3) Wilson axis up to
`beta = 6`, or an equivalent transfer-matrix/gap bridge with the same scope.
Until that theorem exists, this packet remains an open-gate reduction and
does not claim a beta=6 gap. No new lattice fact, external simulation result,
or audit status is introduced here.

## 2026-06-16 transfer-kernel dependency-edge repair

The latest audit also named the standard fixed-lattice Wilson
transfer-matrix/gap setting as part of the restricted packet boundary. This
source-side repair adds the already audited-clean, retained-bounded in-repo
authorities that carry the Wilson transfer-kernel positivity/RP side:

- [`WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md`](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)
  proves the SU(3) Wilson temporal-gauge transfer kernel is positive
  semidefinite for `beta >= 0` as the gauge-kernel positivity half.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  supplies the bounded Wilson-plaquette temporal-gauge RP bridge for the
  gauge-half norm-square application.

These dependencies close only the source-graph route to the Wilson
transfer-kernel/RP setting used by the conditional reduction. They do not prove
the no-second-order-bulk-critical-point premise, do not propagate a small-beta
gap to `beta=6`, and do not turn this row into an unconditional gap theorem.

## 2026-06-17 restricted packet verifier

The re-audit packet is now pinned by
[`scripts/su3_beta6_gap_reaudit_packet_verifier_2026_06_17.py`](../scripts/su3_beta6_gap_reaudit_packet_verifier_2026_06_17.py),
with cached output at
[`logs/runner-cache/su3_beta6_gap_reaudit_packet_verifier_2026_06_17.txt`](../logs/runner-cache/su3_beta6_gap_reaudit_packet_verifier_2026_06_17.txt).

The verifier checks that this parent reduction, the explicit-constant
analyticity floor, and the Wilson transfer-kernel/RP support notes remain
SHA-fresh and keep their non-promotion boundary language. It deliberately
packages only bounded source support: it does not prove the missing
no-second-order-bulk-criticality theorem on the remaining window, does not
claim a beta=6 gap, and does not retag any ledger row.
