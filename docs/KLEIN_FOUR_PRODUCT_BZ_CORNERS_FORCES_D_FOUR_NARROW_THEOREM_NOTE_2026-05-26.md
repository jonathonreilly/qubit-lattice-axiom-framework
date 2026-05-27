# Klein-Four × Klein-Four BZ-Corner Factorization Forces `d = 4` Narrow Theorem

**Date:** 2026-05-26
**Claim type:** positive_theorem
**Claim scope:** the standalone finite-group / integer-arithmetic
identity that, for integers `d ≥ 2`, the `2^d`-element Brillouin-zone
corner set `{0, π}^d ≅ (Z_2)^d` (as elementary abelian 2-group)
admits an internal direct-product factorization into **two equal-
cardinality factors, each isomorphic to the Klein-four group**
`V_4 = Z_2 × Z_2`, **if and only if** `d = 4`. Equivalently, the
equation

```text
(Z_2)^d  ≅  V_4 × V_4                                              (F)
```

(direct-product decomposition with each factor equal to `V_4`, not
merely "an elementary abelian 2-group") holds among integers `d ≥ 2`
exactly at `d = 4`. The forward direction is the elementary-abelian
classification: `(Z_2)^4 = (Z_2)^2 × (Z_2)^2 = V_4 × V_4`. The
converse is the rank-comparison: at any `d ≠ 4`, either the total
cardinality `2^d ≠ 16` (so no factorization into two order-4
factors), or `d = 4` is forced by `|V_4 × V_4| = 16 = 2^4`. The
result is purely a statement about the structure of elementary
abelian 2-groups under direct-product decomposition; no Brillouin-
zone physics, no taste-cube projection, no Wick-rotation premise,
and no upstream framework axiom enter the load-bearing argument.

**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; later status is generated
by the audit pipeline after independent review.
**Source-note proposal disclaimer:** this note is a source-note
proposal; audit verdict and downstream status are set only by the
independent audit lane.
**Primary runner:** [`scripts/audit_companion_klein_four_product_bz_corners_forces_d_four_exact_2026_05_26.py`](../scripts/audit_companion_klein_four_product_bz_corners_forces_d_four_exact_2026_05_26.py)
**Authority role:** narrow class-(A) finite-group / integer-
arithmetic identity that isolates the **balanced V_4 × V_4
factorization condition** for the `2^d`-element BZ-corner set
`{0, π}^d ≅ (Z_2)^d`. This is a **stand-alone algebraic fact** about
elementary abelian 2-groups. Its load-bearing content is the rank-
additive direct-product structure on `(Z_2)^d` and elementary
integer arithmetic on the equality `|(Z_2)^d| = 2^d = |V_4|^2 = 16`.

## 1. Claim scope

Let `d ≥ 2` be an integer. Let the **Brillouin-zone corner set** on
`Z^d` be

```text
C(d)  :=  {0, π}^d                                                 (B)
```

with `|C(d)| = 2^d`. Identifying `{0, π}` with `Z_2 = Z / 2Z` via
the bijection `0 ↦ 0, π ↦ 1` makes `C(d)` an elementary abelian
2-group under componentwise addition mod `2π`, isomorphic to
`(Z_2)^d`. Let `V_4 := Z_2 × Z_2` denote the **Klein-four group**
(the unique non-cyclic group of order 4). Then:

- **(V1) Rank of `(Z_2)^d`.** The group `(Z_2)^d` is elementary
  abelian of rank `d` and order `2^d`. By the elementary divisor
  theorem for finite abelian groups, `(Z_2)^d ≅ (Z_2)^{d_1} × ⋯ ×
  (Z_2)^{d_r}` if and only if `d_1 + ⋯ + d_r = d` (rank is additive
  under direct product). In particular, `(Z_2)^d ≅ A × B` for finite
  abelian groups `A, B` forces `A, B` to be elementary abelian
  2-groups of ranks `a, b` with `a + b = d`.

- **(V2) Cardinality identity at `d = 4`.** At `d = 4`,
  `|(Z_2)^4| = 2^4 = 16 = 4 · 4 = |V_4| · |V_4|`. The orders match:
  the product of two `V_4` factors has the same cardinality as
  `(Z_2)^4`.

- **(V3) Factorization at `d = 4`.** Explicitly,
  `(Z_2)^4 = (Z_2)^2 × (Z_2)^2 = V_4 × V_4`. The isomorphism is the
  identity-on-coordinates map `(b_1, b_2, b_3, b_4) ↦ ((b_1, b_2),
  (b_3, b_4))`. Each factor `(b_1, b_2) ∈ (Z_2)^2 = V_4` is a copy
  of the Klein-four group.

