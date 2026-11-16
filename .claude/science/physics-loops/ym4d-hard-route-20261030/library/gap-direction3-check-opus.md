lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T03:03Z

# Check of row 1051 (`gap-direction3-max`), same provider

Row 1056 of `FINISH.md`. Written by Claude Opus 5.5 at max effort on Mac mini worker 3, from commit 2f317758f, started 2026-11-16T15:03Z. The file checked, `library/gap-direction3-max.md`, was written by Claude Fable 5.2 max (row 1051). Same provider, so this is not an independent check in the sense of the working rules: where I re-derive a statement I say whether my derivation follows a different path. No subagents. No commit, no push. Research-stage working state; no mass gap is claimed.

Brief (row 1056): follow section 7.1 of the checked file exactly; check line by line (i) Lemma RM, (RM-fr), Corollary RM-TREE and its one-cell form (5.1) with the four numbered readings; (ii) Proposition PIN with (P2), (P4), Lemma SF-D (a)-(c) and the count (5.2); (iii) the two stop verdicts and the ranking of 4.2; (iv) the claim of 5.3 that the four blind statements are open for SU(2) inside the band, the taxonomy sentence, and Lemma K4. Decide whether '(N1) in its sign form fails in the mean' is proved for frame TREE as stated and for no other frame, and whether the count of 5.2 is an argument about one form of inequality only. Verdicts HOLDS, HOLDS AFTER CORRECTION (with the text), FAILS (with the first failing line). No new attack.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read the checked file in full; copy here the exact instructions of its section 7.1 (reading list, tests (a)-(e), controls, kill tests) and the statements under check, with line numbers.
2. Check (i): Lemma RM, (RM-fr), Corollary RM-TREE, the one-cell form (5.1) and its four numbered readings, line by line, with my own derivation.
3. Check (ii): Proposition PIN with (P2), (P4); Lemma SF-D (a)-(c); the count (5.2), and whether it is about one form of inequality only.
4. Check (iii): the two stop verdicts and the ranking of 4.2, against the rows and checks they cite.
5. Check (iv): the claim of 5.3 (the four blind statements open for SU(2) inside the band), the taxonomy sentence, Lemma K4.
6. Tests first by hand (a)-(e), the controls and the kill tests of 7.1.
7. The two decisions the brief asks for; the verdict table.
8. RESULT line.

## 1. What is checked, with anchors (step 1; done 2026-11-16 15:04Z by `date -u`)

The checked file `library/gap-direction3-max.md` (row 1051) has 819 lines at 2f317758f; I read all of it. Anchors below are its lines.

| Item | Lines | Mark claimed by row 1051 |
|---|---|---|
| Lemma RM (i)-(iii), proof | L320-336 | PROVED |
| (RM-fr), setting of the ring law | L338-349 | PROVED given Lemma GR+ (row 1046 6.1) |
| Corollary RM-TREE, proof, one-cell form | L351-364 | PROVED given Lemma GR+ |
| The four numbered readings | L366-391 | 1: PROVED for cells of side 1 at pin 1, ARGUED otherwise; 2-4 readings |
| Proposition PIN, (P2), (P4), abelian-pin remark | L399-420 | PROVED |
| Lemma SF-D (a)-(c), twist values | L422-442 | PROVED |
| The count (5.2), the one-sentence reason | L444-468 | ARGUED |
| Ranking 4.2 and the two stop verdicts (lines A and G) | L274-297, L280, L286, L389-391, L465-468 | ARGUED |
| The four blind statements, taxonomy sentence, U(1) and Z_2 lines, seven attempts | L470-527 | OPEN / ARGUED / PROVED as marked in 8.2 |
| Lemma K4 and its reading | L529-551 | PROVED (statement 't Hooft's) |

Section 7.1 of the checked file (L616-638), which the brief says to follow exactly:

- Reading list: row 1046 `gap-o2-extension.md` 2.1 (TAN), 6.1 (GR+); row 1016 `gap-global-reform-max.md` 7.1-7.2 (Identity AV, Theorem BH); row 1013 `gap-invent-selective-max.md` 4.1 (WN), 5.1 (JEN) with the gpt-6-astra check items 12-17; row 1011 `gap-pinned-cell-gauge-max.md` 3.1-3.2 (Proposition A); row 1038 for the frame TREE.
- Tests first, by hand: (a) RM on one link with weight exp(beta t) and S_eps a left translation must read E[t] = (beta/3) E[1 - t^2]; (b) RM-TREE on one plaquette with one tree link; (c) (P2) at a pin of one plaquette against Lemma TAN's force formula; (d) SF-D (b) on the slab with L = 2, T = 1 at first order in beta; (e) the count at b = 2 against OpenAI's Lemma 3.2 (row 1007 L133).
- Controls: compact U(1): RM, PIN (B_F = 0) and SF-D hold word for word and give no gain; the count must return OpenAI's log N at b = 2. Frozen groups: RM and PIN have no content.
- Kill tests: Theorem D2 and Lemma SHEET do not bind an identity in the law of one model (say so or refute); Lemma PT: every statement of Section 5 reads one factor; the four-test spec check on the proposal "rank the blind half first".
- Decide: whether "(N1) in its sign form fails in the mean" is proved for frame TREE as stated and for no other frame; whether the count in 5.2 is an argument about one form of inequality only.

Registry grep (rule 0a): this row attacks nothing; it checks. No open lemma is attacked here, so the grep is not needed for an attack; I still note that row 1057 (`gap-direction3-check-astra`) checks the same file in parallel and I do not read it.

## Status

Step 1 done 2026-11-16 15:04Z (`date -u`). Step 2 (check (i)) next.
