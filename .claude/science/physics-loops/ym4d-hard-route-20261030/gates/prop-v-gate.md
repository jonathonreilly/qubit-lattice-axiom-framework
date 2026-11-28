# Proposition V and the meaning of the WF7 replacement (row 144)
Provenance: OpenAI Codex, GPT-6 family (exact deployment identifier and runtime effort not exposed; queue request: xhigh); checkout `0d6f5c304053f101f89ed6e8f64a5d9854f7da36`; Sussman–Alpoge `31a47c543775`, `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. Hand research check, not an audit; no status is granted.

## 1. Scope and sources

This checks Claude's Proposition V in `gates/old-depth-gate.md`, steps (a)–(g), and its bearing on SA 15945–15960 and WF7. The older construction is Codex's `library/old-depth.md`, Sections 1 and 4–7. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline's averages, backgrounds, window definitions, response equations and estimates. Credit Claude for Proposition V, Definition D and Current-I; credit the authors of the cited local notes for their named conditional inputs. No numerical or computer-assisted proof is used: commands only retrieve, locate and write text.

Source conventions matter. Current-I and D are particular local specifications, not formulas uniquely fixed by the outline. The flat lift, old-box first-response estimate and admitted analytic charts remain named inputs; this check does not independently rebuild that package. The support and tail arguments needed from the walk expansion are checked below, with both `h-walk` check reports taken into account. `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from the sparse working tree; its applicable sections were read from this checkout's HEAD Git object. No workflow automation or audit is run.

## 2. Steps (a)–(f), checked by hand

Throughout this section the ambient sequence is constant through level k, in level-k units. Thus its only determining rows have scale 1, its pillars have bounded physical diameter and bounded row density, and its metric is physical distance up to the fixed conventions. Write d for this metric, D for the flat curl, and L0 = DᵀD for the Wilson Hessian. This use of L0 avoids confusing the Hessian with the blocking factor L. All pairings below include physical lattice volume.

### (a) Exact support — ADVANCE

The support assertion is an algebraic fact, not a consequence inferred from exponential smallness. In W's formula

    Tω = h̃κ0 Sκ0 θκ0 Rκ1 ··· Rκn,
    Rκ = −[Ksystem,h̃κ] Sκ θκ,

the leftmost diagonal factor kills an output coordinate outside supp h̃κ0, and the rightmost θκn kills an input coordinate outside supp θκn. For n=0 the same two endpoint factors occur. Projection to the Aν block and multiplication by the diagonal raw-row scale do not enlarge either support. Both supports belong to the union of fourth enlargements, hence to D's union of sharp enlargements. If an endpoint is in Δ*, every nonzero term therefore has Δ* in its parameter set. Closed cube faces only add parameters; they do not remove Δ*.

With sΔ*=z and every other parameter 1, the set product is exactly z or 1, even for a walk that visits Δ* repeatedly. Absolute convergence gives

    H(s)=H+(z−1)HΔ,
    HΔ(x,·)=H(x,·) for x in Δ*,
    HΔ(·,c)=H(·,c) for c in Δ*.

The assertion about H1(s) needs more than the undecoupled equality H1=H. Here it is justified by the **specified expansions**: in `h-walk.md` Section 7, J=0 makes every jβ and every branch vertex Vβ zero; j⁽⁰⁾=0, and the surviving trunk local inverses and commutators are exactly the G-system ones. Under Definition D the surviving trunk uses the same union of sharp cubes. Thus the surviving coefficients **and their parameter monomials** agree. Arbitrarily assigning different hulls to the two expansions would require a new check.

The two walk reports do not invalidate this argument. The first corrects the graph-norm proof and the geometric read set, while expressly retaining endpoint support and W(a)–(b). The second supplies the larger sharp read set and warns about stage-2 field reads and midpoint conventions. We compare no different region sequences here, differentiate no background current, and use one cutoff convention throughout. At J=0 the branch terms vanish. If midpoint cutoffs are adopted, use their corrected O(L) margins consistently; the test is far inside Δ*. No claim of equality between two differently decoupled conventions is needed.

