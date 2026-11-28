# Push charter: witness

**Your file:** `parts/witness.md` in the target folder `.claude/science/physics-loops/ym4d-hard-route-20261030/`. Read `GOAL.md` there first, in particular the definition of non-trivial (NT1, NT2).

**Target.** Find observables and a proof that the limit in T1 satisfies NT1 and NT2, given what the hard core delivers at a fixed physical scale. Everything beyond the hard core's statements must be proved here or be a named obligation.

**Why the existing witness is not enough.** `gates/net-tier-upper-chain-c3242879df.md` found that the witness in `parts/upper-chain.md`, Text 10, has as its main term the value for three free Maxwell copies, and that no vertex is used. Its clauses are also met by a static random constant field. Read that gate, D1 to D3, and check it rather than trust it.

**First, settle these.**
- **A test that separates from Gaussian.** Name a concrete observable and compute the difference from every Gaussian law, with its coefficient in the coupling. One lead from the gate: the combination (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2) is odd under b -> -b when W_i = exp(i b_i), so its expectation vanishes exactly for a symmetric Gaussian b, and the three-gluon vertex is expected to make it non-zero at relative order g. That coefficient has not been computed, and these loops are joined rather than separated, so decide what it shows and whether a separated test exists. Other leads are welcome, such as deviations from Gaussian values at relative order g^2, or an area-type bound on large loops.
- **What accuracy this demands.** Theorem 10.7 has an error omega(g) with no rate. Say exactly what rate the test needs and which one-step statement of hard-core must supply it, or write that statement under Requests.
- **NT1.** The gate suggests that the connected correlator at two separations, each matching its Gaussian value within a stated tolerance, shows H is not zero. Check this and prove it.

A computation you can finish unconditionally comes first, since a coefficient that vanishes would change the plan. A proof strategy that ignores the actual Wilson weight or works in every dimension cannot be right (`parts/upper-chain.md`, Proposition 10.4).

**Not your job.** UV stability itself, and O(4).

## How this push runs

You own this file for the whole run. A driver resumes you repeatedly and only the driver ends the run, so build on your own context.

**Your file.** Keep one file, named above, and rewrite it as your understanding improves. It is not a log. Keep this structure:

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

**What stopping means.** A conditional theorem with a new named lemma is a checkpoint, not an end. Go to the hardest remaining inequality by a route you have not tried. If it is false, build a counterexample in the actual model and propose the edit.

**Literature.** Use any open source for method. Nothing from a paper is load-bearing until it is proved in your file, or in `library/<lemma>.md` with credit to its authors. Credit Balaban and Dimock wherever their organization is used. A plain request to an open host is fine. Stop at any bot check, sign-in or paywall, and never use Sci-Hub or LibGen. Never pay for anything. Never commit a PDF. Keep downloads outside the worktree, and do not paste long passages from any source: write the argument in your own words.

**Files.** Write only your own file, `library/`, and `checks/witness_*`. Do not commit: the driver does that. Do not edit axioms, audit files or ledgers. Do not produce hash manifests or inventories. Do not re-read workflow documents. The part files are large, so grep first and read with limits.

**Numerics.** Encouraged when they decide something. Write the pass and fail criteria first. Run one job at a time under `python3 scripts/lab_ops.py numeric-lock`, with BLAS threads set to 1, `nice`, and the script checking its own RSS against 2 GB.

**End every turn with a final line that is exactly one of:**
- `PUSH_STATE: CONTINUE`
- `PUSH_STATE: CLOSED` (the target is proved, with every obligation discharged)
- `PUSH_STATE: COUNTEREXAMPLE` (the target is false as stated in the actual model, and you have proposed the edit)
