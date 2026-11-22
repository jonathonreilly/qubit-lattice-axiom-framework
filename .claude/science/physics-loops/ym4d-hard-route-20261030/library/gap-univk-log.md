lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T01:30Z

# gap-univk-log (queue row 1395): the logarithmic two-cutoff comparison (LOG)

Started 2026-11-22T13:30Z (date -u), pinned at commit baeb4c8ad, branch claude/ym4d-hard-route.
Research-stage working state; nothing here is a public claim.

## 0. Plan (written before any reading beyond the queue row)

1. Read row 1391 (library/gap-univk-rate-fable.md sections 4 to 7) and check 1392
   (library/gap-univk-rate-check-astra62.md): the exact statement (LOG), its consumer
   (Theorem T / T*, row 1332; row 1391 section 6.4), examples and ranked defects.
2. Read rows 1233 and 1242 (zero-source stop comparison, Lemma 3.5, identification term D).
3. Read the Sussman-Alpoge sources at the anchors named by the row (YM4_1400 stop
   comparison L130223-130770; CA-III 9.1 and zero-source corollary near 17912-18217;
   re-filed geometric comparison 63225-63288). Port proved steps, do not redo them.
4. State (LOG) precisely with the scalars a_A/a_B and vacuum terms on T_ell and T_(L ell).
5. Attempt: prove or refute. Record each failing term with its scope.
6. State which loss each outcome pays; end with the next two rows.

Steps are appended below as they are completed.

## 1. Repo search and prior work (written 13:45Z by date -u)

Search inside this lane folder only (`origin/main` and the PR branches are not refs in this checkout; check 1392 ran the five-ref search for (UNIV-K), two-cutoff comparison and matched cutoff on 2026-11-22 and found no cutoff rate for the bare masses, `library/gap-univk-rate-check-astra62.md` L5-L8).

- `library/open-core.md`: zero hits for (LOG), (REL), chessboard, log-convex, Harnack, Borel-Caratheodory, Renyi, Bogoliubov.
- FINISH rows with (LOG): 1391 and 1395 only. (REL): row 1391 (Observation REL, `library/gap-univk-rate-fable.md` 7.2b) and check 1392 (HOLDS in its smallness regime; "exactly" fails).
- On file and used below, not redone: row 1233 Lemma 3.5 and Proposition 3.7 with check 1242 (the decomposition Phi = P_9 + Delta H + D, the scalar counterexample, the telescoped bound with 2 eta_H + sigma); row 1391 Lemma SLACK, Remark 7.1, Observation REL; check 1392 (the extremal absolute-to-log loss log min(Q_v, 1 + eps Q_v); the proposals "|P - Q| <= C v e_K min(P, Q)" and "a uniform bound on the actual log derivative along a common real interpolation").
- Chessboard estimates: rebuilt in this folder as Lemma CB of `library/gap-s1-opus.md` 3.2 (row with RESULT at L670; credit Frohlich, Israel, Lieb and Simon 1978; reflection positivity of the Wilson action: Osterwalder and Seiler). No file in the (UNIV-K) family (gap-univk-opus, gap-univk-check-astra, gap-mini-solve-u-opus, gap-onek-check-astra, gap-univk-rate-fable, its check) uses a chessboard estimate or a convexity argument (grep, zero hits for "chessboard"; "convex" zero hits). FINISH L47 (rarity-fresh) records an earlier negative: "centre-plane chessboard fails on the class branch"; Step 6 below meets the same kind of obstruction (tile-locality) and names it.
- Log-convexity is used on file only for the cylinder limit of row 844 (Lemma W), a different object.
So the two tools of Steps 4 and 5 (a convexity or zero-free upgrade of an absolute bound on a long parameter segment; the chessboard lower bound for "no defect anywhere") are not on file for the two-cutoff comparison. Both are classical; nothing below claims a new inequality, only its use here.

## 2. What the account's comparison gives, in the form used below (written 13:45Z by date -u)

Sources: Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the complete account part III at 31a47c543775 ("III n" is a line of LOCAL:ym4d-papers/sa-ca) and YM4_1400.tex ("Y n", LOCAL:ym4d-papers/sa1400). Their construction ports Balaban (CMP 119, CMP 122). READ in this row: III 11804-11990, 17425-17500, 17956-18040, 18120-18330; Y 130223-130512. Standing in the account: III 9.1 is a theorem conditional on its hypotheses (one of them outstanding, check 1242 L74); in Y the same text is a sketch under the header "The interacting estimates themselves remain hypotheses" (row 1391 2.1).

**2.1 Objects (READ III 11812-11905, 11955-11990; Y 130458-130473).** Run A has length n, run B length n+1, matched real centres, zero residual source. The last lattice has N_w = 2L^(m_0+w) sites per side, w = w(g). Each run has a normalised stop integral
  Z~^c = sum over labels h in H^c of tau^c_h(V_w),
