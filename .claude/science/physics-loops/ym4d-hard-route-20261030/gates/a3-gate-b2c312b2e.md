# Gate of `library/a3-response.md`, sections 2–7
Provenance: OpenAI Codex (GPT-6; exact runtime variant and reasoning-effort setting not exposed), checkout `b2c312b2e4f721ddbb488d1810a490d71106242c`; Sussman–Alpoge source `31a47c543775`; research-text hand check, not an audit, grants no status.

Scope: queue row 77, A3. Source line numbers below refer to this checkout, not the note's older header pin `7cd8b4f0f`. The outline was fetched once to `/tmp/sa_ym4.tex`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for A3, the background/straightening setting and the comparison target. Balaban and Dimock are credited by the source for the multiscale averages and response problem; their theorems are not imported as proofs here. No numerical, symbolic or enumeration run discharges any step. Only this report is edited. The workflow document named by AGENTS.md is absent from this checkout.

Verdicts concern the submitted statements and arguments: **ADVANCE** means a useful estimate survives this hand check; **CORRECT-NO-ADVANCE** means a valid identity or conditional implication without closure of its inputs; **WRONG** includes a false statement or an essential unproved inference (distinguished below). A broken proof is not, by itself, a counterexample to its conclusion.

## 1. Setting and initial normalization

The block average is the straight-path average (77), not the original contour-corrected average. For an unwrapped double block of side parameter `s`, its tent has values `1,2,…,s−1,s,s−1,…,1` and `s³` transverse copies. Thus, exactly,

\[
 \|\rho_c\|_2^2=s^{-8}s^3\left(s^2+2\sum_{r=1}^{s-1}r^2\right)
 =\frac{2}{3s^2}+\frac{1}{3s^4}.
\]

**Defect 1 (first numerical failure, line 83):** the claimed upper bound `2/(3s²)` drops a positive term. In particular the level-zero row has norm one. Replace every consequent `0.82/s` by `1/s`, or by the exact square root above. This repair is proved by the displayed sum; it does not repair the geometric arguments below. Boundary and wrapping conventions also need specification: the asserted cubes `D_P⊂Ω₀` are not supplied for layer-zero pillars on `∂Ω₀`, and an arbitrary compatible torus need not contain an embedded cube of side `5Lξ_P`.

## 2. The local lemmas

### Lemma 1 — ADVANCE (box estimate only)

No step fails on an ordinary rectangular lattice box. Redo the count: write its side cardinalities as `n_r≤l`. In the strip for a bond in direction `i`, a plaquette in directions `i<j` fixes the coordinates of `x` before `j` and of `y` after `j`. If its cut in coordinate `j` separates `a` sites from `n_j−a`, the number of contributing `(x,y)` is
`(|D|/n_j)·2a(n_j−a)≤|D|l/2`. The strip has at most `3l` plaquettes. Jensen, then Cauchy–Schwarz, followed by summation gives `||A−dω||²≤(3/2)l²||dA||²`; `sqrt(3/2)<1.23`. Telescoping gives the asserted sign of `A−dω`. This proves no extension across a hole or a wrapped torus box.

### Lemma 2 — ADVANCE (box estimate only)

No step fails. The coordinate path has length at most `4l`; the same cut count for a bond is at most `|D|l/2`. Averaging `|f(x)−f(y)|²` bounds `||f−Av f||²` and gives `2l²||df||²`; `sqrt(2)<1.42`. Degenerate sides have no corresponding edges and cause no exception. The exact variance identity could improve the constant but is unnecessary.

### Lemma 3 — WRONG as stated; repaired identity/estimate is CORRECT-NO-ADVANCE

The telescoping identity `q_c(dω)=Av_{B(c_+)}ω−Av_{B(c_-)}ω` is exact. The first failing step is the norm used at line 149 (Defect 1). Taking `ω=0`, `s=1` and `A(c)=1` would require `1≤0.82`. The complete repair is

\[
 |Av_{B(c_+)}\omega-Av_{B(c_-)}\omega-q_c(A)|
 \le s^{-1}\sqrt{2/3+1/(3s^2)}\,\|A-d\omega\|_{D(c)}
 \le s^{-1}\|A-d\omega\|_{D(c)}.
\]

### Lemma T — WRONG as written; a triangular repair is visible

The same-level construction works. Indeed
`sum_{w=1}^W w=W(W+1)/2` and `sum_{w=W+1}^{2W}w=W(3W+1)/2`, so each half moment vanishes. The total mass is `1+4W²/(3W+1)≥1+W` (including `W=0` separately). The transverse mass is `(m+1)³`, giving the normalization in line 165. Only transverse differences contribute to the curl. These facts give an absolute curl-energy bound, including `s=3`.

At a seam the profile must be reflected if the coarse pillar is the right endpoint. Truncating to the coarse half preserves the unwanted-row moment cancellation, but **requires renormalization**; its mass is now `1+2W²/(3W+1)`, not the previous mass. A fine row cannot read its interior bonds, and cannot read its face bond either: its two fine endpoints must both be outside the coarse region. Conversely, an outward coarse row can read fine bumps in its outer coarse block. An interior coarse row cannot. Separation prevents a bump at an outer seam from also reaching the next inner seam. This is the reason a two-step cross-level chain vanishes; triangularity alone would not imply that.

**Defect 2 (first exact failure of the assembled inverse, lines 180–182):** the first sum runs over all `c`, and the second adds the outward coefficient `β(c')` a second time. Set `β` equal to one on a single outward coarse row and zero elsewhere. There is no fine residual; the displayed formula gives `Tβ=2φ_{c'}` and `q(Tβ)(c')=2`, not one.

