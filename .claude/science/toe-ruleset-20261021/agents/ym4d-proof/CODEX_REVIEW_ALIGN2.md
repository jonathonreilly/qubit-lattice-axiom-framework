# CODEX_REVIEW_ALIGN2

## PRE-STATED

UTC: 2026-10-29T05:28:16+00:00

Role: independent hostile reviewer of ALIGN2_55.md. No model-family independence beyond the assignment is asserted as evidence. No git; write-set is this file only. Read-set: files explicitly named in the assignment, plus the two selected procedural files `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`. No snapshots or audit ledgers; large sources are located by string and read in bounded ranges. All computations will use exact rational/symbolic plain Python, with no generated files.

Prior exposure: the assignment, SCIENCE_WORKFLOW, and an index of matching headings/claim lines in ALIGN2_55. No derivation or check result has yet been independently evaluated. Claims below are targets, not accepted premises.

Targets and pre-stated falsifiers:

1. CW: rebuild flat critical data, constant-chain domain, both sharp norms, annihilation by the alignments, and the lower bound for t_+. A disallowed tangent, noncritical background, vanished commutator, missing norm contribution, or scale-dependent error that removes growth refutes the claimed witness. Distinguish refuting this norm-comparison premise from refuting all possible alignments.
2. N1-L / CONV-P: rebuild the finite-dimensional argument, gauge-action split and G_0/s completion. A hidden injectivity/surjectivity premise, wrong sign/factor, unsupported slot bound or background-dependent constant refutes the asserted proof or numerical constant. Conditional inputs remain explicit.
3. RED-double-prime: multiply maps with domains, signs and chart conversions explicit. A missing inverse, invalid quotient representative or omitted commutator term refutes the algebra.
4. HD: reconstruct the per-level source estimates and summations in the full sharp-to-N pair; test uniformity in k, dependence on sigma/theta, all slots and critical-point covariance. A bound for a different domain/norm or a lost scale factor defeats the upgrade.
5. LP: rebuild the left inverse, hierarchy, transpose locality and polynomial cancellation. Test every cited gate for whether it could distinguish the claim from a false one. Especially test whether B2's zero is forced by its witness, rather than evidence for the claimed detail estimate.
6. Subdivision: verify exact masks, reproduction/nesting, derivative and Holder estimates, constants and quantifiers for arbitrary odd L and the 5-adic beta certificate. Derive corrected numbers when a numeric claim fails. Keep infinite-lattice and periodic claims separate.
7. Recheck the four claimed refutations and level-0 weight dispute. Pin each symbol to a definition before comparing values; check quoted source locations by strings. Historical status assertions alone establish no theorem.
8. Audit the remaining ARGUED list and finish with exactly what may be banked, retaining every unverified premise and domain restriction.

Verdicts will be CONFIRMED / NOT-VERIFIED / REFUTED; mathematical claim statuses will be PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. A false proof step does not by itself prove the theorem false. Findings are appended as the investigation proceeds.

## F1 — N1-L removes the separate transversality assumption

Verdict: **CONFIRMED**. Claim status: **CONDITIONAL** on L1's slice injectivity, differentiable gauge covariance at a critical point, and a nonsingular log chart.

Attachment: `ALIGN2_55.md:124-134`, locating `Lemma N1-L` and `Γ is injective on Ker`.

Let V be the finite-dimensional tangent space (top level fixed), A the root-vanishing gauge functions, H the critical log Hessian, and K:A→V the actual log gauge generator. Gauge invariance gives HK=0. If Kλ=0, the invertible derivative of exp converts this to λ(head)=Ad(U)^{-1}λ(tail). Connected level-0 links propagate the zero value at a root to every site, so K is injective. Slice invertibility gives ker H ∩ ker Γ=0. Consequently Γ embeds ker H into A and dim ker H≤dim A≤dim ker H. Thus ker H=K A, and ΓK is invertible as a consequence. This argument does not assume the desired transversality.

The claim is not unconditional BFT nondegeneracy: the uniform inverse on the slice remains an input. The chart parenthesis at :125 needs an inverse: with the convention fixed at :399-400 (`𝒥` maps left-trivialized vectors to log vectors), the correct relation is Ξ_Z=−𝒥^{-1}K, not `∓J K` unless that J is explicitly the inverse chart. The dimension proof itself is unaffected.

## F2 — LP-1 algebra and polynomial cancellation; B2 cannot certify a rate

Verdict: **CONFIRMED** for the local algebra/polynomial identities; **REFUTED** for B2's nonzero quadratic prediction and for treating CB3 as evidence that B2 discriminates the desired detail rate. Claim status: **PROVEN** for these algebraic statements; **GAP** for a rate certificate supplied by that gate.

Attachments: `ALIGN2_55.md:439-465`, locating `Lemma LP-1`, `Lemma LP-2`, `first nonzero detail is the cubic one`; `checks/a2_55_lp_criteria.md`, `B2 PASS iff`; `checks/a2_55_lp.py:180-198`, `okB2 = (quadmax[2] != 0)` and `ratio_lin != F(1, 27)`.

Independently, M dν=Σ_Y a(y,Y)(ν(y)−ν(Y))=ν−SRν. At a retained node the interpolation row is a delta and its path is empty, so RM=0. Recursing λ_l=Sλ_(l+1)−M_lx_l gives Rλ_l=λ_(l+1); for x_l=dν_l it telescopes to λ_l=−ν_l when ν_k=0. Transposition proves the hierarchy exactly. These statements need neither a Green function nor a norm estimate.

Along a fixed-order coordinate path, summing a polynomial 1-form of degree≤p−1 gives a polynomial in the starting node Y of degree≤p in each coordinate. Tensor interpolation reproduces that polynomial and evaluates it at Y=y, where the path is empty. Hence M annihilates all quadratic 1-forms for p=3. The correct quadratic detail is **0 at both depths**, and the ratio is **undefined**, not 1/27. This is a structural cancellation, not an accidental favorable sample. B2's requirement of a nonzero quadratic detail is impossible for its intended operator. Its linear-interpolation control tests a different operator with different leading moments; failure of that control to have ratio 1/27 cannot turn the original impossible gate into a decay-rate test. In particular the script allows `ratio_lin is None` to fire CB3 too.

