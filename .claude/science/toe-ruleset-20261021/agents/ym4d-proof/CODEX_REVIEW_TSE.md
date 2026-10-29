## PRE-STATED — 2026-10-29 06:25:59 UTC

Independent hostile review of `TSE55.md`. This section was written before reading or deriving the target's mathematics. No git commands; only this deliverable will be written. Calculations will use exact rational/symbolic reasoning and, where useful, plain Python.

Targets and pre-stated refutation criteria:

1. Rebuild Theorem TS's coefficient and object identification. A wrong Wick factor, coupling convention, clover normalization, RG matching factor, or insufficient hypothesis for the stated uniform two-sided bound refutes the corresponding assertion.
2. Test whether (PL-1L) is a precisely quantified, sufficient remaining input and whether its proposed reduction supplies the needed source insertions, localization, relative errors, and scale summability. An unproved necessary additional input defeats the claim of a completed reduction.
3. Re-derive the upper-only route, including the running source radius and H-RED exponent comparison. Check all minima and whether constants remain fixed inputs.
4. Test the all-level leading bubble against a single matched-level leading term, including signed fine-level contributions.
5. Check separated-support mechanisms, reflection positivity, canonical coarse-level decay, source-radius losses, matched-level SA-K, and large-field thresholds.
6. Locate K-dec's cited lemmas and inspect their actual scope. Treat literature-supplied LGF as unverified unless re-derived here; do not silently promote it to a proved lattice estimate.
7. Inspect ts55_1–3 for checks that cannot fail, finite truncations, hard-coded conclusions, and hypotheses not exercised. Locate citations by text before checking cited line numbers.

Finding statuses: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Confirmation will be restricted to the statement actually re-derived, with no numerical check promoted to a uniform theorem. Findings and corrections will be appended as the review proceeds, followed by a summary table and an explicit statement of what may be banked.

## Findings — appended during the review

### R1 — REFUTED: the bare-coupling derivative has the wrong sign

**Locators:** `TSE55.md:331`, string `e = −2∂S_W/∂u_0 per unit volume`; contrast its own §2.1, `h^f_□(p) := ½Σ_{x∈corners(p)}f(x)` and `u_0 → u_0 − Σ_iz_ih^{f_i}_□(p)`.

Each unoriented plaquette occurs at four corners and twice in the ordered plane sum. Consequently

`O(1) = Σ_x a⁴e_a(x) = 2Σ_p s(U_p) = +2 ∂_{u_0}S_W`.

The coefficient multiplying the action derivative is **+2, not −2**. The minus sign belongs instead to differentiating an action with respect to an inserted source: `O(f) = −∂_z S_W[u_0−z h_f]|_{z=0}`. These are different derivatives. This does not change a covariance of two insertions, but the stated operator-matching mechanism has a sign error. **Corrected identity: PROVEN.**

### R2 — CONFIRMED: existing erratum E3 repairs the superseded growth-rate claim

**Locators:** `TSE55.md:253`, string `it grows like u_k/b_−`, and §4.3, `u_k²·Σ growing like u_k/b_−`.

Choose the admissible exact trajectory `u_{k+n}=v+b(m−n)`, `u_K=v>0`, `b_−=b_+=b`, `R_F=0`. Then `u_k=v+bm` and

`Σ_{n=0}^m u_{k+n}^{−2} = Σ_{r=0}^m(v+br)^{−2}`.

The last sum is at least `v^{−2}` and at most `v^{−2}+1/(bv)`, independently of `m`, and converges to a positive finite constant. Therefore **`u_k²Σ u_{k+n}^{−2}=Θ(u_k²)`**, not `Θ(u_k/b_−)`, at fixed terminal coupling. The conclusion that the unsuppressed estimate supplies no vanishing AF bound survives. On reading the file's end, I found that **§10 E3 (`TSE55.md:600–603`) already overrides the erroneous body text**. Thus this is confirmation of an existing repair, not an outstanding error or a new discovery. E3's integral is an order estimate; the exact limiting coefficient is the discrete series above, not exactly `1/(bv)`. **Corrected growth order: PROVEN.**

### R3 — REFUTED: the exact canonical factor is not logically necessary for every per-level route

**Locators:** `TSE55.md:323–325`, string `is an indispensable input of any per-level route`; §7.3, `cannot be dropped by any per-level route`.

The counterexample in §4.3 establishes that *no decay assumption* is insufficient. It does not establish necessity of the particular factor `L^{−8(i−k)}` or of (CSL). Replace that factor throughout the coarse-level proof of Lemma SUM by `L^{−α(i−k)}` for any fixed `α>0`. With `n₁=⌊(u_k/2−R_F)/b_+⌋`, the near part is at most `2^s u_k^{−s}/(1−L^{−α})`; the far part is at most `γ^{2s}L^{−α(n₁+1)}/(1−L^{−α})=O(u_k^{−s})`. The last conclusion follows because an exponential dominates a fixed power. Thus, for example, **α=4** suffices to sum an `s=2` envelope and an `s=2+ϑ` error, although it does not imply the canonical exponent 8. Cancellation estimates could provide other routes.

