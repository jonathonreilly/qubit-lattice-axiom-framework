---
claim_id: kraus_choi_representation_deps_changed_hygiene_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Kraus-Choi Representation Deps-Changed Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dependency-rewire hygiene evidence)
**Status:** companion-only. This supplies review-compatible evidence that the
parent
[`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
does not load-bear on the Record content added to the stable
`minimal_axioms` premise node. It is not a theorem claim, not a direct status change,
and not independent audit work.
**Companion target:** `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`
**Primary runner:**
[`scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py`](../scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt)

## Claim Boundary

The parent theorem now routes finite-dimensional Kraus and Choi
representation content through the framework-local normalization-reconciled
Kraus/Choi correspondence note and runner, applied to a finite qubit-lattice
operator algebra:

```text
A_Lambda = tensor_{x in Lambda} M_2(C) ~= M_d(C),
d = 2^|Lambda|.
```

That load-bearing chain uses:

- the Quantum axiom's per-site one-qubit algebra `M_2(C)`;
- the Lattice axiom's finite `Z^3` region `Lambda`;
- finite-dimensional matrix algebra on the explicit `M_d(C)` surface;
- the framework-local reconciled Kraus/Choi correspondence and proof runner.

It does not use the Record axiom's additive finite scalar readout statement.
The current dependency rewire from the older dated axiom memo to the stable
`minimal_axioms` node therefore adds a Record-containing premise node to the
graph without adding a Record-dependent step to this parent's proof.

## Evidence

The companion runner checks four surfaces:

1. the parent note's load-bearing sections contain the finite
   `M_2(C)`, `Z^3`, Kraus, and Choi content, while the Record/readout language
   is outside that load-bearing surface;
2. the parent note labels its record-lane references as pointer references,
   not load-bearing dependencies;
3. the 2026-06-04 axiom memo preserves the Lattice + Quantum content needed
   by the parent and adds Record as a separate finite scalar readout axiom;
4. direct finite-dimensional matrix checks reproduce the Kraus operator-sum,
   trace-preservation, Choi positivity, and non-CP transpose-map boundaries on
   the framework matrix surface.

These checks support only the narrow dependency-surface statement above. They
do not set any audit verdict and do not decide whether the parent should be
reprocessed by the independent audit workflow.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not promote the parent or this companion.
- It does not edit the parent note, the axiom memo, or the audit registry.
- It does not claim the Record axiom is content-free in general.
- It does not claim a thermodynamic-limit Kraus/Choi theorem for arbitrary
  maps on the full quasi-local algebra; Kraus 1971 and Choi 1975 are now
  parallel references for the finite-region correspondence.
- It does not close infinite-volume channel questions, thermodynamic-limit
  questions, or record-formation dynamics.

The safe downstream use is only this: for the Kraus-Choi finite-region parent,
the stable `minimal_axioms` dependency is load-bearing through Lattice and
Quantum, while Record remains non-load-bearing for the proof itself.

## References

- Parent note:
  [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- Current framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor axiom memo:
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