A genuinely nonzero test can use the one-dimensional component x(i)=i^3, embedded in four dimensions. Its discrete primitive is P(t)=t²(t−1)²/4. At fine y=1 with coarse nodes −3,0,3,6, cubic interpolation gives Mx=P(1)−IP(1)=((1+3)·1·(1−3)·(1−6))/4=10. For own x(i)=ρ^4 i^3 this is **10ρ^4**, and the matching residue at successive ternary depths has ratio **1/81**. This is a new independent witness, not a re-registration or a claimed rerun of B2.

The Taylor estimate for compactly supported fixed-order paths follows by subtracting an affine field and summing its remainder: A_s D_1^(2+α)ρ_l^(2+α)[∇x^c]_α. It proves the stated ρ_(l+1)^(2+α) order with C_D=A_s(D_1/L)^(2+α), on the infinite lattice or a support with a coherent lift. Periodic spline paths require a separate treatment below.

## F3 — The restricted-source comparison does not justify the stated full N bound

Verdict: **REFUTED** for the inference from representation-wise comparison to the displayed unrestricted-infimum bound; **NOT-VERIFIED** for that bound as a theorem. Claim status: **GAP**. The corrected restricted-representation statement is **CONDITIONAL** on L1/L2/CONV-P.

Attachments: `ALIGN2_55.md:206-223`, `N^{(θ)}(f) ≤ C_N·N(f)`; :269-277, `at σ = θ also`; :299-307, `What GP/L2 do not cover`; `CODEX_REVIEW_OFFGLOB.md`, locating `Taking an infimum over all source representations cannot be justified`.

Let R_0(f) be representations with G_l=0 for l≥1, and R_all(f) all representations allowed by ALIGN55's N. For R∈R_0, the geometric series proves J≤P0+Pc/(L^θ−1), and R(θ)=L^{−θ}R. Thus the valid conclusion is

    N^(θ)(f) ≤ C_N N_restricted(f),
    N_restricted(f):=inf_{R∈R_0(f)} N_expression(R),
    N(f)=inf_{R∈R_all(f)} N_expression(R) ≤ N_restricted(f).

The last inequality points the wrong way to replace N_restricted by N. A functional's mere possession of a (G_0;s;j) representation does not repair this: every finite source vector has a plain-current representation (take j=f). The restriction is on the representation used to measure it, not on which vectors exist. The file explicitly leaves uniformly controlled conversion of positive-level G_l open, so it cannot take the unrestricted infimum in :210/:275. For a consumer supplying a specific R∈R_0, the response bound in its **explicit representation cost** is valid; the same bound in the full N(f) has not been obtained. This repeats the exact quantifier problem already identified by OFFGLOB F11.

No counterexample to a possible future uniform N-to-N^(θ) conversion is asserted. It is the claimed deduction and its PROVEN labeling that fail.

## F4 — The chart maps are reversed in the L2 statement, but RED-double-prime's algebra is correct

Verdict: **REFUTED** for the source-conversion parenthesis; **CONFIRMED** for RED-double-prime as a matched-input implication. Claim status: **PROVEN** for the corrected linear algebra; **CONDITIONAL** for its estimates.

Attachments: `ALIGN2_55.md:125`, `Ξ_Z = ∓J K`; :243-245, `S = J^{−T}f`; :274, `equivalently S = J^{−T}f`; :398-420, `Chart map` and `Lemma RED″`.

Pin J=𝒥=ψ_−(ad y), mapping left-trivialized w to log v=Jw, as explicitly defined in §2.2. Duality forces f(v)=S(w), hence **S=J^T f**, **f=J^{−T}S**, **Ξ_Z=−J^{−1}K**. The theorem's S=J^{−T}f is the wrong direction. The §2.2 proof itself uses the correct f=J^{−T}S. A single J convention must be used throughout; the earlier formula cannot be accepted by relabeling J silently.

Re-derivation of RED-double-prime: K=−Ξ+K′, ΛΞ=−I, A=I+K′Λ. Then AΞ=−K, Υ=J^{-1}A has ΥΞ=Ξ_Z, and Υ^TH_ZΥ=A^TH_log A. For K^Tg=0, A^Tg=g+Λ^TΞ^Tg. For a reference representative x_E and u=K′Λx_E, the defect is exactly

    (H_log−H)x_E + Λ^TΞ^T H_log x_E
      + H_log u + Λ^TΞ^T H_log u.

The twisted-charge premise applies to H_log x_E and H_log u, both annihilated by K^T; it is not applied to the Hessian difference. This is the correct F1 repair. The four bounds give precisely the displayed δ_Υ. Invertibility follows from ||ΛK′||<1 on gauge functions via the finite-dimensional I+AB/I+BA identity; J is invertible on the specified chart. The displayed t_+ and t_* follow after supplying their chart/output and completion estimates. Their existence is not proved by the algebra.

## F5 — Periodic spline nesting is sound; a natural torus LP realization fails even on constants

Verdict: **CONFIRMED** for spline nesting and the one-dimensional bounds 3,6,12; **REFUTED** for applying infinite-lattice moment cancellation unchanged to shortest periodic paths; **NOT-VERIFIED** for the full torus P1′ as specified. Claim status: **PROVEN** for nesting and the explicit counterexample; **GAP** for the periodic detail construction.

Attachments: `ALIGN2_55.md:439-454`, path definition and polynomial-annihilation assertion; :511-537, `periodic cubic-spline subdivision`, `torus wrap terms`, `Proposition P1′(LP)`; `checks/a2_55_lp.py:200-260`, Part C.

The periodic collocation matrix is (4I+shift+shift^{-1})/6, with eigenvalues (2+cos t)/3≥1/3. A coarse cubic spline is a fine cubic spline with the same samples, so uniqueness gives exact nesting for every integer L. This proof includes small periodic grids; the tests cover only their listed cases. On the infinite lattice the inverse coefficients solve c_(j−1)+4c_j+c_(j+1)=6δ_j: c_j=√3(√3−2)^|j|. Summing absolute values gives 3. Convolution with the B-spline basis and its derivative bounds gives 3,6,12 and the displayed tensor partial bounds.

However, periodic nodal weights with shortest axial paths do **not** preserve the first path moment. An independent Fraction calculation solved the cyclic collocation system directly. For L=3 and five coarse knots (15 fine sites), the interpolation row at fine y=1 is

    (238/297, 113/297, −10/99, 2/33, −14/99).

