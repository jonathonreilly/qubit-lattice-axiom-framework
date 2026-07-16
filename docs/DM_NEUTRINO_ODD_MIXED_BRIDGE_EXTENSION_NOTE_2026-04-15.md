# DM Neutrino Odd Mixed-Bridge Extension

**Claim type:** bounded_theorem

**Date:** 2026-04-15  
**Status:** conditional extension-class theorem under a separately supplied
nonzero odd-coefficient target
**Script:** `scripts/frontier_dm_neutrino_odd_mixed_bridge_extension.py`

## Question

If a separate source/activation bridge requires `c_odd != 0`, what is the
smallest extension class left after the odd-direction algebra lemma and the
current-stack zero law?

## Bottom line

Conditionally, a **residual-`Z_2`-odd non-additive mixed bridge with one real
amplitude slot**.

More sharply, any realization of that separately supplied nonzero target must:

- lie outside the current retained even support/Hermitian/scalar bank
- live on the canonical non-universal two-Higgs locus
- be residual-`Z_2` odd
- be non-additive over the even/odd circulant decomposition
- reduce to one real amplitude on the unique odd class `i(S - S^2)`

This classifies the algebraic shape of a possible extension. It does not show
that a physical model requires the target or supplies such a bridge.

## Why this is now exact

Under the note's explicit assumptions, the branch knows:

1. the unique odd local class: `c_odd i(S-S^2)`
2. the current-stack law: `c_odd,current = 0`
3. the unique minimal support lane: the canonical distinct-charge two-Higgs
   branch
4. the local sheet on that lane is already fixed on the DM circulant route

The supplied-matrix lemma contributes only item 1. It does not supply a
physical carrier, a source law, or a reason to require a nonzero odd
coefficient.

## Theorem-level statement

**Theorem (Conditional minimal extension class for a nonzero odd
coefficient).** Assume a separate target requiring `c_odd != 0`, the bounded
supplied-matrix odd-direction lemma, the DM odd-slot current-stack zero law,
the DM two-Higgs minimality theorem, and the DM two-Higgs continuity sheet
theorem. Then any realization of that target must:

1. lie outside the current retained even support/Hermitian/scalar bank
2. be supported on the canonical non-universal two-Higgs locus
3. be residual-`Z_2` odd
4. be non-additive over the even/odd circulant decomposition
5. reduce on the local quotient to one real amplitude multiplying the unique
   odd class `i(S-S^2)`

Therefore, under those assumptions, the minimal surviving extension class is a
residual-`Z_2`-odd non-additive mixed bridge with one real amplitude slot.

## What this closes

This closes only the conditional extension-class ambiguity after the nonzero
target is supplied.

The remaining bridge problem is not:

- another even support refinement
- another Hermitian/scalar post-processing trick
- another multi-parameter local coefficient family

It is one specific algebraic bridge class.

## What this does not close

This note does **not** derive the microscopic bridge functional itself, the
source/activation requirement `c_odd != 0`, or a physical readout/transport
interpretation.

It identifies the extension class only.

## Command

```bash
python3 scripts/frontier_dm_neutrino_odd_mixed_bridge_extension.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15](DM_NEUTRINO_ODD_CIRCULANT_Z2_SLOT_THEOREM_NOTE_2026-04-15.md)
  — bounded supplied-matrix Hermitian-circulant / `P_23` even-odd algebra
  lemma only; it does not supply the nonzero target
- [dm_neutrino_odd_circulant_current_stack_zero_law_note_2026-04-15](DM_NEUTRINO_ODD_CIRCULANT_CURRENT_STACK_ZERO_LAW_NOTE_2026-04-15.md)
- [dm_neutrino_two_higgs_minimality_theorem_note_2026-04-15](DM_NEUTRINO_TWO_HIGGS_MINIMALITY_THEOREM_NOTE_2026-04-15.md)
- [dm_neutrino_two_higgs_continuity_sheet_theorem_note_2026-04-15](DM_NEUTRINO_TWO_HIGGS_CONTINUITY_SHEET_THEOREM_NOTE_2026-04-15.md)
