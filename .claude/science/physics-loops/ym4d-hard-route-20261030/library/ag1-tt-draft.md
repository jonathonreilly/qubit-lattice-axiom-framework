# AG1, round 3: trigger tails (TT) — long draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, written for the lead as the round-3 long draft of the part of AG1 that round 2 left Outstanding. It does not rewrite AG1. It drafts (TT) (`library/ag1-draft2.md` (3.2), §10.1) and then states what AG1 still needs. Research text. It is not an audit, it grants no status, and no other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

No step rests on a computation. Every argument is a finite-dimensional integral identity, a one-dimensional integration by parts, a level-set argument, Fubini/Tonelli, a Cauchy estimate, a Schur bound, a geometric series or a continuity argument on [0, 1]. Each is meant to be Lean-formalisable.

Credit. The architecture is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the histories and their kernels, the collar and rim device and its mean bound, the trigger hypothesis of the two-run agreement and the sentence that triggers are paid by the conditional law (SA L23328, L23334), and the cutoff-Gaussian section whose transport proof of marginal log-concavity is rebuilt here (SA L27149–27212). Their complete account (CA-II) supplies the reading of Balaban's step with the window as a product of norm balls, the class of windowed Gibbs measures, the box form of the convexity input used here, and the remark that conditioning on a box puts the mean at the edge of the window. Tadeusz Balaban's papers (CMP 109 (1987) 249; 116 (1988) 1; 119 (1988) 243; 122 (1989) 175, 355) are the source of the step, the conditional fluctuation integral, the window and the operator 𝐂. Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. The analytic lemmas of §4 are standard results rebuilt by hand: Prékopa (1971, 1973) and Leindler (1972) for §4.1–4.2, Brascamp and Lieb (1976) for the one-dimensional variance bound of §4.3, Combes and Thomas (1973) for §4.5. Round 2 of AG1 is `library/ag1-draft2.md` (Claude).

Line references: **SA L** = `scratchpad/sa/ym4.tex`; **CA-II L** = `scratchpad/sa/ca_II.tex`; **IN1 L** = `library/in1-draft.md`; **R2 L** = `library/ag1-draft2.md`. I read every cited range myself in this session, in bounded ranges. Source text is paraphrased, with line numbers; I quote at most a few words.

Status words: **[proved]** = proved here by hand from the stated inputs; **[input: NAME, owner]** = a statement another submanuscript must supply, stated exactly; **[design]** = a choice of the construction; **[outstanding]** = not proved.

Notation kept from R2: levels i, the level-i cell 𝔡 of side c_i = MŘ_iℓ_i, the regions Ω_i, Λ_i^{pre}, Z_i^{pre} of step i before 𝐑 (R2 §3.6), the collar fraction θ_col = 1/(4Θ₁), the rim fraction θ_c, the threshold spread κ_T = 1/4 of (SM), p₀(g) = A₀(log g^{−2})^{𝔭₀}, δ_j = (A₁/A₀)g_jp₀(g_j) (IN1 L43). New: 𝔟_j := δ_j/g_j = (A₁/A₀)p₀(g_j), the scaled threshold (CA-II L79854 writes 𝔟_k = g_k^{−1}δ_k).

---

## 0. Summary

**Result.** (TT) is **proved** as an implication from one new input, (CL), on the conditional law of one step, together with the inputs R2 already uses (Theorem 5.3). The constants are

  c_T = λθ_col²(A₁/A₀)²/(384 c_N² C_𝐂²),  C_T = log 6,  λ ≥ ¾a_−,

with a_− the gap of (I-1), c_N the norm-equivalence constant on su(2) and C_𝐂 the norm of Balaban's operator 𝐂 on one bond.

**The mechanism, in four steps.**
1. *Convexity.* Fix a history and a level i. Condition on everything the run keeps after step i. Then the scaled step-i fluctuation on the free bonds of Λ_i^{pre} has a density 𝟏_𝒲e^{−H}. Here 𝒲 is a product of symmetric convex windows, one per free bond, and H is uniformly convex on 𝒲. This is input (CL) (§3).
2. *Sub-Gaussian statistics.* Under such a law every linear statistic ⟨ℓ, Y⟩ is sub-Gaussian about its mean with variance proxy |ℓ|²/λ. The bound has no volume factor, and it needs no lower bound on any cutoff probability (Lemma 4.4). The proof is Prékopa's theorem plus a one-dimensional integration by parts. The normalisation cancels inside that integration by parts. This is what T5 lacked.
3. *Location of the means.* The means sit where the Gaussian mean 𝐦 = −A^{−1}𝐅 sits, up to K_∞(p₁ + ε_W) (Proposition 4.7). The proof: integration by parts gives m = 𝐦 + A^{−1}(ν(∇H) + ν(∇P)); the wall force ν(∇_bH) is exponentially small wherever the mean is well inside its window (Lemma 4.6); a continuity argument from the even case s = 0 closes the loop. The one place where the construction enters is SA's collar bound |𝐦| < ½θ_cδ (SA L17363). That bound is what SA's rounds produce. At a deep bond 𝐦 is exponentially small in the depth.
4. *The tail.* A deep trigger forces a linear statistic to deviate by θ_col𝔟/(2c_N), that is by a multiple of θ_col(A₁/A₀)p₀ standard deviations. Several triggers of one level give one statistic, the sum (Proposition 5.1). Positivity carries the one-step bound through all levels (Proposition 5.2). R2's Lemma 10.1 then gives (TT) jointly with (MB) (Theorem 5.3).

**Why T5 stopped and this does not.** T5 conditioned on the field outside a small box, bounded the numerator by oscillation and needed a lower bound for the denominator. Here nothing is conditioned except what the run keeps. No box is formed. No denominator is bounded below: Lemma 4.3 bounds a variance directly. No maximum principle is used: the mean is located by convexity (Proposition 4.7). CA-II L84195–84201 explains why the conditional Gaussian of a box puts the mean at the window edge. Attack N2 (§7) shows that this obstruction returns as soon as one localises to a box. So (CL) is needed on the whole region Λ_i^{pre}.

**What (CL) is, and who supports it.** (CL) has six clauses (§3.1). Five follow from statements already in the library or in SA: the step's structure, the windows, the gap of the quadratic form, the force bound and the readout (§3.2). The sixth, (CL)(P), is a Hessian bound on the non-Gaussian part of the exponent on all of Λ_i^{pre}. It follows by Cauchy estimates (Lemma 3.1) from an analytic presentation (P-an) with a fixed sup bound on a tube of radius ρ ≫ 𝔟. One part of (P-an) is not stated by any owner: a zero-free tube for the factors of healed regions (§3.3). CA proves the box form of (CL), on clean histories, under its hypotheses (a)–(j) (CA-II L84948–85075). SA does not assert convexity, symmetry or a force bound for the interacting conditional density (SA L28219–28221).

**What AG1 then still needs.** Nothing of its own. Theorem AG of R2 (R2 L80) holds as an implication from the inputs (K)+(MI), (COV), (SM), (RS), (BGL), (R0)–(R3), (LT), LG1(3) and, in place of (TT), (CL) with the room (5.4′). §8 lists them with owners. The first statement on AG1's path that no owner has yet stated is (CL)(P) on all of Λ_i^{pre}, in the form (P-an)(d): the healed-region factors need a zero-free tube (§3.3, §8).

**Attacks.** N1 (convexity on the whole small-field region; succeeds from (CL)), N2 (convexity on a box; fails at the mean, for the reason above) and N3 (redesign of the trigger at a coarser resolution; fails because the block average of a fluctuation vanishes to first order). §7 also records a second conditional route through SA's regular gas. All three differ from T1–T5 (§7.4).

**Line count**: at the end of the file.

---

## 1. The target and its reduction

### 1.1 (TT), as stated in round 2

The deep trigger event (R2 L164–168). For a level i ≥ 1 and a bond b of level i − 1 with level-i cell 𝔡(b),

  Trig_i(b) := {b ∈ Λ_i^{pre}, no cell of Z_i^{pre} meets 𝔡(b)^{+2}, and |𝒜_{i−1}(b)| > θ_colδ_{i−1}}.

The norm |·| here is the one of SA's tests, an Ad-invariant norm on su(2) (CA-II L80028–80031). In this draft I write it ‖·‖_B and write |·| for the Euclidean norm. Let c_N ≥ 1 be such that c_N^{−1}|v| ≤ ‖v‖_B ≤ c_N|v| for v ∈ su(2) (an absolute constant).

**(TT)** (R2 L170–172). There are c_T > 0 and C_T such that the following holds. Let 𝔷_1, …, 𝔷_m be designated cells as in (MB). Let 𝔅 be a finite set of bonds, each of a level i(b) − 1, with distinct cells 𝔡(b) and with the 𝔡(b)^{+2} pairwise disjoint among bonds of equal level. Then

  ν̃(∩_iE^{(n_i)}_{𝔷_i}(k_i) ∩ ∩_{b∈𝔅}Trig_{i(b)}(b)) ≤ exp(B_k|𝕋^{(k)}| + C_Dm + C_T|𝔅| − 2c_aΣ_iΣ_{j=n_i}^{k_i}r_j − c_TΣ_{b∈𝔅}p₀(g_{i(b)})²).   (1.1)

R2 also asked each 𝔡(b)^{+2} to be disjoint from the ancestors of the designated cells. The proof below does not use that condition (Remark 5.4).

### 1.2 The reduction of round 2

**R2 Lemma 10.1** (R2 L728–734) [proved there]. Write t(h; T) := Z·μ⊗λ({H_k = h} ∩ T). Suppose that for every history h of level k and every 𝔅 as in (TT),

  t(h; ∩_{b∈𝔅}Trig_{i(b)}(b)) ≤ Π_{b∈𝔅}(C_Te^{−c_Tp₀(g_{i(b)})²}) · t(h).   (TT-hist)

