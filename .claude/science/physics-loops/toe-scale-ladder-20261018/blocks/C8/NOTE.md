# C8: lattice Sakharov coefficient of the supplied two-qubit Dirac walk

**Block:** C8 of `toe-scale-ladder-20261018` (R3 → R4).
**Status:** worker note, single author. Not independently reviewed. Unaudited.
**Runners** (all in `scripts/`; logs in `logs/`; `scripts/run_all.sh` writes `logs/run_all.log`,
which ends with the combined `TOTAL:` line):
`c8_exact.py` (sympy identities), `c8_core.py` (the lattice response), `c8_lattice.py`
(production runs, checkpointed to `logs/c8_results.json`), `c8_report.py` (certificates and
pre-registered checks), `c8_ed_check.py` (independent exact-diagonalisation check),
`c8_continuum.py` and `c8_continuum_exact.py` (continuum reference), `c8_tt_mass.py` (q⁰ diagnostic).
The pre-registration (coupling, observable, normalisation, comparison criteria) is at the
top of `WORKLOG.md`. It was written before any coefficient was computed.

## Result in one paragraph

Couple the walk's exact generator H_a (C7 Theorem A) to a static spatial metric through its
spin frame at link midpoints (coupling **M1**, a supplied premise). The induced
Einstein–Hilbert coefficient is then an exact Brillouin-zone number. Per walk (one infrared Dirac
fermion, with its lattice doublers included), in c = ħ = 1 units, the isotropic average is

  **c_G ≡ a²/(16πG_ind) = 7.36673×10⁻³ (b\*), 6.63451×10⁻³ (b_iso)**, certified to < 2×10⁻⁷ relative.

So **G_ind > 0**: the induced gravity is attractive. The sign is positive in every channel, for
every coupling tried, at b\* and b_iso. Then **a/l_P = √(16π N_f c_G) = 0.6085 √N_f (b\*) and
0.5775 √N_f (b_iso)**, with N_f symbolic. In heat-kernel language this is an effective cutoff
Λ_eff = 0.84 π/a (b\*) or 0.80 π/a (b_iso). Two caveats limit the result, and both are results
in their own right.
1. **The coefficient is not unique.** Four couplings with the same continuum limit (minimal
   coupling, proved) give c_G^iso between 3.60×10⁻³ and 9.52×10⁻³, a factor 2.6.
2. **The induced spin-2 stiffness is cubic-anisotropic.** The polarisation-summed TT stiffness
   varies by 25% (b\*) and 55% (b_iso) over q directions. The static induced action is
   therefore not Einstein–Hilbert at O(∂²). It is EH plus O(1) cubic-symmetric
   Lorentz-violating terms.

The lapse channel, by contrast, has exactly zero O(q²) response (Lemma L), as covariance requires.

## 0. Premises (named, not derived)

- **P1–P3** (as in C7): two-qubit site (outside the one-qubit axiom, parked owner fork 4),
  the Clifford walk family U = f + i h·τ + iτ₃ g·σ of the parent note, and the scaling
  τ = a with mass angle θ = m a. Named points b\*, b_iso and b_gold as in C7.
- **P4 (metric coupling, supplied).** This is the declared coupling M1 below. The variants
  M2–M4 are computed only to expose non-uniqueness. None was selected by its output.
- **P5 (observable identification, supplied).** The induced gravitational action is identified
  with the walk's static vacuum (Dirac-sea) quasienergy in the background:
  E_vac[γ] = −L_eff[γ] (Sakharov). The vacuum is the filled lower band of H_a.
  This is well defined for b\* and b_iso (no π-modes, C7). At b_gold it requires θ > 0 (§5).
- **Units.** Lattice units a = τ = 1, where the light speed is s (C7). Physical c = 1 requires
  τ = s a, so physical energies are lattice energies divided by s. Hence c_G = 2 c₂/s, where c₂
  is the q² coefficient of E₂/(Vol λ²) (normalisation in §2).

## 1. The coupling and its continuum limit

