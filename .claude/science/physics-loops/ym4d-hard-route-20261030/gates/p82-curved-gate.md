# Gate of P82° at curved regular references — queue row 100
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort not exposed; queue requests xhigh); pinned checkout `d9608eeebf40ad9babc69b9425f3fbda91fff0a3`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, granting no status.

Credit throughout: T. Balaban for the background-propagator architecture; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's definitions, regular class, straightening and kernel conventions; Claude for the submitted `library/p82-curved.md`; Codex for the explicitly conditional library inputs. The outline was fetched once to `/tmp/sa_ym4.tex`. Source retrieval and text inspection are not proof certificates. All mathematical checks below are by hand. References to numbered sections without a filename mean the submitted curved note at the pinned commit.

`ADVANCE` means the indicated conditional mathematical step survives, with any repair explicitly stated; `CORRECT-NO-ADVANCE` leaves its substantive premise open; `WRONG` means a false statement or a missing inference in the submitted proof, not a counterexample to Yang–Mills existence. This report does not gate the entire flat package by association.

## 1. Statement, inputs and constants

**CORRECT-NO-ADVANCE** for the target and dependency declarations. First failing step: none in identifying the required real-reference interface; the proof of Theorem P is evaluated below. The consumer is exactly `a3-derivative.md` Lemma 8.1 and item 2 of its gate's final pending list: all admissible weights, gradient and Hölder outputs, and the separate map `D(1-R)D^T: X_w -> F_w`. Counting multipliers must stay counting multipliers. A complex-reference theorem, a column estimate, and the actual joined-history hypotheses are not supplied by this interface.

The order of choices is noncircular **provided** the local inverse constant is independent of the walk-box size: fix the flat constants, choose M, then the regularity ceiling, rate, separation and nonlinear radii. Constants denoted C(L) also depend on the fixed Hölder exponent. The critical reference's membership in the stated local-gauge class remains an extra premise, not a consequence of the propagator calculation.

## 2. Counterexample attempts

| Subsection | Verdict | First failing step |
|---|---|---|
| 2.1 | WRONG | The claimed negative bottom of `d^T d + DD^T`. |
| 2.2 | CORRECT-NO-ADVANCE | The useful geometric-series estimate depends on the common-gauge comparison in Section 4. The additional inference from Jacobian errors to a necessary plaquette size is not established. |
| 2.3 | CORRECT-NO-ADVANCE | None as a reason to use local gauges; existence with flat constants still needs Sections 4–6. |
| 2.4 | CORRECT-NO-ADVANCE | None as a warning that this coefficient-comparison proof uses a first-difference bound on the local potential. It proves no necessity for P82° itself. |

**D1 — false instability test; repair proved.** For every real U and every allowed one-form a,

\[
\langle a,(d^{\mathsf T}d+DD^{\mathsf T})a\rangle
=\|da\|_2^2+\|D^{\mathsf T}a\|_2^2\ge0.
\]

This holds on each finite lattice with the stated pairings and boundary conditions. The Nielsen–Olesen negative direction concerns a different Hessian, with its additional curvature term; its spectrum cannot be assigned to this sum of squares. Delete the negative-spectrum claim and its asserted necessity conclusion. Smallness here is sufficient to absorb the coefficient perturbation relative to the supplied flat inverse. This correction is complete and does not damage that possible perturbative proof. Also delete the unproved last inference of 2.2: a locally pure gauge can change coefficients without changing any plaquette; the actual common-gauge geometric-series calculation, if established, is what excludes a depth factor.

## 3. Local system, Schur complement and covariance

**ADVANCE**, for the finite-dimensional algebra and gauge covariance, on the domain where the specified contour means exist. First failing step: none. This does not yet supply any uniform inverse bound.

Redoing the scalar elimination gives, with S=A_s^{-1} and N=(Q'S²Q'^T)^{-1},