Then (TT) holds. The proof sums over the histories in the survival events and applies (MB), which is R2 (3.1) (Lemma E.4 of R2).

So the task is (TT-hist). The geometric conditions of Trig are functions of h. For histories in which they fail, the left side of (TT-hist) is 0.

### 1.3 What must be shown at one step

(TT-hist) is a statement about many levels at once. §5.2 reduces it to one level at a time by positivity of the kernels. At one level i the statement is: conditional on everything the run keeps after step i, the step-i fluctuation passes the collar threshold at |𝔅_i| deep bonds with probability at most (6e^{−c_Tp₀(g_i)²})^{|𝔅_i|}. This is a statement about the conditional law of the step, which SA names as the payer: the price is "borne by the conditional law of the fluctuation field in its box" (SA L23328; the same at L23334). §3 states that conditional law as input (CL). §4 proves the analysis. §5 proves the bound.

---

## 2. What the sources say

### 2.1 Sussman–Alpoge

- *The payer of a trigger* (SA L23328, repeated at L23334). A cell with no large-field cell within two cells and with a bond where a lower threshold is passed by the scaled fluctuation is paid by the conditional law of the fluctuation field. No proof is given there.
- *The collar and rim device* (SA L17348–17367). The stored part of 𝒜_k shifts the mean of the conditional Gaussian on Λ_t to 𝐦 = −C^{(k)}(Λ_t)Δ^{(k)}𝒜_k|_{Ω_t∖Λ_t} (L17351). The map is linear, so the same formula holds for the scaled fields, with every threshold divided by g_k (L17354). The least inner threshold is θ_cδ_k on bonds that cross ∂Λ_t and δ_k further in (L17354). The collar test is |𝒜_k| < δ_k/(4Θ₁) on stored bonds within ϖ_T of Λ_t (L17356). The rim test is |𝒜_k| < θ_cδ_k on the cells of Z_t that touch Λ_t (L17357). At greater distance only |𝒜_k| < Cδ_k is known (L17360). The kernel of 𝐦 is bounded with exponential decay, and |𝐦| ≤ C(Θ₁^{−1} + θ_ce^{−cϖ_T} + e^{−cMŘ_t})δ_k < ½θ_cδ_k if θ_cΘ₁ ≥ C, ϖ_T ≥ C and γ is small (L17360–17364).
- *The cutoff Gaussian* (SA L27091–27147). A centred Gaussian vector with blocks in ℝ³ and the law conditioned on all blocks lying in balls (GCB1–GCB2, L27117–27141). SA notes that the probability of the cut can tend to zero with the volume, so whole-space tails divided by it give nothing uniform (L27094–27100), and that its estimates need no lower bound on the cut probability (L27143–27147).
- *Marginal log-concavity* (SA L27150–27212). A transport proof of the one-dimensional Prékopa–Leindler inequality (GCB3–GCB4), its induction to ℝ^q, and the consequence that the marginal of a jointly log-concave kernel is log-concave (GCB5, L27197–27202). An even log-concave function decreases along rays (L27208–27212).
- *Linear statistics of the centred cut Gaussian* (SA L27493–27529). Under even log-concave cutoffs every increasing function of |⟨ℓ, Z⟩| is dominated by its Gaussian expectation (GCB20), so ⟨ℓ, Z⟩ is sub-Gaussian with the Gaussian variance (GCB21). The proof uses evenness: the conditional weight decreases along rays.
- *What SA does not assert* (SA L28207–28221). In the complete conditional law, an exterior linear force can push the law toward the window boundary, and an old activity can destroy the even log-concavity used for GCB8 (L28209–28213). SA states that no convexity, symmetry or force bound is asserted for the resummed interacting conditional density (L28219–28221).

### 2.2 The complete account (CA-II)

- *Balaban's step* (CA-II L79847–80013), a reading of CMP 119 §3, (3.1)–(3.25). The background is the average of the minimal configuration (item (d), L79896–79910). The fluctuation A_k = (1/i)log V'_k is expanded, the δ-functions are linearised and removed with the operator 𝐂, and the field is scaled (item (e), L79911–79918). The field entering the action is exp(i[g𝐂A − hD̃(g𝐂A)])V^{(k)} (L79925). The small-field cutoffs are the third-test indicators sup_b|A_k(b)| < δ_k over the *free* bonds of each cube's neighbourhood (item (f), L79939–79962). On Λ_{k+1} only these remain (item (g), L79964–79968). The integral over A on Λ_{k+1} is the conditional integral, and the stored part is integrated later by 𝐓 (item (h), L79970–79974). The integrand is the exponential (3.25) (L79980–79993), with the quadratic form, a linear term in the stored field, and the perturbations.
- *The window* (CA-II L80014–80060). The fluctuation window is the product, over the free bonds of Λ_{k+1}, of the norm ball of radius 𝔟_k in the scaled variable. Each ball is open, bounded, convex, symmetric and Ad-invariant (L80045–80046).
- *Class membership in box form* (CA-II L84948–85075). Under hypotheses (a)–(j), for histories in a clean event, the conditional law of the free-bond variables of a box I, given the history, the coarse field, the frozen exterior y_F and the background, has density 𝟏_{𝒲_I}exp[−½⟨y_I, A_{II}y_I⟩ − ⟨y_I, A_{IF}y_F⟩ + P^{tot}(y_I, y_F)] (L85042–85048). It lies in CA's class 𝔖 with convexity constant ½a_− and level-free constants, uniformly in the exterior datum (L85049–85057). The hypotheses include the gap and decay of the quadratic form (a), gradient and Hessian bounds on P^{tot} on a complex tube, |∂P| ≤ C_Pg𝔟² and |∂²P| ≤ C_Pg𝔟e^{−c_P dist} (b), the product window (c), positivity (d), a per-bond clause on pocket-attached terms (g), and a ceiling (j).
- *Tools in the class* (CA-II L81161–81200, L81804–81862). A Lipschitz stability theorem for windowed Gibbs measures under a convexity hypothesis, proved by coupling Hamiltonian flows, and its corollary: sub-Gaussian tails of linear functionals about the mean, with variance proxy |ℓ|²/λ (L81804–81816). Lemma 4.4 below proves the same inequality by a shorter route.
- *Correlation decay* (CA-II L83869–83876). CA's decay of correlations in the class assumes the Helffer–Sjöstrand covariance representation as a statement (L83870).
- *Why conditioning on a box fails* (CA-II L84195–84201). With the exterior field at the edge of the window, the conditional Gaussian mean at the box sites next to ∂I is of the size of the window, so the complement of the window is not small there. CA's decoupling interpolation keeps the window in every measure and uses only log-concavity and locality of the Hessian (L84202–84207).

### 2.3 Our library

- (I-1) (IN1 L57–62): the fibre precision of the step is coercive with constant a, "on every compression to a coordinate subset", with kernel decay H e^{−μ₀d}; [C] at real critical backgrounds; P82° (`library/p82-draft.md`) at curved real critical references.
- (I-5) (IN1 L70–78): the small-field step, its analyticity on its product box and its error bounds, including the large-field terms |B(X)| ≤ 𝖡e^{−κd^♮(X)}.
- (I-8) (IN1 L90–94): the prepared structure of a passed component; its exponent Ψ_ω is bounded above on the complex fixed set U^c_i, Re Ψ_ω ≤ C_ΨV°.
- IN1 L44 and L347: the analyticity radii α_{ι,j} = C_ιθ_j^{−1/2}(log θ_j)^q, with q > 𝔭₀ + 2r and 𝔭₀ ≥ 6r + 1. Scaled by g_j = θ_j^{−1/2}, the radius is C_ι(log θ_j)^q, against the window 𝔟_j = A₁(log θ_j)^{𝔭₀}: the radius exceeds the window by a power of log θ_j.
- R2 Theorem 5.4 items 10 and 11 (R2 L332–333): under (SM) the approximate fluctuation test equals 1 where the third tests pass, and SA's mean bound holds with the factor 5/4.

---

## 3. The conditional law of one step: input (CL)

### 3.1 Statement