Write the generator (C7 Theorem A) as H_a(k) = −ρ(f) x(k)·Γ, with Γ = (τ₁, τ₂, τ₃σ₁, τ₃σ₂, τ₃σ₃)
(five anticommuting Hermitian involutions, c8_exact E4), x = (h₁, h₂, g₁, g₂, g₃) and
ρ = arccos f/√(1−f²). Its spin part is α_j 𝒫_j(k) with α_j = −τ₃σ_j and 𝒫_j = ρ g_j: this is
"the walk's own momentum". Its flavour part −ρ h·τ is a spatial scalar (the mass and the
Wilson-like term).

**Coupling M1 (declared).** Take a static spatial metric γ = 1 + h(x), with lapse 1 and shift 0,
and the symmetric triad e = γ^{−1/2} = 1 − h/2 + 3h²/8 + … Every hop of the spin part,
ψ†_{x+n} α_b A^b_n ψ_x, becomes ψ†_{x+n} α_b e_b{}^i(x + n/2) A^i_n ψ_x, where A^i_n are the
Fourier coefficients of 𝒫_i. The flavour part is not modulated. In momentum space the O(h)
vertex between k and k+q is the symbol at the **midpoint** k+q/2:
V(k+q ← k) = −½ ε_ij α_i 𝒫_j(k+q/2), for h_ij = ε_ij e^{iq·x}.

**Variants (same continuum limit).** M2: 𝒫_j → g_j (the bare walk amplitude, without ρ).
M3: 𝒫_j → s sin k_j (the naive nearest-neighbour current).
M4: V = −½ ε_ij sin k_j ∂_{k_i}H_a. M4 deforms the whole symbol, including the Wilson-like
flavour sector. Every variant uses the same midpoint rule, and any O(h²) part is midpoint-local.

**Proposition 1 (continuum limit of the coupling; proved, conditional on P1–P3).**
(i) For each of M1–M4, uniformly on |p|, |q| ≤ P, (1/a)V(a(p+q/2)) = −½ ε_ij s α_i (p+q/2)_j + O(a).
  The O(a) term is zero at the order shown for M1–M3, because g = sk + O(k³) and
  ρ = 1 + O(k²) (C7 Theorem B; c8_exact E5). For M4 it is −(a/2)(ε_ij p_i p_j) W·τ, the
  metric coupling of the Wilson term.
(ii) Midpoint quantisation of a symbol linear in p is Weyl ordering. So the continuum
  operator is δH = −¼{h_ij(x), s α_i p_j}.
(iii) The flat-measure (half-density ψ̃ = γ^{1/4}ψ) form of the covariant Dirac Hamiltonian
  −iα^a e_a{}^i(∂_i + Γ_i), with the symmetric triad, equals ½{α^a e_a{}^i, p_i} + O(h²) for
  arbitrary symmetric h(x). This is c8_exact E2, an exact sympy identity on an arbitrary spinor field. In symmetric gauge the
  axial (totally antisymmetric) spin-connection term vanishes at O(h).
Together, (i)–(iii) say the lattice coupling converges to standard minimal coupling, with light speed s, at O(h).
What is proved is convergence at the symbol level. The operator-level statement (strong
convergence of the coupled dynamics on band-limited states) would follow by the fibrewise
Duhamel argument of C7 Theorem C. I have not written it out here.

**Lemma C (O(h²) terms do not reach O(q²)).** An O(h²) coupling term that is a midpoint-local
function of h, such as 3h²/8 in M1, has a vacuum expectation equal to Σ_x of
(h h)(x + n/2) times a translation-invariant constant. For a Fourier mode that is independent
of q. In the continuum, the O(h²) remainder of (iii) contains (a) ½{e⁽²⁾, αp}, whose
expectation is local and therefore q-independent, (b) non-derivative terms ∝ α·(h∂h), whose
expectation vanishes because the vacuum current ⟨ψ†αψ⟩ is zero (parity), and (c) the axial term
∝ ψ†Σψ, whose expectation vanishes by time reversal.
**Hence c_G is determined by the second-order bubble of the O(h) vertex alone.** This is
proved for the lattice M1 and for the continuum. For M2–M4 it is part of the definition.

## 2. Observable and the exact second-order formula

