# PRE-STATED — independent hostile review of RLOC55

UTC: 2026-10-29 04:57:24. Recorded before derivation. Target: `RLOC55.md`, especially Theorem LOC, Lemmas SUPP/LBC/ZL/RT, the Cauchy and weighted assembly, and checks `rl55_1` / `rl55_2`. All paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` unless explicitly stated otherwise.

The proposed conclusion under test is that premise (R) follows from the named source proofs with constants uniform in depth and torus size, and can therefore be removed from the conditional downstream items. A status label or another reviewer's acceptance is not evidence.

Pre-stated refutation tests:

1. Rebuild the soft-slot powers from SG, centering, the local residual constraint and analytic remainders. Refute a claimed uniform factor if a local configuration satisfies the stated constraints but violates it, or if the proof needs a missing constraint or a different quantifier.
2. Separate the real and complex pairings, gradients, stationarity and holomorphic continuation. Test slotwise vanishing directly rather than infer it from a covector cancellation.
3. Reconstruct support geometry and Wilson pair domains; test whether every required gradient/Campanato box is actually defined on the declared variables, including endpoint and finite-torus cases.
4. Rebuild directional Cauchy estimates and multilinear weights. Look for a lost factorial, dimension factor, unconstrained direction, or unaccounted enlarged read radius.
5. Rebuild routing per output link, including the boundary links actually read; distinguish an exact cell from a padded cell and distinguish a geometric sum from a weighted/local estimate.
6. Locate source statements by strings and compare any numerical line citations. Keep each radius, depth, residual, constant and exponent tied to its definition; reject stale minima and stale input/output roles.
7. Inspect and reproduce the two geometry checks using only exact integer/rational arithmetic in plain Python. A test must admit failure independently of the conclusion it purports to support; passing geometry cannot establish analytic estimates.

Review verdicts will be CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses will be PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. No git commands, no other file writes, no large-file full reads, no numerical libraries or long jobs. Findings will be appended incrementally, with locating strings and observed line numbers. Final banking decisions will retain every premise not actually discharged.

## Findings

### R1. The Wilson-pair ball is not contained in the advertised patch polydisc

**REFUTED as printed; corrected holomorphic-domain argument PROVEN.** Locations: `RLOC55.md:209–217`, locating string `ν_{p,v}(x) :=`; `:271`, `since 𝒦_D(r) ⊂ 𝔻_D(ϱ_A/4)`; `:355`, `all own variables ≤ Lhr ≤ r`.

Take a plaquette in directions 1 and 2, with base point 0, and translate it by one step in direction 1. Its rectangle has coordinates 3 and 4 identically zero. On the enlarged patch set the direction-1 links to `x_1(z)=a z_3 H`, with fixed nonzero `H∈sl(N,C)`, and all other link components to zero. Choose a sufficiently large allowed torus so this patch has a consistent lift. Every value and permitted gradient inside the rectangle is zero. Every gradient on every Campanato box is constant, hence its mean-free oscillation is zero. Thus `ν_{p,v}(x)=0` for every complex a, although patch links at `z_3=1` have arbitrarily large value. The claimed bound on **all patch variables**, and hence containment in a patch-wide fixed polydisc, is false.

This counterexample does **not** refute LOC(L4): both plaquettes' variables vanish. The exact repair is to let `S=∂p∪∂(p+v)` and use the cylinder `{max_{b∈S}|x_b|<ϱ_A}` in the patch space. The pair slot is the holomorphic pullback of its function of S, and the local ball controls every variable in S. Its unbounded seminorm kernel acts trivially on that function. Directional Cauchy therefore remains valid without any extension theorem or variable-count factor. This cylinder/projection statement replaces the false containment; it must not be banked as containment of the full pair patch.

### R2. The soft plain-slot level factor survives a direct local derivation

**CONFIRMED for existence of uniform finite constants; claim status PROVEN as an implication of the local analytic maximizer.** Locations: `RLOC55.md:286–325`, `(L1)` / `(L2)`; `KFACTOR_OFF55.md:133`, `Lemma SG`; `CODEX_REVIEW_KOFF.md:315`, `A_b(x) =`; `BFT_A.md:129`, `3.4 BA-4`; `:1010`, `13.5 Lemma CR-1`; `HIGHER55.md:212`, `Lemma C2`.

Pin `m=k−1−l`, `h=L^{−(m+1)}` (h is a mesh, not HIGHER's depth). The local constraints give `s_l≤hr`, `|v|≤Lhr`, directional oscillation `δ≤(5L−5)h²r`, and, below the top, `|r_l|≤L^{−(2+σ)m}r`. For a direction-constant field a paired word is a conjugate of the straight μ-word; its quadratic logarithm is `L[D,A_μ]`, with `D=Σν(y−c_X)_ν A_ν`. Averaging y kills D **within this density**. Replacing the constant letters costs `O_L(s_l δ+δ²)=O_L(h³r²)`. Stationarity at degree two removes the Hermitian square terms, so the maximizer contributes precisely that averaged quadratic logarithm. The remaining BCH term is `−[v,r_l]/2`, bounded by `L³h³r²`; the analytic tail is `O_L(h³r³)`. Hence `ρ=r_l+O_L(h³r²)`.

The envelope identity is obtained by differentiating `Re tr(W_0^{-1}M)−Re tr(V^{-1}M)`. The derivative of W_0 drops by stationarity at this one c, and `Re tr(ZG)=0` because `G=H+iθI` and `tr Z=0`. Subtracting the linear residual coefficients leaves `A_b=W_0^{-1}∂_bM−Q_cb=O_L(s_l)`, not the false total derivative `∂_b(W_0^{-1}M)−Q_cb`. Thus `|E_c(b)|≤C_L hr|ρ|`, giving exactly

`h^{−3}|E_c(b)| ≤ C_L[L² L^{−σm}r² + h r³] ≤ C'_L L^{−σm}r²`,

