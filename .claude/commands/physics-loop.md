# /physics-loop — Long-Running Physics Loop

Run the repo-native physics loop skill from:

`docs/ai_methodology/skills/physics-loop/SKILL.md`

## Invocation

```text
/physics-loop "<science goal>" [--mode plan|run|resume|status|campaign] [--runtime DURATION] [--target STATUS] [--literature] [--max-cycles N] [--deep-block DURATION] [--no-pr]
```

Examples:

```text
/physics-loop "retire the DM/leptogenesis 16v support import" --mode plan
/physics-loop "close the Koide Q bridge or prove the next no-go" --mode run --literature --runtime 12h
/physics-loop "work the best open science opportunities" --mode campaign --runtime 12h --target best-honest-status
/physics-loop --mode resume --loop dm-leptogenesis-16v
```

Infer `--mode campaign` for overnight, unattended, long-running, or 12-hour
execution requests even when the user says only `run`.

## Required Behavior

1. Read the skill file above before acting.
2. If execution is requested and `--runtime` is absent, ask the user how long
   to run unattended before launching work.
3. Create or update a durable loop pack under
   `.claude/science/physics-loops/<slug>/`. Existing
   `.claude/science/frontier-workstreams/<slug>/` packs may be read as legacy
   resume surfaces.
4. Ground in current repo authority surfaces, retained work, no-go history,
   atlas/tool surfaces, approved primitive registry entries, and relevant
   publication tables before route selection.
5. For science execution, fetch `origin`, create clean dedicated science block
   branches from `origin/main`, commit coherent science artifacts there, and
   push those branches to `origin`.
6. Build an assumption/import ledger before new derivation work. Read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and enumerate
   approved primitives from `docs/audit/data/axiom_premise_nodes.json` before
   naming imports, walls, or bounded-status sources.
7. Generate and score a route portfolio; execute only a route that can move
   claim state, retire an import, close a blocker, prove a no-go, create a
   decisive artifact, or make a recorded first-principles stretch attempt on a
   named hard residual.
8. Apply the skill's pre-PR gates in writing: the V1-V5 Promotion Value Gate
   for any retained-positive proposal, and the N1-N8 No-Go Discipline Gate
   (`no-go-discipline` skill) for any negative claim. Record both in the
   block's certificate/queue files and PR body as the skill specifies.
9. Add a trace gate for each serious route in `TRACE_GATE.md`: name the exact
   claim/blocker/import the artifact is meant to move, or classify it as
   `frontier_discovery` when it is pure science with no known downstream
   blocker yet. Frontier discovery is valid output, but it must not be framed
   as closing, promoting, or retiring an existing lane.
10. For unattended runs longer than one major cycle, build
   `OPPORTUNITY_QUEUE.md` and keep selecting the next ranked retained-positive
   opportunity until runtime/max cycles expires or the refreshed queue is
   globally exhausted.
11. Write `CLAIM_STATUS_CERTIFICATE.md` for each science block. Do not use bare
   `retained` / `promoted` status language in branch-local source notes. Use
   `proposed_retained` / `proposed_promoted` only when the certificate supports
   a theorem-grade proposal and marks the later independent audit requirement;
   otherwise demote branch-local, conditional, same-surface,
   admitted-observation, or Axiom* consequences to the narrowest honest status.
12. Checkpoint `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md` throughout
   unattended work.
13. After two audit/no-go/blocker cycles in a row, run a stretch attempt before
   declaring a route blocked. If stuck, fan out 3-5 orthogonal premises before
   declaring global queue exhaustion.
14. Run `review-loop` after each major artifact unless explicitly disabled.
   Treat review demotions/blockers as block-level demotion/pivot events, not
   campaign stops.
15. At each coherent science-block closure, open or prepare one review PR
    unless `--no-pr` was supplied; do not wait until the 12-hour campaign ends
    if the block is already coherent.
16. Keep science runs science-only. Record proposed repo weaving in
   `HANDOFF.md`; do not update repo-wide authority surfaces until later review
   and backpressure integration.

## Campaign Rule

If the user asks for a 12-hour unattended run, do not exit early just because a
lane hits a no-go, support-only boundary, human-judgment blocker, failed
retained-proposal certificate, dirty PR, or missing GitHub auth. Checkpoint/demote or
backlog the current block, refresh the opportunity queue, and continue on the
next science target. Stop early only for runtime/max-cycle exhaustion, unsafe
worktree/lock conflict, or documented global queue exhaustion.

## Non-Negotiables

- No hidden fitted values, selectors, observations, normalizations, or
  literature imports.
- Approved primitives are not hidden imports. The registered
  `scale_reference_primitive` grants the Planck scale reference as units
  conversion only and does not bound a row by itself. The registered
  `kinetic_isotropy_primitive` grants only structural OS0 kinetic-form isotropy
  `c_t = c_s` and does not supply dynamics, a Lorentz-closure theorem, scale,
  spacing-ratio theorem, selector, or empirical content. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data). Proposed primitives not
  in `docs/audit/data/axiom_premise_nodes.json` remain unapproved.
- No Nature-grade or retained-grade proposal language without decisive artifact
  support, a passing retained-proposal certificate, review-loop backpressure,
  and explicit independent-audit handoff.
- Do not re-open prior no-go routes unless a new premise is named.
- Do not run low-value churn: more prose, nearby scripts, or repeated wording
  passes are not major loop progress.
- Do not write bare `retained` / `promoted`, `retained branch-local`, or
  hypothetical/Axiom* consequences as retained on the actual current surface.
  `proposed_retained` / `proposed_promoted` are allowed only as audit-ready
  author proposals, never as audit-ratified retained status.
- Push only dedicated science block branches. Do not push science work to
  `main`, merge PRs, or open PRs without enough review surface for
  `review-loop`.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
