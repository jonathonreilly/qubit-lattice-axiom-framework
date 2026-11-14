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

- Step 1: done (13:40Z). Step 2: done (14:05Z). Step 3 next: the inequalities, the decoupling cost, average or supremum.

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

### Step 2 (done): the squeezed geometry and the quantity, exactly

**2.0 Conventions.** B = (Z/b)^3 periodic, b = r a (r = 24 for the slab of rows 931-954; r = 4 for
row 960 4.5). Plaquette weight e^(beta s_p), s_p := (1/2) tr U_p - 1 <= 0 (the normalisation
c(g) = e^(-beta) e^((beta/2) tr g) of `gap-transfer.md`). Slice space X_E = SU(2)^E for a link set
E, Haar measure dU, H_E = L^2(X_E). M_Q := multiplication by e^(-V_Q/2), V_Q := -beta sum over
p in Pl(Q) of s_p >= 0. A^0_Q(u, u') := integral over SU(2)^(sites of Q) of
prod over l = (x, y) in E(Q) of c(h_x u'_l h_y^(-1) u_l^(-1)) dh (the gauge-averaged time-like
kernel; row 960 2.2).

**2.1 Sub-boxes (definition).** For sides 1 <= s_i <= b - 1 and a corner c, the open sub-box Q has
sites x with x_i in {c_i, ..., c_i + s_i - 1} mod b. E(Q): links joining two sites of Q along a
direction i with s_i >= 2, without the wrap link (so a line of s_i sites carries s_i - 1 links).
Pl(Q): plaquettes with all four links in E(Q). A side s_i = b means the periodic direction (b
links per line). Unit cube Q_cube: s = (2, 2, 2), 8 sites, 12 links, 6 plaquettes (the six
faces of one lattice cube). One plaquette Q_pl: s = (2, 2, 1), 4 sites, 4 links, 1 plaquette.

**2.2 Squeeze schedule (definition).** Boxes Q_0 = B, Q_1, ..., Q_n with Q_(t+1) inside Q_t.
"One site per face per step": the first step cuts each periodic direction once (s_i(1) >= b - 1);
later steps remove at most one layer per face (s_i(t + 1) >= s_i(t) - 2). "Per k steps": a layer
is removed only at times divisible by k. E_t := E(Q_t).

**Lemma COUNT (PROVED).** A schedule of one site per face per step reaches Q_cube or Q_pl only
after n >= b/2 steps; with one layer per k steps, after n >= k b/2 - k + 1. On the slab b = 24a:
n >= 12a, twelve times the seed's time extent a. A squeeze that must close inside the slab's
period a (squeeze for a/2 steps, regrow for a/2 steps) keeps every side at least b - a = 23a.
Proof. s_i(t) >= b - 1 - 2(t - 1) for t >= 1. Q_cube needs s_i(n) <= 2, so 2n >= b - 1, n >= b/2
(b even; n integer). Q_pl needs s_3(n) <= 1, so 2n >= b. With one layer per k steps the side
falls by at most 2 every k steps after the first cut. Inside a period a the squeeze lasts at most
a/2 steps: s_i >= b - 1 - 2(a/2 - 1) >= b - a. QED
So "squeeze over the seed's time extent" down to a unit is impossible at the seed's own time
scale: the squeezed object is a different 4D complex, at least 24a - 1 steps long if it closes
(squeeze, then regrow), against the slab's a.

**2.3 The four boundary conditions (definitions; the facts marked PROVED are one-line).**
Common to all: slice t carries the links E_t; time-like links between slices t and t + 1 sit at
the sites of Q_(t+1); temporal gauge and the gauge projection at each slice as in
`gap-transfer.md` 1.6.
- **(F) free.** Plaquettes: Pl(Q_t) in slice t, and one time-like plaquette for each link of
  E_(t+1) between slices t and t + 1. A link of E_t outside E_(t+1) (a dropped link) sits in slice
  t only: it has no future. One step is the operator T^F_t: H_(E_(t+1)) -> H_(E_t) with kernel
    K^F_t(u, u') = e^(-V_(Q_t)(u)/2) A^0_(Q_(t+1))(u|E_(t+1), u') e^(-V_(Q_(t+1))(u')/2).
  PROVED: (i) the restriction u -> u|E_(t+1) pushes Haar on X_(E_t) to Haar on X_(E_(t+1)), so
  f -> f(u|E_(t+1)) is a Markov isometry R_t^*, and its adjoint R_t integrates out the dropped
  links (Haar); T^F_t = M_(Q_t) R_t^* C P M_(Q_(t+1)). (ii) K^F_t is continuous and strictly
  positive (A^0 > 0, as in row 960 2.2). (iii) K^F_t is invariant under gauge transformations at
  every site of Q_t (acting on u) and of Q_(t+1) (acting on u'), because E_(t+1) uses only sites
  of Q_(t+1). This is the time reverse of row 960's insertion step, with restriction to an open
  sub-box in place of decimation (row 960 (G3) noted that restriction leaves the periodic family).
- **(D) Dirichlet.** The full complex of [0, n] x B, every link outside the pyramid
  R := {(t, l): l in E_t} (and outside the time-like links of R) fixed to 1, every plaquette of
  the full complex kept. A kept plaquette with some frozen links is a boundary field on its free
  links (for example the time-like plaquette above a dropped link l of slice t pins u_(t,l)
  towards 1 with weight e^(beta s)).
- **(C) conditioned (quenched).** As (D), with the exterior frozen to a configuration tau instead
  of 1. PROVED (DLR property of a local action): if tau is drawn from a Gibbs measure mu of the
  full complex (the vacuum on Z x B, or the slab Z/a x B), the (C) law with exterior tau is the
  conditional law mu( . | exterior = tau), because the conditional density of the pyramid links
  given the rest contains only the plaquettes that touch the pyramid. This is "conditioning on
  the dropped links".
- **(V) vacuum-averaged (annealed).** On L^2(nu) of the periodic B, nu the vacuum slice law:
  Pi_t := E_nu[ . | sigma(x_l : l in E_t)] (orthogonal projection), and the squeezed chain
    A_n := Pi_n P Pi_(n-1) P ... Pi_1 P.
  After each step of the vacuum chain the dropped links are averaged with the vacuum's
  conditional law given the kept links of the same slice. Pi_t is a Markov operator (positive,
  Pi_t 1 = 1) and an orthogonal projection; A_n 1 = 1.

**2.4 Closure (definitions).**
- *Trace (periodic time).* The time direction closes only if the box returns. Diamond: squeeze
  for n steps, regrow for n steps, each regrow step the adjoint of a squeeze step. (F):
  Y^F := T^F_0 T^F_1 ... T^F_(n-1): H_(E_n) -> H_B and Z_dia^F := Tr(Y^F (Y^F)^*) = ||Y^F||_HS^2.
  (V): Z_dia^V := Tr(A_n^* A_n) = ||A_n||_HS^2. (D) and (C): the same with the frozen-exterior
  kernels. The lens of row 960 2.3 (hold Q_n for k steps, hold B for a steps) is the general
  closed form; the diamond is the lens with a = k = 0.
- *Two-slice law.* (V): J^V_t := the law of (x_t|E_t, x_(t+1)|E_(t+1)) under the stationary vacuum
  process of B, a marginal of J; at the narrow end J^V_n is the marginal of J on the unit box.
  (F): J^F_unit := the two-slice law of the unit box's own stationary vacuum (its transfer
  operator T_(Q_n) with free faces, held in time). No other closure keeps a two-slice law.

**2.5 The squeezed quantity (definitions).**
- Seed side, (F): the narrow-end thermal sum S(k; Q_n) := Tr T_(Q_n)^k/lambda_0(Q_n)^k - 1 of the
  unit box held for k steps; row 960 (L3) is the inequality that reads it. (V):
  S^V_dia(n) := Z_dia^V - 1 >= 0 (the constant function gives the 1).
- LSI side: the log-Sobolev constants alpha(J^V_n) and alpha(J^F_unit) of the narrow-end two-slice
  laws.
- Computability. (F) and (D) endpoint quantities are integrals over at most 12 links (cube) or 4
  links (plaquette) with explicit weights, hence Bessel series (Step 5). (C) and (V) endpoint
  quantities depend on the vacuum of all of B, through tau or through the conditional laws of nu.
  They are not computable by hand. This is the first trade-off: the boundary conditions that make
  the end computable ((F), (D)) are the ones that are far from the vacuum, and the ones that are
  faithful to the vacuum ((C), (V)) make the end as hard as the vacuum itself.

**2.6 Centre blindness after the first cut (PROVED, from row 895 Lemma LOC).** For t >= 1 every
Q_t is an open box, so it wraps no direction of the torus. By Lemma LOC of `gap-glue-max.md` 7.1
(row 895, Claude Fable 5.2), every gauge-invariant function of the links of E_t is invariant under
the centre flips C_1, C_2, C_3. So every squeezed quantity at times t >= 1 lives in the
centre-even (zero-flux) sector H_0. The flux sectors of the seed (Q_0 of row 892, Lemma SPLIT;
the 7 degenerate sectors of frozen groups, row 960 5.2) are invisible to the squeeze after its
first step. Step 4 uses this.

**2.7 Sussman-Alpoge account.** Index search (`library/sa-index/ca-full/index.tsv`) for squeeze,
shrink, pyramid, block dynamics, Glauber, log-Sobolev, spectral gap, mixing, decoupling, Dirichlet
or free boundary, one plaquette, Bessel: the hits are Balaban's decoupling expansion (cluster
parameters, CA-I 4.5, 4.21; CA-II 5.6, 8.3; CA-III 9.5), "Release and squeeze at the constrained
minimiser" (CA-II 8.11, a variational lemma of the large-field analysis), "No shrinking of the
chart on a polydisc" (CA-I 4.22) and "The holonomy of one plaquette in a cube gauge" (CA-I 4.24).
None is a mixing, gap or block-dynamics statement; their Theorem 0 asserts no gap (GOAL.md). There
is nothing to port for this row; the transfer frame itself is theirs (outline (GL8), credited in
row 941).