\[
h=S(g_2+Q'^{\mathsf T}\mu),\quad
\lambda=S(g_1-h),\quad
\mu=N(Q'Sg_1-Q'S^2g_2+g_3).
\]

Thus h=(1-R)g_1 when the other scalar sources vanish. Substitution into the first vector equation gives precisely `d^T d + DRD^T + K^T K`; the last row is `-KA=g_5`. Consequently `S°^{-1}(f,b)` is the vector/multiplier output with sources `(f+K^T b,0,0,0,-b)`. Both signs and the added row mass are needed.

For positivity, zero A_s energy implies a parallel site field with zero transported pillar mean. Each contour transport sends that field to its top value; equivariance and uniqueness of the local mean preserve this statement. The nonzero SU(2) stabilizer is abelian; the zero field needs no stabilizer argument. Every pillar contains its top, so the field vanishes. Disjoint pillars and their nonzero top coefficients give surjectivity of Q'. Hence `Q'S²Q'^T` is positive definite. Finally `ker(Q'S)=Δ_U ker Q'`: for Q'χ=0, A_sχ=Δ_Uχ, and conversely write f=A_sχ with χ=Sf. This identity also explains independence of R from the positive top mass.

Under a real gauge, every insertion is conjugated at its base point. The contour ratio is conjugated at its block top; its mean and each accumulated factor transform in the same way. This proves covariance of the straightened row, including its own-level outward endpoint factors, by induction and then differentiation. All masses are scalar and the norms use covariant differences, so the transformations are isometries. The double-block/read-neighbourhood bounds are the same local geometry required by the flat inputs; no global gauge has been constructed or assumed.

## 4. Near-flat coefficients

**ADVANCE**, conditional on the explicitly supplied one-step analytic/composition input. First failing step: none in (4.1)–(4.2). Here is the depth and seam check, including the transpose powers.

At height j fix **one** fine gauge on the full enlarged read set. The identity-reference value recursion gives `u_m≤C_L δ L^{m-j}`. To check that recursion rather than multiply its constants j times, bootstrap this bound in `u_{m+1}≤L(1+C_Lu_m)u_m`: the correction product is bounded by `exp(C_L Σu_m)`, and `Σ_{m<j}L^{m-j}≤1/(L-1)`. Choose δ so that this improves the bootstrap. The finite-step mean has derivative minus the identity in its defining unknown at zero; its inverse and its first derivatives on a fixed smaller analytic ball have constants depending on L alone. This is the precise supplied local fact, not an assumption that a composed j-step derivative has a depth-free constant.

In the product of Jacobians, the intermediate conjugations are `t_{m+1}^{-1}t_m=z_m^{-1}`. Write the product difference as the sum with exactly one changed factor in each summand. If ε_m bounds its relative error, its row and column norms are at most

\[
L^j e^{\sum\epsilon_m}\sum\epsilon_m,
\qquad L^{-3j}e^{\sum\epsilon_m}\sum\epsilon_m,
\qquad \epsilon_m\le C_L\delta L^{m-j}.
\]

The remaining endpoint conjugation costs O_L(δ) once. Whether it is written as t_{j-1} or as t_j with the last z factor extracted has no effect on this estimate. Multiplication by η gives `δ s_j` and `δ η⁴ s_j^{-3}`. The flat composition has uniform base-site weights because the base coordinates and path indices each run once through their base-L digits. Its row sum is s_j, and its fixed-height column sum is `η⁴s_j^{-3}`. Thus the individual coefficient bound follows from a column bound, not from a row bound divided by the number of sites.

