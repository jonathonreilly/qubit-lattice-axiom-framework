lead: Claude Opus 5.5 lead session, row queued 2026-11-17 06:31Z
row: FINISH 1093, written by Claude Opus 5.5 max (laptop subagent); same provider as the author of row 1091

# Gap face stability check (Opus)

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read FINISH row 1093 (the brief) and record what it asks.
2. Read the object under check (row 1091 output) in full; list its claims.
3. Check the sources it relies on (posted paper copy, repo files) against the claims.
4. Check the claims line by line, part 1.
5. Check the claims line by line, part 2.
6. Optional single serial numeric run to guide or refute (only if useful).
7. Write verdicts (HOLDS / HOLDS AFTER CORRECTION / FAILS) with who checked what.
8. RESULT line.

## Step log

### Step 1 result: the brief (FINISH.md line 1174, row 1093), read by me in full

Object: `library/gap-face-stability.md` (row 1091, written by Claude Fable 5.2 medium).
Do not read row 1094's file (`library/gap-face-stability-check-astra.md`).
Items to check line by line:
- M1, M2: the face law as a family of O(4) sheets in fields of norm at most 2 lambda,
  six neighbours, Lipschitz dependence of a sheet's field on a neighbouring link; against
  row 1077's face law.
- FST-BD (i)-(iv) in full: every inequality, (BD1), (BD2), the 1/N bookkeeping, the
  weights allowed in (i), the shift g -> g + c, the claim that no truncated blocks are needed.
- FST-P: the three influence terms, the count giving gamma(lambda, a), the distance 2l - 1,
  the constant; its corollary to (17), including bounded -> Lipschitz observables and local
  limits of periodic measures.
- FST-F: (C) via interpolation in the field, the convexity step, (D_a) with S_a, (I).
- FST-T: cumulant expansion of g(t), multilinearity, the radius, analytic continuation on (-2, 2).
- K3 against OpenAI Theorem 3.1 as stated (posted paper, open copy); the ARGUED 6.2
  consequence and its loss of rate c/(n+1).
- G1, G2: redo both two-site computations by hand; their claimed scope.
- 7.4 (Ising long-range-order step); the statement of FST-N in 7.5.
Judgements asked: does FST-BD hold as stated; is FST-F weaker than or comparable with FST-P;
is FST-N correctly named as the first missing input; does any item conflict with row 1078's O7(b).
Verdicts: HOLDS / HOLDS AFTER CORRECTION (with text) / FAILS (first failing line). No new attack.

### Step 2 result: the object read in full (330 lines); claims to check, with line numbers

I read `library/gap-face-stability.md` lines 1-330 in full. Claims under check:
- M1 (line 38), M2 (line 40).
- FST-BD setting (67-71), (C) (73-77), (D_a) (79-81), statement (83-99), proof steps A-F (101-125), remarks (127).
- FST-P hypothesis (135-143), theorem (145-153), proof (155-163), corollary (165).
- FST-F hypothesis (169-173), theorem (175-179), proof (181-193), remark (195).
- FST-T hypothesis (201-205), proposition and proof (207-209), chain remark (211).
- K3 (215-223), ARGUED consequence (225), loss of rate (227).
- G1 (233-237), G2 (241-253), 7.3 (257), 7.4 (261), FST-N (265-269), 7.6-7.7 (273-284).
- Controls incl. O7(b) (290-294), marks (298-309), 8.3-8.4 (313-324), RESULT (330).
Sources still to read: row 1077's face law (1), (9), (17) in `library/gap-face-2d-astra.md`;
row 1078's O7(b) and J1 in `library/gap-face-2d-check-opus.md`; OpenAI Theorem 3.1 (posted copy).

### Step 3 result: sources checked (part 1)

- Paper copy. `/tmp/opus-face2d-openai.NylL2Z/src/preliminary.tex` has git blob hash
  a496bb8e87cf5346418236f38b042196a2b7a3e4 (I ran `git hash-object`). `gh api` on
  openai/math gives the same blob for `.../build/sections/preliminary.tex` at the pin
  4eaee87548250b2682affda7d05d947c05554bae and at the current default branch (one commit,
  2026-10-06). So the copy is the posted paper. I made no new download.
