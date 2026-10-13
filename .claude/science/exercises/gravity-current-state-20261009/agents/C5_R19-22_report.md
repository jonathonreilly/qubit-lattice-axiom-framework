# C5 R19-22: pricing the supplied graviton. How large a finite site space reproduces the CCR N-type graviton?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-13, 06:11Z to about 06:45Z. **Unrefereed.** I edited no repository file. Scripts and outputs are in `S/scripts/` (s1–s6; each run takes under 20 s on 2 threads). Rechecks of archived runners are in `S/recheck/`. I downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`; the registration is `TESTS:8175-8205`, with the FIXED readings at `:8201-8204`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `R15-5`, `R16-7`, `R17-1` = `P/agents/C5_<id>_report.md`; `vX` = `P/agents/C5_X_referee_verdict.md`.
- `S` = `scratchpad/C5/R19-22/`.

**Labels.**
- proved: a derivation made here (unrefereed);
- checked: numerics run here;
- suggested: an argument, not a proof;
- reading: an interpretation;
- comparator: literature, RECALLED, not fetched.

**Archived-runner recheck (checked; `S/recheck/recheck_summary.out`).** These archived runners reproduce byte-for-byte (0 diff lines):
- R15-5 s1 and s3;
- R16-7 s1;
- R17-1 s2;
- R16-11 s1.

I rely on them only where cited.

---

## 0. Plain words

- **The question.** R15-5's graviton is light-like with a 1/r pull, but it needs continuous (CCR) field pairs at every site. That breaks "one M₂(C) per site" (`AX:47`). Replace each continuous pair by a large spin S or a Z_N clock. How large must S or N be to pass GW170817 and the Newtonian tests at LIGO wavelengths? The registration expected tens of qubits per site.
- **The cheap part really is cheap (checked).**
  - Truncating one field pair to spin S shifts its oscillation frequency by exactly −(2n+1)/(2S).
  - Truncating to a clock shifts it by about e^{−1.45N}.
  - The lattice's own dispersion at LIGO frequencies is about 1e-82.
  - So if only the two light-like TT modes mattered, a clock of N ≈ 22–24 states per slot, about 30 qubits per cell, would meet |c_g − c| ≲ 1e-15 without retuning.
- **But the graviton is not just the TT field.** R15-5's graviton exists only because two exact gauge constraints do two jobs (`R15-5:122-145`):
  - they remove four partner modes;
  - they remove a negative-energy "conformal" mode.

  The same conformal mode carries the 1/r pull (`N0914:280-296`). For those constraints to be exact, gauge transformations must *translate* the metric field by any real amount. A finite site space cannot do that. In finite dimensions [h, E] can never equal i·1, because the trace of a commutator is zero.
- **What happens at finite S.** Four results (proved, checked):
  1. **Constraints kept exact on finite slots.** The gauge group is then compact, the metric energy must be built from gauge-invariant hops, and R16-7's k⁴ f-sum bound holds at every S. Raising S does not move the compactness rung. The exactly invariant large-S limit is the |R|² rung, not the Einstein–Hilbert term.
  2. **Spin-S fields with the N-type Hamiltonian kept.** The two constraints stop commuting. Their double commutators produce every slot's spin operators, so **no state satisfies both constraints at any finite S** (Lemma J).
  3. **Constraints imposed by local energy penalties instead.** The negative trace direction wins: **the finite-S ground state is "trace-collapsed", at least (3/4)JS per cell below the graviton sector**. The graviton sector is never the low-energy sector, and the gap *grows* with S. Every local repair fails one of three ways:
     - a polynomially growing Jordan chain;
     - a conformal tachyon with growth rate 2√λ|q̂|;
     - six gapless branches instead of two.
  4. **Clocks with exact stabilizer constraints.** In every gauge-invariant state each metric label is uniformly spread, so about a third of slots sit across the wrap. Gauge-invariant stencils then take values ~6N. The clock's exponential accuracy does not survive in the gauge sector.
