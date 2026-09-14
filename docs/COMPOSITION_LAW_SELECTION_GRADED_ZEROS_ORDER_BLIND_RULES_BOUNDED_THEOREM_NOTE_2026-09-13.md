---
claim_id: composition_law_selection_graded_zeros_order_blind_rules_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On the 2x3, 2x2x2 and 3x3 windows of Z^3 at coupling zero, the exact Jordan-Wigner graded nearest-neighbour hopping ground vectors of the composition discriminator have zero sets of sizes 3 (2x3, N=2), 2 (2x3, N=3), 12 (2x2x2, N=4) and 8 (3x3, N=3); covariant order-blind sequential recorded-neighbour support rules reproduce each zero set at its own fixed particle number in both Z^3-realisable exterior conventions, and no single particle-number-blind rule of either convention reproduces all four sectors; each convention already fails on a named sub-collection (the same-cluster pair for exterior-unrecorded, the three discriminator clusters for exterior-empty), while positive kernels, bond-type and star-local rules reproduce no sector and a single fixed formation order with forbidden step classes reproduces only the 2x3 N=3 zeros (20 of 180 order classes; 0 of 180 at N=2, 0 of 840 on the cube)."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - composition_discriminator_record_statistics_bounded_theorem_note_2026-09-02
  - finite_bksf_sign_and_superlattice_marker_census_bounded_theorem_note_2026-09-02
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/composition_law_selection_graded_zeros_order_blind_rules_2026_09_13.py
---

# Composition and law selection: the graded zero pattern against order-blind covariant record rules

**Date:** 2026-09-13
**Type:** bounded_theorem
**Campaign block:** composition and law selection, wave A of the TOE derivation
campaign by underdetermination witnesses (design note 2026-09-13). The block
asks which covariant rule's record statistics carry the graded zeros of the
composition discriminator, and whether the axioms as written select it.

## Result up front

The composition discriminator (2026-09-02) fixes, at coupling zero, the ground
vector of Jordan-Wigner graded nearest-neighbour hopping on three finite
clusters and reads off exact zero sets: three patterns on the `2x3` window at
two particles, twelve on the `2x2x2` cube at four, eight on the `3x3` window at
three. This note adds the `2x3` window at three particles (two zeros) and asks
a single question of every rule family the campaign has classified: can a rule
that satisfies the Admissibility sentence as written, is covariant, and never
refers to a formation order, produce exactly these zeros as the support of its
record statistics?

The answer is two-sided and both sides are exact.

1. **At any single fixed particle number, yes.** Sequential recorded-neighbour
   support rules (a formation step is forbidden or allowed by the class of the
   step, and a pattern is realisable when some formation order avoids every
   forbidden class) reproduce the graded zero set exactly on each of the four
   sectors, in both exterior conventions that a rule on `Z^3` can realise:
   476 / 201 / 8750 / 421 rules when the window exterior is unrecorded, and
   782 / 2607 / 8750 / 1116 rules when the window exterior is recorded empty.
2. **Across sectors, no.** No single particle-number-blind rule of either
   convention reproduces all four sectors (0 rules in both). The two
   conventions fail on complementary sub-collections: with the exterior
   unrecorded, the two sectors of the same `2x3` cluster already admit no
   common rule (0), while the three discriminator clusters admit 160; with the
   exterior recorded empty, the `2x3` pair admits 39 common rules while the
   three discriminator clusters admit none (0).
3. **Positive kernels reproduce no sector; static rules at most one.** The ungraded hopping
   kernel is Perron-positive on every sector (connected configuration graph,
   no zeros), so every kernel with strictly positive local factors, including
   the product and additive kernels of the readability block, has an empty zero
   set. One fixed formation order with forbidden step classes reproduces the
   zeros for 0 of 180, 20 of 180 and 0 of 840 order classes; bond-type
   forbidding rules never produce the graded set; the maximal star-local
   forbidden set is empty; the discriminator's own bond-product comparator puts
   strictly positive weight on every graded zero (minimum 1/48, 1/72, 1/2304,
   1/576).
