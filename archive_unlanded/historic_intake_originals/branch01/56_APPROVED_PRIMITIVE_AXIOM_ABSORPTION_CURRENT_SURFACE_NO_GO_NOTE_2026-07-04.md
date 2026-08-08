# Approved Primitive Axiom-Absorption Current-Surface No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** current-surface triage of whether the 2026-06-29 four-axiom
memo, including the 2026-07-04 Record formation sentence, has absorbed any of
the three approved primitive nodes. This note does not retire, re-grade, add,
or amend any axiom, primitive, Tier-A admission, audit verdict, lane registry,
or publication-status surface.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/approved_primitive_axiom_absorption_current_surface_no_go_2026_07_04.py`](../scripts/approved_primitive_axiom_absorption_current_surface_no_go_2026_07_04.py)

## Target

The front-door foundation surface currently has four axioms and three approved
primitive nodes:

```text
minimal_axioms
scale_reference_primitive
kinetic_isotropy_primitive
realized_state_primitive
```

The question is whether the updated axiom memo now houses any approved
primitive so cleanly that the primitive can be retired by text absorption
alone.

## Source Surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is the
  current four-axiom memo.
- [`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json)
  is the machine registry for axiom and approved primitive premise nodes.
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  declares the single dimensionful ruler.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  declares the OS0 kinetic-form isotropy ratio `c_t = c_s`.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  declares pointwise evaluation at the supplied law-admissible realized state.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  separates approved primitives from Tier-A admitted derivation targets.

## No-Go Statement

No approved primitive is retired by the current axiom text alone.

| Primitive | Axiom overlap | Still outside the axiom memo |
|---|---|---|
| `scale_reference_primitive` | None. The axiom memo is dimensionless structural content. | The single dimensionful unit reference remains outside the axioms; the natural-unit/Planck self-consistency question remains separate. |
| `kinetic_isotropy_primitive` | The Lattice axiom gives spatial cubic adjacency, and Admissibility gives a nearest-neighbor availability rule. | The axiom memo explicitly withholds dynamics, transfer operators, transition weights, time metric, and kinetic branch selection. It does not supply `c_t = c_s`. |
| `realized_state_primitive` | The axiom memo defines a state as a configuration of records and says a law privileges no states. | It still supplies no realized state, state-selection rule, measure, typicality, genericity, boundary condition, or state-contingent value. Pointwise evaluation at the physical history remains the separate primitive slot. |

The realized-state primitive is therefore the only partially overlapping case:
the *type* of a state is axiom text, while the actual realized-state reference
used for pointwise evaluation is not.

## What This Moves

| Before | After |
|---|---|
| The updated Record and Admissibility wording raised the question of primitive absorption. | The absorption shortcut is split primitive by primitive and blocked on the current text. |
| Realized-state looked closest to retirement because the axiom memo now says a state is a configuration of records. | The runner separates axiom-level state typing from actual-history pointwise evaluation. |
| Approved primitives could be conflated with Tier-A admissions during the Tier-A cleanup. | The note records that all three remain approved, non-bounding primitive nodes, not Tier-A rows. |

## What Does Not Move

- No primitive is retired.
- No axiom or primitive registry is edited.
- No Tier-A admission is retired or reclassified.
- No audit status or effective status is changed.
- No claim is made that a future theorem or owner-governance path cannot
  retire a primitive.

## Attack Plan After This No-Go

1. **Scale reference:** leave as an unavoidable non-bounding ruler unless a
   separate gravity/natural-unit theorem derives the physical scale.
2. **Kinetic isotropy:** keep as an explicit primitive unless a retained
   dynamics theorem derives `c_t = c_s` without circularly assuming emergent
   Lorentz form.
3. **Realized state:** preserve the primitive slot, but use the axiom memo for
   state typing whenever a row needs only "state = configuration of records."
   State-contingent values remain registered data under the primitive's
   counterfactual test.
4. **Tier-A work:** continue attacking AC and theta directly; approved
   primitive cleanup does not reduce the current Tier-A count of two.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/approved_primitive_axiom_absorption_current_surface_no_go_2026_07_04.py
```

Expected close: `FAIL=0`.
