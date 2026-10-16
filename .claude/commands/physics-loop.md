# /physics-loop — Long-Running Physics Loop

Adapter for `docs/ai_methodology/skills/physics-loop/SKILL.md`. Read the skill
and the references its routing table requires; this file adds no policy.

## Invocation

```text
/physics-loop "<science goal>" [--mode plan|run|resume|status|campaign] [--runtime DURATION] [--delivery milestone|block] [--target STATUS] [--literature] [--max-cycles N] [--deep-block DURATION] [--no-pr]
```

Examples:

```text
/physics-loop "retire the DM/leptogenesis 16v support import" --mode plan
/physics-loop "close the Koide Q bridge or prove the next no-go" --mode run --literature --runtime 12h
/physics-loop "work the best open science opportunities" --mode campaign --runtime 24h
/physics-loop --mode resume --loop dm-leptogenesis-16v
```

## Checklist (details in the skill references)

1. If execution is wanted and `--runtime` is missing, ask for it.
2. Fetch `origin`; work on a dedicated campaign branch cut from `origin/main`
   (or from the base the user names). Never push science to `main` or merge.
3. Keep the loop pack in `.claude/science/physics-loops/<slug>/`: `STATE.yaml`,
   `HANDOFF.md`, `TRACE_GATE.md`, `OPPORTUNITY_QUEUE.md`, per-block
   `CLAIM_STATUS_CERTIFICATE.md`, and `APPROACH_REGISTRY.md` for theorem
   targets (`references/DELIVERY.md`).
4. Build the assumption/import ledger from
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and
   `docs/audit/data/axiom_premise_nodes.json` before naming imports or walls
   (`references/CLAIM_STATUS.md`).
5. Score a route portfolio and run only routes that can move claim state
   (`references/DISCOVERY.md`). Apply V1-V5 to positive proposals and N1-N8 to
   negative claims (`no-go-discipline`).
6. Never write bare `retained`/`promoted`; `proposed_retained` only with a
   passing certificate and an explicit independent-audit handoff.
7. Checkpoint the pack throughout. On a route stop, demote/backlog, refresh the
   opportunity queue and continue (`references/CAMPAIGN.md`).
8. When the delivery flags permit, open a regular PR at a coherent, review-ready
   milestone or budget-end handoff, then hand it to a fresh `/review-loop`. Honor
   `--no-pr`; do not force incomplete work into a PR. Author checks never grant
   review PASS.
9. Use `docs/ai_methodology/skills/workhorse/SKILL.md` for worker dispatch and
   independent checks.
