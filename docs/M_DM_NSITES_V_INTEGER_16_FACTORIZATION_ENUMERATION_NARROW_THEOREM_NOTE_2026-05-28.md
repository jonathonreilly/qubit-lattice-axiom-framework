# `m_DM = N_sites · v` Integer-16 Factorization Catalog

**Date:** 2026-05-28
**Type:** bounded_theorem
**Status:** bounded finite catalog of four currently cited readings of
`N_sites = 16`; this note does not derive `m_DM = N_sites · v` and does
not assign audit status to any cited row. It does not assign audit status
for this row either.
**Audit status:** assigned only by the independent audit lane.
**Primary runner:** [`scripts/audit_companion_m_dm_nsites_v_factorization_enumeration_2026_05_28.py`](../scripts/audit_companion_m_dm_nsites_v_factorization_enumeration_2026_05_28.py)

## Claim Boundary

This note catalogs four factorization readings of the integer
`N_sites = 16` that are already named in the current DM `eta` authority
chain. It verifies the arithmetic of those readings and records the
source boundary attached to each one.

It does **not**:

- derive `m_DM = N_sites · v`;
- choose one factorization as the physical mechanism;
- retire the supplied `eta` premise;
- introduce a new axiom, selector law, framework substrate, or repo-wide
  vocabulary;
- apply or predict any audit verdict for this row or for a cited row.

The audit ledger is the authority for live effective status. Any status
words below describe source-scope boundaries in the cited notes, not an
audit verdict applied by this note.

## Four Cataloged Readings

| # | Arithmetic | Source reading | Cited source boundary |
|---|---|---|---|
| F1 | `16 = 2^4` | Brillouin-zone corner count on a Wick-rotated `Z^4` reading. | [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md) records the Wick-rotation step as an admission, not as a framework-derived theorem. |
| F2 | `16 = (8/3) · 6` | SU(3) Casimir factor `2 C_F = 8/3` times Wilson bare count `2 r · hw_dark = 6`. | [`CL3_CHIRAL_CUBE_WILSON_HOP_DOUBLING_FORECLOSED_NARROW_NO_GO_NOTE_2026-05-27.md`](CL3_CHIRAL_CUBE_WILSON_HOP_DOUBLING_FORECLOSED_NARROW_NO_GO_NOTE_2026-05-27.md) records a narrow same-link Step-5 route failure for the `U_mu + U_mu^dagger` reading. This catalog does not add a new no-go. |
| F3 | `16 = 4 · 4` | Chirality-pair count times half-cube parity/taste count at `d = 4`. | [`STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md) records the arithmetic/counting identity and keeps the framework-realization step separate. |
| F4 | `16 = L_t · 4` with `L_t = 4` | Klein-four APBC temporal selector times the chirality-pair count. | [`OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md), together with the F3 source, supplies the two factor readings; the bridge identifying their product with `m_DM = N_sites · v` remains open. |

The catalog is finite and bounded to these cited source surfaces. It is
not a claim that no future source can introduce another reading of the
integer `16`.

## Arithmetic Checks

The runner verifies the stable arithmetic content:

- `2^4 = 16`;
- at `N_c = 3`, `C_F = (N_c^2 - 1)/(2 N_c) = 4/3`, so
  `2 C_F = 8/3` and `(8/3) · 6 = 16`;
- at `d = 4`, `2^{d/2} · 2^{d/2} = 4 · 4 = 16`;
- at `L_t = 4`, `L_t · 4 = 16`;
- the positive integer divisor pairs of `16` are `(1,16)`, `(2,8)`,
  and `(4,4)`, while F2 is an explicitly rational factorization;
- the four catalog entries are distinct as source readings even when
  F3 and F4 share the same arithmetic pair `(4,4)`;
- every cited source file exists in `docs/`.

## Downstream Reading

The bounded `eta` prediction source
[`DM_ETA_BOUNDED_PREDICTION_FROM_SUPPLIED_NSITES_V_NARROW_THEOREM_NOTE_2026-05-28.md`](DM_ETA_BOUNDED_PREDICTION_FROM_SUPPLIED_NSITES_V_NARROW_THEOREM_NOTE_2026-05-28.md)
uses `m_DM = N_sites · v` as a supplied premise. This catalog does not
strengthen that premise. It is a route inventory for later work on the
mechanism behind the integer `16`.

The most local follow-up suggested by the catalog is the F4 bridge:
prove or refute whether the Klein-four `L_t = 4` selector and the
chirality-pair count can be connected to the dark `m_DM` selector
without adding a new framework premise.

## Scope Discipline

This note does not ship a new no-go. The F2 row cites an existing
source-scoped failure of the same-link Step-5 route only to explain why
that reading is not being promoted here. Other routes to the same
arithmetic factor, including neighboring-edge Wilson-action mechanisms,
remain outside this catalog.

This note also does not use external observed values, fitted selectors,
or literature numerical comparators. Its load-bearing content is finite
arithmetic plus source-file citation hygiene.
