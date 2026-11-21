# C1: exact positive history operations
Provenance: OpenAI Codex / GPT-6 (exact serving variant and runtime effort not exposed; row 176 requests max); checkout `a09e72326c8a86898546f75dcd038d13c02ccd4f`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; grants no status.

## 1. Check of `d1-floor.md`

Checked line by line by Codex: Lemmas L and B, Theorems F and U; first failing step none. These remain implications from the named inputs. Claude wrote the checked note. The proofs below grant no new status.

**L.** Centred blocks nest because L is odd. A lifted plaquette crosses zero, one, or two coordinate faces. Its holonomy is respectively 1, 1, or a coarse plaquette holonomy. Telescoping its four unitary factors gives the bound 4s. Every contour inside a block has transport 1. Each averaging segment has the same coarse crossing as the straight transport. Thus every W_x is 1. The main rule applies when 4s < c_M L^{-2}, and M(V^(q)) = V^(q+1). Substituted rows at seams therefore have the same lifted values.

**B.** Apply the stated A1 bound with datum error 4s. On the global top layer the corner scale is 1. On a test tower, Definition A and `assign-adopt.md` 4.5 put every tested plaquette in that layer. Frozen outer bonds give the boundary problem used by A1. Thus both curvatures are bounded by 4Bsη². For SU(2), a_p = |U_p−1|²/2. Multiplication by 6η^{-4}N plaquettes gives A ≤ 48B²s²N. The strict inequality 4Bs < ε_K makes every test pass. This uses the supplied A1 and tower geometry, without reproving them here.

**F.** Lemma H follows by integrating (2/π)sin²ϑ on 0 < ϑ < s and using sinϑ ≥ 2ϑ/π. Work in the stated small-coupling regime, with γ ≤ 1, hence s ≤ 1. By (P1), retain the nonnegative S_0 term and then restrict to B_s. By (P2), (P3), and B,

    e^(−E) ρ_(K,S_0)(V) ≥ exp[−(E_− + 96B²c²)N],  V ∈ B_s.

The 4N independent Haar balls have mass at least [8c³θ^(−3/2)/(3π³)]^(4N). Their product gives exactly Theorem F and its coefficient 6 log θ. Neither (P2) nor (P3) follows from C1.

**U.** Write each summand as exp[−E−ℰ(w)−ℰ_S(w)] times e^(ℰ_S(w))τ_S(w). Its modulus is at most e^(C_0N+q(S))W_S by OH2. Sum and apply OH3. This proves OH4 without taking a logarithm. The construction of OH1–OH3 remains separate.

The summation in Section 4a also holds: its R-series is bounded by a constant times Σ_(n≥0)(n+2)(1+λn)^(−κ_0/2), which converges for κ_0 > 4. Section 4c correctly finds a loss in the direct use of A1 (9.2). Its conclusion that ER7 needs a new complex radius reset does not follow. `a3-close.md` Lemma T supplies a larger-ball argument. Section 8 checks it, corrects its raw-datum constant, and closes ER7 from the existing inputs.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the history construction, C1, and the floor and OH4 arguments. SA line numbers refer to their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. T. Balaban supplies the RG constructions in CMP 109 (1987), 249–301, and CMP 119 (1988), 243–285. Any part used below is proved explicitly. Source retrieval and text searches supply no mathematical evidence.

## 2. The spaces and total tests

Fix a finite torus, finite depth, and the real auxiliary frame. Sources never change this frame. Fix orders on the finite bond and component sets for forests and sequential moves. A state consists of a finite history record and its currently stored field coordinates. Each coordinate space is a finite product of SU(2), real vector spaces, and finite sets. Give each slot its level, bond, and creation event. Deleting a slot means taking its marginal. Reading a slot does not create another integration variable.

The relevant precedent is Sussman–Alpoge's YM3_I, I-3-55 and I-4-67 (lines 1971–1995 and 2157–2198). Their QED3 one-step construction (lines 8515–8585) uses Grassmann activities; it supplies no positive Yang–Mills history kernel. We use no positivity assertion from that fermionic expansion.

Here is the required measurability argument. Products, inverses, and the intrinsic logarithm on SU(2) minus {−1} are continuous. The small-diameter mean is analytic: for T_i near 1, write its equation as

    H = H + n^(−1) Σ_i log(T_i exp(−H)).

