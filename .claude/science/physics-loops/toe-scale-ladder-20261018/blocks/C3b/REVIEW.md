# C3b independent review

**Reviewer:** independent mathematical review by a Claude subagent, the same model as the author; not the author session. Date: 2026-10-19.
**Object:** `blocks/C3b/NOTE.md` (author draft, commit 906cbc171), its scripts and logs. C3 `NOTE.md`/`REVIEW.md` were read for context.
**Method:** I re-derived every load-bearing step by hand (below). I also wrote separate code in `review_scripts/`, which imports nothing from `../scripts`. Where possible it uses different methods: exact rational enumeration, forward event simulation, and Dijkstra first-passage.
**Evidence:** `review_scripts/run_review.sh` → `review_scripts/logs/review_all.log`, ending **`TOTAL: PASS=43 FAIL=0`**. The per-script logs are `logs/r1.log` … `logs/r4.log`. The full run takes about 1 min, niced, on one core.
I did not re-run the author's suite. Its log `logs/run_all.log` ends `TOTAL: PASS=50 FAIL=2`, and the per-script outputs match it.

## Overall verdict

The mathematics of Witness X and Theorems K, M, H and J is **correct**. I found no blocking error.

There are four non-blocking scope or wording findings (F1–F4) and some editorial mismatches (F5). The two declared FAILs are reported honestly. The "not LRO" conclusion for H < 1 is justified by the proof, as the note says. The word "diverging" needs one qualifier (F6).

| Claim | Verdict | Severity |
|---|---|---|
| (1) Witness X: ergodic, O_h-covariant, non-mixing, `Cov = ±1/4` | correct | – |
| Lemma 0 / Lemma 1 | correct | – |
| (2) Theorem K1 | correct | – |
| K2 | correct, with a premise fix (F4) | non-blocking |
| K3 (d = 1, Poincaré recurrence) | correct as stated (stationary `T`); scope fix (F1) | non-blocking |
| (3) Theorem M | correct | – |
| (4) Theorem H-a, H-b, sufficient conditions (i) and (ii) | correct | – |
| Corollary H-G, "including all power-law covariances" | **too broad as worded**; correct with fix (F2) | non-blocking |
| H-G fractional, "all H < 1" | correct in d = 2; the d ≠ 2 formula needs a fix (F3) | non-blocking |
| H4 (maximal correlation) | correct as CONDITIONAL | – |
| Candidate (c) with noise `s > 0` | correct (needs bounded offsets `V_c`, as in s4 with `A = 0`) | – |
| (5) Theorem J1–J3 | correct; the "no SSB" step needs its own short argument (F4) | non-blocking |
| Corollary J-KJMA tail and the `ε^{−1/(d+1)}` scale | correct, as an upper bound | – |
| KJMA numerics, exponent −0.326 | reproduced independently | – |
| (6) FAIL reporting / "diverging crossover, not LRO" | honest; justified by proof; one wording fix (F6) | non-blocking |

## Load-bearing steps: derivations and evidence

### 1. Witness X

The clock is `T = (par(x)+φ) mod 2 + 0.4U'`.

- **Stationary.** Translation by an odd vector swaps the two phases, and `φ` is uniform.
- **Ergodic.** The phase factor is a transitive two-point rotation, which is ergodic. The noise factor is iid (Bernoulli), hence weakly mixing. An ergodic action times a weakly mixing one is ergodic.
- **O_h-covariant.** Every element of O_h fixes the origin and preserves parity.
- **Non-mixing.** `Cov(T_0,T_x) = ±1/4` at every separation.
- **Record.** With noise below 1/2, every early site has only late neighbours and vice versa. So the rule gives `ξ =` the late indicator, `L ≤ 1`, and `Cov = ±1/4`. Under the C3 §1 definition this is covariance-LRO of an ergodic law.

r1 a1–a6 checks this exactly with Fractions on a 6³ torus, for both phases. The author's check s1 a3 only asserts the two fractions; r1 computes them from the record.