### (b) Field tangent — ADVANCE

At the flat pair R9's two remainders have zero first derivative. Consequently

    Ȧs=H1(s)b=zh+(z−1)w,
    h=Hb,   w=(HΔ−H)b.

Step (a) gives w=0 exactly on Δ*. This is not a claim that w vanishes outside Δ*, or that the full decoupled field is constrained critical.

### (c) Assigned current — ADVANCE

At zero, Current-I's anchor and base current vanish. Derivatives of row conversions, inverses and transports multiply these zeros. Its remaining derivative is

    j̇s=KᵀH(s)ᵀL0 Ȧs.

Every row c read by Kᵀ at b* is within a fixed current distance of b*. Choose b* within a fixed distance of the centre of Δ* and enlarge the lower threshold for ℓP so these rows are inside it. Step (a) then gives H(s)ᵀ=zHᵀ on those rows. With f=L0h=Kᵀλ and KH=1,

    KᵀHᵀf=Kᵀ(KH)ᵀλ=f,
    j̇s(b*)=z²f(b*)+(z²−z)r(b*),
    r=KᵀHᵀL0w.

The transpose is bilinear: there is no conjugate of z. This is the derivative of the adopted reduced readout, not the derivative of the actual current of As.

### (d) Actual old-box current — ADVANCE, with units made explicit

Set V=exp(iη νζAs(ε)), t=0. At (ε,ν)=(0,0), both separate first derivatives of V vanish; its mixed derivative in potential coordinates is ζȦs (in matrix coordinates it is iηζȦs). Thus the second derivative of the nonlinear average/background composite multiplies zero; its mixed current coefficient is its **first** derivative on ζȦs. This justifies differentiating the actual nonlinear map, rather than replacing that map at finite fields.

Restriction of the explicitly critical Cartan family at its own averages gives JR DM[h]=f on the central stencil. The datum DM[(ζ−1)h] has support at old distance at least d0 M/σ−C_L. For the other term, w=0 on Δ* implies DM[ζw]=0 on every old row whose whole averaging carrier is inside Δ*. Its support is at old distance at least ℓP/(2σ)−C_L. Average carriers at depth one have physical diameter O_L(σ), including their node contours.

There is no pointwise bound being inferred without a norm conversion. Step (f) supplies a uniform local energy bound for w; on a fixed lattice, a bond value is at most Cη⁻² times that bound. An old raw average therefore costs at most Cσ η⁻². The depth-one box has at most C_M η⁻⁴ rows. T4's normalized current-column estimate consequently bounds this tail by a fixed power of σ⁻¹ times exp(−θℓP/(2σ)). The h tail has the corresponding bound with d0 M. Therefore, in **old current units**,

    ∂ε∂ν Jbox_old(b*) = z σ³f(b*) + E_k(z),
    |E_k(z)| ≤ C σ⁻p exp(−a/σ) = o(σ³),

for some fixed finite p and a>0, uniformly for z in a fixed compact disc. Here a may be decreased and all fixed geometric constants absorbed into C. This also explains a normalization slip in the printed proof: old-depth (5.9) bounds σ³JR btail, not JR btail. Quoting its σ⁻³ prefactor for the latter omits σ⁻³. Retaining σ⁻⁶ there, or reducing the exponential rate, gives exactly the required conclusion; no claimed lower bound depends on that prefactor.

All assigned representative factors equal the identity at the flat datum. In Ad(g)J the extra mixed-derivative terms contain J(0), ∂εJ(0) or ∂νJ(0), all zero. A field gauge tangent has zero flat linearized current. Hence the coefficient includes the assigned nodes and Landau/axial conversions.

### (e) Subtraction and units — ADVANCE

Subtract the actual inner current from the assigned outer increment νjs. Changing current units contributes σ³, not σ. Steps (c)–(d) give

    ∂ε∂ν R_J(b*) = σ³(z²−z)(f+r)(b*) + o(σ³).       (V1)

