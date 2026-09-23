# J:derive:ray-limit-of-the-clocked-walk:a4

Worker `w-macbookpro90c72-j3c21` (claude-opus-5-5). This is attempt 4 of 4. No earlier attempt's files exist on `ai/probes`, so the plan is my own.

Definitions come from block 54 (open PR #8570) and block 53 (#8568). The numerical comparison re-implements the construction and measurement of block 54's control, `specs/supervisor_control_block54_orientation.py` on that branch.

## (1) Exact statement

### Setting

- `H = Σ_j σ_j D_j` with `D_j = (i/2)(T_j − T_j†)`, where `(T_j ψ)(x) = ψ(x − e_j)`. The symbol is `h(k) = d(k)·σ` with `d = (sin k_1, sin k_2, sin k_3)` and `ε = |d|`.
- `H_w = √w H √w`, with `u = log w`.
- `|u(x + e_j) − u(x)| ≤ g`, and every second difference is `≤ g₂` (the task's `g₂ = g²`).
- `ψ(t) = e^{−iH_w t}ψ₀` with `‖ψ₀‖ = 1`.
- `E = ⟨H_w⟩` and `ΔE = ‖(H_w − E)ψ‖`; both are conserved.
- `τ_a(t) = ⟨T_a⟩` and `X̄ = ⟨X⟩`.
- `x̄(t)` is the lattice point nearest `X̄(t)`, and `c_a = u(x̄ + a) − u(x̄)`.

### (a) What is proved, and what is assumed

**Theorem A (the wave-vector law).**
1. `|τ̇_a − i(e^{c_a} − 1) E τ_a| ≤ |e^{c_a} − 1| ΔE + 3 e^{g} w(x̄) g₂ 𝓜(t)`.
2. Here `𝓜(t)² = ⟨(|X − x̄|₁ + 1)² e^{2(g+g₂)(|X − x̄|₁ + 1)}⟩`.
3. Hence the mean wave vector `K̄_a = −arg τ_a` obeys `|K̄̇_a + (e^{c_a} − 1)E| ≤ (g e^g ΔE + 3e^g w g₂ 𝓜)/|τ_a|`. This is the ray law `k̇ = −E∇u`, with a remainder that is explicit in:
   - `ΔE/E` (about `1/(kσ)`);
   - `g₂𝓜/g` (about `gσ` when `g₂ = g²`);
   - the time, through `𝓜(t)` and `|τ_a(t)|` (about `gT`).
4. In a uniform gradient (`g₂ = 0`) the second term vanishes; this is block 54's exact lemma.

**Theorem B (the velocity).**
1. `dX̄_j/dt = ⟨√w σ_j C_j √w⟩` exactly, with `C_j = (T_j + T_j†)/2`.
2. `|⟨√w σ_j C_j √w⟩ − w(x̄)⟨σ_j C_j⟩| ≤ w(x̄) g e^g ⟨(|X − x̄|₁ + 1) e^{g|X − x̄|₁}⟩`.
3. `⟨σ_j C_j⟩ = ∫|φ₊|² ∂_jε − ∫|φ₋|² ∂_jε + 2 Re ∫ φ₊* φ₋ ⟨u₊|σ_j|u₋⟩ cos k_j`, exactly, where `ψ̂ = φ₊u₊ + φ₋u₋`.
4. So `|⟨σ_j C_j⟩ − ∫|φ₊|² ∂_jε| ≤ 2β + 2√β`, where `β = ∫|φ₋|²` is the branch admixture.
5. Near `K̄`, `∫|φ₊|² ∂_jε = ∂_jε(K̄) + O(s_k² sup|∇²∂_jε|)`. The momentum spread `s_k² ≈ Σ_j 2(1 − |τ_{e_j}|)` is controlled by Theorem A.

**Lemma C (branch purity) — ASSUMED.** `β(t) = O((g/k)²)` uniformly for `T ≤ c/g`. This is adiabatic following across the gap `2wε`. It is checked, not proved: `β(T) = 3.3×10⁻⁵` at `k = 0.5`, `g = 0.004`, `T = 30`, against `(g/k)² = 6.4×10⁻⁵`.

With Lemma C, A and B give the ray limit for mean position and mean wave vector for `T ≤ c/g`. The errors are:
- zeroth order in the admixture: `O(β)`;
- first order: the anomalous velocity (b), at the level of `√β`.

### (b) The first correction

The positive branch of `h(k)` has the exact lattice curvature (with `A = i⟨u|∇u⟩` and `Ω = ∇ × A`)

`Ω_i(k) = −sin k_i cos k_j cos k_l / (2|d|³)`, for `(i, j, l)` cyclic, and `Ω₋ = −Ω₊`.

- At small `k` this is `−k/(2|k|³)`.
- Near the zero-energy point `K` (`K_j ∈ {0, π}`) it is `−χ_K q/(2|q|³)`, with `q = k − K` and `χ_K = Π_j cos K_j`.

The packet's velocity is `w∇ε − k̇ × Ω = w∇ε + E ∇u × Ω`, with `k̇ = −E∇u`.

The sideways displacement is `∫ E ∇u × Ω dt`. At small `k` with `∇u ⊥ k`, it is `gT/(2k)` along `−(gradient × motion)`. On the lattice it is `gT/(2 sin k)` along an axis.

Rays that carry this term reproduce the walk:

| `k` | walk | rays with anomalous velocity | plain rays |
|---|---|---|---|
| 1 | −0.0685 | −0.0683 | −0.0006 |
| 0.5 | −0.1200 | −0.1185 | −0.0010 |
| 0.25 | −0.2285 | −0.2197 | −0.0014 |

At `k = 1` the continuum `−gT/(2k)` gives −0.0600. The residual 4% at `k = 0.25` is where `kσ = 1.75`.

**Branch dependence.** At the same `k` the anomalous velocity `ε∇w × Ω₊` is the same for both branches. The negative branch moves the other way, so relative to the motion its drift has the opposite sign (walk +0.1200, rays +0.1185).

### (c) Universality

**Universal.** The change of wave vector `k̇ = −E∇u` (block 54). The fall is universal too:
- the anomalous velocity is perpendicular to `∇u`, so it adds nothing to the fall;
- both branches and every zero-energy point fall alike: −1.6164 for the positive branch at `K = 0`, for the negative branch, and at `K = (π,0,0)`.

**Not universal: the sideways drift.** Relative to the motion it is `−χ_K g T/(2|q|)` near `K`. It depends on:
- the wave number, through `1/(2 sin k)` on the lattice;
- the handedness `χ_K`;
- the branch.

**Cancellation.**
- **No single-branch packet at a single point is free of drift.**
- **Within one component:** the two branches at the same `k` drift alike in space.
- **Opposite-handedness pairs cancel.** A positive packet at `k` and a negative packet at `−k` (which move together) drift oppositely. So do packets at points of opposite `χ` that move the same way; each point's velocity near `K` is `q̂`.
- **The zero-energy points.** There are four of each handedness (flux of `Ω₊` is `−2πχ_K`, total zero).
- **Superpositions.** An equal superposition of `χ = +1` and `χ = −1` packets moving together has centroid drift 0.0000 (walk). Its components still separate, by `gT/|q|`.

## (2) Steps

1. **PROVED (identities).**
   - `[X_j, T_j] = T_j`, so `i[H, X_j] = σ_j C_j` and `i[H_w, X_j] = √w σ_j C_j √w`.
   - `T_a† M_f T_a = M_{f(·+a)}`, and `H` commutes with `T_a`, so `[H_w, T_a] = T_a(H_{w(·+a)} − H_w)` with `H_{w(·+a)} = √w e^{δ/2} H e^{δ/2} √w`, `δ = u(· + a) − u`.
   - **CHECKED (B1):** on a `4³` torus with random `u`, to machine precision.

2. **PROVED (Theorem A).** Write `δ = c_a + η` with `η(x̄) = 0`. Then `[H_w, T_a] = (e^c − 1)T_a H_w + e^c T_a R`, with `R = √w(e^{η/2} H e^{η/2} − H)√w`.
   - Take expectations. `⟨T_a H_w⟩ = Eτ_a + ⟨T_a(H_w − E)⟩`, and `|⟨T_a(H_w − E)⟩| ≤ ΔE`.
   - The bound on `R` has three ingredients:
     - `|η(x)| ≤ g₂|x − x̄|₁`, since `δ` changes along a lattice path by second differences;
     - `√(w_x w_y) ≤ w(x̄) e^{g(|y − x̄|₁ + 1)}` for neighbours `x ∼ y`;
     - `|e^z − 1| ≤ |z|e^{|z|}`, with `|H_xy| = 1/2`.
   - Each site has six neighbours, so by Cauchy–Schwarz `‖Rψ‖ ≤ 3 w(x̄) g₂ 𝓜`.
   - For the argument: `d arg τ/dt = Im(τ̇/τ)`.

3. **PROVED (Theorem B.1–4).** `√(w_x w_{x±e_j}) − w(x̄)` is bounded as in step 2, using the bond form of the velocity. `C_j` has symbol `cos k_j`, and `⟨u₊|σ_j|u₊⟩ cos k_j = (sin k_j/ε) cos k_j = ∂_jε`. `|∂_jε| ≤ 1`, and `|⟨u₊|σ_j|u₋⟩| ≤ 1`.

4. **PROVED (Theorem B.5).** Taylor expansion to second order. `1 − |τ_a|²` is the variance of the unitary `T_a`, which bounds `∫|ψ̂|² |e^{−ik·a} − e^{−iK̄·a}|²`.

5. **ASSUMED (Lemma C).** Stated above; standard adiabatic perturbation across the gap `2wε`.

6. **PROVED (Ω, exact).** Use `F_{jl} = i Tr(P[∂_j P, ∂_l P])` with `P = (1 + d̂·σ)/2`. Since `∂_j d = cos k_j e_j`, `d̂·(∂_j d̂ × ∂_l d̂) = sin k_i cos k_j cos k_l/|d|³`.
   - **CHECKED (A1):** sympy at three rational points to `10⁻¹²`; small-plaquette Berry phases fix the sign.
   - **CHECKED (A2):** the flux through a sphere of radius 0.05 around each of the eight `K` is `−2πχ_K`.

7. **DERIVED (anomalous velocity).** This is standard: first-order adiabatic admixture `φ₋ ∝ k̇·⟨u₋|∇u₊⟩/(2E)`, inserted in B.3's interference term, gives `−k̇ × Ω`. For `H_w`, the symbol is `w(x)h(k) + O(∇²w)`: the first-order Moyal terms of `√w # h # √w` cancel. The eigenvectors do not depend on `x`, so there is no mixed or position-space curvature. It is **CHECKED (C1, C2)** by rays against the walk.

8. **CHECKED (C1, floating point).**
   - The three wave vectors, as in (b), using block 54's packets (odd part in `g`, gradient along `z`, motion along `x`).
   - `ΔE/E = 0.17` at `k = 0.5`.
   - The plain-ray sideways motion is at most 3% of the walk's, and the fall agrees to 1.5%.

9. **CHECKED (C2, floating point).** The branch, the `χ = −1` point `K = (π,0,0)`, the equal fall, and the superposition, as in (c).

## (3) Where the route fails

**The first step not proved is Lemma C.** Theorem B controls the position only up to `2β + 2√β`, and `√β` is of the same order as the anomalous velocity. So the zeroth-order ray theorem for the position, and the first correction, both need a quantitative adiabatic bound on the branch admixture. Such a bound needs an integration by parts in time, with the gap `2wε(k)` bounded below along the packet's path. The gap closes at the eight zero-energy points, so the bound must degrade like `g/ε`, that is like `g/k`.

The explicit constants in A and B are crude: `𝓜` grows at most ballistically, `√Var(t) ≤ √Var(0) + 2√3 w_max t`. They are not optimised.

## (4) What would finish it

- A proof of Lemma C: an adiabatic theorem on the lattice for `H_w` with gap `2wε`, giving `β(t) ≤ C (g/ε_min)²` for `T ≤ c/g`.
- Then the anomalous velocity as a theorem, with remainder `O(g², g/(kσ))`.
- The `O(1/(kσ))` shortfall at `k = 0.25`, from averaging `Ω` over the packet's momentum spread.