Repair: define `Rβ=Σ_c β(c)φ_c` using normalized, correctly oriented seam bumps, and `K=qR−I`. The support argument above gives `K²=0`. Then

\[
 T=R(I-K),\qquad qT=(I+K)(I-K)=I.
\]

Equivalently, sum the original coefficients only on nonoutward rows and use the residual coefficient on outward rows. For the bound, use a row **and a column** count: a cross-level entry is `O(L^{-3})`, a coarse row reads `O(L⁴)` fine bumps, and a fine bump meets `O(1)` coarse rows. Thus `||K||_{2→2}≤C/L`, uniformly in depth and volume. Bounded bump overlap gives `E(Rβ)≤C||β||²`, hence `E(Tβ)≤C(1+C/L)²||β||²`; this is absolute for `L≥3`. The correction has exactly the support claimed in T. This repairs the structural estimate, not its printed numerical constants: already `8·86016·(1+48/3)²>10⁷`, and the one-sided normalization also changes the bump constants. No computation is needed for these checks. An embedded-block/periodization convention is still required on the smallest tori.

### Lemma P — WRONG as a complete proof; no counterexample to the estimate established

**Defect 3:** the seam proof omits cases its quantifiers include. The first undefined application is line 195 when `D_P` is not an embedded box. More locally, the transition proof at lines 211–214 uses `||A−dω_P||≤a_P` for a layer-zero `P`, although line 197 set `ω_P=0` without giving that estimate. On a neighborhood reaching into a coarse pillar it is false that this residual is bounded by curvature: take `A=dμ`, with `μ` supported inside that coarse pillar and of mean zero there. All pillar means of `μ`, all rows `q(A)` and `dA` vanish. The coarse local primitive is `μ`, while the prescribed layer-zero primitive is zero; their difference need not have zero gradient on the stated enlarged transition box. The asserted transition bound would give zero. This attacks the transition estimate, not the final restricted-gauge inequality (for this example the correct gauge is `μ`).

The cross-level mean comparison itself is repairable; it must be a comparison through **averages**, not an ordinary chain of pillar means. In a coarse outer block `Z`, write its mean as `L^{-4}Σ_{P⊂Z}m_P`. Fine-grid paths of at most `4(L−1)` links bound each `m_P−Av_Z ω` by that many times the largest fine mean difference. An outward row then compares `Av_Z ω` with the adjacent coarse mean. For corner contacts, use at most four neighboring coarse cells. Each is either a coarse pillar or a full `L⁴` array of fine pillars; compare two fine arrays by averaging translated fine paths. This takes `O(L)` links, stays within the stated enlarged cube on an unwrapped patch, and proves the asserted *type* of bound after replacing `0.82` by one. It also handles a detour whose intermediate cells are coarse. Separation excludes a third scale on this patch.

Visible local repair: use the box primitive normalized at the site also for layer-zero transition charts. On a layer-zero boundary neighborhood containing no coarse pillar, simply use `A(c)=q_c(A)` and `λ=0`; separation ensures such boundary neighborhoods are entirely at level zero. Recheck the transition boxes with these choices. The discrete partition product rule (223) is correct, as is the mean-correction identity in (230); mean-one bumps supported on disjoint pillars do impose `Av_P λ=0`. The overlap counts are finite functions of `L`, not of depth. The printed collection into `10¹⁶L¹²` is not derived by the displayed estimates, and a wrapped-patch case is absent. These repairs and a fresh constant collection are required before accepting P on its full stated domain. They are not supplied by labeling the patching “local.”

## 3. Theorem FL — WRONG as an unconditional completed proof

First failing dependency: line 241 invokes the incorrect assembled T, and line 254 invokes P on its unchecked full domain. With a genuine right inverse, existence follows because a quadratic least-squares problem on a nonempty finite-dimensional affine space attains its minimum; the midpoint identity proves uniqueness of `dA_B` and gives the initial energy bound. Gauge invariance is valid because `d²=0` and every determining endpoint block is a pillar or a union of finer pillars.

The cutoff/competitor argument is otherwise a valid mechanism. Define the transition rows by **nonconstant cutoff on their support**, including threshold endpoints. Then `β=q(χA~)−B`, `qTβ=β`, and `A'=χA~−Tβ` is admissible. Its changes are confined to a bounded metric enlargement of the transition zone. Subtracting the common inner energy gives (3.1). The product-rule error is bounded by `CΣ ξ^{-2}|A~|²`; the repaired tent estimate bounds each row residual. At a seam use the finer endpoint scale in this error estimate.

**Defect 4 (the uniformity step, line 274):** a per-pillar estimate cannot be summed without counting how often its enlarged read set contains a given plaquette. The proof inserts no such multiplicity in `C₁=4+10¹⁰C_P`. This is particularly consequential at a seam, where a coarse chart is read by many fine pillars. It is **not** evidence of an unavoidable depth or volume loss: the missing packing bound has a direct repair, conditional on P.

For completeness, that repair is as follows. If a plaquette in layer `ℓ` belongs to `N(P)`, separation and the collar widths put the layer of `P` in `{ℓ−1,ℓ,ℓ+1}`. A chart contributing to `N(P)` has side at most `5L²ξ_P`; all its centers lie within `C L²ξ_P` of `P`. For each of the three possible layers, centers have spacing `ξ_P`, so at most `(C L²+3)⁴` such centers can read a fixed plaquette. The same argument bounds the row-support multiplicity (more sharply, only two neighboring levels can read a bond). Periodization, once defined, can only reduce the number of distinct centers; it must not silently count repeated copies as new data. Thus one may use

