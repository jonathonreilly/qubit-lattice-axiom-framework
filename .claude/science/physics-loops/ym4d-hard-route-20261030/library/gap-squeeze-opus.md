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

- Steps 1-6 done (Step 6 results written by 14:03Z). Step 7 next: verdict, status table, RESULT.
- Time note. The clock times first written here for Steps 1-4 (13:40Z, 14:05Z, 14:30Z, 14:55Z, 15:10Z)
  were estimates that ran ahead of the clock; they are removed. The file was created at 13:23Z and
  Steps 1-4 were on disk before 13:49:14Z, when the lock record for Step 5's first run starts.

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
after n >= b/2 steps; with one layer per k steps (removals at times k, 2k, ...), after n >= k b/2. On the slab b = 24a:
n >= 12a, twelve times the seed's time extent a. A squeeze that must close inside the slab's
period a (squeeze for a/2 steps, regrow for a/2 steps) keeps every side at least b - a = 23a.
Proof. s_i(t) >= b - 1 - 2(t - 1) for t >= 1. Q_cube needs s_i(n) <= 2, so 2n >= b - 1, n >= b/2
(b even; n integer). Q_pl needs s_3(n) <= 1, so 2n >= b. With removals only at times k, 2k, ...,
the m-th removal is at time m k, and b/2 removals are needed. Inside a period a the squeeze lasts at most
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

### Step 3 (part A, done): the squeezed quantities sit on the bounded side; the exact shell identity

**3.1 Lemma BND (a squeeze bounds less than the seed; PROVED).**
(i) (V) diamond: 0 <= S^V_dia(n) <= S(2n; B).
Proof. Pi_t and P are self-adjoint on L^2(nu), fix the constants and so leave L^2_0(nu) (mean zero)
invariant. On L^2_0, A_n^* A_n = P Pi_1 P Pi_2 ... P Pi_n P Pi_(n-1) ... Pi_1 P (Pi_n^2 = Pi_n) is a
product of 2n factors P and of contractions. Hoelder for Schatten norms (exponent 2n for each P,
infinity for each Pi) gives Tr(A_n^* A_n on L^2_0) <= ||P|L^2_0||_(2n)^(2n) = Tr(P^(2n) on L^2_0)
= S(2n; B). The left side is a trace of a positive operator. QED
(P is unitarily equivalent to T_B/lambda_0 on gauge-invariant functions through f -> f/Omega, so
Tr P^t = Tr T_B^t/lambda_0^t; row 941 (A1).)
(ii) (F), (D) closures: row 960 (L3), Z_lens/(lambda_0(L)^a ||Y||^2 lambda_0(s)^k) <= 1 + S(k; Q_s),
read with restriction in place of decimation (its proof uses only ||Y|| and positivity), and row
960 3.4 (Hoelder puts varying complexes below rectangular ones). PROVED there.
Meaning. A bound on the narrow end bounds a squeezed complex from above, and a squeezed complex is
below the slab. Neither bounds the slab. Every use of the squeeze for the seed needs a REVERSE
inequality; its error term is the decoupling cost. 3.2-3.5 find that term exactly.

**3.2 Theorem SHELL (the exact squeeze identity under (V); PROVED).** Let Q_0 = B, Q_1, ..., Q_n be
a schedule (2.2), Pi_t as in (V), Pi_c the projection on constants, Pi_0 = I. Put
D_k := Pi_k - Pi_(k+1) (k < n), D_n := Pi_n - Pi_c, and S_j(t) := Tr(Pi_j^0 P^t Pi_j^0) with
Pi_j^0 := Pi_j - Pi_c (the seed compressed to functions of the links of Q_j). Then for every t >= 1:
  S(t; B) = sum over k = 0..n of s_k(t),   s_k(t) := Tr(D_k P^t D_k) >= 0,
  S_j(t) = sum over k >= j of s_k(t),   so   S(t; B) = S_0(t) >= S_1(t) >= ... >= S_n(t) >= 0.
Proof. E_(k+1) is inside E_k, so the sigma-algebras decrease and Pi_(k+1) = Pi_k Pi_(k+1) =
Pi_(k+1) Pi_k. Hence each D_k is an orthogonal projection, D_k D_j = 0 for k != j, and
sum over k of D_k = I - Pi_c. P^t is trace class (T_B is) and Tr(P^t) = 1 + S(t; B). So
S(t; B) = Tr((I - Pi_c) P^t) = sum_k Tr(D_k P^t) = sum_k Tr(D_k P^t D_k) (cyclicity, D_k^2 = D_k),
each term >= 0 since P^t >= 0. The same computation with Pi_j^0 = sum over k >= j of D_k gives S_j. QED
Reading.
- The decoupling cost of the squeeze step Q_j -> Q_(j+1) is EXACTLY s_j(t) = S_j(t) - S_(j+1)(t),
  and the total cost from B to the unit is S(t; B) - S_n(t). Nothing is lost and nothing is gained:
  the squeeze re-indexes the seed by shells.
- Each s_k(t) is a vacuum thermal sum of the same kind as the seed (a trace of P^t compressed to the
  functions that are new on shell k). The narrow end S_n(t) = sum over an orthonormal basis (g_j)
  of L^2_0 of the unit box of <g_j, P^t g_j>_nu: vacuum autocorrelations of unit-box observables.
  It is a vacuum quantity, not computable by hand.
- In a massive gas each shell carries about its share of the volume, so the unit end carries about
  |E_n|/|E_0| of S (12/(3 b^3) for the cube; ARGUED; Step 6 measures the shares in a Gaussian model).