The shortest oriented displacements from knots 0,3,6,9,12 to y=1 are (1,−2,−5,7,4). Their weighted sum is **40/99**, not 0. Therefore M(constant 1)=40/99 and μ=−40/99. For three coarse knots the row is (22/27,11/27,−2/9), displacements (1,−2,4), giving **−8/9**, not 0. Both are exact. Embed the first example in d=4 by making the field constant in one direction and evaluating other coordinates at retained nodes; the tensor row reduces to this same calculation. With physical own field ρ_l c, multiply the nonzero detail by ρ_l c. Its gradient Hölder seminorm is zero, so no finite C_D can give the LP-2 seminorm-only bound for this implementation.

The target does label the torus conclusion ARGUED; this finding explains why that qualification is essential. Small wrap terms cannot simply be absorbed into a zero seminorm. A periodized lift with winding paths, or an additional controlled sup-norm term and a revised proof, must be specified. I have not disproved existence of such a repair. Spline nesting and left-inverse algebra alone do not choose it. The compact s3 construction on a torus large enough for a coherent local stencil is unaffected.

## F6 — CW finds the right obstruction, but its slice-cycle proof drops a mesh error

Verdict: **CONFIRMED** for the constant-background calculation and, with the correction below, the asymptotic obstruction under the stated slice regularity/critical-point premises. **REFUTED** for the asserted telescoping of the gauge terms in Step 4. **NOT-VERIFIED** for CW's exact all-k coefficient at the prescribed BFT slice. Claim status: **PROVEN** for the explicit constant-representative calculation; **CONDITIONAL** for transfer to the BFT slice and the resulting obstruction.

Attachments: `ALIGN2_55.md:340-395`, `Proposition CW`, `Step 3 (the first contour moment)`, `Step 4 (the cycle average)`, and `same cycle-average argument applies to every representative`; `checks/a2_55_nc.py:65-108`, `nu_record` / `CN2`.

At the unprojected constant background put h=L^{−k}, a=hη ŷ, b=h ĉ at level 0. A negative traversal contributes −Ad_(prefix·Z^{-1})b, not −Ad_prefix b. The path-product derivative therefore gives, after the common final unitary rotation,

    r_0^Z(w)=Σ_{j=0}^{L−1}(exp(j ad_a)−I)b
            = L(L−1)h²η[ŷ,ĉ]/2 + O_L(h³η²).

This follows by deleting backtracking height crossings; every oriented path between heights 0 and L has the same signed lower-height count. Multiply by coarse conversion L^{k−1} and sharp weight L^{(1+θ)(k−1)}: the leading coefficient is exactly **(L−1)/(2L)** times L^{θ(k−1)}η|[ŷ,ĉ]|. With the stated flat normalization 2, the corresponding leading t_+ coefficient is **(L−1)/(4L)**. Flat plaquettes and soft residuals vanish, so this is a real zero-action critical configuration. Covariant gauge directions do not change the residual when ρ(Z)=0. Both HC and coherent-lift LP kill the constant chain. The missing dexp factor is a real mechanism, not a dimension-count artifact.

But putting this background into the BFT slice is not innocuous for the **unchanged left-trivialized** w. Already in one direction, at fine sites i and coarse roots nL, its first-order gauge contribution is

    Σ_{j=0}^{L−1}(λ(nL+j)−λ(nL)).

The average over coarse links is `sum_all_fine λ − L sum_coarse_roots λ`, divided by the number of coarse links. It does not telescope to zero. A root-pinned periodic exact witness is L=3, k=2, h=1/9, λ(i)=−η h^4 for i≡1,2 mod 3 and λ(i)=0 otherwise (independent of transverse coordinates). It obeys uniform coarse gradient/Hölder bounds: the correction to the coarse connection is O(ηh³), its coarse gradient O(ηh²), and its gradient α-seminorm O(ηh^{2−α}). Every coarse ν-link has first-moment coefficient

    η(3h−2h^4)=η·2185/6561,

instead of **η/3**. The relative factor is **2185/2187**, independent of η. It cannot be put into a relative O(η) remainder at fixed k. This witness challenges Step 4's inference from the stated regularity and root conditions; it is not asserted to be the actual Π_E gauge, whose specific formula is not in this review's read-set.

There is a valid weaker transfer. Expand λ over one contour to first order in spatial distance. The transverse first moments vanish after the centered offset average. Replace d_νλ(c_X) by (λ(c_Y)−λ(c_X))/L; these *coarse differences* telescope, with an error O_{L,C_Π}(h²η) per contour coefficient. Higher adjoint terms contribute O_L(h³η²) after multiplying w. Thus the justified lower factor has the form

    1 − C_{L,Π} h − C_L η,

rather than `1−C_Lη`. For h and η sufficiently small, a safe residual coefficient is **(L−1)/(4L)** and a safe t_+ coefficient is **(L−1)/(8L)**, both multiplying L^{θ(k−1)}η|[ŷ,ĉ]|. These are sufficient weakened constants, not optimal replacements for a verified all-k formula. Fixed positive η and k→∞ still give the obstruction.

For x_E=Π_Ew, linear color-independent projection makes the background scalar connection and x_E proportional at unknown levels. For an oriented scalar path with link values b_e, the first adjoint moment is `( (Σ ε_e b_e)^2 − Σ ε_e b_e^2 )/(2η)`; reverse links use the corrected prefix. On each small contour the connection is constant to O(h²η). The centered average has leading L(L−1)b_ν²/(2η). The coarse-cycle mean of b_ν is hη up to O(h²η), by preserved holonomy; mean square is at least square of the mean. This again gives a positive h²η leading term with an O(h) relative spatial error. Together with the reference bound |||Π_Ew|||≤2C_E this establishes failure of the slice NC estimate asymptotically, conditional on the specified regular projection and critical-point uniqueness. It does not supply CW's printed sharp coefficient for every k≥2.