Fix a history h of level k and a level 1 ≤ i ≤ k. Let I = I_i(h) be the set of free bonds of level i − 1 in Λ_i^{pre}(h): the bonds of level i − 1 in Λ_i^{pre} with the pivot bond of each level-i block removed (CA-II L80025–80030). Let E := (su(2))^I ≅ (ℝ³)^I with the Euclidean product, |y|_∞ := max_b|y_b|, and d(b, b') the level-(i − 1) lattice distance. For c > 0 let S_d(c) := sup_bΣ_{b'}e^{−c d(b,b')}, the sum over all bonds of the level-(i − 1) lattice, a number independent of the volume.

**(CL) Convex conditional law of the step** [input: owner NL1, with PR1(1) for (A), LF1(1) for (0), LF1(4)–(5) for (P); new]. There are constants a_−, a_+, c_A (those of (I-1)), C_𝐂 ≥ 1, R_𝐂, C_ϱ (Balaban's operator 𝐂), C_h, c_h, and numbers p₁, p₂ (functions of g_{i−1}, specified in (P)), such that for every h and i the following holds.

- **(0) Structure.** On {H_k = h} the run defines measurable maps Y = Y^{(i)} into E (the scaled step-i fluctuation; the unscaled one is g_{i−1}Y) and R = R^{(i)} (all other variables of the level-(i − 1) state), with:
 - (0a) every variable that the run reads at levels ≥ i, apart from the inner tests of step i on Λ_i^{pre}, is a function of R;
 - (0b) for each bond b of level i − 1, Trig_i(b) is a function of (Y, R);
 - (0c) let S_n be the state after step n (the variables read at levels > n). Then S_i is a function of R, and (Y^{(i)}, R^{(i)}) is a function of S_{i−1};
 - (0d) under the finite measure G ↦ t(h; G) on functions of (Y, R), the conditional law of Y given R is, for almost every R,
  ν_R(dy) = Z_R^{−1}𝟏_𝒲(y)e^{−H(y)}dy,  H(y) = ½⟨y, Ay⟩ + ⟨𝐅, y⟩ − P(y),   (3.1)
  where 𝒲, A, 𝐅, P depend on (h, R) and satisfy (W), (A), (F), (P), (ℓ).
- **(W) Windows.** 𝒲 = Π_{b∈I}K_b with K_b ⊂ ℝ³ open, convex, K_b = −K_b, and B(0, r_in) ⊂ K_b ⊂ B(0, r_out), where r_in := θ_c𝔟_{i−1}/c_N and r_out := (5/4)c_N𝔟_{i−1}.
- **(A) Quadratic form.** A is real symmetric on E with ⟨ξ, Aξ⟩ ≥ a_−|ξ|² and ‖A(b, b')‖ ≤ a_+e^{−c_Ad(b,b')}.
- **(F) Force.** |𝐅_b| ≤ C_h𝔟_{i−1}e^{−c_h d(b, (Λ_i^{pre})^c)} for every b, and 𝐦 := −A^{−1}𝐅 satisfies |𝐦|_∞ ≤ r_in/8.
- **(P) Perturbation.** P is C² on an open neighbourhood 𝒩 = −𝒩 of the closure of 𝒲, real, and for y ∈ 𝒲: |∂_bP(y)| ≤ p₁ for every b, and ‖P''(y)‖_op ≤ p₂ ≤ a_−/4.
- **(ℓ) Readout.** For each bond b of level i − 1 in Λ_i^{pre} at distance ≥ R_𝐂 from (Λ_i^{pre})^c, 𝒜_{i−1}(b) = g_{i−1}(ℓ_b(Y) + ϱ_b(Y)), where ℓ_b: E → ℝ³ is linear with ‖ℓ_b‖ ≤ C_𝐂, ℓ_b(y) depends only on the y_{b'} with d(b, b') ≤ R_𝐂, and ‖ϱ_b(y)‖_B ≤ C_ϱg_{i−1}r_out² for y ∈ 𝒲.

### 3.2 Where each clause comes from

- **(0)** is the bookkeeping of Balaban's step in SA's form. SA's step is a sequence of moves with positive kernels (SA L17499–17514; R2 (K), (MI-4)). Balaban's conditional integral over A on Λ_{k+1}, with the stored part integrated later (CA-II L79970–79974), is the disintegration (0d). (0a) is R2's read structure (RS-c) (R2 L373): no move other than the listed tests reads a background-relative fluctuation, and the inner tests on Λ_i^{pre} read Y only through the windows. Three points need to be checked. (i) A test that *failed* never reads Y. A failed approximate fluctuation test at □' puts □'^{~2} into Ω_i^c, and a failed third test puts its cube with one layer into Z^{[0]} (SA L17321). Neither meets Λ_i^{pre}. A failed collar or rim test reads stored bonds only. (ii) The passed approximate fluctuation tests equal 1 on 𝒲 (R2 Theorem 5.4 item 10, under (SM) with room (5.3)). Balaban's gauge-fixing characteristic function equals 1 on Ω~_{k+1} (CA-II L79886–79895). (iii) Under (SM) each test is decided by its own uniform (R2 §5.1), and those uniforms are in R. Given them, every passed inner test is a sharp test at radius θs_τ with s_τ ∈ [1, 1 + κ_T]. Every factor of the step kernel that depends on Y and is not a window belongs in e^{−H}. (0b) holds because 𝒜_{i−1}(b) on Λ_i^{pre} is a function of the level-(i − 1) field there, hence of Y, and of the background, which is a function of R. (0c) is the order of moves.
- **(W)** is Balaban's window (CA-II L80014–80053) with SA's thresholds (SA L17354) and the (SM) radii. In Balaban's norm, a free bond carries the ball of radius θ𝔟s with θ ∈ {θ_c, 1} and s ∈ [1, 5/4]. Intersections over the cubes that contain a bond are again such balls. In Euclidean norm this gives (W). **[design]** The inner tests on Λ_i^{pre} must read free bonds only, as in Balaban's (3.16) (CA-II L79939–79962). A test of 𝒜 at a pivot bond would be a nonlinear constraint on Y through ϱ_b, and its set need not be convex. If LF1's construction tests pivot bonds, this is one change to it.
- **(A)** is (I-1)(b)–(c) (IN1 L57–62) applied to the compression of the step's quadratic form to the coordinates I: [C] at real critical backgrounds, and P82° at curved ones.
- **(F)** In the scaled variables, 𝐅 = (Δ𝒜|_{Ω_i∖Λ_i})/g restricted to the rows of I (CA-II L79987, the linear term −⟨A, 𝐂*Δ𝐂A_k⟩), and 𝐦 = −A^{−1}𝐅 is SA's 𝐦 (SA L17351). The force bound uses the stored bounds |𝒜| < Cδ (SA L17360) and the exponential decay of the operator. The bound |𝐦|_∞ ≤ r_in/8 is SA's bound (SA L17363) in Euclidean norm. It needs the room

  (5/4)c_N²C(Θ₁^{−1} + θ_ce^{−cϖ_T} + e^{−cMŘ_t}) ≤ θ_c/8,   (5.4′)

which holds if θ_cΘ₁ ≥ 30c_N²C, e^{−cϖ_T} ≤ (30c_N²C)^{−1} and e^{−cMŘ_t} ≤ θ_c(30c_N²C)^{−1}. These are SA's own conditions with a numerical factor. Θ₁ and ϖ_T are chosen after M₂ and before M (SA L19469); the last condition is a floor on M or on x. This strengthens R2 Theorem 5.4 item 11 (room (5.4)).
- **(ℓ)** is CA-II L79925: on a free bond 𝐂 is the identity, and on a pivot bond 𝐂 reconstructs the variable from the free bonds of its block (range R_𝐂). The term hD̃ is the nonlinear part of the linearised constraint, quadratic in g𝐂A.
- **(P)** is the substantive clause. It is a gradient and Hessian bound for the non-Gaussian part of the exponent, uniform over all of Λ_i^{pre}, up to its boundary, and over every value of R. Lemma 3.1 derives it from an analytic presentation (P-an). §3.3 says what (P-an) asks of NL1 and LF1.

### 3.3 Clause (P) from an analytic presentation

**Lemma 3.1 (Cauchy estimates)** [proved]. Let ρ > 0 and let 𝒯_ρ := {ζ ∈ E_ℂ : there is y ∈ 𝒲 with |ζ_{b,a} − y_{b,a}| < ρ for all b ∈ I, a = 1, 2, 3} (coordinates in an orthonormal basis of su(2)). Suppose P = Σ_{X∈𝔛}P_X, a finite sum, where each P_X is holomorphic on 𝒯_ρ, real on real points, depends only on the coordinates of the bonds of X ⊂ I, and satisfies sup_{𝒯_ρ}|P_X| ≤ π_X, with Σ_{X∋b,b'}π_X ≤ π̄e^{−κd(b,b')} for all b, b'. Then for y ∈ 𝒲:

  |∂_bP(y)| ≤ √3π̄/ρ,  ‖∂_b∂_{b'}P(y)‖ ≤ 6π̄e^{−κd(b,b')}/ρ²,  ‖P''(y)‖_op ≤ 6π̄S_d(κ)/ρ².

