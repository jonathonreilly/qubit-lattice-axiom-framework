lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T15:34Z

# p2-floor: check of `c1-repr.md`, then the floor's (P2) and (P3)

Queue row 179. Pinned at commit f20eba5f1. Complete; the result is Section 4.

**Moves:** D1's floor (`sa-ledger.md` rank 10; `t0-skeleton.md` D1, node "unsourced floor"). Written by Claude (Opus 5.5, max) on the Mac mini worker, fresh session. Research text, not an audit; it grants no status. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the history representation (SA 1a.2.3, L7463; the two layers, L17499), the average (L7049-7074), Theorem 2.1 (L17259), the never-large label and (ER7)-(ER8) (L6560-6640), B2 (L3937) and Theorem 5(a) (L9746). Their YM3_I Proposition I-3-55 (YM3_I L1971) is the precedent for the Borel average. T. Balaban for CMP 98, 102, 109, 119 and 122, as rebuilt in the notes cited. OpenAI Codex for `library/c1-repr.md`, checked below. Claude for `a3-close.md` Lemma T and `d1-floor.md`.

**Sources.** Outline `YM4_sketch_500.tex` and `YM3/YM3_I.tex` at `31a47c543775`, fetched by URL into a private scratch folder. Memory free was 45 percent, below the 50 percent floor, so no numeric job was run. Every step below is a written argument.

## 1. Check of `c1-repr.md` Sections 2-8 (Codex)

Checked line by line by Claude (Opus 5.5, max), commit f20eba5f1. Not an audit. Verdict per section, then remarks. No remark breaks a statement.

| Section | Statement | Verdict |
|---|---|---|
| 2 | Borel tests: the small-diameter mean is a contraction fixed point; existence and uniqueness sets are countable unions of compact projections; the unique solution is Borel; tests total, value 0 off their domain | ADVANCE, first failing step none |
| 3 | Kernel identity (1): K_h ≥ 0, Σ_h K_h = 1, exact sourced mass, \|τ_h^F\| ≤ ‖F‖_∞ τ_h^1; insertion kept inside deleted-slot integrals | ADVANCE, first failing step none |
| 4 | Average as δ_{M(U)}; soft gauge factor ∫G(U^u)du = 1; tests and storage; strip map a diffeomorphism with positive Jacobian; completed square exact | ADVANCE, first failing step none |
| 5 | Healing as relabelling; restriction and commuting kernels; three fates as measure operations | ADVANCE, first failing step none |
| 6 | R kernel (2)-(3) with recorded drop-out off 0 < D_r < ∞; one frame per summand; tree coordinates (4) with Jacobian 1 | ADVANCE, first failing step none |
| 7 | M_*μ ≪ dV (5); Haar densities ρ_{k,h} ≥ 0 and (6) at every finite depth | ADVANCE, first failing step none |
| 8 | (ER7) from A1 (9.2), (AV), (7.14) and Definition A, via a corrected Lemma T | ADVANCE, first failing step none |

**What was redone.**

