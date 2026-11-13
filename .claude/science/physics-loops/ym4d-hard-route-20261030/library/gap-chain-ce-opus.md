# FINISH row 916: links (c) and (e) of the chain (SEED-FP) to (GAP), and (ONE-K)

Author: Claude Opus 5.5 (max effort), FINISH row 916. Work by hand, no subagents.
Clone: /Users/jonreilly/ym4d-lead/clone at commit 32d4b2c3fdcd5d4d64cb641fca9629e067c611bd
(2026-11-13 14:03:51 -0500, "docs(ym4d): record row 913 ...; add rows 914-916").
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Sources on disk: SA outline /Users/jonreilly/ym4d-lead/sa/YM4_sketch_500.tex ("SA Lnnn");
account /Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex ("CA Lnnn").
The outline and the account are the work of Ethan Sussman and Levent Alpoge. Text here is by Claude and Codex lanes.
Tags: PROVED (this file), READ (path:line), ARGUED, OPEN.

## Plan
1. Read row 837 (gap-finishline-opus.md): (SEED-FP) lines 110-160, section 2.5, links (a)-(e).
2. Read gap-os-equiv.md: Proposition P', (P1)-(P4), (H2), (TOT), line 61 instance.
3. Read the account: volume-first limit points nu_j (SA L6879), tori (row 703), OS/limit lines.
4. Link (c): prove or state the exact missing statement with closest account lines.
5. Link (e): check (P1)-(P4), (H2), (TOT) on the account's objects, with line numbers.
6. Read gap-target-max.md (row 913): (ONE-K); find the account's cutoff-universality statement.
7. Assess (ONE-K) exactly.
8. Summary table and RESULT line.

## Step 1. Row 837 (D/library/gap-finishline-opus.md), read in full (266 lines)

- READ gap-finishline-opus.md L113-120: (SEED-FP). Fix odd L, g <= gamma_H, first-passage data (K, beta), beta in W_K(g), a_K = L^(-K).
  There are K_0, a physical size ell with ell/(2 a_K) an integer >= 3 for K >= K_0, and s_* < 1/5041, with
  S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_* for every first-passage datum with K >= K_0 (bare Wilson transfer operator).
- READ L152-161, the table 2.5:
  (a) seed -> gap >= M_* a_K on every periodic cube of integer side >= ell/a_K (PROVED, rows 698, 699);
  (b) -> every limit state at that spacing, along any sequence of integer-sided tori, has a unique vacuum and transfer norm
      <= e^(-M_* t) off it (PROVED, row 703);
  (c) the account's volume-first limit points nu_j (SA L6879) are such limit states (ARGUED);
  (d) the continuum datum: SA L6915 (a)(iii), SA L6928-6933 (b)(v), CA-I L2690-2703 (ii-R^4) (READ, conditional on A-H);
  (e) (d) supplies (P1)-(P4), (H2), (TOT) of Proposition P' (ARGUED; cites gap-os-equiv.md L61);
  (f) -> (GAP) (ARGUED composition).
- Row 837 cites "CA-I" = theorem_0_complete_account_raw_I.tex at 31a47c543775. This lane's brief names the account file
  /Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex. So CA-I line numbers in row 837 need not match YM4_1400.tex.
  This file cites "CA L" for YM4_1400.tex and re-locates each statement there (Step 3).
- Three gaps in (c) as written, to be checked in Step 4:
  (c1) the limit of row 703 is a limit of the bare lattice state at FIXED spacing a_K as the torus grows; the account's
       nu_j is a limit at fixed cutoff index j (READ needed, SA L6879), so (c) must match "spacing" and "cutoff" exactly;
  (c2) the account's limit object may be the law of the renormalized curvature fields (smeared), not the bare state
       on all local functions; the gap of (b) is a statement on the bare transfer operator;
  (c3) the continuum: (GAP) is a statement after j -> infinity; (b) is at fixed spacing. The passage of the
       bound e^(-M_* t) to the j -> infinity limit is Proposition P', and it needs (P1)-(P4), (H2), (TOT) (link (e)).

## Step 2. Proposition P' and its inputs, read in the lane files

- Proposition P' is stated in D/library/gap-seed-limit.md L200-202 (not in gap-os-equiv.md). READ there:
  cutoffs iota_j with a_(iota_j) -> 0; nu_j "limit states as in (b)" (of Proposition P); a continuum datum D_inf with
  (P1)-(P3) and a class C with (H2) "at each time t > 0" and (TOT); conclusion: unique vacuum and, with (P4),
  spec(H) in {0} union [M_*, infinity). Proof: (H1) of gap-os-equiv.md (5) with m_n = M_*, then (5a)-(5c).
  Checked: gap-seed-limit-check.md A10 (L78-82), "HOLD (as conditional statements)".
- "Limit state" (READ gap-seed-limit.md L118-120, 4.1): a map nu on local functions (bounded Borel functions of the
  bare link variables on a finite link set of Z^4) with nu(F) = lim_i <F>_(k_i,T_i) for EVERY local function F,
  along an admissible sequence. Row 703 Part B (READ gap-seed-limit-check.md L175, L184-187): admissible = integer
  sides L_i -> infinity (any order, any residues) and T_i - a_(L_i) -> infinity; symmetric tori T_i = L_i qualify;
  Proposition P' "Unchanged in form; the members may now be limit states along any integer sides".
- The datum of a member (READ gap-seed-limit.md L152, Theorem L3 (e)): V = local functions with time range in
  [0, infinity), b(F,G) = nu(conj(Theta F) G), Theta the SITE mirror t -> -t of Lemma RPc (L132).