The bankable obstruction is narrower: the displayed unweighted per-level upper bounds alone cannot produce TS. The canonical factor is a sufficient, physically motivated localization target. Its claimed universal necessity is **GAP**.

### R4 — REFUTED: (LOC-e) and the lower-bound image-matching obligation are not the same estimate

**Locators:** `TSE55.md:666–668`, string `share one missing estimate; HANDOFF should list it once`; §6.4 (P3), `fluctuation corrections of relative size O(u_i^{−ϑ})`; `SRCAN55.md:558–563`, exact statement `(LOC-e)`.

SRCAN's (LOC-e) says `Osc 𝔦_r ≤ c_r‖h‖₁ℓ_ref^{−4}` with `Σ_r c_r<∞` uniformly in cutoff and volume. This is an upper bound on the oscillations of a conditional **first** image. It specifies neither its coefficient relative to the quadratic image nor a remainder tending to zero with `u_i`. Multiplying every nonconstant image by any fixed `A≠1` preserves (LOC-e), after replacing `c_r` by `|A|c_r`; multiplying a quadratic image by `A=2` multiplies its two-point Gaussian bubble by **4**, whereas (PL-1L) requires its specified coefficient plus a vanishing relative-envelope error. Setting all oscillations to zero also satisfies (LOC-e) and supplies no positive witness.

Consequently the stated identification of obligations is false. A common localization argument may help both, but **canonical upper control, normalization `1+o(1)`, two-insertion covariance matching, and large-field error control must remain distinct obligations**. The claimed merger would erase precisely the information needed for the positive lower bound. The producer reduction is **OPEN/ARGUED**, not a completed proof of (PL-1L).

### R5 — NOT-VERIFIED radius comparison; REFUTED under the same-threshold reading

**Locators:** `TSE55.md:339–346`, especially `the relative polydisc is inside SA-K's class`; `:355–358`, radius `ε̂_*u_kλ⁴`; `SRCAN55.md:114`, `‖ε̂‖_cf`; `:198–202`, SA-K's fixed threshold `ε̂_*`; `:136–137`, `ε̂_0=−h_η/u_0`, `|h_η|≤2‖η‖_∞`.

These two `ε̂_*` objects must be separated. Let `ε_SAK` be SRCAN's already fixed contraction threshold, and `ε_rel` the new existential source-radius constant. For a smooth `f` with a plateau and only `z_1` nonzero, at the proposed radius one has exactly `|ε̂_0|=2ε_rel u_k/u_0` on plaquettes whose four corners lie in that plateau. Along the admissible flow `u_j=v+b(K−j)`, fix `k≥d₀` and send `m=K−k→∞`; then `u_k/u_0→1`. Thus choosing `ε_rel=ε_SAK` violates even the sup-norm requirement eventually: **the factor is 2, not 1**, before the Hölder cost is added.

A sufficient explicit repair at matched depth is

`C_{f,g}:=2Σ_{h=f,g}(1+[h]_{α,≤1}/‖h‖∞)`,

`ε_rel ≤ ε_SAK/(2C_{f,g})`.

Indeed clover averaging gives `‖ε̂_0‖_cf≤C_{f,g}ε_rel u_k/u_0≤2C_{f,g}ε_rel`, using `u_0≥u_k−R_F≥u_k/2`. This is a fixed, test-dependent shrinkage, so it preserves the upper theorem's exponent. It is a missing threshold comparison, not a refutation of TS-up₁ from its independently assumed (SRC-rel). It also does not control the evolved position-dependent coupling field; that remains a producer obligation. **Corrected inclusion: CONDITIONAL on the stated shrinkage and the existing SA-K hypotheses.**

### R6 — REFUTED: AF-cmp does not give the asserted multiplicative fine-share error

**Locators:** `TSE55.md:306–309`, `u_k^{−2}Φ_fine(1 + O(u_k^{−1}))`; `:628`, summary's distinction between toy nonvanishing and generic lane behavior; `checks/ts55_2_gauss.py:122–127`, G3.

AF-cmp gives the **additive** statement

`W_fine = u_k^{−2}Φ_fine + O(u_k^{−3})`.

To factor out `Φ_fine` with a uniform relative constant one needs a uniform lower bound on `|Φ_fine|`. None is provided. A two-coordinate, two-level Gaussian example detects the missing condition: take the fine slice `K_f=[[2,−2],[−2,2]]` and coarse slice `K_c=[[1,1],[1,1]]` (both positive semidefinite), with the two observables the squares of different coordinates. At equal coupling `u`, the fine share is `4(−2)(1)+2(−2)²=0`, hence `Φ_fine=0`. At fine/coarse couplings `U+b,U`, `b>0`, it is