\[
 M(L)\le 3(C L^2+3)^4,\qquad
 C_1^*(L)=C\{1+C_T+C_P(L)M(L)(1+C_T)\},
\]

where the numerical `C` is chosen larger than the fixed product-rule and edge-incidence constants. This keeps `C₁*` free of depth, region volume and support size; the printed value of `C₁` is not justified. Once the corrected local estimates and this packing bound hold, (3.1)–(3.2) give
`f(a+Δ)≤θ f(a)`, `θ=C₁*/(1+C₁*)<1`, with any sufficiently large fixed `Δ=C(L)`. Iteration gives `f(t)≤C(L)exp(−2mt)E(A_B)`, `m=−log θ/(2Δ)>0`. The source's shift from `5c_N+1` to the larger `6c_N+1` is harmless by monotonicity; a fixed prefactor covers the initial interval. Applying P once more gives the potential bound. **This repaired conditional hole-filling implication is CORRECT-NO-ADVANCE.** It does not complete P's seam/boundary/torus proof or give the outline's gauge and derivative estimates.

## 4. Lemmas S and C, and the saddle-point claim

### Lemma S — (i), (ii) ADVANCE after making the cutoff conventions explicit; (iii) WRONG as proved

For (i), `ran Π` contains no nonzero componentwise constant: every component contains a whole pillar, and its mean must vanish. Thus the finite-dimensional quadratic is strictly convex. Its Euler equation has the printed signs if `Δ=δd≥0`. Testing with `λ`, applying Lemma 2 on each pillar, and Cauchy–Schwarz gives exactly (i).

For (ii), the source functional cancels when the cutoff is one on all source pillars. The corrected competitor has zero pillar means. To check the seam error independently, orient a crossing bond's product rule so that the value multiplying `dχ` is taken at the endpoint in the **finer** pillar. Then `|dχ|≤C/ξ_fine`, and the sum of these terms is bounded by `CΣ_P ξ_P^{-2}||λ||_P²≤C||dλ||²`; no ratio of the two pillar sizes is lost. A mean correction satisfies `|m_P|≤ξ_P^{-2}||λ||_P` and costs `Cξ_P²|m_P|²≤C||dλ||_P²`. At most two supported bumps meet a bond. For example normalized tensor tents give `||db_P||²≤8192ξ_P²`, so a zone constant below `10⁷` is available with generous product-rule allowances. Whole-pillar corrections enlarge the zone by a fixed metric distance (a pillar's diameter is at most four). The hole-filling recurrence with step 19 yields a rate larger than `1/(7·10⁸)`; a fixed prefactor covers source-adjacent values of `t`. This establishes the claimed kind of absolute scalar rate, without using T or P's gauge transitions.

**Defect 5 (first failing step in (iii), lines 331–335):** the asserted polynomial count in the weighted metric is false. A fine pillar just outside one coarse pillar can reach each of the `L³` fine pillars along its face by entering the coarse pillar, traversing it at coarse cost, and leaving it. The weighted distance is bounded by an absolute number, independent of `L`. For large odd `L`, this already contradicts `(2n+1)⁴` for same-layer pillars in a fixed-radius ball. This configuration is allowed: take the outer regions to be the full torus and the next region to contain that coarse block. Deeper shortcuts likewise invalidate a polynomial count independent of the accessible coarser levels. The estimate for a source piece in line 329 is legitimate; its asserted Schur sums do not follow from the count given.

Visible repair, **not proved here**: establish a multiscale packing estimate that charges an excursion through each extra layer its separated collar distance, includes the multiplicity of finer pillars reached on returning, and then sums the resulting exponential series. The large `ρ` may pay for those multiplicities, but this has to be shown for both Schur sums with the factor `ξ_{P'}/ξ_P`. Neither the value `10⁹⁰L⁶` nor the threshold `8 log L/m_s` follows from the false polynomial count. (iii) is an uncompleted estimate, not a disproved scalar resolvent theorem.

### Lemma C — WRONG as a discharged lemma; corrected conditional implication is CORRECT-NO-ADVANCE

