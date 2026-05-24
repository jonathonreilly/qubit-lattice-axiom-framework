# Universal GR Invariant-Frame Obstruction Note

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-14 (load-bearing claim narrowed 2026-05-24 per audit verdict)
**Branch:** `codex/review-active`  
**Scope:** universal representation/invariant route only  
**Purpose:** record the bounded representation-theoretic obstruction
information that is algorithmically verified inside the runner.

**Script:** `scripts/frontier_universal_gr_invariant_frame_obstruction.py`

## 2026-05-24 narrowing — load-bearing claim restricted

The previous audit on this row returned `audited_conditional` with re-audit
guidance:

> other: include or cite a retained theorem/runner over the current
> checkout proving atlas exhaustion and absence of invariant section
> selectors, and restore or register the weight-decomposition artifact.

This revision narrows the **load-bearing claim** of this row to the
algorithmically verified bounded facts about the representation-theoretic
decomposition. Specifically, the load-bearing piece is restricted to the
runner-verified statements about the `Pi_A1` invariant section, the
spatial-rotation generator algebra, and the shared-axis weight
decomposition / weight-1 multiplicity space. The stronger meta-statement
that "no representation-theoretic invariant in the *current atlas* selects
a unique universal complement frame" requires an atlas-exhaustion proof
that this note does not derive from a retained authority and is **demoted
to a non-load-bearing conditional corollary** for this row's audit scope.

The weight-decomposition artifact is registered by being recomputed live by
the runner on each invocation; the runner's PASS line "shared-axis
complement weight decomposition has two weight-1 doublets and one weight-2
sector" records the explicit weight multiplicities `{0: 4, 1: 4, 2: 2}` and
doublet counts `{1: 2, 2: 1}` as a runner-attested artifact rather than as
a file.

## Bounded result (load-bearing, 2026-05-24)

The runner verifies the following facts about the universal complement
under the canonical lapse/shift/trace/shear basis on the symmetric `3+1`
sector and the rank-2 invariant projector
`Pi_A1 = diag(1,0,0,0,1,0,0,0,0,0)`:

1. `Pi_A1` is rank 2 and commutes with the tested spatial rotations to
   machine precision (Frobenius norm `< 1e-12`).
2. The full spatial-rotation generator algebra on the universal `3+1`
   basis has rank 3 and acts nontrivially on the complement
   (Frobenius norm `> 1e-6` on each axis).
3. The shared-axis weight decomposition of the universal complement under
   the residual `SO(2)` stabilizer has weight multiplicities
   `{0: 4, 1: 4, 2: 2}` — i.e. four invariant directions, two weight-1
   doublets, and one weight-2 sector.
4. The two weight-1 doublets sit in a multiplicity space whose real
   commutant has dimension 8, so the canonical `SO(2)` doublet model does
   not single out a preferred basis within that block.
5. The unique symmetric `3+1` quotient kernel has a frame-invariant
   spectrum (maximum spectral delta under tested rotations is `0` to
   machine precision).

These are the load-bearing facts of this row. They are exact bounded
representation-theoretic statements on the canonical basis used inside the
runner and do not depend on an atlas-exhaustion proof.

## Strongest invariant-frame candidate

The strongest invariant-frame candidate currently supported is the
`Pi_A1`-anchored orbit bundle:

`P_curv^cand = (Pi_A1, O_{E \oplus T1}, \omega_MC)`

with the exact residual gauge `SO(3)`.

This is an invariant core plus an orbit bundle. The complement is
**orbit-canonical** under the verified spatial-rotation generator algebra
(items 2-4 above) — i.e. on the canonical basis tested by the runner, no
weight-1 doublet is selected by the canonical `SO(2)` doublet model. The
runner does not, however, prove an atlas-exhaustion statement that would
extend this to all representation-theoretic invariants.

## Non-load-bearing remarks (preserved for historical traceability)

The following remarks are **not** load-bearing for this row per the
2026-05-24 narrowing. They depend on imports that are not closed here.

The previous framing of this row asserted as a no-go that
"representation-theoretic invariants alone do not canonically fix the
universal complement frame", treating the canonical-basis weight
decomposition (items 3-4 above) as evidence for an atlas-exhaustion
conclusion. Under the 2026-05-24 narrowing this stronger meta-statement is
explicitly **non-load-bearing**: the bounded result this row supports is
the runner-verified facts on the canonical basis, not an exhaustion claim
over an unspecified atlas of invariants.

The shared-axis decomposition's two equivalent weight-1 doublets remain
the structural obstacle: representation-theoretic invariants on the
canonical basis can identify the isotypic block but cannot choose a
preferred basis within that block. Equivalently, the normalized lift
family

`L_lambda(D) = (cos(lambda) D, sin(lambda) D)`

survives exactly because the weight-1 multiplicity space is not broken by
the canonical-basis tensors the runner checks.

## What the runner checks

The runner `frontier_universal_gr_invariant_frame_obstruction.py` performs
explicit `[PASS]/[FAIL]` checks and emits `PASS=<n> FAIL=<m>`:

- the scalar generator note records the observable-principle output
  `det(D + J) - det D` (text presence in retained authority note);
- the `3+1` lift note records the `PL S^3 x R` lift (text presence);
- the symmetric quotient kernel uniqueness is recorded;
- `Pi_A1` is exact rank-2, commutes with valid spatial rotations;
- the complement carries the rank-3 spatial-rotation generator algebra;
- the shared-axis weight decomposition has the multiplicities above;
- the weight-1 multiplicity commutant has dimension 8;
- the quotient-kernel spectrum is frame-invariant;
- the A1 invariant section note is present and records the lapse / trace
  identification;
- the weight decomposition is recorded in this note (text presence) and
  recomputed by the runner.

A successful run prints `PASS=13 FAIL=0` and exits with status `0`.

## Honest status

The current universal representation/invariant route is, with respect to
the runner-verified canonical basis:

- exact at the scalar observable level (imported);
- exact at the `3+1` kinematic lift level (imported);
- exact at the symmetric quotient-kernel level (imported);
- exact at the invariant `A1` projector level (verified by the runner);
- on the canonical basis tested, the complement is **orbit-canonical**
  under the tested rotation algebra, not section-canonical (verified by
  the runner).

The complement is orbit-canonical, not section-canonical, in the bounded
sense above. The further atlas-exhaustion statement is left explicitly
open and is not a load-bearing claim of this row.
