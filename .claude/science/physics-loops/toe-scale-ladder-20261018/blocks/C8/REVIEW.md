# C8 review: lattice Sakharov coefficient of the supplied two-qubit Dirac walk

**Reviewer provenance.** A Claude subagent running the same model as the author. This is a separate
session with its own code, but it is **not** an independent-family review. Single reviewer.
**Scope read.** C8 `NOTE.md` and `WORKLOG.md` in full, all of `scripts/` and `logs/`, C7 `NOTE.md`
(§0–§6), the parent walk note (Theorems 1–4) and
`docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`
with its runner.
**Pre-registration.** The WORKLOG fixes the coupling M1, the observable, the normalisation
c_G = 2c₂/s and the comparison criteria before any number is reported. The code (c8_core
`vertex`, c8_lattice `run`) implements exactly that declaration. I found no sign of a
post-hoc change of coupling.
**Evidence.** Reviewer code is in `review_scripts/`. `run_review.sh` writes `logs/review_all.log`,
which ends with **TOTAL: PASS=54 FAIL=0**:
`r8_symbolic` 16/0, `r8_crosscheck_pointwise` 17/0, `r8_report` 21/0. The long runs are checkpointed in
`logs/r8_routeB.json` and `logs/r8_routeA.json`, and `run_queue.sh` / `run_queue2.sh` regenerate them
(one core, nice 10, each step under 20 min). Two tolerance/target slips of my own appeared in a first
pass (an S2 target of −Q²/4 where −Q²/8 is correct, and a frame-dependence threshold). Both were fixed
before the final run. The stale outputs were overwritten.

## Verdict summary

| # | claim | verdict | severity of issue |
|---|---|---|---|
| 1 | M1 vertex −½ε_ij α_i ρg_j at the midpoint; continuum limit = minimal coupling at O(h) (Prop. 1, half-density identity) | **correct** | — (one presentational note) |
| 2 | c_G = a²/(16πG) = 2c₂/s; Lemma C | **correct** | — |
| 3 | c_G^iso(M1, b\*) = 7.36673×10⁻³; sign > 0; Lemma L lapse zero | **correct** (reproduced to 1×10⁻⁷ by a different route) | — |
| 4 | repo note's 1/(48π²) should be Λ²/(96π²) per Dirac fermion; sharp-cutoff 13Λ²/(840π²) | **correct** | the repo-note defect is real but already flagged as "not evaluated" there |
| 5a | coupling non-uniqueness, cubic anisotropy | **correct, stated honestly** | — |
| 5b | headline "G_ind > 0: the induced gravity is attractive", "two caveats", a/l_P | **correct with fix** (overstated) | moderate |
| 5c | b_gold: "c_G^iso does not converge as θ → 0", "logarithmic growth", "vertex ρg ~ π/θ near X" | **incorrect** | moderate (only the b_gold paragraph; b\*/b_iso are unaffected) |

## 1. Coupling M1 and its continuum limit — correct

*Vertex.* The spin part of H_a = −ρ x·Γ is −ρ g·(τ₃σ) = α_j ρg_j, with α_j = −τ₃σ_j. With
e = 1 − h/2, the O(h) vertex is −½h_bi α_b ρg_i. I Fourier-transformed the hop
ψ†_{x+n} α A_n e(x+n/2) ψ_x myself. For e ∝ e^{iq·x} the symbol is evaluated at k + q/2, so the
midpoint rule is right. My matrix-route code reads ρg off the explicit generator,
P_j = −Tr(H τ₃σ_j)/4, with H = V diag(ω) V† from diagonalising the explicit 4×4 U(k). It
reproduces the author's F(k,t) to 1e-10 at b\*, b_iso and b_gold (θ = 0.2) (`r8_crosscheck_pointwise`).