Gate audit: N1 is a useful noncommutative ordering check and its wrong-reversed-prefix control is discriminating. N2's first moment is the discrete-antiderivative identity `Δ[t(t−1)/2]=t`, valid for **any** path with the same endpoints; the transverse signed multiset also cancels for every closed one-dimensional height trace. It does not test slice projection or spatial gauge variation. Once its two sums pass, CN2 necessarily fires since replacing h by h+1 adds Σ sign=L. The struck-through reversed-coordinate-order control could not have failed this endpoint identity. These checks cannot certify Step 4, any norm bound, or the all-k coefficient. The author's script appropriately disclaims those scopes.

Consequences: the qualitative NC obstruction and failure of t_+ for HC/LP that annihilate constants survive, with explicit premises and corrected mesh bookkeeping. The stronger claim about **every** possible alignment is not proved, and the file itself leaves that open. The statement that the same constant chain has zero log residual is exact at the constant representative; it is not an exact identity at an arbitrary projected nonconstant representative. Log-chart estimates can still repair the scale problem.

## F7 — CONV-P's algebra and scale sums survive; its norm scope must stay restricted

Verdict: **CONFIRMED** as a matched-input completion estimate in the σ representation norm. Claim status: **CONDITIONAL** on the stated local analytic chart, coarse regularity, and routing construction. It does not prove chart conversion or the unrestricted N comparison in F3.

Attachments: `ALIGN2_55.md:141-204`, `Lemma CONV-P`, `Step 1`, `Step 3`, `Step 4`; :225-240, `weighted form L2_m`; `CODEX_REVIEW_KOFF.md:170-215`, `Lemma HR`; `checks/a2_55_conv.py`, Parts I and II.

Re-derive K in the correct chart. Since δU U^{-1}=a−exp(ad X)c and δlog U=ψ_−(ad X)(δU U^{-1}),

    K_X=ψ_−(ad X)a−ψ_+(ad X)c,
    K′_X=−[X,(a+c)/2]−(1/2)Φ(ad X)(c−a).

Here Φ(z)=z coth(z/2)−2 is even and starts z²/6. This is the **log-chart** generator, despite Step 1 calling it left-trivialized. The identity follows from ψ_−−ψ_+=−z and ψ_−+ψ_+=2+Φ, not from a finite nilpotent sample. Since ad X is skew under the invariant bilinear pairing, Φ(ad X)^T=Φ(ad X). The stated norm majorant follows from its absolutely convergent even series inside the fixed chart.

For a plaquette based at z, split each endpoint mean λbar_b=λ(z)+(λbar_b−λ(z)); the four differences have coefficients (1/2), (1,1/2), (1,1/2), (1/2) along their indicated edges. Invariance of the Lie pairing gives the charge −[G,dy] at z plus a divergence current w_A, and the even remainder gives w_B. Counting incoming contributions to one link gives (d−1)(3/2+1/2)=2(d−1), i.e. **6** in d=4. This verifies both the sign and the coefficient mass independently.

Routing proof: a parent-root-to-child path has divergence δ_child−δ_parent. Summation over levels telescopes to the charge off the top roots. At one level, an axial link has at most M_γ=L^{d−1}(L−1)/2 descendants using it. For a divergence, internal fluxes cancel, leaving opposing boundary pairs. The sup estimate costs 2d M_γ per level; for level-0 Hölder data, opposing faces differ by a coarse distance L^{i−k}, giving d M_γ [w^c]_α L^{−α(k−i)}. The sum is bounded by 1/(L^α−1). For bare charges, the remaining scale sum is bounded by 1/(L−1). This rebuilds the routing facts used here.

In d=4, G_0 is own n^{-2}G_0^c, dy is O(n^{-2}η), and the point charge is at most 2d(d−1)n^{-4}η||G_0^c||. Routing cancels n^4 and gives **324** at L=3. The w_A coarse Hölder bound is 4(d−1)η(||G_0^c||+[G_0^c]_α); routing gives **1296/(3^α−1)**. The remainder is O(n^{-4}η²||G_0^c||), whose route costs k/n≤1/3. Thus the printed **443η** in c_G is a valid upward rounding of **442.8η=2214η/5**, not a refutation. Its 1.01 majorant is justified after the already required small η restriction; r≤1 alone would not justify 1.01. Campanato-to-pointwise conversion is the ordinary telescoping-box argument and its constant remains explicit.

For s, exact gauge covariance gives Dρ Kλ=[λ(head),ρ] (up to the chosen overall sign), hence

    r K′λ = [λ,ρ] + (Dρ−r)Ξλ − (Dρ−r)K′λ.

A fixed local analytic map on finitely many contour variables has ||Dρ−r||≤C_Ψ L^{-q}η, q=k−1−l. Inserting own s size L^{−(2+σ)q} and own ρ size L^{−(2+σ)q}(η+C_ρη²) yields, respectively, routed costs proportional to

    L^{−2σq}η,  (q+1)L^{−σq}η,  L^{−σq}η².

Their sums are 1/(1−L^{−2σ}), 1/(1−L^{−σ})², and 1/(1−L^{−σ}), finite for fixed σ>0. The fixed finite incidence count controls transposition; it has no k/T dependence. This supplies the s-slot completion without importing a false BCH factorization.

The plain-current coefficient is c_j=2d c_Bern L^{d−1}. At d=4,L=3,c_Bern≤59/100 it is **3186/25=127.44**, with strict smallness η<25/3186. For other L use the actual c_j(L), not that numerical threshold. Freeze the analytic radius and evaluate the η-dependent c_G/c_s bounds at its upper endpoint before choosing the final contraction radius; the file supplies no numerical value for C_Ψ or the final ε_L.

For exponential weights, every routed path and local contour lies within a bounded coarse distance of its originating slot, so a fixed weight costs a bounded exp(Cm). Hölder differences additionally use the bounded variation of the weight. Thus the weighted implication survives when the stated (H2)_m and (H3)_m are supplied. Neither weighted inverse input is proved by a2_55_conv.

Gate audit: the script's direct finite exp/log derivative and the coefficient formula are distinct calculations, and all six deliberate sign/coefficient/term controls fired on reproduction. The 6×6 strictly upper-triangular algebra can only check finitely many nested commutators; it cannot certify the entire analytic identity or any σ/norm estimate. The script explicitly disclaims those scopes. They are supplied above by the algebra and scale arguments, with their premises retained.

## F8 — HD in the full flat sharp-to-N pair can be banked in the log chart

