# AI Methodology Note — Cl(3)/Z^3 Framework

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Date:** 2026-04-25  
**Status:** active methodology-capture lane on `main`; curated front-door note,
not the final methodology paper  
**Scope:** how AI systems were used to generate, audit, demote, reject, and
land the framework's science

This note does not add or promote any physics claim. Its job is to document the
method by which claims were produced and controlled.

## 1. Reading Rule

This lane is separate from the physics claim boundary.

- For the current scientific package, use the publication surfaces in
  [`docs/publication/ci3_z3/`](./publication/ci3_z3/README.md).
- For the AI/process methodology, use this note and the methodology index in
  [`docs/ai_methodology/README.md`](./ai_methodology/README.md).

The methodology lane is about:

- how candidate theorems were generated;
- how executable runner harnesses were used to separate algebra from rhetoric;
- how bounded/retained/open status was kept explicit;
- how Claude and Codex were used in partially adversarial roles;
- how branch review, selective landing, and repo hygiene were enforced.

It is not itself a theorem note.

## 2. Snapshot Of The Project Surface

As of the 2026-04-25 capture on current `main`:

- `origin/main` commits: `2666`
- initial commit: `2026-03-13` (`7a5f1dca`)
- current `origin/main` tip at capture: `0a116fa1`
- markdown documents under `docs/`: `1467`
- Python scripts under `scripts/`: `2087`
- `frontier_*.py` runners: `1030`
- visible remote `claude/*` and `codex/*` branches: `89`

These numbers matter because the methodological claim is not "AI helped write
some text." The methodological claim is that a very large theorem/search/review
surface was managed through explicit executable and editorial controls.

## 3. Division Of Labor

### 3.1 Human role

The human author retained responsibility for:

- the founding choice of `Cl(3)` on `Z^3` as the framework surface;
- the physics targets worth pursuing;
- the decision to promote, demote, or reject a claim;
- the final claim boundary on `main`;
- the interpretation of results and the manuscript posture.

### 3.2 Claude role

Claude was used heavily on the forward-production side:

- theorem-note drafting;
- derivation search;
- obstruction and no-go production;
- runner generation;
- branch-local science packaging;
- high-volume exploratory work across parallel worktrees.

### 3.3 Codex role

Codex was used heavily on the adversarial and integration side:

- branch review;
- overclaim detection;
- theorem-premise audits;
- selective subset landing onto `main`;
- claim-surface weaving;
- repo-hygiene and review-note enforcement.

The two tools were not treated as interchangeable. In practice they formed a
partially adversarial pair: one often proposed or extended science, while the
other pressured the claim boundary and forced narrower honest landings.

## 4. Core Method

The working method that emerged in this repository has six recurring parts.

### 4.1 Candidate work happens off `main`

New science is usually developed on a dedicated branch/worktree first. That
keeps exploratory work, failed routes, and overclaimed drafts off the live
package surface.

Relevant repo-side examples:

- [`docs/CLAUDE_BRANCH_RETAINABILITY_NOTE.md`](./CLAUDE_BRANCH_RETAINABILITY_NOTE.md)
- [`docs/UNPROMOTED_BRANCH_RETAINABILITY_AUDIT_NOTE.md`](./UNPROMOTED_BRANCH_RETAINABILITY_AUDIT_NOTE.md)

### 4.2 Notes and runners are paired

A claim is not just prose. The normal unit of work is:

- theorem/support/no-go note;
- paired `frontier_*.py` runner;
- replayable PASS/FAIL output;
- sometimes a retained log.

This pairing is the primary defense against AI-generated rhetorical drift.

### 4.3 Claim status is explicit

The repo uses explicit status distinctions instead of a single bucket called
"proved":

- `retained`
- `bounded`
- `support`
- `conditional`
- `open`
- `no-go`
- `reject`

This is one of the main mechanisms used to stop AI systems from silently
upgrading a suggestive route into a theorem.

The package-wide negative boundary is maintained explicitly in:

- [`docs/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md`](./publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)

### 4.4 No-go production is first-class

The methodology does not only reward positive closes. It also keeps and cites:

- route obstructions;
- failed closure attempts;
- support-only demotions;
- theorem-level no-go notes;
- review notes that explain why a branch is not yet landable.

