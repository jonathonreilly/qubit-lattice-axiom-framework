# Gate of a2-full and assign-adopt (queue row 114)
Provenance: OpenAI Codex (GPT-6; xhigh requested for row 114, runtime effort not independently exposed), checkout `eb9fd12d2fc0ba499ff968e8d4a0b83792ac2d26`; Sussman–Alpoge outline commit `31a47c543775`; hand mathematical review, research text, not an audit, grants no status.

Credit: the outline's definitions, operator identities, profiles, localisation rules and walk conventions are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA line numbers refer to their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. The reviewed notes are Claude's `library/a2-full.md` and `library/assign-adopt.md`. Balaban is credited for the background-field and localisation programme as identified in those notes. No computation is used to discharge a mathematical statement.

Scope: `a2-full` §§2–9 and `assign-adopt` §§2–4, against the earlier layered and curved gates. H-walk, H-ct and H-prof remain premises; the question here is whether the conclusions follow from their stated forms. ADVANCE below means a valid research implication, with its named inputs, not scientific or audit status. Complete; written and saved section by section. The sparse-checkout workflow and scoped-worker instructions were read through `git show` at the same pinned revision; the user's narrower one-file/no-delegation instructions govern.

| Section | Verdict on the written claim | First failure or qualification |
|---|---|---|
| a2-full §2 | WRONG | 2.4 misreads the parameter convention. Tests 2.1–2.3 pass within the scopes below. |
| a2-full §3 | WRONG literally; repaired identification ADVANCE | Theorem I uses the already-free E form inside another C sandwich. Lemmas 3.1–3.6, including every BCH sign, pass. |
| a2-full §4 | ADVANCE with D1's convention | None in the gradient estimate or gap argument. |
| a2-full §5 | ADVANCE, conditional | None; choose the common upper constant for each component and retain the input bounds. |
| a2-full §6 | WRONG on its full stated domain | Fibre coordinates at nonzero B and the boundary completion are not matched. The complex Cauchy argument and layer separation pass. |
| a2-full §7 | ADVANCE under H-ct | None at the centre; a smaller-disc factor is needed away from it. |
| a2-full §8 | WRONG | Wrong parameter monomial; the displayed H-walk premise also omits support needed by mechanism (i). |
| a2-full §9 | WRONG as stated | Inherits §§6 and 8. The repaired implication and the final gap arithmetic pass. |
| assign-adopt §2 | WRONG in the written proof; repaired assignment ADVANCE | A8's injectivity-to-isometry inference and its unlisted size hierarchy. A3 passes. |
| assign-adopt §3 | WRONG as forced source identification | Exact pointwise joining clauses are an additional definition; the second-rule overlap proof also lacks its erosion margin. |
| assign-adopt §4 | WRONG as an unqualified table | Inherits the joining qualifications; 4.5 applies the rule to a test-grid domain not yet included in its definition. |

## a2-full §2 — WRONG as a whole; tests 2.1–2.3 survive with the stated scope

**2.1: ADVANCE for failure of a uniformly small perturbation on the whole fine X space. First failing step: none for that assertion.** One can take the reference exactly flat, avoiding the Wilson remainder entirely. For a bond strictly inside the bare layer, the eight forward differences and the mass give `||h||_X²=9 eta²|v|²`; its six plaquettes give `D²A[h,h]=6 eta²|v|²` in the stated normalization. The quotient is exactly `(2/3)bk g_k²`. Fix `x_k=x_*>0`, take `beta=x_*+bk` and `x_q=x_*+b(k-q)`. Then every coupling is at most `x_*^(-1/2)`, while `bk/x_*` is arbitrarily large; the allowed coupling-difference inequality is respected. Nested aligned cubes on a sufficiently large torus leave a bare-layer bond and all its plaquettes away from every profile margin. Thus depth cannot be hidden in a coupling ceiling.

This does **not** refute every fine-form approach or coercivity: this particular weight is positive, and the bare bond has `Qh != 0` (the level-zero row is the identity in per-length coordinates). It does not test `ker Q` or just the active energy lifts. The exact conclusion is failure of smallness on the *whole* X space required by the proposed route. The named unweighted `G_0,G,G_1` in SA 10149–10153 indeed contain no explicit profile weight. A profile-weighted fine Hessian is nevertheless a well-defined different operator, and the patch operation at SA 17645 contains profile-weighted Gaussian terms. Section 1 excludes that operation. Replace “the profile never enters the fine operators” by “it does not enter the three unweighted fine operators used for the ordinary step treated here.” Its implicit influence through the chosen field is not being excluded.

**2.2: CORRECT-NO-ADVANCE. First failing step: none as the unsubtracted-array test.** On an active interior region where all earlier profiles equal one, differentiating the unsubtracted sum produces `(sum_j b_j)/x_k` times the effective Wilson Hessian. At a flat datum that Hessian is nonzero on a transverse coarse mode; the same trajectory makes its coefficient grow like `bk/x_*`. This tests the unsubtracted grouping only. Summability of the subtracted brackets is H-ct, not a consequence of this example.

**2.3: ADVANCE. First failing step: none.** At an absolute contour value `exp(i theta)`, the derivative is `-(i/2) tr(delta exp(i theta))`; its constant term vanishes by tracelessness, but its linear term in theta need not vanish. The graph chain rule consequently includes the gauge-gradient contraction. It vanishes on the exact axial locus and is small, rather than identically zero, near it. The continuation in this assertion must be the *longer*, depth-`k+1` physical-step family: SA 7186 fixes level-`n` contours only for `n<j` in a level-`j` pillar. A general depth-`k` datum variation does not fix the contours of its own level-`k` datum.

