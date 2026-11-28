lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T13:03Z

# Check of row 1028 (`library/gap-uv-rigidity-max.md`), FINISH row 1030

Checker: Claude Opus 5.5, max effort, Mac mini worker 3. Author of the checked
file: Claude Fable 5.2 (same provider, so this is not an independent-provider
check). Pinned at commit 85d8dfc6d. No subagents. Started 2026-11-16 01:03Z.

Verdicts used: HOLDS, HOLDS AFTER CORRECTION, FAILS (with the first failing
line). No new attack (row 1030).

## Plan (at most eight steps; one per response, each appended before the next)

1. Read FINISH.md rules (efficiency, build on published work), the checked file
   `library/gap-uv-rigidity-max.md` in full, and the definitions it relies on
   (engine axioms, Proposition OM, Omega, D, (W), (LIOU), (BDD-Delta)) in
   `library/gap-compact-rigidity-max.md` and its checks. Record anchors.
2. Test first: Lemma FV, the count of zero modes on the smallest torus, then the
   whole proof of D(n; beta) >= (3/2) log beta - 59 n^4 - 11 (SU(2), beta >= 16).
3. Test first: Proposition CONST against the engine's axioms as stated in
   `library/gap-compact-rigidity-max.md` (constant c critical iff c = log m,
   m >= 2 an integer), with Proposition FRZ.
4. Test first: the family TS against every kept property.
5. Lemma REC and REC+ (exact definition of uniformly recurrent in Proposition OM).
6. Lemma ALPHA, Corollary KEPT, Proposition A1, Proposition TWO, Lemma EXCL,
   Corollary CR-1, Proposition MON+.
7. The GUIDE-grade correction: U(1) with growing beta and five dimensions in
   branch (II); the remaining controls; work item W1 if the file names one.
8. Verdict table and RESULT line.

## Step log