The derivative on the right is zero when all T_i = 1 and H = 0. The log and exponential series make its norm less than 1/2 on a sufficiently small ball. The right side maps that ball into itself after reducing the diameter. Iteration gives a unique limit, continuous in the data. Differentiating the convergent iteration gives its local analytic branch. The estimates use averages, so the number of contours causes no loss.

Existence and uniqueness tests also have Borel domains. Work in a fixed finite gauge slice. The defining equations for a regular critical point, or for a mean, are continuous on their chart. Exhaust that chart by countably many compact sets, with strict inequalities kept a positive distance from their boundaries. Include bounded Lagrange multipliers in this exhaustion where needed. Existence is a countable union of compact projections. Existence of two distinct representatives is treated with two copies and distance at least 1/n. Its projection is also such a union. Their difference is the unique-solution domain. Intersecting the graph with the inverse image of an open set proves that the unique solution is Borel. A rooted forest fixes residual gauges by finite path products, so this argument also tests uniqueness of an orbit. This proves measurability; it does not prove existence on a claimed support.

A test has value 1 precisely where every required object exists and every displayed inequality holds. Give it value 0 elsewhere, as SA 17347 specifies. A failed logarithm or background therefore has a recorded failure outcome. The extension test of R is Borel too: its strict finite curvature inequalities define an open set of exterior and interior fields, whose projection is open. The measure operations require no activity series. Finite hulls, boxing, class decisions, and changes of labels are then Borel maps. Boxing can add cells only finitely often. The collar recursion examines new bonds at each round. Preparation has a prescribed finite number of stages. Thus each finite-depth run has finitely many moves and outcomes.

## 3. The exact kernel identity

For a state x, a total test χ has the two kernels

    P_a(x,dy) = 1_{χ(x)=a} δ_(x,a)(dy),  a = 0,1.

Their sum has mass one. A Borel map uses δ_(f(x)); a draw uses its stated probability law. Projection deletes a slot. Every other slot is carried by an identity kernel. These statements follow directly by integrating the constant function 1.

Let μ_0(dU) = exp[−βA(U)]dU. Compose the moves along each history h, and call the resulting kernel K_h. Induction on the finite tree gives

    K_h ≥ 0,                 Σ_h K_h(U,whole output) = 1,
    τ_h^F(B) = ∫ F(U) K_h(U,B) μ_0(dU),
    Σ_h τ_h^F(whole output) = ∫ F dμ_0,
    |τ_h^F| ≤ ||F||_∞ τ_h^1.                                      (1)

For the last inequality, take a finite Borel partition of B, bound each integral by ||F||_∞, and sum. Taking the supremum over partitions gives total variation. This also proves absolute integrability for bounded complex insertions. Thus the same finite integrations are valid for them. In particular, use F = exp(source) at finite volume, or any bounded gauge-invariant insertion.

Nothing here replaces the input insertion by the same function of the output. If it reads a deleted field, its value remains inside the numerator integration. Equivalently, its output value is dτ_h^F/dτ_h^1, bounded by ||F||_∞. This is the conditional insertion of SA 7463–7478. It depends on the input law; the kernels do not.

## 4. The ordinary step

**Average.** SA 7065–7074 gives three rules. The regular rule uses the mean and logarithm just constructed. The second uses finitely many path products and intrinsic logarithms, unless one product is −1. The last rule returns the straight transport. These rules have Borel domains and values in SU(2). Thus

    T(U,dV) = δ_(M(U))(dV)

is a total probability kernel. For an indicator 1_B, its integral is 1_B(M(U)). Linear combinations and bounded limits prove the push-forward formula for every bounded Borel function. This rebuilds the positivity and mass identity of Balaban CMP 119, (0.1), without treating a delta function as an ordinary density.

**Soft gauge fixing.** Put h(v) = 1_{|v−1|<ε} exp[−x(1−tr(v)/2)] and z = ∫h(v)dv. The Haar ball has positive mass by Lemma H, and the exponential is bounded and strictly positive. Thus 0 < z < ∞. Under a block gauge, each defined contour variable transforms as u(y)C_(yx)u(x)^(−1). The centre has u(y)=1. For each remaining site, Haar invariance gives ∫h(C_(yx)u(x)^(−1))du(x)=z. Undefined means contribute the factor 1, independently of the gauge. Multiplication proves ∫G(U^u)du=1. Draw u with density G(U^u), and transform all affected coordinates together. The coarse average is unchanged. For an invariant integrand, substitution U ↦ U^u gives exactly multiplication by G(U). This is Balaban CMP 109, (0.14)–(0.16), proved here. No determinant sign is assumed.

