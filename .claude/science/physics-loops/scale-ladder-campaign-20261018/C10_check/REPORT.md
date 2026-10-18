# C10 check: lattice Hamiltonian constraints with structure functions

Provenance: a fresh-context checker of the same model family as the C10 worker (and the C9 worker and checker), so not independent in model lineage. All code is new and imports nothing from C10; the C10 runner was read only for conventions. Each load-bearing step is encoded differently:
- Model A uses quadratic-form matrices with brackets computed as QΩR − RΩQ;
- Model P and the staggered example are computed in the full phase space;
- the jet certificates are computed on Z, with shift invariance built into the ansatz and g written as linear forms in u.

Everything is exact (sympy over QQ, QQ(d₁,d₂) and cyclotomic fields; Gröbner over QQ), except the SLAC A1 line, which is 30-digit numerics on top of an exact general-antisymmetric identity. The checker's write was blocked; the supervisor saved this report from the hand-back.

**Verdict.** Every C10 formula and certificate re-derived holds. The corrections concern scope and wording:
- a missing premise: central Δ only;
- a missing hypothesis: a diagonal Π⁺-coefficient;
- an unproved "iff" in L4;
- the overclaim "small windows provably cannot solve".

**Counts: PASS = 62, FAIL = 1.** The single FAIL is the checker's own test point: a symmetric point a = b, where the four terms cancel exactly. A non-symmetric point in chk_P2 gives {H₀, H₁} = 1.

| Script | Content | Result |
|---|---|---|
| chk_A | Model A: brackets, A1, Σ∩U, Dirac algebra, A3 spot checks | 30/0 |
| chk_P | Model P: anomaly, rational points, L4, Fourier constants, P4a (central, L = 5) | 12/1 |
| chk_P2 | forward-difference anomaly at a non-symmetric point | 1/0 |
| chk_P4 | P4a (general antisymmetric L = 5, central L = 6); L3 | 3/0 |
| chk_jet | 8 jet certificates and controls | 8/0 |
| chk_stag | staggered example, L = 4, 6 | 8/0 |

Run notes:
- chk_P and chk_P3 hit the checker's 20-minute limit in the general-antisymmetric P4a simplification. chk_P4 redid that case via the chain rule.
- Two earlier chk_A bugs were the checker's own and were fixed before the counted run.

## (a) Model A: confirmed

- **Brackets.** The three bracket formulas hold for a generic circulant at L = 4, 5.
- **Theorem A1.** Holds as a polynomial identity (with {C⁺, C⁻} = 0) for general antisymmetric Δ at L = 5 and L = 4, and for SLAC at L = 5 to 2.5e−31. It holds for any L by hand.
- **Σ ∩ U is regular and Lagrangian** (central L = 4, 5; general antisymmetric L = 5). By hand, {ℓ,ℓ} = {k,k} = 0 and {ℓ_x, k_y} = 2S_xy, so it is not Lagrangian for the forward difference.
- **Dirac algebra.** Holds at the uniform background: Λ_n = λ̂_n and {H₁, H₋₁} = (λ̂₋₁ − λ̂₁)D₀ ≠ 0. The winding caveat is needed, since in the periodic sector Σm = Σn = 0 on Σ.
- **A3 spot checks.**
  - C⁺ kink anomaly: ⅛A m₀ℓ₁.
  - C⁻ kink anomaly: −⅛A n_x k_y.
  - Forward regular branches are anomalous; the forward (ℓ,n) branch is first class and reducible (rank 9).

## (b) Model P: confirmed

- **Anomaly.** −Δ_xy(a_x g_y − a_y g_x)²/(4g_x g_y), in the full phase space (L = 5, 6). A three-line hand proof gives it for every antisymmetric Δ ≠ 0 at every L. For the forward difference, {C⁺_x, C⁻_y} = −¼S a_x b_y holds strongly.
- **Rational points.** All three are reproduced: 3/784 (forward), 34583/570752 (central) and 2591839/24618825 (range 2). The points are reconstructed with values r/7 cycling through 1, −2, 3, 5, −1, 4, 2.
- **L3.** The logic is sound.
- **L4.** Confirmed with a more general abelian K (central, forward, generic circulant). c̄(m,n) = λ̂_n − λ̂_m, and (S) holds for L = 5–8. The sign is opposite to C9's, as predicted.
- **P4a.** Confirmed. The on-shell anomaly equals g_x g_y F_xy.

