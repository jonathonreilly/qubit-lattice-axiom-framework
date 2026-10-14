# C5 E1 report: the emergent-coarseness toy

- **Worker:** Claude Opus 5.5 probe, the same model family as the supervisor, panel F and every C5 worker. Unrefereed. Run 2026-10-14 from 01:29Z to about 01:50Z.
- **Hygiene:**
  - No repository file was edited. Nothing was downloaded, and there were no web lookups. Observational and literature numbers are the pre-registered ones or RECALLED.
  - Every run used OMP_NUM_THREADS=2, and only one ran at a time.
  - **One breach of the memory rule.** The first run of `e1_ising_tm.py` peaked at 790 MB, over the 0.5 GB cap. Onsager's double integral had allocated full 4000² arrays. I slabbed it and reran (161 MB), and the `.out` kept is from the rerun. Every other run peaked at ≤ 212 MB (`/usr/bin/time -l` records are in `scripts/*.err`).
  - No process of mine is still running.
- **Item:** `TESTS:9538-9575`. The FIXED readings are at `:9567-9574` and the expectation at `:9575`.
- **Paths:**
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`;
  - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`;
  - `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`;
  - `pF/` = `P/agents/panel_F/`;
  - `S/` = `scratchpad/C5/E1/scripts/`. Each script has its `.out`.
- **Read:**
  - `AX` in full;
  - `TESTS:9146-9575` (the C5 follow-up F1–F6, NF-1 and E1);
  - `pF/SYNTHESIS.md` and `pF/condmat_statement.md` in full;
  - `rNF1:1-140,265-273`;
  - `rF6:1-80` plus greps;
  - `rF1:1-75` and `vF1`.
