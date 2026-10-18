# C3 findings: is non-locality necessary for exact lattice closure?

Provenance: a worker of the same model family. Proof-critically checked by a fresh-context same-family agent (`../C3_check/REPORT.md`, PASS=49): Theorem B is confirmed and sharpened (arc lemma), and the corrections are applied below. Saved by the supervisor from the hand-back.

| Runner | Method | Result |
|---|---|---|
| `c3_graded_algebra_groebner.py 9` | exact Gröbner over Q | PASS=17 |
| `c3_relabelling_closure_numerics.py` | numpy | PASS=58 |
| `c3_gc_leibniz.py 7 9 11` | numpy | PASS=42 |
| `c3_sine_algebra_2d.py` | numpy | PASS=9 |

The first Leibniz run is kept as a bug log: the worker's expected N′ sign was wrong, and N′ = +DN is correct.

**Answer.**
- **Non-locality is necessary:** every local or summable discretisation fails (Theorems A and C).
- **It is not sufficient:** a relabelling algebra of any range that closes {G, G} exactly and matches the continuum at the longest wavelength ((S)) cannot have the continuum spectrum beyond |n| = 1 (Theorem B). Such closing algebras exist abstractly; what is lost is the continuum spectrum, not closure itself (note review F1).
- **What SLAC and band-limited constructions do give:**
  - exact sub-brackets;
  - exact closure on band-limited windows, which is not an operator identity;
  - exact (b), but only with a fully non-local lapse–strain coupling.

## Setup

- G[ξ] is linear, injective and translation-covariant, with X_n = G[e^{2πinx/L}] and D = X_0.
- **Grading:** [X_a, X_b] = c(a,b)X_{a+b}, and [D, X_n] = Λ_n X_n.

## Theorem A: the uniform–non-uniform sub-bracket

- Closure requires f(k'+p, k')[d(k'+p) − d(k') − C(p)] = 0.
- **On Z,** with d continuous (any summable kernel) and f non-zero on a dense set, d is constant. So a discontinuous symbol is needed, i.e. a non-summable kernel such as SLAC.
- **On Z_L,** the jumps of d must sit on the zeros of f.
- **SLAC** closes this sub-bracket iff f vanishes on the wrap (Umklapp) set.

## Theorem B: no exact {G, G} closure for any range (main result)

**Hypotheses.**
- Closure within one L-periodic sector, a finite-dimensional algebra with at most one generator per momentum.
- (S) Λ_1 ≠ 0 and [X_1, X_{−1}] ≠ 0, the continuum values at the longest wavelength.

**Conclusion.** For every n ∉ {0, ±1} with X_n ≠ 0:
- (i) 2Λ_n/Λ_1 ∈ Z;
- (ii) Λ_n/Λ_1 ∉ n + LZ.

So Λ_n ≠ nΛ_1.

**Sharpened (arc lemma, check).** δ_n = w_n − 2n mod 2L is a Z_{2L}-grading, and each component is a single irreducible on an arc of consecutive momenta, with Λ_n/Λ_1 = n − (arc centre). Hence Λ_2/Λ_1 ∈ {0, −½, …, −(L−4)/2}: the second mode moves opposite to the first. This is verified exactly by Gröbner for L = 4–8, without (Z).

**Proof sketch.**
1. By (S) and the grading, [X_1, X_{−1}] = c(1,−1)D ≠ 0, and Λ_{−1} = −Λ_1 is forced because ad_D is a derivation. With F = κX_{−1}, κ = 2/(Λ_1 c(1,−1)), the elements H = 2D/Λ_1, E = X_1 and F span an sl2.
2. The algebra is a finite-dimensional sl2-module, so its weights are integers.
3. φ = τ∘exp(iπ ad_H/L), with τ(X_n) = e^{−2πin/L}X_n the grading automorphism, is an automorphism fixing the sl2: φ(X_n) = exp(iπ(w_n − 2n)/L)X_n.
4. Its eigenvalue-1 space is an sl2-submodule. It has only even weights and a 1-dimensional weight-0 space, so it equals the sl2.
5. Every other X_n lies outside it. ∎

**Reading.** A finite-dimensional algebra cannot carry the Witt pattern beyond its sl2 core.

**Applies to:** d dimensions, via the e₁ sector, given covariance under x_j → −x_j (j ≠ 1) and field-independent structure constants (B14's G_m qualifies); Maxwell (mod Gauss), fermion bilinears, and Z (via periodic sectors). It does not need locality, bilinearity or a choice of lattice bracket.

**Certificates (Gröbner).**
- Inconsistent: (S) with Λ_2 = 2 for L = 4–9 with the extra hypothesis (Z), and for L = 4–8 without it (check). Also the SLAC spectrum for L = 5, 7, 9.
- Consistent controls: L = 3 (sl2, a real exception); sl2 ⋉ C² (special affine) at L = 5 (shows (i) is sharp); L = 4 with Λ_2 = 0.

**Band-limited window.** The bracket is exact to 1e−16 for low-band ξ, η and φ, but fails near the band edge. The window is not invariant.

## Theorem C: the uniform part of (b) is a lattice Leibniz rule

- At uniform ξ the gravity relabelling vanishes, so (b) needs {P, H(N)} = H(N′), i.e. a·[λ(k₁) + λ(k₂) − λ′(k₁+k₂)] = 0.
- **No-go cases:** a full-support kernel forces λ − λ(0) to be a homomorphism Z_L → C, hence 0. λ(0) = 0 because D annihilates constants, so λ = 0 for any D (SLAC included). A continuous λ with local a gives the same.
- B14 E5 and B16 T6d are exactly this failure.
- **Exact case:** SLAC with anti-aliased densities, N′ = +D_SLAC N.
- **Non-uniform ξ** (factorisation lemma): the residual is absorbed only by a lapse–strain coupling of full range R = L//2. {C, C} at order hφπ was not tested for it.

## Boundary case: the 2D sine algebra

- The Fairlie–Fletcher–Zachos algebra closes exactly, is translation-covariant and non-local. In the Weyl-ordered basis its structure constants are (N/π) sin(πs/N), so the corrections are O(a²); the earlier O(a) was a basis artefact.
- It has no uniform translation; adjoining one breaks closure.
- So exact closure is possible only non-locally, and only for algebras with no translations and no compressions.

## Relation to earlier blocks

- B19's lattice non-closure, with the continuum spectrum kept, is unavoidable at any range.
- B14 E5 and B16 T6d are instances of Theorem C.
- B15's no-go is separate.

## Caveats

- Theorem B assumes one generator per momentum and closure within span G (adding generators trivially closes).
- Field-dependent structure functions are excluded.
- In d > 1 it rests on the e₁ sector.

## Prior art

- **Confirmed:** Kato–Sakamoto–So, arXiv:0803.3121 and 0810.2360 (lattice Leibniz no-go; SLAC); Loll gr-qc/9708025.
- **Unverified:** Drell–Weinstein–Yankielowicz 1976; Karsten–Smit; Nielsen–Ninomiya; Bahr–Dittrich; Dittrich; Gambini–Pullin; Renteln–Smolin; Kempf; Fairlie–Fletcher–Zachos 1989; Hoppe; Koo–Saleur.
- **Theorem B** is elementary sl2 weight theory and plausibly folklore (cf. simplicity of the Witt algebra; Witt–Zassenhaus W(1;1) in characteristic p; Mathieu; Iohara; Su–Zhang–Zhao). Present it as a new-to-us elementary lemma.
