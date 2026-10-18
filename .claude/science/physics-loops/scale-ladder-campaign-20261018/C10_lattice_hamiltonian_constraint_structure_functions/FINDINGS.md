# C10 findings: first-class lattice Hamiltonian constraints with structure functions (1D periodic lattice)

Provenance: a worker of the same model family. **Unchecked.** Saved by the supervisor from the hand-back (the worker's file write was blocked). All code is new and imports nothing from earlier runners. Only the supplied models are used: a free scalar, one clock pair, two embedding pairs. No physical identification. Literature mentions are unchecked recollection; no literature search was run.

| Item | Result |
|---|---|
| `c10_runner.py` (fast) | **PASS=53 FAIL=0**, 377 s, exact (sympy over QQ and QQ(symbols), cyclotomic reduction, Gröbner, exact linear algebra). Log `c10_runner_fast.log` |
| `c10_staggered_check.py` | PASS=6 FAIL=0 |
| `c10_runner.py --slow` | still running at hand-back; output to scratch `c10/slow.log` |
| second-order test, shift-invariant (1,2) class (`c10_jet_elim.py`) | still in the Gröbner stage (127 unknowns, 195 conditions); no result |

The first fast run had FAILs from three bugs in the runner itself; the computed physics was not changed:
- two sign conventions in F1;
- a transposed index in F4b;
- the A3 branch rule applied to non-maximal pieces instead of the irreducible components.

Slow-only window results quoted below come from `exploration/` scripts, not the runner.

## Answer

- **Model A (one clock pair; phase space 4L).**
  - The naive lattice H and D are first class on an explicit translation-invariant open set for every antisymmetric Δ. They close **strongly**, with local rational structure functions.
  - At a uniform background the on-shell algebra is the Dirac algebra with δ′ → Δ, so (S) holds with Λ_n = λ̂_n.
  - This is cheap: the model has no local degrees of freedom, and the constraints factor into commuting linear constraints.
  - It fails on Σ's "kink" components, and for the forward difference on every regular component.
- **Model P (lattice parametrised field theory, two embedding pairs; real local degrees of freedom).**
  - The naive constraints are anomalous for every Δ tested, with an explicit perfect-square anomaly.
  - Where Π⁺ is solvable, first-classness is exactly a local zero-curvature equation for the Kuchař density h_x.
  - A local solution recombined with the ruler g = ΔX⁺ would give a non-abelian first-class set satisfying (S): C9's P6 mechanism.
  - Exact Gröbner certificates exclude such h for small windows, and in the class where X⁺ enters only through g.
  - In the broader shift-invariant class, flat first-order jets with the correct continuum response exist at window (1,2). Whether an exact finite-range solution exists is **open**.
- **Commuting deparametrised clocks** (H_x = P_x + h_x, with commuting h_x) are trivially first class but abelian, so they fail (S). They also freeze every energy density. Exact certificates show that no finite-range quadratic h_x sums to the lattice free-scalar Hamiltonian H₀ under {h₀, H₀} = 0, in the windows tested.

## Setup

- **Lattice and difference.** Z_L, periodic. Δ is a circulant difference with symbol λ̂_n, Δ1 = 0 and Δx = 1 (needed for winding fields). A = Δ − Δᵀ and S = Δ + Δᵀ.
- **Model A.**
  - H_x = ½(π² + (Δφ)²) − ½(P² + (ΔX)²) and D_x = πΔφ + PΔX: a string with a 2-dimensional target.
  - Light-cone form: C^± = ½(H ± D), with C⁺ = ¼ℓm and C⁻ = ¼nk, where ℓ, m = a ∓ β; n, k = b ∓ γ; a, b = π ± Δφ; β, γ = P ∓ ΔX.
- **Model P.**
  - X^± = x + u^± and g^± = 1 + Δu^±.
  - C⁺ = Π⁺g⁺ + ¼a² and C⁻ = Π⁻g⁻ − ¼b².
  - H = C⁺ − C⁻ and D = C⁺ + C⁻.
  - The C^± are a mirror pair (remark).
- **"Closes with structure functions".** This means {C_α, C_β} = Σ C_αβ^γ C_γ with C smooth on an open U. For regular constraints this is locally equivalent to first-classness by the Hadamard lemma. The on-shell C_αβ^γ are unique but are not invariant under C → AC with field-dependent A.

## Results

### Stage 1: frame, counting, automatic versus genuine

- **L1 [exact, standard; F1, F2].** Constraints ⟨p, V_a⟩ are first class iff span{V_a} is involutive. For a frame, first-classness is automatic (C9's vacuity). A non-involutive example gives −p_z ≠ 0 on Σ.
- **L2 (counting) [exact, standard].** Regular first-class constraints need m ≤ n on 2n dimensions.
  - Model A has 2L constraints on 4L dimensions. It is first class iff Σ is Lagrangian, and then the reduced phase space is 0-dimensional. This is a genuine condition.
  - Model P has 2L constraints on 6L dimensions, so the reduced dimension is 2L.
- **L3 (Kuchař form) [exact; F3].** Let C = A·K with A invertible and K_x = P_x + h_x(X, matter). Then first class ⟺ the K_x commute strongly ⟺ zero curvature F = 0. In the K basis c̄ = 0, so (S) fails.
- **L4 (basis dependence and recombination with the ruler) [exact; F4a L = 5, 6; F4b L = 4–9].**
  - If K is abelian, C_x = g_x K_x satisfies {C_x, C_y} = Δ_xy(g_y/g_x)C_x − Δ_yx(g_x/g_y)C_y strongly (C9's P6 form).
  - At g ≡ 1, c̄(m,n) = λ̂_n − λ̂_m, so Λ_n = λ̂_n.
  - (S) holds iff λ̂₁ ≠ 0 and λ̂₁ ≠ λ̂₋₁. For the central difference Λ₂/Λ₁ = 2cos(2π/L).
  - **So (S) is a property of a basis, not of Σ.** An abelianised H with D reconstructed matches the continuum at the longest wavelength in the recombined basis iff a local abelian K with the right continuum limit exists.

### Stage 2: known constructions (unchecked recollection, not evidence)

- Laddha–Varadarajan polymer parametrised field theory uses finite discrete-embedding gauge maps.
- Gambini–Pullin uniform discretisation uses a single master function.
- Bojowald et al. have a deformed algebra with structure function β.
- Brown–Kuchař dust has commuting densities with a non-free physical Hamiltonian.

**P6 [exact certificates].** Commuting X-independent h_x freeze every energy density. No range-R translation-covariant quadratic h has Σ_x h_x = H₀ and {h₀, H₀} = 0. This holds for (L, R) = (7, 1) central and forward, (8, 1) central, and (9, 2) central and forward; (11, 3) central is empty in exploration. Not proved for general L.

### Stage 3: naive lattice H, D and finite-range modifications

#### Model A

- **Brackets [exact, fully symbolic circulant Δ, L = 4, 5].**
  - {C⁺, C⁺} = ⅛A(ℓm′ + mℓ′)
  - {C⁻, C⁻} = −⅛A(nk′ + kn′)
  - {C⁺_x, C⁻_y} = ⅛S_xy(ℓ_x k_y + m_x n_y)
- **Theorem A1 [exact; A4 symbolic antisymmetric range-2 Δ at L = 5, including SLAC at L = 5; A5].** For antisymmetric Δ and U = {m_x ≠ 0, n_x ≠ 0 for all x}:
  - {C⁺, C⁻} = 0;
  - {C⁺_x, C⁺_y} = Δ_xy((m_y/m_x)C⁺_x + (m_x/m_y)C⁺_y);
  - {C⁻_x, C⁻_y} = −Δ_xy((n_y/n_x)C⁻_x + (n_x/n_y)C⁻_y).

  These hold strongly, so the set is first class on U. Σ ∩ U = {ℓ = 0, k = 0} ∩ U is regular and Lagrangian.
  - At a uniform background: {H_x, H_y} ≈ Δ_xy(D_x + D_y) and {D_x, H_y} ≈ Δ_xy(H_x + H_y). This is the Dirac algebra with δ′ → Δ, so Λ_n = λ̂_n (2cos(2π/L) for central, n̄Λ₁ for SLAC).
  - Caveat: the uniform background needs winding of φ ∓ X, as for C9's ruler.
  - Mechanism: the constraint is null and factorises, with no local degrees of freedom.
- **A3 [exact; L = 4, 5; all 2^{2L} pieces].** A kink rule decides first-classness on each irreducible component of Σ.
  - Central: exactly the 4 uniform branches are first class (2 regular, 2 reducible). Every kink component is anomalous, with anomaly ⅛A m_x ℓ_y ≠ 0.
  - Forward: only the reducible (ℓ,n) and (m,k) branches are first class. Every regular component is anomalous, via ⅛S m_x n_y.
  - So Σ as a whole is never first class.

#### Model P

- **P1–P3 [exact; L = 5: central, forward, symbolic antisymmetric range 2].**
  - On shell, for antisymmetric Δ: {C⁺_x, C⁺_y} ≈ −Δ_xy(a_x g_y − a_y g_x)²/(4g_x g_y). For non-antisymmetric Δ there is also {C⁺, C⁻} = −¼S a_x b_y.
  - At rational points of Σ, {H₀, H₁} is non-zero: 34583/570752 (central), 3/784 (forward), 2591839/24618825 (range 2).
  - The continuum counterpart of the anomaly is (x−y)²δ′ = 0.
- **P4a.** For h = a²/(4g), the curvature is F_xy = −Δ_xy(v_x − v_y)²/4, with v = a/g.
- **Finite-range searches.** Ansatz: h quadratic in the chiral field a, chiral, translation-covariant, and with a nonzero uniform value. The jet certificates impose flatness through order N−1 at the ruler, and are complete for all C^N coefficient functions in the window.

  | Class (window radii) | Result |
  |---|---|
  | Rational h = Σκ aa/g_{x+t}: (1,0), (1,1) | only h = 0 is flat (P4b) |
  | X⁺ only via g: (0,0), (1,0), (1,1), first order | **obstruction**, Gröbner [1] (P5a, b, d); control (1,1) at order 0 consistent (P5c) |
  | Same class, (1,2) and (2,0), full 1/g normalisation | obstruction [1] (exploration only) |
  | Shift-invariant: (1,1); a{0}×u[−2,0] order 2; a{0}×u[−2,2]; a[0,1]×u[−2,0] | **obstruction** (P5f, h, i, j); control at order 0 consistent (P5e) |
  | Shift-invariant (1,2), first order, with and without continuum response | **flat 1-jets exist** (exploration) |
  | Shift-invariant (1,2), second order | **not decided** |
  | No shift invariance (1,1), first order | flat jets exist (P5g); shift invariance is load-bearing |

  - The flatness equations push the uniform value and the u′-response towards the continuum speed; in one witness h → a²/4. This is suggestive only.
  - *Argument, not certified:* F = 0 is solvable order by order (Bianchi plus Poincaré), but the generic range grows with order. Every flat h is pure gauge, h_x = (∂_{u_x}G)G⁻¹.
- **Staggered example [exact; L = 4, 6, 8].** h = a_x²/4 on odd sites and h = (a_x − (u_{x+1}a_{x+1} − u_{x−1}a_{x−1})/2)²/4 on even sites. This is exactly flat with range 1, but only 2Z-covariant, not shift-invariant, and it has the wrong continuum limit site by site.

## Status

- **Exact:**
  - L1–L4;
  - Theorem A1;
  - A3 at L = 4, 5;
  - the Model P anomaly and its non-vanishing points;
  - the Kuchař reduction;
  - every certificate, each only for its stated window, L, Δ and class premises.
- **Conditional:**
  - A1 needs Δ antisymmetric and the open set U;
  - the uniform-background (S) needs winding sectors;
  - "first class ⟺ local flat h" needs a chiral C⁺ that is locally solvable for Π⁺.
- **Expected values.** The P4b/P5 expected outcomes are regression values from exploration runs; the controls show the engine finds solutions when they exist.
- **Relation to C9 and the lane note.**
  - A1 and L4 transfer C9's moved-background evasion of the arc lemma to constraints.
  - Theorems A–C are not contradicted.
  - With local degrees of freedom (PFT), the naive discretisation is anomalous, and first-classness becomes a sharp local zero-curvature problem that small windows provably cannot solve.

## Open

1. Second and higher order for the shift-invariant (1,2) class, and larger windows (`c10_jet_elim.py`).
2. An exact local G(u): a lattice "pullback by the embedding".
3. Non-chiral or non-quadratic densities; constraints not solvable for Π⁺.
4. Model A's degenerate pieces; global first-classness.
5. d > 1.
6. General-L proofs of P6 and A3.
