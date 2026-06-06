# Opportunity Queue

## Current block

1. Close the selector/dial subdivision PR.
   - Status: in progress.
   - Value: splits 210 selector rows into four actionable queues.
   - Runner: read-only sub-bucket scan with hash preservation.

## Next candidates

1. Stability/dynamics selector micro-queue.
   - Inspect 64 rows for supplied map/flow versus actual selector.
   - Risk: manual review needed.

2. Koide/generation selector micro-queue.
   - Separate Koide value, generation ID, sector readout, and cross-sector
     selector gates.
   - Risk: must avoid forcing Koide.

3. Measure/weight/normalization micro-queue.
   - Separate prior, determinant/trace, dimension/Born, and normalization
     gates.
   - Risk: may need source-specific taxonomy.
