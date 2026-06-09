# Per-Plaquette From the Adjacency License: the Last Structural Statement Retires

**Date:** 2026-06-09
**Claim type:** bounded_theorem (an enumeration theorem + a reading of the retained license definition)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py`](../scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py)
(SCORECARD: PASS=13, FAIL=0; cached:
[`logs/runner-cache/frontier_per_plaquette_from_adjacency_license_2026_06_09.txt`](../logs/runner-cache/frontier_per_plaquette_from_adjacency_license_2026_06_09.txt))

---

## The derivation

**D1 (the license, retained, verbatim):** the reachability note *defines* what
adjacency means dynamically — *"(u,v) ∈ R means that the value at vertex v
after one update tick is allowed to use the value at vertex u"* — with the
update form quantified over R only (*"no arguments outside the listed
dependency set"*). The Lattice axiom's NN/no-diagonal adjacency **is the
one-tick dependency license.**

**D2 (the atom):** the kinetic-isotropy primitive fixes *"one tick is one edge
in form"* — the fundamental action is the log of the one-tick kernel, so its
terms are exactly one-tick dependency sets. (Only the fundamental kernel is at
issue; effective long-range correlations are untouched.)

**D3 (the lift dichotomy, computed):** lifting site-adjacency to links: the
strict lift (share a site) forbids even the plaquette (opposite plaquette edges
share no site — computed) ⟹ no gauge dynamics at all. The `B₁` lift (every
endpoint within one R-step of the target link's endpoints) is the **unique
minimal lift admitting gauge dynamics** — the same minimality reading the
axiom's no-diagonal clause records.

**D4 (the enumeration theorem):** exhaustively, on `Z³`: **all 24** simple
closed length-4 loops through a link are plaquettes and **all are licensed**;
**all 264** length-6 loops (rectangles, bent loops) **violate the license**.
The license admits exactly the plaquettes. **The fundamental gauge action is
per-plaquette — derived, not admitted.**

**D5 (the retirement):** combined with the cross-plane theorem (no F̃F slot in
the per-plaquette class, f-independent — PR #3429), `θ_bare = 0` is now **fully
derived** from {Lattice adjacency (axiom) + the retained license definition +
one-tick form (kinetic-isotropy primitive) + gauge invariance
(record-preservation class)}. The "minimal-loop structural statement" retires:
it was the Lattice axiom's no-diagonal adjacency all along, read at the
generator level.

```text
GIVEN SURFACE:  3 AXIOMS + 2 PRIMITIVES
(+ the vacuous species convention, carrying no physics)
Every number downstream — Q=2/3, |δ|=2/9, θ=0, the mass ratios — a theorem.
```

## What this note does NOT claim

- A skeptic may grade D3's dichotomy "a reading of the axiom" rather than a
  derivation — the audit lane's call; either way no *new* statement is added
  (the reading is the retained note's own definition + the axiom's own
  minimality).
- Falsifiers preserved: a framework derivation forcing multi-plaquette
  *fundamental* terms would contradict the license and reopen the slot.
- The record-preservation class theorem's bounded bridges remain its own rows.
  Sets no audit status; no comparator consumed.

## Dependencies

- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — the retained license definition (D1, verbatim).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the NN/no-diagonal adjacency.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — one tick = one edge in form (D2).
- [DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md) — the gauge-invariant-local class.
- `THETA_P1_PER_PLAQUETTE_NO_FTF_SLOT_BOUNDED_THEOREM_NOTE_2026-06-09.md` (plain-text context; PR #3429) — the cross-plane theorem this completes.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
