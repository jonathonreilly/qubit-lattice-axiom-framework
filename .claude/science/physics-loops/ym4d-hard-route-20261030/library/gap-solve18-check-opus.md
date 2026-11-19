lead: anthropic/claude-opus-5-5/max laptop-subagent

# Check of gap-solve18-astra62.md (FINISH row 1185)

Target: `library/gap-solve18-astra62.md` (row 1178, gpt-6.2-astra max, unchecked).
Checker: Claude Opus 5.5, max effort, by hand, line by line.

## Plan (at most eight steps)

1. Read the target file in full. List its statements, labels and citations.
2. Read the cited earlier rows: FINISH.md RESULT lines, the cited
   `library/gap-solve*-astra62.md` files and their `-check-opus.md` checks,
   and `parts/gap.md`.
3. Check positive claim 1: (W), given the one-cube neutral bound, is
   equivalent to the clustering test (41).
4. Check positive claim 2: (17), (27), (36), the interface energy as electric
   splitting rates, and its growth bound in compact width.
5. Check positive claim 3: (40)-(42), open sheets versus flat backgrounds.
6. Check positive claim 4: the local centre-flux recovery (1) and its lift.
7. Check everything else. Check that GUIDE, ARGUED, OPEN labels and the
   RESULT line agree with the body. Run a small numeric guide only if it helps.
8. Write counts, per-statement verdicts, what was not checked, RESULT line.

## Step results

### Step 1. Inventory of the target (done)

The target has 554 lines. It holds 88 PROVED blocks (counted by script),
2 OPEN blocks at the start (L15, L19), 1 OPEN block at L165, 2 OPEN blocks
at the end (L548, L550), 7 GUIDE blocks (L3, L5, L9, L11, L21, L546,
L552), and no ARGUED block. It has
43 numbered displays, (1) to (43). The RESULT line is L554.

Cited lane rows, with the check status found in FINISH.md at the time of
this check:

- row 1139 (`gap-frameless-2d-astra.md`): checked, all 14 hold (row 1140);
- row 1141 (`gap-crux2-astra62.md`): checked, all 34 hold (row 1142);
- row 1157 (`gap-solve8-astra62.md`): checked, holds (row 1160);
- row 1161 (`gap-solve9-astra62.md`): checked, holds after a credit-only
  correction (row 1162);
- row 1165 (`gap-solve11-astra62.md`): checked, holds after a
  constants-only correction (row 1166);
- row 1167 (`gap-solve12-astra62.md`): checked, holds after a
  hypothesis-only correction (row 1168);
- row 1173 (`gap-solve15-astra62.md`): checked, holds (row 1174);
- row 1175 (`gap-solve16-astra62.md`): checked, all 68 hold (row 1176);
- row 1177 (`gap-solve17-astra62.md`): checked, all 58 hold (row 1182);
- `gap-crux-restate.md`: Theorem S, Lemma K, Lemma X, Lemma E' (read).

The GUIDE at L552 says rows 1175 and 1177 are unchecked "at the assignment
pin". That was true when row 1178 started (21:06Z). Both rows have since been
checked (rows 1176 and 1182). This is a stale label, not an error.

### Step 2. Cited statements read in the lane files (done)

I read each cited statement and its proof where a step of the target
depends on it.

- `gap-crux-restate.md` L174-L219: Lemma K (deficit non-negative, convex,
  non-increasing), Lemma X, Lemma E, Theorem S, Lemma E' (L213:
  `1+S(a;h) <= (1+S(a;b))^(h/(b-a))` for `h >= b > a >= 3`). The setting
  needs a symmetric `W(a,b)` with a positive trace-class transfer. The
  target applies it to `Z` and to `V = 2^-3 sum_B Z_B`. Both are symmetric
  under axis exchange (the set of 64 twists is invariant) and both are positive
  traces in every frame. So the setting holds for both.
- `gap-zd-astra.md` item 18 (L403-L420): the corrected (W). The target's L15
  copies it exactly.
- Row 1161 (`gap-solve9-astra62.md` L111-L190): the one-cube alternatives
  I/II (9), the finite-aspect theorem, the consumer at L148 (alternative I
  with uniform tolerance gives (W)), K = 512 at L215. Checked in row 1162.
  The target's "ordinary seed" is I and its "all-magnetic neutral seed"
  (competing branch) is II. The target's use matches.
- Row 1157 (`gap-solve8-astra62.md` L25-L52), (1): `1-lambda_{chi,2}^s >=
  (1-rho^s)/4`. At s = 1 this is the bound `lambda_{chi,2} <= (3+rho)/4` that
  the target uses in (19), (28), (36). The proof is general for a reversible
  positive transfer with the flip group, so rectangular boxes are covered.
- Row 1175 (`gap-solve16-astra62.md`): (14) at L139-L144 (stack parity
  bound by `prod_x tanh J_x`); the eigenfunction rounding at L268
  (`Var |h| <= d/gamma`); the three-cell factor (29) at L306-L313.
