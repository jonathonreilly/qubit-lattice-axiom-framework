# KCPT D2 commutant closed-form lifts and lattice-size independence (L = 4, 6, 8, 10, 12) (bounded theorem)

**Type:** bounded_theorem

registry id: `kcpt_d2_commutant_closed_form_lifts_lattice_size_independence`

**Primary runner:** `scripts/kcpt_d2_commutant_closed_form_lifts_lattice_size_independence_2026_07_25.py`

## claim_scope

- **Kind:** bounded_theorem. Exact integer signed-permutation algebra on the staggered
  operator `D2` of the `L³` torus, at the five even sizes L ∈ {4, 6, 8, 10, 12}
  (N = 64, 216, 512, 1000, 1728). The closed-form sign fields, the commutator signs, the
  element orders, the 2-torsion quadratic form, the liftability of the 48 point-group
  matrices, and the constructed element counts are exact integer facts at each of those
  five sizes. The exhaustive commutant enumeration used as an independent anchor is run
  at L ∈ {4, 6, 8, 10} only.
- **Object:** the signed-permutation commutant
  `Comm(D2) = { signed permutation U : U D2 = D2 U }` of the landed Unit 25 module; the
  three closed-form translation lifts `t_nu = (x ↦ x + e_nu, zeta_nu)` with
  `zeta_nu(x) = (-1)^{Σ_{mu > nu} x_mu}`; the commutator pairing `beta` they induce on
  `T/2T` and the quadratic form `q` on the 2-torsion points `(L/2)v`; the constructive
  lifts of the 48 hyperoctahedral matrices `B₃`; and the subgroup of `Comm(D2)` these
  `96N` elements generate.
- **Scope limits:** r-neutral. No physical, continuum, thermodynamic, flavour or
  generation-counting claim is made; every quantity is an exact invariant of a finite
  even-`L` construction. `L` even is required throughout for `zeta_nu` to be well defined
  on `Z_L`. The equality `|Comm(D2)| = 96N` is established where the exhaustive
  enumeration was actually run (L ∈ {4, 6, 8, 10}); at L = 12 the construction yields the
  lower bound `|Comm(D2)| ≥ 96N` and nothing stronger.

## 1. Objects and setup

- Lattices L ∈ {4, 6, 8, 10, 12} on the `L³` torus with the staggered integer
  antisymmetric adjacency `D2` of the landed Unit 25 lane: `eta_0(x) = 1`,
  `eta_1(x) = (-1)^{x_0}`, `eta_2(x) = (-1)^{x_0+x_1}`, and explicitly
  `D2[x, x+e_mu] = eta_mu(x)`, `D2[x, x-e_mu] = -eta_mu(x)`. The runner builds `D2` and
  the support structures by calling the landed module (`build_lattice`,
  `support_structures`); nothing about `D2` is re-implemented here.
- An element of `Comm(D2)` is stored as `g = (p, s)` with `p` a length-`N` permutation of
  the site basis and `s` a length-`N` sign array; the commutation condition is
  `s_i s_j · D2[p_i, p_j] = D2[i, j]` for all `i, j`, and composition is
  `compose(a, b) = (p_b[p_a], s_a · s_b[p_a])`. All group decisions in this unit are
  exact integer arithmetic on those arrays; no floating tolerance enters anywhere.
- Every prior unit in this lane read the structure of `Comm(D2)` off an EXHAUSTIVE
  enumeration of the group, which is what capped the lane at L ∈ {4, 6}. This unit takes
  that enumeration off the critical path: the translation lifts and the point-group lifts
  are written down in closed form from the staggered phases, and the enumeration
  (`enumerate_commutant`) is called only as an independent anchor at the sizes where it
  still fits the memory budget.
- The reference hyperoctahedral group `B₃` (order 48) is built independently inside this
  runner as the 48 signed 3×3 permutation matrices (`itertools.permutations` of the three
  axes times the eight sign patterns), so every point-group claim is checked against a
  from-scratch object rather than against the enumerator.
