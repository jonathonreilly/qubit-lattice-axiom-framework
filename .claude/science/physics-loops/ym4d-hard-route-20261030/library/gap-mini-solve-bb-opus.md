lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:30Z

# gap-mini-solve-bb-opus: the SU(2) mass gap, attack by the Mac mini worker 3

Queue row 1314 of `FINISH.md`, pinned at commit 44ea76b9f on branch `claude/ym4d-hard-route`. Started 2026-11-20T17:30Z.

Labels used: PROVED (a complete written argument, checkable by hand), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## Status log

- 17:30Z: file created (save protocol). Reading FINISH.md, the earlier RESULT lines, `parts/gap.md`, and `library/prior/gap-onebound-read-sol.md`.

## Step 0. Record read (statements about the record, not evidence; 17:40Z by date -u)

Read: GOAL.md (all), FINISH.md L1-85 and L299-352 (rules, joining, efficiency), the RESULT lines of rows 1290-1313,
`parts/gap.md` L1-104 (state of attack) and L223-268 (route registry), `library/prior/gap-onebound-read-sol.md` (all;
row 1218's reading of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A), the four-author
Hexagon text (B), and Zeng (C)), and the plan of the concurrent row 1309 (`gap-mini-solve-ay-opus.md` Step 1).

Where the lane stands, as the record says it (not re-proved here):
- Given the account's premises (Sussman and Alpoge, with Claude and Codex as authors of their text, after Balaban),
  the Jaffe-Witten gap on the account's tr F^2 sector follows from (N-phys) alone (row 1225 Theorem E-N, built on row
  916 Theorem E, check 917, and row 1179 Theorem BP, check 1183). (N-phys) is a neutral-sector thermal trace bound on
  one physical spatial cube, uniform in the cutoff (row 1218 reading, display (N)).
- (A-B*) of paper A implies (N-phys) (row 1218 reason 1; row 1295 Corollary AU2).
- The carry from one coupling to finer cutoffs has its own open inputs (rows 1256-1309); concurrent rows 1309, 1310,
  1313 work there. Row 1309 attacks the account's `9.1:prop-blind-site-expansions`.
- The seed itself is the infrared problem: every route on file stops at an order-one-coupling estimate (row 998 6b;
  rows 1225, 1229, 1291, 1300). Row 998 9.5 lists what not to repeat.

## Step 1. How best to attack it (judgement, ARGUED; 18:05Z by date -u)

**The seed.** The Jaffe-Witten gap needs, beside the account's existence chain, one infrared statement: (N-phys), or
(A-B*), at one physical size. Along the trajectory this is the lattice gap of Wilson SU(2) on a box a few tens of
correlation lengths wide, at a coupling where the running coupling is of order one. I see no reduction of it. Every
selective fact I can name (asymptotic freedom, the so(3) bracket, the Z_2 centre, pi_3, the O'Neill curvature of the
orbit space) either is perturbative or acts through the running coupling, and the 2D mechanisms (OpenAI's annulus
twist bound, Ding-Huang-Yang's third loop-soup copy, row 1007) use a continuous global symmetry on the integration
variables, which 4D gauge theory lacks: a colour rotation of pinned data is a bulk gauge transformation and costs
nothing (row 1013 Lemma TWIST; row 1016 Lemma CEN+). Grep of FINISH.md and `library/` (18:00Z) finds each angle I
considered on file: O'Neill/orbit space (20 files), Tomboulis-Yaffe (50), Mack-Petkova (63), electric flux (77),
Luscher/van Baal (80), Bakry-Emery (95), (BDD-Delta)/(Z-UNB) (rows 720, 1031-1056, 1135). Row 998 9.5 calls another
screen by this model family a waste. So I do not screen the seed again. Nothing in this file is progress on the seed.

**The item.** `9.10:thm-last-lattice-comparison` of Sussman and Alpoge's complete account (CA-III L63225; "Stated;
proof incomplete at the step marked (*)"; open registry L38, owner none; chain-ca D10). Why:
- It is on the gap carry: the carry reads `9.1:cor-sourced-integrals` at zero source (row 1233 R-i, Lemma 3.5;
  rows 1255-1296), whose hypotheses are those of `9.1:thm-last-lattice-comparison`, and row 1233 3c-3d names
  `9.10:thm-last-lattice-comparison` as the supply of its hypothesis (iv).
- Rule 0a: open-core.md has no entry; the open registry lists it with owner none; no FINISH row attacks it (the
  label occurs in FINISH only inside row 1233's material). Row 1309 (concurrent) attacks the other open input,
  hypothesis (e), `9.1:prop-blind-site-expansions`; this row does not touch that.
- Success: the account's last-lattice comparison becomes an implication from its PROVED statements (or the exact
  failing clause is named), so the carry's hypothesis (iv) loses its outstanding status. Failure: the exact clause of
  the marked step (*) that does not follow, with why.

**Plan (one step per response, appended before the next).**
- Step 2: fetch CA-III at 31a47c543775 into a scratch folder; read the statement, the marked step (*), its proof
  around it, and what the step needs.
- Step 3: prove the marked step from statements the account proves, or isolate the precise missing lemma.
- Step 4: consumers (9.1 hypothesis (iv)) and labels; RESULT.

## Step 2. Correction to Step 1: the 9.10 statement is not on the gap carry (READ; 18:20Z by date -u)

Source: CA-III = `theorem_0_complete_account_raw_III.tex` of Sussman and Alpoge's complete account at 31a47c543775
(Claude and Codex as authors of its text; after Balaban), fetched by URL into a scratch folder outside the repository
(111,583 lines). L-numbers are TeX lines of that file.

- `9.10:thm-last-lattice-comparison` (L63225-63351) is the "geometric" form: rate rho^(n-w) "with no floor". Its
  step (*) is that eleven listed statements also hold "read on the hatted array" (L63230-63255). Its proof applies
  `9.10:lem-objective-test-rest` and `9.10:lem-load-envelope` (itself incomplete at one step) on the hatted array.
- It is cited only inside 9.10: its two corollaries (L63353-63418) and `9.10:thm-exponential-rate` (L63536-63700),
  the exponential rate for the renormalised-coupling family (grep of CA-III for the label: L63354, 63378, 63384,
  63417, 63578, 63582, 63589, 63655, 63691; nothing outside L63225-63700).
- The gap carry reads `9.1:cor-sourced-integrals` (L18136-18215; row 1233 R-i, Lemma 3.5), whose hypotheses are those
  of `9.1:thm-last-lattice-comparison` (L17912-17990): (a) standing hypotheses, (b) the four chapter-9.1 lemmas,
  (c) g at most gamma_U and n at least n_1, (d) theta_chi at most rho, (e) the blind-site expansion. Its rate is
  e_w = rho^(n-w) + Pi_n (L17981-17984) with the power-law floor Pi_n, which the carry already sums (row 1233 3d
  item 3: Pi_n at most C n^(-(kappa_0-4)/2) (log n)^(c_3) with kappa_0 at least 10). No 9.10 statement enters.

So (READ): `9.10:thm-last-lattice-comparison` and its incomplete inputs (`9.10:lem-load-envelope`, clause (a) of
`9.10:thm-refiled-lipschitz`) are off the gap carry; they serve the account's geometric rate. Row 1233's phrase
"hypothesis (iv) ... supplied by 9.10" (its 3b-3c) should be read with this in mind; its 3d already uses 9.1. Step 1's
item is withdrawn. The carry's only chapter-9 outstanding input stays (e), which row 1309 works on.