(Each step's result is appended below as it completes.)

### Step 1 (done): sources read, scope, duplicate check

Read in full: `GOAL.md`; `FINISH.md` L1-85 and L299-356 (rules, efficiency, save protocol) and rows 1028, 1030
(L1109, L1111); the checked file `library/gap-uv-rigidity-max.md` (1165 lines, every line). Read at the cited
ranges: `library/gap-compact-rigidity-max.md` ("R") L125-299 (definitions 3.1, Lemma UF, Theorem CE, the table of
3.4, Proposition OM, Theorem CR, the data A_(m,eps), Lemma PT-inf, Proposition NR, Proposition SI, the test
table) and L350-354 (Corollary TRI); `library/gap-compact-rigidity-check-opus.md` ("CO") L120-243 (OM, LV, CR,
TRI, A_(m,eps), PT-inf, SI, defect list); `library/gap-compact-rigidity-check-astra.md` ("CA") items 11-15,
19, 20 (L231-282, L355-404) and disagreement 2 (L442-450); `library/gap-dichotomy.md` L78-137 (datum, (S0), P,
D^+, (PHYS-SEED), (BDD-Delta), (W), eternal datum, admissible sequence, Omega(D_0), critical element with repair
D8, uniformly recurrent); `library/gap-crux-restate.md` L25-49 (the lane's f).

Anchors this check uses:
- f := inf over all tori n (sides >= 3, unequal allowed) of F(n)/abs(n); F(n)/abs(n) is non-increasing in each
  side (`gap-crux-restate.md` L39). Delta = F - f abs(n) does not change if each link measure is rescaled or a
  constant is added to each plaquette action (both change F by a multiple of abs(n)). So Lemma FV's use of
  normalised Haar measure is the lane's D.
- Critical element (gap-dichotomy L131-134, repair D8): spectral form in each direction; s_* >= 1/5041;
  d_min <= D_* <= D_0; z_*(b) <= 256 D_*(b/4) + 34.11. The centre grading is CE (ii)(e), a property of limits,
  not a clause of the definition.
- Uniformly recurrent (R L230, gap-dichotomy L135-136): "the integers t with abs(sigma^t E - E) < eps on that
  set have bounded gaps". The proof of OM (d) gives the two-sided syndetic form (CA L262-271: every interval of
  2N + 1 consecutive integers holds a return).
- Corollary TRI (R L350-354): (I) (PHYS-SEED); (II) (BDD-Delta) fails; (III) a uniformly recurrent critical
  element (CO D3: of Omega(D_0) of this family, for some D_0). So "branch (II)" means: (BDD-Delta) fails.

Duplicate check (rule 0a): `grep -n -i "uv-rigidity"` over `FINISH.md` and `library/open-core.md`: rows 1028
(the checked row) and 1030 (this row) only. This row is a check, not an attack; no open lemma is attacked.

Provenance of this check: Claude Opus 5.5 checks Claude Fable 5.2. Same provider, different model. It is one
reading, not an audit, and not independent in the provider sense.

### Step 2 (done): Lemma FV (source 4.1, L539-669). Verdict: HOLDS

**Test first: the count of zero modes on the smallest torus (n = 3).** Checked by a route the source does not
use: the linearised complex at a flat point, not the dimension of the moduli set.

- Sizes at n = 3: N = 81 sites, 4N = 324 links, 6N = 486 plaquettes. Comb tree T: (n - 1)(n^3 + n^2 + n + 1) =
  2 x 40 = 80 = N - 1 links. Interior links: 4 n^3 (n - 1) = 216; interior links outside T: 216 - 80 = 136 =
  3 n^4 - 4 n^3 + 1 = M. Wrapping links: 4 n^3 = 108. Slice: 136 + 108 = 244 = 3N + 1 links, real dimension
  3 x 244 = 732 = 9N + 3. All as the source states.
- Linearised complex at U^H: C^0 = su(2)^N, C^1 = su(2)^(4N), d_0 the infinitesimal gauge map, d_1 the
  linearised plaquette map. For H generic abelian (some H_mu not central), the adjoint system splits into the
  Cartan line (trivial monodromy) and a rank-one complex line with monodromies e^(2 i theta_mu), not all 1. The
  trivial line has H^0 = R, H^1 = R^4 on the four-torus; the charged line has zero cohomology (Kunneth on each
  circle factor). So dim ker d_1 = dim im d_0 + dim H^1 = (3N - 1) + 4 = 3N + 3. Restriction of ker d_1 to the
  tree is onto su(2)^(N-1) (integrate xi along T from the origin), so dim(ker d_1 on the slice) =
  3N + 3 - 3(N - 1) = 6. This equals the source's count (four angles and an axis; Remark 1). Stiff directions:
  732 - 6 = 726 = 9N - 3 at n = 3, and 9N - 3 for every n >= 3. At the sixteen central points (all H_mu = +-1)
  the same count gives H^0 = 3, H^1 = 12, and 12 zero modes on the slice (Remark 2's "twelve constant modes").
- The count is not used by the proof. The lower bound reads only the explicit packing (B5) of a 6-parameter set
  of flat points. A larger flat set would only weaken the bound; a smaller one would contradict (B5), which is
  proved directly. So the count supports Remark 1 and does not carry any step.

**Part A, re-derived.**
- (A1) Haar on SU(2) pushes to (2/pi) sin^2 phi d phi on [0, pi] (total mass 1); tr U = 2 cos phi. sin^2 phi
  <= phi^2; 1 - cos phi = 2 sin^2(phi/2) >= 2 phi^2/pi^2 (Jordan on [0, pi/2]). The Gaussian moment
  int_0^inf phi^2 e^(-a phi^2) = (sqrt(pi)/4) a^(-3/2) with a = 2 beta/pi^2 gives (pi/2)^(5/2) beta^(-3/2).
  Right.
- (A2) Comb tree: n^4 - 1 links, connects every site to the origin, so spanning. For l = (x, mu) interior and
  outside T, nu = least index below mu with x_nu > 0. The two nu-links of p(l) sit at x - e_nu and
  x - e_nu + e_mu; their coordinates below nu are those of x, which are 0 by the choice of nu, and both are
  interior; so both lie in T. l' = (x - e_nu, mu) is interior. Injectivity: if p(l_2) = p(l_1), l_2 is a
  non-tree link of p(l_1), so l_2 = l_1 or l_2 = l_1'; in the second case the least corner of p(l_2) is
  x - e_nu - e_nu', which is not a corner of p(l_1) (no wrapping occurs). Order: for i < k, l_k in p(l_i)
  forces l_k = l_i' and h(l_k) = h(l_i) - 1, against h non-decreasing. Right.
- (A3) Weights are at most 1, so dropping all but the M kept ones bounds Z above. Integrate l_M, then l_(M-1),
  and so on: at the step for l_k the kept weights left are p(l_1), ..., p(l_k), and l_k lies in p(l_k) only;
  it enters U_p once, as U_l W or U_l^(-1) W; Haar invariance gives I(beta). Right.
- (A4) f <= F(n)/n^4 <= (M/N) log I and M/N = 3 - 4/n + n^(-4) -> 3; since log I <= 0, f <= 3 log I. Numbers:
  (15/2) log(pi/2) = 3.3869 < 3.42; the source's route (1.5708^5 = 9.563 < 9.57 < 9.61 = 3.1^2;
  log 3.1 = 1.1314 < 1.14) is right.

**Part B, re-derived.**
- (B1) U -> (U on T, V) with V_l = g_x U_l g_y^(-1), g_x the product along T: a bijection onto
  SU(2)^(N-1) x slice; A is gauge invariant; Haar invariance on each non-tree link. Right.
- (B2) U^H flat: in a (mu, nu) plaquette the two mu-links are both interior or both wrapping. Right.
- (B3) Telescoping for products of unitaries, norm(A^(-1) - B^(-1)) = norm(A - B), tree links contribute 0,
  and the holonomy of U^H is 1: norm(V_p - 1) < 4r; (4.1) gives 1 - (1/2) tr V_p < 8 r^2; 6N plaquettes give
  A(V) < 48 N r^2. Right.
- (B4) The ball of chordal radius r about 1 is the cap phi < alpha, r = 2 sin(alpha/2), so alpha >= r and
  alpha <= pi/3 for r <= 1; (2/pi) int_0^alpha sin^2 t dt >= 8 alpha^3/(3 pi^3) (sin t >= 2t/pi);
  3 pi^3/8 = 11.63 < 12. Left translation carries every ball to this one. Right.
- (B5) |Theta| = floor(pi/(2 delta)) + 1 >= pi/(2 delta); the a- and b-grids each have at least 1/(2 delta)
  points; pi^4/64 = 1.52 >= 1. Same axis: t in [delta, pi/2], distance 2 sin(t/2) >= 2t/pi >= delta/2. Two axes:
  the grid gives abs(e - e') >= delta, and abs(s e - s' e')^2 = (s - s')^2 + s s' abs(e - e')^2 >= delta^2/2
  with s, s' >= 1/sqrt(2) (theta in [pi/4, 3 pi/4]). The links ((n - 1) e_mu, mu) wrap, so they lie outside T
  and read H_mu; disjointness follows. Right. (Wording: "two different tuples" means two different parameter
  choices; (B5) itself shows they give different H.)
- (B6) r = beta^(-1/2) <= 1/4 iff beta >= 16. Powers of beta: (4r)^(-6) gives beta^3, (r^3)^(3N+1) gives
  beta^(-(9N+3)/2); total beta^(-(9N-3)/2). Right.

**End of proof, re-computed.** D >= (3/2) log beta - (48 + 3 log 12 + 3.42) N - (6 log 4 + log 12). Exact
values: 3 log 12 = 7.4547, so the coefficient is 58.875 < 58.92 < 59; 6 log 4 + log 12 = 8.3178 + 2.4849 =
10.803 < 10.84 < 11. The source's bounds (log 12 < 2.5 from e^2 > 7.38, e^0.5 > 1.64, 7.38 x 1.64 = 12.10;
log 4 < 1.39) are right.

**W1 (ii): is the f of Lemma FV the lane's f?** Yes. The lane's f is the infimum over all tori with sides at
least 3 (`gap-crux-restate.md` L39), and Lemma FV uses exactly this infimum, bounded above through the symmetric
tori in (A4). Normalised Haar measure gives the lane's Delta (Step 1 anchors).

**Consequences checked.** 4.2 first bullet: given beta_j -> infinity, D_j(n) -> infinity at each fixed n.
Right; these tori have physical side n a_j -> 0. "The count kappa = 3 of row 720 has a proved lower half":
right, since 3 log(1/g) = (3/2) log(beta/4) with beta = 4/g^2. The constant 59 n^4 + 11 grows with n, so FV
says nothing at a fixed physical size of the trajectory; the source says so (4.2, second bullet, and 8.8).