### 2. Theorem K

**(K1).** `Anc(A)` is closed under "strictly earlier neighbour". So, given `T`, the law of `ξ|_{Anc(A)}` is the sequential product `∏ r_y(ξ_y | ξ_{earlier nbrs})`. Ties are handled by the strict convention: same-level sites are conditionally independent.

- **Γ-invariance.** The hypothesis `r(γs|γη) = r(s|η)` maps this product onto itself under a global `γ`. Averaging over Γ gives `E[f|T] = 0` pointwise in `T`.
- **Conditional independence.** On `E_T`, `ξ_A` and `ξ_B` are functions of `T` and of the marks on disjoint sets, so they are conditionally independent.
- **Bound.** The bound follows from these two facts.

r1 b0–b5 checks this with exact rationals. The setting is Potts q = 3 with noisy plurality on a 2×3 grid. The clock law is an arbitrary non-exchangeable mixture that includes tie levels. `g` is not symmetric.

- `E[f|T] = 0` for every realisation.
- `E[fg|T] = E[f|T]E[g|T]` holds exactly on disjoint ancestries.
- `|Efg| = 0.103 ≤ 1.25`.
- Negative control: a biased rule gives `Ef = 0.147`.

**(K2).**
- Overlap forces `max L ≥ (|x| − diam A)/2`, because `Anc(y) ⊂ B(y,L(y))` and the triangle inequality gives `|a − a' − x| ≥ |x| − diam A`.
- `E S_n² → 0` follows from K1. The mean ergodic theorem gives `S_n → E[f|𝓘]`, so `E_{μ_ω} f = 0` for a.e. component.
- Applying this to `h − avg_γ h∘γ` for every local `h` gives `Γ`-invariance of `μ_ω`. So "no SSB" follows.
- Write the bound with `|Cov|`.

**(K3).**
- In d = 1 with nearest neighbours, decreasing paths are monotone runs.
- On an infinite run, a rational `I ∋ T_0` with `|I| < T_0 − T_1` has `inf I > T_1 > T_n` for all `n ≥ 2`. This contradicts Poincaré recurrence on `{T_0 ∈ I}`.
- Use the invertible shift for the left direction. The countable union over `I` is null. The proof is correct.
- r1 c2–c3 runs stationary non-mixing examples, AR(1) with ρ = 0.999 and a random-phase sawtooth. Both have finite runs.

### 3. Theorem M

Under the stated premise, the record is a translation-equivariant factor of (orientation field, marks).

- (i) An ergodic action times a Bernoulli action is ergodic.
- (ii) A mixing action times a mixing action is mixing, and factors inherit both properties.

The orientation field is a factor of the increments, so the "increments" reading is fine. The theorem is correct.

### 4. Theorem H

**(H-a).** Off the ψ event, a decreasing SAW of length `n` has all its values in `[T_0−M, T_0)`. With conditional density `≤ K^n`, a fixed SAW has probability `≤ K^n M^n/n!`. Take the union over `c_n` SAWs. Correct.

**(H-b).** `c_n(Kηn)^n/n! ≤ (D/(D−1))(e(D−1)Kη)^n`. Verified on a grid in r2 c1.

**(i).** Conditioning on `(T_1, Y_0)` and averaging gives the density bound. Correct.

r2 b1 checks H-a against Monte Carlo on Z², with a **deterministic non-stationary tilt** `T_1 = β(x_1+x_2)`, for `n ≤ 10` and 24 values of `M`. It uses exact SAW counts, with `ψ` computed by quadrature. The bound holds, but it is loose (about 0.8–1.0 against P = 0.0025–0.9).

**(ii).**
- The determinant equals a product of successive conditional variances. Each is `≥ Var(T_y | all others) = v`, by stationarity.
- Kolmogorov's formula is checked against the AR(1) closed form `s²(1−ρ²)/(1+ρ²)` to 1e-10, by dense inversion and by spectral mean (r2 a1).
- The determinant bound holds for 300 random `S` (r2 a2).

