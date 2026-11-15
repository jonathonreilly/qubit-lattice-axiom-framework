## PRE-STATED — 2026-10-29 04:14:27 UTC

Independent hostile review of `LCONV55.md` by Codex.

Written before examining the target's mathematics or check implementations. Primary target: `LCONV55.md`, including errata LE1–LE5 and disclosures. Named supporting targets: the `lc55_1`, `lc55_2`, `lc55_3`, `lc55_4`, and `lc55_4b` checks; relevant ranges of `NODEA_RES55.md`, `CODEX_REVIEW_NRES.md`, and `PROOF.md`. Repository instructions and the applicable review procedure will be consulted within the additional-file limit. No git, snapshots, audit ledgers, numerical linear algebra, or other output files.

Refutation criteria, registered before derivation:

1. **Region membership:** the stripe field must satisfy the actual defect-free event at every required level, with the stated boundary conditions and strict inequalities. A nonidentity blocked link, omitted constraint, or incompatible boundary invalidates the claimed instance.
2. **Curvature:** reconstruct the Wilson second variation and the claimed gauge-orthogonality. A negative ambient direction does not establish negative quotient curvature unless the appropriate slice/metric and connection terms are controlled.
3. **Quantifiers:** distinguish a certified example, a family approaching zero field, all admissible thresholds, all volumes, and all couplings. Dependence of support size or constants on the field/threshold must remain explicit.
4. **Chain lift:** independently test Lemma FOL, including the acceleration of a following path and the Hessian's metric/chart dependence. Vanishing kernel energy along a path alone need not imply vanishing Hessian curvature.
5. **Decisiveness:** every accepted gate needs an independent obstruction it can detect. Inspect the corrected horizontality control and avoid treating a tautological or structurally disabled control as evidence.
6. **Positive reformulation:** determine the strongest existential negative-curvature statement actually established, and whether the chain metric or chart used by node A can evade it. Test the proposed convexity/Peierls window comparison with its constants and quantifiers intact.
7. **Replacement route and retractions:** distinguish proven obstructions from argued repairs, and verify precisely what can be withdrawn from nr-15, nr-19, §7 item 4, and (LC-1′).

Statuses: review findings use **CONFIRMED / NOT-VERIFIED / REFUTED**; mathematical claims use **PROVEN / ARGUED / CONDITIONAL / GAP / OPEN**. A check's recorded PASS is not independent verification. Exact rational/symbolic arithmetic only. Citations will use current located strings and verified line numbers where available.

## Findings (incremental)

The findings below were appended as they were derived. Final dispositions and bankable results appear at the end.

### R1 — REFUTED inference: the chart-restricted examples do not refute (LC-1′) as stated

**Locations:** `LCONV55.md:283`, locating string `In any gauge-fixed chart obtained by fixing the level-0 gauge`; `LCONV55.md:296`, `The **joint**-quotient version`; `LCONV55.md:305`, `(LC-1′) as stated`; `LCONV55.md:536`, **LE5**. Comparator: `NODEA_RES55.md:279–282`, `there is a conjugation-equivariant gauge-fixed chart`, and `:317–320`, `(LC-1′)`.

The target itself correctly limits its normal-chart theorem and concedes that the joint chain metric is only ARGUED. LE5 further requires coordinates normal **at the stripe**, because it is not a critical point. The comparator asks for convexity **in a gauge-fixed chart**, with additional domination properties; it does not quantify over all point-centred normal charts. Failure in the displayed charts cannot negate that existential requirement. In local coordinates, for a change `x = y + (1/2)b(y,y)` with derivative the identity at the point,

`D²(S∘x)[v,v] = D²S[v,v] + dS[b(v,v)]`.

If `dS ≠ 0`, choosing `b(v,v)` along the gradient changes this second derivative with either sign. This does **not** construct a globally usable convex chart satisfying the column-action and support conditions; it proves that the claimed refutation needs an additional obstruction. The correct status of the unrestricted (LC-1′) conclusion remains **OPEN / NOT-VERIFIED**, even if the restricted negative-curvature examples survive. The same qualification applies to the blanket retractions of nr-19, the multiscale half of nr-15, and §7 item 4; those prior arguments remain unsupported, not rehabilitated.

**Most dangerous open bridge so far:** the following direction must be an admissible tangent for the actual conditional chain, and its curvature must be computed in the chart/metric the consumer uses. Bare level-0 horizontality alone does not establish this.

### R2 — CONFIRMED: the collared bare-action family, by a simpler independent derivation

**Locations:** `LCONV55.md:249–274`, `A uniform family down to every threshold`; `checks/lc55_4b_cyl_family_ctrl.py:368–384`, `N=cyl_Nhat` and `cstar=`. Mathematical status: **PROVEN for the stated bare Wilson action and cylinder boundary conditions**.