`−8/[U(U+b)] + 8/(U+b)² = −8b/[U(U+b)²] ≠ 0`.

The multiplicative expression would be identically zero. This refutes the claimed algebraic consequence of the splitting; it is not asserted as a counterexample constructed from the lane's actual blocking kernels. The corrected additive estimate is **PROVEN** from the same comparison argument. G3's 12 nonzero random samples never exercise this cancellation case.

The general need to retain the fine source–source term is sound: with fine cross-entry `−1` and coarse cross-entry `2`, both realized by positive semidefinite rank-one slices, the fine/top/total coefficients are exactly **−6, 8, 2**. Thus a matched-image term alone need not approximate the full bubble relatively. **Nonzero fine share for this lane's actual slices and its fixed witness pair remains NOT-VERIFIED**, as the target's summary appropriately qualifies; the toy count 12/12 cannot settle it.

### R7 — CONFIRMED implemented checks; REFUTED parts of their evidentiary description

**Locators:** `TSE55.md:588–594`, check table; `checks/ts55_1_bubble.py:87–92` (A4); `checks/ts55_2_gauss.py:83–127` (G1/G3); `checks/ts55_3_flow.py:34–56,59–89,97–104` (finite ceiling searches and S1–S3); their three `ts55_*_criteria.md` files.

I executed ts55_1 and ts55_2 with `nice -n 10 python3 -I -B`. Both returned their recorded **PASS**, with all displayed failure controls firing. I executed ts55_3's original numerical gates in memory, replacing only the display function `float` by `str`, so every numerical operation stayed exact and no source/output file was changed. Its results were `nseq=126`, `nchecked=1512`, `S1=True`, `S2=True`, `S3=True`, `ok=True`; the exact S2-F threshold was **1449/128**. This is reproduction of finite checks, not proof of their Yang–Mills hypotheses.

- **A1/A2/A3/A5:** the quotient-rule/index contraction and generator calculations can detect errors in their tested formulas. A1 tests only radial Hessians at eight points, not the general tensor theorem; the proof in R9 supplies the general identity. A3 checks tensor antisymmetry/index counting. A5 tests SU(2)/SU(3), while the trace-normalization argument in R9 handles general N.
- **A4 is not an independent clover-count check.** It sets `S4=384` and compares `2·(S4/4)/16` with `(1/32)·16·(S4/16)`. Both simplify identically to `S4/32`; the asserted clover multiplicity 16 is a literal input. Once these literals are fixed, the gate must pass. Changing the literal to 4 proves `3≠12`, but does not reconstruct how many clover terms the observable has. The actual count is re-derived in R9.
- **G1/G1-F/G2-F:** the polynomial-moment calculation is distinct from the closed per-level formula and detects the changed cross coefficient and omitted top term. **G3's scaling half is automatic homogeneity** when all couplings equal u; its nonzero half can fail (R6 gives an exact cancellation example). The reproduced 12/12 nonzero samples and negative examples are facts about those toys only.
- **S1/S2:** genuine finite comparisons of exact sums against stated constants, on synthetic bracket-compatible sequences. The two ceiling searches stop after 200 endpoints without proving the tail in the script. For these parameter sets all initial ceilings are positive; at successive endpoints the ratios are at most `8/6561<1` for T_s (s≤3) and `4/81<1` for V. Thus the omitted endpoints cannot increase the maxima here. This repairs that finite-search justification for the tested parameters, not for arbitrary inputs.
- **S3:** both sides are truncated at n≤6. The implementation checks an aggregate inequality, not separate termwise assertions. The mathematical termwise bound follows directly from `|u_i−u_k|≤b_+n+R_F` and `u_i≥u_k/2`; any nonnegative weight would pass that bound. It therefore does not test the actual fine-slice decay or Yang–Mills flow. The truncation is disclosed, but the explanation `not representable exactly for n≥7` is **REFUTED**: at n=7 the weight is exactly **`22876792454961/2^2187`**, whose denominator has **2188 bits (274 bytes)**. Plain Python `Fraction` constructed it immediately. Far larger n eventually become impractical; n=7 is not that boundary.
- The table's literal `126 sequences × 12 levels × three parameter sets` overcounts by 3. The actual total is **126 sequences across all three sets, hence 1512 sequence/level pairs**, not 4536. The earlier §3.3 wording is consistent with the actual total.

**Claim status:** the Gaussian finite checks are **PROVEN finite computations**; inference from them to (PL-1L), (LGF), source localization, or uniform nonperturbative YM estimates is **NOT-VERIFIED**.

### R8 — CONFIRMED conditional K-dec composition; REFUTED inherited numerical line citations

**Locators:** `TSE55.md:223–240`, Lemma KD; `LINEAR_PACKAGE.md:140–144,153–159,261–282`, Lemmas 2.5/2.7/4.4; `PROOF.md:5396–5405` (Setting N5-0, locate by name), `:5464–5485` (Theorem N5-triv).

