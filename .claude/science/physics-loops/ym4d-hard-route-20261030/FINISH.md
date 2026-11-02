# Finishing the proof: instructions for workers

Written by the target lead on 2026-10-31. `GOAL.md` holds the target and the definition of non-trivial, and it wins over this file and over the charters. The charters' interface wording, UV-EXT, is superseded. This is research-stage working state, and nothing here grants status.

## Where it stands

**Existence is not proved.** As of 2026-11-02:

- **Two routes for the hard core.** Ours (`parts/hard-core--mapped.md`, the rarity work in `library/`) and the Sussman-Alpoge outline (`YM4_sketch_500.tex`, 505 pages, mapped in `library/sa-map.md`; 14 open items by its own index). The independent attempt (`parts/hard-core--independent.md`) is paused. `library/route-decisions.md` will say which route carries each position and why.
- **The shared blocker** is A3, uniform nonabelian multiscale background response (row 77). Our seam chain and the outline's 2.8 both stop there.
- **Closed and gated by hand:** the flat one-jump and several-jump coercivity chain (fan-ext, fd-local, lc-u, c0-loc, each read once by another provider), quadratic (LC) (`library/seam-quadratic-c.md`, ungated). Everything else on the critical path is open or conditional.
- **Upper chain and witness:** `parts/upper-chain.md` and `parts/witness.md`, last gated as recorded in their headers; not the current bottleneck.

## What finishing means

1. The hard core is closed, by our route, the outline's, or a mix as `library/route-decisions.md` records, with every statement it reads verified here, and it delivers an interface statement the upper chain reads as written.
2. The upper chain's conditional theorems lose their conditions.
3. NT1 and NT2 hold, as `parts/witness.md` states them.
4. One clean document holds the whole chain, followed by a line-by-line independent review of it, then the owner's approval of the exact text. Balaban and Dimock are credited by name, and so are Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) for every step, idea or construction taken from their repository, and Grok for anything taken from its pull requests here, in each note that uses it, in the final document and in any public post. Until then there is no public claim.

## State of our route, 2026-11-02

One cross-provider read each, not an audit, no status.

| Step | Where | State |
|---|---|---|
| Flat one-jump coercivity and F-D, fans | `library/fan-ext.md`, gate 73b09692a | stands, flat |
| Flat several-jump coercivity | `library/fd-local.md`, gate 00f9df685 | stands |
| Curved local lift (LC_U) | `library/lc-u.md`, gate 0bfc3ff42 | stands on its domain |
| Curved D-coer, TP-sharp, Ward, (NC) | `library/c0-loc.md`, gate 51679e441 | stands on the admitted domain, D1 threshold repair |
| Several-jump F-D, absolute rate | `library/c0-loc.md` (10.8) | implication; reads stationary class fills, top inclusions, class identification |
| (FALL) rate for DS and COMP-B | Lemma DOM, gate shell-end-c16e2a968 | proved given (FALL) at a smaller rate; same-model; region clause open |
| Small stationary fill, one domain | `library/fill-supply.md` Section 4 | contract written, not closed |
| **Full-law mass outside the chart: rarity** | (AE-R), (HW), Z, DM, `library/one-window.md` | **open. Most likely place for this route to fail** |
| (UP) at nonlinear level | (GLUE-E), (NL-pay), (PATCH) | open |

**Rarity, the next question (`rarity-fresh`).** The consumers need a full-law bound on marked events under class parents, with product form for compatible marks and control through rough intermediate parents. Known: raw fine energy is extensive on typical fields (Lemma TYP), so a raw fine-energy trigger cannot be rare; `heavy-wall` shows the stage's layer selection has no output beside a heavy wall; chart concentration does not bound the complement; centre-plane chessboard fails on the class branch (`one-window` Section 3); a uniform local gain fails. (HW) has no refutation. Propose and attack one complete route to a full-mass producer that the consumers can read, and say which consumers change. You may change the state or a statement if you say what breaks. Do not narrow to a smaller inequality as your output: end by naming the first step of your route that fails, or carry it through.




## Literature first (owner, 2026-11-02, core rule)

Owner: "every route should start with a lit search that runs far and wide before building - this should be a core rule so we dont waste time reinventing. its required that we validate the proofs for our application of them but otherwise we stand on the shoulders of giants here."

