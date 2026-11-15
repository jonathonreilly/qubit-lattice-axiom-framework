lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T10:14Z

# Check of row 1021 (`gap-registry-after-checks-max`), work item W1

Row 1023, queued 2026-11-15 22:13Z. Checker: Claude Opus 5.5 max, Mac mini worker 2.
Source under check: `library/gap-registry-after-checks-max.md` at commit f6c0017dc
(written by Claude Fable 5.2 max; same provider as this checker, so this is not an
independent cross-provider check). Started 2026-11-15 22:14Z (from `date -u`).

No subagents. No commit, no push. Numeric runs only to refute or guide, under the
numeric lock, and none is planned.

## Plan (at most eight steps; revised after reading W1)

1. Read W1 (source 7.7, L797-808) and the FINISH rules. Done; W1 copied below.
2. Read source Section 6 (L508-735) in full; run tests (a)-(e) first, as W1 orders.
3. Lemma EL and Corollary NS, redone by hand (most care; test (c)).
4. Lemma KL (i)-(iii) and (K1)-(K3), redone by hand (most care; tests (a), (b), (e)).
5. Lemma S1 and Proposition FR, redone by hand (test (d)).
6. Section 6.5: Lemma LIFT and Lemma NB.
7. W1 (i): Section 4 rows A1, A2, B5, B6, B7, B8, B10, B13, C1, C8 against the cited
   check files at the cited lines. W1 (iv): 6.4 items 1-4, the verdict on T3, and the
   ARGUED reading on (ABS-flow) in 5.2.
8. Verdict table and RESULT line.

Stop rule (W1): stop at the first WRONG in Lemma KL or Lemma EL and report it; no new attack.

## W1 as written (source L797-808, copied verbatim)

> W1, check (a model that did not write this file; another provider if possible; high effort). Read
> `library/gap-registry-after-checks-max.md` at the commit that holds it. (i) Section 4: for the rows A1, A2,
> B5, B6, B7, B8, B10, B13, C1, C8 open the cited check file at the cited lines and say whether the status
> word is the check's own verdict. (ii) Section 6.3: redo by hand Lemma S1, Proposition FR, Lemma EL, Lemma
> KL (i)-(iii) and (K1)-(K3). (iii) Section 6.5: Lemma LIFT, Lemma NB. Test first: (a) sigma^2 = 1/(2 beta sinh
> omega) against `gap-fc-max.md` L193-197 and L510; (b) in KL (ii), (1 - e^(-omega))/sinh omega = 2/(e^omega + 1);
> (c) in Lemma EL, that the law of the whole path is invariant under time-independent gauge transformations,
> and that side 3 is enough; (d) whether (E1) is used for gauge-invariant f only; (e) whether (K3) is a fair
> reading of (P1) (CA-II 80163-80172 as quoted in `gap-hcphys-max.md` L46). (iv) Judge 6.4 items 1-4 and the
> verdict on T3; judge the ARGUED reading on (ABS-flow) in 5.2. Verdict per statement: ADVANCE,
> CORRECT-NO-ADVANCE or WRONG with the failing line. Stop rule: stop at the first WRONG in Lemma KL or Lemma
> EL and report it; no new attack. Output `library/gap-registry-after-checks-check-<model>.md`.

