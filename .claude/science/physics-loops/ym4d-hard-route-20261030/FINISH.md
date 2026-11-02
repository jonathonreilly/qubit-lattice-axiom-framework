# Finishing the proof: instructions for workers

Written by the target lead on 2026-10-31. `GOAL.md` holds the target and the definition of non-trivial, and it wins over this file and over the charters. The charters' interface wording, UV-EXT, is superseded. This is research-stage working state, and nothing here grants status.

## Where it stands

**Existence is not proved.** Both hard-core attempts report few gaps, but most of what they label derived has been read only by the same push or by its own readers:

| File | gap | unchecked | implication | Last read from outside |
|---|---|---|---|---|
| `parts/hard-core--independent.md` | 1 | 1 | 29 | Gates at `16ca92dd7` and, cross-provider, `independent-2c-codex-b4de676b7`: the cancellation at the saddle stands, (GOOD) is WRONG as displayed, and (TAIL), (R1), (R2) and the wall count do not yet close; counts here predate them |
| `parts/hard-core--mapped.md` | 3 | 0 | 58 | Gates at `60036ba4d`, `7c12c6981` and, cross-provider, `theorem-dm-codex-892504e4c`: Theorem DM, (Z), Lemmas CC and OW CORRECT-NO-ADVANCE, with the free-bond count of DM on the wrong region; and `excess-codex-6c0d4e1c9`: Lemma EX ADVANCE, with Lemma LIFT and Lemma EX2' CORRECT-NO-ADVANCE; counts here predate them |
| `parts/upper-chain.md` | 6 | 1 | 19 | Cross-provider gate `fourth-form-codex-b4de676b7`: Lemmas 20.3, 22.1, 22.2 and Prop 20.4 ADVANCE; Lemma 20.5 and Theorem 14.1c CORRECT-NO-ADVANCE. Codex is working on these as item 10 |
| `parts/witness.md` | 5 | 3 | 10 | Gate at `3b7fd4e57`, which changed the definition of NT2 |

`lab_ops.py status` counts 44 open obligations, but it leaves out both attempt files, so it understates what is open.

**What limits progress.** Each gate so far has changed the route, so a statement labelled derived is not yet safe to build on. The pushes have moved far past the last read. The cheapest useful work now is to try to break load-bearing statements, in fresh sessions, before more text is built on them.

## What finishing means

1. One hard-core attempt has all its obligations discharged, and it delivers an interface statement the upper chain reads as written.
2. The upper chain's conditional theorems lose their conditions.
3. NT1 and NT2 hold, as `parts/witness.md` states them.
4. One clean document holds the whole chain, followed by a line-by-line independent review of it, then the owner's approval of the exact text. Balaban and Dimock are credited by name. Until then there is no public claim.

## Current order

Lead, 2026-11-01, after `gates/strategy-codex-b5251ab07.md`. Three kill tests come first: `joint-induction`, `tail-two-step`, `seam-quadratic`. The unit of work is one fresh session on one inequality, delivering a displayed estimate or a specific failed term.

- **Paused:** the alternating resumed pushes of both attempts. They can resume if a kill test survives; their unread notes are kept.
- **Parked:** general witness work, and routine hand rebuilds, until one hard-core attempt delivers a surviving induction step. A second-jet feasibility check stays allowed.
- **Finish criterion for this phase:** one surviving, fully specified induction step, with its complete norm, its constants and an honest base case. Fewer gap rows is not the measure.
- **If a test kills its route:** compare, on the same two-step example, an induction that carries explicit large-field regions and localized insertions, as Balaban organizes it, before funding more repair. The compressed state of both attempts may be costing more than it saves.

## Queue

Take the first item that is not taken, unless the lead has named one for you. An item is taken if a file matching its output exists with a live lease, or a finished report. Pin the statement at the branch head and put the commit in the file name. A worker on the Mac mini takes these items in order, one at a time, so check the branch before starting one.

