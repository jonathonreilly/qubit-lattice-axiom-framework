# C5 R16-10 report: close R16-2? F_s(0⁺) ≠ 0 class-wide, the λ → 0 limit, and the tuning count

**Author.** Claude Opus 5.5 probe. This is the same model family as the supervisor and every C5 worker. Unrefereed. Written 2026-10-12, 23:20Z to about 23:50Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R16-10/`. Scripts and `.out` files are in `S/`. Copies of the archived R13-7, R16-1 and R16-2 runners are in `S/arch/`. Every run took under 2 min with `OMP_NUM_THREADS=2`. There were no downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`); R13-7 (`:4736-4747`, `:4844-4858`); round 16 items 1–5 (`:5037-5162`); the R16 verdicts (`:5414-5447`); item 10 (`:5449-5476`).
- `agents/`: `C5_R16-2_report.md`, `C5_R16-2_referee.md`, `C5_R16-2_referee_verdict.md` (`vR16-2`); `C5_R16-1_report.md` (§§0–3.2) and its verdict; `C5_R13-7_report.md` and its verdict.
- `SUMMARY.md` §26 (`:677-714`).

**Labels.** **proved** = complete under the stated hypotheses (unrefereed). **checked** = numerics here. **suggested** = argued, not proved. **reading** = an interpretation. **comparator** = literature, RECALLED.

**Rechecking the archived runners.** I re-implemented R16-2's scalar runner and R13-7's Dirac on-shell runner point by point (`r1610_core.py`). On the same grid they reproduce the archived runners to all 10 printed digits (`r1610_validate_exact.out:1-2`).

---

## 0. In plain words

1. **The λ → 0 limit exists. There is no log (proved, Theorem L).**
   - Inside both boxes, the lattice integrand is exactly the continuum one. I split off a small ball of photon momenta there.
   - In the continuum, that ball contributes one universal number K_s for each spin. The 4-dimensional rotation symmetry kills everything else in it.
   - Everything outside the ball is IR-safe. So F_s(m, λ) has a joint limit as m, λ → 0, whatever the path, and **F_s(0⁺) = K_s + Λ_s**. Here Λ_s is an ordinary lattice integral at m = λ = 0.
   - **K_0 = −1/3** (closed form, proved). **K_½ = +2/3** (checked to 6 digits).
   - This also explains the N- and λ-drift R16-2 saw: K_s sits at |q| ≲ max(m, λ), which a fixed grid cannot resolve.
2. **Dirac: a zero exists in the registered class (REFUTED-ZERO, checked).**
   - **Ingredients.** Keep the subluminal D1(1.4, 1/√3) electron, and keep R8-5's photon box (d = q on |q| ≤ 1). Outside the box, multiply the photon's lattice branch by G: d = ρq + (1 − ρ)·G·2 sin(q/2).
   - **Membership in the class.** For G ≥ π/2 this symbol is nondecreasing (proved), so the law is in the class registered at `TESTS:5460-5462`.
   - **Why a zero must exist.** As G grows, F_½(0⁺) rises from −9.74 (G = 1) to +0.687 (G = 16), toward K_½ = +2/3.
   - **Where it is.** F_½(0⁺) = 0 at **G\* = 3.1264** (N = 96; 3.1271 at N = 64). The sign change is ±0.027 at G\* ± 0.05.
   - **Robustness.** The zero is stable under the split radii, the p-step, m ≤ 0.01 and λ ≤ 1e-3. The refereed R13-7 runner, run directly, converges toward the same value.
   - **The cost.** This photon is **faster than light at the lattice scale**: whole-zone v_max = 7.35.
3. **With a slower-than-light photon (d′ ∈ [0, 1]) I found no Dirac zero.**
   - Sampled laws give F_½(0⁺) ≤ −3.8 (checked).
   - New bound (proved): the tadpole is ≤ −2.02 for every such photon. A zero would need the rest to exceed +2.02. The rest is not bounded by proof. **OPEN on that subclass.**
4. **Scalars: no zero found. OPEN.**
   - Every resolved sample has F_0(0⁺) < K_0 = −1/3.
   - Stiffening the photon makes F_0(0⁺) approach −1/3 from below and never cross it (checked).
   - Suggested: F_0(0⁺) ≤ −1/3 on the whole class. Not proved.
   - Some N = 32 search values above −1/3 were quadrature artefacts of sharp band edges. They fall to between −0.55 and −2.2 at N = 128 (`r1610_recheck.out`).
