# Complete corrected argument: Finite lattice constraint examples and polynomial certificates

This is inspectable mathematical source. The canonical claim is limited to: Explicit examples, bracket identities and exact finite jet/Groebner certificates.

**Deferred continuation:** Terminal all-family curvature/constraint exclusion and unproved general Sylvester extension; complete finite obstruction argument retained. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# A one-dimensional lattice Hamiltonian constraint without local degrees of freedom is first class, but lattice parametrised field theory is anomalous, and first-classness is local zero curvature

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. A fresh-context check of the same model family confirmed every formula and certificate it re-derived and corrected the scope; those corrections are built in.
- **Exact:** L1–L4; Theorem A1; A3 at L = 4, 5; the Model P anomaly and its rational non-vanishing points; P4a; every certificate, each only for its stated window, L, Δ and class premises.
- **Conditional:** A1 needs Δ antisymmetric and the open set U. The uniform-background (S) needs a winding sector. "First class ⟺ local flat h" is shown for a C⁺ that is locally solvable for Π⁺ with a diagonal coefficient, which makes h local.
- **Open:** whether an exact finite-range shift-invariant flat Kuchař density exists.

Nothing is adopted.

## Question

The arc-lemma note (`outputs/scale_ladder_continuations_review_2026_10_18/lattice_relabelling_algebra_no_go_arc_lemma_and_non_local_leibniz_2026_10_18_full_argument.md`) (same branch) proves that a relabelling algebra with field-independent structure constants cannot carry the continuum spectrum. Its scope section records that field-dependent structure functions evade this at a background the relabellings move. Its example is momentum-linear, where closure is automatic. This note asks the same question for genuine lattice Hamiltonian constraints, which are quadratic in momenta:
- Can a one-dimensional lattice H and D be first class with field-dependent structure functions?
- If so, does the resulting algebra satisfy (S) at the longest wavelength?
- What decides first-classness once the model has local degrees of freedom?

## Answer

- **Without local degrees of freedom (Model A, one clock pair): yes, cheaply.**
  - For every antisymmetric Δ, the naive lattice H and D are first class on an explicit translation-invariant open set U (Theorem A1).
  - They close strongly, with local rational structure functions.
  - At a uniform background (winding sector) the on-shell algebra is the Dirac algebra with δ′ → Δ, so (S) holds with Λ_n = λ̂_n.
  - This is cheap. The reduced phase space is 0-dimensional, and the constraints factor into commuting linear constraints, which commute only because S = 0.
  - It fails on the kink components of Σ, and for the forward difference on every regular component (A3, L = 4, 5).
- **With local degrees of freedom (Model P, lattice parametrised field theory): the naive constraints are anomalous.**
  - The anomaly is an explicit perfect square, non-zero for every antisymmetric Δ ≠ 0 at every L (hand proof). The forward difference is also anomalous (an exact rational point at L = 5).
- **First-classness is local zero curvature.** Suppose C⁺ can be solved for Π⁺ with a diagonal coefficient, C⁺_x = α_x(Π⁺_x + h_x). Then first-classness is exactly the local zero-curvature equation F = 0 for the Kuchař density h (L3).
  - A local flat h, recombined with the ruler g = 1 + ΔX⁺, would give a non-abelian first-class set satisfying (S) (L4). This is the arc-lemma note's moved-background mechanism, now for constraints.
  - Exact Gröbner certificates exclude flat C^N germs in the listed windows (central Δ, local germs at the ruler, the chiral quadratic translation-covariant ansatz with h(a ≡ 1, u = 0) ≠ 0).
  - In the broader shift-invariant class, flat first-order jets exist at window (1,2). Whether an exact finite-range solution exists is **open**. The smallest open case is shift-invariant (1,2) at N ≥ 3.
- **Commuting deparametrised clocks** H_x = P_x + h_x with commuting h_x are trivially first class. But they are abelian, so they fail (S), and they freeze every energy density. In the windows tested, no finite-range quadratic h sums to the lattice free-scalar Hamiltonian H₀ with {h₀, H₀} = 0 (P6).

## Setup

- **Lattice and difference.** Z_L, periodic. Δ is a circulant, Δ_xy = d(y − x), with symbol λ̂_n = Σ_r d(r) ω^{nr}, ω = e^{2πi/L}. It satisfies Δ1 = 0, and "Δx = 1" is imposed as a definition in the affine (winding) sector (see L4). Write A = Δ − Δᵀ and S = Δ + Δᵀ.
  - Central: d(±1) = ±½, so λ̂_n = i sin(2πn/L). Forward: d(1) = 1, d(0) = −1. SLAC: the antisymmetric circulant with λ̂_n ∝ i n̄, n̄ ∈ (−L/2, L/2].
  - Canonical brackets {q, p} = +1.
