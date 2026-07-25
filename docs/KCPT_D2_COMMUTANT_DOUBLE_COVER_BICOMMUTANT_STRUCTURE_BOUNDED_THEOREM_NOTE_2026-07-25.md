# KCPT D2 commutant double cover and bicommutant structure (L=4 and L=6) (bounded theorem)

**Type:** bounded_theorem

registry id: `kcpt_d2_commutant_double_cover_bicommutant_structure`

## claim_scope

- **Kind:** bounded_theorem. Exact integer group enumeration and an exact-integer
  minimal-polynomial annihilation, plus a numerically resolved eigenspace/character
  block, on the fixed staggered lattices L ∈ {4, 6} (N = 64 and N = 216 on the L³ torus).
  Group orders, the semidirect/extension structure, the derived subgroup, involution
  lift-squares, and the minimal polynomial of `D2` are exact integer facts; the seven
  eigenspace-projector characters are resolved at the stated tolerances on those two
  finite objects.
- **Object:** the signed-permutation commutant
  `Comm(D2) = { signed permutation U : U D2 = D2 U }` exactly as enumerated in the landed
  Unit 25 lane; the permutation-part map `Comm → perms` and its image `I`; the central
  extension `1 → {±1} → Comm → T ⋊ B₃ → 1`; the derived subgroup `[Comm, Comm]`; and the
  endomorphism algebra `End_Comm(C^N)` together with its identification with the
  polynomial algebra `C[D2]`.
- **Scope limits:** r-neutral. No physical, continuum, or thermodynamic claim is made;
  every quantity is a numerical invariant of the finite L ∈ {4, 6} construction. The two
  lattice sizes are two separate finite-surface measurements, not a general-L statement.

## 1. Objects and setup

- Lattices L = 4 (N = 64) and L = 6 (N = 216) on the L³ torus with the same staggered
  integer antisymmetric adjacency `D2` used by the landed Unit 25 lane (`eta_0 = 1`,
  `eta_1 = (-1)^{x0}`, `eta_2 = (-1)^{x0+x1}`). `M = D2²` has spectrum `[0, -4, -8, -12]`
  with shell multiplicities `[8, 24, 24, 8]` at L=4, and `[0, -3, -6, -9]` with
  `[8, 48, 96, 64]` at L=6 (spectrum and multiplicities recomputed and gated).
- The full signed-permutation commutant `Comm(D2)`, with `|Comm| = 6144 = 96N` (L=4) and
  `20736 = 96N` (L=6), is reused verbatim from the landed Unit 25 module: the runner
  imports it and calls its lattice, support-structure, commutant-enumeration, symmetry
  group `H`, dressed-rotation `g_r4`, character-sum, and closure interfaces. No enumeration
  is reimplemented here; this unit reads the enumerated group and derives its structure.
- The reference hyperoctahedral group `B₃` (order 48, ≅ O_h) is built independently inside
  this runner as the 48 signed-permutation 3×3 matrices (`itertools.permutations` of the
  three axes times the eight sign patterns), so every "= B₃" claim is a set equality
  against a from-scratch object, not against the enumerator that produced `Comm`.
- Structural generators of `Comm`: the lifts of the three unit translations, the lifts of
  the three linear maps `A_cyc = [[0,0,1],[1,0,0],[0,1,0]]`,
  `A_swap = [[0,1,0],[1,0,0],[0,0,1]]`, `A_flip = diag(-1,1,1)`, and the central `-1`
  (identity permutation with all signs `-1`). Their closure is gated to recover all of
  `Comm` at both L (a seven-generator presentation of the group).
- All group-theoretic decisions (composition, inverse, membership, closure, order,
  involution test, lift-square) use exact integer signed-permutation arithmetic and byte
  keys; the minimal-polynomial proof stays in exact `int64`; `np.linalg.eigh` of `i·D2`
  (complex Hermitian) enters only for the eigenspace/projector-character block. No floating
  tolerance enters any group decision.

## 2. Theorem claims

