# Cycle 704 — record migration gate — BACKLOGGED, with a flat error

Branch: `physics-loop/record-migration-gate-20260725` (pushed). Runner
4 PASS / 0 FAIL, cold-run isolated, pin verified. **No PR opened.**

Built under owner direction to attack the formation rule and push the frontier,
targeting an item two landed notes mark explicitly OPEN (migrating-record
semantics). The cluster-cap evaluator returned `BACKLOG` with three correct
objections, one of which is a flat error.

## The error (accepted without reservation)

M3 claimed: "a rule cannot bound record density by bounding formation alone —
if records may migrate, denser configurations are reachable than the formation
gate admits."

**That is wrong. Migration conserves record number.** Moving a record from one
site to another changes the arrangement, not the count. There is no density
increase to be had, so the stated consequence does not exist. The witness shows
only that one locked content can arrive where that same content could not have
formed in the compared predecessor configuration — a statement about
arrangement, not density.

## The second objection (also correct)

M2's geometry is right — an adjacent mover vacates one neighbour of the
destination — but it does not establish two intrinsically different gates. It
applies the **same unknown Admissibility rule** to two different neighbourhood
configurations. "One fewer occupied neighbour" implies a weaker gate only if
availability is count-monotone, which the framework does not supply: a covariant
rule may ignore that neighbour, depend on its content or orientation, or reverse
the exhibited ordering. Strict permissiveness holds for the supplied witness
rule and was over-generalized.

## The third objection

M1 is an immediate corollary of the axiom sentence "a readout value is
determined by record content alone". Naming a content-preserving relocation
"migration" does not make it a new theorem.

And, on warrant: an item being marked OPEN in landed notes is sufficient reason
to **investigate** it, not sufficient reason to open a PR.

## Disposition

Target stopped, no revision attempted. This is the fourth consecutive backlog in
this campaign (700, 701 twice, 702, 704) and the second containing a substantive
error of mine that the gate caught — 702's "long-ranged precisely when A=0",
false because the symbol vanishes at nonzero `k`, and now 704's density claim.

## The pattern, recorded for whoever runs this next

The exact-arithmetic content of these cycles has held up every time. The
failures are all in the **inference from** the arithmetic to the structural
claim:

- 701: symbol-disjointness read as independence (true by construction)
- 702: "zero dimensionless content" read as selecting zero; and a global
  long-range claim inferred from the symbol at one point
- 704: a first draft asserting gate identity by writing the same function body
  twice; then a density claim contradicted by conservation of record number

Every one of these would have been caught by writing the one-sentence claim
first and asking what would make it false, **before** building the runner. The
runner is not where the risk is. Recommend that mode change for the next
session on this surface.
