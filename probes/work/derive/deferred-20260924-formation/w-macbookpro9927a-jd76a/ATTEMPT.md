# deferred-20260924-formation: attempt 1 (first bounded pass of batch 5)

- **Worker and unit.** Worker `w-macbookpro9927a-jd76a` (claude-opus-5-5), unit `J-derive-deferred-20260924-formation-a1`.
- **Bundle.** `probes/work/deferred-science-20260924/`: `README.md`, `batch-05.json` and `review-unit5-v1.json`.
- **Heads and hashes.**
  - `origin/main` was `60c5f194d940a7bbaf1cdd545296e31d74a02f1a` when read. The bundle's landing snapshot was `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`.
  - PR8178's frozen head is `e6ffae5b460b9ec0fd0d99c99f9784232bd225bd`. All 18 deferred sources verify against the manifest SHA256 (`Q1`).
  - PR8178 landed in `5efa36e7c357`. Its canonical note has SHA256 `407e07d95da7…`, and the copy on `origin/main` is byte-identical (`Q2`).
- **This pass does not exhaust batch 5.** The remaining ranked groups are in `RECOVERY_STATUS.json`.

## 0. Selection: what main already separates and what it leaves open

The unit asks to *separate the corrected linear transient proxy from the still-unproved nonlinear memory/scaling law* of PR8178. The landed note (block 34) already separates them at the level of wording. Quoted verbatim (`Q3`):

- *"This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel."*
- *"Thus the chosen noise variance is the aligned conditional variance, but the exact Cartesian mean gain is A(3beta), not one. A direction-normalized or strong-coupling approximation needs an additional argument; none is supplied here."*
- `next_trace_action: "Establish a controlled connection to the nonlinear kernel before importing linear conclusions"`.
- Of the six-row historical table: *"The listed samples neither prove size independence nor a limiting coefficient, an exact phase or a universal memory law."*

The frozen sources state the nonlinear law that the review demoted (`Q5`). From `RESULTS_block34.md`:

- the direction diffuses "`1/|m|²` faster";
- "tracking `1/|m|²` of the stationary magnetization within `3–8 %`";
- "the first quantitative target for "spin-wave theory as a theorem"".

From `CHECKER_block34_findings.md`: "the nonlinear excess is a property of the coupling, not of the size (`L = 16` and `32` agree within errors), and tracks `1/|m|²`".

**What main leaves open, and the single residual worked here.** Main does not say how the comparator is connected to the nonlinear law, and does not say whether the `1/|m|²` factor is that connection. The residual worked here is the strong-coupling relation between:

- the nonlinear law's torus memory rate `λ₁`, and
- the comparator's rate `1/τ_L`,

including whether `1/|m|²` gives that relation at first order.

**Prior attempts and why they do not cover it.**