The first failing dependency is P's full-domain estimate at line 344; (iii) of S is another uncompleted dependency. Even assuming them, the sum of P requires the overlap constant from §3: use `C'_P=M(L)C_P`, not an unexplained `81L⁴C_P`. Set `A~=A−dλ` and `f=ΠδA`, `g=A~`. Then
`ΠΔλ=ΠδA−ΠδA~` is exactly S's equation. Consequently

\[
 \|\xi^{-1}A\|_2^2
 \le 2C_S\|\Pi\delta A\|_2^2
       +2(1+C_S)C'_P\|dA\|_2^2.
\]

This is the claimed weighted coercivity with an amended constant, **if** the repaired P and S(iii) are supplied. No further analytic implication is missing in that substitution.

**Defect 6 (independent failure of the saddle-point extension, lines 350–355):** T bounded in curl energy is not T bounded in the graph norm `X`. The printed bumps have longitudinal jumps. For `s=4W+1` (e.g. `L=5` and arbitrary depth), `g` jumps from one to a negative constant at `w=W`. Its normalization is comparable to `1/s`; on a transverse central subbox of `c s³` sites the jump in `δφ_c` is at least `c/s`. The pillar average of this divergence is only `O(s^{-2})`, by flux through the face divided by `s⁴`. Subtracting that average therefore leaves

\[
 \|\Pi\delta\phi_c\|_2^2\ge c s
\]

for large `s`. This is already a single-layer example, where the repaired T is just that bump. Thus the claimed uniform `||Tβ||_X` at line 354 is false for the supplied T, although its curl bound is sound.

A visible replacement is a longitudinal profile with discrete slope `O(1/s)`, normalized amplitude `O(1/s)`, and the same zero moments. Two smooth, separated one-sided hats with unequal first-moment/mass ratios can enforce the two moment conditions; use reflected versions at seams. One must prove their moment determinant, graph bound and cross-level correction together. This replacement has not been constructed in the submitted proof. Alternatively one could gauge-correct a curl lift using an actually proved S(iii). Brezzi's argument needs an `X`-bounded lift and acts from `X×ℓ²` to its dual; the displayed saddle-point matrix is not literally an operator bounded on the same graph space with an `ℓ²` force norm unless those identifications are specified. The subsequent test with `dμ` does correctly force `ΠδA=0` once invertibility is supplied. The passage to Balaban's `RδA=0` remains the gap explicitly acknowledged in lines 359–360.

## 5. Theorem E, its contour inputs, and admissibility

### Theorem E — ADVANCE for its single-layer inequality, with two elementary proof repairs

This theorem can be checked independently of the multiscale P/S gaps. It assumes the flat single-layer minimizer in `ΠδA_L=0`, whose gauge exists by the finite-dimensional positive scalar problem; it does not need a depth-uniform scalar inverse to define that gauge. The following is the full chain of estimates. All local windows can be taken on the periodic lift; if the torus has fewer than three top blocks in a direction, the bounded number of repeated copies costs only an absolute factor.

1. Stationarity gives `δdA_L=qᵀω`. The Landau condition says `δA_L` is constant on each pillar, so `dδA_L=0` strictly inside a pillar. Thus the component equation near its center is `ΔA_L=qᵀω`. Testing with a **single-layer** bump from T's valid same-level construction gives `ω(c)=<dA_L,dφ_c>`. The bound `sqrt(86016)<300` is adequate. The first support oversight is line 405: transverse differences of the bump read a one-plaquette collar of `D(c)`, not just `D(c)`. For the rows reaching the center neighborhood this collar still lies in `N_y`; use `||dA_L||_{N_y}` in the test bound. Only a bounded number of rows reach such a bond, each with coefficient at most `B^{-3}`. Hence `|qᵀω|≤C B^{-3}||dA_L||_{N_y}`, with the stated `4800` still adequate. No seam inverse is used here.
2. Line 409 uses `Δ|x|²=8`, whereas the energy convention `Δ=δd≥0` gives **`−8`**. Fix the sign, not the estimate. For `F=sup_Q|qᵀω|`, the nonnegative barrier `w=(F/8)(B²/4−|x−y|²)` on a cube of side `B/2` satisfies `Δw=F`. The positive-Laplacian maximum principle applied to `w±v` gives `|v|≤F B²/32≤150 B^{-1}||dA_L||_{N_y}` with the source's bound on `F`.
3. For `h=A_L−v`, test the harmonic equation with `η²h`, pair neighboring terms, and use `2ab≤a²/2+2b²`. This yields `Ση²|dh|²≤CΣ|dη|²|h|²`. Differences are harmonic on a slightly smaller cube, so a second application bounds second differences. The discrete Sobolev input has a hand proof: coordinate-line telescoping and the four-factor Loomis–Whitney/Hölder inequality give `||w||_{4/3}≤∏_i||d_iw||_1^{1/4}`; put `w=|u|³` to obtain `||u||_4≤(3/2)||∇u||_2`. This is the argument credited to Gagliardo, Nirenberg, Loomis and Whitney in `lattice_sobolev_box_gauge.md:5–13`, checked here. Applied to cutoffs of `h` and its differences it yields `||h||_4≤Cr^{-1}||h||_2` and `||∇h||_4≤Cr^{-2}||h||_2` on smaller cubes.
4. In the same telescoping inequality put `w=|u|⁹`: Hölder with exponents `3/2,3` gives `||u||_{12}≤18||∇u||_3`. On a cube of side `r`, `||z||_3≤Cr^{1/3}||z||_4`. Applying this to the cutoff derivative and to `∇h` gives `||h||_{12}≤Cr^{-5/3}||h||_2`. Since top normalization multiplies this norm by `B^{1−4/12}=B^{2/3}`, and `r` is a fixed fraction of `B`, the result is `||Bh||_{L^{12}}≤C B^{-1}||h||_2`. The particular part contributes at most `C||dA_L||_{N_y}`. Nested-cube arguments require a fixed lower bound on `B`; the remaining `B` below that absolute threshold are handled directly by `||A||_4≤||A||_2`, enlarging an absolute constant. There are then only a bounded number of shells. No finite enumeration is needed.
5. For the outer shells, choose a cutoff equal to one on radius `5B/6` and supported strictly inside the three-block window. Discrete integration by parts gives `||∇(ηA)||²=||d(ηA)||²+||δ(ηA)||²`; its errors are `O(B^{-1}||A||_{N_y})`. To bound the pillar-constant divergence `c_P`, take a scalar bump of mean one which vanishes on the pillar boundary, with `||db_P||≤CB`. Then `c_P B⁴=<δA,b_P>=<A,db_P>`, so `||δA||_P=|c_P|B²≤C B^{-1}||A||_P`. Using bumps with zero boundary values keeps these tests inside `N_y`. Sobolev now gives the outer `L⁴` bound stated at lines 425–427.

The remaining contour steps require checking the two imported results, not their “discharged” labels:

- **Lemma A of `rel-phi-c.md:186–209` — ADVANCE.** The recursion telescopes to `Φ_nθ(y)=Σ_k Φ^{(k)}Q_path^{(L^{k−1})}θ(y)` because `Φ(dμ)=Av μ−rμ`. For the `k`th summand, the total absolute coarse-path weight is `L−L^{-1}<L`. The same-scale part has the stated `2^{3/4}L` bound by Hölder on a path-average support of at most `2s⁴` bonds. If that support reaches `R_{k−2}`, its transverse coarse coordinates must equal those of `y`, and its longitudinal coordinate is `−s` or zero. These are the eight bonds at `y`, with total absolute weight `1−L^{-4}<1`. With `|A_j|≤64L^{4j}`, the finer contribution is at most `22.7 Σ_{j≤k−2} L^{-3(k−1−j)}||θ||_{ℓ⁴(A_j)}`. Each shell gets two same-scale contributions and a geometric tail at most `22.7/(L³−1)<0.88`. Hence `2·2^{3/4}L+0.88≤3.4L+1`. For `k=1,2` the finer part is empty. No step fails, and no run is used.
- **Corollary A2 of `rel-phi-c.md:216–226` — ADVANCE.** In top measure, `|A_j|≤64L^{-4(n−j)}`. Hölder gives the factor `L^{-(n−j)(1−4/p)}`; summing the geometric series gives exactly the asserted kind of depth-free bound. This argument also bounds the **sum of shell norms itself**, before Lemma A is applied. At `p=12` the exponent is `2/3`. Thus its use on the inner shells in E is valid. A shell wholly inside the cube of side `B/32` is covered by the `L^{12}` estimate. Since `3⁴>64·5/6`, at most four remaining outer shells need the preceding `L⁴` estimate. Lemma A then bounds `Φ_n(A_L)(y)`. There is no hidden `n^{3/4}` loss here.

Therefore E's displayed inequality (394) survives, uniformly in depth and volume. The support oversight at 405 and sign error at 409 have complete repairs above; no further essential step fails. This proves a local estimate in the **local** Landau gauge. The following assertion that its right-hand side is already bounded by local data through C or FL is conditional: C is not completed, applies directly only on `ker q`, and FL(b) supplies an existential restricted gauge rather than this particular Landau gauge. It also does not identify this gauge with Balaban's `R` gauge.

Section 5.1's logarithmic-capacity example does give an unbounded *forward* constraint map `K_M:X→ℓ²`. To redo the scaling, use a Euclidean radial logarithmic bump, smoothed near its outer radius `R≈B/4`, of center amplitude `a`. Its first and second differences are bounded respectively by `Ca/((1+r)log R)` and `Ca/((1+r)²log R)`. Counting at most `C(r+1)³` sites per radial shell gives `B^{-2}||dμ||²≤Ca²/log²R` and `||Δμ||²≤Ca²/log R`; subtracting pillar means cannot increase the latter. Meanwhile `K_M dμ=d'rμ` has size `a` on bonds between the alternating nonzero and zero nodes. Thus the operator norm grows at least as `c√log R`. The sharp outer cutoff would spoil the second-difference bound, so the stated smoothing matters. This alone does not prove an unbounded inverse saddle operator: even the scalar matrices `[[1,t],[t,0]]` have uniformly bounded inverses for `t≥1`. The elementary identity `K_M=Q_path−d'Φ` is correct.

### Step 5.3 — WRONG, even granting Theorem E

**Defect 7 (first failing step, lines 446–448):** a nodal gauge value needed for admissibility is not a freely chosen contour-cancellation amplitude. Use fine-field notation to avoid normalization ambiguity. Let the actual gauge taking an admissible relative field to `θ_L` have nodal values `κ_L(y)`. Then

\[
 K_M\theta_L=d'\kappa_L,\qquad
 \Psi_L=\Phi_n\theta_L,\qquad
 Q_{\rm path}\theta_L=d'(\kappa_L+\Psi_L).
\]

For the proposed point bump `λ_b=−Σ_y κ(y)(1−φ_y)`, disjoint inside blocks, its value at `y` is `−κ(y)` and its block mean is `−c_R κ(y)`. The exact gauge laws therefore give

\[
 K_M(\theta_L+d\lambda_b)=d'(\kappa_L-\kappa),\qquad
 \Phi_n(\theta_L+d\lambda_b)=\Psi_L+(1-c_R)\kappa.
\]

The chosen `κ=−Ψ_L/(1−c_R)` cancels the second expression. It does **not** cancel the first, nor make the total fine gauge equal to one at the nodes. Admissibility requires the actual `κ_L` (up to a common constant for the weaker parent-constraint condition). Theorem E bounds `Ψ_L`, not `κ_L`. The note assumes the very compatibility it needs to prove.

Repair: use `κ=κ_L`, prove a depth- and volume-uniform bound on those nodal values, and retain the resulting **bounded** contour `Ψ_L+(1−c_R)κ_L`; zero contour is unnecessary for REL. A special sufficient extra hypothesis is `Q_path θ_L=0` and connectedness, so `κ_L+Ψ_L` is constant. Normalize that constant to zero, take `κ_L=−Ψ_L`, and the final contour is `c_RΨ_L`, while the gauge is admissible. The denominator in the submitted choice is then absent. This is a correct conditional repair; the required extra hypothesis is not supplied for the stated general datum or relative trial/minimizer pair.

The bump norm mechanism itself is sound for sufficiently large `B`, with small `B` treated separately to keep the supports disjoint. If `a=log(1+R)`, a radial shell contributes at most `C|κ|(log L)^{1/4}/a` to the critical norm. There are at most `1+log R/log L` such shells, giving a depth-free `C|κ|(log L)^{-3/4}` bound after absorbing endpoint shells into `C(L)`. The L² cost is `C B^{-1/2}|κ|/a` and the L⁴ cost is `C|κ|/a^{3/4}`. These estimates do not cure the wrong nodal values. Nor does bounded `κ` alone make a nonlinear error small: its size must be compared with the small field/energy parameter. The nonlinear elliptic estimate is correctly left open, but the first missing step here is already linear admissibility.

### Lemmas H and LR (section 5.4)

**H — ADVANCE.** No essential step fails. Iterating the one-dimensional “average plus total variation” inequality gives `|h(x)|≤Σ_S r^{-(4−|S|)}||d_Sh||_1`. Cauchy–Schwarz contributes `Cr²`; Caccioppoli on successively smaller cubes contributes `C r^{-|S|}||h||_2`. Every term is therefore `Cr^{-2}||h||_2`. Reserve one lattice step at every difference and use the trivial point bound for bounded `r`; this removes the small-cube convention issue.

**LR — CORRECT-NO-ADVANCE as a conditional deduction from a repaired local curl lift; WRONG if labeled unconditionally discharged by the submitted T.** Its first failing dependency is T's assembled inverse at line 492. Given the repaired curl lift, testing stationarity gives the local multiplier bound (the added datum terms are harmless and unnecessary). `dF=0`, `δF=qᵀω` imply `ΔF=d(qᵀω)`. For `F₁=dG_T(ηqᵀω)`, the mean-zero Green equation leaves only the derivative of a constant, which vanishes; consequently `F−F₁` is harmonic on the inner cube. The lattice shell count `#{|z|=r}≤C(r+1)³` gives `Σ_{|z|≤ξ}(1+|z|)^{-3}≤Cξ`, and hence `|F₁|≤Cξ^{-2}(local energy+datum)^{1/2}`. Its local L² norm is bounded by the same energy square root, so H finishes the estimate. The cited Green-gradient proof in `lattice_gehring_hls.md:21–25` is a legitimate hand Fourier-summation route after taking its cutoff at `C/|x|` with a sufficiently large fixed `C`; its claim that `1/|x|` itself exceeds several frequency mesh steps fails at `|x|≈N`. With that harmless cutoff repair, low modes are bounded by the four-dimensional radial sum and five summations by parts give `|x|^{-5}Σ|p|^{-6}≤C|x|^{-3}`. LR still yields curvature, not all potential-gradient/current/Hölder members of outline A3.