since `h/L^{−σm}=L^{−1−(1−σ)m}≤1` for `0<σ≤1`. The upper slot uses `(O_L(|v|)+O_L(s_l²))ρ` and normalization `(Lh)^{−3}`, with the same conclusion. At the top, `|r_data|≤|r_hom|+|B|≤2r` and h is the fixed number 1/L; this changes only an L-dependent constant. No cross-density cancellation, global inverse or global contraction appears. The additive `h r³` defect is essential; setting the linear residual to zero does not set E to zero.

### R3. SUPP and its incidence counts withstand reconstruction

**CONFIRMED; claim status PROVEN for every odd L≥3 in the stated T≥3 setting.** Locations: `RLOC55.md:218`, `Lemma SUPP`; `:444`, `at most 8 soft densities`; `BFT_A.md:130`, `ordered word w·s·w̄`; `PROOF.md`, `Decision 4: the RG kernel`.

Here support means the declared contour-variable support, including variables which may cancel in particular words, rather than an assertion of minimal analytic dependence. In coordinates where the box is `[0,2L−1]` longitudinally and `[0,L−1]` transversely, its longitudinal links number `(2L−1)L³` and its three transverse families number `3·2L·(L−1)L²`. Their sum is **`L³(8L−7)`**: `135+324=459` at L=3 and `1125+3000=4125` at L=5. These are independent combinatorial counts, not numbers extracted from the scripts' expected values.

Containment follows from monotone legs. For the reverse inclusion, any longitudinal link can be covered by a straight L-link leg starting at a permissible y. For a transverse ν-link choose ν last in the axial order, set the other transverse coordinates to the desired link coordinates, and select the ν endpoint on the appropriate extreme face. If its longitudinal coordinate is in the first L-site half, use the go-leg; in the other half use the translated return leg. This covers every box link. For fixed ν the allowable link bases form a rectangle, proving the staircase assertion. Their exact ℓ¹ diameter is `(2L−2)+3(L−1)=5L−5`, also obtained for ν transverse by `(2L−1)+(L−2)+2(L−1)`. Thus 10 and 20 are correct; 5L−4 is a valid looser bound, not an error.

For incidence, each choice of the density's longitudinal direction μ permits at most two longitudinal translates; the transverse block coordinates are uniquely determined if they contain both endpoints. Thus at most `2d=8` same-level soft supports contain a link. The maximum is attained for a link not crossing its transverse L-block face. There is at most one additional soft density from level l−1, located at its own coarse link. There are six Wilson plaquettes through a link. These counts hold for all odd L, not only L=3,5. Finally, the largest local site extent is 2L, whereas the fine period is at least 3L, so no two sites of this patch are identified by periodicity.

### R4. HC's κ-independent sup is false, but local holomorphy has a direct repair

**REFUTED for the printed parameter dependence; corrected claim PROVEN.** Locations: `RLOC55.md:173–177`, `depending only on (N, L)` and the list containing `s_c`; `:355–359`, `Choice of r_L`; `HIGHER55.md:166`, `Lemma AN`.

The analytic radius can depend on N,L alone for the κ-free local functions. The asserted common bound S_A cannot have that dependence when it also bounds `s_c=κ_l(r_hom−Ψ)`. At a top density with x=0 and `B=tH`, one has `s_c=κ_l Π(sinh(tH))=κ_l tH+O(t³)`. Choose a nonzero sufficiently small real t and a nonzero su(2) block H embedded in su(N). Its norm grows linearly with κ_l. Setting (K) imposes no universal N,L-dependent upper bound on κ_+. This is a parameter quantifier error, not a depth loss.

