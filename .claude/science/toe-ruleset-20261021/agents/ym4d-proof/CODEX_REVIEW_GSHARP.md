## PRE-STATED

Independent hostile review of `GSHARP55.md`, requested 2026-10-28. This is a source-and-mathematics review, not an audit-status change. No git operations. Only this file may be written. All calculations will be symbolic or exact rational/integer arithmetic.

Prior exposure: the user supplied the six target claims; I inspected the workflow, review procedure, target headings/locating strings, and the beginning of the target before writing this section. I have not yet independently derived the load-bearing reconstruction or optimization results. The author's and earlier reviewers' verdicts are not evidence of those derivations.

Acceptance/falsification contract, fixed before the mathematical checks:

1. Reconstruct the definitions of the composite gauge action, `S_E`, the field norm, invariant norm, and residual Hölder term. Independently derive EP-opt from the quadratic form and kernel, and EP-rec from the actual local projection and root/curvature data. A hidden inverse bound, missing zero mode, scale-dependent constant, unjustified regularity estimate, or mismatch of gauge or source classes blocks confirmation.
2. For GF-E, verify that CC-INV and RHT-cc have matching quantifiers and source norms and actually control every term of EP-rec, including the top residual. For GF-E′, match RTARGET's source norm and exponent domain, not merely an equivalent-looking label. State any necessary narrowing explicitly.
3. Identify the exact alias object. Test the claimed strip by an explicit holomorphic continuation and denominator estimate, separating analyticity of factors, nonvanishing/inversion, and summability of an alias sum. An unresolved inverse or sum cannot be dismissed merely because individual factors are analytic.
4. Check GF-DEP as an operator family: valid gauge fixing on the same space, fixed source, actual inverse response, nonzero growing field component, and identical invariant outputs. Distinguish independence of all gauge fixings from existence of a controlled slice and from the orbit seminorm.
5. Trace all displacements in the weighted reconstruction. Verify the claimed coarse reach at most 21, the accompanying weight factor, and exactly which positive-mass inputs remain. A finite-reach observation alone does not establish weighted analytic inputs.
6. Check every one of the thirteen advertised refutations against the actual quoted statement and its domain. A new sufficient route does not logically disprove another sufficient route; an undefined claim is not automatically false; a slice-specific result does not settle an unspecified or different slice.

Verdict vocabulary: **CONFIRMED** for a proved statement on its stated or explicitly narrowed domain; **REFUTED** only with a contradiction/counterexample or an incorrect claimed source reading; **NOT-VERIFIED** for a missing proof, unresolved domain match, or unsupported stronger conclusion. Each finding will identify a file and locating string. The final section will list exactly what may be banked and retain all material conditions.

### Exact check plan added after source reading, before execution

These checks are arithmetic/algebra controls, not numerical evidence for uniform analytic theorems: (i) expand the quintic tent identity and its endpoint derivatives; (ii) verify the two-dimensional normal form of GF-DEP, with Hessian `diag(1,0)`, gauge functional `(t,-1)`, fixed source `(1,0)`, and response `(1,t)`; (iii) certify positivity of `9-(196/25)(1800/1751)^2`, which follows from the rational majorant `cosh(7/30) <= 1800/1751`; (iv) test the target's intermediate decimal inequality by the exact lower bound `cosh(t)^2 >= 1+t^2+t^4/3` at `t=1167/5000`. The suspect inequality was noticed during reading and receives no claim of prior registration. Execute only an in-memory standard-library calculation, with no script/log/cache files.

## Disposition

**CONFIRMED:** the substantive new conclusion is a source-only field estimate on **S_E**, at **Z = 1, m = 0**, for the stated composite-co-closed classes. EP-opt and the unweighted EP-rec survive independent derivation. CC-INV plus RHT-cc then gives GF-E. LIN0 plus RHT gives GF-E′ in RTARGET's weaker source norm, with `0 < α < θ < 1`, a θ-dependent constant, and the slice explicitly changed to S_E. The displayed comparison factor `3` is not established; `4` is sufficient and follows directly from the definitions.

**CONFIRMED:** GF-DEP refutes gauge-fixing-independent field bounds over all admissible gauge fixings. The orbit-norm replacement is valid. The nonzero-alias denominators are uniformly separated from zero on the stated fundamental-domain tube of half-width `7/5`; an exact rational proof below repairs the target's false intermediate decimal inequality.

**NOT-VERIFIED:** the particular weighted reach `R_* ≤ 21` from the supplied audit, the original per-level-slice statement, and a blanket endorsement of the target's thirteen refutations. Finite absolute reach, and therefore the conditional weighted reconstruction, do follow; the numerical reach audit mixes metrics. Several purported refutations change the slice, mass range, or source statement. Two substantive assertions in the target are **REFUTED**: that neither piece of its proposed decomposition is necessary (the fine bound is an output consequence), and that GU's weighted Hölder transfer is unwritten (Lemma WT supplies it).

All confirmations below are mathematical review conclusions with their named inputs. They do not change repository audit status or establish the full background-dependent BFT-5(b).

## Source boundary and provenance

All filenames below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. Locating strings are authoritative; line numbers are retrieval aids. Source content was read by `rg` and bounded `sed` ranges. No git command, source edit, reviewer delegation, floating-point computation, or external worker was used. Only this report was written. The requested mathematical review was performed by this Codex reviewer; no separate model invocation or verification log is claimed.

This is the identified local worktree snapshot, not a claim about a fetched main revision. SHA-256 identities recorded at `2026-10-29T00:41:59Z`:

