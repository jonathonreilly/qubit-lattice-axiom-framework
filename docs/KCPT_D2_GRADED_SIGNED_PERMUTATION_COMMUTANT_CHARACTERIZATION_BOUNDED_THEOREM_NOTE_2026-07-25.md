# KCPT D2 graded signed-permutation commutant characterization (L=4 and L=6) (bounded theorem)

**Type:** bounded_theorem

registry id: `kcpt_d2_graded_signed_permutation_commutant_characterization`

## claim_scope

- **Kind:** bounded_theorem. Exact integer group enumeration plus finite-dimensional
  matrix-algebra closures on the fixed staggered lattices L ∈ {4, 6}
  (N = 64 and N = 216 on the L³ torus). Every statement is an exact statement about
  signed permutations, group orders, character sums, and Frobenius projections of those
  two finite objects.
- **Object:** the full signed-permutation commutant
  `Comm(D2) = { signed permutation U : U D2 = D2 U }`, the symmetry group
  `H = closure(G_amb ∪ {S_eps})` and the dressed-rotation extension `<H, g_r4>` located
  inside it, and the Z₂ grading `grade(U) : U D2 U⁻¹ = grade(U) · D2 ∈ {+1, −1}` induced
  on the graded commutant `GC = closure(Comm ∪ {S_eps})`.
- **Scope limits:** r-neutral. No physical, continuum, or thermodynamic claim is made;
  every quantity is a numerical invariant of the finite L ∈ {4, 6} construction. The two
  lattice sizes are two separate exact measurements, not a general-L statement.

## 1. Objects and setup

- Lattices L = 4 (N = 64) and L = 6 (N = 216) on the L³ torus; staggered integer
  antisymmetric adjacency `D2` with `eta_0 = 1`, `eta_1 = (-1)^{x0}`,
  `eta_2 = (-1)^{x0+x1}`. `D2` has integer entries and `D2 = -D2ᵀ` (both gated). `M = D2²`
  has spectrum `[0, -4, -8, -12]` with shell multiplicities `[8, 24, 24, 8]` at L=4, and
  `[0, -3, -6, -9]` with `[8, 48, 96, 64]` at L=6 (spectrum and multiplicities pinned in
  the STRUCT gates).
- `G_amb` = the group of D2-commuting signed permutations built from the affine linear
  bases {identity, `(-x1,-x0,-x2)`, `(x1,x2,x0)`}, the N torus translations, and the 64
  quadratic GF(2) sign fields; `|G_amb| = 768` (L=4), `2592` (L=6). Adjoining the Dirac
  sign operator `S_eps = diag((-1)^{x0+x1+x2})` gives `H = closure(G_amb ∪ {S_eps})`,
  `|H| = 1536` (L=4), `5184` (L=6), `[H : G_amb] = 2`, with `S_eps` not in `G_amb`.
- Natural Dirac core `A_nat = <D2, J_full, S_eps>` has complex dimension 16 at both L
  (gated). The `J_full` properties (real antisymmetric, `J_full² = -I`) are construction
  context carried over from the landed L=6 surface-change lane, not re-gated here.
- Dressed four-fold rotation witness (reproduced through the enumerator, matching the
  landed L=6 gate `B8` and its L=4 analog `E4b`):

      r4_perm = sp_from_fmap(lambda x: (x1, -x0, x2), ...)
      r4_sign = sp_diag(lambda x: (-1)^{x0*x1 + x0}, ...)
      g_r4    = compose(r4_sign, r4_perm)

  `g_r4` commutes with `D2` exactly yet lies outside `H` at both L.

All objects are recomputed from scratch by the runner
`scripts/kcpt_d2_graded_signed_permutation_commutant_characterization_2026_07_25.py`
(stdlib + numpy only). The construction block (lattice, signed-permutation helpers,
`G_amb`/`H`, `A_nat`, the per-shell H-averaged commutant, isotypic blocks, `sep6`, and
`g_r4`) matches the landed L=6 surface-change and separator-census lanes
statement-for-statement in its executable code; the commutant enumerator, sign lift,
exhaustive commutation
verification, and grade map are written fresh for this unit. All group-theoretic decisions
(commutation, membership, closure, order, grade) use exact integer signed-permutation
arithmetic and `array_equal`; no floating tolerance enters any group decision.

