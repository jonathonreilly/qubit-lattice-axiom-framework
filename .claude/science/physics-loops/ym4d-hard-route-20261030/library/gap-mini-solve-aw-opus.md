lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:33Z

# gap-mini-solve-aw-opus: mass gap for 4D SU(2) Yang-Mills (row 1299)

Started 2026-11-20T16:33Z (date -u). Worker: Mac mini Claude worker 2, Claude Opus 5.5 max. Pinned at commit 30dae6625 on branch claude/ym4d-hard-route.

Status labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T16:40Z by date -u)

Read at pin 30dae6625: `GOAL.md` in full; `FINISH.md` L1-90, L299-357 and this row (L1380); the RESULT segments of rows
1250-1304; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; Steps 0-1 and 4-5 of
`library/gap-mini-solve-at-opus.md` (row 1294); Step 1 of `library/gap-mini-solve-av-opus.md` (row 1296, running);
row 1259's Lemma CD and Corollaries CD1-CD2 (`library/gap-mini-solve-ah-opus.md` L95-170); row 1268's statement of
(E0)-(E6) (`library/gap-mini-solve-al-opus.md`, located by grep).

What the record fixes (pointers only):
1. Modulo the ultraviolet carry, the gap clause reads one lattice input at one physical size, (N-phys) (row 1161), or a
   seed at one coupling in the window: a uniform cube gap plus the count (TR) (rows 720, 1259). Every engine on file is
   blind; the one selective proved fact, asymptotic freedom at small coupling, has no carrier through the band
   (`parts/gap.md`, "Hardest open obligation"). Rows 1277-1294 all leave the seed OPEN; rows 1301-1304 (running) work
   the owner's tiling and positivity directions on it.
2. The one-cutoff carry on the pin route (rows 1256-1294, mostly Mac mini worker 2) is reduced to named inputs. Open at
   this pin (row 1294 Step 5, check 1288): (CE) and the margin reading (M); the cut half (E0)-(E6) of (FC-1);
   `9.1:prop-blind-site-expansions` (Proof outstanding in the account, CA-III L16558-16560); (V9) and (DET)'s
   normalisation (row 1296 holds (V9), running); the account's premises; the seed.
3. Balaban's CMP 116 is not in the owner's paper folder and Project Euclid gives a bot check (rows 1264, 1294). Row
   1294 Step 5 notes that the account prints its own expansion machine with one-term bounds and holomorphy for the
   large-field stages (CA-I 4.22, L80618-80700; 4.24, L108354-108610) and cites CMP 116 only for the regular step
   (CA-I L58700-58760), and that applying the printed machine to the regular step "is possible in principle ... but was
   not checked here".
4. Published work (row 1218): Bhattacharjee et al.'s thermal ascent is conditional on its own one-scale seed; their
   Corollary 166 is a blind weak-coupling statement on coarse straight-path variables; Zeng's routes are conditional.
   None supplies the seed.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T16:41Z by date -u)

**The seed.** Modulo the carry, the problem is a lattice statement at order-one coupling (SU(2) Wilson near
beta = 2.4, correlation length a few lattice spacings) on a box of many correlation lengths: a uniform cube gap plus
the count (TR). Any proof needs a selective step at order-one coupling that fails for compact U(1), the free photon,
products with a massless factor and frozen finite groups (`parts/gap.md`, test table). The candidates I could name
before reading the tables (sharpness via OSSS, Ginibre/character positivity, centre-vortex comparison with Z_2,
analyticity in beta, Lee-Yang, chessboard Peierls for disorder, uniform gap implies (TR) via additivity of excitation
energies, Langevin/Bakry-Emery on the orbit space, valley tilings) are on file with a first failing step (rows 998,
1084, 1229, 1237, 1259, 1273-1292, and the screen of row 1296 Step 1). Rows 1301-1304 work the owner's tiling and
positivity directions now. Row 998 9.5 rules another screen by this model family a waste. Verdict: no route to the
seed off the record; I do not attack it, and nothing below counts as progress on it.

**What I do instead.** Only closures count. The unowned carry input that sources on hand can decide is the regular
(all-small-field) step's expansion: (CE) of row 1294 (the input of Proposition HAN, hence of Theorem PE and Corollary
FC-s, the smooth half) and (E0)-(E5) of row 1268 (the input of Theorem FCT', the cut half). Both are read today
against Balaban's CMP 116, which this machine cannot read. Row 1294 Step 5 notes that the account prints its own
expansion machine, with one-term bounds and parameter holomorphy, for the large-field stages, and that applying it to
the regular step "was not checked". Rule 0a: `(CE)` occurs in FINISH.md only in row 1294; no row holds this item;
row 1296 holds (V9) and (DET), which I do not touch.

Moves: the one-cutoff carry on the pin route (rows 1256-1294). Success: (CE) and (E1)-(E3) become readings of the
account's printed and proved statements (no CMP 116), and the carry's list loses its CMP 116 dependence in the smooth
half and, if (E0), (E4), (E5) also close, in the cut half. Failure: the exact clause of the printed machine that does
not cover the regular step. Neither changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 2: read the printed machine (CA-I 4.22 L80178-80239 and L80618-80700; 4.24 L108354-108610) and the regular step
  (4.3, L4073-4210; L58700-58760; L8778-8781). Record what each statement assumes and proves, with its index status.
- Step 3: decide whether the regular step is a case of the printed machine (large-field set empty, no arrested
  components). Prove the reduction or name the clause that fails.
- Step 4: (E0), (E4), (E5) of row 1268 against the same text; then (CE) as row 1294 6.5 states it, including the
  threshold eps_0 and its dependence on the floor (row 1294 6.5 "Robustness").
- Step 5: labels, state of the carry, what a checker should redo, RESULT.