Verdict: **CONFIRMED** for the log-chart estimate with fixed finite local constants and the specified small global background; **NOT-VERIFIED** for any covariant-output conversion inferred from it. Claim status: **CONDITIONAL** on the finite-word analytic residual/action and the stated background sizes. The local argument does not require a new inverse theorem.

Attachments: `ALIGN2_55.md:422-436`, `(HD)_log at all orders`, `(FW)_log`; `CODEX_REVIEW_KOFF.md:321-415`, `Independent local analytic completion` and equations (1)-(3).

A direct re-derivation avoids adopting a prior review's status. Put q=k−1−l and h=L^{−(q+1)}. Local background logs are O_L(hη); direction logs are O_L(h||u||_(σ)). Write the analytic residual as ρ=r+R. For spatially constant fine logs, the centered, order-averaged contour has no quadratic fine-field term: its signed areas are linear in centered offsets and average to zero. The remaining quadratic BCH term between the fine average and the independent next-level log is proportional to their mismatch r. A spatial oscillation gains h, and the cubic Taylor remainder gains h³. Polarizing gives

    |R|≤C h³η²,       |DR[u]|≤C h³η||u||_(σ),
    |ρ|≤C L^{−(2+σ)q}η + C h³η².

For clarity, the **operator** Dρ−r on arbitrary local arrays only has size O(hη); the improved DR[u] above uses the matched smooth/transport direction. Confusing these statements would lose a scale factor. Analyticity at a fixed polydisc, rather than a depth-dependent polydisc, controls the entire Taylor remainder.

Let Ψ=∇w(ρ)=ρ+O(ρ³), after fixing the action's quadratic normalization. The soft gradient splits exactly as κ r^TΨ + κ(DR)^TΨ. Subtracting its quadratic part gives a residual slot κ(Ψ−r) and plain rows κ(DR)^TΨ. Their derivatives in u have sizes

    residual: C L^{−(2+σ)q}η||u||_(σ),
    plain rows after π_l scaling: C′L^{−σq}η||u||_(σ).

The last estimate follows from hη·L^{−(2+σ)q}η, multiplied by h^{-3}; the Taylor remainder gives hη³ after that scaling and is bounded by a constant times L^{−σq}η² when σ≤1. Differentiating introduces one direction factor and leaves the same scale bounds. For Wilson, expand log plaquette=dy+O(y²), use its exact gradient split d^T∇w(F)+(Dq)^T∇w(F), and translate all local arguments together. This gives both the coarse G_0 Hölder bound and the plain P0 bound, of order η||u||_(σ), at all orders.

Now σ=θ. At output level i≥1, the rows from soft levels i and i−1 have combined weighted price at most

    C′(1+L^θ)L^{(θ−σ)(k−i)}η||u||_(σ)
      ≤ 2C′L^θ η||u||_(θ).

The residual N weight is L^θ times the R(θ) weight. There are no positive-level G rows in this explicit representation, but that is sufficient to **upper-bound** the full infimum N. This direction of infimum use is valid, unlike F3. Since ||u||_(θ)≤|||u|||_sharp, the claimed qualitative all-order HD bound follows. Enlarge the unspecified C to include the fine soft P0 row and the sum of Wilson components; no numerical C_HD is certified by the source.

For H itself, choose G_0=du_0 and s_l=κ_l r_l(u). Their cost is at most (2+κ_+L^θ)|||u|||_sharp, hence C_FW≤2+κ_+L^θ+C_HDη with these conventions. Background and data size must both lie in the fixed small analytic ball; the affine top residual controls the data by the top potential plus its mismatch, with an L-dependent constant absorbed here.

This genuinely removes the **log-chart** HD gap. It does not bound J^{-1} from the flat sharp norm into the covariant sharp norm, does not prove covariant N_res conversion, and does not establish (P2-tw)_log. CW's failure of the old chart and the new HD proof are compatible statements.

### F5 supplement — the periodic failure is unavoidable for one path per coarse node

Verdict: **REFUTED** for the constant-annihilation premise of the specified periodic spline LP, including arbitrary windings. Claim status: **PROVEN** counterexample. Attach also `ALIGN2_55.md:494-503`, `M_m and 1 − S_1Q_m both annihilate constant 1-forms` and `new identity, PROVEN-HERE`.

The issue is not merely my shortest-path choice. For L=3, nine coarse knots and y=1, exact cyclic collocation gives weights with common denominator 1377 and integer numerators

    (1102, 521, −126, 34, −10, 6, −14, 50, −186).

For a constant 1-form, any lattice path from coarse site 3j to fine site 1 has integral `1−3j+27n_j`, n_j an integer. The weighted detail is therefore

    M(1) = (3960 + 27 Σ_j a_j n_j)/1377,

where a_j are the integer numerators above. Since **3960≡18 mod 27**, it cannot vanish for any choice of paths. Indeed **|M(1)|≥1/153**. At retained nodes M(1)=0 because the path is empty, so dM(1) is nonzero somewhere. The same argument on three coarse knots gives `(30+9z)/27`, never zero, with |M(1)|≥1/9. Nine knots avoids any concern about the minimum torus size T≥5.

This embeds exactly in d=4 as in F5. Under the target's claimed harmonic reproduction `(I−S_1Q)1=0`, the identity `dM=I−S_1Q+Ñd` would give dM(1)=0, a contradiction. Thus its periodic spline use is not PROVEN algebra. If S_1 is chosen otherwise, its claimed constant-reproduction premise fails instead. Periodizing **unmerged lifted weights and their separate winding paths** can change the construction; it is not the one-path-per-periodic-node M specified in §2.4. No arbitrary enlargement of C_D or C_{S1} repairs this algebraic defect.

## F9 — Spline reconstruction and the 5-adic certificate, with precise scope

Verdict: **CONFIRMED** for spline reconstruction from assumed detail amplitudes and for the exact β=23/50 certificate; **REFUTED** for the superseded β=0.4676 numerical claim; **NOT-VERIFIED** for the printed multidimensional Hölder prefactor without a distance/norm convention. Claim status: **PROVEN** for the numerical certificate and the reconstruction estimate with the safe constants below; **GAP** for obtaining its assumed amplitudes from the specified periodic spline LP.

Attachments: `ALIGN2_55.md:511-549`, `Lemma HB (spline)`, `β ≥ 0.4676`, and its erratum; `checks/a2_55_beta.py` / `_criteria.md`; `CODEX_REVIEW_ALIGN.md`, locating `51447766041/30517578125`.

