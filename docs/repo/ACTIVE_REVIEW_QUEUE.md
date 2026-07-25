# Active Review Queue

**Status:** canonical live queue for current-main review feedback  
**Purpose:** single place to record reviewer findings that still need a decision,
fix, or explicit rejection on `main`

## Rule

Use this file for **active** review feedback only.

- add new reviewer findings here first
- keep each item short and decision-oriented
- link any long-form packet in
  [`docs/work_history/repo/review_feedback/`](../work_history/repo/review_feedback/README.md)
- when an item is resolved, remove it from the open list and record it in the
  queue history section or the linked detailed packet

Do not use scattered backlog notes or branch-local memos as the live review
truth surface.

## Current State

As of `2026-07-16`, the queue includes the four runner/cache audit-readiness
items below together with the existing science-facing open lanes. The runner
failures are recorded honestly; no claim or content gate is weakened to clear
them.

Current science/open-lane follow-ups:

- `2026-07-24-cycle583-landed-provenance-table-drift`
  Scope: the Cycle-583 infinite-internal-content note and its paired
  runner/receipt after the Cycle-578/583 substrate repair.
  Finding: the runner and receipt enforce the repaired landed bytes, but the
  note still prints the superseded Cycle-583 runner and Cycle-578
  runner/receipt/note SHA-256 values.  Editing the note alone would invalidate
  the receipt-to-note binding, so repair requires a source-side sibling-pin
  sweep and regenerated receipt/transcript rather than a one-line table edit.
  Disposition: `fix on main`.
- `2026-07-19-unit-singlet-physical-consumer-projection-repair`
  Scope: the two-Ward/Step-3 notes and runners that consume the abstract
  central-positive Hilbert--Schmidt theorem, together with their canonical
  harness and raw derivation-atlas descriptions.
  Finding: the abstract theorem and its three-mode runner are independently
  valid, but the physical consumers combine a direct-color Fierz coordinate
  with a crossed-spin scalar projection. That mixed pairing does not establish
  the claimed `1/6` scalar coefficient, residual, same-1PI exhaustion, or
  `g_bare` pin. Several sibling runners also remain stale-green or retain
  obsolete accepted/retained authority language. PR #5501 salvages only the
  self-contained abstract theorem; none of those physical conclusions lands
  through that repair.
  Disposition: `science-needed` for a coherent color x spin projector and
  Grassmann sign; `fix on main` for the stale consumer/control-plane wording
  once the physics coefficient is recomputed.
- `2026-07-18-toe-bounded-notes-failed-negative-gate-packaging`
  Scope: the five unaudited bounded claim candidates for continuation
  refinement, extensional nearest-neighbor construction, generated finite
  composition, read/reset cadence, and finite controlled-copy fan-out.
  Finding: each note preserves a durable positive bounded core, but also
  ships semantic negative or bounded-with-named-walls conclusions while its
  own No-Go Discipline N1 result is `FAIL / DO NOT SHIP`. Renaming those
  conclusions as boundaries or import inventories does not clear the
  full-note semantic gate. Split or remove the negative claim surfaces and
  retain only the positive constructions, or supply a narrowed N1--N8 packet
  that passes before review-loop can issue PASS.
  Disposition: `science-needed`.
- `2026-07-10-pr5123-tick-admissibility-physical-realization-bridge`
  Scope:
  `TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md`
  and the conditional equivariant lemma salvaged from PR #5123.
  Finding: the submitted `REAL(U; A, F)` predicate assumes the load-bearing
  rule-to-tick correspondence, with conditioning faithfulness already imposing
  nonzero tick support on every varying edge. The exact fixed-assignment
  covariance implication is reusable bounded algebra, but it does not derive
  the physical tick--Admissibility realization bridge or discharge/requeue the
  selector row's `missing_bridge_theorem` repair target.
  Disposition: `science-needed`.
- `2026-07-10-conformal-causal-source-packet-repair`
  Scope: the record-order and reconstructed-H inputs to the conformal-class
  metric packet, plus
  `scripts/emergent_metric_conformal_class_from_records_runner.py`.
  Finding: a retained no-go is being accepted as a positive causal-order
  premise; the microcausality note conflates one-particle and full-Fock
  spectra, drops `1/a_tau`, and lacks the quasilocal LR composition; the
  consumer exits zero on failures and labels sampled group velocity as an LR
  velocity.
  Disposition: `fix on main`.
  Detail:
  [`CONFORMAL_CLASS_CAUSAL_SOURCE_PACKET_REVIEW_2026-07-09.md`](../work_history/repo/review_feedback/CONFORMAL_CLASS_CAUSAL_SOURCE_PACKET_REVIEW_2026-07-09.md)
- `2026-07-10-acphilambda-retirement-rematch-drift`
  Scope: `ACPHILAMBDA_RETIREMENT_BASIS_REMATCH_AND_CLAIM_SURFACE_NOTE_2026-07-06.md`
  and `scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py`.
  Finding: seven of the sixteen rematch basis rows are currently non-retained
  and the custody-capstone structure/value split fails; PR #5115 refreshes the
  previously stale-green cache but does not weaken or rewrite the gate.
  Disposition: `science-needed`.
