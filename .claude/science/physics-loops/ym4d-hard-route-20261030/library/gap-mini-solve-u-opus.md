lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:20Z

# gap-mini-solve-u-opus: SU(2) Yang-Mills mass gap, an attempt from the crux

Queue row 1233 of `FINISH.md`. Started 2026-11-20T07:20Z (date -u) at commit 398892bd4 on branch claude/ym4d-hard-route.
Model: Claude Opus 5.5, max effort, Mac mini worker 3. No subagents.

Labels used: PROVED (a complete written argument here or a cited rebuilt lemma), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation, never a proof step), OPEN.

## Status log

- 2026-11-20T07:20Z: file created; reading FINISH.md, parts/gap.md, library/prior/gap-onebound-read-sol.md and the RESULT lines of earlier gap rows.
- 07:25Z: read GOAL.md, FINISH.md (rules, rows 1215-1238), parts/gap.md L1-104 (state of attack), library/prior/gap-onebound-read-sol.md (row 1218, whole). Record at this pin: modulo the account's constructive premises and the ultraviolet hypothesis (UNIV-K), the gap clause reduces to (N-phys) (row 1179 Theorem BP, check 1183; row 1225 Theorem E-N, check 1232 HOLDS AFTER CORRECTION). Every crux row since 1188 ends "mass gap NOT proved, nothing disproved".
- 07:45Z: also read row 1225 Sections 2-5 (`library/gap-mini-solve-r-fable.md`: the six structure families valid at every coupling, each with a failure on file), row 924 Steps 1-3 (`library/gap-univk-opus.md`: (UNIV-K) is a rate of approach to the continuum limit of a two-torus free-energy defect; the account's universality theorem compares one horizon only, CA R1), the RESULT lines of rows 778-801 (vortex commutator word, Tomboulis, Kanazawa) and 1025-1029 (decimation line; (TB)_n open for SU(2)), and the obligations list of `parts/gap.md`.
- 08:05Z: read row 1007 (`library/prior/gap-2don-proofs-read-opus.md`, Steps 4-8: the two 2D O(N) proofs and their 4D analogues) and row 924 Steps 4-8 (the open parts of (UNIV-K)). Next: Section 2 (judgement), then the chosen attack.

## 1. Orientation (read, not re-derived)

What a proof of the Jaffe-Witten gap needs, by the record (each item cited; none re-proved here):

- Modulo the account's constructive premises (the T0 chain), the gap clause on the account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1225 Theorem E-N; cross-provider check row 1232: HOLDS AFTER CORRECTION). (N-phys): there are a physical side L and j_0 such that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2 (row 1179, check 1183; K = 512).
- (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) and limsup_j a_j nu(beta_j) < infinity (row 1180, check 1187). Given the ultraviolet hypothesis (UNIV-K), a seed at one cutoff's window suffices (row 916 (ONE-K), check 917). (UNIV-K) is OPEN on (MAPCONV), (VAC-ID) and the large-field comparison (DENS-K) B1-B2 (row 924, check 925); its open parts compare two horizons, which the account says it does not do (row 924 R1, R13).
- So, modulo (UNIV-K), the crux is the lattice gap of Wilson SU(2) at one bare coupling in the account's window, in a thermal-trace form, with a seed side of order exp(c beta_0) lattice units (row 1225 Section 4, ARGUED from checked links).
- Published work on the same target (row 1218): A's one-scale full-thermal seed (A-B*) is stronger than (N-phys); B's weak-coupling Corollary 166 holds for the Villain U(1) theory too (row 1220 Proposition U), so it is not selective; Zeng's rate is the spectral-gap statement of row 1204. None supplies the Wilson estimate at weak coupling.

## 2. How best to attack it (judgement; ARGUED)

**The infrared crux.** Row 1225 Section 4 lists the structure families that hold at every coupling (correlation inequalities, positive duals, coupling monotonicity, exact identities, curvature and orbit geometry, the 2D bracket stiffness step), each with a cited failure. The two posted 2D O(N) proofs cross their band with inputs that pure 4D SU(2) lacks on gauge-invariant data (row 1007 A(5), B(5)):

- OpenAI's stiffness flow (O(4) sharp mass bounds, Sections 3.1-3.8) starts from a change of variables by a localized global rotation, whose cost is beta |df|^2 (their Lemma 2.1). In lattice gauge theory a localized gauge rotation costs exactly zero, and every non-central twist of pinned data is removable (rows 1013, 1016: Lemmas TWIST, CEN+). The only twists left are boundary data and the Z_2 centre.
- Ding-Huang-Yang need an N-copy loop soup (Lupu's isomorphism) and planar crossings; neither has a 4D gauge form.

Both remaining twist lines are on file: boundary-data stiffness (rows 1011-1016, 1188 PC, 1193 PC-c, 1228 P5: the twist squeezes under tiling) and the centre twist (rows 778-801, 1025-1029, 1161-1175). I also checked, by grep of `library/` and FINISH rows, the structures I had in mind outside row 1225's table: twisted small 2-tori with adiabatic continuity (row 1004 I6, row 842 Theorem S1), complex-coupling interpolation (Lee-Yang rows 1004 LYP, LYP2), the trace anomaly (row 1219), local-to-global and stochastic localization (row 971), the Z_2 x SO(3) split with conditional FKG (vortex containers, rows 800, 1025). Each is on file with a failing step. I do not screen further: row 998 9.5 names another screening by this model family as waste.

**Verdict of this step.** I see no route to (N-phys) in this session, and I say so before any work. The honest use of the session is one bounded question on the crux with a definite answer, proved or refuted by hand.

**Choice (made in Section 3 after one more read).** Candidates: (i) (UNIV-K) (ultraviolet, needs the account text outside this checkout, and its open parts are a multi-session cross-horizon project; not chosen); (ii) a rigorous no-go for a whole class of infrared tools that the record holds only as ARGUED.

## 3. The chosen work: does the complete account's chapter 9 supply (UNIV-K)? (started 08:20Z)

**Why this item (FINISH "Is it worth doing?").** Moves: the gap path's open list. Beyond the account's premises, the gap clause has two open inputs: the one-cutoff seed (infrared, no route, Section 2) and (UNIV-K) (ultraviolet; row 916 (ONE-K) turns a seed at one cutoff's window into (N-phys) given (UNIV-K)). Row 924 read (UNIV-K) against an older single file of the account (YM4_1400.tex at 2bc0658f91d2), whose comparison section "does not compare different horizons" (row 924 R1). The complete account at 31a47c543775 has a chapter that compares two cutoffs: the uniqueness theorem `9.8:thm-uniqueness-theorem` and its inputs, a last-lattice comparison "geometric in n, with no floor" (`9.10:thm-last-lattice-comparison`), and `9.12:lem-defect-summability` ("proved implications in the tuned-family setting", `library/chain-ca.md` D11). No lane file maps (UNIV-K) onto these (grep of every file that names UNIV-K, 08:15Z: none cites chapter 9). If chapter 9 supplies (UNIV-K) as an implication from statements already on the T0 chain, then (UNIV-K) stops being a separate open item, and the gap side reduces to the one-cutoff seed plus T0. If it does not, the exact mismatch is the missing statement. Either way the lead learns what the ultraviolet half of the gap path costs. Kind: a port-map reading with proofs of the joining lemmas; not an attack on any account statement (rule 0a: the D-items of `library/chain-ca.md` 2.4 belong to the T0 chain and are not attacked here).

Plan: (3a) fetch CA-III into a new scratch folder and read the statements of 9.12-9.13 and the conclusion of 9.8; (3b) write (UNIV-K) and each candidate statement side by side, with quantifiers; (3c) prove the joining lemma or state the mismatch; (3d) record the standing of every account input used.