Let `A_i` be the conditional fine-curvature response. The Gaussian Markov decomposition gives `𝔎_i=A_i(dC_id*)A_i*`, `i<K`, and `𝔎_K=A_K Cov(F_K) A_K*`. Lemma 4.4 gives `A_i=L^{−2i}K_i^{ax}` on exact forms. Four links per plaquette yield `|dC_id*|≤16c_N5 exp(2m_cov) exp(−m_cov distance)`. Composing the two exponentially decaying response kernels and reserving half the smallest decay rate for separation gives the stated `L^{−4i}` and rate `μ_K=min(m′,m_cov)/2`. Each response sum contributes at most `6 coth⁴(μ/4)`, hence the coefficient **16·6²=576** in the intermediate bound. At the top, `E_K≥c_E‖F_K‖²` implies `Cov(F_K)≤(2c_E)^{−1}` on exact forms; the corresponding coefficient is **6²/2=18**. These factors check out. Gauge-fixing terms do not change the curvature law when the cited admissible quotient construction is used.

This is **CONDITIONAL** on the stated uniform response/locality theorems and admissible Gaussian quotient; it is a free-chain result, not a general-background Yang–Mills covariance estimate. N5's `γ_i` is its spectral gap, not FLOW's coupling ceiling `γ`; no comparison between them is warranted. The displayed N5 constants are uniform because its lower gap and response constants are fixed uniformly, not because a subscript `i` is harmless by itself.

The LP statements were located by strings. Their inherited PROOF line numbers have drifted:

| LP pointer | What that current PROOF line says | Correct current locating line |
|---|---|---|
| LP Lemma 2.5, `l.2181–2218` | line 2181 is cluster-expansion bookkeeping | **2554**, `Lemma N2-a (gauge-orbit lemma)` |
| LP Lemma 2.7, `l.3350–3360` | line 3350 is a nonabelian slice discussion | **3723**, `Lemma E-low` |
| LP Lemma 4.4, `l.3414–3469` | line 3414 starts `Proposition NA-IFT` | **3787**, `Lemma F-df_0 (an exponentially local F-representative...)` |

Those three numerical citations are **REFUTED as current locators**; the intended statements remain identifiable. TSE itself names these lemmas instead of relying on those stale ranges. No direct `PROOF.md l.NNNN` citation was found in TSE. Its separate FLOW line pointer was not rechecked under the file budget and is **NOT-VERIFIED**, not reported as drifted.

### R9 — CONFIRMED: normalization, Gaussian assembly, and the conditional TS constants

**Locators:** `TSE55.md:68–100` (object/symbol pins), `:123–208` (source, GT, coefficient, FREE), `:242–279` (SUM/AF-cmp/Λ-size), `:392–414` (PL-1L/TS); `OSLEAF55.md:166–172` (D8), `:534–563` (TR).

**Object and coefficient, independently rebuilt.** The four corners and the two ordered orientations give `O(f)=Σ_p(½Σ_corners f)s(U_p)`. In coordinates `X=√(2N)Σ_aF^a t^a`, `tr(t^at^b)=δ_ab/2`, the Taylor term is `s(e^{iX})=tr(X²)/(2N)+O(X⁴)=½Σ_a(F^a)²+O(F⁴)`. Hence the action is `u/2 Σ_{p,a}(F^a_p)²` and the quadratic observable is `Σ_{p,a}w_f(p)(F^a_p)²`, with `w_f=¼Σ_corners f`. Equating this Wilson action to the convention with canonical continuum action `¼∫F_std²` gives **`u=2N/g_std²=1/g_FLOW²`**. The continuum clover is `F_std²/(2u)` at this order; it has no extra Z factor. OSLEAF D8 at Z=1 is exactly the centered covariance used by TSE, with matched spacing `ℓ_{K−m}=λ_m`.

For an independent general tensor calculation, orthogonally diagonalize a symmetric T with eigenvalues t_j. On an unordered two-form basis X is diagonal with entries `t_i+t_j`; therefore

`Σ_ordered X² = 4Σ_{i<j}(t_i+t_j)² = 4(d−2)Σ_i t_i² + 4(Σ_i t_i)²`.

For the radial Hessian in four dimensions the eigenvalues are `(6,−2,−2,−2)/r⁴`. Thus the unordered X norm squared is `96/r⁸`, and dividing by `(4π²)²` gives **`Σ_unordered D²=6/(π⁴r⁸)`**. Wick's two pairings and `N²−1` colors give **`c_bub=12(N²−1)/π⁴`**. No coefficient in this chain is refuted. The A4 gate's weakness in R7 does not undermine this separate geometric and algebraic derivation.

