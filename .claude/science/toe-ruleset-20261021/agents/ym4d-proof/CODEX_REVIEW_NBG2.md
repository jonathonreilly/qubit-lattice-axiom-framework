# PRE-STATED independent hostile review

Pre-registration time: **2026-10-28 22:14:19 UTC**. Written before reading or deriving the target mathematics.

Deliverable: `CODEX_REVIEW_NBG2.md`. No git commands; no source edits. Review findings use **CONFIRMED / NOT-VERIFIED / REFUTED**; mathematical claims use **PROVEN / ARGUED / CONDITIONAL / GAP / OPEN**. A label in a reviewed source is not evidence. Independence here means a separate derivation; I do not assert unverifiable model provenance.

## Targets and advance refutation criteria

1. **HESSREL / HR-1:** independently derive the pure-gauge Hessian transformation, accounting for tangent coordinates, constraints, gauge fixing and the identity Hessian. A missing covariance hypothesis, a vanishing commutator, or comparison in incompatible frames refutes the claimed unconditional counterexample. Conversely, an explicit admissible pure gauge with nonzero fixed-frame Hessian difference and zero curvature refutes the stated curvature-only estimate. Test the proposed flat-moduli and frame-conjugated replacements separately.
2. **NBG_ADJ / NBG_B:** reconstruct dependency edges without inferring mathematical truth or distinctness from labels or missing proofs. An edge lacking required hypotheses, a circular gate, or incompatible quantifiers refutes its presentation as a proved implication. Counts require an explicit equivalence/counting convention.
3. **NBG_A / NB-1, NB-3, NB-4, NB-5:** differentiate constrained criticality and the reduced action directly; expand background vertices; track every scale factor producing the four claimed exponents. A surviving lower-derivative term, omitted vertex family, missing derivative/curvature factor, exponent error or absent norm hypothesis refutes the corresponding unconditional claim.
4. **Systemic checks:** identify symbols by local definition, distinguish fixed inputs from selected outputs, and ask for each displayed gate whether it can actually reject an admissible candidate. Verify source anchors by strings; do not inherit historical line numbers.

## Evidence boundary

Target inputs: `NBG_A.md`, `NBG_B.md`, `NBG_ADJ.md`, `HESSREL.md`, `CODEX_REVIEW_GAPZ.md`; `BFT_B.md` only in search-located ranges. At most two additional files, reserved for operating instructions. No snapshots or audit ledgers. Any cross-reference not independently inspected remains **NOT-VERIFIED**. Findings will be appended as the derivations proceed; the final section will contain the proved dependency graph only.

## Findings (incremental)

### F1 — The envelope identity survives, with its actual hypotheses

**Verdict: CONFIRMED. Claim: PROVEN as the finite-dimensional smooth identity; CONDITIONAL for the asserted lattice tower.** Anchors: `NBG_A.md:210-229` (NB-1), `:233-243` (NB-2), `:303-304` (CL-4).

Let `z(B)=(a(B),B)` and `ζ_v=(Da(B)v,v)`. Criticality in a fixed product chart gives `DF[(h,0)]=0` and, after one derivative, `D²F[(h,0),ζ_v]=0` for every `h,v`. Consequently `D²E[u,v]=D²F[ζ_u,ζ_v]`. Differentiate this last identity in `w`: its two additional terms are `D²F[(D²a[w,u],0),ζ_v]` and `D²F[ζ_u,(D²a[w,v],0)]`, both zero by the preceding identity. Thus `D³E[u,v,w]=D³F[ζ_u,ζ_v,ζ_w]`. This proof needs only the stated `C³` functional and `C²` critical family; the first proof's use of `a'''` at `:215-218` is unnecessary and is not justified by its stated regularity.

This is not a proof that a sequential lattice tower is jointly critical, differentiable, or defined throughout the consumer's chart. Those are the explicit CL-4 input. A moving constrained slice must first be represented by a fixed chart, with the full transformed functional differentiated. The lattice application therefore remains CONDITIONAL on those identifications.

### F2 — HR-1's covariance identity is correct; its universal noncommutation clause is false

**Verdict: CONFIRMED for ambient chart covariance; REFUTED for “every non-constant G not valued in the centre.”** Anchors: `HESSREL.md:361-374`; `BFT_B.md:4519-4525` (pointwise action and transported slice).

Write `F_Z(A)=𝔉(exp(A)Z)` in left exponential link coordinates. Gauge covariance gives `F_{G·Z}(M_G A)=F_Z(A)` exactly. Since `M_G` is orthogonal in the real adjoint pairing, twice differentiating gives `H_{G·Z}=M_G H_Z M_G^{-1}`. Therefore `H_{G·1}-H_1=[M_G,H_1]M_G^{-1}`. The exact zero criterion is commutation, as stated in HR-1.

The next quantifier is false. In SU(2), choose any fixed noncentral `g₀`, and a nonconstant sign function `z(y)∈{I,−I}`; set `G(y)=z(y)g₀`. This `G` is nonconstant and none of its values need be central, but `Ad_{G(y)}=Ad_{g₀}` is constant. Global color invariance of `𝔉` at `1` implies `[M_G,H_1]=0`. The associated central-link pure gauge is exactly flat. The corrected criterion is **noncommutation of the adjoint action with the Hessian**, not nonconstancy of the group-valued gauge. This correction does not establish HESS-rel: that universal estimate is defeated by any admissible gauge with a nonzero commutator.

The slice qualifier is essential. Directly re-deriving the minimizing slice equation gives `S_E^{G·1}=M_G S_E` (the squared norm and root pin are preserved). An ambient conjugacy is not an endomorphism identity on one fixed slice unless the domains are identified. After the natural pullback, `M_G^{-1}H_{G·1}M_G-H_1=0` at a pure gauge. Thus `HESSREL.md:709-711` (“in any pair, on any slice”) overstates what the fixed-frame counterexample proves.

### F3 — NB-3 confuses the group-product derivative with the logarithm derivative

**Verdict: REFUTED for the exact derivative identity; CONFIRMED for the three-term chain rule for each local potential; NOT-VERIFIED for the corrected analytic estimate (claim status: GAP).** Anchors: `NBG_A.md:273-291`, especially `:276` and `:290-291`; prior finding to re-check: `CODEX_REVIEW_GAPZ.md` F8.

Let `P(t)` be the plaquette product, `P(0)=exp X`, and `S=P'(0)P(0)^{-1}`. The transported signed sum is `S`. Differentiation of the exponential, by inserting the differentiated factor into its power series, yields

