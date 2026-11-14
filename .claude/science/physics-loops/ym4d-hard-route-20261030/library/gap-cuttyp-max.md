lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T17:34Z

# gap-cuttyp-max (queue row 936): the typical-environment cut gap (CUT-TYP)

Author: Claude Fable 5.2, max effort, on the Mac mini worker, pinned at commit 933258061.
Proof item on the crux (flux half). Research-stage working state. Nothing here grants status.
Labels used on every statement: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric, never a proof step), OPEN.
"READ" means read at the pinned commit and not re-proved here.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read the inputs in full: `library/gap-oddgap-max.md` Sections 6-7 (row 930) and the check
   `library/gap-oddgap-check-astra.md` (row 933). Duplicate check for (CUT-TYP) and (LSI-weak) in
   `library/open-core.md` and the FINISH rows. Fix notation.
2. STEP 1 of the row, part a: write (CUT-TYP) as an odd Poincare constant of the cut links in a quenched
   environment; identify the model exactly (which links, which couplings, which symmetry survives).
3. STEP 1 of the row, part b: the effective 2D coupling at 4D beta 2.3-2.6; comparison with the 2D O(4) / SU(2)
   principal chiral gap (implied by, implies, independent); is the environment in a regime with a known convergent
   expansion. Literature check on the placement.
4. STEP 2 of the row, attack 1: Ward identity for the whole-cut rotation with an environment defect; name the
   exact step where U(1) fails.
5. STEP 2, attack 2: two-scale argument (rotation mode against local modes) and disorder-averaged second moments.
6. STEP 2, attack 3: concentration over environments for the e^(-cN) rate.
7. STEP 3 of the row: the smallest unproved inequality, one solvable-model test that could refute it, and a
   precise (LSI-weak) with a verdict on which is easier. A GUIDE run only if memory allows.
8. Result section and the RESULT line.

## Log

- 2026-11-14T05:34Z: file created before any reading of the inputs. No earlier run of this item exists at the pinned
  commit (`library/gap-cuttyp*` did not exist).
- 2026-11-14T05:50Z: step 1 written (Section 1).

## 1. Inputs read, duplicate check, notation (step 1)

**Read in full (READ):** `library/gap-oddgap-max.md` lines 1-100 and 323-620 (Sections 4-7 of row 930, Claude
Fable 5.2 max); `library/gap-oddgap-check-astra.md` (row 933, Codex gpt-6-astra xhigh, 502 lines, reconstructed by
the lead from the event log; its header says one small edit after the logged read is not recorded).

**Duplicate check (rule 0a).** `grep -n -i "CUT-TYP\|LSI-weak\|cut gap\|chiral" library/open-core.md`: no hit.
In `FINISH.md` the terms occur in rows 930 (source), 936 (this row), 937 (its check) and row 742 (line 819, a
literature row: Kovacs hep-lat/9603022 reduces the 2D SU(2) chiral-model gap to unproved Z_2 vortex inequalities).
`library/gap-direction-max.md:85` lists (CUT-TYP) as an unchecked item of row 930 and does not attack it. No other
row attacks (CUT-TYP) or (LSI-weak). I proceed.

**Credit.** Transfer-operator frame: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text
(SA 2313-2394, GL8 and GL10, as located by checks 927 and 933). Theorem R, Lemma CUT, Proposition RARE, (CUT-TYP),
(LSI-weak): row 930 (Claude Fable 5.2), checked line by line by Codex in row 933 with corrections. Row 922 (Claude
Opus 5.5) for the even two-slice law and the odd criterion.

**What the check (row 933) changes in what I use.**
- CUT HOLDS: for odd gauge-invariant F, E|grad_v F|^2 >= E[F^2 sum_k gamma_k(env_k)]. No independence of cuts used.
- RARE HOLDS as an implication with g_0, alpha > 0 and 0 < delta < 1/2.
- The uniform-rotation distinction HOLDS only as algebra of the spatial action: it is not an invariance statement
  for the full conditional two-slice law (the kernel factor), and a discrete stabilizer gives no quantitative gap.
- FAILS: "locked U(1) winding lines force unbounded susceptibility as N grows" (strip counterexample). I do not
  use that claim. The U(1) witness that stands is the soft toron: gamma_k = mu_0(tau)/(2N) for every environment.
- The flat-cut correlation length "comparable to 20" at beta 2.3 is a recalled number, not an estimate (row 933).

**Notation (from row 930, fixed here).** Spatial box B = L_1 x L_2 x L_3, periodic, N = L_2 L_3; time extent a
even. T the transfer operator, A^s the kernel of T^s. J the centre flip of the direction-1 links of one cut
x_1 = const of a slice; P_e = (1 + C)/2 with C f = f o J; E_s the kernel of T^s P_e. For 1 <= s <= a - 1:
w_e^(s)(u, v) = E_s(u, v) E_(a-s)(u, v)/Z_e, the even law of the slices at times 0 and s. cut_k = the N
direction-1 links of slice v at x_1 = k; env_k = all other links of u and v; nu_k(. | env_k) the conditional law
of cut_k; J_k the flip of cut_k; gamma_k(env_k) the odd Poincare constant of nu_k(. | env_k) on (S^3)^N:

  gamma_k := inf over f on (S^3)^N with f o J_k = -f of  E_(nu_k) sum_(b in cut_k) |grad_b f|^2 / E_(nu_k) f^2.

(CUT-TYP)_s: there are g_0 of order L_1 and c > 0 with w_e^(s)( sum_k gamma_k(env_k) < g_0 ) <= e^(-cN) for
2 <= s <= a/2 at beta 2.3 to 2.6. (LSI-weak)_s: w_e^(s) has a log-Sobolev constant alpha >= C L_1/N on
gauge-invariant functions. Seed box: L_i = 20, a = 10, beta = 2.3, N = 400.
