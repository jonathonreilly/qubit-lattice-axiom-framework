lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T21:00Z

# Direction row 1672: the next attack after the closed Lean chain

Started 2026-11-28T09:00:53Z (date -u), pinned at commit ea82bac16. Author: Claude Fable 5.2, high effort, Mac mini worker; author only, checked by no one. Status: complete; see RESULT at the end.

## 0. Reading log

- Read in full: the row 1672 brief; GOAL.md; FINISH.md L1-L84 and L299-L358; `library/gap-direction8-fable.md` (row 1643); `lean/gapchain/GapChain/Final.lean`; `Stage0.lean` L60-L170; registry rows R10-R12, TWO-PER, VIR-DOWN, LEV-FAIL, WMIX-SLICE, ANISO-TAIL (`library/open-registry.md` L1010-L1031).
- Read as RESULT texts: FINISH rows 1643 and 1652-1671. They are pointers, not evidence. Where a section below relies on one, it names the file that I opened.
- Not yet read: the files named in later sections are added here as I open them.
- Read later: `library/lean-gap-chain-stage0-check-opus.md` 1.4 and L155-L162; `lean/gapchain/RECEIPT-final.md` (axiom reports, "Next row"); `Stage0.lean` L228-L246 and L343-L356; `library/gap-mech-direction4-fable.md` L273-L275 (the triggers of row 1553).
- Grep counts only (a count is not a reading): "Tomboulis" 46 FINISH lines, "Mack" 37, "Bakry" 30, "O(3)" 28, "finite-size criterion" 9, "Knabe" 7.
- Not read: the proofs of any Lean stage; the release sources; the files of rows 1655-1664; the account. No Lean run, no numeric run, no web search.

Labels: KERNEL (checked by the Lean kernel, rows 1670-1671), ON FILE (row), ARGUED (my judgement), GUESSED.

## 1. The state in one paragraph

KERNEL: `GapChain.Final.su2_fixed_observable_gap_of_mNeutral`. For every large odd L, at the release's witnesses (chosen once), every l with `MNeutralAll L M g0 l` gives `HasMassGap (centredOf S) ((2/l) log(2^18/5041))` and a unique vacuum. The release is the work of Sussman and Alpoge, with Claude and Codex as authors of their text, on Balaban's method. The chain has two plug-in points (ON FILE, `Final.lean`, `Stage0.lean` L228):

- `MNeutralAll L M g0 l`: the neutral rank-one test on the cube of side l L^K at beta_K, at every late K;
- `ExpClusters L K nu m` (Stage 2): exponential clustering of the lattice states at one physical rate m. A proof of clustering by any route enters here and needs no cube.

No seed is proved. The hypothesis is the whole open problem: under the standard picture it holds only for m l of about 12,000 (GUESSED: one-particle count x^(3/2) 735 exp(-x/512) below 0.16 at x = m l), so it is a statement in the deep infrared at every late cutoff.

## 2. Verdict: no proof row on the seed is worth running now

Reasons, in order of weight.

1. **No first lemma with a method exists.** ON FILE: row 1643 1.4 and 2.2 (a); rows 1655 and 1661 (two max sessions on 2026-11-28, checks 1662 and 1663: no input moved); registry rows VIR-DOWN, LEV-FAIL, WMIX-SLICE, ANISO-TAIL. Every design on file is one of four kinds (row 1643 2.2 (a)) or an instance of (K-I), and none has a first estimate.
2. **The kernel chain adds no attack.** It fixes the consumer. It does not weaken the seed (section 3, items a and b).
3. **One more blind pass is not evidence.** Rows 1386, 1442, 1496, 1529, 1542, 1553, 1597, 1610 (as row 1643 2.1 counts them), 1643, 1655 and this row used one method: write candidates, then search the folder. A repeat of one method is not an independent check. This row's pass (section 3) gave the same outcome. By check 1443 no exhaustion follows.
4. **Exact computation cannot reach the hypothesis.** KERNEL and ON FILE: at cutoffs K of 70 or more the cubes have side at least 2^70 (`Final.lean`, `hlarge`), the couplings lie above 2^2800 (row 1464, check 1467), and one cube per cutoff is needed at infinitely many cutoffs. A finite computation needs a carry in K first. The only carry on file is the block map of Lemma TW (row 1468), and no step of it is proved at order-one coupling (rows 1418-1437: ruled out by cost).

This is a stop for seed rows, not a statement that no mechanism exists.

