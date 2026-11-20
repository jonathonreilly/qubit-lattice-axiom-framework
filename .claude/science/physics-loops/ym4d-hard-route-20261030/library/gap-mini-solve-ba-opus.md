lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:28Z

# gap-mini-solve-ba-opus (FINISH row 1313): plain brief "prove the SU(2) mass gap"

Row 1313, queued 2026-11-20T17:27Z. Worker: Claude Opus 5.5 (max) on the Mac mini, pinned at a084d7b24 on
`claude/ym4d-hard-route`. No commit, claim or push from this machine; a relay copies this file.

Labels used: PROVED (a complete argument written here or cited with anchor), ARGUED (an argument with a named gap),
GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log

- 2026-11-20T17:28Z (date -u): file created; reading FINISH rules, GOAL.md, `parts/gap.md`, row 1218's digest.
- 2026-11-20T17:29Z (date -u): read GOAL.md in full; FINISH.md L1-84, L320-352 and this row (L1394); `parts/gap.md` L8-104;
  `library/prior/gap-onebound-read-sol.md` (row 1218) in full; RESULT lines of rows 1274-1307; Steps 0-1 of the
  sibling row 1309 (`gap-mini-solve-ay-opus.md`), which owns the account's `9.1:prop-blind-site-expansions`
  (CA-III L16559). So that item is taken; this row picks another.

## 1. Record read (pointers, not evidence)