*Proof.* Fix y ∈ 𝒲. The polydisc D := {ζ : |ζ_{b,a} − y_{b,a}| < ρ for all (b, a)} lies in 𝒯_ρ. For a function f holomorphic on D with |f| ≤ π, Cauchy's formula in one variable gives |∂_jf(y)| ≤ π/ρ and |∂_j²f(y)| ≤ 2π/ρ². In two variables it gives |∂_j∂_kf(y)| ≤ π/ρ² for j ≠ k. Only the P_X with X ∋ b contribute to ∂_bP, and only those with X ∋ b, b' to ∂_b∂_{b'}P. Hence each coordinate of ∂_bP is at most Σ_{X∋b}π_X/ρ ≤ π̄/ρ, and each entry of the 3×3 block ∂_b∂_{b'}P is at most 2π̄e^{−κd(b,b')}/ρ². A vector in ℝ³ has norm at most √3 times its largest coordinate, and a 3×3 matrix has operator norm at most 3 times its largest entry. The last bound is the Schur test, ‖P''‖_op ≤ sup_bΣ_{b'}‖∂_b∂_{b'}P‖, valid because the block-norm kernel is symmetric. ∎

**(P-an)** [input: owners NL1 and LF1(4)–(5)]. There are q₁ > 0 and c_ρ > 0, fixed before γ, such that for every h, i and R the exponent P of (3.1) has a decomposition as in Lemma 3.1, on 𝒯_ρ with ρ ≥ ρ_{i−1} := c_ρ(log θ_{i−1})^{q₁}, and with π̄ ≤ C_π. Here C_π may depend on M and on the constants chosen before γ, but not on the level, the history, the volume or g.

*Consequence.* With (P-an), (CL)(P) holds with p₁ := √3C_π/ρ_{i−1} and p₂ := 6C_πS_d(κ)/ρ_{i−1}². Both tend to 0 as x_{i−1} → ∞, so p₂ ≤ a_−/4 is a ceiling on g. Only ρ → ∞ is used; no margin of the tube over the window is needed beyond analyticity on 𝒯_ρ itself. The analyticity radius of the product box, of order C₀(log θ)^q in scaled units (IN1 L44), exceeds r_out + ρ for ρ up to half of it, because q > 𝔭₀ (IN1 L347). So for the terms (a)–(c) below one expects q₁ = q.

*What (P-an) asks, term by term.*
- (a) The small-field terms E, R of the effective action at level i − 1 and their dependence on Y through the level-(i − 1) field. (I-5) bounds them on the product box (IN1 L70–78), whose scaled radius is of order (log θ)^q (IN1 L44).
- (b) The non-quadratic part of the Wilson action and of the step's Jacobians. Per plaquette these are of order g_{i−1}ρ³ on 𝒯_ρ, which tends to 0 because ρ is polylogarithmic.
- (c) The large-field terms B(X), with |B(X)| ≤ 𝖡e^{−κd^♮(X)} (I-5), as functions of the small-field variables on 𝒯_ρ.
- (d) The factors of components healed at earlier levels, which lie inside Λ_i^{pre} as functions of the level-(i − 1) field near them. Such a factor M_X is positive on real arguments. For log M_X to be a term of (P-an), M_X must have no zero on a complex tube of radius comparable to ρ. Moreover |log(M_X(ζ)/M_X(y))| must be bounded there. (I-8) bounds Re Ψ_ω from above only (IN1 L90–94). It gives the upper half of what is needed, not a zero-free tube. Borel–Carathéodory turns an upper bound C_ΨV° on a tube of radius ρ into a two-sided bound of order C_ΨV°|ζ − y|/ρ on a smaller tube. For log M_X this gives a tube of radius about ρ/(C_ΨV°), with a bounded logarithm there. Then Lemma 3.1 gives a Hessian contribution of order (C_ΨV°)²/ρ². By the class rule, X ∩ Z_j lies in a cube of O(1) level-j cells at each of the O(Ř) levels of its window (SA L17575; R2 (R3)). So V° ≤ CŘ(C_RMŘ)⁴ ~ (log θ)^{5r}, while ρ ~ (log θ)^q with q > 𝔭₀ + 2r ≥ 8r + 1 (IN1 L347). The contribution tends to 0, and q₁ = q − 5r > 0 serves. This is a plausible route, but the step "Ψ_ω is real at real arguments and Borel–Carathéodory applies uniformly in the outer record ω" is not stated by LF1(4). I record it as the open part of (P-an).
- CA's box form replaces (d) by its per-bond clause (c2)♯ on pocket-attached terms (CA-II L79475–79487). That clause defines CA's clean event, whose complement CA pays separately. In SA's framework the analyticity radii of IN1 L44 dominate the window at every level (IN1 Lemma C.10, L614). So the clean clause should not be needed, but (d) above must be supplied.

*Why (P) is needed on all of Λ_i^{pre}.* Lemma 4.4 needs uniform convexity of H on the whole window product 𝒲, because it uses Prékopa's theorem on the whole of E. One region of Λ_i^{pre} where P'' is large destroys the bound everywhere. Localising to a smaller region brings back the mean problem of N2 (§7.2).

---

## 4. Analytic lemmas

Throughout §4, E is a finite-dimensional Euclidean space (in the application, (ℝ³)^I). A function f: ℝ^q → [0, ∞) is *log-concave* if f((1 − t)x + ty) ≥ f(x)^{1−t}f(y)^t for all x, y and t ∈ (0, 1). Zero values are allowed.

### 4.1 Prékopa–Leindler in one dimension

**Lemma 4.1** [proved; Prékopa, Leindler; SA L27150–27181 gives a transport proof]. Let f, g, h: ℝ → [0, ∞) be bounded measurable functions with bounded support, t ∈ (0, 1), and h((1 − t)x + ty) ≥ f(x)^{1−t}g(y)^t for all x, y. Then ∫h ≥ (∫f)^{1−t}(∫g)^t.

*Proof.* If f ≡ 0 or g ≡ 0 the right side is 0. Otherwise put F := sup f > 0 and G := sup g > 0, and replace f, g, h by f/F, g/G, h/(F^{1−t}G^t). The hypothesis is preserved, both sides scale by F^{1−t}G^t, and now sup f = sup g = 1.

*Step 1 (one-dimensional Brunn–Minkowski).* Let A, B ⊂ ℝ be nonempty compact sets. Then (1 − t)A + tB is compact, and it contains the two sets (1 − t)A + t·min B and (1 − t)·max A + tB. The first lies in (−∞, (1 − t)max A + t min B], the second in [(1 − t)max A + t min B, ∞), so they meet in at most one point. Hence |(1 − t)A + tB| ≥ (1 − t)|A| + t|B|.

*Step 2 (level sets).* For 0 < r < 1, the sets {f ≥ r} and {g ≥ r} are nonempty (sup f = sup g = 1) and measurable. If f(x) ≥ r and g(y) ≥ r, then h((1 − t)x + ty) ≥ r^{1−t}r^t = r. So {h ≥ r} contains (1 − t)A + tB for all nonempty compact A ⊂ {f ≥ r} and B ⊂ {g ≥ r}. By Step 1, |{h ≥ r}| ≥ (1 − t)|A| + t|B|. Take the supremum over such compact sets. When a level set has measure zero, a single point serves. Inner regularity of Lebesgue measure gives |{h ≥ r}| ≥ (1 − t)|{f ≥ r}| + t|{g ≥ r}|.

*Step 3 (layer cake).* ∫h = ∫_0^∞|{h ≥ r}|dr ≥ ∫_0^1|{h ≥ r}|dr ≥ (1 − t)∫_0^1|{f ≥ r}|dr + t∫_0^1|{g ≥ r}|dr = (1 − t)∫f + t∫g, because 0 ≤ f, g ≤ 1. By the weighted arithmetic–geometric mean inequality, (1 − t)∫f + t∫g ≥ (∫f)^{1−t}(∫g)^t. ∎

### 4.2 Marginals of log-concave functions

**Lemma 4.2** [proved; Prékopa; SA GCB5, L27197–27202]. (a) Lemma 4.1 holds on ℝ^q for every q ≥ 1, for bounded measurable functions with bounded support. (b) Let k: ℝ^p × ℝ^q → [0, ∞) be log-concave, bounded, measurable, with bounded support. Then w(z) := ∫_{ℝ^q}k(z, u)du is log-concave on ℝ^p.

*Proof.* (a) Induction on q. Write x = (x', u), y = (y', v) with x', y' ∈ ℝ^{q−1}. Fix x', y' and put z' := (1 − t)x' + ty'. The functions u ↦ f(x', u), v ↦ g(y', v) and s ↦ h(z', s) satisfy the hypothesis of Lemma 4.1, so H(z') ≥ F(x')^{1−t}G(y')^t, where F(x') := ∫f(x', u)du, and G, H likewise. F, G, H are bounded, measurable (Tonelli) and of bounded support. The induction hypothesis gives ∫H ≥ (∫F)^{1−t}(∫G)^t, and Tonelli identifies these integrals with ∫h, ∫f, ∫g. (b) Fix z, z' and t. The functions f(u) := k(z, u), g(u) := k(z', u) and h(u) := k((1 − t)z + tz', u) satisfy h((1 − t)u + tu') ≥ f(u)^{1−t}g(u')^t by joint log-concavity. Part (a) gives w((1 − t)z + tz') ≥ w(z)^{1−t}w(z')^t. ∎

### 4.3 A one-dimensional variance bound

**Lemma 4.3** [proved; the one-dimensional Brascamp–Lieb inequality]. Let J = (α, β) be a bounded open interval, κ > 0, and ψ: J → ℝ such that ψ − (κ/2)x² is convex. Let g := e^{−ψ}/Z be a probability density on J, with mean m and variance Var. Then Var ≤ 1/κ. Moreover, for every real s, ∫_Je^{s(x−m)}g(x)dx ≤ e^{s²/(2κ)}, and for every t > 0, ∫_J𝟏{|x − m| ≥ t}g ≤ 2e^{−κt²/2}.

*Proof.* *Regularity.* ψ is convex on the open interval J (a sum of convex functions), hence continuous and locally Lipschitz. Its right derivative ψ'_+ exists everywhere, is nondecreasing, and ψ(x) − ψ(y) = ∫_y^xψ'_+ on compact subintervals. Since ψ − κx²/2 is convex, its right derivative ψ'_+(x) − κx is nondecreasing. Hence (x − y)(ψ'_+(x) − ψ'_+(y)) ≥ κ(x − y)² for all x, y ∈ J. The density g is absolutely continuous on compact subintervals, with g' = −ψ'_+g almost everywhere. The mean m lies in J.

*Integration by parts.* Let α < a < m < b < β. Then

  ∫_a^b(x − m)ψ'_+(x)g(x)dx = −∫_a^b(x − m)g'(x)dx = −[(x − m)g(x)]_a^b + ∫_a^bg.

Here (b − m)g(b) ≥ 0 and (a − m)g(a) ≤ 0, so the bracket term is ≤ 0 after the sign, and the right side is ≤ ∫_a^bg ≤ 1. Subtract ψ'_+(m)∫_a^b(x − m)g:

  κ∫_a^b(x − m)²g ≤ ∫_a^b(x − m)(ψ'_+(x) − ψ'_+(m))g ≤ 1 − ψ'_+(m)∫_a^b(x − m)g.

Let a ↓ α and b ↑ β. Since J is bounded, ∫_a^b(x − m)g → ∫_J(x − m)g = 0, and ∫_a^b(x − m)²g ↑ Var by monotone convergence. Hence κVar ≤ 1.

*Exponential moment.* Put Γ(s) := log∫_Je^{sx}g(x)dx. Since J is bounded, Γ is finite and C^∞, and differentiation under the integral sign gives Γ'(s) = mean and Γ''(s) = variance of the density g_s ∝ e^{sx}g = e^{−(ψ − sx)}. The function (ψ − sx) − κx²/2 is convex, so the variance bound applies to g_s: Γ'' ≤ 1/κ. Taylor's formula with integral remainder gives Γ(s) ≤ Γ(0) + sΓ'(0) + s²/(2κ) = sm + s²/(2κ), which is the claim. Chernoff's inequality with s = ±κt gives each one-sided tail ≤ e^{−κt²/2}. ∎

### 4.4 Sub-Gaussian linear statistics on convex windows

**Lemma 4.4** [proved; the same inequality as CA-II L81804–81816, by a different proof]. Let 𝒲 ⊂ E be open, bounded and convex. Let H be C² on an open neighbourhood of the closure of 𝒲, with Hess H(y) ≥ λ·Id for y ∈ 𝒲, λ > 0. Put ν := Z^{−1}𝟏_𝒲e^{−H}dy. Then for every ℓ ∈ E∖{0}, every real s and every t > 0,

  ν(e^{s(⟨ℓ,Y⟩ − ν⟨ℓ,Y⟩)}) ≤ e^{s²|ℓ|²/(2λ)},  ν(|⟨ℓ, Y⟩ − ν⟨ℓ, Y⟩| ≥ t) ≤ 2e^{−λt²/(2|ℓ|²)}.

*Proof.* U := H − (λ/2)|y|² has Hess U ≥ 0 on the convex open set 𝒲, so U is convex on 𝒲. Put ℓ̂ := ℓ/|ℓ| and write y = vℓ̂ + z with v ∈ ℝ and z ∈ ℓ̂^⊥. This is an orthogonal change of coordinates, so dy = dv dz and |y|² = v² + |z|². The law of V := ⟨ℓ̂, Y⟩ has density proportional to e^{−λv²/2}w(v), with

  w(v) := ∫_{ℓ̂^⊥}k(v, z)dz,  k(v, z) := 𝟏_𝒲(vℓ̂ + z)exp(−λ|z|²/2 − U(vℓ̂ + z)).

The function k is log-concave on ℝ × ℓ̂^⊥. Indeed, on the convex set {(v, z) : vℓ̂ + z ∈ 𝒲} its logarithm is −λ|z|²/2 − U(vℓ̂ + z), a concave function, and elsewhere k = 0. k is bounded, since U is continuous on the compact closure of 𝒲, and it has bounded support. By Lemma 4.2(b), w is log-concave. The set J := {v : w(v) > 0} is the projection of 𝒲 onto ℝℓ̂: for v in this projection the slice {z : vℓ̂ + z ∈ 𝒲} is a nonempty open set, on which the integrand is positive. J is an open bounded interval. On J, ω := −log w is a finite convex function. So V has density e^{−ψ}/Z on J with ψ = λv²/2 + ω, and ψ − λv²/2 is convex. Lemma 4.3 with κ = λ gives ν(e^{σ(V−νV)}) ≤ e^{σ²/(2λ)} for every real σ. Since ⟨ℓ, Y⟩ = |ℓ|V, take σ = s|ℓ|. The tail follows from Lemma 4.3. ∎

### 4.5 Decay of the inverse of the quadratic form

**Lemma 4.5** [proved; Combes–Thomas]. Let A be as in (CL)(A). Let μ ∈ (0, c_A/2] satisfy

  a_+ sup_bΣ_{b'}(e^{μd(b,b')} − 1)e^{−c_Ad(b,b')} ≤ a_−/2.   (CT)

Then ‖A^{−1}(b, b')‖ ≤ (2/a_−)e^{−μd(b,b')}. Hence K_∞ := sup_bΣ_{b'}‖A^{−1}(b, b')‖ ≤ (2/a_−)S_d(μ), and |A^{−1}v|_∞ ≤ K_∞|v|_∞ for all v ∈ E. (CT) holds for some μ = μ(a_−, a_+, c_A) > 0, because the left side is at most a_+μΣ_{b'}d(b, b')e^{−c_Ad(b,b')/2} for μ ≤ c_A/2. That sum is finite and independent of the volume.

*Proof.* Fix b₀ and let T be multiplication by e^{μd(b₀,b)} on the block of b. Put B := TAT^{−1}, so B(b, b') = e^{μ(d(b₀,b) − d(b₀,b'))}A(b, b'). By the triangle inequality |d(b₀, b) − d(b₀, b')| ≤ d(b, b'), and |e^x − 1| ≤ e^{|x|} − 1, so ‖B(b, b') − A(b, b')‖ ≤ (e^{μd(b,b')} − 1)a_+e^{−c_Ad(b,b')}. This kernel is symmetric in (b, b'). The Schur test and (CT) give ‖B − A‖_op ≤ a_−/2. So ⟨ξ, Bξ⟩ ≥ ⟨ξ, Aξ⟩ − (a_−/2)|ξ|² ≥ (a_−/2)|ξ|². Hence |Bξ||ξ| ≥ (a_−/2)|ξ|², B is invertible and ‖B^{−1}‖ ≤ 2/a_−. Since B^{−1} = TA^{−1}T^{−1}, its block (b, b₀) is e^{μd(b₀,b)}A^{−1}(b, b₀). A block of an operator has norm at most that of the operator, so ‖A^{−1}(b, b₀)‖ ≤ (2/a_−)e^{−μd(b,b₀)}. The bound on K_∞ follows by summing, and the last claim is the triangle inequality. ∎

**Corollary 4.5′ (the Gaussian mean at depth)** [proved]. Under (CL)(A), (F), put μ' := min(μ/2, c_h) and C_𝐦 := 2C_hS_d(μ/2)/a_−. Then |𝐦_b| ≤ C_𝐦𝔟_{i−1}e^{−μ'd(b,(Λ_i^{pre})^c)} for every b ∈ I.