4. **Mechanism.** The discriminator's fixed-point character argument accounts
   for all zeros at `2x3` N=2 (3 of 3) and on the cube (12 of 12) but for none
   at `2x3` N=3 (0 of 2) and for half on `3x3` N=3 (4 of 8). The N=3 zeros are
   not character zeros; they are the sector-dependent part of the pattern that
   no fixed local rule tracks.

**Witness pair (recorded, not adopted).** Model G: graded (fermionic)
composition of site possibilities on `Z^3`, whose record statistics at coupling
zero carry the zero sets above with their sector dependence. Model E: ordinary
tensor composition on `Z^3` with the superlattice encoding of the landed
finite-BKSF and role-pattern notes, whose fermionic exchange sign is carried by
a next-nearest-neighbour support rule over roles. Both satisfy every axiom
sentence and every approved primitive; they differ on whether the
sector-dependence of the zero pattern is a property of the composition law or
of an encoding layered on ordinary composition. The minimal separating clause
is a composition (grading) clause or an encoding clause; the campaign records
this as a decision point and continues.

**Decision points recorded for the owner (no gate).**

- Grading clause versus encoding clause: the axioms fix neither.
- The fixed-N zero pattern is not a fingerprint of graded composition (order-blind
  support rules reproduce it); its dependence on particle number is.
- The exterior convention of a finite-window test is load-bearing: the same
  rule family passes or fails the same sub-collection depending on whether the
  window's exterior is unrecorded or recorded empty. Finite-window statements
  about `Z^3` rules must declare the convention.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the four axioms fix no cross-site composition law (tensor or graded) and no encoding; whether the graded record statistics of the composition discriminator can be carried by a covariant order-blind nearest-neighbour record rule was open"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the sequential support-rule census to coupling g>0 and to the degenerate sectors with an exact degenerate-kernel treatment; test whether a role-carrying (superlattice) support rule reproduces the sector dependence on the same windows; feed the grading-versus-encoding decision point into the support-rule (Gauss as glued support) block"
conditional_surface_status: "if a clause fixed the composition law to be graded, the sector-dependent zero pattern would be a derived record statistic of the law; if a clause fixed an encoding over ordinary composition, the same pattern would be a property of the encoding's support rule and the block's cross-sector impossibility would bound which local rules the encoding may use"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation (rational and Q(sqrt 2) arithmetic, complete enumeration of rule families and formation orders) on declared windows, sectors and rule families; nothing is asserted about infinite Z^3, about coupling g>0, or about rule families outside the classified list"
```

## Premises and declared objects

**Axiom text used (quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` on `origin/main`).**
Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations. For each site,
the probability distribution over the possibilities is determined by, and
varies with, the nearest-neighbor conditions." Record: "When present, a record
locks exactly one admissible local possibility. A site never carries more than
one record; records are permanent. Only records are readable." The axioms name
no cross-site composition law, no Hamiltonian, no encoding and no formation
order; the block treats each of these as supplier content and tests which
supplier choices are distinguishable by record statistics.

**Clusters (finite windows of `Z^3`, bonds = unit-distance pairs).** The
`2x3` window with site index `3r+c` (row `r` in {0,1}, column `c` in {0,1,2});
the `2x2x2` cube with index `4x+2y+z`; the `3x3` window with index `3r+c`. The
six-site chain of the discriminator is omitted because its graded ground vectors
have no zeros at any particle number. Bond-preserving site permutation groups
have orders 4, 48 and 8.