- **Reading: OPEN.**
  - No finite S reproduces the N-type graviton as a physical, stable sector in the classes examined. So FINITE-PRICE is not met.
  - What I show is "no physical sector or vacuum at any finite S" in stated classes, not "no z = 1 at any k". It is also unrefereed, and windows remain. So NO-FINITE is not met either.
  - The registered expectation fails for a structural reason. Its premise, a vacuum with occupation ≪ S, does not exist in the extended N-type at any finite S.
  - The price of P-N1 is the **noncompact gauge orbit**, not the size of the site space.
  - A table of *conditional* prices is in §5. It assumes some unbuilt mechanism that protects the graviton, with residue ε, and runs from about 30 to about 2000 qubits per cell.

---

## 1. Hypotheses, classes, excluded realizations

**Setting** (`TESTS:8187-8190`): R15-5's exact N-type, H_N = J/2[E:E − ½(trE)²] + g/2 h:R(h) with constraints G E = 0 and S h = 0 (`N0914:72-76`), with the CCR pairs replaced as follows. Slot positions and integer stencils are N0914's (`N0914:85-113`).

**Classes.**
- **𝒞_HP (spin-S, Holstein–Primakoff embedding).** Each canonical slot a carries spin S, with q_a = S^y_a/√S and p_a = S^z_a/√S, so [q_a, p_b] = iδ_ab S^x_a/S.
  - Constraints: the linear operators (G p)_e and (S q)_y.
  - H = H_N(q, p) plus any of the local completions U|Gp|², V|Sq|², λ(tr p)², μ|Gq|², ν|∇ tr q|².
- **𝒞_clock (Z_N clock, CCR scaling).**
  - δ = √(2π/N). h = δ·(centered label); E is the Fourier-conjugate centered label.
  - H_N uses these diagonal ("kinked") quadratics.
  - Constraints: either N0914's exact commuting Weyl stabilizers, or energetic.
- **𝒬_E^fin (exact vector law, finite slots).**
  - Finite-dimensional slots, with commuting local Hermitian E_a of *any finite spectrum*.
  - [H, (GE)_e] = 0 exactly; H quasi-local with summable second moments.
  - This is R16-7's 𝒬_E (`R16-7:61-72`) with "integer window" relaxed to "finite spectrum".