The certificate simplifies considerably. Put `s = 1+τ²`. Remove the common factor `−3s²` from its vector. The resulting vector is

- `w₁(x)=(1,1,1)` for all nine longitudinal links;
- `w₂(x)=(4τ,−4τ,0)` at `x=1,4,7`, and zero at other sites;
- boundary `w₂(0)=w₂(9)=0`.

This is horizontal **identically**, not just at three sample values: `w₁(x)−w₁(x−1)=0`, and every nonzero `w₂` is on a site where `G(x)=1`, so `(Ad_G−1)w₂=0`. Summation by parts against the gauge generator gives precisely this divergence condition, with the gauge parameter zero at the collar.

Here is a separate local action calculation. Write `A=i(σ₁+σ₂+σ₃)`, `B=4iτ(σ₁−σ₂)`, `G=exp(iβσ₃)`. In each three-plaquette cell, the three products along the geodesic variation are

`e^(tA)e^(tB)e^(−tA)G^−1`,
`e^(tA)G^−1e^(−tA)e^(−tB)`,
`e^(tA)Ge^(−tA)G`.

Using `[i a·σ,i b·σ]=−2i(a×b)·σ`, their contributions to `d²(1−tr/2)/dt²` are respectively

`−32τ²`, `−32τ²`, `−32τ²/s²`.

There are three cells. Thus, exactly,

`H = −96τ²(2+s^−2)`, `|w|²=27+96τ²`,

`RQ_cyl = −96τ²(2+s^−2)/(27+96τ²) < 0`.

This derivation uses no perturbative remainder, eigenvalue search, or numerical proposal. Restoring the certificate's common factor gives

`N(τ)=−864τ² s⁴(3+4τ²+2τ⁴)`,
`D(τ)=9s⁴(27+96τ²)`.

An exact plain-Python coefficient comparison with the selected source calculation agrees. Rebuilding its conservative tail bound gives `tail=2209198201227/15625000000`, `D_max=654643982691/2500000000`, and exactly

`c_* = 2269084551038400/247334195090033`.

No correction to this constant is needed. In fact the explicit quotient gives the stronger uniform coefficient `24321600/2376833` on `0<τ≤1/10`: its positive magnitude divided by `τ²` decreases with τ, so its minimum is at `1/10`.

For the transverse lift, mixed plaquettes reduce to differences of the same Lie-algebra direction on adjacent slices. Their quadratic cost is exactly `|w|²(Δf)²`; divergence acquires no transverse term since `v₃=v₄=0`. Summing gives `RQ_4D=RQ_cyl+2S₁/S₀`. With `m=n_⊥`, direct finite-sum identities give

`S₀=(m+1)((m+1)⁴−1)/30`, `S₁=m(m+1)(m+2)/3`,
`2S₁/S₀=20/((m+1)²+1)`.

Consequently the source's ceiling formula proves `RQ_4D≤−c_*τ²/2`. Exact integer-square-root evaluation independently reproduces `m=21,105,2089` at `τ=1/10,1/50,1/1000`, and

`m(10^−44)=208807809798820024202515358359085930383355647`.

This confirms LE2's correction of the old `0.7/τ` estimate to `sqrt(40/c_*)/τ` (about `2.09/τ`). It establishes a genuine family at arbitrarily small fields on this cylinder, not a fully boxed family at arbitrarily small fields, and not yet a conditional-chain counterexample.

### R3 — CONFIRMED correction, but non-discriminating curvature controls remain

**Locations:** `LCONV55.md:264–268`, `Control disclosure`; `checks/lc55_4b_cyl_family_ctrl.py:424–444`, `RESULTS['ctrl4']` and `corrected controls`; `checks/lc55_2_certify.py:338–347`, `C2a` and `C2b`.

The old perturbation at `w₂(4)` is horizontal because `G(4)=1`; its inability to fire is correctly disclosed. The replacement perturbations really do fire: adding `e₁/7` to `w₁(4)` gives residuals `+e₁/7` and `−e₁/7` at sites 4 and 5. Adding `e₁/7` to `w₂(3)` at `τ=1/10` gives residual `(-800/71407,−3960/71407,0)` at site 3. These were recomputed exactly.

However, C4a is a flat holonomy at τ=0, and C4b is a neutral flat holonomy. Both have Hessian **exactly zero**, so both would also accept a globally sign-reversed Hessian implementation. The torus neutral projection in the displayed certificate has zero components. Those checks are not independent positive-curvature calibration. A useful nonzero horizontal neutral control is `w₂(1)=e₃`, all other components zero: its Hessian is `2cosβ=2(1−τ²)/(1+τ²)`, hence `198/101` at `τ=1/10`, and `2` at τ=0. This follows directly from the two affected plaquettes.

