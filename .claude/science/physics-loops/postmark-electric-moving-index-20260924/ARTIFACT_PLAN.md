# Artifact plan

## Current candidate

The five-note Airy transfer candidate is committed on
physics-loop/postmark-electric-phase-correlation-20260924 at source revision
2d36bafc9ba85a2cd1e5e588d7892a79aa086903 and is based on non-draft PR #9091
at c734332ca227c4371f3c188f96227c494b43f533. The complete source and cache
set is in the proposed delta. The source candidate passed its exact-tree
combined gates; the current packet records those results and the final
package-tree rerun before PR creation. The delivered child PR is intended to
be ready for review, with formal audit and independent review pending.

The candidate is the third milestone in the postmark-electric parent row.
Its distinct mathematical object is transfer across the regular, Bragg,
central-contact, and positive Airy layers, not global quantization or the
readout. See the dated five-note section below for its limits and the
current-head route-selection result.

## Historical packet from the earlier four-note candidate



The following inventory and promotion gate describe an earlier proposal. They
are retained to preserve campaign history and are superseded for current
delivery by the five-note Airy milestone below.

The candidate starts at `origin/main` revision
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The four source notes and their
paired primary runners are in this same proposed review unit, so every
runner-declared input is either on that base or included in the PR delta.

| Artifact | Role | Current evidence | Remaining work |
|---|---|---|---|
| `docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Prepared-profile scalar reduction, exact spectral identities, and endpoint-strip support | Exact runner, fresh cache, exact finite identities, analytic tail/barrier proof | Current-base/source-hash, vocabulary, and combined pre-review gates |
| `docs/POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md` | 15-cell principal symbol and mod-3 folded crossings | Paired runner, cache, symbolic projection checks, finite corroboration | Current-base/source-hash, vocabulary, and combined pre-review gates |
| `docs/POSTMARK_ELECTRIC_TWO_BAND_CENTRAL_MATCH_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Crossing normal forms and finite-support central coefficient limit | Paired runner, cache, symbolic projection and interface checks | Current-base/source-hash, vocabulary, and combined pre-review gates |
| `docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Exact five-site Casimir family, four same-fiber crossing compressions, inter-fiber phase geometry, and principal action | Paired deterministic runner; note and runner hashes bound by the runner cache | Refresh after final note edits; rerun current-hash mutations; full note cold-read and combined gates |
| Four `scripts/postmark_electric_*_2026_09_24.py` runners | Reproduce the four bounded theorem surfaces | Declared timeouts and input manifests; canonical cache envelope | Force-refresh all four against final source bytes |
| `outputs/postmark_moving_index_2026_09_24/` | Runner receipts, route probes, failed attempts, and mutation logs | Full stdout/stderr and JSON retained; finite-spin limits are marked diagnostic; the exact anchor Schur/two-energy identity probe is under `attempt_logs/` | Refresh runner JSON and current-source mutations; keep pipeline's live log outside the fingerprinted worktree, then save its completed bytes here |
| `outputs/postmark_moving_index_2026_09_24/weighted_alias_diagnostic.py` and its JSON/log | Evaluate actual finite-profile lag weights, first-difference aliases, per-lag Abel bounds, and direct spectral-sum agreement | Float64/complex128 at (S=24,48,96); spectral/direct and lag-pair identities agree to numerical precision | Diagnostic only; do not convert sampled values into an asymptotic claim |
| Four `logs/runner-cache/postmark_electric_*_2026_09_24.txt` files | Canonical runner cache envelopes | All four have been force-refreshed after the independent dense echo and nonzero-u slope-check corrections | Preserve the current source bytes through the full pipeline |
| This loop pack | Source identity, route ranking, review record, and handoff | Selection review and campaign state recorded | Update timestamps, findings, PR status, and final gate results |

No audit ledger, audit verdict, authority registry, or publication status is
edited by this author lane. The added notes create citation-graph nodes and
edges; regenerate and inspect the citation manifest from the exact proposed
tree before commit.

## Promotion Value Gate (author self-review; not an audit certificate)

The four new source notes carry `Status: proposed_retained`. This is a request for
independent review, not a prediction of the audit verdict.

| Gate | Answer and evidence |
|---|---|
| V1 — unresolved target | At current base `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`, the core/boundary note leaves the supplied model's fixed-laboratory-time output open. This package reduces the (t=1/4) actual readout to one prepared-profile scalar, removes its endpoint-strip contribution in a double limit, and supplies exact local five-site/15-site bulk structure. The scalar's interior phase limit and the full candidate comparison remain open. |
| V2 — new evidence and search | The current-base search receipt is `outputs/postmark_moving_index_2026_09_24/attempt_logs/promotion_value_gate_repo_search_0e6ad.txt`. Main has the core/boundary and short-time results but not this quantitative (S^{-2}) profile rate, prepared-state endpoint-strip bound, central core correction, exact primitive five-site crossing compressions, or their paired runners. The 15-cell and five-site symbols are distinct local reductions; no matching open postmark PR was found by the recorded `gh pr list` queries. The weighted-alias JSON is a finite diagnostic, not part of the theorem claim. |
| V3 — obligation discharged | Yes for the four notes' declared support claims: the profile/readout reduction and endpoint bound, local folded-cell matrices, central coefficient limit, and exact five-site Casimir/Bloch/crossing/action identities have explicit proofs or exact algebraic derivations with deterministic reproduction. No interior scalar limit or separated actual-readout subsequence is proved. |
| V4 — concrete scientific gain | The prepared-state endpoint contribution vanishes after the relative strip width tends to zero, uniformly over the long phase. The local bulk description is sharpened from the 15-residue fold to an exact five-site coefficient family, with four explicit Bragg compressions, principal slopes, and the period-three cross-phase stationary set. The lobe action is derived with the physical-site factor of five. The weighted finite diagnostic shows the simple per-lag Abel estimate is numerically too large at its sampled spins; this only ranks proof work and has no asymptotic force. |
| V5 — variant/churn check | The current-base repo search found related local-symbol and central-coefficient inputs but no earlier note proves the quantitative endpoint reduction or the exact five-site inter-fiber package. The new results are supporting obligations in the still-open readout problem, not a relabeling of the principal bands. The five-site result does not upgrade the earlier 15-cell local result into global propagation. |

This gate is author self-review only. No independent final-source review,
formal audit, retained status, actual-readout limit, or axiom change is claimed.

## Personal follow-up branch after PR #9078

The current branch adds exploratory actual-generator and weighted-alias
diagnostics, followed by one bounded spectral-distribution theorem derived
from the already-proved five-site principal symbol and exact-side endpoint
norm bound. The new theorem is not part of parent PR #9078; it is a candidate
for a dependent review milestone after its source-specific gates pass.

| Artifact | Role | Current evidence | Remaining work |
|---|---|---|---|
| `docs/POSTMARK_ELECTRIC_PRINCIPAL_WEYL_COUNT_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Weak convergence of the supplied Jacobi empirical spectral measures; macroscopic quantile and normalized-phase profile | Fixed closed-walk moment proof, endpoint-strip rank control, compact-support moment argument; dependencies are the five-site symbol and exact-side norm bound | Cold-read final bytes, refresh paired runner cache and citation graph, run candidate validation; local gaps, phase-accurate quantization, and readout remain open |
| `scripts/postmark_electric_principal_weyl_count_2026_09_24.py` | Finite-spectrum moment and CDF corroboration | Eigensolves at S=8,16,32,64,128; finite errors recorded | Diagnostic only; it is not the analytic proof |
| `outputs/postmark_moving_index_2026_09_24/attempt_logs/` follow-up probes | Actual readout at larger S, all-lag aliases, Weyl-gap comparison, and quadratic-phase discriminators | Full stdout/JSON receipts retained with script/input hashes in `HANDOFF.md` | Keep as diagnostics and scope-corrected evidence; do not promote finite samples to a limit |