*Proof.* |𝐦_b| ≤ Σ_{b''}‖A^{−1}(b, b'')‖|𝐅_{b''}| ≤ (2C_h𝔟/a_−)Σ_{b''}e^{−μd(b,b'')}e^{−c_hd(b'',Λ^c)}. Write e^{−μd} = e^{−(μ/2)d}e^{−(μ/2)d}. Then e^{−(μ/2)d(b,b'')}e^{−c_hd(b'',Λ^c)} ≤ e^{−μ'(d(b,b'') + d(b'',Λ^c))} ≤ e^{−μ'd(b,Λ^c)}, by the triangle inequality. The remaining Σ_{b''}e^{−(μ/2)d(b,b'')} is at most S_d(μ/2). ∎

### 4.6 The force of the walls

**Lemma 4.6** [proved]. Let 𝒲 = Π_{b∈I}K_b be as in (CL)(W), and let H be C¹ on an open neighbourhood of the closure of 𝒲, with ν = Z^{−1}𝟏_𝒲e^{−H}dy. Let G_b := sup_{y∈𝒲}|∇_bH(y)|. Then

  |ν(∇_bH)| ≤ (G_b + 16/r_in)·ν(|Y_b| > ¾r_in).

*Proof.* Fix a C^∞ function ϑ: ℝ → [0, 1] with ϑ = 1 on (−∞, 3/4], ϑ = 0 on [7/8, ∞) and |ϑ'| ≤ 16. Such a function exists, since the interval [3/4, 7/8] has length 1/8. Put χ(u) := ϑ(|u|/r_in) for u ∈ ℝ³. Then χ is smooth, |∇χ| ≤ 16/r_in, χ = 1 on B(0, ¾r_in), and the support of χ is a compact subset of B(0, r_in) ⊂ K_b.

Fix y_{≠b} ∈ Π_{b'≠b}K_{b'}. The function u ↦ e^{−H(u, y_{≠b})}χ(u) is C¹ on ℝ³, extended by 0 outside the support of χ, and has compact support in K_b. So ∫_{ℝ³}∂_a(e^{−H}χ)du = 0 for each coordinate a: integrate along each line in direction a (fundamental theorem of calculus, compact support), then over the other two coordinates. Integrating over y_{≠b} (Fubini) gives ∫_𝒲∇_b(e^{−H(y)}χ(y_b))dy = 0. Therefore

  Zν(∇_bH) = −∫_𝒲∇_b(e^{−H})dy = −∫_𝒲∇_b(e^{−H}(1 − χ(y_b)))dy = ∫_𝒲[(1 − χ)∇_bH + ∇χ]e^{−H}dy.

Both 1 − χ(y_b) and ∇χ(y_b) vanish unless |y_b| > ¾r_in. Also |1 − χ| ≤ 1, |∇_bH| ≤ G_b and |∇χ| ≤ 16/r_in. ∎

### 4.7 Where the means are

**Proposition 4.7 (location of the means)** [proved from Lemmas 4.4–4.6]. Let 𝒲 satisfy (CL)(W), A satisfy (CL)(A), 𝐅 ∈ E, and let P be C² on an open neighbourhood 𝒩 = −𝒩 of the closure of 𝒲 with |∂_bP| ≤ p₁ and ‖P''‖_op ≤ p₂ ≤ a_−/4 on 𝒲. Let H := ½⟨y, Ay⟩ + ⟨𝐅, y⟩ − P and ν := Z^{−1}𝟏_𝒲e^{−H}dy. Put

  λ := a_− − p₂ ≥ ¾a_−,  𝐦 := −A^{−1}𝐅,  G := a_+S_d(c_A)r_out + |𝐅|_∞ + p₁,  ε_W := 6(G + 16/r_in)e^{−λr_in²/24}.

Suppose (i) |𝐦|_∞ ≤ r_in/8 and (ii) K_∞(p₁ + ε_W) ≤ r_in/16. Then the mean m := ν(Y) satisfies

  |m − 𝐦|_∞ ≤ K_∞(p₁ + ε_W).   (4.1)

