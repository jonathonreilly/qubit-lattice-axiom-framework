lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T17:05Z

# gap-mech-direction-fable (row 1380): direction for the mechanism programme

Status: IN PROGRESS. Worker pinned at commit 95f5d4e1a, branch claude/ym4d-hard-route. No commit, no push (relay copies).
Started 2026-11-22T05:05Z (date -u).

## 0. Plan and status log

Plan (written before any derivation):

1. Read the rules (FINISH.md rule sections, GOAL.md), row 1378 (the switch), row 1379's output
   `library/prior/gap-mech-lit-luna.md`, the target statement (M-neutral) of row 1367 with the chain 1342, 1349,
   1356, 1359 and the lead notes after Theorem ZD-c in `library/gap-phys-seed.md`.
2. Read the prior work the row names: rows 1009-1018, 1021 (pinned-cell port, open items (N1)-(N3)), checks 1014,
   1015, rows 1139, 1140.
3. Section 2: the live mechanisms, each with first exact statement, non-equivalence to the seed, U(1) test.
4. Section 3: pick one; first lemma, what it reads, which chain statement consumes it.
5. Section 4: attack on that lemma.
6. Section 5: the next three rows with decisive outcomes.
7. RESULT line.

Status log (each line stamped by date -u in the command that wrote it):

- 2026-11-22T05:05Z file created; reading rules next.

- 05:05Z read: FINISH.md L1-84 and L299-351 (rules, incl. 'Equivalent is not progress'), GOAL.md, rows 1378-1380, `library/prior/gap-mech-lit-luna.md` in full, `library/gap-seed-astra62.md` L1-60 ((M-neutral)), `library/gap-phys-seed.md` L296-330 (ZD, ZD-c, lead notes). Next: rows 1009-1021, 1139, 1140.
- 05:14Z read: RESULT parts of rows 1009-1018, 1021, 1139, 1140; `library/gap-pinned-cell-gauge-max.md` Section 7 (L438-512, (N1)-(N3)); `parts/gap.md` L4-104 (state of attack, methods 19-36, lead rules CL and W2). Section 1 written next.

## 1. Inputs read, the target, and the constraints a mechanism must meet

Credits. The target form and its chain are the lane's: Theorem ZD-c (row 720, `gap-phys-seed.md` L311), (N-phys)
(rows 1161, 1342, 1349), (M-neutral) (Claude Fable row 1356, check 1359; stated in gpt-6.2-astra's row 1367,
`gap-seed-astra62.md` L9-L13). The 2D sources are OpenAI's O(4) and O(3) papers (github.com/openai/math, read in rows
1007, 1009, 1010, 1379) and Ding, Huang and Yang, arXiv:2611.04908 (rows 1006, 1379). The existence chain is Balaban's
and Sussman and Alpoge's (with Claude and Codex as authors of their text). Nothing below is checked by another model.

### 1.1 The target, as read

(M-neutral), `gap-seed-astra62.md` L11: on the prescribed trajectory fix one physical side L, n_j = L/a_j, 4 | n_j,
beta_0 <= beta_j <= B_0 log n_j. In the range of P_0 (zero spatial twist, average over the eight electric centre
translations), with transfer eigenvalues lambda_0 > lambda_1 >= ..., put s(t) = sum over a >= 1 of
(lambda_a/lambda_0)^t. Wanted: some L with s(2 w_j) <= 4/21 at every late cutoff, w_j = floor(n_j/1024).
In words: the neutral thermal trace of the cube of side L at the physical temperature 512/L is the vacuum term up to
4/21. Consumers: rows 1356/1359 (rank-one test), 1342/1349 ((N-phys), then (G_ev-phys), then the matched gap clause
given (P1)-(P4), (H2), (TOT)).

### 1.2 What the record says a mechanism must be (rows 1378, 998, 1011-1021, 1139-1140)

- (S) Selective: no gain for compact U(1) in four dimensions at weak coupling; a gain for SU(2).
- (T) Typical: it reads the Wilson law of the background, not a supremum over pins, tilts or coupling fields
  (Proposition B' and Theorem BH of rows 1011/1016; Theorem D2 row 977; Lemma SHEET row 996; row 1139 far above the
  window).
- (NE) Not equivalent to the seed or to (W) (rule of 2026-11-22).
- The direct port of the 2D engine fails at the twist: SU(2) has the bracket but no non-gauge symmetric continuous
  twist (Lemma CEN+ of row 1016, with the scope corrections of its astra check); compact U(1) has the twist and no
  bracket. The repair (N1)-(N3) needs a colour frame, which exists only above the band.
- The 2D proofs cross their band with an inequality valid at EVERY coupling (rows 1009, 1010). Neither 2D proof
  replaces the supremum by a typical field in the gain step itself (row 1379 (a)); Ding-Huang-Yang is typical in an
  auxiliary environment and selective through the extra intensity N - 2 (row 1379 (b)).

- 05:23Z grep of 46 mechanism terms over the gap files (all on file except 'charge-2'); read results of rows 1141, 1171, 1175, 1177, 1197, 1244; `prior/gap-2don-proofs-read-opus.md` L118-156 (OpenAI's one-annulus engine); `gap-invent-selective-max.md` L99-150 (C1-C8, Lemma WN). Next: kill verdict on C1 and the astra check items 12-17.
- 05:33Z read: C1's kill verdict (`gap-invent-selective-max.md` L152-232) and astra check items 11-18 (`gap-invent-selective-check-astra.md` L50-75): C1 and C2 are open again, the fourth-order family identity was never written. Checked 14 more terms (remnant symmetry, Coulomb confinement: rows 1041, 1045, 1141 and `gap-mini-solve-x-opus.md` L52 hold the frame readings). Next: where the seed chain stopped (rows 1375-1377).