- **Corollary FLUX (PROVED, given 2.6).** Every centre-odd level of P lies in Ran D_0: by 2.6 every
  function of E_1 is centre-even, so it is orthogonal to the odd sectors. Hence
  s_0(t) >= sum over centre-odd levels i of r_i^t. The first step (the cut of the periodic box)
  carries the whole flux half of the seed (Q_0 of row 892), and no later step sees it.

**3.3 Lemma LEAK (the time squeeze under (V); PROVED identity).** With A_0 = I and A_j = Pi_j P A_(j-1):
  P^n - A_n = sum over j = 1..n of P^(n-j) (I - Pi_j) P A_(j-1).
Proof. P^j - A_j = P (P^(j-1) - A_(j-1)) + (I - Pi_j) P A_(j-1); induct. QED
Hence, with the Hilbert-Schmidt norm on L^2_0,
  (1 + S(2n; B))^(1/2) <= (1 + S^V_dia(n))^(1/2) + sum over j of l_j,
  l_j := ||P^(n-j) (I - Pi_j) P A_(j-1)||_HS.
The cost l_j of step j is the part of one step of the vacuum chain, applied to a function of
Q_(j-1), that is not a function of Q_j. It contains the dependence on the dropped layer itself,
not only the influence of the exterior on the interior. So under (V) a squeeze spread over time is
no better than Theorem SHELL: the shell content is lost at the step that drops it and must be paid
back in l_j (ARGUED; Step 6 measures S^V_dia(n) against S(2n; B) in the Gaussian model).

### Step 3 (part B, done): the squeeze as a cone (Theorem CONE), as block dynamics (Lemma QF), average versus supremum

**3.4 Theorem CONE (the seed as a sum of local influences; the squeeze as a backward cone).**
(a) **Lemma PR (pressure identity; PROVED).** For every beta > 0,
  X(a; B) = integral over [0, beta] of sum over p in Pl(Z/a x B) of ( E^a_(beta')[s_p] - E^inf_(beta')[s_p] ) d beta',
with E^a the Wilson measure of the slab Z/a x B and E^inf[s_p] the stationary vacuum expectation of
a plaquette of the same type (spatial or time-like, same orientation) on Z x B.
Proof. Z(a, B) = Tr T_B^a (`gap-transfer.md` 1.7), so d/d beta log Z(a, B) = sum over p of E^a[s_p]
(finite-dimensional compact integral). lambda_0(B; beta) is simple (Lemma 1.1 of `gap-seed-check.md`),
so log lambda_0 = lim over T of f_T, f_T := (1/T) log Z(T, B) (because Z(T, B) = lambda_0^T (1 + S(T; B))
and S(T; B) <= r_1^(T-1) S(1; B) -> 0). Each f_T is convex in beta (its second derivative is a
variance), and lambda_0 is real-analytic in beta (simple isolated eigenvalue of an analytic
trace-class family). Convex functions that converge pointwise to a differentiable limit have
converging derivatives, so d/d beta log lambda_0 = lim over T of (1/T) sum over p in Pl(Z/T x B) of
E^T[s_p] = lim over T of sum over p in one time layer of E^T[s_p] (time translation), and each
E^T[s_p] converges (trace class, simple top level) to E^inf[s_p]. At beta = 0, c = 1, so T_B is the
projection on constants, Z(a, B) = 1 = lambda_0 and X = 0. Integrate
d/d beta X = sum over the a|B| 6 slab plaquettes of E^a[s_p] - a sum over one layer of E^inf[s_p]. QED
(b) **Window identity (PROVED).** Let a be even, h = a/2, p a plaquette at time 0 (spatial, or
time-like between slices 0 and 1). Let phi_p(y, z) be the conditional expectation of s_p in the time
window [-h, h] given the boundary slices x_(-h) = y and x_h = z (the window's own specification:
interior plaquettes and the time-like plaquettes that touch the two boundary slices). Then
  E^a[s_p] - E^inf[s_p] = E_(nu_a)[ phi_p(y, y) ] - E_(J_a)[ phi_p(y, z) ],
nu_a the slab law of one slice (the slices h and -h are the same slice of Z/a), J_a the vacuum law of
(x_(-h), x_h). Proof: the Gibbs property in time; both measures have the window specification inside
the window, and the boundary slices' own spatial plaquettes do not touch the interior. QED
(c) **The worst-case squeeze bound (PROVED).** Both terms in (b) are averages of phi_p, so
  X(a; B) <= 6 a b^3 beta max over beta' <= beta and the six plaquette types of osc(phi_p)(beta'),
osc := sup - inf over all boundary pairs (y, z). A bound on osc(phi_p) is a squeeze: the influence of
the boundary slices at time distance h on the unit p passes through the backward cone of p, which
narrows one site per step from the boundary slice to p (disagreement-percolation or Dobrushin form;
the per-step cost is a worst-case influence coefficient, capped by the ceilings of Step 1).
Required size, by hand: 6 a b^3 beta = 6 x 30 x 720^3 x 2.3 = 1.545 x 10^11 at a = 30, b = 24a,
beta 2.3, so osc <= x_*/(1.545 x 10^11) = 0.2578/(1.545 x 10^11) = 1.67 x 10^-12 (1.48 x 10^-12 at beta 2.6).
On the ratio-4 box of row 960 4.5 (b = 120, x_* = log(26/25) = 0.03922): 6 x 30 x 120^3 x 2.3 = 7.15 x 10^8,
osc <= 5.5 x 10^-11.
(d) **Lemma HALF (any worst-case squeeze pays the square root; PROVED).** For a spatial plaquette p at
time 0 and g_p := s_p - nu(s_p):
  osc(phi_p) >= ||P^h g_p||_(L^2(nu)) = Cov_inf( s_p(x_0), s_p(x_a) )^(1/2) >= r_1^h |<phi_1, g_p>_nu|,
