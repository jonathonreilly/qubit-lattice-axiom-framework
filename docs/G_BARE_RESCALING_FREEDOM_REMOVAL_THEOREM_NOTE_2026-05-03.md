# g_bare Rescaling Conditional Algebra Lemma

**Date:** 2026-05-03. Repair narrowing: 2026-05-25.
**Claim type:** bounded_theorem.
**Status authority:** independent audit lane only.
**Status:** unaudited repair candidate. This note does not apply an audit
verdict and does not promote any downstream `g_bare` row.
**Primary runner:** `scripts/frontier_g_bare_rescaling_conditional_algebra_check.py`

## 0. Audit Repair Boundary

The latest audit blocker for
`g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` was:

```text
missing_dependency_edge: add a retained one-hop dependency for the Wilson
plaquette matching/action-surface premise, or narrow the row title and scope
to an explicitly conditional-on-Wilson-matching algebraic lemma.
```

This revision takes the second path. The row is no longer a theorem that
removes all continuum rescaling freedom from retained first principles. It is
only the conditional algebraic lemma:

```text
CN + WM + rescaling by c  =>  Gram -> c^2 Gram and beta -> c^2 beta.
```

Here:

- **CN** is the canonical trace normalization
  `Tr(T_a T_b) = delta_ab / 2`, supplied by the retained CL3 color algebra
  authority [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md).
- **WM** is the scoped Wilson matching relation
  `beta = 2 N_c / g_bare^2`.
- The Wilson action surface and the matching relation are scoped inputs to
  this lemma, not retained conclusions proved here.

## 1. The Narrowed Claim

> **Lemma (conditional rescaling algebra).**
> Assume:
>
> 1. `Tr(T_a T_b) = delta_ab / 2` on the canonical SU(3) triplet carrier.
> 2. The Wilson matching relation `beta = 2 N_c / g_bare^2`.
> 3. A scalar rescaling of the carrier/connection normalization by `c`,
>    with `c^2 != 1`.
>
> Then exact algebra gives
>
> ```text
> Tr((c T_a)(c T_b)) = c^2 delta_ab / 2,
> beta_new = c^2 beta_old,
> g_bare^2 remains the same scoped symbol in WM.
> ```
>
> Therefore a nontrivial scalar rescaling does not preserve the same
> canonical-normalization plus fixed-beta surface. It changes the trace
> normalization and, under scoped WM, routes the scale into `beta`.

This is a class-A algebraic implication over the listed inputs.

## 2. What Is Not Claimed

This repair intentionally removes the stronger claims that caused the audit
blocker. The note does not claim:

- that the Wilson plaquette action surface is uniquely selected from A1+A2;
- that Wilson matching is itself retained by this row;
- that all continuum rescaling freedom is removed from first principles;
- that `g_bare = 1` follows;
- that `G_BARE_DERIVATION_NOTE.md` is retained or promoted.

The only load-bearing retained authority cited by this note is the CL3 color
algebra authority for the trace-normalized SU(3) carrier. Wilson matching is
an explicit scoped assumption of the lemma.

## 3. Runner Slice

The primary runner is
`scripts/frontier_g_bare_rescaling_conditional_algebra_check.py`.
It checks, using exact rational arithmetic:

- the retained CL3 dependency is present;
- for nontrivial `c^2` values, the Gram matrix scales by `c^2`;
- under scoped WM, `beta_new / beta_old = c^2`;
- the target row has only the CL3 load-bearing dependency after pipeline
  regeneration.

## 4. Proposed Audit-Lane Disposition

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Conditional algebra only: assuming canonical trace normalization CN and
  Wilson matching beta = 2 N_c / g_bare^2, a scalar carrier/connection
  rescaling by c changes the canonical Gram by c^2 and changes the matched
  beta by c^2. The row does not derive Wilson matching, does not prove
  action-surface uniqueness, and does not promote downstream g_bare claims.
proposed_load_bearing_step_class: A
declared_one_hop_dep: cl3_color_automorphism_theorem
audit_required_before_effective_retained: true
parent_update_allowed_only_after_retained: true
```

## 5. Cross-References

The only load-bearing markdown citation in this note is the retained CL3
color algebra authority linked in Section 0. Related rows such as
`G_BARE_DERIVATION_NOTE.md`,
`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`,
`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`, and
`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` are reader
context only and are intentionally not cited as load-bearing authorities
here.