- **Model A (one clock pair; phase space 4L).** Fields (φ, π) and one clock pair (X, P):
  - H_x = ½(π² + (Δφ)²) − ½(P² + (ΔX)²) and D_x = πΔφ + PΔX: a string with a 2-dimensional target.
  - Light-cone form: H = C⁺ + C⁻ and D = C⁺ − C⁻, with C⁺ = ¼ℓm and C⁻ = ¼nk. Here ℓ, m = a ∓ β; n, k = b ∓ γ; a, b = π ± Δφ; β, γ = P ∓ ΔX.
- **Model P (lattice parametrised field theory; phase space 6L).** Fields (φ, π) and two embedding pairs (u^±, Π^±):
  - X^± = x + u^± and g^± = 1 + Δu^±.
  - C⁺ = Π⁺g⁺ + ¼a² and C⁻ = Π⁻g⁻ − ¼b², with H = C⁺ − C⁻ and D = C⁺ + C⁻.
  - The C^± are a mirror pair (remark). For antisymmetric Δ, {a_x, a_y} = 2Δ_xy and {a_x, b_y} = S_xy = 0, so C⁺ involves only the chiral field a.
- **"Closes with structure functions".** This means {C_α, C_β} = Σ_γ C_αβ^γ C_γ strongly, with C smooth on an open set U.
  - For regular constraints this is locally equivalent to first-classness (vanishing of the brackets on Σ), by the Hadamard lemma.
  - For an irreducible regular set the on-shell values of C_αβ^γ are unique. They are not invariant under a change of generators C → MC with a field-dependent invertible matrix M.
  - (S) is the arc-lemma note's condition: Λ₁ ≠ 0 and {X₁, X₋₁} ≠ 0, where Λ_n is the zeroth-order constant c̄(0, n) at a translation-invariant background.

## Frame and counting lemmas (L1, L2)

- **L1 [exact, standard].** Momentum-linear constraints ⟨p, V_a⟩ on T*Q are first class iff the distribution span{V_a} is involutive.
  - For a frame, n constraints on an n-dimensional base, first-classness is automatic: Σ is the zero section. This is the vacuity the arc-lemma note's scope section records for its ruler example.
  - Runner: a non-involutive pair (V₁ = ∂_x, V₂ = ∂_y + x∂_z) has {C₁, C₂} = −p_z ≠ 0 on Σ; an involutive pair closes; a frame is automatic.
- **L2 (counting) [exact, standard].** Regular first-class constraints need m ≤ n on 2n dimensions (Σ is coisotropic).
  - Model A has 2L constraints on 4L dimensions. It is first class iff Σ is Lagrangian, and then the reduced phase space is 0-dimensional. This is a genuine condition, not automatic.
  - Hand computation, certified for a general circulant at L = 5: {ℓ, ℓ} = {k, k} = 0 and {ℓ_x, k_y} = 2S_xy, with rank(ℓ, k) = 2L. So {ℓ = k = 0} is Lagrangian iff S = 0. It is not Lagrangian for the forward difference.
  - Model P has 2L constraints on 6L dimensions, so a first-class version would leave a 2L-dimensional reduced space: one chiral pair per site.

## The Kuchař reduction (L3)

**Lemma L3 [exact].** Let C = M·K with M an invertible field-dependent matrix and K_x = P_x + h_x(X, matter), where P_x is the clock momentum conjugate to X_x. Then
- {K_x, K_y} = F_xy := ∂_{X_y}h_x − ∂_{X_x}h_y + {h_x, h_y}_matter, independent of P;
- the set is first class ⟺ the K_x commute strongly ⟺ F = 0 (zero curvature).

*Proof.* {P_x, h_y} = −∂_{X_x}h_y gives the formula, and it contains no P. Σ is the graph P = −h. A P-independent function vanishes on that graph iff it vanishes identically. First-classness is a property of Σ, so it can be tested in the K basis.

- In the K basis c̄ = 0, so (S) fails there.
- **Diagonal-coefficient hypothesis.** A local, diagonal coefficient, C⁺_x = α_x(Π⁺_x + h_x), gives a *local* h. The naive Model P has α = g⁺ and h = a²/(4g⁺). If C⁺ is solvable for Π⁺ only with a banded non-diagonal coefficient, C⁺ = αΠ⁺ + β, then h = α⁻¹β is quasi-local, not local. The certificates below do not exclude such h.

## Recombination with the ruler (L4)

**Lemma L4 [exact].** Let K be abelian (with h free of the embedding momenta), and let g = 1 + Δu be the ruler. Then C_x = g_x K_x satisfies, strongly on {g ≠ 0},

`{C_x, C_y} = Δ_xy (g_y/g_x) C_x − Δ_yx (g_x/g_y) C_y.`

This is the Poisson form of the ruler model in the arc-lemma note's scope section.
- At g ≡ 1, Fourier transformation gives c̄(m, n) = λ̂_n − λ̂_m, so Λ_n = c̄(0, n) = λ̂_n.
- (S) holds iff λ̂₁ ≠ 0 and λ̂₁ ≠ λ̂₋₁, since {C₁, C₋₁} = (λ̂₋₁ − λ̂₁)C₀. This holds for central and forward Δ (runner L4b, L = 4–9).
- For the central difference, Λ₂/Λ₁ = 2cos(2π/L). This is positive for L ≥ 5, against the arc lemma's Λ₂/Λ₁ ≤ 0 for constant structure.