- Definitions (P1)-(P4): READ gap-os-equiv.md L48-52. Instance (S): READ L61, "V is the span of separated tuples
  supported in {x_4 > 0} (with the empty tuple 1), b(F,G) = sigma(theta F-bar . G)", with (P1)-(P4) taken from
  library/cl1.md Lemma 3, (4), (6)-(7). (H1), (H2): READ L221-222. (H2) asks t in 2T_(inf,+), which includes t = 0.
  (5a)-(5c): READ L225-227. (5d) L228 FAILS AS WRITTEN at one sentence (READ gap-os-equiv-check.md L31, R1);
  P' does not use it.
- PROVED (one line, from (5a) and (3a)-(3b) as READ): (H2) at the times t > 0 only suffices. Take any s > 0 in
  2T_(inf,+); (5a) with s <= t gives u_inf(F,F;t) <= e^(-m(t-s)) u_inf(F,F;s), which is (X_m^C) of Statement (3)
  with C_F = e^(ms) u_inf(F,F;s), t_F = s; (3b) needs no bound on C_F. So P' as written (t > 0) is sound.
- What P' needs from the account, in full: (i) members nu_j that are lane limit states at cutoffs with the seed;
  (ii) a datum D_inf with (P1)-(P3), and (P4) for the spectral form; (iii) a class C, a map iota_j from C to member
  observables (local functions with time range in [0, infinity)), and (H2) for C; (iv) (TOT) for C in H(D_inf).
  Item (iii) has a hidden requirement: iota_j F must be a local function (bounded, finite support) and the member's
  reflected pairing b_j(iota_j F, tau iota_j F) must be the account's Schwinger function of the pair. Step 3 reads it.

## Step 3. The account's objects, read in YM4_1400.tex (CA) and the outline (SA)

The outline and the account are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Every READ item states what the text says at the line. The account states its theorem under its hypotheses
(CA L1748-1751: "Assume the uniform background, interaction, history, flow and ordinary-source estimates").

- (O1) Objects. READ CA L1640-1658: T_ell = (R/ell Z)^4, Lambda_(K,ell) = a_K Z^4/ell Z^4, a_K = L^(-K); compatible sides
  2L^m; L(g) = sides >= ell_*(g); mu_(K,ell,beta)(dU) = Z^(-1) e^(-beta sum_p a_p(U)) dU, a_p = 1 - (1/2) Re tr U_p;
  O(f) = sum_p f(x(p)) a_p(U) (CA L1651), with "no prefactor involving the spacing"; S^T_n = the connected
  correlations of the O(f_i); tests: tuples of real C^1_c functions with pairwise disjoint supports (CA L1656).
  So the bare measure is exactly the lane's Wilson measure at beta_W = beta (the lane's normalization, row 819).
- (O2) Exact covariance. READ CA L1726: for each lattice isometry r, "O(f) o r^* = O(r f)" exactly; if supp f is at
  distance > C a_K from a mirror, "every contributing plaquette and all its bonds stay on that same side".
  READ CA L1726 also: on ell = 2L^m each axis has the even number 2L^(m+K) of sites.
- (O3) Volume-first limits. READ CA L1690 (= SA L6879): "A volume-first limit at g is a limit lim_j S^T_n[nu_j],
  taken along first-passage data (K_j, beta_j) with K_j -> infinity. In it each nu_j in G^tor_(K_j,beta_j) is a limit
  point of the periodically extended torus measures as ell -> infinity, with spacing and coupling held fixed."
- (O4) What "limit point" means. READ CA L99109-99113: Wilson measures "on periodic tori with integer periods
  N -> infinity" are lifted periodically to X = G^E (E = one orientation of each bond of a Z^4; product topology,
  compact metrizable, CA L99078-99081); "The lifted measures have a weakly convergent subsequence" (Riesz limit).
  READ CA L99150-99156: weak limits are invariant Wilson DLR states (translations, hypercubic group).
  READ CA L99172-99175: the same cofinal family of admissible tori is used "for the periodic lifts and for their
  limit points in G^tor_(K,beta)". READ CA L99176-99195: the marginal on a finite window W of a lift, and of "any
  fixed-cutoff torus limit point", has a Haar density bounded below by e^(-2 beta |P(W)|), and these densities
  "converge uniformly along any torus subsequence converging weakly to mu".
- (O5) Lattice observables. READ CA L99284-99294: O_j(f) = sum_p f(x_p) A_p, X_j(f) = O_j(f) - nu_j(O_j(f)),
  m_(j,n)(f) = rho_j prod X_j(f_i); "At a fixed cutoff these are bounded continuous random variables with finite
  bond dependence." For a volume-first limit the integrating and centering states are both nu_j (O3: S^T_n[nu_j]).
- (O6) Uniform bounds. READ CA L1777-1785 ((c)(1), (c)(2)): |S^T_n| <= C^infty_n(d; R) prod ||f_i||_sharp for
  supports in balls of radius R at mutual distance >= d; C^infty_n(d; R) does not increase in d; "The bounds (2)
  also hold, with no condition on a volume, for S^T_n[nu], where nu is an arbitrary periodic Gibbs state on L_K of
  Wilson's weight at beta, and where (K, beta) is a first-passage datum." (uniform in the datum: CA L1692).
