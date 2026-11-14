lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T18:25Z

# gap-lsivac-max (FINISH row 941): (LSI-vac) / (HC-vac) for the SU(2) vacuum slice law on one box

Author: Claude Fable 5.2 max, Mac mini worker 2. Pinned at commit f529763f2, branch `claude/ym4d-hard-route`.
Research-stage working state. Nothing here is a public claim. No statement below is checked by another model yet (check row 943).

Status words: PROVED, CONDITIONAL (on named inputs), GUIDE (a run or heuristic; refutes or guides only), OPEN.

## Plan (at most eight steps; one step per response; each step is appended before the next starts)

0. Read: FINISH/GOAL (done), `library/gap-direction-max.md` in full, `library/prior/gap-lit-hcvac.md`, `library/gap-etohc-opus.md`, check row 938, row 936 (CUT-TYP). Duplicate check against `library/open-core.md` and the FINISH rows. Write the exact target and what is already covered.
1. Fix the objects: the vacuum slice law nu, (LSI-vac)_alpha, (HC-vac)_alpha, Proposition HC, the numbers. Restate in one self-contained block.
2. Fact tests before any proof: U(1), frozen Q_8 and 2T, SMALL-BOX, the ceilings. Each as a statement with its computation.
3. First attack (to be fixed after Step 0).
4. Second attack.
5. Third attack.
6. If not closed: the smallest unproved inequality and one solvable-model test that could refute it.
7. RESULT line.

## Step log

### Step 0: inputs read, duplicate check, the target with the checks' corrections (written 2026-11-14T06:50Z)

**Read in full (READ = read at the pinned commit, not re-proved):** FINISH.md (opening, How we work, Working
efficiently, Rules, rows 931-943), GOAL.md, `library/gap-direction-max.md` (row 931), its check
`library/gap-direction-check-astra.md` (row 938, Codex gpt-6-astra), `library/prior/gap-lit-hcvac.md` (row 939),
`library/gap-etohc-opus.md` (row 940, Claude Opus 5.5, unchecked; check row 942 not on disk),
`library/gap-cuttyp-max.md` (row 936, unchecked).

**Duplicate check (rule 0a).** `grep -n -i -E "LSI-vac|HC-vac|SG-step|log-Sobolev|hypercontract|ground.state"` on
`library/open-core.md`: no hit. Same terms on `library/l17c.md` and `library/open-registry.md`: no hit. FINISH rows
with the terms: 931 (names the lemma), 939 (reading), 940 (the implication (E-to-HC), proved there), 941 (this
row), 943 (its check). No other row attacks (LSI-vac) or (HC-vac). I proceed. I stay off (CUT-TYP), (TYP-1),
(EVEN-PI), (OD) (row 936), (VAC-SUB) (row 934), (E-to-HC) (row 940).

**Repo search.** This clone holds only `claude/ym4d-hard-route` (row 940 records the same), so origin/main and the
PR branches are not searched here. Check 938 and row 939 ran that search for the same terms on the laptop: no
owner, nearest prior text `gap-skeleton-max.md` B11 (hypercontractivity named as a route, citation from memory).

**The target, with the corrections of check 938 and the constant of row 940.**
- Chain: P = Omega^(-1) (T/lambda_0) Omega on L^2(nu), nu = Omega^2 dU, T the Wilson transfer operator of the
  periodic spatial box B, gauge-invariant functions.
- Proposition HC (row 931; HOLDS in check 938 for integer times): (HC-vac)_alpha' gives
  X(2m + 2; B) <= 72 beta |B| e^(-2 alpha' m) for integer m >= 0.
- Seed on B = (24a)^3, a even: X(a; B) <= x_* = log(22/17) once
  alpha' (a - 2) >= log(72 beta 24^3/x_*) + 3 log a. The constant is below 16.0 at beta 2.3 and about 16.12 at 2.6
  (check 938). This is the SH seed. For the two numbers of Form W on the same box use log(20/19) for x_*: the
  constant is then about 17.61 at beta 2.3 (check 938).
- Row 940 (unchecked): (LSI-vac)_alpha and (SG-step)_sigma give (HC-vac)_alpha' with
  alpha' = (1/2) log(1 + alpha/sigma^2). So the target of this row is the pair (LSI-vac), (SG-step) on the one box,
  or (HC-vac) directly.
- Size of the claim (GUIDE, recalled lattice numbers, no proof weight): alpha' <= E_1 (Proposition HC), and E_1 is
  near 1.3 at beta 2.3 and near 0.5 at beta 2.6 (lightest glueball in lattice units). So a is at least about 20 at
  beta 2.3 and about 60 at 2.6, and the box side 24a is 500 to 1400 lattice units.

**Plan, revised after the reading (still at most eight steps).**
1. Objects in ambient form: the chain without gauge projection, the exponential-family structure of the one-step
   law, the convex function Lambda with log Omega = Lambda(beta .) - const on the slice space. Exact formulas.
2. Fact tests, before any proof: U(1), frozen Q_8 and 2T, SMALL-BOX, ceilings, for the target and for the handles
   of Step 1.
3. Attack A: curvature (Bakry-Emery) of the slice law nu and of the mid-slice law eta, in closed form.
4. Attack B: averaged forms through Gaussian domination (no supremum over the conditioning slice).
5. Attack C: where the box size enters (two-scale or block form), if A and B leave room.
6. The smallest unproved inequality and one solvable-model test.
7. Result table and RESULT line.