- **Labels:** proved (a complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED means from memory, not verified here.

---

## 0. Plain words

**The question.** Jon's thought is that the grid's coarseness might not be fixed. It might come from the neighbour rules themselves. In many lattice systems the distance over which the grid "shows" is not the site spacing a but the correlation length ξ. Near a critical point ξ can be much larger than a, and it is set by the rules.

The toy asks two things:
- If a stretch changes the rules along one axis, does that emergent scale stretch with it, so that everything at long distance looks exactly like a relabelled (stretched) copy?
- Do particle masses stay put?

**What I found, in five sentences.**

1. **Yes, the emergent scale stretches with the rules** (checked exactly in Onsager's 2D Ising model).
   - The correlation lengths along x and along y follow the stretch.
   - After relabelling the axes, long-distance behaviour is the same in every direction.
   - The leftover direction-dependence shrinks like (a/distance)², about 0.02·(a/ξ)² in the toy.
2. **But a mass that exists only because a dial is set exactly on a critical point is pushed off that point by any stretch.**
   - The shift is set by the finest scale a, not by the coarse scale ξ.
   - In Ising the gap opens as 0.549·t²/a, whatever ξ was before the stretch. So the shift relative to the mass grows in proportion to ξ.
   - In 3D φ⁴ at one loop the critical point moves by −0.027·λ·t² (lattice units). Modes coarser than a block of b sites contribute only a fraction 0.88/b of that.
   - So making the grid "coarse" does not shield such masses. They see the finest scale.
3. **A mass that is zero because of a symmetry stays exactly zero under stretch:**
   - graphene's Dirac points, until a ~25% bond change merges them;
   - a Hubbard interaction below its threshold;
   - a Goldstone mode;
   - the staggered fermion (NF-1, counted once).

   The stretch only tilts their velocities, which acts like a metric.
4. **The toy fabric itself is not "shapeless".** A uniform stretch changes its free energy at O(t²) with a lattice-sized coefficient. Keeping the gap closed and making the stretch cost nothing are two separate conditions; one neighbour-coupling choice cannot meet both.
5. **One route does give real protection: a coarse scale that grows exponentially out of a weak coupling** (the 2D O(N) model, exact at N = ∞; the same mechanism as the QCD scale). Under stretch it shifts only in proportion to itself.
   - This is the toy version of a composite Higgs.
   - It does not help an elementary Higgs or a Wilson-type fermion, which sit at tuned points.

**Reading: MECHANISM-SPLIT (checked), as expected.** For the framework this says the following:
- Jon's idea is right about where the coarseness can come from.
- It does not by itself remove the F1/F6 hazards. Those come from tuned masses, and tuned masses feel the finest scale, wherever the coarseness comes from.
- The alternatives are a symmetry (staggered / chiral / Goldstone / composite) or a rule (P-R19-34a′ / panel F's single primitive).

---

## 1. Against the FIXED readings (`TESTS:9567-9574`), literal first

| reading | clause | status |
|---|---|---|
| **MECHANISM-SPLIT** | (a) covariant cutoff, leak ≤ O((a/r)²), checked | **Met (checked).** ξ_x/ξ_y equals the emergent-metric ratio up to −0.104·t·(a/ξ̄)² (`S/e1_ising_stretch.out:5-16`). The mass shell is isotropic in the rescaled frame up to 0.021–0.022·(a/ξ̄)² (`:20-27`). At criticality the metric-rescaled propagator has a common limit along x, y and the diagonal, with residual ∝ (a/r)² (`S/e1_ising_leak.out:3-27`) |
| | (b) tuned gaps open under stretch with a fine-scale coefficient | **Met (proved + checked).** Ising: m = 2√2K_c²t² = 0.5493t² (`e1_ising_stretch.out:31-35,41`). With ξ₀ = 10 to 1e4 before the stretch, δm/t² → 0.5493, independent of ξ₀ (`:46-49`). 3D φ⁴, one loop: δr_c = −(λ/2)·0.05429·t², UV-dominated (`e1_phi4.out:5,7-12`) |
| | (c) protected gaps stay exactly 0 | **Met (proved + checked)**, within each protecting regime. Graphene: \|f(K_D)\| ≤ 1.6e-15 below merging (`e1_graphene.out:2-12`). Hubbard: zero below U_c (`:25-33`). Goldstone: an identity (`e1_xy_fabric.out:7-10`). Staggered: NF-1 (`rNF1:139`), counted once |
| MECHANISM-FULL | (a), and tuned gaps suppressed by (a/ξ)^p, p > 0 | **Not met.** For tuned gaps p = 0: Ising δm·a → 0.5493t² as ξ₀ → ∞ (`e1_ising_stretch.out:46-49`); φ⁴ Q(m₀) = Q(0) − 0.040·m₀ (`e1_phi4.out:15-17`). The only p > 0 case is a **non-tuned** (dimensionally transmuted) gap: δln m/t² = O(1)·(1 + ln ξ), so p = 1 up to a log (`e1_onN.out:3-7`). That is outside the clause's "tuned" |
| MECHANISM-NONE | ξ_j fails to track the stretch | **Not met.** ξ_j tracks it: ln(ξ_x/ξ_y) = 1.2465·t near K_c |
| OPEN | otherwise | not needed |

**Worker reading: MECHANISM-SPLIT.**

Scope:
- Toys only: 2D Ising exact; 3D φ⁴ at one loop; 2D honeycomb with a mean-field Hubbard term; 3D XY harmonic and self-consistent harmonic; 2D O(N) at N = ∞.
- A uniform, static stretch acting through the couplings on a fixed grid.
- Mapping the toys onto the root's Higgs and fermions is a reading (§3e).

---

## 2. Setting, hypotheses and choices (stated before any title)

- **Stretch.** The sites never move (`AX:37-41`). A "stretch" is a change of nearest-neighbour couplings along one axis, which is how panel F reads strain (`pF/SYNTHESIS.md:15-16`). The axioms do not say how a physical stretch field maps onto a species' couplings: Admissibility fixes no weights (`AX:116-123`). So the **response law** K_j(t) is a choice, and I carry several:
  - linear K(1 ± t);
  - exponential K e^{±t};
  - the tuned Onsager-curve flow;
  - a symmetric linear law plus an O(t²) isotropic part k.
- **Emergent scale** = the correlation length ξ_j (exact, from the transfer matrix). **Emergent metric** = the q² coefficients of the mass-shell kernel.
- **Ising conventions.**
  - K_x is the coupling within a row and K_y the coupling between rows. Dual: tanh K* = e^{−2K}.
  - Transfer along y: cosh ε(q) = cosh2K_y*·cosh2K_x − sinh2K_y*·sinh2K_x·cos q.
  - Disordered phase: ξ_y = 1/(2(K_y* − K_x)) and ξ_x = 1/(2(K_x* − K_y)).
  - Mass-shell kernel: D(q) = cosh2K_x·cosh2K_y − sinh2K_x·cos q_x − sinh2K_y·cos q_y.
  - These are RECALLED forms. I verified them here rather than trusting memory (§3a-0).
- **"Tuned" vs "protected".**
  - Tuned: masslessness holds only on a codimension-1 surface of couplings (Ising, φ⁴ critical point; the Wilson-fermion critical mass, `pF/condmat_statement.md:56`).
  - Protected: a symmetry forbids every mass term (chiral/sublattice, the PT-type cone, U(1) Goldstone).
  - Transmuted, a third class found here: the scale is exponentially large because a coupling is marginal, with no tuning.

---

## 3. Results

### 3(a) Is the emergent cutoff covariant?

**a-0. The exact inputs, verified.**
- The row-to-row transfer matrix, built exactly on periodic strips L = 6–14, matches the free-fermion NS/R-sector formulas:
  - in its top eigenvalue and its gap, to ≤ 3.6e-15 (checked, `e1_ising_tm.out:3-28`);
  - in both phases and in both orderings of K_x and K_y.
- At L = 16 the gap equals ε(0) = 2(K_y* − K_x) up to e^{−L/ξ} (≤ 2e-6, `:30-32`).
- The 1D ε-integral free energy equals Onsager's double integral to 1e-12 off criticality (`:34-37`).

**a-1. ξ_j against the stretch (checked).**
- At fixed stretch, the exact ratio ξ_x/ξ_y equals the metric ratio √(sinh2K_x/sinh2K_y). The relative deviation is −0.0021, −0.0051 and −0.0104 (for t = 0.02, 0.05, 0.1) times (a/ξ̄)², constant from ξ̄ = 5 to 320 (`e1_ising_stretch.out:5-16`).
- So the scale tracks the stretch at O(t). Near K_c, ln(ξ_x/ξ_y) = 2K_c coth(2K_c)·t = 1.2465·t (proved by expanding the metric ratio; checked against the t = 0.02 row).
- The leak is O((a/ξ)²).

**a-2. Isotropy in every direction, not only along the axes (checked).**
- The decay rate of the mass-shell propagator along direction n is the support function of the region {κ : sinh2K_x·cosh κ_x + sinh2K_y·cosh κ_y < cosh2K_x·cosh2K_y} (proved by shifting the contour). In the frame rescaled by the exact ξ_j, its anisotropy is 0.0208–0.0224·(a/ξ̄)², at stretch ratios K_x/K_y = 1.22 and 1.86 (`:20-27`).
- The anisotropy coefficient barely depends on the stretch, so the leak is the lattice's own cubic anisotropy and is not created by the stretch.
- Cross-check: the support function along (1,1) equals −ln(sinh2K_x·sinh2K_y) to 10 digits (`e1_ising_extra.out:8-11`). That matches the RECALLED exact result that diagonal spin correlations depend only on the product (comparator). It ties the mass shell to the spin correlations off the axes.

**a-3. Leak against r/a at criticality (checked).**
- On the critical curve, stretched by u = 0, 0.3 and 0.8, I computed G(r) − G(0) of the Onsager kernel along x, y and the diagonal. I subtracted the metric-covariant form −(1/π)·ln|r′|, with |r′|² = 2(x²/sinh2K_x + y²/sinh2K_y).
- All three directions converge to one constant. The residual differences scale as n^{−2}, with n²Δ → 0.040 (u = 0), 0.051–0.072 (u = 0.3) and 0.19–0.20 (u = 0.8) (`e1_ising_leak.out:3-27`).
- **Scope:** this is the free-fermion kernel. Spin correlations at criticality off the axes were not computed directly.

**Reading.** The emergent scale is a covariant cutoff for one species, with leak O((a/r)²). That is the MECHANISM-SPLIT (a) clause.

**Caveat (reading; checked numbers):** the metric is per species.
- Under the same coupling stretch K(1 ± t), the Ising fabric's metric anisotropy is ln(ξ_x/ξ_y) = 1.2465·t.
- An XY Goldstone's is ln(v_x/v_y) ≈ t (`e1_xy_fabric.out:11-12`).
- Two species on one fabric see different metrics unless their stretch responses are matched. This is the Collins et al. 2004 issue (comparator, RECALLED) and panel F's companion light-cone clause C3 (`pF/SYNTHESIS.md:78`), counted once.

### 3(b) Tuned gaps under stretch

**b-1. Ising at K_c (proved + checked).**
- With the linear stretch, sinh2K_x·sinh2K_y = 1 − sinh²(2K_c t) < 1. So any stretch moves the fabric off criticality at O(t²) (proved by sinh(a+b)·sinh(a−b) = sinh²a − sinh²b).
- With g(K) = K*, g′(K_c) = −1 and g″(K_c) = 2√2: K_y* − K_x = √2K_c²t² + O(t³). So m = 1/ξ = 2√2K_c²t² = 0.549294t² (proved).
- Checked to 7 digits at t = 1e-3 (`e1_ising_stretch.out:31-35,41`).
- The scaling is |t|^{2ν} with ν = 1.
- The exponential law K e^{±t} goes to the ordered side instead: K_y* − K_x = K_c(√2K_c − 1)t², so m = 0.6642t² (`:36-40,42`). The sign depends on the response law; the size is O(1) in lattice units either way.
- **Mean field never sees this (proved).** Its critical condition depends only on K_x + K_y, which a traceless linear stretch leaves fixed. The shift is a fluctuation effect.

**b-2. Fine scale or ξ? (checked).**
- Start off criticality with ξ₀ = 10, 100, 1e3 and 1e4. Then δm/t² = 0.5267, 0.5470, 0.5491 and 0.5493 → 2√2K_c² (`:46-49`).
- The absolute shift is set by a, and **the relative shift δm/m₀ = 0.549·ξ₀·t² grows with ξ₀**. So p = 0, and coarseness gives no protection.

**b-3. The only way to keep the gap: tune the response law (proved + checked).**
- The flow sinh2K_x = s·e^{u}, sinh2K_y = s·e^{−u} keeps sinh2K_x·sinh2K_y = s² exactly. So at s = 1 it is gapless at every u (`:52-54`).
- Off criticality it shifts the gap only multiplicatively, by −2.2% at u = 0.3 for s = 0.999 (`:55-60`; analytic D(0) = (1−s)²[1 − u²s/(1+s²)] + O(u⁴)).
- With K_x = K_c(1+t), staying critical needs K_y = K_c(1 − t + √2K_c t² + …). That is one number per order (0.62323 at O(t²), `:62-64`): the Ising image of P-R19-34a, a rule rather than a mechanism.

**b-4. 3D lattice φ⁴, one loop (proved + checked).** The setup: m² = r + (λ/2)·I, I = ⟨1/(m² + Σ(1+t_j)e_j)⟩, with E_g stretch t = (t, −t, 0).
- The tree-level and mean-field critical point is unchanged, because ΣJ_j is fixed (proved).
- The first order vanishes by the x ↔ y symmetry.
- I(t) = I(0) + Q·t² with Q = ⟨(e₁ − e₂)²/E³⟩ = 0.054286, extrapolated from N = 128, 256 and 512. The control I(0) = 0.252731 matches the Watson integral ⟨1/E⟩ (RECALLED) to 6 digits (`e1_phi4.out:1-5`).
- So δr_c = −0.02714·λ·t² in lattice units, with λ of dimension 1/a in 3D (`:12`).
- **Composite/block version.**
  - The part of Q from modes inside the block zone |q_j| < π/b is 0.0479/b: share 0.46, 0.22, 0.11, 0.055 and 0.028 for b = 2, 4, 8, 16 and 32 (`:7-11`).
  - The rest comes from fine modes.
  - The block-averaged field's critical point is the fine field's (block averaging is linear and does not change exponential decay; proved). So the shift is set by the fine scale. In coarse units (ℓ = b·a) it is b times the coarse-lattice estimate.
- **Off criticality:** Q(m₀) = Q(0) − 0.040·m₀ for ξ₀ = 3.3–33 (`:15-17`), so p = 0 again. The ξ₀ = 100 row is grid-limited at N = 512.
- **Continuum check (proved).** In the continuum the t² coefficient goes as ∫dq, a linear UV divergence, so it is dominated by the cutoff.
- With a **covariantly stretched** cutoff (the region Σ(1+t_j)q_j² < Λ²), I(t) = Π(1+t_j)^{−1/2}·I(0). That is exactly zero for a volume-preserving stretch.
- So full protection would need a cutoff that moves exactly with the metric at the cutoff scale. The emergent cutoff of (a) is covariant only where r ≫ a, and the loop is dominated by r ~ a.

**b-5. Comparator class: a transmuted coarse scale (checked; exact at N = ∞).**
- In the 2D lattice O(N) sigma model, ξ = a·exp(O(1/g²)) with no tuned point.
- At fixed g², the stretch gives δln m/t² = 1.50, 2.67, 3.82, 4.97 and 6.12 for ξ₀ = 10 to 1e5 (linear law). That is (1/2)·ln ξ₀ + 0.35: the continuum Jacobian √(J_xJ_y) acting on 1/g².
- With the volume-preserving law it is −0.250, constant (`e1_onN.out:3-7`; the ξ₀ = 1e5 row carries a quadrature roundoff warning).
- **The shift is multiplicative.** The absolute shift falls like (a/ξ₀)·log.
- This is the toy image of panel F's "mass-proportional channels are safe" (`pF/condmat_statement.md:253-260`) and of a strong-sector scale (the QCD-like Λ).

### 3(c) Protected gaps under stretch

**c-1. Graphene (proved + checked).**
- f(k) = Σ_j t_j·e^{ik·d_j} vanishes somewhere ⇔ t₁ + t₂e^{iα} + t₃e^{iβ} = 0 has a solution ⇔ the three hoppings close a triangle (proved). The gap is therefore exactly 0 until merging (t₁ = t₂ + t₃; u = 1/4 for (1+2u, 1−u, 1−u)), and 2(t₁ − t₂ − t₃) beyond it.
- Checked: |f(K_D)| ≤ 1.6e-15 at u from −0.4 to 0.249 and for 200 random traceless strains with |s| ≤ 0.3. Gaps 0.08 and 0.40 at u = 0.26 and 0.30 match exactly (`e1_graphene.out:2-12`).
- **The velocities track the strain like a metric:**
  - ln(v_max/v_min) = 4.02u at small u;
  - v₁v₂ changes only at O(u²);
  - the Dirac point moves linearly in u, which is the strain pseudo-gauge field (`:15-21`; isotropic v = 3/2 is the textbook 3ta/2, RECALLED).
- Adding next-nearest hopping keeps the touching, because H = t′g(k)·1 + offdiag(f) has bands t′g ± |f| (proved).

**c-2. Hubbard interaction (proved + checked).**
- The bipartite particle-hole map c_{iσ} → ε_i·c†_{iσ} is a symmetry at half filling. It makes both the CDW mass Σε_i n_i and the AF mass Σε_i S^z_i odd. So no mass is generated at any order of perturbation theory (proved, standard).
- A mass needs spontaneous breaking above a finite threshold.
- Mean field: 1/U_c = ⟨1/(2|f|)⟩. I evaluated it with a closed-form elliptic-K inner integral (checked against brute force, `:24`).
- Results: U_c = 2.2311t isotropic (comparator: the MF literature value 2.23t, RECALLED), falling to 2.1539t at u = 0.249 and 1.863t at u = −0.4 (`:25-33`).
- For U < U_c(u) the gap equation's right side is monotone, so Δ = 0 is the only solution (proved).
- So protection is a property of a phase, with an O(1) margin. Strain of order 1e-21 does nothing.

**c-3. 3D staggered:** NF-1. Σ(0,0) = 0 by (Θ, P_stag) at every strain channel and order (`rNF1:139-141`; `TESTS:9493-9511`). Counted once; not rerun.

**c-4. Goldstone (proved + checked).**
- H depends on θ only through differences, so the quadratic form after any number of loops is Σ_j ρ_j·e_j(q). It vanishes at q = 0 identically.
- Harmonic sum rule: Σ_j J_j W_j = 1 (to 1e-12, `e1_xy_fabric.out:2-5`).
- Self-consistent harmonic stiffness at T = 0.5: ln(ρ_x/ρ_y) = 1.023·ln(J_x/J_y) (`:7-10`).
- The stiffness tensor is the Goldstone's metric, and it tracks the stretch.

### 3(d) The fabric's own uniform-stretch mode

**d-1. Ising at K_c (checked; one sign proved).**
- d²lnZ/dt² per site:
  - +0.10618 (linear law);
  - +0.72939 (exponential);
  - +0.31831 (along the Onsager flow, per u²) (`e1_ising_stretch.out:67-69`).
- These are not zero, and they are O(1) in lattice units.
- For the linear law, lnZ is convex in (K_x, K_y), so d²lnZ/dt² = K²·Var(E_x − E_y) ≥ 0 (proved).
- So with these response laws the isotropic fabric is a **maximum** of the free energy along the stretch (negative stiffness).
- The singular part ∝ τ²·ln τ with τ ∝ t² enters only at O(t⁴·ln t), so the O(t²) term is the lattice-scale regular part (proved).

**d-2. Gap-keeping and shape-free are two separate conditions (checked).**
- In the symmetric family K_x,y = K_c(1 ± t + k·t²):
  - the gap stays closed at k_gap = √2K_c/2 = 0.31161, and then d²lnZ/dt² = +0.49454;
  - the stretch costs nothing at k_stiff = −0.0852, and then (K_y* − K_x)/t² ≠ 0 (`e1_ising_extra.out:1-5`).
- With nearest-neighbour couplings only, one choice cannot meet both. That is two numbers per order: the toy images of P-R19-34a (mass) and (Σ)/(S\*) (vacuum stiffness), counted once with F5's knock-on.

**d-3. Graphene band energy (checked; sign proved).**
- E(u) = −2⟨|f|⟩ per cell, E(0) = −3.149194 (comparator: 1.5746 per spin per cell, RECALLED).
- d²E/du² = −6.688t per cell (`e1_xy_fabric.out:15-18`).
- |f| is convex in the hoppings, so E is concave: again negative stiffness (proved).

**Reading.** The fabric has no shape-free direction. A uniform stretch costs (here gains) lattice-scale free energy at O(t²). Its sign depends on the response law, and a zero needs its own tuning.

### 3(e) Implications (reading / suggested / comparator)

- **Higgs (tuned scalar):** class (b).
  - The toy predicts a nonzero, fine-scale strain coefficient for its mass², independent of any emergent coarseness. That is consistent with F6's c_H ≈ +3.7e-3 on the root's law (`rF6:13-22`), counted once.
  - Emergent coarseness alone does not remove F6's clock and Earth rows.
- **Wilson fermion (tuned critical mass, `pF/condmat_statement.md:56`):** class (b). Consistent with F1's +2.42e-2 e² (`TESTS:9220,9226`), counted once.
- **Staggered fermion:** class (c). Consistent with NF-1, with its taste wall, counted once.
- **A protected Higgs needs the class-(c)/(b-5) route.**
  - A pseudo-Goldstone (composite) Higgs has its mass generated below a strong scale Λ. Λ arises by dimensional transmutation, which the b-5 toy shows shifts multiplicatively.
  - Suggested size: transferring F6's coefficient with Λ in place of 1/a, |c_H,eff| = 3.7e-3·(Λℓ_P)². For Λ = 10 TeV that is 2.5e-33, against the clock-row requirement ≲ 1.4e-21 (`rF6:34,231`): a margin of about 5.6e11.
  - Conditional on: the strong sector's own strain response being multiplicative, as in b-5; a = ℓ_P; F6's estimator.
  - It does **not** cover F6's Wilson-condensate tadpole (`rF6:23`) or F1's elementary-fermion channel. Those need staggered/chiral fermions or the rule.
  - Comparator, RECALLED: Kaplan–Georgi composite Higgs; LHC limits f ≳ 1 TeV.
- **Jon's hypothesis, as tested.**
  - Supported in part: coarseness can be a feature of the neighbour rules, and it stretches covariantly (a).
  - Not supported as a protection: what masses feel under stretch is set by the finest scale where the rules act (b), unless a symmetry protects the mass (c) or the mass is tied to a transmuted scale (b-5).
  - If the fabric's coarse scale were set by nearness to a critical point, that scale would itself shift at fine-scale strength (b-2).

---

## 4. Prior art (counted once)

- F1/vF1 (the Wilson additive-mass Hessian, OPEN on the lift);
- F5 (the knock-on);
- F6 (c_H, SCALAR-HAZARD, unrefereed);
- NF-1 (staggered zero, taste wall, unrefereed);
- panel F (`SYNTHESIS.md:78,81-89`; `condmat_statement.md:56,113-134,253-260`).

Comparators, RECALLED:
- Onsager and Schultz–Mattis–Lieb (verified here);
- the McCoy–Wu diagonal-correlation dependence on the product (consistent here);
- Watson's integral (consistent);
- graphene strain and Dirac-point merging (Pereira–Castro Neto–Peres), with the triangle criterion proved here;
- honeycomb Hubbard MF U_c ≈ 2.23t (consistent);
- Collins et al. 2004;
- Kaplan–Georgi.

No result here changes any C5 number.

## 5. Not computed

- Spin–spin correlations at criticality off the axes (I used the Onsager kernel; the off-axis link to spins is a comparator).
- A 3D Ising exact fabric (only 3D φ⁴ at one loop; true ν = 0.63 would give m ∝ |t|^{1.26}, RECALLED).
- 4D φ⁴ (the comparator says it is quadratically sensitive).
- Dynamics, gauge fields, non-uniform stretch, gravity feedback.
- How a physical stretch field fixes each species' response law.
- QMC beyond mean field for Hubbard (U_c ≈ 3.8t, RECALLED).

## 6. Expectation (`TESTS:9575`) against outcome

**Borne out.**
- Covariant emergent cutoff: yes.
- Tuned points move under stretch (Onsager's curve): yes, with a fine-scale coefficient and p = 0.
- The Higgs needs protection or a rule: yes.
- A pseudo-Goldstone/composite Higgs is the protected-route candidate: yes, sharpened by the transmuted-scale toy (b-5).

**Additions not in the expectation:**
- (i) the metric is per species (a, caveat);
- (ii) a gap-keeping response and a shape-free fabric are separate conditions (d-2);
- (iii) the fabric's stretch stiffness was negative for every response law tested (d-1, d-3).

## Files

All in `scratchpad/C5/E1/scripts/` (each with `.out` and `.err`):
- `e1_ising_tm.py`: transfer-matrix verification;
- `e1_ising_stretch.py`: a1, a2, b1–b3, d1;
- `e1_ising_leak.py`: a3;
- `e1_ising_extra.py`: d2, a4;
- `e1_phi4.py`: b4;
- `e1_onN.py`: b5;
- `e1_graphene.py`: c1, c2;
- `e1_xy_fabric.py`: c4, d3.