For Q', each site has exactly one pillar and weight `η⁴m_y^{-4}`. The products of contour means and intervening z factors again have total error O_L(δ). Each transport is unitary. In particular, in the physical pairings `Q'^T` is an isometry from top values to their transported constant values on disjoint pillars. This verifies the identity used in 4.1(iv), rather than assuming a general averaging transpose is an isometry.

At an outward seam the read set stays in Ω_{j-1}; its smallest scale is s_j/L. Only that adjacent height and the height of the bond can read a given fine bond. The loss is a fixed power of L, with no sum over j. In particular the counting-row Schur estimate is

\[
\|(K_U-K_1)A\|_{\rm count}^2
\le C_L\delta^2\|m^{-1}A\|_2^2;
\]

the factor η⁴ in the column sum cancels the inverse fine-cell weight in the transpose. This verifies the vector row mass and multiplier blocks in (4.2).

For the differential blocks set `D_U=D_1+𝒜`. The coefficients of 𝒜 have size `Cδ/m`; their differences have size `Cδ/m²`, by the local potential's derivative bound and the convergent exponential series. Expanding a second difference gives `𝒜 Dλ`, a shifted `𝒜 Dλ`, and `(D𝒜)λ`; these are bounded by `Cδ(m^{-1}|Dλ|+m^{-2}|λ|)`. Thus both the H² norm comparison and `A_s(U)-A_s(1):H²_m→L²` follow. For the vector second-order blocks integrate one difference by parts; only the first-order coefficient bound is needed. Pair the Q' error with `m²μ`, and use duality for each transposed block. These exhaust (3.1); the identity block has zero error. The derivative premise is doing real work here.

## 5. Curved parametrix and decay

| Statement | Verdict | First failing step |
|---|---|---|
| Cells and local pure-gauge models | ADVANCE, conditional on F1–F2 | None, with read collars chosen before the separation constant. |
| Lemma 5.0 | ADVANCE | None. |
| Proposition 5.1 | ADVANCE, conditional on F1–F2 and Section 4 | None. |
| Lemma 5.2 as an operator norm on all of X* | WRONG | Treating the sharp source projection `1_z` as norm at most one in X*. |
| Supported-source version of 5.2 below | ADVANCE | None; this is sufficient for every later use. |

The geometric choice must include the **whole** gauge cube, not just the smaller cutoff: enlarge a tile by a fixed L-dependent factor containing its double-block read sets and margin. Increase ρ so that even this enlargement cannot cross two complete collars and, if it meets Ω₁, is contained in Ω₀. It then lies in one adjacent-layer pair. Choose the gauge cube at that pair's smaller scale and include it in this fixed enlargement. Reg supplies its gauge. This only increases the constants preceding M in the separation requirement. A cell not meeting Ω₁ is entirely bare. This construction covers irregular interfaces and the boundary without a gauge near arbitrary boundary data.

For a bare cell, `Q'=I`, `K=ηI`, `K^T=η^{-3}I`, and `K^TK=η^{-2}I`. The scalar elimination gives P=I and R=0. Unitarity gives `0≤D^TD≤16η^{-2}` and `0≤d^Td≤24η^{-2}` by counting the eight site incidences and six plaquettes per bond. Hence the displayed scalar and row-Gram intervals follow. Solve the scalar equations and then the constrained vector equations; the scaled E, H², top and counting norms remove every η power. No curvature smallness, boundary smoothness or global holonomy assumption is used here.

In an interior cell the inverse is the supplied **flat** inverse conjugated by its real gauge, not an unproved curved local inverse. The actual-minus-model form is O_L(α) by Section 4. The covariant product rule gives precisely the flat cutoff commutators with unitary transports inserted: second-order scalar blocks have `(Dh)Dλ` and `(D²h)λ`; the vector form has one cutoff difference after summation by parts; averaging blocks have cutoff oscillation O_L(1/M) over their read sets. Pairing against a test field and applying Cauchy–Schwarz with bounded overlap proves

\[
\|\mathbb R\|\le C_L B_L N_L(M^{-1}+\alpha).
\]

The transpose of smooth-cutoff assembly maps X* into the direct sum of local dual spaces. This is the correct way to localize the dual source in Proposition 5.1; it does not use sharp indicators. Choose M then α to make the last bound at most 1/4. The same reasoning works on the scalar subsystem. This proves (5.1) as a conditional perturbation result.

**D2 — sharp source restriction; repair proved.** A pillar indicator is not uniformly bounded on E or H², and by duality not on their duals. Already at U=1, on a fixed physical torus with fixed-scale pillars and η→0, take a constant one-form v. Its E norm is bounded, whereas the zero-extended `1_P v` has squared gradient norm bounded below by `c/η`, from the bonds crossing a face of P. With J_E the matrix of the E inner product, put

\[
F_\eta=J_E(\mathbf1_Pv)/\|\mathbf1_Pv\|_E.
\]