**Reading.** The same Σ is generated by K (abelian, so (S) fails) and by gK ((S) holds).
- **At a background moved by the gauge flow, (S) depends on the choice of generators; first-classness depends only on Σ.**
- *Common zero (checker's argument, with the rescaling corrected in this consolidation; not certified by the runner).* Under C → MC, the zeroth-order constants transform with M(Φ̄), c̄′ = (M ⊗ M) c̄ M⁻¹, plus a term {C, M}(Φ̄). At a common zero (every gauge flow vanishes at Φ̄) that term vanishes. A translation-covariant M is then a circulant, diagonal in momentum with eigenvalues μ̂_n ≠ 0, so c̄′(m, n) = μ̂_m μ̂_n c̄(m, n)/μ̂_{m+n}. Hence Λ′_n = μ̂₀Λ_n: M rescales Λ_n by its uniform Fourier coefficient μ̂₀ and leaves (S) and every ratio Λ_n/Λ₁ unchanged. (The checker's "leaves Λ_n unchanged" holds only for μ̂₀ = 1. A same-family reviewer checked the formula exactly at L = 6 for the forward difference; campaign history, not a repository source.) So the basis dependence is exactly the moved-background mechanism.
- **Only the "if" direction is shown.** If a local abelian K with the right continuum limit exists, then the recombined set gK is first class and satisfies (S) with Λ_n = λ̂_n. In that basis, an abelianised H with D reconstructed matches the continuum at the longest wavelength. The converse is not shown: that every first-class local recombination with (S) comes from a local abelian K.
- **Sign note.** Here Λ_n = +λ̂_n. In the arc-lemma note's ruler example (the vector-field bracket) Λ_n = −λ_n. The opposite sign is what the cotangent lift predicts, {X_a, X_b} = −C_ab^e X_e (campaign C9, P7). Neither sign affects (S) or any ratio Λ_n/Λ₁.
- **Affine ruler.** On Z_L the ruler X⁺ = x is not periodic, so "Δx = 1" is a definition: an affine (winding) sector, as in the arc-lemma note's example.
- **Generators per momentum.** The H/D algebra has two generators per momentum, H_n and D_n; each chiral sector C^± has one.

Runner: L4a checks the identity for a non-trivial abelian K (matter plus a u-gradient term) at L = 5 (central, forward) and for a generic circulant at L = 4. L4b checks c̄, Λ_n, (S) and the central ratio exactly in QQ[ω]/Φ_L for L = 4–9.

## Model A: Theorem A1 and the kink rule

**Brackets [exact; general circulant, L = 4, 5].**
- {C⁺_x, C⁺_y} = ⅛A_xy(ℓ_x m_y + m_x ℓ_y)
- {C⁻_x, C⁻_y} = −⅛A_xy(n_x k_y + k_x n_y)
- {C⁺_x, C⁻_y} = ⅛S_xy(ℓ_x k_y + m_x n_y)

*By hand:* {ℓ, ℓ} = {m, m} = 0 and {ℓ_x, m_y} = 2A_xy, and the Leibniz rule on ¼ℓm gives the first line. The other two lines follow in the same way.

**Theorem A1 [exact; hand proof for every L; certificates for the fully general antisymmetric circulant at L = 4–8].** Let Δ be antisymmetric and U = {m_x ≠ 0, n_x ≠ 0 for all x}. Then, strongly on U:
- {C⁺, C⁻} = 0;
- {C⁺_x, C⁺_y} = Δ_xy((m_y/m_x)C⁺_x + (m_x/m_y)C⁺_y);
- {C⁻_x, C⁻_y} = −Δ_xy((n_y/n_x)C⁻_x + (n_x/n_y)C⁻_y).

So the set is first class on U, with local rational structure functions.
- Σ ∩ U = {ℓ = 0, k = 0} ∩ U is regular and Lagrangian (L2), and the reduced phase space is 0-dimensional.
- *Proof.* With A = 2Δ and S = 0, the bracket formulas give {C⁺_x, C⁺_y} = ¼Δ_xy(ℓ_x m_y + m_x ℓ_y). This equals the right-hand side, since C⁺_x = ¼ℓ_x m_x.
- At L = 5 and 7 the general antisymmetric circulant includes SLAC, so SLAC is covered exactly there.
- Control: for the forward difference {C⁺, C⁻} ≠ 0, so A1 needs S = 0.
- Mechanism: the constraint is null and factorises, with no local degrees of freedom. ℓ = k = 0 are commuting linear constraints, and they commute only because S = 0.

