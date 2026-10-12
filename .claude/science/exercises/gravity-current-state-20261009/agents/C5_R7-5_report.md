# C5 R7-5 report: loops in box-confined Poincaré (does a pair-creating box field theory feed Lorentz violation into the infrared?)

**Author.** Claude Opus 5.5 probe. Same family as the supervisor, R7-1's worker and every C5 worker. Unrefereed. 2026-10-12, 15:17Z to about 15:50Z. No repository file edited.

**Scratch.** `S/` = `.../scratchpad/C5/R7-5/`. Scripts and outputs (each runs in under 15 s with `OMP_NUM_THREADS=2`):
- `S/scripts/r75_oneloop.{py,out}`: d = 3 one-loop speed coefficients for classes P, FF and INV, plus the Collins comparator.
- `S/scripts/r75_extra.{py,out}`: a scan of class-P shapes, and the INV fermion-loop check.
- `S/scripts/r75_bt_production.{py,out}`: d = 1 exact diagonalisation of the BT pair-creation law, against instant-form comparators.
- `S/scripts/r75_bt3d.{py,out}`: d = 3 check of the BT pair-creation law.

**What I read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`:
  - `:2302-2440`: C5 method and round 1;
  - `:3009-3060`, `:3240-3394`: rounds 6 and 7; R7-5 is at `:3375-3386`;
  - `:3396-3407`: the R7-1 referee result;
  - `:1-86`: T0 and T1;
  - `:1295-1311`, `:1377-1395`, `:1438-1442`, `:1527-1548`: lanes RF and RE, and the F2/E1/E2 results;
  - `:2030-2056`: X1.
- `SUMMARY.md:105-120`, `:418-435`.
- `agents/C4_F2_referee.md`, `agents/C4_E1_referee.md`, `agents/C4_E2_referee.md`, `agents/C5_O1_referee.md`.
- The R7-1 report and scripts, and `ref_R7-1/R7-1_referee_verdict.md`.

**Labels.** proved / checked (numerics here) / suggested / reading / comparator (V = verified on the web this session; R = recalled, not verified).

---

## 0. In plain words

- **The answer depends on how the interaction is built.** There are three answers, one for each class of vertex.
- **1. Point vertices, or form factors fixed in the lattice frame: O(1)·g², unsuppressed.** This holds even though every particle's free dispersion is exactly relativistic inside the box (classes P and FF).
  - Loop momenta reach the box edge.
  - The speed shift is δc² = (g²/16π²)·XI, with XI = 1.0 to 7.0 for point vertices (eleven shapes) and XI ≈ 11 for a box form factor.
  - XI does not depend on the box or form-factor scale. This is the Collins et al. mechanism, which I reproduced to 1e-3 as a code check.
  - A dimensionful (super-renormalizable) coupling is suppressed instead by (g/Λ)², times a log.
  - The box therefore does not protect loops of a local field theory.
- **2. Vertices that are Lorentz-invariant functions of the invariant mass of the pair they create, with compact support below the box edge: exactly zero at one loop.** This class (INV) includes vacuum pair creation (Z-graphs).
  - Every LV Taylor coefficient, dimension 4 included, vanishes for external momenta inside a stated budget.
  - Proved for scalar and for Dirac–Yukawa loops; checked to 1e-13 in the continuum and to 1e-8 on the lattice (quadrature-limited).
- **3. A Bakamjian–Thomas "mass operator" law with pair creation: exactly zero at every order in g, for the dressed one-particle sector** (class BT).
  - The interaction acts only on rest-frame variables, so E² − P² of the dressed particle is the same at every lattice momentum on the plateau.
  - Checked: d = 1 exact diagonalisation, spread 1e-14 while the mass² moves from 0.25 to 0.029; d = 3, spread falling 1.3e-4 → 4e-6 with L.
  - The naive instant-form vertex with the same invariant form factor but no Z-graph violates Lorentz invariance at O(g²) (spread 1e-2 at g = 0.3).
- **What this means.** Collins-type loop leakage is not forced by the box itself. It is forced by any part of the dynamics that sees the lattice frame. A box law keeps one light cone through loops only if every vertex is a Lorentz-invariant, compactly supported function of rest-frame (invariant-mass) variables at a scale below the box edge.
  - That is Lorentz invariance *put in* through the choice of dynamics. It is not derived from the lattice. Polchinski's objection applies verbatim (§6).
- **Not shown:**
  - gauge fields (QED's 8.55e-3 split lives there);
  - two loops in class INV;
  - multi-cluster sectors for BT (R7-6);
  - microcausality;
  - gravity.
- **Against the FIXED readings: PASS (worker reading), in the scope of §7.** Classes P and FF are a bounded O(g²/16π²) FAIL-type result *for those classes*. They are not the registered reading and need the referee if recorded.

---

## 1. Hypotheses and classes (stated before any title)

**H-lat.** Z³ × ℝ (continuous time). Box dispersions as in R7-1 (`R7-1_report.md:63-71`):
- for Dirac fields, s(k) = k on |k_i| ≤ b₁, bent smoothly to sin k by b₂, plus a Wilson term W(k) = r Σ_i (1 − ρ(k_i))(1 − cos k_i) that vanishes in the box;
- for scalars, either ε̃² = m² + Σ_i w(k_i), with w = k² in the box and w ≥ b₁² outside (doubler-free), or R7-1's s(k) with an explicit leg cutoff.

**H-pert.** "One loop" means O(g²) in the self-energy of a field. "IR dimension-4 LV" means δc² = ∂²Π/∂p₀² + ∂²Π/∂p₁² at p = 0, in the units of Collins et al.:
- c² = 1 + ξ/2;
- reported as δc² = (g²/16π²)·XI.

**Classes of interaction.**
- **P.** Local point vertex: a Yukawa g φψ̄ψ, or a scalar g φχ†χ, with constant vertex in lattice momenta. The loop runs over the whole Brillouin zone.
- **FF.** A frame-fixed form factor χ(k)χ(k+p) in lattice momenta, smooth, equal to 1 on an inner box, with support inside the relativistic box. Every propagator the loop sees is then exactly relativistic.
- **INV.** An instant-form Hamiltonian H = H₀ + V on Fock space with:
  - all operator orderings (φ ↔ χχ̄, vacuum ↔ φχχ̄, χ ↔ χφ, …);
  - each term carrying relativistic normalisation 1/√(8ωE₁E₂) and a form factor F(M²) of the on-shell invariant mass of the pair the term creates or absorbs;
  - F C^∞, with plateau Λ₁ and support Λ₂.
  - The vacuum ↔ three-particle term carries the product F(M₁₂²)F(M₁₃²)F(M₂₃²) (§3.3).
- **BT.** A Bakamjian–Thomas mass-squared law with particle production on the sector {φ} ⊕ {χχ̄} at each lattice momentum P on a plateau:
  - M² = M₀² + U, with U = 1_P ⊗ u acting on rest-frame variables only (s-wave F(|q|));
  - H = √(M² + P²);
  - the vacuum is inert.
  - This is the relativistic Lee model in the class of Polyzou (comparator V).

**Excluded, not addressed:**
- gauge fields;
- Z⁴ / set B;
- LRL;
- gravity and Ward identities;
- two-loop INV;
- multi-cluster BT sectors (R7-6);
- microcausality and crossing;
- graviton loops.

## 2. Prior art (each counted once)

- **T1 (refereed).**
  - On fixed Z³ with continuous time, a smooth Collins-shaped regulator gives "a finite, cutoff-scale-independent and regulator-shape-dependent O(g²/16π²) fermion–scalar speed split". Δ = −0.696 at r = 1, and +0.61 / −1.55 at r = 0.5 / 2; nearest-neighbour Δ = −2.50; Z⁴ gives 0 by symmetry (`TESTS.md:42-82`).
  - Its referee's open door: T1 "does **not** establish ... that every smooth spatial regulator with continuous time lacks a protected light cone" (`TESTS.md:86`).
  - **Classes P and FF here are new instances of T1's mechanism with a box-exact dispersion. Classes INV and BT walk through T1's open door.**
- **T0 / R3 surface-term lemma.** "A fixed label-space window gives [a nonzero TT term] ... A proper-space window gives 0" (`TESTS.md:11-15`; `agents/R3_price.md:13`). This is the same structural fact one level up. A frame-fixed window in loop momentum leaves a surface term. A window defined by Lorentz-invariant kinematics does not. §3.4 finds the analogue for speeds.
- **F2 / E2 (refereed).** Naive/staggered QED on Z³ × ℝ gives c_e − c_γ = −8.55e-3 (Δ = −14.72·e²/16π²). That needs one counterterm tuned to about 3e-17, and the running is too slow (`SUMMARY.md:423`; `C4_F2_referee.md:60-62`; `TESTS.md:1439,1542`).
- **O1 referee.** The Collins argument is "a radiative-naturalness argument, not a no-go" (`PRICE_NOTE.md:142`). It gives a severe regulator-specific matter naturalness problem, not a universal necessity theorem (`C5_O1_referee.md:99-101`).
- **Lane RE (E1/E2, refereed).** IR attraction of relative speeds exists at strongly coupled fixed points, but SM running is far too slow (`TESTS.md:1527-1548`). Not used here.
- **R7-1 (CONFIRMED WITH CORRECTIONS, PASS WITH SCOPE).**
  - Free P1 is exact on compactly supported box wavefunctions.
  - P2 (two-body BT) is defective as written (boost sign, ¼ prefactor) but repairable in 1D.
  - "A rotationally invariant channel is still needed for d ≥ 2" (`TESTS.md:3396-3407`).
  - The BT law here uses an s-wave F(|q|) and checks only the dressed dispersion H. It does not use P2's boost formula.
- **X1.** Collider bounds on matter non-locality with exponential form factors: ℓ < 7.9e-20 m (LHC Drell–Yan) (`TESTS.md:2050-2056`). That constrains Λ_F ≳ few TeV for any non-local vertex scale.
- **Literature.**
  - **Collins–Perez–Sudarsky–Urrutia–Vucetich, PRL 93, 191301 (2004), gr-qc/0403053 (V).** Yukawa theory; f(|k|/Λ) on the fermion propagators; ξ = (g²/6π²)[1 + 2∫₀^∞ x f′(x)² dx]; "of order the square of the coupling independently of Λ".
  - **Polchinski, the comment on Gambini–Rastgoo–Pullin, arXiv:1106.6346 (V).** The prompt's "1109.3990" is a different paper (Sharif–Waheed, on colliding plane waves).
    - Dimension-4 LV is O(1)·couplings unless forbidden (supersymmetry is "the one known example").
    - GRP's m⁴/M⁴ suppression is "put in by hand".
    - Loops in *other* fields reproduce Collins et al.
  - **Gambini–Rastgoo–Pullin, CQG 28, 155005 (2011), arXiv:1106.1417 (V, abstract only).**
  - **Belenchia–Gambassi–Liberati, "Lorentz violation naturalness revisited", JHEP 1606:049 (2016), arXiv:1601.06700 (V, abstract).** A separation between the EFT validity scale and the LV scale hinders percolation in Yukawa. The suppression power is not in the abstract, so it is not verified here (R: (Λ/M)²).
  - **Polyzou, "Relativistic quantum mechanics: particle production and cluster properties", PRC 68, 015202 (2003), nucl-th/0302023 (V, abstract).** Poincaré-invariant models with particle production, cluster properties and the spectral condition, "limited to systems with a bounded number of bare-particle degrees of freedom". The class includes the relativistic Lee model.
  - **Keister–Polyzou, arXiv:1109.6575 (cited by the R7-1 referee).** Naive BT cluster failure for N ≥ 3.
  - **Terning (1991), gauging non-local Lagrangians with path-ordered links (R).**

## 3. Results

### 3.1 Code check against the comparator: checked

Continuum Dirac loop with f(|k|/Λ) on each propagator, m/Λ = 0.005 (`r75_oneloop.out:2-7`):

| f | ∫x f′² | XI (here) | Collins (4/3)(1 + 2∫x f′²) |
|---|---|---|---|
| e^{−x²} | 0.5 | 2.6646 | 2.6667 |
| (1+x²)^{−2} | 0.4 | 2.3963 | 2.4000 |
| e^{−x⁴} | 1.0 | 3.9996 | 4.0000 |

- The sign, the normalisation and the Λ-independence all agree. The residual is O(m/Λ).
- In T1's units (δc rather than δc²): 16π²δc = XI/2 = 1.332, the same as T1's 1.3304 (`TESTS.md:46`).

### 3.2 Class P (point Yukawa vertex, R7-1 box dispersion): O(g²/16π²), unsuppressed — checked

Method.
- Euclidean, with the k₀ integral in closed form.
- A partition of unity in the loop momentum: an inner sphere (radius r₂ < b₁) done exactly in spherical coordinates, where the integrand is the continuum one; the outer region on a 3D BZ grid.
- J_ww analytic; J_pp from a Cauchy contour (inner) or Richardson differences (outer).

Results (`r75_oneloop.out:13-24`; `r75_extra.out:2-7`):

| m (b₁ = 2, b₂ = 3, r = 1, N = 128) | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 |
|---|---|---|---|---|---|
| XI_P | 2.19 | 1.94 | 1.82 | 1.74 | 1.72 |

- **Limit.** The trend is roughly linear in m: Wilson-type masses break chirality. It extrapolates to XI_P(m → 0) ≈ 1.70.
- **Resolution.** N = 96 / 128 / 160 give 1.732 / 1.741 / 1.743.
- **Shapes.** Over eleven shapes ((b₁, b₂, r) varied, `r75_oneloop.out:20-24`, `r75_extra.out:2-7`), XI_P ranges from 0.98 to 6.97.
  - No zero was found in this scan.
  - T1 found a sign change in r for its own regulator (`TESTS.md:68`), so a tuned zero per species pair is plausible (suggested). It would be a tuning.
- **Structure (checked).** The inner continuum region contributes 1.333 → 4/3 as m/r₁ → 0 (for example −8π²·(−0.016883) = 1.3330). That is exactly Collins' "1", produced by any loop-momentum window fixed in the lattice frame. The outer region adds a shape-dependent piece of either sign (−0.35 to +5.6).
- **Interpretation (suggested).** This mirrors the T0/R3 surface-term lemma: the window, not the in-box dynamics, carries the LV.
- **Reading (numbers).** At QED-strength g² = 4πα: g²/16π² = 5.8e-4, so δc² ≈ 1e-3 for one such loop. That is the same order as F2's split, and 15–16 decades above the photon-decay bound |c_e − c_γ| ≤ 2.66e-19 (`C5_O1_referee.md:76`).
- **Scope.** This is a scalar self-energy from a box-fermion loop, not a QED computation. The fermion's own self-energy and the e–γ split were not computed here.

**The box does not help local loops (checked in this class).** The free box law's exactness (R7-1 P1) is not inherited by point-vertex loops.

### 3.3 Class FF (frame-fixed box form factor, all propagators relativistic): O(g²/16π²), scale-free — checked

- With χ(k)χ(k+p), χ = Π_i plateau(k_i; c₁, c₂), c₂ < b₁: XI_FF = 10.97 for c = (1.0, 1.9). It varies by 3e-3 over m = 0.05 → 0.01, and by 4e-3 over N = 96 → 160 (`r75_oneloop.out:26-30`).
- Halving the form-factor scale, c = (0.5, 0.95), gives 10.92 (`:31`).
- Quartering it gives 9.57 (`:32`). That value is resolution-limited: m/c₁ = 0.04, and the two finite-difference steps disagree by 4%.
- **Collins verbatim.** Lorentz-exact propagators plus a frame-fixed cutoff function give a scale-independent O(g²) speed shift.
- **Bound (suggested).** For multiplicative frame-fixed form factors the excess over 4/3 is a positive quadratic form in ∇f (Collins' 2∫x f′² for spherical f). I conjecture XI_FF ≥ 4/3 for every such f. Not proved for non-spherical f.

**Super-renormalizable control (checked, `r75_oneloop.out:9-11`).**
- For the scalar loop g φχ†χ (g of mass dimension 1) with a Collins regulator: XI_s·Λ² = 4.78, 5.70, 6.62 at Λ = 1, 2, 4 (m = 0.01).
- So δc² ∝ (g²/16π²Λ²)(a + b ln Λ/m). This is power-suppressed: the Collins problem is a marginal-coupling problem (gauge, Yukawa).

### 3.4 Class INV (invariant-mass vertex functions, both time orderings): one-loop LV exactly zero — proved; checked

**Lemma INV-s (proved).**
- Take the O(g²) φ self-energy of a Hamiltonian whose φ → χχ̄ and vacuum → φχχ̄ terms carry g F(M²)/√(8ωE₁E₂). Here M² = (E₁ + E₂)² − p² is the invariant mass of the pair, computed with on-shell energies.
- With both time orderings it is
  Π(E, p) = g² ∫d³k F²/(4E₁E₂) · [1/(W − E) + 1/(W + E)] = g² ∫dM² ρ₂(M²) F(M²)²/(M² − s),  with s = E² − p².
- This holds whenever every k in supp F has both legs where ε̃ equals the continuum dispersion.
- **Proof.** W = E₁ + E₂ = √(M² + p²) is an identity. The bracket is 2W/(W² − E²). Then ∫d³k/(4E₁E₂) G(W) = ∫dM² ρ₂(M²) G(√(M²+p²))/(2√(M²+p²)), with ρ₂ the Lorentz-invariant two-body phase space; integrate d³k₁/2E₁ d³k₂/2E₂ δ⁴ over P⁰. ∎
- The result is a function of s alone for |p| inside the budget. So every LV Taylor coefficient, dimension 4 included, vanishes.

**Lemma INV-f (Dirac–Yukawa loop, proved).**
- After the k₀ integral, the integrand reduces exactly to 4F²[(2m² + P_E²/2)·I₀ − W/(4E₁E₂)], with P_E² = ω² + p². This uses m² − k·k′ + ½(E₁² + E₂²) = 2m² + ½|k − k′|².
- Both pieces are dispersive in the sense of INV-s: ∫d³k F² W/(4E₁E₂) = ½∫dM² ρ₂ F², independent of p.
- So J_f depends on P_E² alone. ∎
- My first guess, that the instantaneous 1/(2E) pieces would spoil this, was wrong. They combine into the dispersive form.

**Lemma INV-k (support and the vacuum vertex; proved, elementary kinematics).**
1. **Legs stay in the box.** For an on-shell pair of total momentum p and M ≤ Λ₂, |k_i| ≤ |p| + Λ₂/2. With a doubler-free extension, ε̃ ≥ √(m² + b₁²) outside the box. So F(M²) = 0 whenever a leg leaves the box, if Λ₂ < √(m² + b₁²) + m − O(p).
2. **The vacuum term.** The vacuum → φχχ̄ term is a single operator, shared by the φ and χ Z-graphs. With the product vertex F(M₁₂²)F(M₁₃²)F(M₂₃²), the two "spectator" pairs have
   M² ≤ μ² + m² + 2(ω_p + |p|)(√(Λ₂² + p²) − m).
   So they sit on the F-plateau whenever μ² + m² + 2(ω_p + |p|)Λ₂ ≲ Λ₁².
   - On that budget every one-loop self-energy (φ and χ) is of the INV-s form.
   - In rapidity, the budget is y ≲ ln(Λ₁²/(2Λ₂μ)): about 50 for Planck-scale Λ and an electron.
   - The product vertex was **not** checked numerically.

**Checks (`r75_oneloop.out:33-53`; `r75_extra.out:9-12`).**
- **Continuum scalar, Λ₁ = 1.0, Λ₂ = 1.6, m = 0.2.** At three values of s and p = 0, 0.3, 0.6, 0.9, Π_full agrees to ≤ 3e-13.
  - The *one-ordering* comparator (no Z-graph) shifts by 4e-3 to 8e-3 on a base of 1e-2 to 3e-2.
  - The largest leg momentum on the support is 1.33 < b₁ = 2.
- **Continuum Dirac loop with F².** J_f at (ω, 0), (0, p) and the diagonal agree to 2e-16 (P_E² = 0.09) and 2e-15 (0.36).
- **Lattice realisation.** 3D BZ sum, N = 128, doubler-free scalar dispersion, M² from the lattice ε̃: Π spread over p = 0, 0.3, 0.6 is 7.2e-9; lattice minus continuum is −1.1e-8. Both are quadrature error; min w outside the box is 4.000 = b₁².

### 3.5 Class BT (mass-squared operator with pair creation): zero at every order, dressed one-particle sector — proved by construction; checked

**Construction.**
- M² = diag(μ², M₀²(k)) + U, with U_{k,φ} = g F(|q(k)|)·√(|∂q/∂k₁|_P Δk^d) and q the rest-frame relative momentum.
- H = √(M² + P²) on the sector at lattice momentum P, with |P| ≤ 0.7.
- U = 1_P ⊗ u commutes with P, J and X_NW. So the dressed eigenvalue z of M² is P-independent at every order in g (standard BT; comparator Polyzou V).
- The lattice operator coincides with the BT operator on the plateau (Lemma L of R7-1) because every leg on supp F lies inside the box. Checked: max |k_i| = 0.83–0.92, below the leg cutoff 1.4 < B = 2.6.

**d = 1, exact diagonalisation** (`r75_bt_production.out:1-10`). The spread of E² − P² over 8 momenta P ∈ [0, 0.7]:

| g | M_phys² (bare 0.25) | L = 400 | 800 | 1600 |
|---|---|---|---|---|
| 0.1 | 0.2210 | 8.2e-9 | 1.3e-11 | 1.7e-15 |
| 0.3 | 0.0891 | 4.4e-8 | 7.1e-11 | 9.1e-15 |
| 0.38 | 0.0287 | 6.1e-8 | 9.8e-11 | 1.2e-14 |

- The convergence in L is the Riemann sum of a C^∞ compact integrand.
- At g = 1 the state is tachyonic (z < 0), so it is not used.

**d = 3, s-wave, secular equation** (`r75_bt3d.out`):
- six momenta, including off-axis and diagonal ones, with |P| ≤ 0.68;
- spread 1.3e-4 / 1.9e-5 / 4.1e-6 at L = 64 / 96 / 128;
- the measure check Σ|∂q/∂k|F²Δk³ / ∫F²d³q − 1 falls to ≤ 8e-5.
- This also answers the R7-1 referee's d ≥ 2 channel point *for the dressed dispersion*. Boosts were not built.

**Comparators (`r75_bt_production.out:11-20`).**
- Instant-form Lee vertex (H = H₀ + V, the same invariant F, no Z-graph), exact diagonalisation: spread 1.0e-2 at g = 0.3 and 0.13 at g = 1. This is O(g²) LV.
- Second order with the Z-graph and invariant F: spread 8e-14 / 2e-15 (L = 1600 / 3200), against 0.10 without the Z-graph (this is INV-s in d = 1).
- Point vertex with the whole zone (lattice dispersion, Z-graph included): 2ω δE varies from −3.32 to −1.93 over P ∈ [0, 0.6]. This is O(1) relative LV. The d = 1 chain's χ has R7-1's zone-edge doubler, which the point loop sees.

### 3.6 Suppressed rather than zero (suggested)

- If F is not compact, the LV part of Π comes only from the region where some leg leaves the box. There ε̃ differs from the continuum.
- So |δc²| ≲ C·g²·sup_{M ≥ M_edge} |F(M)|², with M_edge ≈ 2b₁ − O(p).
- **Power-law tails** (Λ_F/M)^{2n} give (Λ_F/b)^{2n}-type suppression. **Gaussian tails** give e^{−4b²/Λ_F²}.
- This is the Belenchia–Gambassi–Liberati scale separation (comparator V, abstract) in its extreme form. Compact support makes it exactly zero.
- Not computed.

## 4. The answer to the registered question

"Is it O(1)·g², suppressed by a power of (box scale / cutoff), or zero?"

| class | one-loop dimension-4 LV | status |
|---|---|---|
| P (local point vertex, box dispersion) | O(1)·g²/16π²: XI 0.98–6.97, m- and scale-independent | checked (11 shapes); T1's refereed mechanism |
| FF (frame-fixed box form factor) | O(1)·g²/16π²: XI ≈ 11, scale-free | checked |
| P or FF, dimensionful coupling | ∝ g²/(16π²Λ²) × log: power-suppressed | checked (continuum Collins regulator) |
| INV, compact F (both time orderings, vacuum pair creation) | **0** exactly (all LV orders), within the budget of Lemma INV-k | proved; checked to 1e-13 (continuum) and 1e-8 (lattice) |
| INV or BT, non-compact F | ≲ g²·(F weight beyond the box edge) | suggested |
| BT (mass-squared, pair creation) | **0** at every order, dressed one-particle sector | proved (BT); checked d = 1 (1e-14) and d = 3 (4e-6, falling with L) |

## 5. Strong-word check

- **"Exactly zero" (INV):** one loop, external momenta inside the Lemma INV-k budget, vertex functions exactly as stated. Shown for the φ self-energy (scalar and Dirac loops) and argued for χ with the product vacuum vertex, which was not run.
- **"Every order" (BT):** the dressed one-particle sector only, with an inert bare vacuum. Not multi-cluster states, not scattering of two dressed particles (R7-6), not loops with spectators.
- **"Unsuppressed" (P, FF):**
  - P: within the scanned shape families;
  - FF: within the scanned scales;
  - both: for marginal couplings, as m/b → 0.
  - The universal piece is 4/3 (checked); the shape piece has either sign.
  - "Never zero" is **not** claimed. A tuned zero is plausible (T1).
- **"No tuning" (INV/BT):** no parameter is adjusted to cancel anything. Any compact F at any Λ₂ inside the box gives zero. But the Lorentz invariance of every vertex function is a structural choice (§6), not an output.
- **"Field theory":** INV is a Fock-space Hamiltonian with all orderings, including vacuum creation. It is non-local at 1/Λ_F, and microcausality is not shown. BT is relativistic quantum mechanics with particle production (bounded bare particle number in Polyzou's cluster-separable version). Neither is a local QFT.

## 6. What the PASS does and does not mean (reading)

- **Polchinski's objection applies.** In INV and BT, Lorentz invariance of the interacting dynamics is supplied by choosing vertex functions of invariant masses. The lattice contributes only a momentum box that the dynamics never reaches. "The small breaking is put in by hand" (Polchinski V) applies verbatim: here it is zero, put in by hand.
  - The result is a consistency statement: a frame-fixed box does not *force* IR LV through loops.
  - It is not a mechanism that explains one light cone from the axioms.
  - Admissibility does not fix dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-125`), so the choice is allowed but supplied.