5. **The count (reading, from the checked zero).**
   - **SM Dirac content, registered class: n_t = 2.** One photon-shape equation (G = G\*) aligns every charge class, up to residuals ≲ 1e-21. One photon-side condition (κ_γ, or a matter shape with Σ = 0) aligns the photon.
   - **Lower bound n_t ≥ 2: proved, given Lemma Q and the checked Σ ≠ 0 on D1.**
   - So R16-2's 7 or 3 does not hold on the class as registered. It survives only on a subclass that forbids lattice-scale superluminal photons, and only if Lemma F holds there, which is open.
   - **The mechanism (reading).** The photon symbol is a law parameter that acts exactly like a q²-correlated matter counterterm: it shifts every species' F by the same amount, times q_i².
6. **Literal corners.** Each literal Dirac field carries 6 independent valley–direction speeds (reading). Each is q² times its own function. They are not computed; the edge is excluded by R9-1 anyway.
7. **Against the FIXED readings:**
   - **Dirac: REFUTED-ZERO** (checked; the class as registered allows a superluminal photon; see §4).
   - **Scalar: OPEN.**
   - **COUNTED: not met** for either spin.

---

## 1. Hypotheses and classes (stated before any title)

- **Setting** (`TESTS:5459-5465`).
  - One loop on Z³ × ℝ (continuous time), with Peierls coupling along axis paths, Feynman gauge and photon mass λ ≥ 0.
  - The on-shell speed is as in R13-7/R16-2: δc = (c² − 1)/2 along an axis at p → 0, printed in units of e²/16π².
  - The photon is the external soft leg, and the loop variable q is the photon momentum. The matter momentum is k = p − q.
  - Counterterm conventions are as in vR16-2 (`C5_R16-2_referee.md:140-166`).
- **Class 𝒞 (as registered).**
  - Matter: separable box edges with exact continuum symbols on |k_j| ≤ b, b > 0.
    - Dirac: S ≤ q on [b, π], Wilson or not.
    - Scalar: u′/2 ≤ q on [b, π].
  - Photon: t = d² even, periodic and C², t = q² + O(q⁴), **d nondecreasing on [0, π]**. Subluminality is not part of the registered text (`TESTS:5461`).