## 2. Theorem claims

**T1 (structure recap; gates STRUCT_L4, STRUCT_L6).** `D2` has integer entries and is
antisymmetric; its support graph is connected. `|G_amb| = 768 / 2592`, `|H| = 1536 / 5184`,
`[H : G_amb] = 2` with `S_eps` outside `G_amb`, and `dim A_nat = 16` at L = 4 / 6.

**T2 (full commutant, enumerated and verified; gates AUT_ENUM, LIFT, COMM_VERIFY).** The
support graph of `D2` (vertices = sites, edges = the pairs with `D2[i,j] ≠ 0`) has
automorphism group `Aut = { T_v ∘ σ : v a site, σ ∈ Stab(0) }`, where `T_v` is translation
by site `v` and `Stab(0)` is the site-0 stabilizer, enumerated by pruned backtracking and
verified by exact permuted-adjacency equality. `|Stab(0)| = 720 / 48`, and
`|Aut| = N · |Stab(0)| = 46080 / 10368` (orbit–stabilizer, translations acting transitively
and freely on sites; ≥ 200 listed automorphisms spot-verified exactly, all keys distinct).
Each automorphism `p` admits at most one sign lift up to the global flip `s → −s` (the
support graph being connected), found by propagating `s_i s_j D2[p(i),p(j)] = D2[i,j]` over
a spanning tree from site 0 and verified on every support pair. The sign-liftable count is
`3072 / 10368`, equal to `48 · N` at both L, and

    Comm(D2) = { P_p · diag(s) : p sign-liftable, s ∈ {+s_p, −s_p} },
    |Comm| = 2 × (liftable count) = 6144 (L=4), 20736 (L=6).

Every one of the `6144 / 20736` elements is verified to satisfy `U D2 = D2 U` exactly over
all N·N entries (zero failures), and ≥ 400 deterministic pairwise products land back in the
`Comm` key set. `|Comm|_{L=4} = 6144 ≠ 20736`: the two lattice sizes give genuinely
different commutants (rejector gate `COMM_REJECT_L4`).

**T3 (Z₂ grading; gates GRADE_SEPS, GRADE_MULT, GRADE_PART).** `S_eps D2 S_eps = −D2`
exactly, so `grade(S_eps) = −1` and `S_eps` is not in `Comm`; consequently `H` is not
contained in `Comm`, with `S_eps` the named witness. The grade map is multiplicative:
`grade(UV) = grade(U)·grade(V)` on ≥ 400 deterministic products inside `GC`. No element of
`H`, `<H, g_r4>`, or `GC` is "neither" (all lie in {+1, −1}; the neither-count is gated to 0
in each). `H` splits `(768, 768, 0)` (L=4) and `(2592, 2592, 0)` (L=6) into
commuting/anticommuting/neither; `<H, g_r4>` splits `(3072, 3072, 0)` and
`(10368, 10368, 0)`. The commuting part `H⁺ = G_amb` lies in `Comm`, and `<H, g_r4>⁺` lies
in `Comm`, at both L.

**T4 (graded commutant; gate GC).** `GC = closure(Comm ∪ {S_eps})` has order
`12288 (L=4)` and `41472 (L=6)`, equal to `2·|Comm|` at both L; its grade partition is
`(|Comm|, |Comm|, 0)`, so `Comm` is exactly the grade `+1` kernel of `GC` (index 2) and the
grade `−1` coset is `S_eps · Comm`. `Comm`, `H`, and `<H, g_r4>` are all subgroups of `GC`,
and `[GC : H] = 8` at both L. The graded commutant, not `H`, is the ambient signed-permutation
object carrying both the commuting symmetries of `D2` and the anticommuting Dirac sign.