- **(V4) Balanced V_4 × V_4 factorization condition.** The equation
  `(Z_2)^d ≅ V_4 × V_4` with both factors literally `V_4` (i.e.,
  each factor an elementary abelian 2-group of order exactly 4)
  forces `d = 2 + 2 = 4`. By (V1), `(Z_2)^d ≅ A × B` requires
  `rank(A) + rank(B) = d`; if both `A, B ≅ V_4` then
  `rank(A) = rank(B) = 2` and `d = 2 + 2 = 4`.

- **(V5) Counterfactual at `d = 2`.** `(Z_2)^2 = V_4` is the Klein-
  four group itself, so there is no nontrivial direct-product
  factorization into two equal-cardinality factors each isomorphic
  to `V_4`. The only product decompositions are `V_4 ≅ V_4 × {e}`
  (trivial) or `V_4 ≅ Z_2 × Z_2` (factors are `Z_2`, not `V_4`).

- **(V6) Counterfactual at `d = 3`.** `|(Z_2)^3| = 8`, but
  `|V_4 × V_4| = 16 ≠ 8`. No `V_4 × V_4` factorization exists.

- **(V7) Counterfactual at `d = 5`.** `|(Z_2)^5| = 32`, but
  `|V_4 × V_4| = 16 ≠ 32`. No `V_4 × V_4` factorization exists.

- **(V8) Counterfactual at `d = 6`.** `|(Z_2)^6| = 64`. While
  `(Z_2)^6 ≅ (Z_2)^3 × (Z_2)^3` is a balanced direct-product
  factorization into equal-cardinality factors, each factor
  `(Z_2)^3` has order `8`, not `4`; `(Z_2)^3 ≇ V_4`. The balanced
  factorization at `d = 6` is into `(Z_2)^3` factors, NOT `V_4`
  factors. (Alternatively, `(Z_2)^6 ≅ V_4 × (Z_2)^4` and several
  other rank-additive splittings, but none is `V_4 × V_4`.)

- **(V9) Counterfactual at `d = 8`.** `|(Z_2)^8| = 256`. The
  balanced factorization is `(Z_2)^8 ≅ (Z_2)^4 × (Z_2)^4`, with each
  factor of order `16 ≠ 4`. Each factor `(Z_2)^4` is itself
  `V_4 × V_4` (by (V3) applied internally), but neither factor IS
  literally `V_4`.

- **(V10) Uniqueness over `d ∈ {2, 3, 4, 5, 6, 7, 8}`.** Combining
  (V3)-(V9): the equation `(Z_2)^d ≅ V_4 × V_4` (both factors
  literally `V_4`, i.e., elementary abelian 2-groups of rank exactly
  `2`) holds among `d ∈ {2, 3, 4, 5, 6, 7, 8}` exactly at `d = 4`.

- **(V11) Closed-form rank statement.** For every integer `d ≥ 2`,
  `(Z_2)^d ≅ V_4 × V_4` if and only if `d = 4`. The forward direction
  is (V3). The converse: any isomorphism `(Z_2)^d ≅ V_4 × V_4` gives
  `2^d = |V_4 × V_4| = 16 = 2^4`, hence `d = 4`.

Facts (V1)-(V11) are pure finite-group statements on elementary
abelian 2-groups combined with elementary integer arithmetic on
`2^d = 16`. They make **no** claim about Brillouin-zone physics, no
claim about taste-cube projections, no claim about a chosen lattice-
realization, and no claim about the underlying spacetime dimension.
They are class-(A) algebraic identities ratifiable by exact-
symbolic sympy verification on the explicit group structure.

## 2. Why this note exists