The corrected-control script also leaves `RESULTS['ctrl4']` attached to the old failed control and never adds `fired1 and fired2` to that result map. Its actual summary still says **ctrl4 FAIL**. The corrected residual evidence is valid, but describing its machine summary as an all-controls PASS would be false. No script was modified here.

### R4 — CONFIRMED algebraic blocking; complete defect-event membership NOT-VERIFIED

**Locations:** `LCONV55.md:162–182`, `Stripe S(P, β)` and `Membership`; `checks/lc55_1_region.py:43–69`, `transporter` and `center`; `PROOF.md`, locating strings `S4 Averaging (L1)` and `S4' [S3] Order-averaged averaging`.

For `P|L` and the centred stripe, all factors commute. Opposite axial spokes cancel. A direction-2 transporter is exactly `exp(i L a(y₁)σ₃)`; a transporter in any other direction is identity. Counting the two nonzero sites in each period gives

`M̄₂ = r I`, `r=(P−2+2cos(Lβ))/P`; `M̄_μ=I` for `μ≠2`.

The centre lies at a zero of the stripe (also when `P|L`, since `L/P` is odd), so every straight centre transporter is identity. For sufficiently small β, `r>0`, hence every following coarse link is identity. Induction makes all subsequent fields identity. At `L=P=3`, `τ=1/10`, `cosβ=99/101` and `cos3β=851499/1030301`, reproducing exactly `r=2733299/3090903`. A nonsymmetric pattern `(β,0,0)` instead has imaginary mean `sin(3β)/3=580060/3090903`, so C1a is a real falsifier of the scalar-centre assertion. C1b also has an analytic check: for its period-two field at L=3, the two direction-2 means are `(2+G³)/3` and `(1+2G³)/3`, while direction-1 means are the same positive scalar. Their relative product has imaginary part `sin(3β)/3≠0`. Thus every one of the 16 coarse (1,2) plaquettes is nontrivial on the side-two coarse torus, as reported. G1(a), by contrast, is automatic for this abelian input family; it is not an independent test of nonabelian transport.

The fine operator-norm maximum for P=3 is exactly `2sinβ=4τ/(1+τ²)`; for P=5 the source's bound remains a valid upper bound. The logarithmic S4′ map also gives identity when its principal-log domain holds: the two phases cancel before exponentiating. This must be distinguished from merely having zero net block flux, which alone would not prove a scalar arithmetic mean in a nonabelian configuration.

The script G1 tests these algebraic facts, not the lane's full defect-free predicate: it has no `η_q`, `ε_loc`, collar rule, history constraint, or boundary-membership test. The precise RLARGE/HIST definitions are not among the supporting files read under this review's file budget. Thus the implication to the **actual complete event** is **CONDITIONAL** on those being exactly the stated local plaquette/mismatch constraints. The selected PROOF ranges confirm the transporter convention, not the defect-event definition. Small β also has to lie in the local domain of the chosen blocking/normalizer chart; this can be enforced by choosing β still smaller for fixed L.

### R5 — CONFIRMED torus coefficients; LE3 repaired by full polynomial identities

**Locations:** `LCONV55.md:184–202`, `G2a`; `checks/lc55_2_certify.py:138–184`, `poly_basis`; `:252–347`, `G2a`; `LCONV55.md:439–444`, **LE3**.

I extracted the displayed polynomial vectors without running either floating proposal generator, then independently recomputed the reduced plaquette Hessian using planar Pauli trace identities. For `A=i a·σ`, `B=i b·σ` with planar vectors and diagonal `G_θ`, the key identity is

`(1/2)tr(A G_q B G_p^−1) = −Re(conj(a₁+i a₂)(b₁+i b₂)e^−i(q+p))`.

Applying the product rule to `e^(tA)G_q e^(tB)e^(−tA)e^(−tC)G_p^−1`, with all polynomial coefficients rational, reproduces the entire numerator, norm, and the divergence residual as polynomial identities. The nonzero numerator coefficients, in orders `τ²,τ⁴,…,τ¹⁴`, are

- P=3: `−704, −7552, −27328, −37632, −20032, −2944, −64`;
- P=5 and P=7: `−640, −3840, −8064, −7680, −3456, −768, −128`.

Every coefficient is negative, so the tail estimate is unnecessary for these explicit vectors. The denominators at τ=0 are `24,40,56`; the leading quotients are exactly `−88/3,−16,−80/7` times τ², or `−22/3,−4,−20/7` times β². The claimed `approximately −7.33β²` for P=3 is sound. These are exhibited quotients, not exact lowest eigenvalues.

The source's three-point test cannot prove a polynomial identity of its stated degree; LE3 correctly withdraws that inference. The recursion and inverse-rotation relation do give exact horizontality, and the independent polynomial residual calculation verifies it for the certified vectors. On the free-gauge-action cylinder, horizontal restriction equals the quotient Hessian by differentiating an invariant action along a horizontally lifted quotient geodesic; any vertical acceleration pairs to zero with the gradient. On the torus, the reducible stripe has a stabilizer, so “quotient Hessian” needs the corresponding singular-stratum/slice interpretation. The ambient horizontal quadratic forms themselves are unambiguous.

