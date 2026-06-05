---
claim_id: axiom_first_lattice_noether_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Axiom-First Lattice Noether Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent finite
staggered-carrier Noether checks do not use Record axiom content. It is not a
new theorem claim, not a verdict change, and not independent review work.
**Companion target:** `axiom_first_lattice_noether_theorem_note_2026-04-29`
([`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md))
**Primary runner:**
[`scripts/audit_companion_axiom_first_lattice_noether_record_invariance_2026_06_04.py`](../scripts/audit_companion_axiom_first_lattice_noether_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_axiom_first_lattice_noether_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_axiom_first_lattice_noether_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent surface is a bounded theorem on an admitted staggered/Grassmann
carrier. Its load-bearing content is the finite lattice Noether chain: the
symmetry condition `[T, M] = 0`, local-alpha promotion, the bilateral current
specialization to the U(1) current, the on-shell divergence identity, the exact
localized two-step Ward identity, and the `(2Z)^3` periodicity of the
staggered phases.

This companion does not derive the admitted carrier, the KS phase form, or a
new current identity. It does not change the parent row. Axioms and primitives
are premise context here; they are not verdict-grade support for a bounded row.

The narrow evidence recorded here is:

1. the parent note hash, claim type, dependency list, and runner path match the
   live ledger row;
2. the parent runner exits with `PASSED: 7/7`;
3. the parent load-bearing sections contain the symmetry condition, U(1)
   current specialization, on-shell divergence, exact two-step Ward identity,
   and one-site-shift caveat;
4. the parent load-bearing sections do not use Record axiom content;
5. the parent runner output is unchanged under counterfactual markers where
   Record is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not derive the admitted staggered/Grassmann carrier.
- It does not derive the KS phase form.
- It does not change the parent dependency boundary.
- It does not treat axioms or primitives as bounded-row support.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent finite
staggered-carrier Noether checks are record-invariant, while any stronger
chain remains outside this companion.