- `2026-07-10-runner-cache-input-freshness`
  Scope: `scripts/runner_cache.py`, `scripts/codex_audit_runner.py`, and runners
  whose results depend on mutable notes, registries, or ledger data.
  Finding: cache freshness is keyed only to runner-source SHA, so a cache can
  remain classified `fresh` after a load-bearing input changes and can be
  consumed before a live fallback; add a dependency-aware input fingerprint or
  equivalent manifest design.
  Disposition: `fix on main`.
- `2026-07-10-residual-admission-runner-pin-sweep`
  Scope: eight older `acphilambda_*` runners that still index the retired AC
  entry under live `derivation_targets`, plus
  `audit_companion_observable_principle_p2_phase_blindness_sector_resolved_2026_06_04.py`.
  Finding: the sibling pin sweep for PR #5115 found additional pre-existing
  post-retirement crashes and one stale admission-count gate outside the
  four-runner repair slice; repoint them to the historical registry plus exact
  open obligations without weakening their content checks.
  Disposition: `fix on main`.
- irregular off-lattice sign lane: portability beyond the bounded centered
  core-packet surface remains open
- periodic 2D torus diagnostics: nearby torus probes still need code audit
  before reuse outside the corrected retained notes
- Wilson two-body lane: full both-masses law and action-reaction remain open
- boundary-law / holographic lane: keep the effect bounded and do not overread
  it as a holography derivation
- `2026-05-03-gbare-parent-retention-gate`
  Scope: `G_BARE_DERIVATION_NOTE.md` and downstream `g_bare = 1` status
  surfaces.
  Finding: the salvaged rescaling-freedom and constraint-vs-convention
  candidate rows must be independently audited and retained, with retained
  dependency closure, before the parent theorem or status surfaces cite them
  as closing repair targets.
  Disposition: `science-needed`.
- `2026-05-03-pr463-axiom-first-weave-gate`
  Scope: PR #463, `CANONICAL_HARNESS_INDEX.md`,
  `docs/publication/ci3_z3/DERIVATION_ATLAS.md`, and the `AXIOM_FIRST_*`
  package.
  Finding: do not weave grouped axiom-first foundational blocks onto retained
  core or publication authority surfaces while member rows are mixed
  `audited_failed`, `audited_conditional`, and `unaudited`; that would
  authority-promote non-clean claims.
  Disposition: `science-needed`.
  Detail:
  [`PR463_AXIOM_FIRST_WEAVE_REVIEW_2026-05-03.md`](../work_history/repo/review_feedback/PR463_AXIOM_FIRST_WEAVE_REVIEW_2026-05-03.md)
- `2026-05-03-pr484-kz-external-lift-gate`
  Scope: PR #484,
  `GAUGE_SCALAR_BRIDGE_KZ_EXTERNAL_LIFT_THEOREM_NOTE_2026-05-03.md`,
  `scripts/frontier_gauge_scalar_bridge_kz_external_lift.py`, and the
  gauge-scalar temporal bridge parent chain.
  Finding: do not land the K-Z / SU(3) external-lift package as a bounded
  theorem or parent status promotion while the runner fails without optional
  CVXPY and the load-bearing `W_lift = 0.05` is not extracted from an
  explicit SU(3), beta=6 primary-source bracket; this is an open
  external-lift candidate, not retained authority.
  Disposition: `science-needed`.
  Detail:
  [`PR484_KZ_EXTERNAL_LIFT_REVIEW_2026-05-03.md`](../work_history/repo/review_feedback/PR484_KZ_EXTERNAL_LIFT_REVIEW_2026-05-03.md)
- Planck Target 2 / area-law carrier: the simple-fiber Widom class is now
  closed negatively; any positive `1/4` entropy carrier needs a physical
  multi-pocket/multi-interval law or a gapped horizon-sector primitive-boundary
  theorem
- memory lane: protocol- and geometry-stable observable remains open
- emergent-geometry growth: multi-size, multi-seed stability remains open
- `2026-05-20-d3-lower-bound-bridge-sign`
  Scope: PR #1603,
  `DIMENSION_SELECTION_NOTE.md`, and the attempted
  `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md`.
  Finding: the submitted analytic lower-bound bridge was not landed because
  its Green-function/force-sign argument does not consistently match the
  existing runner's phase-coupling observable, especially around the
  two-dimensional logarithmic case.
  Disposition: `science-needed`.
- `2026-05-20-single-clock-uniqueness-negative-gate`
  Scope: PR #1603 and
  `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`.
  Finding: the submitted no-spatial-reflection-positivity / no-second-clock
  uniqueness proof was not landed because it is a broad negative claim with
  unaudited dependencies and no no-go-discipline N1-N8 checklist.
  Disposition: `science-needed`.
