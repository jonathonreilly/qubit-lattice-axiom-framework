# Protocol--Admissibility 3D Realization Bridge And Word Dispersiveness

**Date:** 2026-07-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the named availability-rule model
`B`, the named `REAL3` realization predicate, the period-2 decorated-mover word
class on the one-amplitude `Z^3` carrier, and the stated finite verifications.
No inventory-completeness claim, no protocol-existence claim, and no claim that
the physical tick realizes `REAL3` are made.
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:**
[`scripts/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.py`](../scripts/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.py)
**Runner cache:**
[`logs/runner-cache/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.txt`](../logs/runner-cache/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.txt)

---

## Why This Note Exists

The protocol-selection note
`KINETIC_ISOTROPY_3D_FACTORIZED_PROTOCOL_SELECTION_ON_ANALYZED_CLASSES_BOUNDED_THEOREM_NOTE_2026-07-09`
reads its algebraic filter table as a physical filter only after two inputs are
separately supplied. That note's "Supplied Conditional Physical Reading"
section states them. The first input is that a realized sequential protocol is
supplied with the constituent-factor semantics used there, and that

> translation covariance of the fixed rule requires each constituent factor to be fully covariant modulo local `U(1)` frames and therefore to have zero site-modulus translation defect; nonvacuous variation together with proper cubic axis transitivity requires nonzero constituent-factor support on all three axes.

The second input is that the realized composite word is supplied to be

> dispersive in the characteristic-polynomial sense used by the runner.

This note derives both supplied inputs as theorems from the two Admissibility
clauses plus a named realization predicate `REAL3`, rather than leaving them as
separately supplied physical readings. It does not claim to settle the selection
question; it is the next derivation this step opens, and the residues the
selection note keeps open stay open here.

## Setting And Objects

The carrier is the `Z^3` qubit lattice with one complex amplitude per site
(one-component carrier). The period-2 cell `{0,1}^3` carries the 8-dimensional
Bloch representation. The `L=4` site ring per axis (`4^3 = 64` sites) is used
for exact site-level relation checks. The support law is measured on the `L=6`
ring (`6^3 = 216` sites), where for words through length 5 every axis
displacement satisfies `|net_i| <= 5 < 6` so no wraparound aliases a nonzero
displacement to zero. The normal form is realized as an explicit operator
product on the `L=12` ring (`12^3 = 1728` sites), large enough that a wrong
central exponent `m_i` cannot alias to the identity the way `T_cell_i^2 = I`
makes it on `L=4`. Nearest-neighbor license: every elementary factor
is a nearest-neighbor-supported unitary. A local `U(1)` frame is a
site-diagonal unitary. Whole-cell translation on axis `i` is translation by two
sites on axis `i`, written `T_cell_i`; one-site translation on axis `i` is
`T_i`.

The decorated movers come from the landed parent chain. On the cell coordinate
`p in {0,1}^3` (0-indexed), the eta pattern is

- `eta_1(p) = 1`,
- `eta_2(p) = (-1)^{p_0}`,
- `eta_3(p) = (-1)^{p_0 + p_1}`.

`S_i` is the eta-decorated one-site shift on axis `i` (Bloch form `S_axis(k, i)`;
site form `site_shift(i, +1)`), and `S_i^{-1} = S_i^dagger`.

The availability-rule model is abstract, following the one-axis bridge pattern.
A rule table `B` assigns to each nearest-neighbor condition profile
`c : N6 -> {0,1}`, where `N6` is the six offsets `{+-e_1, +-e_2, +-e_3}`, a
nonempty subset `B(c)` of `{0,1}`. The variation offset set is
`V(B) = { d in N6 : exists c, c' equal off slot d with B(c) != B(c') }`.

## The Two Admissibility Clauses

The two clause sentences, quoted verbatim from the linked axioms note, are:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.

Their formalizations on the availability-rule model are:

- **Clause 1, translation part.** The table `B` is site-independent (one fixed
  rule).
- **Clause 1, rotation part.** `B(c o R) = B(c)` for every proper cubic
  rotation `R`, where the 24-element rotation group acts on the `N6` slots.
- **Clause 2, variation part.** `V(B)` is nonempty.

## The Named 3D Realization Predicate

For a sequential protocol `P = (F_1, ..., F_m)` with composite word
`W = F_m ... F_1`, the predicate `REAL3(P; B)` bundles three conditions.