- What is new relative to the preceding restriction-localization unit
  (`KCPT_D2_COMMUTANT_EXTENSION_TRANSLATION_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-25`)
  is where `beta` comes from, and it should not be overstated. That unit obtained the
  commutator pairing `beta` from the ENUMERATED group at L ∈ {4, 6} — measuring it, then
  matching it uniquely against the 512 bimultiplicative candidates — and from `beta` it
  DERIVED the 2-torsion form `q` by an argument this unit reuses unchanged. This unit
  derives `beta` itself from the staggered phases, so the chain no longer passes through
  an enumeration at any point, and the same `q` argument then runs at L ∈ {8, 10, 12}
  where no enumeration is available. The increment is `beta`'s provenance and the
  resulting reach, not a first derivation of `q`.

## 2. Theorem claims

**T1 (closed-form translation lift; gates G1_TRANSLIFT_L\*, G2_UNIQUE_L\*, G5A_FLIP_L\*,
G5B_MASK_L\*).** For every even `L` and each `nu ∈ {0,1,2}` the signed permutation
`t_nu = (x ↦ x + e_nu, zeta_nu)` with

    zeta_nu(x) = (-1)^{ Σ_{mu > nu} x_mu }

lies in `Comm(D2)`, and it is the unique lift of the translation permutation with
`s(0) = +1`; hence that permutation has exactly two lifts, `±t_nu`.

*Derivation.* Write `p_nu : x ↦ x + e_nu`. On the `mu`-edge at `x` the commutation
condition `s_i s_j D2[p_i, p_j] = D2[i, j]` reads

    s(x) · s(x+e_mu) · eta_mu(x+e_nu) = eta_mu(x),

so `s(x) s(x+e_mu) = eta_mu(x) eta_mu(x+e_nu)` (signs are `±1`, so division is
multiplication). The `-e_mu` edges give the same relation, because
`D2[x, x-e_mu] = -eta_mu(x)` carries the minus on both sides. Now the staggered phases
are *lower-triangular in the coordinates*: `eta_mu` depends only on `x_0, …, x_{mu-1}`.
Therefore shifting the argument by `e_nu` changes `eta_mu` exactly when `nu < mu`:

    eta_mu(x + e_nu) / eta_mu(x) = (-1)^{[nu < mu]}.

Hence `s(x+e_mu)/s(x) = (-1)^{[nu < mu]}`: the sign field must flip across a `mu`-edge
precisely when `mu > nu`, and be constant across the others. The field
`zeta_nu(x) = (-1)^{Σ_{mu > nu} x_mu}` does exactly that, and it is well defined on `Z_L`
precisely because `L` is even. Explicitly `zeta_0 = (-1)^{x_1 + x_2}`,
`zeta_1 = (-1)^{x_2}`, `zeta_2 = +1`.

*Uniqueness.* The nearest-neighbour support graph of `D2` is connected (gated: BFS from
site 0 reaches all `N` sites at every `L` here), so the edge relations propagate `s` from
`s(0)` along a spanning tree and determine it completely; the only freedom is the one
global sign. The runner does not assume this — it runs the propagation from `s(0) = +1`
independently of the closed form and checks that the propagated field equals `zeta_nu`
site by site.

*Discrimination.* Two wrong-value rejectors are run rather than an algebraic identity that
would hold by construction. (a) Flipping the sign of `zeta_nu` at a SINGLE site breaks
commutation: exhaustively over all `N` sites at L ∈ {4, 6} (192/192 and 648/648 failures
over the three `nu`), and over a deterministic stride-`N//32` 32-site subset at
L ∈ {8, 10, 12} (96/96 failures each). (b) Each of the 7 alternative exponent masks —
every subset of `{0,1,2}` other than the correct `{mu : mu > nu}` — yields a sign field
that fails commutation: 21/21 at every `L`, while the correct mask commutes 3/3. So the
mask `{mu : mu > nu}` is singled out by the computation, not by fiat.

**T2 (analytic commutator form; gates G4_BETA_L\*, G4X_LIFTPROD_L4, G4X_LIFTPROD_L6).**
For all `a, b`,

    [t_a, t_b] = (-1)^{1 - delta_ab} · I,

i.e. the commutator is the central scalar `-1` whenever `a ≠ b` and `+1` when `a = b`. Its
bimultiplicative extension to `T/2T ≅ F_2³` is

    beta(s, t) = (-1)^{ (Σ s)(Σ t) - s·t }.

