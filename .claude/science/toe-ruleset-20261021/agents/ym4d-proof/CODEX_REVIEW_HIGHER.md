# PRE-STATED

Independent hostile review of `HIGHER55.md`, restricted to the requested local source packet. This section is written before reading the detailed derivations or executing checks. Prior exposure: the user's target description, grep-selected headings and claim lines of HIGHER55 and the earlier review reports, plus the repository methodology. No git commands will be run. Only this report will be written. Local file hashes, locating strings and line numbers will identify the reviewed material; no git revision or unavailable model metadata will be asserted.

Target: the exact all-orders decomposition of `S_full = Hx* − NB` and the bounds sufficient for critical-point TR∞ and CC-CRIT∞ at the trivial background, weight parameter zero, uniformly in k, T and gauge Γ, conditional on the explicitly imported linear analytic inputs.

Pre-stated failure criteria:

1. **Analyticity / LA:** a local analytic inverse with a radius or coefficient bound that depends on k, T or level; an untreated torus identification (especially `T_(l+1)=1`); a norm/coordinate conversion that grows with volume; or an invalid extraction of `|ρ−r| ≤ C ε_l³ η²`. Finite Taylor checks cannot certify analytic tails.
2. **Quadratic average / BA-4:** a missing quadratic term in the maximizer log, a mismatch between the actual four-dimensional S4′ words and the tested words, or a nonzero constant-direction averaged BCH₂ term. The cancellation check must have a non-vacuous control. Independent algebra, not a rerun alone, must establish the general identity.
3. **Exact plain remainder:** a chain-rule term absent from FAC/HS, or an all-orders term whose coarse-scaled size is only O(η³) per level without a summation mechanism. In particular inspect the own-level derivative, next-level derivative, residual remainders, Wilson remainder and every Jacobian factor.
4. **SG and quadratic matching:** literal residual-decay inheritance must retain the additive `ρ−r` defect; check signs, κ factors and the CR-1/BA-6 commutator cancellation independently.
5. **Closure / disclosure:** verify that the exact source, not merely its quadratic truncation, enters criticality and composite co-closedness; inspect the failed hg55_3 control and hg55_4 replacement without retroactively upgrading the failed test.

Verdicts are **CONFIRMED** (within stated premises), **NOT-VERIFIED** (identified proof gap or insufficient evidence), and **REFUTED** (matched contradiction/counterexample), each tied to a file and locating string. All executed mathematical arithmetic will be exact integers/rationals or symbolic exact arithmetic. Test families will not be promoted to uniform theorems. The completed report will end with exactly what may be banked.

Additional checks fixed before execution, after inspecting the derivations and author scripts:

- Reproduce hg55_1–4 without changing the scripts or creating output files; require exact output agreement with the recorded outputs, and retain hg55_3's nonzero exit / overall FAIL.
- Independently enumerate the six formal degree-two Lie brackets in four dimensions, for all paired axial words at L=3 and L=5. Require the per-word identity `B₂=L[D,A_μ]`, vanishing block average, and nonzero one-y control. Inspect cover-to-torus link identification at fine periods L and 2L; the latter must be injective on the local link set.
- Test the literal all-rows version of `π_l(δj_l)≤C ε_l η³` in HIGHER55 §5 using direction-constant noncommuting fields `x_l=ε_l t A`, `x_(l+1)=Lx_l`, hence r=0. Compute the Wilson cubic coefficient with exact matrices. A nonzero ε_0³t³ own coefficient refutes that stronger statement at level zero as k grows, while leaving the single-level O(η³) sum bound possible. This is an on-ball test, not a claim that these configurations are critical.

## Disposition

**CONFIRMED — the higher-order exact-source obligation is discharged as a qualitative, uniform estimate.** HIGHER55's FAC and HS supply the sufficient repair specified in `CODEX_REVIEW_TR.md`, `One sufficient repair would be an exact decomposition`, and used by `CODEX_REVIEW_TOPCC.md`, final item 4. Consequently TR∞ and CC-CRIT∞ hold as implications of the named linear inputs, with the precise scope below. This conclusion rests on the analytic and algebraic arguments, not the finite checks.

**REFUTED — the stronger assertion that every higher-order plain row, including the Wilson contribution at l=0, has `π_l≤C ε_l η³`.** Its literal occurrence is `HIGHER55.md:324`, `every cubic-and-higher slot decays geometrically`, and the table row `δj_l (degree ≥ 3)` at line 335. HS-b itself correctly writes `δj^{soft}_l`. An exact on-ball counterexample to the broader wording is given below. The correct full statement is geometric decay for the soft remainder, plus a single Wilson contribution bounded by Cη³. That suffices for the requested theorem.

