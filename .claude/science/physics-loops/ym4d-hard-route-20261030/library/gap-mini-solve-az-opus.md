lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:52Z

# gap-mini-solve-az-opus: the SU(2) four-dimensional mass gap (FINISH row 1310)

Started 2026-11-20T17:52Z (date -u) at commit 6d4a6f177 on branch claude/ym4d-hard-route, Mac mini Claude worker 2.
Research-stage working state; nothing here is a public claim. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Record read (statements about the record, not evidence; written 17:56Z by date -u)

Read at pin 6d4a6f177: `GOAL.md` in full; `FINISH.md` L1-100, L299-352 and the rows 1299-1315 (L1380-1396, with their
RESULT lines); `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; Steps 0-2 and 5-6 of
the sibling row 1313 (`gap-mini-solve-ba-opus.md`) and Step 0 of row 1314 (`gap-mini-solve-bb-opus.md`) as they stand at
this pin; Steps 0-1 and 6-7 of row 1309 (`gap-mini-solve-ay-opus.md`); Step 5 of row 1299 (`gap-mini-solve-aw-opus.md`).

What the record fixes (pointers, not evidence):
1. Modulo the ultraviolet carry and the continuum datum, the gap clause reads one lattice input at one physical size,
   uniformly in the cutoff: (N-phys) of row 1161 (row 1218 digest, display (N)); its fixed-coupling forms are the seed.
   Rows 1296, 1299, 1300, 1302, 1309, 1313 find no route to the seed off the record; rows 1301-1308 worked the owner's
   tiling and positivity directions on it and closed them as routes (checks 1305, 1306, 1308, 1312).
2. Published work (row 1218, rows 1295/1311): paper A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha
   Roy) proves a conditional ascent from a one-scale thermal window (A-B*) to a full transfer gap; (A-B*) implies
   (N-phys) (row 1295 Corollary AU2, held by check 1311). Paper B's Corollary 166 is a weak-coupling bound for coarse
   straight-path variables; row 1220 found it carries no gap information. Neither supplies the seed at weak coupling.
3. The one-cutoff carry (rows 1256-1309) is reduced to named inputs. Open after rows 1299, 1309, 1313: the outline's
   premises (row 1313 reduces (P3)-(P4); (P1), (P2), (P5) stay), the margin reading (M), (V9), and in the account's
   OUTSTANDING `9.1:prop-blind-site-expansions` (CA-III L16559, T0 node F56): the reading (H-par'), the (P) part for
   stores younger than the shell, and clause (c)'s second alternative (row 1309 Step 6.2).

## Step 1. How best to attack it (judgement, ARGUED; written 17:56Z by date -u)

**The seed.** A rough count (GUIDE, physical glueball numbers, not a proof step) shows what (N-phys) asks at a window
coupling: with m a about 1 and K = 512, the neutral excited trace on an n^3 cube at time n/K is about
n^3 (m a K / (2 pi n))^(3/2) e^(-m a n/K), which is below 1/2 only for n of order 10^4. So the seed is a statement about
a lattice of side about 10^4 at order-one coupling: the lattice mass gap itself, with its count. The record holds about
45 route families to it, each at its first failing step, and row 998 9.5 calls another screen by this model family a
waste. I name no route off the record, so I do not attack it, and nothing below is progress on it.

**The item.** The two open clauses that row 1309 left in `9.1:prop-blind-site-expansions` (Sussman and Alpoge, CA-III
L16559, Proof outstanding in their account; hypothesis (e) of `9.1:thm-last-lattice-comparison`, CA-III L17912, which
the one-cutoff carry reads; T0 node F56 of `library/chain-ca.md` L208):
- (Y) the (P) part for blind stores younger than the shell. The account's (d3) sends this case to "the class
  assignment of stored terms in the relative expansion at the preparatory integrations" (CA-III L15576-15579), which
  row 1309 could not locate by name. This could hide a real gap in the account, so it goes first.
- (H) the reading (H-par'): a fourth-class unit may keep its island slots in its read set while its localisation
  domain is its active domain.
Rule 0a: `grep -n -i "younger than the shell\|(H-par')\|class assignment\|blind-site\|island-blind"
library/open-core.md` gives nothing; in `FINISH.md` the first three strings occur only in row 1309 (L1390), which is
finished and lists them as OPEN. Row 1313 owns (P3)-(P4); row 1314 had no item at this pin.

Moves: T0 node F56 and hypothesis (e) of Theorem 9.1 on the carry. Success: the (P) part for young stores PROVED or
located as proved text, and (H-par') PROVED from the account's definitions, so that F56 becomes an implication from the
account's own plain site statements. Failure: the exact clause of the account that a young store or an island slot
breaks, which would be a real gap in their outstanding proposition. Neither outcome changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 2: fetch CA-II and CA-III at 31a47c543775 into a new scratch folder; read (d3) and its surroundings
  (CA-III L15540-15600), the preparatory integrations and the relative expansion where stored terms get their class,
  and the (P) site statement the account cites.
- Step 3: the young-store (P) case: proof from the located text, or the failing clause.
- Step 4: (H-par') from the account's T-site definitions (localisation datum versus read set).
- Step 5: labels, what a checker should redo, RESULT.

