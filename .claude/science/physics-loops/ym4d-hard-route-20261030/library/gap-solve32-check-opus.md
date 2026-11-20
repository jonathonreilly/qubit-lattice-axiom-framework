lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:21Z

# Check of row 1283 (`library/gap-solve32-astra62.md`), FINISH row 1289

Research-stage working state. It grants no status and is not a public claim.

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, at commit 1ce538a51
on branch `claude/ym4d-hard-route`. The checked file was written by a
gpt-6-astra lane (row 1283), so this is a cross-provider check. It is one
check by one model; it is not an independent derivation unless a step below
says it uses a different route.

## Plan (at most eight steps; each response does one step and appends here)

1. Read FINISH rules (Build on published work, efficiency), the row 1283
   text, and the checked file in full; list its numbered claims and the
   earlier rows it cites.
2. Check the short-time slice information bounds (29)-(32), line by line.
3. Check the recovery (35) of flux sector ratios from neutral histories.
4. Check the endpoint removal (36)-(40).
5. Check everything else in the file (setup, definitions, remaining
   numbered statements, the conclusion), with cited earlier rows read where a
   step depends on them.
6. Decide whether the main comparison is a restatement of an earlier row
   (grep `library/open-core.md`, FINISH rows, cited files).
7. Optional numeric guide only if useful and memory allows (guides only;
   no verdict rests on it).
8. Verdict table per statement and the RESULT line.

## Step log

(Each step appends below as it finishes.)

### Step 1 (done 14:35Z): inventory and cited rows

Read in full: `library/gap-solve32-astra62.md` (541 lines, at 1ce538a51), the
row 1283 text, GOAL.md, FINISH.md (opening sections, How we work, Working
efficiently, Rules).

Numbered claims of the checked file, by section and line:

| Lines | Claims | Label in file |
|---|---|---|
| L16-56 | (1) adjoint-mode count, (2) two-plaquette defect, (3) block Poincare, (4) | PROVED |
| L59-84 | (5) rare-slice probability, (6) energy-band bound, (7) trace ratios | PROVED; L84 OPEN |
| L87-126 | (8) annealed Green bound, (9) kernel domination, (10) walk bounds | PROVED |
| L129-170 | (11) temporal law, (12) covariance, (13)-(14) patch coherence | PROVED |
| L173-220 | (15)-(18) recovery of Ad g_x, (19) replica overlap | PROVED |
| L223-268 | (20)-(22) chessboard and strip bounds, (23) global sign | PROVED |
| L271-343 | (24)-(26) contraction, (27)-(28) endpoint recovery | PROVED; L343 ARGUED |
| L346-401 | (29) separating event, (30) prism identity, (31)-(32) information | PROVED |
| L404-451 | (33) twist candidates, (34) decoding, (35) sector ratios | PROVED |
| L454-487 | (36) singlet bound, (37) restricted kernel | PROVED |
| L490-521 | (38) orbit volume, (39) layer information | PROVED; L521 OPEN |
| L524-539 | (40) rank-one distance | PROVED; L537-539 OPEN |

Earlier rows the positive claims depend on, with their checks (FINISH RESULT
lines read): row 1141 (`gap-crux2-astra62.md`, check 1142 HOLDS); row 1145
(`gap-solve2`, check 1146 HOLDS); row 1149 (`gap-solve4`, check 1150 HOLDS);
row 1151 (`gap-solve5`, check 1152 HOLDS); row 1153 (`gap-solve6`, check 1154
HOLDS); row 1155 (`gap-solve7`, check 1156 HOLDS); row 1215 (`gap-solve23`,
check 1221 HOLDS); row 1231 (`gap-solve26`, check 1235 HOLDS, one credit
correction); row 1262 (`gap-solve30`, check 1271 HOLDS); row 1272
(`gap-solve31`, check 1282 HOLDS). Each was checked once by Claude Opus 5.5;
those checks are not evidence here. I read the cited statements and proofs
where a step below depends on them.

### Step 2 (done 14:58Z): the short-time slice information bounds (29)-(32)

Inputs read for this step: row 1231 (`gap-solve26-astra62.md` L17-135:
(1), (2), (4), (7)-(11)); row 1151 (`gap-solve5-astra62.md` L302-317: (24)
and the pointwise density bound at L313); row 1153 (`gap-solve6-astra62.md`
L80-110: (3)-(6)).

**(29), L350-386: HOLDS.** Redone by hand:

- *Gaussian separation of means (L356-362).* For one colour, two centred
  Gaussians with variances v and covariance D give
  E e^{-a^2-b^2} = det(I+2Sigma)^{-1/2} = [(1+2v)^2-4D^2]^{-1/2}; three
  independent colours give the joint mean [(1+2v)^2-4D^2]^{-3/2}, and
  independence gives (1+2v)^{-3}. D(s) > 0 on [1,2] since the integrand of
  row 1231 (10) is nonnegative and not a.e. zero; D decreases in s, so the
  least joint mean is at s = 2. Since r is the largest power of two at most
  k, k/r lies in [1,2). Image terms: with numerator at most |xi-hat|^2,
  2 sinh(omega) >= c|xi-hat| and k <= N/2, the time images sum to at most
  2e^{-N omega/2}/(1-e^{-N omega}); with |W(q)|^2 <= C r^4 and xi = 2 pi m/N
  the frequency sum is at most C r^4 N^{-4}. So the finite-cutoff Gaussian
  means are within o(1) of the limits, uniformly in k/r in [1,2]. Correct.