**Tests and storage.** Apply Section 2's two-outcome kernels to P, Q, R, collars, and rims (SA 17317–17367). On Ω^c retain the old bond and its constraint. On Ω retain the fluctuation coordinate; project only its Λ part. This is one partition of the slots. The strip and pivot coordinates describe the same integral, provided their actual inverse and Jacobian are kept. They are not new probability weights.

For clarity, the strip's one-bond map is Φ(W)=W exp(i[1−ϑ(W)]H), with the background held fixed. If |H| Lip(ϑ)<1, solving Φ(W)=Y is a contraction in W=Y exp(−i[1−ϑ(W)]H). It gives a unique inverse on the compact group. Differentiating gives a nonsingular Jacobian, with positive sign by deformation from H=0. On any such chart, substitution therefore uses |det DΦ|. Outside a justified chart one must retain the original variables. No truncated Jacobian or dropped indicator is an exact substitution.

Likewise, completing a conditional square preserves the integral. For a block matrix Δ with positive inner block A,

    (a,b)ᵀΔ(a,b) = (a+A^(−1)Bb)ᵀA(a+A^(−1)Bb)
                   + bᵀ(C−BᵀA^(−1)B)b.

Translation in a has Jacobian 1. Integrate the original indicator at the translated argument. All determinants and normalization factors stay in the expression. Real exponentials are positive, including a real remainder of either sign. Splitting their logarithm into E, R, and B is a further identity, not a proof of positivity for each activity. These are the positive-integral facts used from CMP 119, (3.23)–(3.29). Bounds and existence for the analytic formulas remain B4 and C4.

## 5. Healing, restriction, and large-field storage

**Healing.** Keep the field and change the finite record from h to its standing part. Sum the measures of all histories with that record. Projection and finite addition preserve (1) and positivity. An erased stored variable is integrated with every factor and insertion that reads it. It is never replaced by its vacuum value. This proves the measure operation. Identifying this sum with exp(Σ R(X)) is the separate claim 2.10 (SA 17451, 17958–18015).

**Restriction.** For coordinates (x,y), restriction to x is the kernel δ_x. Thus ∫f(x)d(pr_x μ)=∫f(x)dμ. An insertion depending on y must remain under that marginal. If two moves act on disjoint read and output coordinates, their kernels commute: on rectangles the two iterated integrals are equal; finite sums and monotone limits extend this to every Borel set. The same proof applies to bounded complex insertions by (1). This proves precisely the interchange used in SA 18877–18943 when its read-set premise holds. It does not prove that deleting a cluster and recomputing a background has the same read set. That identification belongs to C2 and 2.10.

**Large fields.** A failed test keeps its complementary indicator. A failed stage keeps its unsummed core, remaining constraints, current fields, and all factors already formed. An island keeps its frame, slice measure, reference denominator, and stored variables. A later move either carries these slots unchanged or projects their whole joint measure. These are the three fates at SA 17642–17655. No estimate on their masses is needed for (1). In particular, a signed connected activity is never substituted for a positive history weight.

## 6. The R operation and its gauges

Freeze the exterior and all passenger slots, denoted e. In frame r, let q be the free bonds of the reference tree slice. Let λ_r(dq) be product Haar on these bonds, with every tree bond fixed to 1. The tree includes its entrance bond. Define the nonnegative Borel function

    a_r(e,q) = 1_(reference defined and cutoff passed)
               exp[−x_k A(φ_X,U_(k,X)(qV_Λ))],
    D_r(e) = ∫ a_r(e,q) λ_r(dq).

Integrals of nonnegative Borel functions are Borel: prove it first for rectangles, then simple functions and monotone limits. On 0 < D_r(e) < ∞, set s_r(e,dq)=a_r(e,q)λ_r(dq)/D_r(e). Else take the recorded drop-out, with all current slots retained. This is exactly the normalization convention of SA 17508 and the reference law of 17604–17608. It needs no uniform lower bound on D_r.

If b denotes the old box slots, replacement is the kernel

    R_r((e,b),de' dq) = δ_e(de') s_r(e,dq).                         (2)

Its integral is 1 for each (e,b). For a sourced input μ_F, its output is

    s_r(e,dq) ∫ μ_F(de,db).                                       (3)

Integration over q recovers the original sourced mass. The insertion is inside the b integral. Pulling it out as F(e,q) would be wrong. Stages are Section 4's tests and projections before (2). Core variables remain stored until a move actually integrates them. The chain identity ∫δ_(M(V_(i−1)))(dV_i)=1 removes each intermediate V_i once, from the top down. It introduces no Jacobian or omitted scalar.