1. The gap clause, modulo the ultraviolet carry, reads one lattice input at one physical size, uniformly in the cutoff:
   (N-phys) of row 1161 (`gap-solve9-astra62.md` L146-148; restated in row 1218's digest L38-44), equivalently a
   uniform cube gap plus the count (TR) of row 1259. Rows 1188-1300 (about 25 plain-brief rows) attacked it or its
   inputs; every route they name is on file with a first failing step.
2. Row 1218 (`prior/gap-onebound-read-sol.md`): the six-author paper A proves a conditional ascent from a one-scale
   thermal window (A-B*) / (A-B**) (L81-101) to a full transfer gap (Theorem F); row 1295 checked its lattice half
   (HOLDS). Paper B's weak-coupling Corollary 166 (L182-187) is BP(n, 1/2) for straight-path block variables on tori
   of side at most exp(2^k/(17k)); row 1220 (`gap-mini-solve-p-fable.md`) found it is the near-Haar property of long
   straight transports (an ultraviolet self-energy effect), and that B's Remark 155 says (H1) carries no gap
   information. Zeng's tunnelling package: row 1251 (`gap-mini-solve-ad-opus.md`).
3. The one-cutoff carry (rows 1256-1299) is reduced to named inputs; sibling rows own them (1309 the blind-site
   expansion).

## 2. How best to attack it (judgement, ARGUED; written 2026-11-20T17:38Z by date -u)

**Where the proof dies.** Modulo the ultraviolet carry and the continuum datum of the T0 chain, the Jaffe-Witten gap
clause reads one lattice estimate, (N-phys), at one physical size, uniformly in the cutoff (checked chain: row 1183,
`gap-neutral-chain-check-astra.md` L142). Its fixed-coupling forms (Theorem S's seed, (SL), (A-B*)) are statements
about finite but huge integrals at order-one coupling (lattice correlation length a few spacings, boxes of tens of
correlation lengths). Under the no-computation rule they need an analytic method valid at order-one coupling. None is
known: published hand gaps for SU(2) Wilson stop near beta_W = 0.36 (row 1218 digest L110-116, L175-180), and every
weak-coupling tool (Balaban's RG, B's Corollary 166) controls only ultraviolet content (row 1220). I re-derived three
quick forms of the seed before reading tables (the Renyi-2 form of (A-B**): 2 log Z(T) - log Z(2T) is the Renyi-2
entropy of the thermal state; the count (TR) as the low-temperature pressure of the confined phase; a small-volume
toron start, which fails because u E_1 <= g^(2/3)/K at small L). All three are on file (Renyi/purity in about 25
lane files; (TR) = row 1259 Lemma CD and row 1300; small-volume reduced models = rows 1285, 1287). Verdict: no route
to the seed off the record. I do not attack it, and nothing below counts as progress on it.

**What I do instead.** FINISH "Hardest first" lets a non-seed item go first only if it "could be hiding a real gap".
The one-cutoff carry's cut half now rests on Sussman and Alpoge's regular-gas chapter (row 1299 4.8, PROVED GIVEN
premises (P1)-(P5)). Two of those premises are decidable from texts on hand and could hide a real gap:
- (P4) the constant conditions (UM14), (UM19), (UM23), (UM26') "in one order of choice", together with q > p_0 of
  row 1299 4.7 (equivalently p_1 > p_0 in CA-I 4.3). If the conditions cannot be met in one order, the route through
  SA's chapter fails at that step.
- (P3) SA's structural identities (heredity, normalized functional, wall factorization, SA L14406-14412) and the
  completeness identity at complete physical pairs (SA L14262-14271), which SA states as hypotheses of its chapter.
  If no text proves them for the carry's step, the carry rests on an unproved hypothesis.
Rule 0a: `grep -n "(P4)\|(P3)" FINISH.md` and row 1299's own file name these only as open premises (row 1299 4.8);
`library/open-core.md` has no entry for them (checked in Step 3 below). Sibling rows: 1309 holds the blind-site
expansion; 1310 and 1314 had no item on the branch tip at 17:36Z.

Moves: the one-cutoff carry on the pin route (rows 1256-1299), premises (P3)-(P4) of row 1299 4.8. Success: (P4)
PROVED (an explicit order of choice) and (P3) located as proved text or reduced to a named statement; the cut half
then rests on (P1), (P2), (P5) only. Failure: the first constant condition that cannot be met, or the identity no
text proves. Neither outcome changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 3: fetch SA's outline and CA-I by URL into a scratch folder; read CA-I 4.3 (p_0, p_1) and SA's chapter
  L13893-14811 for every constant condition; record each condition with its line.
- Step 4: the order of choice (P4), or the conflict.
- Step 5: (P3): read SA L14262-14271, L14406-14412 and search the library for proofs of the identities.
- Step 6: labels, what a checker should redo, RESULT.

## 3. The exponents p_0, p_1, q in the account (READ; written 2026-11-20T17:39Z by date -u)

Sources fetched by URL into a scratch folder outside the repository: Sussman and Alpoge, `YM4_sketch_500.tex`
(32,992 lines) and `theorem_0_complete_account_raw_I.tex` (CA-I, 166,711 lines) at commit 31a47c543775.

**3.1 What CA-I fixes (READ).** CA-I Notation 2.3:not-stages-first (L1332), Stage 0 (L1345-1390):
- p_0 in N, "free upward", with floors p_0 >= 5r (CMP 119) and p_0 >= (d+5) r_0 + 8r + 3 (L1352-1353);
- p_1 "a window": "We assume that 2p_1-(d+5)r_0>p_0" (CMP 122b), **p_1 < p_0** (CMP 122a), and finitely many lower
  bounds on p_0 - p_1 by numbers at most 4r+1 (L1353-1357); the account takes **p_1 := p_0 - 4r - 1** (L1359-1363);
- **q := q_0 = q_1, free upward, with floors such as q >= p_0 + 7r + 1 and q >= 3p_0 + 3r + 1** (L1364-1366).
The same window is restated at L1866-1876 (with r_1 for r_0) and L2017-2019; Proposition 2.4:prop-order-consistent
(L2271) asserts the order can be met. The degree function is p_0(g) := A_0 (log g^(-2))^(p_0) (L1014). In CA-I 4.3
(L4167-4178) the fluctuation domain of CMP 119 (3.43) has radius C_1 p_1(g), p_1(g) = (log g^(-2))^(p_1), and the
cutoff radius is (A_1/A_0) p_0(g).

**3.2 Consequence for row 1299 4.7 (READ, deduced).** Row 1299 4.7 (`gap-mini-solve-aw-opus.md` L352) closes (E0)
"provided q > p_0 (equivalently p_1 > p_0; not checked against the account's choice of p_1 here)". In the account the
two are NOT equivalent: q > p_0 HOLDS (q >= 3p_0 + 3r + 1), and p_1 > p_0 FAILS (p_1 = p_0 - 4r - 1 < p_0, and
p_1 < p_0 is one of the account's own conditions, from CMP 122a). So the cutoff radius (A_1/A_0) p_0(g) GROWS FASTER
as g -> 0 than the fluctuation-domain radius C_1 p_1(g): their ratio is (A_1/(A_0 C_1)) (log g^(-2))^(4r+1) -> infinity.
Which inequality (E0) needs depends on what "the box" of SA's condition (C2) is: if it is the ci-form box R = l^q, (E0)
holds; if the high threshold must lie inside the fluctuation domain of radius C_1 p_1(g), the reading of 4.7 fails as
written. Next: read `library/ci-form.md` and SA L14276-14340 to decide.
