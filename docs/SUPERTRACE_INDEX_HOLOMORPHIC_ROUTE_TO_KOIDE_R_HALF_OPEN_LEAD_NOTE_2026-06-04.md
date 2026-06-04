# Supertrace / Equivariant-Index / Holomorphic Candidate Route to Koide r=1/2 (Open Gate)

**Date:** 2026-06-04
**Type:** open_gate
**Claim type:** open_gate (candidate route). This note identifies a
specific conditional route not covered by the landed trace/vector
companions: a chirality-graded supertrace / equivariant-index /
holomorphic readout would count the complex doublet parameter `b` once
instead of counting its two real components separately.
**Claim scope:** Under the finite C3 generation-triplet model with
`E_singlet = 3a^2` and `E_doublet = 6|b|^2`, the real/vector count
weights `(Re b, Im b)` as two doublet modes and gives the `(1,2)`
weighting (`r = 1`). A holomorphic/chiral count weights the complex
mode `b` once and gives the `(1,1)` weighting (`r = 1/2`). This is an
algebraic candidate route only. It does not show that the framework's
generation fluctuation determinant is chiral, and it does not derive
the Koide value.
**actual_current_surface_status:** open gate. The weighting
identification is verified by the paired runner; the selection of a
chiral/holomorphic determinant remains gated by the staggered-Dirac
mass/Yukawa realization. Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.py`](./../scripts/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.py)
**Runner cache:** [`logs/runner-cache/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.txt`](./../logs/runner-cache/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.txt)

## Context

The landed Koide route-pruning companions cover several trace/vector
mechanisms. In particular, the [corner determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md),
the [staggered-taste normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md),
the [multi-factor companion](MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md),
and [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
all leave the `(1,1)` multiplicity weighting as a residual rather than
deriving it. Those surfaces do not test a chirality-graded supertrace /
equivariant-index / holomorphic readout of the generation fluctuation.

This note characterizes that missing candidate route. The framework has
a finite staggered chirality construction in the
[WZ/Fujikawa finite-lattice theorem](AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md),
but that theorem does not decide the Koide mass/Yukawa determinant's
readout. The [Lattice + Quantum + Record baseline](MINIMAL_AXIOMS_2026-06-04.md)
also does not decide trace versus supertrace; Record supplies only
finite scalar record additivity.

## Statement (exact, verified)

1. The generation triplet is the C3 regular representation; each irrep (trivial, `omega`,
   `omega-bar`) has **multiplicity 1**. As (singlet ; real-doublet), the **multiplicity**
   weighting is `(1,1)`; the **dimension** weighting is `(1,2)`.
2. The two weightings give exactly `r = 1` (dimension/trace → Q=1, kappa=1) and `r = 1/2`
   (multiplicity/index → Q=2/3, kappa=2), with `E_singlet = 3a^2`, `E_doublet = 6|b|^2`.
3. **Holomorphic mechanism.** The doublet coefficient `b` is **one complex** parameter =
   **two real** parameters `(Re b, Im b)`. A holomorphic / chiral count weights `b` once
   (doublet weight 1 → `(1,1)`); a real / vector count weights `Re b, Im b` separately
   (doublet weight 2 → `(1,2)`). `Tr(M^H M) = 3a^2 + 6|b|^2` exactly.
4. A flavor-blind extra tensor/direct-sum factor preserves the `(1,2)`
   trace/vector weighting, as checked in the multi-factor companion. A
   holomorphic readout is a different conditional: it changes the
   real-versus-complex mode count by pairing `(Re b, Im b)` into the
   single complex mode `b`. This is why the route remains open rather
   than being covered by the landed flavor-blind-factor pruning.
5. The supertrace / equivariant index lives in the representation ring `R(G)` with **integer
   per-irrep multiplicities**; the plain heat-kernel trace gives **dimensions**. They are
   different functionals.

All six checks pass exactly (sympy).

## Why this is distinct from the admission

The multi-factor companion shows that a C3-trivial extra factor does not
by itself change the singlet:doublet trace/vector ratio. That does not
cover a separate holomorphic-readout condition. If the relevant
generation fluctuation determinant is chiral or holomorphic, the
doublet's single complex mode `b` is counted once, yielding `(1,1)`
without inserting the flavor-dependent operator
`W = P_+ + (1/2) P_doublet`. A vector/real determinant instead counts
`Re b` and `Im b` separately and yields `(1,2)`.

> **If the generation fermion's fluctuation determinant is the chiral (holomorphic) one, the
> Koide weighting is `(1,1)` -> `r = 1/2` -> `Q = 2/3`.**

That conditional is the point of this open gate. The note does not
claim that the conditional antecedent has been established.

## What is NOT yet established (the gated computation)

This is an **open gate**, not a derivation:

- Whether the framework's generation fermion fluctuation determinant is the **chiral /
  holomorphic** one (counting `b` once) or the **vector / real** one (counting `Re b, Im b`
  separately) requires the **gated** staggered-Dirac mass/Yukawa structure (kinetic-only on
  main; mass at the open substep-4 gate). The kinetic `{eps,D}=0` chirality is suggestive but
  does not by itself fix the fluctuation determinant's holomorphy.
- The selection principle would need to be the **fluctuation
  determinant** read chirally or holomorphically. The plain effective
  potential is still the vector trace `(1,2)`. The Record axiom does not
  decide this readout choice; a separate argument is required.
- Until those are resolved, `r = 1/2` remains the BAE admission; this note only records a
  specific, framework-present, flavor-blind candidate route that remains unevaluated here.

## Correction to the prior route-pruning boundary

The landed route-pruning surfaces remain useful only within their
stated trace/vector or flavor-blind-factor scopes. They should not be
read as proving that every possible dynamical route to `(1,1)` is
closed. This note names one explicit residual candidate route and keeps
it open.

## Trace gate

```yaml
trace_class: open_gate
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: candidate_route
artifact_role: open_gate
next_trace_action: "compute the CHIRAL (Pfaffian / holomorphic) fluctuation determinant of the generation sector on the hw=1 corners and test whether it counts the complex doublet mode b once -> (1,1) -> r=1/2. Requires the gated staggered-Dirac mass structure."
```

## Forbidden imports

- No PDG values as derivation inputs. The C3 regular-representation
  character and the isotype split are computed inside the runner. The
  finite staggered chirality construction is cited only as existing
  framework structure, not as a proof that the Koide readout is chiral.
  Literature (Fujikawa/index, Kawamoto-Smit) is comparator only.

## Cross-references

- [Multi-factor companion](MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - flavor-blind extra factors preserve the `(1,2)` trace/vector
  weighting.
- [Corner determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  and [staggered-taste normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - route-pruning companions whose stated residual remains open.
- [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
  - plain-trace route surface that does not cover the holomorphic
  readout candidate.
- [Finite-lattice WZ/Fujikawa theorem](AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md)
  - existing finite `epsilon`-graded supertrace construction, not yet a
  Koide readout theorem.