**Graded hopping and the zero set.** For an `N`-subset `p` of sites (a record
pattern of `N` occupied sites) and a bond `(a,b)` with `a` in `p`, `b` not in
`p`, the graded hopping matrix carries the amplitude `-(-1)^k` from `p` to
`(p \ {a}) u {b}`, where `k` is the number of occupied sites strictly between
`a` and `b` in the site index (the Jordan-Wigner sign of the discriminator).
Sectors: `2x3` at `N=2` with ground energy `-(2+sqrt 2)`, `2x3` at `N=3` with
`-(1+2 sqrt 2)`, cube at `N=4` with `-6`, `3x3` at `N=3` with `-4 sqrt 2`. All
arithmetic is exact in `Q(sqrt 2)`. The zero set of a sector is the set of
patterns whose ground-vector amplitude is exactly zero. Sectors whose ground
space was found degenerate in preparatory computation (cube at `N` in
{2,3,5,6}; `3x3` at `N` in {2,4,5,7}; not certified by the runner) are
excluded; the four sectors above have one-dimensional kernels of `H-E` and
spectral gap at least `1/4` (negative inertia of `H-(E+1/4)` equals one).

**Formation steps and step classes.** A formation order is a permutation of
the window's sites. At the step that forms site `i` against the set of already
formed sites, the recorded neighbours of `i` are its bonded neighbours already
formed; the step's class is a covariant summary of `(v, recorded neighbourhood)`
with `v` the own value of `i` in the pattern. Three summaries are used, and
they differ only in how the window's exterior is treated:

- **exterior-unrecorded** class `(v, k, m)`: `k` recorded neighbours within the
  window, `m` of them occupied. Neighbours outside the window are invisible,
  exactly as an unrecorded neighbour is invisible; this is the class a rule on
  `Z^3` sees when the window is formed inside an unrecorded exterior.
- **exterior-empty** class `(v, u, m)`: `u` unrecorded neighbours within the
  window, `m` occupied recorded neighbours. Exterior neighbours count neither as
  unrecorded nor as occupied; this is the class a rule on `Z^3` sees when the
  window is formed inside a recorded-empty exterior.
- **boundary-state** class `(v, u, e, m)`: unrecorded, recorded-empty and
  recorded-occupied counts within the window. Its total `u+e+m` reveals the
  window degree, so a rule of this class can see the window wall; it is not a
  rule on `Z^3` without an extra datum for the exterior state, and it is used
  only for an existence remark.

**Rule families tested.**

- **Sequential support rules (exists-order semantics).** A rule is a set `F` of
  forbidden step classes; a pattern is realisable when at least one formation
  order avoids `F` at every step. Order-blind: `F` never refers to an order.
  The runner enumerates all subsets of the classes actually used by the
  sector(s) and counts those whose realisable set is exactly the complement of
  the zero set; every count reported was completed below the enumeration cap,
  so counts are exact. "Forced" classes are forbidden in every such rule,
  "never" classes are allowed in every such rule.
- **Single fixed order with forbidden classes**: the same, but with one fixed
  order (counted up to the bond-preserving permutation group: 180 order classes
  on `2x3`, 840 on the cube).
- **Bond-type forbidding rules**: a pattern is a zero when it contains a bond of
  a declared covariant type (occupied-occupied, occupied-empty, or empty-empty
  along a declared axis).
- **Star-local rules**: a pattern is a zero when some site's closed
  neighbourhood class lies in a forbidden set; the maximal set consistent with
  every nonzero pattern is computed and applied.
- **Bond-product comparator**: the discriminator's own comparator, a product of
  three homogeneous bond weights; support only.
- **Positive kernels**: the ungraded hopping kernel, and by the same argument
  every kernel whose local factors are strictly positive.

**Exactness budget.** Rational and `Q(sqrt 2)` arithmetic throughout; windows
of at most nine sites; no dense space above dimension 84; runner about 80 s,
stdout 5889 characters.

## Prior art and what is new