`S = ∫₀¹ exp(s ad_X)Y'(0) ds`, hence `Y'(0)=J_X S`, where `J_X=ad_X/(exp(ad_X)−1)=I−ad_X/2+ad_X²/12+…`.

For example, with `X=t iσ₃` and `S=iσ₁`, `[X,S]=−2t iσ₂`, so `Y'(0)=iσ₁+t iσ₂+O(t²)`, not `S`. This is an analytic Taylor-coefficient refutation, not a floating-point test. In the inspected definition, `BFT_B.md:4328`, `d_Z` really is the transported signed sum, so renaming the log derivative `d_Z` would silently change the object.

The exact chain rule is still `D³(W∘Y)=W'''[Y',Y',Y']+3W''[Y'',Y']+W'[Y''']`, and likewise for the soft potential: three outer derivative patterns per potential, six altogether, rather than six individually nonzero terms at every background. An analytic `J_X=I+O(|X|)` preserves a derivative output locally, so this error alone does not disprove the four exponent counts. It does require repairing the response maps and their norms before banking NB-4/NB-5. Nontrivial pure gauges also show why “at Z≠1 the outer families switch on” needs qualification: their plaquette logs and matched soft residuals can both be zero.

The genuinely new zero-differentiated-leg family does exist. Take `A=iσ₁`, `B=iσ₂`, `C=iσ₁−iσ₂` and the four-link product `P(t)=exp(tA)exp(tB)exp(−tA)exp(−tB)exp(sC)` (the final fixed factor is the background on the last link). Its first variation is zero, while `[A+B,[A,B]]=4C` and its cubic coefficient is `2C`. Therefore `d³/dt³ Re tr(I−P(t))|₀ = −12 Re tr(C exp(sC)) = 48s+O(s³)`, nonzero for sufficiently small nonzero `s`. Since `Y'(0)=0`, only `W'(X)[Y'''(0)]` contributes. Exact rational multiplication in the basis `(I,iσ₁,iσ₂,iσ₃)` returned the coefficient of `t³s` as `−4I`, hence **48** for the coefficient of `s` in the third action derivative. Thus the failure of the universal “exactly one differentiated leg” rule is independently established even though NB-3's displayed identification of `Y'` is wrong.

### F4 — The tensor norm equality is false: **4 ≠ 2**

**Verdict: REFUTED. Corrected norm relation: PROVEN.** Anchor: `NBG_A.md:122-124`, the displayed definition of `N3`.

For a real symmetric trilinear tensor on two coordinates, set `T111=T112=1`, `T122=T222=−1`, with all permutations assigned the same coefficient. Both fixed-first-index matrices have absolute entry sum **4**. Their bilinear suprema on `|Y|∞,|W|∞≤1` are **2**: for the first matrix the expression is `Y₁(W₁+W₂)+Y₂(W₁−W₂)`, whose maximum is `|W₁+W₂|+|W₁−W₂|=2 max(|W₁|,|W₂|)≤2`; the other matrix has the same maximum. Thus

`max_x Σ_{y,z}|Txyz| = 4`, but `max_x sup_{Y,W}|T(δ_x,Y,W)| = 2`.

These values use real directions. If the intended supremum allows complex directions, its value is **`2√2`**, still not 4: `|W₁+W₂|+|W₁−W₂|≤2√2`, with equality at `(W₁,W₂)=(1,i)`. Thus complexification does not repair the equality.

This is also a genuine symmetric third derivative: take the cubic polynomial `E(x,y)=(x³+3x²y−3xy²−y³)/6`. Plain Python enumeration of the finitely many sign vertices independently returned **4** and **2**. The exact correction is

`sup_{|W|∞≤1} N₀(T[W]) = max_x sup_{|Y|∞,|W|∞≤1}|T(δ_x,Y,W)| ≤ max_x Σ_{y,z}|Txyz|`,

with strict inequality possible. Arbitrary signs on pairs `(y,z)` need not factor as `Y_y W_z`. The consumer Hessian Lipschitz bound uses the left-hand quantity; the coefficient-row `N3` is stronger. A one-ℓ¹-leg/two-sup-leg trilinear estimate does not establish equality. NB-4's stronger `N3` conclusion needs absolute response-kernel estimates carried through the coefficient sums, or the target must be stated in the weaker consumer norm. This finding does not prove that such stronger estimates are impossible.

This is not repairable by one universal factor independent of volume. For `n=2^m`, take the symmetric sign matrix `H_uv=(−1)^{u·v}` indexed by binary vectors. Summing characters gives `HHᵀ=nI`. Define a symmetric tensor by `T_{0ij}=H_ij` and its permutations, with all other entries zero. Its maximum absolute row sum is `n²` for `n≥2`; its displayed bilinear supremum is at most `max(n^{3/2},2n)` by Cauchy–Schwarz for row zero and direct summation for the other rows. Their ratio is at least `√n` for `n≥4`. Hence a volume-independent passage from the weaker norm to the stronger one cannot be assumed.

### F5 — The four slopes are correct at (2,3); the portable thresholds and dimension claims are not

**Verdict: CONFIRMED for the conditional exponent arithmetic; REFUTED for the independent residual relaxation and for treating fixed-weight critical dimensions as those of the advertised dimension-dependent pair.** Anchors: `NBG_A.md:305-331`, `:336-348`, `:368-372`, `:483-498`; `NBG_ADJ.md:496-506`; repeated relaxed threshold at `HESSREL.md:479-480`.

Re-derive without importing the script: let `c=θ_w^c`, `r=θ_w^r`, `a=θ_A`, and depth `n=k−j`. The stipulated mixed response estimate supplies a volume factor `L^{dn}` for the localized ℓ¹ leg. A Wilson differentiated leg supplies `L^{−ck}`, a potential leg `L^{−ak}`, and a residual leg at level `j` supplies `L^{−r(n−1)}`. The new outer-potential coefficient supplies one further background curvature or residual weight. Multiplying these factors gives:

| Family | Product of weights | Leading slope |
|---|---|---|
| Wilson, three differentiated legs | `L^{dk} L^{−ck} (L^{−ck})³` | `d−4c` |
| Wilson, no differentiated leg | `L^{dk} L^{−ck} (L^{−ak})³` | `d−c−3a` |
| Soft, three residual legs | `L^{dn}(L^{−r(n−1)})⁴` | `d−4r`, intercept `4r` |
| Soft, no residual leg | `L^{dn}L^{−r(n−1)}(L^{−an})³` | `d−r−3a`, intercept `r` |

At `(d,c,r,a)=(4,2,3,1)`, these are exactly **−4, −1, −8, −2**. At `L=3`, the soft sums are exactly `Σ_{n≥1}3^{−2n+3}=27/8` and `Σ_{n≥1}3^{−8n+12}=531441/6560`. The existing soft family gives `Σ_{n≥1}3^{−n+3}=27/2=13.5`. These are arithmetic confirmations conditional on the actual response norms and leg weights, not confirmations of those estimates.

With `a=min(1,c−1)`, simultaneous strict negativity at `d=4` requires

**`c>7/4`, `r>4−3 min(1,c−1)=max(1,7−3c)`**.

The independent claim `r>1` is wrong when `7/4<c<2`. The rational choice `c=9/5`, `r=6/5`, `a=4/5` gives **−16/5, −1/5, −4/5, +2/5**. At `c=9/5` the corrected residual floor is **8/5**, not **1**. The prior F9 finding survives independent recomputation.

There is a second stale-quantifier issue. Critical dimensions **8, 5, 12, 6** result from keeping `(c,r,a)=(2,3,1)` fixed while varying `d`. The theorem instead advertises `r=d−1` at `:305-306`. Along that family, the four slopes are **`d−8`, `d−5`, `4−3d`, `−2`**. The soft slopes have **no upper critical dimension**; at `d=5` the old one-residual soft slope is **−1**, not **0**, and at `d=12` the three-residual slope is **−32**, not **0**. The fixed-weight numbers are valid only with the weights frozen and must be labeled accordingly.

Finally, at `c=0,r=3,a=−1`, the new slopes are **4, 7, −8, 4**: **three**, not “every”/four, are positive (`NBG_A.md:371`). Divergence of these upper-bound series shows that this proof fails without H2; it does not by itself prove the weakened mathematical conclusion false.

### F6 — Global FLAT-REF is false on the stated curvature-only class

**Verdict: REFUTED under the displayed all-level quantifier. Counterexample claim: PROVEN.** Anchors: `HESSREL.md:502-504`, `:515-526`, `:748-749`; class and chain definitions: `BFT_B.md:2865-2866`, `:4328-4329` (`Z_k:=V`).

This is stronger than saying a global gauge theorem has not been proved. Fix `N=2`, and let the coarse four-torus have side `T=4m`. Embed a commuting U(1) with generator `H=diag(i,−i)`, of operator norm one. Define a periodic integer ramp on the first coordinate:

`q(s)=s` for `0≤s≤m`, `q(s)=2m−s` for `m≤s≤2m`, and `q(s)=0` for `2m≤s<4m`.

Set `V₂(x)=exp(q(x₁)H/m²)` and `V₁=V₃=V₄=I`. All plaquettes except 12-plaquettes are trivial, and a 12-plaquette is `exp((q(s+1)−q(s))H/m²)`. Thus **`f_k=1/m²`** in this normalization, so these configurations lie in every fixed `𝒦(ε₀)` for large enough `m`. Other fixed Lie-algebra norm normalizations change only fixed factors.

The contractible `m×m` square in the increasing part of the ramp has holonomy **`exp H`**, independent of `m`. Suppose the top-level clause of FLAT-REF held: `V=g·(B exp a)`, with flat `B` and `max_b‖a(b)‖≤C/m²`, with `C` independent of `T`. Flatness makes the `B` holonomy around this square exactly `I`. Telescoping the product of its `4m` unitary link factors gives

`‖Hol_V−I‖ ≤ 4m max_b‖exp a(b)−I‖ ≤ 4C/m`.

Gauge transformations only conjugate the holonomy, so the left side is the fixed nonzero number `‖exp H−I‖=2 sin(1/2)≥23/24` (use `sin t≥t−t³/6` at `t=1/2`). Contradiction for `m>96C/23`.

More quantitatively, **every** gauge and flat comparison satisfies `max_b‖a(b)‖≥23/(96m)=(23/96)√f_k`; no uniform `C f_k` bound can hold. This example has zero net flux and does not need nontrivial bundle topology. The missing scale is the growing diameter. If FLAT-REF is narrowed to exclude the prescribed top level, the displayed argument no longer directly decides it; such a new statement must supply a bridge from its fine chain to `V` and is NOT-VERIFIED here. The statement actually written says “every level” and uses the chain with `Z_k=V`.

Therefore the HR-4 Neumann implication can remain a true abstract implication while its advertised global antecedent is unsatisfiable on the stated class. Naming FLAT-REF OPEN or “the wall” does not make this version a viable research target.

### F7 — The literal pure-gauge obstruction survives; the framed comparison does not share it

**Verdict: CONFIRMED for refuting the ambient, fixed-coordinate HESS-rel; NOT-VERIFIED for a specified restricted-slice version until its domains are identified.** Anchors: `NBG_A.md:430-434`; `HESSREL.md:376-412`, `:661-683`.

An actual Wilson-block witness can be built without accepting the reported 0-form experiment. In a fine 12-plaquette away from coarse roots, put a gauge parameter `λ=T` at its corner `y+e₁` and zero elsewhere, with `T∈su(2)`. The full composite gauge tangent is `x=Ξλ`; at level zero `x₀=dλ`, so the flat Wilson curl is zero. At the trivial chain, gauge invariance and criticality imply `H₁x=0` for the **whole** Hessian, including the soft terms.

Choose a chain gauge whose adjoint action is `R` at `y`, identity at the other three corners, and `RT≠T`. Then `v=M_Gx` has plaquette curl `(R−I)T`: the two contributing edges of `dλ` formerly canceled and now have values `RT` and `−T`. The flat quadratic energy is a sum of nonnegative Wilson and soft squares, so `⟨v,H₁v⟩>0`. But covariance gives `H_{G·1}v=M_GH₁x=0`. Thus `H_{G·1}−H₁≠0` even though every background plaquette and matched residual is flat. This argument uses an admissible gauge tangent vanishing at the coarse roots and works inside four dimensions. It is an ambient argument, not a claim that this gauge tangent belongs to the gauge-fixed physical slice.

It proves the failure for the gauge-orbit reading explicitly adopted in `HESSREL.md:180-185`. Extending this witness to a particular fixed representative `Z^{off}(V)` requires that representative's precise equivariance under the chosen gauges. `BFT_B.md:3845` asserts covariance, but the representative and the gauge-extension map are not constructed in the inspected ranges. I therefore do not upgrade that additional representative-specific assertion to an independent confirmation.

The original numerical certificate was indeed for the wrong operator; HESSREL itself corrects this at `:662-669`. Its replacements report **1536** Wilson-difference entries and squared responses **8** versus **10**. Those script outputs are NOT-VERIFIED in this bounded review. Even if correct, `sqrt(8/10)` is a **ratio of two responses to one vector**, not the asserted ratio of operator norms at `:681-682`. The same distinction applies to **4** versus **20** at `:391-394`. No corrected operator-norm number follows from those data alone.

### F8 — The repaired Neumann arrow is valid only after full operator and frame alignment

**Verdict: CONFIRMED for the matched Banach-space implication; REFUTED as a viable global repair with FLAT-REF as written; NOT-VERIFIED for the local-to-global frame route.** Anchors: `HESSREL.md:442-473`, `:497-512`, `:699-718`, `:748-755`; `BFT_B.md:4332-4333`.

Here is the exact surviving implication. On specified Banach spaces `X,Y`, let `A:X→Y` be an isomorphism with `‖A⁻¹‖≤M`. Let `E:X→Y`, and assume **`q=‖A⁻¹E‖_{X→X}<1`**. Then

`(A+E)⁻¹ = Σ_{n≥0}(−A⁻¹E)^n A⁻¹`, with `‖(A+E)⁻¹‖≤M/(1−q)`.

This follows because the geometric partial sums multiply `I+A⁻¹E` to `I−(−A⁻¹E)^{n+1}`, whose remainder tends to zero in operator norm. It works for rectangular norm pairs; it does not assume Hilbert coercivity or identify that with the weighted inverse bound.

For a flat reference `B` and gauge `g`, use the **pulled-back** full gauge-fixed operator

`A=𝓛_B`, `E=M_g^{-1}𝓛_Z M_g−𝓛_B`,

with the corresponding source and slice identifications. Uniform flat inverse bound `M₀` and `‖E‖≤CΛ₀ f_k` imply a background inverse bound at the explicit threshold **`CΛ₀M₀ f_k<1`**. A hypothesis directly bounding `‖A⁻¹E‖` needs no separate forward bound. If the absolute estimate is obtained through `‖A‖`, one must bound that forward norm uniformly over the actual comparison references. An at-identity bound does not automatically give a bound over all flat moduli.

Two silent object changes remain in the displayed repair:

- `HESSREL.md:193` defines FWD-0 for **`Hess𝔉(1)`**, but `:443-446` uses it for **`𝓛₁=Hess𝔉(1)+ΓᵀΓ`**. Likewise the original HESS-rel prices only the bare Hessian difference, while `:455` substitutes it as a bound for the full gauge-fixed difference. The additional term `Γ_ZᵀΓ_Z−Γ_1ᵀΓ_1` must be controlled or transported explicitly.
- FLAT-REF writes `Z=g·(Z^♭e^a)` at `:504`, but HESS-rel′ subtracts **`𝓛_{Z^♭}`** directly at `:500`. Closeness of `g⁻¹·Z` to `Z^♭` does not imply closeness of `Z` to `Z^♭` in fixed coordinates. Replace the difference by the displayed pullback, or replace the reference by `g·Z^♭` and transport the norms and slice. An isometry transfers inverse bounds; it does not by itself repair this subtraction.

Once these are made explicit, HR-4 is an ordinary **PROVEN implication between hypotheses**. F6 means its advertised global FLAT-REF premise fails, so that implication supplies no global theorem on all of `𝒦(ε)`.

**What remains plausible.** On a fixed-diameter contractible frame, an axial trivialization expresses each transported link as a product of at most `C_d R` plaquettes. Telescoping gives link distance `O(R f)` in unit lattice spacing; with fine spacing `ρ` and fixed coarse diameter `R`, the own-link logarithm is `O(Rρ f)`. Local analyticity then gives small changes in each fixed local coefficient. At a pure gauge, the conjugated Hessian equals its flat counterpart exactly, so HR-1 cannot refute this version. Turning coefficient estimates into a uniform bound in `𝔐→Y`, including gauge fixing, boundary conditions and slice maps, remains GAP. Patching frame inverses into a global inverse is an additional GAP, not an implication of small local curvature alone. Neither the flat-moduli inverse nor global patching is established by translation invariance of constant flat representatives.

The claimed weight window also needs its proper scope. For a diagonal level map with input weight `ϖ_l` and output weight `ω_l`, the cost is multiplied by **`ω_l/ϖ_l`**. If the own-level bound is `CL^{−2(k−l−1)}f`, this upper bound is uniform when `ϑ^Y−ϑ^𝔐≤2`. It is a sufficient worst-case envelope criterion, not an “iff” for an operator whose coefficients may be smaller or zero (`HESSREL.md:467-473`). W-lev at `:318-319` only says each family ignores form degree; it does **not** imply equality of the two families. For example, `ϖ_l=1`, `ω_l=L^{3(k−l)}` are both level-only but cost a growing factor. Thus W-lev alone does not prove the claimed weight-free estimate in `:311-323`.

### F9 — O(k) inverse growth is not O(k) third-derivative growth

**Verdict: REFUTED as the stated inference. The weakened lattice hypothesis remains OPEN.** Anchors: `NBG_ADJ.md:307-312`, `:375-376`; `HESSREL.md:735-738`; contrast `NBG_A.md:167-171` and NB-1.

NB-1 has **three** response legs. An inverse estimate growing like `k` can produce three powers of `k`, before any locality constants are considered. Exact scalar countermodel to the asserted transfer rule:

`F_k(x,b)=x²/(2k)−bx+x³/6`, with the critical branch `a(0)=0`.

Criticality is `a/k−b+a²/2=0`. At zero, `F_xx=1/k`, `F_xb=−1`, so **`a'(0)=k`**. Differentiate criticality again: `a''(0)/k+(a'(0))²=0`, so `a''(0)=−k³`. Since `E'(b)=−a(b)`, **`E'''(0)=k³`**. Equivalently, `F_xxx=1` and NB-1 gives `1·k³`. All local cubic coefficients and the mixed input coupling are fixed; the inverse is `k`. This is a countermodel to a general inference, not a claim that this scalar model is the lattice action.

Thus a permissible `C_♭^{(k)}=O(k)` does not justify replacing H3 by an O(k) inverse estimate. Even the crude bound would require response growth no faster than `k^{1/3}` to reach O(k), with every other constant uniform; that is a sufficient bookkeeping condition, not a sharp lattice requirement. Furthermore `NBG_A.md:167` contains `(𝔠_∞^{(i)})² C_♭^{(i)}` in the threshold: allowing an inverse-related constant to grow can also change that denominator. Every constant must be propagated through the consumer, not just the symbol `C_♭`.

### F10 — NBG_ADJ does not repair the status argument or prove the six non-implications

**Verdict: REFUTED for the claimed proofs of independence/non-implication; NOT-VERIFIED for all six project-specific implication questions.** Anchors: `NBG_B.md:231-238`, `:252-283`, `:729-747`; `NBG_ADJ.md:151-179`, `:272-283`, `:327-343`, `:386-399`.

“P has been proved” and “Q has not been attempted” are not truth values of P and Q. They are compatible with equivalence: an overlooked proof can close Q when P=Q is recognized. This refutes NBG_ADJ's endorsement at `:154-157` under **both** readings β and γ, not just its stated exception α. A status-label gate cannot decide this question.

The proposed replacement at `:166-177` still does not prove non-implication. A decomposition of a desired conclusion into a gap and a Hölder estimate is a list of proof obligations. “No decay claimed” is not “decay cannot follow.” A different slice needs a bounded transfer map; not exhibiting that map does not prove none exists. The cited PROOF descriptions have not been independently read here, but this inference fails even granting every quotation verbatim.

A direct counterexample to the categorical prohibition at `NBG_B.md:252-253` is the local operator `A=I−(S+S⁻¹)/4` on scalar sequences, where `S` is the unit shift. Its real ℓ² gap is at least `1/2`. For the weight `w(x)=(3/2)^{|x−y|}`, the weighted off-diagonal operator has row and column sums at most `3/4<1`; its inverse Neumann series has norm at most **4**, and so `|A⁻¹(x,y)|≤4(2/3)^{|x−y|}`. Thus a gap plus controlled finite range can produce decay that was not included in the input's statement. This does not supply the missing constants in the project's `𝔐→Y` pair.

For the positive direction, an actual observed response has the form `K=C H⁻¹J`. Neither equality of names nor a bound on K establishes a bound on H⁻¹ for arbitrary sources. For `F_n(x,b)=(x−b)²/(2n)`, the data response is identically one while the Hessian inverse is `n`. Conversely, a full inverse bound only gives `‖K‖≤‖C‖‖H⁻¹‖‖J‖` after the maps and norms are specified. `BFT_B.md:4592` explicitly leaves those composition constants and the weighted commutator constant unwritten. This directly blocks the claimed proof of the graph's GAP-Z→H3 bridge.

| Project arrow | Honest disposition after removing status arguments |
|---|---|
| GAP-Z → G♯_0-field | **NOT-VERIFIED**: inverse norm, regularity and slice transfer must be specified; no project counterexample is supplied. |
| G♯_0-field → GAP-Z | **NOT-VERIFIED**: moving from a flat estimate to the full background class requires an actual perturbation/patching theorem. |
| GAP-Z → N-bg | **NOT-VERIFIED**: critical-chain weights, absolute response bounds, localization and chart coverage are missing. |
| N-bg → GAP-Z | **NOT-VERIFIED for this lattice system**; a generic inference from a third-derivative bound to an inverse bound is false (quadratic actions have zero third derivative and arbitrarily small Hessian eigenvalues). |
| G♯_0-field → N-bg | **NOT-VERIFIED**: a flat field estimate is not the displayed background/chart theorem, and no bridge is proved. |
| N-bg → G♯_0-field | **NOT-VERIFIED for this lattice system**; derivative order alone supplies no general inverse/regularity theorem. |

The admissible restriction **a precisely stated uniform background estimate ⇒ the same estimate at Z=1** is PROVEN: `1∈𝒦(ε)` and the displayed covariant operators and slice reduce to the flat definitions (`BFT_B.md:2865`, `:4328-4334`). This restriction does not identify which of the three quantities called GAP-Z is intended.

The table at `NBG_ADJ.md:325-329` can be retained as an **administrative grouping**: three target names and six listed work headings (splitting H2 into curvature and soft parts). It does not establish **two mathematically independent paper-scale obstructions**. No independence proof or exhaustive work decomposition is supplied; the named sufficient routes are incomplete. A node being downstream of a larger hypothesis package does not show that its proof adds no work. “No outgoing edge” in the drawn subgraph is not a mathematical fact about its consumers; `NBG_A.md:161-162` itself names downstream consumers of N-bg. The corrected mathematical count is **undetermined**, not a replacement integer.

### F11 — NB-5's intended reduction is substantive, but the displayed consumer theorem is not yet checked

**Verdict: NOT-VERIFIED for NB-4/NB-5 at their stated norm and consumer quantifiers; REFUTED for NBG_ADJ's promotion of the five/six named inputs to an already-proved edge. Claim status: GAP pending the bridges below.** Anchors: `NBG_A.md:126-151`, `:303-332`, `:389-402`; `NBG_ADJ.md:204-218`, `:243-244`, `:368-383`, `:433-437`.

F1 proves the exact algebraic reduction and F5 proves its numerical slopes under explicit mixed response assumptions. F3 supplies a local repair candidate for the missing logarithm derivative. These support a useful conditional theorem; they do not verify all of the named H3 by reference to uninspected lemmas.

To obtain the actual consumer conclusion one still must establish:

1. A jointly critical C² family in a **fixed product chart**, at every point of the consumer's lift-chart ball, not only at its centre. H1 is stated at V; the consumer at `:133-135` quantifies over every A with `|A|∞≤r₀`. Existence, curvature/residual margins and all constants must cover that tube, with any coordinate changes differentiated.
2. The background response bounds for the **derivative of the logarithmic coordinates**, including `J_X` and the soft-coordinate analogue, in the exact coefficient or consumer norm used. NB-3 currently asserts the wrong exact derivative.
3. Mixed **absolute kernel** ℓ¹/sup bounds if the stronger coefficient-row `N3` is claimed, or an explicit change to the weaker Hessian-Lipschitz norm from F4. The false equality cannot bridge them.
4. A route from the chosen interpretation of GAP-Z to those full response estimates, with all cross-level maps and gauge representatives, not only the two observed outputs. Combes–Thomas in the required weighted pair and the nonlinear soft-residual estimate are not discharged by calling the resolvent a response kernel.

The statement “a first-order hypothesis cannot contain a third-order conclusion” (`NBG_ADJ.md:205`) is not an anti-circularity proof. Establishing a first-response bound may use the very third-derivative bound under construction. As an abstract implication with H1–H3 supplied independently, the method is not automatically circular; the actual proof dependencies must still be checked. Likewise matching exponents is not an independent check of the missing maps, norm identity or quantifier coverage.

There is a precise, **PROVEN conditional replacement**: a C² jointly critical family, plus uniformly bounded corrected local cubic coefficient tensors, plus the mixed absolute response-kernel estimates with the leg weights in F5 **throughout the consumer chart**, imply a uniform coefficient-row cubic bound. To prove it, expand the finite local tensors, take absolute values before summing their coefficient indices, put the first response column in ℓ¹ and the other two absolute row sums in sup, and apply F5. The old Wilson slope is zero and occurs once, the old soft slope is −1, and the four new slopes are negative at `(2,3,1)`; their level sums are finite. This establishes the implication with those explicit premises. It does not assert that the loosely named H3 or the six-item list already supplies them.

### F12 — The gates discriminate arithmetic, but several advertised conclusions are outside their reach

**Verdict: CONFIRMED for the limitations below; NOT-VERIFIED for every cited script implementation/output.** Anchors: `NBG_A.md:475-504`; `NBG_ADJ.md:483-512`; `HESSREL.md:548-570`, `:661-683`; `NBG_B.md:605-624`; `BFT_B.md:4707-4712` (located by the string “Nothing in Tier C is tested”).

| Gate or criterion | Could it fail? What can it actually decide? |
|---|---|
| na1/ad1 exponent substitution | **Yes**: the exact pair `(c,r)=(9/5,6/5)` makes one new slope positive. It tests a leg-counting formula after the ingredients have been supplied; it does not establish any response estimate, chart radius or operator identity. |
| ad1-D, substituting the alternate soft formula | The formula values differ, **−8 versus −4**, but **both pass** the advertised negativity criterion. Thus that change is not a rejecting control for ad1-B; `NBG_ADJ.md:501-502` admits this. It detects formula difference only. |
| na1-B pre-registered formula match | The reported mismatch is consistent with the independently derived four-residual-factor count. Calling it a transcription mistake does not make the original gate pass; it also does not negate the correct new count. |
| hr1, pure-gauge Hessian comparison | **Yes** for a specified operator: constant adjoint rotations give equality, suitable varying ones do not. The first gate tested 0-forms, not the Wilson Hessian. The corrected gate must identify the full operator/domain; a subblock computation and one-vector ratio do not certify the claimed whole operator norm. |
| A proof-status comparison | **Cannot decide identity or non-implication**. Changing a label without changing the mathematics can change this gate's apparent answer. |
| FLAT-REF as a universal global acceptance criterion | **Unsatisfiable on the stated full class**, by F6. This is not merely an unproved input. A local, diameter-dependent replacement is a different criterion. |
| nb1 power-law summability | Exact shell counting suffices: dyadic shells of `ℤ⁴` contain `Θ(R⁴)` points and the radial power −4 has shell mass `Θ(1)`, whereas power −5 has shell mass `Θ(1/R)`. A nonsummable *upper envelope* does not prove an actual kernel nonsummable; a gapped composite resolvent is a different object. No decimal outputs were reproduced here. |
| NBG_B's “no admissible exponent” (`:459-472`) | A sufficient proof window is not a necessary condition on the theorem. The single-symbol collision needs repair, but failure of the displayed contraction argument alone does not prove the target unsatisfiable. The cited original definitions/windows outside this read budget remain NOT-VERIFIED. |

No script files, criteria files or saved outputs were opened: the two additional-file slots were used for the required methodology and review skill. In particular **no reported PASS is adopted as this review's PASS**. Independent checks actually performed here used only rational arithmetic in plain Python: the symmetric tensor maxima; exponent substitutions and geometric sums; and truncated exact SU(2) algebra. The analytic counterexamples and inverse formula were derived in this report, not inferred from those scripts.

### F13 — Edge-by-edge disposition of NBG_ADJ's actual graph

**Verdict: NOT-VERIFIED for the displayed graph as a graph of established project implications. The explicit corrected implications below are PROVEN.** Anchors: `NBG_ADJ.md:345-404`; `HESSREL.md:748-749`.

| Displayed or asserted edge | Review verdict and exact surviving content |
|---|---|
| Per-level physical gap + G♯_0-fine → G♯_0-field | **NOT-VERIFIED.** An order of work is not the sufficiency theorem. The source spaces, reconstruction maps and uniform Hölder estimates were not re-derived in the allowed sources. |
| Flat composite inverse + HESS-rel → GAP-Z | **REFUTED as a working route using the stated HESS-rel**; that perturbation claim is false in fixed coordinates. **CONFIRMED** for the corrected matched-operator Neumann implication with `q<1` (F8). |
| FLAT-REF + flat-moduli inverse + HESS-rel′ + FWD-0 → GAP-Z | **CONFIRMED only as the corrected abstract implication** after frame/slice identification and smallness. It is not a viable global construction with the literal FLAT-REF (F6); the needed flat-moduli bound and local-to-global bridge remain **NOT-VERIFIED**. |
| CL-4 + BFT-1 + GAP-Z + (N-loc)^Z + CT → N-bg | **NOT-VERIFIED** in the displayed names/quantifiers. H2's soft part is separate in the six-item table, the GAP-Z→full-response bridge is missing, and F3/F4 expose errors in the claimed proof. The explicit corrected response-package implication in F11 is **CONFIRMED**. |
| BFT-4/Cauchy on a k-uniform polydisc → N-bg | **NOT-VERIFIED** as the cited project route. Analyticity and a uniform radius alone do not bound derivatives: `E_n(z)=n z³` is entire with unbounded third derivative. A uniform norm bound on the holomorphic Hessian, with a positive interior margin, does give the consumer bound, as derived below. |
| GAP-Z → all Tier-C / TRANSP / closure of both branches | **NOT-VERIFIED**. `BFT_B.md:4592` leaves the weighted commutator and response-composition constants unwritten; `:4600-4601` also specifies N1-nd, the off-shell lift, m=0 and composite-co-closed sources. These do not automatically cover the nonlinear critical chain and every point of its consumer chart. |

For the corrected analytic edge, if `H(z)` is a holomorphic Hessian valued in the `N₀` matrix norm and is bounded by `S` on a complex sup-ball of radius `r`, Cauchy's integral along any unit direction `w` gives `‖DH(0)[w]‖_{N₀}≤S/r`. Apply this at every interior point with its uniform distance to the boundary. This proves the consumer Hessian-Lipschitz estimate in F4's weaker norm; it does not prove the stronger coefficient-row norm without additional coefficient estimates.

### F14 — Symbol and reference accounting

**Verdict: CONFIRMED for the following inspected distinctions and one citation mismatch; NOT-VERIFIED for uninspected cross-references.**

| Symbol/name | Exact object located in this review | Unsafe substitution |
|---|---|---|
| `d_Z` | Transported **group** variation, `BFT_B.md:4328` | Logarithmic derivative `J_X d_Z`, `NBG_A.md:276` (F3). |
| `N3` | Coefficient absolute row sum and a different bilinear supremum are equated at `NBG_A.md:123` | These are not the same norm (F4). |
| `f_j` versus own-unit plaquette log | `f_j` is `ρ_j⁻²` times the maximum plaquette-log norm, `BFT_B.md:2859-2861`, `:4329` | The two differ by `ρ_j²`; at the prescribed top level `ρ_k=1`, as used in F6. |
| `M` / GAP-Z | Data-response kernel at `BFT_B.md:4436`; composite inverse/gap at `:4334`; missing conversion stated at `:4592` | Neither is automatically H3's full absolute response package or the matched flat inverse `M₀` in F8. |
| `Hess𝔉` versus `𝓛` | Bare Hessian at `HESSREL.md:183-193`; gauge-fixed Hessian at `:443-446` | FWD-0 and perturbation estimates cannot silently move between them (F8). |
| `S_E` versus `S_E^Z` | Explicitly distinct slices at `BFT_B.md:4332`, related at a pure gauge by `:4522` | Equal ambient coordinate dimensions do not identify the slices. |
| `c,r,a` versus `ϑ^Y,ϑ^𝔐` | Background/response decay at `NBG_A.md:305-309`, `:344`; norm weights at `HESSREL.md:155-157` | Background rates and norm weights are not interchangeable; a stale `a=1` caused F5, unequal norm weights caused F8. |
| `Z` | Critical tower in `NBG_A.md:233-243`; sibling R^ax chain in `:398`; `Z^{off}(V)` in TRANSP, `BFT_B.md:4600` | Bounds for one chain are not bounds for another without identification. |
| `C_♭` | The local, chart-at-lift and whole-class readings are explicitly separated at `NBG_A.md:92-98` | Their original PROOF/NORMS definitions and claimed consumer assignments were not independently inspected. None was identified with an inverse norm in this review. |

**Verified citation correction:** `NBG_A.md:400` attributes the quoted GAP-Z definition to **BFT_B.md line 4592**. At review time that line is the paragraph beginning **“Status: ARGUED”**, explicitly naming missing Combes–Thomas/composition estimates. The quoted **“the M half … genuinely new analytic input”** is at **line 4590**. This is a concrete source-anchor error, whether caused by drift or original miscitation.

**Read-scope record:** the additional files were `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `/Users/jonBridger/.codex/skills/review-loop/SKILL.md`. All mathematics was read from the six expressly allowed source files in search-located ranges, plus this deliverable. No PROOF.md content, snapshots, audit ledgers or check scripts were read. Therefore **every historical PROOF.md line citation remains NOT-VERIFIED**, including any claimed equality, status or decomposition depending on it. I do not certify the reported drift offsets. No git command was run and no source file was edited. The final anchor spot-check was performed at **2026-10-28 22:30:28 UTC**; source references include matching strings because these files may continue changing.

