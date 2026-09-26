# The sea's static response is continuous at q = 0; member plus sea gives way to every long shear wave

Task `J:derive:the-seas-long-wavelength-shear-response-exactly:a2` · worker `w-jonathonsmac4f50-j9cf0` · model
`claude-opus-5-5` · checker `check.py` (about 3 min; parts A–C exact, part D floating point and marked `[float]`).

**Provenance.**
- Probe #9198 (`w-macbookpro9927a-j5403`) is Claude Opus 5.5 on another machine.
- Block 155 is the supervisor's harvest of #9198's exact part.
- Everything here is the same model family, so a referee from another family is needed.

I took #9198's formula for the static response from its Step 8 and re-derived it (A1–A2). Its q² values are
reproduced by a different method (D).

## (1) The exact statement attempted

**Setting.** Block 62 as landed:
- H = ½Σ_j{E^j(x)·σ, S_j}, with S_j = (T_j − T_j†)/(2i), whose symbol is s_j = sin k_j;
- h = −(ε + εᵀ);
- R₂ is the landed quadratic form in p = 2 sin(q/2);
- the member's static energy for a strain wave is the landed −K R₂ form, with K > 0.

The frame is E = 1 + ε cos(q·x) with ε symmetric. The free sea fills every negative-energy state. The second-order
energy per site is

    E2(q) = −⟨F(k,q)⟩,
    F = [|w|²(ab + s·s′) − 2(s·w)(s′·w)] / (ab(a+b)),
    s = s(k), s′ = s(k+q), a = |s|, b = |s′|, w = ¼ε(s + s′).

- **(2)** E2 is continuous at q = 0, and lim_{q→0} E2(q) = ½ E_unif^{(2)}(ε), the cos² mean of the uniform
  second-order form.
- **(3)** For every K > 0 and every transverse-traceless (TT) shear wave, member plus sea has negative second-order
  energy once the wavelength is long enough.
- **(1)** Is the q² part relabelling-invariant? This is decided in floating point only. The exact reduction is given;
  the certification is open.

## (2) Steps

1. **PROVED + CHECKED A1 (vertex).**
   - ⟨k′|f(x)σ_a S_j|k⟩ = σ_a f̂(k′−k) s_j(k), and ⟨k′|S_j f σ_a|k⟩ = σ_a s_j(k′) f̂(k′−k).
   - With f = ε cos(q·x), f̂(±q) = ε/2. So ⟨k+q|V|k⟩ = σ·w with w = ¼ε(s + s′).
2. **PROVED + CHECKED A2 (two-level element).** |⟨+,n′|σ·w|−,n⟩|² = Tr[P₊(n′)σ·w P₋(n)σ·w] =
   [|w|²(1+n·n′) − 2(n·w)(n′·w)]/2.
   - Only interband transitions (−,k) → (+,k±q) are allowed; intraband ones are Pauli-blocked. The two directions
     give equal averages, which yields F. This is second-order Rayleigh–Schrödinger theory for a Slater
     determinant: ASSUMED standard, and validated numerically by #9198 against exact diagonalisation on a 6³ torus.
3. **PROVED (bound; B1 spot-checks it exactly).** Write N for the numerator.
   - N = 2ab·|⟨+,n′|σ·w|−,n⟩|² ≥ 0.
   - s·s′ ≤ ab and |(s·w)(s′·w)| ≤ ab|w|², so N ≤ 4ab|w|².
   - |w| ≤ ‖ε‖(a+b)/4.
   - Hence **0 ≤ F ≤ ‖ε‖²(a+b)/4 ≤ (√3/2)‖ε‖²**, uniformly in k and q.
4. **PROVED + CHECKED A3–A4 (pointwise limit).**
   - For k away from the eight Dirac points, a > 0 and b → a as q → 0, so F(k,q) → F(k,0) =
     (a²|εs|² − (s·εs)²)/(4a³).
   - The second-order term of −|(1+ε)s| is −(r²|εs|² − (s·εs)²)/(2r³) = −2F(k,0).
   - By dominated convergence (bounded integrand, finite measure, a.e. convergence), **lim E2(q) = ½E_unif^{(2)}**.
     This is (2).
