lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T13:36Z

# gap-mini-solve-i-fable (FINISH row 1199)

Research-stage working state. It grants no status. Nothing here is a public claim.

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 5e5082e7c.
No subagents. Checked by no one. File created 2026-11-20T01:36Z (`date -u`).

**The problem (row 1199).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the
sense of Jaffe and Witten. Labels used below: PROVED, ARGUED, GUIDE, OPEN.

## Plan (written before any reading of the lane files)

1. Step 0: read the lane's map (`parts/gap.md` method list and route registry, the RESULT lines of the
   mini-solve rows a to h, the two screening tables in `gap-mini-solve-b-fable.md` and
   `gap-mini-solve-e-fable.md` Step 2.1, `library/open-core.md`). Record where the lane stands.
2. Step 1: choose one named, unattempted item and say why it is not a repeat (rule 0a grep).
3. Steps 2+: attack that item, one stage per response, each stage appended here before the next.
4. End: one RESULT line.

## Step 0. Where the lane stands (statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L297-360, the row (L1280) and the RESULT lines of
rows 1179, 1180, 1184, 1187, 1188-1190, 1193-1195; `parts/gap.md` L1-104 and L213-322; the screening tables of
`gap-mini-solve-b-fable.md` (Step 2.1) and `gap-mini-solve-e-fable.md` (Step 2.1, Steps 5-6);
`gap-solve9-astra62.md` L120-175 (the form of (N-phys)).

1. **The target splits in two (Theorem BP, row 1179; check row 1183: main chain HOLDS AFTER CORRECTION).** The
   Jaffe-Witten gap clause follows from the continuum datum of the T0 chain (OPEN) and one lattice estimate,
   (N-phys) of row 1161 (OPEN): at one admissible physical side, uniformly in the cutoff, the periodic
   centre-neutral excited trace of the cube n^3 at a time u at most n/K is at most 1/2.
2. **(N-phys) in other words (rows 1180, 1184; check row 1187: main statements HOLD).** It is a neutral lattice
   gap at arbitrarily weak coupling with a bound of asymptotic-scaling type on the seed size. In thermal form:
   the cube at aspect K is on the confined side, with a dilute gas of neutral excitations.
3. **The wall (`parts/gap.md` L321-322).** One selective inequality at every scale between first passage and the
   seed size. Selective means false for a massless factor. Tests a tool must fail on: compact U(1) at weak
   coupling, the free photon, a product with a massless factor, Theorem D2, Lemma SHEET, Proposition V (the K7
   line in theorem form).
4. **Siblings.** Rows 1188-1190 and 1193-1195 (mini-solve a to f) each screened routes from first principles
   and found every one on the lane's map (about 65 route families in all, tables in rows 1189, 1190, 1194).
   Each then worked one item to a first failing step. Rows 1197, 1198, 1200-1202 (g, h, j, k, l) have no
   result at this pin.
5. **Consequence for this row.** I do not screen route families again. Step 1 below records only the candidates
   that are not in those three tables, each with its grep. Then one item is attacked.
