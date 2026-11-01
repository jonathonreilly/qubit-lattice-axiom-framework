# Finishing the proof: instructions for workers

Written by the target lead on 2026-10-31. `GOAL.md` holds the target and the definition of non-trivial, and it wins over this file and over the charters. The charters' interface wording, UV-EXT, is superseded. This is research-stage working state, and nothing here grants status.

## Where it stands

**Existence is not proved.** Both hard-core attempts report few gaps, but most of what they label derived has been read only by the same push or by its own readers:

| File | gap | unchecked | implication | Last read from outside |
|---|---|---|---|---|
| `parts/hard-core--independent.md` | 1 | 1 | 29 | Gates at `16ca92dd7` and, cross-provider, `independent-2c-codex-b4de676b7`: the cancellation at the saddle stands, (GOOD) is WRONG as displayed, and (TAIL), (R1), (R2) and the wall count do not yet close; counts here predate them |
| `parts/hard-core--mapped.md` | 3 | 0 | 58 | Gates at `60036ba4d`, `7c12c6981` and, cross-provider, `theorem-dm-codex-892504e4c`: Theorem DM, (Z), Lemmas CC and OW CORRECT-NO-ADVANCE, with the free-bond count of DM on the wrong region; counts here predate them |
| `parts/upper-chain.md` | 6 | 1 | 19 | Cross-provider gate `fourth-form-codex-b4de676b7`: Lemmas 20.3, 22.1, 22.2 and Prop 20.4 ADVANCE; Lemma 20.5 and Theorem 14.1c CORRECT-NO-ADVANCE. Codex is working on these as item 10 |
| `parts/witness.md` | 5 | 3 | 10 | Gate at `3b7fd4e57`, which changed the definition of NT2 |

`lab_ops.py status` counts 44 open obligations, but it leaves out both attempt files, so it understates what is open.

**What limits progress.** Each gate so far has changed the route, so a statement labelled derived is not yet safe to build on. The pushes have moved far past the last read. The cheapest useful work now is to try to break load-bearing statements, in fresh sessions, before more text is built on them.

## What finishing means

1. One hard-core attempt has all its obligations discharged, and it delivers an interface statement the upper chain reads as written.
2. The upper chain's conditional theorems lose their conditions.
3. NT1 and NT2 hold, as `parts/witness.md` states them.
4. One clean document holds the whole chain, followed by a line-by-line independent review of it, then the owner's approval of the exact text. Balaban and Dimock are credited by name. Until then there is no public claim.

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
| 9 | `fourth-form` | neutral | done | Done by Codex: `gates/fourth-form-codex-b4de676b7.md`. | |
| 10 | `upper-chain` | neutral | max, Codex on the MacBook | Start from `gates/fourth-form-codex-b4de676b7.md`. Take over the parked part. Absorb the entry "TO THE UPPER CHAIN" in the mapped file's Requests, since the definition of quiet changed. Absorb what the interface gates report against the consumer: `gates/interface-mapped-e7d0c6976.md` D1 to D3, D5 to D7, D10(c), and `gates/interface-independent-fcbb20f83.md` D6, D7, D9. Write I(k; D) in `library/induction-with-boundary-data.md`, then the marked form of Lemma 22.2. A session that took item 9 does not take this. | `parts/upper-chain.md` |
| 11 | `witness` | neutral | max | Take over the parked part. Absorb `parts/witness--rank-u.md`: the limit clause of (RANK-U) is false. State NT2 exactly, try to break its running clause with the laws L1 to L3, and compare with the primary Jaffe-Witten text. | `parts/witness.md` |
| 12 | `rank-u` | neutral | done | Codex report: the limit clause of (RANK-U) is false, with a bounded staggered sequence, confirmed numerically at L = 5, 6 by `checks/gate_ranku/`. Theorem 3.19 needs a changed statement. NT2 in `GOAL.md` does not read it. | `parts/witness--rank-u.md` |

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

- **Independent side.** Read `parts/hard-core--independent.md`, `parts/hard-core--independent--good.md` if present, its library files (`lattice_gehring_hls`, `lattice_sobolev_box_gauge`, `path_expansion_locality`, `ultralocal_cluster_expansion`), the statements of the upper chain's clauses and `GOAL.md`. The upper chain's audit tables, Obligations and Requests quote the mapped attempt, so leave them out. Do not read the mapped file, any other file in `library/`, gates on the mapped attempt, the Sussman-Alpoge repository or any other AI-written account of a Yang-Mills proof. This also holds for gates on this side, so that their reports can go back to the attempt.
- **Mapped side.** Read the mapped file, `library/`, and the Sussman-Alpoge repository at `c854ad8b3a42`, credited. It is unvetted and carries no weight until proved here. Do not read `parts/hard-core--independent.md` or gates on it.
- **Neutral.** Read either attempt's statements. Carry no proof text from one to the other.

## Working efficiently

Measured on the pushes so far: a resumed push carries about 300,000 to 580,000 tokens of context on every step, and 70 to 90 percent of its active time is the model generating text. A fresh, narrow session avoids most of that: the first fresh gate wrote 195,000 tokens for about $8 at API rates, where a resumed push wrote 202,000 for about $219.

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
- **Numerics.** One job per machine, under `python3 scripts/lab_ops.py numeric-lock`. Confirm the acquire succeeded before running, and do not pipe it through `tail`. Set BLAS threads to 1, use `nice`, and have the script stop itself above 2 GB RSS. On the Mac mini, start a numeric job only at 50 percent memory free or more, and never use a process pool.
- **Never** edit axioms, audit files or ledgers, run an audit, push to main, or post anything public.
- **Ask the owner only** about axiom edits, public posts, spending and pace. A scientific fork gets probes.

## Prompt for a new worker

```text
Work on PR #10132 of jonathonreilly/qubit-lattice-axiom-framework, branch claude/ym4d-hard-route. Read .claude/science/physics-loops/ym4d-hard-route-20261030/FINISH.md and GOAL.md in that folder. Take the first free item in the queue, follow its rules, finish that item only, push it, and stop with a short result: verdicts or what was proved, and what is still open.
```
