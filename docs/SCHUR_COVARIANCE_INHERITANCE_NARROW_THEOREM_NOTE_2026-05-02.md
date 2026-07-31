# Schur Complement Covariance Inheritance — Narrow Theorem

**Date:** 2026-05-02
**Type:** positive_theorem (proposed; audit-lane to ratify)
**Primary runner:** `scripts/frontier_schur_covariance_inheritance_narrow.py`
**Runner cache:** `logs/runner-cache/frontier_schur_covariance_inheritance_narrow.txt`

## Claim scope (proposed)

> Let `V = V_1 ⊕ W` be a finite-dimensional inner-product space with
> a unitary group action `U = U_1 ⊕ U_W` (block-diagonal in the splitting).
> Let `M` be a Hermitian operator on `V` with block decomposition
> `M = [[A, B], [B†, D]]` and assume:
> 1. `U M U† = M` (group covariance of `M`),
> 2. `D` is invertible.
>
> Then the Schur complement `S = A − B D⁻¹ B†` on `V_1` satisfies
> `U_1 S U_1† = S`, i.e. `S` inherits the `U_1`-covariance.

This is a pure representation-theory / linear-algebra result. It **does
not** claim:

- that any physical operator decomposes this way;
- applicability to charged-lepton effective operators specifically;
- that `D` is invertible in physical settings;
- that the Schur reduction is the physical reduction map.

The narrow theorem provides a clean, reusable structural lemma that
downstream Koide / DM / charged-lepton notes can cite without inheriting
broader scope-creep.

## Cited theorem authority (one hop)

| Authority | Role |
|---|---|
| [`SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md`](SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md) | ordinary theorem authority giving taste-cube / Brillouin-zone-corner context for downstream consumers |

The cited theorem is not a registered framework primitive and is not a
premise of the general proof below, which applies to any unitary group and
any Hermitian operator satisfying the displayed hypotheses. Its current
status belongs to the audit ledger; the runner reads the tracked dependency
shard only as an executable dependency guard.

## Load-bearing step (class A)

Block expansion of `U M U† = M`:
```text
U_1 A U_1† = A,           (top-left block)
U_1 B U_W† = B,           (top-right block)
U_W D U_W† = D.           (bottom-right block)
```

From the third equation: `U_W† D U_W = D`, i.e. `U_W` commutes with `D`,
hence with `D⁻¹`. Then:

```text
U_1 S U_1†
  = U_1 A U_1†  -  U_1 B D⁻¹ B† U_1†
  = A           -  (U_1 B U_W†) (U_W D⁻¹ U_W†) (U_W B† U_1†)
  = A           -  B · D⁻¹ · B†
  = S.
```

The middle line uses `U_W U_W† = I` inserted twice (group unitarity), then
identifies `U_1 B U_W† = B` and the dual `U_W B† U_1† = B†` from the
top-right block equation. This is class (A) — algebraic identity on
abstract block matrix relations.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_schur_covariance_inheritance_narrow.py
```

Verifies with SymPy exact integer/rational matrix arithmetic:

1. The lemma holds on the canonical 3+1 split with `V_1 = ℂ³`, `W = ℂ¹`,
   `U_1 = C₃[111]`, for both `U_W = +1` and `U_W = -1`. In the sign case,
   these are the actions of one common `C₆` generator: the `V_1` action
   factors through `C₃`, while the `W` action factors through `C₂`.
   Covariance forces `B = 0` because `-1` is not in the spectrum of `C₃`;
   the runner checks this edge case explicitly.
2. The lemma holds on a 3+3 split with `V_1 = V_W = ℂ³` and the distinct
   actions `U_1 = C₃`, `U_W = C₃²`, using a nonzero orbit-summed
   intertwiner `B`.
3. Twelve deterministic seeded random 3+3 fixtures, covering all four pairs
   `U_1, U_W ∈ {C₃, C₃²}`. Each fixture constructs exact invariant
   Hermitian `A,D`, an exact nonzero intertwiner `B`, and checks Hermiticity,
   `det(D) ≠ 0`, covariance of `D⁻¹`, and both full and Schur covariance
   without floating-point tolerances.
4. Premise-rejection controls verify that a mixing (non-block-diagonal)
   unitary lies outside the theorem's scope and that a deliberately
   non-covariant `M` has a non-covariant Schur complement in the test fixture.
5. The retained-authority guard reads the canonical tracked sharded ledger
   row directly, so it runs in an audit packet without the untracked
   monolithic `audit_ledger.json` cache.

## Audit-lane disposition (proposed)

```yaml
target_claim_type: positive_theorem
proposed_claim_scope: |
  pure representation-theory / linear-algebra Schur complement covariance
  inheritance: U M U† = M block-diagonal ⇒ U_1 S U_1† = S where S is the
  Schur complement onto V_1; no physical-applicability claim.
proposed_load_bearing_step_class: A
audit_required_before_effective_retained: true
```

Audit status is set only by the independent audit lane. Effective status is
pipeline-derived from `claim_type` and current dependency closure.

## What this theorem closes

A clean, reusable Schur covariance inheritance lemma that downstream Koide
and DM lanes can cite without scope-creep concerns. The lemma is purely
mathematical; physical applicability is a separate downstream claim.

## What this theorem does NOT close

- Applicability to physical charged-lepton effective operators.
- The KOIDE_FULL_LATTICE_SCHUR_INHERITANCE_NOTE_2026-04-18 row's broader
  claim chain.
- Existence of the Schur reduction in physical settings (assumed in
  premise; out of scope).

## Cross-references

- [`SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md`](SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md) — ordinary theorem authority giving
  taste-cube / Brillouin-zone-corner context for downstream consumers; not
  a premise of this general lemma.
- KOIDE_FULL_LATTICE_SCHUR_INHERITANCE_NOTE_2026-04-18.md — parent
  Koide-Schur application for which this note provides the underlying
  lemma. This parent application is not a load-bearing dependency for the
  narrow lemma.
- Cycle 1 (PR #292) — sister narrow theorem: LH-doublet eigenvalue ratio.
- Cycle 2 (PR #293) — sister narrow theorem: Koide cyclic 3-response.