Two local bookkeeping corrections are also required: §6 must add the full Wilson row to the **soft** remainder, not to a remainder already containing the Wilson remainder; §3.4 must distinguish E from κE and must not advertise `C_E≤16` as established by the displayed estimates. Neither correction requires a new nonlinear lemma. The report proves the corrected assembly explicitly.

Throughout, N and odd L≥3 are fixed, d=4, `0<κ_-≤κ_l≤κ_+`, `ε_l=L^{−(k−l)}`, and the weight parameter is zero. To avoid confusing that weight with depth, write `h=k−1−l`. Constants may depend on N, L, κ_± and the fixed exponents `0<α<θ<1`, but not on k, T, l or admissible gauge fixing Γ. Smallness means a fixed sufficiently small analytic neighborhood, with `||x||_𝔐≤η` and `||B_k||_D≤η`. Numerical values for the analytic radius and final smallness window are not supplied.

## 1. Analyticity, including the one-site coarse torus

**CONFIRMED.** Locations: `HIGHER55.md:166`, `Lemma AN`; line 187, `Lemma CE`; `LINEAR_PACKAGE.md`, `1.2 The averaging S4'`; `PROOF.md`, `Lemma NA-alg` / `Stationarity`.

The relevant dimension is the number of local link coordinates used by one density, not the number of links on the whole torus. A contour has at most `p_L=5L−4` letters. For a fixed coarse link its support lies in two adjacent L-blocks. Its extent in the longitudinal direction is less than 2L; transverse extents are less than L. Thus a fine torus of side `T_(l+1)L≥2L` introduces no identification of different local links. Translation across a fundamental-domain seam is harmless. The symbols `24·81` in §3 are the L=3 specialization; for general L the number of words is `24L⁴`, still fixed independently of k and T.

When `T_(l+1)=1`, the local density is precisely the cover density composed with coordinate repetition modulo L. This linear map ι has coordinate-sup norm one: repeating a coordinate does not enlarge a polydisc. Repeated occurrences are retained with their multiplicities. Derivatives with respect to an identified link vary all its occurrences, which is still an admissible bounded direction for Cauchy estimates. A link meets only a bounded local collection of coarse-link supports; the overlap constant n_c therefore remains independent of k and T. There is no division by the number of distinct torus sites.

Independent four-dimensional enumeration found, for each direction, 459 distinct cover links at L=3, identified to 243 at fine period 3 and still 459 at period 6. At L=5 the corresponding counts are 4125, 2125 and 4125. These counts check the edge case; the finite-support/coordinate-repetition argument proves the uniform statement for every odd L and every torus size.

The implicit equation is `Π(e^(−X)M(x))=0`. Its derivative in the real su(N) coordinate X at `(X,x)=(0,0)` is `−id`. The real analytic implicit-function theorem supplies a local analytic X(x), agreeing with the NA-alg maximizer by uniqueness. Complexification is in the **real Lie-algebra coordinates**: the complexified real-linear Π and the real analytic scalar functions have holomorphic extensions. One must not interpret this as retaining complex conjugation of those complexified coordinates. Logarithms, exponentials, the soft density and Wilson maps then admit a common smaller polydisc. Shrinking it if necessary keeps the real logarithms in the traceless local branch required by corrected NA-alg(b).

Taking a minimum radius and maximum local bound over these finitely many functions/types gives R>0 and S<∞ independently of k and T. Coordinate-copying could alternatively use the generic function's neighborhood directly. Applying Cauchy's formula to `ζ↦f(ζz/||z||∞)` bounds each homogeneous Taylor polynomial without a combinatorial factor depending on global dimension. Directional differentiation and the vanishing factors in ŵ then give the needed derivative bounds. Uncomputed R and S are not a gap in this existence-of-uniform-constants claim; they remain an unresolved quantitative feasibility input.

**NOT-VERIFIED — the advertised common numerical bound `C_E≤16` from the written §3.4 argument.** Location: `HIGHER55.md:208–209`, `Consequence for SG's E_l`. The displayed estimate retains `(92/5)y²`, and no argument there lowers that coefficient to 16. Moreover, `KFACTOR_OFF55.md`, `∇_x Σ_cσ_c = κ_l R_l^TΨ_l + κ_l E_l(x)`, defines E with κ factored out; HIGHER55's following E-bound inserts κ_+ again. Read those bounds as bounds for the actual rows κE, or remove the extra κ from the E-bound. With that normalization, a common constant 80 safely dominates the displayed bounds, including conversion `y≤2p_Ls_l`. The qualitative LA-1 estimate is **CONFIRMED**. This numerical/notation issue does not enter the independent FAC proof.