*Prop. 1(i).* ρ = 1 + u/3 + … with u = O(k²), and g = sk + O(k³). Hence ρg = sk + O(k³), and M1–M3 have no
O(a) term. For M4 I re-derived the O(a) term ε_ij k_i k_j W·τ (up to −a/2). Correct.
*(ii)* The Weyl symbol of ½{h(x), p} has matrix elements h_q(k + q/2). Correct.
*(iii) Half-density identity, different route.* I checked it in a different formalism:
a 2-component Weyl operator σ^a e_a^i(∂_i + Γ_i) with the Euclidean 3D spin connection
Γ_i = ⅛ω_iab[σ_a, σ_b] (no Lorentzian sign bookkeeping). For arbitrary symmetric h_ij(x),
γ^{1/4} H γ^{−1/4} = ½{σe, p} + O(h²) holds exactly (S1). A control is included: dropping Γ_i breaks
the identity. There is also a structural argument. The flat-measure operator is Hermitian, so it is
½{αe, p} + M with M Hermitian, zeroth order and linear in ∂h. P and T invariance plus the vanishing of
the totally antisymmetric part of ω_{iab} = ½(∂_b h_ai − ∂_a h_bi) exclude every candidate M
(α∂h and Σ∂h are T-odd, and β∂h is P-odd). So M = 0.
*Note (no fix needed).* The NOTE is right that what is proved is symbol-level convergence. The
operator-level statement is only asserted ("would follow").

## 2. Normalisation and Lemma C — correct

- The EH normalisation is re-derived for TT modes along (110) and (111), both polarisations; the
  author checked only q ∥ z. The cell average of √γ R⁽³⁾ at O(ε²) is −Q²/8 = −¼⟨(∂h)²⟩ (S2).
  With h = 2λε cos(q·x) and ε:ε = 1, E_EH/(Vol λ²) = q²/(32πG), so 1/(16πG) = 2c₂^phys. This matches the
  standard gravitational-wave gradient energy (1/64πG)(∇h)².
- c₂ = −¼∫F₂ follows because t = |q|/2. I checked this independently: route A (below) measures the
  finite-q slope directly, without the t-convention.
- c_G = 2c₂/s. With τ = s a, E_phys = E_lat/(s a), and the lattice vertex −½h sα·k becomes
  −½h α·p at c = 1. Correct.
- **Lemma C.** For M1, the O(h²) term ⅜(h²)(x + n/2) has first-order expectation
  C_{bi,n} Σ_x (hh)_{bi}(x + n/2). For h = 2λε cos(q·x) with commensurate q ≠ 0 this equals
  2λ²(εε)Σ_n C. That is exactly q-independent, so the bubble alone gives c_G. The continuum items
  (a)–(c) are right: there are no second-derivative O(h²) terms, the vacuum current vanishes, and the
  axial term is T-odd. Correct as stated.

## 3. Recomputation of c_G(b\*) by different routes — correct

**Route B** (`r8_walk.py`, `r8_routeB.py`). This route uses none of the author's code:
- The walk is built from G(b) with a self-solved u\*. The f-row is fixed as Gφ₀, and the h-rows come
  from factorising G − (Gφ₀)(Gφ₀)ᵀ.
- The generator comes from explicit diagonalisation of U, and the bubble from an explicit band sum,
  not the Clifford trace.
- The t² coefficient comes from exact 5-point even interpolation, not Richardson.
- The zone integral uses tensor tanh-sinh quadrature on the 8 octant cubes, whose corners are all
  8 TRIMs. There is no partition of unity and no spherical rule.

| b\*, M1 | zA | zB | fA | fB | dA = dB | c_G^iso |
|---|---|---|---|---|---|---|
| reviewer n = 64 | 8.6101513 | 8.3076482 | 7.2418809 | 6.9339075 | 6.6489137 | **7.3667294** |
| NOTE | 8.61015 | 8.30765 | 7.24188 | 6.93391 | 6.64891 | 7.36673 |

(×10⁻³.) Between n = 48 and n = 64 the iso value moves by 1.5×10⁻⁹ relative, and it agrees with the
author's value to 1×10⁻⁷. The cubic form fitted on z, f and d predicts an unused direction (2,3,6)/7
to 9×10⁻¹⁴. I verified the fit inversion and ⟨Σq̂⁴⟩ = 3/5, ⟨q̂x²q̂y²q̂z²⟩ = 1/105 exactly (S5).
The anisotropy is 24.6%. a/l_P = 0.6085√N_f and Λ_eff = 0.841π/a are reproduced.