### R6 — NOT-VERIFIED: following directions in the conditional multiscale region

**Locations:** `LCONV55.md:95–116`, **Lemma FOL** and its `Reading`; `:281–298`, **Theorem NC (i)–(iii)**; comparator `NODEA_RES55.md:317–324`, `boundary datum on a fixed collar` and `Disintegrating … the fields there`.

**FOL(i) is CONFIRMED / PROVEN.** For each smooth kernel cost `g≥0` vanishing on the following graph, `dg=0` there. A curve inside the graph gives `Hess g[v,v]=0` for graph tangents; therefore every curve with that initial tangent has zero second derivative of g. This handles the acceleration term correctly. FOL(ii), as an identity of second derivatives along the specified curve, follows.

The missing implication is admissibility for the conditional chain. FOL requires `v_(m+1)=DB_m v_m` at **every** affected coarse link. The source's C4 certificate imposes only fine-link collar conditions; its tests contain no blocked variation, no coarse collar, and no frozen terminal-field constraint. A width-nine fine slab does not itself supply free coarse links at every scale. Following variations can cross its collar or move a conditioned coarse field.

This is consequential, not a cosmetic missing test. At a scalar SU(2) centre `M=rW`, with coarse V fixed at W while W moves with right velocity b, expansion gives

`φ_M(V)=r|b|²t²/2+O(t³)`, hence `Hess(κu φ)[v,v]=κu r|b|²`.

The purportedly zero kernel curvature is then positive and has the **same coupling order** as the bare curvature. At τ=0 the C4 vector transports a nonzero constant holonomy across the slab; it is precisely a direction that blocking can see. The conditional-boundary compatibility must be constructed, not inferred from point membership or fine horizontality. The joint-metric adjustment is separately acknowledged as only ARGUED in the target.

**Normalizers:** “u-free” cannot mean exact independence from u: `𝒩(r)=∫exp[−κur(1−cosθ)]dV` depends on u. A bounded large-u curvature remainder is plausible and can be justified locally: with `z=1−cosθ`, Haar density is proportional to `sqrt(z(2−z)) dz`, yielding `𝒩(r)=C(κur)^−3/2(1+O((κur)^−1))` and differentiated local expansions for `r` bounded away from zero. Thus a fixed finite tower in a fixed smooth chart has an O(1) remainder. This does **not** establish the stated `C_𝒩,C_D` as functions only of `N,L,κ`, uniformly in depth, region and gauge-chart geometry. Those stronger uniform claims remain **NOT-VERIFIED**.

**Additional problem with the ARGUED joint-metric estimate:** `LCONV55.md:296–298` infers a small gauge correction from coarse divergence `O(τ/K)` on an expanding region. Small divergence does not by itself bound the orthogonal projection by the same order: the inverse gauge Laplacian enters. If `D*D λ=ρ λ` and `w=Dλ/||Dλ||`, then `||D*w||=sqrt(ρ)` while the vertical projection of w is w, of norm one. On longer boxes, `ρ` can tend to zero. The required inverse/elliptic estimate is absent. Also the K in `n_⊥=K/τ` is a new envelope-size multiplier, not automatically the UV cutoff K used elsewhere.

**A limited periodic repair is possible:** for the C2 torus vector, both the background and its tangent repeat with period P in x₁ and are constant in the other coordinates. When `P|L`, translation covariance makes the first blocked tangent constant on the coarse lattice; subsequent flat-background blocked tangents are constant as well. Hence their coarse divergences vanish exactly. For a metric that is a sum of constant scalar weights times the product link metrics, each level's gauge inner product vanishes separately, so this periodic following vector is jointly horizontal. This avoids the envelope projection problem **on that periodic free tower**. It does not identify the lane's actual metric, construct C4's conditional collar, or eliminate the chart quantifier in R1. No general joint-metric theorem is banked.

A bankable conditional lift is narrower: **if** a finite following tower and its direction are admissible for the boundary condition, the fine chart has the certified normal second variation, and the normalizer/gauge-density Hessian stays bounded as the couplings grow, **then** sufficiently large `u₀` preserves the negative direction. It is not an unconditional certificate of the actual conditional chain.

### R7 — CONFIRMED finite box and exponential certificates; a separate first-order construction

**Locations:** `LCONV55.md:207–212`, `G2c`; `:226–247`, `In the exponential/axial coordinates`; `checks/lc55_2_certify.py:464–562`, `G2c`; `checks/lc55_3_certify.py:33–153`, `series_enclosure`, `link_series_p1`, `link_series_p2`, and `G3 overall`.