- No route, lemma lane or repair starts building until a literature search has run far and wide for its statement and its method: Balaban's series, Dimock's expositions, the Sussman-Alpoge repository (outline, QED3 and YM3 manuscripts), the other public projects its README lists, arXiv and journals, older constructive field theory (Glimm-Jaffe, Brydges, Federbush, Gawedzki-Kupiainen, Magnen-Rivasseau-Seneor, King, Feldman-Magnen-Rivasseau-Seneor), recent probabilistic work (Chatterjee, Cao, Chevyrev and others), and lattice gauge theory more widely.
- Each search is written to `library/lit-<topic>.md`: what was found, where, the exact statement, how close it is to ours, and whether its proof is accessible. A lane prompt names the search it builds on.
- Found results are used, credited, and then verified for our application under the rule in "Build on published work". A search that finds nothing is recorded too, so nobody repeats it.
## Build on published work (owner, 2026-11-02; replaces the firewall)

Owner: "we should build on all published work, not reinvent the wheel - that should be a core principle"; "there are no bonus points for independence here". The firewalls are retired: every worker may read every file here, the Sussman-Alpoge repository at its current commit (https://github.com/ethanwsussman/Yang--Mills-LLM-experiment; `YM4_sketch_500.tex` is the 505-page SU(2) outline, its "Index of arguments and proof obligations" lists what it still owes), Balaban's papers, Dimock's expositions and any other literature it can reach.

- Before deriving anything, look for the statement in that outline and in the literature. Prefer filling a named open obligation of the outline over a new route.
- Credit by name: Balaban for the programme, Dimock for expositions, Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) for anything taken from their repository.
- **Verify everything the proof uses (owner, 2026-11-02).** "When we build on published work, I want us to actually verify the derivations the proof uses - using the same validation framework we have so we dont build on mistakes." Reading published work is not accepting it. Every statement the final chain reads, whether from the outline, Balaban, Dimock or elsewhere, passes the same checks as our own: a written hand proof in `library/` (re-derived, not quoted, credited to its source), labelled discharged, implication or gap, then a gate by a reader from another provider before it is load-bearing. Their labels ("proved", "outlined", "cited") grant nothing here.
- `library/sa-ledger.md` is the ledger: every statement of the outline at `31a47c543775` that Theorem 0 reads, with its location, its status there, and its status here (unchecked, re-derived, gated, WRONG). Lanes update their rows. Order: hardest and most load-bearing first; open obligations and verification of outlined steps share the queue.
- The side column of the queue is kept for history only.
- **Grok works here too (owner, 2026-11-02).** Grok's pull requests in this repository are part of the work to build on: #10133 (conditional mass-gap crossover reduction), #10134 (mass-gap interface note, gap against NT1 and NT2) and #10135 (MDTN truncated gauge theory, strong-coupling gap). Read them like any source, verify what our chain uses under the same rule, and credit Grok by name. Do not edit or rebase Grok's branches; propose changes to its work in our own notes, or ask the owner.
- **Our proof first, help when cheap (owner, 2026-11-02):** "its cheap to tell them when we find issues - we just shouldnt go looking for issues if they are not relevant to our lanes. We can share proofs over if the proofs help them out (and we can see how they would help) once we have them and they are validated. We just dont spend extra time on things that are NOT relevant to our path ... help when its cheap to do so, leverage their work wherever possible with attribution." So: every lane serves our proof; we never hunt for their errors outside our lanes; an error our lanes find is reported promptly as an issue; a validated proof of ours that visibly helps them is offered once it has passed its gate. Credit them, and Grok, for every way their work helped.
- **Reporting errors (owner, 2026-11-02):** the bar is high. Owner: "we should only be posting there if we find actual errors in their work not missing references, or we have actual solid lemmas or proofs to share with them." Post only (a) an actual error, a false statement or a wrong derivation shown by an explicit configuration or calculation and confirmed by a gate here, or (b) a solid lemma or proof of ours, gated, that visibly helps them. Missing references, unproved steps, gaps and notation do not qualify; they stay in `library/sa-findings.md` for our own use. The owner approves each issue's exact text.
## Route decisions (owner, 2026-11-02)

Owner: "maybe both paths need worked, the goal is the full proof, not following some other lead. so we need to carefully analize which path we take and why, and re-evaluate that choice as we learn."

- The goal is a complete, checked proof. Our route and the Sussman-Alpoge outline's route are both candidates, position by position; neither is the default.
- Where the evidence does not clearly favour one, both stay live with at least one lane each, hardest open step first. Today that holds for the large-field (rarity) position: the outline's 2.8 (row 71) and our (AR) (row 67, restarted) both run.
- `library/route-decisions.md` holds, for each position, the current choice, the reason, the evidence that would reverse it, and the date. `route-compare` (row 73) writes the first version. The lead revisits a position whenever a lane result touches it, and records any change with its reason. A route is retired only when a gate shows its hardest step fails, or the other route closes that position.
## Hard-core standard (lead and owner, 2026-11-02)