## 6. Conditional curved statements: check of implications only

**Factorization and its twice-differentiated chain rule — CORRECT-NO-ADVANCE.** Given the stated gauge covariance and the compatible one-step factorizations, composing them gives the displayed accumulated site factor and straightened map. Differentiating a composition twice gives exactly the sum in line 578. This is an algebraic identity, not an estimate on those derivatives.

**(W1) — CORRECT-NO-ADVANCE, given the actual transported-average gauge identity.** Differentiating the gauge factor gives the coarse derivative of the transported pillar average; zero transported means therefore kill the constraint derivative. At an outward row the outer coarse block average must be obtained by averaging its finer pillars, with their transports. This is part of the stated exact covariant average identity; it cannot be replaced by an unrelated node restriction.

**(W2) — CORRECT-NO-ADVANCE at a constrained critical point, given the stated gauge-family IFT input.** Write the invariant Lagrangian as `ℒ` and its gauge tangent as `X_μ(a)`. Differentiation gives
`D²ℒ(0)[h,X_μ(0)]+Dℒ(0)[DX_μ(0)h]=0`.
The second term vanishes **because `Dℒ(0)=0`**, yielding W2. Regularity alone does not make it vanish. Thus W2 is not established at an arbitrary regular trial field by this argument; it must remain an input there. This distinction does not invalidate an implication that explicitly assumes W2.