**2.4: WRONG. First failing step:** “Mechanism (i) exempts the first `2^4` cubes.” It does not; see the §8 defect and repair below. The loss of one zero-length summand at `s=0` would not, by itself, prove that the sum's diagonal block vanishes either. The collar warning remains valid.

**2.5: CORRECT-NO-ADVANCE.** For positive `Re tau`, the displayed estimate follows by separating real and imaginary parts. The stated small disc about one ensures this sign. Lemma 5.2 below gives the sharper direct estimate.

## a2-full §3 — WRONG literally at the fibre-form notation; the identification is repairable

**Lemmas 3.1–3.5: ADVANCE as implications from the admitted inverses and critical-branch input. First failing step: none.** Here are the algebraic checks, including the sign-sensitive one.

* **3.1.** Put `F=G'Q'^T`; then `R=1-F(F^TF)^(-1)F^T`, so `R^T=R=R²` and `Q'G'R=0`. From `Delta_U G'=1-Q'^TaQ'G'` one obtains `R Delta_U G'R=R`. Substitution into `S=1-DG'RD^T`, using `QD=Dbar Q'`, gives respectively `QS=Q`, `RD^TS=0` and `SDG'R=0`. The complex statements are bilinear identities, not assertions of Hermitian orthogonality.
* **3.2, BCH.** With `X=it lambda`, `Y=i eta A`, `Z=-it lambda^+`, the terms linear in t through first order in A are
  `X+Y+Z+(1/2)([X,Y]+[Y,Z])`.
  Both commutators contribute `-t eta [lambda or lambda^+,A]/2`. Division by `i eta` therefore gives **plus** `(it/2)[lambda+lambda^+,A]`, alongside `-t Dlambda`. Thus (3.1) has the correct sign. Differentiated invariance gives `Delta^W D=T`, where `<Tlambda,C>=<j,B(lambda,C)>`; its sign is also correct. Expanding `Delta^W-S^T Delta^W S` gives `Tlambda_A` paired with C, `Tlambda_C` paired with A, and **minus** `<Dlambda_A,Delta^W Dlambda_C>`. Symmetrizing the last term and writing `lambda^+=lambda+eta Dlambda` cancels the two eta-commutators. What remains is exactly
  `1/2 < i[lambda_A,C]+i[lambda_C,A]-i[A,lambda_C^+]-i[C,lambda_A^+]-i[lambda_A,Dlambda_C]-i[lambda_C,Dlambda_A],j >`.
  This is SA 10176–10185. There is no BCH-sign defect. Inner-plaquette invariance is essential; this is not an identity for a compressed non-invariant boundary action.
* **3.3.** The cited critical-branch equation is `S'(a)=K_a^T omega`, with fixed linear slice and straightened constraint. Surjectivity gives uniqueness. At the reference, `QH=QH_1=1` gives `H^Tj=H_1^Tj=omega`, with the same pairings. These assertions use the critical-branch input, not just independent-current smallness.
* **3.4.** Substitution yields `G_1^(-1)=S^TK_LS+DRD^T+Q^TaQ`. Apply it to `DG'R`: the first and row terms vanish and the middle term is `DR`. Transposition gives `RD^TH_1=0`, hence `SH_1=H_1`. Pairing with `H_1` then subtracts precisely `a`, leaving `H_1^TK_LH_1=W_1^(-1)-a`. At complex arguments the written squared norm must be read as a bilinear contraction; it is zero because the vector itself is zero.
* **3.5.** Differentiating stationarity subtracts `Delta^(2)[omega]h`; thus `K_Lh=Q^Tomega'`, `Qh=Db`, `RD^Th=0`. Solving gives `omega'=(W_1^(-1)-a)Db` and `h=H_1Db`. Differentiating the value function gives the additional **plus** `<omega,D²b>`. On the active mask the lower-level endpoint factors are fixed, so `Db iota=iota`, `D²b[iota.,iota.]=0`; that is the needed PX100, not an assertion about absolute logarithms.

**Lemma 3.6: ADVANCE. First failing step: none in its formula as defined there.** Twice differentiating `q(Phi(u))=0` gives `Phi''=-h_V q''[C_V.,C_V.]`. Consequently the free Hessian is

`C_V^T F'' C_V - E_free[J]`, where `E_free[J](u,v)=<h_V^TJ,q''[C_Vu,C_Vv]>`.

**D1 — Theorem I then sandwiches this already-free form a second time.** This is the first literal failure in §3: its `C_V^T(...-E_V^(2)[J])C_V` is incompatible with Lemma 3.6's definition, and can even have incompatible matrix dimensions. The same notation recurs in §§4 and 6. The missing active injections in the displayed full-row inverse must also be understood explicitly.

**Written repair (proved by the preceding calculation):** define instead the *ambient* bond form

`E_amb[J](b,b')=<h_V^TJ,q''[b,b']>`, so `E_free[J]=C_V^T E_amb[J] C_V`.

Use `E_amb` inside a sandwich and `E_free` outside one, throughout. Then the physical-step Hessian is exactly

`C_V^T { iota^T(W_1^(-1)-a)iota + K_GF - E_amb[iota^Tomega+J_GF] } C_V`.