## 2. The maximizer's quadratic part and the S4′ cancellation

**CONFIRMED.** Locations: `HIGHER55.md:212`, `Lemma C2`; `BFT_A.md`, `3.4 BA-4 (CEN2)` and `3.5 BA-5`; `checks/hg55_1.py`, `contour_letters`, `A1`, `A5`.

Here is a direct derivation from stationarity, independent of the old polar-factor description. Scale the local letters by t and write

    M = 1 + t M₁ + t² M₂ + O(t³),
    X₀ = t X₁ + t² X₂ + O(t³).

The order-one equation gives `X₁=M₁=Qx`. At order two,

    X₂ = Π(M₂ − M₁²/2).

For each word with first log coefficient Y₁ and second log coefficient B₂,

    M₂ = avg(B₂ + Y₁²/2).

Both `M₁²` and `Y₁²` are Hermitian, so Π kills them. Therefore `X₂=avg B₂` and `â₂=avg B₂` exactly, for general N. There is no missing determinant-phase quadratic contribution.

For direction-constant letters A_ν, the paired word is exactly

    T_y^σ(t) = w_y^σ(t) exp(Lt A_μ) w_y^σ(t)^(−1).

If `log w=tD+O(t²)`, `D=Σ_ν(y−c_X)_ν A_ν`, its log is

    log T = Lt A_μ + Lt²[D,A_μ] + O(t³).

This proves `B₂=L[D,A_μ]` for each word, for every order σ. Centering of the odd-L block gives `avg_y D=0`. The y-average already cancels the quadratic term at each fixed σ. Averaging orders does not substitute for the y-average.

The independent check used the six **formal** brackets `[A_i,A_j]`, not a random representation of su(2). All 7776 words for L=3 and all 60000 words for L=5 satisfied the per-word identity and the linear identity `Σ letters=LA_μ`. Every full block average vanished. Fixing `y=c_X+e_ν`, ν≠μ, left the nonzero formal coefficient `L[A_ν,A_μ]`, providing the control. hg55_1 uses the correct paired return path and reproduced its original A1–A6 outcomes, including A5 firing. Its ℓ¹ calculation tests that norm's stated commutator constant; it is not a numerical proof of the HS estimate.

For a nonconstant field choose direction-constant reference values and deviations bounded by δ. The pairwise commutator estimate gives

    |â₂| ≤ p_L(p_L−1)δ(2|x̄|+δ)/2.

The ball supplies `δ≤5L ε_l²η`, `|x̄|≤ε_lη` and `Lε_l≤1`. Hence `|â₂|≤(35/2)Lp_L² ε_l³η²`. The local analytic tail is `O(ε_l³η³)`, so

    |â| ≤ C ε_l³η²,        |ŵ|=|r+â| ≤ C ε_l²η.

This improvement is a bound on â evaluated on the ball. It is **not** an improved bound on its derivative in an arbitrary individual-link direction. HS correctly uses only `|Dâ|≤C ε_lη` for that derivative.

Finally, `β(X,w)=log(e^(−X+w)e^X)−w` vanishes on both coordinate axes. Its mixed derivative is uniformly bounded on a smaller local polydisc. Thus `|β(X,w)|≤C|X||w|`. With `X=X₀=O(ε_lη)` and `w=ŵ=O(ε_l²η)`, this proves

    |ρ−r| ≤ |â|+|β(X₀,ŵ)| ≤ C ε_l³η².

**CONFIRMED — LA-2**, at `HIGHER55.md:226`. The extra ε is proved by centering plus the gradient component of 𝔐; analyticity alone would not improve a generic quadratic term.

## 3. Exact slots and the complete remainder list

**CONFIRMED.** Locations: `HIGHER55.md:245`, `Lemma NC3`; line 260, `Lemma FAC`; lines 272–303, `Proposition HS` and `HS-3`.

Put `G=e^(−X₀)M`. Stationarity gives `ΠG=0`, and `G=1+O(x²)`. For real small arguments, `ρ∈su(N)`, so `Re tr(ρG)=0` exactly. In the ŵ-chart,

    ρ = ŵ + [ŵ,X₀]/2 + O(3).

The possible cubic cross term in `−Re tr(ρ²)/2` is zero by cyclicity, and `Re tr(ŵ³)=0`. Since G has no linear term, it creates no other cubic term. Consequently

    φ̃(x,ŵ)=|ŵ|²/2+φ̃₄(x,ŵ),
    φ̃₄(x,0)=0,      ∂_ŵφ̃₄(x,0)=0,

