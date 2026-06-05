---
claim_id: koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04
claim_type_author_hint: open_gate
---

# Koide Berezin det_C vs det_R Fork Mechanism

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** open_gate (mechanism / route-pruning support)
**Status:** source-only mechanism support. This note does not approve a new
axiom, primitive, admission, or verdict. It records a tested four-cell fork:
real versus holomorphic polarization, crossed with Gaussian versus Berezin
statistics.
**Primary runner:** [`scripts/berezin_detc_detr_fork_2026_06_04.py`](../scripts/berezin_detc_detr_fork_2026_06_04.py)
**Cached log:** [`logs/runner-cache/berezin_detc_detr_fork_2026_06_04.txt`](../logs/runner-cache/berezin_detc_detr_fork_2026_06_04.txt)

## Claim Boundary

The runner works on the generation algebra `R[Z_3] = R (+) C`. It verifies the
real and complex block decompositions, the doublet complex structure `J`, the
`Q = (1 + 2r) / 3` Koide lever, and the partition-function weights for four
explicit model cells:

| action family | polarization | doublet count | result |
|---|---|---:|---|
| real Gaussian | real | 2 real slots | `r = 1`, `Q = 1` |
| Majorana Berezin | real | 2 real slots | `r = 1`, `Q = 1` |
| holomorphic Gaussian | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |
| holomorphic Berezin | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |

The tested mechanism is that the `r = 1/2` cell follows from holomorphic
polarization: choosing the doublet complex structure `J` and counting the
doublet as one complex slot. It is not supplied merely by changing from a
Gaussian action to a Berezin action, because the real Majorana Berezin cell
lands on the real-slot count.

## Source Links

The `Q = (1 + 2r) / 3` lever is the upstream algebra identity from
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).
The related doublet-counting pin is discussed in
[`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md);
this note does not use that related note as closure, only as context for the
same open complex-structure question.

## No-Go Discipline Disposition

The submitted branch tried to phrase this as a broader negative claim:
`det_C` is not forced by first-order structure alone. That broad negative did
not pass the review-loop no-go gate as submitted: its N1 section listed four
routes, while the repo rule requires at least five before a no-go can ship.

This landed note is therefore demoted. It does not claim that no future native
route can derive `J`, and it does not claim that the complex structure is an
axiom or primitive. It records only the tested four-cell mechanism and leaves
the positive route open: derive a native polarization selector, or show that
the readout functional factors through the doublet complex-slot quotient.

## What This Does Not Claim

- It does not adopt the holomorphic polarization.
- It does not establish a charged-lepton mass prediction.
- It does not use PDG values, fitted parameters, or literature comparators.
- It does not assert that `Q = 2/3` is impossible to derive natively.
- It does not classify the doublet complex structure as an axiom or primitive.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is narrow: this note may be cited to say that the
tested action-side fork separates polarization from statistics. It may not be
cited as a closed no-go against all future `r = 1/2` derivations.