At the axial physical pair `J_GF=0`, giving the intended A. Scaling by `x_k g_k²=1` gives the B-normalized precision. Holomorphic continuation is valid on the longer physical-step family's admitted polydisc, where level-k axiality persists. It is not a proof of axiality on the entire independent level-k fluctuation polydisc. With these conventions, **Theorem I is ADVANCE**, conditional on the explicitly cited branch and inverse inputs. The second-expression remark follows from `RD^TH_1=0` and has no further failure.

## a2-full §4 — ADVANCE with D1's ambient/free convention

**Lemma 4.1 and Theorem II: first failing step none after that convention correction.** A contour mean remains in `SL(2,C)`, so its tangent at the identity has trace zero: the entire GF gradient vanishes there, including at complex axial fields. Near that locus, write `V_c(y,x)=exp(i theta)` with `|theta|<=C_L alpha_1`; the derivative has size `C_L alpha_1 |D|`. Bounded numbers of contour incidences per bond give the sup bound on `J_GF`. The second row jet, pivot inverse and elimination matrix have fixed finite stencils and bounded analytic coefficients. Their row and column sums therefore bound `||E_free[J_GF]||<=C_II alpha_1` without a depth or volume factor. A small local real gauge suffices; global proximity of every link to the identity is unnecessary.

The repaired theorem reads `A_full=A-E_free[J_GF]`. The layered input gives `||A(U_c,J)-A(U,0)||<=C_B(alpha_1+gamma_0)`, with `A(U,0)>=c_L`. Hence the total error is at most `(C_B+C_II)(alpha_1+gamma_0)<=c_L/4`. Zero extension proves the same `3c_L/4` lower bound on each conditioning subspace. This proves a form estimate at independent-current pairs; identification as a background Hessian still requires the physical-current/branch conditions of §3.

## a2-full §5 — ADVANCE, conditional on the repaired layered bounds

**Lemma 5.1: first failing step none.** The variational minimum for positive `G_1^(-1)` is bounded by testing the right inverse `E b`; at level k its row norm is the counting norm. This gives `W_1^(-1)<=2 C_up K_E²`. The row mass, the current correction and the contour Hessian each have bounded active-row norms; sandwiching by `C_V` gives a common `C_A(L)`. Positivity is the earlier real theorem, not a consequence of this upper estimate. The complex estimate is the real upper bound plus the supplied operator-norm perturbation.

**Lemma 5.2: first failing step none.** Directly, `Re< u,tau(A_0+P)u > >=[3c_L/4-t(C_A+c_L/4)-(1+t)e]||u||²`. Since `t<=1/8`, the proposed bounds leave at least `(3/4-1/8-9/80)c_L=41c_L/80>c_L/2`. Compression costs nothing. For the action-only variant choose `C_A` from the start to bound both the full precision and `C_V^T Delta_k C_V` separately; that follows from the same sum of component bounds, rather than from a bound on their sum alone. The estimate is coarse operator stability. It is not itself a new fine relative-Schur theorem.

## a2-full §6 — WRONG on the entire stated domain; the inner-action estimate advances

**Lemma 6.1 for inner plaquettes: ADVANCE. First failing step: none in the double-difference argument or its complex-data input.** Equation (34) and §7 of `a3-derivative.md` explicitly hold throughout the complex datum polydisc at a fixed real critical reference. They are not merely real-axis estimates analytically continued without a bound. Theorem P^c of `a3-clauses.md` concerns a different extension, in the reference itself; that extension is unnecessary for the Cauchy circles here. The proof remains conditional on the cited A1/linear-package inputs and admission of the real reference.

For completeness, differentiating the bondwise dexp factor also works: `Xi_a=1+O(eta a)` and `nabla Xi_a=O(eta nabla a)` in a local frame. Thus the product rule, `eta<=xi`, and T4 give `|dfrak(Xi_a h_c)|<=C xi_p^(-2)e^(-theta d(p,c))`. The plaquette trace kills the identity part of P, so the small-curvature factor supplies the other `eta² xi_p^(-2)`. Complex contour prefixes have bounded norms on this chart; unitarity at complex data is not used.

Write `K_p=C(kappa+r_B)eta^4 xi_p^(-4)` and `r=r_B/4`. On the two circles, the subtracted function obeys both

`|g_tilde|<=2r K_p e^(-theta d(p,c))` and `|g_tilde|<=2r K_p e^(-theta d(p,c'))`.

The minimum is at most their geometric mean. Two Cauchy integrals divide by `r²`, giving `C(kappa+r_B)/r_B` times the product decay. Each of the three subtracted terms misses a variable and has zero integral. When `c=c'`, one derivative Cauchy estimate, or the second-derivative formula with its factorial, gives `C(kappa+r_B)/r_B e^(-theta d(p,c))`, precisely the required coincident-row decay. No second-response estimate was silently imported. The note's weaker `C/r_B` bound follows.

**Theorem IV, layer geometry and Schur sum: ADVANCE for this inner-action input. First failing step: none in the layer-separation estimate.** Here is the missing path detail. If `y` is in layer j and c is active at level k, any path from c to y must exit each of `Omega_k,...,Omega_(j+1)`. For each i between j+1 and k, take the final departure from `Omega_(i+1)` before the first exit from `Omega_i`. The resulting path portion stays in layer i and has physical length greater than `rho xi_i`. Those portions are disjoint. For i=k, starting at the row rather than inside `Omega_(k+1)` loses at most a fixed number of top units. Moving to a pillar or plaquette also loses only a fixed local distance. Thus

`d_B(y,c)>=rho(k-j)-C_L >= (rho/2)(k-j)`