The composition discriminator (2026-09-02) established the graded zero sets on
the three clusters, proved the character prediction for `2x3` N=2, the cube and
the four centre-crossing lines of `3x3`, and showed that a homogeneous
bond-product comparator has full support. The finite-BKSF note and the
role-pattern note (2026-09-02, 2026-09-04) established that ordinary tensor
composition on `Z^3` with a period-`(4,2,2)` superlattice role pattern carries a
fermionic exchange sign, and that the role pattern is a next-nearest-neighbour
support rule over roles that are not record values. The readability block of
this campaign (2026-09-13) classified the covariant order-blind product and
additive kernels of a formation step.

New here: (i) the `2x3` N=3 sector and the proof that its zeros, and half of
the `3x3` zeros, are not fixed-point character zeros; (ii) the Perron
positivity argument that removes every positive kernel from the candidate list
in one stroke; (iii) the complete census of static, bond-type and star-local
rules; (iv) the sequential support-rule family, its fixed-`N` existence in both
`Z^3`-realisable exterior conventions with exact counts and forced/never
classes, and its cross-sector impossibility with the complementary failure
pattern; (v) the boundary-state existence remark; (vi) the witness pair and the
three recorded decision points.

## Exact target and obligation graph

Target of the block (design note, composition and law selection): decide
whether the graded zeros of the discriminator are the record statistics of some
covariant order-blind nearest-neighbour rule, and if not, name the minimal
separating clause. Obligations discharged by the theorems below:

1. Reproduce the discriminator's zero sets and gaps exactly (Theorem 1).
2. Locate the mechanism of the zeros and its limit (Theorem 2).
3. Exclude positive kernels, including the readability block's (Theorem 3).
4. Census the static families (Theorem 4).
5. Census the sequential support rules at fixed `N` (Theorem 5) and across
   sectors (Theorem 6), in every exterior convention a `Z^3` rule can realise.
6. Exhibit the witness pair and record the separating clause (Theorem 7).

## Theorems

**Theorem 1 (exact sectors, gaps and zero sets).** In each of the four sectors
the kernel of `H-E` at the stated energy is one-dimensional and the negative
inertia of `H-(E+1/4)` is one, so `E` is the simple lowest eigenvalue with
spectral gap at least `1/4`. The zero sets of the ground vectors are:

| sector | energy | zeros | zero patterns (occupied sites) |
|---|---|---|---|
| `2x3`, N=2 | `-(2+sqrt 2)` | 3 | `{0,3} {1,4} {2,5}` (the three vertical pairs) |
| `2x3`, N=3 | `-(1+2 sqrt 2)` | 2 | `{0,1,2} {3,4,5}` (the two rows) |
| cube, N=4 | `-6` | 12 | the six faces and the six diagonal planes: `{0,1,2,3} {4,5,6,7} {0,1,4,5} {2,3,6,7} {0,2,4,6} {1,3,5,7} {0,1,6,7} {2,3,4,5} {0,2,5,7} {1,3,4,6} {0,3,4,7} {1,2,5,6}` |
| `3x3`, N=3 | `-4 sqrt 2` | 8 | three rows, three columns, two diagonals |

The signed component counts `(+,-,0)` are `(9,3,3)` at `2x3` N=2 and
`(29,29,12)` on the cube. The three discriminator sectors agree with the
discriminator note; the `2x3` N=3 sector is new.

**Theorem 2 (the character mechanism and its limit).** In every sector the
ground vector is an eigenvector of every bond-preserving site permutation,
acting with the Jordan-Wigner sign, with character `+1` or `-1`. A pattern that
is fixed by a permutation `sigma` with `chi(sigma) sgn_S(sigma) = -1` has zero
amplitude. This predicts 3 of 3 zeros at `2x3` N=2, 12 of 12 on the cube, and
exactly the four centre-crossing lines (middle row, middle column, two
diagonals) of the eight `3x3` zeros. It predicts 0 of the 2 zeros at `2x3` N=3
and none of the four non-centre rows and columns of `3x3`. Those six zeros are
genuine zeros of the exact ground vector that are not fixed-point character
zeros; the character mechanism is therefore sufficient but not necessary for
the zero pattern, and any rule that reproduces the graded zeros must reproduce
these six by another route.