| File | SHA-256 |
|---|---|
| GSHARP55.md | `983bc5a83f44fb84db93a1457dc0ac2125b64a84298526c91b4d45c2c91a5312` |
| BFT_B.md | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| BFT_A.md | `8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| COFUN_CC.md | `2a399a7dce1de8f0a4e9b4dfb81d9f0595e8eb4d8b294e2764b1b518d98ce035` |
| CODEX_REVIEW_TOPCC.md | `68bc5d15520d1cc12e25ff0aef313f75c8bcf00965fce34821c1ed0afbb313d6` |
| RTARGET.md | `e98f1c9c5ee9a7d7f4f90fd9d3cd6958895ffdba5363ca3c167f04b18871cd55` |
| NBG_B.md | `72491c52b9aebf86de3a5930ff80d4cb2dff906fcb29dc82153b2d2c56081e14` |
| NBG_ADJ.md | `cfcb7bd111d6afe800c600b13b027aada197c86d45e51c9875946c1b3aaf3001` |
| PROOF.md | `02beb7dff29d1e23ae4cd8e890480b4d52d28adb55af457a78c4f9ebca309efd` |
| SF.md | `e966acccb5410b8aa86c55ccad6054bc7ac39265f41bdf8945f5eb83cd9ff847` |

The accepted analytic input to the independent reconstruction is **LINEAR_PACKAGE Lemma 3.2'' (LES-div)**, with its stated lattice, interior domain and Campanato hypotheses. This review checks its application, rescaling and energy input; it does not independently re-prove the package's Campanato iteration. CC-INV is imported on the scope explicitly banked in **CODEX_REVIEW_TOPCC, “Exactly what may be banked”, item 3**. W0, GU and the data estimates enter with their named lane/package hypotheses. EP-opt and EP-rec are not imported on the authority of REVIEW_BFT_B_S5: their load-bearing steps are checked below by a derivation that avoids LR-pot for the local potential estimate.

## 1. EP-opt: CONFIRMED

Sources: **BFT_B §15.0 “Setting EΠ”**, **§16.1 “Lemma EP-alg”**, **§16.5 “Theorem EP-opt”**; **BFT_A §7.1 “Setting LIN”** and **§7.2 “Norms”**. Target: **GSHARP55 §5.1(a), “Identification (EP-opt)”**.

Work componentwise on a finite periodic four-dimensional lattice. Write `Dλ = (d ev^(j)λ)_(j<k)` and use the pinned gauge-parameter space `Λ_* = {λ : λ vanishes at every level-k root}`. Thus `𝒢_0 = Ran D`; constants have already been removed by the pinning. Composite co-closedness means annihilation of this space. It need not mean that the unrestricted site function called `D(S)` in BFT_B §27.1 vanishes pointwise at the terminal roots.

The box minimization has a unique pinned minimizer because the connected box graph Laplacian is positive definite after its constant mode is pinned. Changing the input by `dμ` changes its minimizer by

    λ_X(x + dμ) = λ_X(x) − μ + μ(c_X).

The quintic identity `σ(t)+σ(1−t)=1` gives `Σ_Xχ_X=1`, while `χ_X(c_Y)=δ_XY`. Consequently `Λ(x)` vanishes at terminal roots,

    Λ(Dμ) = −μ,
    Π_E = I + DΛ,
    ΛΠ_E = 0,   Π_E² = Π_E,   Π_E D = 0.

Thus `X = S_E ⊕ 𝒢_0` algebraically. This uses no spectral estimate.

On displacements with `x_k=0`, the positive quadratic form is

    𝓑(x,x) = ||dx_0||₂² + Σ_(i<k) κ_i ||Q_i x_i − x_(i+1)||₂².

If it vanishes, `x_0=dλ+h`, where `h` is a constant torus one-form, and every residual vanishes. Root covariance and the action of Q on constants give

    x_j = d ev^(j)λ + L^j h,
    0 = x_k = d ev^(k)λ + L^k h.

The torus mean of an exact form is zero, including on a one-site terminal torus. Hence `h=0`. The terminal values of λ are constant and can be subtracted. This proves `Ker H=𝒢_0`, including the harmonic-mode check. The converse follows directly from root covariance and `d²=0`.

For a covector `S` annihilating `𝒢_0`, finite-dimensional self-adjointness gives `Hx=S`, uniquely modulo `𝒢_0`. Since `Π_Ex−x` is in the kernel, `Π_Ex` satisfies the same equation. A vector in S_E satisfying the homogeneous restricted equation is in the full kernel: test a general `w` by replacing it with `Π_Ew`. Its intersection with S_E is zero. Therefore

    (H|_(S_E))^(-1)(S|_(S_E)) = Π_Ex.

This is the EP-opt identity. It also applies to differences of configurations with the same nonzero terminal datum; fixing the datum does not change the displacement kernel.

With the unweighted boundedness of Π_E established in §2 below,

    inf_(Hz=S) ||z||_𝔐 ≤ ||Π_Ex||_𝔐
      ≤ C_Π inf_(Hz=S) ||z||_𝔐.

These are the claimed optimal-gauge inequalities. They are conditional on solvability/annihilation of the gauge kernel. For an arbitrary covector S, the restricted problem instead corresponds to the full source `Π_E^T S`; it is not legitimate to replace that source's norm by `N(S)` without another estimate.

## 2. EP-rec: CONFIRMED at zero weight, by an independent reconstruction

Sources: **BFT_B §16.2 “Lemma EP-int”**, **§16.3 “Lemma Q-hold”**, **§16.6 “Theorem EP-rec”**; **BFT_A §13.11 “Lemma Λ”**, **§7.3 “Lemma BL-2”**; **LINEAR_PACKAGE “Lemma 3.2'' (LES-div)”**. Target: **GSHARP55 §5.1(b)–(c)**.

Write `h=1/n`, `x_0^c=nx_0`, `f_0=n²dx_0`. All derivatives below are differences divided by the appropriate coarse mesh length. Put

    A_inv(x) = ||f_0||∞ + [f_0]_α + ||x_k||_D
                 + Σ_(i<k)||r_i^c||∞.

### 2.1 Local Neumann potential: a different comparison field

Let `a_X=x_0+dλ_X` on the box `Ñ_X` of coarse half-width 2. The Euler equation gives orthogonality to every box gradient and `d*a_X=0` at interior sites. Thus

    ||a_X||_(2,Ñ_X) ≤ ||x_0+dμ||_(2,Ñ_X)

for **every box function** μ. A global periodic comparison gauge is unnecessary.

Choose μ to be minus the integral of `x_0` along a fixed coordinate-ordered axial path from `c_X` to each site of `Ñ_X`. For a μ-direction link, the difference between the two axial paths is a strip consisting of at most `3·2n=6n` fine plaquettes. Discrete Stokes gives the exact bound

    sup_(Ñ_X) |(x_0+dμ)^c| ≤ 6 ||f_0||_(∞,Ñ_X).

All strips remain in the box. Therefore the normalized L² size of `a_X^c` is bounded by a dimension-dependent constant times `||f_0||∞`. This removes LR-pot, its constants `155,8,40`, and all data/residual estimates from this particular step. A curl-free field is exactly removed by the box gradient projection, as it must be.

Inside the box,

    da_X = dx_0,
    (d*d+dd*)a_X = d*dx_0.

Componentwise this is a scalar difference-Laplacian equation with a divergence-form right side. Its datum in coarse units is f_0. Testing on a smaller box with `η²(a_X−c)` and summing by parts gives

    avg |∇^c a_X^c|²
      ≤ C (avg |a_X^c|² + sup |f_0|²),

where the inner and outer boxes have fixed coarse sizes. The constant is independent of n. Applying LES-div to each component, then telescoping nested box averages down to one lattice site, gives

    ||a_X||_(C^(1,α)(N'_X))
      ≤ C_α (||f_0||_(∞,Ñ_X) + [f_0]_(α;Ñ_X)),

with `N'_X` of half-width `3/2`. The factors `n²∂a_X` and `n²dx_0` have the same coarse derivative scaling; there is no hidden power of n. Only interior equations are used, with a fixed positive margin to the Neumann boundary.