Use a κ-free bound `S_0(N,L)` and either exclude s_c from HC's list or replace the full bound by `S_A=max(1,κ_+)S_0`. The radius remains κ-independent. Use S_0 in the residual calculation, and include κ_+ explicitly in the final bounds for actual slots `s_c` and `−κ_lE_c`. LOC already permits its constants to depend on κ_+, so this correction leaves its intended conclusion intact.

For completeness, the continued stationarity equation is the traceless part of `(e^{−X}M−M̃e^X)/2=0`; its X derivative at the origin is `−id`. A finite local implicit-function theorem therefore constructs X_0, with a common smaller radius over the fixed word types. The real global-maximizer identification can also be rebuilt locally: compactness gives a maximizer W; comparison with I yields `|W−I|²/2≤|W−I||M−I|`, hence `|W−I|≤2|M−I|`. For fixed N, shrink the M neighborhood until every such W lies in the local su(N) exponential chart and the stationarity uniqueness neighborhood. It must then be the implicit-function solution. Complex conjugation is **not** applied to complex coordinates: M̃ is the reversed-inverse-word continuation. All stationarity and SG identities extend by uniqueness on the totally real slice. The local logarithm is traceless because `det(e^{−v}e^{X_0})=1` and `tr log` is continuous, zero at the origin, and takes values in `2πiZ`. This avoids treating `||ρ||<2π/N` as a consequence of an N-independent numerical cutoff. If that sufficient inequality is desired explicitly, shrink the N-dependent radius to enforce it.

### R5. Wilson pair estimates and the corrected boundary convention are local

**CONFIRMED with R1's cylinder interpretation and the target's E1 correction; claim status PROVEN.** Locations: `RLOC55.md:238`, `Lemma LBC`; `:327–353`, `(L3)` / `(L4)` / `(L6)`; `:640`, `2 + 2/n`; `BFT_A.md:628`, `8.4 BL-C`; `:2496`, `Corollary WR`; `BFT4W55.md:212`, `Local constraint sets`.

The original BFT4W constraint-set definition is indeed invalid as a condition on only `x|supp D`: a box meeting the support can read arbitrarily assigned variables outside it. RLOC's soft restriction and single-plaquette restriction avoid that defect. Its pair patch explicitly includes the variables read by its Campanato terms. A box of at most n sites containing an endpoint link base reaches at most n−1 steps beyond it, and a gradient of a link reads at most two further steps in one coordinate. With translation at most n and a plaquette-base offset at most one step, the full pair patch has ℓ∞ radius at most `2+2/n`. The earlier `2+1/n` bound has already been corrected in E1.

Rebuild LBC: two successive dyadic means differ by at most `4 Osc_2` on the larger box in four dimensions. Telescoping up to side between t and 2t costs a geometric series with ratio `2^{−α}`. Comparing both final means through a common box four times larger costs `2·16 Osc_2`. Every box used contains one of the two sampled points; for t>1/8, the two endpoint values suffice. Cauchy–Schwarz is valid for complex HS-valued fields. Thus the displayed C_C and the pair-local choice of Campanato constraints suffice; no outside mean or global extension is used.

On the local rectangle, `|X|≤r/n`, `|X−X'|≤4tr/n`, and the two transverse differences give `|dx|≤2r/n²`. Local analyticity and q's quadratic zero imply `q=O(r²/n²)`, `K=D_bq=O(r/n)`, and `Δq=O(tr²/n²)`. Hence `F=O(r/n²)` and `j=−K^T∇W(F)=O(r²/n³)`. For the pair difference use `Δ(K^T∇W)=ΔK^T∇W+K'^TΔ∇W`: LBC bounds the curl difference by `O(rt^α/n²)`, while `ΔK=O(tr/n)`. This gives `n³|Δj|≤C r²t^α`. The divergence slot `−q−g_3(F)` uses the same Δq estimate and `n^{−4}≤t^α`, since `t≥1/n` and α<1. Every factor is local to the stated patch. The cutoff identity `Δ(ηw)=ηΔw+(Δη)w'` adds at most `2d sup|w^c|` to the Hölder quotient, using `|∂μη|≤2`; the actual W-cut proof gives the stronger first-derivative bound 1, so 2 is safe.

The soft energy formula is quadratic in ρ after stationarity removes `tr(ρG−G'ρ)/2`. Its per-level density count multiplies the two bounds by `L^{4m}`, producing `L^{−2σm}r²` and `L^{−6}L^{−2m}r⁴`. Both sum at fixed σ>0. The top-density subtraction vanishes at x=0 and is `O((ν_c(x)+|B_c|)ν_c(x))`; the Wilson energy is `O(n^{−4}r²)`. Thus the complex local input to E2/E3 is also supplied, without a global contraction.

### R6. Slotwise cancellation and directional Cauchy survive; the corrected weight quantifier is essential

