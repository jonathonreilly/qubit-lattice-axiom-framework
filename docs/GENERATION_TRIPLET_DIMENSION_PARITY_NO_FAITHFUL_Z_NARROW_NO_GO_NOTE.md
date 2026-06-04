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

## No-Go Discipline Gate (N1–N8)

**Status:** PASS for the narrow faithful-`z` (Z₂-graded / spinorial / CAR)
realization route only. The claim being closed is **not** a repo-wide claim that
the generation triplet is undefinable, **not** a rejection of the
`Q = 2/3 <-> r = 1/2` value structure, and **not** a closure of the full
spinor/vector bridge. It is the single structural statement that **no 3-dim
representation of the physical-rotation `SU(2)` carries the spinor center
`z = -1` faithfully**, because the only 3-dim irrep is the integer-spin
(`spin-1`) vector on which `z = (-1)^{2·1} = +1`, and no multiset of even
dimensions sums to the odd integer `3`. The faithful-`z` (CAR/spinor) structure
is therefore hosted on the **site** `C^2` (`spin-1/2`, even, faithful), not on
the **generation** `C^3` — the value-on-`C^3` / carrier-on-`C^2` factorization,
independent of any welding posit.

### N1 — Alternative route enumeration

Every candidate way to put a *faithful* `z` (a genuine Z₂-graded / CAR /
double-cover sign) onto the 3-dim generation carrier `C^3`. The marker column
records whether the runner exercised the route.

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| (Q1) Single adjoint / Bloch / Hopf `q v q^{-1}` | Carry `z` onto `R^3` via the natural `SU(2)->SO(3)` squaring map. | `z = -1` lies in the kernel `{+1,-1}` of `SU(2)->SO(3)`; `adjoint(z) = I_3`. `z` is **quotiented**, exactly the parent adjoint no-go. | ATTEMPTED |
| (Q2) Faithful left multiplication `L_z = -I` on `H = Cl(3,0)^+` | Use the genuinely faithful left action (`z |-> -1`) instead of the squaring map. | The action is faithful, but its module is `H ~ C^2` = `spin-1/2`, dimension **2 (even)** — it lands on the **site spinor**, never on the 3-dim `C^3`. | ATTEMPTED |
| (Q3) A 3-dim rotation-invariant slice of the left-regular module | Restrict `L_z` to a 3-dim `SU(2)`-invariant subspace of `H` to keep faithfulness and reach dimension 3. | No such slice exists: the commutant of left-`SU(2)` on `H` is the division ring `H_right` (Schur), so the only invariant subspaces are `{0}` and `H`, of dimension `0` or `4` — **never `3`**. | ATTEMPTED |
| (Q4) `N`-fold multi-site tensor `(spin-1/2)^{(x)N}` | Build a 3-dim block inside many qubit sites where the global `z = (-1)^N` is faithful. | A 3-dim `spin-1` block appears **only for `N` even** (first `N=2`), where `z = (-1)^N = +1`; for `N` odd (`z = -1`) the module is purely half-integer-spin and has **no 3-dim block at all**. "3-dim block AND `z = -1`" is false for every `N`. | ATTEMPTED |
| (Q5) Direct even-dimension partition of `3` | Find any multiset of spinorial (even-dim) blocks `{2,4,6,...}` summing to `3` so a purely-`z=-1` 3-dim carrier exists. | A sum of even integers is even; `3` is odd. **No partition exists** (the runner enumerates all even-dim multisets up to `6` and finds none totalling `3`). | ATTEMPTED |
| (Q6) Promote `Gamma_chi`'s `+-1` on `R^3` to the faithful `z` | Reinterpret the value-side sign partition `{+1,-1,-1}` (signed-`sqrt(m)`) as the double-cover sign. | `Gamma_chi` lives on the **vector** (`spin-1`, `z=+1`) module; its `+-1` is an adjoint eigenvalue, not the central element. `q_gc^2 = z` but `adjoint(q_gc^2) = I_3`. The two `Z_2`s are distinct objects, not one faithful `z`. | ATTEMPTED |
| (Q7) Non-equivariant frame glue `spinor-axis <-> [1,1,1]` | Identify a chosen spinor axis with the body diagonal by hand to drag `z` onto `R^3`. | This is the **open import** flagged by both parents; it is a posited, frame-dependent identification, **not** a rotation-respecting realization. **Left explicitly out of scope** — not closed here. | OUT OF SCOPE |