For the finite set `L^k<64`, the same assertion follows on the quotient of box link fields by box gradients: curl detects that quotient on a contractible box, and the induced maps are between fixed finite-dimensional spaces. Taking the maximum over that finite set is allowed; it does not turn small torus size into a finite-dimensional-in-k argument. This also repairs any rounding of the `n/4` interior box: use integer subboxes of comparable size, with the remaining bounded n cases treated here.

This establishes the load-bearing content of EP-int(b) using the package LES-div input and an independent L² comparison.

### 2.2 Root-line data: exact telescope, without a product of contour norms

Let `H_i(Y,ν)` be the integral of x_0 along the straight fine path between adjacent level-i roots. Thus `H_0=x_0`, and `H_k` is the terminal root-line sum. Closing a one-step S4' contour against its straight leg requires at most `2L(L−1)` level-i plaquettes. Each such plaquette has fine flux bounded by `L^(2i)||dx_0||∞`. Consequently

    ||H_(i+1)−Q_iH_i||∞
      ≤ 2L(L−1)L^(2i)||dx_0||∞.

The **composite** BL-2 bound is `||Q^(i+1→k)v||∞ ≤ 5L^(k−1−i)||v||∞`. Applying it once to each telescoping error gives

    ||H_k−Q^(0→k)x_0||∞
      ≤ 10L(L−1)L^(k−1) Σ_(i=0)^(k−1)L^i ||dx_0||∞
      = 10n(n−1)||dx_0||∞
      = 10(1−1/n)||f_0||∞.

Using `Q^(0→k)x_0 = x_k + Σ_(i<k)Q^(i+1→k)r_i`, one obtains

    ||H_k||∞ ≤ ||x_k||_D + 5Σ_(i<k)||r_i^c||∞ + 10||f_0||∞.

This checks the sufficient constant 10 and, more importantly, the absence of a k-dependent contour product. The ribbon surfaces and composite contours stay within the two terminal blocks of the terminal link, by nesting of the centered blocks. The same calculation can therefore use local sups on those blocks.

### 2.3 Patching retains regularity and the terminal root information

For `b=(z,z+e_μ)` the exact discrete product rule gives

    (Π_Ex)_0(b)
      = Σ_X χ_X(z+e_μ)a_X(b)
        + Σ_X (λ_X(z)−λ_*(z)) dχ_X(b).

The subtraction is valid because `Σ_Xdχ_X=0`. In any cell, choose the reference root `c_*` among its corners. Neighboring cells needed for a local comparison admit common reference corners; subdivision into these bounded overlaps avoids any dependence on the total number of cells.

On an overlap, `d(λ_X−λ_*)=a_X−a_*`. The integration constant is fixed, not discarded:

    λ_X(c_*) = ∫_(c_X→c_*) (a_X−x_0).

The path uses at most four adjacent terminal-root segments and stays in the interior boxes. Its a_X contribution is bounded by `4 sup|a_X^c|`; its x_0 contribution is bounded by four root-line sums from §2.2. Thus `λ_X−λ_*` has a local `C^(2,α)` bound by `C A_inv(x)`.

The quintic tents have uniformly bounded `C^(2,1)` norms; their continuum value and first two derivatives vanish at the outer support boundary. The sampled discrete product estimates consequently hold across cell interfaces as well as inside cells. **No assertion that every discrete second difference at the last interior site vanishes is needed.** Extend the tent coefficients by zero and use their bounded difference quotients, with λ evaluated on the larger interior boxes. There are only boundedly many overlapping terms. Hence

    ||(Π_Ex)_0||_(C^(1,α)) ≤ C A_inv(x).

The residual sup sum is controlled exactly by

    Σ_(i<k)||r_i^c||∞
      ≤ ||x||inv Σ_(q=0)^(k−1)L^(−q)
      ≤ L/(L−1) ||x||inv.

Therefore the level-zero bound has precisely the proposed right-hand side `C(||x||inv+||x_k||_D)`. It applies to every configuration, not just to a critical response.

### 2.4 Q-hold and the residual sum

For `s=L^(b−a)` and `ρ_b=sρ_a`, use the exact decomposition

    Q^(a→b) = Q_str^(a→b) − d h^(a→b),
    ||h^(a→b)v||∞ ≤ 2(s−1)||v||∞.

In coarse units the straight term is a probability average of translates of `v^c`; a coarse difference quotient is an average of fine difference quotients. It preserves the corresponding sup and pointwise Hölder bounds.

Translation covariance of h gives for its gauge term

    ||(dhv)^c||∞ ≤ 2ρ_b ||∇^c v^c||∞.

For its coarse gradient, write the two translated differences of v as a sum of s fine differences and then take a difference at separation `ρ_b`. This gives

    ||∇^c(dhv)^c||∞
      ≤ ρ_b^(−2) · 2s · sρ_a² · ρ_b^α [∇^c v^c]^∞_α
      = 2ρ_b^α [∇^c v^c]^∞_α.

The output mesh is `ρ_b`. Its Campanato boxes have side at least `ρ_b`, so its gradient Campanato seminorm is bounded by a fixed multiple of the last Hölder seminorm. The local Campanato-to-pointwise conversion is uniform in the mesh for fixed α. This proves Q-hold with a constant independent of `b−a`; it is not a product of one-step constants.

Residuals are exactly invariant under Π_E. Telescoping the chain, for `j<k`, gives

    (Π_Ex)_j = Q^(0→j)(Π_Ex)_0
                 − Σ_(i<j) Q^(i+1→j)r_i(x).

The last sum uses only `i≤k−2`. Consequently

    max_(j<k)||(Π_Ex)_j||_(C^(1,α))
      ≤ C (||x||inv + ||x_k||_D + N_res(x)).

The remaining, weighted-in-level residual terms of 𝔐 are already bounded by `||x||inv`. This proves EP-rec as stated at `m=0`.

The appearance of **the sum** `N_res`, not its maximum, is essential to this argument. EP-rec alone proves a forward reconstruction inequality. Its converse only bounds each residual separately, as BFT_B §16.7 explicitly records under “The converse bounds the max over i”. GSHARP55 §4.3's word “equivalent” therefore also needs RHT/RHT-cc for the particular critical source class; it does not follow from EP-opt and EP-rec alone on arbitrary configurations or arbitrary projected-source families.

### 2.5 Bounded projection and small tori

