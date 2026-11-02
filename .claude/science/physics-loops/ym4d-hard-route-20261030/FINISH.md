# Finishing the proof: instructions for workers

Written by the target lead on 2026-10-31. `GOAL.md` holds the target and the definition of non-trivial, and it wins over this file and over the charters. The charters' interface wording, UV-EXT, is superseded. This is research-stage working state, and nothing here grants status.

## Where it stands

**Existence is not proved.** As of 2026-11-02:

- **Two routes for the hard core.** Ours (`parts/hard-core--mapped.md`, the rarity work in `library/`) and the Sussman-Alpoge outline (`YM4_sketch_500.tex`, 505 pages, mapped in `library/sa-map.md`; 14 open items by its own index). The independent attempt (`parts/hard-core--independent.md`) is paused. `library/route-decisions.md` will say which route carries each position and why.
- **The shared blocker** is A3, uniform nonabelian multiscale background response (row 77). Our seam chain and the outline's 2.8 both stop there.
- **Closed and gated by hand:** the flat one-jump and several-jump coercivity chain (fan-ext, fd-local, lc-u, c0-loc, each read once by another provider); quadratic (LC) (`library/seam-quadratic-c.md`) and Lemma U (`library/lattice-uhlenbeck.md`, with a seed repair), both gated 2026-11-02 in `gates/share-check-199fac1cb.md`. Everything else on the critical path is open or conditional.
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




## How we work