- **Subclass 𝒞_sub (stated separately).** 𝒞 with d′ ∈ [0, 1], i.e. a nondecreasing photon whose whole-zone v_max ≤ 1.
- **Families used** (each states its whole-zone v_max, as S17's rule `TESTS:5039` requires).
  - **D1(b, r)** (R14-1, verbatim `make()`): v_max ≤ 1 for r ≤ 1/√3 (proved, `vR16-1:15`).
  - **Literal L(b₁, b₂)** (R8-5, r = 0).
  - **Dip-rise** (R16-2): S ≤ q checked per law.
  - **Scalar G(b)** = Flat(b, π − b), and **Flat(b, w)**: u = h², h′ = 1 − sstep((|k| − b)/w), so the band is flat beyond b + w. These have u′/2 = hh′ ≤ h ≤ k.
  - **Photons.**
    - R8-5's photon R85(c₁, c₂, G): d = ρq + (1 − ρ)·G·2 sin(q/2). G = 1 is R8-5's own photon; G > 1 is stiffened.
    - Gph(c): d = h_c, with d′ ∈ [0, 1] and d = q on |q| ≤ c.
- **Subtractions named before the runs.** The only subtraction is the split identity of Theorem L, which is exact. No fit. The p-derivative uses Richardson on p ∈ {0, h, 2h} as in the runners.

## 2. Prior art (each counted once)

- **R16-2 and its verdict.**
  - Lemma Q: q_i²F_s, and the photon shift does not depend on λ or on the photon symbol (`vR16-2:5`).
  - Lemma T′: tadpole ≤ −½⟨w(π)⟩ and seagull ≤ −¼⟨w(π)⟩ (`C5_R16-2_report.md:135-141`, `vR16-2:9`).
  - Lemma F, checked only (`vR16-2:11`).
  - The open remainder obligation (`C5_R16-2_referee.md:118-126`).
  - The overshoot zero, outside 𝒞 (`C5_R16-2_report.md:218-221`).
  - Proposition C's 7/3 (`vR16-2:13`).
  - κ_γ is replaceable (`C5_R16-2_referee.md:142-151`).
- **R13-7.** The on-shell runner (`vR13-7:3`) and the tadpole lemma (`C5_R13-7_report.md:111`). Theorem Sgn's integration-by-parts mechanism (`C5_R13-7_report.md:154-163`), counted once through T′.
- **R16-1.** Lemma A_W (analyticity at λ > 0) and Theorem W (`vR16-1:5,9`). Used only for scope.
- **Comparator (RECALLED).** Collins, Perez, Sudarsky, Urrutia and Vucetich (2004): a spatial-momentum cutoff leaves an O(α), cutoff-independent Lorentz-violating speed term, containing a universal piece. K_s here is the lattice-QED analogue for a photon-momentum cutoff. The content is RECALLED; the numbers here were computed independently.
- **Grep** for "K_s", "IR excision", "stiff photon", "superluminal photon" over `agents/`, `TESTS` and `SUMMARY`. Nothing found on a photon-shape zero of F_s, or on a universal continuum constant in the matter speed.

## 3. Results

### 3.1 Theorem L (IR excision; the λ → 0 and m → 0 limits). Proved; checked

- **Claim.**
  - **Hypotheses.** One loop, Peierls coupling, Feynman gauge. Matter symbols are continuum on |k_j| ≤ b, and the photon has d = q on |q| ≤ c, with b, c > 0. All symbols are C². At m = 0, the matter band vanishes only at k = 0 and at isolated valleys outside the excision ball (literal corners).
  - **The split.** Let χ be a smooth radial cutoff: χ = 1 on |q| ≤ r₀ and χ = 0 on |q| ≥ r₁, with r₁ < min(b, c). Then for every (m, λ) with m + λ > 0:

    F_s(m, λ) = Σ_BZ f_lat(q; m, λ)(1 − χ(|q|)) + Φ_χ(m, λ),   Φ_χ := ∫_{ℝ³} f_cont(q; m, λ) χ(|q|) d³q/(2π)³.

  - **The limit.** Φ_χ → K_s as (m, λ) → 0 along any path. K_s does not depend on χ or on the law. The lattice term is continuous at (0, 0).
  - **Conclusion.** F_s(0⁺) exists, does not depend on the path, carries no ln λ or ln m, and equals **K_s + Λ_s**, with Λ_s = Σ_BZ f_lat(q; 0, 0)(1 − χ).
- **Proof.**
  1. **Identity.** On supp χ, every Feynman rule equals the continuum one, because both lines and the external p sit inside both boxes (R8-5's design; R16-2 Lemma Q step 5, `C5_R16-2_report.md:125`). So f_lat = f_cont there.
  2. **Ball structure.** Write χ = ∫(−χ′(r)) 1_{|q|<r} dr. For one ball, use Fubini over q₀:

     ∫_{|q|<r} f_cont = Λ[4-ball |Q| < r] + ∫_{cyl(r)∖4-ball(r)} I_cont,

     where I_cont is the q₀-unintegrated integrand.
     - **The 4-ball term is exactly zero.** It is the self-energy integral over an O(4)-symmetric region, so it is a function Π_ball(P²) alone. On the mass shell P² = −m² that function is constant, and its finite value does not depend on p. So it contributes 0 to dΠ(iE_p, p)/dp². This holds at λ = 0 too, because only the on-shell value enters the first-order shift.
     - **The remainder is IR-free.** The region {|q| < r, |Q| ≥ r} keeps away from Q = 0, and the integrand decays like |q₀|⁻⁴. Dominated convergence therefore gives the (m, λ) = (0, 0) value.
     - That value is r-independent by homogeneity (degree −4). Call it K_s. Since ∫(−χ′) = 1, Φ_χ → K_s.
  3. **The lattice term.** On |q| ≥ r₀, W ≥ d(r₀/√3) > 0. The matter E_k is bounded below except at isolated valleys. There 1/E_k is integrable, and the p-derivative can be routed through the photon by the BZ shift q → q + p. So dominated convergence applies. ∎
- **Uniformity.** The dominating functions depend only on min(b, c), the C² norms of the symbols, and the lower bounds of W and E_k off the ball. So the limit is uniform on any subclass with those bounds fixed. It is **not** uniform on all of 𝒞, where boxes can shrink to 0.
- **Not covered.** Photons with no box (naive 2 sin(q/2)): the identity then holds only up to an O(q²) mismatch on supp χ. The same conclusion is suggested, not proved.
- **Checked.**
  - The split reproduces the direct refereed runners at finite (m, λ), and converges much faster in N:
    - G(1.4), photon (1, 2), m = 0.1, λ = 0.05: split −2.7519/−2.7520/−2.7519 at N = 48/64/96, against the direct runner −2.7031 (N = 96) and −2.7390 (N = 128);
    - D1(1.4, 1/√3), photon (0.7, 1.4): split −9.955 ± 0.006, against the direct runner −9.895 (96) and −9.934 (128) (`r1610_validate_split.out:1-20`).
  - Moving the split radii (r₀, r₁) from (0.15, 0.5) to (0.3, 0.9) changes Λ_½ by < 1e-5 (`r1610_zero_checks.out:4-15`). That is the zero-shell-average property, checked.
  - λ and m: F(0⁺) moves by ≤ 1e-4 between (m, λ) = (1e-6, 0) and (1e-3, 1e-3) (`r1610_zero_checks.out:19-24`).
- **Consequence for R16-2 (reading).** The registered "(b) λ → 0" obstruction does not exist: no IR log. R16-2's λ-trend of −0.07 at N = 192 (`C5_R16-2_report.md:191-196`) is the unresolved K_s region, not physics.

### 3.2 The universal constants K_0 and K_½. Proved (scalar); checked (both)

- **Scalar (proved).** At m = λ = 0 the second-order part of the exchange integrand is −3P²/Q⁴ + 4(P·Q)²/Q⁶. The on-shell combination ∂_{p_x²} − ∂_{p₀²} kills P², leaving I^LV = 4(q_x² − q₀²)/Q⁶.
  - On the region {|q| < r < |Q|}, in 4D polar angle ψ (q₀ = |Q|cos ψ), the radial integral is ln(1/sin ψ).
  - The angular integral is J = ∫₀^π sin²ψ(sin²ψ/3 − cos²ψ) ln(1/sin ψ) dψ = −[(4/3)I₄ − I₂] = −π/24, using I₂ = (π/4)(1 − 2ln2) and I₄ = (3π/16)(7/6 − 2ln2).
  - So c² − 1 = 16π·J/(2π)⁴ = −1/(24π²), and **K_0 = 8π²(c² − 1) = −1/3**.
- **Dirac (checked; closed form suggested).** The Dirac LV integrand is proportional to the same (q_x² − q₀²)/Q⁶, so K_½ is a multiple of the same J. Numerically K_½ = +0.666666 to +0.666667 at (m, λ) = (1, 1), (1, 0.1), (0.1, 1), (1, 0) (`r1610_K.out`). Suggested: K_½ = −2K_0 = +2/3.
- **Checked.** K_0 = −0.333331 to −0.333349 at the same four (m, λ) points, confirming that K does not depend on m or λ. One R = 20000 row degrades to −0.3246 from finite-difference cancellation at large r (`r1610_K.out:4`).
- **The stiff-photon limit (suggested; checked trend).** If the photon is made infinitely stiff outside a cube inside the matter box, every lattice region is suppressed. The leftover continuum cube-minus-ball region contributes 0: the angular profile is P₂(n_x) and the cube is cubic-symmetric. So **F_s → K_s.** Checked at G = 16:
  - Dirac: +0.687, +0.680, +0.691;
  - scalar: −0.353, −0.352, −0.435 (`r1610_scan_N48.out:10,20,30,40,50,60`).

### 3.3 (a) Dirac: an explicit law in 𝒞 with F_½(0⁺) = 0. Checked

- **The law.**
  - Electron D1(b = 1.4, r = 1/√3), R14-1's construction verbatim. It has S ≤ q (`C5_R16-2_report.md:143-146`) and v_max ≤ 1 (`vR16-1:15`).
  - Photon R85(c₁ = 1.0, c₂ = 2.0, G), d = ρ(q)q + (1 − ρ(q))·G·2 sin(q/2), with R8-5's C^∞ plateau ρ.
  - One loop, Peierls coupling, Feynman gauge.
- **Membership (proved).**
  - d′ = ρ + (1 − ρ)G cos(q/2) + ρ′(q − 2G sin(q/2)). Here ρ′ ≤ 0, and 2 sin(q/2) ≥ 2q/π on [0, π], so q − 2G sin(q/2) ≤ 0 when G ≥ π/2. Hence d′ ≥ 0.
  - d = q on |q| ≤ 1, so the photon is box-exact and tree c_γ = 1.
  - d is odd, and t = 2G²(1 − cos q) near ±π, so t is even, periodic and C^∞.
- **The zero (checked).**
  - F_½(0⁺) = K_½ + Λ_½ changes sign between G = 2 (−1.330) and G = 4 (+0.313) (`r1610_scan_N48.out:8-9`).
  - Bisection gives **G\* = 3.1271 (N = 64) and 3.1264 (N = 96)** (`r1610_zero2.out:1-2`), and 3.1279 at N = 48 (`r1610_zero_bisect.out:2`).
  - At G = 3.12788, F(0⁺) = −0.00001, +0.00041, +0.00075 at N = 48, 64, 96. At G\* ± 0.05 it is ∓0.027 (`r1610_zero_checks.out:1-9`).
  - It is unchanged to < 1e-5 under the split radii and to 4e-5 under h = 0.01, and moves by ≤ 0.0016 for m ≤ 0.01 (`r1610_zero_checks.out:10-27`).
  - At N = 128, G = 3.1264: F(m → 0) = −0.00003 (`r1610_litm.out:6`).
  - **Transversal:** dF/dG = +0.537 at the zero (`r1610_zero2.out:2`).
- **Independent check with the refereed runner (checked).** R13-7's `ce2_minus_1`, unmodified, on this law (G = 3.1265) at m = 0.1, λ = 0.05 gives +0.067, +0.027, +0.014 at N = 96, 128, 160. The split value at the same (m, λ) is +0.003 (`r1610_direct.out:2-5`). On D1 with an unstiffened R8-5-type photon, (0.7, 1.4) at G = 1, the same runner gives −9.93 (`r1610_validate_split.out:14-15`). So the refereed code itself moves this law from about −10 to F ≈ 0, to its resolution.
- **The zero is a curve, not a point (checked)** (`r1610_zero2.out`):
  - G\*(b) = 3.126 (b = 1.4), 3.170 (1.2), 3.270 (1.0) on D1(b, 1/√3);
  - 3.124 on D1(1.4, r = 0.2);
  - 2.893 on the literal edge (2, 3).
- **The photon's speed (stated, S17 rule).** At G\*: min d′ = 0.0000, max d′ = **7.353** at q = 1.574, d(π) = 6.253 (`r1610_direct.out:1`). The whole-zone photon v_max is 7.35, attained on the axis. The electron's is ≤ 1.
- **Mass dependence at the zero (checked).** F(m) − F(0⁺) = +0.0009, +0.0023, +0.0061, +0.0182 at m = 0.005, 0.01, 0.02, 0.04 (N = 128, `r1610_litm.out:6`). The leading behaviour is linear, with slope ≈ 0.2, from the Wilson term. On the literal edge it is quadratic, ≈ 7.4m² (`r1610_litm.out:1-4`), consistent with R16-2's evenness.

### 3.4 The subluminal-photon subclass 𝒞_sub. Bound proved; no zero found; OPEN

- **Lemma T′_sub (proved).**
  - If d′ ∈ [0, 1], then d(q) ≤ q, so w(π) ≥ 1/(π²√(π² + q_y² + q_z²)).
  - Hence ⟨w(π)⟩_⊥ ≥ 0.025587 (Gauss–Legendre 200², `r1610_recheck.out:13`).
  - With R16-2's T′: **Dirac tadpole ≤ −2.020, scalar seagull ≤ −1.010** (λ → 0), for every S ≤ q (u′/2 ≤ q) matter edge.
- **Consequence.** A subluminal-photon Dirac zero needs the rest, K_½ + (non-tadpole lattice part), to be ≥ 2.02.
  - On the D1 and literal Gph laws in `r1610_scan_N48.out:2-7,12-17,22-27`, the rest (F − tadpole) is −0.82 to +0.12.
  - R16-2 saw at most +1.9, on dip-rise edges, whose tadpoles are −14 to −18.
- **Random search (checked, indicative).** 92 laws in 𝒞_sub: D1, literal and dip-rise matter, with Gph or monotone R85 G = 1 photons. Every one has F_½(0⁺) ≤ −3.82 (`r1610_search_dirac_sub.out`, last lines).
  - Caveat: the search used N = 32. Laws with plateau widths below about 0.3 are under-resolved there, as §3.5 shows for scalars.
- **Reading.** On 𝒞_sub, F_½(0⁺) < 0 on every sampled law, with a margin ≥ 3.8. No proof bounds the non-tadpole part. **OPEN.**

### 3.5 Scalars. No zero found; OPEN

- **Proved.**
  - F_0(0⁺) = −1/3 + Λ_0 (Theorem L).
  - The seagull part of Λ_0 is ≤ −¼⟨w(π)⟩·16π² < 0 (R16-2's T′), and ≤ −1.01 on 𝒞_sub.
- **Checked.** Resolved values:
  - 30 scan rows (`r1610_scan_N48.out:31-60`): G(1.4), G(2.6) and G(0.6), each under R85(1, 2, G = 1), Gph(0.6–3.0) and stiff R85(1, 2, G = 2, 4, 16) photons. All have F_0(0⁺) ∈ [−3.35, −0.352].
  - 35 targeted rows with the matter box below a stiff photon's box (`r1610_scalar_target.out`; only its last 40 lines were kept). The top five are rechecked at N = 96 and lie in [−0.488, −0.372].
  - **In every resolved row, F_0(0⁺) < −1/3. Stiffening the photon approaches −1/3 from below.**
- **Artefacts.**
  - The N = 32 random searches (`r1610_search_scalar_*.out`) report values up to −0.187.
  - On recheck, those laws (band-edge widths w = 0.05–0.13) give −3.06/−2.17, −1.40/−1.10, −3.76/−1.46 and −0.65/−0.55 at N = 64/128 (`r1610_recheck.out:1-12`).
  - So the N = 32 searches are not evidence for anything near zero.
- **Suggested.** Λ_0 ≤ 0 on 𝒞, i.e. **F_0(0⁺) ≤ −1/3**. That would make COUNTED's "F_0 ≠ 0" part a theorem. I have no proof. The exchange lattice part is positive, and termwise bounds fail, as the referee found (`C5_R16-2_referee.md:118-126`).

### 3.6 (c) Minimality in a convention-independent form. Reading, with a proved lower bound

- **Definition.**
  - Fix the parameter space 𝒫 before counting. It consists of:
    - the continuous shape parameters of the class (matter and photon symbols);
    - one independent coefficient for each counterterm operator allowed by the lattice symmetries. Here that is one kinetic coefficient per species and κ_γ. No coefficient correlations are prescribed, since none is symmetry-enforced.
  - **A tuning** is one real equation on 𝒫 that is not satisfied at the parameter's natural value. Counterterms are natural at 0. Shape parameters have no natural value, so any equation on them counts.
  - **n_t** is the least number of tunings whose solution set aligns every species, |c_i − c_γ| ≤ ε_i.
  - This removes vR16-2's ambiguity about q²-correlated counterterms (`C5_R16-2_referee.md:158-162`): they are not in 𝒫 unless a symmetry forces them. Shape correlations are allowed, because they are law parameters.
- **Result on 𝒞 (SM charged Dirac content, N_s = 9, three charge classes): n_t = 2.**
  - **Sufficiency (checked).**
    - Set G = G\*(b), so F_½(0⁺) = 0. All per-species counterterms stay at 0.
    - Then δc_i = q_i²·F_½′·m_i a·u. With the measured slope ≈ 0.2–0.37 (`r1610_litm.out:6`, `r1610_zero2.out:2`), the top quark's is ≤ 0.37·1.41e-17·(4/9)·5.807e-4 ≈ 1.3e-21, below ε\* = 2.66e-19 (`C5_R8-5_report.md:261`) by a factor of about 200.
    - Then set κ_γ = −Σ, with Σ = 5.807e-4·Σ_j n_j q_j² G_½ ≈ 3e-3 on D1 (`C5_R16-2_report.md:186-190`). Or choose a matter edge with Σ = 0 instead, as the referee found possible in the literal family (`C5_R16-2_referee.md:147`).
  - **Lower bound n_t ≥ 2 (proved, given Lemma Q and two checked facts).**
    - The two facts:
      - (i) Σ depends only on the matter edge (Lemma Q, proved), and Σ ≠ 0 on D1 (checked, G_½ = +0.08 to +0.67, `C5_R16-2_report.md:186`);
      - (ii) F_½ ≠ 0 off the zero curve (dF/dG ≠ 0, checked).
    - The argument:
      - One equation that is not F = 0 leaves classes of different q² split by |q_c² − q_c′²||F|u. That exceeds ε\* unless |F| ≤ ε\*/((4/9 − 1/9)u) = 1.4e-15, which is itself the equation F = 0 at that precision.
      - The equation F = 0 alone leaves Σ ≠ 0 at every D1 point of the zero curve.
      - So one equation never suffices on D1.
    - **Gap.** On edges where Σ and F could vanish together on a hypersurface, the bound is not proved. That would need Σ ≡ 0 on an open set of matter edges, which is not excluded.
  - **Required precision.** |ΔG| ≤ ε\*/(u·dF/dG) = 2.66e-19/(5.807e-4·0.537) ≈ **8.5e-16** — one shape number fixed to about 1e-15, like F2's counterterm size (`TESTS:2380`).
- **On 𝒞_sub (reading, conditional).**
  - If Lemma F holds there (OPEN, §3.4), then n_t = N_s − n_max + 1 = 7 under the same definition. Per-species coefficients are the symmetry-allowed ones.
  - R16-2's 3 needs same-charge species to share a coefficient. That is a structural choice, not a symmetry (`C5_R16-2_report.md:293-295`).
- **With charged scalars** (not SM content in this setting). F_0 ≠ 0 on every sample, so each scalar charge class adds conditions under the same definition (suggested).

### 3.7 (d) Literal-corner accounting. Reading and suggested; partly checked

- **Valleys (reading).** The literal edge (W = 0) has 8 light valleys at mass m: Γ, 3 × X (π,0,0), 3 × M (π,π,0), and R (π,π,π).
  - Γ and R have cubic site symmetry, so their speeds are isotropic: 1 coefficient each.
  - X and M have tetragonal symmetry: 2 each.
  - So each literal Dirac field carries 6 independent one-loop valley–direction speeds. By Lemma Q's argument, which does not depend on the valley, each is q_i²·F_{v,dir}(θ).
- **Count (suggested).** On the literal edge, the zero-curve route needs F_{v,dir} = 0 for all 6, each generically at a different G. That is up to 6 shape equations, plus 1 photon-side condition, unless some valley speeds coincide by structure. With symmetry-allowed per-valley counterterms instead: (6N_s − n_max^v) + 1. None of the corner speeds was computed.
- **Checked.** Only the Γ valley: the literal (2, 3) edge has its own zero at G\* = 2.893 (`r1610_zero2.out:9-10`), with smooth m² dependence (`r1610_litm.out:1-4`).
- **Reading.** The literal edge is EXCLUDED by the Z width (`TESTS:3840`), so this accounting only matters if that exclusion is revisited.

### 3.8 The count, compared with R16-2 and R13-8 (reading)

- R16-2's conditional 7/3 (`vR16-2:13`) rests on Lemma F. On the registered class Lemma F is **false** for Dirac. A photon-shape equation, in a photon that is superluminal at the lattice scale, nulls F_½(0⁺) for every charge at once. Then n_t = 2 for SM Dirac content.
- R13-8's N_s matter rows (`vR13-8:15-18`) cost 2, not 9, in 𝒞 at one loop.
- On 𝒞_sub the question is OPEN, with 7 conditional on Lemma F there.

## 4. Against the FIXED readings (`TESTS:5472-5475`)

**Worker reading. Same family, unrefereed.**

- **Dirac (s = ½): REFUTED-ZERO, checked.**
  - The law: D1(1.4, 1/√3) with the photon R85(1.0, 2.0, G\* = 3.1264).
  - It is in the class exactly as registered: S ≤ q, nondecreasing photon, a D1 member, and a deformation of R8-5's photon. Membership is proved (§3.3).
  - F_½(0⁺) = 0 is checked at N = 48/64/96/128, under split-radius, h, m and λ variations, and by the refereed runner directly.
  - **Scope flag for the referee.** The photon is superluminal at the lattice scale (v_max 7.35). If "admissible deformations" (`TESTS:5462`) is read to exclude superluminal photons, this law leaves the class. On 𝒞_sub the reading is then **OPEN**: no zero found, F_½ ≤ −3.8 sampled, tadpole ≤ −2.02 proved, remainder unproved.
- **Scalar (s = 0): OPEN.** No zero was found. F_0(0⁺) < −1/3 on every resolved sample. F_0 = −1/3 + Λ_0 is proved; Λ_0 ≤ 0 is unproved.
- **COUNTED: not met.**
  - For Dirac it is refuted on 𝒞.
  - For scalars the nonvanishing is not proved.
  - n_t (Dirac SM content, 𝒞) = 2 (§3.6). Sufficiency is checked; the lower bound is proved given Lemma Q and the checked Σ ≠ 0 on D1.
- **(b) λ → 0: closed (proved, Theorem L).** The limit exists jointly in (m, λ), with no log, and F_s(0⁺) = K_s + Λ_s. It is uniform on subclasses with fixed box and band bounds.
- **Expectation** (`TESTS:5476`) **was wrong in both directions.**
  - Dirac is not OPEN but REFUTED-ZERO on 𝒞, because K_½ = +2/3 > 0 is the stiff-photon limit.
  - Scalars are not COUNTED, but OPEN with strong evidence, because K_0 = −1/3 < 0 is approached only from below.

## 5. Prices (named, not adopted)

- No axiom text is touched. Edge and photon shapes and counterterms are downstream dynamics (`AX:114-130`). Physical sizes use a = ℓ_P, the scale-reference primitive (`AX:189-190`).
- **P-r16-10a (new).** One Dirac shape tuning for all charges. A photon symbol that is superluminal at the lattice scale (v_max ≈ 7.35, d(π) ≈ 6.25), with its stiffness fixed to about 8.5e-16. One further photon-side condition. Total 2 for SM Dirac content.
  - This trades R14-1's subluminal programme (S17 rule) for the photon sector against 5 tunings (7 → 2).
  - Matter stays subluminal.
- **P73 (refined again).** On 𝒞 the light-mass e–γ price is 2 for all Dirac charge classes together. On 𝒞_sub it stays R16-2's conditional 7 (or 3 with shared class terms) until Lemma F is settled there.
- **Not a price.** The λ → 0 limit costs nothing (Theorem L).

## 6. Strong-word check

- **"Proved":**
  - Theorem L: the identity from box-exact Feynman rules; O(4) invariance of the 4-ball term on the mass shell; dominated convergence on IR-free regions.
  - K_0 = −1/3 (closed form).
  - Nondecreasing R85(G ≥ π/2) (elementary).
  - Lemma T′_sub (R16-2's T′ plus d ≤ q).
  - The n_t ≥ 2 argument, given the checked inputs (i)–(ii).
  - All are unrefereed.
- **"Checked":** K_½ = 2/3; the Dirac zero and its curve; every F value, with N, m, λ, r₀, r₁ and h in the `.out` files.
- **"Universal":** K_s does not depend on law, m, λ or χ (proved for the continuum ball; checked for 4 (m, λ) pairs).
- **"No log":** proved under Theorem L's hypotheses (box photon and box matter). Suggested for box-free photons.
- **"Superluminal photon":** whole-zone v_max = max d′ = 7.353 (checked on a 2e5-point grid).
- **Not claimed:**
  - any zero in 𝒞_sub;
  - any proof that F_0 < 0;
  - the corner-valley speeds;
  - two loops, non-Peierls vertices;
  - λ = 0 analyticity in m beyond Theorem L's continuity;
  - uniformity on all of 𝒞.

## 7. For the referee

1. **Theorem L, step 2.** That the 4-ball term contributes exactly 0 to dΠ(iE_p, p)/dp² for every m, including λ = 0 where P² = −m² is at threshold. Only on-shell values of an O(4)-invariant Π_ball(P²) enter. Also the dominated-convergence bound on {|q| < r ≤ |Q|}.
2. **K_0 = −1/3:** the expansion −3P²/Q⁴ + 4(P·Q)²/Q⁶, the angular integral J = −π/24, and the units F = 8π²(c² − 1). Also whether K_½ = −2K_0 follows in closed form.
3. **The zero law.** Class membership (S ≤ q for D1; nondecreasing d for G ≥ π/2). The sign change at G\* ± 0.05 at three N. The direct R13-7 runner's convergence toward the split value.
4. **The scope question.** Does "nondecreasing photon symbol … plus admissible deformations" include a lattice-scale superluminal photon? If not, the Dirac reading is OPEN (§3.4).
5. **The tuning definition in §3.6**, and whether the n_t ≥ 2 argument needs Σ ≢ 0 on open sets of matter edges, which is not proved.

## 8. Files (all in `S/`)

- **Core.**
  - `r1610_core.py`: point-wise scalar/Dirac integrands, re-implemented from `r162_scalar.py` and `r137_onshell.py`.
  - `r1610_laws.py`: matter and photon families.
  - `r1610_eval.py`: the Theorem L split evaluator.
- **Validation.**
  - `r1610_validate.py` → `r1610_validate_exact.out`, `r1610_validate_split.out`;
  - `r1610_K.py` → `r1610_K.out`.
- **Scans.**
  - `r1610_scan.py` → `r1610_scan_N48.out`;
  - `r1610_search.py` → `r1610_search_dirac_sub.out`, `r1610_search_scalar_sub.out`, `r1610_search_scalar_stiff.out`. These are N = 32 and indicative only; see §3.5.
  - `r1610_scalar_target.py` → `r1610_scalar_target.out` (last 40 lines kept);
  - `r1610_recheck.py` → `r1610_recheck.out`.
- **The zero.**
  - `r1610_zero.py` → `r1610_zero_bisect.out`, `r1610_zero_checks.out`;
  - `r1610_zero2.py` → `r1610_zero2.out`;
  - `r1610_direct.py` → `r1610_direct.out` (the refereed R13-7 runner, unmodified, on the zero law);
  - `r1610_litm.py` → `r1610_litm.out`.
- **Copies:** `arch/{R13-7,R16-1,R16-2}/`, unmodified copies of the archived runners. Only R16-2's files are imported.
- **Note.** The `Gstiff` photon in `r1610_laws.py` is defined but unused.