The frame is a draw of mass 1/|W_4|. Both numerator and denominator in (2) use that same r. Passing and failing tests partition the same measure in that frame. Thus Σ_r |W_4|^(−1)(χ_r+1−χ_r)=1. One cannot replace D_r by another frame's denominator. These facts prove the R normalization directly. CMP 119 itself postpones the detailed R construction (p. 244); its mention of R is not a proof of (2).

**Tree coordinates.** A tree delta defines a positive slice measure. It is not a function with respect to Haar on all bonds. Here is the exact way to restore Haar coordinates when writing a density. Anchor the exterior root. From leaves toward the root, replace each tree edge by its vertex gauge g_v. Haar left and right invariance makes each replacement have Jacobian 1. The remaining bonds become q. Reversing the recursion gives a bijection Ψ_e(q,g) onto the original bond space, and

    dV_box = λ_r(dq) ∏_v dg_v.                                    (4)

This proves the tree-gauge identity used by Balaban. The entrance bond removes the otherwise free common gauge. For invariant insertions, the integral over g is 1. Keep it when a full Haar representation is wanted. Then the reference density is a_r(e,q(V))/D_r(e), and its integral is 1 by (4).

Use the recorded slice q for each test that was defined on that slice. Restoring its gauge coordinates does not change that test or its frame. Carry the inverse coordinate map with the record. Path products, means, and intrinsic logarithms are gauge covariant, so the next average transports g to its coarse restriction. Thus (4) is a representation of the same invariant integral, not an assertion that a slice law already has a Haar density. Without restoration, (1) remains an identity of positive measures.

## 7. Haar densities at every finite depth

The Haar claim needs more than Borel measurability. We prove the missing fact for the actual three-rule average: it sends every Haar-absolutely-continuous finite measure to such a measure. Double blocks are nonwrapping, as required by the run.

Fix a positive coarse bond c. Every path defining M(U)(c) uses block-interior edges and one edge crossing the face between its two blocks. No other coarse bond reads those crossing edges. On the regular rule, put the double block in a fixed comb gauge at the field under consideration. Moving a path past one elementary square changes its transport by at most the plaquette error. At most C L² such moves compare any defining path with the comb. Thus these transports are within C L² varpi_c ≤ C c_M of 1 in this gauge. Perturb every crossing edge by left multiplication with exp(itH). Each defining transport and U[c] crosses the face once. Differentiating the log and exponential series therefore gives

    (1/i) (d/dt) M(U(t))(c)|_(t=0) M(U)(c)^(−1)
        = H + E_c H,       ||E_c|| ≤ C c_M.

Indeed, each transport derivative differs from iH times that transport by at most C c_M|H|. The averaged contour variables use no crossing edge. The logarithm and exponential derivatives differ from their values at 1 by at most C c_M. Their averages have total weight one. Choose c_M with C c_M < 1/2. This gives three independent output directions for c, on every regular configuration.

For the second rule, first disregard the regular-rule switch. Its formula N_c is analytic wherever all its raw loops Y differ from −1. A loop with transverse coordinate zero is identically 1: its paths retrace the same line. Every other Y contains its noncentral crossing edge exactly once. Varying that edge makes Y a submersion onto SU(2). Thus {Y=−1} is a closed submanifold of codimension three. There are finitely many such sets. Their complement D_c is connected. To check this, join points through coordinate balls. In each ball, choose a broken line avoiding the excluded sets. The forbidden intermediate points lie in cones over codimension-three submanifolds; these cones have dimension at most dim(ball)−2 and measure zero.

Differentiate N_c along the three vector fields that multiply all its crossing edges by the same group element. The determinant d_c of this output matrix is analytic on D_c. At U=1, all path transports become exp(itH), all Y remain 1, and N_c(U(t))=exp(itH). Hence d_c(1)=1. Its zero set has Haar measure zero. Here is the analytic fact used: at a zero of a nonzero analytic function on a connected domain, some finite derivative is first nonzero. The zero lies on the regular zero set of a derivative of one lower order. Countably many such sets cover the original zero set, and each is a smooth hypersurface. Analyticity excludes a point where every derivative vanishes.