5. **PROVED (sign of the uniform form; C1).**
   - The integrand of −E_unif^{(2)} is ≥ 0 pointwise, by Cauchy–Schwarz (s·εs)² ≤ |s|²|εs|². Equality holds iff
     s(k) is an eigenvector of ε.
   - s(k) = (sin k_j) is a local diffeomorphism near k = (π/4, π/4, π/4), so its directions fill an open cone.
   - A symmetric ε for which every direction of an open cone is an eigenvector is a multiple of the identity, since
     the eigenvectors of a non-scalar symmetric matrix lie in finitely many proper subspaces.
   - Hence **E_unif^{(2)}(ε) < 0 for every ε not proportional to the identity**. This needs no lattice constants.
     Block 155's explicit form −(3A/8)Σh_ii² − (B/4)Σ_{i<j}h_ij², with A, B > 0, is consistent with it.
6. **PROVED (3), with C2–C3 checked.**
   - For a TT wave (tr h = 0, hp = 0), R₁ = p²tr h − pᵀhp = 0, so the lapse constraint holds with u = 0.
   - R₂ is homogeneous of degree 2 in p (C2), so the member's energy is at most C·K|p|²‖h‖².
   - By steps 4–5, the sea's energy tends to ½E_unif^{(2)}(−h/2) < 0.
   - So for every K > 0 there is q₀(K,h) > 0 such that member plus sea has negative second-order energy for
     0 < |q| < q₀.
   - The supervisor's prior "(3) yes, for every K" holds. At K_eff q² ~ |E_unif| the wavelength scale is
     q₀ ~ (|E_unif|/K)^{1/2}.
7. **CHECKED D1 + [float] D2 ((1), q ∥ e₃).**
   - The pointwise q-expansion of F is exact, via sin(k₃+q) and b = √(a² + Δ). Its q¹ term is odd in k₃ and
     averages to zero.
   - The q² integrand F₂ is a polynomial over a⁷ in which every monomial has degree ≥ −1, so it is integrable at the
     Dirac points.
   - Each zone moment ⟨s₁^{2i}s₂^{2j}s₃^{2l}/r^{2ν}⟩ is Γ(ν)⁻¹∫t^{ν−1}ΠM(t)dt, with the closed Bessel form
     M_n(t) = ⟨sin²ⁿk e^{−t sin²k}⟩ = e^{−t/2}2⁻ⁿΣ_j C(n,j)(−1)^j 2^{−j}Σ_i C(j,i)I_{|j−2i|}(t/2).
   - Evaluated at 80 digits, with truncation at t = 10⁷ plus a t⁻² tail:

     | Relabelling mode (q ∥ e₃) | q² coefficient of E2 | #9198 (3D grids) |
     |---|---:|---:|
     | ξ = e₁ | 0.0022837612 | 0.00228 |
     | ξ = e₃ | 0.0039357807 | 0.00395 |

     R₂ gives exactly 0 for these modes. The ξ = e₃ values differ by 1.4×10⁻⁵, slightly above #9198's stated grid
     error. The q⁰ coefficients reproduce −B/8 and −A/2.
   - That the q² coefficient equals ⟨F₂⟩ is sketched as follows:
     - on |δ| < 2|q| around each Dirac point, F, F₀, F₁ and F₂ contribute O(q⁴), because F = O(|q|) there, F₁ is
       bounded and F₂ = O(1/|δ|);
     - outside that region, the Taylor remainder is O(q³) with |∂_q³F| ≲ 1/|δ|², which is integrable in 3D.

## (3) First unresolved step

**(1) is not certified.** Two independent floating-point methods agree that the relabelling modes carry nonzero q²
energy: the 1D Bessel reduction here and #9198's 3D grids. A proof needs:
- interval enclosures of the finitely many 1D moment integrals, which are smooth integrands with an explicit
  algebraic t⁻² tail;
- the explicit third-derivative constant in the expansion sketch of step 7.

## (4) What would finish it

- Certified 1D quadrature, for example mpmath interval arithmetic with rigorous Bessel bounds, for the roughly 30
  moments in D, plus the tail bound.
- Then the sign of the combination.

(2) and (3) are complete as stated.

## ASSUMED

- The supplied framed walk and its sea.
- The landed member form and K > 0.
- Second-order Rayleigh–Schrödinger theory for the filled sea (a Slater determinant).
- The static, adiabatic reading of "lowers its energy".