**(W3) — CORRECT-NO-ADVANCE with the quantitative averaging bounds as inputs.** Check the level count rather than appealing to factorization alone: for `r=n−m−1`, an outer derivative coefficient bounded by `C L^{-3r}`, a carrier of `O(L^{4r})` rows, and Cauchy–Schwarz give `C L^{-r}` times the ℓ² norm of the one-step quadratic output. The one-step Cauchy bound and bounded support overlap bound that norm by `C(L)||X_m||_4²`. A composite averaging bound `||X_m||_4≤C||h||_4` then gives a summable geometric series; shifting `r` by one only changes `C(L)`. Local covariant Sobolev and the graph bound on the pillar mean of `D* h` convert this to the quadratic form bound. Pairing with the assumed `||ω₀||_∞≤Cε` yields W3; curvature terms are bounded directly by `εξ^{-2}|h|²`.

This implication really uses depth-uniform **composite** averaging majorants. The outline's passage at lines 9808–9821 gives the one-step row/column bounds **with summable relative errors**, not exact no-loss bounds at a curved field. If `Σ_m e_m≤Cε`, then `∏_m(1+e_m)≤exp(Cε)`, which is a valid repair of the note's omitted errors. Bare one-step analyticity, an unspecified Cauchy constant and exact factorization by themselves do not supply this premise. No claim is made here to prove that outline input on its full nonlinear domain.

**Theorem CL — WRONG as a completed implication from the named inputs; its perturbation algebra is CORRECT-NO-ADVANCE once the additional patch bounds below are supplied.** This check grants (W) and the complete flat saddle estimates, including an `X`-bounded right inverse, so it does not merely repeat their earlier failures. The strip estimate in (a) is correct on a cube whose finest scale is `s`: `|U^g−1|≤3lεs^{-2}`. The next passage to a uniform relative `C R₀L²ε` bound requires control of the ratio between that finest scale and the advertised patch scale. That is the first new gap, detailed in Defect 8.