| # | Item | Side | Effort | Task | Output |
|---|---|---|---|---|---|
| 1 | `lemma-ex` | mapped | high | Try to break Lemma EX and Lemma EX2 in SU(2), d = 4, beyond the one d = 2 field test so far. `library/sector-values.md`, 3A and 3B. Registered criteria first; adversarial backgrounds, several levels, the constant's growth with size. A WRONG here changes the main line of that attempt. | `gates/lemma-ex-<commit>.md`, `checks/gate_ex/` |
| 2 | `field-ineq-search` | independent | high | The attempt's own open gap: a gradient-based adversarial search of (5.5). Hill climbs so far reach only Ratio 1 at L = 3. | `gates/field-ineq-search-<commit>.md`, `checks/gate_fi/` |
| 3 | `independent-core` | independent | high | First outside gate on this attempt. In order: Lemma 4.5k (TREE), Lemma 4.5j, (EI) and (TAIL) in tree form, the rough sets, Text 4.8 with (CUT) item 1, Text 4.1 to 4.4 and Theorem 5.5. | `gates/independent-core-<commit>.md`, `checks/gate_ic/` |
| 4 | `theorem-z-repaired` | mapped | high | Gate the repair in `library/quiet-boundary-rarity.md`: Theorem Z, Lemma OC, Lemma ST, the exploration, Step 5. Check each defect of `gates/theorem-z-3b7fd4e57.md` was actually repaired. | `gates/theorem-z-repaired-<commit>.md`, `checks/gate_tz/` |
| 5 | `closure` | mapped | high | Gate H(k) implies H(k + 1) in `library/one-step-closure.md`, with Prop DS, (SRC), (LIFT-I) of `library/sector-values.md`. | `gates/closure-<commit>.md`, `checks/gate_cl/` |
| 6 | `interface-independent`, `interface-mapped` | that side | high | One item per attempt. Set what the attempt delivers beside what the upper chain consumes, statement by statement: Text 6 against UV-CT and UV-OS, or UV-LOC-R and the clauses of `parts/upper-chain.md` Prop 8.1, Text 14 and Text 22. Read statements only. Report mismatches only. | `gates/interface-<side>-<commit>.md` |
| 7 | `excess` | mapped | max | Item 1 returned no WRONG. Prove Lemma EX, Lemma EX2 and (COMP)(ii), racing the running push, from a statement frozen at your commit. Start from `gates/lemma-ex-7c12c6981.md`: Lemma EX2 has to be rewritten for its D1 to D3, and no field with topological charge at small flux has been tested. | `parts/hard-core--excess.md`, `library/` |
| 8 | `fill` | mapped | done, Codex | (F2) as stated, T to C_a T: proof in `library/fill-cubical-extension.md`, not yet read by an independent reader. Same-threshold (EXT=) stays a gap, and Theorem Z and Lemma OW ask for it. | `parts/hard-core--fill.md` |
| 8a | `fill-cubical` | mapped | high | Gate `library/fill-cubical-extension.md`: Lemmas H, E, G, C, Theorem S, F2-mult, the frozen-brick clause, and whether (EXT=) is what Theorem Z and Lemma OW need given Text 5.9 of the mapped file. | `gates/fill-cubical-<commit>.md`, `checks/gate_fc/` |
| 8b | `history-budget` | neutral | high | Gate `library/generated-observable-history.md` (Theorem GH, sections 7, 8) and `library/history-budget-sum.md` (Lemma HS): does the sum really close with the honest bottom and every source, and is (FLOW-END) something each attempt can deliver? | `gates/history-budget-<commit>.md`, `checks/gate_hb/` |
| 8c | `repair-gate` | mapped | high | Gate the Codex repairs: `library/excess-finite-range-repair.md`, `library/excess-root-frame-repair.md`, and the counterexample and half-unit shift in `library/paid-inputs-frozen-energy.md`, `library/paid-inputs-frozen-mesh.md`. | `gates/repair-gate-<commit>.md`, `checks/gate_rg/` |
| 8d | `rc-far` | mapped | max | Deliver (RC-size), (RC-far) and (MC) of `parts/upper-chain.md`, section The interface, on this map, with the rate condition (PAIR), which forces more than c_* < c_I (the lead forwards the rest): the far-difference bound for the actual current of Lemma 14.16 under its law E^r, with the stated rate margins, and the midpoint completion on a finite torus. Try to kill it first. | `parts/hard-core--rc-far.md`, `checks/rc_far/` |
| 8e | `nt2-gate` | neutral | high | Gate `parts/witness.md` Text 8: the statement of NT2, (NT2-C), the attacks L1 to L3, the dilation mixture, the restricted Theorem 4.3 and (COV8), and whether `library/witness-running-tests.md` holds. | `gates/nt2-gate-<commit>.md`, `checks/gate_nt2/` |
| 8f | `nt2-rewrite` | neutral | max | Absorb `gates/nt2-gate-2285befef.md` into `parts/witness.md`: a chart-free vertex clause in place of |K_vert(tau_*)| >= kappa_*, the coherence of L3 as that gate restates it, and what rejects which law. Then work the near-far criterion NT1-NF of Text 8.6 on: its strict Wilson inequality from named interface clauses. | `parts/witness.md`, `checks/witness/` |
| 9 | `fourth-form` | neutral | done | Done by Codex: `gates/fourth-form-codex-b4de676b7.md`. | |
| 10 | `upper-chain` | neutral | max, Codex on the MacBook | Start from `gates/fourth-form-codex-b4de676b7.md`. Take over the parked part. Absorb the entry "TO THE UPPER CHAIN" in the mapped file's Requests, since the definition of quiet changed. Absorb what the interface gates report against the consumer: `gates/interface-mapped-e7d0c6976.md` D1 to D3, D5 to D7, D10(c), and `gates/interface-independent-fcbb20f83.md` D6, D7, D9. Write I(k; D) in `library/induction-with-boundary-data.md`, then the marked form of Lemma 22.2. A session that took item 9 does not take this. | `parts/upper-chain.md` |
| 11 | `witness` | neutral | done for now, Codex | NT2 stated in Text 8.1, attacked in 8.2, compared with Jaffe-Witten in 8.3; Theorem 4.1 and a restricted 4.3 proved as implications. Next: (COV8)/(G0), (TV-P), the lift norm closure, the tree limits. | `parts/witness.md` |
| 12 | `rank-u` | neutral | done | Codex report: the limit clause of (RANK-U) is false, with a bounded staggered sequence, confirmed numerically at L = 5, 6 by `checks/gate_ranku/`. Theorem 3.19 needs a changed statement. NT2 in `GOAL.md` does not read it. | `parts/witness--rank-u.md` |
| 13 | `compute-inventory` | neutral | high | List every statement of the chain that rests on a machine computation, and every load-bearing step that could not be formalized as written. | `gates/compute-inventory-<commit>.md` |
| 14 | `free-value-hand` | neutral | done | a_L >= a_0 > 0 for (B-1) by hand, with the fibre correction bounded by 2^53 L^-4. Read in `gates/free-value-lead-read-28e261c17.md`. | `library/nt2-free-value-by-hand.md` |
| 15 | `hand-shelling` | independent | done | Shelling by hand for generated patterns, by an induction with an extension property. The claim for every library-good pattern stays open, and (AB) is new. | `library/shelling-by-hand.md` |
| 16 | `hand-staircase` | mapped | done | No pinch and a reflection extension by hand, C_ext absolute, given the class reference. O1's other inputs stay open. Read in `gates/staircase-lead-read-28e261c17.md`. | `library/staircase-by-hand.md` |
| 17 | `hand-upper` | neutral | done | Gruss, Prekopa-Leindler, marginal convexity and Poincare rebuilt; the nest objection written by hand, c <= 284/L at flat walls. Same-model, not gated. The Helffer-Sjostrand form and Bochner sign stay cited. | `library/upper-chain-by-hand.md` |
| 18 | `hand-witness` | neutral | high, finishing, then deferred | From the Witness section of the same report: prove Lemma 3.6 without the symbolic run, write Lemma RM's Stieltjes and density inputs, and apply (H21) of `library/nt2-free-value-by-hand.md` to the order of b and L in Corollary NT1-F. Leave the free value to `free-value-hand`. | `library/witness-by-hand.md` |
| 19 | `compute-inventory-2` | neutral | done | One more statement rests on a run, and four more steps can't be formalized as written. | `gates/compute-inventory-2-28e261c17.md` |
| 20 | `hand-upper-2` | neutral | deferred until a hard-core attempt closes | From the Upper chain section of `gates/compute-inventory-2-28e261c17.md`: write the F20.1 signed-activity example with rational weights by hand, or keep only the missing-denominator objection, and prove Theorem 4's massive Green limit with a stated order of limits. | `library/upper-chain-by-hand-2.md` |
| 21 | `energy-gate` | mapped | done | Six requested statements CORRECT-NO-ADVANCE; (LIFT-1) and the local fine-energy claim WRONG by hand counterexamples; own-level bookkeeping, (4.2) algebra and the small-cube charge ADVANCE. | `gates/energy-stages-codex-b87de884f.md` |
| 23 | `upper-hand-gate` | neutral | done | ADVANCE on the rebuilt inequalities and Theorem N, after a sign repair in Lemma M; the claimed application after eliminating the middle variable lacks a mixed-block bound. | `gates/upper-hand-codex-f3aa2a8c5.md` |
| 24 | `shell-end` | mapped | done | FALL needs only (UP), by way of (WAM) or (E-SHELL). Open: (GLUE-E), (LC). | `library/excess-shell-end.md` |
| 25 | `seam-lc` | mapped | stopped at the first step | The shell route needs (RATE-exact) at the rate nu fixed before L, so a finite A_s(L) is not enough. Needs uniform effective constants, a direct (WAM-req), or a restated order of constants. (LC) and (GLUE-E) not attempted. | `library/excess-seam.md` |
| 26 | `shell-gate` | mapped | high | Gate `library/excess-shell-end.md`, written by Codex: does (INPUT) + (UP) really give the FALL that DS reads; are (WAM) to (UP) and (E-SHELL) to (WAM) right; do the two-site and tensor tests test the right thing; does the rate condition (b_s nu_* <= 1/2) survive the mapped order of constants? Do not read the `seam-lc` output. | `gates/shell-end-<commit>.md`, `checks/gate_se` |
| 27 | `joint-induction` | mapped | done | No inequality failed in the flat limit; stops at unsupplied Theorem F-D with two or more jumps. H(k) reads nothing from the K-class, so this is two passes, not a joint induction. Colour cancellation is out of the test's reach. | `library/joint-induction-two-step.md` |
| 28 | `tail-two-step` | independent | done | Gaussian budgets consistent. (15) undecided; stop is (BANACH) step (4), the conditional normalized density. | `library/tail-two-step.md` |
| 29 | `seam-quadratic` | mapped | done | Quadratic (LC) survives, unchecked. Nonlinear (NL-pay) undecided at (PATCH). | `library/seam-quadratic.md` |
| 30 | `lift-repair` | mapped | done | (LIFT-1) replaced, ES:65 replaced, restoration built. Stops at ES:88: a heavy frozen wall gives the stage no output, by a hand example. | `library/lift-nonlinear.md` |
| 31 | `tail-two-step-c` | independent | done | No counterexample. Contraction fails as written at D1 (block-scale quadratic remainder), plus D2 to D4. Repairs unproved. | `library/tail-two-step-c.md` |
| 32 | `explicit-region` | neutral | high, first | Read `library/heavy-wall.md` and `library/seam-nlpay.md` first: their stops, (HW) and (PATCH), are both fine energy that coarse data cannot see. Test whether an explicit region prices that energy, on those two examples. Both attempts drop multiscale state (no regions or histories). Is that costing more than it saves? Using Dimock's open papers (arXiv 1108.1335, 1212.5562) and any open Balaban abstracts, rebuilt not cited, write one two-step example of an induction that carries explicit large-field regions with their conditional partition functions and a finite set of localized insertions, for SU(2). Say which of these it avoids and which it keeps: boundary-data induction, generated-current K3, across-sector locality, weighted upper bound. Do not read the Sussman-Alpoge repository, or the proofs in either attempt's part files; read only GOAL.md, the interface in `parts/upper-chain.md`, and statements you need. Label memory as memory. | `library/explicit-region-two-step.md` |
| 33 | `seam-quadratic-c` | mapped | high, first | Same test as `seam-quadratic`, blind: do not read `library/seam-quadratic.md`. Read `library/excess-shell-end.md` Section 4.2 and `library/excess-seam.md`. Derive quadratic (LC) in four dimensions at the flat background, with a transverse mode crossing a block face, nested scales and the actual composite constraint, tracking L and depth. Report A_s, r and M_* with their L-dependence and whether (RATE-exact) holds at nu fixed before L. A counterexample stops this gluing, not (WAM). | `library/seam-quadratic-c.md` |
| 34 | `fd-jumps` | mapped | done, Codex | Missing supplier confirmed. Flat inf-sup and the commutator show no automatic depth loss. Stops at (UE), a uniform simultaneous block-average extension, open already at flat nested walls. | `library/fd-jumps.md` |
| 39 | `ue-multilevel` | mapped | done, Codex | Flat raw input bounded at fixed L, not uniformly in L (ratio at least about L^2); cross terms gain a negative power of L. No actual lift, so (UE) stays open. Stops at (WP), one frequency on planar walls. | `library/ue-multilevel.md` |
| 42 | `fd-local` | mapped | Codex, laptop | Decide several-jump F-D by localizing to one-wall patches, avoiding (UE). | `library/fd-local.md` |
| 35 | `heavy-wall` | mapped | done, Codex | Example confirmed with corrections: it defeats ES Section 3's layer selection, not (4.2) or (AE-R). Stops at (HW). J(L) is harmless to K before L, conditionally. | `library/heavy-wall.md` |
| 38 | `hw-fine` | mapped | done, Codex | Universal local fine-removal lemma REFUTED by a hand example with two antipodal constrained minima. (HW) and (PATCH) themselves are not refuted. | `library/hw-fine.md` |
| 40 | `hw-thick` | mapped | Codex, Mini | Decide (HW) on its real domain: try the antipodal frustration in a thick cleared collar with a triggered core. | `library/hw-thick.md` |
| 41 | `pos-beta` | independent | Codex, Mini | Decide the block-scale quadratic remainder, D1 of `library/tail-two-step-c.md`. | `library/pos-beta.md` |
| 36 | `cond-norm` | independent | done, Codex | Stopped at (CN), which implies (15). Quadratic insertion, whitening and two connected orders are written; the all-order sum with cuts is not. | `library/conditional-normalization.md` |
| 37 | `cn-tree` | independent | done, Codex | Forest identity, positivity and a cut-safe tree bound written, and the volume factor is gone. No Gaussian edge carries a factor g. Stops at (BC2), strictly smaller than (CN). | `library/cn-tree.md` |
| 22 | `hand-ab` | independent | done | Literal (AB) stays open. A replacement route on graph balls gives the Morrey estimate with hand proofs, conditional on two consumer bounds in (5.1). Same provider read: none yet. | `library/adapted-domains.md` |

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

