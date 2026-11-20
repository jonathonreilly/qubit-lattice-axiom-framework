lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:32Z

# gap-mini-solve-au-opus (row 1295): four-dimensional SU(2) Yang-Mills mass gap, plain brief

Started 2026-11-20T16:32Z (date -u) on the Mac mini Claude worker 1, branch claude/ym4d-hard-route pinned at e32c8d919.
Model: Claude Opus 5.5, max reasoning. Labels: PROVED, ARGUED, GUIDE, OPEN. Status: in progress; sections are appended as each step ends.

## Step 0: record read (2026-11-20T16:34Z, date -u)

Read at pin e32c8d919: `GOAL.md` in full; `FINISH.md` L1-84, L299-350 and this row (L1376, row 1295); rows 1301-1303 (L1382-L1384:
the owner's tiling and positivity directions, run by rows 1301-1304 elsewhere); the OPEN clauses of the RESULT lines of rows
1259-1293; `parts/gap.md` L8-51 (state of attack, at an older pin); `library/prior/gap-onebound-read-sol.md` in full (row 1218:
Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A, B); Zeng Chunping (C)); the heads of the sibling
files of rows 1294 (`gap-mini-solve-at-opus.md`, the one-cutoff carry's (H-an'), (H-tail)) and 1296 (`gap-mini-solve-av-opus.md`,
the carry's normalisation identity). `library/open-core.md` registers no gap-lane item (grep "gap", "seed", "N-phys": one
unrelated hit, L524).

State, in one paragraph. The lane reduces the Jaffe-Witten gap for Wilson SU(2) to an infrared datum at one coupling in the
crossover band ((N-phys) of row 1161; (W) of row 998; (SL)/(RR) of row 1258; A's thermal window (A-B*) is a stronger full-trace
form, row 1218) plus an ultraviolet carry to finer cutoffs built on Balaban and on Sussman and Alpoge's account. Every plain-brief
row since 1188 ends with the infrared datum OPEN and "no route off the record". Siblings now own: the carry inputs (rows 1294,
1296), tilings (1301, 1302), the positivity object (1303, 1304), the astra chain (1298).

## Step 1: how best to attack it, and the choice made here (2026-11-20T16:59Z, date -u; judgement, ARGUED)

**Repo search (rule "Repo first"; this folder only).** Before choosing, every candidate mechanism I generated was grepped
over `library/gap-*.md`, `library/prior/gap-*.md` and `parts/gap.md` (file counts in brackets). All are on file:
Tomboulis decimation [111] (its one open obligation (TB)_n gives the flux half only, row 1025 L241, row 1296 L53);
vortex free energy [42], Tomboulis-Yaffe [31], Mack-Petkova [29]; Gribov [33], Zwanziger [19], O'Neill [19], Singer [30];
Bakry-Emery [109], Ricci [59], hypercontractivity [40], log-Sobolev [90]; OSSS [8] ("needs FKG, absent for SU(2)", row 839;
A8 of row 1031 FAILS); Duminil-Copin [24], sharpness [60]; Dobrushin-Shlosman [50], complete analyticity [25]; Polchinski
[46], Bauerschmidt [42], stochastic localization [6], spectral independence [9]; Langevin [109], stochastic quantization [7];
icosahedral [41], finite subgroup [61]; Higgs [98]; instanton [43]; Kogut-Susskind [27], spin network [21], Perron-Frobenius
[30]; trace anomaly [22], interaction measure [15], (VIR-log) [22] (row 708 L166-172: the coupling-continuity route stops at
(DEF_K); row 1281 re-found it). Terms with 0 hits: "Weitzenbock", "Witten-Veneziano", "Seiler-Stamatescu", "approximate
tensorization", "ultracontract", "Menshikov", "cluster algorithm"; none of them names a route the record lacks (each is a
variant of a tool on file: Bochner [25], topological susceptibility [2], entropy factorization [2], Aizenman-Barsky [5]).

**Judgement (ARGUED).** The record reduces the gap to one datum at one coupling in the crossover band ((N-phys); (SL)/(RR)
of row 1258, `gap-mini-solve-ag-opus.md` L230-L256 and L342-L380; the published full-trace window A-B* of row 1218), plus
the ultraviolet carry. Every mechanism class I could name is on file with its failing step, or is being run now: tiling
(rows 1301, 1302), a positivity object (rows 1303, 1304), the thermal deletion chain (row 1298), the carry (rows 1294,
1296). Two quick kill tests of the chain's datum found nothing: (i) the four slab geometries of (4.1) have all sides at
least N (row 1258 L242-L246), so no thin periodic side lets a centre sector set by a boundary slice survive the slab;
(ii) a Z_2 magnetic flux carried by a boundary slice is not conserved through a slab of physical thickness in a confining
theory (it is in compact U(1), where it makes eta_* grow like beta: the datum is selective as it should be). So I do not
claim a route to the seed, and I do not attack it blind a fifteenth time.

**Choice.** One unowned item with a live consumer: the published thermal ascent of Bhattacharjee, Bhattacharya, Lockwood,
Romanov, Sessford and Singha Roy (A of row 1218): Proposition 7.57 (A-B** <=> A-B*), Theorem 7.56 (propagation of A-B* to
larger boxes) and Theorem F (full periodic transfer gap, one vacuum). Consumers: the gpt-6.2-astra chain targets A-B**
explicitly (row 1290 L425: "To use the published full thermal criterion, one needs J(1) <= y_0 V(s)/(2(96 T_0)^3)"), and
row 1224 checked A's slab route (Theorem B), not this ascent (its RESULT lists Lemmas 11.4-11.7, Theorem 11.8, App. G,
Lemma 6.2-Theorem B). Grep (`grep -l -F "7.56"`): A's Theorem 7.56 is cited in rows 1218, 1220 (`gap-mini-solve-p-fable.md` L197), 1224 (`gap-mini-solve-q-fable.md` L54, L295) and 1248 (`gap-mini-solve-ab-opus.md` L28), never checked; row 1224 L292-L295 proposes exactly this item ("(c) a check of A's full-thermal ascent (Theorem 7.56 and Theorem F)") and does not do it. Plan: (2) fetch A's
authors' copy (Zenodo 24147967, as row 1218 did) into a new scratch folder; (3) check 7.57, 7.56 and F line by line and
compare with the lane's own engine (Theorem S, `gap-crux-restate.md`); (4) the link from the chain's datum (RR) of row
1258 to A-B**, so that both chains aim at one statement; (5) verdicts, RESULT. If the ascent FAILS, the astra chain's
target changes; if it HOLDS, the lane has a second, published engine for the same datum, checked here.