- (O7) Moving tests. READ CA L99531-99541 ((cc:telescoping)) and L99568-99583 ((cc:moving-tests),
  (cc:translation-modulus)): multilinearity and the uniform bound give convergence when f_(i,j) -> f_i in C^1
  inside fixed separated neighbourhoods; ||tau_v f - tau_w f||_sharp -> 0 as v -> w.
- (O8) The limit. READ CA L1757-1775 ((b)): invariance under W_4 and translations (i); reflection positivity at each
  coordinate mirror for sigma_S (ii); (b)(v) at CA L1768-1771 (= SA L6928-6933): "Take the form
  <F,G> = sigma_S(theta F-bar . G) on C S({x_4>0})", with T_t[F] = [tau_(te_4) F] = e^(-tH) "a strongly continuous
  semigroup of self-adjoint contractions, where H >= 0 and H Omega = 0"; CA L1775: "each volume-first limit is a
  limit of (a)(iii)". READ CA L1709: sigma_S = sum over partitions without singletons of products of S_|J|.
- (O9) The Hilbert space. READ CA L115178-115206 (Proposition "Compact-tuple Euclidean reconstruction"): under
  (HB1) (reflection positivity on every finite combination, CA L115143-115159) and (HB2) (moment bounds
  M_n(d,R) prod ||f_i||_1, CA L115161-115167), "the completion of V_+ by its reflection form is a separable Hilbert
  space H"; V_+ = combinations of separated tuples with supports compactly contained in {x_4 > 0} (CA L115140-115141);
  T_t[F] = [tau_(te_4) F] is a strongly continuous semigroup; H >= 0 unique with T_t = e^(-tH).
- (O10) The account itself flags the limits of its statement: READ CA L99834-99840, the compactness argument
  "supplies no identification of two different extracted limits, no matched-cutoff convergence rate".

## Step 4. Link (c): PROVED

Work in lattice units at a fixed first-passage datum (K, beta); physical lengths are lattice lengths times a_K.
<.>_N is the Wilson expectation on the symmetric torus (Z/N)^4 at beta. mu~_N is its periodic lift to X = G^E.

**Lemma C (link (c)).** Let nu be in G^tor_(K,beta): a limit point, in the weak topology on probability measures on X,
of the lifts mu~_N along the account's family of tori (integer sides N -> infinity; READ CA L99109-99113, L99172-99175).
(i) There are integer sides N_i -> infinity with mu~_(N_i) -> nu weakly.
(ii) For every local function F (bounded Borel, finite link set Gamma): nu(F) = lim_i <F>_(N_i).
(iii) So nu is a limit state, in the sense of gap-seed-limit.md 4.1 with row 703 B4, of the admissible sequence
     (L_i, T_i) = (N_i, N_i).
(iv) If (SEED-FP) holds at (K, beta), with seed time N_0 = ell/(2 a_K) and value s <= s_* < 1/5041, then nu has a
     unique vacuum and ||T_nu^t psi|| <= e^(-M_* a_K t) ||psi|| for psi orthogonal to the vacuum, t in Z_+, in each
     of the four directions, with M_* = 2 log(1/(5041 s_*))/ell in the first-passage unit.

Proof.
(i) X is compact metrizable (READ CA L99078-99081) and C(X) is separable (READ CA L99113-99115). With a countable
uniformly dense family (phi_k) in C(X), d(mu, mu') = sum_k 2^(-k) min(1, |mu(phi_k) - mu'(phi_k)|) is a metric for
the weak topology on probability measures. So every limit point of the family is the limit of a sequence N_i -> infinity.
(ii) Continuous local F: once N_i exceeds every width of Gamma by 2, the quotient Z^4 -> (Z/N_i)^4 is injective on the
end points of Gamma, and mu~_(N_i)(F) = <F>_(N_i) (the lift of a torus configuration restricted to Gamma is that
configuration on the image of Gamma). Weak convergence gives <F>_(N_i) -> nu(F).
Bounded Borel F on G^Gamma: Lemma FE (READ gap-seed-limit.md L124-126; checked, row 703 A5) gives for every torus with
sides >= 3 that the marginal of <.>_N on G^Gamma has a Haar density at most E := e^(12 beta |Gamma|). For continuous
phi >= 0 on G^Gamma, nu(phi) = lim_i <phi>_(N_i) <= E Haar(phi). Both sides are finite Borel measures on a compact
metric space, so by regularity the marginal of nu is at most E Haar as well. Take eps > 0 and a continuous F' with
Haar(|F - F'|) < eps (continuous functions are dense in L^1 of Haar; the density step of Theorem L3 (a), step 4).
Then |<F>_(N_i) - <F'>_(N_i)| <= E eps for every i, |nu(F) - nu(F')| <= E eps, and <F'>_(N_i) -> nu(F').
So limsup_i |<F>_(N_i) - nu(F)| <= 2 E eps for every eps > 0.
A second route is READ in the account: CA L99176-99195 (the Haar densities of the window marginals of the lifts converge
uniformly along any torus subsequence that converges weakly to the limit point).
(iii) The sides N_i are integers tending to infinity and T_i - a_(N_i) >= N_i/2 -> infinity, so (N_i, N_i) is
admissible (READ gap-seed-limit-check.md L175). Statement (ii) is the defining property of a limit state
(READ gap-seed-limit.md L118-120: nu(F) = lim_i <F>_(k_i,T_i) for every local function F).
(iv) (SEED-FP) at (K, beta) is Hypothesis (G) at N_0 (READ gap-finishline-opus.md L119-120: N_0 = ell/(2a_K) is an
integer >= 3). Row 703 B2 gives (G-all) for every integer side >= 2 N_0 (PROVED GIVEN Theorem S, Lemma E'; checked,
rows 698, 699, 703). N_i >= 2 N_0 for large i. Row 703 B4 gives Theorem L3 (c)-(e) along integer sides
(READ gap-seed-limit-check.md L185-187). Proposition P (c) with n_iota = N_0, a_iota = a_K, ell_* = ell/2 gives
m_0 >= M_* a_K (READ gap-seed-limit.md L188-198; checked A10). QED

