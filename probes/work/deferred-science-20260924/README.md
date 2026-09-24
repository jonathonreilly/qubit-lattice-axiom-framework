# Deferred science from the September 23–24 review drain

Status: **11 first-pass recovery units queued for maximum-thinking judgment workers**. This is an intake bundle, not a scientific verdict. The 160 PR landing drain preserved 3249 unmapped path occurrences (2603 distinct byte contents). Exact byte deduplication does not prove semantic equivalence. PR8648 also has a deferred physical-necessity scope despite no unmapped files.

## Start here

Use the ordinary `claim.py next --kind J --model <actual-model>` workflow in `probes/README.md`. No new worker, budget or model setting was started by this intake. Existing Opus maximum-thinking workers and other eligible J workers can claim these units; this is not an exclusive Opus reservation. One first pass per topic avoids spending multiple workers on the same recovery scan. New science HITs still require the existing independent confirmation route.

Read only your batch manifest, its linked canonical notes and necessary frozen sources. Start from the named target; do not read thousands of old files indiscriminately. Check related problem attempts before doing new calculations. If another active unit owns the same question, work a distinct unresolved candidate or record the exact existing assignment.

## Portable evidence

`manifest.json` holds every deferred path, frozen commit, SHA256, preserved remote branch and the accepted claim boundaries. `batch-NN.json` supplies the matching review findings and source subset. Original review reports and landing receipts are copied verbatim for auditability; their `/private/tmp` addresses are historical, not runtime dependencies. The portable Git addresses in the manifests are authoritative for retrieval. `recovery-verification.json` records fresh remote branch reachability and verification of every deferred source blob. No original source must be recovered from a temporary directory.

Fetch `origin <frozen-head>` if needed, then `git show <frozen-head>:<path>`; check its SHA256 before use. For mapped PR8648 source, use its head and accepted paths from batch 15 plus the original report's path mapping. `origin/main` is the current science authority; `ai/probes` may contain older science. The landing snapshot was `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`. Do not import stale science from the probe checkout as current truth.

Routing hints: 922 source-candidate occurrences, 1645 historical evidence occurrences, 682 process/context occurrences. Classification is filename-based and deliberately provisional. Old scripts can duplicate landed controls; a context file can contain substantive proof. Neither gets silently discarded. Use the SHA256 content group to avoid repeating identical bytes across packets.

## Work queue

| Task suffix | First target | Batch | Related existing problems |
| --- | --- | --- | --- |
| `formation` | Formation laws and nonlinear scaling | [5](batch-05.json) | `corrigendum-PR8178`, `corrigendum-PR8180`, `formation-response-kernel`, `plane-memory-loss-2` |
| `transport` | Record transport, capture and anisotropy | [6](batch-06.json) | `collisional-viscosity-and-eta`, `isotropic-streaming-clause`, `inertial-gas-viscosity-and-damping` |
| `ledger` | Local energy ledgers and source closure | [7](batch-07.json) | `a-bond-placed-stress-for-the-walk`, `the-ledgers-force-identity-exactly-on-the-lattice`, `a-ledger-that-reads-bond-energies` |
| `species` | Species, signed rays and field compatibility | [8](batch-08.json) | `are-the-eight-species-all-kept`, `all-eight-species-under-the-three-couplings`, `the-blind-walk-beyond-first-order` |
| `stability` | Stability, crowd thresholds and wall spectra | [9](batch-09.json) | `the-record-gas-chessboard-threshold`, `the-two-wall-level-rule-on-every-ring`, `the-reach-three-coupling-beyond-first-order` |
| `clock` | Clocked walks, topology and endpoint domains | [10](batch-10.json) | `the-clocked-walk-in-an-exponential-field-self-adjoint-realizations`, `the-alternations-walls-under-the-scalar-hop` |
| `formation-packets` | Mobile-record formation and excluded cooling source | [12](batch-12.json) | `formation-events-for-amplitudes-of-negative-energy`, `re-recording` |
| `spin-packets` | Finite-spin tails and saved-vector evidence | [13](batch-13.json) | `composite-bodies-rest-energy-without-a-larger-site-algebra` |
| `star-packets` | Electric-star preparation and uniform supply | [14](batch-14.json) | `composite-bodies-rest-energy-without-a-larger-site-algebra`, `the-rest-energy-of-a-record` |
| `residuals` | Rotor tails and ray/body physical identifications | [15](batch-15.json) | `internal-hop-energy-and-the-two-masses`, `p-equals-q-for-compact-and-strong-bodies`, `bending-over-fall-at-strong-field` |
| `assembly` | Assembly graph versus physical necessity | [15](batch-15.json) | `axioms-and-the-event-lattice` |

## Updating progress

`QUEUE.json` is the immutable intake snapshot, not live completion status. Live status comes from `claim.py status`, checked logs under `logs/probes/J:derive:deferred-20260924-*`, and per-worker `RECOVERY_STATUS.json` under `probes/work/derive/deferred-20260924-*/`. Workers write their own status files to avoid shared-index races. Record inspected hashes, dispositions, source/output links, remaining obligations and the next exact action. A completed first pass does not exhaust all deferred science; the remaining ranked obligations are the next campaign intake. Keep uninspected sources explicitly open. Do not publish a HIT for administration alone.

The landed corrected statements remain the baseline. No retained grade, physical model selection, continuum theorem, new axiom, or audit verdict is granted by this bundle. Previously refuted routes remain refuted. Salvage useful calculations and work explicit missing premises; do not inflate scope to make a task look successful.
