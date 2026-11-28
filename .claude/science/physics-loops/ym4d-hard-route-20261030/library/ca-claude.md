lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:43Z

# CA, completion-collar admission: Claude proof attack (FINISH row 347)

Provenance: Claude Opus 5.5, max effort, Mac mini worker; checkout pinned at `98d2f9435`; 2026-11-06. Research text, not an audit, no status. Proved by Claude, not yet checked by the other model. No computer-assisted step and no numerical run was used.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number below; Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier lanes in this repository: `arr.md` (two rounds), `crca.md`, `prior/ca-claude.md`.

Kind of result (How we work, item 9): proof of a step the account assumes (its collar corollary, I:142283-142291, in the weaker CA form), as an implication from named inputs. One named input, the base bound on the core (B-in), is used by the account and printed nowhere.

## 0. Summary

1. **Seed, pinned part: proved (Lemma A).** On every stratum bond of a removed collar, the completion seed equals the raw real datum, exactly. The rows come from Balaban's splice formula and a separation the account proves. So at b2 the plaquette entries are below 0.04 r1(0), and A' = 0. This settles, for stratum bonds, the datum identification that ARR section 15.2 left open.
2. **Seed, side plaquettes, current and cubes: proved as an implication (Lemma B)** from one account input, the base bound on the core (I:136724-136733, I:138438-138450), used only at cells of level at least one. The account prints no statement or proof of that bound. Result: the seed current is at most 0.48 r3(0), and the index-zero cube clause holds.
3. **Sharpened criterion (Proposition C).** Lemmas A, B and the collar layer bound (CL) imply CA. The layer budget in (CL) is 48 times weaker than ARR (18.4).
4. **The layers: (CL) proved for gamma small (Lemma E, Proposition F).** The account's cut-localisation bound alone gives (CL) only up to a density ceiling k*(gamma): the old raw radius scales with the bare coupling g0, the layer sources with gk, and the account's separation of Z_h from the cut does not grow with k (section 6.1). Lemma E adds the zones of levels 1 to h-1 between the raw collar and the cut: by the account's admissible geometry each is at least L cells thick, so the scaled distance grows like (L-2)(h-1). With the response-field theorem and the source identity applied as the account applies them, this gives (CL) uniformly, under one more ceiling on gamma chosen last.
5. **Result: Proof, as an implication.** CA holds from the account's retained inputs plus the named inputs listed in the Result. The first place it can fail is (B-in).

## 1. Sources and scope

- Read first: `library/prior/ca-claude.md`; `library/arr.md` sections 2-3, 10-18 and Result; `library/crca.md` section 3; `library/open-core.md` sections 1 and 7; the CA row of `library/open-registry.md` (owner `ca-claude`, state open, so no duplicate lane).
- Account sources: fetched by URL from the Sussman-Alpoge repository into a scratch folder of this lane. SHA-256 values agree with `arr.md` section 1. Line numbers below are of those raw TeX files.
- Balaban CMP 122a and 122b are not in `~/ym4d-papers`. Project Euclid answered with a bot check (Incapsula), so the fetch stopped there, as the rules require. CMP 122a/b statements are used only as the account quotes them.
- The level-zero chain proposition and the collar corollary of I:142269-142291, and the cube admission of I:142950, are not used anywhere below.

## 2. Consumer strategy

**Who reads CA.** The consumers are listed in `crca.md` sections 3.2-3.3: clause (e4)' of `4.27:thm-collar-rigidity`, newborn continuation and old-term composition, the arrest uses K1, K2, K7, and the frozen leftovers of the correlation induction (II:25188-25200). Each needs image membership in the old dated raw clause at every removed collar point, for every source, parameter and segment, with the cube clause.

**No entry can be dropped.** A stored term whose domain meets a completed component is absorbed into Balaban's term V(Y) at that completion (I:132301-132303). The absorption evaluates the term on the presented chain at b2, b3, b4. So the old clause is read on the full chain, seed and layers together. No consumer reads only the real seed, a real slice, or a subset of the five entries. I agree with the digest: no weaker all-consumer statement than CA exists.

**What the consumers' threshold buys.** CA's threshold is f0(d^t) r_a(0) with f0 > 3.65 (ARR (10.3)), not the 1/16 that the account assumes. Sections 3-4 show that the seed uses at most 0.04 of r1(0), r5(0) and 0.48 of r3(0). The room left for the two layers is therefore large. Section 5 turns this into the layer budget

  epsilon := F3 + F4 <= min{ 1/85 , (3/Kcur) alpha_{*,0} },   Kcur = 3 + 18d + 2.2 KJ,

where ARR (18.4) asked for min{1/160, alpha_{*,0}/(16 K*)} with K* = Kcur. This weaker statement (CL) is the one attacked in section 6.

## 3. Lemma A: the seed on the stratum bonds is the raw datum (new attack 1, closes)