**H-G Gaussian tail.** `ψ_n(M) ≤ (|B_n|+1)e^{−M²/8σ²}` is correct.

**Fractional clocks in d = 2.**
- `f_H − 8^{−(1+H)} ≥ 0` holds (r2 d1). So `T` can be realised as an intrinsic field with that residual spectral weight plus iid `N(0, 8^{−(1+H)})`. Only increments matter, by Lemma 0, so (i) applies.
- The increment variance is `A_H r^{2H} + O(1)`. The s3b closed form for `A_H` matches my direct Bessel quadrature to 1e-3 (r2 d2).
- So `ψ_n(ηn) → 0` for every `H < 1`. The claim holds in d = 2.

**H4.** The maximal correlation of (clock window, iid marks) pairs equals that of the clock windows (Csáki–Fischer). The truncation error is `2(P(E_A)+P(E_B))`. Correct as a CONDITIONAL claim.

**Candidate (c) with noise.** The oscillation over `B(0,n)` is at most `√3 ×` the largest cell diameter, plus the offset range, plus the noise. That is sublinear, so the claim holds. This needs the offsets `V_c` bounded or light-tailed; s4 uses `A = 0`.

### 5. Theorem J

- **Dependency.** A decision at `(x,s)` depends on the neighbourhood states on `[0,s)`, which are fixed recursively by neighbour points at earlier times. The site's own earlier points depend only on neighbour points before them, so they are covered by chains from `(x,s)`.
- **Revisits and loop erasure.** Chains that revisit `x` loop-erase to chains starting at another point of `x` with `t ≤ τ_0`. The definition allows such a start point.
- **Chain count.** Mecke gives `λ^{n+1}t^{n+1}/(n+1)!` per SAW.
- **Locality.** On `{τ_0 ≤ t, no chain reaches distance n}`, which is a `B(0,n)`-measurable event, `ξ_0` is fixed by the data in `B(0,n)`. That gives J2.
- **Choice of t.** With `t = n/(2e(D−1)λmax)`, the second term is `≤ (D/(D−1))2^{−n}`.
- **J3.** The earliest accepted point in the finite reach would have an empty history. Correct.

r3 is a forward event simulation with history-, age-, content- and time-dependent rates, λmin = 0 and seeds.

- Resampling all data beyond `ρ+1`, fresh and adversarial (sure early seeds), changed `(τ_0, ξ_0)` in **0 of 474** cases.
- Power control: 2 of 198 cases changed. That is weak but nonzero.
- The J2 tail bound holds for n = 2..10.
- J3 holds.

**J-KJMA.**
- The first term uses "sure-ε" points, accepted at any blank site. "Isolated" is not needed.
- The second term: geodesic growth is dominated by Gamma(r, a) through the strong Markov property. The Chernoff bound at twice the mean gives `e^{−0.307r}`.
- The resulting `P(R ≥ n+1) ≤ C(2^{−n}+e^{−c'n}) + exp(−c''ε n^{d+1})` puts the covariance below `C(0)/e` for `r ≥ Cε^{−1/(d+1)}`, with constants depending on `a` and `λmax`. So `ξ(1/e) ≤ Cε^{−1/(d+1)}` is correct as an upper bound.

r4 reproduces the KJMA numerics with an independent Dijkstra site-first-passage implementation:
- `ξ = 4.12, 8.61, 18.49` against the author's 4.15, 8.55, 18.85;
- slope **−0.326**;
- the tail bound holds on a t-grid. That check is weak: no samples had `τ > 40`.

## Findings