For the fully bounded box at `τ=1/10`, I reran the exact horizontal projection and independently evaluated the plaquette Hessian by transporting all four insertions to a common frame. If the background plaquette is `exp(iΘσ₃)` and the transported right velocities are `z₁,…,z₄`, the independent formula is

`H_p = cosΘ |Σ_i z_i|² − 2sinΘ Σ_(i<j)(z_i×z_j)₃`.

It agrees exactly with the source's Hessian. A separately assembled divergence is exactly zero. The lifted quotient is in

`[−133704973854/10^12, −133704973853/10^12]`.

The same projected vector has strictly positive free-field Hessian, a meaningful control. This confirms the finite fully bounded example; it does not extend that exact projected family to arbitrarily small τ.

For the exponential examples, I checked the Taylor formulas and remainder logic and reran the two rational-interval calculations with all floating formatting removed. Both certificates are negative; their conservative lifted upper bounds are below `−385367013554/10^12` and `−66031694203/10^12`, respectively. The source's displayed `−0.3854` is not a conservative rounding of the first **lift upper bound**. However, it is recoverable: using the exact transverse derivative norm, `|dexp_(βe₃)w|²=w₃²+(sinβ/β)²(w₁²+w₂²)`, the actual lifted quotient is below `−385859565133/10^12` (and below `−66042594024/10^12` for β=1/20). Thus I do **not** refute the final negativity or the `−0.3854` action bound; the stronger transverse computation supplies its missing rounding margin. These remain bare-action statements.

Two finite values do not prove a first-order asymptotic. The following independent construction does. On the six-by-six plaquette square let a gauge parameter be `λ(3,2)=e₁`, `λ(3,3)=e₂`, zero elsewhere, and use the fixed coordinate direction `v_(xy)=λ(x)−λ(y)`. It vanishes on fixed boundary links and has `|v|²=8`. At β=0 it is an infinitesimal gauge direction, so `H_0[v,v]=0`. The stripe's neutral action gradient on the direction-2 link at `(3,2)` is `sinβ+sin2β=3β+O(β³)`. The logarithm of the gauge orbit has acceleration `2λ(x)×λ(y)` at β=0, nonzero on only that link. Gauge invariance gives

`H_β[v,v]=−6β+O(β²)`, hence `RQ_2D=−(3/4)β+O(β²)`.

Equivalently, expansion of the four exponential factors through the exact `βt²` coefficient gives zero constant Hessian coefficient and coefficient `−6`; I checked this with plain rational polynomial arithmetic. The possible β-dependence of the orbit tangent contributes no linear correction, since the free Hessian annihilates `v`.

Analyticity on this fixed finite square therefore gives `RQ_2D≤−3β/8` for all sufficiently small positive β. A transverse envelope with `m≥ceil(sqrt(320/(3β)))` contributes at most `3β/16`, leaving `RQ_4D≤−3β/16`. This proves an arbitrarily-small-field first-order obstruction in the displayed exponential coordinate directions, subject to embedding those directions in the claimed axial chart. It does not settle the conditional-chain coarse-boundary problem in R6 or rule out other charts.

**Missing recorded control:** `lc55_3_criteria.md`, `C3b`, promises a Riemannian-chart evaluation of the same proposal. Neither the inspected certifier nor its output records that control. C3a is present and has strictly positive values. The absence of C3b does not invalidate G3's interval negativity, but the full pre-stated comparison was not completed.

### R8 — REFUTED quantifier promotions and coefficient transfer; windows NOT-VERIFIED

**Locations:** `LCONV55.md:261`, `τ = 10⁻⁴⁴`; `:329`, `every UV cutoff`; `:339–343`, `u_0β²`; `:403–410`, **G1**; `:496`, `below every ε_1 the lane can pick`.

