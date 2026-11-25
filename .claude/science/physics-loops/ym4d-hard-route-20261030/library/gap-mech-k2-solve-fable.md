lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-26T09:12Z

# Row 1542, gap-mech-k2-solve-fable: solve brief on the (K-II) step

Pinned commit 1813043e8, branch claude/ym4d-hard-route. Started 2026-11-25T21:12Z (date -u). Worker: Claude Fable 5.2,
reasoning effort high, Mac mini worker 1. No subagents. Status of everything below: unchecked by a second
party unless a check is named.

## 0. Plan (written first, per the save protocol)

1. Read the rule sections of FINISH.md and GOAL.md, the seed statement (gap-k2-tool-design-fable.md 3.1),
   and the results of rows 1528 to 1541 and 1468 to 1500 (RESULT parts first, bodies where needed).
2. State precisely what a (K-II) step must deliver, and what is on file about why each tried step fails.
3. Choose one attack, write it as lemmas with proofs or with the exact failing line.
4. Registry greps (open-core.md, FINISH rows) before any statement is called new.
5. End with the exact stopping statement, its non-equivalence to the seed, its selectivity, and a RESULT line.

## Status log

- 2026-11-25T21:12Z: file created, plan written. Nothing read yet beyond the queue row.
- 21:12Z: read FINISH rule sections (L1-84, L299-360), GOAL.md, queue row 1542, RESULT parts of rows 1528-1541.
- 21:12Z: read RESULT parts of rows 1468-1500 (the earlier K-II tool attempt, checkpoint 1496, check 1497).
- 21:19Z: read gap-k2-tool-design-fable.md 3.1, 4.3-4.5 (seed, (K2-STEP), GA, filter). First candidate under test: the 2+2 split (4D gauge theory as a 2D gauged sigma model on B with target the 2D connections on A), compared with 2D O(4) by a Durhuus-Froehlich type inequality. Registry grep next.
- 21:19Z: the 2+2 candidate is ON FILE: sheets / transverse lattice (rows 1103-1114, GH2, P4, BR-2; prior/gap-gauged-sigma-read-luna.md Section 4), worst-case layer comparison refuted (rows 1139-1140). Not pursued as new. Reading Theorem T (row 1332) for the rate budget.
- 21:26Z: read the digest of the two 2D O(N) proofs (prior/gap-2don-proofs-read-opus.md Step 6, B(1)-B(6)). Blind candidates on file: relative form bound along beta = route B1 / (LEV_K) (rows 669, 708, 1517); MK sandwich = row 1025. Reading Theorem T 4.4 in full for the rate budget (A2)-(A3).
- 21:30Z: read Theorem T 4.4 (row 1332). Note: in the K-II form the seed needs no rate (l is free); a rate is needed only in Theorem T because of (A1). Next: keyword counts for the remaining blind candidates, then Lemma CEN / CEN+ statements.
- 21:33Z: frame decoupling (Proposition LOC 1, gap-invent-selective-max.md L197), twist eaters and the beta^(-3/2) toron count are ON FILE. Found a possible unrecorded combination: row 1108's (MON-L) / BR-2 with the anchor rate pi against Theorem T's budget (A3) (row 1332 is later than row 1108). Reading row 1108's definitions.

## 1. Repo search and reading record

Read in this session (at commit 1813043e8): FINISH.md L1-84 and L299-360 (rules); GOAL.md; queue row 1542;
the RESULT text of rows 1468-1500 and 1528-1541 (rows 1531, 1534, 1538, 1539, 1541 had no RESULT yet);
`library/gap-k2-tool-design-fable.md` 3.1 and 4.3-4.5; `library/gap-shrink-box-fable.md` 4.4 (Theorem T);
`library/prior/gap-2don-proofs-read-opus.md` Step 6, B(1)-B(6); the RESULT text of rows 1105-1114, 1139,
1140, 1332; `library/gap-br2-direction-fable.md` headings and L188-191.

Search method: one shell loop of `grep -l -i -F` file counts over `library/gap-*.md`,
`library/prior/gap-*.md` and `parts/gap.md` for about 50 key words, then the hits opened. No cross-branch
fetch was run in this session (the brief limits reading to this checkout); the cross-branch state is as
recorded by rows 1468 (Section 9) and 1529.