*Proof.* *The path.* For s ∈ [0, 1] put P_s(y) := ((1 + s)/2)P(y) + ((1 − s)/2)P(−y), defined on 𝒩, and H_s(y) := ½⟨y, Ay⟩ + s⟨𝐅, y⟩ − P_s(y), with ν_s := Z_s^{−1}𝟏_𝒲e^{−H_s}dy and m(s) := ν_s(Y). Then H_1 = H. For y ∈ 𝒲 (so −y ∈ 𝒲) we have |∂_bP_s(y)| ≤ p₁ and ‖P_s''(y)‖_op ≤ p₂, since P_s'' is a convex combination of P''(y) and P''(−y). Hence Hess H_s ≥ (a_− − p₂)Id = λ Id on 𝒲, so Lemma 4.4 applies to every ν_s. Also sup_𝒲|∇_bH_s| ≤ G for every b, because |(Ay)_b| ≤ Σ_{b'}a_+e^{−c_Ad(b,b')}|y_{b'}| ≤ a_+S_d(c_A)r_out.

*The even end.* H_0(−y) = H_0(y) and 𝒲 = −𝒲, so ν_0 is invariant under y ↦ −y and m(0) = 0.

*Continuity.* (s, y) ↦ H_s(y) is continuous and bounded on [0, 1] × (closure of 𝒲), and 𝒲 is bounded. By dominated convergence, s ↦ m(s) is continuous.

*The identity.* ∇H_s(y) = Ay + s𝐅 − ∇P_s(y). Taking ν_s-expectations, ν_s(∇H_s) = Am(s) + s𝐅 − ν_s(∇P_s), so

  m(s) = s𝐦 + A^{−1}(ν_s(∇H_s) + ν_s(∇P_s)).   (4.2)

*The bootstrap.* Let S := {s ∈ [0, 1] : |m(s)|_∞ ≤ r_in/4}. S contains 0, and S is closed by continuity. Let s ∈ S and b ∈ I. For each coordinate a, Lemma 4.4 with ℓ the a-th unit vector of the block b gives ν_s(|Y_b^a − m_b^a(s)| ≥ r_in/(2√3)) ≤ 2e^{−λr_in²/24}. If |Y_b| > ¾r_in, then |Y_b − m_b(s)| > ½r_in, because |m_b(s)| ≤ ¼r_in, and so some coordinate deviates by more than r_in/(2√3). Hence ν_s(|Y_b| > ¾r_in) ≤ 6e^{−λr_in²/24}. Lemma 4.6 gives |ν_s(∇_bH_s)| ≤ ε_W for every b. By (4.2) and Lemma 4.5,

  |m(s) − s𝐦|_∞ ≤ K_∞(ε_W + p₁),  hence |m(s)|_∞ ≤ r_in/8 + r_in/16 < r_in/4,

by (i) and (ii). By continuity, every s' ∈ [0, 1] close to s also has |m(s')|_∞ < r_in/4, so S is open in [0, 1]. Since [0, 1] is connected, S = [0, 1]. At s = 1 the displayed bound is (4.1). ∎

*Remark 4.8 (what the proof uses and what it avoids).* The proof uses convexity of H on 𝒲, the force bound (i) and the windows. It does not use a lower bound on any cutoff probability, a maximum principle for A, evenness of the actual law, correlation decay or the Helffer–Sjöstrand representation. Evenness is used only at the starting point s = 0, where it is exact. The two effects that SA names as the obstacle at SA L28209–28213 are handled thus. The exterior force is the term s𝐦, kept below r_in/8 by SA's collar device. Old activities enter only through P, which (CL)(P) asks to have a small Hessian.

---

## 5. The trigger bound

### 5.1 One step

Put τ_{i−1} := θ_col𝔟_{i−1}/(2c_N). Consider the following conditions on the level i − 1, each a ceiling on g or a floor on x (§6):