The author self-review found the moment normalization consistent: the
five-site fiber count reduces to the physical momentum symbol, the normalized
trace factor is `1/2` over the signed cell coordinate, and the limiting
moments are `4^m/(2m+1)`. The result does not differentiate the Weyl law into
an adjacent-gap estimate. Independent review and formal audit remain pending.

## Initial local transfer-phase block — completed

The ten-worker route review selected phase-accurate global quantization and
prepared-overlap transport as the path toward the actual fixed-time scalar.
This milestone isolates the first local calculation:

| Artifact | Role | Current state |
|---|---|---|
| `docs/POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Exact determinant-one five-site trace and oriented local phase through `S^-2` on compact regular bulk arcs | Derived; paired runner and canonical cache pass; final combined candidate validation remains pending |
| `scripts/postmark_electric_five_site_transfer_phase_expansion_2026_09_24.py` | Symbolic coefficient expansion, exact determinant/product identities, and finite trace/phase remainder diagnostics | Executed; source-specific mutation evidence is retained in the attempt logs |
| `outputs/postmark_moving_index_2026_09_24/FIVE_SITE_TRANSFER_PHASE_EXPANSION_RESULTS.json` | Reproducible result receipt | Generated by the primary runner |
| `logs/runner-cache/postmark_electric_five_site_transfer_phase_expansion_2026_09_24.txt` | Canonical source-bound runner record | Generate only after the final note and runner bytes are frozen |

The note's `O(S^-3)` statement rests on the compact analytic Taylor and
implicit-function argument, not on finite samples. Its limits are explicit:
no global quantization, crossing/turning matching, overlap transport, or
two-index cancellation is asserted. The new note creates a citation-graph
node; regenerate and inspect the manifest delta before committing the
review-ready block.

## Earlier four-note transfer/Bragg milestone — superseded by the Airy block

At that checkpoint the proposed review unit was built on the non-draft #9091 branch
`physics-loop/postmark-electric-weighted-phase-20260924` at
`c734332ca227c4371f3c188f96227c494b43f533`, plus the already-pushed phase
accuracy checkpoint commits through `20251000c51d7bd23573d36f091eb1c88ebde92a`.
The latest `origin/main` fetched for the value/search gate is
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`.