**Dirac algebra at a uniform background [exact].**
- At m ≡ m̄ and n ≡ n̄, the A1 structure functions give on shell:
  - {H_x, H_y} ≈ Δ_xy(D_x + D_y);
  - {D_x, H_y} ≈ Δ_xy(H_x + H_y);
  - {D_x, D_y} ≈ Δ_xy(D_x + D_y).
- This is the Dirac algebra with δ′ → Δ. In Fourier form, {D₀, H_n} ≈ λ̂_n H_n and {H₁, H₋₁} ≈ (λ̂₋₁ − λ̂₁) D₀ ≠ 0. So (S) holds with Λ_n = λ̂_n: 2cos(2π/L) for the ratio Λ₂/Λ₁ with central Δ (exact, L = 5–8), and n̄Λ₁ for SLAC (from its symbol).
- **Winding caveat.** In the periodic sector Σ_x m_x = Σ_x n_x = 0 on {ℓ = k = 0}, so a uniform background needs winding of φ ∓ X, as for the ruler. The runner gives an explicit periodic point of Σ ∩ U, so U ∩ Σ is non-empty without winding; only the uniform background needs it.

**A3: the kink rule [exact; L = 4, 5; all 2^{2L} pieces].** Σ is the union, over per-site choices, of the linear pieces with ℓ_x = 0 or m_x = 0 at each site and n_x = 0 or k_x = 0 at each site. A piece is non-degenerate if none of the unchosen factors vanishes identically on it. On every non-degenerate component a kink rule decides first-classness:
- every pair (x, y) with A_xy ≠ 0 must make the same choice at x and y, in both sectors;
- every pair (x, y) with S_xy ≠ 0 (for the forward difference this includes x = y) must pair ℓ_x = 0 with n_y = 0, or m_x = 0 with k_y = 0.

- **Central:**
  - Exactly the 4 uniform branches are first class: (ℓ,k) and (m,n) are regular (rank 2L), while (ℓ,n) and (m,k) are reducible.
  - Every kink component is anomalous. A C⁺ kink (ℓ_x = 0, m_y = 0) carries the anomaly ⅛A_xy m_x ℓ_y ≠ 0, and a C⁻ kink (k_x = 0, n_y = 0) carries −⅛A_xy n_x k_y.
- **Forward:**
  - Only the reducible (ℓ,n) and (m,k) branches are first class.
  - Every regular component is anomalous, for example the (ℓ,k) branch via ⅛S_xy m_x n_y.
- **Counts.** The rule is checked on all non-degenerate components: 64 (central) and 240 (forward) at L = 4, and 1004 at L = 5 for each difference.
- **Degenerate pieces.** At L = 4, 48 degenerate pieces (central) and 16 (forward) are also first class; at L = 5, 20 for each difference. The rule makes no claim about them.
- **Consequence.** Σ as a whole is not first class (shown at L = 4, 5). "Never first class" on kinks is shown only at L = 4, 5.

Runner: the default run checks one C⁺ kink (central, L = 4, component (ℓ,m,ℓ,ℓ | k,k,k,k)), whose only non-vanishing brackets sit on the kink bonds; one C⁻ kink (central, L = 5); and the forward regular (ℓ,k) branch. `--slow` runs the full census at L = 4, 5, central and forward.

## Model P: the anomaly

**P1 [exact; L = 5: central, forward, general antisymmetric range 2].** Strongly:
- {C⁺_x, C⁺_y} = Δ_xy Π⁺_x g⁺_y − Δ_yx g⁺_x Π⁺_y + ¼A_xy a_x a_y;
- {C⁺_x, C⁻_y} = −¼S_xy a_x b_y.

**Theorem P (anomaly) [exact; hand proof for every antisymmetric Δ ≠ 0 at every L].** For antisymmetric Δ, on Σ (with Π⁺ = −a²/(4g⁺)):

`{C⁺_x, C⁺_y} ≈ −Δ_xy (a_x g_y − a_y g_x)² / (4 g_x g_y),` with g = g⁺, and {C⁺, C⁻} = 0.

So the naive constraints are not first class for any antisymmetric Δ ≠ 0, at any L.

*Proof.*
1. P1 with Δ_yx = −Δ_xy and A = 2Δ gives Δ_xy[Π⁺_x g_y + g_x Π⁺_y + ½a_x a_y]. Substituting Π⁺ = −a²/(4g) gives the perfect square.
2. Pick x, y with Δ_xy ≠ 0; then x ≠ y. Take u^± = 0, φ = 0 and π = e_x, with Π^± fixed on shell. This point lies on Σ with g ≡ 1 and a = e_x, so the bracket is −Δ_xy/4 ≠ 0.
3. Near the witness (g^± ≠ 0), Σ is a graph over the remaining variables, so it is regular there, and a bracket that does not vanish on Σ is not in the constraint ideal.

The proof uses only antisymmetry. Runner P-hand evaluates the witness for the fully general antisymmetric circulant at L = 5, 6, 7.