Report format (FINISH, Rules): one provenance line, then a verdict per statement (ADVANCE,
CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure.

## Progress

- Step 1 done (2026-11-15, after 22:14Z). Next: Step 2, read source Section 6 and run tests (a)-(e).

## Step 2. Tests (a)-(e), run first (W1 order)

Read for this step: source L508-735 (Section 6) in full; `gap-fc-max.md` L39-55, L121-227
(Theorem BR, 5.4, 5.5), L487-512; `gap-hcphys-max.md` L30-116; `gap-hcphys-check-astra.md` L30-80.

**(a) sigma^2 = 1/(2 beta sinh omega) against `gap-fc-max.md` L193-197 and L510. PASSES.**
- L510: J has precision [[beta + c, -beta], [-beta, beta + c]]. Redone: with m(dx) = e^(-c x^2/2) dx,
  J(dx, dw) is proportional to m(dx) e^(-beta (x - w)^2/2) m(dw); the exponent is
  -(1/2)[(beta + c) x^2 - 2 beta x w + (beta + c) w^2]. Same matrix.
- Marginal precision of x: (beta + c) - beta^2/(beta + c). With beta + c = beta e^omega (L193-194, and
  omega = log(1 + c/beta) in KL) this is beta (e^omega - e^(-omega)) = 2 beta sinh omega.
- Independent route through L194-197: nu = lim nu_s as s -> 0 has precision c + c/(1 + c/beta)
  = c (2 beta + c)/(beta + c) = beta (e^omega - 1)(e^omega + 1)/e^omega = 2 beta sinh omega. Same value.
- Third route (stationarity): X_1 = e^(-omega) X_0 + noise of variance 1/(beta e^omega) gives
  sigma^2 (1 - e^(-2 omega)) = e^(-omega)/beta, so sigma^2 = 1/(2 beta sinh omega). Same value.

**(b) (1 - e^(-omega))/sinh omega = 2/(e^omega + 1). PASSES.** sinh omega = e^(-omega)(e^omega - 1)(e^omega + 1)/2
and 1 - e^(-omega) = e^(-omega)(e^omega - 1); the quotient is 2/(e^omega + 1), at most 1 for omega >= 0.

**(c) Lemma EL: path law invariant under time-independent gauge maps; side 3 is enough. PASSES.**
- T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2): V is a sum of plaquette traces (gauge invariant);
  <x, w> = sum_l Re(x_l conj(w_l)) is invariant when the same g acts on x and w (the action on each R^4
  factor is q -> g q h^(-1), an element of SO(4)); the product Haar measure is invariant. So T_0 commutes
  with U_g f(x) = f(g^(-1) x). T_0 has a strictly positive continuous kernel on a compact space, so its top
  eigenvalue is simple (Jentzsch); U_g Omega is a positive normalised top eigenfunction, so U_g Omega = Omega.
  Then nu, m and pi_x are invariant/covariant (pi_(gx)(g dw) = pi_x(dw)), and the law
  nu(dx_0) pi_(x_0)(dx_1) ... pi_(x_(n-1))(dx_n) is invariant under (x_t) -> (g x_t) with g fixed in t.
- Side 3: on a periodic cubic box of side n, links (x, x + e_i) and (y, y + e_j) with the same set of
  end sites and l != l' need e_i + e_j = 0 mod n; for i = j this is n | 2, for i != j it is n = 1.
  So n >= 3 is enough, and n = 2 really fails (two links join x and x + e_i). If the end-site sets differ,
  one end site of l is not an end site of l' (two 2-sets, both inside the other, are equal). For l = l'
  the two ends differ (n >= 2), so g and h are independent and the commutant argument applies.
- One unstated step (not a defect of the result): tau_k is written with a link index; the formula
  <f_z, P^k f_z> = tau_k |z|^2/4 needs tau_k the same for every link. This holds: the lattice symmetries
  (translations, axis permutations) commute with T_0, so Omega and the path law are invariant under them,
  and on a cubic periodic box they act transitively on links. "Cubic" is used here.

