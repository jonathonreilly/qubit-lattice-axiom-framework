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

- Steps 1-8 done (last write 2026-11-15T22:28Z). The report is in Step 8 and the RESULT line ends the file.

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

## Step 7. W1 (i): Section 4 status words against the check files; W1 (iv): 6.4, T3, 5.2

### 7.1 W1 (i). Is each status word the check's own verdict?

Check files (source Section 2): 998 = `gap-crux-exercise3-check-astra.md`, 1000 = `gap-d2-inputs-check-astra.md`,
968 = `gap-avgcurv-check-astra.md`, 970 = `gap-direction2-check-astra.md`, 977 = `gap-tiltproof-check-astra.md`,
978 = `gap-ladder-check-astra.md`, 988 = `gap-unit-check-astra.md`. All cited lines were opened.
The checks use HOLDS / HOLDS AFTER CORRECTION / FAILS. Row 1021 maps them to its own words (L336-338):
stands = HOLDS (after correction); narrowed = holds in a smaller written form; no longer supported = FAILS.
So no status word is literally the check's word; the question is whether the mapping is faithful.

| Row | Status word in 1021 | Check verdict at the cited lines | Faithful? |
|---|---|---|---|
| A1 | narrowed (998 L139, L140, L145, L146, L153) | L139 PT1 HOLDS AFTER CORRECTION; L140 I28 FAILS; L145 KF(d) "separating number" FAILS; L146 KF1 HOLDS AFTER CORRECTION; L153 "(better: w_p)" FAILS | Yes in substance: (i)-(iv) match these lines and L213-219. The check rules on row 998's statements, not on rule W2; "narrowed" is the row's summary. Note: `parts/gap.md` L90 already holds the corrected text and names "Villain U(1) at beta at least 2^14" in the product clause (blame: 1e33bfef1, 2026-11-15 20:15Z, before row 1021 ran). So 7.3's "except that its product clause should name the admitted factor" and W2 (c) are already done. |
| A2 | no longer supported (1000 L41-43; 998 L151) | 1000 L41 (e) FAILS, L42 (f) FAILS, L43 (line 46) FAILS; L85 "a conditional benchmark warning, not a proved exclusion"; **998 L151: HOLDS AFTER CORRECTION**, "retain the claim as that row's argued restriction on the specified port" | Yes as "no longer supported as a discard test" (check 1000). Incomplete: A2 cites 998 L151 only for the T2 dependence; its own verdict keeps N2 as an ARGUED restriction. This matches `parts/gap.md` L91 ("kept as a belief"). The same applies to 4.3 row 24. |
| B5 | (a) stands; (b), (c) no longer supported | L329 AVG(a) HOLDS AFTER CORRECTION, L330 AVG(b),(c) HOLDS; L334 "the broader impossibility claim FAILS" and L382-388 "statements about this attempt, not exclusions"; L324 frozen-group inference FAILS, L363-371 | Yes, all three. |
| B6 | (a) narrowed; (b), (c) no longer supported; (d) narrowed | L213 SUB HOLDS; L197 integral growth inference FAILS; L201 "not a mathematical refutation"; L203, L229 quotient/ABS-flow refutation FAILS; L226 CLASS FAILS; L205, L207 | (b), (c) yes. (a) and (d): check 970 alone gives "not a mathematical refutation" (no longer supported); the narrowing to the supremum form comes from check 977 (B7), which B6's last column says. So "narrowed" is a two-check synthesis, not check 970's verdict. |
| B7 | D1 stands; D2, CAP, ZERO-CEIL stand after correction; QUOT-CAP conditional | L384 D1 HOLDS; L389 D2 5.5 HOLDS AFTER CORRECTION; L390 CAP, L383 ZERO-CEIL HOLD AFTER CORRECTION; L391 QUOT-CAP HOLDS AFTER CORRECTION with the uniform-in-b hypothesis; L392 589/69, 178859/8211; L395-396 | Yes. |
| B8 | (a) no longer supported as universal; (b) stands after correction; (c) no longer supported | L386 universal exclusion FAILS (L385 scalar test HOLDS AFTER CORRECTION); L388 R2 HOLDS AFTER CORRECTION; L381 literal identification FAILS (L380) | Yes. |
| B10 | (a) narrowed; (b) stands as an open premise; (c) confirmed after correction; (d) stands | L452 FLOOR HOLDS AFTER CORRECTION (traced sector; inference to an excluded excitation FAILS); L450 Identity G HOLDS AFTER CORRECTION; 998 L152 HOLDS AFTER CORRECTION; L455 7.1 HOLDS AFTER CORRECTION, L451 ORD real time FAILS | (a), (c), (d) yes. **(b) no**: check 988 says it did not check row 988's direction proposals (L457-458; source 2.10 L233-234 records this). Only Identity G was checked. By the row's own vocabulary (L338), (b) is "not covered" (its identity HOLDS AFTER CORRECTION). |
| B13 | (a), (b), (c) no longer supported; (d) split | L145, L140, L153 FAILS; L187-189 "X:755-756 and 770 FAIL" for the printed CONTR; L159 HOLDS for the original CAS | Yes. |
| C1 | narrowed (998 L140, L146, L213-219) | L140 FAILS; L146 HOLDS AFTER CORRECTION; L213-219 domain test (no verdict word) | Yes in substance. "Theorem-grade in the lane for Villain at beta >= 2^14" is not at the cited lines; it is check 998 L95-102 ("relevant prior progress", `gap-tu-retry.md` 198-250), which keeps "the transfer/insertion application" as a named input. "Theorem-grade" should carry that input. |
| C8 | D2 stands after correction; SUB stands | 977: D2 HOLDS AFTER CORRECTION (L389, RESULT L404); 970 L213 SUB HOLDS; L207 typical-tilt form with a bad set not refuted | Yes. |