*Derivation.* The two translation permutations commute, so `[t_a, t_b]` has trivial
permutation part and its sign is a constant, obtained by comparing the two orders of
transport: `t_a` translates by `e_a`, which multiplies `zeta_b` by
`zeta_b(x+e_a)/zeta_b(x) = (-1)^{[a > b]}` (shifting by `e_a` flips `zeta_b` exactly when
`a` lies in the mask `{mu : mu > b}`), and symmetrically `t_b` multiplies `zeta_a` by
`(-1)^{[b > a]}`. The commutator sign is the product,

    [t_a, t_b] = (-1)^{[a>b] + [b>a]} I = (-1)^{1 - delta_ab} I,

since exactly one of `a > b`, `b > a` holds when `a ≠ b` and neither holds when `a = b`.
Bimultiplicativity then gives, for `s = Σ s_a e_a` and `t = Σ t_b e_b`,
`beta(s,t) = Π_{a,b} beta(e_a,e_b)^{s_a t_b} = (-1)^{Σ_{a≠b} s_a t_b}`, and
`Σ_{a≠b} s_a t_b = (Σ s)(Σ t) - s·t`.

This is the same form the preceding restriction-localization unit measured and identified
at L ∈ {4, 6}: that unit obtained it from the enumerated group, and this unit derives it
from the staggered phases. The runner does not take it on trust — it forms the nine
ordered commutators from the ACTUAL closed-form lifts at every `L`, checks each is central
(9/9) and matches the `a ≠ b` rule, checks the bimultiplicative extension against the
closed formula on all 64 pairs of `F_2³` classes at every `L`, and at L ∈ {4, 6}
additionally checks the extension against commutators of actual lift PRODUCTS for all
8 × 8 class representatives (64/64 central, 64/64 matching).

**T3 (order and 2-torsion; gates G6_ORDER_Q_L\*, XL_DICHOTOMY).** `(t_nu)^k` has sign
field `zeta_nu^k`, so `t_nu` has order exactly `L` and `(t_nu)^L = +I`. On the 2-torsion
points of `T`,

    q((L/2) v) = (-1)^{ (L/2)² Σ_{i<j} v_i v_j },      v ∈ {0,1}³,

giving a clean `L mod 4` dichotomy: `L ≡ 0 (mod 4)` ⇒ `q` is trivial on all 8 `v`;
`L ≡ 2 (mod 4)` ⇒ `q = -I` on exactly the four `v` with at least two odd entries.

*Derivation.* The mask `{mu : mu > nu}` does not contain `nu`, so `zeta_nu` is independent
of `x_nu` and `zeta_nu(x + e_nu) = zeta_nu(x)`. Powering `t_nu` therefore accumulates no
cocycle: `(t_nu)^k = (x ↦ x + k e_nu, zeta_nu^k)`. This is the identity exactly when both
`k ≡ 0 (mod L)` and `zeta_nu^k ≡ +1`. Since `zeta_nu² = +1`, the second condition holds for
every even `k`; it is a genuine extra requirement only for `nu ∈ {0, 1}`, where `zeta_nu` is
a nonconstant character, and is vacuous for `nu = 2`, where `zeta_2 = +1` identically. Either
way `L` is even, so `k = L` is the first such `k` for all three `nu`: the order is exactly
`L`, with `(t_nu)^L = +I`. For the 2-torsion form,
let `g_v = Π_nu (t_nu)^{(L/2) v_nu}`; squaring it and reordering the product to pair like
factors costs one `beta` factor per transposed pair, while each like pair contributes
`((t_a)^{L/2})² = (t_a)^L = +I`, leaving
`q((L/2)v) = Π_{a<b} beta(e_a,e_b)^{(L/2)² v_a v_b} = (-1)^{(L/2)² Σ_{a<b} v_a v_b}`.
The dichotomy is then arithmetic: `(L/2)²` is even iff `L ≡ 0 (mod 4)`; and for
`L ≡ 2 (mod 4)`, `Σ_{a<b} v_a v_b` is odd exactly for the four `v` with two or three ones.