with tau^c_h "the h-th term chi T^w e^(A^w - E^c) of that expansion, read as a complex Borel measure" (III 11857-11860), and tau^c_h = P_h[x^c]: "one assembly formula P_h, carrying no run index, applied to the array x^c of the run's stored numbers" (III 11955-11959). The integrand that P_h assembles "is entire in the entries of the array" (III 17441) and each label has a chart with "a reference measure independent of the dial parameter" (III 11905-11907). The vacuum constants of the run are entries of the array: "the pieces that do not depend on z but depend on the run, namely the vacuum constants, the z-pieces [...] and the pieces s^0, D^0 of the real object" (III 11972-11974).

**2.2 The estimate (READ III 17956-17976, 17466-17472, 18136-18154; Y 130251-130274, 130330-130347).** With A^sharp = e^(E_+^sharpsharp N_w^4) the majorant,
  sum_(h aligned) ||tau^B_h - tau^A_h|| + sum_(h in H^A not aligned) ||tau^A_h|| + sum_(h in H^B not aligned) ||tau^B_h|| <= eps_n A^sharp,
  eps_n = 4 E_1^-1 Sigma_k^(q_a) + 4 q_a^(k - n_c) + C_test theta_chi^k <= C_TC(g, N_w)(rho^(n-w) + Pi_n),
and the modulus bound behind it: on the dial domain D*, for every integer a >= 0 and |mu| <= q_a^-a,
  sum_(h aligned) |mu|^(m_a(h)) ||tau_h[x^(lambda, eps); t^A]|| <= A^sharp     (III 17466-17472),
m_a(h) the number of live components of h of age at least a. "The side N_w of the last lattice enters C_TC only through the term of C_test that carries N_w^4. The majorant A^sharp carries the factor e^(E_+^sharpsharp N_w^4). Thus the rate e_w [...] is free of the volume, while the constant is not" (III 18122-18126). One-run bounds: 1/B <= Z~^c(0) <= A, A = e^(E_+^sharp N_w^4), B = e^(C_low N_w^4) (row 1233 L77, III 21073).

**2.3 The three parts of eps_n, and which labels they concern (READ; used in Steps 4-7).**
 (a) Aligned labels at fixed ramps: the first variation in the directions (b, t), b a birth zone and t in [b, k] a read level; each direction has a disc of radius E_1/l_b, l_b the load of the zone. For an old zone, a = (k-b-1)_+ > 0, "Terms that read no slot of that direction are constant on the disc. Subtract the sum over those insensitive labels" and "the incidence check gives m_a(h) >= 1 on each remaining label" (Y 130253-130259): only labels with a live component of age at least a read the zone. Their absolute mass is at most A^sharp q_a^a by the multiplier.
 (b) Labels that are not aligned: first index at most n_c (a live component of age at least k - n_c; these include the labels of B alone, first index 0, III 11938-11942), cost 4 q_a^(k-n_c) A^sharp; and common labels of first index above n_c with alignment functional above 1/80, inside the ramp lemma.
 (c) The ramp move: C_test theta_chi^k A^sharp, with C_test of order N_w^4 ("at most N_w^4 slots on the last lattice", Y 130290).
Every term is (a small number) times the majorant A^sharp. Remark 7.1 of row 1391 and check 1392 (L58) show that the passage to logarithms then costs log min(Q, 1 + eps Q), Q = A^sharp B = e^(c N_w^4).

## 3. The scalars and the common extensive subtraction (written 13:45Z by date -u)