| Artifact | Role | Current evidence | Remaining limit |
|---|---|---|---|
| `docs/POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md` and its paired runner | Exact determinant-one local trace and oriented phase through `S^-2` | Exact symbolic trace/phase identities, finite exact-cell checks, shifted 15-site product identity, forced cache | Regular arcs only; no accumulated global phase |
| `docs/POSTMARK_ELECTRIC_REGULAR_BULK_PHASE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-24.md` and its paired runner | `O(S)`-cell regular transport with geometric overlap phase | Exact Berry identity, homological normal form, finite products with `S*error` bounded in the sample, forced cache | Uniform gap excludes Bragg, central, turning, and endpoint layers |
| `docs/POSTMARK_ELECTRIC_SIMPLE_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md` and its paired runner | Transfer through one simple interior `5k=m*pi` root | Exact symbolic moving-phase identity and two rejected formula mutations; exact finite products through a hyperbolic local cell at each tested `S`; forced cache | One root away from `u=0`; does not cover multiple, central, turning, or endpoint layers |
| `docs/POSTMARK_ELECTRIC_CENTRAL_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md` and its paired runner | Transfer at the four symmetry-suppressed central double contacts | Exact `A1(0)=0` and contact coefficients; fixed off-diagonal mutation rejected; 32 finite products across four energies; forced cache | Fixed energies only; no energy-uniform quantization or turning/endpoint propagation |
| `outputs/postmark_moving_index_2026_09_24/` plus four canonical cache files | Durable results and source-bound execution records | Direct runner outputs, source hashes, finite diagnostics, failed attempts and correction logs | Refresh caches after any source edit; retain complete full-pipeline logs outside the fingerprinted worktree until finished |
| This loop pack and citation-graph manifest | Route, assumptions, handoff, value gate, and source graph | Ten route-selection reviews plus personal proof checks recorded | Exact candidate conformance and final all-stage validation still required before opening the PR |

The four notes prove only conditional support for the displayed scalar Jacobi
family. The finite checks corroborate the calculations; they do not establish
the analytic rates, global quantization, prepared overlaps, or the actual
fixed-time readout. No axiom update is supported.

## Promotion Value Gate for the earlier transfer/Bragg milestone