1. **A fixed `10^−44` is not below every admissible positive threshold.** An upper ceiling `ε₁≤6.7·10^−40` supplies no lower bound. For example `ε₁=10^−50` is smaller than that displayed τ, and the fine plaquette norm is larger still. Correct choice for the inequalities actually quoted is `0<τ<min(1/10,η_q/4,ε_loc/8)`, with any additional blocking-domain smallness imposed too. The symbolic family reaches every positive threshold; the one displayed numerical instance does not.
2. **Fixed thresholds before the coupling justify an existence argument, not “every admissible field is far above the fluctuation scale.”** First fix a nonzero τ below the thresholds, then take `u₀` large enough. If τ is instead allowed to vary with u₀, the admissible choice `τ=1/u₀` gives `u₀τ²=1/u₀→0`. Likewise `β=g₀`, `u₀=1/g₀²` gives exactly `u₀β²=1`, not an arbitrarily large number. The required dominance has to be verified for the chosen witness.
3. **G1 transfers the β² coefficient to a different threshold variable.** Its `t₀` is a plaquette-norm cut, with `t₀≈2β≈4τ`, not β. The P=3 torus coefficient is therefore `RQ≈−(11/6)t₀²`, not `−(22/3)t₀²`; the conversion divides by **four**. The C4 certified 4D bound has leading coefficient `−(c_*/32)t₀²`, rather than `−(c_*/8)t₀²` in β² units. Thus the claimed `c≈2–7` against the plaquette cut is not the coefficient certified by C2–C4. This does not change the order of the deficit.
4. **“Windows do not overlap” is not an exact consequence of order notation.** A necessary bound `u t²≤C_conv` and a rarity requirement `u t²≥C_P` can only be compared after both constants, the desired rarity, and the same metric/chart are specified. Neither the constants nor the boundary/chart bridge are established here. Fixed positive thresholds and `u→∞` do produce the source's conditional asymptotic tension; this is much narrower than excluding every possible modified region or threshold-dependent construction. Negative `Hess V` alone also is not a negative `Hess V+Ric` calculation; LE4's qualification matters.
5. **“Every K≥K₀, every T, every column k” is not certified.** The checks exhibit geometries and vectors; they do not assemble admissible conditional towers and column data at every k. An existential counterexample would suffice for a uniform-convexity refutation. The stronger universal sentence is an unsupported promotion, not extra evidence.

### R9 — REFUTED exact tilt identification; proposed replacement remains OPEN

**Locations:** `LCONV55.md:392–396`, **F3**, `by DOM′ the tilt … is a local lowering of the coupling`; `:411–428`, **G2–G3**; comparator `NODEA_RES55.md:146`, `the minimised column action`, and `:336`, `pointwise Z_A ≤ e^{λ_f𝔞}`.

There are two distinct objects: the minimized column observable `𝔞^col_A` and the unminimized terms of the chain action. A domination inequality does not identify tilting by the former with changing coefficients in the latter.

Even for the easier case of tilting a literal kernel energy, normalization leaves an additional factor. Write `a=κu` and `k_a(V|M)=exp(−aφ_M(V))/𝒩_a(M)`. Exactly,

`exp(λaφ_M(V)) k_a(V|M)
 = [𝒩_((1−λ)a)(M)/𝒩_a(M)] k_((1−λ)a)(V|M)`.

The bracket depends on M. For `M=rI` in SU(2), `𝒩_a(r)=E_Haar[exp(−ar(1−cosθ))]`. Its small-r expansion is `1−ar+O(r²)`, so the ratio is `1+λar+O(r²)`, not a constant. Analyticity rules out its being identically constant on a small-field interval near r=1 either. Those factors can potentially be controlled as additional interactions, but they have not disappeared. With the actual minimized observable, an additional comparison is required before even reaching this formula. Thus F3's **exact identification is REFUTED**; its intended comparison/cluster-expansion strategy is **ARGUED / NOT-VERIFIED**.

G2 is labelled ARGUED in its heading and table, but its sentence “one-step conditional convexity holds” promotes that status. Incoming kernel positivity near a fixed centre is only one term; outgoing kernels, the actual coordinates, normalizers, boundary data, and uniform coupling ratios still need Hessian bounds. Two-sided bounds on a function's values by quadratic forms do not themselves imply a Hessian lower bound. No one-step theorem with the required quantifiers is proved here.

Similarly F4's assertion that the Peierls input is necessary “for every route” does not follow from Proposition NU's sufficient implication. A direct bound on the specified tilted moment could use other information. The proposed inhomogeneous-coupling cluster expansion is a reasonable **OPEN research route**, not a replacement theorem supplied by this file. Nothing here refutes BL-TILT under its hypotheses or the possibility of proving (LCR°).

### R10 — Symbol, status, and citation audit

| Symbol or statement | Located meaning | Review consequence |
|---|---|---|
| `κ` | `LCONV55.md:84`: RG-kernel stiffness; `:258`: `|n₂|−tail` in the polynomial certificate | Two different objects. The latter is `2450.611315121472` exactly as a terminating rational decimal, not the RG stiffness. I used separate names throughout; no comparison between them is valid. |
| `N` | `:84–85`: SU(N) colour number; `:198`, `:257`: polynomial numerator `N(τ)`; `:260`: envelope length `n_⊥+1` | Three different objects. The certificates here use colour number 2, while their polynomial and envelope N vary. |
| `τ` | `:92–95`: vector tangent to the following set; `:165` onward: scalar `tan(β/2)` | Distinct types. The scalar controls the field and the transverse size; the full following tangent is not certified by a scalar test. |
| `β` and `t₀` | `:165`: link-angle amplitude; `:404`: plaquette-norm threshold | The factor-of-four coefficient error in R8 comes from treating their squares alike. |
| `ε₁`, `η_q`, `ε_loc` | `:180–181`, `:278–281`: positive thresholds imported from RLARGE/HIST/SMALLNESS_DAG | Their quoted relationships are not independently sourced within the two-extra-file budget. An upper ceiling is not a fixed value or lower bound. Comparisons to the illustrative `10^−44` cannot be promoted. |
| `c_*` | `:258`: `2269084551038400/247334195090033` | Recomputed exactly, with the same meaning throughout C4/C5. |
| `C_𝒩`, `C_D` | `:109–112`: bounds on density corrections and the complete iterated blocking tangent | Output bounds, not evaluated inputs. Local finite-dimensional boundedness does not establish their asserted uniformity. |
| `u₀` | `:111–113`: called `1/g₀²`; `PROOF.md`, `S3 Wilson action`: coefficient `β_K=2N/g_K²` | These conventions require an explicit conversion before transferring numerical curvature in physical g units. All review computations use the target's factored action `S=Σ(1−tr/2)` and do not identify those g conventions. |