with φ̃₄ starting at total degree four. The normalization is φ̂=Nφ; the factor 1/2 is correct for the HS norm. hg55_2's factor 2 in its coordinate covectors comes from its basis having squared HS norm 2, not from a different density.

Write `Ê=∂_ŵφ̃₄`, `Ω̂=ŵ+Ê`. Local analyticity and the two ŵ-vanishings imply

    |Ê| ≤ C (|x|+|ŵ|)² |ŵ|,
    |∂_xφ̃| at fixed ŵ ≤ C (|x|+|ŵ|)|ŵ|².

The full chain rule, for u_k=0, is

    DΦ_c[u] = <Ω̂_c,Q_lu_l−u_(l+1)>
              + <(Dâ_c)^TΩ̂_c + ∂_xφ̃_c,u_l>.

Subtracting this nonlinear gradient from the quadratic gradient gives the exact source slots

    s_l = −κ_l(â_l+Ê_l),
    j_l^soft = −κ_l Σ_c [(D_bâ_c)^T(r_c+â_c+Ê_c)+∂_(x_b)φ̃_c].

There is no omitted next-level plain row: all dependence on x_(l+1) is through `ŵ=X₀−x_(l+1)`, and its derivative is −id. There is no positive-level divergence slot. Differentiation of the maximizer and of the normalizing/envelope term is already included in this exact chain rule. There is no further derivative of S_full: the source is frozen when applying linear response.

Subtracting the homogeneous quadratic slots gives **exactly**

    δs_l = −κ_l(â_(≥3)+Ê),
    δj_l^soft = −κ_l Σ_c [
        (Dâ−Dâ₂)^T r
        + (Dâ)^T(â+Ê)
        + ∂_xφ̃ ].

All derivative multiplicities, including periodic link repetitions, are included in the local functions. The c-sum has bounded overlap. The complete soft list has these own-unit bounds:

| Term | Bound on the 𝔐-ball | Reason |
|---|---|---|
| `(Dâ−Dâ₂)^T r` | `C ε_l⁴η³` | degree-two derivative tail times `r=O(ε_l²η)` |
| `(Dâ)^T â` | `C ε_l⁴η³` | `Dâ=O(ε_lη)` and the proved centered `â=O(ε_l³η²)` |
| `(Dâ)^T Ê` | `C ε_l⁵η⁴` | `Ê=O(ε_l⁴η³)` |
| `∂_xφ̃` at fixed ŵ | `C ε_l⁵η³` | a quadratic ŵ factor and one further small factor |
| `â_(≥3)+Ê` | `C ε_l³η³` | analytic cubic tail; Ê is smaller |

There is no unpriced soft term of own size `ε_l³η³` in the plain slot. Only the **quadratic** row `−R_l^B=−κ_l(Dâ₂)^T r` has the marginal own bound `C ε_l³η²` before critical-point transport.

The Wilson list must be kept separate. With `X=dx_0+q` and `u_W=∇𝒲(X)−X`, its exact slots are

    G_0=−q−u_W,       j_0^W=−Σ_p(Dq_p)^T(dx_0+q_p+u_(W,p)).

Writing q₂ for the quadratic Taylor polynomial gives the complete Wilson remainder

    δG_0=−q_(≥3)−u_W,
    δj_0^W=−Σ_p[(Dq−Dq₂)^T dx_0 + (Dq)^T q + (Dq)^T u_W].

These three plain terms are respectively bounded by `C ε_0⁴η³`, `C ε_0³η³`, and `C ε_0⁷η⁴` in own units. In particular `(Dq₂)^Tq₂` genuinely has only the second rate. Each link meets six plaquettes. Thus `π_0(δj_0^W)≤C_Wη³`, with no required ε_0 improvement.

For the divergence slot the local degree-three tail bound is `O(ε_0³η³)`. Translating the four links through coarse distance δ changes their values by at most `4δε_0η`; the derivative of that tail is `O(ε_0²η²)`. Multiplication by ε_0^(−2), followed by the Hölder quotient, gives

    ||δG_0^c||∞+[δG_0^c]_α ≤ C_G ε_0η³.

More explicitly the difference is `C ε_0η³ δ`, and `δ≤δ^α` for 0<δ≤1. Campanato oscillation is bounded by this pointwise Hölder seminorm. This extends the argument of `BFT_A.md`, `28.6 Corollary WR (a)`, to the actual Wilson density, including u_W.

The coarse conversions and sums are now exact:

    ||δs_l^c||∞ ≤ C_s L^(−3)L^(−2h)η³,
    π_l(δj_l^soft) ≤ C_J ε_lη³,
    Σ_(l<k) ε_l = (1−L^(−k))/(L−1) ≤ 1/(L−1),
    Σ_(l<k) π_l(δj_l) ≤ [C_J/(L−1)+C_W]η³.