- **One frame-fixed vertex spoils it.** Classes P and FF show that any single frame-fixed vertex (a point coupling reaching the zone, or a lattice-momentum cutoff) brings back O(g²/16π²) in that loop. The requirement is therefore universal across all interactions of all species.
- **QED is the decisive open item.** The F2 split is a gauge-loop effect. Lattice gauge invariance links every charged mode, edge modes included (R7-1 §5.6). Whether gauge invariance (a Ward identity) can coexist with invariant-mass, compactly supported vertex functions on the box is not addressed. The continuum path-ordered-link technique (Terning, R) is a candidate route.
- **Two loops in INV are not shown.** Outer vertex functions are evaluated with bare on-shell energies while the inner lines are dressed. LI at O(g⁴) is not shown, and plausibly fails unless the dynamics is reorganised in BT form (suggested).
- **The BT class trades vacuum fluctuations and cluster separability for exactness.** Polyzou's construction restores cluster properties only for a bounded number of bare particles (V, abstract). That is R7-6's problem.
- **Locality price.** On top of R7-1's sub-exponential tails, the vertices are non-local at 1/Λ_F. X1's collider bounds require Λ_F ≳ few TeV for matter (`TESTS.md:2050-2056`), which is trivially met for Λ_F near the box scale.

## 7. Reading against the FIXED readings (`TESTS.md:3383-3386`)