This matters because AI systems are very good at producing plausible positive
stories. The repo's no-go surface is one of the main controls against that bias.

### 4.5 Review is not cosmetic

The repo has an explicit review workflow for deciding what belongs on `main`:

- [`docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`](./repo/REVIEW_FEEDBACK_WORKFLOW.md)

The narrowest honest fix is the rule:

- wording and packaging problems get fixed on `main`;
- real missing theorem steps do not get patched with rhetoric;
- unsupported science stays off `main` or gets demoted.

### 4.6 Selective landing is normal

A branch is not all-or-nothing. Many branches are valuable but only in part.
The standard `main` move is often:

1. reject the branch as submitted;
2. salvage the honest subset;
3. land that subset at the correct status;
4. keep the rest off `main`.

This selective-landing discipline is central to how AI-produced material was
made usable without allowing every high-volume branch to rewrite the live claim
boundary.

## 5. Repo Hygiene As Methodology

Repo hygiene is not auxiliary here. It is part of the method.

Important surfaces include:

- [`docs/CANONICAL_HARNESS_INDEX.md`](./CANONICAL_HARNESS_INDEX.md)
- [`docs/repo/ACTIVE_REVIEW_QUEUE.md`](./repo/ACTIVE_REVIEW_QUEUE.md)
- [`AUTOPILOT_PROTOCOL.md`](../AUTOPILOT_PROTOCOL.md)
- [`AUTOPILOT_JANITOR_PROTOCOL.md`](../AUTOPILOT_JANITOR_PROTOCOL.md)
- [`AUTOPILOT_SUMMARY_PROTOCOL.md`](../AUTOPILOT_SUMMARY_PROTOCOL.md)

These files encode a reproducibility discipline:

- branch work is isolated;
- locks prevent concurrent corruption;
- handoff state is explicit;
- review queues are canonicalized;
- stale or superseded material is pushed into `docs/work_history/` instead of
  polluting the front door.

In other words, repo hygiene is part of the check on the science, not just an
engineering nicety.

### 5a. Vocabulary hygiene at agent pacing

At repo scale (this repo currently carries ~2600 markdown files, almost
all AI-authored, with parallel agents working continuously), one
specific kind of hygiene fails when handled by discipline alone:
vocabulary. Agents drift, emergent terminology compounds, and per-PR
coordination becomes a synchronous bottleneck the autopilot will not
respect. The empirical anchor in this repo: a single PR (#1262, on
2026-05-16) introduced an ad-hoc filename suffix
(`_HOSTILE_AUDIT_FINDINGS_NOTE_`) and a within-note F-letter labelling
scheme; in the next 24 hours, 83 follow-up notes adopted the same
pattern. Discipline-based control (the existing "no new vocab" rule in
memory) caught the wave only on retrospective review.

The methodological pattern shipped in response is **mechanism-based
vocabulary control**:

1. **One machine-readable canonical source.**
   `docs/repo/controlled_vocabulary.yaml` (created by the companion
   cleanup PR) is the single edit surface for all process vocabulary.
   The human-readable docs
   ([`CONTROLLED_VOCABULARY.md`](./repo/CONTROLLED_VOCABULARY.md),
   [`KEY_TERMINOLOGY.md`](./KEY_TERMINOLOGY.md)) are regenerated from
   the YAML; manual edits to the rendered docs are not permitted.
   Rendered drift is impossible by construction.

2. **Auto-correct integrated into the substantive loops.**
   `scripts/vocab_lint.py --fix` is a mechanical pre-commit step in
   audit-loop, review-loop, and physics-loop (see their respective
   `SKILL.md` files). Routine drift (legacy aliases, forbidden
   filename suffixes, deprecated wording, F-letter codes) is rewritten
   **automatically; each rewrite is recorded in `prose_corrections`
   on the related audit row** (automatic, not silent — the trail is
   auditable). This shifts vocabulary compliance from agent discipline
   (fallible) to loop mechanism (always-on).

3. **Physics verdicts separated from prose verdicts.** Audit ledger
   rows gain a `prose_status` field independent of `audit_status`. A
   clean derivation with vocabulary drift lands as
   `(audit_status: audited_clean, prose_status: auto_corrected)`. A
   non-clean physics verdict is never set by vocabulary drift alone; a
   new-vocabulary requirement is never blocked by a physics non-clean
   verdict. The two concerns are recorded by the same audit cycle but
   reviewed by different mechanisms.