Then `||F_η||_{E*}=1` but `⟨v,1_PF_η⟩=||1_Pv||_E→∞`. Thus `1_P` is unbounded on E*. On this fixed one-scale geometry the flat matrix M is uniformly bounded `X→X*`. Its inverse cannot erase this divergence in the full X norm. That norm is the sum, with bounded overlap, of finitely many pillar output norms. Therefore (5.2), interpreted as the displayed all-source operator norm, cannot hold uniformly for all y,z. The output was correctly defined as a restriction of derivatives, not a zero-extended Sobolev field; the defect is on the **source** side.

The sufficient replacement is: **if F is already supported over z**, then

\[
\|\mathbb M^{-1}F\|_{\mathcal X,y}
\le C e^{-\delta_w d(y,z)}\|F\|_{\mathcal X^*}.
\]

To prove it, apply the convergent series directly to this F, with no sharp projection of an arbitrary dual vector. The n-th term has norm at most `||B||4^{-n}||F||`; its local output vanishes unless `(n+1)D_LM≥d(y,z)`. Restriction of the already evaluated local derivative norm is contractive. Sum the geometric tail; its rate `log(4)/(D_LM)` is stronger than the advertised `δ_w=log(2)/(D_LM)`. A bounded union of source pillars changes only the constant. The identical proof works for the scalar subsystem. This repairs the estimate required in Section 6 without a new quantitative premise.

## 6. Pointwise, gradient and Hölder outputs

**ADVANCE** for Lemma 6.1 and Proposition 6.2, conditional on the stated free local estimate and with the supported-source repair of Section 5. First failing step: none after that repair. In particular, the proof does not infer a gradient or a Hölder bound from an L² estimate alone.

For Lemma 6.1, the positive-Laplacian convention gives `Δ|u_μ|≤|Δ_Uu_μ|`: pair with the unit vector in the direction of u_μ and use orthogonality of each real adjoint transport. At zero the inequality is immediate. The scalar Dirichlet Green–Poisson comparison supplies the local value estimate. Its inputs can be checked directly: reflection bounds the Poisson kernel by `Cr^{-3}`, the positive quadratic barrier bounds the Green sum by `Cr²`, and one of the disjoint boundary shells has squared L² norm at most `Cr^{-1}||u||²_2`. Cauchy–Schwarz on that shell gives the required `r^{-2}||u||_2` term in four dimensions.

The weighted maximum `Φ=sup(d/r)²|u|` absorbs the small finite-range zeroth-order error: on the cube of radius proportional to d, neighbouring d values are comparable, so the error contributes at most `C a Φ`. Sites within a fixed number of mesh steps of the boundary satisfy the estimate directly from `|u(x)|≤η^{-2}||u||_2`. Choose a so that `Ca≤1/2`. This supplies the value bound on the intermediate cube, including the coupling between at most four components.

Pairing forward and backward shifts in the local gauge gives

\[
\Delta_U-\Delta=B\nabla+C,
\qquad |B|\le Ca/r,\quad |C|\le Ca/r^2.
\]

The first-difference bound on the gauge potential is needed in C. Maximize `d₁|∇u|` on the next inner cube; the free central-gradient estimate gives its upper bound by the value bound plus `r²|g|` plus `Ca` times the same maximum. Absorb again. Near the boundary use the elementary one-mesh difference bound. Reserve a slightly wider inner cube than Q; the constants in the note allow this.

For Hölder regularity the resulting equation has bounded ordinary forcing, `|Δu|≤C(r^{-4}||u||_2+|g|)`. In the free estimate set its divergence source equal to zero and choose any auxiliary exponent ε with β<ε<1. Equivalently, split the difference of the first derivative of the Green kernel into distances below 4t and above 4t. The bounded forcing contributes

\[
C|\Delta u|\,t(1+\log(r/t))
\le C_\beta |\Delta u|\,r^{1-\beta}t^\beta.
\]

The harmonic part has the same bound by its second interior difference estimate. No Hölder assumption on this forcing is needed. The correction from ordinary to covariant gradients is Lipschitz, with size controlled by `|∇A₀||u|+|A₀||∇u|`; a straight path of length t has transport within `Ca t/r` of the identity. These give exactly `r^{1+β}[∇_Uu]_β` in (6.1). Pairs outside one of the smaller local cubes are controlled by twice the gradient supremum, with fixed L-dependent constants.