Routes (Q1)–(Q6) each fail the faithful-`z`-on-`C^3` conjunction for a structural
reason; (Q7) is the single non-representation-theoretic residual, deliberately
left open.

### N2 — Wall-independence audit

The collapsed wall set for this no-go has **one** load-bearing wall: the
**dimension-parity** fact that the central character `z = (-1)^{2j}` is `+1` on
every odd-dimensional (integer-`j`) rotation carrier, and no even-dimensional
(spinorial) blocks sum to the odd dimension `3`. The four sub-routes (Q1)–(Q4)
are **not** four independent walls — they are the kernel-quotient view (Q1, Q6),
the wrong-module view (Q2), the no-invariant-slice view (Q3), and the
wrong-parity-of-`N` view (Q4) of the **same** parity obstruction. In particular,
this no-go is **independent of** the chirality/circulant wall
`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` (which constrains
`comm(R) ∩ anticomm(Gamma_chi)` on the *value* operator) and of the `r = 1/2`
amplitude pin: none of those are consumed here, and resolving them would not
change the parity of `3`. Conversely, closing the open frame-glue route (Q7) by
some future structure would not alter the single-`z`-character identity, so the
two are genuinely separate walls.

### N3 — Hidden-wall scan (explicit load-bearing inputs)

The only load-bearing inputs for the negative result are made explicit:

1. **Standard finite-`SU(2)` representation theory** — every finite-dim rep
   decomposes into `spin-j` irreps of dimension `2j+1`.
2. **The central character** `z = exp(2 pi i J_z) = (-1)^{2j} I` on `spin-j`
   (Schur: `z` central ⇒ scalar on each irrep). This is the *sole* physics input.
3. **Parity arithmetic** — `2j+1` is even iff `j` is half-integer; a sum of even
   integers cannot equal the odd integer `3`.
4. **Schur commutant on the left-regular module** — the commutant of left-`SU(2)`
   on `H` is `H_right`, a division ring, so invariant subspaces have dimension
   `0` or `4` (used only to dispatch route Q3).

The words "rotation-respecting", "faithful", "physical rotation", and "carrier"
are **not** used as hidden retained inputs: "rotation-respecting" means precisely
"a representation of the physical-rotation `SU(2)`"; "faithful" means precisely
"`z` acts as `-1`". No `Q = 2/3`, no CAR/fermionic-statistics assumption, no
chirality operator, no welding posit, and no PDG/literature comparator is
consumed. The `internal_external_su2_merger_from_universal_property` row is
**not** load-bearing: the argument only needs *that* there is a physical-rotation
`SU(2)` with this center, not *how* it is sourced.

### N4 — Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02` | Can a **rotation-equivariant map** `C^2 -> R^3` transport `z`? (No: it factors through `SO(3)`, `adjoint(z)=I_3`.) | The sharper **module-level** sub-residual that note's "Next paths" left open: drop equivariance of the *map*, use a genuinely *faithful module*. Even then, the **dimension parity** of `C^3` forbids `z = -1`. | yes (strict sharpening of the same open residual) |
| `KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02` | Is the grade-1 vector an algebraically compatible 3-dim carrier? (Yes, but vector-vs-spinor sign deferred.) | Confirms the carrier is the `z=+1` vector and proves **no faithful-`z` alternative** can replace it; closes the deferred "is there a faithful-`z` 3-dim carrier?" half of that note's open sign sub-question. | yes (answers the deferred sub-question) |
| `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28` (`retained_bounded`) | `z` central in `SU(2)`, acts `+1` on every non-spinorial / integer-spin rep (sign decoupled). | The **dimension-parity** form of the same `z = (-1)^{2j}` decoupling, applied to the specific 3-dim generation carrier. | yes (same decoupling, parity form) |
| `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16` (`retained_bounded`) | Circulant operators anticommuting with `Gamma_chi`: `comm(R) ∩ anticomm(Gamma_chi) = {0}`. | Orthogonal: a constraint on the **value operator's** symmetry, not on the **carrier's** central character. Listed as a sibling on the same gate, **not** as a witness for this parity no-go. | no |
| `koide_signed_eigenvalue_vs_singular_value_readout_…_2026-05-29` (`audited_failed`) | The signed-`sqrt(m)` readout sign a bridge would discharge. | Named only as the value-side `Z_2` the faithful-`z` route was *trying* to reach; **not** load-bearing for the negative conclusion. | no |