## 3. What this row tested before the verdict

I wrote each candidate first and searched the folder second. "Read" names what I opened. "Count" means a grep count only.

| # | Candidate | Where it stands | Standing |
|---|---|---|---|
| a | Weaken the kernel hypothesis: infinitely many cutoffs, a smaller aspect, purity in place of the rank-one test | Read: check 1653 1.4 and L155. `Final.massGap_of_mNeutral` already takes the test frequently along the release's own K. A true (PUR-io) form needs a top theorem that selects the cutoff sequence again, and the converse of Lemma M1. | A Lean row with a method. It moves the consumer, not the seed. Not ranked: an engine will fix the form of the seed it supplies. |
| b | Discharge the hypothesis by an exact computation | Read: `Final.lean` (`hlarge`), rows 1418 and 1643 C4 | Out of reach in principle without a carry in K (verdict, reason 4). |
| c | The seed as thermodynamics: the entropy of the box of side l at temperature 512/l is below log(625/457); a sign for the trace anomaly | Read: row 1643 1.6 (Proposition COOL) | The (T-down) line. Stopped. |
| d | A finite-size criterion whose threshold lies in the small, weak box | Read: row 1643 2.1, candidate 1 ((STEP), (MON-L) of row 1553) | The seed in steps. No mechanism. |
| e | A port of the two-dimensional engines (the twist inequality of the O(3) and O(4) proofs) | Read: RESULT of row 1380; rows 1007 and 1009 as fragments of their RESULT texts | Closed in the lab frame (Theorem C1, check 1381). Row 1380: a gain needs dressed moves, that is, a step in the band. |
| f | Vortex comparisons: Migdal-Kadanoff bounds, the Z_2 times SO(3) split | Count: 46 and 37 FINISH lines; row 1643 2.1, candidate 4 | On file. The recursion alone is not selective. Not opened here. |
| g | Curvature of the orbit space with a Bakry-Emery bound | Count: 30 FINISH lines, among them rows 747, 968 and 1477 | On file as literature and attack rows. Not opened here. ARGUED by me only: the group curvature enters as a mass-type term (compare row 1655 4.1 with the correction of check 1662 (6)). |
| h | A proved small-volume or hot-box statement ((SV-Z), (HOT)) | Read: row 1643 2.3, "Not ranked" | It has a method. It moves no input while the band has none. |
| i | A weak-coupling carry from the release's floor 2^2800 down to the pointwise floors | Read: row 1643 C3, C4; registry R12 | Easy base. The lane's rule is hardest first. |

Outcome: no candidate is new, and none is an attack. Items f and g rest on counts; a reader who needs them must open the rows.

One correction to my own first guess. I meant to name "a proof of the weak-coupling gap of the two-dimensional O(3) model" as the trigger. That proof is on file as a reading (rows 1007 and 1009, the OpenAI papers on the O(3) and O(4) models), and its port is item e. So a new method for a simpler model is not the missing thing. The missing thing is section 4.

## 4. The one thing that would change the verdict

**(EXC) One proved estimate on the calibrated trajectory, at a fixed physical size above the account's range, that is not lattice-local, not an identity and not a negative.**

Exact form. A statement Lambda qualifies if all four clauses hold:

1. Lambda is an inequality with a sign and a size, uniform in the cutoff K, about the Wilson law at beta_K on a box of fixed physical side (or about a law that Lemma TW carries to it exactly), at a scale where the account proves nothing.
2. Lambda is false or void for weak four-dimensional compact U(1), and its proof reads the dimension (tests (g1) to (g6)).
3. Lambda is not equivalent to the seed, and the seed does not follow from Lambda by lattice-local steps alone.
4. The first estimate of the proof is written out, not named.

ON FILE: this is the first exception to Proposition NEG of row 1386 (as corrected by check 1387; row 1643 1.4 confirms that no exception exists through row 1651). It is the common form of the reopen triggers (R1) to (R12) and of (T-copy), (T-ineq), (T-dual) of row 1553 3.3. I add no trigger. I only say that this one is the gate.

Why this and not a weaker event. A new restatement, a new consumer, a new obstruction or more Lean changes no decision: the record has many of each and the verdict did not move. One instance of (EXC), however small, would show for the first time that some tool reads the non-abelian law at order-one coupling. Theorem K2 (row 1468) and the kernel chain then say what to build on it.