For Proposition 6.2 the source normalization is essential. A pillar has physical volume m_z⁴, so

\[
\|mf\|_2\le m_z\,m_z^{-3}\,m_z^2=1,
\qquad \|g\|_2\le m_z^{-2}m_z^2=1.
\]

A counting row source has norm one; its transposed force has size `Cs^{-3}` on a bounded collection of adjacent-scale pillars. Thus the repaired decay statement applies to both kinds of source. For `m_y≤64Lη`, the pointwise L² inequality and finite differences give all three output powers, with constants depending on L and β. This includes the arbitrary bare boundary.

At larger scales use `r=m_y/(4L)` and the common small real gauge. Row 3 is homogeneous and yields

\[
\Delta_Uh=Q'^{\mathsf T}\mu-Q'^{\mathsf T}m^{-2}Q'h.
\]

The two terms have size at most `Cm_y^{-4}` times the decaying local X norm: for μ use its physical top weight, and for Q'h use Cauchy–Schwarz over its pillar. Lemma 6.1 therefore gives `|Dh|≤Cm_y^{-3}e^{-δ_wd}`. In row 1, `K^TKA` has size `Cs^{-4}||A||_{2,carrier}`, while `K^Tν` has size `Cs^{-3}max|ν|`. These and the source terms are the bounded forcing for the component Laplacian. The curl/divergence commutators have coefficients `Cη^{-2}|∂U-1|≤Cα/r²` and belong to the small E term of Lemma 6.1. Its value, gradient and Hölder conclusions have powers `m_y^{-1}`, `m_y^{-2}`, `m_y^{-2-β}`, respectively. Counting ν gives the multiplier output directly.

For (6.3), run precisely the scalar subsystem with sources `(g,0,0)`. Its h output is `(1-R)g`, its third equation still has zero source, and the same h argument proves `m_y³|D(1-R)g|≤Ce^{-δ_wd}`. This separate scalar argument is what supplies the otherwise missing divergence member; it is not an estimate on the vector inverse inferred by formal differentiation.

## 7. Theorem P and the consumer

| Clause | Verdict | First failing step |
|---|---|---|
| (a) | ADVANCE | None, conditional on the repaired preceding chain and F1. |
| (b), (c) | ADVANCE | None; summability is in the actual outline metric. |
| (d) | ADVANCE | None; use the scalar output (6.3). |
| (e) | ADVANCE | None for the first, row half of BGR11, with the finite-colour argument. |
| (f), submitted global Neumann argument | WRONG | Its O(α) curvature estimate is applied to bare cells where Reg imposes no such bound. |
| (f), exact-bare-model repair below | ADVANCE | None under the same flat inputs; no new regularity premise. |
| Consumer reading | ADVANCE as a conditional reduction | None after the repairs; membership of U₀ in Reg and the other consumer premises remain pending. |

Clause (a) follows by scalar elimination, not by replacing R with a comb projection. Surjectivity of K follows by solving with arbitrary second source b. Also `Δ_U:ker Q'→ran R` is onto by Section 3 and injective by scalar positivity. For completeness, the field operator defining G is a sum of nonnegative forms. A zero vector in its kernel has `da=0`, `RD^Ta=0`, `Ka=0`, and would give a null vector of the invertible saddle system. Thus G and then the positive row Gram C₀ exist, justifying all named blocks of the inverse.

For (b)–(c), redo the summation input rather than assume polynomial growth. A path of metric length t starting at level i crosses at most `1+t/ρ` complete collars before reaching a higher level. Reverse the path for lower endpoints. Its highest scale is at most `s_iL^{1+t/ρ}`, its Euclidean length at most t times this scale, and its endpoints have levels within `1+t/ρ` of i. Counting grid points at each possible endpoint scale gives

\[
\#\{z:d(y,z)\le t\}\le C_L(1+t)^5
       \exp(8\log L\,t/\rho).
\]