**Assembly, independently rebuilt.** For the decreasing filtration, write an image increment as its centered fluctuation. Distinct increments are orthogonal, so total covariance is the sum of expected conditional covariances plus the top covariance. In the Gaussian running model let `c` be the surviving coarse part and `z` the current independent fluctuation. The terms `2c_pz_p` and `z_p²` give `4 E[c_pc_q]a_i(p,q)+2a_i(p,q)²`. Odd mixed moments vanish. Entrywise,

`Σ_i[2a_i²+4a_iΣ_{j>i}a_j]=2(Σ_i a_i)²`.

This proves GT, including the top term and absence of a per-level sign requirement, without any Yang–Mills approximation.

For the coarse scale sums, split at `n₁=⌊(u_k/2−R_F)/b_+⌋`. Before that scale `u_{k+n}≥u_k/2`; afterwards the fixed lower coupling bound and geometric tail beat every fixed power of u_k. Fine scales have `ū_i=u_k` and a summable `L^{4n}exp(−μD_-L^n)` weight. This proves SUM. The same splitting with `|1/u_i−1/u_k|≤(b_+|i−k|+R_F)/(u_i u_k)` and the K-dec slice bound gives an entrywise comparison `O(L^{−4k}u_k^{−2})`, then a bubble error **`O(u_k^{−3})`**. The factor `λ⁸a^{−8}L^{−8k}=1` is exact. No exact beta-function slope is used.

Conditional on the **second-difference torus LGF estimate actually needed** (R11), the positive separated Riemann sum gives `½B≤L_free≤3B/2`, `B=c_bub I_8>0`, after choosing fixed d₀,R₀. The weighted (PL-1L) error sums to `A_1 C_SUM(2+ϑ)u_k^{−2−ϑ}`. At the stated U_* the two errors are each ≤`B/(8u_k²)`, so

`½−⅛−⅛=¼`, and `3/2+⅛+⅛=7/4`.

Thus **Theorem TS's displayed ¼ and 7/4 bounds are CONFIRMED as a CONDITIONAL implication** of its precise weighted error hypothesis, K-dec, FLOW-pw plus the terminal trajectory condition, and the needed LGF estimate. Take d₀,R₀ to be maxima of the input thresholds and FREE's thresholds, and m₀ a nonnegative integer; no input threshold may be overwritten by a smaller output threshold. All constants are fixed before K,R. This is not a proof that YM satisfies (PL-1L).

The phrase `relative O(u^{−ϑ})` must mean **relative to the positive envelope `ū_i^{−2}𝔭_i(k)`**, not relative to `Λ_i`, which can vanish or be negative. The displayed absolute inequality is the usable hypothesis. No relative-error conclusion at a zero per-level value follows.

### R10 — CONFIRMED: the upper-only route and the sequential-limit interface

**Locators:** `TSE55.md:335–389` (relative source radius, SRC-rel, TS-up₁/₂); `:499–522` (T_NF/H-RED); `:604` (E4); `:686–687` (E7, locate by `Route (B) still needs`).

On the assumed bidisc, subtract the two single-source parts. CT vanishes from the mixed derivative by its stated source dependence. Only polymers meeting both supports remain. Fine levels sum to a fixed constant by their separation decay; coarse levels contribute at most a fixed constant per level, hence `O(m+1)`. Cauchy costs `‖f‖∞‖g‖∞/(ε_rel²u_k²λ⁸)`. Multiplying by λ⁸ and using `m≤(u_k+R_F)/b_-` gives **`|W_m|≤C/u_k`**. With (CSL), SUM replaces the coarse count by a constant and yields **`C/u_k²`**. These are valid implications of the source representations as stated, independently of their unproved production.

A fixed absolute source radius produces only the bound **`O(m+1)`** by this argument; this is lack of an AF estimate, not proof that the actual covariance grows. At depth K a λ-sized bump has the extra Hölder factor λ^{-α}; at matched depth k this disappears. This explains the `λ^{-2α}` Cauchy loss for a radius chosen **uniformly over the displayed joint domain `K≥m+d₀`**. It does not prove an obstruction to every use of depth K: for fixed m and K→∞, `u_0/u_k` diverges and the same bump can eventually fit. The sequential H-RED argument does not require a uniform-in-m convergence rate. R5's fixed radius shrinkage is still required for the literal SA-K inclusion.

TR gives `U_-(m)≤u_k≤U_+(m)` with positive linear slopes. At each fixed m pass the bound to the limiting separated D8 value, then send m→∞: `U_-^{-1}→0`, while `L^{ηm}U_+^{-2}→∞` for every η>0. Therefore **κ_e=1 is sufficient for the upper half of H-RED**, paired with the separate lower estimate. The target's E4 already fixes the extra λ⁸ in the original prose; E7 correctly admits that route B does not weaken the combined input because it still uses PL-1L for the lower half.

**Claim status: CONDITIONAL.** Value convergence/regularity and the comparator theorem remain separately supplied. This does not produce an OS reconstruction or a YM witness from the upper bound alone.

