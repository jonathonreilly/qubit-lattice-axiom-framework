lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:09Z

# gap-mini-solve-ay-opus (FINISH row 1309): mass gap for 4D SU(2) Yang-Mills

Started 2026-11-20T17:09Z (date -u). Branch claude/ym4d-hard-route, pinned at 74a4c7244.
Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.


## Step 0. Record read (statements about the record, not evidence; written 17:12Z by date -u)

Read at pin 74a4c7244: `GOAL.md` in full; `FINISH.md` L1-84, L299-352 and this row (L1390); the RESULT text of rows
1296 and 1299; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` L1-126 (row 1218); Steps 0-1 and 5 of
`library/gap-mini-solve-aw-opus.md` (row 1299); `library/gap-mini-solve-ax-opus.md` (row 1300, Step 0 only at this pin).
Sources fetched by URL into a scratch folder outside the repository: Sussman and Alpoge's complete account CA-III and
outline `YM4_sketch_500.tex` at commit 31a47c543775.

What the record fixes (pointers, not evidence):
1. Modulo the ultraviolet carry, the gap clause reads one lattice input at order-one coupling: (N-phys) of row 1161, or a
   uniform cube gap plus the count (TR) of row 1259 at one coupling in the window. About 45 route families to it are on
   file with their first failing step (`parts/gap.md` route registry and methods 19-36; rows 1189, 1194, 1199, 1237,
   1241, 1273 tables). Rows 1296, 1299, 1300 find no route off the record; rows 1301-1308 work the owner's tiling and
   positivity directions on it now.
2. The one-cutoff carry (rows 1256-1299) is reduced to named inputs. Open after row 1299 (its Step 5.1 table): the
   outline's premises (UM1, UM4-UM6, UM14), p_1 > p_0 for (E0), (M), `9.1:prop-blind-site-expansions`, (V9), (DET),
   the seed. Row 1296 closed (DET)'s normalisation question (Lemma CONS, Proposition PN) and lists as OPEN "Theorem
   9.1's hypotheses, including the account's outstanding blind-site expansion".
3. `9.1:prop-blind-site-expansions` (CA-III L16559) is the one statement on that list that the complete account itself
   marks "Proof outstanding". It is hypothesis (e) of `9.1:thm-last-lattice-comparison` (CA-III L17912; rows 1233,
   1234, 1255), and `library/chain-ca.md` L208 lists it as F56, outstanding, on the T0 chain (core uniqueness, clause
   (v), CA-III L110798-110824 per chain-ca step 5).

## Step 1. How best to attack it (judgement, ARGUED; written 17:12Z by date -u)

**The seed.** I do not attack it. Every candidate I can name is on file at its first failing step (item 1 above), and
row 998 9.5 calls another screen by this model family a waste. Nothing below is progress on the seed.

**The item.** `9.1:prop-blind-site-expansions` (Sussman and Alpoge, CA-III L16559-16800). Why this one:
- It is OUTSTANDING in the account (index status OUTSTANDING; "Proof outstanding" at CA-III L16634). GOAL.md's method
  puts proof work on exactly such statements on the T0 chain.
- It is on the gap carry (hypothesis (e) of Theorem 9.1, which the carry of rows 1233, 1256-1299 reads).
- Rule 0a: `grep blind library/open-core.md` gives nothing; in FINISH.md the label occurs only in RESULT lines that
  list it as open (rows 1233, 1234, 1255, 1256, 1264, 1275, 1278, 1293, 1294, 1296, 1299); no row attacked it
  ("island-blind" occurs in rows 1234, 1264, 1278, 1284, 1299 only as a pointer). Row 1299 5.4 (2) names it as the
  precise next row on the carry and says its route can now start from the outline's regular-gas chapter.

Moves: T0 chain node F56 (`library/chain-ca.md` L208) and the carry's hypothesis (e) of Theorem 9.1. Success: the
account's last outstanding input of Theorem 9.1 becomes an implication from its PROVED geometry lemmas (9.1:lem-island-
geometry, 9.1:lem-blind-counts) and the site expansion statements as the account states them. Failure: the exact clause
of the site expansion whose proof reads the full tree length in a way the island-blind length cannot replace.

**Plan, one step per response, each appended before the next.**
- Step 2: read the island-blind format (CA-III L15889-16060), the two geometry lemmas (L15478, L15938), the
  proposition's route to its end (L16634-16800), and how its consumers read it (L16801-17060).
- Step 3: read the site (T) expansion statement as the account states it (cluster expansion lemma, marked sub-sum
  corollary, tolerance lemma, T-step expansion lemma (i)-(vii)) and the outline's printed regular gas (SA L13893-14811),
  and list every place where a tree length enters.
- Step 4: prove the (T) part: each place in the list, with d replaced by d°, from the geometry lemmas.
- Step 5: the (L) and (P) parts the same way, or the exact clause that fails.
- Step 6: labels, what a checker should redo, RESULT.
