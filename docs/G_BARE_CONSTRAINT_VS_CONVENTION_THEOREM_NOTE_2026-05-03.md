# g_bare Conditional Algebra Corollary

**Date:** 2026-05-03. Repair narrowing: 2026-05-25.
**Claim type:** bounded_theorem.
**Status authority:** independent audit lane only.
**Status:** unaudited repair candidate. This note does not apply an audit
verdict and does not promote any downstream `g_bare` row.
**Primary runner:** `scripts/frontier_g_bare_constraint_surface_check.py`

## 0. Audit Repair Boundary

The latest audit blocker for
`g_bare_constraint_vs_convention_theorem_note_2026-05-03` was:

```text
missing_dependency_edge: add a retained one-hop authority for the Wilson
beta=6/no-external-scale step, or narrow the row text so the retained claim is
only CN + WM + beta=6 => g_bare^2=1.
```

This revision takes the second path. The retained-grade candidate is no
longer a no-alternative or no-external-scale theorem. It is only the local
conditional algebraic corollary:

```text
CN + WM + beta=6 + N_c=3  =>  g_bare^2 = 1.
```

Here:

- **CN** is the canonical trace normalization
  `Tr(T_a T_b) = delta_ab / 2`, supplied by the retained CL3 color algebra
  authority [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md).
- **WM** is the Wilson matching relation
  `beta = 2 N_c / g_bare^2`.
- **beta=6** is an explicit scoped input to this corollary, not derived here.

## 1. The Narrowed Claim

> **Theorem (conditional algebra only).**
> Assume:
>
> 1. `Tr(T_a T_b) = delta_ab / 2` on the canonical SU(3) triplet carrier.
> 2. `N_c = 3`.
> 3. The Wilson matching relation `beta = 2 N_c / g_bare^2`.
> 4. The scoped Wilson coefficient input `beta = 6`.
>
> Then exact rational arithmetic gives
>
> ```text
> g_bare^2 = 2 N_c / beta = 6 / 6 = 1.
> ```
>
> On the positive-coupling branch, `g_bare = 1`.

This is a class-A algebraic implication over the listed inputs.

## 2. What Is Not Claimed

This repair intentionally removes the stronger claims that caused the audit
blocker. The note does not claim:

- that canonical normalization alone pins the Wilson coefficient `beta=6`;
- that the Wilson plaquette action surface is uniquely selected from A1+A2;
- that all external-scale or alternative-convention routes have been
  enumerated and excluded;
- that `G_BARE_DERIVATION_NOTE.md` is retained or promoted;
- that this corollary closes the separate rescaling-freedom-removal row.

The only load-bearing retained authority cited by this note is the CL3 color
algebra authority for the trace-normalized SU(3) carrier. The Wilson matching
relation and `beta=6` are explicit scoped assumptions of the corollary.

## 3. Runner Slice

The primary runner is
`scripts/frontier_g_bare_constraint_surface_check.py`. The auditable slice
for this row is the exact arithmetic:

```text
N_c = 3
beta = 2 N_c = 6
g_bare^2 = 2 N_c / beta = 1
```

The runner also contains supporting trace-normalization, Wilson-expansion,
and rescaling diagnostics. Those diagnostics are not promoted here into a
retained no-alternative theorem. They are support-only context unless a
separate audit retains the corresponding upstream Wilson action-surface or
rescaling-freedom claim.

## 4. Proposed Audit-Lane Disposition

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Conditional local algebra only: assuming canonical trace normalization
  CN, N_c = 3, Wilson matching beta = 2 N_c / g_bare^2, and scoped input
  beta = 6, exact arithmetic gives g_bare^2 = 1. The row does not derive
  beta = 6, does not exclude external-scale conventions, and does not
  promote the parent g_bare derivation.
proposed_load_bearing_step_class: A
declared_one_hop_dep: cl3_color_automorphism_theorem
audit_required_before_effective_retained: true
parent_update_allowed_only_after_retained: true
```

## 5. Cross-References

The only load-bearing markdown citation in this note is the retained CL3
color algebra authority linked in Section 0. Related rows such as
`G_BARE_DERIVATION_NOTE.md`,
`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`,
`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`, and
`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` are
reader context only and are intentionally not cited as load-bearing
authorities here.