after a fixed larger separation floor; for `j=k` the required lower bound is zero. Excursions, holes and torus winding cannot skip a required nested boundary, and outside `Omega_0` the metric remains bare. This is stronger than the usual arbitrary-top estimate with one unpaid shell because the active row has the extra clearance from `Omega_(k+1)`.

Grouping plaquettes into pillars gives total `eta^4 xi_p^(-4)` at most `6L^4` per pillar. The ball estimate gives

`sum_y exp[-(theta/4)d(y,c)] <= C_L sum_(m>=0) (m+2)^5 exp[-theta m/8] < infinity`

under `theta rho>=64 log L`. The same bound works with a fine top as centre and with active rows as endpoints. Splitting a half-rate exponential into two quarter-rate factors pays for `1+n` by `(1+n)exp[-theta rho n/8]<=1`. Summing the other factor and then the row factor proves the two Schur sums, with no depth factor. The gradient sum and the bounded local pivot jet give the curvature correction. Retaining an extra eighth-rate factor gives the claimed distant-support tail (in fact the harmless polynomial factor in D can be avoided with these generous rates).

**D2 — Exact fibre coordinates at a nonzero complex datum are not the additive chart used in Lemma 6.1.** The first unsupported identification is the setting's formula for `P_w` at general `B_0`, if `C_V,h_V,q_V` refer, as in §3, to left increments about `V_c=exp(iB_0)V_0`. Additive `B_0+z` is not that left chart. This does not spoil the norm estimate, but the chain rule must include the transition.

**Written repair:** on each active bond put

`Psi_(B_0)(D)=log(exp(iD)exp(iB_0))/i`.

Then `Psi(0)=B_0`, `J=Psi'(0)` and `T=Psi''(0)` are bounded analytic one-bond maps on the smaller fixed chart. The correct ambient Hessian is

`J^T F_w''(B_0)J + F_w'(B_0)[T]`,

and its ambient gradient is `J^T F_w'(B_0)`. Apply the pivot correction of D1 to these. J does not enlarge a support; T contributes only same-bond entries bounded by a constant times the already proved gradient bound. Thus all the stated Schur and distant-support estimates survive with enlarged constants. This proves the repair, rather than assuming additive and left coordinates coincide.

Keep the radius dependence honest: the displayed proof gives `C_IV<=C(L,theta)(1+r_B^(-1))`, or the sharper bound retaining `(kappa+r_B)/r_B`. The cited A3 radius is allowed to depend on the fixed walk size (SA 9916). Calling this simply `C_IV(L)` requires fixing those construction constants and a positive admissible radius as functions of L first; it is not uniform over subsequently arbitrary shrinking radii or arbitrary walk sizes. A safe version retains `C_IV(L,theta,r_B)` and chooses the coupling ceiling afterwards. Depth and volume uniformity are unaffected.

**D3 — Corollary IV.3 applies an inner-background curvature estimate to crossing boundary plaquettes. First failing step:** the application of (6.1) to a plaquette meeting but not contained in `Omega_0`. The A1 problem at SA 9612–9616 supplies fields and small curvature on inner plaquettes. It supplies no small curvature for a plaquette completed with arbitrary exterior stored links; indeed the completed plaquette can be `exp(i theta Z)` even with every inner link equal to one. Varying an inner bare link can then give a derivative proportional to `sin theta`, with no `kappa+r_B` factor. Moreover the completion and its gauge transformation have to be defined before `A_p(Phi(B))` makes sense there. H-prof does not supply this missing field information.

**Written boundary repair for the ordinary step:** fix the exterior links and vary only the active level-k datum, as in §3. Separation places every corner of an inner bond belonging to a crossing plaquette in the bare collar. Such an inner bond is itself a level-zero determining row. Its value is fixed throughout the active variation; all other bonds of the crossing plaquette are fixed by the completion. For `k=0` the same conclusion holds because the active mask is separated from that collar. Thus these completed boundary plaquettes are constant on this branch and their active fibre Hessian is exactly zero. This proves the desired smallness for that explicitly fixed completion, with no assertion about its exterior curvature. If a different consumer varies the completion, its boundary map and bounds are an additional premise, not supplied here. Alternatively, for a bounded holomorphic fixed exterior completion one can use crude bare-scale insertion bounds (without the small-curvature factor) and the same distant-support Cauchy estimate.

**Corollary IV.1: ADVANCE as an implication from H-prof and the repaired inner/coarse estimate.** Use `omega_0=C_x/|t|`; no sign is used. For `t=x_k`, this is `C_x g_k²`. On `|t/x_k-1|<=1/2` it is at most `2C_x g_k²`, not literally equal to `C_x g_k²`; absorb the factor two in the constant and coupling ceiling. The region-name interpretation remains part of H-prof, as the user instructed; it has not been discharged by this gate. The claimed “at most n+3 indices” is not needed once H-prof is a premise.

**Corollary IV.2: ADVANCE under its explicit source bound**, by the identical absolute-weight estimate and the same factor-two convention. No source estimate is proved here. **Corollary IV.3: WRONG on its unspecified completion as written; ADVANCE for the fixed-completion repair just proved.** These are distinct domains.

## a2-full §7 — ADVANCE as an implication from H-ct, at the stated centre

**Theorem V: first failing step none in the O-bound, with the factorial and domain conventions below.** Let `R=r_k/g_k`. Cauchy gives `|F_Y,c|<=eps_ct e^(-kappa|Y|)/R` and `|F_Y,cc'|<=2 eps_ct e^(-kappa|Y|)/R²`; the factor two is needed for a repeated variable. It is absorbed in `C_V`. For a fixed root cube, encode a connected n-cube set by a deterministically chosen spanning tree and its depth-first traversal, of length `2(n-1)`. The bounded-degree cube adjacency graph gives at most `C_0^n` such encodings. There are at most `C M^4 n` row coordinates in Y. Therefore the row sum is bounded by