**Notation.** d' = (k;L) is a completion date, d^t its scaffold predecessor, C a completing component, Z the class of the step, h := k - N_k. The set of d^t is B''_k (fact (f), I:142305-142306), and h >= 1 there (I:142307). Put

  Omega := ((Omega''_{h+1})^~)^c,   B_2 := B''_k u B_h(Omega),   U_2 := U_{B_2}(V_2)

(CMP 122b (1.52)-(1.53), quoted at I:92417-92421). St(d^t) = Omega_0(B''_k) \ Omega_1(B''_k), and Col(C) = St(d^t) n C. A stratum bond has both ends in St(d^t); a pinned plaquette has four stratum bonds (I:141013-141014).

**Account inputs, each used on its stated class.**

- (a1) *Position of the collar.* St(d^t) is outside Omega_1 and Omega_1^c is in Z_1 (first-step geometry, used at III:51160-51177, ARR (16.1)); Z_1 is in Z_h by the nesting Omega_{j+1} in Lambda_j in Omega_j (CMP 119 (2.1)-(2.3)); and Omega''_j = Omega_j for j <= h (CMP 122a, quoted at I:92002-92003). So Col(C) is in Z_h. Fact (f) states the same placement: Col(C) is in Z_{h'} n C and in the core (I:142309, I:142583-142586).
- (a2) *Separation of Z_h from the cut.* `4.22:lem-law-site` (PROVED), proof at I:91991-92024: one full layer of MR_{h+1}-cubes of level h+1 (= LMR_{h+1}-cubes of level h) separates Z'_h, which contains Z_h, from (Omega''_{h+1})^{~2}; and Z_h is in D_2 := Z \ (Omega''_{h+1})^~ (I:91823), so Z_h is in Omega.
- (a3) *Splice.* Proof of `4.22:lem-current-localisation` (PROVED), I:92515-92532, read off CMP 119 (2.13)-(2.14): on D_2 the set B_2 has the blocks of B''_k, except in the graded layer Omega \ Omega^{~-2}, the points of Omega within two M_1-cubes of level h of the cut.
- (a4) *Level-zero rows.* CMP 119 (2.10)-(2.11): at level 0 the constraint is the identity, U(b) = V_0(b), where V_0 is the level-zero component of the datum (used at I:142680-142690).
- (a5) *Datum of the seed.* U_2 reads the raw configuration V'' of B''_k through its restriction off (Omega''_{h+1})^{~2} (I:138407-138411). The current-step variables stay real and unrotated (I:78445-78545, as read in ARR section 15).
- (a6) *Level-zero small field.* Input (a) of `4.27:lem-real-point-collar` (I:142611-142617): for real data V in the support of the characteristic functions of the density, every pinned plaquette within 2LMR^_1 of Omega_1 has |V_0(dp) - 1| < eps_0. With its inputs (c), (c'), eps_0 <= (phi_ARR/2.5) r_1(0) < 0.04 r_1(0) (I:142663-142668).

**Lemma A.** Let V be real and in the support of the characteristic functions. For every y in Col(C), every stratum bond b at y and every pinned plaquette p at y,

  U_2(b) = V_0(b),   dU_2(p) = V_0(dp),   |dU_2(p) - 1| < eps_0 < 0.04 r_1(0).

At b2 the presented pair is (U_2, J(U_2)) with A' = 0, so Q_1(y) = Q_5(y) < 0.04 r_1(0) and Q_6(y) = Q_7(y) = 0.

**Proof.**

*Step 1: b is a level-zero bond of B''_k inside C.* Both ends of b lie in St(d^t), hence outside Omega_1(B''_k), hence at level 0 of B''_k. The second end is a lattice neighbour of y. It lies in Z_k, since St(d^t) is in Z_1, which is in Z_k. Distinct components of Z_k are farther apart than one layer of LMR^_1-cubes (I:143030-143031), so the second end lies in C. Thus both ends lie in Col(C).

*Step 2: b is off the graded layer.* The graded layer consists of points within 2M_1 blocks of level h of the cut d((Omega''_{h+1})^~), and the cut lies in (Omega''_{h+1})^{~2}. The source set S of the current localisation is the (2M_1+3 blocks)-neighbourhood of (Omega''_{h+1})^{~2} in Lambda (I:92468-92469). So the part of the graded layer in Lambda lies in S. By (a1), y is in Z_h. The proof of (a2) gives d_sc(Z_h, S) >= R^_k - 1: the separating layer, "diminished by the 2M_1+3 blocks of S, which amount to less than one M-cube" (I:92095-92097). Since R^_k >= L >= 8 (I:20299, I:21526), every point within one lattice step of y is at scaled distance at least R^_k - 2 >= 6 from S, so outside S, hence outside the graded layer. (Those points lie in D_2, which is in Z''_{h+1}, hence in Lambda; I:92430.) Since y is in Z_h, which is in D_2 by (a2), (a3) applies at b: the block of B_2 at b is the block of B''_k, the bond b itself.

*Step 3: the value.* By (a4), the constraint of the row b is U_2(b) = V_2(b). The bond b lies off (Omega''_{h+1})^{~2} (Step 2), so by (a5) V_2(b) = V''(b). The datum of B''_k at a level-zero bond is the level-zero component of the datum: V''(b) = V_0(b). Hence U_2(b) = V_0(b). The constraint fixes the value at this row exactly; the plaquette norms below do not depend on the representative of the minimal orbit in any case.

*Step 4: plaquettes.* The four bonds of a pinned plaquette p at y are stratum bonds at points of Col(C), so Step 3 applies to each. The plaquette variable is the ordered product of the same four group elements, so dU_2(p) = V_0(dp). The point y lies within one layer of LMR^_1-cubes of Omega_1, so p lies within 2LMR^_1 of Omega_1, and (a6) gives |V_0(dp) - 1| < eps_0 < 0.04 r_1(0).

*Step 5: the entries at b2.* By fact (f), I:142310-142317, the base of the presented pair on the core is (U_2, J(U_2)) and the rotation is trivial there. U_2 is real, so A' = 0: Q_6 = Q_7 = 0, and Q_1(y), Q_5(y) are both the maximum of |dU_2(p) - 1| over pinned plaquettes p at y. Step 4 bounds it. QED.

**What Lemma A adds.** ARR section 15.2 proposed this shortcut and stopped because pda identifies neither the rows of the spliced B_2 nor their data. Steps 1-3 identify both from the splice formula (a3), the separation (a2) and the datum statement (a5). Lemma A does not reach plaquettes with a corner in Omega_1; the current at a stratum bond reads them (ARR section 15.2, last paragraph). Section 4 treats them.

## 4. Lemma B: side plaquettes, current and cubes of the seed (new attack 2, conditional on one account input)

**The input (B-in): the base bound on the core.** The account uses it in two proofs: of `4.27:prf-ambient-inclusion` (index: INCOMPLETE, at another step), I:136724-136733, and of `4.27:prf-room-dissolving` (index: PROVED), I:138438-138450. In the second form: on every cell x of D_2 \ B_S, the pair (U_2, J(U_2)) satisfies the defining inequalities of the analyticity spaces, derived entries included, with bound at most 1/64 of every threshold F w c r_a(n), for all F >= phi_flat, w >= 1, c >= 1 and n the current level of x or a finer birth index; on cubes, the cube clause with the gauges of its first clause.

*Its standing.* The account names its source as "the own-level bound for the configuration U_2 of the sealing construction" (I:138438). I found no statement and no proof of a sealing construction, an own-level bound for U_2, or a base bound on the core in CA-I, CA-II or CA-III. (Searched: "sealing", "seal", "own-level", "base bound on the core", "bend floor", "ownership floor", "share statement". CA-II names "the sealing theorem" at II:1128 and II:1212 without a statement.) The account itself excludes raw cells: "At a raw point of the core the current level is 0, and no threshold is provided there" (I:136339-136341). Lemma B uses (B-in) only at cells of level at least one, inside its stated class.

*Scope fact (S-B).* The cells of level at least one that meet the one-bond neighbourhood of Col(C), and the index-zero cubes that meet Col(C), lie in D_2 \ B_S. They lie in D_2: the level-one neighbours of the collar lie in Omega_1 \ Lambda_1, which is in Z_1, hence in Z_h, hence in D_2 by (a2). The account defines B_S only as "the set near S that the base bound on the core excludes" (I:136725-136726). It applies the bound to the frozen cubes "two LMR_{h+1}-layers inside S, hence whole in D_2 \ B_S" (I:136754-136756), and it states that the core contains the collar (I:142583-142586). I take (S-B) as part of the scope of (B-in).

**Lemma B.** Assume (B-in), (S-B) and inputs (e), (f), (g) of `4.27:lem-real-point-collar` (I:142618-142659). Let V be real and in the support of the characteristic functions, and y in Col(C). At b2:

- (i) every plaquette p of Omega_0 that has a vertex at y and a corner in Omega''_1 satisfies |dU_2(p) - 1| <= (phi_flat/64) r_1(1) < 3 x 10^-4 alpha_{0,0} (this covers the plaquettes of the current stencils at y and the non-pinned plaquettes based at y);
- (ii) Q_3(y) <= 0.48 r_3(0);
- (iii) U_2 obeys the index-zero cube clause CMP 99b (3.35) on every index-zero cube that meets Col(C).

**Proof.** (i) Such a plaquette belongs to Omega_1 (convention (ii), I:141043-141044). As in the account's real-point proof (ARR section 10.5), it lies in a cell of level one with weight one: the separation from Omega_1^c to Omega_2 exceeds its diameter, and every arrested weight window has k_0 > h >= 1. Apply (B-in) at that cell with F = phi_flat, w = c = 1, n = 1. This gives |dU_2(p) - 1| <= phi_flat r_1(1)/64. By `4.27:lem-level-zero-ratios` (a) (PROVED under its hypotheses; ARR (10.6)), r_1(1) <= 0.164 r_1(0) = 0.164 alpha_{0,0}. With phi_flat = 1 - 4.51 beta = 0.098 the bound is below 2.6 x 10^-4 alpha_{0,0}.

(ii) By input (e), eta^3 J(W)(b) is a sum over the 2(d-1) = 6 plaquettes of Omega_0 that contain b, each term Ad of pi Im dW(p) with sign +-1. Here |pi X| <= c_pi |X| <= 2|X|, the adjoint action of a unitary preserves the norm, and |Im W| <= |W - 1| for unitary W (W is normal with eigenvalues e^{i theta}, and |sin theta| <= |e^{i theta} - 1|). Each plaquette at a stratum bond at y is pinned, bounded by Lemma A by 0.04 alpha_{0,0}, or of the kind in (i). Hence eta^3 |J(U_2)(b)| <= 6 * 2 * 0.04 alpha_{0,0} = 0.48 alpha_{0,0}, which is (ii) since r_3(0) = alpha_{0,0} eta^-3 (I:140998-141001).

(iii) Let Box be an index-zero cube meeting Col(C), with s <= 10M sites per side. Its plaquettes are pinned or of level one (I:142775-142783). A pinned one lies in Col(C), because the cube is far smaller than the separation of components of Z_k (at least R_k own-scale M-cubes, I:142546), so Lemma A bounds it by eps_0. A level-one one is bounded by (B-in). Put eps := 0.04 alpha_{0,0}. Then 2(d-1) s eps <= 2.4 M alpha_{0,0} <= 1/10, by the first ceiling of (g) (24 M A <= 1, and alpha_{0,0} <= A). Input (f) is a statement about any configuration on such a cube. It gives a gauge on Box with eta|A| <= 25(d-1) M eps = 3 M alpha_{0,0} and eta^2 |nabla A| <= 6 M alpha_{0,0}. The two ceilings of (g) put these bounds in the index-zero cube class, exactly as in the account's real-point proof. QED.

**Exact gap of attack 2.** (B-in) is cited by the account and printed nowhere. If it is not accepted as an input, the missing step is (i) alone: a level-one bound for U_2 on the plaquettes next to Col(C), at 0.04 alpha_{0,0}, which is about 0.24 of the level-one radius r_1(1). A route without (B-in) compares U_2 with U(B''_k, V''); the real-point lemma covers the latter at level one (its input (d)). That route needs a localisation estimate between the two constrained problems. Its decay from the cut has the same separation problem as section 6.

## 5. Proposition C: CA from the collar layer bound

**(CL), the collar layer bound.** For every source pair p of the prescribed arrested source at d', with its full global rider, every parameter in the parameter domain, s in {3,4}, t_s in [0,1], y in Col(C) and stratum bond b at y:

  N_y(t_s H_s) <= F_s,   eta^3 |s^#_{sigma_s}[t_s H_s](b)| <= Kcur F_s,   F_3 + F_4 <= eps* := min{ 1/85 , (3/Kcur) alpha_{*,0} }.

Here N_y is the local norm of `4.27:lem-left-factor-algebra` (I:141265-141281), with the covariant derivative at the preceding partial product (U_2 for s = 3, e^{i eta t_3 H_3} U_2 for s = 4); the layers are defined on the read-sets; Kcur = 3 + 18d + 2.2 KJ, with KJ the current-response constant of I:94996-95025; alpha_{*,0} = min_i alpha_{i,0}. Kcur is fixed before the final ceiling on gamma, as in ARR section 6.2.

**Proposition C.** Lemma A, Lemma B and (CL) imply CA at C: the five strict inequalities at b2, b3, b4 and on every segment, the index-zero cube clause on every whole cube meeting Col(C), one field on overlaps, and full stencils.

**Proof.** Fix y in Col(C). Kcur >= 3 + 72 = 75, so 3/Kcur <= 1/25. The ceilings (g) give alpha_{0,0} <= A <= 1/(24M) <= 1/24.

*First application of the local algebra* (I:141265-141508, PROVED; ARR (10.5)), to e^{i eta t_3 H_3} on U_2 with A' = 0: n <= F_3 <= 1/85 < 1/40; a = 0; theta, the largest |dU_2(p) - 1| over plaquettes based at y, is at most 0.04 alpha_{0,0} < 1/10 by Lemmas A and B(i). It gives the bondwise logarithm A'_3, keeps U_2 and all its gauges, and adds at most 4F_3, 1.06F_3, 1.2F_3 to the plaquette, eta|A'| and eta^2|nabla_U A'| entries.

*Second application*, to e^{i eta t_4 H_4}: n <= F_4 < 1/40; a <= 1.06/85 < 1/80; theta <= 0.04 alpha_{0,0} + 4/85 < 1/10. The same three increments with F_4.

*Totals,* with eps = F_3 + F_4 <= (3/Kcur) alpha_{*,0}:

  Q_1 <= 0.04 alpha_{0,0} + 4 eps <= 0.2 r_1(0);
  Q_3 <= (0.48 alpha_{0,0} + Kcur eps) eta^-3 <= 3.48 r_3(0)   (Lemma B(ii) and the triangle inequality);
  Q_5 < 0.04 r_5(0)   (U_2 unchanged);
  Q_6 <= 1.06 eps eta^-1 <= 0.043 r_6(0);   Q_7 <= 1.2 eps eta^-2 <= 0.048 r_7(0).

Each is below 3.65 r_a(0) < f_0(d^t) r_a(0) (ARR (10.3)). The same bounds hold with either layer partly or wholly absent, so they cover b2, b3, b4 and the segments. The logarithm is one convergent principal series per bond, so two overlapping local sets give the same value on a shared bond. The unitary factor is U_2 throughout, so the cube clause of Lemma B(iii) holds at every member of the chain. QED.

The budget eps* is 48 times the budget alpha_{*,0}/(16 Kcur) of ARR (18.4): the exact seed bound (0.04 instead of 1/24) and the consumers' threshold f_0 > 3.65 pay the difference.

## 6. The collar layer bound

Account facts used in this section:

- (c1) `4.22:lem-current-localisation` (PROVED), I:92480-92484: for z in Z_h and s in {3,4}, K_u Theta_0^loc(H_s)(z~) <= C_L eps_Q(k) e^{-delta_L (d_sc(z,S) - 1)}, with Theta_0^loc(H)(x) := L^{m(x)} eta sup_{B^top(x)} |H| (I:78205-78208), delta_L = min{delta_1, delta_G}/2, C_L = C(d,L,M).
- (c2) eps_Q(k) <= K_Q alpha^+_k, K_Q a (d,L,M)-number, alpha^+_k a linear expression in the level-k radii (I:91736-91739).
- (c3) d_sc(z, S) >= R^_k - 1 for every z in Z_h (proof of `4.22:lem-law-site` (ii), I:92095-92097; the argument is geometric and holds at every point of Z_h).
- (c4) Col(C) is in Z_h (Lemma A, input (a1)).
- (c5) R^_k is non-increasing in k with R^_k < L t_k^r (I:131529-131531), and R^_k >= (log x^_k)^r, which tends to infinity as gamma -> 0 (I:21528-21530).
- (c6) alpha_{i,lambda} <= (64/49) sqrt(lambda) alpha_{i,0} (I:141600; ARR (10.6)).
- (c7) The admissible geometry, `4.21:def-strips-geometry` item (4) (I:63571-63586), stated there "in every label" with the citation CMP 119 (3.5), (3.20), p. 269: (a) Omega_{j+1} in Lambda_j in Omega_j; (b) the Omega_j are nested; (d) every zone Omega_j \ Omega_{j+1} is at least one pi_{j+1}-cube thick, dist_{j+1}(Omega_j^c, Omega_{j+1}) >= 1, that is, at least L cells of level j. Here pi_l is the partition into M-cubes of level l, and a cell of level j is a cube of pi_j (I:62741-62746, I:62765-62770). The thin zones left by earlier attempts are single layers of pi_{i+1}-cubes, L cells wide (I:114355-114357), so (d) covers them. For j <= h the zones of B''_k are those of the label, since Omega''_j = Omega_j (I:92002-92003).

**A lattice fact used below (proved here).** Let U = e^{i eta A'} U with eta|A'| <= 1/80 on the stencil. Then eta^2 |(nabla_{U,mu} h_nu)(x)| = eta |Ad_{U(x,x+mu)} h_nu(x+mu) - h_nu(x)| <= (e^{1/40} + 1) sup eta|h|, because |Ad_{e^Y W} X| <= e^{2|Y|} |X| for unitary W (submultiplicativity, |e^Y| <= e^{|Y|}, unitary invariance). Hence N_y(h) <= 2.03 sup eta|h| over the read-set R(y) of y and its lattice neighbours. At unit spacing, derivative norms cost no smoothness.

### 6.1 Attack L1: cut localisation with the law-site separation

By the lattice fact, the reading (R) of 6.3 (eta|H(x)| <= Theta_0^loc(H)(x~), as m >= 0), and (c1)-(c4) at the points of R(Col(C)):

  sup_{y in Col(C)} N_y(t_s H_s) <= 2.03 (C_L K_Q / K_u) alpha^+_k e^{-delta_L (R^_k - 2)} <= C_1 sqrt(k) e^{-delta_L R^_k} alpha_{*,0},

  C_1 := 2.03 e^{2 delta_L} (C_L K_Q / K_u) A^+ rho_C (64/49),

with A^+ := sup_k alpha^+_k / max_i alpha_{i,k} and rho_C := max_i alpha_{i,0} / min_i alpha_{i,0}, both fixed with the radii (A^+ is finite if p_1 <= q in delta'_k = g_k A_1 t_k^{p_1}; otherwise a factor t_k^{p_1 - q} enters and must be tracked).

**Exact failure.** (i) *Uniformity in k.* (CL) needs C_1 sqrt(k) e^{-delta_L R^_k} <= 3/(2 Kcur). At a fixed ceiling gamma, R^_k does not grow with k by (c5), while k is unbounded as the cutoff is removed. The account bounds alpha_{.,k}/alpha_{.,0} only by (1+beta_0)^2 sqrt(k) ((h1)-(h2) of `4.27:lem-level-zero-ratios`). This is not slack in the flow: under the one-loop flow, g_k/g_0 grows without bound as the cutoff is removed at fixed g_k (a property of the flow, not used as a step here). So L1 proves the sup part of (CL) only for completion densities k <= k*(gamma) := (3/(2 Kcur C_1))^2 e^{2 delta_L R_gamma}, R_gamma := inf_k R^_k. Lemma E in 6.2 removes this gap. (ii) *The current increment.* The source term of the layers satisfies the identity I:94983-94986, j = (Delta_U - P_1 + K) A' - m_H(X) + F(U, H). The terms P_1 A' and m_H(X) are bounded there only through clause (b) of the localised small-solution theorem, in terms of the data norm (I:94992-94995). A sup bound on H, which is all Theta_0^loc gives, does not control them.

### 6.2 Lemma E: the zones between the collar and the cut (new attack 3, closes the gap of 6.1(i))

**Reading of d_sc** (stated, not proved). d_sc is the path metric that counts cells, the M-cubes of the local scale of B''_k (I:91723). The proof of (c3) measures the separating layer in M-cubes of level h, the local scale of B''_k there (I:91991-92024, I:92095-92097). This fixes the reading for (c1) and (c3).

**Lemma E.** For every y in Col(C),

  d_sc(y, S) >= (R^_k - 1) + (L - 2)(h - 1).

**Proof.** Take a lattice path from y to a point z of S. By (c3), S does not meet Z_h, so S lies in Lambda_h, which lies in Omega_h by (c7)(a); thus z is in Omega_h. And y is outside Omega_1, hence outside every Omega_j (nesting). Fix j with 1 <= j <= h-1. Let tau_j be the first index at which the path is in Omega_{j+1}, and sigma_j the last index before tau_j at which it is in Omega_j^c. The points strictly between lie in the zone of level j. By (c7)(d) the two end points are at distance at least M L^{j+1} eta in the maximum norm, so the path makes at least M L^{j+1} - 1 steps inside the zone. In that zone a step has scaled length 1/(M L^j), one lattice unit in cells of level j. So this portion has d_sc-length at least L - 2. Portions for distinct j lie in distinct zones, so they are disjoint. They lie in Omega_h^c, which lies in Z_h by (c7)(a). After its last visit to Z_h, the path has d_sc-length at least R^_k - 1 by (c3). That portion lies outside Z_h, so it is disjoint from the zone portions. Adding the lengths gives the bound for every path, hence for d_sc(y, S). QED.

Lemma E uses only the zone thickness, which (c7) states in every label, re-blocked or not. So the restriction of the law-site increments to unre-blocked nests (I:91846-91849) does not arise. Proposition F needs only some fixed c_s > 0 in place of L - 2: any reading of d_sc that charges at least c_s for crossing a zone L cells thick gives the same conclusion.

### 6.3 Proposition F: the collar layer bound holds once gamma is small

**Named inputs beyond (c1)-(c7).** Each is the account's own usage of a stated result at the completion site.

- (P1) The layers H_3, H_4 are response fields of the response-field theorem, with data the arguments listed in the proof of `4.22:lem-current-localisation`. For H_3 these are f_1, with |f_1(x)| <= C sup|J^{b2}| e^{-delta_G d_sc(x,S)} (I:92576-92582), and an argument supported in S; for H_4 the argument g_k B, supported in S (I:92583-92587). Their sizes obey the budget K_u B_H sum sup|.| <= eps_Q(k) (hypothesis (d'), I:92454-92456), into which the account's proof of (c1) also absorbs the constant C sup|J^{b2}|. The account applies clause (b) of that theorem to these layers at the completion site (I:142540-142546). *Caution.* The account parametrises the layer data in two ways: after the criticality cancellation G''_k Q''^* = 0, as above (proof of `4.22:lem-current-localisation`), and before it, as B_3, B_4 and J_3, with J_3 built from the current at b2 and supported in the completing component (I:142532-142537). (P1) uses the first. With the second, clause (b) would bound the associated fields at Col(C) only by B_# times the seed current there, which is not small enough for the current part of (CL).
- (P2) The partner current of a layer is the source term of the localised small solution, j = (Delta_U - P_1 + K) A' - m_H(X) + F(U,H) (I:94983-94986), and the five-term estimate of I:94988-95020 holds pointwise, each term read at the bond.
- (R) eta|H(x)| <= Theta_0^loc(H)(x~) for x in the block B^top(x~) (definition at I:78205-78208).

**Proposition F.** Under the inputs of CA, Lemma E, (P1), (P2) and (R), there is gamma_* > 0, fixed by one more ceiling of supremum form chosen last in the account's order, such that for gamma <= gamma_* the collar layer bound (CL) holds.

**Proof.** *Sup part, first route ((c1), (R), the lattice fact).* Let y be in Col(C) and x in the read-set R(y). Then x lies in Z_h: the read-set lies within a few level-zero cells of y, hence in Omega_1^c or in Omega_1 \ Lambda_1, because the boundaries of Omega_1 and Lambda_1 are at least 2MR_1 apart (CMP 119, quoted at I:63572-63574); both sets lie in Z_1. Also d_sc(x,S) >= d_sc(y,S) - 1. By (c1), (c2), (R), Lemma E and the lattice fact,

  N_y(t_s H_s) <= 2.03 (C_L K_Q / K_u) alpha^+_k e^{-delta_L (R^_k - 3 + (L-2)(h-1))}.

By (c6), alpha^+_k <= A^+ rho_C (64/49) sqrt(k) alpha_{*,0}. Since k = h + R^_k, sqrt(k) <= sqrt(h) + sqrt(R^_k), and

  N_y(t_s H_s) <= C_1' ( S_L + sqrt(R^_k) ) e^{-delta_L R^_k} alpha_{*,0},
  C_1' := 2.03 e^{3 delta_L} (C_L K_Q / K_u) A^+ rho_C (64/49),   S_L := sup_{h >= 1} sqrt(h) e^{-delta_L (L-2)(h-1)} < infinity.

*Second route, which also gives the current part ((P1), (P2)).* Cut f_1 into its restrictions to M-cubes Q and telescope the response over the pieces. Apply clause (b) to each difference, with second datum zero (where the response vanishes) and the weight e^{-delta_P d^(.,Q)}; exponential weights in d^ are admissible (I:72519-72522). With d^ >= w d_sc and the summation used in the account's proof of (c1),

  sum_Q e^{-delta_G d_sc(Q,S) - delta_P w d_sc(y,Q)} <= C_rho e^{-delta_* d_sc(y,S)},   delta_* := min{delta_G, w delta_P}/2.

Treat the arguments supported in S with the single weight e^{-delta_P d^(.,S)}. This bounds N^Delta_y(H_s) and the associated fields P_1 A', m_H(X) at y by C_6 eps_Q(k) e^{-delta_* d_sc(y,S)}, with C_6 a (d,L,M)-number. At a stratum bond b at y the base parameter is at most 1 (the seed plaquettes are at most 0.04 alpha_{0,0}), and the remainder hypothesis holds for small layers. So (P2) gives eta^3 |s^#_{sigma_s}[t_s H_s](b)| <= Kcur C_6 eps_Q(k) e^{-delta_* d_sc(y,S)}. Lemma E and the ratio bound then give, as in the first route,

  N_y(t_s H_s) and eta^3 |s^#_{sigma_s}[t_s H_s](b)| / Kcur  <=  C_6' ( S_* + sqrt(R^_k) ) e^{-delta_* R^_k} alpha_{*,0},   S_* := sup_{h >= 1} sqrt(h) e^{-delta_* (L-2)(h-1)}.

*Choice of gamma.* Let F_s(y) be the larger of the two bounds. For delta > 0 and S finite, R -> (S + sqrt(R)) e^{-delta R} tends to 0 as R -> infinity. By item (7) of `4.21:def-strips-geometry` (I:63600-63607), R^_k >= T^_k^r and T^_k >= T_gamma for every k, so R^_k >= T_gamma^r =: R_gamma, and T_gamma tends to infinity as gamma -> 0 (I:63521-63522, I:21528-21530). The new ceiling is

  sup_{R >= R_gamma} max{ C_1' (S_L + sqrt R) e^{-delta_L R},  C_6' (S_* + sqrt R) e^{-delta_* R} } <= 3/(2 Kcur),

a one-sided cap of degree minus infinity in the sense of the account (all constants in it are (d,L,M)-numbers, radius constants in A^+ and rho_C, or Kcur, fixed before gamma). Under it, and with alpha_{*,0} <= A <= 1/(24M) <= 1/170 from the ceilings (g), F_3 + F_4 <= min{1/85, (3/Kcur) alpha_{*,0}} uniformly in k, h, the history, the source and the parameters. QED.

*Remark on A^+.* If p_1 > q in delta'_k = g_k A_1 t_k^{p_1}, then A^+ carries a factor t_k^{p_1-q}. Item (7) of `4.21:def-strips-geometry` gives t_k = T_k <= T^_k + 1 <= (R^_k)^{1/r} + 1 (I:63600-63607), so t_k^{p_1-q} e^{-delta R^_k} still tends to 0 as R^_k grows, and the same ceiling, with this factor included, applies.

### 6.4 Routes tried and not needed

- *L1 with (c3) alone* fails at uniformity in k (6.1(i)); Lemma E repairs it.
- *Stratum prices through the law-site increments* (10 R_min per level, I:91843-91849). These are asserted only at law sites inside unre-blocked nests. A partial result, proved here: **Lemma D.** If x lies in a component completed at a date (k';L) before d', then every lattice path from Col(C) to x passes through a point of level at least k' at d^t. *Proof.* At step k', the points of Col(C) lie in Z_1, which is in Z_{k'}, in a component that did not complete at k', since (t4) would have lifted them into Omega_1 (I:133477-133478, I:134967-134968). So the path leaves Z_{k'} and meets Lambda_{k'}, which lies in Omega_{k'} by (c7)(a); its points have level at least k' after the T-step to k', and levels never decrease (I:133480-133482). QED. Lemma E makes this route unnecessary.
- *Scale gain from the level of the sources* (CMP 99b Theorem 3.1, remark after (3.47)). Not needed.

## Result

**Proof**

CA holds, as an implication, for every completing component C of every completion date, every source pair of the prescribed arrested source with its full global rider, every parameter, at b2, b3, b4 and on every segment, with the old index-zero cube clause on every whole cube meeting the collar, one field on overlaps and full stencils; uniformly in the cutoff, density, waiting depth, history and arrest age; once gamma is at most gamma_* of Proposition F, one further ceiling of supremum form chosen last. Constants are in the account's order L -> profiles -> kappa -> kappa_1 -> M_1 -> M -> (q, C) -> gamma; no birth domain or source domain is shrunk. Proof: Lemma A (section 3), Lemma B (section 4), Lemma E and Proposition F (section 6) give the seed bounds and (CL); Proposition C (section 5) gives CA. Proved by Claude, not yet checked by the other model.

**Named inputs** (each cited where used). The account's statements retained by CA on their stated classes, among them fact (f), `4.22:lem-current-localisation`, `4.22:lem-law-site`, `4.27:lem-left-factor-algebra`, `4.27:lem-level-zero-ratios`, the inputs (a)-(g) of `4.27:lem-real-point-collar`, clause (b) of the response-field theorem, the admissible geometry of `4.21:def-strips-geometry` (4), and CMP 119 (2.10)-(2.14) as quoted. Beyond these:

1. (B-in), the base bound on the core, used only at cells of level at least one, with the scope fact (S-B). The account uses it in two proofs (I:136724-136733, I:138438-138450) and prints no statement or proof of it. **This is the first place the proof can fail.** Without (B-in), the missing step is Lemma B(i) only: a level-one bound of 0.04 alpha_{0,0} for U_2 on the plaquettes next to the collar.
2. (P1), (P2), (R) and the reading of d_sc: how the account's response-field theorem, source identity and local layer norm apply to the completion layers. The account applies them there itself. The sup part of (CL) needs only (c1), (R) and Lemma E; the current part needs (P1) with the layer data taken after the criticality cancellation (see the caution in 6.3). **This is the second place the proof can fail.**
3. (c7)(d) for labels changed by R operations: the account states it "in every label" with Balaban's citation for the RG-determined domains.

**Not used.** The level-zero chain proposition and the collar corollary (I:142269-142291), and the cube admission (I:142950). No computer-assisted step.

**Kind (How we work, item 9).** Proof of a step the account assumes: its collar corollary, in the weaker form CA that all dated-collar consumers accept. The proof shows where the assumption's content lies: the layers need a decay that grows with h = k - N_k (section 6.1), and the account's own zone thickness (c7)(d) supplies it through Lemma E.

**What changes for consumers.** None. The consumers listed in `crca.md` sections 3.2-3.3 read CA as stated. The separate chain-margin inputs of `crca.md` section 3.3 (dying frame, kept holomorphy, carriers) are not addressed.

**The three new attacks.** (1) Lemma A, identity rows of the splice: succeeds for the pinned entries. (2) Lemma B, the account's base bound on the core at level-one cells: succeeds for the side plaquettes, the current and the cubes, conditional on (B-in). (3) Lemma E, zone thickness from the admissible geometry: succeeds for the layers, after the cut-localisation bound alone (6.1) failed at uniformity in k.

**Suggested next steps, for the lead.** (a) One line-by-line check by Codex of Lemmas A, B, D, E and Propositions C, F, with attention to (P1), (P2) and the reading of d_sc. (b) A lane on (B-in) at level-one cells next to the collar, or a decision to take it as the account's input. (c) Legal copies of CMP 122a/b, if the check questions (P1) or the d_sc reading.