For δH = λ(O_q + O_q†), the vacuum (sea) energy per unit volume is e₀ + λ² e₂(q) + O(λ³), with

  e₂(q) = −∫_BZ d³k/(2π)³ F(k, q/2) + (q-independent contact),
  F(k,t) = 2[o²(1 + â·b̂) − 2(â·o)(b̂·o)] / (E(k+tq̂) + E(k−tq̂)),

where â = x̂(k+tq̂), b̂ = x̂(k−tq̂), E = arccos f, and O = o·Γ is the vertex at the midpoint k.
This is standard second-order perturbation theory, −Σ|⟨exc|δH|0⟩|²/ΔE, with the Clifford
trace evaluated in closed form (c8_exact E4). F is even in t.

**Normalisation (exact, c8_exact E1).** For TT h, ∫√γ R⁽³⁾ = −¼∫(∂h)² + O(h³). The static
EH energy is E_EH = −(1/16πG)∫√γ R, so for h = 2λε cos(q·x) with ε:ε = 1 we get
E_EH/(Vol λ²) = q²/(32πG). **G > 0 means a positive q² coefficient.**
The coefficient is c_G := a²/(16πG) = 2c₂/s, where c₂ is the q² coefficient of e₂.

**Independent check (c8_ed_check.py, 15/15).** On an L = 6 periodic lattice, H_a + λ(O_q + O_q†)
is diagonalised exactly along k-chains (4L×4L matrices). Here H_a is i·Log of the explicit matrix
M U₀ M, and the M4 vertex uses a finite-difference dH. The λ² coefficient of the sea energy
matches the formula on the same k grid to 3×10⁻¹⁰–1.2×10⁻⁷ relative. This was done for M1, M2, M4
and L2, at b\*, b_iso and b_gold (θ > 0).

**Quadrature and certificate.** The q² coefficient of F is computed pointwise. F(k,t) is
evaluated at t = h, h/2 and h/4 with h = 0.05·min(1, |x(k)|), and Richardson extrapolation in
t² is applied twice. The BZ integral uses a C^∞ partition of unity: a periodic N³ midpoint grid
outside a ball |k| < κ at Γ (plus the three X points at b_gold), and Gauss–Legendre (radial,
96 points) × Gauss–Legendre (polar) × trapezoid (azimuth) inside it. The integrand behaves like
1/|k| at the massless node, which the spherical rule absorbs. Certificate: the maximum
deviation over N ∈ {96, 128}, κ ∈ {1, 1.4} and a finer inner rule (128 radial points) is
≤ 1.7×10⁻⁷ relative. This is numerical evidence with a convergence certificate. It is not
interval-rigorous. A first run with 24 radial points had 2×10⁻⁶ errors; the diagnosis is in
WORKLOG.md, and that run is kept in `logs/c8_results_run1_nr24.json`.

## 3. Results (massless members, θ = 0)

c_G per channel (×10⁻³). The channels are q ∥ (001) "z", (110) "f", (111) "d" and (123) "g".
A and B are the two TT polarisations: for z, A = (xx−yy)/√2 (E_g) and B = (xy+yx)/√2 (T_2g).

| b | coupling | zA | zB | fA | fB | dA = dB | c_G^iso | a/l_P ÷ √N_f |
|---|---|---|---|---|---|---|---|---|
| b\* | **M1** | 8.61015 | 8.30765 | 7.24188 | 6.93391 | 6.64891 | **7.36673** | **0.6085** |
| b\* | M2 | 3.79562 | 3.72509 | 3.59406 | 3.53544 | 3.50082 | 3.60420 | 0.4256 |
| b\* | M3 | 10.21345 | 8.36319 | 7.95729 | 5.00711 | 5.89405 | 7.13271 | 0.5988 |
| b\* | M4 | 7.69750 | 10.23856 | 8.70010 | 10.63185 | 9.89285 | 9.52490 | 0.6919 |
| b_iso | **M1** | 9.21430 | 8.62025 | 6.69368 | 5.29825 | 5.23328 | **6.63451** | **0.5775** |
| b_iso | M2 | 4.22548 | 4.00479 | 3.63060 | 3.37651 | 3.31937 | 3.63093 | 0.4272 |
| b_iso | M3 | 8.95833 | 7.72546 | 6.61311 | 3.98872 | 4.66497 | 6.00624 | 0.5495 |
| b_iso | M4 | 7.01512 | 9.46533 | 7.82109 | 9.98544 | 9.05168 | 8.75199 | 0.6633 |