For completeness, EP-bd at zero weight follows from a different application of the same interior estimate. The equation for λ is `−Δλ=±div x_0`; the equation for its first difference has right side `±div(∂x_0)`. Orthogonal projection controls `dλ` in L² by x_0. Caccioppoli and LES-div thus control λ in `C^(2,α)` on the tent support by the local `C^(1,α)` norm of x_0. Pinning fixes λ's value. Multiplication by the quintic tents and root restriction at every level preserve the bound. Residuals are unchanged. Hence `||Π_Ev||_𝔐 ≤ C_Π||v||_𝔐`, uniformly in k and T for `T≥5`.

For `T≤4`, lift periodically to `T'=cT≥5` and apply the same local boxes there. Coarse translation covariance makes the projected configuration T-periodic. It descends to `Π^(T)` and has the same unweighted local norms, since all Campanato boxes have side at most one coarse unit. Projection, kernel complement and EP-opt descend as well. This verifies the use of **BFT_A §33.13 “Proposition SM”** for every `T≥1`. The weighted same-constant assertion is not imported: **REVIEW_BFT_A_S7, “Proposition SM”** explicitly requires an additional bounded weight factor.

## 3. GF-E and GF-E′: the source norms actually match

### 3.1 GF-E: CONFIRMED as a named-input implication

Sources: **COFUN_CC §6.1 “Theorem CC-INV”**; **CODEX_REVIEW_TOPCC, “Exactly what may be banked”, item 3**; **BFT_B §27.2 “Theorem RHT-cc”**, **§29.3**. Target: **GSHARP55 §5.2 “Theorem GF-E”**.

Fix `d=4`, odd `L≥3`, positive fixed `κ_±`, and `0<α<θ<1`. Let `x_k=0` and let S be a Setting LIN^cc source in the stated `(P0)+(Pl-c)+(G)+(R)` classes. Use exactly the N(S) of COFUN_CC and GSHARP55, with no replacement by a level maximum lacking the class weights.

Here is an independent check of the residual summation. Set `q=k−1−i≥1` and `a=1−α>0`. A transported level-l plain current has residual coarse size at level `i+1` at most `L^(−2q)π_l(j_l)`: its own-unit factor `L^(−3(l−i−1))`, current factor `L^(−3(k−l))`, and residual conversion `L^q` multiply to precisely `L^(−2q)`. The discrete inverse estimate is

    ||H||_(C^(1,α)) ≤ 5L^((1+α)q)||H^c||∞.

It follows by bounding the sup, first difference and its Campanato seminorm separately. Thus transport leaves the summable factor `L^(−aq)`. For a level-l divergence source, `π_l(d*G_l)≤6L^(k−l)||G_l^c||∞` in four dimensions. For the direct residual source the remaining factor is `L^(−θ)L^(-(θ−α)q)`.

The composite-co-closed funnel adds

    π_l(h_l^Tψ_l) ≤ 2d Σ_(l'≤l) L^(−3(l−l'))π_(l')(j_(l')).

After multiplying by `L^(−a(k−l))` and interchanging the finite nonnegative sums, its extra geometric factor is bounded by

    K_f = 2d Σ_(u≥0)L^(-(3−a)u)
        = 2d/(1−L^(-(2+α))).

This is exactly RHT-cc's exponent; no floating approximation to K_f is used. Summing the remaining level weights yields

    N_res(x) ≤ (5/κ_-)[
      (κ_+||x||inv + L^(−θ)||s||_R)/(L^a−1)
      + L^(−θ)||s||_R/(L^(θ−α)−1)
      + (1−L^(−a))^(-1) (
          (1+K_f)||j||_Pc/(L^(a+θ)−1)
          + 6||G||_Y/(L^(θ−α)−1)
          + K_f L^(−ak)||j_0^c||∞ ) ].

All denominators are positive in the stated window. In particular,

    N_res(x) ≤ A ||x||inv + C_N N(S),
    A = 5κ_+ / [κ_-(L^(1−α)−1)],

with finite `C_N=C_N(L,κ_±,α,θ)` independent of k and T. For `k=1`, `N_res=0`, so the conclusion holds directly.

CC-INV supplies `||x||inv≤C_invN(S)` with no unknown terminal residual left on the right. EP-opt identifies `x_E=Π_Ex`. EP-rec then proves

    ||x_E||_𝔐 ≤ C_rec[(1+A)C_inv+C_N] N(S).

This verifies the target's substantive GF-E and its displayed construction of `C_GF`, allowing C_rec and C_N to be any valid constants in their definitions. The orbit estimate follows immediately. It is valid for the larger composite-co-closed class, not just for sources individually co-closed at each level.

This conclusion is a **linear source-norm estimate**. It does not establish that the full nonlinear critical source has a k-uniform `O(η²)` norm. The higher-order/level-count conditions retained by CODEX_REVIEW_TOPCC remain conditions.

### 3.2 GF-E′: CONFIRMED on S_E in RTARGET's source norm

Sources: **RTARGET §33**, locating “the norms below are taken in DIVERGENCE FORM” and “Source norm”; **BFT_A §28.7 “Theorem GU”**, especially “no Hölder norm of G_l”; **§28.8 “Corollary LIN0”**; **BFT_B §18.1 “Corollary RH-inv”**, including its source-class correction. Target: **GSHARP55 §5.2 “Theorem GF-E′”**.

Set all plain and residual sources to zero. The currents are `j_l=d*G_l`; co-closedness and zero mean concern these **one-form currents**, not an additional co-closedness requirement on the representing two-forms G_l.

At level zero, W0 uses `||G_0^c||∞+[G_0^c]_α`. At positive levels, GU gives

    ||x(G_l)||inv
      ≤ C (k−l+1)² L^(α(k−l)) ||G_l^c||∞.

With `ω_l=L^(θ(k−l))`, the sum is bounded by

    C Σ_(u≥1)(u+1)² L^(-(θ−α)u) max_(l≥1)ω_l||G_l^c||∞.

It is finite for `α<θ` and uses no positive-level Hölder source norm. The datum part is bounded by the data theorem. RHT has no j-funnel term in this class; its G term uses the still simpler sum `Σ_(u≥1)L^(-(θ−α)u)`. Therefore

    ||B_E||_𝔐 ≤ C [ ||G||_(Y,α;RTARGET) + ||B_k||_D ],

uniformly in k and T. Since the estimate holds for **each** divergence-form representation of the same currents, take the infimum over representations to obtain RTARGET's own quotient source norm. There is no hidden strengthening to lane A's Hölder norm at every positive level.

The constant depends on θ, and no endpoint `α=θ`, no `α>θ`, and no θ-free estimate is proved here. Most importantly, this is the **S_E analogue** of RTARGET's statement. RTARGET's displayed slice is the per-level slice, and its target includes positive mass. GF-E′ does not prove either of those additional clauses.