| Gate | Answer and evidence |
|---|---|
| V1 — unresolved target | The unresolved obligation is phase-accurate propagation and prepared-overlap transport needed to estimate the interior of the exact `Re(q_S(1/4))` in `docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md`. This milestone supplies phase transport only on regular arcs, one simple Bragg crossing, and four fixed central contacts. |
| V2 — new evidence and search | The exact commands, refs, and hits are recorded in `outputs/postmark_moving_index_2026_09_24/attempt_logs/promotion_value_gate_transfer_search.md`. On refreshed `origin/main` `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` and parent `c734332ca227c4371f3c188f96227c494b43f533`, `git grep` found no matching moving-frame macroscopic product, simple-root transfer, or central quadratic-contact theorem. The nearest parent result is a first-order frozen five-site band correction that leaves global transport open. The PR search returned #9078 and #9091 only; both are non-draft and neither contains the proposed transfer-product results. |
| V3 — obligation discharged | Yes for the four exact bounded statements: the compact-regular `S^-2` cell phase, regular `O(S)`-cell transport with `O(S^-1)` error, simple Bragg transfer with `O(S^-1/3)` error, and central double-contact transfer with `O(S^-1/2)` error. Each proof states its compactness, gap, and crossing hypotheses; no whole-spectrum or readout gap is concealed. |
| V4 — concrete gain | Before this block, the source had a frozen local band correction and crossing matrices but no transfer product over a growing number of actual-index cells. The new derivations add the geometric phase accumulated by moving eigenvectors and explicitly cross two kinds of repeated-root layer. They remove these bounded propagation subproblems from the global target while leaving the hard energy-uniform and overlap problem visible. |
| V5 — variant/churn check | No: this is not a one-step variant of the principal Weyl count or the frozen five-site symbol. The closest prior postmark theorem supplies only fixed-cell coefficients and first-order frozen-band data. Here the load-bearing construction is a slowly varying determinant-one transfer product and its gap-dependent normal form; the central estimate additionally uses the exact vanishing `A1(0)=0`. Both searches above used refreshed `origin/main` and record its commit. |

## Earlier cluster-cap evaluation for the four-note transfer/Bragg block

**OPEN.** The proposed milestone is the third PR in the postmark-electric
parent-row family after #9078 and #9091, so I applied the repository's
cluster-cap brief locally as the user requested personal execution. All four
notes are a single review unit: the local trace/phase expansion supplies the
cell coefficients, the regular theorem proves actual-index transport away
from resonances, and the two crossing theorems close distinct simple and
central degeneracies. The load-bearing addition is not merely another
bounded-theorem label: it is the first macroscopic product estimate for the
slowly varying scalar transfer, with an eigenvector-overlap phase, followed
by two distinct mechanisms for passing repeated-root layers. The artifact
type remains `bounded_theorem`, which is the same broad type as the prior
milestones, but the prior #9078 note gives frozen bands and first-order
crossing compressions while #9091 gives only a macroscopic spectral counting
law; neither provides these product estimates. The notes and their paired
runners make the chain independently reviewable as one source-defined
mathematical family, while keeping physical identification with the supplied
model conditional. A single combined PR is more reviewable than four narrow
variants because the phase coefficient is shared and the crossing bounds
depend on the same moving-frame expansion. The per-PR delta is justified by
the new transport theorems, not by numerical sample volume or the prior PR
count. This verdict gates opening only; it is not an audit prediction.

## Observable-aware phase accuracy checkpoint (personal follow-up branch)

Branch `physics-loop/postmark-electric-quantization-phase-20260924` is based
on `physics-loop/postmark-electric-weighted-phase-20260924`, whose bounded
Weyl-count milestone is open as non-draft PR #9091 stacked on #9078. The new
finite probe
`outputs/postmark_moving_index_2026_09_24/attempt_logs/phase_accuracy_gate_probe.py`
records an exact phase-perturbation inequality, the operator-norm alternative
that removes a common phase, and actual pair-weight mass by lag. At S=96,192,
384,512, the total pair-weight L1 divided by sqrt(S) is 1.209,1.203,1.198,1.197;
most absolute mass is at h>D/4. The best quadratic phase fit has nonmonotone
actual q error 0.00030--0.0232 and does not approximate the prepared state in
norm. All outputs are finite diagnostics, not evidence of a limit or separated
subsequences. The next proof obligation is an observable-aware estimate of the
macroscopic-lag sum with every reciprocal alias; no new theorem or PR is
claimed by this checkpoint.

## Current five-note Airy transfer milestone — 2026-09-24 20:30 UTC