### R11 — NOT-VERIFIED: the needed LGF import; REFUTED if its torus wording includes uncorrected zeroth differences

**Locators:** `TSE55.md:194–208`, `(LGF) [m], IMPORTED-standard, not re-derived here`, `on the torus ... the same holds`, and Lemma FREE; `:443–444`, §6.3.

The infinite-lattice estimate and the **uniform second-difference torus bound** are imported, not proved by ts55_1 or the tensor identity. The orbit-cancellation paragraph is a proposed argument, not a completed uniform estimate: one must specify the periodization/zero-mode convention, compare discrete differences, and bound the remainder after cancellation. This review does not certify that import. The Laplacian normalization must also be fixed: here `Δ=d*d+dd*` is the unnormalized lattice Laplacian; on functions in d=4 it is `8(I−P)` for nearest-neighbor simple random walk. A random-walk Green-function theorem therefore needs division by **8** before giving the continuum coefficient `1/(4π²)`.

There is a literal-scope defect in `the same holds ... with an extra ... T^{−4} at |α|=2`. If this asserts the preceding bound for **all** `|α|≤2` on the torus, adding no torus term at α=0, that version is false. The zero-mode equation is `ΔG_T=δ_0−T^{−4}`. On an annulus with radius proportional to T, let `H=G_T−(4π²|x|²)^{−1}`. Then `ΔH=−T^{−4}+O(T^{−6})`. Choose a smooth nonnegative test φ(x/T) supported inside `T/8<|x|<T/4`. If the stated zeroth-order bound `|H|=O(T^{−3})` held there, summation by parts would give

`Σ H Δφ = O(T⁴·T^{−3}·T^{−2})=O(T^{−1})`,

whereas `Σ φ ΔH → −∫φ ≠0`. Contradiction. A general torus version needs a **`T^{−2}` correction at order 0** (and the natural order-1 correction is `T^{−3}`), or should be restricted explicitly to the **order-2 estimate actually used by FREE**, with its stated `T^{−4}` correction. The latter suffices for TS and is the version used in R9. This is a scope correction, not a refutation of that order-2 estimate.

**Claim status:** needed LGF estimate **OPEN in this review / externally supplied**; FREE **CONDITIONAL** on it. No literature-derived PASS is claimed.

### R12 — NOT-VERIFIED: (P1)–(P6) do not yet produce (PL-1L)

**Locators:** `TSE55.md:446–480` (producer reduction), `:605–609` (E5/P6), `:683–685` (E6, locate by name); `STEP55.md:473–511` (CX setting/hypotheses/conclusion), `:517–524` (open instances), `:679–685` (S8/S9); `SRC2_55.md:307–331` (Rep/Flow-pos and Theorem II).

The target is right to label this reduction ARGUED and (PL-1L) OPEN. The conclusion of STEP55 CX is an analytic polymer representation for an interaction integral relative to a **cut** product Gaussian. Even if CX is accepted, Cauchy estimates its source derivatives in an absolute analytic norm. It does not, by itself, identify the exact e-image with the unit-coefficient quadratic image, identify its mixed covariance, or bound that error relative to a potentially zero Gaussian entry. The Gaussian normalization, source dependence of the Hessian/background, inherited activities, and restoration of the cut complement need their own matching estimates. STEP's S8 also changes the decay rate by a fixed fattening factor and puts a fixed box-volume factor into H_V; those constants must be incorporated before comparing rates or smallness thresholds.

If the resulting **uniform** bound really has `H_V≤C u_i^{−1/2}(log u_i)^q`, then any fixed `0<ϑ<1/2` can absorb the logarithm. This arithmetic does not establish that bound for the inherited/source-dependent terms. P4's proposed top-down induction remains unwritten, including its gauge-covariant pairing, error norm and cumulative error budget. P5 has only been posited. P6's O(1/u_i) scalar kernel-coupling mismatch does not alone control the whole quadratic operator: extracting `β[S_i]=u_i` fixes one coefficient, while resolvent/response comparison needs the full Hessian, with uniform gap/locality constants.

Similarly, the current SRC2 theorem gives a representation on its particular `r₀λ^α` source domain with a separate (Flow-pos) requirement. Increasing a radius to `ε_rel u_kλ⁴/‖f‖∞` for the normalized witness and integrating the top variable with a bounded mixed remainder are stronger producer tasks. They do not follow merely by renaming the radius. SA-K controls a tree-level contraction on its stated domain; it does not supply complex position-dependent flow or the fluctuation representation.

Thus **one named sufficient YM input** is a legitimate packaging of the conditional theorem, but **one solved/reduced singleton obligation is not**. In particular R4 prevents collapsing source-image upper bounds and normalized two-point matching into one completed leaf. The strongest unverified piece is still uniform matching for the actual Z=1 clover images at all short scales, with summable signed errors and large-field terms.

### R13 — CONFIRMED: the LF threshold arithmetic, with its quantifiers and scope

