# Exact affine-chart algebra of the sector grading on the stipulated one-block ledger model — Cycle 876 (salvage)

Date: 2026-08-09

Authority: none

Audit: unset

Status: conditional bounded theorem (exact finite algebra on stipulated
in-file definitions; one primary and one independent checker spec'd to
refute; no axiom surface touched; NO derivation of the grading, NO
negative exhaustiveness claim, NO global or projective maximizer claim,
NO gravity-sign claim, NO selection among candidate laws, NO convention
or owner decision surface)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle876_grading_affine_chart_algebra_2026_08_09.py`](../scripts/frontier_cycle876_grading_affine_chart_algebra_2026_08_09.py)
- [`frontier_cycle876_grading_affine_chart_algebra_independent_check_2026_08_09.py`](../scripts/frontier_cycle876_grading_affine_chart_algebra_independent_check_2026_08_09.py)

Receipt:

- [`grading_affine_chart_algebra_cycle876_receipt_2026_08_09.json`](../outputs/grading_affine_chart_algebra_cycle876_receipt_2026_08_09.json)
- [`grading_affine_chart_algebra_independent_check_cycle876_receipt_2026_08_09.json`](../outputs/grading_affine_chart_algebra_independent_check_cycle876_receipt_2026_08_09.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: rebuilt by the review-loop salvage pass 2026-08-09
after the original Cycle-876 package was REJECTED in review (see the
Review record below). Independent audit still required.

## What the claim is, exactly

An exact finite-algebra result on a stipulated in-file model, and
nothing more. Both runners are SELF-CONTAINED in the scientific sense:
the external and ancestral scientific input set is EMPTY — neither
runner reads, pins, or imports any landed construction, any ancestor
artifact, or any file outside this package, and no certified value
below comes from anywhere but the in-file stipulations. What each
runner does read is declared package-local integrity reading, emitted
in its own certificates and receipt: the primary declares no audit
input paths and reads only its own source bytes for the self-identity
hash; the checker reads the primary's source and the primary's receipt
(its comparison targets, as text, never imported) plus its own source
bytes for its self-identity hash. The model — six signed unit lattice
directions, three sectors (matter, field, auxiliary), supports =
(incoming direction, sector triple), the per-sector recoil ledger, the
balance residual, the modeled single-exchange support families, and
the two-endpoint graded-source response algebra — is stipulated
IN-FILE in the primary and rebuilt from an independent in-file
transcription in the checker.

The landed constructions whose shapes these stipulations restate are
named here as plain provenance text, deliberately NOT linked (they are
cross-references for the reader, not inputs of either runner and not
dependency edges), each at its `origin/main` blob, verifiable with
`git cat-file`:

- the carried-link construction
  `scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py`
  (blob `c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0`) — the modeled
  carried-link support family restates its target shape;
- the two-sector candidate-law construction
  `scripts/proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18.py`
  (blob `7672380148d79f22a4ab9b2700121aac1b097004`) — the modeled
  two-sector constraint restates its support shape;
- the direction-table source
  `scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py`
  (blob `0be8d83ec8ed874ff12e2092dc47121b8030a5bc`);
- the stipulated response-object algebra
  `scripts/frontier_cycle868_response_sign_census_2026_07_28.py`
  (blob `c155a2dafaccde60c17047303c6de358445711c3`, the current-main
  repaired version, which itself records that whether its grading sign
  is the physical conformal-mode sign remains OPEN);
- the tracelessness-provenance source
  `scripts/frontier_cycle873_tracelessness_provenance_2026_07_28.py`
  (blob `e864c431ac9d5596f06d93ac6983986e70a2571d`, the current-main
  repaired version).

Everything below is conditional on the stipulated model and its
declared scope; nothing below is a statement about the axiom surface,
about any landed certificate, about physical gravity response, or
about the selection of any grading.

## The certified calculations, exactly

On the stipulated model (6 directions, 3 sectors, 1,296 supports):

1. **Conditional equivariance collapse.** On the SUPPLIED
   sector-indexed vector-readout ansatz `f_s : {6 directions} -> K^3`,
   proper-cubic equivariance `f(R d) = R f(d)` is a rank-17 condition
   on 18 coefficients per sector, leaving exactly one scalar per
   sector (`f(d) = w * D[d]`). The ansatz is an import: nothing here
   derives it from the framework's scalar record readout, and that
   bridge is OPEN.

2. **The modeled balance planes.** Lawfulness of the modeled
   carried-link support family is exactly
   `-2*w_matter + w_field + w_auxiliary = 0` (rank 1); the modeled
   two-sector constraint is exactly `-2*w_matter + w_field = 0`
   (rank 1). The overall-scale direction (1,1,1) lies inside the
   carried-link plane, and the scale quotient leaves exactly ONE
   scalar degree of freedom — with no coefficient-field restriction
   imposed or needed.

3. **The affine chart, disclosed.** `w(t) = (1, 1+t, 1-t)`
   parameterizes exactly the `w_matter != 0` part of the
   scale-quotiented plane. On that chart the balance residual is
   identically `A + t*B`, with `A` the grading-independent sector
   trace and `B = D[field] - D[auxiliary]` — an affine-in-`t`
   identity, so it holds for every `t` in every characteristic-zero
   coefficient field.

4. **The exceptional-value census, complete on the chart.** Every
   support is lawful for all `t`, for exactly one rational `t`, or for
   no `t` (the census classes 6 / 144 / 210+936 partition the 1,296
   supports), so the lawful count as a function of the chart parameter
   is fully classified: **90 at `t = 0`, 36 at `t = +1`, 36 at
   `t = -1`, and 6 at every other `t`** — off the onset set AND off
   the unit point — in any characteristic-zero field. Lawful
   trace-bearing supports exist exactly at `t` in {-1, +1} (30 at
   each, all 30 with nonzero matter recoil); the always-lawful class
   is exactly the 6 modeled supports, all traceless.

5. **The chart-infinity negative control (the reviewer's
   counterexample, kept as a gate).** At the scale class
   `[0 : 1 : -1]`, excluded by the chart, the lawful-support count is
   **216** (210 trace-bearing, 174 with nonzero matter recoil), and
   lawfulness there is verified scale-invariant. 216 > 90, so the
   rejected package's claim that the unit grading globally maximizes
   lawful support count on the scale-quotiented locus is REFUTED, and
   the refutation is a fail-closed gate in both runners: every
   maximality-flavoured statement in this package is affine-chart
   scoped only, and the projective classification is OPEN.

6. **The stipulated response identity.** On the in-file two-endpoint
   graded-source algebra (per endpoint,
   `graded[s] = block[s] - C/3 + sigma*C/3` with `C` the sector-summed
   conformal channel, endpoints swapped), the sector-summed object
   equals `sigma * C` exactly, so sigma-sensitivity is EQUIVALENT to a
   nonzero sector trace — verified on all 1,296 supports under both
   endpoint embeddings. Whether this stipulated algebra is the
   physical conformal-mode response of any lane is expressly OPEN.

7. **The joint-constraint intersection, conditional.** IF the modeled
   carried-link constraint and the modeled two-sector constraint are
   imposed JOINTLY — and the constructions they restate are
   alternative candidate laws, so nothing licenses the conjunction —
   the rank-2 system meets the chart at exactly `(1, 2, 0)`, chart
   parameter `t = +1`, where the modeled two-sector support is lawful
   and the unit point leaves it unlawful. This is conditional linear
   algebra with NO selector authority: it argues for nothing and
   against nothing.

## Checker

Independent in-file rebuild of the whole model: its own direction
table in a different order, the rotation group built by generator
closure rather than permutation enumeration, its own per-support
lawful-parameter solver, integer multiply-only elimination plus
modular rank over three large primes against the primary's rational
elimination, a four-coordinate chart-infinity enumeration (the
reviewer's route) with a scaled-representative invariance check, its
own response-algebra transcription, and its own joint elimination.
Every advertised claim-survival row is a real recomputed comparison
that fails closed, and the certified-statement texts are re-rendered
verbatim from the checker's OWN recomputed values and compared byte
for byte. The verdict covers every certified value family of the
primary receipt — 17 claim-survival rows, none omitted. Verdict
**CORROBORATES**, 14/14 teeth bite (each tooth plants one corruption
into a copy of the receipt and requires the SAME comparison function
used for the live verdict to catch it — including the exact shape of
the refuted global-maximum overclaim, the chart-infinity count
suppressed to 90). A three-way corruption of the on-disk receipt
(chart-infinity count, unit count, statement text) was confirmed to
exit nonzero with all three row classes refuted, and a single
suppressed chart-infinity count alone was confirmed to exit nonzero.
Both runners exited 0 with all certificates PASS.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "carry the durable exact finite calculations of the rejected Cycle-876 package as affine-scope bounded support: the conditional equivariance collapse, the modeled balance planes, the chart normal form, the complete exceptional-value census, the chart-infinity negative control, the stipulated response identity, the conditional joint intersection"
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "any future work on the sector grading starts from this affine-scope inventory plus the chart-infinity control; everything the rejected package claimed beyond it (a provenance census, a five-route negative boundary, a global maximizer, gravity-sign visibility, an owner decision surface) remains NOT ESTABLISHED and would need to be built from scratch against current-main inputs, starting with the OPEN projective classification"
```