**Cubic decomposition (exact structure, numerical coefficients).** The polarisation-summed
stiffness K(q̂) = Σ_pol c_G(q̂, ε) is an even polynomial of degree ≤ 6 in q̂. The vertex is
linear in ε, the TT projector is quartic in q̂, and the t² coefficient is quadratic in q̂. K is
also O_h-invariant, so K = A + B Σq̂_a⁴ + C q̂_x²q̂_y²q̂_z². These three invariants span the O_h
invariants of degree ≤ 6 on S². The fit on z, f and d predicts the generic (123) direction to
10⁻¹⁴ (a non-tautological test: a deliberately non-symmetric coarse rule fails it at 3×10⁻⁶).
The isotropic (EH) part is c_G^iso = ½(A + 3B/5 + C/105).
For M1: (A, B, C) = (11.434, 5.484, 0.973)×10⁻³ at b\* and (6.149, 11.685, 11.399)×10⁻³ at b_iso.
**The k⁴ dispersion isotropy of b_iso does not make the induced gravity more isotropic. It
is more anisotropic (55% vs 25%), because c_G is a UV (whole-zone) quantity.** The (111)
polarisations are degenerate, as C₃ requires (to 10⁻¹³).

**Sign (pre-registered decisive check): PASS.** c_G > 0 in every entry above, and in the (123) channels. By
Proposition 1 and the continuum computation in §6, the positive sign is the standard Sakharov
fermion sign.

**Non-uniqueness (graded per §2.7: underdetermination with explicit witnesses).** M1–M4 share
the continuum limit of Proposition 1 but differ by a factor 2.6 in c_G^iso. So the lattice
number is fixed only once the UV completion of the coupling is fixed. Proposition 1 constrains
only the O(p) part of the vertex, while c_G integrates the vertex over the whole zone.
c_G depends on b only weakly (b\* vs b_iso: −10% for M1, +1% for M2).

## 4. Lapse channel: exact zero at O(q²)

**Lemma L (proved).** Let H(k) = −ρ x·Γ be any Clifford-form generator, of any b, θ or χ, or the
continuum. Let the lapse vertex be o(k,t) = c(k,t)[x̂(k) + t² z + O(t³)], with o even in t.
Both lapse prescriptions satisfy this: L1, midpoint N·H, gives o = ρx(k), and L2,
½{N, H}, gives o = ½(ρx(k+tq̂) + ρx(k−tq̂)). Then F(k,t) = O(t⁴) pointwise, so the lapse
response has **no O(q²) term**.
*Proof.* Write N(o) = oᵀM(t)o with M = (1 + â·b̂)I − (âb̂ᵀ + b̂âᵀ), which is even in t. Put
â = m + tv + t²w + O(t³) and b̂ = â(−t), with |â| = 1, so that m·v = 0 and m·w = −v²/2. Then
â·b̂ = 1 − 2t²v² and â·m = b̂·m = 1 − t²v²/2. Hence N(m) = (2 − 2t²v²) − 2(1 − t²v²/2)² + O(t⁴) = O(t⁴).
Since M(0)m = 0 and M is even in t, N(m + t²z) = N(m) + 2t² zᵀM(t)m + O(t⁴) = O(t⁴). ∎
Numerically |c_N| < 1.2×10⁻¹² at b\* and b_iso for both prescriptions. This agrees with EH,
since for a static lapse with flat γ, √−g R = −2ΔN is a total derivative. Pre-registered
criterion 4 is met, and the lemma explains why exactly. The lemma is structural: it holds for
any two-band Clifford generator, and it says nothing specific about the walk.
The Newtonian-potential channel also needs the spatial conformal mode, which has the
known wrong sign. **It was not computed here.**

## 5. Mass dependence and b_gold