**Excluded realizations.** Nothing negative here covers:
- emergent or non-perturbative phases not of these forms (P-N3″, P-r16-7a);
- small-N mod-N aliasing windows (R17-1's WINDOW, `TESTS:6157`);
- weak constraint imposition (Gupta–Bleuler/BRST-type, or ⟨G p⟩ = 0 only);
- spin embeddings whose constraints are not linear in S^y, S^z (Lemma J's generalization is only suggested);
- metastable or prethermal sectors;
- families whose hop support grows with S;
- matter, nonlinear gravity, Λ.

---

## 2. Prior art (each counted once)

1. **R15-5 and vR15-5.**
   - The ladder: CCR/CCR z = 1; rotor rungs z = 2; compact/compact z = 3 (`R15-5:158-176`; corrected `vR15-5:17-30`).
   - Lemma W, with the lifting threshold N > 36nM (`vR15-5:33-35`).
   - "Large-N clocks imitating CCR … weak invariance breaks at the wrap" (`R15-5:194`, suggested there). §3.5 below checks it.
   - P-N1 (`R15-5:257`).
2. **N0914.**
   - The H_N comparator (`:72-84`) and the integer clock complex (`:90-113`).
   - The character lemma (`:186-223`) and the moment proof (`:225-258`).
   - **Finite penalties: det K = −J²/2 and F⁴ = 0, a Jordan chain** (`:260-278`). My s2(b) rechecks this, so it is counted once.
   - The static source (`:280-296`).
3. **R16-7 and vR16-7.** Theorem B (TT f-sum O(k⁴) in 𝒬_E, every coupling; `R16-7:141-175`), its dual §7 (`:208-220`) and the clock note §8 (`:224-230`). The referee confirmed the mathematics with a readout-bridge caveat, reading INCONCLUSIVE (`vR16-7:5,7,17`; `TESTS:5582`). My §4 adds only "finite real spectrum" and an S-scaling remark.
4. **R16-11 (TRANSFERS, refereed; `TESTS:5894`).** The dressing transfer.
5. **R15-3 (refereed; `TESTS:5184-5189`).** Finite, continuous, PSD, cubic-covariant Gaussians have ≥ 4 gapless branches. My s2(d) gives 6 in the local completions, consistent with this; counted once.
6. **R11-2 X1 (`TESTS:4407-4409`) and R12-5 (`TESTS:4543`).** Context only.
7. **R17-1 (WINDOW; `TESTS:6157-6167`), R17-6 (OPEN; `TESTS:6285`), R19-1 (NEITHER; `TESTS:7517`), R19-7 (OPEN; `TESTS:7652`).** The Z₂ route. Not touched here.
8. **Comparators (RECALLED).**
   - Holstein–Primakoff 1940.
   - The 1/S spin-wave velocity renormalization, e.g. the AFM Z_c = 1 + 0.158/(2S) (Oguchi 1960).
   - Quantum link models (Chandrasekharan–Wiese 1997; Brower–Chandrasekharan–Wiese 1999; Banerjee et al. 2012–13): spin-S links tend to the *compact* Wilson U(1) as S → ∞, whose 3+1D Coulomb phase has a photon because U(1) invariant characters are O(k).
   - GW170817: −3e-15 ≤ Δc/c ≤ 7e-16.
   - LVK graviton mass bound m_g ≤ 1.27e-23 eV.
   - Chebyshev approximation of 1/x.

---

## 3. (a) Dispersion and static response at k ≪ 1/a; error scaling

### 3.1 The TT field alone (checked; s1, s2(a))
- **HP, one pair.** H = (p² + q²)/2 gives gaps 1 − (2n+1)/(2S) exactly (s1 (1): −2.500e-1 at S = 2 down to −1.953e-3 at S = 256, equal to −1/(2S)). The error is **polynomial, ∝ 1/S**. A matching identity holds: (S^y)² + (S^z)² = S(S+1) − (S^x)².
- **Clock, one pair.** The error falls from 5.6e-4 (N = 8) to 4.2e-14 (N = 24), then reaches machine precision. The fitted log-slope is −1.445 per unit N (s1 (2); π/2 = 1.571 with prefactor powers). The error is **exponentially small**.
- **Two coupled pairs** (normal modes 1 and √2.4):
  - HP error ≈ 0.66/S for S ≥ 16 (s1 (3)). For S ≤ 8 the gap identification is spoiled by the S^x = ±S vacuum doubling.
  - Clock error 3e-3 → 1.9e-11 from N = 8 to 24.
- **Every local completion leaves TT exact (s2(a)).** The TT block stays ω² = Jg q̂² under U, V, λ, μ, ν, along ẑ, (110), (111) and (125), with leakage below 5e-16. TT decouples by covariance.
- **Reading.** The registration's "error ∝ occupation/S" (HP) or "exponentially small" (clock) is right **for the TT field in isolation**.
  - The constant 1/S velocity shift is one retuning of Jg (comparator: spin-wave renormalization).
  - Lattice dispersion at 100 Hz is 1 − v_g ≈ (ka)²/8 = 1.4e-82 (s4).

### 3.2 Lemma Tr: finite slots cannot carry the gauge translation (proved; checked)
- **Statement.** For any finite-dimensional slot with Hermitian q, p, tr[q, p] = 0. So D := 1 − [q, p]/i has tr D = d. The canonical defect has average eigenvalue 1: it can be small only on part of the state space.
- **Consequence.** In H_N, [H, (GE)_e] = −(ig/2)Σ_a G_ea{D_a, (R q)_a}, using G R = 0 for the identity part. The vector law is exact only where D ≈ 0.
- **Checked (s1 (4)).**
  - HP: D = (S − S^x)/S = n/S exactly, with eigenvalues 0…2 and tr D = 2S + 1.
  - Clock: D has eigenvalues from −45 to +65 at N = 32, concentrated at the wrap, with tr D = N.

### 3.3 Lemma J: the HP N-type has no physical sector at any finite S (proved; rank checked)
- **Identity (proved, exact).** [(Gp)_e, (Sq)_y] = −(i/S)Σ_a G_ea S_ya S^x_a (s3: residual ≤ 9e-16 at S = ½, 1, 3/2).
  - At S^x ≡ S this vanishes by G Sᵀ = 0.
  - The single-commutator matrix has rank = #slots − 1 on 3³, 4³ and 5³ (s3). The null vector is the uniform one, so the single commutator alone is not decisive.
- **Double commutators (proved).**
  - [(Gp)_e, [(Gp)_e′, (Sq)_y]] = (1/S)Σ_a G_ea G_e′a S_ya q_a.
  - [(Sq)_y′, [(Gp)_e, (Sq)_y]] = −(1/S)Σ_a G_ea S_ya S_y′a p_a.
  - Both annihilate any joint zero vector ψ of all constraints.
- **Rank (checked).** Both coefficient matrices have **full column rank** on the 3³ and 4³ tori (162/162 and 384/384; s3).
- **Locality (checked, s6).** On a 6³ torus, every one of the 6 slot types at a central site is an exact combination (residual 0) of rows supported within Chebyshev distance 2. The left inverse is therefore finitely supported, and the conclusion holds on the infinite lattice and on any box that contains that neighbourhood. No wrap-around is used.
- **Conclusion.**
  - Full rank gives q_a ψ = p_a ψ = 0 for every a.
  - Then S^x_a ψ = −i[S^y_a, S^z_a]ψ = 0.
  - Then S(S+1)ψ = 0, so **ψ = 0 for every S ≥ ½**.
- **Contrast with CCR.** There the commutator is a c-number (zero), the double commutators vanish, and the (non-normalizable) physical states exist.
- **Control (checked).** A single toy constraint pair on three slots does have joint kernels at integer S (s3, last lines). So the lattice rank, not first-classness at S = ∞ alone, is what forbids a joint sector.

### 3.4 Proposition C: trace collapse; the graviton sector is not low-energy (proved, variational)
- **Statement.** In 𝒞_HP with any finite local penalties (U ≥ 0 on |Gp|², V ≥ 0 on |Sq|², λ = 0):

  E_gs/V ≤ −(3/4)JS + O(J/S + g‖R‖ + V‖S‖²),

  with S-independent constants.
- **Trial state.** All diagonal slots in S^z = +S (p_jj = √S), all off-diagonal slots in |S^z| minimal.
  - The diagonal part of K is 3S − (9/2)S = −(3/2)S per cell. Off-diagonal slots add O(1/S). Checked in s2(e): min K_diag = −(3/2)E_max².
  - The trial state is an eigenstate of Gp with eigenvalue 0, so the vector penalty costs nothing.
  - ⟨q_a q_b⟩ = δ_ab/2, so the h:R(h) and V terms are O(1) per cell.
- **The same bound in the zero-total-trace sector** (where R15-5 superselects the uniform trace, `R15-5:239`). Take sign domains: (+S)·I cells in half the volume, (−S)·I cells in the other. K is −(3/2)S in every cell. The vector penalty acts only on the domain walls, costing O(U S·wall fraction).
- **Comparison.** The HP graviton sector (S^x ≈ S) has ⟨K⟩ = O(1) per cell. So it lies **at least (3/4)JS per cell above the true ground state**, and the gap grows with S.
- **Clock (CCR scaling).** The same bound is −(3π/8)JN per cell.
- **Relation to prior work.** This is the finite-S face of N0914's det K = −J²/2 (`N0914:260-278`). The new content is that bounding the field space does not create a vacuum; it moves the ground state to the boundary.

### 3.5 The clock with exact stabilizers: the wrap is generic (proved; checked)
- **Uniform marginals (proved).** In any state invariant under N0914's vector stabilizers (shifts n → n + Gᵀe_j), every h-slot label is uniformly distributed on Z_N. Each slot is shifted by ±1 by some stabilizer, which forces the marginal to be invariant under ±1.
- **Wrap identity (proved).** A pure-gauge configuration n = Gᵀλ mod N has centered labels c = Gᵀλ − N w with integer wrap pattern w. For any integer stencil A with A Gᵀ = 0 (S here; R2 likewise, since R2 Gᵀ = 0, `N0914:142-147`), A c = −N A w. Hence h:R(h) on a pure-gauge configuration equals 2πN·wᵀR₂w (up to the g normalization): of size N, not small.
- **Checked (s5, 4³ torus, 200 random gauges at N = 16, 64, 256).** The identity holds on every sample. The mean fraction of wrapped slots is 0.32–0.33 at every N. The mean max|S c|/N is about 6.0. Label histograms are flat.
- **Reading.** The clock's exponential accuracy (§3.1) applies to wavefunctions localized away from the wrap. Gauge-invariant states are never localized that way. This makes `R15-5:194` (suggested) precise.

### 3.6 Trilemma for local completions of the extended small-field theory (proved algebra; checked s2)
The small-field (HP or large-N) linearization of any 𝒞_HP/𝒞_clock model is the extended six-pair quadratic theory. TT stays exact (§3.1). The other four pairs can be completed locally in only three ways, and each fails.
- **(i) λ = 0, any finite U, V.**
  - det K_scalar = −1/2 (J = 1) at U = V = 0, 1, 10 and 1000. This is N0914's result, rechecked.
  - The non-TT Hamilton matrix is nilpotent: ranks of F^n are 5, 2, 1, 0. Jordan chains give polynomial growth (s2(b)).
- **(ii) Bound the trace with λ(trE)², λ > J/12.**
  - The kinetic block becomes PSD, but the conformal h mode keeps its negative stiffness −g q̂².
  - It becomes a **tachyon with growth rate γ = 2√λ |q̂|**, exact as k → 0: γ/|q̂| = 0.6325, 1.0000, 2.0000 at λ = 0.1, 0.25, 1 (s2(c)).
  - At any wavelength, including LIGO's, the e-folding time is of order the wave period divided by 4π√λ.
- **(iii) Make everything PSD with local terms.**
  - At small k the scalar h block is q̂²[[2ν−1, √2ν], [√2ν, ν+μ]]. It is PSD iff ν ≥ ½ and 2νμ ≥ ν + μ (derived by hand; checked).
  - In every PSD example there are **6 gapless z = 1 branches**: TT 1, 1; helicity-1 μ-dependent; two helicity-0. On the boundary 2νμ = ν + μ, one of them is softer than z = 1 (s2(d)).
  - This is R15-3's ≥ 4 (refereed), realized. It is not R15-5's two-mode graviton.

### 3.7 Static response and 1/r
- **Where the 1/r lives.** In 𝒩 the 1/r pull is the conformal-mode response fixed by the exact scalar constraint, h_scalar = −ρP/(2q̂²) (`N0914:280-296`). That is exactly the sector Lemma J, Proposition C and the trilemma break at finite S.
- **The exact-scalar finite class (𝒬_h).** Here the attractive 1/r survives (dual rotor), but an Einstein–Hilbert static response forces ω ≤ Ck² (`R16-7:208-220`; counted once).
- **Reading.** At finite S, "1/r" and "z = 1" cannot both come from the N-type structure in any class examined. The TT dispersion is not where it fails.

---

## 4. (b) Does the compactness ladder move with S?

**Theorem B^fin (proved; R16-7 B with one hypothesis relaxed).**
- **Statement.** In 𝒬_E^fin, the V^{−1/2}-normalized TT-electric f-sum obeys m₁(k) = −Σ_[m]|ε·m̂(k)|²⟨H_m⟩ ≤ C_H k⁴ at every S. The Bogoliubov bound and the conditional ω ≤ Ck² then follow (`vR16-7:5`).
- **Proof.**
  - Decompose H into components H_m that shift the joint E-eigenconfiguration by m. Now m is real, not integer.
  - Exact invariance means G m = 0.
  - N0914's moment lemma is real-linear (`N0914:225-250`), so m̂ = O(k²). The rest is R16-7's proof verbatim.
- **HP normalization (proved).** With E = S^z/√S and the h-side energy of order g, the invariant hop coefficients scale as gS. So C_H is **S-independent**, and the S → ∞ limit of the exactly invariant family is gS(1 − cos(R·h/√S)) → (g/2)|R(h)|², the |R|² rung.
- **Comparator.** Large-S quantum links tend to the *compact* Wilson theory, not noncompact Maxwell (RECALLED). The limits S → ∞ and exact gauge invariance do not commute into CCR.

**Proposition F1′ (suggested; sketch using a RECALLED approximation bound).**
- **Setting.** The hop support is bounded by R₀ (nearest-neighbour admissibility, `AX:57`).
- **Why the shape is S-independent.** m₁(k)/k⁴ is an entire function of bounded exponential type ~R₀ along each ray, whatever S and the coefficient sizes are. Mimicking the Einstein–Hilbert m₁ ≈ c₀k² to relative accuracy ε on a window [k_c, k₀] with k₀ ≤ 1/R₀ means approximating c₀/k² by such a function.
- **The bound.** By the Chebyshev bound for 1/x (RECALLED), that needs an effective polynomial degree ~(k₀/k_c)ln(1/ε). Bounded type allows only ~R₀k₀ + ln(1/ε).
- **Conclusion.** k₀/k_c = O(1): **no crossover scale k_c(S) → 0** at bounded support. A crossover needs supports that grow with S, i.e. non-local hops.

**In 𝒞_HP and 𝒞_clock.** There is no ladder at Gaussian level: TT is z = 1 at every S (§3.1). The obstruction moves from the dispersion to the constraint and conformal sector (Lemma J, Proposition C, the trilemma), and it does not shrink as S grows.

**Answer to (b).**
- The rung does not move with S in the exact class (proved).
- At bounded support no k_c(S) → 0 (suggested).
- In the approximate class the "crossover" picture does not apply: the failure is S-independent in kind and grows in depth ∝ S.

---

## 5. (c) The S needed for GW170817 at a = ℓ_P, and for the 1/r pull

**Observational numbers** (s4; inputs RECALLED):
- At 10–1000 Hz, ka = 3.4e-42 to 3.4e-40, so lattice dispersion is 1e-84 to 1e-80.
- m_g ≤ 1.27e-23 eV gives m_g a ≤ 1.04e-51, i.e. (m_g a)² ≤ 1.1e-102 (Compton range 1.6 ly). At 10–100 Hz a mass at this bound shifts the speed by only 5e-20 to 5e-22, so **the mass bound binds, not GW170817**.
- Static fields near the Sun are h ~ 4e-6. In lattice units the canonical displacement is ~h/√(32π), so the local occupation from sources and GWs is ≪ 1. Field amplitude is not what limits S.

**No unconditional S exists** in 𝒞_HP or 𝒞_clock:
- Lemma J: no physical sector.
- Proposition C: the ground state lies ∝ S below the graviton sector.
- §3.5: the clock's gauge sector sits on the wrap.

**Conditional price table** (suggested; scenario arithmetic only; s4). It assumes an unbuilt mechanism that stabilizes the extended sector and leaves a gauge-breaking residue ε, either as a speed offset (absorbable by one retuning) or as a TT mass m_g²a² ~ ε (not absorbable).

| Residue scaling | Speed only, ε ≤ 1e-15 | TT mass, ε ≤ 1.1e-102 |
|---|---|---|
| HP, ε ~ 1/S | S ≥ 1e15: 51 qubits per slot, 305 per cell | S ≥ 9e101: 340 per slot, about 2040 per cell |
| HP, ε ~ 1/S² | S ≥ 3e7: 26 per slot, 156 per cell | S ≥ 1e51: 170 per slot, about 1020 per cell |
| clock, ε ~ e^{−πN/2} | N ≥ 22: 5 per slot, 30 per cell | N ≥ 150: 8 per slot, 48 per cell |

- The clock row is **not** realized by the clock N-type itself: its gauge sector is wrap-dominated (§3.5).
- A lifetime variant: if the HP sector were metastable with lifetime t* ~ S^α t_P, surviving 8e60 t_P needs S ≥ 8e60 to 7e121 (203–406 qubits per slot) for α = 1 down to ½. The exponent α is not computed.

---

## 6. (d) Qubits per site and the AX:47 price

- **No finite qubit count is established.** The irreducible content of P-N1 is the noncompact gauge orbit. Exact weak invariance of h:R(h) needs gauge translations of h by real amounts, which no finite slot carries (Lemma Tr). With exact compact gauge you get 𝒬_E^fin / X1, and so the |R|² rung (§4).
- **What "supply the graviton" costs, as currently understood.** P-N1 together with P-r15-5b (an exact, noncompact, first-class constraint pair), not "a larger finite site space".
- **Prices (named, never adopted).**

| Price | Axiom touched | Buys |
|---|---|---|
| P-N1 + P-r15-5b (as R15-5) | Qubit `AX:45-53` (`:47`); constraint redundancy not in Admissibility `AX:57-61` | the only class with 2 helicity-±2 z = 1 branches and 1/r (checked, R15-5) |
| **P-r19-22a**: a block site algebra M_{(2S+1)^6}(C) per cell, or blocking ~6·log₂(2S+1) sites into one gravity cell | Qubit `AX:47` (or Lattice `AX:37` plus nearest-neighbour Admissibility `AX:57`, if blocked) | the field truncation of §3.1 only. Insufficient alone (Lemma J, Proposition C) |
| **P-r19-22b**: an unbuilt mechanism that stabilizes the extended sector and leaves gauge residue ε (a mass-protecting symmetry or emergent constraint; a sharpening of P-N3″/P-r16-7a) | none named; dynamical | the conditional table in §5 |
| **P-r19-22c**: a metastable (prethermal) HP graviton sector, not the ground state | none named; a state-selection hypothesis outside Record/Admissibility (`AX:77-83`) | a lifetime-limited graviton; S set by t* ≥ age (α not computed) |

- **The AX:47 price.** Under the literal axiom, each lattice site is one qubit. A cell carrying six slots of dimension 2S+1 needs about 6·log₂(2S+1) qubits; with blocking, the gravity cell is ~(6 log₂(2S+1))^{1/3} lattice spacings. That ranges from about 3a (N = 22 clock) to about 13a (2040 qubits). This is conditional on P-r19-22b, which is unbuilt.

---

## 7. Readings against the FIXED clauses (`TESTS:8201-8204`)

- **FINITE-PRICE: no.**
  - A stated S or N with checked graviton reproduction exists only for the TT field in isolation (§3.1).
  - The graviton of R15-5 needs the constraint and conformal sector. At every finite S in 𝒞_HP and 𝒞_clock that sector has no physical states (Lemma J), no vacuum (Proposition C) and no viable local completion (the trilemma). With exact compact gauge the rung is |R|² at every S (B^fin).
- **NO-FINITE: no.**
  - It needs a refereed demonstration that no finite S reproduces z = 1 at any k.
  - What is shown is different: the TT branch is z = 1 at Gaussian level at every S, while the *physical sector and vacuum* fail.
  - It is shown only in stated classes, and it is unrefereed.
  - Windows remain: emergent non-Gaussian phases, small-N aliasing (R17-1), weak constraint imposition, other spin embeddings, metastable sectors.
- **OPEN: yes.**
  - **Candidate no-gos for the referee:**
    - Lemma J (no joint physical sector at any finite S in 𝒞_HP);
    - Proposition C (trace collapse, depth ≥ (3/4)JS per cell);
    - Theorem B^fin with S-independence (exact class);
    - the uniform-marginal and wrap identity (exact clock).
  - **Decisive missing item:** a finite-dimensional mechanism that removes the conformal and partner modes without exact noncompact constraints (P-r19-22b), or a proof that none exists for finite slots beyond the classes above.
- **Expectation check.**
  - The registration expected FINITE-PRICE with tens of qubits per site, error ∝ occupation/S and k_c(S) ~ 1/(aS^p) (`TESTS:8205`).
  - The error scaling is right for the TT field (checked). But the premise of a vacuum with occupation ≪ S is false for the extended N-type at every finite S (Proposition C), and k_c(S) does not go to 0 in the exact class (B^fin, F1′).
  - The clock's "tens of qubits per cell" appears only as a conditional row, and the clock N-type does not realize it (§3.5).

---

## 8. Strong-word check and scope

- **"Proved"** is used for:
  - Lemma Tr (trace);
  - the commutator and double-commutator identities, and Lemma J's logic. The rank step is checked on 3³ and 4³ tori, and the local isolation within distance 2 on 6³ (s6);
  - Proposition C (variational; constants S-independent);
  - the uniform-marginal lemma and the wrap identity;
  - B^fin (R16-7's proof with real m; N0914's real-linear moment lemma);
  - the scalar-block PSD condition and γ = 2√λ|q̂|.

  All are unrefereed.
- **"Checked"** is used for s1–s5 and the five archived-runner rechecks.
- **"Suggested"** is used for:
  - F1′ (sketch, RECALLED Chebyshev bound);
  - the generalization of Lemma J to non-standard spin embeddings;
  - every row of the §5 table and the lifetime scenario.
- **"Exactly two"** is not claimed anywhere for a finite-S model.
- **"No physical sector"** means no nonzero vector annihilated by all linear HP constraints. Weakly imposed or approximate sectors are not excluded. How small the violations ⟨(Gp)²⟩ and ⟨(Sq)²⟩ can jointly be at finite S was not computed.
- **"Every local completion"** in §3.6 means the five stated quadratic terms and their PSD region. Higher-derivative or nonlinear completions are not covered.
- **Not covered:** matter coupling and Lemma T (`R15-5:204-219`), nonlinear gravity, Λ, fermionic slots, readout bridges (`AX:82-83`; `vR16-7:5`).

## Files (`S/`)

- `scripts/s1_single_mode_truncation.py/.out`:
  - HP vs clock truncation of one and two canonical pairs (error scalings);
  - the commutator defect D.
- `scripts/s2_extended_sector_trilemma.py/.out`:
  - TT invariance under local completions;
  - N0914's scalar determinant and Jordan chain (recheck);
  - the conformal tachyon rate;
  - PSD completions with 6 gapless branches;
  - the trace-collapse minimum.
- `scripts/s3_hp_constraint_algebra.py/.out`:
  - N0914 stencils (G Sᵀ = 0);
  - the HP commutator identity;
  - single- and double-commutator ranks (Lemma J);
  - the toy control.
- `scripts/s6_lemmaJ_local_isolation.py/.out`: the local (distance-2) left inverse for Lemma J's rank step.
- `scripts/s4_price_numbers.py/.out`: LIGO ka, the mass bound, the conditional price table, the lifetime scenario.
- `scripts/s5_clock_wrap.py/.out`: wrap fraction, the wrap identity and uniform marginals in the exact clock gauge sector.
- `recheck/`: copies of the R15-5, R16-7, R16-11 and R17-1 runners, their `.recheck.out`, and `recheck_summary.out` (all 0-diff).