Non-matching witnesses (the `Z_3` anticommuting no-go and the signed-readout
note) are **not** used as load-bearing proof of this no-go; only the three
matching residuals carry it.

### N5 — Rhetoric audit (scope of "no-go", "cannot host", "parity")

- **"no 3-dim carrier carries `z` faithfully"** is scoped to: *no representation
  of the physical-rotation `SU(2)` on a 3-dim space has `z` acting as `-1`*. It
  does **not** claim no future *non-representation-theoretic* structure (e.g. an
  `O_h`-equivariant or frame-selection construction) could relate the two `Z_2`s.
- **"cannot host a faithful Z₂-graded / spinor structure on `C^3`"** means: the
  carrier `C^3`, *qua* `SU(2)`-rotation module, has central character `+1`, so a
  faithful (CAR/double-cover) grading cannot be a `C^3`-internal rotation rep. It
  does **not** claim `C^3` admits no algebra action of any kind.
- **"parity"** is used in the precise arithmetic sense (even-vs-odd dimension),
  **not** spatial parity `P`. The two are kept distinct; spatial parity is the
  separate subject of the cited `parity_violation_does_not_reach_generation_triplet`
  note and is not invoked here.
- The note **never** writes "only route", "closes the route", "exhausted", or any
  finite-enumeration framing for the full bridge; the live residual (Q7) and the
  `O_h` direction are explicitly carried forward.

### N6 — Partial-closure path scan (open paths, none a new axiom)

The following remain open and **none is a new axiom**:

1. **Non-representation-theoretic spinor/vector pairing** — a framework-canonical
   `spinor-axis <-> [1,1,1]` glue (route Q7) pairing the 2-dim faithful-`z`
   spinor `C^2` with the 3-dim generation `C^3` by structure other than a single
   `SU(2)` rep. This note shows the *representation* route cannot supply it; it
   does **not** assert the pairing is impossible by other means.
2. **`O_h`-equivariant construction** — the 48-element signed-permutation symmetry
   of the axes is strictly richer than the `C_3` / `SO(3)` structures used here;
   whether an `O_h`-equivariant vector/spinor pairing is *forced* (not posited)
   is unexplored.
3. **A discrete binary-octahedral sign carrier** — relating the signs through the
   `2O` double cover rather than a continuous `SU(2)` rep.

Each is a *partial-closure path*, not an axiom; the note adds none.

### N7 — Steelman

The strongest objection: *`z` "must" reach the generations because it is the same
`Z_2` that enforces spin–statistics in the continuum, and the three generations
are fermions, so the fermionic (Z₂-graded / CAR) sign should live on the
generation index.* This steelman is the best case for the faithful-`z` route. It
**fails on parity**, and the failure is structural, not incidental: the central
character is `z = (-1)^{2j}`, which is `+1` on **every** integer-spin
(odd-dimensional) carrier, and the generation triplet `C^3` is exactly such a
carrier (`spin-1`, the unique 3-dim irrep). The fermionic CAR/double-cover sign
is genuinely present — but on the **site** `C^2` (`spin-1/2`, `z=-1`, even,
faithful), which is a *different space* from `C^3`. So the steelman correctly
identifies that a faithful `z` exists in the framework; it is wrong only about
*where* it lives. This blocks the broad claim "the spinor `Z_2` cannot appear at
all"; it does **not** break the scoped no-go, which is solely about the 3-dim
generation carrier.

### N8 — Cross-cycle echo

Prior negative-claim overclaims in this repo failed by testing one
representative object and declaring an entire lane closed. This note avoids that
echo by (i) keeping the claim boundary at *the faithful-`z`-on-`C^3` conjunction*
and (ii) explicitly carrying forward the Q7 frame-glue and `O_h` routes. It is
**consistent with** the retained
`binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28`
(`retained_bounded`: `z` central, `+1` on every integer-spin / vector rep) and
with its own parent adjoint-map no-go: this is the **dimension-parity** statement
of the same `z`-decoupling that the binary-octahedral note made discretely and
the adjoint-map note made at the level of equivariant maps. The three notes are
the discrete-sign, equivariant-map, and dimension-parity faces of one
decoupling; this note adds the parity face, not a new wall and not a closure of
the bridge.

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