## Status fields

```yaml
actual_current_surface_status: conditional-support (exact affine-chart finite algebra, conditional on the stipulated in-file definitions and the supplied vector-readout ansatz; unaudited)
target_claim_type: bounded_theorem
conditional_surface_status: conditional on the stipulated in-file model, the supplied vector-readout ansatz, the disclosed affine chart, and (for the joint intersection) the expressly unlicensed conjunction of the two modeled constraints
hypothetical_axiom_status: null
admitted_observation_status: null
packet_helper_runner: scripts/frontier_cycle876_grading_affine_chart_algebra_independent_check_2026_08_09.py
claim_type_reason: "exact finite certificates of the equivariance collapse, the balance planes, the chart normal form, the exceptional-value census with its domain-neutral count function, the chart-infinity negative control, the stipulated response identity, and the conditional joint intersection; nothing derived beyond the stated conditionals, nothing selected, no negative boundary claimed"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (load-bearing; stipulated definitions and scope inputs only)

- the stipulated in-file model definition: the six signed unit
  directions, the three sectors, the per-sector recoil ledger, the
  balance residual, and the two modeled single-exchange support
  families (restated in-file in both runners);
- the SUPPLIED sector-indexed vector-readout ansatz
  `f_s : {6 directions} -> K^3` consumed by the equivariance collapse;
- the stipulated two-endpoint graded-source response algebra;
- the disclosed affine chart `w_matter = 1` (equivalently
  `w_matter != 0`) for every chart-scoped statement;
- for the joint intersection only: the expressly unlicensed
  conjunction of the two modeled constraints.

### Provenance context (non-load-bearing)

- the five landed sources named in the opening section, each at its
  `origin/main` blob — plain text cross-references, not inputs, not
  dependency edges; the legacy module names and the rejected
  Cycle-876 package runners are import-blocklisted in both runners;
- the identification of the stipulated model (and its response
  algebra) with any landed substrate is an OPEN bridge, as the
  current-main response-census source itself records.

### Derived (conditional on the stipulated model and stated imports)

- the rank-17 equivariance collapse to one scalar per sector;
- the two balance-plane equations, the in-plane scale direction, and
  the one-dimensional scale quotient;
- the `A + t*B` chart normal form with trace = `A`;
- the complete exceptional-value census and the domain-neutral count
  function 90 / 36 / 36 / 6 with onset exactly {-1, +1};
- the chart-infinity counts 216 / 210 / 174 and the refutation of the
  global-maximum claim;
- the response identity `sector sum = sigma * C` and the
  sensitivity-iff-nonzero-trace equivalence;
- the conditional joint-intersection point `(1, 2, 0)`.

### Open (expressly not decided here)

- the projective classification of the full scale-quotiented lawful
  locus (the chart-infinity point is certified only as a negative
  control; no maximizer statement of any scope is made);
- any derivation of the sector grading, of the vector-readout ansatz,
  or of any point on the chart;
- whether any route family exhausts the forcing arguments (no
  negative boundary is claimed; the rejected package's five-route
  ledger is NOT re-shipped);
- whether the stipulated response algebra is the physical
  conformal-mode response of any lane (gravity-sign visibility,
  escape, and wall statements are all OPEN);
- any conjunction bridge that would license imposing the two modeled
  constraints jointly, and any selection among candidate laws;
- the disposition of the grading choice itself (no convention, no
  primitive, no owner decision surface is proposed here).

## Review record

The original Cycle-876 package ("the unit grading: supplied, priced to
one rational", PR #5931) was REJECTED by the sole combined adversarial
science review (FAIL/SALVAGE_REJECT, 18 findings, 2026-08-08).
Decisively, and recorded here so it cannot be lost: the original
package's claim that the unit grading is the GLOBAL maximizer of
lawful support count (90) on the scale-quotiented lawful locus was
**REFUTED by the reviewer's projective counterexample**: the omitted
scale class `[0 : 1 : -1]` — unreachable by the package's
`w_matter = 1` gauge chart — carries **216 lawful supports** (210
trace-bearing, 174 with nonzero matter recoil), exceeding 90 and
adding a sigma-visible locus at chart infinity. This salvage claims
the AFFINE-scope result only; the projective extension is an OPEN
question; and the reviewer's counterexample is ADDED to both runners
as a fail-closed negative-control gate (216/210/174, with
216 > 90 asserted), so the same overclaim cannot recur silently.

Further grounds for the rejection, compressed:

- the shipped negative boundary (five routes plus four checker
  families, "none forces") had no landed no-go evidence packet and no
  multiresolution execution certificate;
- the package was pinned to rejected/unlanded ancestor semantics
  (pre-repair response-surface and tracelessness sources and a
  superseded premise registry) and could not run against
  `origin/main`;
- the independent checker reported PASS and exited zero even when an
  attack landed a refutation, and several primary PASS gates did not
  assert their load-bearing targets;
- the claimed axiom-derived readout shape assumed the vector/sector
  ansatz it purported to derive, and its scalar cross-check was
  tautological;
- rationality of the surviving parameter was assumed, not derived or
  disclosed;
- the intersection of two ALTERNATIVE candidate laws was promoted to
  what "the landed tree selects";
- sigma sensitivity was proved only for a stipulated two-object
  algebra yet shipped as gravity-sign visibility with an escape
  declared live;
- a consequence-changing grading choice was mislabeled a "named
  convention" on an owner decision surface;
- a hand-listed 13-site "provenance census" was presented as
  exhaustive while the runner's own scan found an uncensused site;
- support-level lemmas were promoted to "every Cycle-320 certificate
  survives";
- naming used bare route codes and campaign/branch vocabulary as
  primary science names, and the new audit node was unacknowledged by
  the citation-graph manifest.

Per the salvage disposition, ONLY the exact affine finite-algebra
calculations were preserved, on in-file stipulated definitions — which
is exactly and only what this package contains, with every formerly
hidden import now declared (the vector ansatz, the chart restriction,
the stipulated response algebra, the unlicensed conjunction) and the
coefficient-field question resolved domain-neutrally (the census
holds over every characteristic-zero field, so no rationality premise
is imported). Every claim of the rejected package beyond these
calculations (the provenance census, the five-route negative
boundary, the global-maximum and unique-maximizer claims, the
"tree argues against the unit grading" selector reading, gravity-sign
visibility and the escape declaration, the weakened-wall restatement,
the owner decision surface and the convention proposal, and every
statement about landed certificates surviving) was DROPPED, is NOT
ESTABLISHED, and must not be cited from this note or from the rejected
package. The rejected delta files are deleted on this branch and
remain recoverable on the retained PR head.

Fail-closed and packet-visibility properties are built in from the
start, per the paired-salvage precedent:

- the checker's verdict rows are all real recomputed comparisons; any
  refutation exits nonzero; 14 planted-corruption teeth run the same
  comparison function as the live verdict, and an on-disk corruption
  battery (three-way, and single-flip chart-infinity suppression) was
  confirmed to exit nonzero;
- runner-emitted receipts carry no hand-added review metadata; all
  review provenance lives in this Review record;
- the independent checker is deliberately not imported by the
  primary, so import discovery cannot see it; it is declared
  claim-scoped and co-load-bearing with a machine-readable
  `packet_helper_runner` line in the Status fields. HARD LANDING
  CONDITION: at landing, the orchestrator must add exactly this
  claim-scoped entry to `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py` (this branch must not
  edit audit tooling):

  ```python
  "grading_affine_chart_algebra_cycle876_support_note_2026-08-09": [
      "scripts/frontier_cycle876_grading_affine_chart_algebra_independent_check_2026_08_09.py",
  ],
  ```

  HARD LANDING CONDITION (manifest): the note changes citation-graph
  topology, so the regenerated
  `docs/audit/data/citation_graph_manifest.json` acknowledgment must
  co-land at landing time; it is deliberately absent from this
  branch-local package.

Three mechanical findings from the confirmation round were fixed in a
second pass, with no change to any computed value:

- the blocker source now carries the canonical value `review_loop`;
  the branch-local wording it replaced was not a permitted value;
- the current surface status is now `conditional-support`. The claim
  mix is the deciding factor: the census is exact on its computed
  domain, but the equivariance collapse rests on the supplied
  vector-readout ansatz and the response identity on the stipulated
  in-file algebra, so the package as a whole stands only if those
  supplied objects are granted. That is what landed notes call
  conditional support — an exact finite result held up by a supplied
  input, as with a supplied color ray or a supplied operator skeleton
  — rather than bounded support, which scopes an unconditional result
  to a restricted domain. `bounded_theorem` remains the claim type;
  it is not a status value;
- the earlier absolute claim that neither runner reads any repository
  file was wrong and is replaced everywhere by the two-part inventory
  above: an empty external and ancestral scientific input set (the
  firewall claim, which holds) and explicitly listed package-local
  integrity reads, now emitted by the runners themselves.

## Verdict

A stipulated finite model and the exact algebra it satisfies on a
disclosed affine chart: one conditional representation collapse, two
balance planes, a normal form, a complete exceptional-value census, a
stipulated response identity, one conditional intersection — and, kept
permanently on guard, the reviewer's chart-infinity counterexample
that refuted the rejected package's global claim. Nothing is derived
beyond the stated conditionals, nothing is selected, and every
question that would make this physics is stated in Open. Independent
audit still required.