- *Prism identity (30), L364-374.* For F = dB, the Bianchi relation gives
  F_12(t+1,z) - F_12(t,z) = (nabla_1 F_02 - nabla_2 F_01)(t,z) up to the
  square convention, and summation by parts (f has compact support) gives
  a_{j+1} - a_j = <nabla_1^* f, F_02> - <nabla_2^* f, F_01>. The telescoping
  identity is exact: r^{-1} sum_{j<r} a_j = a_0 + sum_{i<=r-2}(1-(i+1)/r)
  (a_{i+1}-a_i). Each face carries one coefficient, so the squared l2 weight
  is at most r^{-1}||f||^2 + r sum_i ||nabla_i^* f||^2 <= C_phi, using
  ||f||^2 <= C r and ||nabla f||^2 <= C/r. Only dF = 0 inside the prism is
  used, so any open box containing the prism suffices. HOLDS.
- *Comparison costs (L376-384).* Action cutoff (L236): Z >= e^{-CV log beta}
  from the radius-beta^{-1/2} Haar balls (each plaquette deficit <= C/beta,
  6V plaquettes, ball measure ~ beta^{-3/2} per link), so
  P(S_W > C_0 V log beta) <= e^{-(C_0-C)V log beta}. A bad box needs internal
  deficit >= c/h^8, so on the cutoff the bad boxes cover a fraction
  <= C h^{12} log(beta)/beta = o(1) (gamma < 1/12). Full-to-linear error of
  the global mean: each product moves by an absolute constant times the two
  reading errors; each reading error is <= ||f||_2 <= C sqrt(r) times the l2
  colour error on its faces; Cauchy-Schwarz over n_p ~ V/r^4 readings and
  row 1231 (8) give C r^{5/2}(h^{-1} + r h^{-7/2}) sqrt(S_W/V), which is o(1)
  because gamma > 4 delta > 5 delta/2. I recomputed this exponent.
  Open-box to periodic coupling: Tr(P_H - P) <= CV(1/h + h/N) (row 1231 (1));
  the difference is exact inside each kept cube, so (30) applies; the error
  per reading is C r^2/sqrt(h) = o(1) exactly because gamma > 4 delta.
  Lipschitz constant C/sqrt(J L_0^3) of the average: the reading map Z ->
  (A_i) is linear with bounded norm only through (30) on exact arrays, and
  the reference arrays are exact in each box, including the diluted Gaussian
  replacements. Correct.
- *Density transfer (L384).* Row 1151 L313 states the pointwise bound: the
  law of the tree-chart array with bad boxes replaced by independent
  Gaussians has density at most exp(CV Delta) times the product Gaussian
  (per-box factor 1 + e^{C' b^3}, V/b^4 boxes). A pushforward keeps a
  pointwise density bound. With r^4 Delta_h = o(1) this beats
  exp(-cV/r^4). Correct; the remark that an entropy bound alone would not
  suffice is right.
- *Chessboard and counting (L376, L386, L234).* The product of two
  independent Wilson tori is reflection positive for the diagonal site
  reflections (its action is a sum of two Wilson actions). Tile functions
  read only spatial links on two interior slices (times 2r, 2r+k <= 4r < T),
  inside the closed tile; reflected prisms fit forward or backward. Per tile
  cost exp(-c 8^4 L_0^3) with c independent of L_0 (the forced deviation and
  the overlap bound do not depend on L_0). Union over at most 2^G subsets and
  c L_0^3/2 > 2 log 2 give exp(-c' L_0^3 G), G = (N/(8 L_0 r))^3 ~ (N/k)^3.
  Dyadic N, r, L_0 make tiles divide the periods. Correct.

**(31), L391-396: HOLDS.** The pair density e^{-g_N}K_k(x,y)K_{N-k}(y,x),
the bound K_j(x,y) <= sqrt(K_j(x,x)K_j(y,y)) for a continuous kernel of a
positive operator, the normalizer bound by Cauchy-Schwarz and Mercer
(int K_j(x,x) dx = Tr U^j), and the chain rule
D(P||nu x nu) = I + D(P_1||nu) + D(P_2||nu) give I_k <= g_k + g_{N-k} - g_N.
Convexity: (g_N - g_{N-k})/k >= (g_{N-k} - g_k)/(N-2k), and g_{N-k} >= 0
(the Perron term), give the second inequality. Data processing covers the
neutral orbits.

**(32), L397-401: HOLDS.** Affinity split: int_A sqrt(pq) <= sqrt(P(A)Q(A))
<= sqrt(Q(A)), likewise on A^c; Jensen gives D >= -2 log(affinity). Row 1153
(5) is (m^3/N_sites) log Tr[(F/||F||)^m] -> pi^2/15 for m -> infinity with
m^4 eps_beta -> 0, F the gauge-projected transfer with temporal holonomy;
k <= beta^delta, delta < 1/48 gives k^4 eps_beta -> 0. The file's note that
row 1153's N counts sites is right. Lower bound from (29) for large N/k.

Notes (no correction needed): the limit used in (29) at L362 is uniform in
s in [1,2] because row 1231's majorant in (10) does not depend on s >= 1.
