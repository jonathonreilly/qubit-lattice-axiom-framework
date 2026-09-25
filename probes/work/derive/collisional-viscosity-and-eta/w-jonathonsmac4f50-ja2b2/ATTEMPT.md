# The collisional viscosity of the record gas, and η — attempt a1

Worker `w-jonathonsmac4f50-ja2b2`, model `claude-opus-5-5`.

**Provenance.**
- Blocks 44 and 51 are by the same model family (Claude).
- This machine's `next-order-force-between-capturing-bodies` a3 (#8836) used a shear viscosity ν as a free parameter.
- This machine also attempted `isotropic-streaming-clause`.
- Neither computed `ν_coll`.
- No prior attempt on this problem was printed at claim time.
- The referee should come from another family.

**Sources, as landed on main.**
- Block 51, `docs/ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_..._2026-09-21.md`. It is conditional on dilute independent streaming and a first-harmonic closure, and gives `ν_lat = √3/16`. It leaves "the collision viscosity ... not derived".
- Block 44 for the clause: the re-draw `P/2 ± r w`, with `w` uniform on the circle orthogonal to `P`, on bonds at rate `γ`, and exchange at occupied targets.
- Simulator: `probes/lib/inertial.py`, `tick_s`, unchanged.

**Result.**
- The route the task outlines has a precise failure at its molecular-chaos step.
- Within that closure, exactly: `ω₂ = 3γρ`, and `ν_coll = 1/(45γρ)`, isotropic.
- The gas does not follow it. Re-drawing a pair that was just re-drawn changes nothing (the re-draw kernel is idempotent). On a bond clock the same adjacent pair is re-drawn again and again, so the stress relaxes at the rate fresh adjacencies form, not at `6γρ/2`.
- Executed transverse waves give a viscosity that saturates in `γ`. So the measured `η` is about `0.24` at `(ρ, γ) = (0.1, 2)` and `0.31` at `(0.3, 1)`, against the closure's `0.46` and `0.48`.
- Exact pieces that stand:
  - the halving identity;
  - the Chapman–Enskog form `ν = 1/(15ω₂)` for any `ℓ = 2` rate;
  - the exchange's momentum currents at finite density: `ν_lat`'s isotropic part gains `ρ/(4√3)`, and its cubic part stays `√3/16`;
  - a polarization test of `η` that does not need `ω₂`.

## 1. Statement attempted

The task asks for:
- (a) the relaxation rate `ω₂` of the second harmonic under the bond re-draw, and `ν_coll` by the expansion about local equilibrium, with its isotropy;
- (b) `η(ρ, γ) = ν_lat/(ν_lat + ν_coll)`, compared with block 51's executed pattern;
- (c) what exclusion at finite density does to `ν_lat`.

## 2. Steps

1. **PROVED and CHECKED (E1) — sphere moments.**
   - `⟨|s_k|⟩ = 1/2`, `⟨max(s_k, 0)⟩ = 1/4`.
   - `⟨s_i²|s_i|⟩ = 1/4`, `⟨s_i²|s_k|⟩ = 1/8`.
   - `⟨s_k² 1(s_k > 0)⟩ = 1/6`.
   - `⟨s_k⁴⟩ = 1/5`, `⟨s_i² s_k²⟩ = 1/15`.