## Keeping the two attempts independent

- **Independent side.** Read `parts/hard-core--independent.md`, `parts/hard-core--independent--good.md` and `parts/hard-core--independent--ct.md` if present, its library files (`lattice_gehring_hls`, `lattice_sobolev_box_gauge`, `path_expansion_locality`, `ultralocal_cluster_expansion`), the statements of the upper chain's clauses and `GOAL.md`. The upper chain's audit tables, Obligations and Requests quote the mapped attempt, so leave them out. Do not read the mapped file, any other file in `library/`, gates on the mapped attempt, the Sussman-Alpoge repository or any other AI-written account of a Yang-Mills proof. This also holds for gates on this side, so that their reports can go back to the attempt.
  A worker that can reach forbidden files will sometimes read them by accident, so a worker on this side gets a filtered copy with no git history where the machine allows it.
- **Mapped side.** Read the mapped file, `library/` (not `gates/history-budget-*`, `gates/compute-inventory-*` or `gates/strategy-*`, which read both attempts; the lead forwards extracts), and the Sussman-Alpoge repository at `c854ad8b3a42`, credited. It is unvetted and carries no weight until proved here. Do not read `parts/hard-core--independent.md`, gates on it, `library/shelling-by-hand.md`, `library/adapted-domains.md`, `library/tail-two-step*.md`, `library/mixed-coefficient*.md`, `library/conditional-normalization.md`, `library/cn-tree.md` or `library/pos-beta.md`.
- **Neutral.** Read either attempt's statements. Carry no proof text from one to the other.