Numeric jobs: none. `memory_pressure` showed 34 percent free at 21:34Z, below the 50 percent rule. All work
below is by hand.

## 2. Blind candidates and where each one is on file

I derived each candidate before searching. Every one is on file. None is claimed as new.

| # | Blind candidate | On file at | State there |
|---|---|---|---|
| 1 | Split Z^4 = A x B (two planes). The links along A at a site b of B are a "spin" in the space of plane connections; the links along B are a gauge field with group G^A. So the theory is a two-dimensional gauged model on B, and with the B-links frozen and the A-plaquettes off it is one free 2D O(4) model per A-link. Compare the 4D theory with these sheets. | Model W(beta_L, beta_M, beta_T) on Z^2 x Z^2, route BR-2: `gap-bridge-exercise-opus.md` L380 (row 1072); `gap-br2-direction-fable.md` S7 L35, D1 L48 (row 1108); first cases GH2, P4 (rows 1109-1114); literature `prior/gap-gauged-sigma-read-luna.md` Section 4 (transverse lattice) | (MON-L) and (FACE-SG) open, no mechanism; first cases stopped (rows 1109, 1110; checks 1113, 1114) |
| 2 | "Gauging disorders": a Durhuus-Froehlich layer comparison, used twice | rows 1139-1140 (`gap-frameless-2d-astra.md`) | worst-case form refuted (a background orders the frameless layer above b_* >= 4.0e3); typical-background form open |
| 3 | A relative form bound: the level velocity along beta is at most K times the level gap | route B1 `gap-skeleton-max.md` L104 (row 669); (LEV_K) `gap-mid-max.md` L138 (row 708); row 1517 | the wall in the coupling variable; equivalent kind |
| 4 | Two-sided Migdal-Kadanoff bounds for the sixteen masses | (TB)_n `gap-cr-tomboulis-max.md` L38 (row 1025; check 1029) | errors are extensive; one open inequality (TB)_n |
| 5 | Port the one-annulus engine of the posted 2D O(n) proof (vanishing twist cost from a commutator identity) | `prior/gap-2don-proofs-read-opus.md` B(5) L153; row 1011 (`gap-pinned-cell-gauge-max.md` 4.3 Lemma CEN L263); row 1529 | no continuous twist on gauge-invariant data; fails |
| 6 | Use Haar translations of links by fixed Lie-algebra fields as the change of variables of that engine. After the gauge average the colour frames at different sites are independent, so two-site brackets average to zero | Proposition LOC 1, `gap-invent-selective-max.md` L197 (row 1013); second-order Schwinger-Dyson with bracket, row 1011 Proposition W | gain zero |
| 7 | The twist ratio as a running coupling: a single-plane centre twist has a zero-action flat connection (anticommuting holonomies), so Z^z/Z^0 is a power of beta at one loop, not an exponential | "twist eater" in 24 files, "toron" in 68 files of the lane; Proposition TW of row 1533; Proposition J of row 1179 | the flux half only; proved bounds favour U(1) (row 1533) |
| 8 | No continuous non-abelian symmetry acts on gauge-invariant data (higher-form symmetries are abelian; the centre is Z_2), so no twist engine of the 2D kind exists | `gap-crux-fp.md` L88 (per my notes of row 1011; "1-form" occurs in 36 files) | reading, on file |

Reading of the table (mine): candidates 1, 2 are one route (sheets). Candidates 5, 6, 8 are one fact (no
frame). Candidates 3, 4 are the wall in two variables. Candidate 7 is the flux half.
- 21:35Z: Sections 1-2 written (reading record; table of eight blind candidates, all on file).
- 21:37Z: read gap-sing-direction-fable.md 4.2-4.3 (row 1115): the face is stiffer than the anchor at guide grade (one-loop stiffness about 2.7 b at beta_T = 2.4), so its rate is far outside Theorem T's budget (A3); my candidate remark that Theorem T's slack reopens Way B of row 1108 is REFUTED at guide grade by row 1115. Next: the thin twisted torus base (row 669 B14, gap-ac-lat.md).
