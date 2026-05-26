# Gauge-Normalization Trace-Form Rigidity Lemma

**Date:** 2026-04-14. Repair narrowing: 2026-05-25.
**Claim type:** bounded_theorem.
**Status authority:** independent audit lane only.
**Status:** unaudited repair candidate. This note does not apply an audit
verdict and does not promote any downstream `g_bare` row.
**Primary runner:** `scripts/frontier_g_bare_rigidity_trace_form_check.py`

## 0. Audit Repair Boundary

The latest audit blocker for `g_bare_rigidity_theorem_note` was:

```text
missing_bridge_theorem: add a retained derivation or retained cite for
U = exp(i A_op a) from the framework's discrete gauge primitives, or keep
the row explicitly conditional on (HF).
```

Earlier source text tried to keep the holonomy form `(HF)` as an explicit
admission, but the row still carried a `g_bare` / no-free-coupling conclusion
through that open holonomy dictionary. This repair narrows further: the
retained candidate is only the trace-form algebraic core and does not use
the holonomy form.

## 1. Load-Bearing Dependencies

The algebraic carrier is supplied by retained upstream rows:

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md):
  structural finite-cube SU(3) carrier, excluding physical SM color and
  electroweak readouts.
- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md): native
  cubic Cl(3) taste algebra plus retained graph-first structural SU(3),
  excluding abelian/electroweak/matter/Wilson/phenomenology claims.

No holonomy, Wilson action, physical coupling, or continuum gauge dictionary
authority is load-bearing for this narrowed row.

## 2. The Narrowed Claim

> **Lemma (trace-form rigidity).**
> On the retained finite SU(3) carrier with Hilbert-space trace form fixed,
> choose a canonical Hermitian traceless basis `{T_a}` satisfying
>
> ```text
> Tr(T_a T_b) = delta_ab / 2.
> ```
>
> Then:
>
> 1. Orthogonal rotations of the basis preserve the Gram matrix
>    `Tr(T_a T_b)`.
> 2. A uniform scalar dilation `T_a -> lambda T_a` with `lambda^2 != 1`
>    changes the Gram matrix to `lambda^2 delta_ab / 2`.
> 3. Therefore scalar dilation is not an allowed ambiguity of the canonical
>    trace-normalized basis.

This is a class-A finite-dimensional algebra statement over the supplied
carrier and fixed trace form.

## 3. What Is Not Claimed

This note no longer claims:

- a derivation of the lattice holonomy form `U = exp(i A_op a)`;
- a derivation of `g_bare = 1`;
- a removal of all physical bare gauge-coupling freedom;
- Wilson action-surface uniqueness;
- any downstream dark-matter, Higgs, CKM, or strong-CP closure.

Those claims require separate retained bridge theorems before they can use
this row as support.

## 4. Runner Slice

The primary runner is `scripts/frontier_g_bare_rigidity_trace_form_check.py`.
It verifies:

- retained dependency status for the two structural SU(3) carrier rows;
- canonical `Tr(T_a T_b) = delta_ab / 2` for the standard SU(3) basis;
- invariance of the Gram matrix under orthogonal basis rotation;
- failure of Gram preservation under scalar dilation;
- post-pipeline dependency routing for this target row.

## 5. Proposed Audit-Lane Disposition

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Finite-dimensional trace-form rigidity only: on the retained structural
  SU(3) carrier with fixed Hilbert-space trace form, orthogonal basis
  rotations preserve Tr(T_a T_b)=delta_ab/2 while scalar dilations do not.
  The row does not derive a lattice holonomy, does not assert g_bare=1, and
  does not remove physical gauge-coupling freedom.
proposed_load_bearing_step_class: A
declared_one_hop_deps:
  - graph_first_su3_integration_note
  - native_gauge_closure_note
audit_required_before_effective_retained: true
parent_update_allowed_only_after_retained: true
```

## 6. Cross-References

The only load-bearing markdown citations are the two retained structural
SU(3) carrier rows linked in Section 1. Related rows such as
`G_BARE_DERIVATION_NOTE.md`,
`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`, and
`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md` are reader
context only and are intentionally not cited as load-bearing authorities.