Where it can come from (ARGUED): a new published method, a new model generation, or a reader outside the lane. I do not expect it from one more row by the present models over the present folder.

## 5. What to run instead

1. **No direction row 10 and no seed row** until a candidate for (EXC) is on the table. This is the main saving.
2. **The gate row, run only when a candidate appears** (`gap-exc-gate`, the number is the lead's). Target: decide clauses 1 to 4 for the candidate Lambda. Model: the provider that did not write Lambda, at high effort; any machine; reading only. Decisive outcome: PASS on all four clauses with the first estimate checked line by line, then one proof row on the next estimate; or the first failing clause, filed in the registry.
3. **Standing probes (row 1643, rank (S)), with the kernel statement as the brief.** For each new model of any provider: one closed-folder solve whose target is the Lean proposition "there is l with `MNeutralAll L M g0 l`", or `ExpClusters` at one positive rate, at the release's witnesses. Give it `Stage0.lean` L60-L170, the six tests and nothing else. Release the weekly watch, row 1599. Decisive outcome: a candidate for the gate row, or a filed negative.
4. **Proof capacity goes off the band (row 1643, rank (U)); the owner chooses.** SU(N) existence or uniqueness of the limit (A1*), with the first rows that row 1643 2.3 names.

Not ranked, with the reason: the (PUR-io) top theorem in Lean (item a); a strong-coupling instance of the hypothesis (not on the path; beta_K grows); (HOT) or (SV-Z) (item h); a carry below the floor (item i); a further obstruction theorem (row 1643 2.2 (b)).

For the lead and the owner, not for a worker: the kernel theorem stands on the release of Sussman and Alpoge. Its authors are among the readers who could supply (EXC) or show it out of reach. An offer to them is an outward post under rules 0g to 0i and 6.

## 6. Labels and limits

| Statement | Label |
|---|---|
| The kernel theorem and its hypothesis | KERNEL (rows 1670, 1671); I read `Final.lean` and `Stage0.lean` L60-L170, L228-L246, L343-L356, not the proofs of the stages |
| The two plug-in points | ON FILE (`Final.lean`, `Stage0.lean` L228) |
| "m l of about 12,000" | GUESSED (a count of one-particle states; a guide, not a step) |
| Verdict of section 2 | ARGUED; a judgement over the record |
| Candidates a to e, h, i | ON FILE, read as named; f and g by count only |
| (EXC) as the gate | ARGUED; in kind ON FILE (Proposition NEG of row 1386; the triggers of rows 1442 and 1553) |
| The ranking of section 5 | ARGUED; item 4 is the owner's call |
| The seed, (EXC), the gap | OPEN |

Limits. No statement is proved here. No Lean, no numeric run, no web search. Rows 1378 to 1651 enter through row 1643's tables and the RESULT texts, which are pointers. Rows 1655 to 1664 enter through their RESULT texts only. This row is one more pass by the method of reason 3, and it has that weakness.

Credits: Balaban; Sussman and Alpoge, with Claude and Codex as authors of their text (the account and the YM4 Lean release); OpenAI (the two-dimensional O(3) and O(4) papers read in rows 1007 and 1009); the lane's rows by gpt-6.2-astra, gemini-4-neon, gpt-6-luna, Claude Opus and Claude Fable, named at each use.

Provenance: Claude Fable 5.2 (claude-fable-5-2), high effort, Mac mini worker, one session; nothing committed, pushed or posted; no other file written. Finished 2026-11-28T09:10:52Z (date -u).

RESULT: Row 1672 (Claude Fable 5.2 high; author only, unchecked; no proof, no Lean, no numeric run). Verdict: no proof row on the seed is worth running now. The kernel chain fixes the consumer at two plug-in points (`MNeutralAll`, and `ExpClusters` of Stage 2) and adds no attack; nine candidates written before searching are all on file or are not attacks; exact computation cannot reach the hypothesis without a carry in the cutoff. The one thing that would change this: (EXC), one proved estimate on the calibrated trajectory at a fixed physical size above the account's range, with a sign and a size, void for weak 4D U(1), reading the dimension, not equivalent to the seed, with its first estimate written (the first exception to Proposition NEG of row 1386). Instead: no direction row 10; a gate row only when a candidate for (EXC) appears; one closed-folder solve per new model with the Lean hypothesis as the brief, and the weekly watch; proof capacity off the band at the owner's choice. Open: the seed (M-neutral-all), (PUR-io), the gap.