4. **Vocabulary disjoint from physics.** Framework primitives
   (`Cl(3)`, `Z³`, `A_min`, `Axiom 1`, `Axiom 2`, `g_bare`, `u_0`,
   `M_Pl`, etc.) are *not* vocabulary terms. They live in
   [`MINIMAL_AXIOMS_2026-05-03.md`](./MINIMAL_AXIOMS_2026-05-03.md)
   and per-claim notes only. The vocabulary system governs
   process labels (status, audit fields, repair classes, evidence
   terms, prose voice) — never the physics itself. Conflating the two
   creates rot in both directions.

5. **Agent pacing preserved.** Routine vocabulary rewrites do not
   require PRs; the lint applies them inline. Only *genuinely new
   terms* enter a periodic vocab-extension review queue (recorded as
   `prose_status: needs_human_vocab_decision`), batch-resolved with
   one PR against the canonical YAML. The synchronous-bottleneck
   failure mode the 84-note wave exposed is structurally removed.

The vocabulary **conforms to established standards where the domain
matches**, with explicitly-tagged AI-physics extensions for the
generation failure modes the standards do not cover. The schema is
engineered for conformance, not nodding-toward-standards:

- **Lifecycle** uses the W3C recommendation-track values directly
  (`unaudited` = Working Draft, `audit_in_progress` = Candidate
  Recommendation, `audited_clean` = Recommendation,
  `audited_retired` = Retired with cause). AI-specific failure modes
  (renaming / decoration / numerical-match) are recorded in a
  separate `failure_mode` field rather than inflating the lifecycle
  enum.
- **Grade** uses GRADE's two-axis structure (recommendation strength
  × evidence certainty), implemented as `closure_status` ×
  `chain_certainty`. The conventional publication-facing labels
  (`retained`, `retained_bounded`, …) become derived names for
  specific cells in the grid, not the source of truth.
- **Defect classification** uses IEEE 1044-2009 anomaly-classification
  axes (`defect_type` × `defect_class` × `severity`); our seven
  historical repair classes map into them. `compute_required` is
  correctly recorded as a `defect_class: problem` (not a defect;
  deferred verification).
- **Independence tiers** are partially novel: the human-reviewer
  tiers (`strong`, `external`) match standard peer review;
  the model-family tiers (`weak`, `fresh_context`, `cross_family`)
  are AI-physics extensions explicitly tagged in the YAML.

Every term that is not standards-conformant carries
`ai_extension: true` and an `ai_extension_rationale` field. The
transferable parts of the mechanism (the conformant cells) transfer
unchanged; the AI-physics extensions transfer only to repos facing
the same generation-failure modes.

The full design is in
[`docs/repo/VOCABULARY_HYGIENE_DESIGN.md`](./repo/VOCABULARY_HYGIENE_DESIGN.md);
the canonical YAML and the lint script land in the companion cleanup
PR. This mechanism is offered as a transferable pattern, but with
explicit preconditions — it works only in repos that already have:

- a *structured claim ledger* (audit-ledger JSON or equivalent) where
  process labels are first-class fields;
- *controlled / generated docs* (a renderer pattern so the
  human-readable surface is a product, not a source);
- *CI gates* that fail builds when the rendered surface drifts from
  the canonical source-of-truth;
- *agents that respect pre-commit hooks* and run the lint
  automatically in their loops;
- a *central source-of-truth* for the vocabulary itself (YAML, JSON
  Schema, or equivalent), with explicit `schema_version` and
  migration scripts.

Repos without those preconditions can still adopt the *principle*
(vocab disjoint from physics, auto-correct over discipline,
physics-versus-prose separation), but the mechanical implementation
will need to be redesigned around whatever ledger / docs / CI surface
they actually have. Without those preconditions, the discipline-based
fallback is the realistic ceiling, and the failure modes we saw
(emergent suffixes, F-letter labelling waves, alias rot) will recur.

## 6. Current Evidence Surface

The curated methodology lane on `main` now consists of:

- this front-door note;
- a methodology index:
  [`docs/ai_methodology/README.md`](./ai_methodology/README.md);
- a canonical per-paper disclosure paragraph:
  [`docs/ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md`](./ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md);
