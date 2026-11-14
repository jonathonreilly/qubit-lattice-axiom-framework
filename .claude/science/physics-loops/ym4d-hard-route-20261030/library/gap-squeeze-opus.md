lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T01:23Z

# Row 965, gap-squeeze-opus: squeezing the spatial box over the seed's time extent

Started 2026-11-14T13:23Z on the Mac mini worker 2, at commit 08d52f924 of
`claude/ym4d-hard-route`. Test item (analysis plus GUIDE). Owner's idea
(row 965): "im kinda wondering if we just squeeze the sub-box down on the seed
over time". Labels: PROVED, CONDITIONAL, GUIDE, OPEN. No statement here rests
on a run; runs are GUIDE only.

## Plan (at most eight steps; one step per response; results appended below)

1. Read rows 960 (`gap-vargeom-opus.md`), 959 (`gap-shape-link-check-astra.md`),
   947 (`gap-fc-max.md`: Theorem BR, law J, (LSI-J-seed)), 941 Step 1 (slice
   chain as exponential family); record the exact seed statements S(a;(24a)^3)
   and (LSI-J-seed) and every worst-case ceiling (2/3, 0.775, 4G_3) with source
   lines. Grep `open-core.md` and FINISH rows for overlap.
2. Task (1): define the squeezed geometry exactly (which links drop at each
   step, boundary condition: free / Dirichlet / vacuum-averaged / conditioned),
   and how it closes for a trace (periodic time) and for the two-slice law.
3. Task (2): prove the best inequality linking the squeezed quantity to the slab
   seed or (LSI-J-seed); isolate the decoupling cost per squeeze step; average
   versus supremum; compare with Martinelli-Olivieri, Stroock-Zegarlinski
   block dynamics and Theorem SH, Lemma E', Proposition B3.
4. Task (3): fact tests (free photon, compact U(1), frozen Q_8/2T, SMALL-BOX,
   K7).
5. Task (4): hand computation of the one-plaquette and one-cube endpoint
   quantities at beta 2.3-2.6 (Bessel functions).
6. Task (5): GUIDE run in a solvable model (free photon / 2D / small SU(2) by
   heat bath), decoupling cost per step against the threshold. Scripts in
   `library/guide/lane965/`.
7. Verdict: does squeezing reduce the crux to something weaker, or move it into
   the decoupling term unchanged, with the reason; statement-by-statement
   labels; RESULT line.

## State of attack (checkpoint, updated in place)

- Step 1: done (13:40Z). Step 2 next: exact definitions of the squeezed geometries.

## Step log

### Step 1 (done): inputs read, duplicate check, prior work (READ; no new claim)

**Duplicate check (rule 0a).** `grep -i squeez` on `library/open-core.md`, `library/l17c.md`,
`library/open-registry.md`: no hit. FINISH rows: only 965 (this row) and 966 (its check). No other
row attacks a squeeze statement. This row attacks no lemma of open-core; it tests a reduction. I stay
off (LSI-J-seed) itself (row 947, check 949), the DS-type block route (rows 691/693,
`gap-blockcrit-opus.md`), and (GLUE-FP) (row 895). Proceed.

**Read at 08d52f924.** GOAL.md; FINISH.md opening, How we work, Working efficiently, Rules, rows
959-966; `gap-vargeom-opus.md` (row 960) in full; `gap-fc-max.md` (row 947) Steps 5 and 7;
`gap-lsivac-max.md` (row 941) Steps 0-1; `gap-glue-max.md` (row 895) Stop 4 (Lemma MC) and
7.1-7.2 (Lemma LOC, Proposition FIB); `gap-status-1113.md` lines 68, 110, 112, 341 (ceilings);
row 959's RESULT (in FINISH).

**Objects used below (quoted in short, with sources).**
- Box B periodic, sides >= 3; H_B = L^2(SU(2)^(E_B)); T_B the Wilson transfer operator (positive,
  trace class, simple top eigenvalue lambda_0(B), eigenvector Omega_B > 0; `gap-transfer.md` 1,
  `gap-seed-check.md` Lemma 1.1). Seed S(t; B) = Tr T_B^t/lambda_0(B)^t - 1 = sum_(i >= 1) r_i^t,
  r_i = lambda_i/lambda_0. X(t; B) = log(1 + S).