**T1 (structure; gates STRUCT, KERNEL, TRANS, CANON_LINEAR, B3GEN, STRUCTGENS).** The
kernel of the permutation-part map `Comm → perms` is exactly `{±1}` (size 2, both signs
constant). The image `I` contains all `N` translations `T` as a normal subgroup (every
translation present; each `T`-element conjugated by the three linear generators lands back
in `T`); `I/T` has exactly 48 cosets; every 0-fixing canonical coset representative is
LINEAR, `x ↦ Ax mod L`, verified on all N sites, and the 48 matrices `A` are exactly the
independently built reference `B₃` — the SAME 48-matrix set at L=4 and L=6 — and the 48
canonical representatives are closed under composition. Hence `I = T ⋊ B₃` as an internal
semidirect product at the permutation level, and
`|Comm| = 2·|T|·|B₃| = 2·N·48 = 96N` — the structural account of the Unit 25 census law
`|Comm| = 6144 / 20736` at both L. The seven structural generators close to all of `Comm`.

**T2 (non-split central double cover; gates INVOL, DERIVED, MINUS1_DERIVED, PIDERIVED,
EVENSUB, A4IMAGE).** The central extension `1 → {±1} → Comm → T ⋊ B₃ → 1` is a
**non-split central double cover**, by two independent computations.
(a) *Involution lift-squares.* Each involution `σ ∈ I` has exactly two lifts `±ŝ` in
`Comm` sharing one square (`(−ŝ)² = ŝ²`). A split extension via a section would give every
involution a lift squaring to `+1`; instead, of 359 involutions in `I` at L=4, 192 have
lift-square `−1`, and of 799 at L=6, 400 have lift-square `−1`. Any lift-square-`−1`
involution obstructs a section.
(b) *`−1 ∈ [Comm, Comm]`.* A split central extension is the direct product
`{±1} × (T ⋊ B₃)`, whose derived subgroup omits `(−1, 1)`; the computed containment
`−1 ∈ [Comm, Comm]` at both L refutes the direct-product form. Together these refute the
naive conjecture `Comm ≅ ⟨−1⟩ × (T ⋊ B₃)`.
Fine structure of the derived subgroup (both L): `|[Comm, Comm]| = 12N = |Comm|/8`
(abelianization order 8); `π([Comm, Comm]) = [I, I]` has order `6N`; its translation part
is exactly the **even-parity sublattice** `{v : v₁+v₂+v₃ ≡ 0 mod 2}` (order `N/2`, EXACT
set equality); and its `B₃`-image is exactly `A₄` (order 12, order-spectrum
`{1:1, 2:3, 3:8}`, all determinant `+1`). So `[I, I] = T_even ⋊ A₄`, and `[Comm, Comm]` is
its preimage double cover.

**T3 (bicommutant / spectral completeness; gates MINPOLY, ENDCOMM_CD2, KERDIM, EIGDIMS,
CHARNORM).** `End_Comm(C^N) = C[D2]` exactly, by four steps. (i) `dim End_Comm = 7` at
both L, from the landed Unit 25 integer character sum. (ii) `C[D2] ⊆ End_Comm` always, and
a deterministic sample of the enumerated commutant is re-verified to commute with `D2`.
(iii) `dim C[D2] = deg minpoly(D2) = ` the number of distinct `D2` eigenvalues `= 7`,
proven in exact `int64`: with `M = D2²`, the product
`D2·(M+4I)(M+8I)(M+12I) = 0` at L=4 and `D2·(M+3I)(M+6I)(M+9I) = 0` at L=6 (a degree-7
annihilating polynomial whose factors are read off the distinct `M`-shells), while dropping
ANY single factor — including the leading `D2` — leaves a nonzero integer matrix
(`.any()` true), so the degree is exactly 7. (iv) Equality by the dimension count `7 = 7`.
Corollary: `End_Comm` is abelian, so the `Comm`-representation on `C^N` is
**multiplicity-free** with exactly 7 pairwise-inequivalent irreducible components — the 7
`D2`-eigenspaces. Each eigenspace-projector character, summed over all `|Comm|` group
elements, has squared norm `1` (irreducible) and pairwise inner product `~0` (inequivalent),
observed to `≤ 1e-15`. The kernel of `D2` has dimension 8 at both L (a two-size-stable
anchor) and is a single irreducible component. Eigenspace dimensions, ordered by ascending
`i·D2` eigenvalue, are `[4, 12, 12, 8, 12, 12, 4]` (L=4, eigenvalues
`−2√3, −2√2, −2, 0, +2, +2√2, +2√3`) and `[32, 48, 24, 8, 24, 48, 32]` (L=6, eigenvalues
`−3, −√6, −√3, 0, +√3, +√6, +3`). This is the structural account of the Unit 25 L-stable
`dim End_Comm = 7` headline: `7 = ` #distinct `D2` eigenvalues, stable because the spectral
type `{0, ±iμ₁, ±iμ₂, ±iμ₃}` is stable across the two sizes.