The third-rule set is contained in the finite union {Y=−1}, so it is Haar-null. For finitely many coarse bonds, discard the union of these null sets and determinant zero sets. The derivatives in their separate face variables form a block diagonal matrix of full rank. Each fixed choice of regular or second rule extends analytically to an open domain. There are finitely many choices. The inverse function theorem supplies local coordinates (M(U),remaining coordinates) at every surviving point. In those coordinates, the inverse image of a Haar-null set is null by product integration. A countable cover proves

    μ ≪ dU  ⇒  M_*μ ≪ dV.                                       (5)

This argument uses no enumeration or numerical rank test.

Now induct on the moves. The bare Wilson measure has a Haar density. A test takes a submeasure, so preserves absolute continuity of the current field marginal. A soft gauge draw preserves it too: for each fixed gauge the action preserves Haar; integration over the gauge then preserves null sets. Coordinate changes retain their exact measures. Ordinary blocking uses (5). In (2), the unchanged exterior marginal is absolutely continuous; the restored reference law has a density in the box for every allowed exterior datum. Product integration proves absolute continuity of the new full field marginal. The drop-out branch retains the preceding marginal. Finite sums and projections over passenger slots preserve these conclusions.

Consequently each history, in the Haar representation (4), has a nonnegative density ρ_(k,h), defined almost everywhere. Group histories by their output label S. Equations (1) and (5) give, at every finite k,

    ρ_(k,S) := Σ_(h:S(h)=S) ρ_(k,h) ≥ 0,
    ρ_k := Σ_S ρ_(k,S),        Z(0) = ∫ρ_k(V)dV.                  (6)

Set every density to zero on the common null exceptional set if pointwise nonnegativity is desired. The measure identity is exact. Applying the same kernels to Fμ_0 proves the sourced identity. It does not identify ρ_k with T^kρ_0 after R acts.

## 8. ER7: the larger ball cancels the scale loss

ER7 follows from the checked real A1, its datum continuation (9.2), the straightened-average bounds (AV) with their endpoint factors, and Definition A. Credit Claude's `a3-close.md` Lemma T for the larger-ball and three-real-values argument. Checked line by line by Codex: **WRONG at Step 3's factor 2 for the raw datum**; the endpoint factors must be retained. The repair below changes fixed constants only. Credit also Sussman–Alpoge, SA 9746–9753, for the target estimate. No layered extension beyond the stated tower geometry is asserted.

Work in level-p units. Truncate either tower at n ≤ p and put λ=L^(n−p) ≤ 1. Take an element in the prescribed inner region, which lies in the top member by Definition A. Set

    Φ(w) = U_n(Z; exp(iη_p w)U),
    f(w) = η_p^(−2)(∂Φ(w)−1),  or  f(w)=λ^(−2)J_n(Φ(w)).

Here U is real, and J_n is the actual current in level-n units. It is not the triple's independent current.

**Real input.** If a real field has curvature at most aη_p², the curvature recursion is v_(q+1) ≤ L²v_q + C(L²v_q)². Its linear term counts the L² elementary plaquettes; interior edges cancel. Log and exponential series bound the remaining terms by the displayed square. Dividing by L^{2(q−p)} and summing the geometric errors gives v_q ≤ C a L^{2(q−p)}. The substituted rows at seams cost the fixed factor L². Thus the tower datum has radius at most C aλ². A1 gives |f| ≤ C_R a on the inner region. This holds for both tower rules and every allowed restriction.

**The raw-datum correction.** At the flat field, take a coarse bond in direction μ. Set the fine μ-potential to H, with |H|=1. For each transverse direction ν, set the positive-edge potential to sign(x_ν+1/2)H in the first block, and its negative in the second. Every contour then contributes |x_ν|H at each end. The straight segment contributes LH. Since L is odd, the average of |x_ν| is (L²−1)/(4L). Thus the raw one-step derivative is

    η_p[L+3(L²−1)/(2L)]H > 2Lη_p H,       L ≥ 3.

Multiplying this field by arbitrarily small real numbers disproves the raw bound with coefficient 2. This is a hand calculation, not a counterexample to ER7.

**A larger analytic ball.** For the straightened angles, (AV), from `a1-balaban.md` 3.5, gives

    a_(q+1) ≤ (1+Cε_0 t_q²)a_q + C t_(q+1)a_q²,
    t_q=L^(q−p),     a_0=||w||_∞.

Set b_q=λa_q. Then the quadratic coefficient becomes C t_(q+1)/λ. Both Σ t_q² and Σ t_(q+1)/λ are bounded independently of n,p. Choose the small constants so the product of linear factors is at most 5/4 and the quadratic increment at most b_0/4. Induction gives a_q ≤ 2||w||_∞ for these straightened angles.