- **Non-antisymmetric Δ.** The cross bracket {C⁺, C⁻} = −¼S a_x b_y also contributes, for instance for the forward difference.
- **Rational non-vanishing points [exact, L = 5].** Take values r/7, with r cycling through 1, −2, 3, 5, −1, 4, 2 over (φ, π, u⁺, u⁻) in that order, and fix Π^± on shell. Every g^± is non-zero there, and:

  | Δ | {H₀, H₁} on Σ |
  |---|---|
  | forward | 3/784 |
  | central | 34583/570752 |
  | antisymmetric range 2, d(1) = 2/3, d(2) = −1/12 | 2591839/24618825 |

- **Continuum counterpart.** The anomaly's continuum counterpart is (v(x) − v(y))²δ′(x − y) = 0, since a double zero annihilates δ′. So the anomaly is purely a lattice effect.

## P4a: the curvature of the naive Kuchař density

**P4a [exact; central L = 5, 6; general antisymmetric L = 5].** The naive C⁺ has the diagonal form α = g with h = a²/(4g). Its curvature in the chiral bracket {a_x, a_y} = 2Δ_xy is

`F_xy = −Δ_xy (v_x − v_y)² / 4,` with v = a/g.

The on-shell anomaly of Theorem P equals g_x g_y F_xy, as L3 requires.

## Finite-range flat densities: certificates

**Ansatz.**
- h is quadratic in the chiral field a, chiral, and translation-covariant: h_x = Σ_{r≤s} c_rs(·) a_{x+r} a_{x+s} with the a-offsets in a window.
- Each coefficient c_rs is a function of the embedding variables in a window around x.
- Normalisation: a non-zero uniform value, h(a ≡ 1, u = 0) ≠ 0.
- The chiral ansatz suffices because {a, b} = S = 0.

**Jet certificates.**
- The coefficients are expanded as Taylor polynomials of degree N at the ruler u = 0. Flatness F = 0 is imposed through order N − 1. F contains one u-derivative of h, so this is complete for all C^N coefficient functions in the window: the certificates exclude local C^N germs at the ruler, not only polynomials.
- The ring is taken large enough that no bracket wraps, so the computation is equivalent to one on Z.
- A Gröbner basis [1] over QQ certifies that there is no solution over C. "Consistent" means a non-trivial basis, so solutions exist over C; no real witness was extracted.

**Classes.**
- *g-only*: X⁺ enters only through g = 1 + Δu, via the variables g_{x+t} − 1. This is automatically shift-invariant.
- *Shift-invariant*: the variables are u_{x+t}, with Σ_t ∂h_x/∂u_{x+t} = 0 imposed.
- *No shift invariance*: the same, without that condition.
- A window (R_a, R_w) gives the radii of the a-offsets and of the coefficient variables. One-sided windows are written as offset ranges.

**Premises of every row:**
- central Δ only;
- local germs at the ruler u = 0;
- the normalisation h(a ≡ 1, u = 0) ≠ 0;
- the chiral quadratic translation-covariant ansatz above.

| Class | Window, N | Result | Source |
|---|---|---|---|
| rational, h = Σκ a a/g_{x+t} | (1,0), (1,1) | only h = 0 is flat | runner P4b |
| g-only | (0,0), (1,0), (1,1); N = 2 | **no flat germ** (Gröbner [1]) | runner P5a, P5b, P5d |
| g-only, control | (1,1); N = 1 | consistent | runner P5c |
| g-only, with full 1/g normalisation | (1,2), (2,0); N = 2 | no flat germ (Gröbner [1]) | campaign exploration only |
| shift-invariant | (1,1); N = 2 | **no flat germ** | runner P5f |
| shift-invariant | a{0} × u[−2,0]; N = 3 (through order 2) | **no flat germ** | runner P5h |
| shift-invariant | a{0} × u[−2,2]; N = 2 | **no flat germ** | runner P5i |
| shift-invariant | a[0,1] × u[−2,0]; N = 2 | **no flat germ** | runner P5j |
| shift-invariant, control | (1,1); N = 1 | consistent | runner P5e |
| no shift invariance, control | (1,1); N = 2 | consistent: shift invariance is load-bearing | runner P5g |
| shift-invariant | (1,2); N = 2 | **consistent**: flat first-order jets exist, independently confirmed in a second encoding | runner P5m (`--slow`); campaign check |
| shift-invariant, with continuum u′-response | (1,2); N = 2 | consistent | campaign exploration only |
| shift-invariant | (1,2); N ≥ 3 | **open** (smallest open case) | the campaign's second-order run hit its time limit |

**Wording.** No flat C^N germ exists in the listed windows under the stated premises. Nothing is claimed for other windows, for other Δ, or for quasi-local h. In particular, "small windows provably cannot solve" is not claimed.