**Tie-backs (gates HCAPCOMM, D3, AR4, OCLOSURE, FULLCLOSURE_L4, CROSSL_B3, CROSSL_D3).**
`H ∩ Comm` and `[Comm, Comm]` have the SAME order `12N` at both L but are DIFFERENT
subgroups (intersection exactly `3N`). The `B₃`-coordinates of `H ∩ Comm` are exactly the
6-element proper-rotation dihedral group of the body diagonal,
`D₃ = {A ∈ B₃ : A(1,1,1)ᵀ = ±(1,1,1)ᵀ, det A = +1} ≅ S₃` (order-spectrum
`{1:1, 2:3, 3:2}`, all det `+1`) — the SAME 6 matrices at both L, checked as a set equality
against the independently built body-diagonal predicate subset of the reference `B₃`.
Adjoining the `B₃`-coordinate of the dressed rotation `g_r4` — which is the bare rotation
matrix `[[0,1,0],[−1,0,0],[0,0,1]]`, the sign dressing being invisible at the `B₃` level —
generates the full proper-rotation subgroup `O ≅ S₄` (order 24, order-spectrum
`{1:1, 2:9, 3:8, 4:6}`, all det `+1`), matched as a set to the det-`+1` half of the
reference `B₃`. The chain `D₃ (6) ⊂ O (24) ⊂ B₃ (48)` is graded by determinant: `H ∩ Comm`
reaches only det-`+1` elements at both L, and at L=4 — the only surface on which the full
closure is enumerated — `⟨H, g_r4⟩ ∩ Comm` likewise reaches only det-`+1` elements, while
the improper det-`−1` half of `B₃` is reached by `Comm` but not by these subgroups. At L=4 only, the full closure
`⟨H, g_r4⟩` has order 6144 with `⟨H, g_r4⟩ ∩ Comm` of order `3072 = |Comm|/2` (consistent
with the landed Unit 25 fact `|⟨H, g_r4⟩ ∩ Comm| = |Comm|/2`), and its `B₃`-localization
computed from the full closure agrees with the 3×3-matrix-land route (route-agreement gate).
This 6144 is NOT the Unit 25 graded commutant `GC` (order `2|Comm| = 12288`, a different
object); this unit does not recompute `GC`.

## 3. Evidence — measured values

| quantity | L=4 (N=64) | L=6 (N=216) |
|----------|-----------:|------------:|
| `M` shell mults | `[8, 24, 24, 8]` | `[8, 48, 96, 64]` |
| `|Comm|` = 96N | 6144 | 20736 |
| kernel of perm map | `{±1}` (size 2) | `{±1}` (size 2) |
| `|I|` = 48·N | 3072 | 10368 |
| translations present in `I` | 64 / 64 | 216 / 216 |
| `|I/T|`, canonical reps linear | 48, 48/48 | 48, 48/48 |
| A-set == reference `B₃` | yes (48) | yes (48) |
| `<A_cyc,A_swap,A_flip>` order | 48 | 48 |
| 7-generator closure = `|Comm|` | 6144 | 20736 |
| involutions in `I`, lift-square `−1` | 359, 192 | 799, 400 |
| `|[Comm,Comm]|` = 12N, abelianization | 768, 8 | 2592, 8 |
| `−1 ∈ [Comm,Comm]` | yes | yes |
| `|π([Comm,Comm])|` = 6N | 384 | 1296 |
| `π(derived) ∩ T` = even-parity sublattice (N/2) | 32 (set-eq) | 108 (set-eq) |
| `B₃`-image of derived (= `A₄`) | 12, `{1:1,2:3,3:8}`, det+1 | 12, `{1:1,2:3,3:8}`, det+1 |
| minpoly `D2·∏(M+cᵢI) = 0`, cᵢ | 0, `[4,8,12]` | 0, `[3,6,9]` |
| drop-one-factor products nonzero | 4/4 | 4/4 |
| deg minpoly = dim `C[D2]` | 7 | 7 |
| `dim End_Comm(C^N)` (U25 char sum) | 7 | 7 |
| commute-with-`D2` sample | 512/512 | 506/506 |
| `dim ker D2` | 8 | 8 |
| eigenspace dims (asc `i·D2`) | `[4,12,12,8,12,12,4]` | `[32,48,24,8,24,48,32]` |
| 7 projector-character norms, max cross | 1.0 (dev ≤1e-15), ≤1e-16 | 1.0 (dev ≤1e-15), ≤1e-16 |
| `|H ∩ Comm|` = 12N, `|derived ∩ (H∩Comm)|` = 3N | 768, 192 | 2592, 648 |
| coords(`H∩Comm`) = `D₃` | 6, `{1:1,2:3,3:2}`, det+1 | 6, `{1:1,2:3,3:2}`, det+1 |
| `A_r4` = `[[0,1,0],[−1,0,0],[0,0,1]]`, det | yes, +1 | yes, +1 |
| `⟨D₃, A_r4⟩` = `O` | 24, `{1:1,2:9,3:8,4:6}`, det+1 | 24, `{1:1,2:9,3:8,4:6}`, det+1 |
| `|⟨H,g_r4⟩|`, `∩ Comm` = `|Comm|/2` | 6144, 3072 | — (matrix-land route only) |
| coords(`H∩Comm`) same 6 across L | yes | yes |