**Massive b\*, b_iso** (M1, θ = 0.2, 0.1, 0.05, twist χ = 0 and π/2; reported, not asserted).
c_G(θ) approaches c_G(0). The deviation at θ = 0.05 is about 3% (Wilson-aligned) and about 1%
(maximal twist), and it shrinks roughly like θ^0.8. Linear extrapolation recovers c_G(0) to
0.02–0.9%. The sign of dc_G/dθ follows the twist, as the C7 O(a) twist dichotomy suggests.
These are O(m a) corrections to an a⁻² coefficient, so they are irrelevant in the continuum
limit. The full table is in `logs/c8_report.log`.

**b_gold.** At θ = 0 the X triplet consists of massless π-modes (C7). The sea is then
ambiguous, and ρ(f) diverges at f = −1, so the generator coupling is singular there. I
computed only θ > 0, where U(X) = −U(0) gives π-modes at quasienergy π − θ. The partition-of-unity
balls are at Γ and at the three X points.
| θ | zA | zB | fA | fB | dA | c_G^iso (×10⁻³) |
|---|---|---|---|---|---|---|
| 0.4 | 14.695 | 14.332 | 11.217 | 11.535 | 10.199 | 11.970 |
| 0.2 | 23.777 | 22.937 | 15.049 | 15.404 | 12.298 | 16.797 |
| 0.1 | 36.218 | 34.704 | 20.097 | 20.077 | 14.714 | 23.098 |
| 0.05 | 48.265 | 46.177 | 24.882 | 24.313 | 16.834 | 29.065 |

(entries ×10⁻³; certificates ≤ 1×10⁻⁷ absolute). c_G^iso **does not converge as θ → 0**. Each
halving of θ adds 4.8, 6.3 and 6.0 (×10⁻³), consistent with logarithmic growth, about
0.009 ln(1/θ) (an empirical description, not proved). The q-axis channels grow fastest. The
origin is that the vertex ρ g of M1 is ~π/θ near X: the exact generator becomes singular at the
massless π-modes. **So M1 has no θ → 0 limit at b_gold, and the light-speed member gives no
finite Sakharov coefficient under this coupling.** At fixed θ the values are positive, and
their size is set by θ, not by the Γ cone.

## 6. Comparison with the continuum (replacing the cutoff import)

- **Heat kernel (c8_exact E3, exact).** Γ_E = −log det D = −½ log det D². With a proper-time
  cutoff s > 1/Λ² and tr a₁ = −R/3, this gives **1/(16πG) = +Λ²/(96π²) per Dirac fermion**.
  The repo note `UNIVERSAL_GR_SAKHAROV_…_2026-06-17` writes (4π)⁻²(1/3)Λ² = Λ²/(48π²). That is
  twice this value: its own corrigendum lists the ½ of det D = (det D²)^{1/2} as not evaluated,
  and here it is evaluated. With Λ = π/a the heat kernel gives c_G = 1/96 = 1.0417×10⁻².
- **Same bubble, continuum, sharp cutoff (c8_continuum_exact.py, exact sympy).** For H = α·p,
  vertex −½ε_ij α_i p_j and |k_mid| < Λ: ∫dΩ F₂ = −52π/105, so **c_G = 13Λ²/(840π²)**, which is
  (52/35)× the heat kernel. It is positive. The numerical runner agrees to 10⁻¹⁰.
  The scheme dependence of the continuum estimate is itself O(1).
- **Lattice (exact zone sum).** c_G^iso(M1) = 7.367×10⁻³ (b\*) and 6.635×10⁻³ (b_iso). These
  correspond to Λ_eff a = √(96π² c_G) = 2.642 = 0.841π (b\*) and 2.507 = 0.798π (b_iso).
  Pre-registered criterion 2 (Λ_eff/(π/a) ∈ [0.1, 10]): met. Across M1–M4, Λ_eff spans
  0.59π–0.96π.
- **q⁰ sector (diagnostic, M1 only, not pre-registered; c8_tt_mass.py).** The bubble plus the
  midpoint contact 3h²/8 gives a q → 0 TT coefficient of −0.37 (lattice units, per λ²). The
  covariant √γ structure would give −ρ_vac/2 = +2.02. The mismatch, about −2.39 a⁻⁴, is an
  induced TT "mass" term, and its sign is the destabilising one. It is the same phenomenon as
  in the continuum with a coordinate-momentum cutoff. A homogeneous TT deformation gives
  ⟨|e p|⟩ = |p|(1 + (3/20) tr h²) instead of √γ = 1 − ¼ tr h², a mismatch of (2/5)ρ_vac tr h²
  (hand computation). A fixed coordinate lattice does not count modes covariantly. Like the
  induced cosmological constant (ρ_vac = −4.03 a⁻⁴), this term would have to be cancelled by
  other sectors. Sakharov's programme assumes such cancellations; this block does not supply one.