Notation. For a function f of the torus put Delta f := L^4 f(T_ell) - f(T_(L ell)). Z^c_T is the Wilson integral of run c on T with product probability Haar measure. Phi of Theorem T is Delta log Z at one datum; the increment that (UNIV-K), Lemma SLACK and (A1*) read on the edge from A = (K-1, beta') to B = (K, beta) is
  I_K := Phi_ell(K, beta) - Phi_ell(K-1, beta') = Delta [ log Z^B - log Z^A ].

**3.1 Lemma SC (the scalar identity). PROVED (algebra); it restates check 1242 L52-L64 for one edge.** Let kappa^c_T > 0 be any scalars and Z~^c_T := kappa^c_T Z^c_T. Then
  I_K = Delta [ log Z~^B - log Z~^A ] - Delta [ log kappa^B - log kappa^A ].
If on each of the two tori | log Z~^B_T - log Z~^A_T | <= C vol(T) e_K with the same C (vol in any unit common to both tori), then | I_K + Delta[log kappa^B - log kappa^A] | <= 2 L^4 C vol(T_ell) e_K.
Proof. log Z^c = log Z~^c - log kappa^c, and Delta is linear. For the bound: L^4 C vol(T_ell) e_K + C vol(T_(L ell)) e_K and vol(T_(L ell)) = L^4 vol(T_ell). QED

So (LOG) of row 1391 5.5 is two statements, and no estimate on normalised integrals touches the second:
 (LOG-N) | log Z~^B_T - log Z~^A_T | <= C N_w(T)^4 e_K on T_ell and T_(L ell), same C, for one fixed rule that assigns the scalars kappa^c_T;
 (LOG-S) the scalar term s_K := - Delta [ log kappa^B - log kappa^A ] for that same rule.
The "common extensive subtraction c vol(T)" of (LOG) is the part of log kappa^A_T - log kappa^B_T that is exactly proportional to vol(T); it cancels in Delta whatever its size.

**3.2 What the account fixes about kappa (READ).** III 18234-18255: "The normalisation admits exactly one free positive constant for each run and each centre", constrained only by Z~^c(0) in [1/B, A] ("A subtraction made once for each length [...] would put Z~^c(0) outside the interval [1/B, A]"). Y 130405-130413: I_k(0) = e^(-E_(k)) Z(0) with "E_(k) the source-independent vacuum constant", and Y 130459-130464 "choose one positive scalar a_c for each run and real center, in the one-run vacuum normalization". So kappa^c_T = a^c_T e^(-E^c_(k_c)(T)), and the constraint pins log kappa^c_T only up to +-(E_+^sharp + C_low) N_w^4. That freedom is extensive with an O(1) density. Check 1242's counterexample (L58) uses exactly it. Consequence, PROVED by that counterexample: (LOG-S) is not implied by any statement about the normalised integrals; a rule for kappa has to be part of the hypothesis.

**3.3 Proposition SC2 (the rule that makes (LOG-S) a telescoping wrapping term). PROVED GIVEN (V1)-(V2); it is check 1242 L34-L39 and L60-L64 read for the scalar alone.** Fix the rule
  (RULE) kappa^c_T := exp(-H^c_T), H^c_T := sum over the levels j of run c (all levels, not only those before the stop) of sum over X in D^(j)(T) of h^c_j(X),
the run's own full vacuum counterterm (check 1242's S_8 = e^(-H_T) Z^bare; then its term D is zero by definition). Assume
 (V1) for a domain X that does not wrap the torus, h^c_j(X) depends only on the lift of X and on the run's data (bare coupling and number of steps), not on the torus (the account's 8.22(a)-(c) and its torus-independence lemma, check 1242 L75);
 (V2) the wrapping domains obey the bound of row 1233 Lemma 3.6: | Delta H^c | <= eta_V(m) for every run c, with eta_V(m) = V_(m+1) 2(E_0+1) K_* e^kappa sum_(u>=0) L^(4u) exp(-kappa L^(m+u)/(4M)).
Then: (i) H^c_T = c^c vol(T) + W^c_T with c^c free of the torus and Delta H^c = Delta W^c; (ii) s_K = Delta H^B - Delta H^A; (iii) along any chain of edges d_0, ..., d_K the scalar terms telescope: sum of s_j = Delta H(d_K) - Delta H(d_0), at most 2 eta_V(m) in absolute value, which tends to zero faster than any power of 1/ell.
Proof. (i) Let c^c be the density on the infinite lattice: the sum, over the levels and over the finite domain shapes rooted in one unit cell, of the common value that (V1) gives (absolutely convergent by the decay that (V2) rests on). On T the nonwrapping domains of one shape are its translates, vol(T) per unit cell, each with that value. So H^c_T - c^c vol(T) =: W^c_T is the sum over the wrapping domains of T minus vol(T) times the density of the shapes too large to embed in T. These are the "two wrapping tails per root" of check 1242 L34, and (V2) is the bound on Delta W^c. Delta(c vol) = 0. (ii) is 3.1 with log kappa = -H. (iii) the intermediate data occur with opposite signs; (V2) bounds the two ends. QED
Remarks. (1) The common subtraction c vol(T) of (LOG) is (c^B - c^A) vol(T). It is not small: run B has one more bare level, whose vacuum density per physical volume is of order L^(4K). Only its exact proportionality to vol(T) is used. (2) (iii) is one-cutoff in form: the scalar terms are not claimed summable edge by edge (check 1242 L64 has the alternating example). The consumer of row 1391 (Lemma S1, Proposition S2(d), Lemma SLACK) reads a tail defect, so a telescoped term 2 eta_V(m) is enough: apply Lemma SLACK to Phi' := Phi - Delta H (that is, to Delta log Z~) and add 2 eta_V(m) once. (3) What (RULE) costs: (LOG-N) must then be proved for these representatives, that is, with the vacuum constants of all levels of each run inside the compared objects. In III 9.1 the run-dependent vacuum constants are slots of the array (2.1), so their run-to-run differences are marks with loads; whether the representative of III 9.1 is the one of (RULE) is the question D of check 1242 and is NOT decided here (the account's text leaves the constant free, 3.2).