- Theorem 3.1 as posted (preliminary.tex lines 14-45), read by me: unpinned rectangular torus,
  each side at least C Xi(beta), couplings 0 <= beta_e <= beta; F, G local on A, A' at distance d;
  |Cov(F,G)| <= C (1 + beta + |A| + |A'| + d)^20 L_F L_G e^{-c d / Xi(beta)};
  L_F = ||F||_inf + max_{x in A} Lip_x(F) (round distance); the same on unpinned free subgraphs;
  distances between supports use the MAXIMUM norm (periodic on a torus). Lines 47-52: only the
  last part of the proof needs nonnegative untwisted couplings.
- Row 1077 face law (1) (gap-face-2d-astra.md lines 106-132): density proportional to
  exp{beta sum_<uv> sum_e tau(Phi_e(v) Phi_e(u)^{-1}) + lambda sum_u W_T(Phi(u))},
  W_T = sum_p tau(Phi_e1 Phi_e2 Phi_e3^{-1} Phi_e4^{-1}), T >= 3, four distinct edges per square.
  (17) (lines 539-557): translation-invariant RP local limits of periodic measures (1); rate
  m_beta uniform in T >= 3 and lambda; prefactor free of T, lambda, state, translations, for
  G_T-invariant local Lipschitz F, H.
- Row 1078 O7(b) (gap-face-2d-check-opus.md lines 412-426): the comparison (14)-(15) uses only
  K_0 >= 0, the gap a and osc V; it is sharp (example (16)); a size-uniform interval must use the
  product form over sheets, the locality of V and decay of the sheets' correlations.
  J1 corrected (lines 520-528) is the target used by row 1091 (line 32). Quoted correctly.

### Step 3 result (part 2): the paper's Sections 3.10-3.11, read by me (preliminary.tex 977-1182)

- eq:pre:10-3 (line 1004) is the 61st numbered display of Section 3 (my count of
  `\begin{equation}` in the file; Section 3 = `sections/preliminary` per main.tex lines 60-62).
  So "(3.61)" in row 1091 line 29 is right. Its text (lines 1001-1005): bounded O on A with
  identically zero common-left average, |E O| <= C ||O||_inf |A| e^{-c d_pin/s}. Line 1016:
  right twists and signed couplings still allowed. Row 1091 line 29: HOLDS.
- Line 1020: "From now on use the untwisted zero-field ferromagnet ... This restriction is
  essential." Row 1091 line 30: HOLDS (Newman (11-1), Ginibre for zero-field XY, FK for
  zero-field Ising, lattice condition for the angle marginals, two localizations in L^1 that
  use ||F||_inf: lines 1022-1182).
- 3.11.1 (lines 1040-1048): zero-field ferromagnetic XY: cosine-character means >= 0; covariance
  of two cosine characters >= 0; hence monotonicity of two-point functions in every coupling.
- 3.11.2 (lines 1062-1068): split (tau^1 cos gamma, tau^2 sin gamma), gamma in [0, pi/2] with
  density 2/pi; given the angles, two independent ferromagnetic Ising species; the gamma marginal
  is associated. Lines 1104-1110: d f_0 / d gamma_i = E_0[d F] + sum_{e,h} (dJ_e^h) Cov_0(F, tau tau),
  each covariance bounded by 2 ||F||_inf. Lines 1112-1114: L^1, not pointwise, control suffices.
- 3.11.3 (lines 1133-1152): q = (cos alpha z, sin alpha w); given alpha, two independent XY
  sectors with J^1_e = b_e cos alpha_x cos alpha_y, J^2_e = b_e sin alpha_x sin alpha_y.
So the paper facts that row 1091 uses in 3.2-3.3, G1, G2 and 7.4 are quoted faithfully.

### Step 4 result: M1, M2, FST-BD, FST-P and its corollary, checked line by line by me