Owner: "if that type of thinking and work is going on in our own repo, we may not be being hard core enough in our approach." Measured on 2026-11-02: of about a dozen attack lanes, one closed a statement by hand (`seam-quadratic-c`); the rest ended STOPPED at a smaller inequality, and each stop was handed to a fresh session, which narrowed again. Notes ran 30 to 48 KB, much of it labels, scope paragraphs and lists of unchecked inputs. That is cataloguing, not proving.

- **Proofs and counterexamples are the only output that counts.** A lane's result is a closed lemma, with every step written, or an explicit configuration that kills a statement. Lists of gaps, missing references, unverified inputs and scope caveats are not results; write them in one short paragraph at most.
- **Run to closure.** STOPPED is what happens when the budget runs out, not a goal. If you reach a smaller inequality you expect to be true, attack it in the same session; if you expect it false, try to build the counterexample. Hand off only when the budget is spent, and then say how far the attack got.
- **Gates look for errors.** A gate redoes the proof and reports WRONG with the explicit failure, or confirms the step. It does not list every input the step reads unless one of them is false or unavailable.
- **Short notes.** The proof, the counterexample, or the precise point where the argument fails. No restating the setting the folder already holds.
- **The lead counts closures.** Each update reports lemmas closed and gated on the critical path, and statements killed, not lanes run.
## Methods adopted from the Sussman-Alpoge project (owner, 2026-11-02)

Owner: "lets adopt any methods or approaches that will accelerate our work." What we take, and where:

- **Their skeleton.** The thirteen positions of `YM4_assembly_overview` (L, M, G, E, N, P, C, T, R, K, H, V, Z) are the skeleton for `library/route-decisions.md` and `library/sa-ledger.md`. Hardest-first runs inside a complete skeleton, not instead of one.
- **A model ladder.** Before a YM4 lane on a position, read the same position in their QED3 and YM3 manuscripts (their assembly overviews give the correspondence). A mechanism that works there is the first candidate; a check that fails there is a cheap kill.
- **Generate, then distil, then check, where risk is low.** For positions that are standard (rank 8 and below in `library/sa-map.md` Section 4: backgrounds, small-field step, one-loop law), one long full draft at max, then a distillation to a minimal written proof, then a cross-provider gate. Forced-decision lanes stay for the positions where the proof could fail (ranks 1 to 4).
- **Freeze what is checked.** A section that passes its gate is frozen and cited, and is reopened only by a WRONG verdict.
- **Sharing.** Errors reported promptly; validated proofs that help them offered once gated; per "Our proof first, help when cheap".
## Current order

Lead, 2026-11-02, after `library/sa-map.md`, `library/sa-2.8.md` and `library/lit-large-field.md`.

- **First: A3 (row 77).** Both routes now stop at one statement, the uniform nonabelian multiscale background response. Its flat linear part is Balaban CMP 96, with a readable abelian proof by Dimock to port; the curved nonlinear part is open.
- **Beside it:** our (AR) (row 67), the one-loop law (row 76), checks of our own proofs and the outline's route questions (row 75), and the ledger of what the outline's main theorem reads (row 72).
- **Then:** `route-compare` (row 73) writes `library/route-decisions.md`, part by part.
- **Measure:** lemmas closed and gated on the critical path, and statements killed.


## Queue

Take the first item that is not taken, unless the lead has named one for you. An item is taken if a file matching its output exists with a live lease, or a finished report. Pin the statement at the branch head and put the commit in the file name. A worker on the Mac mini takes these items in order, one at a time, so check the branch before starting one.

Past rows are in `QUEUE_DONE.md`.