**Route A** (`r8_routeA.py`). This is a genuine finite periodic lattice: L³ with antiperiodic boundary
conditions, so the Γ node is off-grid and the sea is unambiguous. It uses the exact second-order sea
energy at **finite** q = 2πn/32 along z, with L = 64, 96, 128, 160 and L → ∞ fits. The residual at
L = 160 is ≤ 2×10⁻⁹. A q-fit c₂ + q²(a + b ln q) then gives c₂(zA) = 3.93616×10⁻³ against
c_G s/2 = 3.93666×10⁻³ (1.3×10⁻⁴), and zB agrees to 1.0×10⁻⁴. So the Taylor-coefficient definition
equals the finite-q lattice stiffness, and e₂(q) − e₂(0) > 0 at every computed q.

**Sign.** c_G > 0 in all 8 channels I computed (B6, A2).
**Lemma L.** I checked the algebra numerically on random curves in R⁵: N(m + t²z) ∝ t⁴ (S7). The lapse
L1 coefficient from my route is |c_N| ≤ 1×10⁻¹⁴ (B8). The lemma is correct, and the NOTE's own remark
is fair: it is structural and generic.

## 4. Heat-kernel factor and sharp cutoff — correct

- **Own derivation.** Z = det D, so Γ_E = −log det D = −½ log det D² = +½∫_{1/Λ²}^∞ (ds/s) Tr e^{−sD²}.
  The second heat-kernel coefficient is tr a₁ = 4(R/6 + E) with E = −R/4 (Lichnerowicz), so
  tr a₁ = −R/3. This gives Γ_E ⊃ −(Λ²/96π²)∫√g R, and S_E,EH = −(1/16πG)∫√g R then gives
  **1/(16πG) = +Λ²/(96π²)**, which is G = 6π/Λ² per Dirac fermion (S4).
- I checked E = −R/4 and the a₁ normalisation against an exact spectrum. The unit-S² Dirac heat trace
  4Σm e^{−sm²} = 2/s − 1/3 + O(s) matches (4πs)⁻¹[2·Area + s·tr a₁·Area] (S3).
- **The repo note.** Its matching line 1/(16πG) ~ (4π)⁻²(1/3)Λ²N_f = Λ²/(48π²) is the value without
  the ½, so it is too large by 2. Its "live result" G = 3π/(N_fΛ²) should be 6π/(N_fΛ²) once the ½ is
  evaluated. **This is a real factor-2 defect in the matching line.** It is not an unflagged error,
  though: the note's 2026-10-04 boundary and the 2026-09-30 corrigendum both list "the determinant
  half-factor" as open and not evaluated. C8's wording ("twice this value … its own corrigendum lists
  the ½ … as not evaluated, and here it is evaluated") is accurate and fair.
  *Suggested repo action, outside C8, for the audit lane:* the repo note could cite C8 / S4 to close
  that open item, changing 3π to 6π. This review edits no repo file.
- **Sharp cutoff.** A numerical 4×4 band-sum route with H = α·p and vertex −½ε α_i k_j gives
  ∫dΩ F₂ = −1.5558363618, against −52π/105 = −1.5558363618 (relative 2×10⁻¹¹). It is the same for zA,
  zB, dA and dB (S6). Hence c_G = 13Λ²/(840π²) = (52/35)× the heat kernel. Correct, and as the NOTE
  says, the O(1) scheme dependence of the continuum reference is itself a result.

## 5. Scope and honesty

**5a. Correct and honest.** The factor 2.6 spread over M1–M4, with the same proved continuum limit,
is shown with explicit witnesses and is not hidden. The cubic anisotropy (25% at b\*, 55% at b_iso,
reproduced at b\*) and its "EH plus O(1) Lorentz-violating terms" reading are appropriate.
c_G^iso is the direction average of K/2. That is a convention for projecting an anisotropic stiffness
onto EH; the NOTE uses it consistently. Stating it as a convention would be cleaner (minor).