**Theorem 3 (positive kernels have no zeros).** In every sector the ungraded
hopping matrix has non-positive off-diagonal entries and a connected
configuration graph. By Perron-Frobenius the ground vector is strictly
positive, so its zero set is empty. The same argument applies verbatim to any
composition kernel whose one-step factors are strictly positive, including the
covariant product and additive kernels classified by the readability block:
no such kernel carries the graded zero pattern in any sector. Grading is not a
refinement of a positive kernel's statistics; it changes the support.

**Theorem 4 (static families).** (a) One fixed formation order with a forbidden
set of step classes reproduces the graded zeros for 0 of 180 order classes at
`2x3` N=2, 20 of 180 at `2x3` N=3, and 0 of 840 on the cube. (b) Bond-type
forbidding rules give zero sets of sizes `15,15,7,15,15,15,15` (`2x3` N=2),
`18,20,18,20,18,20,20` (`2x3` N=3), `68,70,68,70,68,70,70` (cube) and
`84,84,62,84,84,84,84` (`3x3`), never the graded set. (c) The maximal star-local
forbidden class set consistent with the nonzero patterns is empty in all four
sectors and kills no zero. (d) The bond-product comparator puts strictly
positive weight on every graded zero, with minima `1/48`, `1/72`, `1/2304`
and `1/576`. Static and one-shot local rules therefore do not carry the pattern
beyond a single sector.

**Theorem 5 (fixed-N existence of sequential support rules).** In the
exterior-unrecorded convention the number of order-blind sequential support
rules whose realisable set is exactly the complement of the zero set is 476
(16 used classes; no forced class; class `000` never forbidden) at `2x3` N=2,
201 (18 classes; forced `031 132`; never `032 131`) at `2x3` N=3, 8750 (20
classes) on the cube, and 421 (26 classes; forced `020 021 131 140 142`; never
`000 010 022 120 121`) at `3x3` N=3. In the exterior-empty convention the
counts are 782 (16 classes), 2607 (19), 8750 (20; equal to the
exterior-unrecorded count because the cube is degree-regular) and 1116 (26;
forced `020 021 101 102`; never `011 130`). Every count is exact (the
enumeration finished below the cap). At any single fixed particle number the
graded zero pattern is therefore the record statistic of a covariant
order-blind nearest-neighbour rule in either `Z^3`-realisable exterior
convention. The forced classes are read as `(v, k, m)` or `(v, u, m)` digits.

**Theorem 6 (cross-sector impossibility, with complementary structure).**
Exterior-unrecorded: a single particle-number-blind rule reproduces the three
discriminator sectors jointly in 160 ways (forced `020 021 031 032 100 110 131
140 142`; never `000 010 011 022 030 120 121 130 132 141`; example
`F = {020 021 031 032 033 040 041 042 043 100 110 111 131 140 142}`), and the
pairs in 1021 (`2x3` N=2 with cube), 384 (`2x3` N=2 with `3x3`) and 189 (cube
with `3x3`) ways; but the same-cluster pair `2x3` N=2 with `2x3` N=3 admits
0 rules, and all four sectors jointly admit 0. Exterior-empty: the same-cluster
pair admits 39 particle-number-blind rules (forced `010 020 111 112 130`; never
`000 001 002 011 021 101 120 121`; example
`F = {003 010 020 030 100 102 110 111 112 130}`), but the discriminator triple
admits 0 and all four jointly admit 0. The two `Z^3`-realisable conventions fail
on complementary sub-collections: what one convention can do (three clusters at
their own particle numbers) the other cannot, and what the other can do (one
cluster at two particle numbers) the first cannot. Boundary remark: a rule of
the boundary-state class, which can see the window wall through the total
`u+e+m`, does reproduce the same-cluster pair (one rule found at cap one); this
class is not a rule on `Z^3` without an exterior datum and is recorded as an
existence fact only.