**T5 (order coincidence forced by the grading; gate ORDER_COINCIDENCE).**
`|<H, g_r4>| = |Comm|` at both L (`6144` at L=4, `20736` at L=6), yet `<H, g_r4> ≠ Comm` as
subgroups: `|Comm \ <H, g_r4>| = |<H, g_r4> \ Comm| = |Comm|/2` (`3072 / 10368`). Explicit
deterministic witnesses are exhibited — an element of `Comm \ <H, g_r4>` with grade `+1`,
and an element of `<H, g_r4> \ Comm` with grade `−1` (the latter cannot be in `Comm`, whose
elements are all grade `+1`). The order equality is forced by the grade map:
`|<H, g_r4> ∩ Comm| = |Comm|/2` at both L, i.e. `<H, g_r4>` has an index-2 commuting part
sitting inside `Comm` together with an equal-size anticommuting coset, so its order matches
`|Comm|` structurally rather than by numerical accident.

**T6 (endomorphism dimensions; gates END_COMM, END_HG, END_H).** With
`c(K) = mean_{U∈K} χ(U)²`, `χ(U) = Σ_{i: p(i)=i} s_i`, equal to the complex dimension of the
endomorphism algebra `End_K(C^N) = Σ m_i²`:
`dim End_Comm(C^N) = 7` at BOTH L (the L-stable headline); `dim End_{<H,g_r4>} = 4 (L=4)`
and `7 (L=6)`, cross-checked against the per-shell commutant sums `[1,1,1,1]` and
`[1,2,2,2]` computed by the H-averaged shell machinery; and `dim End_H = 6 (L=4)`,
`19 (L=6)`, reproducing the landed anchors. Passing from `H` to the full commutant — two
groups, neither containing the other (T3, T5) — the endomorphism dimension changes from
`6 → 7` (L=4) and `19 → 7` (L=6): the commutant's endomorphism algebra is L-stable at 7
while `dim End_H` grows `6 → 19` with L.

**T7 (algebra reach of the dressed rotation; gate WORD_R4).** The real word algebra
`<A_nat, g_r4>` has complex dimension `52 (L=4)` and `60 (L=6)`, closed under basis cap 600
at both L. Through the fresh enumerator `g_r4` is an element of `Comm \ H` at both L — an
independent confirmation, from the exhaustive commutant, of the landed `B8`/`E4b` fact that
`H` is not the maximal signed-permutation symmetry group of `D2`. (The gate pins the reach
dimension exactly — 52 at L=4, 60 at L=6; the explicit `≠ 20` exclusion at L=6 is kept
but redundant given the equality pin.)

**T8 (separator H-specificity, L=6; gates SEP6_ANCHOR, SEP6_GENSET_MOVE).** The ind-8
separator `sep6 = P8a − P8b` has rank sum 16 and `||sep6||_F = 4`, and is invariant under the
generators of `H` and their inverses below the `1e-10` gate (observed `~1e-14`). A verified
generating set of `Comm` (its closure has exactly `|Comm| = 20736` elements) moves `sep6`:
the maximum displacement `||U sep6 Uᵀ − sep6||_F` over the generators is `8` and the mod-sign
variant `min(||U sep6 Uᵀ − sep6||, ||U sep6 Uᵀ + sep6||)` is `4√2`, both pinned by the gate
to `1e-9`. `sep6` is an
invariant of the `H`-structure, and the larger commutant actively moves it — not even up to
an overall sign.

**T9 (reach sample outside the landed census domain; gate OMEGA_SAMPLE).** For the first 5
deterministic elements of `Comm \ H` (sorted enumeration order), the reach observable
`omega(g) = ||Pi_{<A_nat,g>}(sep6)||_F² / ||sep6||_F²` measured `0` for all 5, each with word
algebra of complex dimension 32 and closed under cap 600. These 5 elements lie outside the
landed reach census (which ranged over `G_amb`); this is a deterministic sample of five, not
a census, and every measured value lies in the landed value set `{0, 1/4, 4/15, 1/3, 1/2, 1}`.

**T10 (rejectors; gates PERT1, PERT2).** The sign field `diag((-1)^{x0})` classifies as
"neither" under the grade map (`grade = 0`): it neither commutes nor anticommutes with `D2`,
proving the classifier is not a parity proxy that would misfile it. A deliberately corrupted
candidate — a valid `Comm` generator composed with a transposition of two adjacent sites —
fails the exact commutation check, proving the element-by-element verification is real.