with phi_1 the first excited eigenfunction of P.
Proof. By the tower property and the Markov property of the vacuum chain, averaging phi_p(y, .) over
z with the vacuum's conditional law of x_h given x_(-h) = y gives E^inf[s_p | x_(-h) = y] = (P^h s_p)(y).
So inf phi_p <= P^h s_p(y) <= sup phi_p for every y, and osc(phi_p) >= osc(P^h g_p). P^h g_p is
continuous with nu-mean 0, so it takes both signs and osc(P^h g_p) >= ||P^h g_p||_inf >= ||P^h g_p||_2.
||P^h g_p||_2^2 = <g_p, P^(2h) g_p> = Cov_inf(s_p(x_0), s_p(x_a)) = sum over i >= 1 of r_i^a |<phi_i, g_p>|^2. QED
(e) **The true term is first order; spectral form (PROVED).**
  E^a[s_p] - E^inf[s_p] = (1 + S(a; B))^(-1) sum over i >= 1 of r_i^a ( <psi_i, s_p psi_i> - <psi_0, s_p psi_0> )
(psi_i the orthonormal eigenfunctions of T_B; spatial p; insert s_p as a multiplication operator).
Both this and Cov_inf(s_p(x_0), s_p(x_a)) are of order r^a when g_p has a non-zero overlap with the lowest
levels; Lemma HALF says a worst-case squeeze then needs the SQUARE ROOT of the second to be below the first's
required size. (Scope, added in Step 6: the loss needs <phi_i, g_p> != 0 on the lowest band. For SU(2) the
plaquette creates the lightest 0++ glueball, which is how lattice glueball masses are measured, RECALLED; so the
loss applies. In a free scalar with g = phi_x^2 the lowest band coupled to g is the two-particle threshold 2m,
and the square root then decays at the same rate m as the true term: no loss in the rate there.) Reading (ARGUED; GUIDE in
Step 6): if the worst-case cone influence decayed at the vacuum rate m, the route would need
e^(-m a) <= (1.67 x 10^-12)^2, about m a >= 54, where the seed itself needs about m a >= 27 plus
logarithms: the time extent doubles, and the box b = 24a with it.
(f) **The averaged form is the claim (PROVED).** Summing (b) over the 6 a b^3 plaquettes and
integrating over beta' returns X(a; B) exactly (Lemma PR). An averaged bound on the influences of the
size the seed needs is the seed itself (the slab analogue of row 895's Lemma MC).

**3.5 The squeeze as block dynamics (gap and LSI).**
(a) **Lemma QF (two-block quasi-factorization of the variance; PROVED).** Let E_1, E_2 be orthogonal
projections (conditional expectations) on L^2(mu), E_cap the projection on Ran E_1 intersected with
Ran E_2, eps := ||E_1 E_2 - E_cap||. For every f orthogonal to Ran E_cap:
  ||f||^2 <= (1 - eps)^(-1) [ (||f||^2 - ||E_1 f||^2) + (||f||^2 - ||E_2 f||^2) ].
For E_i = E_mu[ . | F_(A_i^c)] (resample the block A_i) and Ran E_cap = constants, this reads
Var(f) <= (1 - eps)^(-1) sum over i of E Var(f | F_(A_i^c)).
Proof. E_i commute with E_cap, so they reduce on (Ran E_cap)^perp, where ||E_1 E_2|| = eps. Put
u = E_1 f, v = E_2 f, s = ||u||^2 + ||v||^2. Then s = <f, u + v> <= ||f|| ||u + v|| and
<u, v> = <u, E_1 E_2 v>, so ||u + v||^2 <= s + 2 eps ||u|| ||v|| <= (1 + eps) s. Hence s <= (1 + eps) ||f||^2,
which is the claim. QED
(b) **Average versus supremum (PROVED, from row 895).** If A = A_1 union A_2 is a finite block with a
non-empty exterior, E_1, E_2 and E_cap commute with multiplication by every bounded function of A^c,
so by Proposition FIB of `gap-glue-max.md` 7.2 eps is the supremum over ALL exteriors tau of the
fibre value eps(tau): the L^2(mu)-averaged condition IS the worst case. If A is the whole torus (the
top level of a recursion), there is no exterior and eps is a global maximal correlation: for past and
future time slabs at distance w it is r_1^w exactly (row 895 Lemma MC). For spatial half-slabs the same
lemma applies along x_1 once that direction is unrolled to Z: it gives (r_1^(1))^w, r_1^(1) the ratio of
the top two levels of the transfer operator in direction 1 of the slab's cross-section (the slab is
reflection positive in every direction, CA-II 8.7 of Sussman and Alpoge); on the periodic box the two
arcs also meet the other way round, so it is that value up to the wrap. Either way: the gap in the
crossed channel. So every averaged squeeze
condition is either the worst case (finite blocks) or the claim (the top level).
(c) **Recursions in the literature (RECALLED, not rebuilt).** Martinelli and Olivieri (CMP 161, 1994):
strong mixing on regular boxes gives a uniform gap and LSI for Glauber dynamics, by block dynamics and
a recursion over box sizes. Lu and Yau (CMP 156, 1993): the martingale (squeeze-by-shells) method.
Cesi (PTRF 120, 2001): quasi-factorization of the entropy, under an L^1 -> L^inf decoupling (a
supremum by its form). Stroock and Zegarlinski (CMP 149, 1992; JFA 104, 1992): a log-Sobolev inequality
uniform in the volume and the boundary condition is EQUIVALENT to Dobrushin-Shlosman complete
analyticity, a worst-case mixing condition. So in this family the decoupling cost is the
worst-case mixing coefficient, and it cannot be weakened (the equivalence). For the gauge theory the
first levels (single links, vertex blocks) are exactly where the ceilings 1/3 and 0.775 sit; blocks
larger than the correlation length are OPEN (row 836). For (LSI-J) one first passes to the local 4D
parent (row 960 3.7, J has no local specification, row 947 7.3); the same equivalence then holds.