- `2026-05-22-prr-framework-rule-approval-gate`
  Scope: PR #1658, pre-record reference state invariance, and the downstream
  Born-rule audit chain.
  Finding: LSP-projective was explicitly approved and ratified on 2026-05-22
  in `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening III"; the
  independent audit lane still owns all downstream verdicts. Do not ratify PRR
  as a load-bearing framework rule from review-loop alone. The submitted branch
  identified plausible conditional bridges and dispatch targets, but PRR remains
  a new framework-rule commitment rather than a derivation from Axiom 1 /
  Axiom 2, so it requires explicit user approval before any ratification or
  audit-dispatch sidecar can land.
  Disposition: `science-needed`.
- `2026-05-29-pr2203-so4-power-counting-marginal-anisotropy-gate`
  Scope: PR #2203,
  `EMERGENT_SO4_CONDITIONAL_ON_CONTINUUM_LIMIT_POWER_COUNTING_NARROW_THEOREM_NOTE_2026-05-29.md`,
  and its companion power-counting runner.
  Finding: the exact spatial `O_h` / cubic-harmonic power-counting checks are
  useful, but the submitted theorem over-promotes them to a full SO(4)
  all-`n`-point continuum implication; on a `Z^3 x Z_tau` surface with only
  spatial cubic symmetry, a marginal time-vs-space kinetic anisotropy is not
  excluded by the runner. Salvage should either add an explicit retained or
  admitted Euclidean kinetic-normalization / 4D-hypercubic premise, or narrow
  the theorem to spatial cubic artifact power counting.
  Disposition: `science-needed`.
- `2026-05-29-pr2207-eta-holonomy-braid-invariant-gap`
  Scope: PR #2207,
  `ETA_PHASE_HOLONOMY_AREA_FLUX_NOT_BRAID_INVARIANT_NARROW_NO_GO_NOTE_2026-05-29.md`,
  and its companion runner.
  Finding: the exact `eta`-phase spin-diagonalization and `Z_2` area-flux
  computation are valuable, but the no-go conclusion is not yet supported:
  the runner asserts rather than proves that the compared detour swaps are the
  same element of `B_2(Z^3)` and that a one-token plaquette loop is
  null-homotopic in `UD_2(Z^3)`. A graph treated as a 1-complex does not
  automatically include geometric plaquette faces. Salvage should either
  compute/establish the relevant `UD_2` homotopy or land only the narrower
  base-connection area-flux theorem.
  Disposition: `science-needed`.
## Intake Format

Record each new finding as one bullet:

- `ID`
  short label; date if needed
- `Scope`
  affected lane, note, script, or package surface
- `Finding`
  one-sentence statement of the issue
- `Disposition`
  one of: `triage`, `fix on main`, `support-only demotion`, `science-needed`,
  `reject`
- `Detail`
  optional link to a longer packet in work history

## Queue History

- `2026-07-10-wilson-plane-representation-ring-route`
  Resolved on `main`: the repaired finite-volume `SU(N)` note proves
  nonnegative Wilson character coefficients directly from tensor powers of
  `F direct-sum Fbar`, and the companion adds exact normalization, `SU(3)`
  fusion, positive-kernel, and wrong-sign gates. The direct runner reports
  `25 PASS / 0 FAIL`, with a matching current cache SHA.

- `2026-07-10-record-p1-dependency-audit-drift`
  Resolved as a frozen-history contract: the 91-row June 4 classification is
  no longer equated to the evolving live graph, and the verifier observes the
  current tracked sharded ledger separately while preserving the no-rewrite,
  no-alias, no-premise-insertion, and no-status-edit disciplines. The direct
  runner passes on the clean current checkout and its cache is SHA-pinned.

- `2026-07-16-uv-gauge-yukawa-direct-consumer-scope-drift`
  Repaired all seven unaudited direct consumers. The UV radius note now
  consumes only the exact `C_pert = 1/(2 N_c)` versus public
  `C_strong = 1/N_c^2` comparison and leaves expansion selection/convergence
  open. The six YT consumers no longer use the bridge for canonical
  `alpha_LM`, historical `delta_PT`/NLO, source-action, or plaquette authority;
  conditional canonical arithmetic is linked to its currently unaudited bounded
  source, and unsupported selector/transport inputs are explicit open
  conditions. Changed source rows remain subject to independent re-audit.

- `2026-07-16-su3-wigner-downstream-status-prose-drift`
  Resolved the two named SU(3) Wigner consumer notes by removing every
  source-authored audit-status snapshot, directing readers to pipeline-derived
  current status, and adding explicit no-inheritance boundaries. The consumer
  formulas remain unchanged and do not consume Block 1's corrected `H` values
  or channel ordering; Block 1's cubic-Casimir label/equivariance repair
  remains subject to independent re-audit. The paired runners now fail on any
  return of literal status pins or removal of those boundaries, and their
  canonical caches were refreshed.

- `2026-06-12-pr3511-theta-retirement-gate`
  PR #3511 preserved a review of the former admission-era theta treatment.
  The supplied-premise class was later removed; the scientific gaps are now
  ordinary derivation obligations. Historical grade language in that review
  does not describe current pipeline status.

- `2026-04-18`
  repo-wide review/backlog cleanup completed; the old operational review
  packets and planning backlogs were moved out of the front-door `docs/`
  surface into [`docs/work_history/repo/review_feedback/`](../work_history/repo/review_feedback/README.md)
  and [`docs/work_history/repo/backlog/`](../work_history/repo/backlog/README.md)