## 3. Evidence — measured values

| quantity | L=4 (N=64) | L=6 (N=216) |
|----------|-----------:|------------:|
| `M` shell mults | `[8, 24, 24, 8]` | `[8, 48, 96, 64]` |
| `|G_amb|` | 768 | 2592 |
| `|H|`, `[H:G_amb]` | 1536, 2 | 5184, 2 |
| `dim A_nat` | 16 | 16 |
| `|Stab(0)|` | 720 | 48 |
| `|Aut|` = N·|Stab(0)| | 46080 | 10368 |
| sign-liftable = 48·N | 3072 | 10368 |
| `|Comm|` = 2×liftable | 6144 | 20736 |
| `Comm` element-verify failures | 0 | 0 |
| `grade(S_eps)` | −1 | −1 |
| `H` grade partition (+/−/0) | (768, 768, 0) | (2592, 2592, 0) |
| `<H,g_r4>` order, partition | 6144, (3072,3072,0) | 20736, (10368,10368,0) |
| `|<H,g_r4> ∩ Comm|` = |Comm|/2 | 3072 | 10368 |
| `|Comm \ <H,g_r4>|`, `|<H,g_r4> \ Comm|` | 3072, 3072 | 10368, 10368 |
| `|GC|` = 2·|Comm|, `[GC:H]` | 12288, 8 | 41472, 8 |
| `GC` grade partition (+/−/0) | (6144, 6144, 0) | (20736, 20736, 0) |
| grade-multiplicativity products | 400/400 | 400/400 |
| `dim End_Comm(C^N)` | 7 | 7 |
| `dim End_{<H,g_r4>}` (per-shell) | 4 `[1,1,1,1]` | 7 `[1,2,2,2]` |
| `dim End_H` | 6 | 19 |
| `dim <A_nat, g_r4>` (closed) | 52 (yes) | 60 (yes) |
| `g_r4` in `Comm \ H` | yes | yes |
| `sep6` rank sum, `||sep6||_F` | — | 16, 4.0 |
| `sep6` H-invariance residual | — | ≤ 1e-10 gated (observed ~1e-14) |
| `Comm`-generator max displacement / mod-sign | — | 8 / 4√2 (gated ±1e-9) |
| `omega` sample (5 of `Comm \ H`), dims | — | {0, 0, 0, 0, 0}, dim 32 each |
| `grade(diag((-1)^{x0}))` (PERT1) | — | 0 (neither) |
| corrupted-element commutes (PERT2) | — | False |

All 32 gates pass with zero failures; the runner prints `TOTAL: PASS=32 FAIL=0`, peak RSS
below 0.7 GB, wall-clock about 320 s.

## 4. The grading picture

The full signed-permutation symmetry structure of `D2` is not a single group but a
Z₂-graded pair. `Comm(D2)` is the exhaustively enumerated group of signed permutations
commuting with `D2`; `S_eps` anticommutes; and the graded commutant `GC` glues them, with
`Comm` as the grade `+1` kernel and `S_eps·Comm` as the grade `−1` coset. Both the landed
symmetry group `H` and its dressed-rotation extension `<H, g_r4>` embed in `GC`. `H`
straddles the grading — half of it (namely `G_amb`) commutes and half anticommutes — which
is exactly why `H` is not inside `Comm`. `<H, g_r4>` also straddles it, with an index-2
commuting part inside `Comm`; that index-2 structure is what makes `|<H, g_r4>|` coincide
with `|Comm|` while the two groups share only half their elements. The endomorphism
dimension over the full commutant is 7 at both sizes, a stability that `dim End_H` (6 at
L=4, 19 at L=6) does not share.

## 5. Dependencies