**(d) Is (E1) used for gauge-invariant f only? YES (PASSES), with one wording mismatch.**
Every use: FR (L562-565, gauge-invariant f), 6.4 item 3 (L645-647, gauge-invariant f), 6.5 (L677,
f = <e, V> with V gauge invariant). Lemma EL, Corollary NS and Lemma KL do not use (E1).
Wording: L550 states (E1) "for every continuous f", while the lane states it for gauge-invariant f
(`gap-hcphys-max.md` L64) and L563 says so. The wider form is also true: Theorem BR step (ii) at q = 2
(`gap-fc-max.md` L160-169) and the end limits (`gap-hcphys-check-astra.md` L40-54, "Signed continuous
functions cause no problem") use no invariance. So the mismatch breaks nothing.

**(e) Is (K3) a fair reading of (P1)?** Provisional answer, to be finished after reading the account's
text (next part of this step): (K3) is a mode-model translation of (P1), not a consequence of it.
(P1) bounds the fluctuation form Q against the IDENTITY on the level-k fluctuation variables (free bonds,
rescaled by g_k), not against a Laplacian symbol at a fine frequency. (K3) replaces "identity in level-K
rescaled units" by "beta_K times the four-dimensional Laplacian symbol at a frequency of order L^(-K)".
Two features of (K3) do follow from (P1)'s form: the bound is two-sided, and it is isotropic (the identity
does not distinguish time-like from space-like bonds). The source marks every use as "given the reading of
(P1) in (K3)" (L628, L657-658, L760) and lists this reading first among its likely errors (L847).

**(e), finished. (K3) is a fair reading of the shape of (P1); it is not derived from (P1). PASSES as
labelled ("given the reading"), with one precision on what is read.**
- The quote at `gap-hcphys-max.md` L46 is faithful. I fetched CA-II at 31a47c543775 into my own scratch
  folder and read 80025-80048 and 80150-80180: Definition 8.3:def-box-precision states, "at each real
  background configuration of the step", a_- <= Q <= a_+ as forms and ||Q(b, b')|| <= a_+ e^(-c_A dist(b, b')),
  constants free of the level, K, m, the background and the volume; order relations refer to the Euclidean
  inner product of g^(B+). The variables are A(b) on the free bonds Lambda^(k)*_(k+1) (all level-k bonds of
  Lambda_(k+1) minus one bond b-hat(c) per block c), "in the rescaled normalisation in which the unscaled
  fluctuation field is g_k A" (80039-80041). Credit: Sussman and Alpoge, with Claude and Codex as authors
  of their text; Balaban for the operator theorem.
- What (K3) keeps from (P1): a two-sided bound; isotropy (the Euclidean identity on g^(B+) treats time-like
  and space-like bonds alike); the level-K coupling beta_K = g_K^(-2) as the unit of the bound.
- What (K3) adds: the identity on level-K free bonds is replaced by beta_K times the Laplacian symbol
  (2 - 2 cos p + q^2) at one fine frequency of order L^(-K), with the factor 2 a_+. (P1) is a bound on the
  form restricted to the free-bond subspace of one step, not a bound on the full precision at one Fourier
  mode, and the constant depends on the block map. This passage is not derived (row 1021 does not claim it).
- Why the conclusion of 6.4 item 1 is still the expected one (ARGUED here; not a new attack): for a Gaussian
  chain with the bare kernel the time-like coefficient is beta_0 at every frequency (K1). The level-K
  fluctuation form of such a chain, on free-bond fluctuations that vary in time inside a block, is then of
  order beta_0 in the unscaled metric, and (P1) at level K needs it below a_+ beta_K times a constant of the
  block map. So the qualitative clause "a Gaussian chain in the class of Theorem BR cannot satisfy (P1) at
  level K once beta_0/beta_K is large" survives the literal form of (P1); the threshold 2 a_+ does not
  transfer without a computation of the block map.
- So the source's label "given the reading of (P1) in (K3)" (L628, L657-658, L760) is the right label.

**Tests: all five pass; (e) passes only as a reading, as the source already says.** Next: Step 3.

## Step 3. Lemma EL and Corollary NS (most care)