**Not checked as proofs (marked so in the source):** Remark 2 (GUIDE), Remark 3 (ARGUED), Remark 5 (ARGUED;
judged in Step 7 below).

Verdict: **Lemma FV HOLDS.** First failing step: none. No repair needed.

### Step 3 (done): Proposition CONST (4.4, L725-745) and Proposition FRZ (4.3, L686-723)

**Test first: CONST against the engine's axioms as row 1017 states them.** R names the engine twice: L28
(Theorem S, Corollary S3', Lemmas A, K, X, E of `gap-crux-restate.md` L37, L178-219) and A3 at L81 (Theorem S,
Theorem SH, Proposition Delta, Lemmas Z, Z', Z3, Theorem ZD, Corollary Z4: "each is a finite chain of
inequalities between values of Z at finitely many tori"). The centre data are A4 (L82: flips commute with T,
twisted partition functions are traces with C_nu inserted, 0 <= Z_odd <= Z). Two independent checks:

- (Route 1, structural.) The lemmas of `gap-crux-restate.md` 3.4 are proved in the setting of its L174: a
  positive symmetric W(a, b) = Tr T_b^a with ell finite. That is (E1)-(E3). CO 6.4 (L172) says the same for
  Lemma Z3 and Theorem S, and R's own proof of CE (ii)(d) applies Proposition Delta and Lemma Z "for each datum".
  So every engine inequality holds for each datum A_(m,eps), and, being non-strict and finite, passes to the
  limit constant log m by CE (ii)(c). Strict statements do not pass: "the top eigenvalue is simple" fails for
  log m (m-fold vacuum), which R's table 3.4 lists as "can be lost". The definition of a critical element
  (repair D8) does not ask for it.
- (Route 2, direct, on the constant itself; e_0 = 0, the gap 0, S = m - 1, Delta = D = log m at every size.)
  A2 / CE (c) first example: log m <= 2 log m. Proposition Delta: log m <= (b/a)^3 log m (b >= a) and m - 1 <=
  m^8 - 1. Theorem S: m - 1 <= (m^64 - 1)^2. Lemma K: the deficit is 0, so non-negative and non-increasing.
  Lemma X: a.0 + log m = b.0 + log m. Lemma E: m <= m^(2b/(b-a)). Lemma E': m <= m^(h/(b-a)) with h >= b > b - a.
  Lemma Z (as used in CE Step 5): m - 1 <= exp(64 log m - 0) = m^64. Every one holds for every integer m >= 2.
  Theorem ZD and Corollary Z4 are equivalences and dichotomies built from these; at a constant they give branch
  G (no seed, bounded D), which is what the constant is.
- Centre data (A4 and CE (ii)(e)). With all m levels even: zeta = 1, Z_odd = 0, so 0 <= Z_odd <= Z holds; the
  vacuum is even; the three flips give the trivial joint Z_2^3 grading; the twisted functions equal the
  untwisted ones, so the symmetry Z^(mu nu) = Z^(nu mu) of (TM-c) holds. No engine statement in R's two lists
  reads a twisted function (R L409 says the engine reads the periodic seed, flux sectors included).

Result of the test: no axiom R states excludes a constant log m, m >= 2. CONST (iii) holds as stated.

**CONST (i), re-derived.** "Only if": with Delta = c at (T, B) for every dyadic T, e_0 < 0 makes the right side
unbounded as T -> infinity; e_0 > 0 makes it tend to 0 (domination: for T >= T_1, sum exp(-T e_r) <=
exp(-(T - T_1) e_0) sum exp(-T_1 e_r)); so e_0 = 0, its multiplicity m(B) is at most e^c, and the remainder
e^c - m(B) is independent of T and tends to 0, so it is 0; there is no finite level above 0, e^c = m(B) for
every B, so m is one integer; s_* = m - 1 >= 1/5041 forces m >= 2. "If": the constant log m has the spectral
form (m levels at 0, the rest +infinity), s_* = m - 1, D = log m in [d_min, D_0] when log m <= D_0, z_* = 0 <=
256 log m + 34.11; it is also the limit of A_(m,eps) (CA item 21, CO 7.1). Right. **(ii)** is the clause
D_* <= D_0 of the definition. Right. **(iii)** follows from (i) and the test above. Right.

**Verdict: Proposition CONST HOLDS.** First failing step: none.