Status of Step 3: the scalars a_A/a_B and the vacuum terms are tracked exactly; they reduce to (RULE) + (V1) + (V2), all on file as hypotheses from check 1242, and they cost the consumer 2 eta_V(m), decreasing in ell. The rest of this file is about (LOG-N).

## 4. First tool: an absolute bound on a long parameter segment gives an extensive logarithmic bound, if the family is log-convex or zero-free (written 13:47Z by date -u)

The account's absolute estimates hold on dial discs that are long: radius E_1/l_b in the interpolation parameter, with l_b small for the zones close to the stop. Remark 7.1 of row 1391 used the estimate at the two end points only. The next statements use the whole disc.

**4.1 Theorem A (one segment). PROVED (elementary); unchecked.** Let Lambda be real.
 (cvx) Let S > 0 and phi : [-S, 1+S] -> R be convex with phi(-S) <= Lambda and phi(1+S) <= Lambda. Put d(x) := Lambda - phi(x). Then d >= 0 on the segment and
   d(0) / (1 + 1/S) <= d(1) <= d(0) (1 + 1/S).
 (zf) Let R > 1 and Z be holomorphic and without zeros on the open disc D(0, R), with |Z| <= e^Lambda there. Put d(x) := Lambda - log|Z(x)|. Then d >= 0 and
   d(0) (R-1)/(R+1) <= d(1) <= d(0) (R+1)/(R-1).
In both cases | phi(1) - phi(0) | = | d(0) - d(1) | <= d(0) (gamma - 1), with gamma = 1 + 1/S, respectively gamma = (R+1)/(R-1) (phi := log|Z| in case (zf)).
Proof. (cvx) A convex function on a segment is at most the larger of its end values, so d >= 0. Slopes of a convex function increase: phi(1) - phi(0) >= [phi(0) - phi(-S)]/S >= -d(0)/S, so d(1) <= d(0)(1 + 1/S); and phi(1) - phi(0) <= [phi(1+S) - phi(1)]/S <= d(1)/S, so d(0) <= d(1)(1 + 1/S). (zf) Z has no zero on a simply connected domain, so log|Z| is harmonic there and d is a nonnegative harmonic function on D(0, R). Harnack's inequality on D(0, R'), 1 < R' < R, at the point 1, and R' -> R. QED

**4.2 Theorem B (a chain of segments). PROVED (induction on 4.1); unchecked.** Let phi_1, ..., phi_n be real functions, each as in 4.1 (cvx) with its own S_i, or of the form log|Z_i| with Z_i as in 4.1 (zf) with its own R_i, all with the same Lambda, and phi_(i+1)(0) = phi_i(1). Put gamma_i as in 4.1, Gamma := prod gamma_i, d_0 := Lambda - phi_1(0). Then
   - d_0 (Gamma - 1) <= phi_n(1) - phi_1(0) <= d_0 (1 - 1/Gamma).
In particular | phi_n(1) - phi_1(0) | <= d_0 (e^sigma - 1), sigma := sum_i log gamma_i <= sum_i 1/S_i (cvx), <= sum_i 2/(R_i - 1) (zf).
Proof. With d_i := Lambda - phi_i(1): d_i / d_(i-1) lies in [1/gamma_i, gamma_i] by 4.1, so d_n lies in [d_0/Gamma, d_0 Gamma], and phi_n(1) - phi_1(0) = d_0 - d_n. QED
What is new against Remark 7.1 and Observation REL of row 1391: no lower bound is asked at the intermediate points, no smallness condition of the form (constant) e^(c N^4) eps <= 1/2, and no relative majorant. The only volume-dependent quantity is d_0 = Lambda - phi_1(0), the logarithm of (majorant)/(mass of run A), and it enters linearly.

**4.3 Corollary (extensive form). PROVED from 4.2.** If e^Lambda = A^sharp = e^(E_+^sharpsharp N_w^4) and e^(phi_1(0)) >= 1/B' = e^(-C' N_w^4), then | phi_n(1) - phi_1(0) | <= (E_+^sharpsharp + C') N_w^4 (e^sigma - 1), and for sigma <= 1 this is at most 2 (E_+^sharpsharp + C') N_w^4 sigma. The condition sigma <= 1 does not involve the torus when the radii S_i, R_i do not.