| problem | what it settles | overlap with this residual |
|---|---|---|
| `corrigendum-PR8178` (a1 `j9532`, a2 `j888a`, referees `j3bc2`, `jb1e0`) | the multiplier convention `φ` vs `φ_c` | none; main's T1.1 uses the positive-exponent convention, so already landed |
| `corrigendum-PR8180` (my own a1, issue #8846) | block 35's kernel | none (a different statement), not reopened |
| `formation-response-kernel` a1–a6 and six referees | the linear comparator's response `R = 1/(1 − φe^{iw})` | none; linear model only |
| `plane-memory-loss` a1–a4 | the infinite-plane `m_t → 0`; mean-field; the uniform-twist cost | none; not the finite-torus rate |
| `plane-memory-loss-2` a1–a4 and referees | the space-time twist cost is Θ(1); `β < 1` uniqueness | a2's transverse sensitivity `A(|V|)/|V|` is the Cartesian derivative already on main (U5-R1); no memory rate |

No active claim covers the finite-torus nonlinear memory rate or the `1/|m|²` factor. The review findings kept intact are:

- **U5-R1:** the gain-one recurrence is not the Cartesian mean derivative.
- **U5-R3:** no size independence, no limiting coefficient and no universal law are restored.
- **U5-R8:** the historical data stay historical.

Nothing below is imported from an unlanded note.

## 1. The statement attempted

**Setting (main's note, restated).**

- The plane is `Λ = Z_L²` and each record is a unit vector `s_x(t) ∈ S²`.
- The local field is `S_x = s_x + s_{x−e₁} + s_{x−e₂}`. Given level `t`, the records of level `t+1` are independent with density `∝ exp(β s·S_x)` on the unit sphere.
- `A(κ) = coth κ − 1/κ`, `σ² = A(3β)/(3β)`, `τ_L = L²/σ²`, and `u_k = |φ(k)|²` with `φ = (1 + e^{ik₁} + e^{ik₂})/3`.

**Definitions introduced here.**

- `M(t) = L⁻² Σ_x s_x(t)`, `n = M/|M|`, and `x₁ = 1 − E_st[n(t+1)·n(t)]` (the one-level direction decorrelation).
- `λ₁ = −lim_ℓ ℓ⁻¹ log E_st[n(t+ℓ)·n(t)]` (the torus memory rate).
- `S*_L = L⁻² Σ_{k≠0} 1/(1 − u_k)`. This equals `V_L/σ²` in the note's notation.
- `st` denotes the stationary chain. Its direction law is rotation invariant.

**Claims.**

- **(I) Exact identities, for every `β > 0` and `L ≥ 1`.** Steps S1–S8 below.
- **(II) Single-site control, `L = 1`.** Here the three predecessors coincide.
  - `λ₁τ₁ = −3β log A(3β)/A(3β) > 1 = 1/|M|²` for every `β > 0`.
  - As `β → ∞`: `λ₁τ₁ = 1 + (3/2)σ² + O(σ⁴)`.
- **(III) First-order strong-coupling law.** Fixed `L`, `β → ∞`, under premises A1–A2 of §2:
  ```
  x₁ τ_L    = 1 + σ² (S*_L + 2 − 1/L²)      + O(σ⁴)
  λ₁ τ_L    = 1 + σ² (S*_L + 2 − 1/(2L²))   + O(σ⁴)
  1/E|M|²   = 1 + σ² · 2S*_L                + O(σ⁴)
  ```
  Hence `λ₁ τ_L · E|M|² = 1 + σ² (2 − 1/(2L²) − S*_L) + O(σ⁴)`.
  - The first-order gap to the `1/|m|²` factor is positive for `L = 2,…,7`: `1.031, 0.722, 0.492, 0.311, 0.162, 0.035`. It is exact rational at `L = 2, 3, 4, 6`.
  - It is negative at `L = 8, 9, 10, 16, 32, 64`: `−0.074, −0.171, −0.258, −0.646, −1.219, −1.792`. These values are numerical.
  - As `L → ∞`, `S*_L = 2c₀ log L + 0.3528… + o(1)` (the note's offsets, `c₀ = 3√3/(4π)`). So the excess of `λ₁τ_L` over one has log coefficient `2c₀σ²`, while `1/|m|²` has `4c₀σ²`.
- **(IV) Seeded Monte Carlo (numerical, not exact) agrees with (III) and discriminates it from `1/|m|²`.** Results are in §4.

**Minimal premises.** Only the note's kernel and the definitions above. There is no bridge, axiom or physical reading. The rate `λ₁` is a property of the supplied nonlinear chain.

**Success witness.** A theorem would need a rigorous version of A1–A2. What is delivered is:

- the exact identities and the `L = 1` inequality;
- the first-order law as a derivation that is explicit up to A1–A2;
- Monte Carlo agreement, with the `1/|m|²` alternative rejected at `≥ 5` SE at `L = 2, 3, 4, 16`.

## 2. Steps

Notation used in the steps:

- `κ_x = β|S_x|` and `Ŝ_x = S_x/|S_x|`.
- `b(κ) = A(κ)/κ` and `ℓ(κ) = 1 − 2b(κ) − A(κ)²`.
- `c_x = Ŝ_x·n`. For a vector `v`, `v^⊥` is its projection off `n`.
- `π̃_x = s_x^⊥` is the relative field. `Σ_x π̃_x = 0` exactly, because `M ∥ n`.

**S1 (PROVED; CHECKED V1–V3, P2).** For the record drawn with local field `S`, let `w = s·Ŝ`. Its density is `∝ e^{κw}` on `[−1, 1]`, with uniform azimuth. Then:

- `E w = A`, `E w² = 1 − 2A/κ` and `E w³ = coth κ − 3/κ + 6A/κ²`.
- `E[s|S] = AŜ`.
- `Cov(s|S) = b(I − ŜŜᵀ) + ℓŜŜᵀ`, because the tangent part has isotropic covariance `(E(1 − w²)/2) I₂ = b I₂`.

The moment recursion is `m_j = [e^κ − (−1)^j e^{−κ}]/(κZ) − (j/κ)m_{j−1}`, with `Z = 2 sinh κ/κ`.

**S2 (PROVED; CHECKED D1). Drift identity.** On the periodic plane `Σ_x S_x = 3Σ_x s_x`, and `AŜ = S/3 + (A − |S|/3)Ŝ`. Hence
```
E[M(t+1) | level t] = M(t) + L⁻² Σ_x g_x Ŝ_x ,   g_x = A(κ_x) − |S_x|/3 .
```
The gain-one comparator is the case `g ≡ 0`. For the sphere kernel `g` is never identically zero: at alignment `g = A(3β) − 1 < 0`.

**S3 (PROVED; CHECKED D3). The direction's drift.** Since `Σ_x S_x^⊥ = 3L² M^⊥ = 0`,
```
(Σ_x g_x Ŝ_x)^⊥ = Σ_x (h_x − h̄) S_x^⊥   for any constant h̄,   h_x = g_x/|S_x| .
```
So the direction's drift comes only from site-to-site differences of the field magnitude `|S_x|`. It vanishes whenever all `|S_x|` are equal, and is cubic in the relative field near alignment.

**S4 (PROVED; CHECKED D2).** For unit vectors, `|S_x|² = 9 − Σ_{i<j} |s_i − s_j|²` over the three predecessors. Hence `|S_x| = 3 − q_x/2 + O(π̃⁴)`, where `q_x = Σ_j |π̃_{x−j} − (Pπ̃)_x|²`.

**S5 (PROVED; CHECKED P1). Projected noise.** Let `η_x = s_x(t+1) − E[s_x(t+1)|t]`. Then
```
E[|η_x^⊥|² | t] = b_x(1 + c_x²) + ℓ_x(1 − c_x²) .
```
A record whose local field is tilted from `n` puts part of its noise along `n`, where the noise changes `|M|` and not the direction.

**S6 (PROVED; CHECKED V4, V5). Third moment.**
```
E[(1 − w²)(w − A)] = 2/κ − 6A/κ² − 2A²/κ = −2/κ² + 4/κ³ + O(e^{−2κ}) .
```

**S7 (PROVED). Stationarity.** Write `M(t+1) = (m + a) n + b` with `m = |M(t)|` and `b ⊥ n`. Then `E|M(t+1)|² = E|M(t)|²` gives exactly `2E[ma] + E[a²] + E|b|² = 0`.

**S8 (PROVED). Chord identity.** `n·n' = (m + a)/√((m + a)² + |b|²)`. So `|n' − n|² = X − (3/4)X² + O(X³)` with `X = |b|²/(m + a)²`.

**S9 (PROVED; CHECKED C1, C2). Gain-one comparator with the zero mode removed.** Per component, the stationary moments are:

- `E π̃_x² = σ² S*_L`;
- `E (Pπ̃)_x² = σ²(S*_L − 1 + L⁻²)`;
- `E q_x = 6σ²(1 − L⁻²)`, summing both components.

The exact values are `S*_2 = 27/32`, `S*_3 = 11/9`, `S*_4 = 189/128` and `S*_6 = 2627/1440`. These come from the Fourier sum and are cross-checked by an exact rational solve of the circulant Lyapunov equation `c = (1/9)Σ_{j,j'} c(·−j+j') + (δ − L⁻²)`, with `Σc = 0`.

**A1 (ASSUMED). Small-noise stationary statistics.** At fixed `L` as `β → ∞`, the stationary relative field has the moments of S9 to leading order. Its fourth moments are `O(σ⁴)`, and site-averaged quantities fluctuate at relative order `O(σ²)`. This is the standard small-noise behaviour, and it is not proved here.

**S10 (DERIVED from S1–S9 and A1; CHECKED F1).**

- **Local noise.** By S4, `κ_x = 3β − βq_x/2`. So `b_x = σ²(1 + q_x/6) + O(σ⁶)` (`V6`).
- **Transverse noise.** With S5, `c_x² = 1 − |Ŝ_x^⊥|²` and S9:
  `E|b|² = (2σ²/L²)[1 − σ²S*_L + 2σ²(1 − L⁻²)] + O(σ⁶)`.
- **Magnitude.** `E m = 1 − σ²S*_L + O(σ⁴)`.
- **Longitudinal drift.** S7 gives `E a = −σ²/L² (1 + O(σ²))`.
- **Third moment.** From S6, `E[|b|²a_noise] = L⁻⁴·(−2σ⁴)`.
- **Fourth moment.** `E|b|⁴ = 2(E|b|²)²`, the Gaussian sum identity at leading order.

Inserting these into S8,
```
x₁ = E|b|²/(2m²) − E[|b|² a]/m³ − (3/8)E|b|⁴/m⁴ = (σ²/L²)[1 + σ²(S*_L + 2 − 1/L²)] + O(σ⁶) .
```
The first-order terms read as follows:

- `+2S*_L` from `1/m²`;
- `−S*_L + (1 − L⁻²)` from the tilt projection in S5;
- `+(1 − L⁻²)` from the weaker local fields;
- `+(4 − 3)/L²` from the longitudinal drift, the third moment and the chord.

**A2 (ASSUMED). Increment correlations are higher order.**
```
Σ_{k≥1} E[Δn(t)·Δn(t+k)] = O(σ⁶/L²) × (a constant depending on L).
```
The reason: the noise part of each increment is a martingale difference, and the drift part is cubic in the relative field (S3). A correlation with an earlier zero-mode noise therefore needs one more factor `σ²`. This order count is not a proof.

**S11 (DERIVED from S10 and A2; CHECKED F2).**
```
λ₁ = −log(1 − x₁) + O(σ⁶/L²) ,   i.e.   λ₁τ_L = 1 + σ²(S*_L + 2 − 1/(2L²)) + O(σ⁴) .
```

**S12 (PROVED given A1; CHECKED F3).** `|M| = 1 − (1/2)L⁻²Σ_x|π̃_x|² + O(π̃⁴)`, so `1/E|M|² = 1 + 2σ²S*_L + O(σ⁴)`.

**S13 (PROVED; CHECKED E1–E3). The single-site control `L = 1`.** Here `S = 3s`, `|M| = 1` and `E[s(t+1)·e | s(t)] = A(3β) s(t)·e`. So `E[n(t)·n(0)] = A(3β)^t` and `λ₁ = −log A(3β)`. The inequality `λ₁τ₁ > 1` holds for every `β > 0`:

1. **An exact identity (E1).** For `κ > 0`: `A(κ) − κ/(κ+1) = [2κ² + 2κ − (e^{2κ} − 1)] / [(e^{2κ} − 1)(κ² + κ)]`.
2. **Its sign (E2).** The numerator is negative because `e^{2κ} − 1 − 2κ − 2κ² = Σ_{n≥3}(2κ)ⁿ/n! > 0`.
3. **The chain.** So `A < κ/(κ+1)`. Hence `1 − A > 1/(κ+1) > A/κ`, and `−log A ≥ 1 − A > A/κ`. This is `λ₁τ₁ = −κ log A/A > 1` with `κ = 3β`.

The series `1 + (3/2)σ²` equals (III) at `S*_1 = 0`, `L = 1` (E3).

**S14 (CHECKED F4).** The first-order gap to `1/|m|²` is positive at `L = 2, 3, 4, 6` (exact) and at `L = 7` (numerical). It is negative at `L = 8, 9, 10, 16, 32, 64` (numerical).

## 3. First failing step and exact next obligation

As a theorem, the route stops at **A1**. There is no proof that the stationary law of this non-reversible chain on `(S²)^{L²}` concentrates near the aligned orbit with the comparator's second moments at leading order, and fourth moments `O(σ⁴)`. The one-level law `x₁τ_L` needs only A1. The memory-rate law also needs **A2**.

The exact next obligation, at fixed `L`, uniformly in `β ≥ β₀`:

1. Find a Lyapunov function for the relative field, for example `Σ_x|π̃_x|²` with the P-weighted correction, giving `E_st|π̃_x|⁴ ≤ C_L σ⁴`.
2. Then obtain S9's moments from the stationarity equation of the second moments, with an `O(σ⁴)` remainder.
3. Bound the correlation sum in A2 through the geometric mixing of the relative-configuration process. By S3 the drift is cubic.

A2 has partial numerical support (§4b, c). The coefficients themselves are fixed by S10–S11 and CHECKED; only the premises A1–A2 are open.

## 4. Numerical evidence (seeded; `mc_evidence.py`, output `mc_evidence.out`)

The chains are independent and start from the aligned plane with burn-in. Errors are jackknife over 20 blocks of chains. The estimators are those defined in §1, and `D₁` of the historical script equals `(1 − C(ℓ))/ℓ`.

**(a) The one-level coefficient `(x₁τ_L − 1)/σ²`**, fitted linearly in `σ²`. The `β` values are 20, 40, 80 and 160 at `L = 2`, 20, 40 and 80 at `L = 3, 4`, and 48 and 96 at `L = 16`.

| `L` | intercept (MC) | slope | first order `S*+2−1/L²` | `2S*` | intercept vs `2S*` |
|---|---|---|---|---|---|
| 2 | 2.574 ± 0.027 | 11.0 | 2.594 | 1.688 | 32 SE |
| 3 | 3.044 ± 0.039 | 16.9 | 3.111 | 2.444 | 15 SE |
| 4 | 3.385 ± 0.038 | 18.5 | 3.414 | 2.953 | 11 SE |
| 16 | 4.71 ± 0.19 | (2 points) | 4.640 | 5.289 | 3.1 SE |

In every run `(1/E|M|² − 1)/σ²` approaches `2S*` (S12). For example, at `L = 2` it takes the values `1.771, 1.728, 1.708, 1.698`.

At `L = 16` the direct comparison within the same run is sharper. The one-level rate lies below `1/E|M|²`:

- at `β = 48`: `x₁τ = 1.03342` against `1.03803`, which is 11 SE;
- at `β = 96`: `1.01653` against `1.01868`, which is 7 SE.

**(b) The memory rate at `β = 20`**, from the slope of `−log C(ℓ)` over a window of about 0.3 memory times:

| `L` | `λ₁τ_L` | `−log(1−x₁)τ_L` | `1/E|M|²` | above `1/E|M|²` | first order |
|---|---|---|---|---|---|
| 2 | 1.04754 ± 0.00063 | 1.04725 | 1.02902 | 29 SE | 1.04456 |
| 3 | 1.05484 ± 0.00119 | 1.05562 | 1.04259 | 10 SE | 1.05190 |
| 4 | 1.06255 ± 0.00189 | 1.06106 | 1.05187 | 5.7 SE | 1.05646 |

A2 holds here within 0.8 SE: the memory rate equals `−log(1 − x₁)`.

**(c) `L = 16`, `β = 12`** (a historical row). The quantity `−log C(ℓ)/ℓ · τ_L` takes these values:

| lag | `−log C(ℓ)/ℓ · τ_L` |
|---|---|
| 1 | 1.1510 ± 0.0007 |
| 4 | 1.1479 ± 0.0013 |
| 16 | 1.1447 ± 0.0022 |
| 64 | 1.1445 ± 0.0043 |

Against `1/E|M|² = 1.1702`, the lag-64 rate is 5.9 SE below. The correlation correction is negative (about −0.6%). The author-reported short-lag value is `1.139 ± 0.007`.

**Caveat on A2 at larger `L`.** The historical raw series `supervisor_control_block34_torus_msd.out.txt` at `L = 32`, `β = 12` rises with lag, from `1.165 ± 0.005` (lag 25) to `1.188 ± 0.010` (lag 100) and `1.225 ± 0.026` (lag 400). The curvature bias of that estimator is below 1% at these lags. So at `L = 32` and this coupling, the increment correlations may be positive and of order 5%. That is not the `O(σ⁴)` smallness A2 needs in practice there.

The first-order law is asserted only at fixed `L` as `β → ∞`. Its second-order coefficients grow with `L`: the one-level slopes are 11, 17 and 19 at `L = 2, 3, 4`. The historical rows at `L = 32`, `β ≤ 12` lie outside the range where the first-order law has been tested.

## 5. The historical rows against the law (`H1`; the rows are author-reported and not re-verified)

Every short-lag `D₁` ratio in main's table lies below its `1/|m|²`, by 2–7%. At first order the gap `2 − S*_L − 1/(2L²)` has the same sign at `L = 16, 32` (`−0.646`, `−1.219`). But these rows have `σ²S*_L` between 0.02 and 0.17, well outside the range tested in §4a. Their size relative to the first-order values (`+0.09` at `β = 6`, `L = 16`) is not predicted here. The rising `L = 32` lag series (§4, caveat) shows that the long-lag rate there is not settled.

Nothing in this section is a check of the historical rows. No limiting coefficient is claimed, and the size independence of the excess stays demoted (U5-R3). At first order in `σ²` the excess grows like `σ²S*_L`, that is like `2c₀σ² log L`. So the first-order law has no size-independent excess either.

## 6. What this changes, and what it does not

- **It gives the "controlled connection" that main asks for, as an explicit derivation modulo A1–A2.** The gain-one comparator is the leading strong-coupling term of the nonlinear law's direction memory (`λ₁τ_L → 1`). Modulo A1–A2, the first correction is `σ²(S*_L + 2 − 1/(2L²))`. The Cartesian gain `A(3β)` of U5-R1 never enters the direction's rate: S2–S3 show that the plane average's drift lies along the local fields, apart from a term cubic in the relative field.
- **It separates the historical `1/|m|²` reading from that law.** The factor has the right leading term but not the first-order coefficient: the two differ at every `L ≥ 2` checked, and the difference changes sign between `L = 7` and `L = 8`. Its log L coefficient is twice the law's.
- **It does not change** main's exact comparator theorems T1–T3, anything about the infinite plane (the plane-memory-loss family) or any physical reading.