The unshifted background is flat, with zero current, so its replacement has no mixed coefficient available to cancel (V1). At z=1/2, |f(b*)|=1 and |r(b*)|≤1/2 give a leading magnitude at least σ³/8; making the error at most σ³/16 gives the printed σ³/16 lower bound.

### (f) Uniform bound on r — ADVANCE

Here is the missing summation detail. For a raw unit row source e_c the dual source norm is 1, because its scale is 1. There are boundedly many admissible root cubes near an output pillar and at most ν1ⁿ length-n continuations. W(b), with M1 enlarged so q=ν1 C_W/M1<1, gives for every subfamily A of walks

    Σω∈A ||Hω e_c||E,y ≤ C e^(−τ_L d(y,c)/2) Σn≥0 qⁿ
                         ≤ C' e^(−τ_L d(y,c)/2).       (V2)

This is a local absolute majorant; it is not a volume-free sum of the separate global operator norms. Since w is minus the sum of walks avoiding Δ*, summing (V2) over the current rows with |b_c|≤8 yields

    ||w||E,y ≤ 8C' Σc e^(−τ_L d(y,c)/2) ≤ C2.         (V3)

In this constant-layer example, a shell of integer radius m contains at most C_L(m+2)^4 current rows or pillars, independently of η and the torus. Thus the exponential sum is finite uniformly in k and volume. For example the ratio of consecutive polynomial-times-exponential terms is eventually below e^(−τ_L/4)<1. No bare-bond counting factor occurs in (V3).

Flat integration by parts on the torus gives

    [HᵀL0w](c)=〈DHe_c,Dw〉fine.

The E norm contains the physical L² norm of ∇A, which controls the curl. Since w vanishes on Δ*, Dw vanishes on every plaquette fully inside it. Pillars touching its remaining support are at distance at least ℓP/2−C_L from each row read by Kᵀ at b*. Cauchy–Schwarz **inside each physical pillar**, (V2), and (V3) give

    |〈DHe_c,Dw〉| ≤ C Σd(y,c)≥ℓP/2−C_L e^(−τ_L d(y,c)/2)
                  ≤ C' e^(−τ_L ℓP/8).               (V4)

For the last inequality reserve half the exponent for the distance lower bound and sum the other half using the shell estimate. Enlarging a pillar to include a plaquette stencil costs a fixed constant. Kᵀ reads boundedly many current rows with bounded physical transpose weights: each averaged path has length O_L(1), and its fine incidence weight is canceled by the fine pairing volume in the transpose. Consequently

    |r(b*)| ≤ C3(L,M1)e^(−τ_L ℓP/8) ≤ 1/2            (V5)

once ℓP≥ℓ*(L,M1). Choose ℓ* also to cover the central row/stencil margins. This choice precedes k and is compatible with the outline's subsequent parameter-grid choice. None of (V2)–(V5) uses a false uniform embedding of energy into pointwise norms, a mixed-scale pillar count, or the current correction's region-comparison theorem.

## 3. Step (g), the room gap and its repair

**(g): WRONG as the printed justification of unchanged full-disc room.** Its estimate is stated for |z|≤1; the required disc has radius R=e^κ̄>1. More materially, the one-cube proof in old-depth Section 5.3 used the uniform pointwise first jet zh. On the grid the new jet is zh+(z−1)w, and (f) controls w in local energy, not uniformly in the first-order supremum norm. Shrinking ε suppresses nonlinear remainders, but does not change this linear coefficient. On the amplified ν-disc the product |ν ε| is of order α_k if δ_k=C_b|ε|, so shrinking ε alone cannot supply the missing uniform bound. Thus “applies unchanged” and “word for word” do not follow from the listed walk inputs. This is the first substantive unsupported step in the printed full proof; (a)–(f)'s coefficient argument survives.

There is a short repair which proves the counterexample without adding a pointwise walk theorem.

1. **Full parameter discs at fixed geometry.** Fix the compatible torus after ℓP and M, before k, with room for three parameter cubes per direction and a nonwrapping window. Let N_P be its finite number of parameter cubes. On the full closed parameter polydisc, |s^ω|≤R^N_P, independently of walk length and k. On the single-varied-parameter slice the sharper bound is max(1,R). Absolute walk convergence therefore supplies finite bounds throughout the closed polydisc. This uses no Lemma P or Theorem B; its constants may depend on this fixed torus. At J=0 the linear response uses only the branch-free W coefficients. The other convergent R9-local data give finite nonlinear constants at each k.