- a package-level accountability note:
  `docs/ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*);
- a raw methodology annex:
  [`docs/ai_methodology/raw/README.md`](./ai_methodology/raw/README.md);
- a synthesized methodology surface:
  [`docs/ai_methodology/METHODOLOGY_SYNTHESIS_2026-04-25.md`](./ai_methodology/METHODOLOGY_SYNTHESIS_2026-04-25.md);
- a case-study packet:
  [`docs/ai_methodology/METHODOLOGY_CASE_STUDIES_2026-04-25.md`](./ai_methodology/METHODOLOGY_CASE_STUDIES_2026-04-25.md);
- a first methods-paper draft:
  [`docs/ai_methodology/METHODOLOGY_PAPER_DRAFT_2026-04-25.md`](./ai_methodology/METHODOLOGY_PAPER_DRAFT_2026-04-25.md);
- an adversarial review of the synthesis packet:
  [`docs/ai_methodology/METHODOLOGY_SYNTHESIS_REVIEW_2026-04-25.md`](./ai_methodology/METHODOLOGY_SYNTHESIS_REVIEW_2026-04-25.md);
- a methodology-paper source packet:
  [`docs/ai_methodology/METHODOLOGY_PAPER_SOURCE_PACKET_2026-04-25.md`](./ai_methodology/METHODOLOGY_PAPER_SOURCE_PACKET_2026-04-25.md);
- a repo trajectory / governance evidence note:
  [`docs/ai_methodology/REPO_TRAJECTORY_AND_GOVERNANCE_EVIDENCE_2026-04-25.md`](./ai_methodology/REPO_TRAJECTORY_AND_GOVERNANCE_EVIDENCE_2026-04-25.md);
- a reusable LLM skill pack:
  [`docs/ai_methodology/LLM_SKILL_PACK_2026-04-25.md`](./ai_methodology/LLM_SKILL_PACK_2026-04-25.md).

The first four items are the current publishable disclosure surface. The
synthesis, derivation-centered case-study, draft, trajectory, and skill-pack
files are the working bridge toward a methods-and-case-studies paper.

The raw annex is now on `main` as evidence for the later methodology paper, but
it remains intentionally unpolished: machine-local paths, prompt excerpts,
branch/worktree inventories, review traces, and direct command outputs.

## 7. Raw Annex Boundary

This pass lands the raw-capture material that was previously branch-local,
plus a current Codex desktop raw packet from the `/Users/jonBridger` machine.

The raw annex includes:

- prompt/session dumps;
- full protocol captures;
- machine-local path inventories;
- Claude-side and Codex-side raw capture files;
- branch-review and repo-hygiene evidence;
- the current Codex desktop prompt/session, branch/worktree, and landing trace.

That material is useful precisely because it is raw. It should not be treated as
the final methodology paper or as polished disclosure language.

The following still need a dedicated grooming pass before publication use:

- deduplication across repeated prompt/session captures;
- normalized citations for machine-local paths;
- separation of representative examples from exhaustive inventories;
- selection of case studies from the raw review and selective-landing history.

## 8. Next Capture Targets

The next methodology pass should groom and extend the raw annex:

1. Full Codex prompt/session extraction beyond the representative current pass.
2. Review-note corpus expansion (`review.md` on science branches).
3. Selective-landing case studies.
4. Repo-hygiene and claim-surface correction examples.
5. Cross-tool disagreement/reconciliation events where one system caught an
   overclaim or premise gap introduced by the other.

This pass also adds the reusable-method layer requested for the methodology
lane: a full synthesis from raw evidence, case studies, a first paper draft,
and LLM skill specifications for lane building, adversarial claim review,
reviewer-backpressure integration, and methodology-paper synthesis. Those
skills are repo-native instructions that another LLM agent can reuse or adapt.

The remaining grooming work is now editorial rather than structural: choose
final case studies, sanitize representative excerpts, and turn the first draft
into submission-quality prose.

## 9. Bottom Line

The central methodological fact of this repository is not just that AI was
used. It is that AI-assisted theorem production was embedded inside an explicit
control structure:

- executable runners;
- bounded/retained/open labeling;
- no-go preservation;
- adversarial cross-tool review;
- selective landing;
- repo-hygiene and historical archiving.

That control structure is what made the resulting scientific package auditable.
