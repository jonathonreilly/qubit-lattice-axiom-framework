# Planck-Mass Conventional Anchor Meta Note

**Date:** 2026-05-27
**Claim type:** meta
**Status:** review-loop source proposal. This note adds no axiom, no theorem,
no numerical prediction, and no audit verdict. The independent audit lane sets
audit and effective status.
**Primary runner:** [`frontier_planck_mass_conventional_anchor_meta_verifier.py`](../scripts/frontier_planck_mass_conventional_anchor_meta_verifier.py)

## Scope

This is a repo-language and audit-routing note for references to the
Planck-mass external scale anchor in hierarchy lanes. It does not derive
`M_Pl`, `m_W`, `v_EW`, `alpha_LM`, or any other dimensional value.

The narrow proposal is:

```text
Purely dimensionless framework data cannot by itself determine an SI-valued
mass, length, time, or energy. Mapping framework units to SI units requires one
dimensional convention/anchor.
```

That is the ordinary Buckingham-Pi / dimensional-analysis fact: dimensionless
inputs determine only dimensionless outputs until a dimensional unit convention
is supplied.

## Meta Claim

When a lane has reduced every structural input except the absolute SI scale,
the remaining Planck-mass scale reference should be described as a
**conventional dimensional anchor** rather than as a hidden theorem step.

Equivalent one-anchor descriptions include:

- a framework lattice spacing in meters;
- a Planck mass in GeV;
- a value of `hbar`, `c`, and `G` in SI units sufficient to choose the
  meter/second/kilogram conversion;
- an experimentally maintained clock-frequency convention used to define an SI
  second.

These are different coordinate choices for one dimensional anchor. Selecting
one of them does not create a framework derivation of the dimensional value.

## Boundaries

This note does not:

- change the minimal axiom surface;
- add a repo-wide axiom, primitive, or physics import;
- retire any existing admission or audit row;
- promote any hierarchy, lepton, electroweak, Planck, or publication claim;
- use observed comparator values as derivation inputs;
- assert that a downstream formula has any audit-ratified status.

It only proposes native wording for this residual:

```text
Planck-mass conventional anchor
```

rather than an overloaded branch-local label.

## Precedent

The repo already has convention-scope notes such as
[`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md`](CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md)
and
[`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md).
This note asks the audit lane to treat the Planck-mass anchor wording as the
same kind of meta-scope question: language and routing, not theorem promotion.

## Downstream Use

If independently ratified, downstream notes may say that a result is specified
up to one Planck-mass conventional anchor. They still may not claim a
zero-anchor SI prediction, and they still may not promote any dimensional
prediction without a separate audit-ratified derivation of all
non-conventional inputs.

If the audit lane declines this framing, no science changes. The same lanes
continue to carry the absolute-scale residual as an open admission.