All 50 gates pass with zero failures; the paired runner
`scripts/kcpt_d2_commutant_double_cover_bicommutant_structure_2026_07_25.py` prints
`TOTAL: PASS=50 FAIL=0`, wall-clock about 19 s (`np.linalg.eigh` of `i·D2` only for the
eigenspace/character block). The evidentiary verdict is PASS WITH BOUNDED CLAIMS:
exact-integer facts where stated, the eigenspace/character block resolved at the gated
tolerances, everything bounded to the two computed surfaces L = 4 and L = 6.

## 4. The cover-and-bicommutant picture

The signed-permutation commutant of `D2` is not a bare product but a **non-split central
double cover** of a familiar crystallographic group. At the permutation level `Comm`
projects onto `I = T ⋊ B₃`: all `N` translations, extended by the full 48-element
hyperoctahedral point group. The two signs `{±1}` in the kernel are not a spectator factor
— the cover is non-split, witnessed independently by involutions whose lifts square to `−1`
and by `−1` sitting inside the commutator subgroup. The derived subgroup is itself the
double cover of `T_even ⋊ A₄`: the point-group part collapses from `B₃` to its rotation-even
`A₄`, and the translation part collapses to the even-parity sublattice. On the module side,
the commutant sees `D2` as a multiplicity-free operator: `End_Comm(C^N) = C[D2]`, a
commutative algebra of dimension 7 = the number of distinct `D2` eigenvalues, so the 7
eigenspaces are exactly the 7 inequivalent irreducible components and the 8-dimensional
kernel of `D2` is one of them. The landed symmetry group `H` and its dressed extension
`⟨H, g_r4⟩` localize, at the `B₃` level, to the determinant-`+1` rotation chain
`D₃ ⊂ O ⊂ B₃` (the `⟨H, g_r4⟩` localization enumerated in full at L=4; the chain itself
generated in matrix land, `⟨D₃, A_r4⟩ = O`, at both L); the improper half of `B₃` is
present in `Comm` but out of reach of those subgroups. Both the group-order law `96N` and the two-size-stable `dim End_Comm = 7` of the
Unit 25 census read off directly from this structure: `96N = 2·N·48` and
`7 = ` #distinct `D2` eigenvalues.

## 5. Dependencies

- [KCPT D2 graded signed-permutation commutant characterization (L=4 and L=6) (bounded theorem)](KCPT_D2_GRADED_SIGNED_PERMUTATION_COMMUTANT_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)

## Boundary

- The structure is a finite fact about the two fixed staggered lattices L ∈ {4, 6}. Group
  orders, the extension and derived-subgroup structure, involution lift-square counts, the
  minimal polynomial, endomorphism dimension, and eigenspace dimensions are numerical
  invariants of those constructions; no continuum limit or physical content is claimed, and
  the statement is r-neutral.
- The extension `1 → {±1} → Comm → T ⋊ B₃ → 1` is identified as non-split (two independent
  obstructions), but its class in `H²(T ⋊ B₃, Z₂)` is not further classified here.