## 7. a/l_P

Take N_f copies of the walk, each one IR Dirac fermion with its doublers included in c_G, and
no other induced contributions. Then 1/(16πG) = N_f c_G/a², so G = a²/(16π N_f c_G) and

  **a/l_P = √(16π c_G N_f)**: 0.6085 √N_f (b\*, M1), 0.5775 √N_f (b_iso, M1). The range over
  M1–M4 is 0.43–0.69 √N_f.

N_f is not fitted. Bosons, gauge fields and the cancellation sectors needed for Λ_cc and for the
TT q⁰ term (§6) would add their own (possibly negative) contributions to 1/G. This formula
counts only the walk.

## 8. Claim types

| claim | type |
|---|---|
| EH normalisation, minimal-coupling identity at O(h), heat-kernel Λ²/(96π²), Clifford trace, ρ series | exact (sympy) |
| Proposition 1 (continuum limit of M1–M4 is minimal coupling at O(h)) | proved, conditional on P1–P3, with C7 Theorem B imported |
| Lemma C (O(h²) terms are q-independent; c_G is from the bubble alone) | proved (M1 and continuum); definitional (M2–M4) |
| second-order formula | standard; independently checked by exact diagonalisation (15/15) |
| c_G values, cubic coefficients, Λ_eff, a/l_P | numerical with convergence certificate (≤ 2×10⁻⁷ rel.), not interval-rigorous |
| c_G > 0 (all channels, couplings and points computed) | numerical (margin: values are ≥ 3.3×10⁻³, errors ≤ 2×10⁻⁹) |
| non-uniqueness (factor 2.6 spread with the same continuum limit) | underdetermination with explicit witnesses |
| cubic anisotropy of the induced spin-2 stiffness | numerical; the O_h structure of K is exact |
| Lemma L (zero O(q²) lapse response) | proved theorem; numerics agree to 10⁻¹² |
| continuum sharp-cutoff 13Λ²/(840π²) | exact (sympy) |
| mass dependence, b_gold values | numerical, reported |
| q⁰ TT mismatch | numerical diagnostic (M1-specific) |
| P4 coupling, P5 observable identification | supplied premises |

## 9. Load-bearing step for independent check

1. **The vertex and its normalisation**: V = −½ε_ij α_i ρ g_j at the midpoint, together with
   c_G = 2c₂/s, where c₂ is the q² coefficient of e₂ = −∫F and h = 2λε cos(q·x). A reviewer
   should recompute c_G^iso(M1, b\*) = 7.3667×10⁻³ by a different route. One option is a
   finite-L exact diagonalisation at several commensurate q, followed by a fit of the q²
   coefficient as L → ∞. Another is an analytic q-Hessian (automatic differentiation) instead of
   pointwise Richardson.
2. **Lemma C** (no O(h²) contribution at O(q²)), which removes the contact terms from c_G.
3. The cubic-fit isotropic average ½(A + 3B/5 + C/105), using ⟨Σq⁴⟩ = 3/5 and ⟨q_x²q_y²q_z²⟩ = 1/105.

## 10. Literature (from memory; I did not re-read these)

Sakharov 1967 (Dokl. Akad. Nauk SSSR 177, 70; reprinted in Gen. Rel. Grav. 32 (2000) 365);
Visser, Mod. Phys. Lett. A 17 (2002) 977 (gr-qc/0204062), a review of induced gravity, its
sign and its regulator dependence; Adler, Rev. Mod. Phys. 54 (1982) 729, and Zee, induced
gravity from ⟨TT⟩ (the Adler–Zee formula). The regulator dependence of the induced G and the
fermion sign are textbook. As far as I know, what is specific here is the exact Brillouin-zone
coefficient for this walk, the witnessed coupling non-uniqueness, the cubic decomposition of
the induced TT stiffness, and Lemma L.