**CONFIRMED after R1/R4; claim status PROVEN.** Locations: `RLOC55.md:375`, `Lemma ZL`; `:395`, `Corollary PW′`; `:417`, `Multilinear weights`; `CODEX_REVIEW_BFT4W.md:32`, `W2`.

The residual slot has x-linear part `κ(R_cx−R_cx)=0`, with the top data term `κB_c` retained. The two fine plain factors Θ and A each vanish at zero; the coarse plain terms contain `(Z−id)Θ` or `Θ(G−I)`. Wilson G starts quadratically and Wilson j is a product of two vanishing factors. Consequently **every chosen slot**, including pair differences, has zero x derivative at (0,0). This is stronger than cancellation of the assembled covector.

For a normalized direction u, the two scalar parameters in `Φ(tx+zu;tB)` have radii `r_L/(2η)` and `r_L/2`. Cauchy gives `|∂_zΦ|≤2M/r_L`; its value at t=0 vanishes, so Schwarz gives `4Mη/r_L²` at t=1. Directions in the seminorm kernel act trivially by R1. For p+w directions introduce distinct scalar parameters, each of radius `r_L/(2(p+w))`, and differentiate once in each. This yields exactly `M(2(p+w)/r_L)^{p+w}` times the direction norms. There is no missing factorial and no dependence on patch cardinality. At p+w=0 one uses the sup bound directly, rather than the displayed division by zero; the derivative formula is for p+w≥1.

For weights, each input seminorm is the maximum of its finitely many local quantities. At the maximizing base point z_i, it is at most `e^{−μF_i(z_i)}||u_i||_{μ,F_i}`. If each F_i is 1-Lipschitz and `F(z)≤Σ_iF_i(z)+Σ_jd_1(z,y_j)`, multiplying the estimates gives the factor `e^{(p+w)ρ_Sμ}`. The same-weight multilinear assertion without this compatibility is not recovered. Polarized differences follow by integrating P1 on the convex local ball, including the `h^{−3}(ρ−r)` normalization used in E3 of the target.

### R7. RT's inequality is local, but the full input does not lie in the output's cell

