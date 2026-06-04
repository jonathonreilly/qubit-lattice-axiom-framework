# The Supertrace / Equivariant-Index / Holomorphic Route to Koide r=1/2 (Open Lead; Corrects the "Dynamical Class Exhausted" Claim)

**Date:** 2026-06-04
**Type:** open_lead
**Claim type:** open_lead (positive direction) — identifies the one genuinely untested
dynamical mechanism for the Koide `(1,1)` multiplicity weighting (r=1/2), and **corrects**
the "dynamical class exhausted" framing of block 3 (#2611).
**Claim scope:** the `(1,1)` multiplicity weighting that `r = 1/2` (Q=2/3, kappa=2) needs is
exactly the chirality-graded **supertrace / equivariant index / holomorphic** count: it
counts the **complex** doublet parameter `b` as **one** mode (chiral/holomorphic), where the
plain real trace counts `(Re b, Im b)` as **two** (vector) → the `(1,2)` weighting (r=1). This
route is **genuinely untested** (Probe 25's seven routes are all plain ungraded `Tr`), the
framework **has** the flavor-blind chirality grading `eps = (-1)^{x+y+z}` with `{eps,D}=0`, and
the Record axiom is **neutral** between trace and supertrace. Because the chirality is
flavor-blind and changes real↔complex counting (not a flavor reweighting), this route
**escapes** the flavor-blind-FACTOR analysis of block 3.
**actual_current_surface_status:** an **open lead**, not a derivation. The exact weighting
identification is verified (sympy); whether the chiral fluctuation determinant actually counts
`b` once is the **gated** computation. Conditional on the open staggered-Dirac realization gate.
Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.py`](./../scripts/audit_companion_supertrace_index_route_to_koide_multiplicity_open_lead_exact.py)

## Context (physics-loop dirac-corner-coupling, block 4 — completeness-critic pass)

Blocks 1–3 (#2601, #2607, #2611) ruled out the **trace-based** dynamical routes for the Koide
`r = 1/2`: free Gaussian measure, corner fermion determinant, Z3 scalar potential,
taste-breaking normalization, and multi-factor Connes-Lott — all deliver the `(1,2)`
real-**dimension** weighting (F3, kappa=1, r=1). Block 3 framed this as "the dynamical class is
exhausted." A completeness-critic pass found that framing **premature**: every route tested —
including all seven of Probe 25's `PHYS-AV1..7` — uses the **plain ungraded trace** `Tr`. The
chirality-graded **supertrace** `Str = Tr(eps · ...)` / equivariant index was never tested. This
note corrects the overclaim and characterizes the untested route.

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
4. The chirality grading `eps` is **flavor-blind** (a spacetime grading, scalar on flavor,
   commutes with C3). So it changes real↔complex (vector↔chiral) counting, **not** a flavor
   weight. This is **outside** block 3's flavor-blind-FACTOR analysis: tensor/direct-sum
   factors preserve `(1,2)`, but a holomorphy change halves the doublet real-count by pairing
   `(Re b, Im b)` into the single complex mode `b`.
5. The supertrace / equivariant index lives in the representation ring `R(G)` with **integer
   per-irrep multiplicities**; the plain heat-kernel trace gives **dimensions**. They are
   different functionals.

All six checks pass exactly (sympy).

## Why this is the promising route (and distinct from the admission)

Block 3 concluded that `(1,1)` requires a **flavor-dependent** operator `W = P_+ + (1/2)
P_doublet` — an admission. That conclusion is correct **for flavor-blind factors** (tensoring or
direct-summing with a C3-trivial space cannot change the singlet:doublet ratio, by Schur). But
it does **not** cover the mechanism here: a flavor-blind **chirality** that makes the
fluctuation counting **holomorphic**. Holomorphic counting weights the doublet's single complex
mode `b` once — giving `(1,1)` **without** any flavor-dependent reweighting. A chiral (Weyl)
fluctuation determinant is holomorphic (Pfaffian / chiral determinant); a vector (Dirac) one is
real. So:

> **If the generation fermion's fluctuation determinant is the chiral (holomorphic) one, the
> Koide weighting is `(1,1)` → `r = 1/2` → `Q = 2/3` — derived, flavor-blind, from the staggered
> `eps` grading the framework already carries.**

This is the **first** route in the whole campaign that could **derive** `r = 1/2` rather than
admit it. It is consistent with — and sharpens — the framework's recurring "the `i` does double
duty" theme (composition + phase): here the complex structure of `b` (the same `i`) is what a
chiral count sees as one mode.

## What is NOT yet established (the gated computation)

This is an **open lead**, not a derivation:

- Whether the framework's generation fermion fluctuation determinant is genuinely the **chiral /
  holomorphic** one (counting `b` once) or the **vector / real** one (counting `Re b, Im b`
  separately) requires the **gated** staggered-Dirac mass/Yukawa structure (kinetic-only on
  main; mass at the open substep-4 gate). The kinetic `{eps,D}=0` chirality is suggestive but
  does not by itself fix the fluctuation determinant's holomorphy.
- The selection principle must be the **fluctuation determinant** (effective potential) read
  **chirally**; the plain effective potential is the vector trace `(1,2)`. The Record axiom
  permits a graded readout but does not mandate it — so a separate argument that the readout is
  the chiral/holomorphic one is required.
- Until those are resolved, `r = 1/2` remains the BAE admission; this note only shows the
  admission has a **specific, framework-present, flavor-blind candidate derivation** that has
  never been tried.

## Correction to block 3 (#2611)

Block 3's convergence table is accurate for the **trace/vector** routes but its summary phrase
"the dynamical class is exhausted" is **too strong**. Corrected reading: *the trace-based
(vector) dynamical routes are exhausted; the chirality-graded **supertrace / index /
holomorphic** route is the genuine open residual — and the most promising, because it is
flavor-blind and uses the framework's existing `eps` grading.* This note supersedes that phrase.

## Trace gate

```yaml
trace_class: open_lead
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: candidate_derivation
artifact_role: open_lead
next_trace_action: "compute the CHIRAL (Pfaffian / holomorphic) fluctuation determinant of the generation sector on the hw=1 corners and test whether it counts the complex doublet mode b once -> (1,1) -> r=1/2. Requires the gated staggered-Dirac mass structure."
```

## Forbidden imports

- No PDG values as derivation inputs. The chirality grading `eps`, the C3 regular-rep character,
  and the isotype Frobenius split are reproven from primitives. Literature (Fujikawa/index,
  Kawamoto-Smit) is comparator only.

## Cross-references

- `MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 3, #2611) — the trace/vector convergence this note corrects and extends.
- `CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 1, #2601) and
  `STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 2, #2607).
- `KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md` — the
  seven plain-trace routes (PHYS-AV1..7) that this lead shows are not exhaustive.
- `AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md` — the framework's existing
  supertrace `A_t = Tr(eps exp(-t D^dag D))` construction (on a finite grading), never yet
  applied to the Koide weighting.