**M1 (line 38). HOLDS (one parenthesis imprecise).** For unit quaternions, tau(q r^{-1}) = Re(q rbar) = q.r,
so the bond term of (1) is beta Phi_e(u).Phi_e(v). In a square word, cyclicity of the trace puts
Phi_e first or Phi_e^{-1} first. If e1 is first, tau(Phi_e X) = Phi_e . Xbar with X = Phi_e2 Phi_e3^{-1} Phi_e4^{-1}.
If e3 is first as an inverse, tau(Phi_e3^{-1} Y) = Phi_e3 . Y with Y = Phi_e4^{-1} Phi_e1 Phi_e2. In both
cases h_p(u) is a unit vector and tau_p is linear in Phi_e. For T >= 3 every edge lies in exactly
two squares of P_T, with four distinct edges each (row 1077 line 108). So the conditional
density of sheet e is exp{beta sum Phi.Phi + sum_u H_u.Phi(u)}, H_u = lambda(h_p + h_p'), |H_u| <= 2 lambda.
Note: "the conjugate of the product" is right only when e is not inverted in the word; otherwise
h_p is the product itself. Nothing downstream uses which one.

**M2 (line 40). HOLDS.** h_p(u) uses only links at the same u. |a q b - a q' b| = |q - q'| for unit a, b,
and |q^{-1} - q'^{-1}| = |qbar - q'bar| = |q - q'|; chord <= arc. Horizontal edge (i,j)->(i+1,j) lies in
the squares based at (i,j) and (i,j-1). Their other edges coincide only if j+1 = j-1 mod T, so
T = 2. So for T >= 3 two distinct edges share at most one square, the two triples of other edges
are disjoint, and e has exactly six neighbours. A change of one neighbour link moves one h_p only.

**FST-BD setting (lines 67-71). HOLDS AFTER CORRECTION.** Line 67 asks (Omega_x, rho_x) to be a compact
metric space. Line 69 and Theorem FST-P (line 155) then use the discrete metric on S^3, which is
not compact. The proof never uses compactness of rho_x: rho_x enters only through Lip_x and D_0,
and measurability comes from the topology of Omega_x. Corrected text for line 67: "Omega_x is a
compact metric space with its Borel sets, and rho_x is a metric on Omega_x of diameter at most D_0;
rho_x need not define the topology (the round metric and the discrete metric are both allowed)."

**(C), (D_a), statement (lines 73-99). HOLD** as definitions; gamma >= 0 is forced (left side >= 0, n_u >= 1),
so theta is in [0, 1).

**Step A, (BD1) (lines 101-107). HOLDS.** P_V f depends on eta_{V^c} only. The first bracket is at most
Lip_x(f) rho_x. For the second, F(xi_V) = f(xi_V, eta'_{V^c}) depends on V only and Lip_u(F) <= Lip_u(f),
so (C) applies.

**Step B, (i) (lines 109-113). HOLDS.** Lip_x is subadditive and homogeneous. The first sum is
sum_x w(x) Lip_x(f) #{V : x not in V}/N = sum_x w(x) Lip_x(f)(N - n_x)/N. Exchanging sums,
the second is (1/N) sum_u Lip_u(f) sum_{V ni u} sum_{x notin V} w(x) k^V_{x->u} <= (gamma/N) sum_u n_u w(u) Lip_u(f).
Total coefficient of w(u) Lip_u(f): 1 - (1 - gamma) n_u/N <= theta.

**Step C, (ii) (line 115). HOLDS.** w = 1 is allowed; mu(P^n f) = mu(f) lies between inf and sup of P^n f.

**Step D, (BD2) (lines 117-121). HOLDS.** Cov = mu(g)(nu(f) - mu(f)); nu(P^n f) -> mu(f) uniformly by (ii);
telescoping; if V misses B then P_V(gh) = g P_V h, so nu(h - P_V h) = 0.

**Step E, (iii) (line 123). HOLDS AFTER CORRECTION (one phrase).** |h - P_V h| <= D_0 sum_{u in V} Lip_u(h)
by telescoping inside V. w = e^{-a d(., B+)} is allowed: d(u, B+) <= d(u, x) + d(x, B+). Every block
that meets B lies in B+, where w = 1, so sum_{V meets B} sum_{u in V} Lip_u(h) <= n_max Delta_w(h).
The 1/N bookkeeping: (1/N) sum_n theta^n = (1/N) N/((1 - gamma) n_min) = 1/((1 - gamma) n_min). Right.
The shift: Cov(f, g + c) = Cov(f, g) and g + c > 0 for c > ||g||. But "mu(g + c) tends to 2 ||g||" is false
in general (it tends to mu(g) + ||g||). Corrected text: "mu(g + c) = mu(g) + c <= ||g|| + c, which tends
to 2 ||g|| as c decreases to ||g||." The bound (iii) is unchanged.

**Step F, (iv) (line 125). HOLDS.** The nu-conditional law on V is g mu_V^eta / mu_V^eta(g), so
nu(h - P_V h) = nu-average of Cov_{mu_V^eta}(h, g)/mu_V^eta(g); mu_V^eta(g) >= inf g. W(x) <= e^{a d(x,u)} W(u)
by the triangle inequality, and W > 0 if g is not constant (osc g <= D_0 sum_b Lip_b(g)). A pair u, b
lies in at most n_max common blocks. (mu(g) + c)/(inf g + c) -> 1 as c -> infinity. Right.

**Remarks (line 127). HOLD.** The proof uses P_V for the listed blocks only, the tilt nu, and a geometric
series. It never conditions on B and never forms a truncated block. On a torus no block is cut.
Credits are marked from memory.

**FST-P hypothesis and theorem (lines 135-153). HOLD.** Check of the admissible choice:
e^{a(2l-1)} = 2/(1 + gamma_0) and the bracket <= gamma_0 + (1 - gamma_0)/4 give
gamma <= (1 + 3 gamma_0)/(2 + 2 gamma_0), which is < 1 iff gamma_0 < 1.

**FST-P proof (lines 155-163). HOLDS, given the corrected FST-BD setting.** For L, M >= l + 2, the l x l
block and its 4l outer sites are distinct in the torus (left and right outer columns differ mod L
iff L >= l + 2), so the untilted block law is the pinned law of FST-P. N = |D||E_T|, n_x = l^2.
Tilt: |sum_u H_u.Phi(u)| <= 2 lambda l^2, normalized density ratio in [e^{-4 lambda l^2}, e^{4 lambda l^2}],
|mu'(F) - mu(F)| <= (e^{4 lambda l^2} - 1) osc(F) (a factor 2 is even spare). A pin (y, e) does not enter H
(H_u uses links at u in the block). So k = k0 + 2(e^{4 lambda l^2} - 1) by the triangle inequality. A link
(u, e'), e' ~ e, moves H_u by <= 2 lambda: k = e^{4 lambda} - 1 for every w. No other outside site enters.
(D_a) at (w, e): over the l^2 blocks containing it, w - z runs over all of Lambda, so the pin part is
sum_{y,w'} k0 + l^2 4l 2(e^{4 lambda l^2} - 1) <= l^2 [gamma_0 + 8l(e^{4 lambda l^2} - 1)], and the link part is
l^2 6 l^2 (e^{4 lambda} - 1). Distances: pin to block site <= l + (l - 1) = 2l - 1; link to target
<= 2(l - 1) + d_T(e', e) = 2l - 1. B+ lies within 2(l - 1) of B (same sheet, l x l square). So the
stated bound follows from FST-BD (iii) with D_0 = 1, n_max = n_min = l^2.

**Corollary (line 165). HOLDS AFTER CORRECTION (local-limit wording).** osc_x <= pi Lip_x (diameter of S^3
is pi). For x in supp F and b in supp H + n e_0, d(x, b) >= n - r with r the e_0-extent of
supp F u supp H, but only while the periodic distance equals the planar one. Corrected text for
"The bound holds on every torus, so it holds for every local limit of the periodic measures":
"The bound in d(x, B) holds on every torus with L, M >= l + 2; for fixed n it gives C_{F,H} e^{-a n} once
the side along e_0 is at least 2(n + r). Lipschitz F, H are continuous, so the bound passes to every
local limit." Also read gamma as gamma(eps, a) (gamma is increasing in lambda), so C_{F,H} is uniform
on [0, eps]. In the marks table (line 302), "all bounded local observables" holds on tori; in local
limits it holds for continuous local observables. Neither change moves (17).

### Step 5 result: FST-F, FST-T, K3, 6.2, G1, G2, 7.4, FST-N, checked line by line by me

**FST-F hypothesis and theorem (lines 169-179). HOLD.** With gamma <= 1/2 (lambda <= 1/(12 X e^a S_a)),
X/(1 - gamma) <= 2X, which gives the stated prefactor (same periodic-distance proviso as above).

**FST-F proof (lines 181-193). HOLDS.**
- (C): x = (u, e'), e' ~ e, moves only H_u, by delta with |delta| <= lambda rho (M2, one common square).
  The interpolation: d/ds mu^{H + s delta}(F) = Cov_{H + s delta}(F, delta.Phi(u)), integrated over [0, 1].
  Convexity: only coordinate u moves, and |(1 - s) H_u + s (H_u + delta)| <= max(|H_u|, |H_u + delta|) <= 2 lambda <= h_0.
  Lip_u(delta.Phi(u)) <= |delta| (Cauchy-Schwarz, chord <= arc), other Lip = 0. FST-F then gives
  k = lambda X e^{-2a|u-w|}. Links in non-neighbour sheets do not enter.
- (D_a): d((u, e'), (w, e)) = |u - w|_1 + 1. Sum over u of e^{-a|u - w|} on the torus is at most the sum
  over Z^2 (the periodic distance is the norm of the nearest representative), and
  sum_{Z^2} e^{-a|u|_1} = (sum_Z e^{-a|k|})^2 = ((1 + e^{-a})/(1 - e^{-a}))^2 = S_a. Six neighbours give gamma.
- (I): the block law is mu_D^H with |H| <= h_0, and e^{-2a t} <= e^{-a t}. n_max = n_min = 1. Right.

**Remark after FST-F (line 195). HOLDS AFTER CORRECTION (GUIDE sentence).** "eps is of order 1/X" is false
for small a: S_a is about 4/a^2, so eps = min(h_0/2, about a^2/(48 X)). With X of order Xi^2 and a of
order 1/Xi this gives Xi^{-4}, not Xi^{-2}. Corrected text: "The interval is explicit: eps is of order
1/(X S_a), about a^2/(48 X) for small a. The kernel sum X S_a plays the role of the sheet's
susceptibility. If X S_a is of order Xi(beta)^2 (X of order one, a of order 1/Xi), then eps is of order
Xi^{-2}. This matches the region beta_T Xi^2 <= eps of row 1066. GUIDE grade, not a proved size."

**FST-T and Proposition FST-T (lines 201-209). HOLD.** Z(t, s, r) = E_0 exp{tW + sF + rG} is entire on C^3
(bounded exponent on a finite compact space) and positive on R^3, so log Z is holomorphic near R^3
and g(t) = d_s d_r log Z (t, 0, 0) = Cov_{tH}(F, G) is real-analytic on R, with g^(n)(0) = kappa_{n+2}(F, G, W, ..., W).
Multilinearity with W = sum_u |H_u| a_u.Phi(u) (a_u = 0 where H_u = 0; FST-T allows |a_u| <= 1) gives
|g^(n)(0)| <= h_0^n n! C_T^n X_T K, so the coefficients are <= X_T K 2^{-n} and the series has radius >= 2.
Its sum and g are real-analytic on the connected interval (-2, 2) with equal derivatives at 0, so
they agree there (identity theorem; Mathlib has it). g(1) = Cov_H(F, G), |g(1)| <= 2 X_T K. Right.

**Lemma K3 against Theorem 3.1 as posted (lines 215-223). HOLDS.** I expanded kappa_3 = E[123] - E1 E[23] - E2 E[13] -
E3 E[12] + 2 E1E2E3 and the right side; they agree. L_{F2F3} <= L_{F2} L_{F3} (product rule for each
Lip_x, sup of a product), so the stated factor 2 is safe. (1 + beta + n + d) <= (1 + beta)(1 + n)(1 + d)
for nonnegative arguments. The two side terms have distance d' >= d_1, and
(1 + d')^20 e^{-c d'/Xi} <= sup_r (1 + r)^20 e^{-c r/(2 Xi)} e^{-c d_1/(2 Xi)}. Count 2 + 1 + 1 = 4. Precision: the
distances in K3 are Theorem 3.1's maximum-norm (periodic) distances; K3 does not say so, and every
later use (summability over u, the tree remark) is unaffected. Tree remark: with pairwise distances
a <= b <= c, d* = b >= (a + b)/2 = half the minimal spanning tree, hence rate c/(4 Xi). Right.

**6.2 ARGUED consequence (line 225). HOLDS as ARGUED.** (a) With F_j = E[F | sheets j, ..., J],
M_j F = F_j - F_{j+1} are orthogonal and E[M_j F M_j G | sheets > j] = Cov_{mu_j}(F_j, G_j); F_j has sup
norm and one-site constants at most those of F. (b) A joint cumulant with one entry independent of
the others is 0; each sheet lies in two squares, so at most 2 x (number of sheets that meet the
supports) squares contribute, a count free of T.
(c) Plausible as written, with the K3 identity applied on the product law through (a); the decay in
n uses the largest isolation distance, which is at least about n/2 for every u. Constants are not
tracked, as the file says. Remark: K3 refines row 1078 O7(c)'s clause "Theorem 3.1 says nothing ...
about third cumulants": at lambda = 0 it does give them; O7(c)'s conclusion is unchanged.

**Loss of rate c/(n+1). HOLDS as ARGUED.** A minimal spanning tree on n + 2 points has n + 1 edges;
its longest edge is a minimum crossing edge of the cut it defines (cut property), so the best
two-group gap is >= (tree length)/(n + 1), with equality for equally spaced collinear points. The
count ((n + 1) Xi/c)^{2n} against 1/n! leaves about n^n (times C^n). No radius follows; the file does
not claim one.

**G1, redone by hand (lines 233-237). HOLDS.** At J = 0 the law is p_1(t) ~ e^{h cos t}, p_2(t) ~ e^{-h cos t}.
E_1 cos = I_1(h)/I_0(h) = r in (0, 1); E_2 cos = -r (t -> t + pi); E sin = 0 (t -> -t). So
E cos(t_1 - t_2) = E cos E cos + E sin E sin = -r^2 < 0. d/dJ E_J cos t_1 = Cov_J(cos t_1, cos(t_1 - t_2)); at J = 0,
Cov(cos t_1, cos t_1 cos t_2) = Var_1(cos) E_2 cos = -r Var_1(cos) and Cov(cos t_1, sin t_1 sin t_2) = 0
(E_2 sin = 0). So the derivative is -r Var_1(cos) < 0. Continuity in J gives small J > 0. Precision: the
property of 3.11.1 that fails is "the covariance of two cosine characters is nonnegative" (lines
1041-1048), of which monotonicity in couplings is the consequence; in the two-site model the
two-point function itself stays monotone in its own coupling (its derivative is a variance).
Scope as stated (small J, fixed h): right.

**G2, redone by hand (lines 241-253). HOLDS.** With s_i = (tau^1_i c_i, tau^2_i s_i), the exponent is
J tau^1_1 tau^1_2 c_1 c_2 + J tau^2_1 tau^2_2 s_1 s_2 + h tau^1_1 c_1 - h tau^1_2 c_2. Species 2: 2e^{J s1 s2} + 2e^{-J s1 s2} = 4 cosh(J s1 s2).
Species 1: (+,+) and (-,-) give 2 e^{J c1 c2} cosh(h(c1 - c2)); (+,-) and (-,+) give 2 e^{-J c1 c2} cosh(h(c1 + c2)). Right.
At J = 0, Z^1 = 4 cosh(h c1) cosh(h c2), so a ~ cosh(h cos gamma). d_J log Z^2 = 0 at 0, and
cosh(x - y) - cosh(x + y) = -2 sinh x sinh y, cosh(x - y) + cosh(x + y) = 2 cosh x cosh y give U = -phi(c1) phi(c2).
With m = E_a gamma, p = E_a phi, k = Cov_a(gamma, phi): Cov_0(gamma1 gamma2, phi1 phi2) = (k + mp)^2 - m^2 p^2,
Cov_0(gamma_i, phi1 phi2) = p k, so d/dJ Cov_J(gamma1, gamma2) at 0 = -[k^2 + 2kmp] + 2mpk = -k^2. phi(cos gamma)
strictly decreases (c tanh(hc) strictly increases on (0, 1]), gamma strictly increases, a > 0, so k < 0
(Chebyshev: the double integral of (x - y)(phi(x) - phi(y)) a a is negative). Cov_0 = 0, so Cov_J < 0 for
small J > 0. The paper's split and claim (lines 1062-1068) are quoted right. Scope: right.

**7.4, the Ising long-range-order step (line 261). HOLDS.** The pointwise route bounds
Cov_0(F, tau_a tau_b) by Newman (11-1) in the signs, which yields sum_w l_{F,w} (E[tau_w tau_a | gamma] + E[tau_w tau_b | gamma]);
so a Newman form along that route needs these conditional correlations to decay uniformly in gamma.
Given (alpha, gamma), species 1 of the z-sector is a zero-field Ising model with couplings
b cos alpha_x cos alpha_y cos gamma_x cos gamma_y (lines 1064-1066, 1141-1144); at alpha = gamma = 0 it is b. For
b >= 2.3 > (1/2) ln(1 + sqrt 2) = 0.4407 the 2D Ising model is ordered; Peierls already gives a
lower bound on <tau_0 tau_x> uniform in x and in the torus (e^{-2b} <= 0.0101). The same holds for all
(alpha, gamma) with every coordinate below a small eps, so the failure is not a null-set artefact.
The paper's L^1 localization (line 1114) avoids it. "OPEN, not refuted": right.

**7.5, FST-N (lines 265-269). HOLDS AFTER CORRECTION (quantifiers and scope).** As written FST-N fixes no
norm of O, no dependence on |A|, and no comparison of two pin sets, so it cannot yet be proved or
refuted. Corrected text: "FST-N (OPEN). There are C, c, p > 0 such that for the O(4) sheet at every
beta in [2.3, 2.6], on every square Lambda with pins eta, eta' on its outer boundary, every bounded O
on A in Lambda that is invariant under the common left rotation obeys
|E^eta O - E^eta' O| <= C ||O||_inf |A|^p e^{-c d(A, dLambda)/Xi(beta)}; and the same with eta = eta' and two fields
of sup norm at most h_0 that differ only on a set Delta, with d(A, Delta) in place of d(A, dLambda).
(3.61) gives the pinned bound for charged O. FST-P needs more: the single-pin form, with d(A, y)
for pins that differ only at y (7.6). FST-F implies the field form." Two checks behind this text:
(a) (3.61) controls charged O through the distance to all pins only: with k0_{y->w} bounded by
e^{-c d(w, dLambda)/s} for each of the 4l pins, the Dobrushin-Shlosman sum is about 16 l^2 s/c, not
below l^2 (s is large). So this direct count does not give FST-P from FST-N plus (3.61); the route
needs the single-pin form of 7.6. This is a count, not a proof that the implication fails.
(b) FST-F implies the field form: for fields H, H' (sup norm <= h_0) that differ only on Delta,
E_H F - E_H' F = integral_0^1 Cov_{H' + s(H - H')}(F, (H - H').Phi) ds, the intermediate fields have sup norm
<= h_0, and FST-F bounds the integrand by 2 X h_0 sum_v Lip_v(F) sum_{u in Delta} e^{-2a|u - v|}.
Remark (not a correction): FST-N may be narrowed to observables invariant under the common left AND right rotations. The pinned law is invariant under
q -> qbar with pins eta -> etabar (qbar.rbar = q.r, Haar is inversion invariant), and q -> qbar exchanges
left and right; so (3.61) also covers observables with zero common-right average.

### Step 6 result: one serial guide run (GUIDE only; it proves nothing)

Script `scratchpad/chk1093/num.py` (session scratchpad, outside the repo), pure Python, run once with
`nice -n 10`, OMP/OPENBLAS threads 1, `python3 -I`. It uses a different data path from the hand
computations: G1 and G2 are integrated on a 1000 x 1000 grid in the original angles (theta_1, theta_2),
with gamma(theta) = atan2(|sin theta|, |cos theta|); the Z^1 Z^2 formula of G2 is not used. FST-BD is
tested on a 7-site Ising cycle (random J in [0.15, 0.35], fields in [-0.6, 0.6]) with single-site and
pair blocks, k = the largest block total-variation change under one outside flip, and 40 random f, g.
Output, verbatim:

```
G1 h=0.5: E0cos(t1-t2)=-0.058806 (-r^2=-0.058806); dJ Ecos t1 (fd)=-0.110626 (-r Var=-0.110627); Ecos(t1-t2) at J=.01: -0.053834
G2 h=0.5: Cov_J(g1,g2) J=0: 6.85e-14, J=.01: -5.134e-05; dJ Cov (fd)=-0.005380; -[Cov_a(g,phi)]^2=-0.005380; Cov_a=-0.07335
G1 h=1.0: E0cos(t1-t2)=-0.199264 (-r^2=-0.199264); dJ Ecos t1 (fd)=-0.158175 (-r Var=-0.158177); Ecos(t1-t2) at J=.01: -0.194597
G2 h=1.0: Cov_J(g1,g2) J=0: -2.33e-14, J=.01: -1.355e-04; dJ Cov (fd)=-0.013736; -[Cov_a(g,phi)]^2=-0.013736; Cov_a=-0.11720
G1 h=2.0: E0cos(t1-t2)=-0.486889 (-r^2=-0.486889); dJ Ecos t1 (fd)=-0.114591 (-r Var=-0.114591); Ecos(t1-t2) at J=.01: -0.483793
G2 h=2.0: Cov_J(g1,g2) J=0: 3.10e-14, J=.01: -1.380e-04; dJ Cov (fd)=-0.013849; -[Cov_a(g,phi)]^2=-0.013849; Cov_a=-0.11768
FST-BD single-site blocks a=0.0: gamma=0.542; max lhs/rhs: {'i': 0.8363404437452321, 'iii': 0.02059798145686718, 'iv': 0.019369463688169223}
FST-BD single-site blocks a=0.2: gamma=0.662; max lhs/rhs: {'i': 0.806775120774108, 'iii': 0.026672358111204362, 'iv': 0.014802775532344865}
FST-BD pair blocks a=0.0: gamma=0.489; max lhs/rhs: {'i': 0.6759287600761109, 'iii': 0.03772225248907848, 'iv': 0.014128509595897938}
FST-BD pair blocks a=0.2: gamma=0.665; max lhs/rhs: {'i': 0.6871074108987044, 'iii': 0.02231889488635026, 'iv': 0.010952499369356192}
```

Reading: G1's -r^2 and -r Var(cos) and G2's -[Cov_a(gamma, phi)]^2 agree with finite differences to five
digits or better for h = 0.5, 1, 2; Cov_J(gamma_1, gamma_2) < 0 at J = 0.01. No violation of FST-BD (i), (iii), (iv)
in the toy runs (largest ratio 0.84, in (i)). Guide only: a refutation attempt that found nothing.

### Step 7 result: verdicts and the four judgements

Who checked what: every item below was checked line by line by me, Claude Opus 5.5 max (laptop
subagent, row 1093), against row 1091's text, row 1077 (face law, (9), (16), (17)), row 1078 (O7, J1)
and the posted paper (Theorem 3.1, Sections 3.10-3.11, blob a496bb8e). Same provider as the author
(Claude Fable 5.2 medium), so this is not a cross-provider check. I did not read row 1094's file.
Nothing was formalized in Lean. The step 6 run is a guide only.

| # | Item (row 1091 lines) | Verdict |
|---|---|---|
| 1 | M1 (38) | HOLDS (h_p is the conjugate only when e is not inverted; nothing uses it) |
| 2 | M2 (40): Lipschitz dependence, at most one common square, six neighbours | HOLDS |
| 3 | Paper facts used (28-30) | HOLDS |
| 4 | FST-BD setting (67-71) | HOLDS AFTER CORRECTION (step 4 text: admit the discrete metric) |
| 5 | (C), (D_a), statement (73-99) | HOLDS |
| 6 | Step A, (BD1) (101-107) | HOLDS |
| 7 | Step B, (i) and the weights (109-113) | HOLDS |
| 8 | Step C, (ii) (115) | HOLDS |
| 9 | Step D, (BD2) (117-121) | HOLDS |
| 10 | Step E, (iii): 1/N bookkeeping, weight, shift (123) | HOLDS AFTER CORRECTION (one phrase on mu(g + c); bound unchanged) |
| 11 | Step F, (iv) and its shift (125) | HOLDS |
| 12 | Remarks: no truncated block, no conditioning on B (127) | HOLDS |
| 13 | FST-P hypothesis, theorem, admissible choice (135-153) | HOLDS |
| 14 | FST-P proof: three influence terms, count, 2l - 1, constant (155-163) | HOLDS (given item 4) |
| 15 | Corollary (17) from FST-P; bounded to Lipschitz; local limits (165, 302) | HOLDS AFTER CORRECTION (torus-size and continuity wording, step 4) |
| 16 | FST-F hypothesis and theorem (169-179) | HOLDS |
| 17 | FST-F proof: interpolation, convexity, (D_a) with S_a, (I) (181-193) | HOLDS |
| 18 | Remark on the size of eps (195), GUIDE | HOLDS AFTER CORRECTION (eps ~ a^2/X, step 5 text) |
| 19 | FST-T and Proposition FST-T (201-209) | HOLDS |
| 20 | Strength claims (63, 211) | HOLDS AFTER CORRECTION (text below) |
| 21 | Lemma K3 against Theorem 3.1 as posted (215-223) | HOLDS (distances are max-norm) |
| 22 | 6.2 consequence (225) | HOLDS as ARGUED |
| 23 | Loss of rate c/(n+1) (227) | HOLDS as ARGUED |
| 24 | G1, redone by hand (233-237) | HOLDS |
| 25 | G2, redone by hand (241-253) | HOLDS |
| 26 | 7.4, Ising long-range-order step (261) | HOLDS |
| 27 | FST-N statement and its role (265-269, 313) | HOLDS AFTER CORRECTION (step 5 text, and J3 below) |
| 28 | Control against row 1078 O7(b) (293) | HOLDS; no conflict |

Count: 28 items; 22 HOLD (two of them as ARGUED), 6 HOLD AFTER CORRECTION (items 4, 10, 15, 18,
20, 27), none FAILS.

**J1. Does FST-BD hold as stated?** Yes for its stated setting: every inequality, (BD1), (BD2), the 1/N
bookkeeping ((1/N) sum theta^n = 1/((1 - gamma) n_min)), the weights in (i), the shifts in (iii) and (iv), and
the claim that no truncated block is used all check. Two text corrections: line 67 must admit a
metric rho_x that does not define the topology, because line 69 and FST-P use the discrete metric on
S^3, which is not compact; and line 123's "mu(g + c) tends to 2 ||g||" must read
"mu(g + c) <= ||g|| + c, which tends to 2 ||g||". No inequality changes.

**J2. Is FST-F weaker than or comparable with FST-P? Yes: FST-P implies FST-F.** This follows from FST-BD (iv)
in a few lines; row 1091 says (line 211) that it did not prove it. Derivation (checked by me): take one
sheet on a torus D with L, M >= l + 2, a fixed field H with sup |H_u| <= h, the discrete metric, and the
blocks z + Lambda, z in D (N = |D|, n_u = l^2). The block law is the zero-field pinned law tilted by
exp{sum_u H_u.Phi(u)}, so as in item 14, (C) holds with k = k0 + 2(e^{2 h l^2} - 1) for the 4l pins and k = 0
otherwise, and (D_a) holds with gamma' = e^{a(2l-1)} [gamma_0 + 8l(e^{2 h l^2} - 1)]. (I) holds on each block with
X_I = e^{2a(l-1)}/4, since |Cov(F, G)| <= osc(F) osc(G)/4 <= (1/4)(sum_u osc_u F)(sum_b osc_b G) and |u - b|_1 <= 2(l - 1)
in a block. FST-BD (iv) and osc_x <= pi Lip_x give, for gamma' < 1,
|Cov_H(F, G)| <= (pi^2 e^{2a(l-1)} / (4(1 - gamma'))) sum_{v,w} Lip_v(F) Lip_w(G) e^{-a|v - w|_1},
that is FST-F(h, a/2, pi^2 e^{2a(l-1)}/(4(1 - gamma'))) with L_0 = l + 2. No converse is known to me.
Corrected text for line 63: "(i) isolate the statement as a hypothesis, in three forms (FST-P pinned
square; FST-T zero-field multi-point; FST-F small field). FST-P and FST-T each imply FST-F; no
implication between FST-P and FST-T is proved." Corrected text for line 211, sentences 2-4: "FST-P
gives (17) directly, and it also gives FST-F by FST-BD (iv) with the discrete metric and the trivial
block bound (I) (check row 1093). I did not prove FST-T from FST-P. So FST-F is the weakest of the
three; I do not claim that it is the weakest statement that exists."

**J3. Is FST-N correctly named as the first missing input?** Yes on the pinned route, which by J2 serves
both theorems: the paper gives charged decay with pins ((3.61), line 1004) and its only route to
the other observables needs the unpinned zero-field ferromagnet (line 1020). Three precisions. (a) FST-N
needs quantifiers (corrected text in step 5). (b) It is the first missing input, not the only one:
FST-P needs a single-pin form, and my count (step 5, (a)) shows that (3.61)'s form gives a
Dobrushin-Shlosman sum of order 16 l^2 s/c, not below l^2 (a count, not a refutation); the 7.6 step (weak to strong mixing for S^3
spins) is the next unverified input, as row 1091 itself says. (c) On the field route the charged part
is missing too, since (3.6) fails in a field (7.3); so for a field, FST-N is not the first missing
input, but the pinned route avoids the field. Corrected text for line 313, last clause: "and the first
missing input on the pinned route is FST-N (quantified as in row 1093); the step from it to the
single-pin form of FST-P is a further unverified input (7.6)."

**J4. Does any item conflict with row 1078's O7(b)? No.** O7(b) says that (14) uses only K_0 >= 0, the gap
and osc V, that it is sharp, and that a size-uniform interval must use the product form over sheets,
the locality of V and the decay of the sheets' correlations. FST-BD, FST-P and FST-F use exactly
these: M1 (product of sheets with a one-site field), M2 (six neighbours, one site), and a decay
hypothesis (FST-P or FST-F). They never use the anchor gap or ||V||. Example (16) has a pin and a
diagonal (frozen) transfer kernel, so it is not a positive-density lattice law of FST-BD's setting.
Row 1091 line 293 says this correctly. One related note: K3 refines row 1078 O7(c)'s clause that
Theorem 3.1 "says nothing ... about third cumulants" (at lambda = 0 it does give them); O7(c)'s conclusion,
that the posted two-point bound gives no positive interval by any written step, stands, and row 1091
agrees (7.7).

### Step 8 result: limits of this check

- Same provider as the author; not an independent cross-provider check. Row 1094 (astra) not read.
- No Lean formalization. The step 6 run is a guide; no verdict rests on it.
- Literature statements of row 1091 marked "from memory" (Dobrushin-Shlosman, Martinelli-Olivieri-
  Schonmann, Follmer, Kunsch, Statulevicius, Messager-Miracle-Sole-Pfister) were not checked; none
  carries a PROVED mark. Peierls and the 2D Ising critical value are cited, not rebuilt.
- 6.2 and the c/(n+1) loss were checked as outlines only, as row 1091 marks them.
- Files changed: this file only. Scratch script and output in the session scratchpad (`chk1093/`).
  No download: the paper copy is row 1078's, hash-checked against openai/math by two read-only
  `gh api` metadata queries (blob hash, commit list); nothing was saved from them. No commit, no push.

RESULT: row 1091 (gap-face-stability.md) checked line by line by Claude Opus 5.5 max, same provider as its author: 28 items, 22 HOLD (two as ARGUED), 6 HOLD AFTER CORRECTION (FST-BD's setting must admit the discrete metric that FST-P uses; one phrase on mu(g + c) in (iii); the torus-size and continuity wording of the corollary to (17); the GUIDE size of eps, of order a^2/X not 1/X; the strength claims, since FST-P implies FST-F by FST-BD (iv) with the trivial block bound, while FST-P and FST-T are not compared; FST-N needs quantifiers and is the first, not the only, missing input on the pinned route), none FAILS; every inequality of FST-BD (i)-(iv), FST-P, FST-F, FST-T, K3, G1 and G2 checks, with G1 and G2 redone by hand and matched by one guide quadrature; 6.2 and the c/(n+1) loss hold as ARGUED; no item conflicts with row 1078's O7(b); target (17) on a positive interval stays OPEN; not formalized; no mass gap claimed.