**CONFIRMED for RT's displayed inequality and fixed-radius locality; REFUTED for literal cell-only locality of the density-input bound. Corrected claim status PROVEN.** Locations: `RLOC55.md:427–442`, `Lemma RT`; `:448`, `read in the cell of b′`; `:460–462`, `Read radius`; `:476`, `reads only the output's cell`; `KFACTOR_OFF55.md:246`, `Lemma HR`.

For a charge at z, summing the nested path divergences gives `δ_z−δ_root(cell(z))`. Root charges have empty paths. For an input at level l, paths below l are empty. At output level i≥l, summing `d*w_l` on one i-block cancels its internal links and leaves `d L^{3(i−l)}` opposing boundary pairs. The largest axial-path multiplicity is `M_γ=L³(L−1)/2`: it is attained on the first-coordinate link next to the center on one side. Therefore the sup bound, after coarse normalization, is

`L^{3(k−i)} M_γ 2d L^{3(i−l)} L^{−3(k−l)} max π_l = 2dM_γ max π_l`.

For l=0 the two members of each opposing pair are exactly `L^i/n` apart, giving instead `dM_γ L^{−α(k−i)}` times its local Hölder quotient. This is a cancellation within that one routing block, not cancellation of different nonlinear densities. The exact sums are

`Σ_{m=0}^{k−1}(m+1)a^m=[1−(k+1)a^k+ka^{k+1}]/(1−a)²≤(1−a)^{−2}`, `a=L^{−σ}`,

and `Σ_{i=0}^{k−1}L^{−α(k−i)}=(1−L^{−αk})/(L^α−1)`.

The current-level input is precisely the links Λ(b′) with an endpoint in the parent block, **including crossing links**, as RT actually defines. After substituting `w=Σ_D plain(Y_D)`, a contributing density can have its other half in the adjacent cell: Box(c) is two neighboring L-blocks when c joins their roots. Its ν_c bound explicitly reads that other half. Likewise the Wilson-pair Campanato boxes can extend outside the routing cell. Thus the cell-only sentence is not an accurate statement of the bound on the original field variables. The exact correction is **Λ(b′) for current inputs; the union of the contributing density/pair patches for field inputs**.

This does not produce a growing read radius. A routed output and a current input with an endpoint in its cell have coarse ℓ¹ separation at most `4+1/(2L)<9/2`. For a Wilson term, the input-link midpoint and the plaquette base differ by at most `3/(2n)`. The corrected pair patch costs at most `4(2+2/n)`. Their sum is at most `9/2+8+19/(2n)≤47/3<16`, since n≥3. Soft inputs cost less than `9/2+5<16`. Thus the advertised **ρ_S=20 remains valid**, with a fixed neighborhood in place of the literal cell. Small tori use periodic images of these patches; every individual Campanato box has side ≤1<T and is well defined. Identifications in the union of boxes merely repeat coordinates.

Divergence slots have zero composite divergence; residual slots have zero **off-root** divergence. At the top their full divergence can be root-supported. Equivalently, `R_c Ξλ=0` is used on root-pinned λ. No `(CC-0)` premise is being smuggled into RT or CB. Multiplying a residual/divergence slot before applying its defining transpose keeps this property. The cutoff Hölder argument of R5 then supplies the localized F^σ estimate.

### R8. The factor-six concern is real bookkeeping, not a refutation of the whole printed K_1

**NOT-VERIFIED for the literal BFT4W K_1; CONFIRMED for RLOC F11's reservation and existence of a safe finite replacement.** Locations: `RLOC55.md:568–572`, `The explicit K_1 formula`; `BFT4W55.md:249–260`, `Proof of Theorem H3` / `K_1 :=`.

With c_W interpreted as a **per-plaquette/per-pair** bound, a current-link pair contains six translated plaquette pairs. Its routing contribution is therefore `6dM_γ c_W/(L^α−1)`, not the single-pair contribution `dM_γ c_W/(L^α−1)`. This establishes the missing multiplicity in that derivation. It does not prove that the entire displayed K_1 is numerically too small: c_W,c_S,N_inc are uncomputed majorants and the other positive terms can provide slack. Keep the literal total formula NOT-VERIFIED, as the target does.

A fully specified safe alternative is available. Let c_W bound all normalized individual Wilson slots/pairs by `c_W r²`. Let c_S bound the **actual** normalized soft slots, including κ_l, by `c_S λ r²`, with the top bound `c_S(r+r²)`. Set `a=L^{−σ}` and `A=4(1+1/r_L)`. R3 and P1 then give the sufficient choice

`K_safe = A [8c_W + c_S + 9c_S/(1−a) + 18dM_γ c_S/(1−a)² + 6dM_γ c_W/(L^α−1)]`.

The terms are, respectively: Wilson value/Hölder and six direct plain contributions; the residual maximum; at most nine direct soft contributions per level; their sup-route geometric sum; and the six-pair Wilson Hölder route. The level-(l−1) neighbor has factor `a^{k−l}≤a^{k−1−l}` and is safely included in nine. This replacement is uniform in k,T,μ,f at fixed α,σ, and uses precisely the corrected κ convention. It supplies H3(a)'s existence constant, but it is **not** an evaluation of the printed K_1.

### R9. Geometry replays pass; several gates cannot independently decide the stronger claims

**CONFIRMED for present finite execution and the reported counts; NOT-VERIFIED for historical pre-registration timing.** Locations: `RLOC55.md:523–537`, `Check record`; `checks/rl55_1.py:122–168`, P4/P5; `checks/rl55_2.py:90–116`, Q1/Q2/K1; both named criteria files.

Both scripts were inspected before execution, then run sequentially with `python3 -I -B`, without redirection or file writes. Both returned exit 0. rl55_1 printed P1–P5 PASS for L=3,5 and all three controls FIRES at both L. Its exact incidence-frequency maxima were **83/81** and **629/625**, with maximum support incidence 8 and diameters 10,20. rl55_2 printed Q1/Q2 PASS, control FIRES, and **459 / 4125** at each of the four orientations. The y=center control has exactly L links, hence 3 / 5. These outputs match the stored output files.

The discriminating scope of each gate is narrower than a generic PASS suggests:

| Gate | Can it decide its claimed geometric property? | Limitation / independent mechanism |
|---|---|---|
| rl55_1 P1 | Yes: a wrong box or displaced y-range can fail | K1/K2 fire; this is containment, not analyticity |
| P2 | Yes: missed extreme faces can fail | Tests tight bounding faces, not filling of the box |
| P3 | The diameter comparison can fail; K3 fires | The rectangle-in-Box clause follows from endpoint containment and rectangular convexity. It does not show all intermediate links belong to the word support |
| P4 | Only as a path/endpoint sanity check | Signed counts telescope to the common endpoint displacement for **every** such word, even without a centered y-average. It cannot test the BCH₂ cancellation |
| P5 | Redundant after P1 for these same enumerated supports | `n_c≤n_box` follows from support containment. No gate asserts `max n_c=8`; the number is reported. R3 proves eight independently |
| rl55_2 Q1 | Yes | Compares independently generated box links and word links; the one-y control fails equality |
| Q2 | A hole can fail its rectangle tests | Q1 plus rectangular convexity already implies it; it is not an additional independent proof |
| rl55_2 K1 | Yes for loss of the full y-family | Actual output is a strict subset. It does not test complex estimates or higher orders |

For a concrete P4 blind spot, use the uncentered offsets `{0,…,L−1}⁴`. The signed μ count is still L, while the average coefficient of `[A_ν,A_μ]` in `L[D,A_μ]` is `L(L−1)/2`, equal to 3 and 10 at L=3 and 5. This is why P4 cannot authenticate centering. The overall geometry check still rejects that mutation through P1; it is not a tautological overall PASS. No analytic theorem is inferred from these checks. Their mtimes and self-reported timestamps do not independently establish historical criteria-before-script order.

### R10. The quoted PROOF line locations have already drifted again

**REFUTED as current line citations; source content identity CONFIRMED for the bounded NA-alg passage.** Locations: `RLOC55.md:73–74`, `now at l.3232-3266` / `drift +17`; `:11`, `PROOF.md l.1-35`; `KFACTOR_OFF55.md:134`, `PROOF l.3207-3222`.

At 05:04:10 UTC, locating by string placed NA-alg at **PROOF.md:3238**, and the previously reviewed 36-line passage at **3238–3273**. Its SHA-256, computed only from that bounded sed range, is `f7b709739edd89484ec5d67e8e601e66e45aad91047fac94002cf9bc9cd8c50d`, exactly the passage hash recorded in `CODEX_REVIEW_HIGHER.md:295–296` for **3215–3250**. Thus the verified current shift is **+23**, because `3238−3215=23` and `3250+23=3273`, not +17. The heading was at 3236 on this review's earlier read: PROOF moved concurrently even during this review. These are timestamped observations, not a promise that later line numbers will remain fixed.

The current BFT-4(a) `(R)` summary is at **PROOF.md:39**, outside the quoted 1–35 range. The old KFACTOR citation 3207–3222 points to the PG physical-gap material rather than NA-alg. Use the locating strings `Lemma NA-alg (explicit su(N) algebra`, `Stationarity`, and `BFT-4 (a) on 𝒞_glob`; no scientific status is inferred from those summary lines. This is source-location drift, not evidence that the local analytic content changed.

**Final bounded recheck, 2026-10-29 05:21:28 UTC:** NA-alg had moved again to **3239–3274**, now **+24** from 3215–3250, with exactly the same passage hash. The BFT-4(a) summary remained at 39: the drift is nonuniform. The latest corrections to the target's citation are therefore `3232–3266 → 3239–3274` and `+17 → +24`; the older KFACTOR 3207–3222 citation must likewise be replaced by the located NA-alg passage. RLOC55 itself remained unchanged at the recorded size and mtime on the final check.

### R11. The Wilson citation changes the meaning of s and loses a factor sixteen

**REFUTED for the claimed source conversion; NOT-VERIFIED here for the sharper inherited coefficient 9 on its original whole domain.** Locations: `RLOC55.md:120`, `Wilson q: ... ≤ 9η²`, citing BA-3; `BFT_A.md:122`, `|q_p| ≤ 9s_j² ... PROOF l.3512`; `PROOF.md`, `Elementary bounds` / `(BCH) If x_1, ..., x_n`, observed at 4306–4310 on the final targeted read.

The cited source defines **`s=Σ_i|x_i|`**, whereas BA-3 uses **`s_j=max_b|x_j(b)|`**. For four plaquette letters, the cited estimate implies

`|q_p|≤9(Σ_{i=1}^4|x_i|)²≤9(4s_j)²=144s_j²`,

under `4s_j≤1/4`. Thus **9 must be replaced by 144 when that particular bound is the justification**. The underlying elementary proof is local: for `Y=Πe^{x_i}−I`, its exponential tail is at most s² and `|Y|≤2s≤1/2`; the logarithmic tail is at most `|Y|²/(1−|Y|)≤8s²`. This rebuilds the 9 in total-word units and exhibits the missing factor 16 in the one-link conversion. The proof also works for sufficiently small complex matrices by HS submultiplicativity.

This is **not a counterexample to the sharper inequality `|q_p|≤9s_j²`**. Its quadratic part is bounded by 6s_j², so a separately controlled tail can give a sharper bound on a smaller neighborhood. What is refuted is the assertion that the cited elementary estimate already gives coefficient 9 in link-size units. The old PROOF:3512 reference currently points to `(S6) Ψ = ...` in a different argument; locate the actual BCH paragraph by string. RLOC's LOC(L3) instead uses `2S_0ϱ_A^{−2}` and its own radius choice, so its finite-constant local theorem does not rely on this erroneous conversion. The qualitative banking decision below survives; the inherited numerical 9 is not certified by this review.

## Bound-by-bound disposition of premise (R)

The CONFIRMED entries below concern the **local complex estimates with finite constants**, after R1/R4/R7's corrections. They do not certify every inherited printed numerical constant. Each named underlying proof was located and its relevant passage read; no aggregate-to-density inference is used.

| Bound / source location | Rebuilt local mechanism | Verdict |
|---|---|---|
| ROW(a), BCH₂ row; `BFT_A.md:887–891`, `Soft rows (second order, level l)` | `2κ〈r_c,B_c(x,u)〉`; a fixed finite quadratic word form has derivative `O_L(s_l)`, so its slot is `O_L(s_l|r_c|)`; all arguments belong to this c | CONFIRMED |
| ROW(a), BA-6 residual; `BFT_A.md:152`, `3.6 BA-6` | Direction-constant cancellation plus the internal staircase bound gives `O_L(h³r²)`; the `[v,r]` term is local as in R2 | CONFIRMED |
| ROW(a), CR-1; `BFT_A.md:1010`, `13.5 Lemma CR-1` | At this c, trace cyclicity gives `〈r,[u_v,r]〉=0` and moves the other commutator into `(κ/2)[v,r]`; no sum over c is involved | CONFIRMED |
| ROW(a), Wilson q and plain quadratic current; `BFT_A.md:120`, `BA-3`; `:2496`, `Corollary WR`; `KFACTOR_OFF55.md:183–190` | Four-variable Taylor expansion, translation staircases, and pair-local BL-C; six incidences enter only upon assembly. R11 excludes certification of the inherited coefficient 9 | CONFIRMED for the finite-constant local form |
| ROW(b), SG / LA-1′ / LA-2; `KFACTOR_OFF55.md:133`; `CODEX_REVIEW_KOFF.md:315`; `HIGHER55.md:212` | Envelope at one maximizer, `A_b=O(s_l)`, and the locally improved residual; R2 retains the additive defect | CONFIRMED |
| KOFF §4.3 (1), residual and difference; `CODEX_REVIEW_KOFF.md:349–366` | Local `h³r²` bound and directional Cauchy/segment integration, with the local gradient and residual constraints retained | CONFIRMED |
| KOFF §4.3 (2), both plain output levels; `:368–377` | R2's fine and coarse normalizations; κ is included in actual current constants | CONFIRMED |
| KOFF §4.3 (3), residual source; `:379–387` | `Ψ−r=(ρ−r)+O(ρ³)` and `L^{(2+σ)m}h³=L^{−3}L^{(σ−1)m}≤L^{−3}` | CONFIRMED |
| KOFF Wilson all orders; `:389–407` | R5's per-pair product estimate, then R6 for differences/derivatives | CONFIRMED |
| CB; `KFACTOR_OFF55.md:305`, `Proposition CB` | One-block flux cancellation followed by summable nonnegative level majorants; R7 | CONFIRMED |
| Cutoff plain-current Hölder; `BFT_B.md:1238`, `W-cut`; `BFT4W55.md:495`, `F^σ` | `Δ(ηw)=ηΔw+(Δη)w'`, with bounded first derivatives of η; R5/R7 | CONFIRMED |
| Complex energy input; `BFT4W55.md:507`, `Explicit holomorphic forms` | Stationarity removes the linear ρ term; R5's density and level power count | CONFIRMED |

HIGHER's alternative FAC/HS decomposition was also read (`HIGHER55.md:261–310`). Its identities and remainder products are per c before the bounded-overlap sum; the equality `κρ^(2)+s^C=κ avg BCH₂` cancels two terms **of the same density**. That representation is different from SG's chosen slots. No improved derivative in an unconstrained single-link direction, and no geometric level-zero Wilson decay, is inferred from it.

## Symbol, minimum and evidence boundary

The relevant symbol assignments are `m=k−1−l`, `h=L^{−(m+1)}`, `r_l=Q_lx_l−v`, `ρ=log(e^{−v}W_0)`, `ϱ_A` the own-variable analytic radius, and `r_L` the local-constraint radius. KOFF's q=k−l is m+1; HIGHER review's h is a depth and is **not** this h. κ_l multiplies the actual soft plain current; E itself is κ-free. The local C_1/C_2 used in LOC(L4) are derivative bounds of q and K in that proof, not numerical constants imported from other files. No cross-file comparison of generic C_1/c_1 symbols was accepted. R4 identifies a real parameter-quantifier error in S_A; R11 identifies a real total-word-size versus single-link-size collision.

After choosing a genuine κ-free analytic radius/bound and C_ρ, the displayed minimum for r_L can be taken (or shrunk) once, before applying directional Cauchy. It contains no k,T,l-dependent input. σ is used only in inequalities valid throughout 0<σ≤1, not evaluated at an obsolete endpoint. The inherited smallness thresholds must use the resulting radius and a justified H3 constant such as K_safe; this review certifies no numerical threshold obtained by inserting the unverified printed K_1. The target's E2 already repairs its `cosh(1)/6≤1/4` intermediate inequality by working at t≤1/2; the final cubic majorants used here remain valid.

Only the requested deliverable was written. No git command, other source edit, audit-ledger read, snapshot read, or numerical-library job was used. The procedural reads were the supplied `SCIENCE_WORKFLOW.md` and its repository `skills/review-loop/SKILL.md`; scientific reads stayed with the user-named target/source/review files and the named rl55 check artifacts. Large sources were located with rg and read in bounded sed ranges. BFT34's route implications were not re-audited from their separate source files: the dependency updates below use the already stated conditional interfaces in the permitted BFT4W sources. The target inspected through its final E5 has 71,945 bytes and recorded mtime epoch 1793249781; no claim of a git revision is made.

## Summary table

| Finding | Verdict on the printed claim | Bankable corrected claim |
|---|---|---|
| R1: pair-patch polydisc containment | REFUTED | PROVEN holomorphic pullback on the endpoint-variable cylinder |
| R2: soft `L^{−σm}` factor | CONFIRMED | PROVEN local estimate, with the nonlinear residual defect retained |
| R3: SUPP, 459/4125, incidence eight | CONFIRMED | PROVEN for every odd L≥3, T≥3 |
| R4: S_A independent of κ_+ while bounding s_c | REFUTED | PROVEN with κ-free S_0 or `max(1,κ_+)S_0` |
| R5: LBC, Wilson pairs, energy input | CONFIRMED with stated corrections | PROVEN local complex estimates and fixed pair patch |
| R6: ZL, scalar Cauchy, compatible weights | CONFIRMED | PROVEN; no variable-count loss; compatible multilinear exponents required |
| R7: RT inequality / full cell-only input claim | CONFIRMED / REFUTED | PROVEN on the union of local patches; `ρ_S=20` remains valid |
| R8: literal printed K_1 | NOT-VERIFIED | PROVEN existence; explicit sufficient K_safe supplied |
| R9: geometry execution / historical timing | CONFIRMED / NOT-VERIFIED | Finite geometry only; redundant gates identified |
| R10: current line citations / NA-alg content | REFUTED / CONFIRMED | Timestamped corrected range and matching bounded-passage hash |
| R11: total-word s read as one-link s_j | REFUTED source conversion; sharper 9 NOT-VERIFIED here | PROVEN cited-bound conversion to 144; qualitative LOC unaffected |

## Exactly what may be banked, and which items lose (R)

**The corrected qualitative premise (R) is CONFIRMED; claim status PROVEN as an implication of the stated local finite-word setup and its local maximizer/analytic identities.** Bank the complex per-density/per-pair bounds, slotwise cancellation, weighted directional/multilinear estimates, cutoff Hölder estimates and routing bounds with **R1's cylinder interpretation, R4's κ convention, R7's neighborhood convention, and a justified finite H3 constant**. A bare endorsement of every literal statement of RLOC55 is not bankable. The original aggregate-to-local inference remains invalid in general; the explicit local derivations, not that inference, discharge this instance.

| Currently conditional item | Dependency update justified by this review |
|---|---|
| Theorem H3(a)–(d), including its Lipschitz/multilinear use | Loses (R); PROVEN from the corrected local estimates, compatible weight quantifiers and HR |
| Lemma F^σ | Loses (R); PROVEN as the localized nonlinear estimate, with the cutoff and corrected local-neighborhood bounds |
| E2^σ / E3^σ complex local-density input | Discharged; the existing energy/Cauchy implications can use R5, with their prior corrections |
| BFT-3 route C | Loses its (H3)_μ / (R) obligation; remains CONDITIONAL on (H1), (H2)_μ and the existing route's stated scope |
| BFT-3 route T | Loses its (H3)^Lip_μ / (R) obligation; remains CONDITIONAL on (H1), (H2)^Lip_μ and the existing route's stated scope |
| Nonlinear decoupling family, Dcc/UQ/IDcc | Loses (R)/F^σ as an extra analytic premise; retains its named linear, Ward and projection inputs, and Dcc's restriction to cc sources |
| BFT-4(a) on 𝒞_glob | Loses (R) only. Remains CONDITIONAL on the corrected contraction/linear package and (GV), (EP) at zero weight, CD, H2W's zero-weight local-torus response/projection bounds, Ward/CCP inputs, and W8's corrected all-torus prefactor plus `ε≤ρ_E/C_0` |

No promotion is made for BFT-4(b), local gauge invariance of polymer pieces, the per-level branch identification, data outside 𝒞_glob, a weighted inverse, a numerical value of r_L or K_1, or the proof project's tally. **Single most dangerous unverified quantity in this target: the literal printed K_1 as an input to downstream smallness minima.** A finite replacement is proved above; its existence must not be confused with certification of that inherited expression or of a previously evaluated threshold.