*Measured `q = -I` sets.* The runner squares the ACTUAL half-power products and reads the
central sign, then compares against the formula (8/8 agreement at every `L`). Measured:
empty at L = 4, 8, 12; and `{(0,1,1), (1,0,1), (1,1,0), (1,1,1)}` at both L = 6 and
L = 10 — the four points with at least two odd entries, exactly as the dichotomy predicts.
Both branches are confirmed at a new size: L = 8 is the first check of the
`L ≡ 0 (mod 4)` branch beyond the previously enumerable L ∈ {4, 6}, and L = 10 the first
check of the `L ≡ 2 (mod 4)` branch beyond L = 6.

**T4 (constructive point-group lifts; gates G7_B3_L\*, G8_SHEAR_L\*, G7E_ENUM_L\*).** At
each `L ∈ {4, 6, 8, 10, 12}` and for every `A` in the 48-element hyperoctahedral group
`B₃`, the permutation `x ↦ A x mod L` admits a consistent sign propagation over the
support graph of `D2`, hence exactly two lifts `±`. Combined with T1 this constructs
`2 · 48 · N = 96N` distinct elements of `Comm(D2)` at those five sizes, with NO
enumeration. Unlike T1–T3 this claim is quantified over the sizes tested, not over all
even `L` — see the derivation note below.

*Derivation and check.* `A ∈ B₃` permutes the six directions `±e_mu` among themselves, so
`x ↦ Ax` maps nearest-neighbour edges to nearest-neighbour edges and the support graph is
preserved as a graph; the only question is whether the sign relation
`s_j = s_i · D2[i,j] · D2[p_i,p_j]` is consistent around cycles. The runner propagates from
`s(0) = +1` along the BFS spanning tree and then verifies the FULL commutation condition on
all `N²` entries — a cycle inconsistency shows up either as a missing image edge during
propagation or as a commutation failure afterwards. Result: 48/48 liftable at every
L ∈ {4, 6, 8, 10, 12}, with 48 distinct permutation parts. Because the support graph is
connected the kernel of the permutation-part map is `{±1}`, so each of the 48 has exactly
two lifts; where the enumeration is available (L ∈ {4, 6, 8, 10}) this is confirmed
directly by counting the enumerated elements over each constructed permutation part
(48/48 with exactly two lifts each, and each constructed lift and its negative found in
the enumerated key set).

*Why T4 is size-quantified and T1–T3 are not.* T1 exhibits a closed-form sign field and
verifies the edge condition symbolically for all even `L`; T2 and T3 follow from T1 by
algebra with no size dependence. T4 has no counterpart closed form here: the
cycle-consistency question is settled by the runner at five sizes rather than by an
argument. The route to closing that is visible and is recorded in section 6 — the same
edge condition used for T1, with the translation `p_nu` replaced by `x ↦ Ax`, is a linear
system over `F₂` in the unknown sign field, and solving it in closed form for all 48 `A`
would make T4 general-`L`. Until that is done, a reader should take T4 at the five sizes
and nothing wider.

*Discrimination.* The liftability claim would be vacuous if every integral lattice
bijection lifted. The runner runs the explicit non-`B₃` rejector `[[1,1,0],[0,1,0],[0,0,1]]`
— determinant `1`, a genuine bijection of `Z_L³`, but not a signed permutation matrix — and
finds the propagation inconsistent at every `L` (a tree edge whose image is not a support
edge). So liftability is a real property of `B₃`, tested against a nontrivial competitor.

**T5 (size independence, exactly where it is exact; gates G3_ENUM_L\*, G9_COUNTS_L\*,
G9S_SUPPORT_L\*, G10_CLOSURE_L4, G10_CLOSURE_L6, XL_96N, XL_ENUM_EQ).** The construction
of T1 and T4 yields exactly `96N` distinct elements of `Comm(D2)` at every
L ∈ {4, 6, 8, 10, 12}. Both halves of the size statement, stated separately:

- **Equality where the enumeration was run.** At L ∈ {4, 6, 8, 10} the exhaustive
  enumeration gives a liftable-automorphism count `48N` and `|Comm(D2)| = 96N`, matching
  the constructed count exactly. At L ∈ {4, 6} this is sharpened to KEY-SET EQUALITY: the
  closure of `{t_x, t_y, t_z, -I}` together with the 48 constructed point-group lifts (52
  generators) has order `96N` and its key set is EQUAL, as a set of byte keys, to the
  enumerated `Comm(D2)`. At L ∈ {8, 10} the closure is NOT ATTEMPTED — the runner sets
  `L_CLOSURE = (4, 6)`, so the cache records no attempt, no failure and no memory figure
  at those sizes; this is a scoping cut taken to keep the unit inside its budget, not a
  measured infeasibility, and it should not be read as one. The comparison there is by
  count plus generator membership: each of the 51 constructed generators and its negative
  is found in the enumerated key set, with exactly two enumerated lifts per permutation
  part.
- **Lower bound where it was not.** At L = 12 no enumeration is run. The construction then
  establishes only `|Comm(D2)| ≥ 96N = 165888`. Equality there is NOT established by this
  unit: it would require knowing that the LIFTABLE support-graph automorphisms are exactly
  the `48N` affine maps `x ↦ Ax + v` at that `L`, which this unit does not prove. Note
  that this is strictly weaker than requiring the support-graph automorphism group itself
  to be the affine maps — the L = 4 row below is a lattice where that stronger statement
  is FALSE (46080 automorphisms against 3072 affine maps) and yet `|Comm(D2)| = 96N` holds
  exactly, because the non-affine automorphisms fail to lift. The same applies to every
  larger even `L`.

## 3. Evidence — measured values

| L | N | constructed `2·48·N` | enumerated `nComm` | enumerated `nLift` | support `nStab` | support `nAut` | `q = -I` set | single-site flip rejections |
|--:|--:|--:|--:|--:|--:|--:|---|---|
| 4 | 64 | 6144 | 6144 | 3072 | 720 | 46080 | empty | 192/192 (exhaustive, all `N`) |
| 6 | 216 | 20736 | 20736 | 10368 | 48 | 10368 | `{011, 101, 110, 111}` | 648/648 (exhaustive, all `N`) |
| 8 | 512 | 49152 | 49152 | 24576 | 48 | 24576 | empty | 96/96 (32-site stride `N//32`) |
| 10 | 1000 | 96000 | 96000 | 48000 | 48 | 48000 | `{011, 101, 110, 111}` | 96/96 (32-site stride `N//32`) |
| 12 | 1728 | 165888 | — (≥ 165888) | — | — | — | empty | 96/96 (32-site stride `N//32`) |

Supporting per-`L` measurements, at every L ∈ {4, 6, 8, 10, 12}: closed-form lift commutes
with `D2` 3/3; BFS propagation from `s(0) = +1` reproduces `zeta_nu` exactly 3/3 on a
connected support graph; `[t_a, t_b]` central 9/9 with the `-1`-iff-`a≠b` pattern, and the
bimultiplicative extension matching `(-1)^{(Σs)(Σt) - s·t}` on 64/64 class pairs;
`(t_nu)^k` sign field `= zeta_nu^k` on `3L`/`3L` powers with order exactly `L`; `q`
matching the formula 8/8; the 7 alternative exponent masks rejected 21/21; all 48 `B₃`
matrices liftable 48/48 with 48 distinct permutation parts; the shear rejector not
liftable. At L ∈ {4, 6} additionally: commutators of actual lift products central 64/64 and
matching 64/64; closure of the 52 constructed generators equal to the enumerated `Comm` as
a key set. At L ∈ {4, 6, 8, 10} additionally: `t_nu` and `-t_nu` both present in the
enumerated `Comm` 3/3 with exactly two enumerated lifts 3/3; each point-group lift and its
negative present 48/48 with exactly two lifts 48/48.

The constructed count is measured, not asserted: for each of the 48 lifted point-group
permutations and each of the `N` translations the composite permutation is fingerprinted by
its images of the four probe sites `0, e_0, e_1, e_2` packed into one `int64`, and the
number of DISTINCT fingerprints is counted. Distinct fingerprints certify distinct
permutations, so `48N` distinct fingerprints (3072, 10368, 24576, 48000, 82944 measured)
give `96N` distinct group elements once the two central signs are included. No injectivity
is assumed of the fingerprint map.