2. **PROVED — the re-draw kernel is a projection.**
   - Given the pair's two contents, the output is `(P/2 + r w, P/2 − r w)`, with `P = s + s'`, `r² = 1 − |P|²/4`, and `w` uniform on the unit circle orthogonal to `P`.
   - Its law depends on the input only through `P`, which it keeps. So a second re-draw of the same pair, with nothing in between, gives the same law as the first: the kernel is idempotent.
   - An exchange between the two sites only relabels the pair, and the output law is symmetric under `w → −w`.
   - `E_w[w wᵀ] = (I − P̂P̂ᵀ)/2` (E2a).
3. **PROVED and CHECKED (E2b, E2c) — the halving identity.**
   - For `s₁ = ẑ` and `s₂` uniform on the sphere, the mean change of the pair's summed second moment `s₁s₁ᵀ + s₂s₂ᵀ` under one re-draw is exactly `−(1/2)(s₁s₁ᵀ − I/3)` (sympy, over the full sphere).
   - The lib's `scatter_pair` agrees by Monte Carlo, `10⁵` samples (F0, floating-point evidence).
   - The re-draw is covariant under rotations of the contents. So its linearization about the isotropic law is a scalar on each harmonic `ℓ`:
     - zero on `ℓ = 0, 1`, since number and momentum are kept (E2c);
     - on `ℓ = 2`, one event removes half of a record's deviation.
4. **The step that fails: molecular chaos.** The route assumes that each re-draw meets a partner drawn independently from the one-site law.
   - With events at `6γρ` per record (six bonds, partner present with probability `ρ`, rate `γ`), this gives `ω₂ = 3γρ`.
   - It fails for this clause, by step 2. An adjacent pair keeps its bond clock until one record leaves, which happens at rate `λ ≈ 5/(2√3) ≈ 1.44` at small density: five of a record's six directions separate it, at `1/(4√3)` each.
   - So at `γ = 2` a pair is re-drawn several times per adjacency episode, and every re-draw after the first relaxes nothing.
   - **Executed, with the unchanged simulator.**
     - **F3.** A uniform stress `⟨s_z² − 1/3⟩` from a product start (`ρ = 0.1`, `γ = 2`, side 48) decays at `0.276` over the first tick and at `0.203` on average over six ticks, against `3γρ = 0.600`.
       - If each adjacent pair relaxes at most once in the first tick, the rate is `3ρ(1 − e^{−γ}) = 0.259`.
     - **F2.** Transverse-wave viscosity at `ρ = 0.1`:

       | γ | measured ν | molecular chaos |
       |---|---|---|
       | 1 | 0.544 ± 0.027 | 0.345 |
       | 2 | 0.448 ± 0.027 | 0.234 |
       | 4 | 0.415 ± 0.027 | 0.178 |
       | 8 | 0.407 ± 0.020 | 0.150 |

       - It saturates: `ν(8)/ν(2) = 0.91`, against the closure's `0.64`.
       - At `γ = 8` it exceeds the closure's value by 13 standard errors.
       - Side 48 (smaller `q`) gives `0.439 ± 0.016` at `γ = 2`, the same as side 32: the measurement is in the hydrodynamic regime.
   - This is the first failing step.
5. **PROVED and CHECKED (E3) — Chapman–Enskog, conditional on an `ℓ = 2` rate `ω₂`.**
   - Local equilibrium is `f₀ = (n/4π)(1 + 3s·U)`.
   - The second harmonic of the transport `(1/√3)s·∇f₀` is `(1/√3)(3n/4π)(s_k s_l − δ_kl/3)∂_l U_k`.
   - So `f₁ = −(1/ω₂)` × that, and `δΠ_ij = −(n/ω₂)[(2/15)S_ij − (2/45)δ_ij ∇·U]`.
   - The momentum equation gains `(1/(15ω₂))(∇²g_i + (1/3)∂_i∇·g)`, so `ν_coll = 1/(15ω₂)`.
   - It is **isotropic**: the transport `s·∇/√3` and the re-draw are both rotation-covariant in content space. Only the second-order streaming term (`ν_lat`) carries the lattice's cubic symmetry.
   - With molecular chaos, `ν_coll = 1/(45γρ)`. With the gas's own `ω₂` it is larger.
6. **PROVED and CHECKED (E4) — (c) exclusion at finite density, in product states.**
   - A record at `x` attempting `x + e_k` at rate `max(s_k, 0)/√3` either enters an empty target or exchanges with the target's content `s'`.
   - The momentum current is `(1/√3)[Σ_s ρ_x(s) s_i max(s_k,0) − A⁺_x g_i(x+e_k)]` minus the mirror term, with `A⁺ = Σ_s ρ(s) max(s_k, 0)`.
   - The exchange's forward carry restores exactly what exclusion removes (E4a). Contents are carried forward as in free streaming, so the second-order streaming term, and with it `ν_lat` and its cubic part `√3/16`, is unchanged.
   - The new term is the backflow of the target's content. In local equilibrium `A^± = ρ/4 ± g_k/2` (E4b).
   - Its linear part adds `(ρ/(4√3))∇²g_i`, the same for every axis and component: isotropic (E4c).
   - Its quadratic part `−(1/√3)g_k g_i` is an advective flux, beyond linear response.
   - So at finite density `ν_lat → √3/16 + ρ/(4√3)` in the isotropic part and `√3/16` in the cubic part, within the product-state closure for the currents.
