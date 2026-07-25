# Route Portfolio — audit-unlock-toe-20260724

Artifact-type routes (kept separate from mathematical approach families, which
live in APPROACH_REGISTRY.md).

## Lane A routes (audit-unlock)

- **A-R1 (active):** codex audit-loop coordinator drain on clean clones —
  routine audit commits push directly to main under the audit-loop lane
  authorization; one orchestrator per clone (clone-wide lock).
- **A-R2 (available):** additional parallel worker on a second clean clone with
  a distinct AUDIT_WORKER_ID, if machine headroom permits (memory_pressure
  free % checked per dispatch; keep repo-wide codex load <= 8-10 processes).
- **A-R3 (available):** fix-class source repairs for rows the drain surfaces as
  repairable (audited_conditional / demotion-vocabulary repairs), landed as
  ordinary science-branch PRs — never touching docs/audit/data/.

## Lane B routes (TOE-completion science)

- **B-R1 (active):** KCPT chain continuation — bounded_theorem triples
  (note + runner + cache) on the L=4 staggered Dirac complex under
  H = <G_amb, S_eps>, each citing only landed chain notes. Unit 20 in review.
- **B-R2 (candidate, Unit 21+):** obligation-facing structural units — what the
  landed algebra registers about occupancy (obligation #1) or determinant
  reality across sectors (obligation #3). Requires Fable algebra-before-spec.
- **B-R3 (candidate):** repair-class units from the active review queue
  (OPPORTUNITY_QUEUE item 4).

## Execution mechanism (all lane-B routes)

Fable: recon, derivation sketch, spec, line-by-line review, panel synthesis,
landing decision. Opus 5 (Agent tool, max effort): implementation per spec,
anti-fabrication clauses verbatim. Workflow adversarial-verification pass
(3 lenses: fabrication-hunt, algebra-re-derive, framing-audit) before every
landing. codex: review-loop on opened PRs, audit-loop on landed rows — codex
lanes only, never driven by this session's judgment.