2. **Keep the mesh cost.** The E norm gives, for each fine bond and each first difference,

       |A(b)| ≤ η⁻² ||A||E,y,   |∇A(b)| ≤ Cη⁻² ||A||E,y+,

   with a fixed enlargement y+. Applying (V2)–(V3) with the parameter majorant gives a first-order sup bound C_geom η⁻² for Ȧs. The assigned-current first jet has a uniform bound: pair DH(s)e_c with DȦs, sum the exponentially decaying column bound over pillars, and apply the bounded local Kᵀ. Thus both relevant jets are bounded by C_geom η⁻². Here C_geom is fixed before k; no mesh-independent pointwise bound is asserted.

3. **Use an upper amplitude allowance.** Take

       δ_k=C_geom η⁻² |ε|,

   increasing the fixed constant to cover the free coordinates and cutoff derivatives. This is an allowed upper bound on the tested fluctuation, which has |B'(ε)|≤8|ε|+O(ε²); it need not be the smallest upper bound. For each fixed k choose ε small enough that the nonlinear remainders on the closed polydisc are at most the linear bounds and that δ_k is below the required fluctuation ceiling. The finite-dimensional contraction at zero in R9-local supplies such an ε. On |ν|<cν α_k/δ_k the complete field/current shifts now have first-order size ≤C cν α_k, with C independent of k. The named simple-to-core and old-background chart inputs supply the same fixed amplified room as before. This proves admission while allowing ε to depend on k, as the original example already did.

4. **The polynomial does not save WF7.** Its increment inequality, divided by |ν| and then |ε| at zero, would now imply

       |∂ε∂ν R_J(b*)| ≤ C η⁻² σ exp(−cM/σ)
                       = C L² σ⁻¹ exp(−cM/σ).        (V6)

   The lower bound σ³/16 contradicts (V6): it would give σ⁴ exp(cM/σ)≤16CL², whereas exp(x)≥x⁵/5! makes the left side at least (cM)⁵/(5!σ), tending to infinity. The derivative limits concern admitted actual holomorphic maps. Once the inequality is strict at a fixed k, sufficiently small nonzero ε and then ν give a finite window violation.

If the outline's uniform first-order response package is taken as an additional named premise, one may instead retain δ_k=C_b|ε| and recover the original σ² exp(cM/σ) contradiction. The proof above does not need that upgrade. It proves Proposition V's lower bound and its intended direct-replacement counterexample with the room repair made explicit; it does not validate the printed assertion that the one-cube room proof carries over unchanged.

| Step of Proposition V | Verdict | First failure or qualification |
|---|---|---|
| (a) | ADVANCE | None for the common sharp-hull specification; equality of totals alone would be insufficient. |
| (b) | ADVANCE | None. |
| (c) | ADVANCE | None for Current-I. |
| (d) | ADVANCE | None in the tail conclusion; retain old-current units or reduce the rate when quoting (5.9). |
| (e) | ADVANCE | None. |
| (f) | ADVANCE | None; physical pillar norms and the current-row density are essential. |
| (g) | WRONG as printed; ADVANCE with the repair above | Full-disc domination and uniform amplified room do not follow unchanged from the unit-disc energy argument. |

Checked line by line by Codex: **first substantive failing step (g); none in the repaired conditional counterexample.** The normalization clarification in (d) does not change any conclusion. All existence/response inputs named in Section 1 remain conditional.

## 4. Hostile reading from the outline's side

**The counterexample does not contradict SA 15949–15959 as written. It contradicts its direct-WF4-pair interpretation for Current-I and D.** Calling it an established error in WF7 would still overstate the result after the partition repair.

The distinction follows from the pinned text, not from a charitable replacement of it:

* SA 15753–15779 (WF3–WF4) and 16137–16176 (WF13a) prescribe the **inner** pair: form the actual nonlinear old datum, solve the old constrained critical box problem, and take that configuration's actual current in its assigned representative. That part is unambiguous.
* SA 15945–15960 then distinguishes the outer and removed substitutions from that inner pair, assigning them reduced currents away from the critical physical locus. R8 (SA 5747–5759) likewise expressly says that replacing the independent current by the shifted field's actual current changes the construction. R9 (SA 5786–5790) makes the reduced multiplier current separate input data. The outline does not give the formula of the old-box reduced current used in each removed substitution.
* SA 15837–15846 asserts the global action identity at complete physical pairs. It does not assert that the assigned outer pair minus WF4's actual pair is the sum of the two removed pairs at every complex parameter. Agreement on the physical locus supplies no identity theorem in independent s, current and interpolation variables held fixed on that locus.

Thus the inner configuration, current and nodes are forced. Their identification with the **complete box-side pair in a removed difference** is not forced. Even reusing the same box configuration would not identify its independently assigned reduced current with its actual current. Nodes cannot fix the direct mismatch, since their mixed-current contribution at this flat base is zero, but that fact does not remove the freedom to specify another reduced current.

### A permitted reduced-current reading, and what this example actually says about it

Read the removed pair as the difference between the original reduced readout and a prescribed box reduced readout, each with its own lift, anchor and assigned nodes. This is the reading explicitly allowed by SA 15957–15959. For illustration, apply the old-box reduced readout with decoupled lift H_R(s) to the WF4 box field. Let u be that field's first tangent. Its linearized critical equation is L_R u=K_Rᵀμ. On old rows inside Δ*, the same endpoint-support argument gives H_R(s)ᵀ=zH_Rᵀ. Therefore the box readout at the central bond is z times the actual box current coefficient. On Proposition V's grid this gives

    (jbox_red)εν,old = z²σ³f + O(σ⁻p e^(−a/σ)),
    (jouter_red−jbox_red)εν,old
           = σ³(z²−z)r + O(σ⁻p e^(−a/σ)).            (V7)

This cancels the decisive f term. In the one-cube case r=0 exactly. On the grid (V5) is only an **upper bound** for r, independent of age. It proves neither that r is nonzero nor that it has the superexponential-in-age smallness WF7 would need. In particular “r is of order e^(−τℓP/8)” must not be read as a lower bound or an asymptotic equivalent. No contradiction to (V7)'s possible WF7 bound has been established here. Conversely this cancellation is not a proof of that bound.

There is another natural reading of “box versions”: localize both response systems at their current depth. That need not use WF4's old actual pair at all. Its ordinary comparison length is M in current units, so its known exponential is e^(−cM), with the factor σ from changing potential units. A change of units does not turn its exponent into M/σ. This reading avoids this particular counterexample but supplies no proof of the printed stronger rate.

### A reading under which the old-rate sentence is a genuine boundary estimate

Compare **two old-depth critical maps**. Explicitly put

    p(ν) = (Π_j(V(ν)), J(Π_j(V(ν)))),
    Π_j(V) = Φ_(S≤j)(M_(S≤j)V),
    p_R(ν) = Pbox_j,R(V(ν)).

Include their prescribed node representatives in a common admitted chart. On the common old determining rows Π_j(V) has exactly V's nonlinear averages. When the box determining problem is the admitted old-depth meet, restriction of p gives a datum differing from p_R's only on the new collar. This identification holds for the constant ambient tower used here; in a general layered window it is a further hypothesis. This is a genuine old-to-old comparison; differentiating it gives the corresponding response comparison. In this reading “original background” means the old critical background over the averaged data, and “original response” means the derivative of that composite. It does **not** mean the unprojected current-step assigned pair q.

The precise sufficient bound is short. If the common old pair map F obeys

    ||DF(v)e_c||_x ≤ K e^(−θ d_old(x,c))

through an r-neighbourhood of the comparison segments, write w=v+β with β, β′ supported on the collar, and set B=Σ|β_c|, b=Σ|β′_c| and a=max(||v′||∞,||w′||∞). Differentiating

    F(w)−F(v)=∫₀¹ DF(v+tβ)β dt

