# bound-bodies-and-the-two-far-fields, attempt 2 of 2

**The far fields' difference is the hop energy minus the field energy, exactly. The lattice breaks the virial that would make them equal for a self-bound body.**

Worker `w-jonathonsmac4f50-ja0f7` (`claude-opus-5-5`), unit `J:derive:bound-bodies-and-the-two-far-fields:a2`.

**Provenance.**
- *Plan first.* I formed my plan before reading attempt a1: the two weight identities of the ledger at held walls, then the leading-order virial of a heavy self-bound walker computed on the lattice.
- *Attempt a1* (`w-macbookpro90c72-j7e6e`, `claude-opus-5-5`, same model family as me, unrefereed, issue #8649) derives:
  - (a) the field equations and `P − Q`;
  - (c) `P − 3Q = (3/8K)Σe(w − 1)/(wχ)`;
  - (b) block 66's dilation identity on a box (`i[H, G_x]` = the two-step hop, with no wall operator), and that massive content needs the two-step relabelling;
  - (b) `P = Q` at leading order, through two continuum steps marked ASSUMED;
  - (d) no exact statement.
- *New here:*
  - **the exact identities `8KQ = E + F`, `P − Q = (T − F)/(4K)` and `P + Q = (E + T)/(4K)`**, at every strength, for any content. These answer (d).
  - **the lattice value of the virial defect**, which qualifies a1's leading-order `P = Q`.
  - the exact light-like form `P − 3Q = −F/(2K)`, equal to a1's on solutions.
  - independent re-checks: of the field equations (A1), and of a1's box identity (B3).
- *Definitions* come from block 60 (PR #8590), which uses blocks 53–59, and from blocks 66 (#8597) and 77 (#8612):
  - `w = e^u`, `ℓ = e^λ`, `χ = √ℓ`, `N = wχ`;
  - content crossed at `√(w_x w_y)/(χ_xχ_y)` on bonds, plus rest terms `ρw` on sites;
  - `e = ∂⟨H⟩/∂u` and `τ = −∂⟨H⟩/∂λ`;
  - `E = ⟨H⟩` and `T = Στ`, the hop energy;
  - the curvature member `F = −8KΣ_bonds(N_y − N_x)(χ_y − χ_x)` over every bond with an interior end;
  - walls held at `w = ℓ = 1`;
  - `Q = −Σ_interior Δχ` and `P = Σ_interior ΔN`. Far away `χ − 1 = Qg` and `1 − N = Pg`, so the lengths carry `2Q` and the rates `P + Q`.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a)** Stationarity of `⟨H⟩ + F` in `u_z` and in `λ_z` gives `Δχ = −e/(8KN)` and `ΔN = (e + 2τ)/(8Kχ)`. Hence
>
> `P − Q = (1/8K)Σ[2τ − e(1/w − 1)]/χ`.
>
> This is the supervisor's scratch result, re-derived. **(exact)**
>
> **(d) Exact, at every strength.** This holds for any content with bond and rest energies, whether or not the content is stationary, provided the fields are stationary in the interior:
>
> **`8KQ = E + F`,  `P − Q = (T − F)/(4K)`,  `P + Q = (E + T)/(4K)`.**
>
> On solutions, also `F = Σe(1/N − 1)`, so `P − Q = (1/4K)Σ[τ + e(1 − 1/N)]`. In words:
> - the rates' far field counts the energy plus the hop energy;
> - the lengths' far field counts the ledger;
> - **the two agree iff the content's hop energy equals the field energy: `T = F`.**
>
> The pinned body (`T = 0`) has `P = Q − F/(4K) < Q`.
>
> **(c) Light-like content, exactly.** With no rest term, `e = τ` at every site. Then `P − 3Q = −F/(2K) = (1/2K)Σe(1 − 1/N)`:
> - `P = 3Q` up to relative order `u`;
> - the rates' far field `P + Q` is twice the lengths' `2Q`.
>
> **(b) Weak field.** Use the bound body's power counting: `e`, `u`, `λ` are `O(ε)` and `τ` is `O(ε²)`. Then:
> - `P − Q = (1/8K)(2T + Σeu) + O(ε³)`;
> - so `P = Q` at leading order iff `2T = −Σeu`, equivalently iff `T = F` with `F = −½Σeu`;
> - for a heavy walker, `T = 2E_kin` exactly at leading order, and the condition is the virial balance `2E_kin + W = 0` with `W = ½Σeu`;
> - block 66's dilation identity on a box balances the **two-step** hop against the force moment, so it does not supply the balance exactly on the lattice. The walls add no operator (a1's B2, re-checked).
>
> **(b) Executed, not claimed: the balance on the lattice.** At leading order, the heavy walker bound by its own weak field is a lattice Schrödinger–Newton problem, whose shape is fixed by `β = m³/(2K)` alone. Its virial defect `v = (2E_kin + W)/|W|` gives `(P − Q)/Q = v × O(u)`.
> - **Extended bodies:** `v·R² ≈ 5.2`, constant for `R = 5.8` to `14`. So `P = Q` at leading order holds only as `R/a → ∞`.
> - **Compact bodies,** held on about one site by their own well for `β ≳ 12`: `v` runs `+0.74, +0.33, −0.26, −0.62, −0.94` for `β = 12, 16, 30, 60, 400`. **`P = Q` fails at leading order**, and for heavy compact bodies `P → Qw`, as for a pinned body.
> - **The walls** add a term falling roughly as `1/L` through the images in the field's Green function.
>
> The task's HIT condition, `P = Q` failing for a self-bound body at leading order, is met at the executed level, together with the exact identity of (d).

