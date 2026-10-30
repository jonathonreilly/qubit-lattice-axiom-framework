# Agent entry point

1. **Rules:** read `docs/ai_methodology/SCIENCE_WORKFLOW.md`. It is the single
   operating map: evidence rules, current owner settings, stages, where
   material belongs and, in section 10, how sessions on any provider work as a
   lab.
2. **Procedure:** pick the skill for the job from section 6 of that file
   (`docs/ai_methodology/skills/<name>/SKILL.md`). `.claude/commands/` are thin
   adapters to the same skills.
3. **Planning state:** dispatcher instructions, the TOE scorecard and campaign
   status live on the orphan `ai/execution` branch, which never merges into
   `main`. Read without touching your working tree:

   ```bash
   git fetch origin ai/execution --quiet
   git show origin/ai/execution:AGENTS.md
   ```

   Planning supplies no scientific status. `origin/main` is the only authority
   for science content and audit status. Do not check `ai/execution` files out
   into a `main` working tree.

Original mathematics is welcome within the user's task. It does not by itself
add a physical axiom or establish a physical identification.

Historical automation protocols are in `docs/work_history/automation/` and must
not be executed.