For clarity, the rest of the *conditional* operator argument is valid: given those patch comparisons and the stated IMS/constraint-commutator estimates, choose `R₀` first to absorb `C R₀^{-2}`, and `ε` second to absorb the local perturbation and `c_Wε`. This gives coercivity on `ker K`. A bounded graph lift with row error `||E||<1` gives a right inverse via the Neumann series. Coercivity plus this right inverse yields the saddle inverse in the natural dual force spaces. If the stated conjugation estimate is `||S_m−S||≤CLm`, then `||S^{-1}(S_m−S)||<1/2` at sufficiently small `m`; the resolvent identity gives the exponential weighted bound. Finally W1 and W2 annihilate the other terms when testing with `Dμ`; positivity of `ΠD*DΠ` gives `ΠD*h=0`. These implications do not prove the patch comparisons or the graph-lift premise. Defects 3, 5 and 6 additionally prevent the submitted flat work from supplying the latter.

**Defect 8 (first new conditional gap in CL, lines 539–543):** a Euclidean patch of side `R₀ξ#` need not contain only the two advertised local scales. The later choice `R₀²≥16CC_C` has no upper bound relative to `ρ`; the hypotheses only gave lower bounds on `ρ` unrelated to this `R₀`. To see the geometric issue, take nested cubical regions whose successive outward collars have thickness just above `ρs_i`. From a top pillar of side `s_k`, the total physical thickness of *all* lower collars is of order `ρΣ_{i<k}s_i<ρs_k/(L−1)`, even when `k` is arbitrarily large. A sufficiently large fixed multiple of `s_k` can therefore reach layer zero. Its finest scale is one, not `ξ#/L`. The comb estimate just established cannot give the subsequent claimed comparison by substituting only one factor of `L²`.

Visible repair: after fixing the flat constants and `R₀`, impose a sufficiently large separation such as `ρ>C R₀L²`, and construct the seam cover so each patch sees at most two consecutive scales; or provide an adapted metric cover and prove its operator comparisons with all encountered scales. The first repair strengthens the stated domain but preserves a depth-free perturbative implication. Neither condition is among the currently named assumptions, and its preservation cannot be inferred from (W). This is a gap in the implication, not a counterexample to the curved inverse itself.

**Defect 9 (application after CL, lines 626–628):** the cited TOP-tr curvature bound is not the full regularity assumption in lines 509–510, which also bounds current at scale `ξ^{-3}`. Even in a fixed abelian color, take on an even torus `A_1(x)=ε(-1)^{x_2}/(2s²)`, all other components zero. Its plaquette angle has size `ε/s²`, but `δdA_1=4A_1` has size `2ε/s²`, not `O(ε/s³)`. For the corresponding small SU(2) abelian links, replacing the angle by its sine preserves this discrepancy (use `sin t≥t/2` for `0≤t≤1`). Thus a fine-curvature bound alone cannot certify that the iterated trial meets CL's current hypothesis. Nor does regularity certify the critical-point premise in the W2 derivation. Repair: retain the current bound and W2 at the trial as explicit additional inputs, or prove them for that actual trial. A general regular-background implication must not silently be applied on the strength of curvature alone.

## 7. Two-background comparison — WRONG from the named inputs as stated

**Defect 10:** even granting CL, uniqueness (U), chart smoothness and the indicated single-plaquette LR, the continuation paragraph needs more than those statements provide.

The first questionable inference is line 639. Stationarity passes to a **smaller tangent space**, not to fewer fixed equations. At `t=0` one must show that each joined, collar-preserving variation extends to an old admissible variation, including the action boundary terms. If “larger constraint set” means a larger admissible manifold and that inclusion has been established, the implication is valid; if it means more determining rows, its direction is reversed. Feasibility and uniqueness alone do not supply the inclusion. For example `f(x,y)=x+x²+y²` is stationary at `(0,0)` under `x=0`, but not without that constraint, although both problems have unique critical points. The joined-row/restriction compatibility must be a named premise, not inferred from uniqueness.

Even granting that compatibility, the first definite norm failure is line 643. CL estimates the potential and covariant curl in weighted local **L²**. The admissible radius requires pointwise curvature **and current**, and chart membership in the specified neighborhood. No depth-uniform implication from those L² norms to that full regularity norm is given. The curved LR named later only for the final plaquette comparison does not supply a current bound along the interpolation. Moreover CL has an ℓ² datum norm; replacing it by `sup|Δv|` requires a uniform sum of response columns over the collar. In a multiscale path metric the polynomial count in line 650 is not automatic (the shortcut issue in S applies again). The lower bound on `ρ` chosen for `m_s` does not establish summability at the potentially much smaller CL rate `m'`. Hence the proposed open–closed argument cannot be justified by the listed inputs, even if the fixed-background CL estimate is granted in full.

Visible repair: either assume a common admitted critical branch for the whole interpolation, or add an inverse estimate into the complete regularity/chart norm and the corresponding collar summability bound, with quantitative room to the domain boundary. Also state the tangent-space/restriction compatibility and a common transported gauge. Under these strengthened inputs the remaining implication is valid: linearity, triangle inequality and integration bound the local response norm by
`C ε exp(−mD_p/2)`. Squaring gives the displayed energy scale; the holonomy **norm**, unlike its square, is of order `ε exp(−mD_p/2)`, correcting the wording at line 654. A pointwise curvature-response estimate restores the fine factor `η²`. Finally, for aligned plaquettes with `||1−G||,||1−H||≤r`,