- **(R1-factor)** Each constituent factor is built from the fixed rule data by
  one site-independent assignment, modulo a local `U(1)` frame:
  `F_j = g_j F_j^{(0)} g_j^dagger` with `g_j` diagonal and `F_j^{(0)}` exactly
  translation covariant.
- **(R2-factor)** Every variation offset `d in V(B)` is carried by some
  constituent factor: some `F_j` has a nonzero matrix element at
  nearest-neighbor displacement `d`.
- **(R2-word)** For every axis `i` with `+e_i in V(B)` or `-e_i in V(B)`, the
  composite `W` has a nonzero site-level matrix element `W[x,y]` whose
  displacement `y - x` has nonzero axis-`i` component, at any displacement
  length.

R2-word is a genuine additional realization premise at the composite level. It
is not a consequence of the factor-level conditions R1-factor and R2-factor;
the `P_CANCEL` witness below satisfies both factor conditions while failing
R2-word.

## Theorem 3B1 (Factor Covariance And Zero Modulus Defect)

**Statement.** Clause 1 (translation part) together with R1-factor implies that
each constituent factor is fully covariant modulo local `U(1)` frames, meaning
`T_a F_j T_a^dagger = h F_j h^dagger` for a diagonal `h` per axis generator, and
therefore that each constituent factor has zero site-modulus translation
defect.

**Proof.** By R1-factor, `F_j = g_j F_j^{(0)} g_j^dagger` with `F_j^{(0)}`
exactly translation covariant, so translating `F_j` conjugates it by the
diagonal `h = T_a g_j T_a^dagger g_j^dagger`, which is a local frame. Frame
conjugation multiplies each matrix element by unit-modulus diagonal phases, so
it preserves entrywise moduli: `|F_j| = |F_j^{(0)}|` entrywise, and the
right-hand side is translation invariant. Hence the site-modulus translation
defect of `F_j` is zero. The runner realizes this with the bare undecorated
one-site shift as `F_j^{(0)}`, which it checks is exactly translation covariant
on all three axis generators. The decorated mover is then `g F_j^{(0)} g^dagger`
for the explicit diagonal frame `g = diag((-1)^{x_0 x_1})` built from the eta
pattern; the runner checks this reconstruction, checks that the decorated mover
itself is not translation covariant (its translation gap is 2 on axis 0, taken
as a maximum over axes so it cannot be masked by a covariant axis), and checks
zero modulus defect for the decorated factor.

**Strictness (necessary, not sufficient).** The alternating diagonal factor
`D_alt = diag((-1)^{x_1})` has zero modulus defect, and every local frame `h`
satisfies `h D_alt h^dagger = D_alt` because diagonals commute, while
`T_1 D_alt T_1^dagger = -D_alt != D_alt`. So `D_alt` is not covariant modulo
local frames although its defect is zero. Zero defect is only the derived
necessary shadow of full covariance.

**Rejector.** A site-dependent-amplitude factor built as a direct sum of
`2x2` Givens rotations on axis-1 nearest-neighbor pairs with the fixed angle
list `(0.3, 0.9)` along the ring is unitary and nearest-neighbor supported yet
has modulus defect `> 0.05`. The defect functional therefore has teeth.

The zero-defect filter of the selection note is the derived necessary shadow of
this theorem.

## Theorem 3B2 (Rotation Transport And All-Axis Factor Support)

**Statement.** The 24 proper cubic rotations act transitively on the six
nearest-neighbor offsets. Hence Clause 1 (rotation part) together with Clause 2
(some variation offset `d0`) implies that `V(B)` contains all six offsets, and,
combined with R2-factor, the constituent-factor support vector is `(1,1,1)`.

**Transport proof.** Let `(c, c')` witness variation at slot `d0`, so they agree
off slot `d0` and `B(c) != B(c')`. Fix a proper cubic rotation `R`. The rotated
profiles `c o R^{-1}` and `c' o R^{-1}` agree off slot `R d0`, and by the
rotation part `B(c o R^{-1}) = B(c) != B(c') = B(c' o R^{-1})`, so `R d0` is a
variation slot. As `R` ranges over the group, `R d0` ranges over the full orbit
of `d0`, which by transitivity is all six offsets. Thus `V(B) = N6`. R2-factor
then forces some factor to carry nearest-neighbor support on each axis, so the
support vector is `(1,1,1)`.

**Covariant witness.** The parity table `B(c) = {0,1}` if `sum(c)` is even else
`{0}` is invariant under every slot permutation, hence rotation covariant, and
varies at every slot.