7. **PROVED and CHECKED (E6) — an η meter independent of ω₂.**
   - For `g = ê cos(q·x)`, the operator `ν_iso ∇²g_i + ν_cub ∂_i²g_i` has these eigen-dampings, in units of `q²`:
     - `ν_iso` along an axis, for both transverse polarizations;
     - `ν_iso + ν_cub/2` along a face diagonal, polarized in the face (`ê ∝ (1, −1, 0)`);
     - `ν_iso` for the same wave polarized across the face (`ê = ẑ`).
   - So at the same `q`, `(in-face)/(across-face) = 1 + η/2`, with `η = ν_cub/ν_iso`.
8. **(b) η.**
   - **Molecular chaos** (step 4's rate), with the backflow: `η = (√3/16)/(√3/16 + ρ/(4√3) + 1/(45γρ))`.
     - `0.463` at `(0.1, 2)` and `0.480` at `(0.3, 1)`.
     - Without the backflow: `0.493` and `0.594`.
   - **Executed** (F1, F2; side 32, 12 runs):
     - axis waves give `ν_iso = 0.437 ± 0.017` (F1; F2's run with another seed: `0.448 ± 0.027`) at `(0.1, 2)` and `0.352 ± 0.011` at `(0.3, 1)`;
     - with `ν_cub = √3/16` (step 6), `η ≈ 0.24` and `0.31`;
     - the polarization ratio gives `1.16 ± 0.17` and `1.17 ± 0.11`, that is `η = 0.33 ± 0.34` and `0.35 ± 0.21`, consistent with the above.
   - **Against block 51.** Its executed wind shapes near a body (shell 6–10, sink smeared) read `η ≈ 0.3–0.5`. The executed viscosity puts `η` at the low end of that range.
9. **Estimate, not proved — what replaces step 4.**
   - Counting only the first re-draw per adjacency episode gives `ω₂ ≈ (1/2)·6ρλ·γ/(γ + λ)`: episodes form at `6ρλ`, and each is re-drawn at least once with probability `γ/(γ + λ)`.
   - That gives `ν_iso ≈ 0.388` at `(0.1, 2)` and saturation at `0.30` as `γ → ∞`.
   - The measured values are `0.448` and about `0.41`: the right mechanism and trend, about 25 % low.
   - Re-encounters of former partners, whose contents are anticorrelated by the re-draw, are the obvious missing piece. They are not computed.

## 3. Where the route fails

**Step 4.** The kinetic equation with independent partners (molecular chaos) does not describe the bond re-draw:
- the kernel is idempotent (step 2), so successive re-draws of one adjacent pair are redundant;
- the executed stress decay and viscosity (F2, F3) contradict the closure's `ω₂ = 3γρ` and its `ν_coll ∝ 1/γ`.

What survives:
- the halving identity;
- the Chapman–Enskog form and the isotropy of `ν_coll` at that order;
- the exact exchange currents (c);
- the polarization meter.

## 4. What would finish it

- A two-site kinetic theory that follows pair correlations: the `ℓ = 2` relaxation rate as half the rate of re-draws with a fresh partner. It needs the adjacency-episode statistics and the re-encounter probability of the lattice streaming. The measured target is `ω₂ ≈ 0.21` at `(0.1, 2)`, from `ν_coll = ν_iso − √3/16 − ρ/(4√3)`.
- The same test at `ρ → 0` with `γρ` fixed, to separate the density and bond-clock effects.