Count: eight rows faithful in substance (A1, B5, B7, B8, B13, C1, C8, and A2 with the noted omission);
one wrong status word (B10 (b): "stands" where the check did not rule); one two-check synthesis labelled
with one check (B6 (a), (d)). None of these changes the registry of Section 5 or its ranking: LC's
unblocking rests on A2/A10 (check 1000 L41-43, L85), which is faithful.

### 7.2 W1 (iv). Section 6.4 items 1-4, the verdict on T3, and the reading on (ABS-flow) in 5.2

**Item 1 (L628-640). CORRECT given (K3); ADVANCE.** Redone: for any target slice variance S, a Gaussian chain
with the bare kernel exists (sinh omega = 1/(2 beta_0 S), c = beta_0 (e^omega - 1)). With S = L^K/(a_+ beta_K),
(K2) gives omega <= a_+ beta_K/(2 beta_0 L^K); then mu^2 = 2 beta_0 (cosh omega - 1), about beta_0 omega^2, at most
about a_+^2 beta_K^2/(4 beta_0 L^(2K)): space-like stiffness of order beta_K^2/beta_0 at q of order L^(-K), time-like
stiffness beta_0 (K1). (K3) then forbids (P1) once beta_0 > 2 a_+ beta_K. Cross-provider agreement: check 1000
L53-83 builds the same chain (E = (beta_K/beta_0)|p|, covariance about 1/(2 beta_K |p|), "bare kinetic
coefficient unchanged") and its sigma^2 = 1/(2 beta_0 sinh E) (L65-66) is test (a) by another provider. Check
1000 used the chain to break an inference; row 1021 adds that the chain fails (P1) in reading (K3). The two
agree. The last sentence (the independent-level field breaks (ii)) is ARGUED, as marked.

**Item 2 (L641-644). CORRECT; CORRECT-NO-ADVANCE.** The count is made for linear statistics in a gauge-fixed
chart (row 982 L88, L113); NS shows that ambient linear statistics are not soft. Check 1000 L45-51 makes the
same point (the colour test is not invariant under the full SU(2) action). Limit, which the source does not
overstep: linear statistics of a gauge-fixed chart are other functions of the slice, and item 2 says nothing
about whether some gauge-invariant function is soft.

**Item 3 (L645-651). CORRECT given (E1) and the gap on the gauge-invariant sector; CORRECT-NO-ADVANCE.**
For mean-zero gauge-invariant f, ||P f||^2 <= e^(-2 E_1) ||f||^2, so EE(f) = ||f||^2 - ||P f||^2 >= (1 - e^(-2 E_1)) Var(f).
Per unit of s: beta_0 (1 - e^(-2 M a)), about 2 beta_0 M a. This bounds interpolant energies only, not the
constants gam_s, so it does not conflict with check 982 L63-67 (no lower bound on the integral of gam_s from E_1).
"The gap restated" is the right label.

**Item 4 (L652-654). Direction CORRECT; the mark over-reads. CORRECT-NO-ADVANCE with a label defect.**
PROVED part: all terms D_k D_k^T/rho_k are positive semidefinite, so the TEL output 1/||sum_k D_k D_k^T/rho_k|| is
at most rho_K/||D_K||^2. The size a_- beta_K a/l_unit needs ||R_0 D_K||^2 of order L^K, which row 982 L113 marks
ARGUED; check 982 (`gap-hcphys-check-astra.md` L80) holds the use "AFTER CORRECTION as a conditional benchmark
only", and asks for the full-action rate lambda_k beta_k in place of a_- beta_k. So item 4 is "PROVED for the
structure, ARGUED for the size", not "PROVED in row 982; check 982 HOLDS". It is a warning; nothing rests on it.

**Verdict on T3 (L656-658). CORRECT given (K3); ADVANCE (a filter narrowed).** "FAILS as a discard test" means:
no M' in K with H true and T false is on record, and in the Gaussian class there is none once
beta_0 > 2 a_+ beta_K, given (K3). It does not mean that T3's conclusion is false; a non-Gaussian benchmark is
not excluded, and the source says so ("No model ... is on record"). Before row 1021, `parts/gap.md` L91 already
had N2 UNSUPPORTED after check 1000; row 1021 adds the Gaussian-class reason and moves T3 to a warning on TEL.

**Reading on (ABS-flow) in 5.2 (L476-482). Rewriting CORRECT; conclusion CORRECT as labelled (ARGUED); the
stated reason is incomplete. CORRECT-NO-ADVANCE.**
- Redone at t = 0 from `gap-avgcurv-max.md` L373-375, with mu' = F nu_s (E F = 1), v = grad log F, C_phi the
  covariance of J_(b,phi): grad F^(1/2) = F^(1/2) v/2 gives LHS = (1/2) E_mu'[v^T C_phi v],
  2 kap E|grad F^(1/2)|^2 = (kap/2) E_mu'|v|^2, (1/4) E[F |Hess log F|^2] = (1/4) E_mu'|grad v|^2. Times 2:
  E_mu'[v^T (C_phi - kap) v] <= (1/2) E_mu'|grad v|^2. Same as the source.
- Conclusion "the supremum argument of D2 does not transfer": correct as a statement about D2's proof, which
  evaluates C_phi at single pinned tilts, while (ABS-flow) averages over a smooth gauge-invariant density.
  Consistent with check 970 L203, L229 and C8.
- Reason given ("that part is charged with the same kap on the right"): incomplete. kap is subtracted from C_phi
  pointwise, so the kap term alone does not block a transfer where C_phi > kap (D2's sheets give exactly that).
  What blocks the direct transfer is the localisation cost (1/2) E_mu'|grad v|^2 together with the gauge
  invariance of F (no linear log F, Lemma INV). One-line illustration (ARGUED, not a bound on kap): for
  F = e^(lambda G), v = lambda grad G vanishes at the maximum of G where mu' concentrates, and near it
  E|v|^2 grows like lambda while E|grad v|^2 grows like lambda^2. The source's own label "ARGUED; not a bound on
  kap" is right.

### 7.3 Two notes for the lead on the W2 edits (outside (i)-(iv); one line each)

- W2 (a) proposes "A row on level convexity must name ... and the pointwise bound (R-pt)". (R-pt) is the
  hypothesis (ii) of Lemma LIFT, the first open step of the attack in 6.5, not a necessary condition for every
  level-convexity row. Suggested wording: "... with a unit-level inequality; through Lemma LIFT this needs the
  pointwise bound (R-pt)". Also cite 6.4 as "given the reading of (P1) in (K3)".
- W2 (c) is already in `parts/gap.md` L90 (see A1).

## Step 8. Report

**Provenance.** Claude Opus 5.5, max effort, Mac mini worker 2; source `library/gap-registry-after-checks-max.md`
at commit f6c0017dc (row 1021, written by Claude Fable 5.2 max). Same provider as the author: this is one
reading by a different model of the same provider, not a cross-provider check and not an audit. No
subagents, no numeric run, no commit or push. One public source was read: CA-II at 31a47c543775, lines
80025-80048 and 80150-80180 (Sussman and Alpoge, with Claude and Codex as authors of their text).

**Verdict per statement.** (Words: ADVANCE = correct and it changes the lane's record; CORRECT-NO-ADVANCE =
correct, record unchanged; WRONG = a line fails.)

| Statement (source line) | Verdict | Note |
|---|---|---|
| Test (a) sigma^2 = 1/(2 beta sinh omega) | passes | three routes; also check 1000 L65-66 (other provider) |
| Test (b) (1 - e^(-omega))/sinh omega = 2/(e^omega + 1) | passes | |
| Test (c) gauge invariance of the path law; side 3 | passes | side 2 really fails |
| Test (d) (E1) used for gauge-invariant f only | passes | L550 states it for all f; also true |
| Test (e) (K3) a fair reading of (P1) | passes as a reading | quote at hcphys L46 faithful to CA-II 80163-80172; the 2 a_+ threshold is model-dependent |
| Lemma S1 (L557) | CORRECT-NO-ADVANCE | |
| Proposition FR (L562) | CORRECT-NO-ADVANCE (given (E1)) | at T = 1 it is (E1) |
| Lemma EL (L573) | ADVANCE | one unstated step (tau_k free of l, by lattice symmetry on a cubic box) |
| Corollary NS (L588) | CORRECT-NO-ADVANCE | about ambient linear statistics only |
| Lemma KL (i)-(iii) (L594) | ADVANCE | |
| (K1), (K2), (K3) (L616-620) | CORRECT (part of KL's ADVANCE) | (K3): edge case p = 0 excluded by mu^2 > 0 |
| 6.4 item 1 (L628) | CORRECT given (K3); ADVANCE | last sentence ARGUED, as marked |
| 6.4 item 2 (L641) | CORRECT-NO-ADVANCE | |
| 6.4 item 3 (L645) | CORRECT-NO-ADVANCE (given (E1)) | the gap restated |
| 6.4 item 4 (L652) | CORRECT-NO-ADVANCE; mark over-reads | size is ARGUED, not PROVED (defect 2) |
| Verdict on T3 (L656) | CORRECT given (K3); ADVANCE | "FAILS as a discard test" = no valid benchmark on record; T3's conclusion is not shown false |
| 6.5 arithmetic after LIFT; averaged statement (L671-681) | CORRECT (given (E1) and the stated hypothesis) | |
| Lemma LIFT (L665) | CORRECT-NO-ADVANCE | |
| Lemma NB (L683) | CORRECT-NO-ADVANCE | ambient gradient; tangential version has the same ratio |
| 5.2 reading on (ABS-flow) (L476) | CORRECT-NO-ADVANCE as ARGUED | reason incomplete (defect 3) |
| Section 4, ten rows of W1 (i) | eight faithful in substance, B6 (a)/(d) a two-check synthesis, B10 (b) wrong word | table in 7.1 |

**Stop rule.** No WRONG in Lemma KL or Lemma EL. The rule was not triggered.

**Defects (ranked by what each breaks; none breaks a PROVED statement, the T3 verdict or the ranking).**
1. B10 (b) (source L372): "stands as an open premise" is not a check verdict. Check 988 L457-458 did not check
   row 988's direction proposals (the source says so at L233-234). By the source's own vocabulary (L338) it is
   "not covered"; only Identity G HOLDS AFTER CORRECTION (L450).
2. 6.4 item 4 (L652): "PROVED in row 982, Lemma TEL; check 982 HOLDS" over-reads. The bound
   TEL output <= rho_K/||D_K||^2 is proved; the size a_- beta_K a/l_unit rests on ||R_0 D_K||^2 of order L^K, ARGUED in
   row 982 L113 and held only "as a conditional benchmark" by check 982 L80 (which also asks for lambda_k beta_k).
3. 5.2 (L478-480): the reason "charged with the same kap on the right" does not by itself block a transfer of
   D2; kap is subtracted from C_phi pointwise. The block is the localisation cost (1/2) E_mu'|grad v|^2 and the
   gauge invariance of F. The conclusion and its label ARGUED stand.
4. B6 (a), (d) (L368): "narrowed" uses check 977 (B7); check 970 alone says "not a mathematical refutation"
   (L201) and FAILS the growth inference (L197).
5. A2 (L349): check 998 L151's own verdict is HOLDS AFTER CORRECTION, keeping N2 "as that row's argued
   restriction"; A2 cites that line only for T2. (Same for 4.3 row 24.)
6. C1 (L412): "theorem-grade in the lane for Villain at beta >= 2^14" comes from check 998 L95-102, which keeps
   "the transfer/insertion application" as a named input.
7. 7.3 (L776-777) and W2 (c) (L815): already done; `parts/gap.md` L90 names "Villain U(1) at beta at least 2^14"
   since 1e33bfef1 (20:15Z), before row 1021 ran.
8. W2 (a) (L812-813): "must name ... the pointwise bound (R-pt)" turns the first open step of one attack (the
   LIFT route) into a requirement for every level-convexity row. Repair (unproved wording): "through Lemma
   LIFT this needs (R-pt)"; and cite 6.4 "given the reading of (P1) in (K3)".

**What this check does not cover.** Sections 1-3 and 5.1 of the source beyond the rows W1 names; rows of
Section 4 outside A1, A2, B5, B6, B7, B8, B10, B13, C1, C8; the derivation of (E1) itself (taken from row 982
and its check, as the source does); CA-I Def 1.5 (the source's reading in Lemma NB); a derivation of (K3)
from the literal (P1) (not attempted: no new attack). The ARGUED transfer of the qualitative clause of 6.4
item 1 to the literal (P1) in Step 2 (e) is mine and unproved.

## Status log

- 2026-11-15T22:14Z: file created with plan (Step 1).
- Steps 2-7 appended in order (tests; EL and NS; KL; S1 and FR; LIFT and NB; Section 4 rows and 6.4/5.2).
- 2026-11-15T22:28Z: Step 8 (this report) written.

RESULT: Row 1023 (Claude Opus 5.5 max, Mac mini worker 2; same-provider check of row 1021 W1, not cross-provider; no numeric run, no subagents): tests (a)-(e) pass ((e) only as a reading: (K3) keeps the two-sided isotropic shape of (P1), CA-II 80163-80172 quoted faithfully, but its frequency form and threshold 2 a_+ are not derived from (P1)); Lemma EL and Lemma KL with (K1)-(K3) redone by hand, no WRONG, both ADVANCE (stop rule not triggered); Lemma S1, Proposition FR (given (E1)), Corollary NS, Lemma LIFT, Lemma NB CORRECT-NO-ADVANCE; 6.4 items 1-3 correct (item 1 given (K3)), item 4 correct in direction but its size is ARGUED not PROVED; the verdict "T3 FAILS as a discard test" is CORRECT given (K3) and means no valid benchmark is on record, not that T3's conclusion is false; the 5.2 (ABS-flow) rewriting is correct and its ARGUED conclusion stands, with an incomplete reason; Section 4: eight of the ten named rows match their check lines in substance, B6 (a)/(d) is a two-check synthesis, and B10 (b) "stands" is not a check verdict (should be "not covered"); W2 (c) is already in parts/gap.md L90, and W2 (a) should not make (R-pt) a requirement for every level-convexity row. Still open: (R-pt), a unit-level log-Sobolev inequality for a gauge-invariant slice variable, a derivation of (K3) from the literal (P1), (W), (LIOU), (BDD-Delta), the seed.
