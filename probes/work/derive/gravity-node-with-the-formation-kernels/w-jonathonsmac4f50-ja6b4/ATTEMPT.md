# gravity-node-with-the-formation-kernels: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-ja6b4` (claude-opus-5), unit `J-derive-gravity-node-with-the-formation-kernels-a3`.

**Sources.**
- The gravity lane's statements on `main` at `abb98a12`, quoted with file and line in §1.
- The candidate kernels as the task gives them.
- The light-cone 3+1 facts come from the refereed round-1 reports under `probes/work/derive/lightcone-formation/` and `formation-response-kernel/`. The round-1 authors were grok; the referees were claude-opus-5, my model family.
- The backward 2+1 identity comes from my own PR #8180 corrigendum packet (T3′), re-checked here.

No other attempt on this problem was on `origin/ai/probes` when I started.

## 1. The node and the properties it uses (main @ `abb98a12`)

**The node's input.** `docs/work_history/repo/review_feedback/pr8093-evidence/pr8093-original-proposal.md` L627–629: "The gravity node takes as input the covariant scalar record statistic whose two-point function on the formation law is the lattice Green function; that statistic is a record-dynamics block output." Nearby: "gravity (`(kappa, nu) = (1, 1)` conditional; the exact Regge result of pull request #8085; the Ward scalar bound of #8086)".

**The kernel's properties as the gravity lane uses them.**

| # | Property | Source on `main` |
|---|---|---|
| P1 | The symbol: the kernel is the `Z³` graph Green function, `Ĝ(k) = 1/E(k)` with `E(k) = Σ_a (2 − 2 cos k_a)` | `GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md` L13, L25–29 ("The A1 graph-Laplacian dispersion is `λ(k) = Σ_μ (2−2cos k_μ)` …", heat-kernel/Bessel form of `G`); `UNIVERSAL_GR_NEWTON_TENSOR_SCALAR_CONSISTENCY_BOUNDED_THEOREM_NOTE_2026-06-08.md` L16–19, L22 ("an inverted `Z^3` graph-Laplacian propagator form") |
| P2 | Unit Newtonian tail: `4π r G(r) → 1` | `UNIVERSAL_GR_…` L29–31 ("`G(0)=0.252731` and `4 pi r G(r)` approaches `1`"); `GRAVITY_LEADING_…` L13–14 ("leading term is `1/(4π\|r\|)`") |
| P3 | Leading lattice correction `[5/(32π)] K₄(n̂)/r³`, the `l = 4` cubic harmonic | `GRAVITY_LEADING_…` L17–18 |
| P4 | On-site value `G(0) = 0.252731` | `UNIVERSAL_GR_…` L29–30 |
| P5 | Small-k symbol `\|k\|² − (1/12) Σ k_μ⁴ + …`, shared with the tensor channel's `2 − 2cos k` | `GRAVITY_LEADING_…` L26, L67; `UNIVERSAL_GR_…` L18–19 |
| P6 | The Regge reduction's symbol `Delta = Σ_a p_a²`, `p_a = 2 sin(k_a/2)`, which equals `E(k)` at zero frequency | `REGGE_EXACT_REDUCTION_POSITIVE_TENSOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-13.md` L130 |
| P7 | The node's input is a *two-point function* of a covariant scalar record statistic *on the formation law* | the #8093 line above |

The absolute Newton constant and the tensor/scalar normalization are explicitly not supplied on `main` (`UNIVERSAL_GR_…` L23–25). So "the node's normalization" below means the unit coefficient of P1–P2.

## 2. Steps

**S1 (PROVED; CHECKED `N1`).** `Σ_a (2 sin(k_a/2))² = Σ_a (2 − 2 cos k_a) = E(k)`, and `E = |k|² − (1/12) Σ_a k_a⁴ + O(k⁶)`. So P1, P5 and P6 are one symbol.

**S2 (PROVED; CHECKED `L1`). Candidate (iii), light-cone 3+1.**
- The linearized transverse field is `θ_{t+1} = P θ_t + ξ_t` with the symmetric 7-stencil average. Its multiplier is `φ = (1 + 2 Σ_j cos k_j)/7 = 1 − E/7`, which is real, and the noise is `Var ξ = σ² = A(7β)/(7β)` per component.
- The static response to a persistent source, from `θ = Pθ + h`, is exactly `χ = 1/(1 − φ) = 7/E`.
- The stationary equal-time covariance is `C = σ²/(1 − φ²) = 49σ²/(E(14 − E)) = (7/2) σ² (1/E + 1/(14 − E))`.
- The fluctuation–response ratio is `C/(σ² χ) = 1/(1 + φ) = 7/(14 − E)`. It is `1/2` at `k → 0` and `7/2` at the zone corner.
  - The single-site vMF has variance equal to response: transverse variance and linear response are both `A(κ)/κ`.
  - The formation law's two-point function is nonetheless half its static response at long wavelength.

**S3 (PROVED; CHECKED `L2`). The remainder is short-range.**
- On the torus `0 ≤ E ≤ 12`. So `H := 1/(14 − E) = Σ_n (1/14)(E/14)^n`, and `(E/14)^n` has sup norm `≤ (6/7)^n` and support `|r|₁ ≤ n`.
- Hence `|H(r)| ≤ Σ_{n ≥ |r|₁} (1/14)(6/7)^n = (1/2)(6/7)^{|r|₁}`.
- In real space, `C(r) = (7/2) σ² (G(r) + H(r))`: the lattice Green function plus an exponentially decaying term.
- Exact partial sums respect the bound (largest ratio `0.281` on `|r|₁ ≤ 6`).