HB itself needs no unknown periodic wrap theorem once the amplitudes are supplied. Periodize the cardinal spline basis. The sum of absolute values of any periodized derivative basis is at most the corresponding full infinite-lattice sum, so the same Lebesgue bounds apply independently of the period. Nesting identifies every refinement iterate with samples of this interpolant. Hence, writing A_0=3^d, A_1=6·3^{d−1}, A_2=12·3^{d−1}, and using the componentwise maximum gradient norm and spatial ℓ∞ distance, safe bounds are

    ||λ_l||∞ ≤ A_0 M/(1−L^{−(2+α)}),
    ||∇λ_l||∞ ≤ A_1 M L^{2+α}/(L^{1+α}−1),
    [∇λ_l]_θ ≤ M L^{2+α}[d A_2/(1−L^{−α})
                                  +2 A_1/(1−L^{−1−α})],  0<θ≤1.

For the last line, split at a separation t: scales ρ_m≥t contribute at most d A_2 M L^{2+α} t Σρ_m^α; scales ρ_m<t contribute at most 2 A_1 M L^{2+α}Σρ_m^{1+α}. Divide by t^θ and use t≤1. Discrete gradients are averages of continuum derivatives. The dimension factor in the first term is the safe ℓ∞ line-segment bound from all mixed partials; the target's scalar-style first-term prefactor omits this accounting. I have not produced a counterexample to that potentially nonoptimal smaller constant, so I do not label its inequality false. Along a single coordinate axis its stated prefactor follows. This refinement reconstructs arbitrary periodic detail arrays under the assumed amplitude bounds, but F5 shows those bounds do not follow from the target's periodic M on constant inputs.

For L=5 I independently generated cubic Lagrange weights at all residues, divided the mask twice by σ_5(z)=1+z+...+z^4 by low-degree exact elimination, formed c=5a/σ_5², and convolved integer-scaled masks. The exact ℓ∞ iterate norms for n=1,...,5 are

    21/25, 249/625, 2541/15625, 24369/390625, 226821/9765625.

Thus ||S_c^5||²=51447766041/5^20, agreeing with the cited input by independent arithmetic. For β=23/50 the certificate is A^5<5^77, A=51447766041, which holds. For β=47/100 it would require A^10<5^153, which fails. The superseded β=0.4676=1169/2500 would require **A^250<5^3831**, which also fails. The safe certified value is **23/50=0.46**; the exact five-step certificate threshold is `(20−log_5 A)/10`.

The regularity mechanism is re-derived, not inferred from the decimal: divided first differences refine by b=La/σ_L, and their differences refine by c=La/σ_L². The strict five-step contraction makes successive derivative approximants Cauchy geometrically; affine reproduction bounds each change by a fixed local multiple of those differences. Splitting scales at the separation then gives C^{1,β} for β=23/50 (and smaller β). This supplies a regularity certificate, not the complete LP completion/source estimate. In particular it cannot justify θ=1 or every odd L for the 4-point DD scheme. The separate spline construction supplies smooth scalar reconstruction for every L; its periodic path moments are the distinct defect in F5.

The beta gate can fail (both the larger exponents do), but by itself it only compares an imported integer. Here that integer was independently rebuilt. The target's final erratum already corrects 0.4676; do not count that corrected historical error as a new uncorrected finding.

## F10 — Level-0 G bookkeeping is a real correction; the new completion formula has a periodic harmonic gap

Verdict: **CONFIRMED** for the correction to the level-0 weight and for the telescoping source identity when its operator factorization is valid. **REFUTED** for applying the asserted factorization to the periodic spline operator as defined. **NOT-VERIFIED** for the full (P2-tw)_log bound. Claim status: **CONDITIONAL** for the corrected representation estimate; **GAP** for the full periodic construction.

Attachments: `ALIGN2_55.md:491-506`, `Divergences — the representation that avoids Pc growth`; :607-609, G15; `ALIGN55.md:381`, `weighted cost`; `CODEX_REVIEW_ALIGN.md:145`, `G_l divergence`.

With the stipulated source definition ω_0=1, the earlier inequality L^{θk}|z_0^c||G_0^c|≤Cη||G||_Y is false uniformly in k. The absent factor is **L^{θk}**; it is not available from the level-0 norm. A positive-level plain-current representation of the completion pays, at level 1, **L^{θ(k−1)}**, which also cannot be absorbed by ω_0. The previous CODEX_REVIEW_ALIGN F7 line invoking a Y weight for G_l needed l≥1 explicitly. Its treatment did not resolve l=0. This is a valid correction to the earlier reviewer, not a reason to reject all of F7's positive-level sums.

Use distinct notation: q_m for the coarsened charge, and B_m for the block averaging map (the target calls both Q_m). Suppose a specific pair satisfies dM_m=I−S_{1,m}B_m+Ñ_m d and w_(m+1)=S_{1,m}^T w_m. Then

    c_m=−M_m^T d^T w_m
       =−w_m+B_m^T w_(m+1)−d^T Ñ_m^T w_m.

Pair with x and sum m≥l, using x_k=0. The result is exactly

    −<w_l,x_l> + Σ_m <w_(m+1),r_m(x)>
                 −Σ_m <Ñ_m^T w_m,dx_m>.

Thus the proposed representation has the correct signs and slots **provided that factorization exists for this operator**. Given |w_m|≤C_{S1}L^{3(m−l)}|w_l|, its residual cost is bounded by C_{S1}L^θπ_l(w_l) since the remaining depth factor is L^{−(1−θ)(k−1−m)}. Positive-level G′ costs are also compatible with a uniform bound if Ñ has the required quantitative local and Campanato estimates. At l=0 the one surviving plain current uses P0, avoiding the spurious positive-level Pc price.

But `vanishes on closed forms` does not by itself furnish a local factorization with controlled norm on a torus. F5 gives a stronger failure for the specified periodic spline M: it does not annihilate harmonic constants, so the asserted factorization fails algebraically under the target's own harmonic-reproduction premise. On a contractible finite stencil one can seek an explicit Stokes filling; on the torus one must also handle harmonic forms. Neither a normalized S_1 column count nor the Campanato bound for G′ is supplied by LP's gates. The target's phrase **“mechanisms ... complete”** in §2.5 and §6 is therefore too strong for its periodic spline instance.

