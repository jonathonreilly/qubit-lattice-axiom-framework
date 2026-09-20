This is an active part of the physics-loop skill. Read it when the
entry point routes the current operation here, from the same source
revision. Repository paths in code remain relative to the repository.

## Campaign Continuation Policy

Long unattended runs must continue through local stops.

Nonfatal events that must **not** end a campaign while runtime remains:

- a route produces a no-go, exact negative boundary, demotion, or blocker;
- review-loop returns `demote` or `block` for the current artifact;
- retained-proposal certification fails;
- a PR is dirty, stacked, or cannot be opened because of GitHub/network auth;
- a lane reaches a human-judgment premise;
- optional literature access is unavailable for one route;
- the repo automation lock is unavailable but a branch-local supervisor lock
  can still prevent duplicate work.

Required response to a nonfatal event:

1. demote or archive the current artifact honestly;
2. checkpoint `STATE.yaml`, `HANDOFF.md`, `REVIEW_HISTORY.md`,
   `TRACE_GATE.md`, and `CLAIM_STATUS_CERTIFICATE.md`;
3. preserve coherent work in the campaign branch; open a PR only when the
   selected delivery cadence and review-readiness conditions are met, or record
   an actionable delivery failure in `PR_BACKLOG.md`;
4. refresh `OPPORTUNITY_QUEUE.md`;
5. choose the next highest-ranked science opportunity by expected evidence
   value and continue.

Global stop is allowed only when:

- runtime or max cycles is exhausted;
- the worktree/repo changes externally in a way that makes safe continuation
  impossible;
- required core tooling for all viable routes is unavailable;
- a lock conflict means another active worker owns the same repo/task and no
  clean independent worktree can be created;
- the refreshed opportunity queue proves every viable target is blocked and no
  independent useful candidate remains;
- the documented corollary/value-gate exhaustion conditions in Stop Conditions
  are met after the required substantive search.

## Cluster-Cap Evaluator

The cluster-cap rule (see Stop Conditions) is JUDGMENT-BASED, not a hard
ceiling. After 2 PRs are open in a single parent-row family within one
campaign, the loop must run a cluster-cap evaluation BEFORE opening PR
#N for any N >= 3 in that cluster. Use a separate evaluator agent only
when the active tool policy and user authorization allow it; otherwise
the loop agent applies the same evaluator brief locally and records the
judgment in `HANDOFF.md` or `PR_BACKLOG.md`. The evaluator's verdict
gates only the PR opening — science work continues regardless.

### Evaluator brief

The evaluator is either a separate research agent, when available, or
the current loop agent running an isolated local pass with this brief:

> You are a cluster-cap evaluator for a physics-loop campaign. The
> campaign has already opened {N-1} PRs in the parent-row family
> `{family_pattern}`. The campaign now proposes opening PR #{N} for
> {block_summary}. Your job: decide if this proposed PR represents
> genuinely new content warranting audit-lane review, OR is corollary
> churn / review-burden inflation that should be backlogged.
>
> Read the proposed PR's deliverable note + paired runner output (if
> any). Apply the project's **content-integrity criteria**:
>
> 1. **New load-bearing premise.** Does the proposed PR introduce a
>    structural premise (theorem, derivation chain, no-go, named
>    obstruction, numerical artifact) NOT present in the prior {N-1}
>    PRs of this cluster?
> 2. **Distinct claim type.** Is the proposed PR a different *kind* of
>    artifact (positive theorem vs no-go vs exploration vs numerical
>    comparator) than the prior cluster PRs, or just another instance
>    of the same kind?
> 3. **Independent reviewability.** Can the audit lane review this PR
>    on its own merits, or does its content essentially restate what
>    a single combined PR for the cluster would already cover?
> 4. **Marginal review value.** Is the per-PR review effort justified
>    by the per-PR content delta, or would the audit lane be better
>    served by a single combined PR (or commits-only into a future
>    campaign)?
>
> Output a one-line verdict: `OPEN` (proposed PR is genuinely new and
> should be opened) or `BACKLOG` (content is real but should go to
> `PR_BACKLOG.md` for a future campaign or combined PR). Justify in
> ~200-400 words. Do NOT consider the audit verdict — only the PR
> opening decision. The evaluator does NOT decide audit outcomes.

### Default behavior

If the deliverable note, paired runner output, or local review context is
unavailable enough that the evaluator cannot make the judgment, default
to `BACKLOG` for PRs N >= 3 — fail-closed on the cap rather than
fail-open. The science work still continues; the commit lands on the
loop branch and is recorded in `PR_BACKLOG.md`.

### Anti-patterns (evaluator should reject)