| # | Item | Side | Effort | Task | Output |
|---|---|---|---|---|---|
| 67 | `annular-reset` | neutral | restarted 2026-11-02, Mini Codex after `sa-ledger` | Our route's hardest open step on the large-field position, kept live beside the outline's 2.8 (Route decisions). Also usable by the outline if its prepared-shell locality leaves an exterior extension gap (`library/sa-histories.md` 6.6). | Prove (AR) of `library/sp-nonlinear.md` Section 7 by hand, a statement about one connection on a lattice annulus with no hierarchy. The threshold epsilon_r may depend on r and the constant may not. Candidate route, to be attacked before use: with epsilon_r small, all plaquettes are small, so after an axial or Landau gauge on the annulus the nonlinear errors are a factor C(r) epsilon_r^(1/2) relative and can be absorbed; the uniform content is then a linear Poincare inequality for 1-cochains on the annulus, ||a||_2 <= C r ||d a||_2 in a suitable gauge, with C absolute, built from explicit cone homotopies on overlapping convex pieces and the vanishing of H^1 of the annulus, proved by hand. Hardest first: test whether the relative-error absorption really holds uniformly, and whether the matching of both boundary gauges costs a radius factor. End PROVED, REFUTED or STOPPED. | `library/annular-reset.md` |
| 72 | `sa-ledger` | open | done, Codex Mini high | 358 statements of the outline that Theorem 0 reads, by position, all unchecked here. The twenty to verify first, in order: A1 (critical orbit), A2 (fibre coercivity), A3 (background response, row 77), WF substitution room, 2.8, 2.13, 2.10, F2, B3, D1, link symmetry, the all-mirror theorem, 7.6, 4.14, F3, E3, UI insertion, AK gluing, AC polygon divisibility, the OS reconstruction H3. | `library/sa-ledger.md` |
| 73 | `route-compare` | open | high | Owner: "we should only follow their route if its better than ours." Decide, on evidence, which large-field (rarity) route to carry: ours (`library/rarity-fresh-c.md` S1 to S6 with the repairs in rows 60 to 65 and their gates, and `rarity-fresh-x.md`) or the outline's healed-history mechanism at `31a47c543775` (Package C, read through `library/sa-histories.md`, `library/sa-map.md` and `library/sa-2.8.md` if present), or a combination. For each: what is proved and gated, the open steps listed hardest first, the best evidence for and against the hardest open step, what already covers depth, many marks and the measure mu, and how much remains to reach the consumers (here, the upper chain; there, Theorem 0). Then the same coverage table for the whole chain, ours against theirs, position by position. Recommend, per position, one route or both, with the reason, and say what evidence would reverse each recommendation. Write the result as the first version of `library/route-decisions.md` as well. | `library/route-compare.md`, `library/route-decisions.md` |
| 75 | `share-check` | open | Codex, laptop, xhigh | Gates of our own proofs that our chain needs, plus two route questions. Items, each against the outline at `31a47c543775`: (a) gate `library/seam-quadratic-c.md` (quadratic (LC), absolute constants) and say whether it bears on their A3 and Props 2.8, 2.10; (b) gate Example E and Theorem R of `library/rel-phi-c.md` and decide whether their Landau-pair gauge of (1b) Theorems 3 and 4 avoids Example E; (c) gate `library/lattice-uhlenbeck.md` (gauge uniform in box size; their gauges are pointwise and box-size dependent per `library/sa-map.md` Section 3) and say where in their text it would help; (d) whether the examples of `library/hw-fine.md` and `library/heavy-wall.md` can sit in their old floor F of L18334 to L18415, their hardest open item; (e) the lead's reading that L17508 points to a paragraph '(2e), Reality and positivity' that (2e) does not contain (their Prop 4.5 at L22602 is at real sources), and whether positivity of the reference normalisation on supports is supplied anywhere. Verdict per step ADVANCE, CORRECT-NO-ADVANCE or WRONG; any checked defect in their text goes into `library/sa-findings.md`. | `gates/share-check-<commit>.md` |
| 76 | `p1-gate` | open | Codex, laptop, high | Low-risk position run in parallel (Methods adopted). Gate Theorem P1 of `parts/hard-core--mapped.md` (one-loop telescoping, abs(sum beta^0_l - k c_0) <= c_2) and `library/twisted-order-calculus.md` by hand, and compare with the outline's (CP2) and its one-loop section (about L21065 of `YM4_sketch_500.tex` at `31a47c543775`) and with Balaban CMP 109. Take whatever of theirs shortens our proof, re-derived here and credited. Verdict per step. | `gates/p1-gate-<commit>.md` |
| 77 | `a3-response` | open | max | Both routes stop at uniform nonabelian multiscale background response (outline A3, (1b) Theorems 3, 4, 6(c); our (REL), (R2), (R3), (REL-D); stop (L) of `library/sa-2.8.md`). Per `library/lit-large-field.md` Section 3: first PROVE the flat linear statement by porting Dimock arXiv 1712.10029 Section 3.7 ((296) to (303), Lemma 12) to d = 4 and SU(2) at V_0 = 1, with Balaban CMP 95, 96 credited; read it from arXiv (https://arxiv.org/abs/1712.10029; fetch the PDF or source and read the cited sections; do not commit it). Then attack the curved nonlinear part: the response between two critical backgrounds (L), and whether Balaban's multiscale Landau gauge keeps the contour averages of Example E (`library/rel-phi-c.md`) bounded, so (REL-D) holds. Run to closure under the Hard-core standard. | `library/a3-response.md` | `library/a3-response.md` |

## Joining

Use a fresh session on Opus 5.5 at the item's effort. Do not resume the sessions of the running pushes.

```bash
python3 scripts/lab_ops.py worktree-add ym4d-<item> --target claude/ym4d-hard-route --path .claude/science/physics-loops/ym4d-hard-route-20261030
```

**Claim first.** Create your output file with these two lines, then push. If the push conflicts or the file exists, take the next item.

```text
lead: <provider>/<model>/<effort> <session or worker name>
lease_until: <now + 12 h, UTC>
```

To share, run `git pull --rebase origin claude/ym4d-hard-route && git push origin HEAD:claude/ym4d-hard-route`. A machine with no push rights to this branch leaves its files for the lead, who commits them.

**Remove the worktree** when your work is pushed, with `lab_ops.py worktree-remove`.



## Working efficiently

Measured on the pushes so far: a resumed push carries about 300,000 to 580,000 tokens of context on every step, and 70 to 90 percent of its active time is the model generating text. A fresh, narrow session avoids most of that: the first fresh gate wrote 195,000 tokens for about $8 at API rates, where a resumed push wrote 202,000 for about $219.

- **Hardest first.** Owner, 2026-11-01: go after the hard statements first, to save grinding on the easy base. Work goes to the statement the proof is most likely to die on. A routine hand rebuild, or an elementary citation, waits until a hard-core attempt closes, unless it could be hiding a real gap.
- **One item, one session, run to closure.** Stay on the item until it is proved or refuted, including any smaller statement it reduces to, as long as the budget lasts. Do not move to unrelated items or tidy other files.
- **Do not read whole files.** Part files are 145 to 350 KB, and the folder holds about 1.6 MB of text. Find the statement with `grep -n`, then read the statement, its proof and what it cites.
- **Try to kill it first.** A short computation with pass and fail criteria written first can save a long argument. Report what a run can and cannot establish. A search that finds nothing does not prove a bound.
- **Save as you go.** Write your report section by section. A reader that dies at the output limit with nothing saved is a total loss.
- **Keep reports short.** At most ten defects, ranked by what each breaks. If a defect breaks the consumer's statement, say so and stop unless the rest is independent of it. Give a repair if you see one, marked as unproved.
- **No subagents** unless the item needs a separate reader. Each one is a full extra cost.

## Rules

- **Write only** your output file, `library/` for a new lemma, and your `checks/` folder. Evidence for another file's owner goes in your report, and the lead forwards it.
- **Gate reports** open with one provenance line (model, effort, commit, not an audit), then a verdict per statement (ADVANCE, CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure. Keep them short; see Hard-core standard.
- **Label honestly**: gap, unchecked, implication, discharged. A step recalled from memory but not proved is a gap. A truthful gap is never penalized.
- **Literature.** See Literature first and Build on published work. Stop at a bot check, sign-in or paywall; never pay, never commit a PDF, and do not paste long passages.
- **No computer-assisted steps.** See the section of that name in `GOAL.md`. A run can refute or guide, never discharge. If a statement you need rests on a computed value, label it gap and look for a hand proof.
- **Numerics.** One job per machine, under `python3 scripts/lab_ops.py numeric-lock`. Confirm the acquire succeeded before running, and do not pipe it through `tail`. Set BLAS threads to 1, use `nice`, and have the script stop itself above 2 GB RSS. On the Mac mini, start a numeric job only at 50 percent memory free or more, and never use a process pool.
- **Never** edit axioms, audit files or ledgers, run an audit, push to main, or post anything public; the owner approves every public post's exact text.
- **Ask the owner only** about axiom edits, public posts, spending and pace. A scientific fork gets probes.

## Prompt for a new worker

```text
Work on PR #10132 of jonathonreilly/qubit-lattice-axiom-framework, branch claude/ym4d-hard-route. Read .claude/science/physics-loops/ym4d-hard-route-20261030/FINISH.md and GOAL.md in that folder. Take the first free item in the queue, follow its rules, finish that item only, push it, and stop with a short result: verdicts or what was proved, and what is still open.
```