Now retain the exact identity (7.14) of `a1-balaban.md`: M^q(exp(iη_p w)U)=(exp(i𝔞_q)M^qU)^(v_q). Each new endpoint factor differs from 1 by at most C t_(q+1)||w||_∞. This follows by differentiating its contour products, whose length is O(L), and its mean equation. Its constant term is 1. The previous factors restrict to the next nodes; they are not formed again. Therefore

    |v_q−1|, |v_q^(−1)−1|
       ≤ exp[C||w||_∞ Σ_(r<q)t_(r+1)]−1
       ≤ C' t_q||w||_∞,

when λ||w||_∞ is small. The sum is at most t_q/(1−L^(−1)). Since M^qU is unitary, the raw logarithmic increment now obeys |B(w)(c)| ≤ C_A t_q||w||_∞, with C_A fixed before depth. For

    ||w||_∞ < R := c_T/λ,       C_A c_T < r_B,

all its rows lie in A1's fixed continuation ball. First choose c_T below the averaging and datum thresholds, then ε_0,ε_1 ≤ c_T/2. The compositions are holomorphic on this ball. A1 (9.2) gives the crude bound

    |f(w)| ≤ S := C_0 λ^(−2),                                  (7)

where C_0 is fixed before n,p,volume. The large radius is for w; B(w) remains small.

**Three real values.** Write A'=a+ib with a,b Hermitian and traceless. Expanding one plaquette and moving all unitary links to the right gives

    η_p^(−2)|∂(exp(iη_p A')U)−∂U−iη_p²D_U A'|
       ≤ C(ε_1²+ε_0ε_1).

Both supplied curvatures are at most ε_0η_p². Hence |D_U A'| ≤ C(ε_0+ε_1²). Unitary transport commutes with Hermitian conjugation, so the same bound holds for D_U a and D_U b. Expanding again gives real fields exp(iη_p a)U and exp(iη_p b)U with curvature at most C(ε_0+ε_1²)η_p². The real-input argument therefore bounds f(0), f(a), and f(b) by C_1(ε_0+ε_1²).

Let Q(w)=f(w)−f(0)−Df(0)w. Cauchy's formula on the one-variable disc z ↦ f(zw) and (7) give

    |Q(w)| ≤ 2S(||w||_∞/R)²,       ||w||_∞ ≤ R/2.

Complex linearity gives the exact identity

    f(a+ib)=f(a)+if(b)−if(0)+Q(a+ib)−Q(a)−iQ(b).

For all three remainders, the bound is at most 2C_0c_T^(−2)ε_1²: λ^(−2) cancels against R^(−2). Therefore

    |∂Φ(A')−1| ≤ K_T(ε_0+ε_1²)η_p²,
    |J_n(Φ(A'))| ≤ K_T(ε_0+ε_1²)L^{2(n−p)},
    K_T := 3C_1+6C_0c_T^(−2).                                  (8)

This proves ER7 at complex data as an implication from the named checked inputs. At a domain of level p ≤ j, the radii become L^{−2(j−p)}ε_0 and L^{−(j−p)}ε_1. Equation (8) then has the factor L^{−2(j−p)}, which is stronger than ER7's required L^{−(j−p)}. The independent current remains subject to its supplied simple bound. No assertion equates it with the generated background's current.

## Result

- `d1-floor.md`: Lemmas L and B and Theorems F and U checked line by line by Codex; first failing step none, as implications. Section 8 removes its claimed need for a new complex radius reset.
- **C1 proved for the measure operations**, with total failure outcomes, fixed frame, and the insertion carried inside every deleted-slot integral. First failing measure operation: none. Equations (1) and (6) give exact sourced mass and nonnegative label measures at every finite depth. Equation (6) uses the explicitly restored Haar coordinates (4); an unrestored tree delta is a slice measure.
- **ER7 proved from the checked A1, average bounds with their endpoint factors, and adopted tower geometry**, by (7)–(8). Claude's Lemma T supplies the argument; its Step 3 needs the displayed raw-datum correction.
- The floor still needs (P2), and (P3)'s remaining CG and B2 inputs. OH4 still needs OH2–OH3, including Inn. Identifying the positive measure construction with the localized activity formulas remains B4, C2, 2.10, and C4; no such identification or stability estimate follows merely from C1.

The new C1 argument and the ER7 endpoint correction are by Codex, not yet checked by the other model. Only this output file was edited. All proofs are by hand; no audit, computation of a proof certificate, subagent, commit, push, PR, or post was used.