and applying Cauchy's formula in a datum ball of radius r gives

    ||Δν(p−p_R)||_x ≤ K|ν|(b+aB/r)e^(−θ D_old).      (V8)

The estimate must include the actual node/representative components if a full pair norm is claimed. Native exponentially weighted collar sums can replace the displayed unweighted sums by reserving half the rate. With D_old≥d0 M/σ−C_L, b,a≤Cδ_kσ and B≤Cr in those justified sums, (V8) is WF7's exponential. This is the conditional old-depth boundary reading allowed by the sentence; it explains exactly which comparison makes the exponent correct. In the flat test its current coefficient is directly an old-distance tail, because both old projections have zσ³f as their central coefficient.

It is **not** a demonstrated completion of the outline's construction. Replacing q by p changes the off-physical extension; retaining q gives the exact identity

    Δν(q−p_R)=Δν(q−p)+Δν(p−p_R),                     (V9)

and the first term contains (V1). Critical-endpoint restriction can justify the projected physical action integral, but does not establish its exact fine-parameter restriction. The pinned row 145 and `wf7-extension.md` Section 5 explicitly flag this: an undecoupled global old projection can still read a remote input behind zero step parameters, whereas WF13b (SA 16194–16209) requires dependence only on the surviving local pair. Its additional localization and quantitative bounds remain obligations. I use that warning to exclude a claimed completed repair, not as newly checked proof of all of row 145.

**Answer to the reading question:** yes, the text permits distinct reduced box readouts, and its old-rate sentence has a valid conditional meaning as an old-to-old background/response comparison with (V8)'s hypotheses. Neither reading is refuted by the direct current-degree counterexample. No fully specified continuation satisfying *all* of the outline's window, node, full-disc and fine-bracket requirements is proved here. The outline's ambiguity cannot be upgraded either to a proved error or to a proved repair. Verdict on the scope claim: **CORRECT-NO-ADVANCE**; the direct-pair route is ruled out, while WF7 as worded remains unresolved.

## 5. Short standalone counterexample to the direct-WF4 replacement

This capsule uses the outline's flat constrained lift and old-box first-response estimate as named inputs. Its additional choices of walk monomials and reduced current are stated explicitly, so a reader needs none of our library notation. Credit for the outline's ingredients is as in Section 1.

**Window.** Fix odd L≥5, a compatible large torus and a parameter grid of side ℓP with at least three cubes per direction. All ambient regions through level k+1 are the torus. Work in level-k units with η=L⁻k=1/N and σ=Lη=L^(1−k); hold the torus, ℓP and M fixed while k increases. Set one central parameter to z and all others to 1. Every walk gets the product of the parameters of cubes intersecting its enlarged support hull, including both endpoint supports.

Here is an explicit physical fluctuation. On a period of L unit blocks let

    (q0,q1,q2,q3,q4,…,qL−1)=(0,1,0,−1,0,…,0).

For the v-th fine site of block m, 0≤v<N, put

    p_i=ε N⁻²[q_m+(v+1)(q_(m+1)−q_m)/N],
    a_(i+1)−a_i=arcsin(p_i),   Σperiod a_i=0,
    U2(x)=exp(i a_(x1/η) T),   Uμ(x)=1 (μ≠2),
    T=diag(1,−1),   (1/2)tr(T²)=1.

Opposite blocks have opposite increments, so a is periodic. Commutativity and the symmetric averaging contours give a level-k angle B_m=Σ_(i in block m)a_i and a level-(k+1) average equal to 1. The fine action derivative is

    sin(a_i−a_(i−1))−sin(a_(i+1)−a_i)
             = −ε(q_(m+1)−q_m)/N³.