**Suggestive only.**
- In the consistent windows the flatness equations push the uniform value and the u′-response towards the continuum density; in one witness h → a²/4.
- *Argument, not certified:* F = 0 is solvable order by order (Bianchi identity plus Poincaré lemma), but the generic range grows with the order. Every flat h is pure gauge, h_x = (∂_{u_x}G)G⁻¹, so the question is whether a local G exists: a lattice "pullback by the embedding".

## The staggered example

**[exact; L = 4, 6 (8 with `--slow`); central Δ].** Take

- h_x = a_x²/4 on odd sites;
- h_x = (a_x − (u_{x+1}a_{x+1} − u_{x−1}a_{x−1})/2)²/4 on even sites.

This h is exactly flat (F ≡ 0) and has range 1. With the opposite sign inside the bracket it is not flat (control). Mechanism: odd-site a's commute at distance 2, and the even-site density is the odd-site gauge flow applied to a_x.
- It is only 2Z-covariant and is not shift-invariant, so it lies outside the certified classes.
- At uniform a = A its linear u-response is −A²e_x/2 on even sites and 0 on odd sites, with e = Δu. The continuum density a²/(4g) gives −A²e/4. So the continuum limit is wrong site by site; only the two-site average matches at linear order.

## Deparametrised clocks (P6)

- If K_x = P_x + h_x with h_x independent of the clock and the h_x commute, the set is trivially first class. But it is abelian, so (S) fails, and {h_x, Σ_y h_y} = 0 freezes every energy density.
- **[exact certificates].** Let H₀ = ½Σ(π² + (Δφ)²). There is no translation-covariant range-R quadratic h with Σ_x h_x = H₀ and {h₀, H₀} = 0 (exact linear algebra), for:
  - (L, R) = (7, 1), central and forward (runner default);
  - (8, 1) central, and (9, 2) central and forward (runner `--slow`);
  - (11, 3) central, empty in campaign exploration only (not certified).
- Control: the naive range-1 density ½(π₀² + (Δφ)₀²) sums to H₀ but does not commute with it.
- Not proved for general L.
- *Checker's argument, not certified.* P6 holds on Z for any finite R, without needing Σh = H₀. {h₀, H₀} = 0 is a Sylvester equation at each momentum pair (k, k′), which forces the kernel to vanish wherever ω_k ≠ ω_{k′}. A trigonometric polynomial that vanishes on a dense set is zero.

## Relation to the arc-lemma note and to campaign C9

- **Upstream.** The arc-lemma note (`outputs/scale_ladder_continuations_review_2026_10_18/lattice_relabelling_algebra_no_go_arc_lemma_and_non_local_leibniz_2026_10_18_full_argument.md`) proves Theorem B (the arc lemma) under field-independent structure constants (P2), with one generator per momentum. Its scope section records campaign C9: at a background the relabellings move, field-dependent structure functions evade the arc lemma, via the momentum-linear ruler model δu = ξ(1 + Δu).
- **What this note adds.** It extends that scope section from momentum-linear relabellings to constraints quadratic in momenta.
  - Theorem A1 and L4 transfer C9's moved-background evasion to genuine lattice Hamiltonian constraints. They give first-class sets with (S) and Λ_n = λ̂_n, so Λ₂/Λ₁ = 2cos(2π/L) > 0 (central, L ≥ 5) and Λ_n = n̄Λ₁ (SLAC). Model A does this only without local degrees of freedom.
  - With local degrees of freedom (Model P) the naive discretisation is anomalous. First-classness becomes the sharp local zero-curvature problem F = 0 of L3. Under the stated premises, no flat C^N germ exists in the listed windows.
- **Not contradicted.** None of this contradicts Theorems A–C of the arc-lemma note. Their premise (P2) excludes field-dependent structure functions, and every algebra here with (S) and Λ₂/Λ₁ > 0 has them.
- **Campaign C9** (plain text; campaign history, not a repository source): P6 (the ruler model, Λ_n = −λ_n), P7 (the Poisson form and its sign) and the frame vacuity. This note's L1 and L4 are the constraint-level versions.
- The arc-lemma note's curvature-member brackets {G, C} and {C, C} are not examined here.

## Scope

- One spatial dimension, Z_L periodic. Two supplied models: Model A (a free scalar plus one clock pair) and Model P (a free scalar plus two embedding pairs), and the deparametrised clock of P6.
- Theorem A1: antisymmetric Δ, on the open set U only. The uniform background and its (S) need a winding (affine) sector.
- A3: L = 4, 5, central and forward, non-degenerate components only.
- Theorem P: every antisymmetric Δ ≠ 0 and every L. The rational points are at L = 5.
- L3 and the certificates: C⁺ locally solvable for Π⁺ with a diagonal coefficient, chiral, quadratic in a, translation-covariant, central Δ, local germs at the ruler, h(a ≡ 1, u = 0) ≠ 0, and only the listed windows.
- P6: only the listed (L, R) and the two differences.

## Not claimed