- "Apply theorem X (just landed in PR N-1) to label Y" — relabeling
- "Same matrix structure, different physical interpretation" —
  reframing not deriving
- "Sympy-exact verification of the existing primary runner's identities"
  when the runner already exists
- "Pattern A narrow rescope of the algebraic core" — creates audit
  row but no closer derivation

### Patterns the evaluator should approve

- A no-go theorem that retires a route the prior PRs assumed
- A numerical artifact (NEW computation) under a different action /
  geometry / coupling
- A structural finding orthogonal to the prior cluster PRs (e.g.
  gauge-group exploration when prior PRs were action-form)
- An exact closed-form derivation when prior PRs derived only inputs

### When the evaluator is moot

If the campaign has runtime and queue-budget but the evaluator says
`BACKLOG` for every remaining queued candidate, that is a stop signal
(corollary exhaustion). Update `HANDOFF.md` accordingly.

## Long-Running Execution

For unattended runs, follow
[`references/long-running-execution.md`](long-running-execution.md).
In short:

- ask for runtime if absent;
- avoid mid-run questions;
- checkpoint enough state that another agent can resume;
- refresh the lock before it expires;
- continue to the next ranked opportunity when one lane blocks and runtime
  remains;
- stop cleanly only when runtime, max cycles, global queue exhaustion, or a
  global safety/tooling condition dictates;
- push only dedicated science campaign/block branches;
- open or prepare PRs at review-ready milestones, or at review-ready block
  closures when `--delivery block` was requested;
- never push science work to `main`.

## Stop Conditions

Stop and write a clear `HANDOFF.md` when:

- runtime or max cycles is reached;
- no route in the refreshed opportunity queue or active approach-family
  registry passes the dramatic-step gate **after** the Deep Work Rules and any
  applicable theorem-strength gap tests have been satisfied for the target;
- **corollary exhaustion**: every remaining ranked opportunity would produce
  only a one-step algebraic corollary of an already-landed campaign cycle
  with no new load-bearing premise. This is a real stop condition, not a
  reason to fill the cycle cap with thin restatements. The campaign's
  substantive ground is covered when the highest-value remaining moves are
  "apply cycle N's exact-support theorem to a different label";
- **value-gate exhaustion**: every remaining ranked opportunity would fail
  V1-V5 of the Promotion Value Gate (DISCOVERY.md, workflow step 8). If the only PRs the
  campaign can produce are textbook re-verifications, near-tautological
  rescopes, or one-step variants of landed cycles, the campaign must stop
  rather than fill the cycle cap;
- **(no volume cap)**: there is NO fixed PR-count cap per campaign or per
  day (owner decision 2026-06-11; the former 5-PRs-per-24-hour volume cap
  is removed). PR volume is gated by CONTENT, not by a counter: every PR
  must pass the V1-V5 Promotion Value Gate, negative claims must pass
  N1-N8, and the judgment-based cluster-cap evaluator applies from the
  3rd PR in a parent-row family. A campaign stops on quality-gate
  exhaustion (the two conditions above), never on a PR count;
- **cluster cap evaluator triggered**: at the 3rd and every subsequent
  PR in a single parent-row family (`koide_*`, `dm_neutrino_*`,
  `gauge_vacuum_plaquette_*`, `ckm_*_2026-04-25`, `bridge_gap_*`, etc.)
  per campaign, BEFORE opening that PR, the loop must run the
  cluster-cap evaluation described above to decide whether the proposed
  PR is genuinely new content warranting audit-lane review, OR is
  corollary churn / review-burden inflation that should be backlogged.
  Use a separate evaluator agent only when the active tool policy and
  user authorization allow it; otherwise run the same evaluator brief
  locally. The cap is JUDGMENT-BASED, not a hard 2-PR ceiling. The
  evaluator's verdict gates only the PR opening — science work
  continues either way (commits-only into the loop branch, recorded in
  `PR_BACKLOG.md` if the evaluator says "backlog"). Past N=2 in a
  cluster the burden is on the proposed PR to demonstrate non-churn
  content, not on the cap to be lifted;
- the worktree changes externally in a way that affects the route;
- the requested target status is honestly achieved and the user did not ask for
  a continuing campaign;
- required core tooling for every viable queued route is unavailable.

Do not stop solely because review-loop finds a blocker, retained certification
fails, PR creation fails, or one lane needs human science judgment. Demote or
backlog that block and pivot.

When stopping for corollary exhaustion, name in `HANDOFF.md` the highest-blast-
radius unattempted hard residual so the next campaign can resume on fresh
ground rather than re-mining the already-covered surface.