## (c) Certificates (central Δ, on Z): all reproduced

| Class | Window, N | Result |
|---|---|---|
| g only (P5b) | a[−1,1] × g[0,0], 2 | none ([1]) |
| g only (P5d) | a[−1,1] × g[−1,1], 2 | none ([1]) |
| control (P5c) | same, 1 | consistent |
| shift-invariant (P5f) | a[−1,1] × u[−1,1], 2 | none ([1]) |
| shift-invariant (P5h) | a{0} × u[−2,0], 3 | none ([1]) |
| control (P5e) | shift-invariant (1,1), 1 | consistent |
| control, no shift invariance (P5g) | (1,1), 2 | consistent |
| shift-invariant (1,2) | a[−1,1] × u[−2,2], 2 | **consistent** (90 unknowns) |

"Consistent" means a solution exists over C; no real witness was extracted.

The staggered example is confirmed at L = 4, 6. At uniform a = A, its linear u-response is −A²e/2 on even sites and 0 on odd sites, against the continuum's −A²e/4. So the two-site average matches the continuum at linear order.

## (d) Framing

1. **"Model A first class but cheap": correct.** Add three points: only on U and only for antisymmetric Δ; the reduced phase space is 0-dimensional; and ℓ = k = 0 commute only because S = 0.
2. **"(S) is a property of a basis": correct, but sharpen it.** Under C → AC the zeroth-order constants change by conjugation plus {C, A}(Φ̄). At a common zero, translation-covariant A leaves Λ_n unchanged. So the basis dependence is exactly C9's moved-background mechanism. Suggested wording: at a background moved by the gauge flow, (S) depends on the choice of generators; first-classness depends only on Σ.
3. **Certificate premises: add these.**
   - **Central Δ only.**
   - They are local germs at u = 0. The C^N completeness argument is valid.
   - The normalisation is h(a ≡ 1, u = 0) ≠ 0.
   - The g-class rows (1,2) and (2,0) use an extra full-1/g normalisation.
   - The chiral ansatz suffices because {a, b} = S = 0.
4. **Overclaims.**
   - "Small windows provably cannot solve" is overstated. Use instead: no flat C^N germ exists in the listed windows under the stated premises; the smallest open case is shift-invariant (1,2) at N ≥ 3.
   - Name the excluded g-class windows.
   - L4's "iff" is shown only in the "if" direction.
   - A3: "never" is shown only at L = 4, 5. "Exactly the 4 uniform branches" holds for non-degenerate components only; 48 (L = 4) and 20 (L = 5) degenerate pieces are also first class. C⁻ kinks carry −⅛A n_x k_y.
5. **Missing hypothesis in L3.** A local h needs a diagonal Π⁺-coefficient. A banded non-diagonal coefficient gives only a quasi-local h = α⁻¹β, which the certificates do not exclude.
6. **Relation to C9: accurate.** Add the sign note, the affine-ruler caveat on Z_L, and that the H/D algebra has two generators per momentum while each chiral sector has one.

**Possible strengthening (the checker's argument, not certified).** P6 holds on Z for any finite R. {h₀, H₀} = 0 is a Sylvester equation at each (k, k′), forcing M(k,k′) = 0 where ω_k ≠ ω_{k′}. A trigonometric polynomial vanishing on a dense set is zero, so h₀ = 0. This does not need Σh = H₀.

## Corrections (applied by the supervisor to `../C10_lattice_hamiltonian_constraint_structure_functions/FINDINGS.md`)

1. Central Δ.
2. Diagonal-Π⁺ hypothesis.
3. Window-specific wording.
4. Named g-class windows.
5. L4 "if".
6. A3 scope.
7. Model A qualifiers.
8. Moved-background wording.
9. Model P every-Δ anomaly, sign note, affine-ruler caveat.
10. (1,2) N = 2 consistency independently confirmed.

## Not checked

P4b and P6 re-runs; the full A3 census; P5i and P5j; the (1,2) run with continuum-response normalisation; the slow runner and `c10_jet_elim.py` outputs.