LE1, LE2, LE3 and LE5 address real errors in the earlier text. LE4 correctly distinguishes the weighted curvature `Hess V+Ric`, but does not compute it for the joint quotient. The target's remaining lead summary continues to state a broader result than these qualifications support.

The reviewed LCONV/check references to PROOF use section/locating strings rather than numeric `PROOF.md l.NNNN` citations. I located the S4/S4′ definitions by those strings. No stale numeric PROOF citation was found in those reviewed references. Other imported-file line references were not treated as verified source evidence.

## No-Go Discipline Gate — scoped review, no blanket no-go or landing claim

- **N1 — actual alternatives:** point-centred normal-slice convexity (bare counterexamples confirmed); exponential/axial convexity (bare examples and first-order construction confirmed); the chain's joint metric (open); a different global chart satisfying support and tilt domination (open); one-step conditional estimates with fixed coarse data (open, and able to add positive pinning); direct tilted-moment/cluster-expansion estimates (open). These are real mechanisms, not five exhausted routes.
- **N2 — dependencies:** collar admissibility and chart/metric choice are premises of the chain lift, not two proven independent impossibility walls. Completing the local Hessian calculation does not settle either. No independent-wall count is claimed.
- **N3 — hidden premises:** the following graph must be smooth, its tangent admissible for the conditional boundary, the density corrections controlled, and the exact defect predicate matched. Each is explicit in R4/R6. “By construction” is accepted only where the displayed algebra verifies it.
- **N4 — residual matching:** torus/cylinder certificates attack the factored bare action; NC attempts to attack a conditional normalized chain; (LC-1′) additionally allows a suitable gauge-fixed chart. These residuals do not match without bridges. The NU sufficient implication does not establish necessity for every route.
- **N5 — resolution:** coarse invisibility is proved link by link and inductively in the following tower; negative bare curvature is proved on specified finite geometries and an explicit scaling family. Universal claims about every column, every conditional tower, and every useful chart are not banked.
- **N6 — partial closure:** no additional physical axiom is indicated. This is a mathematical task of conditional boundaries, gauge/density geometry, and uniform estimates. The finite bare-action obstruction is useful without resolving those tasks.
- **N7 — steelman against the broad no-go:** freeze the coarse variables required by the actual conditional law. Then the slow following mode may cease to be admissible and its mismatch penalty contributes order-κu curvature. A suitable fixed chart may also move the noncritical-point Hessian contribution into the density and constraint geometry. Establish uniform conditional bounds and control the remaining coupling-response interactions. None of these mechanisms is ruled out by the present bare-action certificates; each still has concrete proof obligations.
- **N8 — prior evidence checked:** CODEX_REVIEW_NRES item 5 explicitly left arbitrary thresholds and the full normalized chain unverified. The current work closes the arbitrary-small-field **bare** family issue and strengthens the chart-specific obstruction. It does not close the complete conditional-chain/chart issue. No snapshots, audit ledgers, or broader history were read.

No formal packet/landing PASS is claimed; this is the one authorized review deliverable. The two additional files read were `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/no-go-discipline/SKILL.md`. All other reads were named targets/checks. No git commands, writes to other files, floating proposal runs, numerical libraries, or large-lattice jobs were used.

## Summary table