**One marking defect in the remark after CONST and in table 4.5 (row "for a finite c, link (c) names a family
... PROVED for the constants and sums; the photon member is BELIEF").** For a given finite c the proved members
are only the constant c itself (when c = log m): a sum of constants is a constant, and Lemma PT-inf (i) produces
a non-constant member only from a non-constant limit with D constant on the diagonal, of which the record has
only the photon limit (BELIEF, I10). So "more than one element with D = c" is BELIEF, not PROVED. Repair:
"for a finite c = log m the proved member is the constant log m; that the set is larger rests on the photon
limit (BELIEF)". It changes no verdict: for the SU(2) value the set is empty (CONST (ii)), and for a finite
value the constant alone already defeats "exclude it by the axioms" (CONST (iii)).

**Proposition FRZ, re-derived. Verdict: HOLDS.**
- (i) Flat count. The map of (B1) is a bijection onto G^(N-1) x slice for finite G too. A flat slice field is
  1 on every interior link by induction on h: flatness of p(l) with its two nu-links in T gives V_l = V_l', and
  l' is in T or an interior non-tree link of lower h. A plaquette with one wrapping mu-link and interior nu-links
  gives V_(x, mu) = V_(x + e_nu, mu); the sites with x_mu = n - 1 form an open grid {0..n-1}^3, connected by such
  steps, so the wrapping mu-links carry one H_mu. A plaquette wrapping in both directions gives H_mu H_nu =
  H_nu H_mu. With (B2): flat slice fields are the U^H with H a commuting 4-tuple. Count abs(G)^(N-1) c_4(G). This
  agrees with the standard count of flat lattice fields, sum over conjugacy classes [rho] of Hom(Z^4, G) of
  abs(G)^N/abs(C(rho)) = abs(G)^(N-1) abs(Hom(Z^4, G)), a second derivation. Z -> c_4 abs(G)^(-3N-1). Right.
- (ii), (iii): F >= log c_4 - (3N + 1) log abs(G) at every beta, c_4 >= abs(G), so f >= -3 log abs(G); f <=
  F(n)/abs(n) for every n gives the upper limit. Delta -> log(c_4/abs(G)) at each fixed torus. Right (the limit
  is beta -> infinity at each fixed size, as the source says).
- (iv) Burnside: orbits on commuting triples = (1/abs(G)) sum_g c_3(C_G(g)) = c_4/abs(G). Recursions re-checked
  by hand with the class data of Q_8 (centre 2, six elements with centraliser C_4) and 2T = SL(2,3) (centre 2,
  six elements of order 4 with centraliser C_4, sixteen of order 3 or 6 with centraliser C_6; 2 + 6 + 16 = 24):
  Q_8: 8, 40, 176, 736, m = 92. 2T: 24, 168, 1008, 5856, m = 244. Z_2: 16/2 = 8. Cross-check: c_2 = abs(G) k(G)
  with k = 5 classes for Q_8 (40) and k = 7 for SL(2,3) (168). Right.
- Remark (3) keeps the large-but-finite-beta limit sets of Q_8 and 2T at BELIEF. Right as marked.

### Step 4 (done): the family TS (3.5, L460-498) and the product of 3.6 (L502-513)

**Test first: TS against every kept property.** "Kept" = the list of R 3.4 (L202-208): (K1) spectral form with
non-negative integer multiplicities in each direction; (K2) symmetry under exchange of axes; (K3) the engine,
CE (ii)(c); (K4) the centre grading, CE (ii)(e); (K5) the gapless branch at every scale, CE (ii)(d). Plus the
family-level hypotheses that every statement about Omega needs: (S0), (BDD-Delta), failure of (PHYS-SEED).

- Datum. Each factor is A_(m,eps) (R L253) with eps = eps_j/u_j^4 and eps = (rho u_j)^(-4). A product of data is
  a datum: T_B = T^1_B (x) T^2_B, top eigenvalue 1 x 1 simple, Z(k, B) = Tr (T^1 (x) T^2)^k; log Z(n)/abs(n) > 0
  and tends to 0, so f = 0 (CO fact (F2)). (K1), (K2) hold for every datum, and (K3) for every datum (Step 3,
  route 1).
- Units. u_j = 12 x 2^j: u_j/4 = 3 x 2^j is an integer at least 3, so (S0); 2^i u_j/4 = 3 x 2^(i+j) >= 3 for
  j >= -i, so (S0-Z).
- Continuum datum. abs(u_j x) = u_j^4 abs(x), so Delta_j(u_j x) = log(1 + (m_0 - 1) e^(-eps_j abs(x))) +
  log(1 + (p - 1) e^(-abs(x)/rho^4)), increasing in j to E_c(x) = log m_0 + log(1 + (p - 1) e^(-abs(x)/rho^4)).
  Right.
- Ultraviolet value. With w = (p - 1)(1 - e^(-y))/p in [0, 1): log(1 - w) >= -w/(1 - w) and w/(1 - w) =
  (p - 1)(1 - e^(-y))/(1 + (p - 1) e^(-y)) <= (p - 1)(1 - e^(-y)) <= (p - 1) y. So log(m_0 p) - (p - 1)(L/rho)^4
  <= D^+(L) <= log(m_0 p), and D^+(L) > log m_0 strictly at every finite L. Right (this is repair 4 of the
  source's Section 7, now correct).
- (BDD-Delta). For L >= rho l_1, e^(-(L/rho)^4) <= 1/e. Right; take L_0 = the least element of P at least
  rho l_1 (rho need not be a power of 2; wording only).
- (PHYS-SEED) fails. Thermal sums of a product: 1 + S = (1 + S_1)(1 + S_2), so S >= S_1 = (m_0 - 1)
  e^(-eps_j l^4/2) -> m_0 - 1 >= 1 at every size l. Right.
- Limit set. At scale 2^m along (j_i, k_i): S_1 = (m_0 - 1) e^(-gamma_i 16^m/2), S_2 = (p - 1)
  e^(-16^(k_i+m)/(2 rho^4)) -> 0. If gamma_i >= gamma > 0 on a subsequence, pick m with (m_0 - 1)
  e^(-gamma 16^m/2) < 1/10082; then s = S_1 + S_2 + S_1 S_2 < 1/5041 for large i there, against (H2). So
  gamma_i -> 0 and every limit is log m_0 + 0. Non-empty: k_i = i, eps_(j_i) <= 16^(-3i) gives gamma_i <=
  16^(-2i); (H1) by log(1 + z) <= z; (H2) since s >= (m_0 - 1) e^(-16^(m - 2i)/2) -> m_0 - 1. Right. The
  argument uses no property of D_0 beyond D_0 >= log m_0, so Omega(D') = {log m_0} for every D' >= log m_0.
- (K4), (K5) on the limit: the constant log m_0 is a critical element (Step 3), with the trivial grading
  (abstract data carry no flips; put Z^(1 nu) = Z, so 0 <= Z_odd = 0 <= Z).
- Verdict on (a) for TS. The only element is log m_0, uniformly recurrent (fixed by sigma), with limit
  log m_0 at minus infinity. In the fixed-size form c_UV = D^+(L_1) > log m_0 for every L_1; in the limit form
  c_UV = log(m_0 p). So (UV-KEPT; c_UV) is false in both forms. Right.

**Verdict: the family TS HOLDS.** It is a family of data with units in the sense of `gap-dichotomy.md`
L85-101 (W1 (iii): yes), with (S0-Z) as well, and its limit set is as stated. First failing step: none.

**The product of 3.6 (the divergent law), re-derived.** On every torus D_(X x Y) = D_X + D_Y with 0 <= D_Y <=
log m (Lemma PT (a) for abstract data, CO (F2)); S_(X x Y) >= S_Y = (m - 1) e^(-eps_j (l u_j)^4/2) -> m - 1 at
each fixed l because eps_j u_j^4 -> 0; so X x Y has no seed; (BDD-Delta) for X gives it for X x Y with
D_0 + log m; CE (i)(b) gives Omega(X x Y) not empty; by KEPT (4) the divergent law is not kept. Lemma FV's
lower bound holds for X x Y since D_Y >= 0. Right, and conditional on (BDD-Delta) for X, as the source says.

**Checker's remark (ARGUED here, a sketch; used for no verdict).** The conditional can be removed with a
TS-type family whose ultraviolet law diverges: Z_j = A_(m_0, eps_j/u_j^4) x prod over i = 0..j of
A_(2, 16^i/u_j^4). Then D^+(L) = log m_0 + sum over i >= 0 of log(1 + e^(-16^i L^4)) (L in units of l_1):
bounded for L >= 1, and at least (k + 1) log(1 + e^(-1)) at L = 2^(-k), so it diverges as L -> 0; there is no
seed (S >= S_1); along any admissible sequence the extra factors contribute at most sum over i of
e^(-16^(i + k_i) abs(x)) -> 0, so Omega = {log m_0}. So even a divergent ultraviolet law, joined to every kept
property, does not give link (a). This agrees with the source's conclusion (a proof of (a) must read the whole
state space, rule W2) and does not change it.

### Step 5 (done): Lemma REC (2.4, L254-284), Lemma REC+ (6.2, L903-910), Lemma EXCL (3.3, L408-417)

**Test first (the source's own point 1 of Section 7): does "bounded gaps" give returns unbounded below?** The
definition (R L230, gap-dichotomy L135-136) says "the integers t with abs(sigma^t E - E) < eps on that set have
bounded gaps", t ranging over Z. Read as "syndetic in Z" (there is N such that every block of N consecutive
integers holds such a t), the set is unbounded in both directions. This is the form the proof of OM (d) gives
(every block of 2N + 1 consecutive integers holds a return: CA L262-271, with the 2N + 1 repair of CA L442-450),
so every element that (LIOU) speaks of has it. A one-sided reading ("consecutive returns differ by a bounded
amount", which allows a set bounded below) would not give the step directly; the conclusion would still hold,
because a point with syndetic forward returns has a minimal orbit closure (Birkhoff), and in a minimal set the
cover argument of OM (d) gives two-sided returns, but the source does not prove that. Precision P1 (wording, no
statement breaks): say "syndetic in Z" in the definition, as CA reads it.

**REC (i), re-derived.** Lambda o sigma^s is continuous on Omega, so U = {E'' in Omega : abs(Lambda(sigma^s E'')
- Lambda(sigma^s E)) < eps} is relatively open and contains E. The topology of Omega is the subspace topology
of the product over the countable set DD^4, so U contains a basic set {E'' in Omega : abs(E'' - E) < eps' on F},
F finite. Returns of E to it are syndetic in Z, hence there are t_n -> -infinity with sigma^(t_n) E in U, that
is abs(Lambda(sigma^(s + t_n) E) - Lambda(sigma^s E)) < eps; and Lambda(sigma^(s + t_n) E) -> c. So
abs(c - Lambda(sigma^s E)) <= eps for every eps. Right. Its special case: D_E(2^m) -> c gives D_E(2^m) = c for
every m (Lambda_D is a coordinate). Right.

**REC (ii)** (t -> +infinity) is the same with returns unbounded above. Right.
**REC (iii).** Each coordinate Lambda_x(E) = E(x) is continuous; a pointwise limit at -infinity gives
E(2^s x) = c_x for every s, so E(2x) = E(x). Right.
**REC (iv).** For each s and eps there are t_n -> -infinity with Lambda(sigma^(s+t_n) E) < Lambda(sigma^s E) +
eps; so liminf at -infinity <= inf over s, and >= trivially; the other three cases alike. Right.

**REC+.** Lambda is bounded on the compact Omega; a sequence monotone for t <= t_0 (as t -> -infinity) or for
t >= t_0 (as t -> +infinity) and bounded converges at that end; REC (i) or (ii) gives the constant. Right. It
is OM (e) with the hypothesis on one orbit near one end instead of on all of Omega, as the source says.

**EXCL.** (i) is REC (i)'s proof for the coordinate Lambda_D; continuity of a coordinate holds on the whole
product, and the proof reads only returns at times unbounded below, so no property of Omega is used. Right.
(ii) a return at time t to {abs(E''(1,1,1,1) - E(1,1,1,1)) < 1} gives D_E(2^t) < D_E(1) + 1, impossible for
all t below some bound when D_E(2^t) -> +infinity. Right.

**Verdicts: Lemma REC HOLDS; Lemma REC+ HOLDS; Lemma EXCL HOLDS.** First failing step: none. Precision P1 above.
Link (b) of the lead's reading is right as the lead states it, and REC (iii) is a true strengthening.

### Step 6 (done): ALPHA (2.2), KEPT (2.3), A1 (3.1), A2 (3.2), TWO, A3, CR-1 (3.3), MON+ (3.4), 3.6

**Lemma ALPHA. HOLDS.** (i) Omega is compact metrisable and sigma-invariant (OM (a), with CO D1 / CA item 11):
sigma^(-n) E has a convergent subsequence with limit in Omega; alpha(E) = intersection over T of the closures of
{sigma^t E : t <= -T} (sequential limits = this set in a metrisable space), so closed; sigma^(t_n +- 1) E ->
sigma^(+-1) E' by continuity of sigma and its inverse, so sigma(alpha(E)) = alpha(E). (ii) Lambda continuous on
compact Omega is bounded; limit points of Lambda(sigma^t E) at -infinity are the values on alpha(E) (one
direction by a convergent subsequence, the other along the defining sequence); a bounded sequence converges iff
it has one limit point. (iii) alpha(E) is in Omega, which is the set of limits of admissible sequences (closed
by OM (a)). The reading "in units" is right: D_E'(1) = lim D_(j'_i)(2^(k'_i) u_(j'_i)) with k'_i -> infinity, so
every value of an element of Omega, alpha-limit points included, is a limit at physical sizes tending to
infinity. This is CO D14's sentence made exact.

**Corollary KEPT. HOLDS.** (1) is ALPHA (ii) applied to each E. (2): Omega not empty gives E and E' in alpha(E);
sigma^s E' is in alpha(E) by ALPHA (i), where Lambda = c. (3): every element of Omega is a critical element (CE
(ii)(d) along a subsequence on which the levels converge; CO D8, Lemma LV), so d_min <= c <= D_0. (4): if Omega
is empty the statement is vacuous; if not, (3) bounds c; the divergent form fails because D_E <= D_0 everywhere on
Omega. The source's own test point ("sigma^s E' lies in alpha(E) for every s") is right.

**Proposition A1. HOLDS.** (1) = KEPT (1) for Lambda_D. (2) = KEPT (2), (3), and the coordinate formula
D_E'(2^m) = lim D_(j_i)(2^(k_i + m) u_(j_i)). (3) = KEPT (4) plus Theorem CR (1) iff (3), which needs Omega built
at a (BDD-Delta) bound (CO D2); 3.1 fixes exactly that ("a bound (L_0, D_0) of (BDD-Delta), and Omega =
Omega(D_0)"). **W1 (i): yes**, A1 (3) is right with (BDD-Delta) as the only hypothesis beyond Theorem CR (and
CR's own inputs: Theorem ZD-c and its setting). Precision P2 (no statement breaks): for a finite c the case "c
outside [d_min, D_0]" depends on the chosen bound D_0, because Omega(D_0) grows with D_0 and a larger bound
D_0' >= c puts the same c inside the range, where (UV-KEPT; c) over Omega(D_0') is a plateau statement, not (W).
The divergent law has no such dependence, and it is the SU(2) case (Lemma FV). The equivalence is therefore a
statement about the pair (c, D_0), and 8.6's "link (a) with the free value of SU(2) is equivalent to (W)" is the
D_0-free case. Right as written.

**Proposition A2. HOLDS.** For E the limit of (j_i, k_i), b = 2^m: for large i, j_i >= j_eps, L = 2^(k_i + m) l_1
is in P and at least L_eps, and (H2) at the scale m + R_eps is exactly "no seed at 2^(R_eps) L" in the form of
(PLATEAU). So abs(D_(j_i)(2^(k_i + m) u_(j_i)) - c) <= eps for large i, and abs(D_E(2^m) - c) <= eps. (ii) is A1
(2). Right.

**Proposition TWO. HOLDS (given (S0-Z), (TH-Z)).** (i) A2 of R (Delta(n)/abs(n) does not increase when a side
is multiplied by an integer) gives Delta_j(u_j x) <= (abs(x)/mu^4) D_j(u_j mu) <= (abs(x)/mu^4)(D^+(mu l_1) + 1)
for large j; (S0-Z) makes u_j mu an integer at least 3 for mu < 1. Steps 1-4 of CE's proof need such bounds at
(T, B) and at (T/2, B), all dyadic: available. (ii) trivial. (iii) Lemma UF's subsequence; a seed at 2^i l_1
(i < 0) would give one at l_1 by Theorem S (the time 2^i u_j/2 = 2(2^i u_j/4) >= 6 is an integer, so D7 holds);
closed inequality passes to the limit. (iv) the three conditions on j_n each concern finitely many quantities
and hold for all large j in J'; then (j_n, t_n) is admissible with i(m) = max(1, abs(m)) (the source's test
point: right) and its limit at x_p is lim (sigma^(t_n) E_c)(x_p) = E'(x_p). Forward invariance and closedness as
in ALPHA. Right.

**Lemma EXCL.** HOLDS (Step 5).

**Corollary A3. HOLDS AFTER CORRECTION (precision P3).** "If the Casimir free energy of the trajectory is not the
same at all sizes, E_c is not recurrent" needs the hypothesis that D_(E_c)(2^m) has a limit in [0, +infinity] as
m -> -infinity: EXCL (i) needs a finite limit, EXCL (ii) a divergent one; if D_(E_c) oscillates at small scales
without a limit, neither part applies, and nothing proved here excludes backward recurrence. Link (a) posits an
ultraviolet value, so in the setting of the row the hypothesis is present. Repair: add "if D_(E_c)(2^m) has a
limit in [0, +infinity] as m -> -infinity (an ultraviolet law exists)". The conclusion of the row ("CE cannot be
strengthened to keep (a)") is unchanged; 8.8 already limits its scope to extraction by sequences (j_i, k_i).

**Corollary CR-1. HOLDS.** (=>) Lemma UF's subsequence, then the extraction on G_0 with the bound
(abs(x)/mu^4)(D_0 + 1) for mu in G_0 (here D^+ <= D_0 replaces (TH-Z)), then TWO (iii), (iv) on G_0; for each x,
2^t x is in G_0^4 for large t, so omega(E_c) is defined on DD^4. (<=) Theorem S from a seed with margin q' < 1
gives S_j <= q'/5041 at every 2^k l for large j, so s <= q'/5041 for every continuum datum at such sizes. The
last sentence ("in that case ... contains a uniformly recurrent element") holds for the E_c built in (=>); it
also holds for any continuum datum with s >= 1/5041 at every b, because by Theorem S a seed of lattice j at b
forces S_j(2b) <= ((1 + 1/5041)^64 - 1)^2 < 1.64 x 10^(-4) < 1/5041, so s_(E_c)(2b) >= 1/5041 forces no seed at
b for all large j of its subsequence, which is what (H2) needs. OM (d)'s proof applies to any non-empty compact
invariant set. Right.

**Proposition MON+. HOLDS.** Each coordinate of sigma^t E_c is bounded for t >= t_0 (TWO (iv) for large t,
finitely many finite values before), so the closure of the forward orbit is compact and Lambda is bounded; a
non-increasing bounded sequence converges; for E' in omega(E_c), sigma^s E' = lim sigma^(t_n + s) E_c lies in
the closure, and continuity gives Lambda(sigma^s E') = Lambda_IR. Right. The sentences after it ("a constant D
comes from monotony", "the ultraviolet data enter ... in no other way") are readings: MON+ shows that monotony
suffices, not that it is necessary. They carry no step.

**Section 3.6. HOLDS as readings.** The product: Step 4. D2 and SHEET: `parts/gap.md` L29 (at this pin) states
them as rules against a hypothesis "with a supremum over tilts" and one "uniform over plaquette coupling
fields"; (UV-KEPT) and (PLATEAU) contain neither, so they are not bound. Right. 3.1's paragraph on the account's
normalisation: the index rows it cites (`library/sa-index/chunk-06.md` rows 6854-6895) give a free two-point
kernel and a short-distance error scope for correlations, so "the account's normalisation is not a statement
about D" agrees with the index (the account's TeX was not opened by the source or by this check).

### Step 7 (done): the GUIDE-grade correction (5.2, L803-813; remark 5 of 4.1, L653-669), the controls, W1

**Remark 5 (the Gaussian count), re-derived. ARGUED as marked; the count is right.** Lattice Gaussian U(1) with
compact constant modes on n^d: gauge orbit (2 pi)^(N-1) N^(-1/2) (det' Lap)^(1/2) (the map chi -> d chi has
kernel the constants, of length 2 pi sqrt(N)); coexact directions, (d - 1) N - d + 1 of them, with the
(d - 1)-fold non-zero spectrum of Lap: (2 pi/beta)^(((d-1)N - d + 1)/2) (det' Lap)^(-(d-1)/2); holonomy modes:
c_mu in [0, 2 pi/n) with norm sqrt(N) abs(c_mu), so (2 pi n^(d/2 - 1))^d. With log det' Lap = cN + 2 log n + O(1)
(a published asymptotic for discrete tori: Duplantier and David for d = 2; Chinta, Jorgenson and Karlsson for
general d; recalled, not re-read here), the non-extensive powers of n are -d/2 + 1 - (d - 1) + d(d/2 - 1) =
(d - 1)(d - 4)/2 and the power of beta left after subtracting f N is (d - 1)/2. So D = ((d - 1)/2)
log(beta n^(d-4)) + O(1) for the Gaussian model, with the O(1) uniform in n because the determinant asymptotic
has a convergent constant. The scalar case (1/2) log(beta n^(d-2)) is right by the same count. Monopole and vortex
terms of the Villain model are not treated; for them the statement is GUIDE, as the source marks it.

**The correction itself. Verdict: HOLDS AFTER CORRECTION, at GUIDE grade, with two citation repairs.**
- U(1) with beta_j -> infinity (R L294). In four dimensions the count gives D_j(L/a_j) = (3/2) log beta_j + O(1)
  at every physical size, so D^+(L) = +infinity, (BDD-Delta) fails, Omega(D_0) is empty for every D_0 ((H1)
  fails), and the family is in branch (II) of Corollary TRI. R L294 rests its "if D is bounded" on
  `gap-phys-seed.md` L336, a belief stated at one coupling; the transfer to beta_j -> infinity was R's. Fair.
- Five dimensions at weak coupling. The count gives D about 2 log(beta n) at one coupling (GUIDE for SU(2):
  the abelian moduli count with (d - 1) rho = 4, and the infrared coupling 4/(beta n) falls with n), so D is
  unbounded in n and the constant family is in branch (II). Fair.
- **Citation repair P4.** Row 720's sentence (`gap-phys-seed.md` L336) has two parts. "U(1) at weak coupling:
  (BDD-Delta) holds (GUIDE: scale invariance)" is at one coupling, and the count supports it (d = 4: D does
  not depend on n). Only its five-dimensional part ("SU(2) in five dimensions at weak coupling: (Z-UNB) fails";
  then "in every comparison model ... (BDD-Delta) holds") is corrected. The source's 5.2 says "the same
  correction applies to row 720" and lists both models; the U(1) half applies to R L294 only. The source's own
  W2 (5) wording ("at one coupling, in four dimensions") is the right repair.
- **Citation repair P5.** R's five-dimensional row (L300: "not empty | BELIEF (A17)") is not a conditional "if
  D is bounded": it rests on R L270, "if five-dimensional SU(2) at weak coupling has massless gluons ... it has
  critical elements". The source (5.2, and table 5.4 row 5: "valid as conditionals") misquotes it. The repaired
  statement is stronger: R L270's inference skips (BDD-Delta); massless gluons give no seed, which leaves
  branch (II) or (III) by Corollary TRI, and the count puts the five-dimensional model in (II). So R L270 and
  L300 are wrong at GUIDE grade, not merely conditional.
- Both sides of the correction are GUIDE or ARGUED, as the source says (5.2, 8.3, 8.8). It changes what these
  two controls test ((BDD-Delta), not (LIOU)); it changes no theorem.

**The chain as a tool (5.1). HOLDS.** H_a = (UV-KEPT; c) and a uniformly recurrent E in Omega give, by REC (i),
D_E = c at every scale; so "H_a implies T" is proved. The other controls of 5.2 are marked BELIEF where they rest
on a limit set that is not proved (U(1) at one coupling; frozen Q_8, 2T at large finite beta), PROVED for TS and
the product (Step 4). In the U(1) row, H_a holds with c = c_inf(beta) and not with the lattice value D(3; beta);
the row says so.

**Smaller items in Sections 4.2, 5.3 and 6 (none breaks a statement).**
- P6 (4.2, third bullet): "Omega does not depend on this choice" of unit is right when the new unit is the old
  one times a power of 2 (Omega is sigma-invariant); for another ratio the grid P changes and the sentence is
  not proved. It is used by no verdict.
- 5.3 row R4 ("wrong for finite c": a family is left) inherits the marking defect of Step 3: for a finite c the
  proved member is one constant; "a family" is BELIEF.
- 6.3 outside lens (Conley) and routes U1-U5: readings and recalled facts, marked so; not checked as proofs.

**W1 judgements, collected.** (i) A1 (3): right, with (BDD-Delta) as the only hypothesis beyond Theorem CR;
precision P2 (Step 6). (ii) Lemma FV: holds with its constants, and its f is the lane's f (Step 2). (iii) TS:
a family of data with units in the sense of `gap-dichotomy.md` L85-101; limit set as stated (Step 4). (iv) The
correction of 5.2 is fair as a GUIDE-grade statement, after P4 and P5.

### Step 8 (done): verdicts, ranked defects, scope, RESULT

**Provenance.** Claude Opus 5.5, max effort, Mac mini worker 3, at commit 85d8dfc6d; one line-by-line reading
of `library/gap-uv-rigidity-max.md` (written by Claude Fable 5.2, who pinned d8496276a; read here as
committed at 85d8dfc6d, last relay commit 292ba65d6; the working copy has no diff against the pin). Same provider, different model. Not an audit. No subagents. No numeric job was run.

**Verdict per statement (first failing line: none).**

| Statement (source section) | Verdict | Notes |
|---|---|---|
| Lemma ALPHA (2.2) | HOLDS | Step 6 |
| Corollary KEPT (2.3) | HOLDS | Step 6 |
| Lemma REC (2.4), Lemma REC+ (6.2) | HOLDS | Step 5; P1 (wording) |
| Proposition A1 (3.1) | HOLDS | Step 6; P2 (precision) |
| Proposition A2 (3.2) | HOLDS | Step 6 |
| Proposition TWO (3.3), given (S0-Z), (TH-Z) | HOLDS | Step 6 |
| Lemma EXCL (3.3) | HOLDS | Step 5 |
| Corollary A3 (3.3) | HOLDS AFTER CORRECTION | P3: needs a limit of D_(E_c) at minus infinity |
| Corollary CR-1 (3.3) | HOLDS | Step 6 |
| Proposition MON+ (3.4) | HOLDS | Step 6 |
| Family TS (3.5) | HOLDS | Step 4; family with units, limit set as stated |
| Product argument and blockers (3.6) | HOLDS (product conditional on (BDD-Delta) for X, as stated; D2, SHEET readings right) | Step 4, Step 6 |
| Lemma FV (4.1), with its constants | HOLDS | Step 2; zero-mode count 6 (generic) and 12 (central) confirmed by the linearised complex |
| Proposition FRZ (4.3): log 8, log 92, log 244 | HOLDS | Step 3 |
| Proposition CONST (4.4) | HOLDS | Step 3; tested against every engine statement R names |
| Remark after CONST; table 4.5 row "(c) names a family"; 5.3 row R4 | HOLDS AFTER CORRECTION (marking) | defect 1 below |
| Remark 5 of 4.1 (Gaussian count) | ARGUED, count right | Step 7 |
| GUIDE-grade correction (5.2): U(1) with beta_j -> infinity and five dimensions in branch (II) | HOLDS AFTER CORRECTION, at GUIDE grade | P4, P5 |

**Defects, ranked by what each would break (none breaks a proved statement).**

1. **Marking: "for a finite c, link (c) names a family" is BELIEF, not PROVED** (remark after CONST L742-745;
   table 4.5; 5.3 row R4; the RESULT line's "for a finite value link (c) names a family"). Sums of constants
   are constants; the only proved element with D = c on the diagonal is the constant c = log m. A second element
   needs a non-constant critical element with constant diagonal D; the record has only the photon limit
   (BELIEF). Repair: "for c = log m the proved member is the constant log m; that more elements have D = c
   rests on the photon limit (BELIEF)". No verdict changes: CONST (iii) already shows the axioms cannot exclude
   the constant.
2. **P3, Corollary A3:** add "if D_(E_c)(2^m) has a limit in [0, +infinity] as m -> -infinity". Without a limit,
   EXCL says nothing about backward recurrence of E_c.
3. **P5, the five-dimensional row of R (L300, from L270) is not a conditional "if D is bounded".** R infers
   critical elements from massless gluons alone. The correction is therefore stronger than the source states:
   R L270 and L300 skip (BDD-Delta) and are wrong at GUIDE grade. Table 5.4 row 5 ("valid as conditionals")
   should say so for L300.
4. **P4, row 720's U(1) sentence is at one coupling and stands** (`gap-phys-seed.md` L336; the count agrees
   with it in four dimensions). Only its five-dimensional part and the closing "in every comparison model
   (BDD-Delta) holds" are corrected; the U(1) half of the correction applies to R L294. The source's W2 (5)
   wording ("at one coupling, in four dimensions") is right.
5. **P2, Proposition A1 (3) for a finite c depends on the chosen bound D_0** (Omega(D_0) grows with D_0). The
   divergent law, which is the SU(2) case, has no such dependence.
6. **P1, definition of uniformly recurrent:** say "syndetic in Z" (the form OM (d) gives, CA L262-271). A one-
   sided reading would need Birkhoff's theorem, which no file proves.
7. **P6, 4.2:** "Omega does not depend on this choice" of unit holds for a change of unit by a power of 2 only.

**Checker's remark (ARGUED, a sketch, used for no verdict; Step 4).** A TS-type family with a divergent
ultraviolet law and Omega = {log m_0} exists: A_(m_0, eps_j/u_j^4) times the product over i = 0..j of
A_(2, 16^i/u_j^4). It removes the condition "(BDD-Delta) for X" from the product argument of 3.6.

**What this check did not cover.** The account's TeX (the source did not open it either; the index rows were
read). Remarks 2 and 3 of 4.1 as proofs (GUIDE and ARGUED). The monopole and vortex terms of the Villain model.
The determinant asymptotic of Remark 5 was recalled, not re-read. The routes of 6.3 and the outside lens are
readings and recalled facts. The source's guard run (4.6) was not repeated: every claim it touched (the counts
c_k, the shelling at n = 3, 4, 5, the inequalities G3-G5) was re-derived by hand here, for all n and all r in
range. Inputs taken as checked by CO and CA (Theorem S, Lemma UF, Theorem CE, Proposition OM, Theorem CR,
Lemma PT, Lemma PT-inf, Lemma LV) were read at their statements and the steps this file reuses, not re-checked.
`origin/main` and the open PR branches were not searched.