**4.4 Remark (some structural hypothesis is necessary; three examples). PROVED (substitution).** Let 0 < m < M, Q := M/m, R > 1.
 (E1) Z(x) = m + (M - m) x/R. Holomorphic, |Z| <= M on D(0, R), Z(0) = m, positive on [0, 1]. log Z(1) - log Z(0) = log(1 + (Q-1)/R). It has a zero at x = -R/(Q-1), inside the disc when Q > 2.
 (E2) Z(x) = m + (M - m) x^2/R^2. Holomorphic, |Z| <= M on D(0, R), positive on the whole real axis. log Z(1) - log Z(0) = log(1 + (Q-1)/R^2). It has zeros at +-i R (Q-1)^(-1/2), inside the disc, and log Z is not convex on [-R, R] (it is concave where x^2 > R^2/(Q-1)).
 (E3) Z(mu) = m + mu M q, 0 < q < 1: linear with nonnegative coefficients, |Z| <= m + M on |mu| <= 1/q; the fraction of Z(1) carried by the second term is M q/(m + M q), close to 1 when q > 1/Q.
With Q = e^(c N^4), (E1) and (E2) show that a bound by a majorant on a disc of radius R, together with positivity on the real axis, does not give a logarithmic bound of order N^4/R: the loss is c N^4 - 2 log R until R exceeds Q^(1/2). So Theorem A cannot drop both (cvx) and (zf). (E3) is used in Step 5.

**4.5 Lemma EXP (a sufficient structure for (cvx)). PROVED (Holder).** Let (Omega_h, mu_h), h in a countable set, be measure spaces with mu_h >= 0, f_h >= 0 and w_h real measurable, and Z(x) := sum_h integral f_h e^(x w_h) d mu_h finite on an interval J. Then log Z is convex on J.
Proof. On the disjoint union of the Omega_h, Z(x) = integral f e^(x w). For a, b in J and 0 < t < 1, Holder with exponents 1/(1-t), 1/t gives Z((1-t)a + tb) = integral (f e^(aw))^(1-t) (f e^(bw))^t <= Z(a)^(1-t) Z(b)^t. QED
So (cvx) holds along a direction whenever, at real arrays and zero source, every label term is a nonnegative density on the label's common chart whose dependence on the interpolation parameter of that direction is through a real exponent that is affine in the parameter.

**4.6 Lemma RENYI (a form with no labels). PROVED (power means).** Let rho_A, rho_B be positive densities on one measure space, Q := integral rho_A, P := integral rho_B, nu_A, nu_B the normalised measures, c real, r := e^(-c) rho_B/rho_A, and S > 0. Then
   c - (1/S) log E_(nu_A)[ r^(-S) ] <= log(P/Q) <= c + (1/S) log E_(nu_B)[ r^S ].
Proof. e^(-c) P/Q = E_(nu_A)[r] >= (E_(nu_A)[r^(-S)])^(-1/S) by Jensen for x -> x^(-S). e^c Q/P = E_(nu_B)[1/r] >= (E_(nu_B)[r^S])^(-1/S) the same way. QED
S -> 0 is the Gibbs (Jensen) inequality; S -> infinity is the pointwise density bound (DENS-K) of row 924. If the moments of order S = 1/e_K obey log E[r^(+-S)] <= C_1 vol, then |log(P/Q) - c| <= C_1 vol e_K. So an extensive moment bound of order 1/e_K for the density ratio suffices; (DENS-K) is the case of all orders. On the upper side it is the case x = 1 + S of 4.1 (cvx) for the family integral rho_A^(1-x) rho_B^x, which is log-convex by Holder for every pair of positive densities. I record it because it is strictly weaker than (DENS-K) and needs no structure; I did not find a way to feed it from the account's label estimates (the label measures of the two runs can be mutually singular on V_w, III 11895-11900, so there is no common density there).

**4.7 What the account supplies for 4.2, and what it does not (READ for the first sentence; the rest ARGUED).** Supplied, given the hypotheses of III 9.1: the majorant. On the dial domain the aligned sum is bounded by A^sharp (2.2), "holomorphic in eps and continuous in lambda" (III 17436), jointly holomorphic "wherever the total dial of every slot stays at most 2 E_1" (III 17456-17458); the disc of a direction (b, t) has radius E_1/l_b (Y 130251-130253). Not supplied: (cvx) or (zf). The account states that the integrand is "entire in the entries of the array" (III 17441) and takes total variations with "arbitrary bounded Borel phases"; I found no statement in III 11804-18330 that the aligned terms are nonnegative at real arrays and zero source, or that the array enters through exponents only. So the structural hypothesis is
 (STR) along each segment of a fixed path from x^A to x^B in the dial domain (at zero source, real centres), the restricted aligned sum of Step 6 is either positive with convex logarithm on the real segment [-S_i, 1+S_i], or without zeros on the complex disc of radius R_i.