## Summary table

| Finding | Verdict | Result/correction |
|---|---|---|
| F1 NB-1 | **CONFIRMED** | Envelope identity at any twice-differentiable joint critical family; no third derivative of the branch needed. |
| F2 HR-1 | **CONFIRMED / REFUTED** | Ambient conjugacy survives; “every nonconstant noncentral gauge” is false. |
| F3 NB-3 | **REFUTED / CONFIRMED** | Insert `J_X=I−ad_X/2+…`; six chain-rule patterns and a genuine zero-derivative-leg term survive. |
| F4 N3 | **REFUTED** | Claimed equal norms give **4 versus 2** for real directions (**4 versus 2√2** for complex directions); the ratio can grow with volume. |
| F5 Exponents | **CONFIRMED / REFUTED** | **−4,−1,−8,−2** survive. Residual floor is `max(1,7−3c)`, hence **8/5** at `c=9/5`, not **1**. Soft critical dimensions **12,6** apply only with r frozen at 3; with `r=d−1` there is no upper soft critical dimension. At d=5 old soft slope is **−1**, not **0**. At c=0 **three**, not four, new slopes are positive. |
| F6 FLAT-REF | **REFUTED** | For curvature **1/m²**, every global flat comparison has some log-link difference at least **23/(96m)**; uniform O(f) is impossible on the written class. |
| F7 HESS-rel | **REFUTED** | Fixed-coordinate curvature-only estimate fails on pure gauges. Script counts/ratios remain **NOT-VERIFIED** and are not operator-norm ratios. |
| F8 Repaired route | **CONFIRMED / NOT-VERIFIED** | Matched Neumann implication is PROVEN at **q<1**; frame-local perturbation plus global patching is still GAP. |
| F9 Growth transfer | **REFUTED** | An O(k) inverse can yield **E'''=k³**, not O(k). |
| F10 Independence/counts | **REFUTED** as proofs | No mathematical count of two independent obstructions established; six project non-implications remain **NOT-VERIFIED**. |
| F11 NB-4/NB-5 | **NOT-VERIFIED** as stated | Corrected absolute response-package reduction is PROVEN; maps, norm and full chart coverage remain to be supplied. |
| F12 Gates | **NOT-VERIFIED** implementations | Formula test can fail; −8 versus −4 does not flip the negativity gate; FLAT-REF acceptance criterion is impossible globally. |
| F13 Graph | **NOT-VERIFIED** as published | Retain only the explicitly repaired implications below. |
| F14 Citation | **REFUTED** cited line | NBG_A's quoted BFT_B definition is at **4590**, not **4592**; all PROOF citations remain unverified. |

**Most dangerous remaining unverified claim:** that fixed-size frame-conjugated inverse estimates can be patched into a global, k- and T-uniform inverse on the required composite slice/source pair. The refuted global FLAT-REF shortcut cannot supply that bridge.

## Honest dependency graph — PROVEN edges only

Every arrow below is a proved implication **between explicitly stated hypotheses**. Its antecedents are not claimed established for the lattice project. `GZ(X,Y)` denotes the specifically matched composite inverse estimate `Y→X`, not the ambiguous response-symbol/gap name. `R_abs` denotes the first-response absolute kernel bounds and scale weights used in F5/F11, with the corrected logarithmic derivatives and uniform local coefficient bounds. “Throughout chart” includes existence, differentiability and the full consumer ball.

```text
Gauge covariance in exponential charts
    ──PROVEN──▶ H_{G·Z} = M_G H_Z M_G⁻¹

Flat inverse on X₀,Y₀ + covariant slice/source isometries M_G
    ──PROVEN──▶ same inverse bound on the pure-gauge transported X_G,Y_G

Uniform GZ(X,Y) over an admissible class containing Z=1
    ──PROVEN──▶ the identical matched estimate restricted to Z=1

Uniform matched inverse over a flat reference family containing 1
    ──PROVEN──▶ the matched flat inverse at 1

Matched flat-reference inverse A⁻¹:Y→X, ||A⁻¹||≤M₀
  AND fully aligned gauge-fixed perturbation E:X→Y
  AND q=||A⁻¹E||<1 uniformly
    ──PROVEN──▶ ||(A+E)⁻¹||≤M₀/(1−q)
                  [global only if these are global hypotheses;
                   frame-local hypotheses give a frame-local conclusion]

Uniform inverse ||A⁻¹||≤M
  AND uniform weighted commutator estimate ||WAW⁻¹−A||≤η
  AND Mη<1, with matching spaces and admissible weights W
    ──PROVEN──▶ ||WA⁻¹W⁻¹||≤M/(1−Mη)

Twice-differentiable joint critical family F_A(a(B),B)=0, F∈C³
    ──PROVEN──▶ D³E = D³F[ζ·,ζ·,ζ·]

Joint critical family throughout chart
  AND corrected local coefficient bounds
  AND R_abs at (c,r,a)=(2,3,1) throughout chart
    ──PROVEN──▶ uniform coefficient-row cubic bound
    ──PROVEN──▶ uniform consumer Hessian-Lipschitz bound

Holomorphic Hessian uniformly bounded by S in N₀
  AND uniform complex interior radius r>0 throughout chart
    ──PROVEN──▶ consumer Hessian-Lipschitz bound ≤S/r
```