**Theorem 7 (witness pair and separating clause).** Model G: graded
(Jordan-Wigner) composition of the site algebras on `Z^3` with the axioms'
nearest-neighbour hopping kernel; its record statistics carry the four zero
sets above. Model E: ordinary tensor composition on `Z^3` with the landed
superlattice role pattern (finite BKSF relations, period-`(4,2,2)` marker
template, roles as next-nearest-neighbour support data that are not record
values). Both models satisfy every sentence of the four axioms and the three
primitives; they differ on which finite-window record statistics are
realisable, and by Theorems 3 to 6 no covariant order-blind nearest-neighbour
record rule on `Z^3` reproduces Model G's statistics across sectors without
additional data (particle number or an exterior datum), while Model E supplies
that data through roles. The minimal separating clause is one of: a
composition clause (the cross-site product is graded) or an encoding clause
(roles are admissible support data carried outside the record). Neither is
adopted here. Decision points recorded for the owner: (i) grading clause versus
encoding clause; (ii) the fixed-`N` zero pattern is not a fingerprint of
grading, its sector dependence is; (iii) the exterior convention of every
finite-window test of a record rule is load-bearing and must be declared.

## No-Go Discipline Gate

The negative content of this note is Theorem 6 (no particle-number-blind
sequential support rule in either `Z^3`-realisable exterior convention
reproduces all four sectors) and Theorems 3 and 4 (positive kernels and static
families). The gate is applied to that content only.

- **N1 alternative routes.** Enumerated and tested: positive kernels (Theorem
  3), single fixed order (4a), bond-type (4b), star-local (4c), comparator (4d),
  sequential rules in three exterior conventions (5, 6). Not tested and left
  open: rules that read particle number, rules with a declared exterior datum
  (the boundary-state class succeeds on the same-cluster pair), rules over
  role-carrying support data (Model E), rules at coupling `g > 0`, and
  degenerate sectors.
- **N2 wall independence.** The impossibility is an complete finite count over
  all subsets of the used classes; it does not depend on any retained or
  bounded claim, only on the exact ground vectors of Theorem 1.
- **N3 hidden walls.** The exists-order semantics is the most permissive
  order-blind reading; a for-all-order reading is strictly weaker and cannot
  rescue the count. The window size is a wall: larger windows enlarge the class
  set and are not covered.
- **N4 residual matching.** The positive-count results (Theorem 5, the joint
  triple, the exterior-empty pair) match the impossibility exactly: each
  convention fails on the sub-collection the other passes, so no residual is
  unexplained.
- **N5 rhetoric.** The note claims impossibility only for the named families on
  the named windows at coupling zero, and uses no finite-enumeration or
  closing language about the search for a composition law.
- **N6 partial closure.** Fixed-`N` rules exist (Theorem 5); a boundary-state
  rule exists for the same-cluster pair. Both are recorded as openings.
- **N7 steelman.** The strongest case for an order-blind rule is the 160-rule
  joint triple; it is stated with its forced and never classes so that its
  failure on the same-cluster pair is checkable.
- **N8 cross-cycle echo.** Consistent with the discriminator note (mechanism
  and comparator), the readability block (positive kernels have full support at
  second order), and the formation-order block (order is unreadable at first
  order): none of those results predicted the sector dependence found here.

## Falsifiers

1. A particle-number-blind sequential support rule in the exterior-unrecorded
   convention whose realisable set is the complement of both `2x3` zero sets.
   The runner's complete count is 0; one such rule falsifies Theorem 6.
2. A particle-number-blind rule in the exterior-empty convention reproducing
   the three discriminator sectors jointly. Count 0; one rule falsifies.