**3.6 Comparison with Theorem SH, Lemma E' and Proposition B3.** SH, E' and B3 extrapolate UP from one
fixed box with the time scaled with the box (a_k = j^k a); their input is a seed on (a; (ra)^3), r >= 2
(threshold 1/550 at r = 2 by Theorem SH' of row 960, 3/10 at r >= 24). The squeeze goes DOWN to a unit.
By COUNT it lasts at least 12a steps, so it cannot sit inside the seed's slab. By SHELL its exact cost
under (V) is the seed minus the unit's share. By CONE its worst-case form needs osc <= 1.7 x 10^-12 on
the slab and pays the square root (HALF). By QF and FIB its block form needs worst-case mixing or the
gap itself. Row 960 5.4 (no small-box inequality uniform in the large box at fixed time holds in the
class) is the same fact seen from the other side: SHELL shows the cost is a volume sum. No squeeze
inequality found here is better than SH in threshold or in box size; SH's input box stays the
smallest input of the static method.

**3.7 Answer to task (2), in one table.**

| Squeeze form | Best inequality found | Decoupling cost | Average or supremum | Against the crux |
|---|---|---|---|---|
| (V), one time (shells) | Theorem SHELL: S = sum of s_k, exact | s_j = S_j - S_(j+1); total S - S_n | average | the seed itself, re-indexed |
| (V), over time | Lemma BND (i) and Lemma LEAK | l_j: one step's loss of the dropped layer | average | no better than SHELL (ARGUED) |
| cone to one plaquette | Theorem CONE (c), Lemma PR | osc(phi_p) <= 1.7 x 10^-12 (slab) | supremum | needs the square root (HALF): time extent doubled; capped by the ceilings |
| cone, averaged | Lemma PR, (f) | the influences summed | average | the seed itself |
| block dynamics (gap, LSI) | Lemma QF; MO, LY, Cesi, SZ | eps of overlapping blocks | L^2 average = supremum (FIB); top level = r_1^w (MC) | worst-case mixing or the gap; SZ: equivalent to complete analyticity |
| (F), (D) computable end | Lemma BND (ii) (row 960 L3) | none: wrong side | n/a | no reverse inequality |
| (C) conditioned | DLR: exact | averaging over tau returns the vacuum | average = exact; pointwise = supremum | end not computable |

### Step 4 (done): fact tests

Rule for this step: a squeeze statement passes a model if it claims no gap where the model has none,
and the test says WHERE the model's difficulty sits (endpoint or decoupling cost).

**4.1 Free photon and compact U(1) (power-law decay must make the cost blow up).**
- *Gaussian (non-compact) fields, Theorem CONE (c). PROVED: the worst-case cost is infinite.* In a
  Gaussian field the conditional mean of the window given the boundary slices is linear in (y, z) and
  the conditional covariance is constant, so for a plaquette observable that is quadratic in the
  field, phi_p(y, z) = q(L y + L' z) + const with q a non-zero quadratic form and (L, L') not zero
  (the time-like plaquettes couple adjacent slices). An unbounded quadratic form has osc = infinity.
  So the worst-case squeeze gives nothing for the free photon at any a and any box. PASS.
- *Compact U(1), Coulomb phase (beta above about 1.01). ARGUED from RECALLED power laws.* By Lemma
  HALF, osc(phi_p) >= Cov_inf(s_p(x_0), s_p(x_a))^(1/2). With massless photons, s_p ~ -theta_p^2/2
  and the connected autocorrelation decays like c a^(-8) (two-photon exchange; c of order
  1/(pi^4 beta^2), RECALLED free-field value). Then the right side of CONE (c) is at least
  6 a (r a)^3 beta c^(1/2) a^(-4) = 6 r^3 beta c^(1/2), INDEPENDENT of a: about 8 x 10^4 beta c^(1/2),
  of order 10^3 to 10^4 at r = 24, against x_* = 0.26. The cost does not fall as the seed box grows,
  as it must not. PASS.
- *Theorem SHELL.* An identity; it claims nothing. In the compact Gaussian model of row 960 5.4,
  S(a; L^3) -> infinity as L grows at fixed a, while the unit-end term S_n(a) is a sum of
  autocorrelations of unit-box observables and stays bounded (ARGUED: those decay in time and do
  not grow with L). So the shell cost S - S_n diverges with the box. PASS; the cost carries all of it.
- *Block dynamics (Lemma QF).* For a massless field the L^2 angle eps between two overlapping blocks
  at a fixed ratio of overlap to size is scale invariant, so it does not fall along the recursion,
  and the product of the factors (1 - eps) over the log_2 b levels decays like a power of b (ARGUED),
  as the photon gap 2 pi/b requires. PASS.

**4.2 Frozen Q_8 and 2T (and Z_2 at large beta).** The flux sectors are degenerate with the vacuum,
so S(a; B) >= 7 - o(1) (RECALLED count, row 960 5.2).
- *SHELL with Corollary FLUX. PROVED given the count.* s_0(t) >= sum over the odd levels of r_i^t
  >= 7 - o(1). All the flux half sits in the FIRST squeeze step, the cut of the periodic box. Every
  later shell and the narrow end see only the centre-even sector (2.6), where the frozen model has
  a large gap (local excitations cost of order beta). So the squeeze is cheap after the first step and
  the first step costs at least 7. PASS, and it locates the difficulty: a squeeze cannot touch the
  flux half; only the first, non-local step carries it.
- *CONE.* Lemma PR integrates over beta' in [0, beta]; the path crosses the bulk transition of the
  finite group (Z_2 near 0.44, Q_8 near 1.15, 2T near 2.15; the ladder of `gap-brainstorm-max.md`
  Prop F6, ARGUED there from GUIDE values), where
  the worst-case influence is of order one (coexisting phases). So the bound of CONE (c) is large
  and gives nothing. In the frozen phase itself local plaquette autocorrelations are tiny and
  centre-blind, so Lemma HALF gives no obstruction there; the log 8 of the seed is collected near
  the transition, consistent with Lemma PR being exact. PASS.
- *Block dynamics.* Local blocks are centre-blind (row 895 Lemma LOC); their recursion can give at
  most the even gap. The top level is the whole torus, where eps = r_1^w with r_1 -> 1 (odd sectors
  degenerate): the last step fails. PASS (row 895's flux-half point, in this form).

**4.3 SMALL-BOX (a small box at large beta has no gap, so the cost must grow with beta).**
- *The open unit endpoint HAS a gap at large beta. PROVED structure, ARGUED limit (Step 5 computes it
  at beta 2.3-2.6).* On Q_pl the gauge-invariant functions are the class functions of the holonomy U
  of the one plaquette, and the transfer operator is T = M D M with M = e^(beta s_p/2) and
  D chi_j = (c_j/d_j)^4 chi_j (each of the 4 links convolves by c, which acts on the irreducible
  representation j as the scalar c_j/d_j; c_j/d_j = e^(-beta) (2/beta) I_(2j+1)(beta)). At large beta,
  c_j/c_0 -> e^(-2 j(j+1)/beta), so D ~ e^((2/beta) Laplacian of S^3) and V = beta (1 - cos theta)
  ~ beta theta^2/2: a three-dimensional lattice oscillator with mass beta/4, omega^2 = 4 and time step 1,
  independent of beta. Its exact one-step transfer matrix has cosh(omega~) = 1 + omega^2/2 = 3, and class
  functions are its s-waves, so the gap tends to 2 omega~ = 2 arccosh 3 = 3.526. (Corrected in Step 5:
  the first text said 2 omega = 4, the small-time-step value; Step 5's GUIDE gives 3.40 at beta 8,
  3.47 at 16, 3.50 at 32.) The periodic small box of
  SMALL-BOX fails through its flat directions (torons) and its 1/b gluon levels; an open box has
  neither (on a simply connected open box a flat connection is a pure gauge).
- So the squeeze endpoint is easy at EVERY beta, and the beta-dependence of the seed (asymptotic
  freedom: correlation length growing like e^(c beta)) must sit entirely in the decoupling cost. It
  does: in CONE the worst-case influence per step tends to one below the correlation length (Lemma
  HALF with photon-like autocorrelations up to that scale); in SHELL the shell terms carry the gluon
  levels; in QF eps stays of order one at every level below the correlation length (ARGUED, as in
  4.1). PASS.

**4.4 K7 (mixed weight exp(beta_F x + beta_A (4x^2 - 1)/3), first-order line).** Two phases coexist
and every periodic thermal sum is at least 1 - o(1) (READ `gap-mid-max.md` L48).
- *Endpoint.* Under (F) the open unit box is a finite system with a smooth weight: gap of order one,
  no coexistence. Under (V) the unit end is a vacuum quantity: a unit-box plaquette has an overlap of
  order one with the tunnelling state phi_1 (the two phases have different mean plaquettes), so
  S_n(t) >= r_1^t ||Pi_n phi_1||^2 is of order one for t below the tunnelling time (ARGUED). So the
  computable endpoint misses the coexistence, and the faithful endpoint already contains it.
- *CONE.* osc(phi_p) is at least half the jump of the plaquette between the two phases, which does
  not decay with h (boundary slices select the phase); Lemma HALF gives the same with r_1 near 1.
  The bound is of order 6 a b^3 beta times that jump. PASS.
- *QF.* Top level eps = r_1^w with r_1 near 1. PASS.

**4.5 Summary of the fact tests.** Every squeeze statement of Step 3 passes every test, by claiming no
gap. The tests say where the difficulty goes: photon and U(1) into a cost that does not fall with
the box; the flux half of frozen groups into the first squeeze step; asymptotic freedom (SMALL-BOX)
into the per-step cost, the open endpoint being gapped at every beta; K7 into the passage from the
computable endpoint (F) to the faithful one (V). In no model does the endpoint carry the difficulty.

### Step 5 (done): the endpoint values, by hand, at beta 2.3-2.6

Arithmetic check and GUIDE diagonalisation: `library/guide/lane965/endpoint.py`, log
`logs/endpoint.log` (lock holder lane965-opus, 13:55:12Z-13:55:40Z, 73 percent memory free, one thread,
nice 10, RSS guard 2 GB). Two code errors were found and fixed before the numbers below (a trace
formula that summed l only to j, and a cube coefficient that used c_j/d_j for c_j); one run was stopped
at 2.5 GB RSS (a 12000-point Gauss-Legendre rule) and replaced by a midpoint rule. The hand values
below agree with the final log to the digits shown.

**5.1 Bessel series (hand).** I_nu(x) = sum over k of (x/2)^(2k+nu)/(k! (k+nu)!).
beta = 2.3 (x/2 = 1.15): I_1 = 1.15 + 0.760437 + 0.167613 + 0.018472 + 0.001221 + 0.000054 + ... = 2.09780;
I_2 = 0.66125 + 0.291501 + 0.048189 + 0.004249 + 0.000234 + 0.000009 = 1.00543;
I_3 = 0.253479 + 0.083807 + 0.011083 + 0.000814 + 0.000039 = 0.34922; I_4 = 0.09442, I_5 = 0.02083.
beta = 2.6 (x/2 = 1.3): I_1 = 1.3 + 1.0985 + 0.30941 + 0.04357 + 0.003681 + 0.000207 = 2.75538;
I_2 = 0.845 + 0.476017 + 0.100559 + 0.011330 + 0.000798 + 0.000039 = 1.43374;
I_3 = 0.366167 + 0.154705 + 0.026145 + 0.002455 + 0.000148 + ... = 0.54963; I_4 = 0.16537, I_5 = 0.04079.
Ratios A_j := I_(2j+1)/I_1: A_(1/2) = 0.47928, A_1 = 0.16647, A_(3/2) = 0.04501, A_2 = 0.00993 (beta 2.3);
0.52034, 0.19947, 0.06002, 0.01480 (beta 2.6). Tail: I_nu(x) <= ((x/2)^nu/nu!) e^(x^2/4), so A_(5/2) <= 0.0132
at beta 2.6 and every term with j >= 5/2 below is under 10^-7.

**5.2 One plaquette, static, free faces (PROVED formulas).** Z_pl = c_0 = e^(-beta)(2/beta) I_1(beta):
0.18289 (2.3), 0.15743 (2.6). Mean <x> = <(1/2) tr U> = I_2/I_1 = 0.47928, 0.52034.
Var(x) = 1 - 3A/beta - A^2 with A = I_2/I_1 (from I_nu' = I_(nu-1) - (nu/x) I_nu): 0.14515, 0.12885.

**5.3 Proposition EP1 (the one-plaquette box, (F) endpoint of the seed side; PROVED, by hand).**
On Q_pl, T = M D M (4.3). Then
  S(1; Q_pl) <= N/R - 1,   N := 1 + sum over j >= 1/2 of A_j^4 sum over integers l = 0..2j of (2l+1) A_l,
                           R := sum over j of (2j+1)^2 A_j^6,
and S(k; Q_pl) <= S(1; Q_pl)^k for k >= 1, r_1 <= S(1; Q_pl).
Proof. D is diagonal on the orthonormal characters, so Tr T = Tr(D M^2) = sum over j of (c_j/d_j)^4 <chi_j, M^2 chi_j>.
M^2 = e^(beta s) = e^(-beta) e^((beta/2) tr U) = sum over l of c_l chi_l with c_l = e^(-beta)(2/beta)(2l+1) I_(2l+1)(beta) = (2l+1) c_0 A_l,
and chi_j chi_j = sum over integers l = 0..2j of chi_l (Clebsch-Gordan), so <chi_j, M^2 chi_j> = sum over those l of c_l.
Hence Tr T = c_0^5 N. For the top level take psi = M 1: <psi, T psi> = <M^2 1, D M^2 1> = sum over j of (c_j/d_j)^4 c_j^2
and ||psi||^2 = c_0, so lambda_0 >= c_0^5 sum over j of A_j^4 (2j+1)^2 A_j^2 = c_0^5 R. (R is also the partition function of the
closed cube surface divided by c_0^6, 5.4: one step of M 1 is the cube.) So 1 + S(1) = Tr T/lambda_0 <= N/R. The bound
S(k) <= S(1)^k is "the l^k norm is at most the l^1 norm" (row 960 Lemma Q). QED
Values (j <= 1 terms; the rest is below 2.2 x 10^-5 in N and 10^-6 in R):
- beta 2.3: N = 1 + 0.052766 x 1.49941 + 0.000768 x 1.54905 = 1.080308; R = 1 + 4 x 0.012121 + 9 x 0.0000213 = 1.048677;
  S(1; Q_pl) <= 0.03017. GUIDE value 0.02872.
- beta 2.6: N = 1 + 0.073309 x 1.598422 + 0.001583 x 1.672432 = 1.119827; R = 1 + 4 x 0.019849 + 9 x 0.0000630 = 1.079963;
  S(1; Q_pl) <= 0.03691. GUIDE value 0.03409.
So E_1(Q_pl) >= -log 0.0302 = 3.50 at beta 2.3 and >= 3.30 at beta 2.6 (GUIDE: 3.56, 3.47 at 2.45, 3.40).
Large beta (GUIDE): 3.24 (4), 3.40 (8), 3.47 (16), 3.50 (32), towards 2 arccosh 3 = 3.526 (4.3, corrected).

**5.4 One cube, free faces (static; PROVED formula, hand values).** The six faces form a closed surface with
Euler characteristic 2 and every link in two faces, so the character expansion gives
  Z_cube = sum over j of d_j^2 (c_j/d_j)^6,   d_j = 2j + 1.
(Checked on two small surfaces: the sphere of two discs glued along one loop gives sum of c_j^2; the torus of one
face gives sum of c_j/d_j; both by Schur orthogonality.) Values: Z_cube/c_0^6 = 1.04868 (2.3), 1.07996 (2.6).
Mean plaquette <x>_cube = 1 + (1/6) d/dbeta log Z_cube = sum_j w_j (2j/beta + I_(2j+2)/I_(2j+1))/sum_j w_j,
w_j = d_j^2 A_j^6: 0.49340 (2.3), 0.53884 (2.6) (the closed surface raises it above the free plaquette's 0.479, 0.520).
E[chi_1(U_f)] on the cube: one face carries c(U) chi_1(U) = sum_j c'_j chi_j, c'_j = c_(j+1) + c_j [j >= 1/2] + c_(j-1) [j >= 1];
at beta 2.3: c'_0 = 0.091338, c'_(1/2) = 0.208234, c'_1 = 0.283306 (with c_0 = 0.18289), and
E[chi_1] = (0.49942 + 0.057587 + 0.000594)/1.048675 = 0.53172 (0.64606 at 2.6).
Cube transfer operator, leading term only (NOT a bound): the six one-face spin networks give
6 A_(1/2)^4 Var(chi_(1/2)(U_f)) = 6 x 0.052766 x (1 + 0.53172 - 0.98680^2) = 0.177 at beta 2.3 (0.213 at 2.6): six face
excitations, each about the size of the one plaquette's S(1). The full cube thermal sum needs every spin network on
the 12-link cube graph; it is OPEN by hand and not needed (5.6).

**5.5 The LSI-side endpoint.** For block dynamics with one-link blocks on the local 4D parent of J (row 960 3.7;
J itself has no local specification), the endpoint is the conditional law of one link, exp((beta/2) tr(u A^dagger))
with A the sum of its six staples. At zero staple sum (an allowed exterior: staples can cancel) it is Haar on the
unit S^3, whose Poincare and log-Sobolev
constants are both 3 (first eigenvalue of S^3; Mueller-Weissler for the log-Sobolev constant of S^n, RECALLED).
A tensorization or quasi-factorization bound has the form (minimum endpoint constant) x (factors <= 1), so with
one-link blocks it certifies at most 3. (LSI-J-seed) needs 2 beta K_a: 4.30 at beta 2.3, a = 30 (slab), and 3.73 on
the ratio-4 box of row 960 4.5. So one-link block dynamics cannot reach (LSI-J-seed) at a = 30 even at zero
decoupling cost. It needs a >= 45 on the slab (K_45 = 27.42/43 = 0.638, 2 beta K = 2.93) or a >= 40 on the ratio-4
box (K'_40 = 23.58/38 = 0.621, 2.85). Larger blocks remove this cap, but their worst-case constants are not
computable by hand.

**5.6 What the endpoint values mean.** The computable end is small and easy: S(k; Q_pl) <= 0.0369^k at beta 2.6,
below the 1.67 x 10^-12 of Theorem CONE (c) once k >= 9 (0.0369^9 = 1.3 x 10^-13), and the open unit box has a gap
above 3.3 at every beta of the window and as beta grows. The owner's hope for the narrow end holds. But the end
enters only on the bounded side (Lemma BND (ii)): every reverse inequality of Step 3 has a cost that must itself be
below the seed's required size (1.7 x 10^-12 per plaquette on the slab, or the whole shell sum S - S_n). So the
endpoint's smallness buys nothing; the whole crux sits in the decoupling term.

### Step 6 (GUIDE; criteria written at 13:58Z, before any run)

**Models, stated as models.** (M1) The lattice free scalar of mass m on B = (Z/b)^3 (row 960 Step 6): per mode
2 cosh eps_k = 2 + m^2 + sum_i 4 sin^2(k_i/2); vacuum covariance C = (2 sinh eps)^-1; one-step mean map
A = e^(-eps); time-t cross covariance C A^t. It is Gaussian: P = Gamma(A) on the first chaos with the C inner
product, Pi_j = Gamma(pi_j) (pi_j the C-orthogonal projection onto the span of phi_x, x in Q_j; RECALLED standard
fact for Gaussian Hilbert spaces), and Tr Gamma(X) = det(1 - X)^-1. Hence, exactly in the model,
  S(t; B) = det(1 - A^t)^-1 - 1,   S_j(t) = det(C_QQ)/det(C_QQ - (C A^t)_QQ) - 1  (Q = Q_j),
  S^V_dia(n) = det(1 - a_n^* a_n)^-1 - 1,   a_n = pi_n A pi_(n-1) A ... pi_1 A.
It has no gauge field, no flux sectors, no interaction. (M2) The one-plaquette box Q_pl of SU(2) (5.3): T = M D M on
class functions, exact up to the truncation j <= 12; there s_p couples the vacuum to the first excited level.

**Runs and pre-stated criteria.**
- G0 (code test): for Q_0 = B the shell formula returns S(t; B); s_k >= 0; sum of s_k = S; S^V_dia(n) <= S(2n; B)
  (Lemma BND (i)). Any failure = code error; stop and fix.
- G1 (SHELL shares, M1, b = 8, 12, 16, m a in {2, 4, 6}, t = a, schedule one site per face per step to the unit
  cube): report S, S_n/S against |Q_n|/|B| = 8/b^3, the first-shell share s_0/S, and sum over k < n of s_k / S.
  The reading of 3.2 ("the unit end carries about its volume share; the cost is a volume sum") FAILS if
  S_n/S > 10 x 8/b^3 in some instance with m a >= 4, or if sum over k < n of s_k < 0.5 S.
- G2 ((V) diamond, M1, b = 8, 12): S^V_dia(n) for n = b/2 - 1 (to side 2... the unit cube) against S(2n; B) and against
  S_n(2n). The reading of 3.3 FAILS if S^V_dia(n) >= 0.5 S(2n; B) in some instance.
- G3 (Lemma HALF, M2, beta 2.3 and 2.6, even a = 2..12): X(a; Q_pl) and L(a) := ||P^(a/2) g_p||_(L^2(nu)), g_p the
  centred spatial plaquette. Fit decay rates. The reading of 3.4 (e) FAILS if the fitted rate of L(a) exceeds
  0.75 E_1 (it predicts E_1/2 for L and E_1 for X).
- G4 (massless limit, M1 with the zero mode removed, fixed ratio r = b/a = 4, b = 8, 12, 16): the scalar analogue of
  the cone's L^2 lower bound, V(a) := a b^3 sqrt(2) (C A^a)_xx (one-sided influence of the far time boundary on
  phi_x^2, times the number of sites of the slab). Prediction (4.1): V does not fall as a grows at fixed ratio.
  FAILS if V(a) falls by more than a factor 2 from b = 8 to b = 16.
Runs under `python3 scripts/lab_ops.py numeric-lock`, one job, BLAS threads 1, nice 10, self-stop above 2 GB RSS.
Scripts and logs: `library/guide/lane965/`.

**Results (GUIDE; lock holder lane965-opus, run 14:00:00Z-14:00:08Z, 71 percent memory free, one thread, nice 10,
peak RSS 1.13 GB; log `library/guide/lane965/logs/squeeze_guide.log`, script `squeeze_guide.py`; recheck
`recheck_shells.py`, log `logs/recheck_shells.log`).** The GUIDE schedule cuts the periodic box to side b - 2 at
the first step, then removes one layer per face per step down to side 2 (the unit cube of 8 sites; n = b/2 - 1).
- **G0: PASS.** Shell formula on the full box against the mode formula: relative mismatch at most 2 x 10^-11
  (4 x 10^-9 absolute at S = 8680). Every s_k >= 0. S^V_dia(n) <= S(2n; B) in all four G2 instances. numpy's
  slogdet printed floating-point warnings; `recheck_shells.py` recomputed two instances (b = 12, r = 2 and b = 16,
  r = 4, m a = 4) by eigenvalue log-determinants with warnings turned into errors: no warning, and the values agree
  with the main run to the digits shown (S_1 = 0.12234 and 3.7837; S_n = 1.6054 x 10^-3 and 6.1315 x 10^-3). The
  warnings are spurious (as in row 960's log).
- **G1 (SHELL shares): the reading of 3.2 is NOT refuted.** In all 18 instances the decoupling term carries
  97.8-100 percent of the seed: sum over k < n of s_k / S = 0.978-0.996 at ratio 2 and 0.995-1.000 at ratio 4. The
  unit end carries S_n/S = 0.0040-0.0215 at ratio 2, which is 1.2-3.3 times its volume share 8/b^3 (criterion
  bound 10 times), and 2 x 10^-5 to 5 x 10^-3 at ratio 4 (below its volume share: at short time the light modes
  dominate, and they are spread over the box). The first cut alone carries s_0/S = 0.19-0.56 at ratio 2 (close to
  or below the outer shell's volume share 1 - (1 - 2/b)^3 = 0.58, 0.42, 0.33 for b = 8, 12, 16) and 0.40-0.99 at
  ratio 4. Example, b = 16, r = 2, a = 8, m = 0.5: S = 0.1505, S_n/S = 0.0049, s_0/S = 0.2175, the rest 0.9951.
- **G2 ((V) diamond): the reading of 3.3 is NOT refuted.** S^V_dia(n)/S(2n; B) = 0.030, 0.024 (b = 8; m = 0.5, 1)
  and 0.0084, 0.0073 (b = 12). The time squeeze keeps 1-3 percent of the seed at time 2n, and in all four
  instances it is BELOW the unit share S_n(2n) (3.3 x 10^-3 against 4.6 x 10^-3; 3.6 x 10^-4 against 4.0 x 10^-4;
  1.3 x 10^-4 against 2.2 x 10^-4; 2.8 x 10^-6 against 3.3 x 10^-6). Spreading the squeeze over time loses at least
  as much as squeezing at once.
- **G3 (Lemma HALF on the one-plaquette box): the reading of 3.4 (e) is NOT refuted; it is exact here.** Fitted
  rates for a = 6..12: X(a; Q_pl) decays at 3.5643 = E_1 and L(a) = ||P^(a/2) g_p|| at 1.7822 = E_1/2 (beta 2.3);
  3.3990 and 1.6995 at beta 2.6. L/X grows from 12.9 (a = 2) to 7.1 x 10^8 (a = 12) at beta 2.3. The overlap of the
  plaquette with the first excited level is large: <psi_1, x psi_0> = -0.365 (2.3), -0.336 (2.6). So a worst-case
  squeeze bound, which is at least L, needs the time extent doubled to reach the same size as the true term.
- **G4 (massless scalar, zero mode removed, ratio 4): the prediction of 4.1 is NOT refuted.** The cone's L^2 lower
  bound times the slab volume, V = a b^3 sqrt(2) (C A^a)_xx, GROWS with the box at fixed ratio: 9.1, 17.7, 28.5,
  59.5, 103.6 for b = 8, 12, 16, 24, 32. The true X stays of order one to ten (13.5 down to 6.6): no seed, and a
  cost that does not fall.
- **G4' (scope note of 3.4 (e)).** Massive scalar m = 0.5, ratio 4, observable phi_x^2: V/X = 0.65, 1.31, 2.27,
  4.70, 7.30, 9.93 for a = 2, 3, 4, 6, 8, 10, roughly linear in a and not exponential. As the scope note says, in a
  free field the even observable couples first to the two-particle threshold, so there is no square-root loss in
  the rate, only a polynomial factor. The loss of G3 needs an observable that creates the lightest state, as the
  plaquette does in SU(2).

**What Step 6 changes.** Nothing in the verdict of Steps 3-5; it adds the scope note to 3.4 (e) (written before
the run, at 13:58Z) and measures the sizes: the decoupling term is 98-100 percent of the seed in the free scalar,
the time squeeze keeps 1-3 percent, and the square-root loss of HALF is exact in the one-plaquette box.