**PASS — worker reading, same family, unrefereed.** The clause asks for "an explicit box field theory whose one-loop IR dimension-4 LV vanishes, or is suppressed below current bounds without tuning, checked". Met by:
- **(a)** the INV Hamiltonian on Z³ × ℝ (φ, χ, χ̄ with pair creation including vacuum pair creation, compact invariant-mass vertex functions) — one-loop LV exactly zero (Lemmas INV-s, INV-f, INV-k; checked continuum and lattice);
- **(b)** the BT pair-creation law — zero at every order for the dressed particle (checked d = 1 and d = 3).

**Scope that must travel with it:**
- vertex functions of invariant masses, compact below the box edge, for every vertex of every species;
- non-local at 1/Λ_F, with microcausality not shown;
- a rapidity budget;
- one loop for INV, and the product vacuum vertex not run numerically;
- one-cluster sector for BT, with an inert vacuum;
- no gauge fields, no gravity;
- continuous time;
- d = 3 for INV and the BT dispersion; d = 1 for BT exact diagonalisation;
- the R7-1 box law, whose referee confirmed it with corrections.

**Not the registered FAIL.** Classes P and FF give O(g²/16π²) unsuppressed LV in stated classes (checked). That is a class-bounded FAIL-type result, consistent with T1's refereed (a2) FAIL. If the supervisor records it as a FAIL for those classes, it needs the codex referee first.