Also `||δs||_R≤C_s L^(θ−3)η³`, since the remaining factor is `L^(−(1−θ)h)≤1`. These bounds prove `Ñ_Σ(ΔS)≤Cη³` for the explicit slot representation. They do not assert that ΔS separately belongs to the admissible composite-co-closed source class. The full-source transport error budget is exactly bounded by

    E_i ≤ L^(−2h)η³ [2C_s^(3)+C_f C_j^(3)],
    C_f=1+2d/(1−L^(−3)).

This is the sufficient repair in the earlier TR review, including its missing plain-current sum.

## 4. SG precision and the commutator cancellation

**CONFIRMED — the exact SG identity and the qualified decay consequence.** Locations: `KFACTOR_OFF55.md:133`, `Lemma SG`; line 168, `inherits whatever level decay the residual has`; `HIGHER55.md:102–127`, `SG-a` through `SG-d`.

Envelope differentiation gives `δ Re tr(W₀^(−1)M)=Re tr(W₀^(−1)δM)`. Using `V^(−1)=(1+Θ)W₀^(−1)` and `G=H+iθ1`, the remaining next-level derivative splits into `Re tr(ZΘG)+Re tr(ZG)`. The last term vanishes because Z is traceless anti-Hermitian. Thus

    δσ=κ[−Re tr(ΘW₀^(−1)δM)+Re tr(ZΘG)]

is exact. Projection gives `Ψ=Π(−Θ*)=ρ+O(ρ³)`. The derivative in LA-1 must mean `W₀^(−1)D_bM` with W₀ frozen in that coefficient; it is not `D_b(W₀^(−1)M)`. HIGHER55 correctly identifies this distinction.

The norm consequence has an additive defect. At the lower level it reads, with constants absorbing local incidence,

    π_l(κE_l|_l) ≤ C ε_l^(−2)η |r_l| + C ε_lη³.

This uses `|Θ|≤2|ρ|≤2|r|+C ε_l³η²`. The upper-level component has the analogous r-dependent contribution plus a summable defect, after using its own coarse units and `s_(l+1)+p_L²s_l²`. Thus SG does not say that the soft plain rows vanish when the **linear** residual r vanishes, nor that arbitrarily fast r-decay eliminates the additive defect. LA-2 prices that defect. The unqualified inheritance slogan is not the theorem being banked. The exact factorization and this qualified bound are.

**CONFIRMED — exact quadratic commutator cancellation.** Locations: `HIGHER55.md:290`, `HS-d`; `BFT_A.md:1010`, `13.5 Lemma CR-1`; `BFT_A.md`, `3.6 BA-6`.

For the positive nonlinear gradient,

    ρ₂=Ȳ₂−[x_(l+1),Q_lx_l]/2,
    s^C=κ[x_(l+1),r_l]/2,
    Q_lx_l=r_l+x_(l+1).

