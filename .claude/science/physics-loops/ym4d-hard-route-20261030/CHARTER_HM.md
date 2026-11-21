# Push charter: hard-core, attempt with the public map

**Your file:** `parts/hard-core--mapped.md` in the target folder `.claude/science/physics-loops/ym4d-hard-route-20261030/`. Read `GOAL.md` there first.

**Target.** The same as the independent attempt: for SU(2) Wilson lattice gauge theory on a periodic four-torus, a hard-constraint block RG with all-scale UV stability delivering the interface UV-EXT, small and large fields included.

**What differs.** You may read the public Sussman-Alpoge repository, https://github.com/ethanwsussman/Yang--Mills-LLM-experiment , pinned at commit `c854ad8b3a42` or the commit you record. It is unvetted LLM-written text and a map, not a proof. Its own assembly chapter says none of its clauses is fully proved. Read it through the GitHub API or raw files; it is very large, so grep and read excerpts. Contact nobody connected to it. Credit it by name for anything you take. Your file must say plainly that this line is not independent of it.

Do not read the sibling attempt `parts/hard-core--independent.md`.

**Method.**
1. In your first cycle, extract the map into your file, in your own words and briefly: the induction, where UV stability enters, which steps it marks as unproved, and which sentences of Balaban it uses as printed.
2. Then verify rather than admire. Choose the load-bearing step it is least sure of, on UV stability or large fields, and prove it, or show it is wrong in the actual model with the edit that fixes it.
3. Nothing from the account is load-bearing until proved in your file. Treat its claims as you would a stranger's draft.

**Also available.** Dimock's expositions (arXiv:1108.1335, 1212.5562, 1304.0705, 1410.2798, 1712.10029), Goswami (arXiv:2204.08252), BFKT part 4. In the existing program: `BALABAN_EXTRACT.md`, `SOFTHARD.md`, `CHARGE.md`, `RENEW.md`, `LIB1.md`.

## How this push runs

You own this file for the whole run. A driver resumes you repeatedly and only the driver ends the run, so build on your own context.

**Your file.** Keep one file, named above, and rewrite it as your understanding improves. It is not a log. Open it with this structure:

```text
lead: <provider>/<model>/<effort> <session id>
lease_until: <driver sets this>

## State of attack
Current formulation, order of constants, hardest remaining inequality, routes tried and why they failed, next action.

## Obligations
- gap: <descriptive name> -> <consumer>
- unchecked: <descriptive name> given <hypotheses> -> <consumer>
- implication: <descriptive name> given <hypotheses> -> <consumer>
- discharged: <descriptive name> -> <consumer>

## Requests
- <part or interface>: <what is asked and why>

## Text
Definitions, statements, proofs.
```

Update the state of attack at every stop, so that a fresh session could restart from the file alone.

**Honesty.** Never write plausible text in place of an argument, and never invent a constant. A step you recalled from memory but did not prove is a gap. A truthful gap is never penalized. Before each stop, attack your newest step as a hostile skeptic and record what you found. Say which steps you actually derived and which you only believe.

**What stopping means.** A conditional theorem with a new named lemma is a checkpoint, not an end. Go to the hardest remaining inequality by a route you have not tried. If it is false, build a counterexample in the actual model and propose the edit. Work the crux first. Leaf lemmas, such as random-walk bounds and Haar estimates, get a frozen statement and a named consumer, and you come back to them later.

**Literature.** Use any open source for method. Nothing from a paper is load-bearing until it is proved in your file, or in `library/<lemma>.md` with credit to its authors. Credit Balaban and Dimock wherever their organization is used. A plain request to an open host is fine. Stop at any bot check, sign-in or paywall, and never use Sci-Hub or LibGen. Never pay for anything. Never commit a PDF. Keep downloads outside the worktree, and do not paste long passages from any source: write the argument in your own words.

**Files.** Write only your own file, `library/`, and `checks/<your part>_*`. Do not commit: the driver does that. Do not edit axioms, audit files or ledgers. Do not produce hash manifests or inventories. Do not re-read workflow documents.

**Reading the existing program.** Use `git show origin/claude/ym4d-proof-draft:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/<FILE>`. Files are long, so grep first and read with limits.

**Numerics.** Encouraged when they decide something. Write the pass and fail criteria first. Run one job at a time under `python3 scripts/lab_ops.py numeric-lock`, with BLAS threads set to 1, `nice`, and the script checking its own RSS against 2 GB.

**End every turn with a final line that is exactly one of:**
- `PUSH_STATE: CONTINUE`
- `PUSH_STATE: CLOSED` (the target is proved, with every obligation discharged)
- `PUSH_STATE: COUNTEREXAMPLE` (the target is false as stated in the actual model, and you have proposed the edit)
