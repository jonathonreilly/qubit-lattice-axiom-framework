# Scale Reference Primitive (the units import)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`; each row points to the canonical source-of-truth doc.

**Date:** 2026-05-30
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as `scale_reference_primitive`.
Owner science-level decision recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §6.

## What this note declares

The framework takes exactly **one** dimensionful number: a single **scale
reference** `a^{-1}`, used as the unit that converts the framework's natural
(lattice) units to physical units. By convention its value is the Planck scale,
`a^{-1} = M_Pl`.

This is a **units conversion, not a physics axiom**. It carries zero
dimensionless content: no mass ratio, coupling, mixing angle, or phase is
supplied by it. Every physical theory makes exactly this one choice — the single
overall scale that connects its internal units to a laboratory ruler.

## Why it is a primitive (irreducible by dimensional analysis)

`A_min` — a qubit at every site of `Z^3` (equivalently `Cl(3)` on `Z^3`) —
carries zero dimensionful content. Every quantity derived from `A_min` is
therefore either dimensionless or carries a power of the lattice spacing
`[a]^n`, whose physical value is undetermined until one dimensionful observable
is supplied. That single supplied number is this scale reference. It is
foundational and **not a derivation gap**: a dimensionful scale cannot be
derived from dimensionless structure.

The three retained no-go notes
`planck_finite_response_no_go_note_2026-04-24`,
`planck_parent_source_hidden_character_no_go_note_2026-04-24`, and
`planck_boundary_orientation_incidence_no_go_note_2026-04-30`
are consistent with this: they show the scale/carrier is not forced by symmetry
alone, i.e. the scale behaves as the unit, not a theorem.

## What this note does NOT do

- It does **not** assert `a/l_P = 1`. Whether the framework's natural unit
  self-consistently equals the Planck length is a **separate, open** gravity
  derivation (the `c_cell = 1/4` / boundary-carrier chain), tracked elsewhere
  and unaffected by this declaration. This note pins the unit by choice; it does
  not claim the framework derives which scale that is.
- It does **not** add a physics axiom or amend `A_min`. The two framework axioms
  A1 (qubit per site) and A2 (`Z^3` lattice) are unchanged; see
  `docs/MINIMAL_AXIOMS_2026-05-20.md`.
- It does **not** supply any dimensionless quantity. A lane's dimensionless
  content must still derive from `A_min`; this primitive only anchors the single
  overall unit.

## Provenance

This declaration supersedes the prior treatment of the scale as the Tier-A
admitted input "S" (formerly tracked under `not_a_node` in
`docs/audit/data/tier_a_admissions.json`). The single scale reference is the
units conversion, not one of the genuine admitted physics inputs (which are P1,
AC_phi_lambda, and theta). See
`docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`.