- *Mean (2).* For Φ(H;T) = H + n^{-1}Σ log(T_i e^{-H}), D_HΦ = I − I = 0 at (T,H) = (1,0). So ‖D_HΦ‖ < 1/2 on a small ball, and |Φ(H;T)| ≤ |n^{-1}Σ log T_i| + r/2 < r for T near 1. Banach's theorem gives the unique, continuous, analytic mean. Right covariance moves any small family to one near 1.
- *Tests (2).* With the chart C σ-compact and the defining map F continuous, {V : ∃U ∈ C, F(V,U) = 0} = ∪_n π(F^{-1}(0) ∩ (X_m × K_n)) is F_σ. Two solutions at distance ≥ 1/n give another F_σ set. For open O, s^{-1}(O) is F_σ by the same argument with C ∩ O. So the unique solution is Borel.
- *Gauge factor (4).* C_{yx}(U^u) = u(y)C_{yx}(U)u(x)^{-1}, since the mean is bi-covariant. With u(y) = 1, each factor reads only u(x), and Haar invariance gives z for each. The draw keeps M(U) fixed. It equals multiplication by G only for a gauge-invariant measure, as SA L17499 says.
- *Average, regular rule (7).* Write P for the transport from x to the crossing edge along [x,x'], and Q for the same along U[c]. Under left multiplication of every crossing edge by e^{itH} (comb gauge of the double block),
  W_x(t) = (U(c_-,x)P) e^{itH} (U(c_-,x)P)^{-1} W_x Q e^{-itH} Q^{-1},
  so (1/i)Ẇ_x W_x^{-1} = Ad(U(c_-,x)P)H − Ad(W_xQ)H = O(c_M)\|H\|, because each transport is within CL²ϖ_c ≤ Cc_M of 1 (SA L7213). The factor U[c] gives Ad(e^{Y}Q)H = H + O(c_M)H. This is (1/i)Ṁ M^{-1} = H + E_cH, ‖E_c‖ ≤ Cc_M. Crossing edges of c are read by no other coarse bond, so the Jacobian has a block-diagonal full-rank minor.
- *Average, second rule (7).* A loop Y with transverse coordinate zero is identically 1; every other Y contains one non-central crossing edge once, so Y is a submersion and {Y = −1} has codimension 3. The determinant d_c is analytic on the connected set D_c, and d_c(1) = 1. Its zero set is covered by countably many regular hypersurfaces of lower-order derivatives. So M is a submersion off a Haar-null set, and (5) follows by Fubini in local coordinates.
- *Raw-datum correction (8).* At the flat field M has derivative Q^{pl}a = σ(c_-) + Q^s a − σ(c_+) (SA L7080, L7084); on one-colour fields M(e^{ifT}) = e^{i(Q^{pl}f)T} exactly (SA L7227), and Codex's field has one colour. In Codex's field, ā(c_-,x) = Σ_{ν≠μ}\|x_ν\|H, so σ(c_±) = ±3(L²−1)/(4L)·H, and Q^s a = LH. The raw coefficient is L + 3(L²−1)/(2L), which exceeds 2L for L ≥ 2. So `a3-close.md` Lemma T Step 3, "\|B(w)(c)\| ≤ 2ξ'_q sup\|w\|", is false for the raw increment. The bootstrap it cites (`a1-balaban.md` 3.5) bounds the *straightened* angle, with the endpoint factors removed. Codex's repair is right: (7.14) writes M^q(e^{iη_p w}U) = (e^{i𝔞_q}M^qU)^{v_q}; each new factor is within C t_{q+1}‖w‖_∞ of 1 (`a1-balaban.md` 7.6: ‖u − 1‖ ≤ C_L r_* t_r); so \|v_q − 1\| ≤ exp(C‖w‖_∞ Σ_{r<q} t_{r+1}) − 1 ≤ C' t_q‖w‖_∞ when λ‖w‖_∞ is small. Unitarity of M^qU then gives \|B(w)(c)\| ≤ C_A t_q‖w‖_∞. With R = c_T/λ and C_A c_T < r_B, the datum stays in the ball of (9.2). The rest is Lemma T Steps 1, 2 and 4: (7) S = C_0λ^{-2}; Cauchy on z ↦ f(zw) gives \|Q(w)\| ≤ 2S(‖w‖/R)²; the identity f(a+ib) = f(a) + if(b) − if(0) + Q(a+ib) − Q(a) − iQ(b) holds; λ^{-2} cancels against R^{-2}. So (8) holds with K_T = 3C_1 + 6C_0c_T^{-2}. The change of unit gives the factor L^{-2(j−p)}, stronger than (ER7) needs.

**Remarks (none breaks a statement).**

1. *Minimisers.* Section 2 makes tests Borel when their objects are critical points of continuous equations. SA L17346 says "localised minimal orbit", and Proposition 2.4 (L17636) uses the minima in a class. On the domain the run reads, A1 (8.2) and `ref-chart.md` Theorem 2.4 identify the minimum with the unique regular critical orbit, so Section 2 applies. Off that domain the test value is 0 by totality. If a later note defines a test by a minimum over a class without that identification, the existence set is a projection of a Borel set. It is then analytic, hence universally measurable, and integration against the history measures still holds.
2. *Gauge-restored densities.* (6) uses the restored Haar coordinates (4). The floor integrates ρ_{K,S_0} over B_s, which is not gauge invariant. (P2)'s right side is invariant under level-K gauge maps of V: a coarse map changes the representative (Id) by a block-constant map, under which the terms are invariant (Section 3b, (F1)). So (P2) can hold almost everywhere only for a density with that invariance. So the floor must read the restored densities, and (P2) must assert their invariance. With the slice measures, ∫_{B_s} ρ_{K,S_0} depends on the slice. This is a reading instruction for `d1-floor.md` Theorem F, not a defect.
3. *Section 8 versus `d1-floor.md` 4c.* 4c showed only that (9.2) applied to the raw increment at the near-zero radius gives a depth-dependent radius. Section 8 avoids this with the large ball R = c_T/λ and three real values. So 4c's "(ER7) is not in the library" is superseded: (ER7) is now an implication from A1 (9.2), `a1-balaban.md` 3.5 and 7.6, and Definition A, by Codex, checked here.

**State after this check.** C1 (P1) is proved by Codex and checked by Claude, first failing step none: exact sourced mass and non-negative label densities at every finite depth. (ER7) is proved by Codex from Claude's Lemma T with the raw-datum correction, checked by Claude, first failing step none. These remain implications from A1 (conditional on F0) and the adopted tower geometry.

## 2. (P2): the form at the never-large label

**Claim.** (P2) is Theorem 2.1 (SA L17259) read at the final label S_0. It adds no clause of its own. Its first input that is not supplied is the response input of B4's (19), which fails for the adopted representative (Section 3b). After it come (LOC) and the typed tests.

**Reduction at S_0, checked against the outline's definitions.** At S_0, Ω_j = Λ_j = T and S_j = ∅ for every j, and there are no marks.

- T'_K(S_0) = 1. The integral operations of a label are those of its standing marks (SA L17257, L17451). S_0 has none.
- χ_{K,S_0} = χ_K(Ω_K) = Π_{□⊂T} χ_K(□) = χ_K (Lemma 2.2(c), SA L17369).
- B_K = 0. B-terms are indexed by X ∩ Z̃_j ≠ ∅ (SA L7624), in the action sequence (SA L17440). For S_0 that sequence has Z_j = ∅ at every level.
- x_K(·) ≡ x_K, since φ_j ≡ 1 when Λ_j = T (SA L17640).
- −ℰ_{K,S_0} = E = Σ_{j<K} 𝖤^{(j)}(T, T) (SA L7499).

So Theorem 2.1's display at S_0 is (P2), term for term. Nothing specific to S_0 remains to prove.

**How the outline treats it (FINISH item 9).** Theorem 2.1 is the conclusion of "the closed induction" (SA L17255). The outline lists its extension beyond Balaban as "Package C statements that we must prove" (SA L17290-17302): label independence of the remainders on all tori, positivity of each term, measure and formula as two layers, the class, the flow, the mass bound, the hull length, the three fates, the order of constants, and "exactness for each partition of the histories". It states that "the exponential form given below holds for sums of histories and not for an individual history" (SA L17257). The R-part of R^{(k)} "arises only through the sum over (𝔛, ς), a sum which R itself performs (Proposition 2.10 [outlined below ...])" (SA L17451). Classification: sketched. The step formulas 1a.2.8-1a.2.9 (SA L7569-7630) are implications from named obligations; 2.10 and 2.11 are outlined.

**Why the floor reads the label, not one history.** `d1-floor.md` Section 2: E carries Σ_X R^{(j+1)}(X, 1) at every level, and these include the healed parts. The never-large history alone lacks them.

**What (P2) reads, and the state of each input.** At every level k ≤ K, and for every label that heals into S_0:

| Input | State |
|---|---|
| C1, positivity and exactness | proved by Codex, checked here (Section 1), first failing step none |
| (ER7) = (ER8u) | proved by Codex, checked here (Section 1) |
| B4_k and 1.6_k, the step | implication from P + H_{<k} + BX⁺ + UR + YA + LOC (`b4-induction.md`, Codex, not yet checked); typed tests open (row 219) |
| (19)_{k−1}, inside B4 | Proposition W of `b2-extract.md`; it reads the response bound (R), false for (Id) (`ur-ya.md` (3)-(4)); see 3b |
| 2.10, the healed sums | reduces to (LOC); open (rows 204, 211, 214) |
| 2.11, class preserved (tube, flow, mass) | carried by the rows above; not closed |

**First failing input of (P2).** In reading order, B4's (19) at its response input: (R) is false for the adopted representative, and its substitute (Γ) of Section 3b is not supplied. Then (LOC). This is the same input that stops (P3) (Section 3).

## 3. (P3): (CG), the R-part, and B2

Notation of `d1-floor.md`: ε := 4s = 4cθ_K^{-1/2}, U := U_K(V) for V ∈ B_s, σ := σ_j = L^{−(K−j)}, D_X := 2 + diam_j X, r_j = cα_{0,j} the radius of (ER8). (P3) ⇐ (E_j) and (R_j) for all j, by `d1-floor.md` 4a (checked by Codex).

### 3a. Lemma G: (CG) holds

**Lemma G (one gauge with both C¹ bounds).** Assume the ceilings of `d1-floor.md` Theorem F and, in addition, that M·4Bcγ is below the threshold of Proposition 6 below. Let V ∈ B_s, j ≤ K, and let Q be a cube of side D ≥ 1 in level-j units with Dσ ≤ 1. Then there is a real gauge u on Q with U^{u^{-1}} = e^{iη_j a} on Q and, in level-j units,

  sup_Q \|a\| ≤ C_G Bε σ² D,  sup_Q \|∇_j a\| ≤ C_G Bε σ²,   C_G := C(L)·M·L.

*Proof.* (i) *Regularity at a coarser layer.* For S_0 every corner scale is 1 in level-K units. By A1 (8.2) and Lemma B(i), \|∂U(p) − 1\| ≤ Bε η_K² at every bare plaquette and \|J(U)(b)\| ≤ Bε at every bond, in level-K units. Let p be the least level with 2M L^{p−j} ≥ D. Since D ≤ σ^{-1} = L^{K−j}, p ≤ K, and L^{p−j} ≤ max(1, LD/(2M)) ≤ LD. Write s_p = L^{p−K} for the level-p scale in level-K units and α := Bε s_p². Then \|∂U − 1\| ≤ α η_K² s_p^{-2} and \|J\| ≤ Bε ≤ α s_p^{-3}. With the real-to-matrix conversion of `a1-balaban.md` Section 2, U lies in 𝔘(C(L)α) on every layer up to p, because every region of S_0 is the torus.
(ii) *Proposition 6.* `a1-balaban.md` 3.8, Proposition 6, needs no critical background (checked ADVANCE, conditional on F0: `gates/a1-balaban-gate.md` §2). On the two-layer cube of side 2Ms_p it gives a real gauge with U^{u^{-1}} = e^{iη_K A}, \|A\| ≤ CMα s_p^{-1} and \|∇A\| ≤ CMα s_p^{-2}, in level-K units, when Mα is small. Here Mα ≤ MBε, small by the added ceiling.
(iii) *Units.* Passing to level-j units multiplies lengths by σ^{-1}, a potential by σ and a difference quotient by σ². With s_p^{-1} = L^{K−p}, \|a\| ≤ CMBε σ L^{−(K−p)} = CMBε σ² L^{p−j} ≤ CMLBε σ² D, and \|∇_j a\| ≤ CMBε σ² L^{−2(K−p)} L^{2(K−p)} = CMBε σ². The cube of side 2ML^{p−j} ≥ D contains Q. ∎

This is (CG) of `d1-floor.md` 4b, with the sup bound in the same gauge. 4b took the sup bound from an axial gauge (SA Lemma 1a.3.1) and the gradient bound from another gauge. A Cauchy estimate on the ball (ER1) needs both in one gauge; Lemma G gives that. Axial potentials alone would not do: their transverse differences are not controlled by curvature alone (`gates/a1-balaban-gate.md`, on (7.10)).

### 3b. The Taylor path needs a representative the terms are not known to accept

Both (R_j) and (E_j) compare a level-j term at U with its value at the vacuum, by Cauchy estimates on a complex neighbourhood of a path from 1 to U. The only neighbourhood of 1 known to lie in the core is the near-zero ball of (ER8), ‖(A', J)‖_{1,j} < r_j, uniform in j. Three facts decide which paths it contains.

- **(F1) Supplied invariance.** The library gives invariance of members and terms only under bare gauge maps that are constant on level-j blocks (`b2-extract.md` §4, input (G); `carrier-adopt.md` Lemma L(c) and the limitation after it). Full covariance of single precision terms is impossible: the gauge-fixing Hessian G^{(2)}_V is not covariant (`h-walk.md` §2.1).
- **(F2) Evaluation point.** Terms are evaluated at the adopted representative (Id), the augmented contour-gauge branch (`b2-extract.md` §4).
- **(F3) Face-crossing response.** For the constant level-j datum B_1 = T, \|T\| = 1, the (Id) background is e^{itv} with v = T on the bonds that cross level-j block faces and 0 elsewhere. In level-j units \|H_jB\| = η_j^{-1} and \|∇_jH_jB\| = η_j^{-2} there (`ur-ya.md` (3)-(4), Codex). The smooth response of the same datum, in Landau gauge, is the constant T (`ur-ya.md` (5)).

**Consequence at the never-large background.** Let W_j = M^jU be the level-j datum. A coarse gauge map is block-constant at the bare level, so (F1) allows it. The best one, a coarse axial gauge about a root of X, makes the coarse angles of W_j on X^~ of order δ_X := Bεσ²D_X, and no smaller, since the curvature there is of order Bεσ². At first order the (Id) background of this datum contains the field (F3) with amplitude of order δ_X. Its potential relative to 1 has difference quotients of order η_j^{-2}δ_X at face-crossing bonds. For fixed K − j, the ratio η_j^{-2}δ_X/r_j = L^{2j}δ_X/(cα_{0,j}) is unbounded as j grows. So the straight path from 1 to the (Id) representative leaves the near-zero ball after a fraction of order η_j²r_j/δ_X of its length. A complex datum disc around the real path has width of that order, so a Cauchy bound along it costs a factor η_j^{-4} per domain, and the sum over domains diverges with the depth.

**The missing premise.** The path must run through a representative with C¹ control (Lemma G, or the Landau branch). That needs:

> **(Γ) Real local gauge invariance on the core.** For every level j, every term T of the class of level j (each remainder R^{(j)}(X, ·) and each pointed total of a member), every non-wrapping domain X, every real pair P in the core of X, and every real gauge map u on X^~ with P^u also in the core: T(X, P^u) = T(X, P).

Three remarks on (Γ).
- *What it gives.* It lets the path start at the representative of Lemma G (Proposition R' below). It also gives F^{(Id)}_z = F^L_z at real data, where F^·_z := G_z ∘ P^· for the contour-gauge and Landau branches. F^L_z is holomorphic and bounded on the whole disc ‖B‖_∞ < cα_{0,j}, by (R) for the Landau branch and (ER8u). The floor reads only real values, so it may take its Cauchy bounds from F^L_z. Where complex data are read (Proposition W inside B4), F^{(Id)}_z is holomorphic on a thin strip around the real ball (outer substitution, SA Theorem 5(c), L9757), and the identity theorem extends the equality to that strip. Differentiating at the vacuum gives D²G(X,0,z)[(dχ,0),w] = 0 for gradients dχ that vary inside level-j blocks. That is the identity `ur-ya.md` §3 names for (UR) (row 217). The floor needs more than this second-order jet, because its Cauchy estimates use a whole disc.
- *Where it stands in the outline.* The outline assumes it: B2's member "is locally gauge invariant" (SA L3942), and "each pointed total has local gauge invariance" (SA L16950). The class clause (ii) asserts only "invariance under a single fixed gauge action on the stored data" and independence of the splitting (SA L19420). So the outline assumes (Γ); it does not prove it.
- *Where it stands here.* The library supplies only (F1). For the precision terms from which the class's terms are built, (Γ) fails term by term (`h-walk.md` §2.1). So if (Γ) holds for the class's terms, it holds by cancellation inside each remainder and each pointed total. Whether it does is open.

**Defects found (each breaks a stated reduction, none refutes a target).**

1. *`d1-floor.md` 4b, (R_j).* The path (1, λa, J(e^{iλη_ja})), "where a is a gauge of U on X^~", evaluates R^{(j)}(X, ·) at a representative other than (Id). Equality with the value at (Id) is an instance of (Γ). 4b does not state it, and the library does not supply it. So "(R_j) needs no counterterm" is right, but (R_j) also reads (Γ).
2. *`b2-extract.md` Proposition W, Step 1.* "By (ER8u), the pair on X stays in the near-zero ball" needs ‖P_j(B)\|_X‖_{1,j} ≤ C‖B‖_∞, a response bound of type (R). For (Id), (F3) refutes it. So Proposition W reads (R), or (Γ), in Steps 1 and 4 as well as through (UR) in Step 3. Its input list should name it.
3. *The Landau switch of row 217 does not remove the requirement.* With the Landau branch, a coarse gauge map acts on backgrounds by a bare map that is not block-constant. Example: g(y) = e^{iy_1T} sends the zero datum to the constant datum B_1 = T. Its Landau background is the smooth constant T, which is 1^{g^L} for the smooth map g^L(x) = e^{ix_1T} (bare coordinates in level-j units). The block-constant transform of 1 is the field (F3) instead. So Theorem P's input (G) would need invariance of G under g^L, which (F1) does not give. The requirement moves from (R) to (G).

### 3c. Given (Γ), the R-part closes

**Proposition R' ((R_j) given (Γ)).** Assume (Γ), (ER8) with r_j = cα_{0,j}, Lemma G, the class clauses for R^{(j)} (‖R^{(j)}‖_{j,κ} ≤ g_j^{κ0} on the core, reality, splitting independence), and the real admission of `a3-close.md` Lemma R. Then, uniformly in K and the torus,

  \|Σ_X [R^{(j)}(X, U) − R^{(j)}(X, 1)]\| ≤ C (K + 2 − j) g_j^{κ0} N.

*Proof.* *Small domains, (1 + 2M)D_Xσ ≤ 1.* Take a cube Q ⊃ X^~ of side D ≤ (1 + 2M)D_X, so Dσ ≤ 1, and the gauge a of Lemma G. By (Γ) and splitting independence, R^{(j)}(X, U) = R^{(j)}(X, (1, a, J_a)), with J_a the current in that gauge. In level-j units \|J_a\| ≤ Bεσ³ ≤ Bεσ²D. So ‖(a, J_a)‖_{1,j} ≤ τ_X := (1 + 2M)C_G Bε σ² D_X. Put f(λ) := R^{(j)}(X, (1, λa, λJ_a)). For \|λ\| < Λ := r_j/τ_X the triple lies in the core by (ER8), so f is holomorphic there with \|f\| ≤ g_j^{κ0}e^{−κd_j(X)}. Its first derivative at 0 vanishes, since constant colour invariance makes DR^{(j)}(X, (1,0)) an invariant linear form on 𝔰𝔲(2)-valued fields, hence 0 (SA ER3). If Λ ≥ 2, Cauchy's estimates give \|f(1) − f(0)\| ≤ g_j^{κ0}e^{−κd_j(X)} Σ_{n≥2} Λ^{−n} ≤ 2g_j^{κ0}e^{−κd_j(X)}(τ_X/r_j)². If Λ < 2, then τ_X/r_j > 1/2, and Lemma R puts the real pair (U, J(U)) in the core, so \|R^{(j)}(X,U) − R^{(j)}(X,1)\| ≤ 2g_j^{κ0}e^{−κd_j(X)} ≤ 8g_j^{κ0}e^{−κd_j(X)}(τ_X/r_j)². In both cases the bound is 8g_j^{κ0}e^{−κd_j(X)}(τ_X/r_j)².
*Sum over small domains.* The rooted count with κ > κ_D sums D_X²e^{−κd_j(X)} over X containing a fixed cube (`b2-extract.md` §7, Step 6). There are at most Cσ^{-4}N root cubes. So the small domains give at most C g_j^{κ0}(Bε/r_j)² N: the factor σ⁴ cancels the cube count. Now (ε/r_j)² = C θ_K^{-1} α_{0,j}^{-2} ≤ C θ_j/θ_K, by SA L19430, α_{0,j}^{-2} = cθ_j(log θ_j)^{-2q}. The flow (Theorem 2.1's hypothesis x_i − x_j ≤ B_♯(j − i)) gives θ_j ≤ θ_K + B_♯(K − j), so θ_j/θ_K ≤ C(K + 2 − j) for θ_K ≥ 1.
*Large and wrapping domains.* For (1 + 2M)D_Xσ > 1, Lemma R gives \|R^{(j)}(X,U) − R^{(j)}(X,1)\| ≤ 2g_j^{κ0}e^{−κd_j(X)}, with d_j(X) ≥ c_M/σ − 2 in the tree-length units, c_M > 0 depending on M. Per root cube the sum is at most Cg_j^{κ0}e^{−c'/σ}, and σ^{-4}e^{−c'/σ} is bounded. Wrapping domains have d_j(X) of order the torus side and obey the same bound. ∎

With (ER8) supplied, this is `d1-floor.md` 4b's (R_j), with (Γ) added as a premise. Σ_j (K + 2 − j)g_j^{κ0} converges for κ0 > 4 (`d1-floor.md` 4a).

### 3d. Given (Γ), the E-part reduces to B2's identities

**Reduction E' ((E_j) given (Γ)).** Under (Γ), the members may be read on the Landau branch, whose response has the uniform bound (R): `ur-ya.md` (5), from the checked `flat-port.md` (9.9) and `a3-derivative.md` (34), (39). Then Proposition W, Steps 1-6 at one base point (`b2-extract.md` §7), applies to the never-large datum W_j with these inputs:

| Input | State |
|---|---|
| (P20): (20) for the pointed totals, one coefficient b_j | Theorem P, checked by Codex (row 202), under (TI) via Lemma R; Theorem TI checked by Codex (row 212); its premises (DOM) (Codex, not yet checked) and (ID) (= B4 at lower levels, row 213) |
| (ER8u) | supplied: (ER7), checked in Section 1 |
| (UR) and the coefficient bound (8) | `ur-ya.md` (1)-(2) from (ER8u) and (R) for the Landau branch; (8) follows from (UR) |
| (BX_0): near each base point z, in a coarse axial gauge about z, W_j = ℓ_z + E_z with the bounds of (BX), α_k replaced by CBε | `bx-fix.md` Lemma 3 (axial expansion; Claude, not yet checked, row 220), once U satisfies the Hölder clause (H). (H) holds at radius CMBεσ² by `a1-balaban.md` Section 6 (the four local bounds and the Hölder estimate for a critical background), rescaled as in Lemma G. The box-Hessian clause of (BX) is not needed: there is no box |
| (YA) | `ur-ya.md` (6)-(10) given (8), with the real admission of `a3-close.md` Lemma R |

Step 7's window, brackets and ν-disc are not needed. The age bound ρ² ≤ C(K + 2 − j) is the radii comparison of SA L7569. Summing the per-base-point bound C E_0[ρ²σ^{4+α_H} + ρ³σ⁶] over the Cσ^{-4}N base points gives (E_j) with f_ν = Cν^{3/2}L^{−α_H(ν−1)}, which is `d1-floor.md` 4a's input. This is a reading of Proposition W with a new datum, not a step-by-step rederivation; its check belongs with Proposition W's.

### 3e. Verdict on (P3)

- **(CG): proved** (Lemma G), an implication from `a1-balaban.md` 3.8 Proposition 6 (checked, conditional on F0), A1 (8.2) and `d1-floor.md` Lemma B.
- **(R_j): proved given (Γ)** (Proposition R'), from (ER8), Lemma G, the class clauses and `a3-close.md` Lemma R.
- **(E_j): reduced given (Γ)** to (P20) and (BX_0), with every other input supplied (Reduction E').
- **First failing input of (P3): (Γ).** Without it, the route fails at the response bound (R) for (Id), which (F3) refutes. Neither (Γ) nor its negation is proved here. No target statement is refuted.

## 4. Result

**Check of `c1-repr.md` (Codex), Sections 2-8: ADVANCE, first failing step none.** C1 holds for the measure operations, so (P1) is closed as an implication. (ER7) holds from A1 (9.2), `a1-balaban.md` 3.5 and 7.6, and Definition A. Codex's correction of `a3-close.md` Lemma T Step 3 is right: the raw coefficient is L + 3(L²−1)/(2L) > 2L.

**(P2): open.** It is Theorem 2.1 at the label S_0, with no clause of its own (Section 2). The outline sketches it. Its first failing input is the response input of B4's (19), then (LOC) and the typed tests.

**(P3): open.** (CG) is proved (Lemma G). The R-part is proved given (Γ). The E-part reduces, given (Γ), to (P20) and (BX_0). The first failing input is (Γ), real local gauge invariance of the class's terms on the core. The outline assumes it (SA L3942, L16950). The library supplies only block-constant invariance, and the precision terms fail (Γ) one by one (`h-walk.md` §2.1).

**For the floor as a whole.** (P1) is closed. (P2) and (P3) both stop first at (Γ), which is the same input that stops (UR) and hence B4 (row 217). So the floor adds no open input beyond B4's, except (BX_0) at the never-large datum.

**For the lead (evidence for other files; nothing else was edited).**

1. `d1-floor.md` 4c is superseded: (ER7) is now an implication (Section 1, remark 3).
2. `d1-floor.md` 4b reads (Γ) without stating it (defect 1 of 3b). Its sup and gradient bounds came from two gauges; Lemma G gives both in one.
3. `b2-extract.md` Proposition W, Step 1, reads the response bound (R) (defect 2 of 3b). With (Id), (R) is false by `ur-ya.md` (3)-(4). So Proposition W, not only (UR), stops at (R) or (Γ).
4. Row 217 (`ur-gauge`): the Hessian identity at the vacuum suffices for (UR) alone. Proposition W's Steps 1 and 4, and the floor, use Cauchy estimates on whole discs, so they need (Γ) on a real ball, not only its second-order jet at the vacuum. For B4's complex data the identity theorem then extends it. The switch to the Landau branch moves the requirement from (R) to Theorem P's input (G) (defect 3 of 3b). A repair candidate, not proved: build the terms with a gauge fixing that is covariant under all bare gauge maps, so that (Γ) holds term by term. `h-walk.md` §2.1 shows that the present gauge-fixing Hessian G^{(2)}_V prevents this.
5. `t0-skeleton.md`, node D1 (floor): (P1) proved by Codex and checked by Claude; (P2) and (P3) read (Γ); (CG) proved.

**What would change.** If (Γ) holds, the floor reduces to (P20) (the check of (DOM), and (ID) = B4 at lower levels), (BX_0) (with `bx-fix.md`'s check, row 220) and the class clauses of Theorem 2.1 ((LOC), typed tests). If (Γ) fails, B2's own-counterterm cancellation needs a bound on the contracted Hessian in the contour branch that does not pass through C¹ balls. Proposition W and (P3) would both need it.

**Method.** No numeric job was run; memory free was 45 percent, below the 50 percent floor. Every step is a written argument. Only this file was written.

**Status:** complete, 2026-11-04 (worker).