**Lemma EL (source L573-586). Redone by hand. CORRECT. Verdict: ADVANCE** (it extends the lag-0 and lag-1
Elitzur statements of rows 941, 947, 968 to every lag, and it is the tool that Corollary NS and 6.4 item 2
use).
- Gauge invariance of the path law: test (c) above.
- l != l': with a the end site of l that is not an end site of l', the map g = -1 at a (1 elsewhere) is a
  time-independent gauge map; it sends X_(t,l) to -X_(t,l) for every t and fixes X_(t,l') (n >= 2, so no
  link has both ends at a). Invariance of the path law gives E[X_(0,l) (x) X_(k,l')] = -E[...] = 0. The same
  map gives E X_(0,l) = 0.
- l = l': the ends a != b carry independent g, h in SU(2); the map q -> g q h^(-1) runs over all of SO(4)
  (SU(2) x SU(2)/{+-1} = SO(4)). So M_k := E[X_(0,l) (x) X_(k,l)] satisfies R M_k R^T = M_k for every R in
  SO(4). SO(4) acts absolutely irreducibly on R^4 (its complexification is the irreducible (1/2, 1/2)
  representation), so M_k = (tr M_k/4) Id_4 = (tau_k/4) Id_4.
- tau_0 = E|X_(0,l)|^2 = 1 (unit quaternions). tau_(2j) = 4 <f_z, P^(2j) f_z>/|z|^2 = 4 ||P^j f_z||^2/|z|^2 >= 0
  (P self-adjoint on L^2(nu)).
- Consequences: <f_z, P^k f_z> = E[f_z(X_0) f_z(X_k)] = sum_l z_l^T (tau_k/4) z_l = tau_k |z|^2/4 (this line uses
  tau_k independent of l: true on a cubic periodic box, see test (c)); Var_nu(f_z) = |z|^2/4 since E f_z = 0;
  ||f_z||^2 - ||P^T f_z||^2 = (1 - tau_(2T)) |z|^2/4. All three hold.
- Scope: side >= 3 is needed (side 2 fails, test (c)). The lemma is about the temporal-gauge chain of
  Theorem BR (M = (S^3)^L, kernel e^(beta <x, w>)); it says nothing about gauge-invariant functions.

**Corollary NS (source L588-592). CORRECT. Verdict: CORRECT-NO-ADVANCE** (an immediate reading of EL).
- Slice covariance E[X_0 X_0^T] = (1/4) Id_N and normalised autocorrelation tau_k for every z != 0: from EL.
- "A covariance ... with norm of order L^K/beta_K is not the covariance of the slice law in these
  coordinates": true, since the slice covariance has norm 1/4 and L^K/beta_K grows without bound as a -> 0
  with beta_K of order one.
- The parenthesis on nu_s: by `gap-fc-max.md` (B3) and EL at lag 1, Cov(nu_s) = v_s Id_N with
  v_s = (1 - 2 lam (1 - lam)(1 - tau_1))/4 + lam (1 - lam)/beta, recomputed: (1 - lam)^2/4 + lam^2/4
  + 2 lam (1 - lam) tau_1/4 + lam (1 - lam)/beta. Same. (The phrase "the same holds" fits the covariance;
  an autocorrelation along s is not defined there. Wording only.)
- Limit of the corollary, not a defect: it is about linear statistics in ambient coordinates. These are
  not gauge invariant (Lemma INV, `gap-fc-max.md` L261-266). Linear statistics in a gauge-fixed chart are
  other functions of the slice; NS says nothing about them.

No WRONG in Lemma EL. Stop rule not triggered. Next: Step 4, Lemma KL.

## Step 4. Lemma KL (i)-(iii) and (K1)-(K3) (most care)

Setting (source L594-597): one real mode, transition pi_x(dw) proportional to e^(-beta (x - w)^2/2) e^(-c w^2/2) dw,
c > 0, omega = log(1 + c/beta), so beta + c = beta e^omega.

**Chain law. CORRECT.** pi_x is Gaussian with precision beta + c and mean beta x/(beta + c) = e^(-omega) x.
So X_(t+1) = e^(-omega) X_t + (noise of variance e^(-omega)/beta). Stationary variance: test (a), three routes,
sigma^2 = 1/(2 beta sinh omega). Covariance E[X_0 X_k] = sigma^2 e^(-omega |k|) (AR(1)).

**(i) CORRECT.** Sum over k in Z of r^|k| e^(i k p), r = e^(-omega), is the Poisson kernel
(1 - r^2)/(1 - 2 r cos p + r^2); dividing top and bottom by r gives sinh omega/(cosh omega - cos p).
Times sigma^2: S(p) = 1/(2 beta (cosh omega - cos p)) = 1/(beta (2 - 2 cos p) + 2 beta (cosh omega - 1)).
Convention: S(p) = sum_k C(k) e^(i k p), so Var(sum c_t X_t) = integral of |c-hat|^2 S dp/(2 pi), as (iii) uses.

**(ii) CORRECT.** E|X_T - X_0|^2 = 2 sigma^2 (1 - e^(-omega T)) = (1 - e^(-omega T))/(beta sinh omega);
1 - r^T = (1 - r)(1 + ... + r^(T-1)) <= T (1 - r); then test (b): (1 - e^(-omega))/sinh omega = 2/(e^omega + 1) <= 1.
So E|X_T - X_0|^2 <= 2T/(beta (e^omega + 1)) <= T/beta.

**(iii) CORRECT.** S(p) <= 1/(beta (2 - 2 cos p)) for p != 0, and c-hat is a trigonometric polynomial with
c-hat(0) = 0, so |c-hat(p)|^2 = O(p^2) and the bound is integrable. The free-walk value is checked independently:
for a walk W with independent steps of variance 1/beta and sum c_t = 0, sum c_t W_t = sum_s xi_s d_s with
d_s = sum over t > s of c_t (finitely supported); d-hat (1 - e^(ip)) = -c-hat, so by Parseval
Var = (1/beta) integral of |c-hat|^2/(2 - 2 cos p) dp/(2 pi). Same as the source.

**(K1) CORRECT.** The inverse-covariance symbol of AR(1) with coefficient r and noise variance v is
(1 - 2 r cos p + r^2)/v; with r = e^(-omega), v = e^(-omega)/beta it is beta (2 cosh omega - 2 cos p)
= beta (2 - 2 cos p) + mu^2, mu^2 = 2 beta (cosh omega - 1). The split into a difference term and a
p-independent term is unique, so "the coefficient of the time-like difference term is beta" is exact.
For a product of modes each mode has its own c and the same beta.

**(K2) CORRECT.** 2 beta sigma^2 sinh omega = 1 is the formula for sigma^2. If sigma^2 >= S then
sinh omega <= 1/(2 beta S), and omega <= sinh omega for omega >= 0.

**(K3) CORRECT as an implication (including its edge case).** Upper half: beta (2 - 2 cos p) <=
beta (2 - 2 cos p) + mu^2 <= a_+ beta_K (2 - 2 cos p + q^2) <= 2 a_+ beta_K (2 - 2 cos p) when q^2 <= 2 - 2 cos p.
Dividing needs 2 - 2 cos p > 0. At p = 0 the side condition forces q = 0, and then the upper bound reads
mu^2 <= 0, false since c > 0 gives omega > 0 and mu^2 > 0. So any frequency where the hypothesis holds has
p != 0, and beta <= 2 a_+ beta_K follows. (Only the upper form bound is used.)

**Verdict: Lemma KL with (K1)-(K3): CORRECT; ADVANCE** (a new exact tool for the lane; it is what removes the
Gaussian benchmark of T3). (i), (ii), (K1), (K2) are the standard AR(1) facts and agree with row 947 5.4
(alpha = omega there). The use of (K3) against (P1) is a reading: test (e).
No WRONG in Lemma KL. Stop rule not triggered.

## Step 5. Lemma S1 and Proposition FR

**Lemma S1 (L557-560). CORRECT; CORRECT-NO-ADVANCE.** Spectral theorem; with mu = lambda^2 in [0, 1]:
mu^T <= mu gives the left inequality, and 1 - mu^T = (1 - mu) times a sum of T terms in [0, 1] whose first is 1
gives the right one.

**Proposition FR (L562-571). CORRECT given (E1); CORRECT-NO-ADVANCE.**
- ||f||^2 - ||P^T f||^2 = <f, (1 - P^(2T)) f> (P self-adjoint). S1 and (E1) give
  EE(f) <= ||f||^2 - ||P^T f||^2 <= T EE(f).
- Stationarity: E|f(X_(2T)) - f(X_0)|^2 = 2 ||f||^2 - 2 <f, P^(2T) f> = 2 (||f||^2 - ||P^T f||^2). So the second
  form holds.
- Reading L569-571 checked: at T = 1, E|f(X_2) - f(X_0)|^2 = 2 EE(f) = (2/beta) times the mean over s in
  (0, 1/beta) of E_(nu_s)|grad u_s|^2. "Blind": the proof uses no property of V.
- Test (d): (E1) is used here for gauge-invariant f only (L562-563), and it holds for all continuous f.
- Why no advance: at T = 1 FR is (E1); for T > 1 it adds S1. It is used in 6.4 item 3 (T = 1, "the gap
  restated", as the source says) and in 6.5 (an averaged bound under an underived hypothesis). No status moves.

## Step 6. Section 6.5: Lemma LIFT and Lemma NB

**Lemma LIFT (L665-669). CORRECT; CORRECT-NO-ADVANCE.** Ent_mu(phi(V)^2) = Ent_rho(phi^2) (push-forward).
grad f = DV^T grad phi(V), so |grad f|^2 = <grad phi(V), G grad phi(V)> >= r |grad phi(V)|^2 mu-a.e. Then
Ent_rho(phi^2) <= (2/varrho) E_mu |grad phi(V)|^2 <= (2/(varrho r)) E_mu |grad f|^2. Scope, as the source says:
it gives the inequality only for functions of V, not for every gauge-invariant function that (LSI-br) reads.
- Arithmetic after LIFT (L671-674): varrho r = varrho_0 beta_K r_0 (beta_0/beta_K) L^(-K) = varrho_0 r_0 beta_0 a/l_unit,
  since L^(-K) = a/l_unit. CORRECT.
- Averaged statement (L676-681): FR with T = L^K gives EE(<e, V>) >= L^(-K) (||<e, V>||^2 - ||P^T <e, V>||^2);
  if (1/2) E|increment over 2 L^K steps|^2 >= c/(2 beta_K), the mean over s in (0, 1/beta_0) of the energy is
  beta_0 EE >= (c/2)(beta_0/beta_K) L^(-K). CORRECT, given (E1) and the stated hypothesis, as marked.
  (<e, V> is continuous and gauge invariant when V is, so (d) holds here too.)

**Lemma NB (L683-693). CORRECT for the ambient gradient; CORRECT-NO-ADVANCE.**
d n-hat = (Id - n-hat n-hat^T) d Phi/|Phi|; for e orthogonal to n-hat, <e, d n-hat> = <e, d Phi>/|Phi|
= (1/(n |Phi|)) sum <e, d S_i>. So grad_(S_i) <e, n-hat> = e/(n |Phi|), and the sum of squared norms is
1/(n |Phi|^2); for <e, Phi> it is 1/n. One precision, not a defect: these are gradients in the ambient
(R^d)^n. If the S_i are held on the unit sphere (tangential gradient, as on M), each squared norm gets the
factor 1 - <e, S_i>^2, the same for n-hat and for Phi, so the ratio 1/|Phi|^2 and the Reading do not change.
The Reading (variance and squared gradient scale by the same 1/|Phi|^2) is first order in the fluctuation of
|Phi|; it is a reading, and the source does not mark it PROVED. The clause on CA-I Def 1.5 is flagged by the
source as not re-read; I did not read it either.

(S-a) example checked: V(y) = y^3 gives G = 9 y^4, zero at 0, positive mean under any law not carried by 0.

Next: Step 7, W1 (i) (Section 4 rows against the check files) and W1 (iv) (6.4 items 1-4, T3, 5.2).