### 3.3 The displayed factor 3: NOT-VERIFIED; factor 4 is sufficient

Sources: **GSHARP55 §1 “𝔐-pair”**, **§5.2**, locating `≤ 3||B||`; **BFT_A §1.4 “𝔐^∇”**; **RTARGET §33 “configuration”**.

Let `M=||x||_𝔐`. The stated componentwise estimates give

    ||x||_(X_c) ≤ 2M,
    [f_0]_α ≤ 2M,
    ||x||_(X_c)+[f_0]_α ≤ 4M.

The maximum over levels in X_c and the separate level-zero seminorm need not attain their bounds at the same level. The target's two cited inequalities therefore do not give 3. I have not constructed a configuration refuting the sharper 3; that numerical comparison is **NOT-VERIFIED**, not declared false. Replacing it by 4 leaves GF-E and GF-E′ unchanged as existence-of-a-uniform-constant statements.

## 4. Alias analyticity: CONFIRMED with exact arithmetic and an object distinction

Sources: **GSHARP55 §3.4(ii)**; **PROOF “Lemma EXP-strip”, proof “(P4)”**; **“[R1314-fix] The f_0 half written out”**; **LINEAR_PACKAGE “Lemma 6.5 (SRC-id and SRC-all)”**.

Take `K∈{0,…,n−1}^4\{0}`, `x∈[−π,π]^4`, and `z=x+iy`. Define

    φ_K(z)=4n² Σ_(ν=1)^4 sin²((z_ν+2πK_ν)/(2n)).

Some nonzero coordinate of K has real angle between π and `2πn−π`. Consequently

    φ_K(x) ≥ 4n² sin²(π/(2n)) ≥ 9,   n≥3.

For the second inequality, `sin t/t` decreases on `(0,π/2]`, so `n sin(π/(2n))` increases with n, and the n=3 value is `3/2` exactly.

Using `Re sin²(a+ib)≥sin²a−sinh²b` and `sinh t≤t cosh t` for `t≥0`, for `|y_ν|≤η` one obtains

    Re φ_K(z) ≥ 9−4η²cosh²(η/6).

Set `η=7/5`. Since `(2r)!≥2^r`, the positive Taylor series gives the entirely rational majorant

    cosh(7/30) ≤ Σ_(r≥0)((7/30)²/2)^r = 1800/1751.

Hence

    Re φ_K(z)
      ≥ 9−(196/25)(1800/1751)²
      = 2192409/3066001 > 0,

and

    |1/φ_K(z)| ≤ 3066001/2192409.

This proves a nonvanishing open neighborhood of the closed fundamental-domain tube, uniform in n and K. It does not assert that a fixed alias label is nonsingular for **all** real parts in R⁴: shifting the real part by `−2πK` reaches its zero. Alias labels permute when the coarse Brillouin domain is crossed. The claimed scope in GSHARP55 is the fundamental-domain one, which is correct.

**The target's intermediate numerical bound is REFUTED.** Its locating string is `cosh²(0.2334) ≤ ... 1.0554`. For `t=1167/5000`,

    cosh²t ≥ 1+t²+t⁴/3,
    1+t²+t⁴/3 − 5277/5000
      = 40472216107/625000000000000 > 0.

This invalidates that intermediate rounding, but the exact bound above proves the intended strip and needs no decimal computation.

Three objects must remain separate:

1. **Each nonzero-alias reciprocal `1/φ_K`: CONFIRMED** on the width-`7/5` tube just proved.
2. **The screened, fixed-n source-to-curvature symbol for SRC-id's co-closed source class on the package's smaller admissible strip: CONFIRMED as an implication of SRC-id and the EXP-strip inverse bounds.** The K=0 curl formula cancels φ; its remaining β and Ψ inverses require their own nonvanishing estimates. For nonzero input aliases the effective datum is analytic, and the package's analytic datum-response map supplies the remaining part. Finite alias summation at fixed n preserves analyticity. The width `7/5` is not thereby a strip for the whole inverse, and this does not assert an arbitrary-source, arbitrary-gauge symbol theorem.
3. **A uniform norm estimate after fine-offset/alias summation: not a consequence of either analyticity statement.** The size of the sum and its fine-grid operator norm still require estimates. For divergence-form sources the local order-zero singular integral has the `|x|^(−4)` behavior of RTARGET's G0-F2. Hölder oscillations replace the logarithmic shell sum by a convergent sum `Σ_(r≥0)2^(−αr)`. W0/LE supplies the actual local-plus-far argument; GU supplies the positive levels. The target is correct that this produces the unweighted invariant input needed here.

It is inaccurate to identify **every** old alias-related concern with G0-F2. **PROOF**, locating “G0-F3 is undecided”, separately discusses long-range exponential decay. The strip-factor calculation alone proves neither a uniform weighted source estimate nor the general weighted COF assembly. Thus the alias pole obstruction is absent on the checked strip and is unnecessary for the proved unweighted route; the blanket positive-mass closure does not follow from it.

There is also a source-fidelity error: **NBG_ADJ §2.4** says “has not been shown analytic in a strip”, and its graph says “not shown analytic”. Those are faithful to the quoted historical sentence. **PROOF [S25-fix 5]** drops “shown” and says “not analytic”. GSHARP55 §3.4(ii)'s assertion that **both** NBG_ADJ and that PROOF amendment made the misquotation is **REFUTED** by the actual NBG_ADJ text.

## 5. GF-DEP and the orbit norm: CONFIRMED

Sources: **GSHARP55 §4.2 “Proposition GF-DEP”**; **BFT_B §16.1(e)**; **§32.1(b)**, locating “independent of the gauge fixing”; **BFT_A §28.9 “Lemma FG”**.

The operator family in the target is valid. Here is a concrete choice that removes any existential ambiguity about the fixed nonzero-curvature source.

Fix `k=1`, `L=3`, `T=5`, one real Lie-algebra component, and positive κ. Let v_0 be one unit oriented fine link, with all other links zero and terminal datum zero. Choose an incident plaquette p with `(dv_0)(p)=1`. Set `S=Hv`. This is composite-co-closed because `HD=0`; it is a source of the permitted form, with `G_0=dv_0`, `s_0=κ_0r_0(v)` and no plain current. Its norms are finite on this fixed lattice. Its S_E response is `x_E=Π_Ev`, and `ℓ(x_E):=(dx_(E,0))(p)=1`.

Let μ_0 be a unit scalar at any nonterminal-root fine site and zero elsewhere. It belongs to Λ_* and `Dμ_0≠0`. For each integer t, define

    Γ_t x = Λ(x)+tℓ(x)μ_0.