(STR) is a statement about one assembly formula and real arrays. It is not a two-run estimate and it is not equivalent to (LOG): it carries no rate (it holds for a family that does not depend on x at all, and for the exponential families of 4.5 with any loads).
Which directions 4.2 can pay for. For a direction with load l_b the factor is gamma - 1 of order l_b/E_1. The account's own sum is age-weighted: Sigma_k^(q_a) = sum_b (k-b+1) q_a^((k-b-1)_+) l_b, and the loads of old zones are not small by themselves (the two runs differ at order one near their bare ends; the weight q_a^(k-b-1) is what makes the old zones harmless). Theorem B gives the unweighted sum. So Theorem B pays for the recent zones only, b > k - a_0, and the old zones have to be removed first. That is Step 5: old zones are read only by labels with an old live component (2.3(a)), and those labels are rare.

## 5. Second tool: rare labels. The majorant cannot bound their share; a chessboard estimate can (written 13:48Z by date -u)

**5.1 Remark (the absolute rarity bound says nothing about the share). PROVED by (E3) of 4.4.** The account bounds the labels that are not aligned, and the labels that read an old zone, by A^sharp q_a^a in absolute mass (2.3). Their share of the mass of the run is that number divided by Z~ >= 1/B, so the bound on the share is A^sharp B q_a^a, which is below 1 only when q_a^a < e^(-c N_w^4). (E3) satisfies the multiplier bound sum_h |mu|^(m(h)) |tau_h| <= m + M on |mu| <= 1/q with all terms positive, and has share M q/(m + M q). Log-convexity in log mu does not help: it bounds the mean number of old components by log(A^sharp B)/log(1/q^a) = c N_w^4/(a log(1/q_a)), a density of order 1/a, not q_a^a. So for the rare labels the needed input is of a different kind from Step 4: a product (independence-like) structure over the volume.

**5.2 Theorem C (no defect anywhere, from the chessboard estimate). PROVED GIVEN (CB); (CB) is the classical chessboard estimate (Frohlich, Israel, Lieb, Simon 1978), rebuilt in this folder for a two-direction base as Lemma CB of `library/gap-s1-opus.md` 3.2; its four-direction torus form is cited here, unchecked.** Let nu be a probability measure, T a finite set of N tiles, A_t the algebra of bounded functions of the fields of the closed tile t, and theta_t : A_0 -> A_t unital, linear, multiplicative maps (the reflections), with
 (CB) nu( prod_t theta_t f_t ) <= prod_t [ nu( prod_s theta_s f_t ) ]^(1/N) for all f_t >= 0 in A_0.
Let E be an event of A_0, E_t := theta_t E, p := nu( all E_t )^(1/N), G := (no E_t occurs). Then
 (i) nu( E_t for all t in S ) <= p^|S| for every S;
 (ii) nu(G) >= (1 - p)^N, so 0 <= -log nu(G) <= N p/(1 - p);
 (iii) nu(G^c) <= N p.
Proof. (i) f_t = 1_E on S and 1 elsewhere. (iii) from (i) with |S| = 1. (ii) Put f^1 = 1_E, f^0 = 1 - 1_E. Then 1 = nu( prod_t theta_t (f^0 + f^1) ) = sum over s in {0,1}^T of nu( prod_t theta_t f^(s_t) ) <= sum_s prod_t ||f^(s_t)|| = ( ||f^0|| + ||f^1|| )^N, with ||f|| := nu(prod_s theta_s f)^(1/N). Here ||f^1|| = p and ||f^0|| = nu(G)^(1/N). So nu(G)^(1/N) >= 1 - p. QED

**5.3 Corollary C2 (the N-th root removes the exponential volume constant). PROVED from 5.2.** If nu( all E_t ) <= Q pi^N with Q <= e^(C_s v N), v the number of last-lattice sites per tile, then p <= e^(C_s v) pi, a number free of the torus. So an ABSOLUTE bound with the stability constants A^sharp B = e^(c N_w^4), applied to the one event "a defect in every tile", gives the extensive bound -log nu(G) <= 2 N e^(C_s v) pi as soon as e^(C_s v) pi <= 1/2, a floor that does not involve the torus.

**5.4 Remark (Peierls upper bounds alone do not give (ii)). PROVED (example).** Let exactly k = pi N of N sites be defective, the set uniform. Then nu(defects on S) = prod_(i<|S|) (k-i)/(N-i) <= pi^|S| for all S, and nu(G) = 0. So 5.2(ii) uses the mixed products of (CB), not only 5.2(i).