| Target | Review verdict | Mathematical status and exact scope |
|---|---|---|
| Stripe's scalar centres, identity coarse fields and zero mismatches | **CONFIRMED** | **PROVEN** algebraically for the stated pattern and sufficiently small β; R4 |
| Membership in the lane's complete defect-free conditional event | **NOT-VERIFIED** | **CONDITIONAL** on the exact imported indicator and collar rules; R4/R6 |
| P=3,5,7 torus bare Hessians and leading coefficients | **CONFIRMED** | **PROVEN** by independent polynomial identities; R5 |
| Width-nine collared cylinder at every sufficiently small τ; `c_*` and transverse sizes | **CONFIRMED** | **PROVEN**, with an exact quotient stronger than the source's tail bound; R2 |
| Fully bounded horizontal box at τ=1/10 | **CONFIRMED** | **PROVEN** for that instance; R7 |
| Two exponential-chart examples | **CONFIRMED** | **PROVEN** by rational enclosures; R7 |
| First-order exponential-chart failure at arbitrarily small β | **CONFIRMED** | **PROVEN** for the explicit coordinate directions by the new `−3β/4+O(β²)` construction; axial-chart embedding remains explicit; R7 |
| FOL's zero kernel Hessian on following tangents | **CONFIRMED** | **PROVEN** as a local differential identity; R6 |
| NC on the actual collared normalized chain, with uniform correction constants | **NOT-VERIFIED** | **GAP**: admissibility, density bounds and chart/metric identification; R6 |
| Claim that (LC-1′) as stated, nr-19 and nr-15's multiscale half have been conclusively refuted | **REFUTED as an inference** | Those actual chain/chart claims remain **OPEN**; failed specified charts do not settle the existential chart requirement; R1 |
| Joint-metric correction of size `O(u₀βτ/K)` | **NOT-VERIFIED** | **ARGUED**; inverse gauge-Laplacian control missing. Constant-weight periodic towers admit a limited repair; R6 |
| Corrected horizontality controls | **CONFIRMED** | Nonzero residuals computed exactly; original `ctrl4 FAIL` remains in the result map; R3 |
| Zero-valued curvature controls as positive-curvature calibration | **REFUTED as a discriminating check** | They cannot detect overall sign reversal; use the nonzero `198/101` neutral control; R3 |
| Fixed `10^−44` below every admissible threshold; automatic large `u₀β²` for every admissible field | **REFUTED** | Correct quantifier is: choose a nonzero field below the thresholds, then choose sufficiently weak coupling; R8 |
| Transfer of the β² coefficient to the plaquette-norm cut t₀² | **REFUTED** | Divide by four: torus `11/6`, C4's displayed 4D bound `c_*/32`; R8 |
| Exact disjointness of convexity and Peierls windows; every-K/every-column promotion | **NOT-VERIFIED** | **ARGUED**, with constants and conditional geometry missing; R8 |
| Tilt is exactly a normalized chain at lowered couplings | **REFUTED** | A field-dependent normalizer ratio remains, and the observable is minimized; R9 |
| One-step conditional positivity, tilted Peierls input, inhomogeneous-coupling cluster expansion | **NOT-VERIFIED** | **OPEN** obligations, not results supplied by the target; R9 |

### Numerical corrections and retained numbers

- **Confirmed existing LE2 correction:** the old transverse `0.7/τ` is replaced by `sqrt(40/c_*)/τ`, approximately `2.09/τ`; the exact ceiling is used in the proof.
- **New coefficient correction:** `−(22/3)β²` becomes `−(11/6)t₀²` to leading order when `t₀=2sinβ`; C4's `−(c_*/8)β²` bound becomes `−(c_*/32)t₀²`, where `c_*/32=70908892219950/247334195090033`.
- **Quantifier correction, not a new universal number:** replace the fixed `τ=10^−44` assertion by `τ<min(1/10,η_q/4,ε_loc/8)` and the chart-domain condition. At `β=g₀`, the target's convention gives `u₀β²=1`; choosing thresholds first does not change that equality.
- **Unchanged:** `c_*=2269084551038400/247334195090033`, torus `−88τ²/3`, and all four C4 ceiling sizes. The displayed `−0.3854` exponential action bound is independently recoverable using the actual transverse derivative norm; its original rounded lift estimate alone was insufficient.

## Exactly what may be banked

1. **The explicit coarse-invisible stripe construction**, including its transporter averages, fine plaquette bound, and induction to an identity following tower. Admission to the complete lane event remains a separately checked hypothesis.
2. **The bare Wilson-action counterexamples:** the horizontal torus coefficients, the exact width-nine cylinder quotient at arbitrarily small field, the transverse lift, the stated `c_*` certificate, and the fully boxed τ=1/10 instance. These are substantial positive mathematical results.
3. **The exponential-coordinate obstruction:** the two certified finite examples and the independent fixed-vector asymptotic `RQ=−3β/4+O(β²)`, with a finite transverse lift at sufficiently small β. This concerns the specified coordinate directions, not all charts.
4. **FOL's local zero-kernel-curvature identity.** Its extension to a particular finite normalized chain is conditional on an admissible following tangent, the relevant chart/metric, and bounded density corrections. The periodic constant-weight horizontality observation is a restricted additional result, not the missing general conditional theorem.
5. **The corrected controls and explicit limitations.** No unrestricted (LC-1′) refutation, no universal convexity/Peierls no-go, no exact lowered-coupling identity, and no completed replacement proof of (LCR°) may be banked from this file. The prior BL-TILT implication under its complete hypotheses is unaffected; it was not independently re-proved in this review.