All 64 gates pass with zero failures; the paired runner
`scripts/kcpt_d2_commutant_closed_form_lifts_lattice_size_independence_2026_07_25.py`
prints `TOTAL: PASS=64 FAIL=0`. The runner deliberately emits no wall-clock or
resident-memory figures: those are machine- and load-dependent, and printing them would
make the cached output differ on every regeneration. Cost is instead reported here as a
bound — on the machine used for this unit the full run stayed under two minutes and under
1.5 GB resident, dominated by the L = 10 enumeration and the L = 12 support build. The
enumeration structures are freed between sizes, so peak memory tracks the largest single
`L` rather than their sum, and the L = 12 pass inherits that high-water mark rather than
adding to it. Every quantity is exact integer arithmetic; there is no floating tolerance
anywhere in this unit.

## 4. The picture: the lane is no longer enumeration-bound

Up to this unit, everything the lane knew about `Comm(D2)` came from listing its `96N`
elements — which is why the lane lived at L ∈ {4, 6}. The staggered phases are
lower-triangular in the coordinates, and that single structural fact is enough to write the
generators down. A translation by `e_nu` disturbs `eta_mu` exactly when `nu < mu`, so the
compensating sign field must flip across the `mu`-edges with `mu > nu` and no others — that
is `zeta_nu(x) = (-1)^{Σ_{mu > nu} x_mu}`, a closed form with no `L`-dependence at all
beyond the parity of `L`. The whole extension class follows from the same triangularity:
the commutator `[t_a, t_b] = (-1)^{[a>b]+[b>a]} I` is `-1` off the diagonal because exactly
one of the two orderings flips, and the 2-torsion form `q = (-1)^{(L/2)² Σ_{i<j} v_i v_j}`
is trivial or not according to the parity of `L/2` alone. The point group needs no new
idea: `B₃` permutes the six lattice directions, so its elements preserve the support graph
and the sign relation propagates consistently — 48 out of 48, at every size tested, while a
determinant-1 shear that is not a signed permutation fails immediately.

The pay-off is that `96N` becomes a construction rather than a census. At L ∈ {4, 6, 8, 10}
the exhaustive enumeration is still run and still agrees — including key-set equality at
L ∈ {4, 6}, where the closure of the 52 closed-form generators is literally the same set of
elements the enumerator produces. At L = 12 the enumeration is not affordable and the
honest statement is a lower bound: the construction exhibits `165888` elements and does not
prove there are no others. The gap between the two halves is a single missing ingredient —
that the LIFTABLE support-graph automorphisms are exactly the `48N` affine maps at general
even `L`. The L = 4 row of the table is the reason that ingredient has to be stated in that
liftability form rather than as a statement about the automorphism group: there the support
graph carries `46080` automorphisms, far more than the `3072` affine ones, and equality
still holds — because only the affine ones lift.

## 5. Dependencies

