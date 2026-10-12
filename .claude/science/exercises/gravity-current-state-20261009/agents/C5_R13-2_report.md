# C5 R13-2: producing the graviton — the compact non-Gaussian window, by Euclidean Monte Carlo

**Worker.** Claude Opus 5.5 (same family as every C5 worker and the supervisor). 2026-10-12, 20:18Z to about 20:55Z. **Unrefereed.** No repository file was edited. Scripts and outputs: `scratchpad/C5/R13-2/scripts/` (s1, s2, s2b, s3, s4, s4b, s5, s5b; every run < 10 min on 2 threads).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md` (R13-2 registration `TESTS:4600-4617`). `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`. `R12-5` = `P/agents/C5_R12-5_report.md`; `vR12-5` = `P/agents/C5_R12-5_referee_verdict.md`; `vR11-2` = `P/agents/C5_R11-2_referee_verdict.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.** proved = derivation here (unrefereed); checked = numerics here; suggested = argument; reading = interpretation; comparator = literature (RECALLED unless stated).

**What I used from R12-5, per its referee.** Lemma DW-q is confirmed but only as a first-order expectation bound (`vR12-5:5`); the finite-penalty Gaussian determinant −J²/2 is confirmed (`vR12-5:7`, `N0914:262-270`); the "one exact constraint caps TT at k²" claim is **not** class-wide (the referee's exact-S control has five linear branches, two TT plus three partners, `vR12-5:7`); X1-E is **not** assembled (`vR12-5:13`) and is not used here.

---

## 0. Plain words

- **The question.** Can a compact lattice model of a symmetric tensor field, with both gravity constraints imposed only by energy penalties, have a phase whose only gapless excitations are two light-like (z = 1) graviton polarizations? R12-5 left this as the last unpriced window. The registered method is Euclidean Monte Carlo.
- **(a) The sign problem is real and sits exactly in the "conformal" (trace) sector.** In either natural basis (fields h diagonal, or conjugates E diagonal), Monte Carlo weights are positive only if the *other* side's energy is "ferromagnetic", which forces that side's quadratic form at its minimum to be positive. The graviton-like (N-type) model has a negative direction on *both* sides: the trace of E (the Hamiltonian form of gravity's conformal-factor sign) and the transverse trace of h. So the N-type model itself has no sign-free product-basis Euclidean form (proved, for product bases with diagonal rephasing). With integer E and the quadratic N-type kinetic term, the energy is not even bounded below (uniform E = n·1 has energy −1.5 J n²; proved).
- **New theorem: a stable local Gaussian cannot do it.** If the low-energy theory is any stable (positive) local quadratic theory of the six tensor components and their conjugates, then:
  - gapless gravitons along an axis force two gapless vector partners and one gapless scalar partner (Lemma P; proved, checked). The reason is simple: at zero momentum the graviton directions and the partner directions sit in the same cubic multiplets.
  - the partners can be made non-propagating only by a gauge-type flat direction, and a *positive* quadratic form with that flat direction leaves the graviton with z ≥ 2 (Theorem G; proved in the cubic class, checked by LP in the general class).
  So the window, if it exists, needs a low-energy quadratic form that is **indefinite** (the conformal sign), held up by something beyond Gaussian order. That is exactly the structure that causes the sign problem.
- **(b) Monte Carlo on the cheapest sign-free deformation.** I simulated a sign-free member that keeps the indefinite (conformal-sign) h-potential and compactness, with the E side made positive (DeWitt λ = 0), energetic vector and scalar constraints, on 4D lattices L = 4, 6, 8 (HMC). Semiclassically its ground state is a period-2 "conformal crystal" with **every mode gapped** (ω_min = √3 at L = 4, 6, 8 for κ_B = κ_s = 1; ω_min = 0.80 at κ_B = ¼, κ_s = 4, L = 4; checked). The Monte Carlo sits in that ordered phase at all three couplings (staggered order 0.79–0.99 at L = 4). It shows no clean z = 1 TT branch at L = 4, 6, 8. At the middle coupling the graviton and partner channels soften together, which is noisy but consistent with Lemma P (§6a). This is far below the registered target (L ≥ 12), and the deformation removes the scalar gauge invariance, so it says nothing about the undeformed N-type phase.
- **Reading: OPEN.** Not PRODUCED. EXCLUDED is not reached: Theorem G and the sign lemma go to the referee as a stated-class no-go candidate; the strongly coupled, indefinite, non-Gaussian window itself (Gu–Wen's regime) is not covered by anything here.

---

## 1. Hypotheses, classes, excluded realizations

- **Fields (as N0914 and R12-5).** Six canonical slots per cell, q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz) (off-diagonals on faces), conjugates p = E; N0914's integer stencils G (vector, on E) and S (scalar, on h), G Sᵀ = 0 (`N0914:85-115`).
- **N-type comparator** H_N = J/2 [E:E − (tr E)²/2] + g/2 h:R(h) (`N0914:73-77`), plus energetic penalties U_v|GE|², U_s S² (`N0914:262-270`).
- **Classes.**
  - **𝒢 (stable local Gaussian):** quadratic Hamiltonians on the 6 pairs (plus optionally finitely many auxiliary local pairs for Lemma P), real, cubic-covariant, Hessian symbol 𝓗(k) positive semidefinite (PSD) and C⁴ at k = 0 (summable fourth moments).
  - **𝒮_q / 𝒮_E (product-basis Trotter–Villain):** Euclidean weights from e^{−εH} in the q-basis (h diagonal) or the E-basis (E diagonal), with any diagonal unitary rephasing of that basis, ε → 0.
  - **𝒟₀ (the simulated sign-free deformation):** §6.
- **Excluded, as registered:** matter, nonlinear gravity, Λ (`TESTS:4605-4606`). Also excluded here: non-product bases, complex Langevin / thimbles / meron-cluster sign cures, fermionic representations.

## 2. Prior art (each counted once)

1. **R11-2 + verdict:** X1 (regular lifted compact class ⇒ O(k³)); Lemma A_c; dressing law (`vR11-2:7-9,17`).
2. **R12-5 + verdict:** DW-q (first order only), Gaussian determinant, the five-linear-branch exact-S control, X1-E not assembled (`vR12-5:5-17`).
3. **N0914:** finite-penalty det K = −J²/2 and Jordan chain (`N0914:262-278`); "momentum term scalar-gauge invariant only on G=0" (`N0914:75`); regular-character bound "not a no-go for qubits … strongly interacting constraint phases" (`N0914:214-216`).
4. **Lane R:** "Scalar charge gives linear TT modes only together with gapless partners" (`TESTS:753`). Lemma P below generalizes this.
5. **Repo, DeWitt λ and reflection positivity:** `docs/GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_UNITARITY_REDUCES_TO_EMERGENT_DIFFEOMORPHISM_NARROW_THEOREM_NOTE_2026-06-08.md:22-50` — the trace/conformal sign is acceptable only if the conformal mode is gauge; trace weight ∝ 1 − λd. (Lagrangian λ. The Hamiltonian kinetic E:E − ½(trE)² inverts to the Lagrangian ḣ:ḣ − (trḣ)², i.e. Lagrangian λ = 1; proved by inversion.)
6. **Repo, rank-1 positivity:** Wilson/Villain positivity and sign-free QMC remarks for the U(1) photon (e.g. `docs/POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md`; `docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:375,459`). Rank-1 only; no tensor model.
7. **Literature (comparator, RECALLED, not verified in this run, not load-bearing):** Gu–Wen 0907.1203 (N-type linear result "unreliable", via `vR11-2:9`, `vR12-5:15`); Pretko 1606.08857 (scalar charge: five linear modes, via `vR12-5:19`); Xu cond-mat/0609595 (trace branch plus two graviton-like branches, via `vR12-5:19`); Hořava–Lifshitz λ ≠ 1 gives a propagating scalar graviton (RECALLED); conformal-factor problem of Euclidean gravity, Gibbons–Hawking–Perry 1978 (RECALLED). The registered "published Monte Carlo of rank-2 U(1) Coulomb phases" was **not** verified and is not used.

## 3. Probe (a): Euclidean Villain form and positivity

**Villain form (written).** With the vector penalty decoupled by a shift field ξ on time links (Hubbard–Stratonovich, e^{−εU_v|GE|²} ∝ ∫dξ e^{−ξ²/(4εU_v) + iξ·GE}),

Z = Σ_{E_τ} ∫ Dq Dξ Π_τ exp[ i E_τ·(q_{τ+1} − q_τ + Gᵀξ_τ) − ε H_E(E_τ) − ξ_τ²/(4εU_v) − ε H_q(q_τ) ],

with H_E the E-side (kinetic) energy, H_q = U_s Σ(1 − cos Sq) + (compact h-potential). Summing E gives the q-basis (Villain) weight: the Fourier transform of e^{−εH_E}. Integrating q gives the E-basis weight: the Fourier transform of e^{−εH_q}.

**Lemma U (proved; checked s3(1)).** With integer (U(1)) E and the quadratic N-type kinetic term, H is unbounded below for every U_v, so Z diverges.
- The uniform configuration E = n·1 has GE = 0 and J[E:E − (trE)²/2] = J n²(3 − 9/2) = −1.5 J n². The h-potential is bounded (compact).
- At k ≠ 0 the scalar block keeps a negative eigenvalue −0.5 J at U_v = 1, 100 and 10⁴ (s3(1)), consistent with `N0914:267`.
- The uniform mode survives even exact G, because on a torus the scalar gauge image vanishes at k = 0. So a U(1) Villain model needs a compact (bounded) E-side.

**Lemma S (product-basis positivity; proved).**
- *q-basis.* For a Z_N or U(1) E-side H_E with Fourier coefficients Ĥ_E(r), the small-ε Trotter weight ⟨q′|e^{−εH_E}|q⟩ is non-negative for all q, q′ (after any diagonal rephasing e^{iφ(q)}) iff, after a constant shift E → E + E₀ (the only rephasings that act consistently on every link), Ĥ_E(r) ≤ 0 for every r ≠ 0.
  - Proof: at order ε the off-diagonal kernel is −εĤ_E(r)e^{ir·(q′−q)}. Rephasing by φ multiplies it by e^{i(φ(q′)−φ(q))}. Requiring a fixed sign for every q forces φ to be affine on each orbit, i.e. a shift by E₀. Conversely, if Ĥ_E(r) ≤ 0 then e^{−εH_E} = const·exp(ε Σ|Ĥ_E(r)|χ_r) has non-negative Fourier coefficients for all ε. ∎
  - Then H_E(E + E₀) − H_E(E₀) = Σ_r |Ĥ_E(r)|(1 − cos(2πr·E/N)) ≥ 0. So E₀ is a global minimum and, in the small-field (large-N) expansion, the E-Hessian there is Σ|Ĥ_E(r)| r rᵀ ⪰ 0.
- *E-basis.* The same statement holds with the h-potential: weights are positive iff the potential, after a shift q → q + q₀, is a sum of ferromagnetic characters. Its Hessian at q₀ is then PSD.
- **Consequence (proved).** In 𝒮_q the small-field E-Hessian at the expansion point must be PSD. In 𝒮_E the h-Hessian must be PSD. The N-type comparator violates both:
  - K_N = E:E − ½(trE)² has eigenvalue −½ on the trace (s3(2)). At k ∥ z it is indefinite in the (E_t, E_z) plane (`N0914:262-267`).
  - h:R(h) has one eigenvalue −k² on the transverse trace of h, the S-conjugate direction, at every k (s3(4); s2).
- So **the N-type has no sign-free product-basis Euclidean form; the sign problem lives in the trace/conformal sector on the E side and in the transverse-trace (scalar-constraint) sector on the h side.** This proves R12-5's "QMC is likely sign-problematic" (`R12-5:224`) for 𝒮_q and 𝒮_E.
- **Checked (s3(3)).** On one Z₄ site with Gu–Wen-type single-clock cosines and a negative trace cosine, the q-basis kinetic weight has 512 negative Fourier coefficients at λ_H = ½.
  - The same form at λ_H = 1/3 or 1/4 still has 896 negative coefficients. A negative trace *cosine* is an antiferromagnetic character even when the small-field form is PSD.
  - Rewriting E:E − λ(trE)² for λ ≤ 1/3 as ferromagnetic cosines of integer combinations, Σ_{a<b}(E_aa − E_bb)²/3 + 2Σ_off E_ab² + (1/3 − λ)(trE)², gives zero negative coefficients.
  - So **PSD is necessary; a ferromagnetic integer rewrite is what is sufficient.**
- **Not covered:** non-product bases, mixed bases, and sign cures other than positivity.

## 4. New result: the stable-Gaussian partner theorem

**Lemma P (continuity / partner lemma; proved; checked s1).**
- *Setting.* Let 𝓗(k) be a PSD Hessian symbol on finitely many canonical pairs per cell, cubic-covariant and continuous at k = 0. The frequencies are the |eigenvalues| of iJ𝓗(k), which are continuous in k. For k ∥ z the little group C4v splits the modes into sectors compatible with the O_h irreps at k = 0 (O_h → C4v: Eg → A1 + B1, T2g → B2 + E, A1g → A1). For each C4v sector, the number of frequencies tending to 0 as k → 0 equals the zero multiplicity of the k = 0 blocks subducing to it.
- *Consequence for the 6 tensor pairs (A1g ⊕ Eg ⊕ T2g on each side).*
  - The TT modes at k ∥ z are xx − yy ∈ Eg (B1) and xy ∈ T2g (B2).
  - Both gapless ⇒ the Eg and T2g blocks of 𝓗(0) have zero symplectic eigenvalues.
  - By Schur, the zero covers the whole multiplet. So the vector modes (xz, yz ∈ T2g → E) and one scalar mode (2zz − xx − yy ∈ Eg → A1) also have ω → 0.
  - **Gapless TT ⇒ ≥ 2 vector + 1 scalar partners with ω → 0.** A local mass that gaps the partners gaps the TT component in the same multiplet.
- *Checks (s1).* Random local cubic PSD models (range ≤ √2, h–E cross terms included), sectors decoupled to ~1e-14:
  - V1: TT, vector and one scalar all linear (exponent 1.000), the other scalar gapped (four seeds).
  - V2: a T2g mass gaps B2 (TT xy) *and* both vector modes (ω ≈ 25.6 each). B1 and one A1 stay linear.
  - V3: an Eg mass gaps the rest.
  - V4: h entering only through R(h) gives vector modes flat (ω ≡ 0), one scalar flat, and TT at exponent 2.000.
- *SO(3) form (proved).* If the zero-mode space at k = 0 carries an SO(3) representation (emergent isotropy), helicity ±2 lies in spin j ≥ 2, which contains helicities 0 and ±1. So partners again have ω → 0.
- *Not covered:* the cubic-only loophole of extra fields in A2g ⊕ A2u (subducing to B1 + B2 along axes but to A1 + A2, not E, along body diagonals).

**The flat-partner alternative.**
- ω → 0 partners either propagate (ω(k) > 0 for small k ≠ 0, i.e. gapless partners) or are flat (ω ≡ 0 near 0).
- Flat means 𝓗(k) has a kernel in the partner sector, i.e. a quadratic-order gauge-type invariance. For PSD 𝓗, a kernel vector of the h-block is a full kernel vector, since the cross terms annihilate it by Cauchy–Schwarz.

**Theorem G (stable local Gaussian no-go; proved in the cubic class, checked in the general class).**
- *Hypothesis F.* In class 𝒢, assume the vector partners are flat by a one-sided transverse gauge invariance: B′(k)(k ⊗_s α) = 0 for all α ⊥ k (h side), or the same for K′ (E side). Then the TT block of that side is O(k⁴), and ω_TT = O(k²). So z = 1 TT without propagating vector partners is impossible in 𝒢 under F.
- *Proof.*
  - (1) Order 0: span{k ⊗_s α : α ⊥ k} is all traceless symmetric tensors, so B′(0) = b·P_trace.
  - (2) Order 1 vanishes by inversion (−1 ∈ O_h acts trivially on rank 2), or by PSD.
  - (3) At order k², the PSD part on traceless tensors must annihilate transverse gauge directions. The isotropic forms with this property are a(k²h:h − 2|hk|²) + b k²(tr h)² + c(k·h·k)tr h. This is 3-dimensional, and the cubic-covariant space has the same dimension 3 (s2), so they coincide.
  - On traceless h at k = ẑ these reduce to a(h:h − 2|hẑ|²). TT gives +a h:h, vector gives 0, and the traceless scalar diag(−1, −1, 2)/√6 gives −a/3. PSD therefore forces a = 0, i.e. TT order-k² block = 0.
  - (4) PSD gives c_T² ≤ b_T κ_T = O(k⁴)·O(1), so ω_T² = b_Tκ_T − c_T² = O(k⁴). The E-side case is symmetric. ∎
- *Checks (s2, s2b).*
  - Full linear vector invariance: the order-k² space is **1-dimensional even without cubic symmetry** and is spanned by h:R(h), whose eigenvalues are (−1, 0, 0, 0, 1, 1)k². This is the Fierz–Pauli-type uniqueness: the unique invariant two-derivative form is indefinite.
  - Transverse-only invariance: 13-dimensional without symmetry. A cutting-plane LP gives max_{TT trace = 1} min-eig = −1/6 over all 13 dimensions; coefficient bounds 50 and 2000 and two seeds agree. That is: no PSD member has TT ≠ 0 (checked; LP over 400 sampled directions, an upper bound).
- *Not covered:* mixed h–E flat kernels (reducible to one side by the local canonical map E → E + r(k)h when the kernel ratio r(k) is analytic; suggested, not shown); flatness only along axes; non-local symbols. A homogeneous degree-0 piece of the symbol corresponds to an r⁻³ tail after subtracting the analytic (local) part; such a piece is the generic non-local escape, e.g. the projector P_TT(k̂).

**Reading.**
- Lemma P plus Theorem G say that a phase whose IR is a stable local Gaussian of the tensor field cannot be the registered graviton.
- Any semiclassical expansion about a true classical minimum of a compact local model has a PSD local Hessian, so it lands in 𝒢.
- So the remaining window is an IR whose local quadratic form is **indefinite** (the N-type's own conformal sign, `N0914:262-270`), made consistent only by emergent *exact* constraints below a charge gap. That is Gu–Wen's uncontrolled scenario (`vR12-5:15`).
- In that window the conformal direction is O(1) on the E side, while local terms vanishing on G = 0 are O(k) at k ∥ z (G_z = ik E_zz). So no local off-shell completion removes the indefiniteness (proved at this order: the E_t–E_z entry −J/√2 is O(1), and E_t does not appear in G).
- This is the same structure that Lemma S turns into a sign problem.

## 5. Probe (c): the cheapest sign-free deformations and what they change

| Deformation | Basis made sign-free | What it changes (status) |
|---|---|---|
| **D-λ**: Hamiltonian DeWitt λ_H from ½ to ≤ ⅓, with the ferromagnetic integer rewrite | q-basis (h-potential may stay indefinite) | Breaks scalar-gauge invariance of the kinetic term on G = 0: ‖P_kerG K_λ(scalar direction)‖ = 0 at λ = ½, 1/3 at λ = ⅓, 1 at λ = 0 (s3(2)). S is no longer compatible with H, so the helicity-0 sector gets kinetic weight J(1 − 2λ). Polarization content changes: a dynamical scalar, the Hořava-λ analogue (proved for the symbol; the Hořava link is a RECALLED comparator) |
| **D-h**: ferromagnetic (PSD-at-minimum) h-potential | E-basis | B_N cannot be the Hessian. With quadratic vector invariance the order-k² potential is h:R(h) only (s2(i)), and PSD forces it to 0, giving TT O(k⁴), so z ≥ 2 with bounded K. Without it, vector partners propagate (Lemma P; the referee's five-linear-branch control, `vR12-5:7`) |
| Both | either | z ≥ 2 or partners (Theorem G) |

## 6. Probe (b): Monte Carlo on the sign-free deformation 𝒟₀

**Model (pre-registered in the header of `s4_hmc.py` before any run).**
- θ_a(x, τ) ∈ [0, 2π) (canonical slots), shift field ξ, and
  S_E = Σ β_t[1 − cos(Δ_τθ + Gᵀξ)] + Σ μξ²/2 + κ_s Σ[1 − cos(Sθ)] + (κ_B/2) Σ sin θ · B_N · sin θ.
- This is D-λ at λ_H = 0 (E side: J·1 + U_v GᵀG, positive). It keeps energetic G (through ξ), energetic S (integer N0914 stencil), and a **compact indefinite** N-type h-potential whose small-field form is h:R(h). The weights are positive by construction. This is exactly R12-5's "compactness must stabilize the conformal-like scalar sector" (`R12-5:163`), in its sign-free form.
- Code checks: symbol 2π-periodic (8.9e-16), real (0), G/Gᵀ and S/Sᵀ adjoints (≤ 2e-13), S Gᵀ = 0 (≤ 9e-15), HMC force vs finite difference (≤ 4e-8).
- **Pre-registered fit:** z = slope of log Ω_eff(2π/L) vs log(2π/L), L ∈ {4, 6, 8}, L_t = L. Operational PRODUCED: B1 and B2 with z ∈ [0.9, 1.1], and E and both A1 channels with slope < 0.3.
- **Correction logged:** the first observable, sin θ, is gauge-variant and came out time-uncorrelated (R ≈ 1 in every channel). It was replaced at 20:37Z, before production, by the gauge-invariant electric field e = sin D on time links. With the Gaussian reading 1/G(n) = β_eff + m²/ω̂_n² (n = 1, 2) this gives Ω_eff² = m²/β_eff. The first outputs are kept in `scripts/superseded/`.
- Known contamination: in the E and A1a (zz) channels, Gᵀξ adds white noise, so their Ω_eff are not clean dispersion readings. B1, B2 and A1t are clean.

**Semiclassical result (checked; s5, s5b).**
- The static potential's minimum is a **period-2 (k = (π, π, π)) condensate** of the conformal direction with |sin θ| ≈ 1: V/site = −27.000 at L = 4, 6, 8 (2³ cell tiled and re-minimized; |∇V| ≤ 1.4e-2).
- Hessian min eigenvalue +6.0, so it is a true minimum.
- **All harmonic frequencies are gapped, ω_min = 1.7321 = √3, at L = 4, 6, 8.** κ_B = ¼, κ_s = 4 at L = 4: ω_min = 0.80, also gapped.
- Random multi-start minimization at L = 6 finds glassy local minima (V/site ≈ −21) with lower soft modes (0.27). These are not ground states.
- Reading: compactness does stabilize the conformal sector, but by crystallizing it at the lattice scale. That gaps the gravitons too.

**HMC (checked; s4, s4b; 4000 trajectories per size, 1/4 discarded).**
- Staggered order |⟨(−1)^{x+y+z} sin θ⟩| at L = 4: 0.985 (weak, β_t = κ = 4), 0.937 (mid, all 1), 0.785 (strong, all 0.4). For uncorrelated θ it would be ≈ 0.09. All three points are in the crystal phase.
- Ω_eff table and collapse fits: §6a.

### 6a. HMC results (accepted runs: acceptance ≥ 0.5; `scripts/s4c_fit.out`)

- **Rejected runs.** At L = 8 with dt = 0.03 the HMC acceptance was 0.00 (mid, strong) and 0.11 (weak); at L = 6 (weak) it was 0.27. The mid and strong L = 8 outputs are identical because the chain never left its start. These runs are kept in `scripts/rejected_acc0/` and excluded. They were rerun with dt = 0.015 and 40 steps (acceptance 0.65–0.96).

| Point (β_t = κ_B = κ_s) | L | ⟨cos D⟩ | Ω_eff B1 (TT) | B2 (TT) | E (vector)* | A1a (zz)* | A1t (xx+yy) |
|---|---|---|---|---|---|---|---|
| weak (4) | 4 / 6 / 8 | 0.86 / 0.87 / 0.83 | 1.345 / 0.519 / 0.534 | 1.100 / 0† / 0† | 0† / 0.446 / 0.256 | 0.397 / 0.612 / 0.952 | 0.331 / 1.168 / 0† |
| mid (1) | 4 / 6 / 8 | 0.56 / 0.58 / 0.55 | 0.757 / 0.419 / 0.252 | 0.267 / 0.240 / 0.014 | 0.328 / 0.153 / 0.019 | 0† / 0.202 / 0† | 0.873 / 0.467 / 0.109 |
| strong (0.4) | 4 / 6 / 8 | 0.22 / 0.27 / 0.24 | 0† / 0.297 / 0† | 0.179 / 0† / 0† | 0.241 / 0.159 / 0.068 | 0† / 0.275 / 0.103 | 0† / 0.265 / 0.110 |

\* contaminated by the auxiliary ξ white noise (Gᵀξ enters D in these channels). † fitted m² ≤ 0 within errors, i.e. the Gaussian reading fails.

- **Collapse fits (pre-registered slope over L = 4, 6, 8).**
  - weak: B1 z = 1.40; B2 has no fit (m² ≤ 0 at L = 6, 8).
  - mid: B1 z = 1.58, B2 z = 3.99, E z = 3.96, A1t z = 2.91.
  - strong: B1 and B2 have no fit; E z = 1.77.
- **Reading (checked numbers; interpretation is a reading).**
  - No point meets the operational PRODUCED: there is no point with B1 and B2 both at z ∈ [0.9, 1.1] and the partner channels not softening.
  - At the mid point every channel softens together (TT B2, vector E and scalar A1t). That is what Lemma P predicts for multiplets that share a k = 0 block. But the numbers are noisy (m² at L = 8 is at the resolution limit, ~1e-5), so this is not evidence beyond illustration.
  - The MC Ω_eff values are far below the classical ω_min = √3. Thermal/anharmonic fluctuations in the crystal are large, so the Gaussian propagator reading is unreliable here.
  - The registered L ≥ 12 target was not attempted: at L = 8 one run already takes ~6 min at acceptable acceptance.

## 7. Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| P-N1 (supplied noncompact CCR graviton, = P41/P49) | Qubit `AX:43-53` | light-like TT at tree level (R9-9); still the only known source |
| P-N3″ (sharpened P-N3): an IR fixed point whose local quadratic form is **indefinite** (conformal sign), consistent only through emergent exact constraints below a charge gap. Unbuilt. It has no sign-free product-basis Euclidean form (Lemma S), and no stable local Gaussian substitute (Theorem G) | none named; a dynamical hypothesis | possibly light-like (uncontrolled) |
| D-λ (DeWitt λ_H ≤ ⅓) | Admissibility rule content `AX:57` | sign-free q-basis; costs a dynamical scalar (helicity-0) partner |
| D-h (ferromagnetic h-potential) | Admissibility rule content `AX:57` | sign-free E-basis; costs z ≥ 2 or propagating vector partners |
| Non-local (degree-0 homogeneous) symbols, r⁻³ tails after subtracting the analytic part | Admissibility locality `AX:57` | evades Lemma P (as exact constraints do through P_TT(k̂)) |

## 8. Readings against the FIXED clauses (`TESTS:4613-4616`)

- **PRODUCED: no.** No phase with z = 1 ± 0.1 and two gapless TT polarizations without partners was found. The one sign-free model simulated (𝒟₀) is a gapped period-2 crystal semiclassically, and its MC (L = 4, 6, 8) shows no point with both TT channels at z ∈ [0.9, 1.1] and non-softening partners (§6a). The registered L ≥ 12 was not reached.
- **EXCLUDED: not reached.** No refereed no-go yet. One stated-class candidate goes to the referee:
  - **(X-G)** Lemma P + Theorem G: in 𝒢 (stable, local C⁴, cubic, PSD, 6 tensor pairs, hypothesis F for flatness), gapless TT ⇒ propagating gapless vector partners or ω_TT = O(k²).
  - **(X-S)** Lemma S + Lemma U: the N-type comparator has no sign-free 𝒮_q/𝒮_E form, and its U(1) quadratic version is unbounded below.
  - Together: every sign-free product-basis model whose IR is semiclassical (a PSD local Hessian) is in 𝒢.
  - Not covered: the strongly coupled indefinite-IR window (P-N3″), non-product bases, mixed flat kernels, the cubic A2g ⊕ A2u loophole.
- **Overall: OPEN** (matching the registered expectation, `TESTS:4617`). The registered expectation predicted the sign problem in the trace sector (confirmed, proved). It predicted "a confined phase at strong coupling" (here: a period-2 crystallized phase at all three couplings simulated, fully gapped at the classical level; the MC dispersion readings are too noisy to confirm the gap). And it predicted a weak-coupling phase with k² or k³ modes or partners (Theorem G supplies this at the Gaussian level).

**Perturbative-order statement (new rule).** No PRODUCED/PASS is claimed. Lemma P, Theorem G and Lemma S are exact statements about the quadratic (Gaussian / order-ε Trotter) level. Their exactness conditions (PSD, C⁴ symbol, cubic covariance, ferromagnetic Fourier signs) are required at that order only.

## 9. Strong-word check and scope

- **"Proved"** is used for:
  - Lemma U (two lines);
  - Lemma S (product bases, diagonal rephasing, ε → 0);
  - Lemma P (eigenvalue continuity plus Schur; cubic, finite pairs);
  - Theorem G in the cubic class under hypothesis F. Step (3) uses the numerically computed dimension 3 to identify cubic with isotropic forms; that rank is computed in floating point (SVD tolerance 1e-9), not in exact arithmetic.
- **"Checked"** is used for the general-class LP (an upper bound from sampled directions) and all numerics.
- **"No sign-free Euclidean form"** is limited to 𝒮_q and 𝒮_E. Not to all bases.
- **"Gapped crystal"** is the classical minimum (L ≤ 8) plus HMC order at L = 4. It is not a thermodynamic-limit phase diagram.
- **The Monte Carlo is far below the registered target:** L ≤ 8, not ≥ 12; noisy; two channels contaminated by ξ; the operational Ω_eff assumes a Gaussian propagator. It does not test the undeformed N-type phase (the deformation removes the scalar gauge invariance).
- **Tail clause:** the only tail statement (non-local escape) names its subtraction: the r⁻³ tail of a degree-0 homogeneous symbol after subtracting the symbol's analytic part.

## Files (`scratchpad/C5/R13-2/scripts/`)

- `common.py` — tensor basis, cubic group, N-type symbols (as R12-5 s2).
- `s1_partner_lemma.py/.out` — Lemma P on random local cubic PSD models (V1–V4).
- `s2_invariant_forms.py/.out`, `s2b_bounds.py`, `s2b_bounds_2000.out` — invariant order-k² forms, dimensions, PSD LP.
- `s3_sign_structure.py/.out` — Lemma U, DeWitt λ, Z_N Fourier signs, h:R(h) eigenvalues.
- `s4_hmc.py` — HMC of 𝒟₀. Outputs: `rejected_acc0/s4_hmc_{weak,mid,strong}.out` (L = 4, 6 accepted except weak L = 6; L = 8 rejected) and `s4_hmc_*_dt015.out` (reruns). `superseded/` holds the first (sin θ) outputs. `s4c_fit.py/.out` assembles the accepted runs and the collapse fits.
- `s4b_order.py/.out` — staggered order parameter, L = 4.
- `s5_classical_min.py/.out`, `s5_classical_min_b.out`, `s5b_tiled_min.py/.out` — classical minima and harmonic spectra.