- That an exact finite-range (or local) shift-invariant flat Kuchař density exists, or that none exists beyond the listed windows.
- That small windows "provably cannot solve" in general.
- The converse of L4.
- Any statement about quasi-local h (banded non-diagonal coefficients), non-chiral or non-quadratic densities, or differences other than central in the certificates.
- First-classness of Model A on its degenerate pieces, or global first-classness of Σ.
- A3 and P6 for general L.
- Anything in d > 1.
- Any physical identification: no clock, embedding or difference operator is identified with physical time, space or gravity.

## Open

1. Second and higher order for the shift-invariant (1,2) class (N ≥ 3), and larger windows.
2. An exact local G(u) with h_x = (∂_{u_x}G)G⁻¹: a lattice "pullback by the embedding".
3. Non-chiral or non-quadratic densities; constraints not solvable for Π⁺, or solvable only with a banded non-diagonal coefficient (quasi-local h); differences other than central in the certificates.
4. Model A's degenerate pieces, and global first-classness.
5. d > 1.
6. General-L proofs of P6 and A3 (for P6, see the checker's Sylvester sketch above).
7. A certified run of the slow-only campaign windows: (11,3) for P6, the full-1/g g-class rows, and the continuum-response (1,2) row.
8. A check from a different model family, or by a human reviewer.

## Premises

- **Axioms used.** None beyond the lattice and its translations (axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)). The axioms supply no dynamics, so every constraint here is supplied.
- **Supplied.** Models A and P and the P6 clock, as defined in the setup; the circulant Δ (central, forward, SLAC, general antisymmetric); canonical brackets {q, p} = +1; the ruler background u = 0 and its affine sector.
- **Standard facts used.**
  - The Frobenius theorem; coisotropy and counting for first-class constraints; the Hadamard lemma.
  - Gröbner bases over QQ ([1] certifies inconsistency over C).
  - Exact linear algebra over QQ; cyclotomic reduction in QQ[ω]/Φ_L.
  - Taylor's theorem, for the completeness of the jet certificates for C^N germs.

## Relation to prior work

Unchecked recollection by the campaign worker; no literature search was run. These items are context, not evidence.
- Laddha and Varadarajan: polymer parametrised field theory, with finite discrete-embedding gauge maps.
- Gambini and Pullin: uniform discretisation, with a single master function.
- Bojowald and collaborators: deformed constraint algebras with a structure function β.
- Brown and Kuchař: dust, with commuting densities and a non-free physical Hamiltonian.

Novelty: L1–L3 are standard. A1 is an elementary factorisation. The new content is narrow: the exact lattice statements, the anomaly formula, the curvature formula and the window certificates under the stated premises.

## Historical packet proposal (promotion deferred)

The negative sentences:
- the naive lattice PFT constraints are not first class for any antisymmetric Δ ≠ 0 (Theorem P);
- no flat C^N germ exists in the listed windows (certificates);
- no range-R quadratic density sums to H₀ and commutes with it, at the listed (L, R) (P6);
- Model A's kink components are anomalous (A3, L = 4, 5).

- **N1: routes by which they could fail or mislead.**
  - Quasi-local h, from a banded non-diagonal coefficient.
  - Non-chiral, non-quadratic, or non-translation-covariant densities. The staggered example shows that 2Z-covariant ones exist.
  - Larger windows or higher order: the (1,2) class is consistent at first order.
  - Other differences, or backgrounds other than the ruler.
  - Infinite range.
- **N2/N3: scope.** Theorem P is proved for every L. The certificates and P6 hold only at the listed windows and sizes. A3 holds at L = 4, 5.
- **N4: inputs.** All exact: sympy over QQ and QQ(symbols), cyclotomic reduction, Gröbner bases over QQ, exact linear algebra. No floating point is used in any gating test.
- **N5: wording.**
  - "First class" means that the brackets vanish on Σ (on U where stated).
  - "Local" means finite range.
  - "Anomalous" means not first class.
  - "Flat" means F ≡ 0 to the stated order at the ruler.
  - No physical identification is made.
- **N6/N7: strongest objections.**
  - *"Model A is trivial."* Reply: yes. That is its point, and the note says so: no local degrees of freedom, a 0-dimensional reduced space, and commuting linear factors.
  - *"The certificates are tiny windows."* Reply: yes. They are stated per window. The (1,2) class is open, and is named as the smallest open case.
  - *"(S) is a basis artefact."* Reply: at a moved background, yes (L4). This note says so; first-classness is the basis-free statement.
- **N8: earlier claims.** The campaign C10 wording "small windows provably cannot solve", the unqualified "iff" in L4, and an A3 "never" not scoped to L = 4, 5 are superseded by the forms above.

## Historical checking narrative (not fresh evidence)

**Provenance.**
- The C10 worker and its checker are agents of the same model family; neither is independent in model lineage.
- The checker worked in fresh context, wrote new code that imports nothing from C10, and encoded each load-bearing step differently:
  - Model A through quadratic-form matrices;
  - Model P and the staggered example in the full phase space;
  - the jet certificates on Z, with shift invariance built into the ansatz and g written as linear forms in u.