## F11 — Symbol collisions, citation drift, and the remaining hypotheses

Verdicts: **REFUTED** for the stale literal PROOF locations and for using the known completion constant as if it were the chart constant; **NOT-VERIFIED** for the remaining analytic conversions. Claim status: **GAP** where these are needed by the full periodic R2 conclusion.

Attachments: `ALIGN2_55.md:60-61`, cited PROOF locations; :150 and :404, `C_CV`; :486 and :492, `Q_m`; :556-570, the R2-full-log input table; :720-721, remaining work.

Symbol audit:

- At :150, C_CV=max(c_j,C_CH c_G,c_s) controls **P_cc completion in N^(σ)**. At :404, the same C_CV labels **J^{−T}:N_Z→N**. Those are different maps, different norm pairs and different obligations. Rename them C_projection and C_chart; CONV-P supplies only the first. No numerical or existence result for the second follows by reusing its symbol.
- Q_m is a **charge vector** at :486 and :492's first clause, then an **averaging operator** in `I−S_1Q_m`. F10 separates the types before doing algebra.
- J/K chart direction errors are F4; the log generator mislabeled left-trivialized is F7. The mesh ρ_l and residual ρ_l(y) were kept separate as h and ρ in the derivations above. Λ_* is consistently root-vanishing; Λ_0 in older sources cannot be imported without its definition.
- The 127.44 threshold is only d=4,L=3; for general L use 2d(59/100)L^{d−1}. Background/data η, the frozen radius η_*, and output-dependent constants must not be substituted for one another. For CW, enlarging C_0 to cover C_Π requires shrinking the dependent smallness bound; no pre-existing numerical minimum is thereby certified.

Citation audit by locating strings: `PROOF.md:791` currently discusses Euclidean invariance, not `Balaban takes L sufficiently large`. The latter is at **:799**. The `Lemma H1 (one step from i.i.d. Haar)` heading is currently **:4031**, not :4023; :4023 is still in the preceding contour lemma. The quoted `range L ≥ 5 ... SU(2)` qualification is **:4045-4047**, outside the cited :4023-4040 interval. These particular anchors have moved by **+8**. This is not assumed to be a global offset elsewhere. No scientific result was inferred from the moved citation.

Remaining analytic boundaries:

1. (AC)_log: its displayed power count is compatible with uniformity, but a proof must include the exact polarized local remainder, the independent level-(l+1) variable, and the summed C^{1,α} residual norm. The new display starts with C p_L², so ending at L^{-2} is consistent; it does not inherit the old display's extra L^{-2}. The full lemma remains NOT-VERIFIED here.
2. (P2-tw)_log: finite range and the left inverse do not provide full N completion. The periodic harmonic defect in F5/F10 must be repaired before the claimed operator identity can support its norms. S_1 stability and G′ Campanato estimates remain needed.
3. (NC)_log and (CV)_log: the true dexp map fixes the constant-background mechanism, but the full covariant sharp norm includes transported derivatives and N_res. A local norm equivalence without the depth weights is insufficient. The source infimum also requires an estimate for every permitted representation before taking that infimum. These are NOT-VERIFIED.
4. Torus reconstruction HB can be banked from amplitude hypotheses by periodization (F9). **Obtaining those amplitudes and the completion identity from the periodic LP definition is the unresolved part**, with a concrete obstruction to the printed intermediate identities. For the compact s3 alternative, the target still needs its compatible finite-level C^{1,θ} reconstruction/completion bounds in the stated θ range.
5. Weighted L2 remains conditional on (H2)_m and (H3)_m. A bounded-distance path is compatible with exponential weights; it does not prove weighted RW♯ or weighted rows 6-11 of the GA theorem. The full weighted, covariant R2 is not banked.

Smallness cannot close an absent estimate or an algebraic contradiction. Freeze the local analytic radius and all valid operator constants first, cap their η-dependent majorants at that radius, then choose η small enough for c_jη<1, GK(2η+s)<1, C_𝒞C_ACη<1 and C_♯δ_Υ<1. The note's thirteen-row theorem is a valid conditional assembly after its map conventions are corrected; its proposed periodic spline instantiation has not met those hypotheses.

## F12 — What the four advertised refutations and the check suite actually decide

Verdicts: **CONFIRMED** for the narrower decisions below; **NOT-VERIFIED** for the unproved extensions. Claim status: **CONDITIONAL** for the full R2 implications.

- NC / G9: the old left-trivialized sharp comparison is obstructed asymptotically, with the slice premises and mesh correction in F6. The exact all-k CW coefficient is not banked.
- RED′ with HC / G10: its uniform t_+ cannot hold for the constant-annihilating map in that norm pair. RED′ remains correct as a conditional algebraic reduction; the obstruction is to satisfying its premises.
- Level-0 completion / G15: the old use of a positive-level Y weight at l=0 is wrong, as F10 derives. A full completion bound still needs the repaired periodic operator and its norm estimates.
- Exponentially local left inverse / G16: compact s3 LP supplies one, by the direct telescoping construction and finite path radius. This resolves the narrow existence question posed in ALIGN55. A historical “OPEN” status is superseded, not a false theorem. Existence of a left inverse alone does not close weighted R2 or all regularity/completion requirements for the same instance.

Captured reproductions, using plain Python Fractions/integers and no output-file writes: a2_55_nc N1/N2 and both controls reported PASS/FIRES; a2_55_conv I1/I2/II1/II2 and all six controls reported PASS/FIRES; a2_55_beta reported PASS/FIRES. a2_55_lp reproduced A1-A5/A1r, B1, C1-C3 and their listed controls, **B2 FAIL**, **OVERALL FAIL**; radii were **20/9**, **65/27**, both ≤3; the linear-interpolation control ratio was **1211/8073**. An earlier LP launch's completion output was not retained and is not used as a second receipt. No gate was changed.