**S4 (PROVED; CHECKED `L3`). The normalization equations.**
- `A(κ)/κ` is decreasing, since the series of `cosh u − 1 − u²/4 − (u/4) sinh u` has nonpositive coefficients (the lemma of my plane-memory-loss-2 attempt). So `A(7β)/β` decreases strictly from `7/3` to `0`, and each equation below has exactly one root.
- **Response reading** (the task's "χ = 7/E as input, σ² as the normalization"). The node's output kernel is `σ² χ = A(7β)/(βE)`, that is, `(A(7β)/β) · G`. Unit coefficient requires `A(7β) = β`, so `β_resp ∈ [0.8273, 0.8274]` (interval arithmetic, 50 digits; root `0.82735…`).
- **Two-point reading** (the #8093 statement, P7). The tail coefficient of `C` is `(7/2) σ² = A(7β)/(2β)`. Unit coefficient requires `A(7β) = 2β`, so `β_cov ∈ [0.2340, 0.2341]` (root `0.23405…`).

**S5 (PROVED; CHECKED `B1`). Candidate (ii), backward 3+1.**
- `φ = (1 + Σ_{j=1}^3 e^{ik_j})/4` gives `1 − |φ|² = (1/8)[Σ_j (1 − cos k_j) + Σ_{i<j} (1 − cos(k_i − k_j))]`. This is the twelve-neighbour (FCC) Laplacian of the level lattice of the `Z⁴` event lattice.
- So `C = 8σ²/E_FCC` is that lattice's Green function. Its small-k form is `kᵀ(4I − J)k/16`, with eigenvalues `4, 4, 1` in the lattice coordinates: isotropic only in the level lattice's own metric, and not a multiple of `|k|²`.
- `χ = 1/(1 − φ)` is complex with `χ(−k) = conj χ(k) ≠ χ(k)`, so the static response is one-sided in real space.

**S6 (PROVED; CHECKED `B2`). Candidate (i), backward 2+1 (block 35).** In the `Z³` coordinates `K = (k₁ + w, k₂ + w, w)`, `E(K) = 3|1 − φ e^{iw}|² + 3(1 − u(k))` with `φ = (1 + e^{ik₁} + e^{ik₂})/3`. So:
- the formation spectral density `σ²/|1 − φ e^{iw}|²` is not `c/E(K)`; the difference is the mass-like `3(1 − u)`;
- its equal-level kernel `σ²/(1 − u)` is two-dimensional, since `1 − u = kᵀMk + …` on the level plane.

## 3. The candidates through the node

Verdicts per property:

| Property | (i) backward 2+1 | (ii) backward 3+1 | (iii) light-cone 3+1: `χ = 7/E` | (iii) light-cone 3+1: `C` |
|---|---|---|---|---|
| P1 symbol `c/E(k)` | fails (S6) | fails: FCC symbol (S5) | holds exactly, `c = 7` | holds up to the short-range `H` (S3), `c = (7/2)σ²` |
| P2 tail `1/(4πr)` | fails (2D level kernel; diffusive space-time kernel) | a `1/r` tail in the level lattice's metric, not in `Z³`'s | holds, coefficient `7` | holds, coefficient `(7/2)σ²` |
| P3 `K₄/r³` correction | fails | fails (FCC anisotropy) | holds, times `7` | holds, times `(7/2)σ²`, plus an exponentially small term |
| P4 `G(0)` | fails | fails (FCC value) | `χ(0) = 7 G(0)` | `(7/2)σ²(G(0) + H(0))` |
| P5 small-k symbol, shared with the tensor channel | fails | fails (eigenvalues `4, 4, 1`) | holds | holds |
| P6 Regge `Delta` at zero frequency | fails | fails | holds (S1) | holds |
| P7 two-point function on the formation law | holds, but the wrong object | holds, but the wrong object | fails: `χ` is a response, not a two-point function | holds |
| Symmetric response | n/a | fails (one-sided) | holds | n/a |

**The node's output for (iii).**
- With `χ` as input and `σ² = A(7β)/(7β)`, the node outputs the lattice Green function times `A(7β)/β`:
  - `Φ(r) = [A(7β)/β] · [1/(4πr) + (5/(32π)) K₄(n̂)/r³ + O(r⁻⁵)]`;
  - the Regge and tensor-channel symbol is unchanged;
  - the unit coefficient needs `β ∈ [0.8273, 0.8274]`.
- With the two-point function (the #8093 input), the tail coefficient is `A(7β)/(2β)`, and the unit coefficient needs `β ∈ [0.2340, 0.2341]`.
- The two readings differ by the fluctuation–response factor `1/(1 + φ) → 1/2`.

## 4. What would finish it, and caveats

- **Which object the node consumes, the static response or the two-point function, is the gravity lane's decision.** The #8093 line says two-point function. On `main` the gravity notes use `G` as a propagator, which is a response. The two normalizations differ by a factor of 2 at long wavelength (S2).
- **The executed normalization of the nonlinear light-cone law** (`0.96–0.99` of the linear kernel, per the task) would multiply either coefficient. It shifts the roots slightly. Not claimed.
- **The linearization is about an aligned state.**
  - `β_resp ≈ 0.827` lies above the light-cone long-range-order threshold `(3/2)(I₀ + I₂) ∈ [0.5879, 0.5931]` claimed for referee in my own lightcone-long-range-order a5. That claim is not yet refereed.
  - `β_cov ≈ 0.234` lies below it, where no aligned state is established. There, the linearized `σ²` is not the relevant normalization.
- **The backward kernels (i) and (ii)** would need the node re-posed on their own lattices: the 2D level plane with level-time diffusion, or the FCC level lattice with a one-sided response. `main` has no such node.