Hence `κρ₂+s^C=κȲ₂` identically. The term involving `[u_(l+1),r]` in CR-1 pairs to zero with r by ad-invariance; no next-level plain contribution survives at this order. For the source convention actually under review, `𝔑^0=Hx−NB−∇F`, the resulting residual slot is **−κȲ₂**. HIGHER55's S₂ definition has that correct sign; its phrase `S_2's residual slot κ_lȲ` in HS-d must be read as the positive-gradient comparison before the common sign reversal.

## 5. Counterexample to the blanket per-level decay claim

**REFUTED in its literal all-rows reading.** Location: `HIGHER55.md:335`, `δj_l (degree ≥ 3)`; compare its correct restriction to soft rows in `HS-b` and its separate Wilson bound at line 236.

Take N=3 and the rational real skew matrices

    A=(E₁₂−E₂₁)/2,       B=(E₂₃−E₃₂)/2,
    C=[A,B]=(E₁₃−E₃₁)/4.

At every level set the direction-0 field to `ε_l t A`, the direction-1 field to `ε_l t B`, and the other directions to zero, with matching terminal datum. These fields are constant in position, `Q_lx_l=Lx_l=x_(l+1)`, and r=0. Their gradients vanish, and `|A|²=|B|²=1/2`, so `||x||_𝔐≤t` and `||B_k||_D≤t`. This works for arbitrary depth and torus size. Set η=t and let t decrease inside the fixed small neighborhood.

For a (0,1) plaquette, `q₂=(ε_0t)²C` and dx_0=0. Translation invariance identifies the per-link Wilson current with the derivative of the action density under a uniform variation in that direction. The degree-three source coefficient in direction 0 is

    (δj_0^W)₍₃₎ = −(ε_0t)³[B,[A,B]]
                   = −(ε_0t)³ A/4.

Here `|A/4|²=1/32`. Independently multiplying rational matrix exponential series gave the Wilson density's degree-four coefficient `1/16` and its derivative along A's degree-three coefficient `1/8`, agreeing with this current. The soft plain current has no degree-three term on this family: r=0 and â₂=0 make every candidate in the exact soft list vanish at that degree.

Therefore, after the coarse plain conversion, the squared norm of the t³ coefficient of δj_0 is exactly `1/32`, independently of k. A bound `π_0(δj_0)≤C ε_0t³` for every small t would imply `1/32≤C²L^(−2k)` for all k, impossible for a fixed C. This is an exact Taylor-coefficient contradiction, not a floating-point large-k experiment.

It refutes only the stronger on-ball per-level assertion. The field is not asserted to be critical. The single-level estimate `π_0(δj_0^W)≤Cη³` remains valid and is all the summation proof needs. Correct §5's row label to `δj_l^soft`, and state the Wilson exception explicitly.

## 6. Transport and the nonlinear critical-point implication

**CONFIRMED as implications, with the explicit bookkeeping just below.** Locations: `HIGHER55.md:357`, `Theorem TR∞`; line 379, `Corollary CC-CRIT∞`; `CODEX_REVIEW_TR.md`, §§1–4 and final items 1–2; `CODEX_REVIEW_TOPCC.md`, final items 3–4.

At an actual critical point, the full source is exactly `S_full=Hx*−NB`. It is composite-co-closed in the pinned sense required by the linear theory. Neither S₂ nor ΔS is assumed independently admissible, and no (CC-0) assertion is restored.

There is a notation collision in `HIGHER55.md:370`, `per level π_l(j_l)`, and at line 374: its δj was defined in §4.3 to include δj_0^W, whereas j_0^W there denotes the full Wilson row. The triangle-inequality decomposition to use is

    j_l = −R_l^B + δj_l^soft + 1_(l=0)j_0^W.

Accordingly replace δj by δj^soft in those two assembly steps. One may keep the printed upper constants C_Δ and C_j^(3), since they are larger than the soft-only constants. This fixes the step without changing the stated upper K_Σ^∞. Alternatively use the quadratic Wilson row together with the full δj. Do not mix those two decompositions.

The now-proved full-source estimates give `||s_i^c||≤A_s L^(−2h)η²`, a per-level bound on the **whole** plain source, and no positive-level divergence slots. Applying the previously checked RT-cc/TC/FT argument to that exact source gives

    ||r_i^c||∞ ≤ κ_-^(−1)L^(−2h)η[κ_++(2A_s+hA_j)η].

Substitution into the banked local BCH₂ row estimate gives an upper bound of the form `C L^(−h)(1+C'η+hC''η)η²`. At h=0 the original ball bound suffices. The sums are

    Σ_(h≥0)L^(−h)=L/(L−1),
    Σ_(h≥0)hL^(−h)=L/(L−1)².

Thus the quadratic row sum is uniform. Add the proved geometric soft remainder and the full, single-level Wilson row. No absorption and no condition `kη≲1` occur. The FT convolution contributes only `C_f`; at d=4, L=3 it is exactly `121/13`. The other sum constants at L=3 are `3/2`, `3/4` and `1/(L−1)=1/2`. Taking η_H in coefficient bounds fixes constants for the whole small ball.

Together with the full Wilson divergence bound and the full residual bound, this proves

    Ñ_Σ(S_full) ≤ C_*η².

The earlier CC-INV/TOP-cc implication then applies to the homogeneous-data response `x_rows=x*−x(B_k)` and controls its complete invariant curvature tower, Hölder outputs and all residuals, including the top one, uniformly in k, T and Γ. The inputs remain those named in HIGHER55 §6 (I1)–(I3) and `CODEX_REVIEW_TOPCC.md`, final item 3: the reviewed linear transport/row estimates and lane-A/package response estimates with their corrected constants. This review does not re-prove those global linear analytic inputs.

This is the full nonlinear **critical-point** COF-crit/NCE(i)/CC-CRIT conclusion in its composite-co-closed, trivial-background, weight-zero, invariant-output scope. The old proofs in `BFT_B.md`, `35.6 Corollary COF-crit` and `36.5 Theorem NCE (i)`, that claim criticality implies (CC-0), remain invalid. A correct new route to the conclusion does not rehabilitate that assertion.

## 7. Check record and disclosure

**CONFIRMED — the reported check outcomes, including the failure.** Locations: `HIGHER55.md:425`, `Check record`; line 434, `hg55_3's failure, explained`; the four `checks/hg55_*_criteria.md` files and corresponding scripts/outputs.

The source scripts were inspected in ranges before execution. The shared arithmetic/model code of hg55_3 and hg55_4, lines 7–298, is byte-identical. All four scripts were parsed: no float or Python complex literals occur. The scientific arithmetic uses integers and Fractions, including the Gaussian-rational pairs. They were executed unchanged with `python3 -B`, capturing output in memory; no check files, logs or bytecode were written.

| Check | Process exit | Reproduced outcome | Match to saved stdout |
|---|---:|---|---|
| hg55_1 | 0 | A1–A4/A6 PASS; A5 FIRES; overall PASS | byte for byte |
| hg55_2 | 0 | B1–B3/B5 PASS; B4 FIRES; overall PASS | byte for byte |
| hg55_3 | 1 | C1–C3 PASS; C4 FIRES; C5 DOES NOT FIRE; overall FAIL | byte for byte |
| hg55_4 | 0 | D1–D3 PASS; D4 FIRES in 16/16 comparisons; overall PASS | byte for byte |

All four stderr streams were empty. hg55_1 reproduced the exact maximum ratio `674438/80310285`. hg55_2's one-contour control reproduced plain ε³ coefficients 1152 and 576. hg55_4 reproduced the ε³ mismatch `34021/2187` versus `12220/2187` in its first control comparison. Its Hermitian second-order G part is nonscalar: subtracting its scalar trace part gave exact squared HS norms `3690187/23328` and `3769135/23328` in the two samples.

The failure explanation is sound at the order claimed. In hg55_3's C1 family all words have the same first log coefficient, so their spread Δ is O(ε²). The anti-Hermitian traceless stationarity defect of using exp(Ȳ) starts at order ε⁵. A control based on it cannot discriminate through ε⁴. In the displayed expansion in HIGHER55 §8 and hg55_4's criteria, write `Π(avg Δ³)/6` for the cubic-moment term (or put Π around the whole right side); at N≥3 that trace projection must not be silently omitted. It does not change this order argument. hg55_4 deliberately changes the family to one with spread O(ε), where the defect is visible at ε³.

The report correctly keeps hg55_3 overall FAIL and uses its C3/C4 pair only as a disclosed NC3 subcheck, not as support from a successful SG control. hg55_4 has separate criteria that explicitly name the failed control and motivation. Its script's opening docstring still says hg55_3, a stale label; the executable D1–D4 gates match hg55_4's criteria. **NOT-VERIFIED — independent authentication of the claimed historical creation/run timestamps or same-second heredoc ordering.** The files disclose that history, but this review did not inspect an independent execution transcript. The mathematical outputs and present criteria agree; no timestamp claim is needed for the proof.

Finite checks cover the stated ranks, contours and truncation orders only. Uniform analytic tails and all k,T are established by the arguments above, not by these tests. The independent formal-bracket enumeration and rational Wilson counterexample were executed from in-memory heredocs; their exact constructions and outputs are recorded in §§2 and 5.

## 8. Local source identities

All paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof`. These identify local content, not a git revision or a landed/audited status. No git command was run, and only this report was written.

The final source check found HIGHER55 and the other listed mathematical/review sources unchanged except for PROOF.md, whose whole-file hash changed concurrently. I re-read its cited NA-alg statement and proof: the stationarity equation, corrected local-log hypothesis and bounds used here remain as reviewed; the section moved to lines 3215–3250. Both whole-file hashes and the re-read passage hash are recorded below. This review makes no claim about unrelated concurrent PROOF.md edits.

```text
HIGHER55.md         f6c3a48e9f6699af7022d7b817ef4e0ff1f65567e88cedba9c262d26a624ee45
KFACTOR_OFF55.md    6a47b6543bfefa31f8eb103ff057c4d64b38a97a48f35a195caa70367a9c3159
KFACTOR_O55.md      24ff96d127a4298805377fd450d1905729064f8599385e2b41e508f206ce6881
CODEX_REVIEW_TR.md  4899db7f4badeaaea98fd586948d3cffc094710883dab3910f8c49d80502ff37
CODEX_REVIEW_TOPCC.md 68bc5d15520d1cc12e25ff0aef313f75c8bcf00965fce34821c1ed0afbb313d6
BFT_A.md            8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0
BFT_B.md            b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6
PROOF.md, first hash 02beb7dff29d1e23ae4cd8e890480b4d52d28adb55af457a78c4f9ebca309efd
PROOF.md, final hash f8337f4a90d24bbc74e1e300dbaf2c4ac59596c4e8506d2dd986d7ea6f8b587c
PROOF.md, lines 3215–3250 (sed output)
                    f7b709739edd89484ec5d67e8e601e66e45aad91047fac94002cf9bc9cd8c50d
COFUN_CC.md         2a399a7dce1de8f0a4e9b4dfb81d9f0595e8eb4d8b294e2764b1b518d98ce035
LINEAR_PACKAGE.md   0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad

hg55_1.py           b8db7399363cfc78e57f59a134fdd92c8a0e619f0fa3fb24c6b375d65504c347
hg55_1 stdout       6341c06a3b6489853d68b13e9a2888a3b0be4b194baa88149f6ac8862199d762
hg55_2.py           6f0ae24a3eab20b7a7193165597108b14b4d16bbaa7d0687872e440bf76fefb1
hg55_2 stdout       cb8b7b94d91721ab36a51c25b9e8a7d0281d70378773d091c4b276d3dccaf45f
hg55_3.py           dcc94441739dfffd53bdeb64268487860d97a9213e0355370fe061a5d5138bf5
hg55_3 stdout       d6e2d2c9577db139e99a8479584e289de10e1033477c044cce469947f242ec3a
hg55_4.py           71ea2984518375eb42b67cc93e2ae50b47c9557410a3c21102c1e377fe060d4d
hg55_4 stdout       6f85c3ebe4f4da80164019cc07a811adec29708c6df125d74d82f740372ec135
```

## Exactly what may be banked

1. **CONFIRMED — local all-orders inputs.** Bank the existence of k-, T- and level-independent analytic constants, including the `T_(l+1)=1` identification; `â₂=avg B₂`; the paired S4′ centering cancellation; `|ρ−r|≤C ε_l³η²`; NC3; and the exact, correctly signed FAC representation. Locations: `HIGHER55.md`, `Lemma AN`, `Lemma C2`, `(LA-2)`, `Lemma NC3`, `Lemma FAC`. Do not bank numerical values for R, S or the final feasibility window, nor the unsubstantiated common `C_E≤16`.

2. **CONFIRMED — the precise higher-order repair.** Bank `δG_l=0` for l≥1, `||δs_i^c||≤C_s^(3)L^(−2(k−1−i))η³`, `Σ_lπ_l(δj_l)≤C_j^(3)η³`, and the level-zero sup/Hölder divergence bound. Bank the stronger `π_l(δj_l^soft)≤C ε_lη³` for the soft rows. Locations: `HIGHER55.md`, `HS-a`, `HS-b`, `HS-c`, with the full Wilson exception explicitly retained. The blanket extension to the full δj_0 is **REFUTED**, by §5's rational on-ball witness.

3. **CONFIRMED — SG and the quadratic matching with their precise meanings.** Bank the exact SG identity, decay up to the additive ρ−r defect, and `κρ₂+s^C=κȲ₂` for the positive gradient, hence `s₂=−κȲ₂` for this source. Locations: `KFACTOR_OFF55.md`, `Lemma SG`; `HIGHER55.md`, `SG-c`, `HS-d`; `BFT_A.md`, `Lemma CR-1`. Pure inheritance without the additive defect is not the banked statement.

4. **CONFIRMED — full nonlinear critical-point TR∞ and CC-CRIT∞ as implications.** With the named accepted linear inputs, fixed N,L,κ_± and `0<α<θ<1`, an actual critical point in the stated 𝔐/data ball at trivial background and weight zero has `Ñ_Σ(S_full)≤C_*η²`, uniformly in k≥1, T≥1 and admissible Γ. Its homogeneous-data linear response has the full invariant curvature/residual estimate, including the top residual. Locations: `HIGHER55.md`, `Theorem TR∞`, `Corollary CC-CRIT∞`, using §6's corrected Wilson bookkeeping; `CODEX_REVIEW_TOPCC.md`, final items 3–4. The specific higher-order obligation in the earlier TR/TOPCC reviews may therefore be removed in this scope. (CC-0) remains refuted.

5. **CONFIRMED — the disclosed finite evidence, in its finite scope.** Bank the reproduced hg55_1/2/4 PASS outcomes, hg55_3 overall FAIL with its non-firing control, and the separately discriminating C3/C4 NC3 subcheck. Locations: the four check criteria/scripts/outputs and `HIGHER55.md`, `Check record`. **NOT-VERIFIED by this packet:** numerical analytic feasibility, HS-Lip/off-critical contraction, existence of the assumed critical point, gauge-variant field estimates, nontrivial-background transfer, the general positive-weight assembly, or a constructive four-dimensional Yang–Mills theorem. Locations: `HIGHER55.md`, `What is still missing`, and `CODEX_REVIEW_TOPCC.md`, final item 5.