- Vacuum chain (row 941 (A1)): P = Omega^(-1)(T/lambda_0)Omega on L^2(nu), nu = Omega^2 dU,
  gauge-invariant functions. One-step law pi_x(dw) = e^(beta<x,w>) m(dw)/(lambda_0 phi_0(x)),
  m = phi_0 rho, phi_0 = e^(V/2) Omega, rho = e^(-V) dx. Two-slice law
  J(dx, dw) = e^(beta<x,w>) m(dx) m(dw)/lambda_0, both marginals nu. log Omega = -V/2 +
  Lambda(beta x) - log lambda_0, Lambda convex (A2): the non-locality of Omega is a conditional
  covariance of the local 4D measure.
- Proposition HC (row 931, HOLDS in check 938): (HC-vac)_alpha on B gives
  X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m).
- (LSI-J-seed)_a (row 947 7.3, check 949): (LSI-J) on B = (24a)^3, even a >= 30, with
  alpha_J >= 2 beta K_a, K_a = (C_beta + 3 log a)/(a - 2), C_beta about 16.0 at beta 2.3.
  Corollary BR-J (row 947 7.2) turns it into (HC-vac)_(K_a), hence the slab seed. Necessary:
  E_1(B) >= K_a. Row 960 4.5: on (4a)^3 the constant drops to C_beta(4) = 12.51 (K_30 = 0.811).
- What a slab seed must supply (row 959 RESULT, Codex astra xhigh): integer a >= 3, b >= 24a, one
  common s_0 < 3/10 for every K >= K_0 and every beta in W_K(g), a common finite bound on b a_K,
  for the same bare Wilson measure on the rectangular torus.
- Ceilings (status file `gap-status-1113.md` 68, 110, 112, 341; rows 834-841, 857, 861): worst-case
  single-link criteria stop at beta 1/3; the area-law chart at 2/3; vertex blocks with
  worst-case single-link responses at 0.775 (Proposition CEIL; one family of majorants, row 861);
  background-uniform layer twist bounds are false above 4 G_3 = 1.0109 (given
  Frohlich-Simon-Spencer). "Exterior-uniform or annealed responses of blocks larger than the
  correlation length stay open (row 836)."

**Prior work that bears directly on the squeeze (credit: rows 895 and 960).**
- Row 960 (`gap-vargeom-opus.md`, Claude Opus 5.5, check row 961 pending): the decimation map J
  (2.1), mixed transfer operators T_(B,B^+) and their 4D complexes (2.2), lenses (2.3), Lemma NO-OP
  (no operator comparison T_L^t <= C Y T_s^t' Y^* after a growth step), Lemma DEN and Lemma OVL
  (no room in the denominator), Lemma Q, 5.4 (no small-box extrapolation uniform in the large
  box holds in the class). Verdict: varying geometry buys nothing for the seed. A squeeze is
  the time reverse of a growth, so 2.1-2.3 and NO-OP apply to it as they stand (Step 2 says
  which ones).
- Row 895 (`gap-glue-max.md`, Claude Fable 5.2): **Proposition FIB** (an operator that commutes
  with multiplication by every exterior function of a finite block is a direct integral over
  exteriors; its L^2(mu) norm and gap are the supremum and infimum over ALL exteriors), and
  **Lemma MC** (the maximal correlation of past and future slabs at distance w in the vacuum
  chain is exactly r_1^w). Their reading: an averaged block condition is the worst case (finite
  blocks) or the claim itself (slabs). These two facts decide most of task (2) of this row; Step
  3 uses them and says exactly where.
- Sussman-Alpoge account (CA-I/II/III at 31a47c543775; Ethan Sussman and Levent Alpoge, with
  Claude and Codex as authors of their text): row 960 searched its index for transfer-operator,
  volume-change and torus-change statements and found only the chessboard family (CA-II 6.2,
  8.7 `lem-chessboard-torus`, reflection positivity on rectangular tori). I re-ran the index
  search for squeeze-type words in Step 2 (result recorded there).