## Working efficiently

Measured on the pushes so far: a resumed push carries about 300,000 to 580,000 tokens of context on every step, and 70 to 90 percent of its active time is the model generating text. A fresh, narrow session avoids most of that: the first fresh gate wrote 195,000 tokens for about $8 at API rates, where a resumed push wrote 202,000 for about $219.

- **Hardest first.** Owner, 2026-11-01: go after the hard statements first, to save grinding on the easy base. Work goes to the statement the proof is most likely to die on. A routine hand rebuild, or an elementary citation, waits until a hard-core attempt closes, unless it could be hiding a real gap.
- **One item, one session.** Stop when the item is done. Do not continue into the next item or tidy up other files.
- **Do not read whole files.** Part files are 145 to 350 KB, and the folder holds about 1.6 MB of text. Find the statement with `grep -n`, then read the statement, its proof and what it cites.
- **Try to kill it first.** A short computation with pass and fail criteria written first can save a long argument. Report what a run can and cannot establish. A search that finds nothing does not prove a bound.
- **Save as you go.** Write your report section by section. A reader that dies at the output limit with nothing saved is a total loss.
- **Keep reports short.** At most ten defects, ranked by what each breaks. If a defect breaks the consumer's statement, say so and stop unless the rest is independent of it. Give a repair if you see one, marked as unproved.
- **No subagents** unless the item needs a separate reader. Each one is a full extra cost.

