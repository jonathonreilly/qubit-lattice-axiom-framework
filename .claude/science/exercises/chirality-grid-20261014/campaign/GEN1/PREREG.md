# GEN-1 PREREG: generation placement (X2′)

Written 2026-10-17 11:37Z (from `date -u`), before any run. Worker: Claude Opus 5.5 (same family as supervisor, panel E and OBS-2..4/CLS-1 workers; not independent). Cap 0.4 GB via `scripts/capped.sh`, one process at a time. Deadline 17:30Z.

Readings are FIXED by TESTS.md "Campaign wave 3" (CH/TESTS.md:648-668) and are copied, not changed:
- **GEN-CONE(n):** a1–a5 hold and n ≤ 8.
- **GEN-PRICE(n):** a1–a5 hold, but n > 8 or a non-covariant structure is needed.
- **GEN-NO-GAIN:** any of a1–a3 fails.
- **OPEN:** otherwise.

## Object (X2′, panel_E/strategy/statement.md:42-53)

Continuous time, Z³, fermion statistics supplied. ψ(x) ∈ C²(walker spinor) ⊗ C¹⁶(Spin(10)) ⊗ C³(generation, internal; lattice symmetries act trivially on it). 96 complex modes per site.

H = Σ ψ†σ_a sin p_a ψ + W·Q(ψ_S) + H_Yuk + G_SM links, with
- ψ_S = F_Γ ψ, F_Γ = f_Γ(p) ⊗ 1₂ ⊗ 1₁₆ ⊗ 1₃, f_Γ(p) = (3 − Σ_a cos p_a)/2 (7-site star; any positive multiple equivalent);
- Q: X2's Spin(10)-singlet filtered quartic (CH/combos/X2/COMBO_REPORT.md:68), generation structure flavour-blind;
- H_Yuk: on-site, G_SM-covariant, one k = 0 Higgs doublet (nearest-neighbour lattice scalar), law-level 3×3 complex Y_u, Y_d, Y_e (Y_ν Dirac); fit to PDG masses and CKM.
- Light: 3×16 Weyl at Γ (one chirality). Mirror: the 7 corners ≠ Γ, ×16×3.
- Comparator: X2-corner numbers (OBS-2/3/4, CLS-1 REPORTs and referee verdicts).

## Items and operational criteria ("holds" = the panel's predicted outcome)