**5b. Overstated headline (moderate). Fix suggested.**
- "G_ind > 0: the induced gravity is attractive" rests on the TT q² stiffness alone. It holds only if
  the induced static action is Einstein–Hilbert.
- §6 shows it is not. There is a destabilising TT q⁰ term of about −2.39 a⁻⁴, plus an induced vacuum
  energy ρ_vac = −4.03 a⁻⁴. At physical q ≪ 1/a both dominate the O(a⁻²q²) term by (qa)⁻².
- The Newtonian channel, which needs the conformal mode with its known wrong sign, was not computed.
- So the result-paragraph's "Two caveats limit the result" should be **three**: add the non-covariant
  q⁰ TT term, which must be cancelled by other sectors. The sentence should read "positive TT (spin-2)
  stiffness; attractive only if the q⁰ and conformal sectors are fixed by other contributions".
- a/l_P = √(16πN_f c_G) is computed correctly, and §7 caveats it honestly (walk-only, N_f symbolic).
  The headline should carry the coupling range 0.43–0.69√N_f next to 0.6085√N_f, because the
  number is fixed only once the UV coupling is fixed (§3's own conclusion).

**5c. b_gold section (§5): incorrect conclusion and mechanism (moderate).**
- The NOTE's numbers at θ = 0.4–0.05 are correct. I reproduce θ = 0.2 and 0.05 to 3×10⁻⁵ (G1).
- **The θ → 0 limit exists.** With route B (X points at octant corners, tanh-sinh clustering):

  | θ | 0.05 | 0.0125 | 0.003 | 0 |
  |---|---|---|---|---|
  | c_G^iso (×10⁻³) | 29.068 | 35.956 | 38.156 | **38.894** |

  At θ = 0, n = 48 and n = 64 agree to 1×10⁻⁶ (G2). The approach is |c(θ) − c(0)| ∝ θ^{0.87–0.97}, not
  logarithmic (G3). The "about 0.009 ln(1/θ)" description was fitted only on pre-asymptotic points.
- **The mechanism is wrong.** |ρg| = E|g|/|x| ≤ E ≤ π identically, because |g| ≤ |x| = √(1−f²). The
  M1 vertex is bounded near X. It is not ~π/θ (G4: maximum 3.1403).
- **Power counting.** At θ = 0, near X, F₂ ~ 1/|δk|² (direct probe: |F₂|δk² → 0.091). That is
  integrable in 3D.
- **Fix.** Replace "does not converge … logarithmic … no finite Sakharov coefficient" with: "c_G^iso
  converges to ≈ 3.889×10⁻² as θ → 0 (approached roughly linearly in θ), even though H_a itself is
  non-analytic at the f = −1 points, which are of measure zero. That gives a/l_P ≈ 1.40√N_f, Λ_eff ≈ 1.93π/a."
- The single-tick-clock caveat on the π-modes (C7 §5) remains a legitimate reason to treat b_gold
  separately.
- **Minor.** At b_gold W = 0, so the twist angle χ is undefined. The author's "χ = π/2" is the second
  axis of a numerically produced h-plane frame. Results depend on this choice only at the 10⁻⁴ level
  (frame comparison at θ = 0.05: 8.5×10⁻⁵), but the NOTE should state the convention.

**Mass dependence (§5, b\*, b_iso).** This part was not re-verified independently. The data and the
retracted ad-hoc check are reported transparently in the WORKLOG.

## Required / suggested edits (NOTE)

1. §5 b_gold: replace the non-convergence and log-growth claim and the "vertex ~ π/θ" mechanism as in 5c
   (required).
2. Result paragraph and §7: add the q⁰ TT term and ρ_vac as a third caveat, change "attractive" to
   "positive TT stiffness (attractive if EH)", and quote the coupling range next to a/l_P (required).
3. State the c_G^iso projection convention and the b_gold mass-direction convention (minor).

With 1–2 applied, claims (1)–(4) stand as stated. The headline numbers 7.36673×10⁻³ (b\*) and the
continuum references are confirmed by two routes different from the author's.