Because `ℓD=0` and `ΛD=−I`,

    Γ_tD = −I.

Every Γ_t is an admissible gauge fixing onto the same gauge-parameter space. Moreover `H+Γ_t^TΓ_t` is positive definite: a vector in its kernel lies both in `Ker H=Ran D` and `Ker Γ_t`, hence is zero. The inverse response to the **same** S is exactly

    x_t = x_E+tDμ_0,

since `Hx_t=S` and `Γ_tx_t=0`. Its field norm obeys

    ||x_t||_(X_c) ≥ |t| ||Dμ_0||_(X_c) − ||x_E||_(X_c),

which is unbounded. Curvatures, residuals, `||x_t||inv`, and `N_res(x_t)` are identical for every t.

The two-coordinate normal form makes the algebra explicit: with `H=diag(1,0)`, `D=(0,1)^T`, `Γ_t=(t,−1)`,

    H+Γ_t^TΓ_t = [[1+t²,−t], [−t,1]],
    det(H+Γ_t^TΓ_t)=1,
    (H+Γ_t^TΓ_t)^(-1) = [[1,t], [t,1+t²]],
    (H+Γ_t^TΓ_t)^(-1)(1,0)^T=(1,t)^T.

This is not a numerical lattice surrogate; the preceding lattice construction already provides the witness. It also shows exactly why invertibility of ΓD alone cannot impose a uniform norm bound over all Γ. No boundedness/locality class for Γ was imposed in BFT_B's quoted gauge-independence clause.

At the flat background the proposed repair follows from EP-bd:

    ||[x]||_𝔐 := inf_(g∈𝒢_0)||x+g||_𝔐,
    ||[x]||_𝔐 ≤ ||Π_Ex||_𝔐 ≤ C_Π||[x]||_𝔐.

For the second inequality, apply EP-bd to each representative and use `Π_E(x+g)=Π_Ex`, then take the infimum. This is a genuine quotient norm on the displacement quotient, not a claim that all representatives have comparable norms. At nontrivial backgrounds the corresponding equivalence requires the background projection estimate; the flat EP-bd does not supply it.

## 6. Positive mass: finite reach is enough, but 21 is not verified by this audit

Sources: **GSHARP55 §5.3**, locating “R_* ≤ 4 + 3 + 5 + 8 + 1 = 21”; **BFT_B §12.1 “(W-Π)”**, **§16.1(g)**, **§18.0 “Weighted residual size”**; **RTARGET §33 “ℓ¹ torus distance”**; **BFT_A §13.11**, **§13.12 “Weights”**, **§33.10 “Lemma WT”**.

**CONFIRMED — finite absolute reach.** The independent reconstruction in §2 is local in the following precise sense. The Neumann solve reads one box of fixed coarse half-width 2. Its interior estimates read only smaller boxes. Patching reads a bounded collection of neighboring boxes and adjacent root segments. A root segment's flux telescope is supported in its two terminal blocks: recursively replacing a level-i contour by lower-level contours stays in the parent blocks, rather than accumulating a new coarse displacement per scale. The composite Q maps likewise stay in two output-level blocks. All Campanato boxes have coarse side at most one. These are finitely many bounded enlargements of an output neighborhood, independent of k and T. Consequently there is an absolute radius R in the **ℓ¹ coarse metric** for the localized reconstruction inequality.

For `w(z)=exp(m d_1(z,X_0))`, `w(z)/w(y)≤exp(mR)` on that neighborhood. Multiplying the local inequality by the output weight, and using the box-corner weights for the Campanato inputs, proves

    ||Π_Ex||_(𝔐,m)
      ≤ C_rec exp(C_*m)
           [||x||_(inv,m)+||x_k||_(D,m)+N_(res,m)(x)]

for some absolute `C_*`. No derivative of the weight is taken in this step. Periodic descent for small tori incurs only another bounded factor, as the corrected SM statement records. This confirms the weighted **implication**, with no loss of the admissible mass rate caused by reconstruction.

**NOT-VERIFIED — the asserted numerical radius 21.** The particular calculation in GSHARP55 does not establish it. EP-alg's radius 4 is explicitly a `B_∞` radius; the Neumann half-widths and the tent supports are also ℓ∞ dimensions. RHT_m and RTARGET use ℓ¹ distance. In four dimensions an ℓ∞ radius r gives an ℓ¹ bound `4r`, not r. Likewise, a unit-side Hölder box can have ℓ¹ diameter 4, not 1. The audit's last step silently uses its mixed-radius sum as an ℓ¹ displacement in `e^(mR_*)`. The supports of the quantities at the separate intermediate output points must also be composed. Neither the summands 3 and 5 nor the final conversion have that accounting written out.

This defect does **not** prove that every possible corrected audit exceeds 21. It means that 21, and the precise displayed factor `e^(21m)`, cannot be banked from this audit. Finiteness is independently justified above. I also do not bank the older 24 merely because it is larger: it inherited a reach qualification in REVIEW_BFT_B_S5.

**CONFIRMED — conditional reduction to (R3) on the (cc) class.** If the required weighted CC-INV/COF/TOP-cc source estimate is supplied in its correct weighted source norm, RHT_m-cc controls `N_(res,m)` with the top residual now supplied by that estimate. The weighted reconstruction then controls the field. This is what “the field half adds nothing beyond (R3)” can mean rigorously. It is not a proof of (R3).

**REFUTED — “Its Hölder part is not written.”** GSHARP55 §5.3 and its lead-facing conclusions say that weighted GU still has a separately unwritten Hölder half. **BFT_A §33.10 “Lemma WT”** expressly transfers the Hölder steps of W0, GU, CO-0R and CO-B from their weighted sup bounds. **BFT_A §35's table**, locating “their Hölder parts follow by Lemma WT once the sups hold”, states this directly; **REVIEW_BFT_A_S7**, locating “m > 0: Lemma LES-dd ... Lemma WT”, confirms its stated scope. The correct remaining analytic inputs include DX_m and DB_m and the required full weighted assembly. A separate unwritten GU Hölder transfer is stale bookkeeping.

## 7. Audit of the thirteen advertised refutations

The table adjudicates **GSHARP55's rebuttal**, not an invented replacement for the sentence being rebutted. A narrowed confirmation states exactly what is being contradicted. An earlier failure to verify a claim is not itself refuted by a later proof; the additional proof changes what may now be used.

