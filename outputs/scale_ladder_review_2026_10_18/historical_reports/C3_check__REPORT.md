# C3 check (proof-critical)

Provenance: a fresh-context checker of the same model family; not an independent family. All code is new and imports nothing from C3. Saved by the supervisor from the hand-back. The aborted log `chk_thmB_arcs_L8_L9.log` was removed by the supervisor.

**Totals: PASS=49, FAIL=0.**

| Runner | Result |
|---|---|
| `chk_thmB_arcs.py 4 5 6 7` | 16 |
| `chk_thmB_arcs.py 8` | 3 |
| `chk_thmB_numeric.py 5–8` | 20 |
| `chk_thmC_ffz.py` | 10 |

## Verdicts

| Item | Verdict |
|---|---|
| Theorem B | Confirmed, sharpened |
| Theorem A | Confirmed, hypotheses tightened |
| Theorem C (uniform part) | Minor correction |
| Factorisation lemma | Not checked |
| Sine algebra | "O(a)" corrected to O(a²) |

### Theorem B

**Proof steps.**
1. [X_1, X_{−1}] = c(1,−1)D, which is non-zero. Λ_{−1} = −Λ_1 is forced because ad_D is a derivation (Gröbner R0 confirms it). With F = κX_{−1}, κ = 2/(Λ_1 c(1,−1)), the sl2 relations hold exactly.
2. Integer weights follow from Weyl complete reducibility over C.
3. τ(X_n) = e^{−2πin/L}X_n is the grading automorphism, so φ(X_n) = exp(iπ(w_n − 2n)/L)X_n.
4. The weight-0 space of g^φ is C·D, since an X_n with Λ_n = 0, n ≠ 0 has eigenvalue ≠ 1. So g^φ is irreducible and equals sl2.
5. L = 3 is a genuine exception.

**Sharpening (arc lemma; proved, and verified exactly).**
- δ_n = w_n − 2n mod 2L is a Z_{2L}-grading, and each component is a single irreducible on an arc of consecutive momenta.
- On each arc, Λ_n/Λ_1 = n − (arc centre).
- So **Λ_2/Λ_1 ∈ {0, −½, …, −(L−4)/2}**, i.e. Λ_2/Λ_1 ≤ 0: the second mode moves opposite to the first.
- **Gröbner R1:** the consistent Λ_2 set equals the arc prediction for L = 4–8, without (Z).
- **Gröbner R2:** the variety's projection equals the arc partitions for L = 4–7.
- **Numerics (LM, 400 starts):** every converged solution obeys the arcs. With Λ_2 = 2 the best residual is 2.0.

**Corrections.**
- (a) Define τ, and state that Λ_{−1} = −Λ_1 is derived.
- (b) Replace |Λ_2/Λ_1 − 2| ≥ ½ with the arc result.
- (c) The "L = 4–9" certificate used (Z). The no-(Z) checks cover L = 4–8 (checker) and L = 5–8 (worker).
- (d) Write "sl2 ⋉ C² (special affine)", not "affine sl2".

**Scope.**
- For d > 1, state the premises: covariance under x_j → −x_j for j ≠ 1, and closure within span G with field-independent structure constants. B14's G_m satisfies the reflection premise.
- The physical requirement is weaker than "matching the continuum": even Λ(2k)/Λ(k) → 2 is excluded for every k = 2π/L at which (S) holds.
- On Z, it also needs a periodic-ξ extension (pointwise c(k,q)).

### Theorem A

Confirmed. The density condition is per p and automatic for finite range. SLAC "iff" assumes f is not identically zero on the non-wrap set. Even L, p = L/2 needs a convention.

### Theorem C

- With full support, λ = const and λ′ = 2·const. So λ − λ(0) is the zero homomorphism, and λ(0) = 0 because D annihilates constants (exact nullspace, L = 4–9).
- The π symbol is −λ(−k).
- The no-wrap solution space is 2-dimensional and contains SLAC (L = 5, 7, 9).
- B14 E5 and B16 T6d as instances was not independently verified.

### Sine algebra

In the Weyl-ordered basis the structure constants are (N/π) sin(πs/N), so the deviation is O(a²) (slope −1.97). The "O(a)" was a basis artefact. "No uniform translation" strengthens: an additive Λ on Z_N² is 0.

## Novelty

Theorem B is elementary sl2 weight theory and plausibly folklore. Related:
- the Witt algebra is simple;
- Witt–Zassenhaus W(1;1) in characteristic p;
- graded algebras with 1-dimensional pieces (Mathieu; Iohara; Su–Zhang–Zhao);
- Koo–Saleur.

Present it as a new-to-us elementary lemma, not a new mathematical theorem.
