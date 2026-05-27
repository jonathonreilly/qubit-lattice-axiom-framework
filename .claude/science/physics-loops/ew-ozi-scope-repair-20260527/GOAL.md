# Goal

Repair `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` without
adding axioms or claiming the physical EW connected-trace selector.

The audit blocker was that the row relied on OZI/large-N suppression and a
physical readout selector to upgrade beyond conditional support. The live
retained no-go shows that `kappa_EW = 0` is not selected by the current packet.

This branch preserves the exact channel split and bounded OZI size class as
bounded support:

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9).
```