| Target ID | Verdict on the claimed refutation | Source and decisive scope check |
|---|---|---|
| F2 | **NOT-VERIFIED** for the original statement | **NBG_B §3**, “Status: OPEN, and specifically ‘not attempted’”, explicitly pins the **per-level slice** and positive-mass range. GF-E′ proves the S_E, m=0 analogue. Its §5.5 transfer to the original slice is expressly unwritten. The new analogue can supersede a current need for that formulation; it does not prove that formulation. |
| F3 | **NOT-VERIFIED** as a literal refutation | **NBG_B §3**, “None of it is the configuration statement”, refers to the immediately listed **lane-A W0/GU/LIN0** results for invariant outputs. EP-rec/EP-lin are additional lane-B inputs. Their addition proves a field estimate; it does not make those lane-A theorem statements into field estimates. The following “none ... on the per-level slice” remains true. |
| F4 | **NOT-VERIFIED** as a claim about the old per-level requirement | **NBG_B §6.2**, “extra input”, is a table about the explicitly per-level-slice G♯_0-field. **CONFIRMED** within the new S_E argument: EP-rec needs no additional per-level physical-gap estimate. A different proof route is not a counterexample to necessity in a different specified slice. |
| F5 | **NOT-VERIFIED** as the blanket rebuttal | **NBG_B §6.5**, “the gauge-variant half, and the multi-level slice gap”, continues that per-level discussion. Its **§9 S9/S11(i)** explicitly distinguishes the S_E live target. The S_E field half is now confirmed, but the asserted internal contradiction disappears once the two slices are kept distinct. No joint per-level gap was proved here. |
| F8 | **NOT-VERIFIED** as a refutation of the proposed implication | **NBG_ADJ §2.4**, “So ... = [multi-level per-level-slice gap] + [(G♯_0-fine)]”, supplies no sufficiency proof. Its equality/necessity reading was already unsupported. A new S_E sufficient route does not refute the old sufficient route. The target's added claim “Neither piece is necessary on S_E” is separately **REFUTED** below. |
| F9 | **NOT-VERIFIED** for the joint-gap reading | **NBG_ADJ §5.2 graph**, “multi-level per-level-slice physical gap [OPEN]”. **LINEAR_PACKAGE Proposition 6.4** and **PROOF “Lemma N5-coer”** do establish the one-level effective-energy inequalities for each i. Thus the refutation is **CONFIRMED only if** the node means precisely those inequalities. Neither source identifies them with a quantitatively specified joint-chain gap in the original field norm. An unspecified joint claim is not proved false by being unspecified. |
| F10 | **CONFIRMED**, restricted to the claimed live obstruction at m=0 | **NBG_ADJ §2.4**, “(G♯_0-fine) is OPEN”, is stale on the `α<θ`, m=0 class because W0+GU+data give it. The nonzero-alias denominator pole concern is also removed by §4. But GSHARP55's accusation that NBG_ADJ says “not analytic” is **REFUTED**, and positive-mass general-source closure does not follow from the denominator calculation. |
| F11 | **CONFIRMED** as a refutation of “unrecorded” | **NBG_ADJ A6**, “Its status is unrecorded anywhere I could find”, and **PROOF [S25-fix 5]**, “recorded NOWHERE”: **BFT_B §12.1 (W-lin-Π)** names the slice inverse bound; **§16.7 EP-lin** and **§18.1 RH-inv** record its conditional route and class restrictions. It is recorded. This does not certify an arbitrary non-cc source operator needed by every perturbation argument. |
| F12 | **CONFIRMED**, only for a separate Z=1, m=0, S_E field obstruction | **PROOF [S25-fix 5]**, “Independent paper-scale obstructions: TWO”, was already marked reverted. With the established invariant inputs, the flat unweighted S_E field conclusion now follows by reconstruction, so it need not be a separate missing theorem in that scope. No count of independent papers, no original per-level weighted closure, and no relation to all versions of GAP-Z is proved. |
| F13 | **CONFIRMED** at Z=1, m=0, on S_E and the (cc) class | **COFUN_CC §6.2 (R1)**, “CC-INV gives nothing here ... the wrong direction”. The inequality alone cannot be reversed, but EP-rec plus RHT-cc supplies precisely the missing direction and GF-E. This is a substantive correction to the extra-obligation list in that scope. |
| F14 | **CONFIRMED** with the target's express restriction | **COFUN_CC “Verdict T2”**, “still OPEN, with (R1) ...”: remove the separate flat unweighted S_E field obligation. The conclusion that the full clause remains open is not refuted; (R2), (R3) and applicable nonlinear source-size conditions remain. |
| F15 | **CONFIRMED** | **BFT_B §32.1(b)**, “independent of the gauge fixing”: §5 supplies a fixed-lattice, fixed-source family violating any uniform field-component version. Only invariant outputs are Γ-independent; use S_E or the orbit norm. |
| F16 | **NOT-VERIFIED** as a refutation of the stated weighted status | **BFT_B §32.2(1)** explicitly includes “with the weighted constants”. A zero-mass result does not make that full statement proved. Its m=0 S_E part should be replaced by GF-E/GF-E′ on their proper classes. The positive-mass implication is §6; the extra “unwritten Hölder half” asserted by GSHARP55 is itself stale. |

Accordingly, **the blanket count “REFUTED 13” is NOT-VERIFIED** as an endorsement of thirteen original mathematical statements being false. There are genuine corrections in that list, but several others establish a replacement formulation, an additional input, or a restricted special case.

### A direct logical error: the fine bound is necessary as an output consequence

Source: **GSHARP55 §0 item 3**, **§6 F8**, and **§7 CODEX_REVIEW_NBG2**, locating “neither piece is necessary”; compare its own **§3.2**, “does contain (G♯_0-fine)'s content”.

For identical sources, data, mass and exponents,

    ||f_0||∞+[f_0]_α
      ≤ ||B||_(X_c)+[f_0]_α.

The fine curvature is gauge invariant. Thus a field estimate in any slice implies the fine estimate with the same source norm and constant. The assertion that the fine piece is unnecessary as a mathematical consequence is **REFUTED**. It need not be an independently assumed lemma in every imaginable proof; that different statement is not a non-necessity theorem. In the target's actual proof it is explicitly supplied through LIN0/W0/GU.

### The original consumers cannot be changed by a source-reading claim

Sources: **PROOF “B-NA-red”, [R1314-fix](2)**; **SF §6.2 “(a5-G♯)”** and **§7.2 “Lemma G-pert”**, especially **[RSF2-fix GP-1/GP-2]**; target **GSHARP55 §2(P-4), §4.1 and §10 item 7**.

The abstract IFT permits a suitably controlled slice. That does not establish its hypotheses on every slice. The actual corrected B-NA-red formulation names the per-level slice, and SF's G-pert proof works in the **trivial-background per-level slice** held fixed at x^r. “TRIVIAL slice” there distinguishes a fixed slice from a re-centered one; it does not identify that slice with S_E. SF explicitly requires either a restatement or a bounded slice-change lemma. Choosing S_E for the current program is reasonable and GF-E supports that choice, but the nonlinear remainder, source-space and gauge-chart hypotheses still have to match the changed formulation. “Nothing consumes that choice” is not a proof that all stated consumer theorems have already been transported.