**5.5 Several tilings (straddling events). PROVED for the union bound; the floor-free form NOT OBTAINED.** Let tilings tau = 1, ..., J each satisfy (CB), with events E^tau, norms p_tau and N_tau tiles, and G := no E^tau_t for any tau, t. Then nu(G^c) <= sum_tau N_tau p_tau by 5.2(iii), so -log nu(G) <= 2 sum_tau N_tau p_tau when that sum is at most 1/2. I did not obtain nu(G) >= prod (1 - p_tau)^(c N_tau): Holder across the tilings and (CB) in each give 1 <= prod_tau ( p_tau^(1/J) + nu(G_tau)^(1/(J N_tau)) )^(N_tau), a lower bound on each nu(G_tau) and not on the intersection.

**5.6 What an application to the two runs needs (NOT VERIFIED; each item is a statement about one run).** nu_c is the Wilson measure of run c on its bare torus; it is reflection positive in every site hyperplane (Osterwalder and Seiler; cited), which gives (CB) for closed cubic tiles with an even number of tiles per direction.
 (PART) The labels of the run group into classes that correspond to a measurable partition of the bare configuration space, so that the summed mass of the good classes is kappa^c times the Wilson integral over a bare event G_c: Z^c_G/Z~^c = nu_c(G_c). (The terms tau_h are complex measures in general and carry the classes of the events of the operation R; the grouping must absorb every signed splitting. Not read.)
 (TILE) The bad event is covered by tile events: G_c^c is inside the union over finitely many reflection tilings tau and tiles t of events E^tau_t measurable in the bare fields of the closed tile. For history events this is not automatic: block averages and the enlargements of large-field regions use fields across tile faces. That is why 5.5 has several tilings. FINISH L47 records an earlier failure of a chessboard argument on a history class ("centre-plane chessboard fails on the class branch"); I did not test (TILE) on the account's regions.
 (PROD) nu_c( E^tau_t for every t ) <= A^sharp B pi_K^(N_tau). The account's multiplier bound (2.2) gives this only if a defect in every tile forces m_a(h) >= N_tau/C; one live component that meets many tiles is counted once. So (PROD) needs the multiplier per tile met (a weight exponential in the size of an old live component), which I did not find in the lines read.
Given (PART), (TILE), (PROD): | log(Z^c_G/Z~^c) | <= 2 J N_t e^(C_s v) pi_K on every torus with J N_t e^(C_s v) pi_K <= 1/2 (union form, a polynomial floor N_w^4 pi_K <= c), and with no floor if one tiling suffices (5.2(ii)).
 (RAR) is the name used below for the conclusion: | log(Z^c_G/Z~^c) | <= N_w^4 r_K for c = A, B on both tori, with r_K free of the torus (possibly under the floor N_w^4 r_K <= 1/2).
(RAR) replaces the "conditional rarity estimate, uniform in the outside" that row 1391 7.2b proposed as (REL-hist). It is weaker: 5.2 derives it from one absolute bound and reflection positivity, with no conditioning.

## 6. Assembly: (LOG-N) from (STR) and (RAR), and what the printed discs give (written 13:48Z by date -u)

**6.1 Theorem D. PROVED from 4.2 (algebra); unchecked.** Fix a torus T and an edge (A, B), in one normalisation rule. Assume
 (D1) Z~^c = Z^c_G + Z^c_bad with Z^c_G > 0 and | log(Z^c_G/Z~^c) | <= rho_T, c = A, B;
 (D2) a chain as in Theorem B with one Lambda, phi_1(0) = log Z^A_G, phi_n(1) = log Z^B_G, and sigma := sum log gamma_i.
Then | log Z~^B - log Z~^A | <= (Lambda - log Z~^A + rho_T)(e^sigma - 1) + 2 rho_T.
Proof. log Z~^B - log Z~^A = [log Z^B_G - log Z^A_G] - log(Z^B_G/Z~^B) + log(Z^A_G/Z~^A). The bracket is at most d_0 (e^sigma - 1) by 4.2 with d_0 = Lambda - log Z^A_G <= Lambda - log Z~^A + rho_T. QED
One-sided use (what Lemma SLACK reads): the upper bound uses only the right ends phi_i(1+S_i) <= Lambda and the lower bound on Z^B_G/Z~^B; the lower bound uses the left ends and the lower bound on Z^A_G/Z~^A. The consumer needs the upper bound on T_ell and the lower bound on T_(L ell).

