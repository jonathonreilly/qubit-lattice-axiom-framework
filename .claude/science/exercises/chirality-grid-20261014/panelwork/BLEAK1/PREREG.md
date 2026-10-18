# BLEAK-1 pre-registration (written 2026-10-14 ~21:25Z, before any run)

Agent: Claude Opus 5.5 (same family as supervisor, panelists and all workers; not independent). Unrefereed.
Item: TESTS.md "Panel D work items", BLEAK-1 (branch origin/claude/chirality-grid-exercise-20261014, TESTS.md:69-76).
Inputs: gravity panelist statement §5 (panel_D/gravity/statement.md:233-253); gravity packet
`agents/C5_R19-33_report.md` (§2.1, §4.1, §5) + verdict; `C5_R19-28_report.md` + verdict; `C4_K2_report.md` + referee;
`scripts/C5/R19-33/r1933_c_decomp.py`, `r1933_cd_static_cov.py` (stress and kernel definitions re-implemented locally).

## FIXED readings (copied verbatim in substance from TESTS.md:72-76; not changed)

|δc| at a = ℓ_P with the canonical coupling:
- **LEAK-ZERO:** zero by an identity.
- **LEAK-SMALL:** below 1e-15.
- **LEAK-PLANCK:** |δc| ≥ 1e-6.
- **OPEN:** otherwise.

Mapping rule (mine, fixed now): the reading is decided by the **target** case M1 (D2 stress + spatial-TT + D2 bridge).
LEAK-ZERO needs a named identity that makes the M1 dimension-4 row vanish (a numerical ≤ 1e-12 alone is "checked", and is
reported as LEAK-ZERO only together with a named identity). If the one-loop coefficient is computed nonzero and
|δc(a = ℓ_P)| ≥ 1e-6, the reading is LEAK-PLANCK. Since at a = ℓ_P the expansion parameter G/a² = 1, I will state
explicitly that the number is a one-loop coefficient (perturbation theory not controlled at a = ℓ_P); this does not change
the reading, which is defined on the one-loop row.

## Theory (exactly R19-33's realization, scalar)

- Euclidean Z⁴, a_t = a_s = a (lattice units a = 1). Massless scalar first (m = 0); m > 0 only as a check.
  S_m = ½Σ[Σ_μ(Δ_μφ)² + m²φ²]; G(p) = 1/(ŝ(p)² + m²), ŝ_μ = 2 sin(p_μ/2).
- Stress: K2's exactly conserved symmetric stress (C4_K2_report.md:61-65), K7a placement (diagonals on sites,
  off-diagonals on face centres), Fourier transforms taken with the half-shifts so all symbols are real functions of ŝ, c = cos(p/2).
  D2: T₄₄ → T₄₄ + ¼(∇₄²φ)² (R19-33 §2.2, `r1933_cd_static_cov.py:82-84`); spatial components unchanged.
- O(κ²) matter effective action after integrating out h^TT (κ-exact Gaussian) plus the bridge exponent:
  S_int = −(κ²/2) ∫_k D(T(−k), T(k)), κ² = 8πG in R19-33's normalization (G_N = λ/2π, λ = κ²/4; R19-33 §4.2),
  i.e. the canonical κ_can² = 32πG convention gives the same S_int = −4πG∫ T·P·T/k².
- Kernels (bilinear forms on symmetric 4×4 J at lattice momentum k):
  - **foliated** D_fol = J'^TT:J^TT/ŝ² + [½J'₄₄J₄₄ − ½(J'₄₄A + A'J₄₄) + 2P'_⊥·P_⊥ + ½P'_L P_L]/q̂² (R19-33 §4.1; the bridge
    exactly as realized, applied to the actual, not-necessarily-conserved stress);
  - **covariant (pure W(B4) control kernel)** D_GR = [J':J − ½trJ' trJ]/ŝ² (de Donder / K7a symbol).
- Zero mode: k = 0 (q = 0) removed (R19-33 used zero-mode-removed K). Consequence: the tadpole contraction (⟨T⟩D(0)T) is zero
  by the prescription; equivalently it is the vacuum-gravitates term handled by (Σ)/Λ = 0. Stated as an assumption.
