# h2_55_b — contraction identity and the nonabelian-flow ("Gaussian connection") realisation (criteria, written
# 2026-10-29T03:18Z (file mtime), before any h2_55_b script; header time corrected at 03:19Z — it first said 03:22Z)

Owner: HINT2_55.md (claude-opus-5-5). Exact symbolic algebra only (`sympy`, including non-commutative symbols); no floats.
nice 10, single thread. Final `VERDICT: PASS` only if every gate passes AND every designed-FAIL control fires.

## Gates
- **B1 (Lemma CONTR, jet level).** su(2) with T^a = −iσ^a/2 (so [T^a,T^b] = ε^{abc}T^c, tr T^aT^b = −δ^{ab}/2). Symbols:
  field components b^a_μ, first jets b^a_{μ,ν}, second jets b^a_{μ,νρ} (symmetric in νρ), a = 1..3, μ,ν,ρ = 1..4.
  Define, for a coupling c, G^{(c)}_{μν} := ∂_μB_ν − ∂_νB_μ + c[B_μ,B_ν] and its first jet (product rule), and the flow
  field Φ^{(c)}_μ := Σ_ν(∂_νG^{(c)}_{νμ} + c[B_ν,G^{(c)}_{νμ}]) + α₀(∂_μ∂_νB_ν + c[B_μ,∂_νB_ν]) (α₀ a symbol).
  Let S_c denote "scale field and all jets by c". Gates: B1.1 G^{(1)}∘S_c ≡ c·G^{(c)}; B1.2 Φ^{(1)}∘S_c ≡ c·Φ^{(c)}
  (all components, α₀ symbolic); B1.3 E^{(1)}∘S_c ≡ c²·E^{(c)} with E := ¼Σ_{μν}Σ_a(G^a_{μν})² ; B1.4 at c = 0,
  G^{(0)} is the abelian dB (no b·b terms) and E^{(0)} is a quadratic form in the first jets.
- **B2 (gauge-rotation expansion).** Non-commutative symbols λ, D (= ∂λ), A (= A_T), scalar c. With Ω := exp(cλ) as a
  truncated series and ∂(λ^n) := Σ_{i=0}^{n−1} λ^i D λ^{n−1−i}: B2.1 (∂Ω)Ω^{−1} = cD + (c²/2)[λ,D] + (c³/6)[λ,[λ,D]] +
  O(c⁴); B2.2 A^Ω := ΩAΩ^{−1} − c^{−1}(∂Ω)Ω^{−1} with A := A_T + D has c-coefficients
  c⁰: A_T;  c¹: [λ,A_T] + ½[λ,D];  c²: ½[λ,[λ,A_T]] + ⅓[λ,[λ,D]]  (exact, through order c²).
- **B3 (colour factors).** SU(2) (f = ε) and SU(3) (T^a = −iλ^a/2, Gell-Mann λ^a; f^{abd} := −2 tr([T^a,T^b]T^d)):
  B3.1 tr(T^aT^b) = −½δ^{ab}; B3.2 Σ_{b,d} f^{abd}f^{dbe} = −N δ^{ae}; B3.3 Σ_{a,b,c}(f^{abc})² = N(N² − 1).
- **B4 (IR cancellation of the ξ-linear order-c² terms; algebraic core).** With q = 0 (k = p): B4.1
  (p²δ_{νσ} − p_νp_σ)(δ_{νσ} − p_νp_σ/p²) = 3p² (symbolic p ∈ R⁴), i.e. 2·3p² = 6p² = the tree trace;
  B4.2 the ratio (first term at q = 0)/(tree) = Σ f^{abc}f^{abc}/(N²−1) = N and (second term)/(tree) = 2·(½)·(Σ_{bd}
  f^{abd}f^{dbe} / δ^{ae}) = −N, using the B2 coefficient ½ and B3; their sum is 0 for N = 2, 3.
- **B5 (Lemma NOBS core: a lattice abelian pure gauge is not nonabelian-flat).** B5.0 for corner values λ₀ = 0, λ₁ = X,
  λ₂ = X + Y, λ₃ = Y the abelian plaquette sum (λ₁−λ₀)+(λ₂−λ₁)+(λ₃−λ₂)+(λ₀−λ₃) ≡ 0. B5.1 SU(2), X = i a σ₁,
  Y = i b σ₂ (exact closed-form exponentials): P := e^X e^Y e^{−X} e^{−Y} has 2 − tr P ≢ 0, and at a = b = π/4 the value
  2 − tr P equals a nonzero exact number (registered: printed and checked ≠ 0).
- **B6 (ξ² term: vertex antisymmetry, UV-finiteness core).** B6.1 q_μ(p−q)_ν − (p−q)_μq_ν ≡ q_μp_ν − p_μq_ν;
  B6.2 Σ_{μν}(q_μp_ν − p_μq_ν)² ≡ 2(q²p² − (q·p)²).

## Designed-FAIL controls
- **B1-F** [corrected 2026-10-29T03:21Z (file time; first typed as 03:22Z), before any h2_55_b script existed; the first version read "coupling kept in G but
  removed from the covariant derivative in Φ (i.e. ∂_νG_{νμ} only): B1.2 must fail" — that control cannot fire, because
  every commutator in Σ∂_νG^{(c)}_{νμ} still carries exactly one c, so it scales correctly]. Corrected control: G built
  with the commutator WITHOUT c (G′ := dB + [B,B]) while the covariant derivative keeps c: Φ′^{(c)} := Σ_ν(∂_νG′_{νμ} +
  c[B_ν,G′_{νμ}]). B1.2 must FAIL for Φ′ (the identity needs exactly one c per commutator).
- **B2-F** the claim "c² coefficient of the D-part is ½[λ,[λ,D]]" must be refuted by the computed series.
- **B3-F** generators −iλ^a (no ½): Σ f f must be −4N δ (≠ −N δ): gate B3.2 must fail for it.
- **B4-F** coefficient 1 (instead of ½) for [λ,[λ,A_T]]: the sum in B4.2 must be −N ≠ 0.
- **B5-F** commuting X = i a σ₁, Y = i b σ₁: 2 − tr P ≡ 0 (the non-flatness detector must report "flat").
- **B6-F** without antisymmetrisation, q_μ(p−q)_ν retains the term −q_μq_ν (quadratic in q): detector must report it.

PASS = all gates hold and all six controls fire; otherwise FAIL (reported as is).