The hierarchy formula honest-status note
[`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
names **P2** — the Wick-rotation `Z³ → Z⁴` admitted convention — as
one of four open primitives carrying the `(7/8)^{1/4} × α_LM^{16}`
match.

The retained narrow theorem
[`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
ratifies that chirality existence forces `n = d_s + d_t` even.
Recent companion narrows
[`SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md`](SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md),
[`F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md),
[`BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md),
[`CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md`](CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md),
and
[`CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
isolate four further algebraically independent witnesses for the
forcing of `d = 4` from distinct algebraic directions (Lie algebra,
exterior algebra, integer arithmetic, Clifford algebra, Chern-
character formal expansion).

The present narrow adds **one more algebraically independent
witness**: the finite-group statement that the `2^d`-element BZ-
corner set, viewed as the elementary abelian 2-group `(Z_2)^d`,
admits the **balanced** direct-product factorization into two copies
of the Klein-four group `V_4` exactly at `d = 4`. The argument is
pure elementary-abelian rank arithmetic; it does not consume the
parent retained chirality narrow, the existing Klein-four APBC
orbit narrow (which is a 1D statement on temporal Matsubara modes),
the bosonic-bilinear selector note, the retained `1 + 3 + 3 + 1`
hw-decomposition narrow on `(Z_2)^3`, or any framework-substrate
content.

The narrow theorem **does not close P2**. It provides one of multiple
converging structural witnesses on the dimension `d = 4`, each
ratifiable at exact-symbolic precision. Each witness operates on a
distinct algebraic surface (Lie algebra, exterior algebra, integer
arithmetic, Clifford algebra, Chern-character expansion,
elementary-abelian factorization); their convergence is documented
as the multi-witness convergence pattern for `d = 4` forcing.

## 3. Cited authorities (one hop)

None load-bearing. (V1)-(V11) are pure abstract finite-group /
elementary-abelian-2-group identities and elementary integer
arithmetic on the equation `2^d = 16`. The references to Brillouin-
zone corners and lattice fermion doublers are informational context
(Susskind, *Phys. Rev. D* 16 (1977) 3031; Kogut-Susskind,
*Phys. Rev. D* 11 (1975) 395; Karsten-Smit, *Nucl. Phys. B* 183
(1981) 103), not load-bearing internal authorities. The narrow only
consumes the **identification** of the BZ-corner set with `(Z_2)^d`
as elementary abelian 2-group (a definition, not a theorem) and
the elementary divisor theorem for finite abelian groups (textbook
material, M. Hall, *The Theory of Groups* 1959, Theorem 3.2.2;
S. Lang, *Algebra* 3rd ed., §I.8).

## 4. Admitted-context inputs

- **Finite group theory.** The Klein-four group `V_4 = Z_2 × Z_2`
  is the unique non-cyclic group of order 4 (M. Hall, *The Theory
  of Groups* §1.5). Elementary abelian 2-groups `(Z_2)^d` are
  classified by their rank `d` up to isomorphism (S. Lang,
  *Algebra* 3rd ed., §I.8, Theorem 8.1). Admitted-context
  mathematical infrastructure on the framework's accepted surface
  (per [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)
  "mathematical infrastructure (ordinary)" admissions).
- **Direct-product rank additivity.** For elementary abelian
  2-groups, `(Z_2)^a × (Z_2)^b ≅ (Z_2)^{a + b}`. Equivalently,
  `rank(A × B) = rank(A) + rank(B)` on the category of elementary
  abelian 2-groups. Standard finite-group fact.
- **Cardinality of direct product.** `|A × B| = |A| · |B|` for
  finite groups `A, B`. Elementary set theory.
- **Exact arithmetic on integers `d, 2^d`.** The equation `2^d = 16`
  has unique solution `d = 4` over the integers. Verified by the
  companion runner via sympy.

No PDG values consumed. No literature numerical comparators consumed.
No fitted selectors consumed. No framework-substrate-instance-
specific input. No Wick-rotation admission consumed. No BZ-corner
physics identification consumed (the BZ-corner set is identified
with `(Z_2)^d` as an abstract group, no momentum-space integration
or staggered-fermion structure enters). No taste-cube content
consumed.

## 5. Proof

The argument is direct rank arithmetic on elementary abelian
2-groups.

### 5.1 (V1) Rank classification of `(Z_2)^d`

The elementary divisor theorem for finite abelian groups (Hall §3.2,
Lang §I.8) states that every finite abelian group decomposes
uniquely (up to ordering of factors) as a direct product of cyclic
prime-power groups. Restricted to the elementary abelian 2-group
`(Z_2)^d`, this gives `(Z_2)^d ≅ Z_2 × Z_2 × ⋯ × Z_2` (`d` factors)
as the unique decomposition into cyclic prime-power factors. The
integer `d` is the **rank** of `(Z_2)^d`.

For any direct-product factorization `(Z_2)^d ≅ A × B` with `A, B`
finite abelian groups, the elementary divisor theorem forces both
`A, B` to be elementary abelian 2-groups (any cyclic factor of
order `p^k` with `p ≠ 2` or `k > 1` would appear in the full
decomposition of `A × B`, contradicting the uniqueness of the
`(Z_2)^d` decomposition). Hence `A ≅ (Z_2)^a, B ≅ (Z_2)^b` for some
integers `a, b ≥ 0`, with `a + b = d` (rank additivity under
direct product).

### 5.2 (V2) Cardinality match at `d = 4`

By direct integer arithmetic: `2^4 = 16 = 4 · 4 = |V_4| · |V_4|`.
So `|(Z_2)^4| = |V_4 × V_4|`.

### 5.3 (V3) Explicit factorization at `d = 4`

The map

```text
φ : (Z_2)^4  →  V_4 × V_4,                                         (F1)
    (b_1, b_2, b_3, b_4)  ↦  ( (b_1, b_2),  (b_3, b_4) ),
```

is a group homomorphism (componentwise addition mod 2) and a
set bijection (each output pair `((b_1, b_2), (b_3, b_4))` with
`b_i ∈ {0, 1}` is in bijection with the input 4-tuple). Hence `φ`
is an isomorphism `(Z_2)^4 ≅ V_4 × V_4`, with each factor equal to
`V_4 = Z_2 × Z_2`. ∎

### 5.4 (V4) The balanced V_4 × V_4 condition forces `d = 4`

Suppose `(Z_2)^d ≅ V_4 × V_4`. By (V1), any such isomorphism gives
`a + b = d` with `(Z_2)^d ≅ (Z_2)^a × (Z_2)^b` and the right side
literally `V_4 × V_4`. The hypothesis "both factors are `V_4`"
means each factor has rank 2, i.e., `a = b = 2`. So `d = 2 + 2 = 4`.

Alternatively (purely by cardinality): `|(Z_2)^d| = 2^d` and
`|V_4 × V_4| = 16`. Equality forces `2^d = 16`, hence `d = 4`. ∎

### 5.5 (V5) Counterfactual at `d = 2`

At `d = 2`, `(Z_2)^2` itself is the Klein-four group `V_4`. Its
only direct-product factorizations into equal-cardinality factors
are `V_4 ≅ V_4 × {e}` (trivial; one factor is the trivial group of
order 1, not `V_4`) or `V_4 ≅ Z_2 × Z_2` (both factors are `Z_2`,
which has order 2, not order 4). Neither is `V_4 × V_4`.

Equivalently by cardinality: `|(Z_2)^2| = 4 ≠ 16 = |V_4 × V_4|`. ∎

### 5.6 (V6)-(V9) Counterfactuals at `d ∈ {3, 5, 6, 7, 8}`

- `d = 3`: `|(Z_2)^3| = 8 ≠ 16`.
- `d = 5`: `|(Z_2)^5| = 32 ≠ 16`.
- `d = 6`: `|(Z_2)^6| = 64 ≠ 16`. The balanced factorization at
  `d = 6` is `(Z_2)^6 ≅ (Z_2)^3 × (Z_2)^3`, with each factor of
  order `8`, not `4 = |V_4|`. So `(Z_2)^3 ≇ V_4` (different
  cardinalities).
- `d = 7`: `|(Z_2)^7| = 128 ≠ 16`.
- `d = 8`: `|(Z_2)^8| = 256 ≠ 16`. The balanced factorization at
  `d = 8` is `(Z_2)^8 ≅ (Z_2)^4 × (Z_2)^4`, with each factor of
  order `16 ≠ 4`. Although each `(Z_2)^4` factor internally
  decomposes as `V_4 × V_4` via (V3), neither factor literally IS
  `V_4`. ∎

### 5.7 (V10) Uniqueness over `d ∈ {2, 3, 4, 5, 6, 7, 8}`

Combining (V3) and (V5)-(V9): among `d ∈ {2, 3, 4, 5, 6, 7, 8}`,
the equation `(Z_2)^d ≅ V_4 × V_4` (both factors literally `V_4`)
holds exactly at `d = 4`. ∎

### 5.8 (V11) General closed-form statement

For every integer `d ≥ 2`: `(Z_2)^d ≅ V_4 × V_4` iff `d = 4`. The
forward direction is (V3). The converse is the cardinality
argument `|V_4 × V_4| = 16 = 2^4` combined with `|(Z_2)^d| = 2^d`,
giving `2^d = 16 ⇔ d = 4`. ∎

### 5.9 Combining

From (V1)-(V11): the `2^d`-element BZ-corner set `(Z_2)^d` admits
the **balanced V_4 × V_4 factorization** (direct product of two
equal-cardinality factors each literally Klein-four) iff `d = 4`.
Among integers `d ≥ 2`, this property is unique to `d = 4`. The
combinatorial obstruction at every other `d` is either cardinality
mismatch (`2^d ≠ 16` at `d ∉ {4}`) or rank-of-factor mismatch (at
`d ∈ {6, 8}`, both factors have rank `≠ 2`, hence are not `V_4`).
QED.

## 6. Derivable corollaries

- **The 16-corner BZ structure at `d = 4` carries a structurally
  unique balanced Klein-four-pair action.** The `V_4 × V_4` factor
  group acts on `(Z_2)^4` by `((u, v), (w, x)) · (b_1, b_2, b_3,
  b_4) := (b_1 + u, b_2 + v, b_3 + w, b_4 + x)` (componentwise). The
  two `V_4` factors act independently on the first-two-coordinate
  and last-two-coordinate halves of the corner set; this product
  structure is the unique pairing of the 4 coordinate directions
  into a `(2, 2)`-split where each pair carries a full Klein-four
  group action.

- **Rank-2 factor uniqueness.** Among balanced factorizations
  `(Z_2)^d ≅ (Z_2)^k × (Z_2)^k` (with `d = 2k`), only at `k = 2`
  (i.e., `d = 4`) is the rank-`k` factor `(Z_2)^k = V_4`. At
  `k = 1` (`d = 2`), `(Z_2)^1 = Z_2 ≠ V_4` (order 2 vs. 4). At
  `k = 3` (`d = 6`), `(Z_2)^3` has order 8, not 4. At `k ≥ 3`,
  the factor has order `2^k ≥ 8`, exceeding `|V_4| = 4`.

- **No `V_4`-pair structure at odd `d`.** For odd `d ∈ {3, 5, 7,
  9, ...}`, there is no balanced direct-product factorization of
  `(Z_2)^d` into two equal-cardinality factors at all (any such
  factorization requires even total rank). The Klein-four-pair
  structure fails for purely parity reasons at odd `d`.

These corollaries are direct consequences of (V1)-(V11).

## 7. What this claims

- (V1)-(V11), the explicit balanced `V_4 × V_4` factorization at
  `d = 4`, the counterfactuals at `d ∈ {2, 3, 5, 6, 7, 8}`, and the
  general closed-form statement `(Z_2)^d ≅ V_4 × V_4` iff `d = 4`
  over all integers `d ≥ 2`.
- The pure finite-group / integer-arithmetic status of the identity
  (no Wick-rotation load-bearing, no Brillouin-zone-physics load-
  bearing, no staggered-fermion load-bearing).

## 8. What this does NOT claim

- Does **not** claim that the framework's BZ-corner set is
  physically realized at `d = 4` (this requires upstream Wick-
  rotation and staggered-Dirac realization closure, both currently
  open per [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)).
- Does **not** invoke any taste-cube content, taste-decomposition,
  or BZ-corner-as-physical-momentum content. The BZ-corner set is
  treated purely as the abstract group `(Z_2)^d`.
- Does **not** claim that the `V_4 × V_4` factorization at `d = 4`
  is the only direct-product factorization of `(Z_2)^4` (it is not;
  `(Z_2)^4 ≅ (Z_2)^1 × (Z_2)^3 ≅ Z_2 × (Z_2)^3` is another, and
  `(Z_2)^4 ≅ V_4 × V_4 ≅ V_4 × Z_2 × Z_2` further decomposes). The
  claim is the **specific** factorization where both factors are
  rank-2 (= equal cardinality 4 = `|V_4|`).
- Does **not** close P2 (Wick rotation `Z³ → Z⁴`) from the
  hierarchy honest-status note. The narrow provides one of multiple
  converging structural witnesses, not a substitute derivation.
- Does **not** consume any framework gauge-theoretic identification.
  The BZ-corner set is treated purely on the abstract finite-group
  surface.
- Does **not** consume the existing
  [`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md`](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
  bounded note, nor the
  [`HIERARCHY_LT4_KLEIN_FOUR_SIN_SQUARED_UNIFORMITY_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_LT4_KLEIN_FOUR_SIN_SQUARED_UNIFORMITY_NARROW_THEOREM_NOTE_2026-05-10.md)
  Class-A narrow (which operates on the **1D temporal APBC mode
  set**, not the **d-dimensional BZ-corner set**). The two Klein-
  four statements are logically independent: the existing narrow
  is "Klein-four acts on `R / 2πZ` and partitions APBC roots-of-
  unity"; the present narrow is "`(Z_2)^d` factors as `V_4 × V_4`
  iff `d = 4`". Different group action, different object.
- Does **not** claim that the `V_4 × V_4` factorization implies any
  physical selection rule, doubler-counting, taste-quotient, or
  EWSB content.
- Does **not** claim positive-theorem promotion for any parent. The
  narrow is a stand-alone finite-group identity.

## 9. Relation to existing framework primitives

The framework's existing narrow theorems on `d`-dimensional
structure each carry a different algebraic content:

- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (retained_bounded) — chirality existence requires `n = p + q` even.
- [`SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md`](SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md)
  (companion narrow A) — `so(d) ≅ su(2) ⊕ su(2)` uniquely at
  `d = 4`.
- [`F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  (companion narrow B) — `ω ∧ ω` of a 2-form is a top-form on `R^d`
  iff `d = 4`.
- [`BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  (companion narrow C) — `binom(d, 2) = 2(d - 1)` iff `d = 4`.
- [`CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md`](CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md)
  (companion narrow D) — `Cl(3, 1) ≅ M_4(R)` with
  `dim_R Cl(3, 1) = 16 = 2^4`.
- [`CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  (companion narrow E) — `ch_k(F)` is a top-form on `R^d` iff
  `2k = d`; `k = 2` forces `d = 4`.
- The present narrow — `(Z_2)^d ≅ V_4 × V_4` (balanced direct
  product into two equal-cardinality Klein-four factors) iff `d = 4`.

The six witnesses (W_A through W_F) are **algebraically independent**:

- W_A (`SO4_UNIQUE_SU2_SU2_SPLIT`): operates on the **real rotation
  Lie algebra** `so(d)` via the Cartan classification (semisimple
  decomposition into simple ideals).
- W_B (`F_WEDGE_F_TOP_FORM`): operates on the **graded exterior
  algebra** `Λ^*(R^d)` via additive degree counting on a single
  2-form `ω`.
- W_C (`BINOM_D_2_EQUALS_TWICE_DMINUS1`): operates on **integer
  arithmetic** of the binomial coefficient `binom(d, 2)` and the
  linear factor `2(d - 1)`.
- W_D (`CL31_M4R_DIMENSION_SIXTEEN`): operates on the **real
  Clifford-algebra Cartan-Bott classification** at signature
  `(3, 1)`, with `dim_R Cl(3, 1) = 2^4 = 16`.
- W_E (`CHERN_CHARACTER_K2_TOP_FORM`): operates on the **Chern-
  character formal exponential expansion** `ch(F) = tr exp(i F /
  (2π))` via per-term degree matching `2k = d` and the `k = 2`
  ABJ specialization.
- W_F (the present narrow, `KLEIN_FOUR_PRODUCT_BZ_CORNERS`):
  operates on the **elementary-abelian 2-group structure** of the
  `2^d`-element BZ-corner set via rank-additive direct-product
  decomposition into two equal-cardinality Klein-four factors.

The present narrow's independent content vs. each prior witness:

- vs. W_A (`so(d)`): present narrow is on `(Z_2)^d` (finite abelian
  group, order `2^d`), W_A on `so(d)` (real Lie algebra, dim
  `d(d-1)/2`). Different objects; no shared algebraic content.
- vs. W_B (`ω ∧ ω` top-form): present narrow is on `(Z_2)^d` (no
  graded algebra), W_B on `Λ^*(R^d)`. Different categories.
- vs. W_C (`binom(d, 2) = 2(d - 1)`): present narrow is on the
  integer `2^d` and its factorization as `4 · 4`, W_C on the integer
  `binom(d, 2) = d(d - 1)/2` and its equality with `2(d - 1)`.
  Different algebraic invariants (`2^d` vs. `binom(d, 2)`).
- vs. W_D (`dim_R Cl(p, q) = 2^{p + q}`): present narrow uses the
  same exponent `2^d` but on a different object (finite abelian
  group `(Z_2)^d` vs. real Clifford algebra `Cl(p, q)`). W_D
  selects `(3, 1)` via the Cartan-Bott periodicity classification;
  the present narrow selects `d = 4` via the rank-2 factor
  condition on a Klein-four pair. The two narrows match
  numerically (both give `2^4 = 16`) but operate on
  algebraically independent surfaces; no same-surface bridge is
  asserted.
- vs. W_E (`ch_k(F)`): present narrow has no graded exterior
  algebra or formal Chern-character expansion; W_E operates on
  `Λ^*(R^d) ⊗ M_N(C)`. Different categories.

Neither narrow consumes the others; none carries a Wick-rotation
admission; none closes P2. Together they document six distinct
algebraic pressures pointing to `d = 4`.

The convergence: chirality forces `n` even; the rotation algebra
factorization picks `d = 4` among Cartan-classification dims; the
wedge-square arithmetic picks `d = 4` from graded-algebra degree
counting on 2-form squares; the binom arithmetic picks `d = 4` from
integer roots; the Clifford algebra `Cl(3, 1)` lands at total dim
`16 = 2^4`; the Chern-character `k = 2` term picks `d = 4` from
the factorial expansion `1 / k!` at the canonical chiral-anomaly
index; and the elementary-abelian 2-group `(Z_2)^d` admits the
balanced Klein-four-pair factorization exactly at `d = 4`. Each is
a class-(A) narrow theorem ratifiable independently.

## 10. Honest open items

- The narrow theorem does not close P2 from the hierarchy honest-
  status note. Closing P2 requires a framework-native derivation of
  the time direction from `A_min` primitives, which this narrow
  does not provide.
- The narrow theorem does not identify the BZ-corner set with any
  framework-realized momentum-space corner structure. The
  identification with a physical Brillouin zone at `d = 4` is a
  downstream substrate-level question requiring upstream gate
  closures (staggered-Dirac realization at `d = 4`, Wick rotation).
- The narrow theorem does not derive any physical selection of
  `d = 4` as the spacetime dimension. Only the finite-group
  identity `(Z_2)^d ≅ V_4 × V_4` ⇔ `d = 4` is established.
- The `V_4 × V_4` factor structure does not by itself imply any
  doubler-counting, taste-quotient, or chirality-decomposition; the
  link to staggered-fermion physics is a separate matter handled
  by the upstream `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT`
  narrow at `d = 3` (different `d`, different group action).

## 11. Declared dependencies (graph-visible)

None. No internal note is load-bearing for the present finite-group
identity. The references to existing framework narrow theorems in
§9 are informational cross-references for the multi-witness reading,
not load-bearing imports.

## 12. Forbidden imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No admitted unit conventions load-bearing on the claim.
- No same-surface family arguments.
- No `d = 4` forced claim from any framework axiom; the narrow is a
  pure finite-group / integer-arithmetic identity that singles out
  `d = 4` among all `d ≥ 2` via the balanced Klein-four-pair
  factorization condition.
- No Wick-rotation admission consumed.
- No staggered-Dirac realization gate consumed.
- No taste-cube content consumed.
- No physical BZ-corner identification consumed.

## 13. Validation

Primary runner:
[`scripts/audit_companion_klein_four_product_bz_corners_forces_d_four_exact_2026_05_26.py`](../scripts/audit_companion_klein_four_product_bz_corners_forces_d_four_exact_2026_05_26.py)
verifies, at exact integer / symbolic precision via sympy:

1. (V1) Rank classification: for `d ∈ {2, 3, ..., 8}`, the
   elementary abelian 2-group `(Z_2)^d` has order `2^d` and rank
   `d`. Direct-product decompositions `(Z_2)^d ≅ A × B` with both
   `A, B` finite abelian groups force `A, B` elementary abelian
   2-groups with `rank(A) + rank(B) = d`.
2. (V2) Cardinality identity at `d = 4`: `|(Z_2)^4| = 2^4 = 16 =
   4 · 4 = |V_4| · |V_4| = |V_4 × V_4|`.
3. (V3) Explicit isomorphism `φ : (Z_2)^4 → V_4 × V_4`,
   `(b_1, b_2, b_3, b_4) ↦ ((b_1, b_2), (b_3, b_4))`. Verifies
   bijectivity by enumerating all `2^4 = 16` 4-tuples and checking
   that `φ` is a well-defined homomorphism (preserves componentwise
   addition mod 2). Verifies `φ(0) = (0, 0)` and
   `φ(b + b') = φ(b) + φ(b')` over all `2^4 · 2^4 = 256` ordered
   pairs.
4. (V4) Balanced V_4 × V_4 forces `d = 4`: solves `2^d = 16` over
   the integers via sympy; unique solution `d = 4`.
5. (V5)-(V9) Counterfactuals at `d ∈ {2, 3, 5, 6, 7, 8}`:
   - `d = 2`: `|(Z_2)^2| = 4 ≠ 16`; only product factorizations
     are `V_4 × {e}` (trivial) or `Z_2 × Z_2` (factors `Z_2`,
     not `V_4`).
   - `d = 3`: `|(Z_2)^3| = 8 ≠ 16`.
   - `d = 5`: `|(Z_2)^5| = 32 ≠ 16`.
   - `d = 6`: `|(Z_2)^6| = 64 ≠ 16`. The balanced factorization
     `(Z_2)^6 ≅ (Z_2)^3 × (Z_2)^3` has each factor of order
     `8 ≠ 4`, so neither factor is `V_4`.
   - `d = 7`: `|(Z_2)^7| = 128 ≠ 16`.
   - `d = 8`: `|(Z_2)^8| = 256 ≠ 16`. The balanced factorization
     `(Z_2)^8 ≅ (Z_2)^4 × (Z_2)^4` has each factor of order
     `16 ≠ 4`.
6. (V10) Uniqueness scan over `d ∈ {2, ..., 8}`: only `d = 4`
   satisfies the balanced `V_4 × V_4` factorization.
7. (V11) Closed-form: `(Z_2)^d ≅ V_4 × V_4` ⇔ `d = 4` over all
   integers `d ≥ 2`, by sympy `solve(2**d - 16, d)`.
8. Klein-four structure verification: `V_4 = Z_2 × Z_2` is verified
   by checking the 4-element group table: 4 elements, each non-
   identity element of order 2, abelian, non-cyclic.
9. Group homomorphism check: the map `φ` defined in (V3) is
   verified to satisfy `φ(b + b') = φ(b) + φ(b')` for all ordered
   pairs `(b, b')` in `((Z_2)^4)^2`. Computed at exact integer
   precision.
10. Rank-2 factor uniqueness: among balanced factorizations
    `(Z_2)^{2k} ≅ (Z_2)^k × (Z_2)^k` for `k ∈ {1, 2, 3, 4}`, only
    at `k = 2` is `(Z_2)^k = V_4`.

Target PASS = (large), FAIL = 0.

## 14. Cross-references (non-load-bearing)

- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained Clifford-algebra narrow on chirality requiring even
  `n = d_s + d_t`.
- [`SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md`](SO4_UNIQUE_SU2_SU2_SPLIT_NARROW_THEOREM_NOTE_2026-05-26.md)
  — companion Lie-algebra narrow on `so(4) ≅ su(2) ⊕ su(2)` unique
  among `so(d)` for `d ≥ 2`.
- [`F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  — companion exterior-algebra narrow on `ω ∧ ω` being a top-form
  on `R^d` iff `d = 4`.
- [`BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  — companion integer-arithmetic narrow on `binom(d, 2) = 2(d - 1)`
  iff `d = 4`.
- [`CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md`](CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26.md)
  — companion Clifford-algebra narrow on `Cl(3, 1) ≅ M_4(R)`,
  `dim_R Cl(3, 1) = 16 = 2^4`. Numerically matches `|(Z_2)^4| = 16`
  in the present narrow but on an algebraically independent surface.
- [`CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`](CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md)
  — companion Chern-character narrow on `ch_k(F)` top-form iff
  `2k = d`, with `k = 2` forcing `d = 4`.
- [`HIERARCHY_LT4_KLEIN_FOUR_SIN_SQUARED_UNIFORMITY_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_LT4_KLEIN_FOUR_SIN_SQUARED_UNIFORMITY_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained Class-A narrow on a different Klein-four orbit (the
  1D temporal APBC mode set). Logically independent of the present
  narrow: the existing narrow's Klein-four acts on `R / 2πZ` and
  partitions roots-of-unity; the present narrow's Klein-four pair
  acts as a direct-product factor of the `d`-dimensional BZ-corner
  group. Different group action, different object, different
  algebraic surface.
- [`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md`](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
  — bounded note that uses Klein-four orbit closure as part of a
  broader physics argument for selecting `L_t = 4`. Not consumed
  here; the present narrow extracts only the algebraic
  factorization identity.
- [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  — retained Class-A narrow on the `S_3`-orbit decomposition of
  `(Z_2)^3`. Logically independent of the present narrow:
  different `d` (3 vs. 4), different group action (`S_3` coordinate
  permutation vs. direct-product factorization), different
  algebraic content (orbit partition vs. internal direct-product
  structure).
- [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
  — package-level honest-status note naming P2 (Wick rotation
  `Z³ → Z⁴`) as an open primitive.
- [`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)
  — current framework baseline.
- M. Hall, *The Theory of Groups* (Macmillan 1959) — textbook
  reference for Klein-four group and elementary divisor theorem
  (§1.5, §3.2).
- S. Lang, *Algebra* (3rd ed., Addison-Wesley 1993) — textbook
  reference for elementary abelian groups (§I.8, Theorem 8.1).
- Susskind, *Phys. Rev. D* 16 (1977) 3031 — textbook reference for
  the staggered-fermion BZ-corner doubling (cited as context only;
  not load-bearing).
- Kogut-Susskind, *Phys. Rev. D* 11 (1975) 395 — textbook reference
  for the original staggered-fermion construction (cited as
  context only; not load-bearing).