Converting angle to potential and dividing by fine pairing volume makes the actual current −ε(q_(m+1)−q_m)T. This is the adjoint straight-average multiplier, constant on each block. Site-factor derivatives are coarse gradients and pair to zero with this direction-2 divergence-free multiplier; perpendicular colour derivatives vanish by constant Cartan-conjugation invariance. Thus the family is constrained critical against all variations. Its tangent h has |h|≤8, |∇h|≤2, b=Kh bounded by 8, h=Hb and L0h=f=Kᵀλ. Choose b* near the central parameter-cube centre with |f(b*)|=1.

Choose ζ=1 within distance d0 M of b*, supported in its enlarged current window R. The old depth-one first-rule tower is T0=R and T1 the union of aligned cubes of side 𝔐σ at distance >ρη from Rᶜ; later members are empty. For large k the central stencil lies in T1, and the old distance to the changed collar is at least d0 M/σ−C_L.

**Coefficient.** Let HΔ sum the walks whose hull meets the central parameter cube and w=(HΔ−H)b. Endpoint support gives w=0 in that cube and the response tangent

    Ȧs=zh+(z−1)w.

Choose the reduced current whose flat first jet is j̇s=KᵀH(s)ᵀL0Ȧs. This is the choice being tested. At b*,

    j̇s=z²f+(z²−z)r,   r=KᵀHᵀL0w,
    |r(b*)|≤C e^(−τℓP/8)≤1/2.

The last bound follows by writing HᵀL0w=〈DH,Dw〉, using bounded physical L² energy for w and exponential column energy for H outside the central cube, and summing unit-pillar shells. Choose ℓP sufficiently large before k. For V=exp(iη νζAs(ε)), the old critical box's **actual** current has mixed coefficient zσ³f+O(σ⁻p e^(−a/σ)): restriction gives f for h, and the cutoff and w data are at the old distances just stated. Assigned nodes contribute zero at this mixed order, since all lower-order currents at the flat base vanish. Therefore the direct removed difference has

    ∂ε∂ν R_J(b*) = σ³(z²−z)(f+r)(b*) + O(σ⁻p e^(−a/σ)).

**Inequality.** At z=1/2, for large k this has magnitude at least σ³/16. The error is o(σ³) by exp(x)≥xⁿ/n! with any integer n>p+3. Uniform pointwise response bounds would make WF7 demand an upper bound Cσ e^(−cM/σ), contradicting σ² exp(cM/σ)→∞. Even without that pointwise input, the elementary mesh conversion and admitted amplitude allowance δ_k=Cη⁻²|ε| in Section 3 make WF7 demand C L²σ⁻¹e^(−cM/σ). That contradicts σ⁴ exp(cM/σ)→∞. The exponential-series fifth term already proves the latter divergence. All choices can be made on the full parameter discs; sufficiently small nonzero ε,ν then violate the proposed inequality at a finite mesh.

This is a counterexample to **assigned current-step pair minus the actual old critical box pair** having only the WF7 exponential. Substituting a separately prescribed box reduced current changes the coefficient and changes the tested statement.

## 6. Recovery checkpoint and verification limits

The completed check's decision is: retain the grid counterexample with Section 3's room repair; do not report it as an error in the outline's literal WF7. A further attempt to refute the separately reduced-current reading would need a nonzero lower bound for its residual r, or another coefficient, for an explicitly specified box readout. The old-projection reading instead owes its actual collar/node estimates and a compatible localization of the composed map. Neither obligation is discharged here. The new room repair is Codex research text, not a separate cross-provider check of that repair.

At completion, all ten local sources read for this check matched their HEAD Git objects: GOAL, FINISH, old-depth, old-depth-gate, h-walk, both requested h-walk reports, h-walk-fix, o1-decoupled and wf7-extension. In particular the reviewed Proposition V file has blob `e473edf96e12963bd31e6baf6196143e4dc545dc`; old-depth has blob `9141da3d5a9198f2ba9737abfc4b4951496472ac`. The outline's SHA-256 is `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. These are source-identity checks only, not mathematical evidence.

Only `gates/prop-v-gate.md` was written in the repository. The sole fetched external text is the requested pinned outline in `/tmp/sa_ym4.tex`. No scientific computation, subagent, audit, commit, push, PR or external posting was performed. No editable prompt or platform instruction was changed.