## 2. The steps

1. **PROVED + CHECKED (A1).**
   - `∂/∂u_z` of a bond term `h√(w_xw_y)/(χ_xχ_y)` is half the term; `−∂/∂λ_z` is also half. So `e − τ = ρw`, the rest term.
   - `∂F/∂u_z = 8KN_z(Δχ)_z`, since `F = 8KΣN(Δχ)` over all sites and `Δ` is symmetric.
   - `∂F/∂λ_z = 4K[N_z(Δχ)_z + χ_z(ΔN)_z]`.
   - Solving the two stationarity equations gives the pair of (a).
   - Checked symbolically on a box of two interior sites and ten walls, with every rate and length a free symbol, a bond energy and two rest energies.

2. **PROVED + CHECKED (A2): the two weight identities.**
   - *Rates.* Every term of the ledger has degree one in the set of all rates: the content by weight one, `F` because it is linear in `N = wχ`. So `Σ_all ∂𝓔/∂u_x = 𝓔`.
     - Stationarity at interior sites leaves the walls' share: `𝓔 = Σ_W ∂F/∂u_x`.
     - At `w = χ = 1` on the walls this is `8KΣ_{wall bonds}(χ_y − 1)`, which is `8KQ` by Gauss.
   - *Lengths.* Put `χ → e^{s/2}χ` at every site. Hop terms scale by `e^{−s}`, rest terms are unchanged, and `F` scales by `e^{s}`. So `Σ_all ∂𝓔/∂λ_x = F − T`.
     - Interior stationarity leaves `Σ_W ∂F/∂λ_x = F − T`.
     - At the held walls this is `4KΣ_{wall bonds}[(χ_y − 1) + (N_y − 1)] = 4K(Q − P)`.
   - *Hence* `8KQ = E + F` and `P − Q = (T − F)/(4K)`.
   - Every piece is checked symbolically: both weights, both wall derivatives, both Gauss sums. The content's own stationarity is never used.

3. **CHECKED (A3, A4).**
   - *Exact.* Block 60 T4's pinned body (`m = 3`, `K = ½`, centre of the `3³` box, `Q` in radicals) satisfies the three identities exactly.
   - *NUMERIC.* On a `3³` box with random bond and rest energies at strong field (`u` down to −0.30), solved to `1e−11`:
     - the identities hold;
     - the supervisor's formula and `(1/4K)Σ[τ + e(1 − 1/N)]` give the same `P − Q` to `1e−9`;
     - with no rest term, `P − 3Q = −F/(2K)` equals a1's `(3/8K)Σe(w − 1)/(wχ)`.

4. **PROVED (c).** From step 2 with `E = T`: `P − Q = (E − F)/(4K)` and `2Q = (E + F)/(4K)`, so `P − 3Q = −F/(2K)`. On solutions `F = Σe(1/N − 1)`, which is second order.

5. **PROVED + CHECKED (B1): weak field.**
   - `1 − 1/N = (N − 1) + O(ε²)`, and `N − 1 = u + λ/2`.
   - At first order `Δλ = −e/(4K)` and `Δu = (e + τ)/(4K)`, so `u + λ = −(1/4K)G_Dτ = O(ε²)`.
   - Hence `P − Q = (1/4K)[T + ½Σeu] + O(ε³)`.
   - NUMERIC check: with content strength `ε = 10⁻², 10⁻³` and hop energies of order `ε²`, the relative mismatch falls from `6.2e−4` to `6.2e−5`.

6. **CHECKED (B3): block 66 with `ξ = x` on a `3×2×2` box, truncated shifts.**
   - `i[H, G_x] = Σ_aσ_a(T_a² − T_a†²)/(4i)`, exactly. This is a1's B2, re-checked independently.
   - A stationary state of `φHφ` therefore has `⟨φψ|H₂|φψ⟩ = Σx·f`. This is the two-step hop, not `T`, so the lattice gives no exact `2T = −Σeu`.
   - The walls add no operator. They enter the virial through the field's Green function (step 9).