## Rules

- **Write only** your output file, `library/` for a new lemma, and your `checks/` folder. Evidence for another file's owner goes in your report, and the lead forwards it, respecting the firewall above.
- **Gate reports** open with provenance: model, effort, commit, and that a same-model check is not independent in model and is not an audit. Then a verdict table per statement, then numbered defects with the concrete failure, then what was and was not read. ADVANCE: the proof stands at the level of its steps, and any defect is local with a repair in hand. CORRECT-NO-ADVANCE: no counterexample to the conclusion, but a step fails as written or the statement adds nothing yet, so nothing downstream may rest on it. WRONG: false as written. Verdicts steer research and grant no status.
- **Label honestly**: gap, unchecked, implication, discharged. A step recalled from memory but not proved is a gap. A truthful gap is never penalized.
- **Literature.** Use open sources for method, and rebuild any lemma you need in `library/` with credit. Stop at a bot check, sign-in or paywall. Never pay for anything, never commit a PDF, and do not paste long passages.
- **No computer-assisted steps.** See the section of that name in `GOAL.md`. A run can refute or guide, never discharge. If a statement you need rests on a computed value, label it gap and look for a hand proof.
- **Numerics.** One job per machine, under `python3 scripts/lab_ops.py numeric-lock`. Confirm the acquire succeeded before running, and do not pipe it through `tail`. Set BLAS threads to 1, use `nice`, and have the script stop itself above 2 GB RSS. On the Mac mini, start a numeric job only at 50 percent memory free or more, and never use a process pool.
- **Never** edit axioms, audit files or ledgers, run an audit, push to main, or post anything public.
- **Ask the owner only** about axiom edits, public posts, spending and pace. A scientific fork gets probes.

## Prompt for a new worker

```text
Work on PR #10132 of jonathonreilly/qubit-lattice-axiom-framework, branch claude/ym4d-hard-route. Read .claude/science/physics-loops/ym4d-hard-route-20261030/FINISH.md and GOAL.md in that folder. Take the first free item in the queue, follow its rules, finish that item only, push it, and stop with a short result: verdicts or what was proved, and what is still open.
```