Every gate was examined for scope: LP A1/A1r test telescoping with two path choices; A2 restriction; A3 upward independence (a perturbation of the top variable has only the fixed top level above it and is vacuous for unknown levels); A4 tests transpose locality at l=k−1, not every l; A5 tests two depths and one impulse, not a uniform theorem; B1 tests finitely many polynomial fields; B2 is structurally unsatisfiable; CB3 is not a valid rate control for it; C1 compares independently formed refinement matrices at three (L,M) pairs; C2 checks sampled interpolation/constants; C3 checks only M=1,...,8. Their universal algebraic counterparts were proved above where banked. N2/CN2's endpoint identity and dependence are detailed in F6; conv's finite nilpotency limitation is F7; beta's imported-number limitation was removed by the independent mask calculation in F9. The proofs, rather than a collection of PASS labels, determine the banking list.

## Summary table

| Finding | Review verdict | What survives / what fails |
|---|---|---|
| F1 N1-L | CONFIRMED | Slice injectivity plus connected root-pinned gauge action gives exact Hessian kernel; no separate FP premise. CONDITIONAL on L1 inputs. |
| F2 LP / B2 | CONFIRMED algebra; REFUTED quadratic nonzero/rate gate | Polynomial degree≤2 detail is 0. B2 ratio is undefined; a nonzero cubic witness has ratio 1/81. |
| F3 source infimum | REFUTED inference; NOT-VERIFIED full bound | Restricted representation cost cannot be replaced by the smaller unrestricted N(f). |
| F4 charts / RED″ | REFUTED parenthetical maps; CONFIRMED corrected algebra | S=J^T f and Ξ_Z=−J^{-1}K. The four-term defect and matched-input reduction are sound. |
| F5 periodic spline LP | REFUTED moment cancellation and its completion-factorization premise | On nine knots, any one-path-per-node choice has |M(1)|≥1/153; shortest paths already give 40/99 on five knots. |
| F6 CW | CONFIRMED leading/asymptotic obstruction; REFUTED claimed telescoping; NOT-VERIFIED exact all-k coefficient | Retain a spatial O(ρ_0) error in addition to O(η). Old norm pair remains obstructed under the stated slice inputs. |
| F7 CONV-P | CONFIRMED in σ representation norm | Exact generator split and G_0/s/j routing estimates survive. No chart conversion or unrestricted N transfer. |
| F8 HD_log / FW_log | CONFIRMED with matched local inputs | Full flat sharp→N bound follows from an explicit all-order local representation and scale calculation. |
| F9 HB / subdivision | CONFIRMED safe reconstruction and β=23/50; NOT-VERIFIED smaller multidimensional prefactor | Periodic HB follows from supplied amplitudes; the periodic LP does not supply the claimed seminorm-only amplitudes. 0.4676 was already corrected by the author. |
| F10 G_0 / P2 | CONFIRMED level-0 correction; REFUTED periodic spline factorization; NOT-VERIFIED full P2 | ω_0=1. Conditional telescoping slots have the correct signs, but harmonic and quantitative source estimates remain. |
| F11 symbols / citations / outputs | REFUTED stale locations; NOT-VERIFIED remaining conversions | C_projection≠C_chart, charge q_m≠averaging map B_m. PROOF anchors moved to 799, 4031, 4045-4047. |
| F12 four claims / gates | CONFIRMED narrow decisions; NOT-VERIFIED full extensions | A finite-range exact left inverse exists; neither it nor the recorded PASSes establishes full periodic/weighted R2. |

**Single most dangerous unverified item:** **(P2-tw)_log in the full N pair on the periodic lattice.** For the proposed spline instance its claimed supporting identity already fails on harmonic constant fields; for the compact s3 alternative, the required matched reconstruction/completion estimates are still not supplied. This is a concrete obstacle to instantiating the full theorem. Output chart conversions are separate additional gaps.

## Exactly what may be banked

1. **CONDITIONAL:** L1/L2 on the small global log-chart slice, using the stated uniform linear inverse and nonlinear bounds; N1-L removes the separate Faddeev–Popov-transversality premise. CONV-P supplies G_0, s and j completion in the σ representation norm. At σ=θ, use a specified restricted representation cost or N_restricted, **not the unrestricted infimum N**. Weighted versions require (H2)_m and (H3)_m. This does not include N_res or the covariant output theorem.
2. **PROVEN algebra / CONDITIONAL estimates:** corrected RED″ with J:left→log, Υ=J^{-1}(I+K′Λ), S=J^T f, and the four correctly charged defect terms. The GA conclusion remains an implication from its full, valid, uniform hypotheses.
3. **CONDITIONAL local estimate:** all-order HD_log and FW_log in the full **flat sharp→N** pair for fixed N,L and 0<α<θ≤1, within the stated small analytic background/data class. The representation and scale proof is F8; no covariant-output conclusion is included.
4. **PROVEN:** compact-path LP's left inverse, root restriction, hierarchy, transpose level locality, finite range, polynomial cancellation and Taylor detail estimate for coherent local lifts. These resolve the narrow existence of a local exact hierarchical left inverse. The infinite-lattice spline version has exponential moments and the same Taylor argument.
5. **PROVEN:** periodic cubic-spline scalar subdivision is interpolatory and nests for every integer L≥2; its one-dimensional Lebesgue bounds are 3,6,12. HB reconstruction holds uniformly on infinite and periodic lattices **given** its detail amplitudes, with the safe norm-specific constants in F9. Infinite-lattice spline P1′ follows. Do **not** bank periodic spline LP-2 or its printed completion factorization; F5 refutes their constant-field premise for the operator as defined.
6. **PROVEN:** the independently rebuilt five-step 5-adic norm is 226821/9765625, yielding the C^{1,23/50} certificate. It does not give β=0.4676, β=0.47, θ=1/2, or a full L=5 alignment theorem.
7. **PROVEN at the constant representative / CONDITIONAL at the BFT slice:** CW's leading chart-mismatch mechanism and the asymptotic obstruction to the old sharp norm comparison and constant-annihilating HC/LP alignment. The slice transfer uses the regular projection/uniqueness premises and a mesh error; do **not** bank the printed all-k coefficient or a no-go theorem for every alternative alignment.

Nothing here banks the full periodic R2-full-log conclusion, (AC)_log, the full periodic (P2-tw)_log, the covariant output conversions, or a constructive four-dimensional Yang–Mills theorem. The target's remaining-work list must include the actual periodic harmonic/path repair and the source-infimum restriction, not just constants and wrap bookkeeping.

Closing UTC: 2026-10-29T05:58:43+00:00