\[
 |a(G)-a(H)|
 =\tfrac12\big|\|1-G\|^2-\|1-H\|^2\big|
 \le r\|G-H\|.
\]

With `r≤C a_kη²` and `||G−H||≤C a_kη²e^{-mD_p}`, this gives `(L)` with the two powers of `a_kη²`. That last scalar implication is **CORRECT-NO-ADVANCE**. The norm/domain and boundary hypotheses needed to reach it are not closed here. No conclusion about the ten-term remainder or existence of Yang–Mills follows.

## 8. Are FL and E the flat linear form of outline A3?

**No.** They are useful subestimates for one response in a different gauge, not A3 with the background specialized to the identity. This comparison is to Ethan Sussman and Levent Alpoge's text, with Claude and Codex as its authors, at `31a47c543775`, A3 lines 3864–3896 and (1b) Theorems 3–4 around lines 9693–9746.

| Requirement in the stated A3 / (1b) response | What FL and E supply, even after repairs |
|---|---|
| Actual inverse kernels and conditional covariances, with the prescribed force/cell weights and boundary rows | FL concerns the constrained energy minimizer's datum response; it supplies neither all those inverses nor conditional covariance estimates. |
| Weighted multiscale exponential response, including potential, first differences, current/second-order members and Hölder differences | FL gives curvature energy and potential L² in an existential restricted gauge. LR adds curvature pointwise under its hypotheses. No uniform potential-gradient/current/Hölder package follows. |
| The specified Landau pair, including its top gauge factor | E controls contours in `ΠδA=0` on a **single-layer** lattice. The map to `RδA=0` is explicitly unwritten. Step 5.3 does not repair that identification and fails its own admissibility claim. |
| Full complex datum domains, enlarged complex decoupling discs, Cauchy estimates and decay retained by joining derivatives | Neither FL nor E addresses decoupling parameters. Complexifying a real flat linear operator would not establish this parameter-dependent package. |
| Compatible restriction, seam and finite-box equations | T/P have the repairs and missing full-domain cases recorded above; no identification with all actual outline boundary/gauge rows is proved. |

The outline itself distinguishes its established classical flat reference precision/covariance kernels from the still-open multiscale/background/decoupled response. That distinction must also be retained here. In particular the local gauge is not a harmless unnamed replacement when the desired quantities include derivatives of the potential.

## 9. Disposition and recovery point

| Statement | Verdict on this read | First failure or surviving scope |
|---|---|---|
| Lemma 1 | ADVANCE | None on an embedded rectangular box. |
| Lemma 2 | ADVANCE | None. |
| Lemma 3 | WRONG | Tent norm at lines 83/149; exact repair in §1–2. |
| Lemma T | WRONG | Outward data counted twice at 180–182; triangular repair given, numerical constants must change. |
| Lemma P | WRONG | Embedded-box application/full seam coverage and layer-zero transition; estimate not refuted. |
| Theorem FL | WRONG as completed; repaired conditional iteration valid | T/P dependencies, then the missing overlap constant at 274. A depth-free packing repair is given. |
| Lemma S | ADVANCE for (i)–(ii); WRONG as completed for (iii) | False metric counting at 331; weighted Schur estimate remains unproved. |
| Lemma C | WRONG as completed; conditional algebra valid | P and S(iii), with an amended overlap/energy constant. |
| Saddle-point extension of C | WRONG | The supplied lift's `Πδ` norm grows like `s^{1/2}` at 354. |
| Theorem E | ADVANCE for its single-layer inequality | Support at 405 and sign at 409 repaired; Lemma A/A2 uses valid. No admissible-gauge conclusion included. |
| Step 5.3 | WRONG | Chosen bump values need not be the required nodal gauge values. |
| Lemma H | ADVANCE | None after explicit small-cube conventions. |
| Lemma LR | CORRECT-NO-ADVANCE as conditional | Valid from the repaired local curl lift/Green estimate; its submitted T dependency is not discharged. |
| Factorization, W1–W3 | CORRECT-NO-ADVANCE with the full inputs stated in §6 | Uniform composite bounds and criticality where used cannot be omitted. |
| Theorem CL | WRONG as the stated implication; repaired perturbation algebra valid | Patch-scale comparison at 539–543; a separation/cover hypothesis is missing, even granting the flat saddle inputs and (W). |
| Section 7 comparison | WRONG from the named inputs | Missing restriction/tangent compatibility; definitely, L² CL does not close the regularity bootstrap at 643. |

The earliest false displayed estimate is the tent norm at line 83; the earliest failure in the named lemma conclusions is Lemma 3. The first broken assembled construction is T at line 180. The strongest surviving progress is the elementary box estimates and the independent single-layer Theorem E, including its depth-free contour/shell bound. The multiscale FL proof is repairable in its hole-filling mechanism but is not closed on the stated domain; admissible gauge conversion and the full A3 package remain open. The ten numbered defects above are failures of this text or its stated implications, not no-go claims about the intended Yang–Mills route.

Recovery: keep the pinned source identities above; repair T's algebra **and** its graph lift, finish P on seams/boundaries/compatible tori, prove the scalar weighted packing/resolvent bound, then rerun the corrected FL constants. Independently, retain E and replace 5.3 by an actual nodal-gauge compatibility statement. For the nonlinear comparison, obtain admitted-path/current-norm and boundary-row control before invoking uniqueness or continuation. No other editable prompt or source file was changed; no platform instruction was modified. No subagent, audit, numerical proof, commit, push, PR or post was used.