- (Q) C_ϱg_{i−1}r_out² ≤ ½θ_col𝔟_{i−1};
- (M) K_∞C_𝐂(p₁ + ε_W) ≤ τ_{i−1}/(4√3) and K_∞(p₁ + ε_W) ≤ r_in/16;
- (D) LMŘ_i ≥ 2R_𝐂 + 1 and C_𝐂C_𝐦𝔟_{i−1}e^{−μ'(2LMŘ_i − R_𝐂 − 1)} ≤ τ_{i−1}/(4√3).

**Proposition 5.1 (deep triggers at one step)** [proved from (CL), Lemma 4.4, Corollary 4.5′, Proposition 4.7]. Assume (CL), (Q), (M) and (D). Let h be a history and i a level. Let 𝔅_i be a set of bonds of level i − 1 with distinct cells 𝔡(b) and pairwise disjoint 𝔡(b)^{+2}, such that each b satisfies the geometric conditions of Trig_i(b) in h. Then for almost every R,

  ν_R(∩_{b∈𝔅_i}Trig_i(b)) ≤ (6e^{−c₁θ_col²𝔟_{i−1}²})^{|𝔅_i|},  c₁ := λ/(96c_N²C_𝐂²).   (5.1)

*Proof.* *Depth.* A level-i cell has side MŘ_i level-i units, which is LMŘ_i level-(i − 1) units. No cell of Z_i^{pre} meets 𝔡(b)^{+2}, and Ω_i ∖ Λ_i^{pre} and Ω_i^c lie in Z_i^{pre}. So d(b, (Λ_i^{pre})^c) ≥ 2LMŘ_i − 1 (two layers of cells, less one lattice unit for the bond convention), and every b' with d(b, b') ≤ R_𝐂 has d(b', (Λ_i^{pre})^c) ≥ 2LMŘ_i − R_𝐂 − 1 ≥ R_𝐂, by the first part of (D). So (CL)(ℓ) applies to b, and every bond read by ℓ_b is in I.

*From the event to linear statistics.* On Trig_i(b), (CL)(ℓ) and (Q) give ‖ℓ_b(Y)‖_B ≥ θ_col𝔟 − C_ϱgr_out² ≥ ½θ_col𝔟, hence |ℓ_b(Y)| ≥ τ := τ_{i−1}. A vector v ∈ ℝ³ with |v| ≥ τ has a coordinate of absolute value ≥ τ/√3. So there is u_b ∈ U := {±e_1, ±e_2, ±e_3} with ⟨u_b, ℓ_b(Y)⟩ ≥ τ/√3. Hence

  ∩_{b∈𝔅_i}Trig_i(b) ⊂ ∪_{u∈U^{𝔅_i}}{⟨L_u, Y⟩ ≥ |𝔅_i|τ/√3},  L_u := Σ_{b∈𝔅_i}ℓ_b^𝖳u_b ∈ E.

*The size of L_u.* The vector ℓ_b^𝖳u_b has norm ≤ C_𝐂 and is supported on the bonds within R_𝐂 of b. Two bonds of 𝔅_i lie in cells whose two-layer neighbourhoods are disjoint, so their distance is at least 4LMŘ_i − 1 > 2R_𝐂. The supports are disjoint, the vectors are orthogonal, and |L_u|² ≤ C_𝐂²|𝔅_i|. If L_u = 0, the event {⟨L_u, Y⟩ ≥ |𝔅_i|τ/√3} is empty; otherwise Lemma 4.4 applies below.

*The mean of the statistic.* By Proposition 4.7, whose hypotheses (i) and (ii) are (CL)(F) and (M), and by Corollary 4.5′ and (D), every b' within R_𝐂 of a bond of 𝔅_i satisfies

  |m_{b'}| ≤ |𝐦_{b'}| + K_∞(p₁ + ε_W) ≤ C_𝐦𝔟e^{−μ'(2LMŘ_i − R_𝐂 − 1)} + K_∞(p₁ + ε_W) ≤ τ/(4√3C_𝐂) + τ/(4√3C_𝐂) = τ/(2√3C_𝐂).

So |ν_R(ℓ_b(Y))| = |ℓ_b(m)| ≤ C_𝐂max_{d(b',b)≤R_𝐂}|m_{b'}| ≤ τ/(2√3), and ν_R⟨L_u, Y⟩ ≤ |𝔅_i|τ/(2√3).

*The tail.* By Lemma 4.4, for each u ∈ U^{𝔅_i},

  ν_R(⟨L_u, Y⟩ ≥ |𝔅_i|τ/√3) ≤ ν_R(⟨L_u, Y⟩ − ν_R⟨L_u, Y⟩ ≥ |𝔅_i|τ/(2√3)) ≤ exp(−λ|𝔅_i|²τ²/(24|L_u|²)) ≤ exp(−λ|𝔅_i|τ²/(24C_𝐂²)).

There are 6^{|𝔅_i|} choices of u. Finally τ² = θ_col²𝔟²/(4c_N²). ∎

### 5.2 All levels: positivity

**Proposition 5.2 ((TT-hist))** [proved from (CL)(0) and Proposition 5.1]. Assume (CL), and (Q), (M), (D) at every level i ≤ k. For every history h of level k and every 𝔅 as in (TT), with 𝔅_i := {b ∈ 𝔅 : i(b) = i},

  t(h; ∩_{b∈𝔅}Trig_{i(b)}(b)) ≤ Π_{i≤k}(6e^{−c₁θ_col²𝔟_{i−1}²})^{|𝔅_i|}·t(h).   (5.2)

*Proof.* Put T_{≤n} := ∩_{b∈𝔅, i(b)≤n}Trig_{i(b)}(b) and ε_n := (6e^{−c₁θ_col²𝔟_{n−1}²})^{|𝔅_n|}. If some b ∈ 𝔅 fails the geometric conditions of Trig in h, the left side of (5.2) is 0. Otherwise, let Claim(n) be: for every measurable Γ ≥ 0 that is a function of the state S_n,

  t(h; 𝟏_{T_{≤n}}·Γ(S_n)) ≤ (Π_{j≤n}ε_j)·t(h; Γ(S_n)).

Claim(0) holds with equality: there are no triggers of level 0, since Trig_i is defined for i ≥ 1. Assume Claim(n − 1), and let Γ be a function of S_n. By (CL)(0b)–(0c), 𝟏_{T_n}·Γ(S_n), where T_n := ∩_{b∈𝔅_n}Trig_n(b), is a function of (Y^{(n)}, R^{(n)}) and hence of S_{n−1}. Claim(n − 1) applied to it gives

  t(h; 𝟏_{T_{≤n}}Γ(S_n)) = t(h; 𝟏_{T_{<n}}·[𝟏_{T_n}Γ(S_n)]) ≤ (Π_{j<n}ε_j)·t(h; 𝟏_{T_n}Γ(S_n)).

By (CL)(0c), Γ(S_n) is a function of R^{(n)}. By the disintegration (CL)(0d) and Proposition 5.1,

  t(h; 𝟏_{T_n}Γ(S_n)) = ∫Γ(S_n(R))·ν_R(T_n)·t(h; dR) ≤ ε_n·t(h; Γ(S_n)),

where t(h; dR) is the image of t(h; ·) under R^{(n)}. This is Claim(n). Claim(k) with Γ ≡ 1 is (5.2). ∎

*Why positivity is enough.* The later steps act on the state S_n by positive kernels, and none of them reads Y^{(n)} ((CL)(0a)). So the one-step bound needs no control of the later steps. The earlier steps enter only through the effective density, and Claim(n − 1) is applied to a nonnegative test function. This is the step that R2 L736 described in words.

### 5.3 The theorem

**Theorem 5.3 ((TT))** [proved from (CL), R2 Lemma 10.1 and (MB)]. Let x_k ≥ max(X₁, X_TT), where X₁ is the floor of (MB) (R2 Lemma E.4) and X_TT is the floor at which (Q), (M), (D) and p₂ ≤ a_−/4 hold for all i ≤ k (§6). Then (TT) holds with

  c_T := c₁θ_col²(A₁/A₀)²/4 = λθ_col²(A₁/A₀)²/(384c_N²C_𝐂²),  C_T := log 6.

*Proof.* 𝔟_{i−1} = (A₁/A₀)p₀(g_{i−1}), and p₀(g_{i−1}) ≥ ½p₀(g_i) for γ small (IN1 L490). So c₁θ_col²𝔟_{i−1}² ≥ c_Tp₀(g_i)², and (5.2) is (TT-hist) with these constants. R2 Lemma 10.1 gives (1.1). ∎

**Remark 5.4 (hypotheses not used).** (i) The proof does not need the 𝔡(b)^{+2} to be disjoint from the ancestors of the designated cells. That hypothesis of R2 L170 may be dropped. (ii) The depth actually used is 2LMŘ_i − 1 level-(i − 1) units, through (D). Any depth D_T ≥ 2R_𝐂 + 1 with C_𝐂C_𝐦e^{−μ'(D_T − R_𝐂)} ≤ θ_col/(8√3c_N) would do, and that is a fixed number of lattice units. R2's two cells is far more than needed. I do not change R2's definition. (iii) Triggers at different levels are paid at different steps, and no separation between levels is needed.

**Remark 5.5 (the payer is the one SA names).** SA L23328 says the price of a trigger is borne by the conditional law of the fluctuation field in its box. Proposition 5.1 is that statement, with "box" replaced by the whole small-field region Λ_i^{pre} of the step. The replacement is necessary (N2, §7.2).

---

## 6. Constants and their order

The IN1 constraint: every constant that a choice before κ reads must be fixed before κ, independent of M and κ̄, and M may appear only as a lower bound. The constants introduced here, in order:

| Constant | Where | Fixed | Depends on | M, κ̄ |
|---|---|---|---|---|
| c_N | §1.1 | absolute | the norms on su(2) | independent |
| U (6 directions), C_T = log 6 | Prop. 5.1, Thm 5.3 | absolute | — | independent |
| C_𝐂 ≥ 1, R_𝐂, C_ϱ | (CL)(ℓ) | with L | Balaban's 𝐂 (blocks of side L) | independent |
| a_−, a_+, c_A | (CL)(A) = (I-1) | with L (IN1 L57: L and `c4-order.md` rows 1–7) | L | independent |
| μ, K_∞, S_d(·) | Lemma 4.5 | with L | a_−, a_+, c_A, d = 4 | independent |
| C_h, c_h | (CL)(F) | with L | the operator Δ, 𝐂, and SA's stored bound C (SA L17360) | independent |
| C_𝐦, μ' | Cor. 4.5′ | with L | C_h, c_h, a_−, μ | independent |
| λ = a_− − p₂ ≥ ¾a_− | Prop. 4.7 | with L (given p₂ ≤ a_−/4) | a_− | independent |
| c₁ = λ/(96c_N²C_𝐂²) | Prop. 5.1 | with L | λ, c_N, C_𝐂 | independent |
| room (5.4′) | §3.2 | at SA's positions: θ_c first, (Θ₁, ϖ_T) after M₂ and before M (SA L19469) | SA's C | a floor on M only (third part) |
| c_T | Thm 5.3 | after A₁/A₀ (SA L19469: (A₁, A₀, …) after M) | c₁, Θ₁, A₁/A₀ | depends on A₁/A₀ |
| C_π, ρ_{i−1}, p₁, p₂ | (P-an) | NL1's constants; C_π may depend on M | NL1 | enter only ceilings on g |
| r_in, r_out, τ_{i−1}, G, ε_W | §3–5 | functions of g_{i−1} | 𝔟_{i−1} | — |
| X_TT | Thm 5.3 | last: a ceiling on g | everything above | — |

*The two constants that are not independent of M.* c_T contains (A₁/A₀)², and C_π may depend on M. Both enter AG1 only through (F4) of R2 Theorem 7.4 and through X_TT. Those are conditions x_k ≥ X_F, that is, ceilings on g, the last choice. No constant chosen before g reads c_T or C_π, so no cycle arises. This is the same situation as R2's C_q (R2 L712).

*The ceilings that make up X_TT.*
- (Q): C_ϱ(25c_N²/16)g𝔟 ≤ θ_col/2.
- (M): K_∞C_𝐂(√3C_π/ρ_{i−1} + ε_W) ≤ θ_col𝔟/(8√3c_N). Since 𝔟 → ∞, ρ → ∞ and ε_W ≤ C𝔟e^{−λθ_c²𝔟²/(24c_N²)} → 0, this holds for x large. The second half of (M) follows from the first, because θ_col ≤ θ_c and C_𝐂 ≥ 1.
- (D): LMŘ_i ≥ 2R_𝐂 + 1 and e^{−μ'(2LMŘ_i − R_𝐂 − 1)} ≤ θ_col/(8√3c_NC_𝐂C_𝐦). Since Ř_i ≥ Ř_k ≥ (log x_k)^r, both hold for x_k large and every M ≥ 1.
- p₂ = 6C_πS_d(κ)/ρ_{i−1}² ≤ a_−/4.
- (F4) of R2 Theorem 7.4 with ϰ_i = min{2c_ar_i − C_D, c_Tp₀(g_i)² − C_T}. It holds for x large, because p₀² has degree 2𝔭₀ > 5r in log x (R2 L604).

---

## 7. The three attacks, and their relation to T1–T5

### 7.1 Attack N1: convexity on the whole small-field region (this draft)

*Idea.* Do not localise. Use the conditional law of the step on all of Λ_i^{pre}, given what the run keeps. Under (CL) this is a uniformly convex Gibbs measure on a product of symmetric convex windows. Then use three facts: linear statistics are sub-Gaussian with no volume factor (Lemma 4.4), the means are located by integration by parts and continuity (Proposition 4.7), and SA's collar device bounds the force everywhere (SA L17363).

*Outcome.* (TT) is proved from (CL) (Theorem 5.3).

*Where it could fail.* Only through (CL). If (CL)(P) fails anywhere in Λ_i^{pre}, Lemma 4.4 is lost on the whole of Λ_i^{pre}, since convexity is a global hypothesis. If the inner tests read pivot bonds, (CL)(W) can fail (the design point of §3.2).

### 7.2 Attack N2: convexity on a box (CA's class form)

*Idea.* Use CA's box form of class membership (CA-II L84948–85075), which is proved there conditionally under (a)–(j): fix a box I around the deep bond and freeze the exterior free bonds y_F, those of Λ_i^{pre} ∖ I included. Lemmas 4.1–4.6 apply verbatim to the box law.

*Exact reason it fails.* Hypothesis (i) of Proposition 4.7 fails. The force on the box is 𝐅^I = A_{IF}y_F. The exterior y_F is only known to lie in its windows, so at a box bond next to ∂I, |𝐅^I_b| can be of order a_+r_out. The Gaussian mean 𝐦^I = −A_{II}^{−1}𝐅^I can then be of order a_+r_out/a_− ≥ r_out > r_in/8. The continuity argument cannot start. Lemma 4.6 then gives only |ν(∇_bH)| ≤ G at bonds near ∂I, and through A^{−1} these forces move the mean at depth d by up to K(d)·G with K(d) ~ e^{−μd}. A graded argument controls the mean only beyond the depth where K(d)G ≤ r_in/16. The bonds in between remain uncontrolled. The bootstrap would have to be run again on a region whose boundary bonds are uncontrolled, which is the same situation, so it does not close. Without a maximum principle nothing prevents the gauge fluctuation operator's Dirichlet extension from exceeding its boundary data. T1 records the analogous constant C_K (R2 L740). CA-II L84195–84201 records this obstruction. CA avoids it by a decoupling interpolation whose correlation decay rests on an *assumed* Helffer–Sjöstrand representation (CA-II L83870). That is not an elementary statement, and I do not adopt it.

*Lesson.* A box boundary inside Λ carries no test that keeps the exterior field away from the window edge. SA's rounds provide such a test only on ∂Λ (SA L17354–17364). So (CL) must be stated on the whole region. N2 differs from T5: T5 bounded oscillations and needed a lower bound on a denominator; N2 needs no denominator and fails only at the mean.

### 7.3 Attack N3: redesign the trigger at a coarser resolution

*Idea.* Replace the potential collar and rim tests at deep bonds by a test of the averaged field at level i, or relate a deep trigger to a test of level i − 1. A trigger would then become a recorded large-field event, paid by C3 like any creation (IN1 Lemma C.3).

*Exact reason it fails.* Two facts.
- (a) *The block average of a fluctuation vanishes to first order.* The level-(i − 1) field and the background have the same level-i block averages: 𝓜V_{i−1} = V_i, and the background is the average of a configuration whose level-i average is V_i (CA-II L79896–79910). The constraint is removed with 𝐂 after linearisation (CA-II L79911–79918). So the block average of 𝒜_{i−1} is O(‖𝒜‖²). For a deep trigger this is at most O(δ²) ≪ θ_colδ. A test of averages cannot see a deep trigger.
- (b) *A deep trigger fails no test of any level.* Its bond lies in Λ_i^{pre}, so it passed the third test at δ_{i−1} > θ_colδ_{i−1}. The tests of level i − 1 read other quantities: plaquettes of V_{i−1} at ε_{i−1}, and the fluctuation 𝒜_{i−2} of the previous step. A fluctuation of size θ_colδ_{i−1} at one bond fails none of them. Only a new test at threshold ≤ θ_colδ_{i−1} on Λ_i could record it. The pass branch of such a test cuts the Λ-integral at θ_colδ, and that is T1/T2 again: the mean bound near the holes this creates needs a 2/5 sup-norm contraction (R2 L740–741).

*Lesson.* A deep trigger is a sub-threshold event of the step's own integration variable. No coarser record sees it. Its price must come from the tail of the conditional law, which is what N1 bounds.

### 7.4 A second conditional route, and the relation to T1–T5

*Remark 7.1 (the regular gas).* SA's regular polymer gas carries signed failed-bond tests. Its local Gaussian comparison gives a tail factor p per distinct failed bond (SA L14389–14401, (UM6)), and its integral bound carries p^v (SA L14518–14530, (UM15)). A deep trigger could be inserted as a forced failed bond at the radius θ_col𝔟, with tail of order e^{−γ_tiltθ_col²𝔟²/2}, where γ_tilt ≍ (LM)^{−4} (IN1 L296). A ratio estimate for the hard-core expansion with forced polymers would then give (TT-hist) with c_T ≍ γ_tiltθ_col²(A₁/A₀)². This route needs (UM4)–(UM6), which SA assumes (index rows 14373–14401), and the identification of the gas with the step integral (SA L14262–14266, assumed). It also needs the exterior force and the old activities in the complete conditional law, which SA leaves open (SA L28209–28221). Its inputs are heavier than (CL), so I do not use it.

*Relation to T1–T5.*
- N1 and N2 use convexity and a mean argument. T1–T5 used neither.
- N1 does not redesign the tests (unlike T1, T2) and does not use the bare action (unlike T3).
- N1 uses no monotonicity (unlike T4) and no box conditioning (unlike T5).
- N2 is the convex analogue of T5. It locates T5's failure precisely: the issue is the mean, not the denominator.
- N3 is the coarse-resolution redesign the lead suggested. It reduces to T1/T2 for the reason in §7.3(b).

---

## 8. What AG1 then still needs

### 8.1 Theorem AG after this draft

**Theorem AG (R2 L80), updated.** (0.1*) holds at every level k with x_k ≥ max(X_F, X_TT), with ϖ_k = δ𝗇MŘ_k/512. It is proved as an implication from (K)+(MI), (COV), (SM), (RS), (BGL), (R0)–(R3), (LT), LG1(3), and (CL) with the room (5.4′), through R2 Theorem 7.4, R2 Theorem 6.7, R2 Lemma E.4 and Theorem 5.3 here. Status: [proved] as that implication. AG1 has no statement of its own left Outstanding.

### 8.2 The inputs, with owners

| Input | Owner | Status as recorded | Used in |
|---|---|---|---|
| (K)+(MI-1)–(MI-7) | LF1(1) | (I-6) [C]; (MI) additions [design] | R2 §3.1, §5.2 |
| (COV) | LF1 | stated, proof incomplete (CA-III L111428, via R2 L136) | R2 Lemma 3.1 |
| (SM) with rooms (5.1)–(5.6) | LF1 [design] | R2 Theorem 5.4; item 16 (ST1 admission) a requirement on ST1 | R2 §5 |
| (5.4′) | LF1, SA's constants | a numerical strengthening of SA L17364 | (CL)(F) |
| (RS) | LF1(2) | checked against SA L17317–17610 only | R2 §6 |
| (BGL) | BG1/PR1 | checked conditional; the reading W = W̃ ∩ Ω₀ flagged | R2 §6.2 |
| (R0)–(R3) | LF1(2) | inputs; (R2) is the chain form of CA's age lemma (proof incomplete in CA) | R2 §4 |
| (LT) | LF1(3) | ⟦LF-mass⟧ open in the assembly; fraction ¼ not checked | R2 Lemma E.4 |
| LG1(3) | assembly [C] | — | R2 Lemma 3.1 |
| **(CL)(0), (W), (A), (F), (ℓ)** | NL1, PR1(1), LF1(1) | derived in §3.2 from (I-1) [C], SA L17351–17364, CA-II L79847–80060, R2 Theorem 5.4; the free-bond design point of (W) | Prop. 5.1, 5.2 |
| **(CL)(P), via (P-an)** | NL1, LF1(4)–(5) | **not stated by any owner**; box form proved conditionally by CA (CA-II L84948–85075); not asserted by SA (SA L28219–28221) | Lemma 4.4, Prop. 4.7 |

### 8.3 The first remaining statement on AG1's path

AG1 has no Outstanding statement of its own. The first input on its path that no owner has yet stated is **(CL)(P) on all of Λ_i^{pre}**, in the form (P-an):

> For every history h, level i and value of the retained variables R, the non-Gaussian exponent P of the step-i conditional law of the scaled fluctuation on the free bonds of Λ_i^{pre} is a finite sum Σ_XP_X of functions, each holomorphic on the tube 𝒯_ρ of radius ρ ≥ c_ρ(log θ_{i−1})^{q₁} about the window (some fixed q₁ > 0), real on real points, depending only on the bonds of X, with Σ_{X∋b,b'}sup_{𝒯_ρ}|P_X| ≤ C_πe^{−κd(b,b')} and C_π independent of the level, the history, the volume and g.

Within it, part (d) is the one not covered by any library statement. The factor of a component healed at an earlier level, as a function of the level-(i − 1) field near it, must have a logarithm that is holomorphic and bounded on such a tube. A tube of radius about (log θ)^q/(C_ΨV°) suffices, since V° ~ (log θ)^{5r} and q > 5r. (I-8) gives Re Ψ_ω ≤ C_ΨV° (IN1 L90–94), which is the upper half. Turning it into a two-sided bound needs Ψ_ω real at real arguments, uniformly in the outer record ω, followed by Borel–Carathéodory (§3.3). Parts (a)–(c) are the analyticity of the step (I-5) on its product box, read as functions of the step's fluctuation.

### 8.4 Checks AG1 now needs

- One check, by another model, of §4 and §5: Lemmas 4.1–4.6 and Propositions 4.7, 5.1 and 5.2. They are self-contained finite-dimensional analysis.
- A check of §3.2: that (CL)(0), (W), (A), (F), (ℓ) follow as stated, in particular the free-bond design point of (W) and the room (5.4′).
- NL1 and LF1(4)–(5) must state (P-an), including part (d). If NL1 prefers CA's box form, AG1 cannot use it without a localisation theorem (N2).

---

## 9. Status of every statement in this draft

| Statement | Where | Status |
|---|---|---|
| R2 Lemma 10.1 (reduction to (TT-hist)) | §1.2 | [proved in R2] |
| (CL) | §3.1 | [input: NL1 with PR1(1), LF1(1), LF1(4)–(5); new] |
| (CL)(0), (W), (A), (F), (ℓ) from named inputs | §3.2 | derived from (I-1) [C], SA L17351–17364, CA-II L79847–80060, R2 Theorem 5.4; (W) needs the design point (free bonds) |
| (5.4′) | §3.2 | [design/room], SA's conditions with a numerical factor |
| Lemma 3.1 (Cauchy) | §3.3 | [proved] |
| (P-an) | §3.3 | [input]; part (d) not stated by any owner |
| Lemma 4.1 (Prékopa–Leindler, 1D) | §4.1 | [proved] |
| Lemma 4.2 (PL in ℝ^q; marginals) | §4.2 | [proved] |
| Lemma 4.3 (1D variance bound, exponential moment) | §4.3 | [proved] |
| Lemma 4.4 (sub-Gaussian linear statistics on convex windows) | §4.4 | [proved] |
| Lemma 4.5, Corollary 4.5′ (Combes–Thomas; Gaussian mean at depth) | §4.5 | [proved] |
| Lemma 4.6 (wall force) | §4.6 | [proved] |
| Proposition 4.7 (location of the means) | §4.7 | [proved] |
| Proposition 5.1 (one step) | §5.1 | [proved] from (CL), (Q), (M), (D) |
| Proposition 5.2 ((TT-hist)) | §5.2 | [proved] from (CL)(0) and Prop. 5.1 |
| Theorem 5.3 ((TT)) | §5.3 | [proved] from (CL), R2 Lemma 10.1, (MB) |
| Remarks 5.4, 5.5 | §5.3 | [proved] |
| Attack N1 | §7.1 | succeeds from (CL) |
| Attack N2 | §7.2 | fails: hypothesis (i) of Prop. 4.7 (force at a box boundary) |
| Attack N3 | §7.3 | fails: block averages vanish to first order; reduces to T1/T2 |
| Remark 7.1 (regular gas route) | §7.4 | conditional on heavier inputs; not used |
| Theorem AG, updated | §8.1 | [proved] as an implication; no AG1-own Outstanding statement |

*RAM and method.* No computation was run. Every source was read in bounded ranges, cited above.

End of round 3 (TT). Line count: see the final line.


This file has 485 lines.
