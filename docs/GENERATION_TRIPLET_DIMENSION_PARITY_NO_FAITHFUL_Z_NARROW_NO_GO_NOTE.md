# No 3-Dimensional Carrier of the Physical Rotation Carries the Spinor z Faithfully: the Generation Triplet Is the Adjoint (z Quotiented), Not a Left-Regular z-Realization

**Date:** 2026-06-02
**Claim type:** bounded_theorem (narrow no-go on a candidate route)
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it answers
an open sub-question negatively for the proposed faithful-z route.
**Primary runner:** `scripts/frontier_generation_triplet_dimension_parity_no_faithful_z.py` (SCORECARD PASS=31)

## Context (the open sub-question / the attacked assumption)

The on-site bridge no-go
`KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02` shows that
the **natural** spinor->vector map (adjoint / Bloch / Hopf, `q |-> q v q^{-1}`)
quotients the spinor central element `z = -1`: on the vector `R^3`,
`adjoint(z) = I_3`. Its own "Next paths" flags one explicitly non-equivariant
escape it did not settle, and the session question sharpens it:

> The on-site no-go uses the *squaring* (adjoint) map, where `z` acts `+1` on the
> vector `R^3`. But **left multiplication** on `H` (`q |-> z q = -q`) is
> **faithful** (`z` acts `-1`). Could the generation `C^3` be realized in the
> multi-site qubit algebra (left-regular) where `z` acts faithfully, carrying
> `z` onto the generation?

This note answers that route **negatively**, for a structural
dimension/parity reason that holds for *every* rotation-respecting candidate.
The parent grade-1 bridge note
`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02` already
identifies the generation triplet with `Cl(3,0)` grade-1 = the vector/adjoint,
where `z = +1`; this note proves no faithful-`z` alternative can replace it.

## Claim

The A5 premise is **true**: left multiplication `L_q` on the qubit's even
subalgebra `H = Cl(3,0)^+` carries `z = -1` faithfully (`L_{-1} = -I`). But it
does so on the **even-dimensional** module: `H ~ C^2` is the 2-dim **spinor**
(`spin-1/2`) irrep of the physical-rotation `SU(2)`, **not** `C^3`. The
generation triplet is **3-dimensional (odd)**, and:

> Because `z` is **central** in `SU(2)`, it acts as a scalar on any
> representation (Schur), and that scalar is the central character
> `z|_{spin j} = (-1)^{2j}`. Hence `z = -1` (faithful on the center) holds
> **iff** the representation is **spinorial** — a sum of half-integer-spin
> blocks. Every half-integer-spin irrep `spin-j` has **even** dimension
> `2j+1 in {2, 4, 6, ...}`. No sum of even numbers equals the **odd** number `3`.

Therefore **no 3-dimensional carrier of the physical rotation carries `z`
faithfully** — not the single adjoint, not a 3-dim slice of the left-regular
module, and not any `N`-fold multi-site tensor. The **unique** 3-dim rotation
carrier is `spin-1` = vector = `Cl(3,0)` grade-1 = the **adjoint**, on which
`z = +1` (quotiented), exactly as the grade-1 bridge note found. The faithful-`z`
object is the even-dimensional spinor `C^2`, a **different space** from the
generation `C^3`. **Classification: the faithful-`z` route is closed for a
dimension-parity reason; `z` is not transportable onto `C^3` by any
rotation-respecting realization. This is a narrow no-go on that route, not a
closure of the full bridge.**

### The computation (runner, all 31 checks pass)

- **(1) The A5 premise is real but lands on `C^2`.** `L_z = L_{-1} = -I_4` on
  `H` (faithful: `z |-> -1`); as a complex left-`SU(2)` module `H ~ C^2 =`
  `spin-1/2` (dim 2, **even**). The adjoint, by contrast, sends
  `adjoint(z) = I_3` on `R^3` (`z` quotiented). The faithful-`z` carrier is the
  2-dim spinor, not the 3-dim vector.
- **(2) Central character.** For `j = 0, 1/2, 1, 3/2, 2`, the explicit `2 pi`
  rotation `exp(2 pi i J_z) = (-1)^{2j} I`, with the parity link
  `(z = -1) <=> (dim even)` verified on each.
- **(3) The core obstruction.** No purely-spinorial (`z = -1`) decomposition of
  dimension `3` exists (sum of evens `!= 3`); for every even target dimension
  `2, 4, 6` a spinorial carrier does exist (`(2,)`, `(2,2)`, `(2,2,2)`); `3` is
  odd; the unique 3-dim irrep is `spin-1` = vector = grade-1 = adjoint, `z = +1`.
- **(4) Multi-site / tensor steelman.** The diagonal physical rotation on `N`
  qubit sites is `(spin-1/2)^{(x)N}` with central character `z = (-1)^N`
  (verified against the explicit global-`2 pi` operator `(-I_2)^{(x)N}`). A 3-dim
  `spin-1` block appears **only for `N` even** (first `N = 2`), where `z = +1`;
  for `N` odd (`z = -1`) the module is purely half-integer-spin, so **no 3-dim
  block exists at all**. The conjunction "3-dim block AND `z = -1`" is **false
  for every `N`**.

### Why this is the right (and complete-for-this-route) statement