- The seven irreducible-component dimensions are computed from the exact character sum and
  the eigenspace decomposition; they are not matched to an abstract character-table
  classification of `Comm`.
- Theorems at these sizes: `|Comm| = 96N`, kernel `{±1}`, the `= B₃` identification,
  `I = T ⋊ B₃`, non-splitness by both obstructions, `|[Comm,Comm]| = 12N` with
  `[I,I] = T_even ⋊ A₄`, `H ∩ Comm` of order `12N` with `3N` intersection, the
  `D₃ ⊂ O ⊂ B₃` chain, `dim ker D2 = 8`, and `End_Comm(C^N) = C[D2]` with 7
  multiplicity-free irreducibles are established at L=4 and L=6. The L-stability of this
  common FORM (the same `B₃`, the same 6 body-diagonal matrices, `96N`, `12N`, `3N`,
  `N/2` even sublattice, `A₄`/`D₃`/`O` chain, `dim ker = 8`, seven irreducibles) is an
  observation at two sizes, stated as a conjectured stable pattern — the general-L
  statement is the next path this opens, not a theorem here.
- The body-diagonal `D₃` identification (and the `B₃` and `O` identifications) are
  computed set equalities against independently built reference matrices at these two L,
  matched on order, full order-spectrum, and determinant set. The `A₄` identification of
  the derived subgroup's point-group image is matched on order, full order-spectrum, and
  determinant set as a subgroup of the set-equality-verified `B₃` — which forces `A₄`,
  since the det-`+1` half of `B₃` is `O ≅ S₄` and its unique order-12 subgroup is `A₄`.
- The single dependency row (the landed Unit 25 characterization) is landed on main but
  itself unaudited; its anchors (`Comm`, `|Comm| = 96N`, `dim End_Comm = 7`, `g_r4`, `H`)
  are consumed here as landed values, not as audited facts.

## Honest-auditor read

- The dangerous move this unit could make is to presuppose the extension splits — to write
  `Comm ≅ ⟨−1⟩ × (T ⋊ B₃)`. It does not: two independent computations refute it, an
  involution whose lift squares to `−1` (192 of 359 at L=4, 400 of 799 at L=6) and the
  containment `−1 ∈ [Comm, Comm]`. Either alone obstructs a section; both are printed.
- Every completeness claim is built to fail if the object were wrong. The minimal-polynomial
  gate multiplies exact integer matrices and checks that the full product vanishes AND that
  each of the four drop-one-factor products is nonzero (`.any()` on the exact `int64`
  matrix), so degree 7 is discriminated, not assumed. The character-norm gate is the actual
  mean of `|χ_k|²` and `χ_j·conj(χ_k)` over all `|Comm|` elements, not an asserted `1`. The
  `B₃`, `D₃`, and `O` identifications compare order, full order-spectrum, and the
  determinant set against reference matrices built from scratch, and additionally as full
  set equalities; the `A₄` identification rests on order, full order-spectrum, and
  determinant set inside the set-equality-verified `B₃`, which admits exactly one
  order-12 all-det-`+1` subgroup — an order-only check would not distinguish these.
- The `96N` law is derived, not fitted: kernel size 2 times `|I| = |T|·|B₃| = N·48`, with
  `T` shown normal in `I`, the 48 canonical representatives shown linear on all N sites and
  equal to `B₃`, and closed under composition. The seven-generator closure independently
  recovers the full `|Comm|`.
- The tie-back order coincidence is recorded with its resolution: `H ∩ Comm` and
  `[Comm, Comm]` both have order `12N` yet are different subgroups (intersection `3N`,
  printed), and the determinant grading explains why the landed rotation witnesses reach only
  the det-`+1` chain `D₃ ⊂ O ⊂ B₃`. At L=4 the full-closure route and the matrix-land route
  are checked to agree.
- Residual softness a reader should weigh: the group facts and the minimal polynomial are
  exact integers, but the eigenspace dimensions and the seven projector-character norms come
  from a floating Hermitian diagonalization of `i·D2` (observed character deviations at the
  `~1e-15` level, gated at `1e-9`/`1e-12`); the tolerances are conventional choices well
  inside those margins, not derived bounds. Every L-stable statement here is an observation
  at two sizes, not a proof for all L.

This row is unaudited: its grade is set exclusively by the independent audit lane on
origin/main, not by this note or its runner.
