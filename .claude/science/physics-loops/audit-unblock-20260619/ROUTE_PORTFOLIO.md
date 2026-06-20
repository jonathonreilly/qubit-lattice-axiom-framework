# Route Portfolio

## Chosen Route

Repair canonical source metadata for the ready no-go packet:

1. Add `Claim type: no_go` to the note.
2. Update the note validation text to include source metadata as an explicit
   audit-support check.
3. Add a runner guard that requires `Type: no_go`, `Claim type: no_go`,
   independent audit authority, and no prediction of an audit outcome.
4. Refresh generated audit artifacts through the normal pipeline.

## Rejected Routes

- Audit verdict route: rejected because this loop only opens source-side repair
  PRs.
- New theorem route: rejected because the task is not to strengthen the claim.
- Global helper-packet resolver route: deferred because block120 is a narrow
  claim-specific metadata unblock.
- Direct main update: rejected by campaign contract.

## Residual Risk

The row is easier for the audit queue to classify, but the claim remains
unaudited and still needs independent review before any retained status can be
trusted.