**Locators:** `TSE55.md:472–478`, (P5); `:568–570` (V8, locate by name); `CODEX_REVIEW_NONFREE.md:18–26`, R1.

At `2p=1`, `exp[−c log(1/g_j)]=u_j^{−c/2}` in the lane convention. For U large and b>0, integral comparison gives

`Σ_{n≥0}(U+bn)^{−c/2} = U^{1−c/2}/[b(c/2−1)] + O(U^{−c/2})` for c>2.

It is therefore `O(U^{−2−ϑ})` exactly when **`c≥6+2ϑ`**; equality is allowed for this big-O target. It is `o(U^{−2})` exactly when **c>6**. The body briefly writes `c>6+2ϑ` but its following derivation and final statement correctly allow equality. For example `ϑ=1/2,c=7` gives exponent **−5/2** and integral coefficient **2/(5b)**. For `2p>1`, the exponential of a superlinear power of log u is bounded by u^{-M} for every fixed M at sufficiently large u; choosing M>3+ϑ makes the scale sum sufficiently small.

The coarse-level omission in the original λ≥ℓ_j formulation is real. A coarse-scale summability bound is needed for this route, and the proposed canonical factor supplies it. Its *precise exponent 8* is sufficient rather than logically necessary (R3). These are **PROVEN arithmetic implications of the per-level LF estimate as stated**; they do not prove the LF estimate, its event localization, or absence of additional inverse-coupling/scale losses. Those remain **OPEN**.

### R14 — CONFIRMED: separated Lemma-V contribution is zero; RP gives only a sign; SA-E1 is only an upper bound

**Locators:** `TSE55.md:283–297` (LV-sep/RP), `:325–330` (tree bound), `:558–562` (V5, locate by name); `SRCAN55.md:543–584`, SA-E1 and E2.

For the sparse set S of links oriented in direction 1 with all-even base coordinates, no plaquette contains two selected links. Conditional on all other links, the selected links are independent. The six plaquettes through a given selected link have corner-set diameter √5a. At support separation >4a, its contribution can therefore depend nontrivially on at most one source. Every summand in the conditional mixed covariance is zero, so **`E Cov(O(f),O(g)|𝔉)=0` exactly**. The covariance of the conditional means remains; a same-point variance lower bound does not bound it from below. For a reflected pair RP implies nonnegativity and supplies no positive numerical lower bound.

For SA-E1, `Σ_p|h_□|≤12Σ_x|h(x)|` and `s(e^X)≤‖X‖op²/2`, combined with the assumed background plaquette bound, give the corrected coefficient **6** (or **6/N** with a Frobenius-norm plaquette bound) and the canonical `ℓ_r^{−4}` scaling. This verifies the elementary implication under the background hypothesis, not that hypothesis itself. It is a tree-level size upper bound. Neither it nor formal constant-curvature reproduction fixes the coefficient of the *quantum* images or their two-point covariance. **Claim status: PROVEN elementary consequences / CONDITIONAL on the cited tree background bound.**

## Scope, provenance, and systemic checks

The target's §10 errata E1–E5 and final E6–E8 were read and respected. In particular the already repaired growth rate, extra λ⁸, and omission of P6 are not counted as new outstanding findings. The target hash recorded during this review was `d02cc8b265c20da5fc59812a59d68e12d3c9a550d9f9df0890db1c61a38f7340` (SHA-256). The final stability check at **2026-10-29 06:51:11 UTC** returned the same hash. The deliverable's PRE-STATED-first structure, fourteen findings and summary/bank sections were also checked.

All scientific attachments without a directory prefix are under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. Read named sources: TSE55, bounded portions of OSLEAF55, SRCAN55, SRC2_55, CODEX_REVIEW_NONFREE, LINEAR_PACKAGE and PROOF, and ts55_1–3's scripts/criteria. The methodology file named by the owner's entry instructions was also read. The two additional files were `/Users/jonBridger/.codex/skills/review-loop/SKILL.md` and `STEP55.md` (CX and its relevant errata only). The user's restricted deliverable/read contract controlled this review; no landing/audit workflow was launched. No git command, snapshot, audit-ledger read, external messaging, or source-file edit was used. No extra report or test file was written. Python computations used exact rational/symbolic arithmetic; the three small checks ran sequentially.

- **Symbol collisions:** the critical unchecked comparison was the two ε̂_* radii (R5). Separately pinned: u versus g_std/g_FLOW; k=K−m versus the terminal K; kernel κ versus κ_e/κ_e′ and polymer entropy; N5's γ_i versus FLOW's γ; torus R versus R_F; c_LF multiplying log(1/g) versus a coefficient multiplying log u. No imported C_1/c_1 or smallness threshold was accepted by its name alone. In particular P1's C_1 is the CE activity constant, not a Hessian gap or a source radius.
- **Stale minima/quantifiers:** the source radius must be newly chosen below the already fixed SA-K threshold; d₀,R₀ must dominate all input thresholds; u_K is fixed by the trajectory while u_k grows with m; the scale limit is taken only after the fixed-m continuum limit. Finite sample maxima and n≤6 checks are not uniform suprema unless supplemented by the analytic arguments above.
- **Checks that cannot decide:** A4 assumes its clover multiplicity; G3's scaling test follows homogeneity; S3 uses a bracket inequality valid for any positive test weights. None decides source-image normalization, canonical quantum localization, large-field decoupling, LGF, or actual Yang–Mills one-loop matching. The all-orders torus reading of LGF would itself be an impossible hypothesis; its needed second-order clause must be stated separately.