`C M^4 eps_ct R^(-2) sum_(n>=1) n C_0^n e^(-kappa n)`.

The series converges geometrically above the displayed threshold. Symmetry gives the column sum. The once-differentiated sum bounds the gradient. Since the B-coordinate graph is `g_k^(-1)Phi_V(g_k u)`, its second derivative is `g_k Phi_V''`; the curvature term is at most `C eps_ct g_k/R=C eps_ct g_k²/r_k`, which is at most `C eps_ct(g_k/r_k)²` when `r_k<=1`. D1 fixes which form is sandwiched.

This uses H-ct's **local dependence on fluctuation coordinates in Y**, not merely polymer locality before composing with the background. That strong premise is left untouched. At a centre with `||g_k B_0||_infty<=v r_k`, `v<1`, the same proof costs `(1-v)^(-2)`, with the chart transition of D2. There is no uniform Cauchy bound up to the open polydisc boundary. If H-ct is supplied in a centred fluctuation chart at each admitted complex reference, the displayed bound applies at zero in each such chart. A claim on a complex reference family must retain that uniform version of H-ct.

The asymptotic radius gives the stated logarithmic smallness if `q_1>0`. The initial warnings about unsubtracted arrays and crude locality estimates are warnings about those estimates, not counterexamples to all alternative counterterm proofs. The last integrand remark is valid on a bounded test domain: it may enlarge `F_0`, but does not by itself assert a volume-free bound on `F_0`.

## a2-full §8 — WRONG as written; a collared implication is repairable

**Theorem VI, first failing step:** the parameter monomial specified in the first paragraph is not mechanism (i)'s monomial. **D4 — parameter convention and geometric support were conflated.** SA 10552–10558 leaves the factor `exp(16 kappa_bar)` precisely because the first sixteen cubes can carry parameters without paying a length proportional to the parameter-cube side. Its middle factor counts cubes crossed **without** parameters. It does not instruct one to delete the first sixteen parameter factors from every walk. SA 14178–14183 independently says that a carrier meeting m parameter cubes costs at most `exp(m kappa_bar)`. With S the set of variable cubes, the consumer's monomial is

`s^omega=product_(Delta in P(omega) intersect S) s_Delta`,

with unvaried cubes set to one. Test 2.4 and the first sentence of Theorem VI's proof must be changed accordingly. A zero-length term may depend on a parameter; exclusion by the *support collar*, rather than an artificial exemption in the monomial, is what must prevent that near `Z_0`.

