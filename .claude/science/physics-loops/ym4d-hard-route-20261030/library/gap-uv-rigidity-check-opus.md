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

### Step 1 (done 2026-11-16 ~01:15Z): sources read, scope, duplicate check

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

### Step 2 (done ~01:35Z): Lemma FV (source 4.1, L539-669). Verdict: HOLDS

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

### Step 3 (done ~01:55Z): Proposition CONST (4.4, L725-745) and Proposition FRZ (4.3, L686-723)

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

### Step 4 (done ~02:10Z): the family TS (3.5, L460-498) and the product of 3.6 (L502-513)

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