The proposed review unit contains the four local/regular/Bragg transfer notes
and the positive simple-turning-point Airy note, with their five paired
runners, result files, caches, mutation receipts, and this source pack. The
active branch is `physics-loop/postmark-electric-phase-correlation-20260924`
at committed head `20251000c51d7bd23573d36f091eb1c88ebde92a` plus staged
science. It is based on the pushed non-draft #9091 head
`c734332ca227c4371f3c188f96227c494b43f533`. The intended child PR must keep
that base until its source dependencies land. The Airy note proves a fixed
window and ordered allowed-side match only; no tail selection, full-spectrum
quantization, prepared overlap, or readout closure follows.

| Source pair | Bounded result | Current limit |
|---|---|---|
| Five-site transfer phase | Local trace/eigenphase through `S^-2` on compact regular arcs | No growing-cell phase claim |
| Regular bulk transport | `O(S^-1)` product error on a compact nonresonant interval | No crossing or edge coverage |
| Simple Bragg transport | `O(S^-1/3)` at one simple interior root | No energy-uniform crossing family |
| Central Bragg transport | `O(S^-1/2)` at four fixed contacts | Fixed energies only |
| Positive turning-point Airy transfer | Jordan-scaled `q''=b_lambda tau q`, edge shift, and ordered WKB match | Remote forbidden tail and boundary selection are open |
| Citation manifest and campaign pack | Dependency topology and source recovery | Regenerated manifest has 6,658 nodes/14,643 edges: five added note nodes, eight intended outgoing edges, no removals or rewires; pack names the next tail campaign | Exact-tree pipeline and final source identity still required |

## Cluster-cap evaluation for the five-note transfer milestone

**OPEN**

The proposed PR is the third item in this postmark-electric parent
row, after #9078 and #9091, and therefore repeats the broad `bounded_theorem` claim type.
That repetition is a real review risk; the case for a separate milestone is
the mathematical object added, not the number of artifacts. The current-main
source search found no five-residue turning-point Airy transfer note or
moving-cell transfer estimate with the present hypotheses. The first note
defines the scalar coefficient family directly. Four dependent notes then
prove separate results for regular propagation, a simple Bragg root, central
double contacts, and the parabolic `k=pi` turn. Their common recurrence,
transfer convention, and phase gauge make them one review unit; splitting
them would make each small PR rely on an unlanded local premise from its
immediate predecessor.

The Airy result is not another Bragg variant. At `k=pi` the exact cell has a
parabolic Jordan block and the characteristic gap opens like the square root
of distance. Its `S^-2/3` rescaling yields the Airy system, fixes the
coefficient `800 a_lambda/lambda`, and matches the allowed principal frame
with an outer error `C R^-3/2`. The `S^-1` finite edge displacement is also
derived and checked against the trace expansion. The paired result receipt
reports zero symbolic residuals for the edge slope and shift identities, a
maximum scaled-cell determinant error of `1.16e-14`, and finite propagator
errors within the stated envelope at three energies and four spins. Those
products corroborate the formulas; the proof rests on the determinant
identity, uniform Taylor expansion, normal form, and discrete Gronwall
argument.
Physical identification with the supplied model remains conditional, and
endpoint selection, global quantization, overlaps, and the readout stay open.
I judge this unit distinct enough for one ready-for-review PR after the exact
combined gates pass. That is an author-side cluster-cap judgment, not an
independent review or audit prediction.

## Promotion Value Gate for the Airy transfer milestone

| Gate | Answer and evidence |
|---|---|
| V1 — unresolved target | The interior `Re(q_S(1/4))` still requires phase-accurate eigenfunctions and prepared overlaps. |
| V2 — new evidence and search | The current-main source-search receipt is `outputs/postmark_moving_index_2026_09_24/attempt_logs/airy_turning_point_current_main_search.md`; it found no matching Airy/turning or five-site transfer source. The new note derives the Jordan form, turning scale, coefficient, and edge shift; its runner checks the exact identities and finite diagnostics. |
| V3 — obligation discharged | Only the fixed compact-energy Airy window and ordered allowed-side match are proved; remote forbidden propagation and finite-endpoint mode selection remain open. |
| V4 — concrete gain | The `k=pi` local coalescence and its `O(R^-3/2)` overlap error are now explicit inputs for a later global quantization proof. |
| V5 — variant/churn check | The Jordan/Airy normal form differs from both the simple/central Bragg layers and the principal Weyl count; it supplies no global closure claim. |