## Summary table

| Finding | Review verdict | Claim status and disposition |
|---|---|---|
| R1, bare action derivative | REFUTED | PROVEN correction: +2, not −2 |
| R2, unsuppressed growth | CONFIRMED | PROVEN order Θ(u_k²); E3 already repairs the body |
| R3, necessity of exact canonical factor | REFUTED | GAP in universal necessity; any fixed exponential decay suffices for the displayed summation |
| R4, LOC-e equals matching obligation | REFUTED | OPEN: upper image control does not fix a coefficient or two-point remainder |
| R5, source radius fits SA-K | NOT-VERIFIED; same-threshold reading REFUTED | CONDITIONAL after an explicit test-dependent shrinkage |
| R6, multiplicative fine-share error | REFUTED | PROVEN additive repair; actual lane nonvanishing NOT-VERIFIED |
| R7, implemented finite checks | CONFIRMED; description defects REFUTED | PROVEN finite outputs; A4/S3 limits, 1512 pairs, exact n=7 weight disclosed |
| R8, K-dec composition / citations | CONFIRMED / REFUTED | CONDITIONAL free-chain composition; three stale PROOF pointers corrected |
| R9, normalization and TS assembly | CONFIRMED | CONDITIONAL TS with ¼, 7/4 and 12(N²−1)/π⁴; actual PL-1L OPEN |
| R10, κ_e=1 upper route / H-RED | CONFIRMED | CONDITIONAL; radius production and limit existence remain inputs |
| R11, needed second-difference LGF | NOT-VERIFIED | OPEN import in this review; literal uncorrected order-0 torus extension REFUTED |
| R12, producer reduction P1–P6 | NOT-VERIFIED | ARGUED/OPEN; no uniform source matching proved |
| R13, LF thresholds | CONFIRMED | PROVEN arithmetic: 2p>1, or c≥6+2ϑ for the stated big-O error |
| R14, LV-sep, RP, SA-E1 size | CONFIRMED | PROVEN elementary implications; no positive quantum lower bound follows |

## Exactly what may be banked

1. **PROVEN algebra:** the exact clover source identity, the quadratic normalization `u=2N/g_std²`, the Gaussian conditional-covariance decomposition including every level, and `c_bub=12(N²−1)/π⁴`. These concern the same OSLEAF Z=1 observable at matched level k=K−m.
2. **PROVEN implications from named inputs:** SUM and AF-cmp from the stated flow/slice bounds; K-dec as the composition of the stated free response/coercivity/locality bounds; FREE from the **needed order-2** lattice/torus estimate. The underlying imported estimates do not acquire an unconditional certification here.
3. **CONDITIONAL TS:** with the precise absolute weighted (PL-1L) error, K-dec, FLOW-pw plus the terminal trajectory, and the needed LGF clause, the bounds `¼c_bub I_8u_k^{-2}≤W_m≤(7/4)c_bub I_8u_k^{-2}` follow uniformly with properly enlarged input thresholds. Exact beta-function slope data are unnecessary for this assembly.
4. **CONDITIONAL upper route:** SRC-rel plus FLOW-pw gives κ_e=1, enough for H-RED's upper half. Adding CSL gives κ_e=2. Fixed-m limit passage is valid once the named separated-value convergence holds.
5. **PROVEN scoped obstructions/corrections:** Lemma V's selected-link variance mechanism contributes exactly zero at separated supports; RP alone provides no magnitude; a single matched image can omit a leading Gaussian source–source term; some coarse-scale summability control is needed by this bound-based route, with exponent 8 sufficient but not universally necessary; the LF threshold arithmetic and the corrections R1/R5/R6/R7/R8/R11 are as stated above.

**Not banked:** (PL-1L) for Yang–Mills; its proposed P1–P6 production; replacement of two-point normalization/matching by SRCAN's (LOC-e); actual nonvanishing of the lane's fine-share coefficient; the needed LGF import as a re-derived theorem; SRC-rel/CSL/LF-dec; or an unconditional Yang–Mills non-freeness witness.

**Single most dangerous unverified item:** uniform (PL-1L) for the exact Z=1 clover images—especially their unit-coefficient quantum matching and summable two-insertion/large-field error above the source scale. A canonical first-image upper bound cannot supply that positive lower-bound information.

