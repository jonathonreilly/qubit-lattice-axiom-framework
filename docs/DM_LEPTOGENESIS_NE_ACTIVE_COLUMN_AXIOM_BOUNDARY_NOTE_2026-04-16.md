# DM Leptogenesis `N_e` Active-Column Four-Summary Ambiguity Diagnostic

**Status:** bounded - bounded or caveated result note
**Type:** bounded_theorem
**Date:** 2026-04-16  
**Script:** `scripts/frontier_dm_leptogenesis_ne_active_column_axiom_boundary.py`  
**Framework baseline:** Lattice, Qubit, Admissibility, and Record axioms.

## Status

Finite ambiguity diagnostic for an explicit four-summary equivalence class,
conditional on the supplied transport equations, profiles, and finite column
functional used by the named runner.

This note asks whether four explicitly tested summaries already force the
selected transport column on the charged-lepton-active branch `N_e`.

The answer is no.

## Question

On the PMNS-assisted DM lane, is the selected `N_e` active transport column
already determined by the tested seed averages, phase, support count, and
branch bit?

Equivalently: after importing

- one-sided active-block localization,
- the supplied finite flavored transport functional,
- the active seed pair,
- the active branch/support data,

is there still any real ambiguity left in the transport-relevant `N_e` column?

## Bottom line

Yes, there is still real ambiguity.

There exist explicit charged-lepton-active microscopic samples that share the
same four tested summaries:

- the same seed pair `(xbar, ybar)`,
- the same fixed phase `delta`,
- the same one-sided active support count,
- the same active branch bit,

but carry different active five-real source data

`(xi_1, xi_2, eta_1, eta_2, delta)`,

and those different sources induce:

- different active projector packets,
- different values of the supplied finite transport functional,
- and different selected active columns.

In fact the same tested-summary `N_e` class can realize selected column
`0`, `1`, or `2`.

So the selected `N_e` transport column is **not** fixed by those four summaries.
This finite family does not establish that the samples are indistinguishable
under every datum available from the current framework.

## Supplied selector used by the counterexample

The negative result is not coming from transport ambiguity.

Conditional on the supplied one-source flavored transport equation and its
computed profiles, the branch uses

`F_K(P) = Σ_alpha Psi_K(P_alpha)`.

So once an active column `P` and that transport fixture are supplied, the
finite transport read is algorithmic.

The question here is strictly upstream and limited: do the four tested
summaries already force the relevant active column on `N_e`?

For that supplied finite fixture, the explicit samples show it does not.

## Explicit counterexample family

The runner exhibits three explicit charged-lepton-active samples in the same
tested-summary class:

- same `xbar = 0.973333333333...`,
- same `ybar = 0.41`,
- same `delta = 0.2`,
- same support count `= 2`,
- same active branch bit `= 0`,

but different active five-real source data, yielding:

- sample A: selected column `0`,
- sample B: selected column `1`,
- sample C: selected column `2`.

So the transport-selected column is still sensitive to the active five-real
source.

## Consequence

This sharpens the finite diagnostic boundary for the tested equivalence class.

What is available on the stated conditional surface:

- one-sided PMNS projectors localize to the active block,
- the flavored transport functional follows from the supplied equations,
- the canonical `N_e` middle-column ordering is known on one finite sample,
- the seed averages, phase, support count, and branch bit are supplied and
  equal across the three samples.

What is still not fixed:

- the active five-real source,
- and therefore the selected `N_e` active column.

Within this tested class, the active five-real source data, or equivalent
information, can change the selected active column.

## Honest endpoint

The honest endpoint on this lane is now:

- transport functional: conditional on supplied equations, profiles, and
  boundary data
- active-block localization: closed
- selected `N_e` column: **not** fixed by the four tested summaries

This is a finite conditional ambiguity diagnostic only. It does not prove a
full current-framework no-go, does not exhaust all PMNS-side data, and does not
derive an axiom-native transport bridge or final PMNS-side value law.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_ne_active_column_axiom_boundary.py
```

## Cited dependencies

These are the supplied functional and active-projector inputs used by the
finite diagnostic:

- [dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md)
- [dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md)