- **(a1) holds** iff exact translations + one k = 0 Higgs permit arbitrary complex Y_u, Y_d (proof), and a constructed pair reproduces the PDG 2024 inputs used by OBS-3 (`OBS3/scripts/obs3_core.py:162-167`) — 6 masses, all |V_ij| and J — to relative error ≤ 1e-10 (check). Fails if any translation or cubic selection rule restricts generation indices.
- **(a2) holds** iff (L1) the Γ label sector has net index 3 per component with one chirality and no translation-invariant Spin(10)×Z₄^F-allowed bilinear gaps it (proof), and (L2) [H_W + W·Q, ψ(Γ)] = 0 (proof) with: f_Γ = 0 only at Γ (41³ grid: min |f_Γ| at distance > 0.3 from Γ is > 0); f_Γ A1g (24 spin-lifted rotations and 3 translations, commutators ≤ 1e-12 at L = 4); Fock check (L = 2, X2's T2 code with f_Γ): |[H, ψ(Γ)]| ≤ 1e-10 while mirror corners and the unfiltered control give ≥ 1e-2. Fails if any of these fails.
- **(a3) holds** iff (i) the cyclic Z₁₆ gate passes for every g·i^F (g ∈ Z₂³) with ν_R (d = 16), recording whether d = 15 fails (ν_R forced, as in X2 — that is the X2 price, not a failure); and (ii) the mixed Z₂³ × Spin-Z₄ anomaly of the 7-corner mirror vanishes. (ii) is to be decided by an argument (exponent bound on Ω₅^{Spin×Z₂Z₄}(BZ₂³) from the AHSS, using comparator values of Ω_q^{Spin-Z₄}(pt), q ≤ 5), plus a Spin(10)-instanton 't Hooft-vertex check for mixed Z₂³/Z₄^F–Spin(10)² classes. If the argument cannot be closed, (a3) is undecided → OPEN. Classes mixing Z₂³ with Spin(10) beyond the 't Hooft vertex will be listed as not computed.
- **(a4) holds** iff no first-order traceless-strain (E_g ⊕ T₂g) shift of any Γ mode's rest energy is symmetry-allowed for arbitrary flavour data (proof by little-group representation theory; check by characters over the 24-element spin lift).
- **(a5) holds** iff no tree-level ΔF = 2 operator at dimension 6 arises beyond the SM's (proof: one doublet ⇒ Higgs couplings ∝ M; momentum-conservation argument for mirror and lattice-scale modes). Higher-dimension remnants are estimated (suggested).
- **(b)** The one-loop dimension-4 Yukawa-induced Lorentz-violating speed residual at Γ, after the per-field universal (flavour-blind) speed counterterm — one per Weyl field Q, u^c, d^c, L, e^c, ν^c, chosen to minimise the worst clean-row ratio — on the clean D44 rows (u: c̊ > −3e-23, |d̊| < 3e-23; d: c̊ > −1e-22, |d̊| < 1e-22, as printed; OBS3/scripts/obs3_core.py:172) and the electron rows (obs3_core.py:173). Conventions from obs3_core.py:5-13 (c̊ = −(δv_L + δv_R)/2, d̊ = −(δv_L − δv_R)/2, c_TT = ¾c̊).
  - **Kernel:** OBS-2's one-loop Brillouin–Wigner model (`OBS2/scripts/yuk_lv.py:1-18`) evaluated at Γ, with the mirror proxy m(k) = m0 + Δ·f_Γ(k) (vanishes only at Γ; Δ ∈ {0, 0.5}); vertices on-site and with a Γ-selective flavour-universal symbol g_Γ(k) = (1 + Σ cos k_a)/4 in sym/int/ext placements; N ∈ {48, 96}; m0 = mH ∈ {0.1, 0.05, 0.025}. κ_Γ = B_a + S1.
  - **n (counting rule, fixed now):** the number of independent linear flavour-covariant structures — Hermitian flavour matrices linear in one spurion from {H_u = Y_uY_u†, H_d on Q; Y_u†Y_u on u^c; Y_d†Y_d on d^c; H_e, H_ν on L; Y_e†Y_e on e^c; Y_ν†Y_ν on ν^c} — whose coefficients must be set, beyond the per-field universal counterterms, to bring every clean row within bound. Counted in the spurion basis (the one-loop equality of coefficients is reported separately as n_min). Also reported: n_all, the number needed to remove all one-loop flavour-pattern LV in every field.
  - **Tuning:** required relative precision of each counterterm coefficient against κ_Γ.
  - A structure is "non-covariant" if it needs a flavour matrix not built from the law's Yukawas, or a cubic-anisotropic (non-A1) tensor.

## Controls (must pass before readings)
- C1: at Δ = 0, on-site vertex, my kernel reproduces OBS-2's archived 'o' corner table (`OBS3/scripts/tables/yuk_kin_N*_m*_D0.0_*.json`, pair '00') to ≤ 1e-9 relative.
- C2: B at Γ isotropic (B_x = B_y = B_z to ≤ 1e-10 relative); the identity (a-type) component of Σ₀ at Γ is zero to roundoff.
- C3: residual rows independent of the unphysical generation basis (random right-handed rotations and random W_u with W_d = W_u V) to ≤ 1e-12 relative.

## Error type
Systematic bracket (N, regulator, Δ, vertex variant, Yukawa scale ×1 and ×0.45); no statistical error. Inputs recalled (PDG 2024 as in OBS-3), not fetched.

## Memory estimate
Kernel: per slab N² = 9216 points × ~20 arrays → < 50 MB. Fock check: 16 modes, sectors ≤ C(16,4) = 1820; X2's identical code peaked at 238 MB. Anomaly/representation checks: trivial.