**F1 (non-blocking): K3 scope.**
- K3 needs `T` itself stationary. Lemma 0's "increments" reading does **not** extend to it.
- Counterexample: the level clock `T_x = x` on Z has stationary increments, `L(0) = ∞`, and under the copy rule two solutions (all +1 and all −1). See r1 c1.
- K3 also uses nearest neighbours: with range h > 1, paths are not monotone runs.
- **Fix:** in §0 item 2 and K3, write "stationary (not merely gradient-stationary) clock, nearest-neighbour rule".

**F2 (non-blocking, genuine overstatement): "including all power-law covariances" (§0 item 4, H-G).**
- Counterexample: `T_x = W_x − W_{x+e1}`, with `W` a power-law field. This is stationary Gaussian with a power-law covariance (|C| ~ r^{−3} along e2). Its spectral density vanishes on `k_1 = 0`, so `∫f^{−1} = ∞`, the interpolation variance is 0, and (H1) is not established. See r2 e1–e2.
- **Fix:** write "power-law covariances whose spectral density is bounded below (e.g. any with a white-noise component)". The s3 families, `f = s2 + lap^{(α−2)/2}`, qualify.

**F3 (non-blocking): fractional formula and dimension.**
- `f = lap^{−(1+H)}` gives `Var(T_0−T_y) ~ |y|^{2H}` only in d = 2. In general d, use `lap^{−(d/2+H)}`; the floor becomes `(4d)^{−(d/2+H)}`.
- State the (i)-decomposition explicitly: intrinsic part with residual spectral weight, plus white noise. `T` is defined only modulo a constant.

**F4 (non-blocking): premises in K2 and J.**
- K2 assumes `T` stationary, but H-G applies it to fractional clocks. The proof only uses stationarity of the orientation field, so state that premise instead.
- J's "no SSB (Theorems M and K)" cites K, which is proved for the clock model only. In J, argue directly: assume Γ-equivariant `λ` and content kernels and translation-covariant rates. Then the FFIID record law is unique, mixing and Γ-invariant.

**F5 (editorial).**
- §7(a): the stated `χ_L` slopes "−0.04 ± 0.15 / −0.04 ± 0.26" do not match `logs/s2_nucleation_growth.out`, which gives **−0.011 ± 0.114 / −0.080 ± 0.161**.
- §6 "ξ/ℓ ≈ 0.3": the logged ratios drift. They are 0.49 at ℓ = 4, 0.35–0.38 at ℓ = 8 and 0.31 at ℓ = 12, and they mix runs with δ = 0 and δ = 0.02. Say "0.3–0.5, decreasing".
- s1 a3 asserts the covariance and does not compute it; my r1 a3 computes it.

**F6 (non-blocking): the two FAILs and the "diverging crossover" reading.**
- The FAILs are honest. They are kept in the total, the criteria were declared beforehand, and the note explicitly says the numerics cannot separate H = 0.95 from slow ordering.
- The no-LRO / no-SSB statement for every H < 1 rests correctly on H-G + K + M.
- New supporting evidence (r2 d3–d4): on the author's tori, the clock law itself is not converged at H = 0.95. The scale-free shape `Var(32)/Var(1)` is still 22% below its L = 2048 value at L = 512, against 4.5% for H = 0.5. So the box dependence of `⟨L⟩` is expected.
- Wording: what is *proved* to diverge as H → 1 is the guaranteed scale of the bound (`n*`). The true ancestry scale is only observed to grow. **Fix:** write "the bound's guaranteed scale diverges as exp(O(1/(1−H))); simulated `⟨L⟩` grows; a divergence of the true crossover scale is not proved".

## Process disclosures

- **r2 d4.** The first version of the criterion compared absolute variances. It failed, and it was ill-posed: a global rescaling of `T` does not change the record. I replaced it with the scale-free shape ratio. In r2, I also replaced the planned exponent-fit check with a check of the `A_H` constant, because midpoint/torus quadrature is IR-biased for H near 1.
- **r3.** The first parameters (p = 0.04) gave too few usable samples: only 22, with 0 changes. I retuned to p = 0.3 before the final run.
- The container restarted once mid-review. All scripts were re-run from scratch for the final log.