- [KCPT L=6 surface-change module structure, natural-algebra invariance (bounded theorem)](KCPT_L6_SURFACE_CHANGE_MODULE_STRUCTURE_NATURAL_ALGEBRA_INVARIANCE_BOUNDED_THEOREM_NOTE_2026-07-25.md)
- [KCPT L=6 ind8-separator reach census, surface comparison (bounded theorem)](KCPT_L6_IND8_SEPARATOR_REACH_CENSUS_SURFACE_COMPARISON_BOUNDED_THEOREM_NOTE_2026-07-25.md)

## Boundary

- The characterization is a finite fact about the two fixed staggered lattices L ∈ {4, 6}.
  Orders, grade partitions, endomorphism dimensions, and reach values are numerical
  invariants of those constructions; no continuum limit or physical content is claimed, and
  the statement is r-neutral.
- The identity `liftable = 48·N` holds at both measured sizes, but two data points are a
  two-point observation; a general-L scaling law is the next path this opens.
- The `omega` values are reported for a deterministic sample of five elements of `Comm \ H`,
  not a census. A full reach census over `Comm \ H` (the analog of the landed `G_amb`
  census, now over the strictly larger commutant) is another path this opens.
- The commutant is enumerated as exact integer signed permutations and verified
  element-by-element; the endomorphism dimensions come from exact character sums; the reach
  quantities are floating Frobenius projections. Gate tolerances: `1e-10` for the `sep6`
  norm and H-invariance anchor, `1e-9` for the `omega` sample and the pinned displacement
  values — all well inside the observed `~1e-14` residuals.
- The two dependency rows (the landed L=6 surface-change and separator-census lanes) are
  landed on main but themselves unaudited; their anchors (`dim End_H`, `sep6`, `g_r4`) are
  consumed here as landed values, not as audited facts.

## Honest-auditor read

- The dangerous move this unit could make is to presuppose that `H` (or `<H, g_r4>`) already
  is the full signed-permutation symmetry group of `D2`. It is not: the exhaustive commutant
  has order `6144 / 20736`, strictly larger than `H`, and `g_r4` is exhibited inside
  `Comm \ H` at both L through an enumerator that shares no code with the object it is
  testing. The enumeration is verified two ways — every automorphism by permuted-adjacency
  equality, and every one of the `6144 / 20736` signed permutations by the full `U D2 = D2 U`
  identity — with explicit wrong-value rejectors (`|Comm|_{L=4} ≠ 20736`, the corrupted
  element failing commutation, the equality-pinned reach dimensions 52/60 with the kept
  `≠ 20` exclusion at L=6).
- The order coincidence `|<H, g_r4>| = |Comm|` is recorded with its explanation and its
  witnesses, not as numerology: the two groups are shown to differ as sets (deterministic
  elements on each side), and the coincidence is traced to the index-2 commuting part forced
  by the grade map (`|<H, g_r4> ∩ Comm| = |Comm|/2`). A reader who distrusts the explanation
  can check the two witness elements and the intersection order directly.
- The grade map is shown to discriminate: `S_eps` reads `−1`, the parity field
  `diag((-1)^{x0})` reads "neither" (a parity-proxy classifier would misfile it as `±1`), and
  grade multiplicativity is checked on 400 products. The zero "neither"-counts inside `H`,
  `<H, g_r4>`, and `GC` are printed even though they are zero.
- The separator claim is the H-specificity one only: `sep6` is invariant under `H` below
  the `1e-10` gate and is moved by the commutant generators by `4√2` up to sign (gated).
  The 5-element
  `omega` sample is labelled as a sample; all five read `0`, which lies in the landed value
  set, and no census-level claim over `Comm \ H` is made from it.
- Residual softness a reader should weigh: the endomorphism dimensions are exact integers
  (character sums), but the reach and displacement quantities are floating projections whose
  pinned values (`8`, `4√2`, the `omega` sample) are gated at `1e-9` (`1e-10` for the `sep6`
  anchor) while carrying observed errors at the `~1e-14` level; the tolerances are
  conventional choices well inside those margins, not derived bounds. The
  `dim End_Comm = 7` L-stability is a statement about two sizes, not a proof for all L.

This row is unaudited: its grade is set exclusively by the independent audit lane on
origin/main, not by this note or its runner.