**What moved.** Nothing on the critical path: (LIOU), (BDD-Delta) and (W) stay OPEN. The check makes row 1028's
pricing of the route "kept ultraviolet condition" usable: link (a) is target-equivalent for SU(2), link (b)
holds, and the axioms cannot exclude a constant log m. Lemma FV is a checked lower half of the count kappa = 3
on a fixed lattice (same provider). For the lead's W2 of the source: items (1), (3), (4) can go in as written;
item (2) should carry P5; item (5) should carry P4.

**Run record.** Started 2026-11-16T01:03Z; this section written at about 01:20Z-01:25Z by `date -u` (the step
headings carry no times; times first written there were estimates and were removed). Files written: this one
only. No numeric job, no memory-pressure check needed, no scratch files, no commit, no push.

RESULT: Row 1030 (Claude Opus 5.5 max, check of row 1028 by Claude Fable 5.2; same provider; first failing line none). HOLDS: Lemma FV (D(n; beta) >= (3/2) log beta - 59 n^4 - 11 for SU(2), beta >= 16, every step and constant re-derived; zero-mode count 6 at generic and 12 at central flat points confirmed by the linearised complex on the 3^4 torus; its f is the lane's f), Proposition CONST (tested against every engine statement row 1017 names, the centre data and the spectral clause: they exclude a constant c exactly when e^c is not an integer >= 2), Proposition FRZ (92 and 244 re-counted), Lemmas REC, REC+, ALPHA, EXCL, Corollaries KEPT and CR-1, Propositions A1, A2, TWO, MON+, the family TS (a family with units; Omega = {log m_0}; ultraviolet value log(m_0 p)). HOLDS AFTER CORRECTION: Corollary A3 (needs a limit of D_(E_c) at minus infinity); the marking "for a finite c link (c) names a family" (only the constant is proved; more members are BELIEF); the GUIDE-grade correction (U(1) with beta_j -> infinity and five dimensions in branch (II): the count is right, but row 720's one-coupling U(1) sentence stands, and row 1017's five-dimensional row L300 is an unconditional inference from massless gluons, so the correction is stronger there). Precisions P1 (syndetic), P2 (A1 (3) depends on D_0 for finite c), P6 (unit change). OPEN, not moved: (LIOU), (BDD-Delta), (W).