3. A positive-kernel ground vector with a zero in any of the four sectors.
   Excluded by connectivity plus Perron-Frobenius; a disconnected configuration
   graph would falsify Theorem 3.
4. A fixed-point character zero at `2x3` N=3 or on a non-centre line of `3x3`.
   The runner computes the fixed-point prediction exactly (0 of 2, 4 of 8).
5. A sector energy, gap or zero set differing from Theorem 1; the independent
   floating-point recomputation matched every value.

## Boundaries and non-claims

- Finite windows only (`2x3`, `2x2x2`, `3x3`); no infinite-lattice statement.
- Coupling zero only; the discriminator's `g > 0` sectors are not treated.
- Non-degenerate sectors only. Cube N in {2,3,5,6} and `3x3` N in {2,4,5,7}
  were found degenerate in preparatory computation, are not certified by the
  runner, and are excluded; the six-site chain has no
  zeros.
- Exists-order semantics for sequential rules; the counts are over subsets of
  the classes actually used by the sector(s), which is the full family for the
  exact-complement question.
- No clause is adopted. The witness pair is recorded; the encoding model is
  cited from the landed superlattice notes and not re-derived here.
- The boundary-state result is an existence statement (cap one), not a count.
- No statement about which composition law the axioms select; the note shows
  that the fixed-`N` zero pattern does not select it and that its sector
  dependence does, within the tested families.

## Imports

None. All objects are finite exact computations from the declared clusters,
the Jordan-Wigner hopping kernel of the discriminator note, and the axiom text
quoted above.

## Review record

- **Seat:** one Fable 5.1 seat; no subagents; runner and note by the same seat.
- **Independence sources:** (i) a floating-point recomputation (numpy `eigh`)
  of every sector energy, gap and zero set, agreeing to `1e-14`; (ii) an
  explicit enumeration over all site orders (not class masks) of the support
  rule counts 476 (exterior-unrecorded, `2x3` N=2), 782 (exterior-empty, `2x3`
  N=2), 0 (exterior-unrecorded pair) and 39 (exterior-empty pair), all equal to
  the runner's; (iii) the discriminator note's independently stated zero sets
  and character predictions for its three sectors.
- **Mutation census** (each mutant run to its first failing check):

| mutation | substitution | result |
|---|---|---|
| drop the Jordan-Wigner sign | `s = jw_sign(p, a, b) if graded else 1` to `s = 1` | FAIL `2x3` N=2 kernel dimension 0 |
| flip the character sign | `== QS2(-1)` to `== QS2(1)` | FAIL character predicts 15 of 3 zeros |
| wrong `2x3` N=2 energy | `QS2(-2, -1)` to `QS2(-1, -2)` | FAIL kernel dimension 0 |
| cube bond criterion | `d == 1` to `d == 2` | FAIL cube N=4 kernel dimension 0 |
| ungraded ground vector | `graded=True` to `graded=False` | FAIL kernel dimension 0 |
| exterior-empty class made equal to exterior-unrecorded | `(v, nu, n1)` to `(v, n0 + n1, n1)` | FAIL `2x3` N=2 exterior-empty gives 476 rules |
| joint triple expectation | `160` to `161` | FAIL 160 rules |
| exterior-empty pair expectation | `39` to `0` | FAIL 39 rules |

- **Vacuity guard:** every existence count is positive where claimed and every
  impossibility count is exactly 0; the runner fails if any expected count is
  off by one (two such mutants above).
- **Budget:** about 80 s, 63 checks, stdout 5889 characters, largest dense
  space 84-dimensional (the three-site patterns of `3x3`).

## Verification

```bash
python3 scripts/composition_law_selection_graded_zeros_order_blind_rules_2026_09_13.py
```

Expected final line: `TOTAL: PASS=63 FAIL=0`. Cached output:
`logs/runner-cache/composition_law_selection_graded_zeros_order_blind_rules_2026_09_13.txt`.
