# T21 pre-registration (written before any test script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). Date 2026-09-29.

Wall: rest energy (Dirac mass) has no source in the rules (L05-W6, L02-W12).
Working thesis to be tested (suggested, not yet checked): every in-framework rest
energy is a Z2 order parameter for single-site translation (a chessboard, momentum
(pi,pi,pi)) coupled to the walker. The lane prices the chessboard record gas at
"g <= 9/62500, otherwise never". I suspect (a) that price is a proof artifact, and
(b) whether the chessboard yields a walker gap depends on how records form (T01).

Common definitions
- Walker: H = sum_j sigma_j S_j on the L^3 torus (L even), S_j=(T_j-T_j^*)/(2i), 2 coin states.
- Record coupling (block 79): H_tot = H + c * n_x (scalar site coupling, both coin states).
- Ideal chessboard n=(1+eps)/2: spectrum c/2 +- sqrt(|s|^2 + c^2/4), empty interval [0, c] (width c).
- Record gas (block 81/117, no contents, zeta=g^-3): weight g^(#bonds with equal occupancy / 2).

## Test A: the record gas is the 3D Ising antiferromagnet; where does it order?
A1 (exact identity) PASS: on >=200 random configurations of a 4^3 torus, the log-weight
   ln w_gas - ln w_Ising(K=ln g/4) is one constant (spread < 1e-9). FAIL: not constant.
A2 (threshold) PASS: Binder-cumulant curves of the staggered magnetization for L=6,8,10
   cross within g in [0.39, 0.43] (prediction g_c = exp(-4 K_c) = 0.4119 with K_c=0.221655).
   FAIL: crossing outside [0.37, 0.45] => my identification (or code) is wrong; report as such.
A3 PASS: <|sigma|> (staggered magnetization per site, L=8) >= 0.90 at g=0.25 and >= 0.99 at g=9/62500;
   defect density p = P(sigma_x=-1) at g=0.25 is < 0.03.
Reading if pass: the lane's "very expensive" price (g<=9/62500) is a proof bound, ~2900x below the true
   threshold; the chessboard exists at O(1) bond cost in the gas.

## Test B: walker spectrum on typical Gibbs arrangements (block 117's open item)
c in {1, 2, 4}, L=8 (and L=12 for one setting), >=20 independent equilibrated samples per g,
g in {0.25, 0.35, 0.60 (disordered control), 1.0 (free control)}.
Metrics per sample: w_max/c = largest empty interval in the spectrum (ideal 1.0);
f_in = fraction of eigenvalues with E in (0.1c, 0.9c) (ideal 0); dmin = min |E - c/2| (ideal c/2).
PASS (gas -> gap viable at O(1) parameters): at g=0.25, c=2: median w_max/c >= 0.5 and median f_in <= 0.05.
FAIL: median w_max/c < 0.25 or median f_in > 0.15 (defect bound states fill the gap).
Controls: g=1.0 must show f_in > 0.3 (no order, no gap); if not, the metric is broken.
Also record how f_in and dmin scale with L (8 vs 12) at g=0.25, c=1 and c=2.

## Test C: formation order (T21 depends on T01)
Records are permanent (axioms), so a final configuration is a formation history, not obviously a Gibbs draw.
Three formation orders on the L=8 torus, hard NN exclusion, all permanent, all "one record per site":
 (i) lexicographic greedy independent set; (ii) random-order sequential adsorption (RSA) to jamming;
 (iii) checkerboard-sweep order (even sites first) as control.
PASS-for-thesis (mass depends on formation order): (i) gives the perfect chessboard, w_max/c = 1 exactly (to 1e-9);
   (ii) RSA has |global staggered order| < 0.2 and median f_in >= 0.15 at c=2 (gap filled), i.e.
   the same walker and coupling has a rest energy under one formation order and none under another.
FAIL: RSA also gives median w_max/c >= 0.5 and f_in <= 0.05 (formation order harmless for the gap).

## Test D: interaction-driven chessboard (outside route: Gross-Neveu / CDW on the sea)
Mean-field (Hartree) gap equation for a one-mode-per-site staggered sea with NN repulsion V:
 1 = 3 V < 1/sqrt(sum_mu sin^2 k_mu + Delta^2) >_BZ.
PASS (threshold structure): finite V_c = 1/(3 <1/|s|>) exists (3D Dirac density of states vanishes),
   Delta(V) = 0 for V < V_c and Delta ~ sqrt(V - V_c) just above; Delta/t = O(1) at V = 2 V_c.
This shows any interaction-generated mass is a threshold phenomenon of lattice size unless tuned.
It is a mean-field estimate (Hartree only), labelled as such; it is not evidence about the framework.
FAIL: no finite V_c (Delta > 0 for all V > 0).

Outcome rule: if A and B pass and C passes, the wall is PRICED (not passed): mass = a supplied
formation order (T01) + record ensemble (g<0.412) + walker-record coupling c; the lane's "very expensive"
threshold is corrected. If C fails, formation order is harmless and the price shrinks to (g, c).
If B fails, the gas route is dead at O(1) g for a robust reason (defect states).

## Amendment 1 (written after the first run of Test B at L=8, before Test B2/C)
Test B result at first look (t21_B_L8.out): the pre-registered whole-gap metric was ambiguous. The ordered gas
gave f_in ~ 0.02 (pass) but w_max/c ~ 0.27 at c=2 (neither pass nor fail); disordered controls gave f_in ~ 0.25
(my >0.3 control guess was too high; contrast with ordered is x10, so the metric works).
Reason: isolated flipped sites are impurities that bind localized levels in the gap, like donor levels in a
semiconductor. Whether the RATIONAL notion of rest energy survives is the band-edge gap of extended states.
New pre-registered Test B2 (L=8, eigenvectors, inverse participation ratio IPR = sum_x (sum_a |psi|^2)^2, states
with IPR*N > 10 called localized):
 PASS (rest energy = band-edge gap survives in the ordered gas): at g=0.25, for c in {1,2}, median over samples of
   d_ext = min over EXTENDED states of |E - c/2|, in units of c/2, is >= 0.5, and localized in-gap states number
   < 3 per flipped site.
 FAIL: d_ext/(c/2) < 0.3 or extended states inside (0.1c,0.9c) have fraction > 0.02.
 At the disordered control g=1.0: d_ext/(c/2) should be < 0.1 (no gap).

## Results against the pre-registered readings (added after all runs; outputs are the *.out files here)
- A1 PASS: spread of ln w_gas - ln w_Ising <= 8.5e-14 over 300 configs at each of 4 values of g (t21_A.out).
- A2 PASS: Binder crossings 0.408 (L 6,8), 0.413 (8,10), 0.411 (6,10); prediction g_c = exp(-4*0.221655) = 0.412.
  Wolff vs Metropolis <|M|> at L=6, g=0.30: 0.9086 vs 0.9089.
- A3 PASS: <|sigma|> = 0.956 at g=0.25 (L=8 and 12), 1.000 at 9/62500; defect density 0.022 (< 0.03).
- B (first version) AMBIGUOUS: f_in 0.0205 (pass) but w_max/c 0.273 (neither); control f_in 0.245 (<0.3 guess). -> Amendment 1.
- B2 PASS at g=0.25: c=1: extended edge 0.89(c/2) [L=8], 1.00 [L=10], localized levels 0.18 / 0.09 per flipped site;
  c=2: no extended states in the window, localized 2.00 per flipped site (L=8 and 10), edge 1.00 (finite-size corner
  degeneracy, see t21_B3_inspect.py: E=0 and E=c stay exact while defects on the same sublattice number fewer than 4).
  g=0.35 (defect density ~0.10): c=1 edge 0.50, 12 extended states in the window (1%) -> gap halved.
  Control g=1.0: edge 0.006-0.014 (no gap). PASS conditions met; FAIL conditions not met.
- C PASS for the thesis: lexicographic greedy = the even sublattice exactly (w_max/c = 1.0000000); random-order RSA with
  hard NN exclusion: jam density 0.306, sublattice imbalance 0.176 (<0.2), in-gap fraction 0.203 (>=0.15) at c=2;
  soft sequential formation stopped at density 1/2 (g=0.25, 0.05): imbalance 0.145, 0.255; in-gap 0.129, 0.089
  (Gibbs g=0.25: imbalance 0.951, in-gap 0.024; unordered: 0.038, 0.240). At c=1 contrast is 4x (RSA 0.039, soft 0.0156,
  Gibbs 0.0039, unordered 0.0156). Density-matched (soft) comparison is the fair one; RSA is at a different density.
- D PASS: <1/|s|> = 0.9106; V_c = 0.3661 (Dirac velocity 1); Delta = 0.42 at 1.1 V_c, 1.84 at 2 V_c; Delta ~ sqrt(V - V_c).
Caveats: contentless gas only (contents change the weights); scalar coupling only; L <= 10; ~20 samples per point;
same-family check, not independent; Test D is Hartree mean field (no Fock, no fluctuations) and is not about the framework.