## 8. Further scope checks

**CONFIRMED — PL-adm as finite-dimensional algebra.** **GSHARP55 §5.5**, locating “Lemma PL-adm”, uses `h_i(dν)=avg_(B(X))ν−ν(c_X)`. Starting at the top, its two zero conditions put λ_i in the pinned, block-mean-zero residual space and give `||dλ_i||₂²=0`. Induction proves injectivity. Per block, value at the root and mean are independent constraints for `L^4>1`, so the target dimension is `Σ_i(N_i−N_(i+1))=N_0−N_k`. Injectivity therefore gives bijectivity. This proves admissibility, not a uniform estimate for its inverse in the field norm. The propagation hole in the target's S_E-to-per-level transfer remains **NOT-VERIFIED**.

**NOT-VERIFIED — the background reconstruction.** **GSHARP55 §5.4**, locating “Status: ARGUED — an outline only”, correctly stops at an outline. The identities `d²=0`, flat root covariance, and the box gauge behavior used above do not simply persist at curved Z. Locality is useful after a covariant local estimate is established; it is not that estimate. This report grants no `(EP-rec)_Z`, no `CC-dec_Z`, and no background orbit-norm equivalence.

**NOT-VERIFIED — unrestricted projected-source closure.** **GSHARP55 §4.3**, locating “Π_E^Ty”, has the correct algebraic projection identity. But `N(Π_E^Ty)≤C||y||` does not follow from the fact that Π_E^Ty is (cc). Boundedness of Π_E in the field norm does not identify the representation norm N with the full dual norm. A perturbation or off-critical remainder must supply the relevant corrected-source estimates. GF-E does not settle that general-source input.

**CONFIRMED — the old review's scope can now be extended.** **CODEX_REVIEW_TOPCC**, “Field components — NOT-VERIFIED”, was explicit about what that review had not checked. Adding the independently checked reconstruction and the residual estimate establishes the S_E field implication. This supplies missing evidence; it does not invalidate TOPCC's invariant-only argument or its warning about arbitrary gauges.

## 9. Exact checks actually executed

One in-memory `python3 -I -B` process used only `fractions.Fraction`, integer arithmetic and `math.comb`, with bytecode disabled. No script, cache, or log file was created. The output was:

    tent partition coefficients: 1,0,0,0,0,0
    tent derivative order 0 at 1: 0
    tent derivative order 1 at 1: 0
    tent derivative order 2 at 1: 0
    GF-DEP 2x2 exact controls: 0, 1, -2, 7/3; all identities hold
    alias denominator rational lower bound: 2192409/3066001
    lower bound minus target 1.0554: 40472216107/625000000000000
    claimed radius conversion: 4+3+5+8+1 = 21 ; in four dimensions ||z||_1 <= 4||z||_infinity

The matrix controls verify the displayed algebra at those rational t; the all-t proof is the symbolic determinant/inverse identity in §5. The strip certificate is the rational majorant proved in §4, not a finite-n numerical test. The last line is an arithmetic/metric reminder, not a support certificate for radius 21. No finite-depth computation is offered as evidence of uniformity in k or T.

## Exactly what may be banked

1. **CONFIRMED — flat unweighted reconstruction and slice identification.** For fixed `d=4`, odd `L≥3`, `0<α<1`, every `k≥1`, `T≥1`, and every configuration x,

       ||Π_Ex||_𝔐 ≤ C_rec (||x||inv+||x_k||_D+N_res(x)),

   with the descended S_E slice on small tori and the named LES-div input. For sources annihilating the composite gauge kernel, EP-opt identifies this representative with the unique slice response. EP-bd and the optimal-gauge/orbit inequalities hold at zero weight. No new multi-level physical-gap input is used by this reconstruction.

2. **CONFIRMED — GF-E.** At `Z=1`, `m=0`, `0<α<θ<1`, for the stated Setting LIN^cc source classes with zero terminal datum,

       ||x_E(S)||_𝔐 ≤ C_GF N(S),

   uniformly in k and T, as an implication of CC-INV, RHT-cc and the independently checked reconstruction. The same bound holds for the orbit norm. It does not hold uniformly for every gauge representative.

3. **CONFIRMED — GF-E′ on S_E.** For RTARGET's divergence-form currents, arbitrary terminal datum, `m=0` and `0<α<θ<1`,

       ||B_E||_(X_c)+[f_0]_α ≤ 4||B_E||_𝔐
         ≤ C [||G||_(Y,α;RTARGET)+||B_k||_D],

   uniformly in k and T, including the infimum over source representatives. The constant may depend on θ. This banks the S_E analogue, not the unproved per-level-slice or positive-mass version. The target's sharper comparison factor 3 remains **NOT-VERIFIED**.

4. **CONFIRMED — GF-DEP and the flat orbit-norm repair.** The explicit Γ_t family has the same admissible gauge derivative, a fixed composite-co-closed source, identical invariant outputs and unbounded field response. Replace arbitrary-gauge field uniformity by a named controlled slice or the orbit norm, equivalent to S_E up to C_Π at the flat background.

5. **CONFIRMED — nonzero-alias denominator analyticity.** On the fundamental-domain tube `|Im z_ν|≤7/5`, `n≥3`, `K≠0`,

       Re φ_K(z) ≥ 2192409/3066001 > 0.

   The whole screened symbol still uses the package's smaller strip and inverse hypotheses. Analyticity alone supplies no uniform fine-offset summability bound; W0/GU supplies the unweighted source estimate used here.

6. **CONFIRMED — conditional weighted reduction with an absolute finite reach.** Weighted invariant control plus RHT_m-cc and the localized reconstruction implies the weighted S_E field bound with a factor `exp(C_*m)` for some absolute C_*. Thus the flat (cc) field half adds no new analytic input beyond the full required (R3). **Do not bank `C_*=21` from the supplied audit.** The claim that GU's Hölder transfer is unwritten is **REFUTED**; Lemma WT already supplies that transfer once the weighted sup inputs hold.

7. **CONFIRMED — only the scoped status corrections in §7.** The S_E, zero-mass field implication can leave the separate open list once its named inputs are accepted. The recorded W-lin-Π route and the false arbitrary-gauge claim should be recognized. **Do not bank “thirteen refutations” without their domains.** The original per-level transfer, background reconstruction, full weighted COF/CC-INV assembly, general off-critical source control, and full nonlinear source-size hypotheses remain **NOT-VERIFIED by this review**.