**6.2 Corollary (extensive form; GIVEN the hypotheses of III 9.1, (STR), (RAR)).** Take G := the aligned labels with no live component of age a_0 or more (1 <= a_0 <= k - n_c). Labels outside G have a live component of age at least a_0, or are common, of first index above n_c, and not aligned (2.3(b)). Labels in G read no slot of a zone b < k - a_0 (2.3(a)), so the restricted sum Z_G depends on the recent classes only, and a path that changes the recent classes one at a time joins Z^A_G to the hybrid of B with the ramps of A. With Lambda = E_+^sharpsharp N_w^4 (2.2), Z~^A >= e^(-C_low N_w^4), and N_w = ell L^w:
   | log Z~^B - log Z~^A | <= L^(4w) ell^4 [ (E_+^sharpsharp + C_low + r_K)(e^(sigma_K) - 1) + 2 r_K ] + (ramp term, 6.3),
   sigma_K <= 2 E_1^-1 sum_(b >= k - a_0) (k-b+1) l_b <= 2 E_1^-1 q_a^(-(a_0 - 1)) Sigma_k^(q_a)   (if each l_b/E_1 <= 1/2),
the last step because q_a^((k-b-1)_+) >= q_a^(a_0-1) for b >= k - a_0. The constants in the square bracket are free of the torus; the conditions sigma_K <= 1 and e^(C_s v) pi_K <= 1/2 are floors in K that do not involve ell.
Rate. With pi_K = q_a^(a_0) and Sigma_k^(q_a) <= C e_w, e_w = rho^(n-w) + Pi_n (2.2), the two terms are C q_a^(-a_0) e_w and C q_a^(a_0). Choosing a_0 with q_a^(a_0) between e_w^(1/2) and q_a e_w^(1/2) gives
   e'_K := sigma_K + r_K <= C e_w^(1/2).
So this crude split pays the square root of the account's rate: geometric stays geometric (rho^(K/2)); the power K^(-(kappa_0-4)/2) becomes K^(-(kappa_0-4)/4), summable for kappa_0 > 8. A direct use of the load envelope for the recent zones (III lemma on the load envelope, not read) may avoid the square root; not done.

**6.3 The ramp move: the failing term for extensivity as printed, and its scope (READ Y 130281-130306; ARGUED).** The ramp interpolation has the disc |s| <= (20 C_chi N_w^4 theta_chi^k)^(-1): the radius carries N_w^(-4), chosen so that the product of the N_w^4 slot factors (1 + 20 C_chi theta_chi^k |s|) is at most e. With that disc, 4.1 gives gamma - 1 of order N_w^4 theta_chi^k and a contribution of order (E_+^sharpsharp + C_low) N_w^8 theta_chi^k: quadratic in the volume, not extensive, and not exponential. Scope: this is a property of the printed disc, not of the ramps. An extensive bound needs the disc |s| <= (20 C_chi theta_chi^k)^(-1) with the product of slot factors, at most e^(N_w^4), absorbed in an enlarged majorant e^((E_+^sharpsharp + 1) N_w^4); the text asks for "doubled component majorants" on its disc (Y 130296-130299) and does not state the larger one. (STR) for the ramp parameter is also open (the slots are cut-off functions, not exponents). For the consumer the quadratic term is harmless when theta_chi < 1: it is geometric in K.

**6.4 Theorem E (the conditional form of (LOG) that this row reaches). PROVED GIVEN the named inputs; unchecked.** Assume, for all admissible ell, on T_ell and T_(L ell), for all K >= K_1 and all matched real centres in the window of Lemma SLACK:
 (H1) the hypotheses and conclusions of III 9.1 in the form of 2.2 (majorant on the dial domain; one of its hypotheses is outstanding in the account);
 (H2) (STR) of 4.7 for the restricted aligned sum, along the recent classes and the ramp parameter;
 (H3) (RAR) of 5.6;
 (H4) (RULE), (V1), (V2) of 3.3, with III 9.1 holding for the representatives of (RULE).
Then on every edge
   Phi'_ell(K, beta) - Phi'_ell(K-1, beta') <= 2 L^4 L^(4w) ell^4 C_1 e'_K + C_2 L^(8w+4) ell^8 theta_chi^(K-w),   Phi' := Phi - Delta H,
with C_1, C_2 free of ell and K, and | Phi - Phi' | <= eta_V(m). Hence, by Lemma SLACK applied to Phi' (row 1391 6.1), at every datum of cutoff K >= K_0 >= K_1 reached by a slack-matched chain,
   Phi_ell <= sup over the widened base window of Phi_ell(K_0, .) + C ell^4 sum_(K > K_0) e'_K + C ell^8 theta_chi^(K_0)/(1 - theta_chi) + 2 eta_V(m).
Proof. 3.1 with Z~ of (RULE): the scalar term is Delta H^B - Delta H^A, moved to the left side as Phi'. 6.2 and 6.3 on each torus give (LOG-N) with the two remainders; 3.1 turns them into the two-torus bound. Lemma SLACK telescopes Phi'; (V2) converts back at the two ends. QED
This is a carry, not a seed: it contains no smallness of Phi at any datum (the base supremum is an input), so it is not equivalent to (SEED-FP); and it is not equivalent to (LOG), since (H2) and (H3) carry no comparison between cutoffs.
