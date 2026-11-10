# Agent entry point

`origin/main` is the authority for rules, science and standing. A local
checkout may be behind it: `python3 scripts/lab_ops.py doctor` says whether
this one's rules are current, and `git show origin/main:<path>` reads the
current ones.

1. **Rules.** `docs/ai_methodology/RULES.md`. Read it once per task. It is short
   on purpose and everything else defers to it.
2. **Settings.** `docs/ai_methodology/SETTINGS.md`: the owner's current choices
   (cadence, method defaults, audit trigger, models by role). No other rule or
   procedure prescribes a model.
3. **Procedure.** Pick one from `docs/ai_methodology/PROCEDURES.md` and read
   that one.
4. **Foundation.** The axioms are `docs/MINIMAL_AXIOMS_2026-06-29.md`. Quote
   them from `origin/main`, never from a summary, a skill or memory.
   `docs/ai_methodology/FRAMEWORK_PRIMER.md` says how to read them.
5. **State.** A target's state is its folder on its pushed branch;
   `python3 scripts/lab_ops.py status <folder>` summarises it. Planning notes
   and the list of targets are on the orphan `ai/execution` branch
   (`git show origin/ai/execution:CAMPAIGN_STATUS.md`). They are an as-of aid
   and grant nothing.

`docs/work_history/`, `archive/` and dated campaign packs are history. Read
them for recovery; never execute them as procedure.

This repository is public by design. Everything pushed is public.
