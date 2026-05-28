# No-Go Ledger

## Retained promotion in this block

Status: no-go for this PR.

Reason: every theorem-like row in the batch still has at least one missing
bridge or dependency-status import under the latest audit feedback. Promoting
any of them to retained from this branch would bypass independent audit and
overstate the current framework surface.

## Manual ledger retagging

Status: no-go.

Reason: changed rows become reauditable only through source/support hash
changes plus the pipeline reset. No terminal verdict was edited directly.

## Framework-vs-lattice-QCD theorem from the existing runner

Status: no-go for this block.

Reason: the runner supports a graph-propagator diagnostic and Sorkin
linearity diagnostic. It does not supply the physical graph-gravity or
probability/readout bridge needed for the stronger comparison theorem.