- One graviton loop = the exchange contraction of S_int: Σ(p) = −32πG ∫_k D_k(V(−p,p−k), V(p,k−p)) G(p−k).

## Cases

- **C0** K2 stress + D_GR. Pure W(B4) control: row must vanish by W(B4) (expected exactly, ≤ 1e-12 on a W(B4)-symmetric grid).
- **C1** K2 stress + D_fol ("the same loop with K2's exactly conserved stress"; R19-33's K2-GR realization, not RP).
  TESTS states W(B4) forces this row to zero. I will TEST that premise, not assume it: the internal matter line is off shell,
  so TT + bridge = D_GR is not guaranteed inside the loop (the identity holds on conserved sources only, R19-33 verdict item 3).
- **M1 (target)** D2 stress + D_fol (the RP realization).
- **M2** D2 stress + D_GR (diagnostic: separates vertex non-conservation from kernel foliation).
- Wilson fermion: comparator only (no RP bridge for fermions exists on record; R19-33 §8 "scalar only"). Attempted only if
  time remains, with a W(B4)-covariant point-split stress through D_fol vs D_GR; otherwise power-counted and labelled so.

## Observable

Γ(p) = G⁻¹(p) + Σ(p) = (1+δZ₄)p₄² + (1+δZ_s)p⃗² + O(p⁴). c² = Z_s/Z₄, δc = ½(δZ_s − δZ₄) at O(G).
At m = 0 the only scale is a, so δc = C·G/a² = C·(ℓ_P/a)² exactly at one loop (C a pure number); at a = ℓ_P, δc = C.
Pass scale: a*/ℓ_P = sqrt(|C|/B) for a bound B (B = 1e-15 the FIXED LEAK-SMALL line; matter-cone bounds 1e-15..1e-21 as RECALLED comparators).

## Method

1. Closed-form O(p²) extraction at m = 0: V(0,k) = 0, so Σ(p) = −32πG p_αp_β ∫_k D_k(U^α, U^β)/ŝ(k)² + O(p⁴), with
   U^α = ∂_{p1,α}V(p1, k)|_{p1=0}. (Pre-run analytic observation, to be CHECKED numerically, not assumed: D2's extra vertex
   ¼ŝ₄(p1)²ŝ₄(p2)² is O(p²) in the external leg, so it cannot enter the O(p²) row; predicted M1 = C1 and M2 = C0 at dim 4.)
2. BZ midpoint grids N = 24, 32, 48, 64, 96, 128 (offset grid, avoids k = 0 and q = 0), chunked ≤ 2^18 points per chunk;
   Richardson extrapolation in 1/N (the 1/q̂² line singularity gives an O(1/N) midpoint error).
3. Independent check of the O(p²) extraction: direct evaluation of Σ(p) at finite small p (p = δ e₁, δ e₄, δ = 0.02–0.08)
   with the full (not expanded) vertices including D2's term, finite differences, same grids.
4. Identity checks: (i) K2 Ward identity in momentum space, ŝ_μ(k)V_μν(p1,p2) ∝ EOM, at random momenta (≤ 1e-12);
   (ii) D_fol = D_GR on lattice-conserved J (reproduce R19-33's 1.8e-12); (iii) W(B4) 1↔4 invariance of C0's integrand sums.
5. Decomposition of C1 − C0 into a contact (internal-propagator-cancelled) term via the Ward identity, as an analytic
   explanation of any nonzero result (proof attempt; label as proved only if complete).

## Expectation (suggested, pre-run)

C0 = 0 (symmetry). C1 ≠ 0: the foliated kernel differs from D_GR by longitudinal (pure-gauge) pieces; contracted with the
off-shell loop vertex these give a contact term ∝ ∫(1/a²) with a frame-dependent coefficient, which in a gauge-invariant
theory is cancelled by a seagull; R19-33's realization has no seagull and K2 shows O(κ²) closure fails. M1 = C1 at dim 4.
So the expected reading is LEAK-PLANCK with |C| ~ 0.01–10 (one-loop factor times 32π·0.155).

## Budget

Memory cap 0.4 GB per run, OMP_NUM_THREADS=2, one process at a time; largest chunk ~2^18 points × ~60 float64 arrays ≈ 130 MB.
Return by ~23:10Z.