Any realization of the generation `C^3` that is a representation of the physical
rotation group must assign a single central scalar to `z`. The only freedom is
which spin blocks appear; the dimension `3` being odd forbids a uniform `z = -1`.
The three candidate forms the A5 premise could take —
(a) the adjoint/vector (grade-1), (b) a rotation-invariant 3-dim subspace of the
left-regular module, (c) an `N`-fold multi-site tensor block — are each covered:
(a) and (the only 3-dim block of) (c) are `spin-1`, `z = +1`; (b) does not exist
(the left-regular `H`-module under `SU(2)` has commutant the division ring
`H_right`, so its only invariant subspaces are `{0}` and all of `H`, dimension
`0` or `4`, never `3`). The faithful-`z` left module is genuinely `C^2`.

## No-Go Discipline Gate

This gate applies only to the **faithful-`z` (left-regular / multi-site)
realization** of the generation triplet `C^3`. It does not foreclose the full
bridge.

- **N1 alternative routes:** (1) single adjoint/Bloch/Hopf (`z |-> +1` on `R^3`);
  (2) left multiplication `L_z = -1` (faithful but on `C^2`, even dim);
  (3) a 3-dim rotation-invariant slice of the left-regular module (does not
  exist; commutant is a division ring); (4) `N`-fold multi-site tensor (3-dim
  block only at `N` even, `z = +1`); (5) a non-equivariant frame-dependent
  spinor-axis `<-> [1,1,1]` glue (still an import, untouched here).
  Routes (1)-(4) cannot put a faithful `z` on a 3-dim rotation carrier.
- **N2 wall independence:** the dimension-parity obstruction and the
  non-equivariant frame glue are distinct; closing the faithful-`z` route does
  not close a posited frame identification.
- **N3 hidden-wall scan:** "rotation-respecting" means a representation of the
  physical-rotation `SU(2)` (the merger `SU(2)`); the only input is the central
  character `z = (-1)^{2j}`, standard finite `SU(2)` representation theory.
- **N4 residual matching:** the parent adjoint no-go asked whether `z` can be
  transported onto the vector by any rotation-equivariant map; this note answers
  the specific *faithful left-regular / multi-site* sub-residual: even dropping
  equivariance of the *map* and using a faithful *module*, the **dimension
  parity** of `C^3` forbids `z = -1`.
- **N5 rhetoric audit:** "no 3-dim carrier carries `z` faithfully" means "no
  representation of the physical rotation on a 3-dim space has `z` acting as
  `-1`," a parity fact. It does not claim no future non-representation-theoretic
  structure could relate the two `Z_2`s.
- **N6 partial-closure scan:** a frame-selection theorem, a binary-octahedral
  discrete-sign carrier, or an `O_h`-equivariant (richer than `C_3`) construction
  could still relate the signs by additional structure.
- **N7 steelman:** a reviewer may insist `z` "must" reach the generations because
  it is the same `Z_2` in the continuum spin-statistics story. The steelman fails
  on parity: `z = (-1)^{2j}` is `+1` on every integer-spin (odd-dim) carrier, and
  the generation triplet is exactly such a carrier.
- **N8 cross-cycle echo:** consistent with the retained
  `binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28`
  (`z` central, acts `+1` on every non-spinorial / integer-spin rep) and with the
  adjoint-map no-go; this is the dimension-parity version of the same decoupling.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `koide_adjoint_map_quotients_spinor_z2_narrow_no_go_note_2026-06-02` | unaudited (the parent route this sharpens; freshly merged) |
| `koide_generation_id_cl3_grade1_bridge_narrow_theorem_note_2026-06-02` | unaudited (identifies generation = grade-1 = adjoint; freshly merged) |
| `binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28` | retained_bounded |
| `per_site_su2_spin_half_theorem_note_2026-05-02` | retained |
| `parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23` | retained_bounded |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | retained_bounded |

The `internal_external_su2_merger_from_universal_property` row is **unaudited**
on origin/main and is **not** load-bearing here: the result is self-contained
finite `SU(2)` representation theory (central character `z = (-1)^{2j}`),
independent of how the physical-rotation `SU(2)` is sourced.

## Non-circularity

The central character, the spin-block decomposition, the left/right
multiplication matrices, and the tensor spin content are direct finite-dimensional
computations. `Q = 2/3`, fermionic statistics (CAR), and any `z`-transport are
**never** assumed; the conclusion (no faithful-`z` 3-dim carrier) is computed.

## Next paths this opens

- The faithful-`z` object is the **even-dimensional** spinor `C^2`. The remaining
  way to relate the two `Z_2`s is therefore a **non-representation-theoretic**
  pairing of the 3-dim generation `C^3` with the 2-dim spinor `C^2` (e.g. a
  framework-canonical `spinor-axis <-> [1,1,1]` glue), which the adjoint-map
  no-go already flagged as an open import. This note shows the *representation*
  route cannot supply it.
- The `O_h`-on-axes symmetry (48 signed permutations) is richer than the `C_3`
  and `SO(3)` structures used here; whether an `O_h`-equivariant pairing of the
  vector and spinor carriers is forced (rather than posited) is unexplored.
- The generation **count** `3` (the odd dimension that creates the obstruction)
  is itself the prize question; the parity obstruction is a structural feature of
  that odd count, not an independent wall.

This is a narrow no-go on the faithful-`z` realization route, localizing the
remaining freedom to a non-representation-theoretic spinor/vector pairing; it is
not a closure of the full bridge.