## Files

- `review_scripts/rv_common.py`
- `review_scripts/r1_witness_and_K_exact.py`
- `review_scripts/r2_theorem_H.py`
- `review_scripts/r3_theorem_J_forward.py`
- `review_scripts/r4_kjma_dijkstra.py`
- `review_scripts/run_review.sh` → `review_scripts/logs/review_all.log` (`TOTAL: PASS=43 FAIL=0`)

**Final verdict: READY after the text fixes F1–F6.** None of them changes a proof.

## Correction confirmation

I re-read the complete corrected `NOTE.md` (commit 54d7c144e), §0–§10, and diffed it against the reviewed commit 906cbc171. The proofs of Witness X and of Theorems K1, M, H-a/H-b, J1–J3 are unchanged. I did not re-run either suite, and my evidence is unchanged (`review_scripts/logs/review_all.log`, `TOTAL: PASS=43 FAIL=0`).

| Finding | Resolved? |
|---|---|
| F1 | **Yes.** K3 and §0 item 2 now require `T` itself stationary and a nearest-neighbour rule. The level-clock counterexample and the range-`h` caveat are stated. |
| F2 | **Yes.** The claim is restricted to spectral density bounded below, and the `W − W(·+e1)` counterexample is recorded. |
| F3 | **Yes.** The exponent is now `lap^{−(d/2+H)}`, and that is correct: `∫(1−cos k·r)|k|^{−d−2H}d^dk ∝ r^{2H}`. The floor `(4d)^{−(d/2+H)}` follows from `lap ≤ 4d`. The intrinsic-plus-white-noise decomposition and the remark that `T` is defined only modulo a constant are both correct. |
| F4 | **Yes.** K2 is now stated with a stationary orientation field, which is all its proof uses. The new J argument for no SSB is **correct**; see the check below. |
| F5 | **Yes.** The slopes now match `logs/s2_nucleation_growth.out`, and ξ/ℓ is stated as "0.3–0.5, decreasing", with the δ pooling noted. |
| F6 | **Yes.** Only the bound's guaranteed scale is said to diverge. The clock is noted as unconverged at H = 0.95. `ε^{−1/(d+1)}` is labelled an upper bound, and N1 item 3 is aligned with this. |

**Check of the new J no-SSB argument.**
- Let `ζ` be the process with selector `Φ`, and define the twisted selector `Φ'(H,u) := γ^{−1}Φ(γH,u)`.
- `Φ'` has law `r(·|H)`, by the assumed equivariance of the content law.
- On the same data, `ζ' := γ^{−1}ζ` satisfies the dynamics with selector `Φ'`:
  - acceptance is unchanged, since `λ(H_ζ) = λ(γH_{ζ'}) = λ(H_{ζ'})`;
  - the contents satisfy `γ^{−1}Φ(H_ζ,U) = Φ'(H_{ζ'},U)`.
- On each finite reach the record law is the time-ordered sequential kernel, which does not depend on the selector. Hence `law(γ^{−1}ζ) = law(ζ)`.
- Together with mixing (translation-covariant rates, FFIID), this gives a unique, mixing, Γ-invariant law, so there is no SSB.
- The conclusion is correct. The note's phrase "apply γ to the iid data" is loose. Γ acts on the menu, not on the marks `U`, so the mechanism is the twisted selector plus selector-independence of the law. Suggested wording: "by the twisted selector `γ^{−1}Φ(γ·,u)` and selector-independence of the law". This is editorial.

**New issues introduced (editorial, non-blocking).**
- **N-a.** H-G, first bullet: "(H1) is not established with finite correlation scale" is garbled. The words "with finite correlation scale" belong to the earlier phrase "smooth fields with finite correlation scale".
- **N-b.** The J wording described in the check above.

**Final verdict: READY.** No mathematical defect remains. N-a and N-b are editorial and can be fixed without re-review.