Remarks.
1. Lemma C uses no hypothesis of the account. G^tor_(K,beta) is non-empty by plain compactness (READ CA L99112-99113).
   Only part (iv) uses the seed.
2. The account's sides: ell = 2L^m in physical units, so N = 2L^(m+K) lattice sites per axis (READ CA L1726).
   The account's limit points are taken with "spacing and coupling held fixed" (READ CA L1690). Both facts match (iii).
3. The bare measure is the lane's: mu_(K,ell,beta) has weight e^(-beta sum_p (1 - (1/2) Re tr U_p)) (READ CA L1640-1650),
   the plaquette term of Lemma FE, so the constant 12 beta |Gamma| applies unchanged.
4. Row 837 marked (c) ARGUED. What it lacked was the account's definition of G^tor (CA L99109-99195), which shows that
   the account's limit is weak convergence of measures on the bare links. With it, (c) is a lemma about measures.

## Step 5. Link (e): PROVED, given the account's statements (O3) and (O6)

**Setting.** S is a volume-first limit at g with defining sequence (K_j, beta_j, nu_j) (READ CA L1690; the phrase
"defining sequence (K_j, beta_j, nu_j)" is READ CA L1893). (SEED-FP) holds at g; drop the finitely many j with
K_j < K_0. Put a_j = a_(K_j) and sigma = sigma_S (READ CA L1709).
- Continuum datum D_inf (instance (S) of gap-os-equiv.md L61; the account's form, READ CA L1768): V = V_+, the complex
  combinations of separated tuples X = (f_1, ..., f_n) of C^1_c tests with supports compactly inside {x_4 > 0}, and the
  empty tuple 1 (READ CA L115120-115141); b(F, G) = sigma(theta F-bar . G); tau_t (t >= 0) translates every entry by
  t e_4; time set R.
- Class C = the separated tuples in V, with 1.
- Members D_j = the datum of Theorem L3 (e) for nu_j: V_j = local functions with time range in [0, infinity),
  b_j(F, G) = nu_j(conj(Theta F) G), Theta the site mirror at time 0, physical time set a_j Z. Each nu_j is a lane
  limit state with the seed (Step 4, Lemma C (iii), (iv)).
- Lattice versions: for X in C let delta_X > 0 be the distance of its supports from {x_4 = 0}. For C a_j < delta_X put
  iota_j X = prod_i X_j(f_i), X_j(f) = O_j(f) - nu_j(O_j(f)) (READ CA L99284-99294); iota_j 1 = 1; for the finitely many
  other j put iota_j X = 1 (only j -> infinity enters (H2)). Extend linearly to V.

**E1 (iota_j X lies in V_j). PROVED.** READ CA L1726: if supp f is at distance > C a_K from the mirror, every bond of
every contributing plaquette lies on the same side. READ CA L99293-99294: O_j(f) is bounded, continuous, with finite
bond dependence. So iota_j X is a local function with time range in (0, infinity).

**E2 (exact lattice identities). PROVED.** For X, Y in C, j large and s in a_j Z_+:
 (a) conj(Theta iota_j X) = iota_j(theta X-bar); (b) tau_s iota_j Y = iota_j(tau_s Y);
 (c) b_j(iota_j X, tau_s iota_j Y) = M_j(theta X-bar . tau_s Y), where M_j(Z) = nu_j(prod over entries f of Z of X_j(f));
 (d) M_j(Z) = sum over partitions pi of Z with no singleton of prod over blocks J of S^T_|J|[nu_j](Z_J).
Proof. The site mirror x_4 -> -x_4 and the shift by s e_4 are lattice isometries r of a_j Z^4. READ CA L1726:
O(f) o r^* = O(r f) exactly. READ CA L99150-99156: nu_j is invariant under lattice translations and the hypercubic
group, so nu_j(O_j(r f)) = nu_j(O_j(f)) and centering commutes with r. O_j is complex linear, so conj O_j(f) = O_j(f-bar).
This gives (a), (b); (c) is the definition of b_j. (d): a moment of centred variables is the sum over partitions of
products of cumulants; first cumulants of centred variables vanish, and cumulants of order >= 2 do not change under
centering. The tuple theta X-bar . tau_s Y is separated: its first entries lie in {x_4 <= -delta_X}, the others in
{x_4 >= delta_Y + s}, and inside each part the supports are disjoint compact sets. QED

**E3 (convergence). PROVED GIVEN READ.** (i) M_j(Z) -> sigma(Z) for every separated tuple Z: by E2 (d), READ CA L1690
(S_n = lim_j S^T_n[nu_j] on separated tuples, n >= 2) and READ CA L1709 (sigma_S = sum over Part_(>=2) of products of S).
(ii) If Z_j -> Z entrywise in ||.||_sharp, with all supports in fixed pairwise separated compact sets, then
M_j(Z_j) -> sigma(Z). Reason: READ CA L1785: the bound (c)(2) holds for S^T_n[nu], nu any periodic Wilson Gibbs state at a
first-passage datum, with C^infty_n(d; R) independent of the datum (READ CA L1692, L1724); nu_j is such a state (READ
CA L99150-99156: "periodic, with the whole lattice as a period group"). Multilinearity gives the telescoping bound of
READ CA L99531-99541 for each product in E2 (d), uniformly in j; then (i).

**The six items of Proposition P'.**
- (H2) PROVED. Let X in C and t >= 0. Take t_j in 2 a_j Z_+ with |t_j - t| <= 2 a_j. By E2,
  u_j(iota_j X, iota_j X; t_j) = M_j(theta X-bar . tau_(t_j) X) - M_j(theta X-bar) M_j(X). By E3 (ii) and the
  translation modulus (READ CA L99578-99583) this tends to sigma(theta X-bar . tau_t X) - sigma(theta X-bar) sigma(X)
  = u_inf(X, X; t). This holds at every t >= 0, t = 0 included (the reflected pair is separated by 2 delta_X).
  Remark: at the L-adic times t = 2p L^(-q), t lies in 2 a_j Z once K_j >= q; there t_j = t and E3 (i) suffices, so
  (H2) on a dense set of times uses only the definition of S.
- (P1) PROVED. For F = sum_k c_k X_k in V: b(F, F) = sum c_k-bar c_l sigma(theta X_k-bar . X_l)
  = lim_j sum c_k-bar c_l M_j(theta X_k-bar . X_l) = lim_j b_j(iota_j F, iota_j F) >= 0, by E2 (c), E3 (i) and (P1) of
  each member (Theorem L3 (c), (e) under (G-all), Step 4 (iv)). Also READ CA L1759 ((b)(ii)) for the account's own proof.
- (P2) PROVED. sigma is invariant under real translations (READ CA L1757-1758, (b)(i); proved at CA L99589-99594 from
  E3 (ii)). On tests theta tau_t = tau_(-t) theta. So b(F, tau_t G) = sigma(tau_(-t)(theta F-bar) . G)
  = sigma(theta (tau_t F)-bar . G) = b(tau_t F, G).
- (P3) PROVED, with k_F = 0 and C_F = b(F, F). By (P2), b(tau_t F, tau_t F) = b(F, tau_(2t) F). Take s_j in a_j Z_+,
  s_j -> 2t. By E2 and E3 (ii), b(F, tau_(2t) F) = lim_j <[iota_j F], T_j^(s_j) [iota_j F]>_j, and the modulus of each
  term is at most b_j(iota_j F, iota_j F) because ||T_j^(s)|| <= 1 (gap-os-equiv.md (1b) for the member). The bound
  tends to b(F, F). (READ alternative: (b)(iv) at CA L1761 gives (c)(2) for the limit; the radii of the tuple
  (theta tau_t F-bar, tau_t F) do not change with t and its separation does not decrease.)
- (P4) PROVED. sigma is multilinear and obeys (c)(2) on separated tuples (pass the uniform bound of E3 (ii) to the
  limit, a closed inequality for each fixed tuple; also READ CA L1761 with L1775). With the translation modulus,
  |b(X, tau_s Y) - b(X, Y)| <= C(X, Y) sum_i ||tau_s h_i - h_i||_sharp -> 0 as s decreases to 0; extend linearly.
  Also READ CA L1769-1770: T_t is "a strongly continuous semigroup".
- (TOT) PROVED. span({1} union C) = V, and the Hilbert space of D_inf is the completion of V/N (gap-os-equiv.md (1a));
  it is the account's H(S) (READ CA L115178-115181, L115205: "its completion defines H"). So {Omega} union {[X]: X in C}
  is total.
- (H1) for the members, with m_n = M_*: Step 4 (iv) (Proposition P (c); READ gap-seed-limit-check.md L80, A10).

**Theorem E (links (e) and (f) on the tr F^2 sector). PROVED GIVEN (SEED-FP), the checked lane statements (rows 698,
699, 703), and the account's statements READ at CA L1690, L1709, L1726, L1785 (with L1692, L1724), L99150-99156.**
For every volume-first limit S at g: ker H = C Omega in H(S), and spec(H) lies in {0} union [M_*, infinity),
M_* = 2 log(1/(5041 s_*))/ell. Proof: Proposition P' (READ gap-seed-limit.md L200-202) with the six items above.
Corollary (PROVED GIVEN READ CA L1895): the map P_0[F] -> (xi -> sigma_xi(F)) is unitary from ker H onto
L^2(X, lambda) with Omega -> 1. Since ker H = C Omega, L^2(X, lambda) has dimension 1. X = supp lambda, so X is one
point, and sigma_S is its own canonical component.

What the proof does not use: (P4) for the members; totality of iota_j(C) in H_j; any bound on member constants; the
account's diagonal mirrors, rotations or O(4) clause; the account's existence clause beyond the definition of S. The
account statements it uses are conditional on the account's hypotheses (CA L1748-1751). The rate M_* is the lane's;
the account supplies only the datum and the convergence.

## Step 6. (ONE-K) as written, and the account's statements on cutoff universality

- READ gap-target-max.md L198 (row 913, 4.3): (ONE-K), ARGUED there. "(SEED-L) is an open condition on a pair of total
  masses. If the first-passage densities at consecutive cutoffs at one g satisfy, on T_ell and T_(L ell), log of the
  integral of rho_(K+1) minus log of the integral of rho_K = c_K vol + O(eps_K) with one constant c_K for both tori and
  the sum of eps_K finite, then (SEED-L) at one cutoff K_0 with margin gives (SEED-L) for every K at least K_0."
  The hypothesis is named (UNIV-K). Row 913 8.2 (L321-322) lists (ONE-K) as ARGUED.
- READ gap-finishline-opus.md L126: (SEED-L) is limsup over first-passage data of
  Phi_L := L^4 log Z_(K,ell,beta) - log Z_(K,L ell,beta) <= phi_*, phi_* < (L/2) log(13/10); Lemma FL (L128-134, ARGUED,
  not checked) turns (SEED-L) into (SEED-FP) at the size 6^(k_1) L ell.
- READ CA L1666-1667: K(beta, g) = min{k : x_k(beta) <= g^(-2) + B_sharp}; W_K(g) = {beta >= g^(-2) + B_sharp :
  K(beta, g) = K}. READ CA L1681: "The final value x_K(beta) lies in the window but is not fixed at g^(-2)."
- The account's universality statements, read in the primary text:
  (U1) READ CA L1831-1835, clause (d) "Fixed-torus uniqueness": W_K(g) lies within rho/4 of the tuned coupling;
       x^natural_K is bi-Lipschitz uniformly in K; on each torus of the family there is a family S^(ell,x), x in I, of
       connected functions on tuples with pairwise disjoint supports, and S^T_(n;K_j,ell,beta_j) -> S^(ell,x)_n whenever
       x^natural_(K_j)(beta_j) -> x, "with no passage to a subsequence". READ CA L1726: "only n >= 2 and only separated
       tuples are considered". So log Z (the case n = 0) is not covered. READ CA L99837-99839: no "matched-cutoff
       convergence rate".
  (U2) READ CA L94364-94381, Proposition "Finite-horizon exponential universality": two initial profiles H, H~ in a
       bounded ball, "the same endpoint, horizon and frozen presentation"; |x_j(H) - x_j(H~)| <= C e_j q_2^j ||H - H~||,
       ||h_j(H) - h_j(H~)|| <= C q_2^j ||H - H~||; "These constants are independent of the horizon and compatible volume."
       READ CA L94466-94468: the final effective interactions differ by at most C V q_2^N ||H - H~|| in sup norm.
       READ CA L94473-94474: "Scalar vacuum factors may differ and do not affect a normalized final law."
       READ CA L94505-94512: "a finite-volume bound on one common final domain. It is not uniform over growing volumes,
       ... No complementary-history measure has been introduced in this comparison."
  (U3) READ CA L86303-86310, (RF62), "The explicit leading vacuum requirement":
       |E_(K,ell,beta) + (3/2)(N^2-1)(L^4-1) sum_(j<K) (log x_j) N_(j+1)| <= C N_0, a requirement, not a theorem.
  (U4) READ CA L98404-98409, (ST5), a required torus hypothesis (CA L2360): Z_(a,ell)(0) >= e^(V_(a,ell) - C_- ell^4) and
       an upper bound with + C_+ ell^4. READ CA L98412: V_(a,ell) is "The source-independent vacuum number"; no
       extensivity is stated.
  (U5) READ CA L61932: E^(j), R^(j) on non-wrapping domains are values of "a single family on Z^4"; "The constant
       E_(k,S), by contrast, depends on the label and on the torus."
- Row 904 (READ FINISH.md L981) read (U2) the same way and stopped (UNIV-FP); I re-read the primary lines above myself.

## Step 7. (ONE-K): exact statement PROVED; its hypothesis (UNIV-K) OPEN; the account does not supply it

Fix g, odd L >= 25 and ell with T_ell, T_(L ell) in the account's family. For a first-passage datum d = (K, beta) put
F_d(T) = log Z_(K,T,beta) and Phi(d) = L^4 F_d(T_ell) - F_d(T_(L ell)). vol(T_(L ell)) = L^4 vol(T_ell).

**(UNIV-K), exact form.** K_0 is fixed. pi maps each first-passage datum d of cutoff K > K_0 to a datum pi(d) of cutoff
K - 1. There are eps_K >= 0 with E(K_0) := sum_(K > K_0) eps_K < infinity, and for each d one real c_d, such that
|F_d(T) - F_(pi d)(T) - c_d vol(T)| <= eps_K for both T = T_ell and T = T_(L ell).

**Lemma ONE-K. PROVED.** Under (UNIV-K), |Phi(d) - Phi(pi^(K-K_0) d)| <= (L^4 + 1) sum_(k=K_0+1)^K eps_k for every d of
cutoff K > K_0. Hence, if Phi(d_0) <= phi_* - (L^4 + 1) E(K_0) for every datum d_0 of cutoff K_0 reached by the
iterates of pi, then Phi(d) <= phi_* for every first-passage datum with K >= K_0. That is (SEED-L) for all K >= K_0,
and Lemma FL (row 837, ARGUED, not checked) then gives (SEED-FP) at the size 6^(k_1) L ell.
Proof. Phi(d) - Phi(pi d) = L^4 [F_d(T_ell) - F_(pi d)(T_ell)] - [F_d(T_(L ell)) - F_(pi d)(T_(L ell))]. The volume terms
cancel: L^4 c_d vol(T_ell) - c_d vol(T_(L ell)) = 0. So |Phi(d) - Phi(pi d)| <= (L^4 + 1) eps_K. Telescope. QED

**Three corrections to the wording of row 913.**
1. (PROVED as logic.) The chain must be named. (SEED-FP) asks for every first-passage datum with K >= K_0 (READ
   gap-finishline-opus.md L119-120), or, for one volume-first limit, for its defining sequence (READ L147). Row 913's
   "the first-passage densities at consecutive cutoffs" picks one datum per cutoff. The predecessor map pi is the
   exact form, and "one cutoff" means every datum of cutoff K_0 that the chains reach.
2. (ARGUED; the scaling input is GUIDE.) pi must match endpoints. If pi sends data with different final couplings
   x_K to one datum, (UNIV-K) compares two last-scale theories at different couplings. The account's own limits depend on
   that coupling (READ CA L1831-1835, (d)(3)). In the first-passage unit the correlation length scales like
   e^((3 pi^2/11) x_K) (GUIDE, two-loop law, row 837 1.6), and the window (g^-2, g^-2 + B_sharp] is about one block step
   wide (READ CA L1663: the increments satisfy b_k <= B_sharp; READ CA L4202: lambda_sharp (j-i) - c_5 <= x_i - x_j <= B_sharp (j-i)), so the length changes by a factor of order L
   across it (GUIDE). Phi depends on ell in correlation lengths (GUIDE). On a chain that alternates between the two ends of
   the window, |Phi(d) - Phi(pi d)| stays above a fixed positive number infinitely often, so sum eps_K = infinity.
   The natural choice is x_(K-1)(beta') = x_K(beta) for pi(d) = (K-1, beta'). READ CA L1832-1833 ((d)(1), (d)(2)): the
   windows lie within rho/4 of the tuned couplings, x^natural_K is bi-Lipschitz uniformly in K, and its limit range I
   contains [g^-2 - c' rho, g^-2 + c' rho]. Matching at the edges of the windows is a technical point I did not settle.
3. (PROVED from READ CA L1666-1667.) W_0(g) = {g^-2 + B_sharp}: K(beta, g) = 0 means beta = x_0 <= g^-2 + B_sharp, and
   W asks beta >= g^-2 + B_sharp. So K_0 = 0 would make "one cutoff" one coupling. It is not usable as it stands
   (ARGUED): matched chains cannot all end at the top of the window, and E(0) < phi_*/(L^4 + 1) < 0.131 L^(-3) asks for
   tiny eps_K from K = 1 on.

**Which account statement would supply (UNIV-K).**
- The closest is (U2), the finite-horizon exponential universality (READ CA L94364-94381). On the regular part it is
  the needed contraction (ARGUED): run d = (K, beta) one block step; at spacing a_(K-1) its density is the Wilson weight at
  x_1(beta) plus an irrelevant profile H (and large-field terms); pi(d) starts from the Wilson weight, H~ = 0. With
  matched endpoints, (U2) gives final couplings within C e_j q_2^j ||H|| and final regular interactions within
  C V q_2^(K-1) ||H|| (READ CA L94466-94468), V the number of unit cells (fixed: ell^4 or L^4 ell^4). So the regular part
  of (UNIV-K) would hold with eps_K <= C L^4 ell^4 q_2^K, which is summable, if H lies in the smaller initial-profile
  ball. I did not check that last condition.
- What (U2) leaves out, each READ in the primary text: scalar vacuum factors (CA L94473-94474), which carry both the
  volume term c_d vol and its non-extensive remainder; the large-field histories (CA L94511-94512); unnormalized masses
  (the bound is for normalized laws "on one common final domain", CA L94505-94508). In addition the account controls the
  vacuum term only to C N_0 ((RF62), CA L86303-86310) and log Z only to e^(C ell^4) ((ST5), CA L98404-98409); both are
  requirements, not theorems; and the label constant "depends on the label and on the torus" (CA L61932).
- (U1), clause (d), is cutoff universality for the connected functions with n >= 2, with no rate (READ CA L1831-1835,
  L1726, L99837-99839). log Z is the case n = 0 and lies outside it.
- So the statement that would supply (UNIV-K) is the n = 0 form of (U2): a comparison of the UNNORMALIZED total masses
  of the last-scale densities (READ SA L17285 via row 837: the integral of rho_K is Z, exactly) of two endpoint-matched
  runs one block step apart, vacuum factors and large-field histories included, on the two FIXED tori T_ell, T_(L ell),
  with a summable error. Equivalently: the n = 0 case of (d)(3) with a summable rate. No uniformity in the volume is
  needed, since both tori are fixed.

**Does it hold?** OPEN. The account does not state it, and it names the missing parts (CA L94473-94474, L94505-94512,
L99837-99839). The precision gap is the one of row 837 1.4 (ARGUED from (U3), (U4)): the account fixes Phi only to
O(L^4 ell^4), while Lemma ONE-K needs (L^4 + 1) E(K_0) < 0.131 L. GUIDE, used in no proof: under asymptotic scaling the
lattice artefacts of a free-energy defect at fixed physical size fall like a_K^2 times powers of log, which is summable.

**What (ONE-K) buys if (UNIV-K) held (ARGUED).** (SEED-FP) at all large cutoffs would follow from (SEED-L) with margin
(L^4 + 1) E(K_0) at the data of one cutoff K_0: a lattice statement on tori of 2L^(m+K_0) and 2L^(m+K_0+1) sites, at the
couplings of W_(K_0)(g). These are weak couplings (READ CA L1755 (a)(i): beta^natural_K - g^-2 lies between
c_0 K/2 - c_5 and 3 c_0 K/2 + c_5; READ CA L1832: W_K(g) lies within rho/4 of beta^natural_K). It removes the uniformity
in the cutoff, not the crux. This agrees with row 913 (READ gap-target-max.md L198: "It does not touch the crux").

## Step 8. Summary

| Statement | Mark |
|---|---|
| Lemma C (i)-(iii): every nu in G^tor_(K,beta) (a weak limit point of the periodic lifts of the bare Wilson torus measures) is a lane limit state along the symmetric integer-sided tori (N_i, N_i), on every bounded Borel local function | PROVED (Step 4), from READ CA L99078-99195, L1690 and Lemma FE (checked, row 703 A5); no hypothesis of the account |
| Lemma C (iv): under (SEED-FP) at (K, beta), such nu has a unique vacuum and transfer bound e^(-M_* a_K t), in all four directions | PROVED GIVEN Theorem S, Corollary S3' (checked, rows 698, 699) and row 703 Parts A and B (Part B was written in the check row; I found no separate check of Part B) |
| Link (c) of row 837 | PROVED (Lemma C) |
| E1, E2: the lattice versions iota_j X = prod_i (O_j(f_i) - nu_j(O_j(f_i))) are member observables, and b_j(iota_j X, tau_s iota_j Y) is exactly the centred moment of theta X-bar . tau_s Y | PROVED, from READ CA L1726, L99150-99156, L99284-99294 |
| E3: convergence of centred moments, with moving tests | PROVED GIVEN READ CA L1690, L1709, L1785 (L1692, L1724) |
| (H2), (P1), (P2), (P3) with k_F = 0, (P4), (TOT), (H1) for the account's datum | PROVED (Step 5); (P2) also uses READ CA L1757-1758 |
| Link (e) of row 837 | PROVED GIVEN the account's statements above (they are conditional on its hypotheses, CA L1748-1751) |
| Theorem E: every volume-first limit at g has ker H = C Omega and spec(H) in {0} union [M_*, infinity) on the tr F^2 sector; its canonical decomposition has one point | PROVED GIVEN (SEED-FP), the checked lane statements and the READ account statements; the last clause also READ CA L1895 |
| Lemma ONE-K: (UNIV-K) on a predecessor map pi gives abs(Phi(d) - Phi(pi d)) <= (L^4 + 1) eps_K, so (SEED-L) at the data of one cutoff with margin (L^4 + 1) E(K_0) gives (SEED-L) at all larger cutoffs | PROVED (Step 7) |
| pi must match final couplings; on unmatched chains (UNIV-K) fails | ARGUED (the scaling input is GUIDE) |
| W_0(g) is the single coupling g^-2 + B_sharp | PROVED from READ CA L1666-1667 |
| (UNIV-K) | OPEN. Would be supplied by an n = 0 form (unnormalized masses, vacuum factors, large-field histories) of CA L94364-94381 on the two fixed tori; the account does not state it (READ CA L94473-94474, L94505-94512, L99837-99839; clause (d) is n >= 2 only, CA L1726, L1831-1835) |
| Regular part of (UNIV-K), eps_K <= C L^4 ell^4 q_2^K on matched chains | ARGUED from READ CA L94364-94381, L94466-94468; the condition that the first-step profile lies in the account's smaller ball is not checked |
| Lemma FL ((SEED-L) gives (SEED-FP) at the size 6^(k_1) L ell) | ARGUED in row 837; not re-checked here |

**Not done, not verified.** No proof inside the account was read; only statements at the lines named. Lemma FL was not
re-checked. Matching of endpoints at the edges of the first-passage windows was not settled. Whether the profile after
one block step lies in the account's smaller initial-profile ball was not checked. No other model has checked this file.
Row 837 cites CA-I lines of theorem_0_complete_account_raw_I.tex; this file re-located each statement it uses in
YM4_1400.tex and cites those lines.

**What changed against row 837.** Links (c) and (e) were ARGUED there. Here (c) is a lemma on measures that needs no
hypothesis of the account, and (e) is proved from five READ statements of the account. So granted the account, (GAP) on
the tr F^2 sector follows from (SEED-FP) by a written composition (Theorem E). The one remaining input on this chain is
(SEED-FP) itself, and (ONE-K) can lower its uniformity in the cutoff to one cutoff only through (UNIV-K), which is OPEN.

RESULT: link (c) PROVED (Lemma C: every nu in G^tor_(K,beta), a weak limit point of the periodic lifts of the bare Wilson torus measures (YM4_1400 L99109-99195), is a lane limit state along symmetric integer-sided tori, with no account hypothesis, and under (SEED-FP) has a unique vacuum and transfer bound e^(-M_* t)); link (e) PROVED given the account's statements L1690, L1709, L1726, L1785 (Theorem E: with V_+ the separated tuples in {x_4>0} and iota_j X = prod(O_j f_i - nu_j O_j f_i), exact covariance makes the member pairing the centred moment, and (H2), (P1)-(P4), (TOT), (H1) hold, so every volume-first limit at g has ker H = C Omega, spec H in {0} union [M_*, infinity) on the tr F^2 sector, and one canonical component, L1895); (ONE-K) PROVED as an implication (a predecessor map matching final couplings, |Phi(d) - Phi(pi d)| <= (L^4+1) eps_K), but its hypothesis (UNIV-K) is OPEN: it would need an n = 0 form (unnormalized masses with vacuum factors and large-field histories) of the finite-horizon exponential universality L94364-94381 on the two fixed tori, which the account does not state (vacuum factors "may differ" L94473-94474, no complementary-history measure L94511-94512, clause (d) n >= 2 only and without rate), and on unmatched chains it is expected to fail (ARGUED, GUIDE scaling).
