lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T02:08Z

# gap-d2-inputs: check and rebuild of the inputs that carry lead rules (W3 of row 998)

Queue row 1000 (`gap-d2-inputs-opus`), pinned at f75650fe8. Work item W3 of `library/gap-crux-exercise3-max.md` 9.7. Research-stage working state; no status granted.

## Plan (at most eight steps; one per response)

1. Read FINISH efficiency rules, row 998, W3 text in `gap-crux-exercise3-max.md` 9.7, and grep open-core/FINISH for overlap.
2. (i) Verdict on T3 of row 982 (`gap-hcphys-max.md` L99, L177), with the line.
3. Read `gap-tiltproof-max.md` 5.2-5.3 and `gap-tiltproof-check-opus.md`; fix the exact abstract RP form and the (G1)-(G4) form Theorem D2 uses.
4. Test first: gauge-fixed crossing links and the end weights of 5.2 (do they fit the RP lemma's hypotheses?).
5. Hand proof of the reflection-positivity lemma in that abstract form (credit Osterwalder-Seiler).
6. Hand proof of Frohlich-Simon-Spencer Gaussian domination with (G1)-(G4) (credit FSS).
7. Check the consumption in 5.2-5.3 line by line against the proved statements.
8. Verdicts table and RESULT line.

## Step log

### Step 1. Brief and overlap check (done)

- Brief: W3 of `library/gap-crux-exercise3-max.md` L920-932, copied in row 1000. Statements: (i) T3 of row 982 (`library/gap-hcphys-max.md` L99, L177); (ii) the two lemmas Theorem D2 imports (`library/gap-tiltproof-max.md` 5.2, 5.3; `library/gap-tiltproof-check-opus.md`). Test first: gauge-fixed crossing links and end weights of 5.2. Stop rule: a proof, or the first failing line.
- Overlap (rule 0a): grep of `library/open-core.md`, `library/l17c.md` and FINISH for "Gaussian domination", "Frohlich-Simon", "FSS", "gap-d2", "T3 of row 982". Only hits: rows 977 and 979 (the author and the check of Theorem D2, which this row serves) and row 1000 itself. No other row rebuilds these lemmas or checks T3. Proceeding.

### Step 2. (i) Verdict on T3 of row 982

**Statement checked.** `library/gap-hcphys-max.md` L88 (table row T3), L99 (3.2 item 1), L177 (Route 1, place 1): "the account's small-field convexity (P1)-(P3), fed into Theorem BR through Lemma TEL, gives a rate short of (HC-phys) by the factor beta_K/beta_0, which tends to 0 like 1/log(1/a_iota)". Read: L1-L115, L169-L183 of that file; Theorem BR and 5.1-5.5 of `library/gap-fc-max.md` L121-L215.

**Verdict: HOLDS AFTER CORRECTION, mark stays ARGUED.** First line needing a correction: L88, "Linear count: one level-k bond moves L^(3k) fine slice links ...". The count is right, but it is done on linear functionals of the link field, and (LSI-br) (`gap-fc-max.md` L156-L158) is asked only for gauge-invariant phi. `gap-fc-max.md` 5.5 (L203-L210) shows that this restriction carries weight. The correction below redoes the count on gauge-invariant test functions and gets the same order.

The check, step by step.

(a) *The needed size (L88 first clause; Lemma CAP (c), L72).* Theorem BR returns alpha = A/2 with A = integral over an interval of length below 1/beta of alpha_s. So A/2 <= (1/(2 beta)) sup_s alpha_s. Here beta is the coefficient of the kinetic kernel e^(beta <x, w>) (`gap-fc-max.md` (B1), L130). For the Wilson action in temporal gauge, the time-like plaquette term of link l is beta_0 <x_l, w_l>, with beta_0 the bare coupling. So (HC-phys) through Theorem BR needs sup_s alpha_s >= 2 beta_0 M_H a_iota. CHECKED, by hand.

(b) *The given size, corrected count.* Linearise at the identity: the slice field is a Lie-algebra field A on the spatial links, and the benchmark of L88 is a four-dimensional Gaussian field with independent levels of stiffness beta_k. In fine lattice units, its four-dimensional transverse covariance at momentum p, with |p| between L^(-k-1) and L^(-k), is of order 1/(beta_k p^2). Restrict it to one time slice: the integral over p_0 of 1/(beta (p_0^2 + |p|^2)) gives 1/(2 beta |p|). So the slice covariance of a transverse (co-exact) mode of spatial momentum p is of order 1/(2 beta_(k(p)) |p|). A transverse linear functional f = <w, A>, with w = d^* psi and psi smooth at the unit scale, is gauge invariant in the linearised model; it is the smeared field strength. For it Var_nu(f)/|grad f|^2 is of order L^K/(2 beta_K) at |p| of order L^(-K). This is the count of L88 (||R_0 D_K||^2 of order L^K), now on a gauge-invariant function.

(c) *From nu to the bridge laws nu_s.* By (B3) (`gap-fc-max.md` L139), nu_s is the law of (1 - lam) U_0 + lam U_1 + (lam (1 - lam)/beta_0)^(1/2) xi. For X = f(U_0), Y = f(U_1) with equal variance sigma^2 and correlation rho >= 0, Var((1 - lam) X + lam Y) >= sigma^2 (1 + rho)/2 >= sigma^2/2. The benchmark has rho >= 0 for these smooth modes (time correlation about e^(-|p|); ARGUED). So alpha_s <= 2/(sigma^2/|w|^2), of order 4 beta_K L^(-K), for every s. The noise term adds variance and only lowers alpha_s. L88 skips this step; it changes a factor 2 only.

(d) *Comparison.* Given: sup_s alpha_s of order a_+ beta_K a_iota/l_unit. Needed: 2 beta_0 M_H a_iota. Ratio given/needed: (beta_K/beta_0) times a_+/(2 M_H l_unit). On the family of the account, beta_K stays in the window at fixed g and beta_0 - beta_K grows like b_0 log(l_unit/a_iota) (one loop). So the ratio tends to 0 like 1/log(1/a_iota), and the failure is on the tail of the family. That is what L177 says. The factor a_+/(2 M_H l_unit) is large when the mass is small in unit cells, so at moderate cutoffs the bound is not violated; L177 says this too. CHECKED.

(e) *What "the port alone gives no more" means.* The precise form that the argument supports: there is a law satisfying (P1)-(P3) (the benchmark, truncated to the window of (P3)) whose bridge laws, built by (B3) with the bare beta_0, have alpha_s <= C a_+ beta_K a_iota/l_unit on gauge-invariant functions. So any lower bound on alpha_s that reads only (P1)-(P3) and (B3) is short by beta_K/beta_0. Two points keep this ARGUED, not PROVED: the truncation of the Gaussian to the window is not written, and the benchmark is linearised (Lie-algebra variables, not the spheres M of Theorem BR). I do not write them; the verdict does not depend on constants.

(f) *A remark that L115 already makes, confirmed in the corrected count.* The benchmark with a running stiffness cannot itself be the slice law of a chain with kinetic coupling beta_0. In a Gaussian chain with kinetic coupling beta_0 the energy identity (Lemma CAP (a'), L68) on a linear f gives Var_nu(f)(1 - e^(-2E)) = |w|^2/beta_0. This forces slice covariance 1/(2 beta_0 |p|): no running. So the true Wilson slice law must carry the factor beta_0/beta_K in the roughness of gauge-invariant gradients, as L115 says. This does not weaken T3: T3 is about what the port can deliver, and the port does not see the transfer structure. It does mean that the rule built on T3 should read "(P1)-(P3) with Lemma TEL", not "sub-unit convexity" in general.

**Consequence for the lead rule (row 982 N2, `gap-crux-exercise3-max.md` L856).** The rule "do not queue (LSI-br) from sub-unit convexity" is supported in the narrower form: "do not queue (LSI-br) from the account's level convexity (P1)-(P3) through a level-by-level entropy bound; a route must use the transfer structure at each level (the bare kinetic coupling), which the port does not contain." Checked by Claude Opus 5.5 (high), a model other than the author (Claude Fable 5.2); same provider, so not a cross-provider check.

### Step 3. The two lemmas, in the exact form Theorem D2 uses

Read: `library/gap-tiltproof-max.md` L175-L256 (Lemma D1, Step 5); `library/gap-tiltproof-check-opus.md` L51-L103 (its Steps 3, 4) and L153 (the ported lemmas as used). Theorem D2 imports exactly two outside statements. The check (row 979) already moved the first from the Wilson-specific theorem (Osterwalder-Seiler) to an abstract criterion. I state both in a form a little more general than the check's, because 5.3 needs the reflected weight to depend on a parameter (the shift field), and the check's (RP-abs) has fixed A and C_i.

**Setting S (the slab measure mu_n of 5.1, with the shift of 5.3).** S >= 4 even, n >= 1. Sites (x_1, y_2, y_3, t) with x_1, y_2, y_3 in Z/S and t in {-n, ..., n+1}. Links: spatial links of directions 1, 2, 3 in every slice t; time-like links between t and t+1, -n <= t <= n. Each link carries U_l in SU(2), identified with the unit sphere S^3 of R^4 (quaternions), so (1/2) tr(a b^(-1)) = <a, b>. Pinned links (point mass at 1): the direction-2 and direction-3 links of slices 0 and 1, and the time-like links of layer 0 (between slices 0 and 1). All other links: normalised Haar measure. Weight exp(sum over plaquettes p of kappa_p (1/2) tr U_p), with kappa_p = beta for spatial plaquettes of slices -n+1, ..., n, kappa_p = beta/2 for spatial plaquettes of slices -n and n+1, kappa_p = beta for time-like plaquettes of layers t != 0, and kappa_p = b (any real number) for time-like plaquettes of layer 0. The plane k: the direction-1 links P(y) := U of the link from (k, y, 0) to (k+1, y, 0), y = (y_2, y_3) in (Z/S)^2, A := S^2. Sheet bonds: nearest-neighbour pairs <y, y'> of (Z/S)^2. In slice 0 the (1,2)- and (1,3)-plaquettes of plane k equal <P(y), P(y')> (their transverse links are pinned at 1), so their weight is beta <P(y), P(y')> = beta - (beta/2)|P(y) - P(y')|^2. For h: (Z/S)^2 -> R^4, Z(h) is the integral of the same weight with each sheet-bond term replaced by beta - (beta/2)|P(y) - P(y') - h(y) + h(y')|^2. So Z(0) is the normaliser of mu_n.

**Lemma RP (reflection positivity, abstract form; credit Osterwalder and Seiler 1978, and the form of Frohlich, Israel, Lieb and Simon 1978, Section 2, used by Frohlich, Simon and Spencer 1976).** Let X be a compact metric space with a finite positive Borel measure nu_+, and let theta: X -> X' be a measurable bijection onto a second copy, with nu_- := theta_* nu_+. Let I be any index set. For each i in I let a_i: X -> R be bounded measurable, and let C_(i,1), ..., C_(i,m): X -> R be bounded measurable (m fixed, not depending on i). Let c_1, ..., c_m >= 0. Put, for i, j in I,

  K(i, j) := integral over X x X' of exp( a_i(u) + a_j(theta^(-1) v) + sum over r of c_r C_(i,r)(u) C_(j,r)(theta^(-1) v) ) nu_+(du) nu_-(dv).

Then K is a positive semi-definite kernel on I: for finitely many i_1, ..., i_N and real lambda_1, ..., lambda_N, sum over p, q of lambda_p lambda_q K(i_p, i_q) >= 0, and K(i, j) = K(j, i). In particular K(i, j)^2 <= K(i, i) K(j, j).

(The check's (RP-abs) is the case where the C_r do not depend on i and a_i = A + log F_i; the form above also covers 5.3, where A and C depend on the shift field.)

**Lemma GD (Gaussian domination; credit Frohlich, Simon and Spencer 1976).** In Setting S, Z(h) <= Z(0) for every h: (Z/S)^2 -> R^4.

**Consumption.** D2 5.2 uses Lemma RP through (G1) at h. D2 5.3 uses Lemma GD and its second-order expansion. D2 5.5 uses a further instance of Lemma RP (positive type of e^(b<x,w>), b >= 0), which W3 does not list. I prove it too, as Corollary PT, because 5.5 rests on it in the same way.

### Step 4. Test first: the gauge-fixed crossing links and the end weights of 5.2 (verdict: both HOLD)

Fix the reflection theta_j in direction 2: y_2 -> 2j + 1 - y_2 (mod S), all other coordinates fixed. It fixes the two planes y_2 = j + 1/2 and y_2 = j + S/2 + 1/2 (since theta_j(j + S/2) = j + 1 - S/2 = j + 1 + S/2 mod S). Halves: Lam_+ = {y_2 in {j+1, ..., j+S/2}}, Lam_- the rest. A link is crossing if its two ends lie in different halves: exactly the direction-2 links from y_2 = j to j+1 and from j + S/2 to j + S/2 + 1, in every slice.

(T-a) *Crossing links in slices 0, 1.* They are direction-2 links of slices 0, 1, so pinned at 1. HOLDS.

(T-b) *Crossing links in slices t not in {0, 1}: the gauge fixing.* Define, for a configuration U, the gauge transformation g(U) that is 1 at every site except at the sites s_1 = (x_1, j+1, x_3, t) and s_2 = (x_1, j + S/2 + 1, x_3, t), t not in {0, 1}. Convention: U^g(l) = g(start) U(l) g(end)^(-1). With l_1 the crossing link from (x_1, j, x_3, t) to s_1, put g(s_1) := U(l_1), so U^g(l_1) = U(l_1) U(l_1)^(-1) = 1; same for s_2 with l_2 from (x_1, j + S/2, x_3, t). The sites s_1 over all (x_1, x_3, t) and the sites s_2 are pairwise distinct (S >= 4), each fixed link has exactly one gauged end, and g(s) depends only on the one crossing link that ends at s. Claims:
- *The integrand is invariant.* Every plaquette weight is gauge invariant. The pinning constraints involve only links with both ends in slices 0, 1, where g = 1. The functions read in D2 (the P(y), the slice-1 links) and the shift terms of Z(h) are functions of slice-0 links, where g = 1. HOLDS.
- *Jacobian one.* For fixed values of the crossing links, the map U -> U^(g(U)) acts on every other link by U(l) -> g(start) U(l) g(end)^(-1) with fixed group elements; Haar measure is invariant under left and right translation, so the image of the product Haar measure on the non-crossing links is the same product measure. The crossing links themselves go to 1. So integral of F(U) = integral of F(U^(g(U))) = integral of F with every crossing link of slices t not in {0, 1} set to 1, Haar on the rest. A time-like link from s_1 to slice 0 or 1 (t = -1 or t = 2) is translated on one side only; this needs the time-like links of layers t != 0 to be Haar variables, which 5.1 restores (check L55, HOLDS there). HOLDS.
- *Each reflection may use its own gauge fixing.* The fixing does not change Z(h) for any h, so the FSS step (Step 6) may apply a different fixing for each theta_j. HOLDS.

(T-c) *The straddling plaquettes.* A plaquette contains a crossing link iff it lies in a (2, mu) plane, mu in {1, 3, time}, with its direction-2 links between y_2 = j and j+1 (or j + S/2 and j + S/2 + 1). Its two direction-2 links are crossing, so equal to 1. Its other links are U_mu at y_2 = j+1 (call it C, in Lam_+) and U_mu at y_2 = j, the mirror of C. The plaquette value is (1/2) tr(C D^(-1)) = <C, D> with D the mirror link, which is theta C in the sense C(Theta U) where (Theta U)(l) := U(theta l) for links of direction other than 2 and (Theta U)(l) := U(theta l reversed)^(-1) for direction 2. So the weight is kappa_p sum over a of C^a (theta C)^a, kappa_p in {beta, beta/2} for spatial plaquettes, beta for time-like plaquettes of layers t != 0. For the time-like plaquettes of layer 0 the four links are pinned (two crossing direction-2 links of slices 0, 1 and two time-like links of layer 0): a constant. So every cross coefficient is beta or beta/2, never b: c_r >= 0 for every real b. HOLDS.

(T-d) *The end weights and the layer weight.* The couplings depend only on the slice or layer (beta/2 on slices -n, n+1; b on layer 0), and theta_j preserves every slice and layer. The pinning set (transverse links of slices 0, 1; time-like links of layer 0) is theta-invariant. Under Theta, the image of a plaquette in Lam_+ is a plaquette in Lam_- with the same coupling and the same value of (1/2) tr (for SU(2), tr U^(-1) = tr U and the trace is a class function, so orientation and base point do not matter). So the sum of the weights of plaquettes inside Lam_- is (sum inside Lam_+) composed with Theta. HOLDS.

(T-e) *Product reference.* The reference measure is the product over links of Haar or a point mass at 1. Splitting into the Lam_+ links (nu_+) and the Lam_- links, Theta maps nu_+ onto the reference on Lam_- (Haar is invariant under inversion; the pinning pattern is symmetric). The crossing links are constants after (T-b). HOLDS.

(T-f) *Direction 3.* Same with y_3 in place of y_2 (crossing direction-3 links: pinned in slices 0, 1, gauge fixed elsewhere; straddling plaquettes in (3, mu) planes, mu in {1, 2, time}). HOLDS.

So in Setting S, after the fixing of (T-b), for each theta_j the weight of Z(h) has the form of Lemma RP. The h-dependent form is (G1) of Step 6. **Test-first verdict: the gauge-fixed crossing links HOLD, the end weights HOLD (any real b). No failing line in 5.2.** This agrees with the check (`gap-tiltproof-check-opus.md` L58-L71), here redone from the definitions.

### Step 5. Lemma RP: hand proof (PROVED, by hand)

Statement: Step 3. Credit: the method is Osterwalder and Seiler (Ann. Phys. 110, 1978) for lattice gauge theory, in the abstract form of Frohlich, Israel, Lieb and Simon (CMP 62, 1978, Section 2) and Frohlich, Simon and Spencer (CMP 50, 1976). Rebuilt here; not copied.

Proof.
(1) *Absolute convergence.* Let M_a := sup over u of |a_i(u)| and |a_j|, M_C := max over r, u of |C_(i,r)(u)|, |C_(j,r)(u)|, and c := sum over r of c_r. The integrand is at most exp(2 M_a + c M_C^2), and nu_+ x nu_- is finite. So K(i, j) is finite.
(2) *Change of variables.* nu_- = theta_* nu_+, so for any bounded measurable G on X x X', integral of G(u, v) nu_+(du) nu_-(dv) = integral of G(u, theta u') nu_+(du) nu_+(du'). Hence
  K(i, j) = integral over X x X of exp( a_i(u) + a_j(u') + sum over r of c_r C_(i,r)(u) C_(j,r)(u') ) nu_+(du) nu_+(du').
This form is symmetric under (i, u) <-> (j, u'), so K(i, j) = K(j, i).
(3) *Expansion.* For real numbers, exp(sum over r of c_r s_r) = sum over multi-indices alpha in N^m of (c^alpha/alpha!) s^alpha, with c^alpha = product of c_r^(alpha_r), alpha! = product of alpha_r!, s^alpha = product of s_r^(alpha_r). Put s_r = C_(i,r)(u) C_(j,r)(u'), so s^alpha = C_i(u)^alpha C_j(u')^alpha. The series of absolute values is exp(sum of c_r |s_r|) <= exp(c M_C^2), bounded uniformly in (u, u'). So, by dominated convergence (finite measure, bounded dominating function), the sum and the integral exchange:
  K(i, j) = sum over alpha of (c^alpha/alpha!) Phi_alpha(i) Phi_alpha(j),   Phi_alpha(i) := integral over X of e^(a_i(u)) C_i(u)^alpha nu_+(du).
Here the double integral factorises because the integrand is a product of a function of u and a function of u' (Fubini; everything is bounded).
(4) *Positivity.* Each c^alpha/alpha! >= 0 because every c_r >= 0 (0^0 := 1). For real lambda_1, ..., lambda_N:
  sum over p, q of lambda_p lambda_q K(i_p, i_q) = sum over alpha of (c^alpha/alpha!) (sum over p of lambda_p Phi_alpha(i_p))^2 >= 0.
The exchange of the finite sum over p, q with the series over alpha is allowed since each series converges absolutely (|Phi_alpha(i)| <= e^(M_a) M_C^(|alpha|) nu_+(X)).
(5) *Cauchy-Schwarz.* Take N = 2, (i_1, i_2) = (i, j). The quadratic form lambda_1^2 K(i,i) + 2 lambda_1 lambda_2 K(i,j) + lambda_2^2 K(j,j) is non-negative, so its discriminant is not positive: K(i, j)^2 <= K(i, i) K(j, j). QED

No step uses compactness beyond (1); compactness of X is not needed if a_i and C_(i,r) are bounded. Lean-formalisable: finite measure spaces, a multinomial exponential series, dominated convergence, Fubini.

**Corollary PT (the positive-type step of D2 5.5; PROVED, by hand).** Let Y be a compact space with a finite positive measure rho, let f: Y -> R and x_1, ..., x_m: Y -> R be bounded measurable, and b >= 0. Let the law Q on Y x Y have density proportional to exp(b sum over r of x_r(u) x_r(u')) with respect to rho x rho. Then under Q the two coordinates have the same law, and Cov_Q(f(u), f(u')) >= 0.
Proof. The density is symmetric in (u, u'), so the marginals agree; call the common mean mu_f, and put g := f - mu_f (bounded). With Z_Q the normaliser, Z_Q E_Q[g(u) g(u')] = integral of g(u) g(u') exp(b sum over r of x_r(u) x_r(u')) rho(du) rho(du'). Steps (3) and (4) of the proof of Lemma RP apply word for word with the bounded weight g in place of e^(a_i) (those steps use only that the weight is bounded and real; positivity comes from the square): Z_Q E_Q[g(u) g(u')] = sum over alpha of (b^|alpha|/alpha!) Psi_alpha^2 >= 0, with Psi_alpha := integral of g x^alpha d rho. Since E_Q g(u) = E_Q g(u') = 0, this is Z_Q Cov_Q(f(u), f(u')) >= 0. QED
Use in 5.5: Y = the product of the free direction-1 links of one slice (the hard-pinned set), rho = m-density times Haar (m-density is positive and continuous, so rho is finite), x_r the four coordinates of each direction-1 link, f = <z, P>. The density of the hard-pinned law is m(x) m(w) e^(b <x, w>) with <x, w> = sum over links and coordinates of x_l^a w_l^a. So Cov(<z, P>, <z, P'>) >= 0 for b >= 0. This is the check's argument (`gap-tiltproof-check-opus.md` L91, "Schur products"), here with the series written out.


### Step 6. Lemma GD (Gaussian domination) and the infrared bound: hand proof (PROVED, by hand, given Lemma RP and Step 4)

Statement: Step 3, in Setting S, with beta > 0. Credit: Frohlich, Simon and Spencer (CMP 50, 1976), the reflection-and-maximiser argument; here rebuilt for the pinned slab with shifts on one sheet. The hypotheses (G1)-(G4) of the check (`gap-tiltproof-check-opus.md` L76-L84) appear below as (F5), (F7), (F3)-(F4) and (F6).

Notation. For an unoriented sheet bond b = {y, y'} pick an orientation and put grad P(b) := P(y) - P(y'), grad h(b) := h(y) - h(y'); the term |grad P(b) - grad h(b)|^2 does not depend on the orientation. N(h) := the number of sheet bonds with grad h(b) != 0. H_0 := {h: h(y_0) = 0} for a fixed site y_0. W(U, h) := the full weight of Z(h), so Z(h) = integral of exp(W(U, h)) d(reference).

(F1) *Gradient dependence and positivity.* W(U, h + v) = W(U, h) for a constant v in R^4, so Z(h + v) = Z(h) and N(h + v) = N(h). Every h is a constant plus an element of H_0. The reference measure has mass 1 and the integrand is positive, so Z(h) > 0.

(F2) *Bound and continuity.* Every plaquette term is at most |kappa_p| (|<a, b>| <= 1 on S^3), and every shifted sheet term is at most beta. So exp(W) <= C_0 := exp(sum over p of |kappa_p| + beta N_b), N_b the number of sheet bonds, uniformly in U and h. W is continuous in h for each U. By dominated convergence Z is continuous on (R^4)^A.

(F3) *Decay.* |P(y)| = 1, so |grad P(b)| <= 2 and |grad P(b) - grad h(b)| >= |grad h(b)| - 2. If D(h) := max over b of |grad h(b)| >= 2, the term of a maximal bond is at most beta - (beta/2)(D(h) - 2)^2, so Z(h) <= C_0 e^(-(beta/2)(D(h) - 2)^2).

(F4) *A maximiser exists.* Put D_* := 2 + ((2/beta) log(C_0/Z(0)))^(1/2) (C_0 >= Z(0), so the root is real). By (F3), Z(h) < Z(0) when D(h) > D_*. On H_0, |h(y)| <= S D(h) for every y (a path of at most S bonds joins y_0 to y in (Z/S)^2). So F := {h in H_0: Z(h) >= Z(0)} is closed (F2), bounded by S D_* in each coordinate, contains 0, hence compact and non-empty. Let M := max of Z on F. Then M = sup of Z over all h, by (F1) and since Z < Z(0) <= M off F within H_0.

(F5) *The reflection inequality.* Fix a reflection theta = theta_j of direction mu in {2, 3} (Step 4). For a field h define R_+ h := h on Lam_+ sheet sites and h o theta on Lam_- sheet sites, and R_- h := h o theta on Lam_+ and h on Lam_-. Claim: Z(h)^2 <= Z(R_+ h) Z(R_- h).
Proof. Work in the gauge fixing of Step 4 (T-b) for theta; it does not change Z of any field. Let X be the product of the free non-crossing links with both ends in Lam_+, nu_+ its product Haar measure (the pinned Lam_+ links are constants), Theta the configuration map of (T-c), so the Lam_- links are Theta of a copy of X, with measure Theta_* nu_+ (T-e). Split the weight W(U, h):
- Plaquettes with all links in Lam_+: A_0(u); in Lam_-: A_0 o Theta (T-d), except the sheet bonds, handled below.
- Straddling plaquettes that are not sheet bonds: kappa_p sum over a of C_p^a(u) (theta C_p^a), kappa_p in {beta, beta/2} (T-c), no h.
- Sheet bonds inside Lam_+: beta - (beta/2)|grad P(b) - grad h(b)|^2, a function of u and of h on Lam_+ sheet sites. Inside Lam_-: by the symmetry of (T-d) this equals [the same expression for the mirror bond theta b in Lam_+, with field h o theta] o Theta.
- Crossing sheet bonds {y, theta y}, y in Lam_+ (direction mu, at the two planes of theta): writing Q(y) := P(y) - h(y),
  beta - (beta/2)|Q(y) - Q(theta y)|^2 = [beta/2 - (beta/2)|P(y) - h(y)|^2] + [beta/2 - (beta/2)|P(theta y) - h(theta y)|^2] + beta sum over a of (P(y) - h(y))^a (P(theta y) - h(theta y))^a.
  P(theta y) is P(y) o Theta (direction 1 is not reversed by theta), and h(theta y) = (h o theta)(y). So the second bracket is [beta/2 - (beta/2)|P(y) - g(y)|^2] o Theta with g := h o theta on Lam_+, and the cross term is beta sum over a of C^a_(f, y)(u) (C^a_(g, y) o Theta) with C^a_(f, y) := (P(y) - f(y))^a and f := h on Lam_+.
So with f, g ranging over fields on the Lam_+ sheet sites, put a_f(u) := A_0(u) + (sheet bonds inside Lam_+ at field f) + sum over crossing y of [beta/2 - (beta/2)|P(y) - f(y)|^2], and take as the list C_(f, r) the h-free C_p^a (coefficient kappa_p) and the C^a_(f, y) (coefficient beta). All are bounded, every coefficient is >= 0, and the list length does not depend on f. Then Z(h) = (mass of the pinned point masses, 1) x K(f, g) with f = h|Lam_+, g = (h o theta)|Lam_+, K as in Lemma RP. And K(f, f) = Z(R_+ h), because the field with value f on Lam_+ and f o theta on Lam_- is R_+ h; K(g, g) = Z(R_- h) likewise. Lemma RP (5) gives the claim. QED (F5)

(F6) *Counting.* For theta as in (F5): every crossing bond {y, theta y} has R_+ h(y) - R_+ h(theta y) = h(y) - h(theta theta y) = 0, and the same for R_- h. theta maps the bonds inside Lam_+ one to one onto the bonds inside Lam_-, and R_+ h on a bond inside Lam_- has the gradient of h on the mirror bond. So N(R_+ h) = 2 N_+(h), N(R_- h) = 2 N_-(h), where N_+, N_-, N_x count the bonds with non-zero gradient of h inside Lam_+, inside Lam_-, and crossing. Hence N(R_+ h) + N(R_- h) = 2 (N(h) - N_x(h)).

(F7) *Every sheet bond is crossing for some theta.* A sheet bond of direction mu in {2, 3} between y_mu = j and j + 1 crosses the plane y_mu = j + 1/2 of theta_j in direction mu.

Proof of Lemma GD. The set of maximisers {h in F: Z(h) = M} is non-empty (F4). N takes values in {0, ..., N_b}; choose a maximiser h_* with N(h_*) least. Suppose N(h_*) >= 1 and take a bond b with grad h_*(b) != 0. By (F7) take theta with b crossing, so N_x(h_*) >= 1. By (F5), M^2 = Z(h_*)^2 <= Z(R_+ h_*) Z(R_- h_*). Both factors are positive (F1) and at most M (F4), so both equal M. By (F6), one of R_+ h_*, R_- h_* has N <= N(h_*) - N_x(h_*) <= N(h_*) - 1. Subtract its value at y_0 (F1): it is a maximiser in F with smaller N, a contradiction. So N(h_*) = 0. (Z/S)^2 is connected, so h_* is constant, h_* = 0 in H_0, and M = Z(0). So Z(h) <= M = Z(0) for every h. QED

**Remark (the single-reflection form cited at `gap-tiltproof-max.md` L203-L205).** "For a weight e^(A + theta B - sum (kappa_i/2)|C_i - theta C_i - h_i|^2) over an RP product measure, the integral is at most the geometric mean of the two integrals with (A, A), (B, B) and h = 0." With constant shifts h_i on crossing terms only, this is TRUE and follows from Lemma RP: write C_i - theta C_i - h_i = (C_i - h_i/2) - theta(C_i + h_i/2) (theta acts on the configuration, not on constants), take f := h/2 and g := -h/2 as the two indices; then K(f, f) and K(g, g) carry the shift f - f = 0 and g - g = 0. It is not what D2 uses: in D2 the shifts sit on all sheet bonds, so the iteration (F4)-(F7) is needed. The citation is harmless; the tool actually used is Lemma GD.

**Corollary IR (the infrared bound of D2 5.3; PROVED, by hand).** In Setting S with beta > 0 and any real b: for e in R^4 with |e| = 1 and p in ((2 pi/S) Z)^2, p != 0,
  G^e-hat(p) := sum over d of e^(i p d) E_(mu_n)[<e, P(0)> <e, P(d)>] <= 1/(2 beta E(p)),   E(p) := 2 - cos p_2 - cos p_3.
Proof. (i) phi(eps) := Z(eps h)/Z(0) <= 1 for all real eps (Lemma GD), phi(0) = 1. Expand the sheet term: -(beta/2)|grad P - eps grad h|^2 = -(beta/2)|grad P|^2 + eps beta <grad P, grad h> - (eps^2 beta/2)|grad h|^2. So phi(eps) = E[e^(eps X)] e^(-eps^2 c/2), X := beta sum over bonds of <grad P(b), grad h(b)>, c := beta sum over bonds of |grad h(b)|^2. |X| is bounded, so phi is smooth with derivatives under E. eps = 0 is an interior maximum: phi'(0) = E X = 0 and phi''(0) = E X^2 - c <= 0.
(ii) Summation by parts on the torus (Z/S)^2: sum over bonds of <grad P, grad h> = sum over y of <P(y), (-Lap h)(y)> and sum over bonds of |grad h|^2 = sum over y of <h(y), (-Lap h)(y)>, with (-Lap h)(y) := sum over mu in {2, 3} of (2 h(y) - h(y + e_mu) - h(y - e_mu)). (Each bond {y, y + e_mu} contributes <P(y) - P(y + e_mu), h(y) - h(y + e_mu)>; collect the terms of each P(y).)
(iii) Take h(y) := e cos(p.y). Then -Lap h = 2 E(p) h and E(p) > 0 for p != 0. So X = 2 beta E(p) T, T := sum over y of cos(p.y) <e, P(y)>, and c = 2 beta E(p) sum over y of cos^2(p.y). (i) gives 4 beta^2 E(p)^2 E[T^2] <= 2 beta E(p) sum over y of cos^2(p.y).
(iv) mu_n is invariant under the translations of (Z/S)^2 (the box is periodic and the weights and pinning are translation invariant), so g(d) := E<e, P(y)><e, P(y + d)> does not depend on y, and g(-d) = g(d). With cos a cos a' = (cos(a - a') + cos(a + a'))/2 and y' = y + d: E[T^2] = (1/2) sum over d of g(d) [A cos(p.d) + Re(e^(i p.d) sum over y of e^(2 i p.y))]. If 2p != 0 mod 2 pi, the inner sum is 0, so E[T^2] = (A/2) G^e-hat(p) (G-hat is real since g is even), and sum of cos^2 = A/2. If p in {0, pi}^2 minus {0}, cos(p.y) = +-1, E[T^2] = A G^e-hat(p) and sum of cos^2 = A. Both cases: G^e-hat(p) <= 1/(2 beta E(p)). QED
The limit n -> infinity (to the hard-pinned law) is D2 5.1, checked in row 979 (`gap-tiltproof-check-opus.md` L55-L56); it is not part of W3.

### Step 7. The consumption in D2, line by line against Steps 4-6

| D2 line (`gap-tiltproof-max.md`) | What it takes | Supplied by | Verdict |
|---|---|---|---|
| L204-L205, tool 1: "reflection positivity of the Wilson action for planes that bisect links (Osterwalder-Seiler; FILS)" | a positivity statement for the pinned, gauge-fixed, shifted slab | Lemma RP (Step 5) with Step 4 (T-a)-(T-f) | HOLDS AFTER CORRECTION of the citation (the Wilson-specific theorem does not cover pinned links, beta/2, b, or shifts; Lemma RP does). Same correction as row 979, now with a proof. |
| L204-L205, tool 2: FSS single-reflection form, "geometric mean ... with (A, A), (B, B) and h = 0" | as stated | Remark in Step 6 | TRUE as stated (constant shifts on crossing terms only), PROVED from Lemma RP. Not the form D2 uses. |
| L216-L222 (5.2): crossing links pinned in slices 0, 1 and gauge fixed elsewhere; straddling plaquettes kappa <C, theta C>; end weights beta/2; layer b; directions 2 and 3 | (T-a)-(T-f) | Step 4 | HOLDS, for every real b |
| L224-L226 (5.3): Z(h) <= Z(0), shifts on sheet bonds only, all in directions 2, 3 | Lemma GD | Step 6, (F1)-(F7) | HOLDS (beta > 0) |
| L226-L227: "The first-order term vanishes (E P = 0, D1)" | E X = 0 | Corollary IR (i): forced by the interior maximum | HOLDS; E P = 0 is not needed for the inequality, only to read E X^2 as a variance |
| L227-L228: G^e-hat(p) <= 1/(2 beta E(p)), p != 0 | second-order expansion | Corollary IR (ii)-(iv), both cases 2p != 0 and p in {0, pi}^2 | HOLDS |
| L229: "passes to n -> infinity ... for every b in [0, beta]" | limit of finitely many expectations | D2 5.1 (row 979 check), not rebuilt here | not in W3; Lemma GD holds for every real b |
| L235-L237 (5.5): Cov(<z, x>, <z, w>) >= 0 for b >= 0 | positive type of e^(b<x,w>) | Corollary PT (Step 5) | HOLDS |
| L240 "(also Q_8, 2T)" | the same tools for finite subgroups | Steps 4-6 use only: links in S^3 with (1/2) tr(a b^(-1)) = <a, b>, an invariant probability on the group (Haar or counting), tr U^(-1) = tr U, |P| = 1 | HOLDS for Q_8 and 2T with counting measure |

**First failing line: none.** Theorem D2's two imported lemmas are now rebuilt in this file with hand proofs. D2 stays "PROVED, checked by one same-provider model (row 979)", now with its inputs rebuilt; its arithmetic for sides 12, 16, 120 stays ARGUED (floating G_S), as row 979 says. Not done here: D2 5.1 (Jentzsch limit), 5.4, the numbers; Theorem D2's consequences in rows 970, 977 (Corollary CAP, QUOT-CAP).

### Step 8. Verdicts

| Item | Statement | Verdict | Mark |
|---|---|---|---|
| (i) | T3 of row 982 (`gap-hcphys-max.md` L88, L99, L177): (P1)-(P3) through Lemma TEL into Theorem BR is short by beta_K/beta_0 | HOLDS AFTER CORRECTION: redo the count on gauge-invariant (transverse) test functions, since (LSI-br) is restricted to them; slice covariance 1/(2 beta_K |p|) gives the same order; one bridge-mixing factor 2 (Step 2 (b), (c)) | ARGUED (benchmark linearised; window truncation not written) |
| (i') | the lead rule on T3 (row 982 N2) | supported only in the narrower form of Step 2: no (LSI-br) from the account's level convexity through a level-by-level entropy bound | ARGUED |
| (ii-a) | Lemma RP, abstract form with a parameter (Step 3) | PROVED by hand (Step 5); Corollary PT too | PROVED, checked by no one |
| (ii-b) | Lemma GD in Setting S, with (G1)-(G4) as (F1)-(F7) | PROVED by hand (Step 6), given Lemma RP and Step 4; Corollary IR too | PROVED, checked by no one |
| test-first | gauge-fixed crossing links and end weights of D2 5.2 | HOLD (Step 4), any real b | PROVED |

Provenance: Claude Opus 5.5 (high), Mac mini worker 2, one session, no subagents, no numeric run, no computer step in any proof. T3 was written by Claude Fable 5.2 (row 982); this verdict is one reading by a different model of the same provider, not a cross-provider check. Lemmas RP and GD and Corollaries PT, IR are new text here and are checked by no one; the literature rule asks for a check by another provider before they count as closed. Credit: Osterwalder and Seiler (1978); Frohlich, Israel, Lieb and Simon (1978); Frohlich, Simon and Spencer (1976); the setting and the reduction are row 977 (Claude Fable 5.2) and its check row 979 (Claude Opus 5.5).

What it changes: rows 970, 977 and the rule against supremum forms now rest on hand-proved inputs (subject to one cross-provider check of this file). Row 982 N2 should be reworded to the narrower form of Step 2 (lead's edit).

RESULT: Row 1000 (Claude Opus 5.5 high, Mac mini worker 2; checked by no one; no numeric run). (i) T3 of row 982 HOLDS AFTER CORRECTION, stays ARGUED: the beta_K/beta_0 shortfall of (P1)-(P3) via Lemma TEL into Theorem BR is confirmed once the count is redone on gauge-invariant transverse modes (slice covariance 1/(2 beta_K |p|), same order; bridge factor 2), so the N2 rule holds only in the narrower form "not from the account's level convexity through a level-by-level entropy bound". (ii) PROVED by hand, unchecked: Lemma RP (abstract reflection positivity with a parameter, credit Osterwalder-Seiler, FILS) with Corollary PT (positive type of e^(b<x,w>), D2 5.5), and Lemma GD (Frohlich-Simon-Spencer Gaussian domination on the pinned slab, (G1)-(G4) as (F1)-(F7)) with Corollary IR (G-hat(p) <= 1/(2 beta E(p))); the test-first items, gauge-fixed crossing links and end weights of D2 5.2, HOLD for any real b; first failing line in D2 5.2-5.3 and 5.5: none; the cited single-reflection FSS form is true but not the one used. Open: a cross-provider check of this file; D2 5.1, 5.4 and the floating G_12, G_16, G_120 stay as row 979 left them.