- Row 1177 (`gap-solve17-astra62.md`): (2) at L34-L39 (Lemma X for the
  planar pressure); the tile estimate (4) at L62-L67; (9) at L110-L114 (the
  same propagation as the target's (5)); (22)-(24) at L262-L299.
- Row 1141 (`gap-crux2-astra62.md` L55-L68), (3): `P{|u x n| <= t | other
  links} <= 4(1+6b) t^2`, valid for a plaquette holonomy with its other three
  links fixed.
- Row 1167 (`gap-solve12-astra62.md` L13-L20), (1): directional deletion
  `E exp(beta sum_D a_p) <= z_beta^(-|D|)`, by `C_0 <= C_beta` and trace
  Hoelder.
- Row 1173 (`gap-solve15-astra62.md` L108-L114), (8): `Var(d.z) >=
  c|d|^2/(1+h)^2 + ...`.
- Row 1165 (`gap-solve11-astra62.md` L283-L294), (19) and the one-sign
  test with `H = ker chi`, `u = 2 floor(n/1024)`, threshold 1/32.
- Row 1139 (`gap-frameless-2d-astra.md`) through row 1177's restatement
  (L270-L276); the target re-proves its small-angle variant directly.

No cited statement is used beyond what its source proves.

### Step 3. Claim 1: (W), given the one-cube neutral bound, iff (41) (done)

The chain is: row 1161 dichotomy; (5) and (4); (37), (38); the
ordinary-branch bound at L480; (42); and, for the competing branch,
(17), (19) and (27), checked in Step 4. I rederived each link.

- **L81, (5): HOLDS.** For `A = Z` or `V`, `V` is the sum of the neutral
  parts of the eight static sectors in any frame (Fourier inversion of the
  temporal twists). `0 < Z_B <= Z` follows by removing a commuting temporal
  flip in successive frames, since `Tr(T^a C) <= Tr T^a` for a flip `C`
  commuting with `T >= 0`. So `Z/8 <= V <= 8Z` and the top eigenvalues
  agree. Propagation: `d = 2^k n_0 <= w/32`, so `32 <= w/d < 64`; Theorem S
  gives `S_A(d/2; d^3) <= q^{d/n_0}/5041`; E' to `(16d, w, w)` at time `d/2`
  costs `32 (2w/d)^2 <= 2^19` on `log(1+S)`; each doubling step costs
  `64/31 < 4`, and `(1+x)^4 - 1 <= 15x` for `x <= 1` gives
  `S_{i+1} <= 225 S_i^2`; the last enlargement costs `< 4`; and
  `S(r) <= S(u)^{r/u}` for `r >= u`, `S(u) <= 1` (l^p monotonicity).
  Every E' use has `H >= h > t >= 3`.
- **L68 and L87, (4): HOLDS.** Ordinary: with direction 1 as time the 13
  twist is `Tr(T^a C_3)`, so `1 - Z_13/Z <= 2 S_Z(a; b,w,w)`; (5) applies with
  `s = b in {a, 2a}`, `r = a >= s/16`. Then `Tr M^{2a} >= 1 - Ce^{-ca/n_0}`,
  `Tr M^a <= 1 + Ce^{-ca/n_0}`, and `||M||^a >= Tr M^{2a}/Tr M^a` for
  `M >= 0`. `||M|| <= 1` by removing the temporal flip and taking roots.
  Competing: the strictly positive static-13 vacuum is fixed by all flips,
  so it lies in a non-periodic neutral summand of `V`, and
  `e^{-rE} <= S_V(r; a,w,w) <= Ce^{-cr/n_0}` for `r >= a/16`. Upper bound:
  the twist flips `w` spatial plaquettes per slice, so the multipliers and
  hence the sandwiches are ordered within `e^{+-2 beta w}`.
- **L456, (37): HOLDS.** `d_s d_t L = beta^2 Cov_{s,t}(sum_{S_1} W_p,
  sum_{S_2} W_q)`. Flipping the 3-links at `x_3 = 0` for `1 <= x_1 <=
  floor(a/2)` negates exactly the two 13-columns (23-, 34- and inner
  13-plaquettes contain two flipped links or none). So `L(s,t) = L(-s,-t)`,
  and each stack holds one face of each of the `bw` 13-planes, so
  `L(1,-1) = log Z_13`. The double integral is `2[-log z]`.
- **L464, (38): HOLDS.** Ordinary: `1 - z <= 2 S_Z(a_b; b,w,w)`.
  Competing: by (17), (19), `x_b = a_b Delta(b)` has
  `log x_b = (theta - T) b + O(log b)`; the error `e^{-d a_b}` is doubly
  exponentially small; `(1-e^{-1}) min(x,1) <= 1-e^{-x} <= min(x,1)`;
  `1 <= Z_0/lambda^a <= C`. So `-b^{-1} log z -> (T - theta)_+`, also at
  `theta = T` (then `-log z = O(log b)`).
- **L480 (ordinary-branch control): HOLDS.** Direction 1 as time; the
  altered layer kernels lie in `[e^{-2 beta N} F, e^{2 beta N} F]`; an
  inserted bounded function has absolute kernel at most `K_s`; normalized
  norms `<= e^{2 beta N}`; `||(F/lambda)^d - P||_1 = S_Z(d; b,w,w) <=
  Ce^{-cd/n_0}` for `d >= floor(a/2) - 1 >= b/16`; trace-norm replacement
  error `<= 2C e^{4 beta N - c a/n_0}`; exact denominator `>= e^{-4 beta N}`;
  the rank-one replacement factorizes with values of modulus at most one.
  So `|Cov| <= C e^{8 beta N - c a_b/n_0}`.
- **L472, (39): HOLDS.** Competing: (27) gives `T(w) > 1` for all large
  `w`; (38) at `theta = 1` and `C <= 4 sup|Cov|` give the stated liminf
  `>= (T-1)/(2 beta^2 w^2) > 0`. Ordinary: L480 with `N = bw`,
  `a_b = ceil(e^b)` gives `b sup|Cov| -> 0` for every `w >= K n_0`.
- **L504, L516, (41)-(42): HOLDS.** `Z_{i+1,j}/Z_{ij} = E_{ij} X_{p_i}` and
  `Z_{i+1,j+1}/Z_{ij} = E_{ij}(X_{p_i} X_{q_j})`, so `l_ij` is as displayed.
  Telescoping gives `sum l_ij = log(Z_00 Z_NN/(Z_N0 Z_0N)) = 2[-log z]`
  (`Z_NN = Z_00` and `Z_N0 = Z_0N = Z_13` by the same link flip). At a pair
  with `l_ij >= 2[-log z]/N^2 >= 0`, `Cov(X,X') >= l_ij E X E X' >=
  e^{-4 beta} l_ij`, and the affine change to `B` divides by
  `(e^{2 beta} - e^{-2 beta})^2`. This is (42). Competing: (38) at
  `theta = 1` with `T > 1` gives a positive liminf. Ordinary: L480 applies
  to every prefix (prefix layers differ from `F` by at most `e^{+-2 beta N}`,
  `B in [0,1]`). The one-bit reading and the perimeter count `2w + 2` are
  correct.
- **L111 (8) and L115: HOLDS.** At each fine cutoff exactly one branch holds
  (row 1161), with seed side `n_{0,j}` and a common margin. A single width
  `w >= K n_{0,j}` with a zero liminf excludes the competing branch at that
  cutoff; exclusion at all fine cutoffs gives alternative I with uniform
  tolerance, hence (W) by row 1161 L148. Conversely (W) gives the ordinary
  seed after enlargement and then (4).

Verdict for claim 1: the equivalence of (W), given the one-cube neutral bound,
with (41) **HOLDS**. Remark: with `a_b = ceil(e^{theta_j b})` and
`theta_j < c_q/n_{0,j}`, the same test would need only (4), not (27). The
stated `a_b = ceil(e^b)` needs (27), which holds (Step 4).

### Step 4. Claim 2: (17), (27), (36), interface energy as splitting rates (done)

- **L252, (18): HOLDS.** `u = ceil(C_q n_0 log(2+a))`; (5) on `(2u,w,w)` at
  time `u` (`s = 2u >= w`, `r = u >= s/16`); E' from `2u` to `a` costs
  `a/(2u-u) = a/u`, and `(a/u) C (2+a)^{-c C_q} <= 1` for large `C_q`. Then
  `Z_13 <= Z_0 <= 8V <= 8e lambda_0^u`, and for `b >= u` the two-sided trace
  bounds give `-log z = bE + O(uE + 1) = bE + O(log(2+a))`. The bound
  `z >= e^{-2 beta w b}` also follows directly (the representative flips
  `bw` faces), so the remark after (18) holds for every `b`.
- **L259, (19): HOLDS.** Direction 1 as time on `(b,w,w)`. With signs
  `(-1)^{chi_3}`, `1`, `(-1)^{chi_3+chi_4}` on the long-even characters, the
  three lines follow. The two singly odd characters have identical traces
  by the 3-4 exchange (equal short sides), so they cancel exactly in
  `Z_13`. Long-odd weight: by the parity identity of row 1175 (14) over the
  `ab` disjoint 12-stacks (each one face per 12-plane, `w^2` faces),
  `(Z_0 - Z_12)/(2 Z_0) <= tanh(beta w^2)^{ab}`, which is `O(e^{-da})` once
  `b log coth(beta w^2) >= d` (large `b` at fixed `w`). Neutral excited ratio
  `rho <= e^{-c/n_0}` from (5) for `V` (the periodic neutral sector is a
  summand of `V`). Second levels `<= (3+rho)/4` by row 1157 (1) at `s = 1`.
  Half-time traces: `Tr_chi <= Tr_0 <= 1 + S_V <= C` (all temporal twist
  integrals are positive). Nonempty characters: products of winding traces,
  and the convolution has positive multipliers.
- **L269, (20): HOLDS.** For `L_1 b <= a <= b^2`: the error is
  `O(e^{-dL_1 b}) = o(e^{-2 beta w b}) = o(z)`; `z -> 0` by (4) and (18)
  (`-log z >= bc/n_0 - C log(2+b^2)`); `1 - e^{-a Delta}` and then
  `a Delta` are within constant factors of `z`; logs give (20). With
  `b = floor(a/L_1)`, every `a' in [a,2a]` is in range for large `b`;
  subtraction and a dyadic sum give the rate `O(log(2+a)/a)`; then
  `a = ceil(L_1 b)` gives the last line of (17).
- **L241, (17): HOLDS** (consequence of (18)-(20) and (4)).
- **L276, (21): HOLDS.** Ordinary: `Delta(b) >= c_q/n_0` by (5) for `Z`;
  the two-winding product `f` is an eigenfunction of the electric
  convolution with ratio `r_{1/2}^{2w} > 0` (gauge invariant, central
  one-link convolution); the Rayleigh quotient of `D^{-1} f` and the
  `max/min` ratio `e^{C beta b w^2}` of `D^2` give
  `Delta(b) <= C beta b w^2 - 2w log r_{1/2}`. The character of `f` is
  (even, odd, odd), as needed.
- **L282, (22): HOLDS.** `D(b) >= (1/2 - o(1)) Delta(b)` from positivity of
  `Z_{13+14}` at `a = b^2` (there `b^2 Delta -> 0` and `e^{-d b^2} = o(b^2
  Delta)`). The two regimes and the bounded-`b` case (unique even vacuum
  in direction 1) give the crossover with error `O(log log a)`, using
  `Delta(b) e^{bT}` between fixed powers of `b`.
- **L357, (28): HOLDS.** `Y = (Z_13 + Z_{13+12})/2` is
  `Tr(T^a C_3 (1+C_2)/2)` in direction 1 and `Tr(T_-^b (1+C_1)/2)` in
  direction 2. So `Z_13/2 <= Y <= Z_13`, and the long-odd states drop out
  exactly. The remaining four-character expansion is that of (19), with
  `(3+rho)/4 <= e^{-c'/n_0}`, so the error is `O_q(e^{-d_q a/n_0})`.
- **L368 (uniform thermal time): HOLDS.** Case `h <= w`: E' on three sides,
  cost `(2a/h)^3`, and `8 (a/h)^3 q^{h/n_0}/5041 <= 1` for large `K_q`.
  Case `w < h <= a/2`: (5) on `(2h,w,w)` at time `h`, then E' cost `a/h`.
  Case `a < 2h`: (5) directly (`r = h >= a/16`).
- **L370, (29)-(30): HOLDS.** `y = Y/Z_0 in [z/2, z]`, so
  `e^{-bE}/(16e) <= y <= 8e e^{-(b-u)E}` and `1 <= Z_0/lambda^a <= C`. With
  `d_q L_w/n_0 >= 2 beta w + 1`, the error over `y` is `<= C_q e^{-b}`,
  uniformly in `w`. Then `|-log Delta - bE| <= C + log a + uE`, which is
  (29). For `a >= ceil(w^4)`, `b = floor(a/L_w) >= w` and `b >= 2u(a')`
  for all `a' in [a,2a]` once `w` is large (`a/(w log(2+a))` diverges at
  `w^4`). Subtraction gives `|E(a') - E(a)| <= C_* w L_w log(2+a)/a`, and a
  dyadic sum gives (30). No upper limit on `a/b` is needed here, because
  `b >= 2u(a)` already makes `y` small.
- **L385 (calibration) and L350, (27): HOLDS.** I checked the tile bound
  directly and against row 1177 (4). With spectators 1 (`a_0`) and
  3 (`w`), active 2 and 4, `h` the first dyadic multiple of `n_0` above
  `K_q n_0 log(2 + a_0/n_0)`: E' cost `4 a_0 w/h^2 <= 4(a_0/h)^2`;
  `G = 2^-3 sum_{B_13 = 1} Z_B` is a positive trace in both active frames
  and lies in the excited part of `V`; `G(h,h) <= lambda^h S_V(h/2)^2`; Lemma X
  gives `h kappa(h) <= 2 log(1 + S_V(h/2; h))`; `l^p` monotonicity
  (`Tr T^L <= (Tr T^h)^{L/h}`, no divisibility needed) gives
  `G(b_0,w) <= G(h,h)^{b_0 w/h^2}`; `V >= e^{b_0 w f}` by the infimum
  definition of `f`. So `Z_13/Z_0 <= 64 G/V <= 64 e^{-c b_0 w/(n_0 h)}`.
  With `c e^{-b_0 E} <= Y/Z_0` (needs `b_0 >= u(a_0)`, true for large `w`),
  `E(a_0,w) >= c_q w/(n_0 h) - C/b_0`, and `h <= C_q n_0 log(2+w)`. With
  (30), `T >= c w/(n_0^2 log(2+w))` for large `w`.
- **L433-L450, (36): HOLDS.** For `chi != 0` the two `g` with
  `chi.g = 1` give the coefficient `(1/2) sum (-1)^{gamma.g}` equal to
  `1, -1, 0` for `gamma = 0, chi`, other; I checked all three `chi`. So
  `Y_chi/lambda^a = 1 - e^{-a Delta_chi} + O_q(e^{-d_q a/n_0})`. The
  compact-side enlargements in (5) stay bounded (`u, v < 128 d`). In
  direction 2, `Y_chi` is half the sum of two static transfers on the
  `C_1`-even space; `c e^{-b e(a)} <= Y_chi/Z_0 <= C e^{-(b-u)e(a)}`;
  `c_q/n_0 <= e(a) <= 2 beta (u+v)` (`v` 13-planes and `u` 14-planes per
  slice). The rest repeats (29)-(30) with `L_m`. Calibration: each `g`
  has `B_{13} = 1` or `B_{14} = 1`; the tile bound with that pair as
  spectators has active product `>= bm`, and the 12 entry is included in
  the sector sum.
- **L452 (consequence and limitation): HOLDS.** The three numbers
  `min_{chi.g=1} E_g` are the pairwise minima `{x, x, y}` of the sorted
  static energies `x <= y <= z`, so the two smallest limits agree and `z`
  is not seen.

Verdict for claim 2: (17), (27), (36) and their supporting steps **HOLD**.

### Step 5. Claim 3: (40)-(42), open sheets versus flat backgrounds (done)

(42) is checked in Step 3.

- **L491 (four low states): HOLDS.** `E(h(X)-h(Y))^2 = 2 d_chi`; `|h|` is
  neutral with no larger Dirichlet form, and the one-step neutral Poincare
  bound gives `Var |h| <= d_chi/gamma`, hence `|| |h| - 1 ||^2 =
  2(1 - E|h|) <= 2 d_chi/gamma`. On opposite signs `(h(X)-h(Y))^2 >=
  4|h(X) h(Y)|`. Splitting `|hh' - 1| <= |hh' - |h||h'|| + ||h||h'| - 1|`
  and Cauchy-Schwarz give `d + 2 sqrt(2d/gamma)`. `d_* <= C b^C e^{-t_* b}`
  from the `b`-line of (36). For large `b`, `r_chi > (3+rho)/4`, so each top
  level is simple by row 1157 (1); the rank-one terms are well defined.
- **L498: HOLDS.** For coefficients in `[1-delta, 1]` on `N` faces, the
  transformed density ratio lies in `[e^{-beta delta N}, e^{beta delta N}]`.
  The matrix-element difference is `E_p[b(X,Y)(h(X)h(Y) - 1)]`. With
  `delta <= t_*/(16 beta w)`, `eps_b = C e^{2 beta delta N} sqrt(d_*) <=
  C b^C e^{-3 t_* b/8} -> 0`. The ratio comparison follows.
- **L500 and L482, (40): HOLDS.** Simultaneous spatial flips leave every
  temporal plaquette (two spatial links at the same position) and every
  spatial plaquette invariant, so cross-character matrix elements vanish.
  The retained part is exactly `Cov_w(A, B)` over four positive weights;
  with all ratios within `C eps_b` of the vacuum ratio it is
  `<= C eps_b^2 = C e^{4 beta delta N} d_* <= C b^C e^{-3 t_* b/4}`.
  Discarded levels: long-odd by the stack bound at time `d_i` (small once
  `b log coth(beta w^2)` is large), others by the neutral gap and row 1157.
  The reinstating cost `e^{4 beta delta N - c e^b/2}` is negligible. The
  `(-1,-1)` corner follows from the link flip, which negates both inserted
  traces.
- **L530: HOLDS.** `t_* <= t_{(1,1)} = T` since `Delta = Delta_{(1,1)}`. With
  `theta = T - t_*/4`, (38) gives `-log z/b -> t_*/4`, and (42) gives a
  positive prefix covariance `>= c/b`. In `Z_00`, `Z_NN`, (40) at
  `delta = 0` applies to any `[0,1]`-valued function of one temporal
  plaquette trace, because the proof uses only the absolute kernel bound and
  flip invariance.
- **L532: HOLDS.** A fully negative stack in one layer is the kernel
  `F(x, C_3 y)` (only the 13-faces at `x_3 = 0` contain one flipped
  3-link). So the extra multiplier is `(-1)^{chi_3}`. The signed weights
  have total variation `M <= C/z`, `z = e^{-t_* b/4 + O(log b)}`, and
  `|Cov_w| <= C M^2 d_* <= C b^C e^{-t_* b/2}`.
- **L534: HOLDS.** Referencing to the nearer flat end changes at most
  `delta_0 b` coefficients per layer: ratio errors `C e^{4 beta delta_0 b}
  sqrt(d_*)`, total variation `C e^{8 beta delta_0 b}/z_flat`, covariance
  `C e^{24 beta delta_0 b} d_*/z_flat^2 <= C b^C e^{-t_* b/4}` since
  `24 beta delta_0 <= t_*/4`. So a pair attaining `c/b` has `d(i) > delta_0 b`
  or `d(j) > delta_0 b`, and that prefix and its complement each cover at
  least `floor(delta_0 b/w)` full rows.

Verdict for claim 3: (40)-(42) and L530-L534 **HOLD**.

### Step 6. Claim 4: local centre-flux recovery (1) and its lift (done)

- **L23, (1) and the recovery of Ad U_e: HOLDS.** With
  `U_{p,x} = U_e U_2 U_3 U_4` and `U_{p,y} = U_2 U_3 U_4 U_e`,
  `U_{p,x} = U_e U_{p,y} U_e^{-1}`, and the sign `omega_p` is common. The two
  calibration faces in the +3 and +4 directions have distinct private links
  (parallel to `e`, at `x_3+1` and `x_4+1`). Each face is
  `A g^{+-1} B` in its private link, a Haar-preserving map, and the
  conditional law of the two private links has a positive smooth density
  w.r.t. product Haar in every sign sector. So the pair of imaginary parts is
  noncollinear almost surely, at all finitely many edges together. `Ad U_e`
  maps the pair at `y` to the pair at `x`; a proper rotation fixed on two
  noncollinear vectors (and so on their cross product) is unique.
- **L29 (lift and flux): HOLDS.** With `L_e = eps_e U_e`,
  `C_{p,x} = omega_p (prod eps_e) L_{p,x}`, so `d_p = omega_p prod eps_e`,
  read off as `C_{p,x} L_{p,x}^{-1}`. Each edge of the 12-torus lies on two of
  its faces, so `prod_p d_p = prod_p omega_p`. Vertex frame changes conjugate
  both sides of (1) and leave `d_p` unchanged. The scalar-data version holds:
  from a noncollinear pair, the coordinates of any other vector are two dot
  products and one oriented triple product (I checked the frame formulas).
  The closing caveat (a recovered flux in a fixed sector says nothing about
  that sector's weight) is correct.

Verdict for claim 4: **HOLDS**.

### Step 7. Everything else, labels, guide runs (done)

Area bound (2) and its scope:

- **L34 (2), L47 (3), L53, L61: HOLD.** (3): with `|u_1| >= |u_2|` and the
  sign of `n` nearest `u_1/|u_1|` (angle `phi <= pi/2`),
  `|u_1/|u_1| - n| = 2 sin(phi/2) <= sqrt2 sin phi`, so
  `|u_2 x u_1/|u_1|| < (1+sqrt2) t`; row 1141 (3) then applies to face 2
  (tilt `<= 6 beta` with any fixed signs), and the other ordering to face 1.
  L53: `Ad_{R_e} U_{p,x} = V_e U_{p,y} V_e^{-1}`, so
  `|Ad_R U - U| <= d_{p,x} + d_{p,y}`, and `|Ad_R U - U| = 2|Im R x Im U|`;
  `|R - eps|^2 = 2(1 - |Re R|) <= 2|Im R|^2`; on a face with
  `omega prod eps = -1`, telescoping gives `2 <= d_{p,x} + sum |R_e - eps_e|`
  (also for inverse traversal, since `|R^{-1} - eps| = |R - eps|`); the
  2/5 split and `h_e >= t` give `>= c t^2`. L61: the rounded sign field
  `omega d eps` is closed, its components are closed, each meets all `w^2`
  parallel 12-tori; the selection, greedy disjointness, iterated
  conditioning and the `6v C_2^m` count give (2). `D(U,U) = 4w^2` for the
  one-stack representative.
- **L63: HOLDS.** For `a = b = floor(e^{s w^2/2})` and `A > s`,
  `C_A v e^{-A w^2} -> 0`; row 1177 (24) gives `Z_12/Z_0 -> 1` there. The
  scalar increment `Re U - Re(BU) = (1 - Re B) Re U + Im B . Im U` is
  correct.

Cylinder identity and the local criterion:

- **L92 (6), L103 (7): HOLD.** `E(xi | U) = tanh(beta A)`; the two values
  of `xi` give `J_{k,m+1}` and `J_{k+1,m}`; trace cyclicity in the common
  sandwich. `psi_s = C^{1/2} M_s^{1/2} phi_s/sqrt(lambda_s)` is a unit top
  eigenvector of `T_s`; the overlap is a matrix element of the positive
  kernel `C` between positive functions; trace-norm convergence of the
  normalized powers gives (7).
- **L117, L119, L121: HOLD.** Finite-range continuous specification, so DLR
  passes to weak limits. The reflection in direction 2 plus the half-space
  3-link flip (`x_1 >= 1`, `x_3 = 0`) negates only the 13-column at
  `x_1 = 0`, at all times, and `xi -> -xi` restores the central row; so it is
  a symmetry of the one-end specification and maps `tanh(beta A)` to its
  negative. L121: `bw` disjoint 13-planes replace `w^2`.

Scalar reconstruction and finite precision:

- **L126, L128: HOLD.** I checked the formula for `Re(PQR)` (also by
  guide, below). Gram matrix and triple products fix each vertex list up to
  a proper rotation; (1) fixes `Ad U_e`; the residual sign cochain is closed
  and is a coboundary times cut flips; winding signs read the flips.
- **L130, (9): HOLDS.** `1 + chi^2` of the projected pair is
  `||Pi_D P^t Pi_D||_HS^2`; for `(S,B)` the projection is the identity on the
  gauge-invariant space, for `S` it is centre averaging.
- **L137: HOLDS.** The quotient has dimension `3(2v+1) - 3 = 6v`; the
  `3v` elementary traces have rank `<= 3v`, so a nonzero neutral `f` with
  zero conditional mean on the traces exists; `F` is injective (positive
  spin multipliers, `D > 0`); then `P^t f != 0` forces a strict HS loss
  by the two-term decomposition.
- **L142 (10), L148, L155, L157: HOLD.** Bin geometry: `A, D_0 >= r` by
  testing the two axes; errors `C delta/r, C delta/r^2, C delta/r^3`, frame
  coordinates `C delta/r^5`, relative links `C delta/r^6 = C h^2`; equal
  winding signs exclude a nonzero period when `C_*` exceeds the telescoping
  constant. Exceptions: the endpoint marginal of `p_D^2 dpi dpi/H_D` is the
  normalized diagonal (a seam mixture of Wilson tori); (3) and the winding
  cap bound `C(1+6 beta)^{3/2}` give total `<= eta`. Integration: log
  oscillation `<= C beta v h^2 <= eta` on good cell pairs; Jensen for the
  upper bound.
- **L159 (11): HOLDS.** `e^{2 eta}/(1-eta) = 1 + 3.0e-5 < 1 + 4 eta` at
  `eta = 1e-5`, so `H - 1 < 2.8e-4 < 1/1650`. Neutral version at
  `eta = 1/100`: `H_S - 1 < 0.289 <= 1/2`. The converse via E' at fixed time
  (cost `1024^3` on the log) is correct.

Pinned layer (12):

- **L170, L179, L181 (13), L188, L190, L192: HOLD.** Tile energy: identity
  bonds connect each 2-cube, special bonds give
  `2|sin theta| |Im q x i|`, `2|sin theta| |Im q x j| <= C sqrt(D)`, and
  `|u x i|^2 + |u x j|^2 >= |u|^2`. Entropy: cap of radius `beta^{-1/2}` in
  the trivial class (conjugation fixes `+1`), half the bad-cube energy kept,
  leaf integrals `<= C beta^{-3/2}` for any sign. Reflection: site planes
  have no crossing bonds, the flat-sign constraints factor, the background is
  reflection symmetric; the chessboard maximizer argument is correct.
  Surface: `s_x xi^(2) s_y` is gauge independent and closed in the class of
  `xi`; negative coarse bonds touch only bad cubes; `bw/4` disjoint coarse
  1-windings; `l/12` distinct cubes. Vacuum energy: `Tr T^b <=
  ||T||^{b-1} Tr T`, `log(Tr T/||T||) <= C(1+beta) aw`, divide by `b = a^2`.

Deletions (14):

- **L197 (14), L208, L210, L212: HOLD.** Erasure of a group has conditional
  probability `>= e^{-2k beta}`; Chernoff with `lambda = 1` gives
  `c = 1/2 - e^{-1}`; the retained terms have range in `Pi_l`; `0 <= R <=
  pF^t` pointwise; the two-sided HS bound uses `F^t = F^{t*}`. L210: joint
  erasure `= e^{-k beta} Z_del/Z_0 <= [C(1+beta)^{3/2} e^{-2 beta}]^k` by
  row 1167 (1) (all faces temporal in one layer). L212:
  `11/(3 pi^2) = 0.3715` lies in `(3/10, 3/8)`.

Endpoint sign and majority:

- **L217 (15), L225: HOLD.** `L'' = beta^2 Var_s A >= 2 g_beta w` from
  `floor(w/2)` separated 1-links and row 1173 (8); `E_nu sech = e^{L(0)}/
  ((e^{L(1)} + e^{L(-1)})/2)`; AM-GM and Markov. Reading note: the step
  `floor(w/2) >= w/3` needs `w >= 2`; every torus in the file has
  `w >= 3`.
- **L227 (16), L234, L236: HOLD.** `E e^{-lambda sigma} = sqrt(1-m^2)` at
  `lambda = artanh |m|` (guide confirms); `|sgn x - tanh x| <= 2e^{-2|x|}`;
  the majority mean is an odd polynomial of degree `<= k`; a sign change
  under moves with `|beta Delta A| <= g w/2` must start in the exceptional
  set.

Cylinders, scalar tests, comparisons:

- **L292 (23): HOLDS.** `e^{-H} <= c_{k,m} <= e^H` (Cauchy-Schwarz with
  `A^{2k} <= A`, and the vacuum term with the overlap bound); convexity and
  monotonicity in each index bound the increments by `2H/(k-1)`.
- **L300 (24), L306, L308: HOLD.** `||K||_op = X^{-1/2}`, `C_b` a
  compression, `0 <= C_b <= B`, `||B - C_b||^2 <= 1 - ||C_b||^2 <= 3 eta`,
  `A_h = <sqrt l_h, B sqrt l_h>`; Hellinger `d_0^2 = 2(1 - X^{-1/2})`,
  contraction, product cost `2 d_0`, total `3 d_0`. At `eta = 1e-12`,
  `A_h > 1 - 1e-4` gives `X - 1 < 2.04e-4 < 1/1650`.
- **L313, L315, L317 (25), L324: HOLD.** The three edge flips
  `(+1,+2), (-2,+3), (-3,-1)` negate each face of the core cube once;
  occupancy agreement across temporal 3-faces leaves the empty and full
  slice; `3M` shared faces; eigenvalues `1, r_j = (rho_j h_j^4)^M`;
  `-log r_j^t = O(L^4 alpha_j) -> 0`. Read-out: on a line a nonempty
  selection has a first endpoint of degree one, on a circle only the full
  selection survives; the tilt by `prod v^2` has total variation
  `<= (1 - h^{MT})/h^{MT} = O(alpha_j)`.
- **L327: HOLDS.** `f = D^{-1} v/||D^{-1} v||` is orthogonal to the range of
  `Pi_l` (flip the three omitted links of one core); `|Rg| <= p F |g|` gives
  `||R|| <= p lambda`, and the adjoint step gives `||F f|| <= p lambda`, so the
  spectral weight at ratio `>= r` is `<= p/r`.
- **L330: HOLDS.** `d_H <= d_bin + 6 sqrt(eta)`, and
  `1/64 + 6e-4 < 1/32`. Reading note: `<A, A_b> >= e^{-eta/2}(1-eta)`
  holds; the stated `e^{-eta}(1-eta)` is weaker and also true.
- **L335 (26), L343, L345: HOLD.** With `d_x < eps r^6`, the frame
  coordinates differ by `C eps r` and relative links by `C' eps`, so the
  rounding is positive on the face; the count of (2) gives `(1+6 beta)^6`.
  L345: both arrays have total product one (`e^{i alpha ab} = -1` with one
  negative sign per plane); the column construction realizes them; all
  readings are `cos alpha` or 1.

Line costs and one-plaquette tests:

- **L387 (31): HOLDS.** `p = 1/(1+e^T)`; ordinary `p = 1/2`; competing
  `-log p >= T`. The `O(1 + beta^2/g_beta^2)` sample size is correct.
- **L396 (32), L405: HOLD.** `delta = omega^+ omega^-` has negative
  coboundary on the `w` face-disjoint 123-cubes at the ring; the face
  inequality holds with `omega^-` in place of the twist sign; the count is
  over `w` cubes. Hellinger affinity `= e^{L(0) - (L(1)+L(-1))/2}`.
  Mixtures of a Gibbs law and its image are Gibbs.
- **L410 (33), L417 (34), L423 (35): HOLD.** `L'(s) = beta w f(s)` by
  translation in direction 4; `L(1) - L(-1) = log(J_{k,m+1}/J_{k+1,m})`;
  the log-ratio error of (23) is `O(a w^2/a^2)`. (35): `f' >= 2 g_beta/beta`
  and `f(s) - f(-s) >= 2s min f'`.
- **L536 (43): HOLDS.** Regions `b <= a <= Lb` (`-log z <= 2 beta bw`),
  `Lb <= a <= e^{(T+1)b}` (`x(K_b - x)_+ <= K_b^2/4`), and the tail
  (`D >= Delta/3`, `a Delta >= e^{b/2}`) give the upper limit; (38) at
  `theta = T/2` attains it; ordinary branch gives zero.

Labels. The 7 GUIDE and 5 OPEN blocks agree with the body: L15 copies
item 18; L19 restates rows 1161 and ZD-c correctly; L165, L548, L550 state
only what the body leaves open, and each "obstruction" sentence in L548 and
L550 matches a proved statement ((2), (12), (26), (32), (35), (40), L530,
L534, (14), (25), L327). Two notes: L552 is stale (rows 1175 and 1177 now
hold, rows 1176 and 1182); L5 calls Chatterjee's method a
"finite-coupling" free-energy comparison, while the lane credit line names
the weak-coupling free-energy method (wording only). The RESULT line L554
matches the body and the FINISH RESULT of row 1178.

Guide runs (guides only, outside the repository, BLAS threads 1, peak about
224 MB, numpy via `python3 -E -P`): (a) `Re(PQR)` formula and
`2|Im R x Im U| = |Ad_R U - U|` to 1e-15; (b) the (3) ratio
`|u_2 x u_1/|u_1||/t` has sample maximum 1.92 against the bound 2.414;
(c) on random faces with negative rounded sign, `d + sum |R - eps| >= 3.17`
(the bound is 2); (d) on a random `3^4` torus with a 12 twist, the
recovered `Ad U_e` matches to 1e-14 and the lifted flux product is `-1` on
all nine 12-planes; (e) all numerical thresholds in (11), (24), L308, L330,
L212; (f) a 6 x 3 Ising toy with two column stacks: `sum l_ij = 2(-log z)`
to 1e-14, the (37) double integral matches to 1e-15, and the maximum positive
prefix covariance 0.0370 exceeds the (42) bound 0.0037. No guide is used in
any verdict.

### Step 8. Counts, verdicts, scope (done)

**Counts.** 88 PROVED statements checked line by line by hand:
88 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. 12 labelled blocks (7 GUIDE,
5 OPEN) checked against the body: all agree; 2 wording notes (L5, L552).

**Per-statement verdicts (target line numbers).**

| Lines | Content | Verdict |
|---|---|---|
| L23, L29 | (1), recovery of `Ad U_e`, lift and flux | HOLD |
| L34, L47, L53, L61, L63 | (2), (3), deterministic bound, count, scope | HOLD |
| L68, L81, L87 | (4), (5), the two energies | HOLD |
| L92, L103, L111 | (6), (7), (8) | HOLD |
| L117, L119, L121 | one-end Gibbs states, symmetry, (2) on 13 geometry | HOLD |
| L126, L128, L130, L137 | reconstruction from scalar words, (9), strict loss | HOLD |
| L142, L148, L155, L157, L159 | (10) and its proof, (11) | HOLD |
| L170, L179, L181, L188, L190, L192 | (12), (13), reflection, surface, vacuum energy | HOLD |
| L197, L208, L210, L212 | (14), scale, conditional slope | HOLD |
| L217, L225, L227, L234, L236 | (15), (16), majority, equilibration | HOLD |
| L241, L252, L259, L269, L276, L282 | (17)-(22) | HOLD |
| L292, L300, L306, L308 | (23), (24) | HOLD |
| L313, L315, L317, L324, L327 | (25), read-out, Wilson exclusion | HOLD |
| L330, L335, L343, L345 | one winding bit, (26), commuting example | HOLD |
| L350, L357, L368, L370, L385 | (27)-(30), thermal time, calibration | HOLD |
| L387, L396, L405 | (31), (32), two positive comparisons | HOLD |
| L410, L417, L423 | (33)-(35) | HOLD |
| L433, L444, L450, L452 | (36) and its limits | HOLD |
| L456, L464, L472, L480 | (37)-(39), ordinary-branch control | HOLD |
| L482, L491, L498, L500 | (40) and the four low states | HOLD |
| L504, L516, L530, L532, L534 | (41), (42), flat backgrounds, prefix extent | HOLD |
| L536 | (43) | HOLD |

**Reading notes (no verdict change).** (i) With `a_b = ceil(e^b)` the
competing-branch half of (39) and (41) needs (27) (so that `T > 1`); with a
cutoff-dependent rate `theta_j < c_q/n_{0,j}`, (4) alone would suffice.
(ii) In (15), `floor(w/2) >= w/3` needs `w >= 2`; all tori in the file
satisfy it. (iii) L330: the inner-product bound holds with `e^{-eta/2}`.
(iv) L252: `z >= e^{-2 beta w b}` holds directly for every `b`.
(v) L552 is stale: rows 1175 and 1177 now hold (rows 1176, 1182).
(vi) L5: Chatterjee is credited for a "finite-coupling" comparison; the lane
credit line names the weak-coupling free-energy method.

**Not checked.** The external sources: the outline and complete-account lines
cited at L5 and L546, and the PR files and commits in L3 (PR 10114, 10133,
10134, 10141, 10149; `gap-phys-seed.md` Theorem ZD-c on main). The phrase
"common convolution sandwich of GL8" (L96) was not compared with the outline;
I checked the transfer facts used (positivity, kernel bounds, gauge
projection) directly. From the lane rows I read the statements used and the
proofs the target's steps depend on, but did not re-derive row 1161's
finite-aspect theorem and its K = 512 constants (checked in row 1162), the
rest of row 1157 beyond (1), row 1139's own text (the target re-proves its
small-angle variant, which I checked directly), or row 1167 (11)-(13)
(contrast only). `parts/gap.md` and `gap-council-synthesis.md` are cited
only as pointers at L550 and were not read; no step depends on them. Credit
and novelty remarks (for example L130, L306) were not audited. Guide runs
were used for no verdict.

RESULT (2026-11-19 22:45Z (date -u), Claude Opus 5.5 max, laptop subagent; cross-provider check of gpt-6.2-astra row 1178, grants no status): row 1178 HOLDS. 88 PROVED statements checked line by line by hand, positive claims first: 88 HOLD, 0 corrections, 0 FAIL. The equivalence of (W), given the one-cube neutral bound, with (41) holds through (4), (5), (37), (38), (42) and the ordinary-branch bound; (17), (27), (36) hold, so the competing interface energy is the diagonal electric splitting rate and grows at least like w/(n_0^2 log w); (40)-(42) and the flat-background and prefix-extent bounds hold; (1) and the flux lift hold. Six reading notes, two of them on labels (L552 stale, L5 credit wording). External sources not re-read. Guide runs agree. Open: the Wilson clustering bound for the open sheets in (41), the physical neutral bound, (W).