**Non-covariant control.** The table `B'(c) = {0,1}` if `c(+e_1) = 1` else
`{0}` varies only at slot `+e_1` and violates the rotation-covariance identity
for some `R`. Its variation set misses axes 2 and 3, exactly the failure mode
the transport argument rules out under covariance.

The all-axis factor-support filter of the selection note is the derived
necessary shadow of this theorem.

## Theorem 3B3 (Word Reduction And The Dispersiveness Dichotomy)

Consider finite words in the six letters
`{S_1^{+1}, S_1^{-1}, S_2^{+1}, S_2^{-1}, S_3^{+1}, S_3^{-1}}`.

**Relations (recomputed exactly at site level, `L=4`).** For `i != j`,
`S_i S_j = - S_j S_i`, including with any inverse letters, because the
staggered eta pattern contributes exactly one sign flip per cross-axis
transposition. Same-axis letters commute. `S_i^2 = T_cell_i`, the whole-cell
translation, which commutes with every letter. `S_i^{-1} = S_i^dagger` and
`S_i S_i^{-1} = I` exactly.

**Exact normal form.** Every word `w` reduces to
`W = sigma * (prod_i T_cell_i^{m_i}) * S_1^{eps_1} S_2^{eps_2} S_3^{eps_3}`,
where `net_i` is the net signed exponent of axis `i` in `w`,
`eps_i = net_i mod 2 in {0,1}`, `m_i = (net_i - eps_i)/2`, and `sigma in {+1,-1}`
is the parity of cross-axis adjacent transpositions used to sort the letters by
axis. Same-axis letters commute, so they contribute no sign; the sign is the
parity of the cross-axis inversions.

**Support law.** `W` has site-level support at some displacement with nonzero
axis-`i` component if and only if `net_i != 0`.

**Dispersiveness dichotomy.** The Bloch characteristic-polynomial coefficients
of `W` are momentum-independent if and only if `net = (0,0,0)`, i.e. exactly
when `W = +-I`. If any `net_i != 0`, then either a residual mover
(`eps_i = 1`) contributes momentum-dependent bands, or a pure central part
(`eps_i = 0`, `m_i != 0`) contributes the momentum-dependent scalar phase
`exp(-i m_i k_i)` through the determinant, so the characteristic polynomial
depends on momentum.

**Proof sketch.** Sort the letters by axis using adjacent transpositions. A
cross-axis transposition flips a sign by pairwise anticommutation; a same-axis
transposition is free. After sorting, each axis run is a power of `S_i`, and
`S_i^2 = T_cell_i` splits that power into the central translation part `m_i` and
the residual mover `eps_i`. The central factors commute through, giving the
normal form. The support law reads off displacements: `S_i^{eps_i}` moves by one
site on axis `i` when `eps_i = 1`, and `T_cell_i^{m_i}` moves by `2 m_i` sites,
so axis-`i` displacement is nonzero exactly when `net_i != 0`. The dichotomy
follows because `S_i^2 = e^{-i k_i} I` on the Bloch cell, so a pure central word
is a momentum-dependent scalar and a residual mover has momentum-dependent
eigenvalues, while `net = (0,0,0)` gives `+-I`. The runner verifies the
reduction by building the normal form as an explicit operator product of central
cell-translation and residual-mover operators on the `L=12` ring and matching it
to the direct letter product, exhaustively for all words through length 5 (9330
words) and on named length-6 witnesses; a rejector confirms that a wrong central
exponent `m_i` is caught on `L=12` while it aliases to the identity on `L=4`, so
the `m_i` are load-bearing. The support law is checked on the `L=6` ring, where
words through length 5 never wrap. The induction is the prose argument above.

**Bridge conclusion.** Under Clauses 1 and 2 and `REAL3`, Theorem 3B2 gives
variation on all three axes; R2-word forces axis support on all three axes; the
support law gives `net_i != 0` for all `i`; the dichotomy gives that the
realized composite word is dispersive in the characteristic-polynomial sense.
This derives, on the analyzed word class, the condition the selection note lists
as its supplied input 2.

**Separating witness (R2-word is load-bearing).** The cancelling word
`P_CANCEL = S_1 S_1^{-1} S_2 S_2^{-1} S_3 S_3^{-1}` has zero constituent-factor
modulus defect and factor support union `(1,1,1)`, so it satisfies R1-factor and
R2-factor against the parity table, yet it composes to the identity:
`net = (0,0,0)`, no off-site composite support, flat. It violates exactly
R2-word. The unconditional claim that nonvacuous variation alone forces
composite dispersiveness is therefore false and is not made; R2-word is the
named extra realization premise.

