lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T20:41Z

# gap-mini-solve-y-opus: mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1241 of FINISH.md. Started 2026-11-20T08:41Z (date -u). Worker: Claude Opus 5.5, max effort, Mac mini worker 2. Branch claude/ym4d-hard-route at c941f01ed.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Step 0. Reading log (reading only; no new claim; written 08:47Z by date -u)

Read at this pin (c941f01ed): GOAL.md in full; FINISH.md L1-90 and L296-356 (state, how we work, queue rules,
joining, working efficiently, rules), row 1241 (this row) in full, the full texts of rows 1218-1227 and the RESULT
cells of rows 1228-1246; `parts/gap.md` L1-104 (state of attack, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `library/gap-solve9-astra62.md` L130-160 (row 1161: (N-phys) and its proof frame);
`library/gap-mini-branch-fable.md` L295-315 (row 1179: (N-phys) restated, Theorem BP); `library/gap-mini-solve-j-fable.md`
Step 8 (row 1200); the sibling files of rows 1234 (v-opus) and 1243 (z-opus) as they stood at 08:42Z.

Where the problem stands on file (cited, not re-derived):

1. Consumer side. Beside the premises of Sussman and Alpoge's complete account (the T0 chain), the Jaffe-Witten gap
   on the account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1179 Theorem BP, check 1183; row
   1225 Theorem E-N, check 1232 HOLDS AFTER CORRECTION).
2. (N-phys) (row 1161 L146-148; row 1179 L304-310): at one physical side L, for every cutoff j >= j_0, some u_j with
   3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where s_+ is the centre-neutral excited trace of the vacuum-normalised
   periodic transfer matrix on the spatial cube n_j^3 and K is an existence constant fixed first.
3. Ultraviolet carry. Rows 1233, 1237, 1238 reduce the all-cutoff form to a one-cutoff seed plus named statements of
   the account ((UNIV-K) sub-items; checks 1240 and 1242). Modulo these, the crux is a finite seed for Wilson SU(2) at
   one fixed coupling inside the account's window (row 1225, ARGUED; row 1229).
4. Engines. About 45 route families are screened with named failing steps (rows 1189, 1194, 1199, 1200, 1229, 1237;
   methods 1-36 of `parts/gap.md`). The 2D pinned-cell engine has no 4D gauge form (rows 1011-1016, 1228). Uniform
   curvature or Poincare bounds force a trivial limit (row 1237 Proposition UNI, check 1240).
5. Published work (row 1218): A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy) gives a
   stronger full-thermal one-scale seed with a proved ascent; B (the first four authors) gives cube-dynamics criteria
   and a weak-coupling Poincare bound for coarse straight-path variables (Corollary 166), not selective by row 1220;
   C (Zeng Chunping) gives common-rate criteria and a conditional tunnelling route. None proves the Wilson estimate.

Rows running now on the same plain brief: 1234 (v-opus), 1243 (z-opus), 1244 (aa-opus), 1246 (solve28-astra62).
This row will name its item in Step 1 and keep it distinct from theirs as they stood when read.

## Step 1. How best to attack it (judgement, ARGUED; written 09:15Z by date -u)

**1.1 What a proof has to supply (cited).** For SU(2) along the account's trajectory, the gap clause needs exactly
one lattice input beside the T0 chain: (N-phys) (Step 0, items 1-3). On R^4 the vacuum sector carries no centre
charge: electric flux sectors exist only on tori. So the Jaffe-Witten gap is the **neutral** half. Every flux-half
tool (twist ratios, (X), the theta channel, Route T) is an instrument for the neutral half, not a proof of it. This
matches row 1161 ("the gap target needs no flux clause") and row 1200 Step 5.4; it is not new.

**1.2 Why no tool on file crosses the band (ARGUED; each clause cited).**
- A seed has to sit where the running coupling is of order one (rows 998 6b, 1219, 1225). With no computed
  certificate (GOAL.md), it must come from a structure that holds at every coupling.
- Structures that hold at every coupling and are on file: reflection positivity, gauge invariance, the Z_2 one-form
  symmetry, positive character coefficients, the loop (Schwinger-Dyson) equations with their bracket term (row 1011
  Proposition W), and convexity in beta. Each tool built from them has a named failing step in the tables of rows
  1189, 1194, 1199, 1229 and 1237, and methods 1-36 of `parts/gap.md`.
- The two posted 2D proofs (OpenAI; Ding, Huang and Yang; read in row 1007) cross their band with a continuous
  global non-abelian symmetry acting on all integration variables, or with an N-copy loop soup. Pure 4D SU(2) has
  neither on gauge-invariant data (row 1011 Lemma CEN; row 1016 CEN+). Both 2D proofs control the **charged**
  (spin) sector; their neutral sector comes from association of the O(4) ferromagnet (OpenAI Section 3.11, read in
  row 1009). In 4D association of link coordinates is empty by Elitzur's theorem (row 1194 2.2).
- So in 4D the crux has two layers. The flux half would need a band-crossing engine; the twist-index engine has a
  one-loop margin but no proof through the band (row 1200, (X)). The neutral half has no engine with a margin at
  all (row 1200 Step 5.4), and no conversion from charged to neutral decay without association is known in any
  non-abelian model (the lane's (SING); smallest open member K_3 of row 1194).

**1.3 Choice for this row.** Re-screening routes would repeat rows 1189-1238. I take the deepest layer, the neutral
half without association, in a model where the charged half is supplied: the cycle models K_N of row 1194 (N O(4)
sheets on a 2D base with product one; K_2 is the O(4) model at 2 beta; K_3 is the smallest open member). Row 1194
tried three ways (association, conditional sheets, dual gas); each stopped at the neutral response of one twisted
sheet. This row tries a fourth way, stated in Step 2, and records where it stops. Row 1194 (L226) notes that even a
proof of (K_3-N) is a mechanism, not a step of the chain; I accept that and say so in the result.

What would change on success: the lane would have its first neutral conversion with no association, which is the
missing kind of step in 1.2. On failure: the first failing step of a fourth way, so the next row does not repeat it.