7. **The heavy walker at leading order.**
   - **CHECKED (B2), exact:** with the staggered rest term `(H + mε)² = s² + m²`, and the positive branch's hop energy per state is `s²/√(m² + s²)`. So `T = ⟨S²⟩/m + O(m^{−3}) = 2E_kin`.
   - **ASSUMED, the standard leading-order expansion:** the positive branch's energy is `m + S²/(2m) + mu` on one parity class. At leading order that class is `ε = +1`, and `S²` preserves each coordinate's parity. The field is `Δu = e/(4K)` with `e = mρ`.
     - Then `T − F = 2E_kin + W`.
     - Stationarity is `[S² − βGρ]ψ = λψ` with `β = m³/(2K)`, `S² = ¼(−Δ_coarse)` on the class, and `G` the lattice Green function of `−Δ`.
     - This gives `(P − Q)/Q = 2v|W|/m`, with `|W|/m` of order `u`.
   - Weak field needs `m² ≫ βG(0)/2` together with `m ≫ 1`, which is consistent for every `β`.

8. **NUMERIC (B4): the virial defect on the infinite lattice, with no walls.**
   - *Method.*
     - `G` from `∫∏ ive(x_i, 2t)dt`: `G(0) = 0.25273100` against Watson's `0.2527310098`, `G(1,0,0)` to `3e−9`, and the two-term asymptotic form beyond `r = 24`.
     - The potential by FFT convolution on the class.
     - Self-consistent iteration to `10⁻¹⁰`.
   - *Two branches.* Both were found for `β = 12–17`. From wide starts at `β = 18` and `20` the iteration reached only the compact branch; whether the extended one still exists there was not settled.
   - *Extended branch* (`β = 16, 12, 10, 8`):
     - `R_rms = 5.83, 8.79, 10.92, 13.99`;
     - `v = 0.156, 0.067, 0.0435, 0.0265`;
     - `vR² = 5.29, 5.20, 5.18, 5.19`.
   - *Compact branch* (`β = 12, 16, 30, 60, 400`):
     - `R_rms = 0.58, 0.40, 0.20, 0.10, 0.01`;
     - `v = +0.737, +0.328, −0.261, −0.619, −0.941`.
   - `v` crosses zero between `β = 20` (`+0.080`, in an earlier scratch run) and `β = 25` (`−0.115`, in a Dirichlet box of 65, whose wall term is negligible for a compact body): a compact body satisfies the balance only there, by accident. The limit `v → −1` is a body with no kinetic share, which is block 60's pinned body.

9. **NUMERIC (B5): the walls.** Dirichlet boxes `L = 49, 73, 97` at `β = 16` give `v = 0.423, 0.324, 0.278` against the infinite lattice's `0.156`, with `(v − v∞)L ≈ 13.1, 12.3, 11.9`. The walls' images add a term of order `R/L` to the field's energy.

## 3. Where this stops

- **(d) has an exact answer:** `P − Q = (T − F)/(4K)`. There is no exact `P = Q` for a self-bound lattice body, because nothing on the lattice forces `T = F`: the dilation that would do so in the continuum is not a lattice symmetry (step 6).
- **(b) at leading order:** `P = Q` iff `T = F`, which is the virial balance. The executed defect is `≈ 5.2(a/R)²` for extended bodies and of order one for compact ones.
- **The route's first unproved step is step 7:** the leading-order reduction of the massive walk to lattice Schrödinger–Newton. It is a standard expansion, but it is not proved here to all orders. Also, the full nonlinear self-consistent massive walk in the exact fields of the curvature member is not solved. The identity of step 2 is exact; the size of the defect comes through the reduction.

## 4. What would finish it

1. **A full self-consistent solution** of `φ(H + mε)φ`, with lengths, in the exact fields `Δχ = −e/(8KN)` and `ΔN = (e + 2τ)/(8Kχ)`, at moderate strength. Read `P` and `Q` at the walls, and compare with `(T − F)/(4K)` and with step 8's `v`.
2. **An exact lattice virial for massive content,** a1's two-step relabelling `G_P` with the staggered term. It would give `T − F` exactly as a lattice-correction functional.
3. **The owner's view** on whether compact self-bound records, the branch where `P = Q` fails at leading order, are the framework's bodies.
4. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/bound-bodies-and-the-two-far-fields/w-jonathonsmac4f50-ja0f7/check.py
```

- It has 9 lines:
  - A1–A3, B2, B3 are exact (sympy);
  - A4, B1, B4, B5 are labelled NUMERIC.
- `snlat.py` holds the lattice Schrödinger–Newton solvers and the Green function.
- It runs in about 70 seconds.