**Non-removal witness.** The weighted word `P_WEIGHT = S_1 S_1 S_2 S_3` has
`net = (2,1,1)`, satisfies R2-word (axis-1 support at displacement 2 through
`T_cell_1`, nearest-neighbor support on axes 2 and 3), and is dispersive. The
bridge does not remove `P_WEIGHT`; the four-member candidate set of the
selection note is kept intact.

**Scope honesty.** The reduction and dichotomy are proved on words in the
decorated movers. Non-word protocols, such as commuting pairing factors and
diagonal-phase protocols, are outside 3B3's scope; in the analyzed ten-member
inventory they are removed upstream by the 3B1 defect filter or the 3B2 support
filter, not by 3B3.

## Endpoint Corollary (Consistency With The Selection Note)

Applying the three derived necessary conditions -- zero constituent-factor
modulus defect, all-axis factor support, and R2-word (which on the word class
implies composite dispersiveness) -- to the ten-member inventory of the
selection note reproduces exactly the four-member candidate set
`{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`. Nothing is consumed: the four-member
set is reproduced, not narrowed, and the octant, central-sign, and whole-cell
translation residues stay open exactly as in the selection note.

## Boundary And Honest Auditor Read

- The availability-rule model `B` and the predicate `REAL3` are named
  formalizations. The three theorems are conditional on them. Whether the
  physical tick realizes `REAL3` is not derived here.
- The 3B3 dichotomy is proved on the decorated-mover word class only, with
  exhaustive machine verification through length 5 plus named longer witnesses,
  and an algebraic induction argued in prose.
- Nothing here selects among the four surviving protocols and nothing removes
  `P_WEIGHT`.
- The two derived factor conditions are necessary consequences of the bridge,
  not equivalences. Their converses are false and are shown false by explicit
  witnesses: `D_alt` has zero modulus defect without being covariant modulo
  local frames, and a constant-rule uniform mover pattern shows that factor
  support does not certify variation. Binary all-axis factor support is much
  weaker than full protocol covariance.

## Falsifiers

- A word with `net != 0` whose Bloch characteristic polynomial is
  momentum-independent across the fixed grid.
- A frame-conjugated fixed-assignment factor with positive site-modulus
  translation defect.
- A rotation-covariant varying table whose variation set misses an axis.
- A rebuild of the ten-member filter application yielding a survivor set other
  than `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`.
- A word whose direct site-level product disagrees with its predicted normal
  form.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the two Admissibility clause sentences and the explicit boundary that
  Admissibility does not choose a transfer operator or kinetic branch.
- [KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md](KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  supplies the 3D decorated-mover constructions, the factor identities, and the
  bounded-class scope.
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)
  supplies the nearest-neighbor site-license as a finite forward-reachability
  theorem.

Context (no dependency edge):
`KINETIC_ISOTROPY_3D_FACTORIZED_PROTOCOL_SELECTION_ON_ANALYZED_CLASSES_BOUNDED_THEOREM_NOTE_2026-07-09`,
`TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09`,
`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09`,
`TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10`.

## Runner And Cache

The runner recomputes the six decorated letters on the `L=4` ring and the Bloch
cell, the cross-axis anticommutation and central-square relations, the 24 proper
cubic rotations and their transitive action on the six offsets, the modulus
defect functional with its Givens rejector and `D_alt` strictness witness, the
parity availability table with its rotation-transport and non-covariant control,
the exhaustive normal-form reduction and support law and dispersiveness
dichotomy over all 9330 words through length 5, the named length-6 witnesses,
and the ten-member endpoint reproduction. The check-group inventory is A
(surface reconstruction), B (Theorem 3B1), C (Theorem 3B2), D (Theorem 3B3), and
E (quote pins). The expected final line is `TOTAL: PASS=30 FAIL=0`. The runner
is deterministic: it uses no randomness, a fixed momentum grid, and fixed word
and phase lists, and it reads no audit metadata.

Primary runner:
[`scripts/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.py`](../scripts/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.py)

Runner cache:
[`logs/runner-cache/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.txt`](../logs/runner-cache/protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_2026_07_10.txt)

Current local runner result is recorded in the SHA-pinned cache.

## Changelog

- **2026-07-10.** Initial bounded note and deterministic runner deriving the
  two supplied inputs of the selection note as the theorems 3B1, 3B2, and 3B3
  under the named availability-rule model and the `REAL3` realization predicate.