There is a second required geometric qualification within this defect. The tree distance in SA 10210 is required to meet `X_1,...,X_m`, **not X_0**. H-walk's displayed pointwise bound and the count `C^m` alone do not assert that `A_omega(y,y')` vanishes unless y touches `X_0`, or control how far the parameter carrier extends beyond a tree meeting its cells. SA 10552 explicitly conditions its use on that left-support fact. The proof's `d_B(omega;y,y')>=w-C` cannot be deduced by saying only that a tree meets a cell near the parameter cube: cells and their hulls have radius `O(M_1)` in local units, not radius uniformly `O(1)` as `M_1` varies.

For example, if the support clause is dropped, the numerical H-walk inequalities allow a single zero-length term with `A_omega(y,y)=1`, `X_0` far from y and one parameter on `X_0`. The tree distance is zero, the term is constant and holomorphic on every local class, and the length-zero count is one. The undecoupled scalar A is positive, but its corrected monomial makes `A(0)=0` at arbitrarily large w. This is a counterexample to the **stripped-down stated kernel premise**, not a counterexample to the actual outline operator or its full walk construction. Restoring its support clause excludes it.

**Written repair, conditional on H-walk with its source's support/carrier clauses retained:** let `R_h=C_L M_1` bound the local metric distance from any point of a walk cell or its hull enlargement to a tree point in that cell; for `X_0` use its left endpoint y. Require boundedly many possible first cells at each y, as in the local cell covering. An s-dependent carrier is then within `R_h` of an admitted tree, so

`d_B(omega;y,y') >= w-R_h`.

Choose the parameter-cube side after this radius, `ell_P>=8R_h`, enlarging the fixed numerical factor for the top-unit conversion. A hand count gives the needed length-against-parameters estimate: traverse a finite tree of length t twice, divide the traversal into pieces of length at most `ell_P/4`, and thicken each piece by `R_h`. Each piece lies in a coordinate box of side less than `ell_P` and therefore meets at most `2^4` partition cubes. Hence

`#P(omega) <= 16 + C_L t/ell_P`.

The weighted length dominates physical length in top units up to a fixed L factor. Apply the count to trees approaching the defining infimum. It gives

`|s^omega| exp[-delta_0 d_B(omega)/2] <= exp(16 kappa_bar)`

when `ell_P>=2C_L kappa_bar/delta_0`. The remaining quarter factors pay respectively for `w-R_h` and the endpoint sum. Keeping the original `M_1^(-m/2)` reserve, the geometric series over tree walks converges above the stated walk-size floor. The top/row ball count closes the endpoint Schur sums. Thus the actually established estimate is

`||chi(A(s)-A)chi|| <= C exp(16 kappa_bar) exp[-delta_0(w-R_h)/4]`.

In particular the simpler uniform bound with `exp[-delta_0 w/8]` holds if `w>=2R_h`. It costs at most `c_L/20` provided also

`w >= (8/delta_0)[16 kappa_bar + log(20C/c_L)]`.

This proves a corrected conditional theorem by the same Schur method. It has explicit cell-size room and the actual monomial; it does not prove H-walk, nor infer its missing support clauses merely from holomorphy. If only the literal quantitative H-walk paragraph is admitted, those clauses remain a named extra obligation. The note's stated `C_VI(L,C_A')` and collar threshold cannot hide `exp(C delta_0 M_1)` without fixing `M_1` first.

For `A_full` the local GF correction can be kept undecoupled by definition. To identify that choice with decoupling every term of an actual precision expansion requires its carrier to stay inside the collar (a fixed finite-stencil clearance). The same caveat applies to the perturbations that §9 explicitly leaves undecoupled. These are choices of which operator is being decoupled, not consequences of a norm estimate.

## a2-full §9 — WRONG as the stated assembly; arithmetic and repaired implication survive

**First failing step:** invoking Theorem IV on its unqualified boundary/chart domain and Theorem VI with the wrong monomial and insufficiently specified walk support. No sign error occurs in the final addition: a starting `3c_L/4`, less four errors of `c_L/20`, leaves `11c_L/20`; one more such error leaves `c_L/2`.

**Repair:** use D1's ambient/free convention; restrict identification to the longer physical-step family; use D2's correct complex chart and retain its radius-dependent constant; specify D3's fixed exterior completion; supply H-ct uniformly at the centres being used (or work on a fixed smaller fluctuation disc); and use D4's actual parameter monomial, support clauses and enlarged collar. Choose all construction scales and an admitted datum radius before the coupling ceiling. Then impose the same four `c_L/20` error ceilings, with their repaired constants. The displayed addition and zero extension prove the stated half-gap for this **explicitly repaired conditional precision**. H-walk, H-ct, H-prof and the source bound remain inputs. This does not supply the patch Gaussian or seam-node boundary operators excluded in §1, and it gives no unrestricted full-A2 closure from the two reviewed notes alone.

## assign-adopt §2 — WRONG in the written A8 proof; the assignment has a direct repair

**Lemma A, A1–A7: ADVANCE. First failing step: none under the stated aligned-grid conventions.** Check each clause separately:

* **A1:** a cube at positive distance from `T_q^c` lies in `T_q`. The initial M-cube unions subdivide into both smaller grids, since the side ratios are integer powers of odd L. Subsequent members are cube unions by their construction. Empty members cause no problem.
* **A2:** taking the union of admitted cubes preserves the same lower distance bound; the first rule has a strict inequality, the second a weak one. Do not replace one by the other at a lattice equality case.
* **A3:** this induction is correct. The complement inclusion is equivalent to the previous erosion bound. For `d(x,Z^c)>e_q+c_q`, every z in `T_q^c` has `d(x,z)>c_q` by the 1-Lipschitz distance function. Every point of the aligned cube containing x is less than its side from x. Subtracting that side gives the defining next gap. The sums are
  `sum_(i<q)xi'_i < xi'_q/(L-1)` and `sum_(i<q)xi'_(i+1) < L xi'_q/(L-1)`.
  Consequently the first bound follows from `L mathfrakM <= (L-2)rho`; the hypotheses `rho>=L mathfrakM`, `L>=3` suffice. The second bound is `2L/(L-1) M_1'xi'_q<=3M_1'xi'_q`. This is an **upper** bound on lost depth, not an inference from the lower gap alone.
* **A4:** membership of the next cube asks whether its forbidden-distance neighbourhood is contained in `T_q`. Relative to x that neighbourhood has radius at most `c_q`; previous dependence adds `e_q`. This proves locality, including the strict/weak choices at the two thresholds.
* **A5:** enlarging Z shrinks each complement, so every previously admitted cube stays admitted. This compares the same *absolute* grids and levels, as stipulated; comparing two differently rescaled towers without that convention would not suffice.
* **A6:** the recursion does not read the cutoff depth. Truncation really does commute with construction.
* **A7:** the side ratios divide M, so a translation preserving the input partition preserves all finer grids. Distances are translation invariant. On site sets, odd centred cubes also have the claimed common-centre point symmetries. No assertion about translating a fixed grid by an incompatible displacement is needed.

**D5 — A8 uses a false metric inference and an unstated hierarchy. First failing step:** “the covering map is a sup-isometry ... implied by injectivity on `N_r(Z_tilde)`.” Injectivity on a tube does not make distances between all its points equal to torus distances. A long lifted box can have an injective small tube while its opposite ends are closer around the torus. Also the neighbourhood of a cube of side s with radius a has diameter approximately `s+2a`, not the asserted `c_q=s+a`. The proof needs a radius relative to a chosen point, not that diameter.

**Written repair of A8 (proved):** for an aligned lifted cube `Q_tilde`, let `N(Q_tilde)` be its threshold neighbourhood, with `<=` for the first rule and `<` for the second. Quotient distance gives the exact set identity

`N_T(pi Q_tilde)=pi N_Z(Q_tilde)`.

This identity needs no isometry of the projection. If `N_Z(Q_tilde)` lies in the lifted previous member, its projection is admitted on the torus. Conversely, choose a lifted x in `Z_tilde` over an admitted torus cube, and its aligned cube `Q_tilde`. Every point of `N_Z(Q_tilde)` is within `c_q` of x, hence lies in `N_r(Z_tilde)`. Its projection is in `T_q(Z)=pi T_q(Z_tilde)`. Injectivity on that tube identifies it with its unique preimage in `T_q(Z_tilde)`. Thus the whole neighbourhood lies in that member and the lifted cube is admitted. This proves both inclusions inductively, on every depth, without requiring `r>=sum c_i`: each previous member stays inside the original lifted Z.

The final numerical sentence also needs `M_1'>=rho`, which does **not** follow from displayed (1.0). The outline does give that intended hierarchy (SA 10212, describing the larger cube size). Retain it explicitly. Then `max c_q<=max(2rho,2M_1')<=2M_1'<M`, so the proposed one-M-cube tube suffices. Without it, (1.0) allows arbitrarily large rho at fixed `M_1',M`; one M collar is no longer justified, and the second-rule meet need not have the first rule's separation rho. Alternatively retain the actual `r>=max c_q` in A8 and impose the separate separation inequality where consumed.

**A9: CORRECT-NO-ADVANCE; first failing step none.** Relabelling absolute levels and units together preserves `q-p`, the integer side ratios and every distance inequality. This is a coordinate covariance, not a new estimate.

With these repairs, Definition A supplies actual finite nested sets, the two specified gaps, a single compatible grid rule on all admissible tori, and equality on common lifts **with the required room**. SA 5884 makes that room explicit for the companion consumer. The proof does not justify projecting an arbitrarily chosen disconnected collection of lifts without its neighbourhood being injective. SA 5598–5610 allows a supplied assignment, so adoption of this corrected rule is admissible; neither Balaban's original assignment nor a theorem identifying it with this one is required.

## assign-adopt §3 — WRONG as a uniqueness claim extracted from SA; correct as an explicit definition

**Lemma JS with its exact clauses (i), (ii): CORRECT-NO-ADVANCE for the first rule. First failing step: none in the pointwise uniqueness argument.** Nestedness and `Omega''_0=W` put every member inside W. The collar union and its complement cover W, so (i) and (ii) prescribe membership at every point. For the cut meet, A3 makes all tower factors equal one away from their erosion strips. In collar b, the original sequence has membership exactly through level `j_b`; the other factors are one by boundary separation. This gives (i). Away from all collars it gives (ii). On overlapping single-layer collars the levels agree, and the prescriptions agree. Once the prescribed sets exist there is plainly at most one such sequence. Old-row and lifted-new-row datum assignment then follows from Lemma J's row classification, with no independent choice of datum left.

**D6 — what is defined and what is forced must be separated. First failing step as a claim about the source:** replacing “well inside” by equality on *every* point of `W minus union collars`, and replacing the tower clause by the precise cut/intersection formula, is a specification of the qualitative source text, not a consequence of fixing the tower recursion. SA 9786's new-row level restriction is necessary; the previous gate expressly did not accept it as a proof of the unique cut formula. Definition A already **adopts** the joined-sequence formula. That is an available resolution, and the pointwise argument checks its stronger specified clauses. It should not be advertised as a theorem that the unsupplemented SA wording singles it out. The note's own sentence saying that the ruling is definitional is the correct formulation.

There is also a genuine gap in the displayed overlap proof for the second rule. It uses `2rho max xi > e_(j_b')`. A3 supplies that for the first rule, but for the second only `e'_(j_b')<=3M_1'xi_(j_b')`. Even with `mu=M_1'>=rho`, the available margin `(n_s-n_c)mu>=2mu` does not imply the required `>3M_1'`. Lemma J(c)'s quoted estimate has the same first-rule limitation. Thus its invocation does not close this case. This is a failure of the written proof, not a demonstrated counterexample to the maximally aligned second-rule meet.

**Written repair:** explicitly define the joined sequence by the cut meet, retain the exact clauses (i), (ii) as its specification, and use

`(n_s-n_c)mu > max(rho,3M_1')`

when second-rule parts are compared. For the consumers with `mu=M_1'`, `n_s>=n_c+4` suffices. The other tower factors are then one in each collar by A3, so the preceding pointwise existence and uniqueness proof applies unchanged. The deeper-member separation uses `n_c mu-3M_1'>rho`, valid for `n_c>=5`, `mu=M_1'>=rho`. These are allowed explicit choices for the source's O(1) collar constants. A proof at the original weaker second-rule separation would instead need a sharper aligned erosion argument; the present note does not supply it.

For one-part localisations no overlap issue arises. Adopting both the assignment **and** the cut-meet joining convention removes the need to identify an unspecified old convention in our defined chain. It does not establish uniqueness among all possible readings of SA 9786. The empty-member assignment still refutes a universal upper-erosion/SEP-L claim; it does not refute this supplied assignment.

## assign-adopt §4 — WRONG as the unqualified all-consumers table; the main uses have explicit repairs

**Rows 4.1–4.3: ADVANCE as conditional uses of the adopted construction**, after D5's hierarchy and D6's joined-sequence convention/separation. For a meet, the complement is a union of complements, so its gap is the minimum of the component gaps. The second tower contributes at least `L M_1'xi_q>rho xi_q`. Cubical intersections preserve the common finer grid. Restriction reads `T_q subset Z subset Omega_p subset Omega_q`; it needs the displayed `Z subset Omega_p`. Comparison then reads the repaired mismatch strip and the same A1/response assumptions. None of these algebraic facts alone proves the analytic comparison theorem.

**Row 4.4: ADVANCE for the explicitly adopted second-rule meets. First failing step: none in the strip arithmetic.** The loss at the top is at most `3mu`, a row and its double-block carrier cost at most three more units, and

`3mu+3 <= 4mu <= M Rcheck/4`

for `mu>=3`, `M>=16mu`, `Rcheck>=1`. Thus all determining data and carriers outside that strip are unchanged: this is the actual upper-loss input required by SEP-L. Under (1.0), `M>=L^3 M_1'` already gives this floor for `L>=3`, `mu=M_1'`. W1/W2 use this strip. W3's equality of full and cut meets additionally uses its stated GEO3 clearance, not just A3. W4 uses the periodic set recursion directly; no common-lift hypothesis is needed for its wrapping complement. This does not discharge GEO or EXT.

**D7 — row 4.5 uses the rule outside its declared input class. First failing step:** defining the tower of a fourfold enlarged *test* cube by Definition A, whose domain in §1 was only unions of `pi_p` M-cubes. Test cubes have side `M_2 Rcheck_t`; the source does not impose in this statement that this side is at least M, and the note argues using only its lower bound `M_2`. A smaller test-cube enlargement need not be a union of M-cubes. The same recursion can certainly be applied, but that extension must be stated before the universal table says the adopted assignment covers it.

**Written repair (proved):** extend the supplied rule to any union of cubes of a centred aligned grid of side `S>=M_1'`, where S is a power of L, with its actual input partition carried along. This includes `S=M_2 Rcheck_t`. The original M-grid assignment is unchanged. A1 holds because S subdivides into every grid used in the recursion; A2–A6 and A9 do not use M at all. A7 now refers to translations preserving this input grid. A8 uses its actual `max c_q` tube, or an M tube if available. Thus this is a compatible explicit extension, not an appeal to a different tower.

With that extension, **4.5 is ADVANCE.** Let `S>=M_2>=L M_1'`. The twice-enlarged cube, with adjacent unit blocks included, has depth at least `2S-3` inside the fourfold enlargement. Since `2S-3>3M_1'` for the admitted large sizes, A3 puts the entire required footprint in the top member. Every lower member also contains it by nesting. The tower problem and all its lifted data are formed inside that part; therefore the localised background depends only on datum there. For restriction between two test towers, compare them in absolute levels and apply A5 to the stated containment of their parts. The required geometric containment and the passed indicators remain the consumers' premises. No equality with Balaban's exact erosion pattern is used.

**Row 4.6: ADVANCE for the current outer collar and the named top-member uses, after that extension. First failing step: none in these estimates.** One outside M layer plus an inside strip of width `3M_1'+3` is bounded by `2M`, using `M>=L^3M_1'`. Thus `(12.2)` of `support-envelope.md` is `2M+3<M Rcheck_k`, valid for `Rcheck_k>=3` and these large M. Its floor exclusion uses the separately supplied two-cell clearance in (12.1); it does not prove admission of arbitrary retained older collar reads. The top-member inclusion for `support-physical.md` is the one just proved for 4.5. Floor screening still reads Theorem 6(c) with its own hypotheses. The consumer claim is therefore a statement about exactly these reads, not a new proof of screening or support on all histories.

**Row 4.7: CORRECT-NO-ADVANCE, conditional exactly as flagged.** The extra hereditary margin follows from `M>=L(3M_1'+2)`, implied by the chosen large powers. Ambient containment still requires `Z subset Omega_p`. For the layered quantifier that is an explicit reading premise, not a result of A1–A9. **Row 4.8: ADVANCE as a use of the repaired A7–A9** on translations preserving the input grid and on common lifts with room; it makes no stronger covariance assertion. The table's exhaustive “every consumer” wording should retain these domain qualifications and the named upstream geometric/analytic premises.

## Ranked defects and disposition

There are seven defect groups, in order of what they block:

1. **D4:** the claimed enlarged-decoupling theorem is for the wrong monomial and uses walk support not contained in its quantitative premise. The repaired collared implication is written above; the walk construction itself remains an input.
2. **D2:** the claimed entire-complex-domain fibre identification omits the local coordinate transition. Its bounded correction is proved above, with the actual Cauchy-radius dependence retained.
3. **D3:** the boundary comparison uses curvature on plaquettes outside the background problem's domain. The ordinary step with fixed exterior data has the stronger exact-zero repair; other completions remain unspecified.
4. **D6:** supplied erosion does not itself derive the precise joining convention from qualitative wording, and the second-rule overlap proof uses a first-rule erosion bound. Adopt the joining formula explicitly and strengthen the stated collar-separation constant as above.
5. **D5:** the lift proof's metric inference is invalid and its one-cube/separation conclusions need the intended `M_1'>=rho` hierarchy. The quotient-neighbourhood proof repairs this without enlarging the total erosion radius per depth.
6. **D7:** the test-cube consumer needs an explicit extension of the assignment's input class. The same recursion supplies it and retains the required containment and locality.
7. **D1:** ambient and already-free quadratic forms are conflated. The exact corrected contraction is supplied; no new estimate is required.

No failing BCH sign, complex double-difference Cauchy step, or active-row layer barrier was found. Test 2.1 kills uniform smallness on the whole fine X space, not positivity or every possible fine-form proof. The preserved advances are the physical Hessian algebra after its notation correction, the local complex GF correction, coarse stability, the inner-profile estimate on its admitted domain, H-ct's centred Hessian implication, and the explicit erosion/locality construction after its repairs. Neither the actual H-walk expansion, H-ct accounting, H-prof identification, source bound, nor the upstream A1/A3 and history-geometry inputs is discharged here. Only this output file was written in the checkout; no audit, numerical proof, subagent, commit, push or external post was performed.