- [KCPT D2 graded signed-permutation commutant characterization (L=4 and L=6) (bounded theorem)](KCPT_D2_GRADED_SIGNED_PERMUTATION_COMMUTANT_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
- [KCPT D2 commutant double cover and bicommutant structure (L=4 and L=6) (bounded theorem)](KCPT_D2_COMMUTANT_DOUBLE_COVER_BICOMMUTANT_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-25.md)

Context (not a dependency edge): the preceding restriction-localization unit,
`KCPT_D2_COMMUTANT_EXTENSION_TRANSLATION_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-25`,
already carries both closed forms — it measured `beta` on the enumerated group at
L ∈ {4, 6} and matched it uniquely among the 512 bimultiplicative candidates, then derived
`q` from it. This unit does not consume either result; it re-derives `beta` from the
staggered phases instead of from an enumeration, and reruns the same `q` argument on that
derived input, which is what lets both run at L ∈ {8, 10, 12}.

## 6. Next paths this opens

- **Prove that the liftable support-graph automorphisms are exactly the `48N` affine maps
  at general even `L`.** That is the one missing ingredient that would upgrade T5's lower
  bound `|Comm(D2)| ≥ 96N` to equality at every even `L`, with no enumeration anywhere.
  L = 4 fixes the shape such a proof must have: the support-graph automorphism group there
  is `46080`, strictly larger than the `3072` affine maps, and equality nevertheless holds.
  So the proof must NOT go through "there are no extra automorphisms" — the extra
  automorphisms need not go anywhere, they need only fail to lift, which is what the L = 4
  row measures. A liftability obstruction, not an automorphism census, is the object to
  chase.
- **Solve the point-group edge condition in closed form and make T4 general-`L`.** The
  edge condition of T1 with the translation replaced by `x ↦ Ax` is a linear system over
  `F₂` in the unknown sign field; a closed-form solution for all 48 `A ∈ B₃`, together
  with the cycle-holonomy condition, would replace T4's five-size verification with a
  derivation and remove the last size quantifier from the construction side.
- **Odd `L`.** `zeta_nu` is not well defined on `Z_L` for odd `L`, so the closed form as
  written does not apply. What replaces the translation lift on an odd torus — and whether
  the group order law survives in any form — is untouched here.
- **Carry the closed-form generators into the bicommutant computations.** The double-cover
  and bicommutant work in this lane consumed the enumerated group. With generators in
  closed form, the extension class, the derived subgroup, the endomorphism algebra and the
  eigenspace/character block become computable at sizes the enumeration cannot reach, which
  is the natural way to test which of those structures are `L`-stable in form.

## Boundary

- The equality `|Comm(D2)| = 96N` is exhaustively established only at L ∈ {4, 6, 8, 10},
  where the enumeration was actually run. At L = 12 and at every larger even `L` the
  construction of T1 and T4 gives only the LOWER BOUND `|Comm(D2)| ≥ 96N`. Equality at
  those sizes is not claimed here; it would need the support-graph automorphism group to be
  exactly the affine maps at that `L`.
- `L` even is required throughout, because `zeta_nu(x) = (-1)^{Σ_{mu > nu} x_mu}` is well
  defined on `Z_L` only when `L` is even. Odd `L` is outside the scope of this unit.
- This unit adds no physics identification. It is a statement about the symmetry group of a
  finite staggered operator `D2` — nothing about `r`, generations, flavour, the continuum
  limit, or any physical observable is claimed, and the statement is r-neutral.
- **A planner-supplied anchor did not reproduce as literally labelled, and is recorded
  here.** The anchor table this unit was built against listed, for the exhaustive
  enumeration, `nStab = 48` and `nAut = 3072` at L = 4. The landed enumerator actually
  returns `nStab = 720` and `nAut = 46080` at L = 4, with `nLift = 3072`: the anchor's
  `nAut` column is the LIFTABLE count `nLift`, and its `nStab` column is `nLift / N`. At
  L ∈ {6, 8, 10} the two readings coincide (`nStab = 48`, `nAut = nLift = 48N`) and the
  anchor is exact as written. The substantive claims are unaffected — `nComm = 96N` and
  `nLift = 48N` hold at all four enumerated sizes, and the constructed set equals the
  enumerated `Comm(D2)` at L = 4 as a key set — but the L = 4 support-graph census is
  genuinely different from the liftable census and the runner gates the two separately
  (`G9S_SUPPORT_L*` against the support-graph values, `G9_COUNTS_L*` against the liftable
  ones) rather than conflating them.
- The `q = -I` dichotomy is verified at five sizes covering both residues mod 4
  (L = 4, 8, 12 for `L ≡ 0`; L = 6, 10 for `L ≡ 2`); it is derived from T2 and T3 for all
  even `L`, and the five sizes are confirmations of that derivation, not its basis.
- The single-site sign-flip rejector is exhaustive over all `N` sites only at L ∈ {4, 6}; at
  L ∈ {8, 10, 12} it runs on a deterministic stride-`N//32` subset of 32 sites per `nu`
  (no randomness). A sign dressing that differed from `zeta_nu` only at sites outside that
  subset would not be caught by that particular gate at those sizes — though it would be
  caught by the full `N²` commutation check of G1 and by the propagation-equality check of
  G2, both of which are exhaustive at every `L`.
- The two dependency rows are landed on main; their anchors (`D2`, the support structures,
  the commutant enumerator, the `96N` census law) are consumed here as landed module
  values.

## Honest-auditor read

- The dangerous move this unit could make is to let the closed form validate itself — to
  compute `zeta_nu` and then "check" it against `zeta_nu`. It does not. The sign field is
  obtained twice by independent routes: once from the closed formula, and once by BFS
  propagation of the edge relation `s_j = s_i · D2[i,j] · D2[p_i, p_j]` over the support
  graph starting from `s(0) = +1`, which never sees the formula. The gate compares the two
  and separately verifies the full `N²` commutation condition. Likewise the commutator
  signs come from actual signed-permutation products, and `q` comes from actually squaring
  the half-power products, not from evaluating the formula they are compared against.
- Every completeness claim is built to fail if the object were wrong, via explicit
  wrong-value rejectors rather than identities that hold by construction. Single-site sign
  flips of `zeta_nu` must break commutation, and do (192/192 and 648/648 exhaustively at
  L = 4, 6; 96/96 on the fixed 32-site subsets at L = 8, 10, 12). Each of the 7 alternative
  exponent masks must fail, and does (21/21 at every `L`), so the mask `{mu : mu > nu}` is
  discriminated among all 8 subsets. The determinant-1 shear `[[1,1,0],[0,1,0],[0,0,1]]` —
  a real lattice bijection — must NOT lift, and does not, at every `L`; without it the
  "all 48 of `B₃` lift" claim would carry no information.
- The `96N` count is measured by distinct fingerprints of the constructed permutations, not
  asserted from `2 · 48 · N`. The fingerprint packs the images of four probe sites
  (`0`, `e_0`, `e_1`, `e_2`) into one integer, so distinct fingerprints certify distinct
  permutations; no injectivity of the fingerprint map is assumed anywhere. A collision
  therefore cannot hide — it would push the distinct count BELOW the constructed `48N` and
  fail the gate — and the count comes out exactly `48N` at all five sizes, including
  82944 at L = 12 where nothing is enumerated.
- The honest asymmetry in T5 is stated rather than smoothed over. At L ∈ {4, 6} the claim
  is a set equality of byte keys; at L ∈ {8, 10} it is a count plus generator membership,
  because the runner sets `L_CLOSURE = (4, 6)` and does not attempt the closure at the two
  larger sizes — a scoping cut, not a measured infeasibility, and the cache records no
  attempt and no failure there; at L = 12 it is a lower bound and is labelled as such in
  the runner's own output line. A reader should not read the L = 12 row as an equality.
- The L = 4 anchor discrepancy is reported rather than absorbed. The planner's anchor table
  labelled the liftable count as `nAut`; the enumerator's `nAut` at L = 4 is 46080, fifteen
  times larger. Rather than re-label a gate to match, the runner gates both quantities
  separately and prints both, and the note records the mismatch. It also happens to be the
  most informative row in the table: L = 4 is precisely where the support graph has more
  automorphisms (46080) than affine maps (3072), and yet `|Comm(D2)| = 96N` holds there
  exactly. That row is what fixes the SHAPE of the missing general-`L` argument — the extra
  automorphisms need not be absent, they need only fail to lift, and at L = 4 they do fail
  to lift. The open ingredient is therefore a liftability obstruction, not an automorphism
  census.
- Residual softness a reader should weigh, in two distinct places. (i) T1–T3 are derived for
  all even `L`; T4 is not — its cycle-consistency question is settled by the runner at
  L ∈ {4, 6, 8, 10, 12} and by no argument, so the construction of `96N` elements is a
  five-size statement, not a general-`L` one. (ii) Even granting the construction at a given
  `L`, the step from "the construction gives `96N` elements" to "`Comm(D2)` has exactly `96N`
  elements" is made only where the enumerator runs (L ∈ {4, 6, 8, 10}); at L = 12 it is not
  made at all. Section 6 names a concrete route for each: an `F₂` closed form for the
  point-group edge condition for (i), and the liftability obstruction above for (ii).

This row is unaudited: its grade is set exclusively by the independent audit lane on
origin/main, not by this note or its runner.