0. **Is it worth doing? Ask before every lane, gate, edit or message, lead included.** It must name the open item on the critical path that it closes or kills (an obligation in `GOAL.md`, a row of `library/sa-ledger.md`'s top twenty, or a position in `library/route-decisions.md`), and what we would do differently if it succeeds or fails. No named item, or no change either way: do not do it. Each queue row opens with "Moves:" and that item. Each lead update lists what moved; work that moved nothing is named as waste, so it is not repeated.
1. **Literature first.** Each route or proof step starts from one wide search (Balaban, Dimock, the Sussman-Alpoge repository at `31a47c543775`, arXiv, older constructive field theory), recorded once in `library/lit-<topic>.md` and reused. A smaller lane reads those records and does a short targeted search.
2. **Build on published work; verify what the proof uses.** No firewall. Use any published result at once, labelled `unchecked`, credited by name (Balaban, Dimock, Sussman and Alpoge with Claude and Codex as authors of their text, Grok for its PRs #10133 to #10135). Before it counts as closed, it is re-derived in `library/` and gated by another provider. `library/sa-ledger.md` lists what the outline's Theorem 0 reads, with the twenty to verify first.
3. **Choose routes on evidence.** Ours and the outline's are both candidates, part by part. `library/route-decisions.md` records the choice, the reason and what would reverse it. Keep both live only while the evidence is open; budget follows evidence.
4. **Only closures count.** A lane ends with a proof, every step written, or an explicit counterexample. Try the counterexample first when unsure. A smaller statement is attacked in the same session; after two reductions with no closure, stop and report to the lead. Gates redo the proof and report WRONG with the failure, or confirm it. Notes are short.
5. **Go faster.** Use the outline's thirteen-part skeleton; read the same step in their QED3 and YM3 manuscripts first; for routine steps write a full draft, distil it and gate it; freeze what passes, reopening only on WRONG or a changed input; keep every machine on the critical path in parallel.
6. **Our proof only.** Workers do no work for other projects and never post outside this repository.

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
| 72 | `sa-ledger` | open | done, Codex Mini high | 358 statements of the outline that Theorem 0 reads, by position, all unchecked here. The twenty to verify first, in order: A1 (critical orbit), A2 (fibre coercivity), A3 (background response, row 77), WF substitution room, 2.8, 2.13, 2.10, F2, B3, D1, link symmetry, the all-mirror theorem, 7.6, 4.14, F3, E3, UI insertion, AK gluing, AC polygon divisibility, the OS reconstruction H3. | `library/sa-ledger.md` |
| 73 | `route-compare` | done (`library/route-decisions.md`): carry Package C for large field, retire our rarity obligations, Balaban for G, ours for L, C, Z and the witness | high | Moves: `library/route-decisions.md`, every position. Owner: "we should only follow their route if its better than ours." Decide, on evidence, which large-field (rarity) route to carry: ours (`library/rarity-fresh-c.md` S1 to S6 with the repairs in rows 60 to 65 and their gates, and `rarity-fresh-x.md`) or the outline's healed-history mechanism at `31a47c543775` (Package C, read through `library/sa-histories.md`, `library/sa-map.md` and `library/sa-2.8.md` if present), or a combination. For each: what is proved and gated, the open steps listed hardest first, the best evidence for and against the hardest open step, what already covers depth, many marks and the measure mu, and how much remains to reach the consumers (here, the upper chain; there, Theorem 0). Then the same coverage table for the whole chain, ours against theirs, position by position. Recommend, per position, one route or both, with the reason, and say what evidence would reverse each recommendation. Write the result as the first version of `library/route-decisions.md` as well. | `library/route-compare.md`, `library/route-decisions.md` |
| 77 | `a3-response` | gated WRONG (`gates/a3-gate-b2c312b2e.md`): Theorem FL not closed (Lemma 3 tent norm, Lemma T double count, Lemma P seams, missing overlap constant, repair given) and, even repaired, not the outline's A3 (other gauge, no derivative or Hölder package, no complex domains); 5.3 and CL wrong as stated. Survives: Lemmas 1, 2, H, single-layer Theorem E. Next: row 82 | max | Moves: `library/sa-ledger.md` #3, and our (REL). Both routes stop at uniform nonabelian multiscale background response (outline A3, (1b) Theorems 3, 4, 6(c); our (REL), (R2), (R3), (REL-D); stop (L) of `library/sa-2.8.md`). Per `library/lit-large-field.md` Section 3: first PROVE the flat linear statement by porting Dimock arXiv 1712.10029 Section 3.7 ((296) to (303), Lemma 12) to d = 4 and SU(2) at V_0 = 1, with Balaban CMP 95, 96 credited; read it from arXiv (https://arxiv.org/abs/1712.10029; fetch the PDF or source and read the cited sections; do not commit it). Then attack the curved nonlinear part: the response between two critical backgrounds (L), and whether Balaban's multiscale Landau gauge keeps the contour averages of Example E (`library/rel-phi-c.md`) bounded, so (REL-D) holds. Run to closure (How we work, item 4). | `library/a3-response.md` |
| 78 | `a2-curved` | open | Codex, laptop, max | Moves: `library/sa-ledger.md` #2. The outline's A2 (L3835 of `YM4_sketch_500.tex` at `31a47c543775`, rank 2 in `library/sa-ledger.md`): coercivity Re<B, E B> >= c ||B||^2 on gauge-fixed fluctuation fibres QB = 0 at regular, curved backgrounds, on every conditioning set, uniform in scales, and with c/2 on the complex neighbourhoods. The outline has only the flat case (CF18, WI15). Our curved D-coer line (`library/c0-loc.md`, `library/lc-u.md`, `library/fan-ext.md`, `library/fd-local.md` and their gates) proves the real-background version for our class map. Port it to the outline's block average, gauge fixing and conditioning sets, then extend to complex neighbourhoods. Run to closure (How we work, item 4). | `library/a2-curved.md` |
| 79 | `a1-orbit` | done: fixed-geometry A1 proved, real and holomorphic; uniformity across separated layers open, row 81 | Codex, Mini, max | Moves: `library/sa-ledger.md` #1, the outline's A1 (L3811) and its Theorem 1 (L9660): one regular constrained critical orbit for every allowed nested family and regular datum, unique in a stated neighbourhood, with a gauge representative Borel in real data and holomorphic nearby, radii and constants uniform in the number of scales, compatible with restriction, seams and torus change. If it holds, the outline's background construction stands; if it fails, the outline's route loses its foundation and ours is the only candidate. Use our gated Lemma U (`library/lattice-uhlenbeck.md`, `gates/share-check-199fac1cb.md` (c)) for gauge control uniform in box size, Dimock arXiv 1712.10029 for the multiscale minimiser in the abelian case, and Balaban CMP 102 (1985) where reachable. Try first to build a regular datum with two regular critical orbits, or one whose representative's constants grow with depth. Run to closure (How we work, item 4). | `library/a1-orbit.md` |
| 80 | `lit-balaban` | done; lead checked against the CMP 102b scan: Theorem 1 (p. 279) is (U) uniform in depth, Proposition 8 puts every critical point of (6) in (8), and (189)-(190) are "We do not perform these calculations here", so nonlinear A3 stays ours (row 77). (1b) Theorem 2 first half is not in Balaban | high | Moves: the outline's (1b) Theorem 2 and (U) (rows 77, 79), and the R operation of our rarity route. Citing and building on Balaban is the plan; we only rebuilt A3 because his proofs had not been read. Find legal full texts of Balaban's CMP papers (95, 96, 98, 99, 102, 109, 116, 122 and the rest of the series): Project Euclid, the Rutgers repository (it marks CMP 95 open access), author or university pages, arXiv. No paywalls, sign-ins or bot-check bypass. For each one you can read, record where it proves Theorem 2 or (U) (CMP 102 Prop. 8 per the outline), the nonlinear background response, and the R operation (CMP 122), with exact statement and page, so the next lane ports and checks his proof instead of writing a new one. Name the texts you could not reach. | `library/lit-balaban.md` |
| 81 | `a1-balaban` | open | Codex, Mini, max | Moves: `library/sa-ledger.md` #1 (A1) and (U) for rows 77 and 80. Balaban CMP 102 (1985) 277-309, Theorem 1, proves the unique critical orbit with regularity by induction over the layers, which is the open part of `library/a1-orbit.md`. Port his proof onto the outline's A1, starting from `library/a1-orbit.md` Sections 7-8. Paper outside git on the Mini: `~/ym4d-papers/cmp102.txt` (OCR text) and the PDF. His inputs from CMP 98 (17-52), CMP 99 (75-102) and CMP 99 (389-434) are not yet in hand: state each exactly, then supply it from our library (`lattice-uhlenbeck.md`, `fibre-propagator.md`, `c0-loc.md`, `a3-response.md`) or mark it cited-pending. Credit Balaban. Run to closure. | `library/a1-balaban.md` |
| 82 | `a3-balaban` | running, laptop Codex | Codex, laptop, max | Moves: `library/sa-ledger.md` #3 (A3). Port Balaban's propagator bounds (CMP 95 Sect. 1, CMP 96 Lemma 2.1, CMP 99b Theorems 3.1-3.13) onto the outline's A3 as the gate states it (`gates/a3-gate-b2c312b2e.md` Section 8: kernels and covariances, weighted derivative and Hölder package, Landau pair, complex domains, seam and box rows). Keep what the gate kept from `a3-response.md`. Papers outside git (Mini `~/ym4d-papers/`, README lists them). Credit Balaban. Run to closure. | `library/a3-balaban.md` |
| 83 | `floor-screen` | open | max | Moves: `library/route-decisions.md` position H (Package C, rank 1) and its first reversal test. In the outline's floor screening (SA L18334-18415; excluded floor L18353-18397): does the localized background exist and decay outside the floor for arbitrary data inside it? Counterexample first: a heavy wall in the floor whose influence through the fixed-width collar is not R_m^2 eps_m e^(-delta_0 M R_m)-small. Use Balaban CMP 102 Theorem 1 and Propositions 8-9 and CMP 99 (389-434) from `~/ym4d-papers/` (outside git; README lists them; never copy them into the repository). If no counterexample, prove the screening statement, or reduce it exactly to nonlinear A3 on localized families with rows 81 and 82 cited as pending. Run to closure. | `library/floor-screen.md` |

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
- **Gate reports** open with one provenance line (model, effort, commit, not an audit), then a verdict per statement (ADVANCE, CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure. Keep them short; see How we work, item 4.
- **Label honestly**: gap, unchecked, implication, discharged. A step recalled from memory but not proved is a gap. A truthful gap is never penalized.
- **Literature.** See How we work, items 1 and 2. Stop at a bot check, sign-in or paywall; never pay, never commit a PDF, and do not paste long passages.
- **No computer-assisted steps.** See the section of that name in `GOAL.md`. A run can refute or guide, never discharge. If a statement you need rests on a computed value, label it gap and look for a hand proof.
- **Numerics.** One job per machine, under `python3 scripts/lab_ops.py numeric-lock`. Confirm the acquire succeeded before running, and do not pipe it through `tail`. Set BLAS threads to 1, use `nice`, and have the script stop itself above 2 GB RSS. On the Mac mini, start a numeric job only at 50 percent memory free or more, and never use a process pool.
- **Never** edit axioms, audit files or ledgers, run an audit, push to main, or post anything public; the owner approves every public post's exact text.
- **Ask the owner only** about axiom edits, public posts, spending and pace. A scientific fork gets probes.

## Prompt for a new worker

```text
Work on PR #10132 of jonathonreilly/qubit-lattice-axiom-framework, branch claude/ym4d-hard-route. Read .claude/science/physics-loops/ym4d-hard-route-20261030/FINISH.md and GOAL.md in that folder. Take the first free item in the queue, follow its rules, finish that item only, push it, and stop with a short result: verdicts or what was proved, and what is still open.
```