## 8. Price (named, not adopted)

"Every interaction vertex, of every species, is a Lorentz-invariant C^∞ function of the invariant mass of the multi-particle state it creates or absorbs (rest-frame variables), with compact support below the box edge. The dynamics is the instant-form Hamiltonian with all orderings (one-loop exactness), or a Bakamjian–Thomas mass operator (all-order exactness in the one-cluster sector). The result is non-local at the form-factor scale 1/Λ_F < 1/b, and a single frame-fixed vertex reintroduces O(g²/16π²) LV in its loops."

This extends R7-1's price (`R7-1_report.md:274`). It touches no axiom text, since Admissibility does not choose dynamics (`MINIMAL_AXIOMS:114-125`). It does require a supplied dynamics bridge.

## 9. For the referee

Check, in order:
1. **Lemma INV-s:** the phase-space identity, and that W = √(M² + p²) holds by definition of M.
2. **Lemma INV-f:** the algebraic reduction m² − k·k′ + ½(E₁² + E₂²) = 2m² + ½p², and that ∫F²W/(4E₁E₂) is p-independent.
3. **Lemma INV-k:** the spectator invariant-mass bound and the box-support bound.
4. **The sign convention:** fermion Π_M = +g²J_f, scalar Π_M = −g²J_s, validated by Collins' formula (§3.1).
5. **The class-P partition** (inner continuum part plus outer lattice part), and convergence in N, h and m.
6. **The BT lattice embedding:** the leg cutoff is inactive on supp F; the Jacobian is |∂q/∂k₁|_P = W E_q²/(E₁E₂M₀) (measure check ≤ 8e-5 at L = 128).
7. **Scope:** whether a non-local, non-crossing Hamiltonian counts as a "box field theory" in the registered clause. If it must be local, the strongest reading is FAIL in class P/FF (with T1) and OPEN beyond.
