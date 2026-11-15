lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T13:45Z

# gap-unit-check-opus: line-by-line check of row 988 (`library/gap-unit-max.md`)

Queue row 991 (`FINISH.md` line 1069). Check item, no new attack. Worker: Claude Opus 5.5 max, Mac mini worker 3. Started 2026-11-15T01:45Z at pinned commit d0d88c388. Author of the checked file: Claude Fable 5.2 max (row 988). This check is a different model on the same text; it is not an independent derivation of the lane's results except where a step below is re-derived by a different argument, and each such step says so.

Marks: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of `library/gap-unit-max.md` it refers to.

## Plan (at most eight steps; one per response, each appended before the next)

1. Read `FINISH.md` rules (efficiency, build on published work) and `library/gap-unit-max.md` in full; record the exact statements to be checked with their line numbers. Grep `library/open-core.md` and FINISH rows for overlap.
2. Check Identity G (S = 0 at beta_t = 0 for every beta_s; X as a beta_t integral).
3. Check Lemma ORD (S(t; B) has a zero of order 4t at beta = 0).
4. Check Lemma FLOOR (sector form).
5. Check the consequence in 7.1.
6. Check the Schwarz form of the Route Z transport, and write out the Borel-Caratheodory step (zeta_n := Z/Z(beta = 0), zeta_n(0) = 1, log|zeta_n| <= c |beta| Vol on D' gives |log zeta_n| <= C Vol on D).
7. Verdict table, corrections, what stays open; RESULT line.

## Status

- 2026-11-15T01:45Z: Step 1 in progress.
- Step 1 written (below).

## Step 1. Sources, statements under check, overlap

**Read.** `GOAL.md` in full; `FINISH.md` lines 1-84, 299-356 (Joining, Working efficiently, Rules) and rows 988, 991, 992 (lines 1066-1070); `library/gap-unit-max.md` in full (369 lines); `library/gap-crux-restate.md` Section 1 (L29-46), 3.1 Theorem D (L90-116), 3.4 setting and Lemmas K, X, E, Theorem S (L170-201); `library/gap-hcphys-max.md` 4.2 (L131-163) for S, X, U; `library/gap-skeleton-max-b.md` L299-308 (Theorem LP, Lemma HM, Corollary 4), L347-358 (Theorem Z), L460-463 (Theorem ZB).

**Statements under check** (line numbers of `library/gap-unit-max.md`):

| Item | Lines | Claimed mark in the file |
|---|---|---|
| Identity G (a), (b) and proof | 199-209 | PROVED by hand, not checked |
| Lemma FLOOR and its use (17.04, pi, pi/2) | 174-186 | PROVED (one line) |
| Lemma ORD and proof | 286-296 | PROVED given two RECALLED facts, not checked |
| Schwarz form of the transport | 298-300 | PROVED (classical) |
| Consequence in 7.1 (zero-freeness gives (SEED)) | 302-310 | ARGUED; Borel-Caratheodory step not written |
| Borel-Caratheodory step asked by N1 | 350-352 | to be written here |

Definitions used (from `gap-crux-restate.md` Section 1 and 3.1): Z(n) = int exp(-beta A) dU on the torus with sides n = (n_1, ..., n_4), A = sum over plaquettes of (1 - (1/2) tr U_p), F = log Z; (TM): Z(n) = Tr T^(n_mu), T positive trace class with simple top eigenvalue; S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k; Phi(n) = 16 F(n^4) - F((2n)^4); Theorem D (b) proof: 1 + S(n; B_2) <= Z(n, 2n, 2n, 2n)^2 / Z((2n)^4).

**Overlap (rule 0a).** `library/open-core.md`: no line names Identity G, Lemma ORD, Lemma FLOOR, the Schwarz form or this Borel-Caratheodory step (its one hit for "Borel", L231, is Borel component-locality, unrelated). `library/l17c.md`: no hit. `FINISH.md`: these names occur only in rows 988 (the source), 991 (this row) and 992 (the reading N4, a different item). Prior uses of Borel-Caratheodory in the lane: Theorem Z step 3 (`gap-skeleton-max-b.md` L355), Theorem ZB (L463), and row 681's repair (Lemma S: a Harnack chain and Borel-Caratheodory, after its defect Z1: no bounded domain satisfies (TUBE)). Step 6 compares with these. This row is a check, not an attack, so rule 0a does not stop it.
