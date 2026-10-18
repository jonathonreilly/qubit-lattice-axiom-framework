# C3 findings: is non-locality necessary for exact lattice closure?

Provenance: a worker of the same model family; the proofs are the worker's own and are not yet checked. Saved by the supervisor from the hand-back.

| Runner | Method | Result |
|---|---|---|
| `c3_graded_algebra_groebner.py 9` | exact Gröbner over Q | PASS=17 |
| `c3_relabelling_closure_numerics.py` | numpy | PASS=58 |
| `c3_gc_leibniz.py 7 9 11` | numpy | PASS=42 |
| `c3_sine_algebra_2d.py` | numpy | PASS=9 |

The first Leibniz run is kept as a bug log: the worker's expected N′ sign was wrong, and N′ = +DN is correct.

**Answer.**
- **Non-locality is necessary:** every local or summable discretisation fails (Theorems A and C).
- **It is not sufficient:** no relabelling algebra of any range closes {G, G} exactly while matching the continuum at the longest wavelengths, on any torus with L ≥ 4 or on Z (Theorem B).
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

So Λ_n ≠ nΛ_1, and |Λ_2/Λ_1 − 2| ≥ ½ for L ≥ 4. This is an O(1) gap.

**Proof sketch.**
1. By (S), H = 2D/Λ_1, E = X_1 and F ∝ X_{−1} span an sl2.
2. The algebra is a finite-dimensional sl2-module, so its weights are integers.
3. φ = τ∘exp(iπ ad_H/L) is an automorphism fixing the sl2.
4. Its eigenvalue-1 space is an sl2-submodule. It has only even weights and a 1-dimensional weight-0 space, so it equals the sl2.
5. Every other X_n lies outside it. ∎

**Reading.** A finite-dimensional algebra cannot carry the Witt pattern beyond its sl2 core.

**Applies to:** d dimensions (via the e₁ sector and reflection covariance), Maxwell (mod Gauss), fermion bilinears, and Z (via periodic sectors). It does not need locality, bilinearity or a choice of lattice bracket.

**Certificates (Gröbner).**
- Inconsistent: (S) with Λ_2 = 2 for L = 4–9; the SLAC spectrum for L = 5, 7, 9.
- Consistent controls: L = 3 (sl2, a real exception); the affine sl2 ⋉ C² at L = 5 (shows (i) is sharp); L = 4 with Λ_2 = 0.

**Band-limited window.** The bracket is exact to 1e−16 for low-band ξ, η and φ, but fails near the band edge. The window is not invariant.

## Theorem C: the uniform part of (b) is a lattice Leibniz rule

- At uniform ξ the gravity relabelling vanishes, so (b) needs {P, H(N)} = H(N′), i.e. a·[λ(k₁) + λ(k₂) − λ′(k₁+k₂)] = 0.
- **No-go cases:** a full-support kernel forces λ to be a homomorphism Z_L → C, hence 0, for any D (SLAC included). A continuous λ with local a gives the same.
- B14 E5 and B16 T6d are exactly this failure.
- **Exact case:** SLAC with anti-aliased densities, N′ = +D_SLAC N.
- **Non-uniform ξ** (factorisation lemma): the residual is absorbed only by a lapse–strain coupling of full range R = L//2. {C, C} at order hφπ was not tested for it.

## Boundary case: the 2D sine algebra

- The Fairlie–Fletcher–Zachos algebra closes exactly, is translation-covariant and non-local, and has O(a) corrections to the continuum structure constants.
- It has no uniform translation; adjoining one breaks closure.
- So exact closure is possible only non-locally, and only for algebras with no translations and no compressions.

## Relation to earlier blocks

- B19's lattice non-closure is unavoidable at any range.
- B14 E5 and B16 T6d are instances of Theorem C.
- B15's no-go is separate.

## Caveats

- Theorem B assumes one generator per momentum and closure within span G (adding generators trivially closes).
- Field-dependent structure functions are excluded.
- In d > 1 it rests on the e₁ sector.

## Prior art

- **Confirmed:** Kato–Sakamoto–So, arXiv:0803.3121 and 0810.2360 (lattice Leibniz no-go; SLAC); Loll gr-qc/9708025.
- **Unverified:** Drell–Weinstein–Yankielowicz 1976; Karsten–Smit; Nielsen–Ninomiya; Bahr–Dittrich; Dittrich; Gambini–Pullin; Renteln–Smolin; Kempf; Fairlie–Fletcher–Zachos 1989; Hoppe; Koo–Saleur.
- **Theorem B's exact statement** was not found in a brief search; treat it as new to us.
