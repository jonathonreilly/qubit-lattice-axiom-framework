# Push charter: upper chain

**Your file:** `parts/upper-chain.md` in the target folder `.claude/science/physics-loops/ym4d-hard-route-20261030/`. Read `GOAL.md` there first.

**Target.** Assuming only UV-EXT, in a form you make exact, prove the rest of the existence chain for SU(2) Wilson lattice gauge theory: volume-free, cutoff-free bounds on local gauge-invariant correlations at separated points; a joint subsequence on R^4 keeping translation, hypercubic symmetry and reflection positivity; and reconstruction on separated tests. Everything except UV-EXT must be proved here or be a named obligation.

**Why this may be much smaller than it looks.** Reflection-positivity chessboard estimates can turn an extensive bound on a torus into a local bound. If the source in each block is a constant shift of the coupling, then its reflected images fill the torus with a constant shift, so the local exponential moment is controlled by Z(beta + s)/Z(beta) to the power |block|/|torus|. If that is right, the hard core only needs the constant-coupling statement, not a position-dependent RG. Establish exactly which reflections and block shapes the Wilson action permits, for real and complex s. The existing `HRP.md` covers geometric reflection positivity.

**The decisive question, first.** This is a hand estimate of mine, so check it rather than trust it. For an operator of dimension four, the second derivative of the free energy density in s contains a contact contribution of order a^-4, because the two-point function behaves like x^-8 at short distance. A chessboard bound does not see separation, so it may give a bound that diverges with the cutoff, while the separated-point correlation stays finite. Determine whether this happens, and settle one of:
- the bound survives with a named subtraction and yields separated-point bounds uniform in a;
- it fails, and you find the replacement, for example observables at a coarser scale, block-averaged fields, or a bound on separated products that does not pass through the total-energy moment;
- UV-EXT must change, in which case write the exact stronger statement the hard core must deliver under Requests.

This outcome decides what the hard core must prove, so state it in your file as soon as you have it.

**Then.** Build the subsequence and reconstruction. `REC_LIB.md` and `REC_CONT.md` have separated-test reconstruction, `REALONLY.md` a moments-to-distributions implication, and `SPINE.md` a table of the chain. Check their hypotheses against what you actually deliver before relying on them. They are branch-level notes, not established results.

**Not your job.** Non-triviality and O(4), except to record what your endpoint gives them.

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