Lift paths to the covering Euclidean lattice on a torus; that only overcounts endpoints. For `τ=δ_w/2` and `ρ≥32 log L/δ_w`, the shell sum is bounded by a constant times `Σ_{n≥0}(n+2)^5e^{-δ_w n/4}`, which converges by comparison with a geometric tail. This is `a3-balaban.md` (5.1)–(5.5), with p=0. No convolution lemma or polynomial metric-ball assertion is used. Splitting the actual forcing into already supported pillar pieces and the datum into counting row sources now proves all-weight value, gradient, multiplier and Hölder estimates. In the displayed line of 7(b), apply the sum separately with centre y for the field output and centre y_{c'} for the multiplier; the same uniform supremum bounds both.

For (d), `D^Ta` is a sum of transported backward first differences. The X norm includes their forward versions on the neighbouring stencils; scales differ by at most L and weights by a fixed exponential. Therefore

\[
|D^{\mathsf T}a|_z\le C_Lm_z^{-2}w(z)^{-1}\|a\|_{X,w}.
\]

Use (6.3) on each supported piece and the same convergent sum. At a Dirichlet boundary m=η and the zero-extension difference is also bounded by the value member. This proves exactly `D(1-R)D^T:X_w→F_w`, with no extra regularity of its input.

For (e), use the actual amplitudes `s_f=m^{-3}`, `s_a=m^{-1}`, `s_{∇a}=m^{-2}`, `s_b=s_λ=1`. The fine input measure is η⁴; the raw row input measure is 1. If the row kernel is rewritten with physical row cell weights, divide its entries by those weights before applying BGR10; the resulting operator and row sum are unchanged. For any fixed output i choose `w_j=e^{-θd(i,j)}`. Fix an output colour coordinate e_r and choose each input vector of magnitude `s_j/w_j` so that `e_r^*A_{ij}v_j` is nonnegative with maximal modulus. The all-weight bound then controls

\[
\sum_j\mu_j s_i^{-1}s_j\|A_{ij}^*e_r\|e^{\theta d(i,j)}.
\]

Sum over the fixed number of output colour/direction coordinates and use `||A_{ij}||≤Σ_r||A_{ij}^*e_r||`. Apply this separately to the differentiated output operator. This proves BGR11's **row** sums at θ; no fine-bond count occurs, and no column conclusion follows. The scalar density/length conversions agree with SA 11864–11954.

**D3 — bare-boundary curvature in (f); counterexample to the claimed perturbation estimate.** Take Ω₁ empty and Ω₀ a single admissible Mη cube, smaller than the prescribed `c_reg Mη` gauge cube, in a sufficiently large torus. There is no cube to test in Reg, so Reg₀ holds for arbitrary real links on Ω₀. All rows are bare. Put one noncentral link H on the ν-edge from an interior site x and all other links equal to one. Put a=v on the μ- and ν-edges from x, and zero elsewhere, with `Ad(H^{-1})v≠v`. On their common plaquette, with orientation μν,

\[
da=\eta^{-1}(v-v)=0,\qquad
\mathfrak da=\eta^{-1}(v-\operatorname{Ad}(H^{-1})v)\ne0.
\]

Every other plaquette contains at most one of those two nonzero field edges; its squared norm is the same for the two curls, since its coefficient is a unitary transport. Hence

\[
\langle a,(\mathfrak d^{\mathsf T}\mathfrak d-d^{\mathsf T}d)a\rangle
=\eta^2|v-\operatorname{Ad}(H^{-1})v|^2>0.
\]

The asserted bound `||V||_{X_w→F_w}≤Cα` would give V=0 here, because α=0. Thus the global small-perturbation step is false on the stated class. This is not a counterexample to clause (f)'s inverse bound: on this bare problem K fixes the field directly.

**Repair of (f), proved conditional on F1–F3.** Use the enlarged system with vector block `𝔡^T𝔡+DD^T+K^TK` from the outset. In each bare cell keep the actual U and the actual plaquette curl. Every plaquette insertion is a unitary transport of one of four edge variables, so `0≤𝔡^T𝔡≤24η^{-2}` exactly as in Lemma 5.0. Its local inverse bound is therefore identical in kind and needs no smallness. In interior cells the flat model is unchanged, since the two curls coincide at one. There Reg gives `|𝔡-d|≤Cαη/m²≤Cα/m`; its vector **form** perturbation is O_L(α). Cutoff commutators have the same four transported insertions and the same O_L(1/M) estimate. Thus the parametrix and the repaired supported-source decay proof apply unchanged.

At coarse outputs, the extra operator `V=𝔡^T𝔡-d^Td` has a fixed-range coefficient bound `Cα/m²` on the interior cube: expand `d^TE+E^Td+E^TE` and use `|d_{pq}|≤C/η`, `|E_{pq}|≤Cαη/m²`. This needs no derivative of curvature. Include `-V` in the small finite-range E term of Lemma 6.1. At outputs with `m≤64Lη`, retain the energy-to-pointwise finite-mesh argument; no small curvature estimate is used there. The scalar subsystem and (d) are unchanged. Summation and the finite-colour argument give (b), (c), (e) for this system too. Choose a single C° large enough for both curl constructions before the final decrease of α_*; the advertised allowance 2C° is then valid. This repair preserves the exact stated regularity class.

## 8. Completion claim, dependencies and research decision

**WRONG as submitted** for the assertion that every step is already written and that F1 is the first possible failure. The first false step in reading order is 2.1 (D1); the first erroneous quantitative lemma used downstream is the all-source formulation of 5.2 (D2); the additional extension failure is 7(f)'s global O(α) estimate (D3). All three have repairs above. A failure of the sufficient flat enlarged-system premise F1 would block this proof; no converse has been proved saying that it must refute Theorem P itself.

| Submitted section | Verdict on the submitted text | First failing step; disposition |
|---|---|---|
| 1 | CORRECT-NO-ADVANCE | None in the target/dependency contract; its completion claim depends on the later proof. |
| 2 | WRONG | 2.1's negative spectrum of a sum of squares; delete the mistaken heuristic. |
| 3 | ADVANCE | None on the averaging chart. |
| 4 | ADVANCE | None, conditional on its stated finite-step analytic input. |
| 5 | WRONG | (5.2)'s sharp-source operator norm; the proved supported-source replacement suffices. |
| 6 | ADVANCE | None after the Section 5 repair; retain F3. |
| 7 | WRONG | (f)'s small-curvature bound on bare cells; use the proved exact-bare-model repair. Clauses (a)–(e) survive. |
| 8 | WRONG | Unqualified completion and the claim that F1 is now the first possible failure. |

**Repaired result: ADVANCE, as an implication only.** With D1–D3 repaired, Theorem P(a)–(f) follows from the explicitly supplied flat local inverse/cutoff/free-regularity inputs. No additional curved scalar-projection comparison on changing sequences is used. In particular the scalar enlargement provides the projection output without inserting the nonlocal R into the local coefficient matrix. At the real critical reference it still requires the stated P81/F0-based proof that this reference belongs to Reg. The real-reference P82° reduction can therefore advance, but neither row 95's flat input nor the reference-class premise is discharged by this gate. It grants no status to nonlinear A3 or any consumer.

### Exact reads of `library/a3-balaban.md`

The submitted [A] list omits the elementary projection identities used elsewhere in its own text and the free-kernel source underlying (7.19). The complete direct mathematical reads are as follows; a repeated derivation is distinguished from a new quantitative assumption.

| Location | What is read, and where it enters |
|---|---|
| §3, (3.1)–(3.2) | Formula for R, positivity of its Gram matrix, and `ran R=Δ ker Q'`; Sections 3 and 7(a). Re-derived finite-dimensional algebra. No bound on the gauge-conversion operator (3.3) is consumed. |
| §5, (5.1)–(5.5) | Collar crossings, scale comparison, metric-ball count and exponential sum, only p=0 in the final curved proof; Section 7(b)–(d). Re-derived above. **(5.6) is not needed** despite the broader header citation. |
| §7, value and gradient proof of (7.19) | Real covariant Kato/Green–Poisson value estimate and the small-drift gradient absorption; Lemma 6.1. The vector zeroth-order coupling and Hölder step are added in the curved note, not contained in (7.19). |
| §8.4, finite-step definition, holomorphy and (8.3) | Existence/uniqueness of the small contour mean, bounded derivatives at fixed L, cancellation of endpoint terms at identity, row/column factors L and L^{-3}; Lemmas 3.2 and 4.2. The identity-reference value recursion does not need the nonzero-curvature recurrence (8.5). |
| §8.5, read-neighbourhood/composition/value recursion, (8.7), (8.9) | Bounded read width, exact straightened iteration, its derivative row/column bounds and accumulated site factors; Sections 3–4. The comparison is re-derived by a single-gauge telescoping sum. The Cauchy estimates for higher nonlinear derivatives (8.8) are not an extra input to this linear theorem. |
| §8.6, outward-row convention (8.10) | Identification of the actual own-level factors at an outward endpoint. This fixes which covariant K is being estimated; it supplies no propagator estimate. Checked against SA 9627–9646 and the derivative gate's Section 6.1. |
| §8.7, (8.11)–(8.12) | Common-gauge comparisons of K and Q' with flat rows/pillar means; explicitly re-derived in Lemma 4.2 and checked in this report's Section 4. The complex-reference paragraph is used only by the unproved final remark. |
| §12, (12.1) | Free Green-function decay and its first differences behind the Poisson gradient argument; explicitly offered in Lemma 6.1 as an alternative to `flat-port.md` (4.2). The second-difference version also underlies the bounded-forcing Hölder calculation. The free argument is reproduced in flat-port, so this is not an additional curved propagator premise. |

There are also **inherited flat scalar facts inside [F1]**: pillar Poincaré (7.10), reproduced as flat-port (4.0), and the smooth scalar lift/Gram lower-bound argument (7.11)–(7.12), reproduced in flat-port (5.1)–(5.2). Flat-port's broader scalar section additionally cites (7.13)–(7.15), (7.19)–(7.20) and §5; those weighted scalar estimates are not silently being required as curved inputs here. The particular local inverse/cutoff/free estimate package used by the curved proof is flat-port §§8.1–8.2 and the **multiplier enlargement** in §9.2, with §4.1. Giving just the unaugmented flat vector inverse would be insufficient. This report keeps all of that flat package pending its own gate.

In particular the curved proof does **not** consume the curved scalar Gram kernel estimates (7.16)–(7.18), the projection-kernel estimate (7.21), a curved vector propagator from §13, or the changing-sequence comparison left open in §14. It also does not use a Ward identity to replace the outline's pillar projection by the comb projection. These exclusions follow from the actual elimination and local matrix, not from the source's completion label.

### Published-source check and remaining scope

Balaban CMP 99, 389–434, OCR lines 423–469 (pp. 396–397) separates (3.35), the small local potential and first derivative, from the additional (3.36). Corollaries 3.5–3.6, OCR 990–1018 (pp. 407–408), give the flat perturbation/local real-gauge architecture. The cover, local models, cutoff identity and walk expansion at OCR 1018–1135 (pp. 408–410), especially (3.87)–(3.90), support the attribution. They do not identify his comb rows with the outline's rows or prove this enlarged system in the new norms. His global weighted conclusion also invokes a separate summation lemma; the explicit outline-metric count above is the required replacement. His Theorem 3.1, (3.42)–(3.47), distinguishes value/gradient, Hölder and differentiated-source clauses, consistent with retaining each member separately here. No garbled OCR exponent is used as a proof step, and no OCR text was copied into the repository.

SA 10129–10137 confirms the small-gauge condition on whole cubes; it also has separate curvature, complex-part and independent-current conditions. The submitted Reg is the premise actually proved against here, not an automatic identification with that entire pair class. SA 11890–11954 fixes the weighted-kernel conventions and distinguishes the two halves of BGR11. Credit for all of these outline definitions and arrangements is to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

The complex-reference remark remains **CORRECT-NO-ADVANCE**: analytic local coefficients do not by themselves provide the real Kato step at complex links, and the indicated weighted resolvent argument is not supplied. M1, M2, the flat periodisation clause, (G1), and the actual consumer matching retained by the derivative gate remain outside this result. None is removed by the repaired real-reference implication.

Only this gate file was written. No numerical or symbolic computation, audit, subagent, commit, push, PR or external post was used.