- The checker's result was PASS = 62, FAIL = 1. The single FAIL was the checker's own degenerate test point, where four terms cancel exactly; a non-symmetric point gives {H₀, H₁} = 1.
- This note was written by the supervisor's delegate, also of the same model family. It is a consolidation, not a further check.

**Confirmed by the check.**
- Every formula and certificate it re-derived: the brackets, A1, Σ ∩ U, the Dirac algebra, the A3 spot checks, the Model P anomaly and all three rational points, L3, L4 (with a more general abelian K), P4a, and 8 jet certificates and controls.
- The staggered example.

**Corrections from the check, built in here.**
1. Central Δ for the certificates.
2. The diagonal-Π⁺ hypothesis.
3. Window-specific wording.
4. The named g-class windows.
5. L4 shown in the "if" direction only.
6. A3 scoped to L = 4, 5 and non-degenerate components, with the C⁻ kink form.
7. The Model A qualifiers: U, antisymmetric Δ, a 0-dimensional reduced space, and S = 0.
8. The moved-background wording.
9. Model P's every-Δ anomaly, the sign note and the affine-ruler caveat.
10. The (1,2) N = 2 consistency, independently confirmed.

**Not checked by the campaign check:** P4b and P6 re-runs, the full A3 census, P5i and P5j, the (1,2) run with continuum-response normalisation, and the slow runner.

**Runner provenance.**
- The runner ports the C10 worker's model builders, kink census, jet and rational-class certificates and P6 solver. It ports the checker's non-trivial abelian K for L4, its rational-point reconstruction, its chain-rule P4a encoding and its staggered response test. It imports nothing.
- New in this consolidation (same family):
  - sparse-polynomial-ring arithmetic for Model A, with A1 certified for the fully general antisymmetric circulant at L = 4–8 (the campaign covered L = 4, 5);
  - the Theorem P hand-proof witness at L = 5, 6, 7;
  - the controls A1-control and P6-control;
  - the A1-U periodic point.
- The jet certificates use the worker's encoding only, so re-running them is not the checker's independent route.
- **Review edit (same family).** L4b and A5-F originally recomputed λ̂_n from the same formula they compared against, so their c̄ and Λ_n parts were tautological. The reviewer replaced them with the Fourier coefficients computed from the matrix entries of the L4 Poisson form and of the A5 structure functions, at two sites z (so translation covariance is tested too). A sign-flipped expectation (Λ_n = −λ̂_n) now fails them. The check count is unchanged.
- **First run of this runner: TOTAL PASS = 52, FAIL = 1.** The A1-U witness point chosen for this consolidation had n₃ = 0, so it was not in U. One coordinate (X₄ = 3 → 8) was changed after seeing the result. The claim tested, that Σ ∩ U contains a periodic point, is existential, and the criterion was not changed. P5d and P5g were then moved from `--slow` into the default run.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/lattice_hamiltonian_constraint_first_class_and_zero_curvature_2026_10_18.py
python3 scripts/lattice_hamiltonian_constraint_first_class_and_zero_curvature_2026_10_18.py --slow
```

- **Default:** `TOTAL: PASS=59 FAIL=0`, about 2 min (116 s, 132 s and, after the review edit, 120 s measured; Python 3.13, sympy 1.14, single-threaded).
- **With `--slow`:** `TOTAL: PASS=68 FAIL=0`, about 10 min (608 s, 640 s and, after the review edit, 591 s measured). The extra checks are the full A3 census (4), the shift-invariant (1,2) N = 2 consistency P5m (126 unknowns, about 4.5 min), the staggered example at L = 8, and P6 at (8,1) central and (9,2) central and forward.

Runner parts:
- L: frame and counting, Kuchař form, recombination and Λ_n;
- A: Model A brackets, Theorem A1, Σ ∩ U, the Dirac algebra, A3 kinks (`--slow`: full census);
- P: Model P brackets, anomaly, hand-proof witness, rational points, P4a;
- J: rational class and jet certificates with controls (`--slow`: shift-invariant (1,2) N = 2);
- G: staggered example;
- K: P6.

Campaign material (history, not repository sources): `.claude/science/physics-loops/scale-ladder-campaign-20261018/C10_lattice_hamiltonian_constraint_structure_functions/ (unavailable historical pointer; not a proof premise)` (worker runner, fast PASS = 53, and exploration scripts) and `.../C10_check/` (PASS = 62, FAIL = 1 as described).

## Load-bearing sources

- Arc-lemma note (same branch): Theorem B and its scope section on structure functions, which this note extends (`outputs/scale_ladder_continuations_review_2026_10_18/lattice_relabelling_algebra_no_go_arc_lemma_and_non_local_leibniz_2026_10_18_full_argument.md`)
- Context, not a dependency: campaign blocks C9 (structure functions and the arc lemma) and C10 (this lane), with their same-family checks. Their packs are campaign history, not repository sources.
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
