---
claim_id: emergent_3d_fermion_one_qubit_superlattice_existence
claim_type: bounded_theorem
claim_scope: "On the cubic lattice Z^3 with one qubit per site and one translation- and rotation-covariant law, ordinary (commuting) composition of the sites throughout, a designed diagonal marker rule on a 5x5x5 window together with the Bravyi-Kitaev superfast encoding written on the coarse sublattice 2Z^3 gives, exactly and with no floating point anywhere: (T1) an encoding satisfying relations R0-R4 and prod_i B_i = +I on the open and periodic 3x3x3 coarse blocks, code dimension k = V - 1 on the open 3x3x3 (27/54/26) and 4x4x4 (64/144/63) blocks, k = V - 1 + 3 for faces only and k = V - 1 after adjoining three non-contractible Wilson loops on the tori 3^3, 4^3 and 3x3x4 (29/26, 66/63, 38/35), and k = 3 for the full vacuum stabilizer set on every one of those tori, independent of L; a hop T_ij = (i/2) A_ij (B_i - B_j) supported on exactly 11 fine sites, every one a coarse edge site, of L-infinity radius 2, identical along the three axes, commuting with all 240 face stabilizers of the open 5x5x5 block over all 144000 pairs and flipping exactly B_i and B_j with 0 wrong syndromes; three closed three-dimensional circuits of hops lying in the face-stabilizer group with phase +1; a Levin-Wen T-junction sign of -1 over 10 leg geometries on the open 7x7x7 block, including two non-coplanar triples and one rerouted triple, and a direct exchange sign of -1 over 4 triangle geometries including one with all legs detoured out of the plane, against controls in the same toolkit giving +1 for a bound pair of two such excitations, +1 for the ordinary 3D toric code point charge, and -1 for the 2D toric code epsilon = e x m. (T2) The rotation-symmetrised marker rule, 48 templates being 16 translates times 3 axis orientations of the period-(4,2,2) role pattern (corner (s[ax]/2) mod 2, face 0, cube centre 1, coarse edge free), has on the 4x4x4 torus exactly 48 zero-penalty cylinders, each of penalty 0 for all 2^24 free-bit fillings, pairwise inconsistent, zero set 48 x 2^24 with no junk, established by exhaustive branch-on-role constraint propagation in 48 search nodes with no SAT solver; the same complete search on the commensurate 8x4x4 torus returns exactly the 48 sectors, zero set 48 x 2^48, and on the incommensurate tori 5x4x4, 4x5x4 and 7x4x4 it closes every branch, 0 zero-penalty configurations. The 5x5x5 window is minimal: 3x3x3 leaves 2 unseparated pin-pairs, the 7-site star leaves 29, every period-2 role assignment fails at every window size 3 to 9, and 5x5x5 leaves 0 across all 48 templates. (T3) The locality census of the assembled law on the fine lattice classifies 16 quantum and 49 marker term types as 4 star-local (A_x, the A B_i component along x and along z, and B_i), 61 through with an explicit 6-connected hub chain, and 0 across; and over the 48 sectors the corner-centred 7-site star realises all 128 value patterns and adjacent pairs all 4 value pairs, so no rule reading only star values pins any role. (T4) The connected one-qubit-per-site rule IXZZXIIII on Z^2, support {(-1,0), (-1,1), (0,-1), (0,0)}, has all translates commuting, k(6) = k(8) = 2, three nontrivial charge classes whose T-junction signs are +1, +1 and -1 over 12, 12 and 18 geometries, and a mutual braid table equal to the toric-code S-matrix. (T5) Among fully translation-invariant Pauli stabilizer rules with one qubit per site on Z^3 whose generator support is the unit cube, 1011 of the 4^8 patterns commute with all their translates, 735 with support at least 4, giving 21 inequivalent one-pattern rules of support at least 4 (28 at support at least 1) and 423 two-pattern rules; for each of the 21 the ideal (f_X, f_Z) of the Laurent ring F2[x,y,z] is proper, a common unit-coordinate zero being exhibited over GF(2), so the charge module is nonzero, while Krull's height theorem bounds its height by 2 < 3 so the module is never zero-dimensional; and the independent exact finite-window mobile-cluster test, solving for the cluster shape together with the moving operator on a 2x2x2 cell block with margin 3, finds 0 of the 21 and 0 of the 423 rules with one nontrivial cluster mobile along all three axes, the 21 distributing 10, 5, 2, 4 over the number of axes carrying some mobile cluster. The law of T1-T3 is declared by this note as a supplier model, not derived from any axiom; no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py
---

# A three-dimensional fermion from one qubit per site: a superlattice role pattern the law forms by itself, and what one site per repeating unit allows

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py`](../scripts/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.txt`](../logs/runner-cache/emergent_3d_fermion_one_qubit_per_site_superlattice_role_pattern_existence_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

The question this note answers is whether the four framework axioms, taken with ordinary composition of the physical sites, already admit a fermion in three
dimensions. They do, and the construction is exhibited: one qubit on every site of `Z^3`, one law identical at every site and covariant under the proper cubic
rotations, and a point excitation mobile along all three axes that exchanges with a sign. The price is that the state the law forms does not treat every site
alike -- it is a repeating arrangement of pinned values with a period larger than the lattice, and the fermion is a shape inside that arrangement -- and a
separate exact theorem says that price is not optional inside the Pauli stabilizer class.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster existence theorem for a three-dimensional emergent fermion at one qubit per site, together with the exact selection theorem for the superlattice role pattern it lives on, an exact locality census, an exact two-dimensional positive rule, and an exact scope theorem for the fully homogeneous one-qubit stabilizer class. No floating point enters any statement."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: whether the framework's law is the one exhibited here."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`F`. Every one is exact -- integer and `F2`/`Z4` bit
arithmetic, exhaustive enumeration, exhaustive constraint propagation -- so no floating-point value and no external solver enters any claim.

1. `T1` (`A`, `B`, `C`). Existence: with one qubit per site of `Z^3` and one covariant law there is a point excitation that is mobile along all three axes,
   carries deformable strings, exchanges with sign `-1`, and sits in an `L`-independent `k = 3` gauge structure; three controls in the same toolkit return
   the known answers.
2. `T2` (`D1`-`D5`). Selection: the marker rule's zero set is exactly the 48 superlattice role-pattern sectors with the coarse-edge bits free, incommensurate
   boxes carry no zero-penalty configuration at all, and the `5x5x5` window is the minimal cubic window that separates the roles.
3. `T3` (`D6`, `D7`). Locality census: every term of the assembled law is star-local or an explicit product of star-local factors on a connected hub chain, and
   none is across; while the marker *rule*, read as a constraint on values, is across for value-reading rules.
4. `T4` (`E`). Two dimensions, homogeneous: the connected rule `IXZZXIIII` on `Z^2` carries a genuine point fermion with the toric-code braid table.
5. `T5` (`F`). Three dimensions, homogeneous: for fully translation-invariant Pauli stabilizer rules with one qubit per site on `Z^3` the charge module is
   never zero-dimensional, and the exact finite-window test finds no rule with a charge mobile along all three axes.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Levin-Wen T-junction statistic, Krull's height theorem and the
depth lemma are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's defining relations included.
No observational value, no fitted number, and no framework premise enters any proof. Non-load-bearing context pointers, plain file names with no grade and no
dependency weight:

- `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (the readable shadow of a cross-site sign in record statistics, and the
  finite test that separates the two compositions in two and three dimensions).
- `RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md` and
  `ENDPOINT_LOCALIZATION_THREE_ROUTE_DISCRIMINATOR_CYCLE705_NOTE_2026-07-26.md` (earlier superfast and bosonization compiler surveys on this lattice).
- `FINITE_FLAT_LINK_EVEN_CAR_SUPPORT_CENSUS_BOUNDED_THEOREM_NOTE_2026-07-23.md` (the finite flat-link even-CAR support census).
- `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md` (the earlier ring and chain probes).
- `MINIMAL_AXIOMS_2026-06-29.md` (the four framework axioms quoted in "Setting").

This note cites none of their grades, consumes no row, and adopts no hypothesis: it declares one law and computes with it.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." **Qubit**: each site has a domain of local possibilities with algebraic presentation
`M_2(C)` -- one qubit per site, and no more. **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." **Record**: records form, lock exactly one admissible local possibility, are permanent, and are the only readable thing.

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded or
signed composition clause is used anywhere. That is the setting of everything below.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P6`.

1. `P0` (declared here): the fine lattice and its four coordinate-parity roles, the coarse sublattice `2Z^3`, the encoding, the hop, the marker rule, and the
   homogeneous rule classes.
2. `P1` (`A`): the encoding's relations, and the code dimensions on open blocks and tori.
3. `P2` (`B`): the hop's support, its commutation with every face stabilizer, its syndrome, and closed three-dimensional circuits.
4. `P3` (`C`): the exchange sign, by two independent methods, with three controls.
5. `P4` (`D`): the zero set of the marker rule, the frustration of incommensurate boxes, window minimality, the locality census, and the star proposition.
6. `P5` (`E`): the two-dimensional homogeneous fermion and its braid table.
7. `P6` (`F`): the census of homogeneous one-qubit cube rules, the charge-module statement, and the finite-window mobility test.

## Definitions

Every site of `Z^3` carries one qubit. A site's **role** is its coordinate parity: all coordinates even is a **corner**, exactly one odd an **edge**, two odd a
**face**, three odd a **cube centre**. The **coarse sublattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` in
direction `e_ax` sits at the fine site `2v + e_ax`, an edge site. So each coarse cell holds eight fine sites: one corner, three edges, three faces, one cube
centre.

The **superlattice role pattern** is a repeating arrangement of pinned site values with period `(4, 2, 2)` along a chosen axis `ax`: a corner is pinned to
`(s[ax] / 2) mod 2`, a face to `0`, a cube centre to `1`, and an edge site is **free** -- it is a live qubit. The lattice itself is unchanged and remains the
plain cubic lattice; what has a larger period is the arrangement of pinned values on it. There are `16` translates of the pattern for each of the three axis
orientations, `48` **sectors** in all.

The **encoding** is the Bravyi-Kitaev superfast encoding written on the coarse sublattice, with the code qubits exactly the coarse edge sites. The direction
order at every coarse vertex is `-x < -y < -z < +x < +y < +z`. For an ordered coarse edge `(i, j)`,

```text
A_ij = X(edge site of (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),   A_ji = -A_ij,
B_i  = prod of the six Z's on the edges incident to i,
S_f  = the ordered product of the four A's around a coarse plaquette f.
```

`B_i = -1` marks the excitation; the **hop** across the coarse edge `(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`.

The **marker rule** is diagonal in the site basis and identical at every site. For each of the `48` templates it carries the projector onto that template's
pinned offsets in the `5x5x5` window and, when the template pins its own centre, a penalty for the centre disagreeing; it also carries a penalty for no
template matching. Its **penalty** on a configuration is the number of terms that fire.

A term is **star-local** when its support fits inside one site's seven-site six-neighbour star, **through** when it is an explicit product of star-local
factors whose hub sites form a `6`-connected chain, and **across** otherwise.

A **homogeneous rule** on `Z^d` is one qubit per site with `t` Pauli generator patterns per cell, the same at every cell, all translates commuting. Its
**charge module** is `M = R^t / im(eps)` with `R` the Laurent ring `F2[x^{+-1}, ..., ]`; for `t = 1` it is `R/(f_X, f_Z)`.

## Theorem 1 -- a fermion in three dimensions at one qubit per site

**Conclusion.** With one qubit on every site of `Z^3` and the law declared above:

1. The encoding satisfies `R0`-`R4` and `prod_i B_i = +I` on the open and periodic `3x3x3` coarse blocks. On open blocks the face stabilizers alone leave
   `k = V - 1`, at `3x3x3` (`V/n/k = 27/54/26`) and `4x4x4` (`64/144/63`): one fermionic mode per coarse vertex less the global parity.
2. On the coarse tori `3^3`, `4^3` and the anisotropic `3x3x4`, face stabilizers alone leave `k = V - 1 + 3` (`29`, `66`, `38`), and adjoining the three
   non-contractible Wilson loops leaves exactly `k = V - 1` (`26`, `63`, `35`). The full vacuum stabilizer set leaves `k = 3` on all three, independent of `L`
   -- the signature of a genuine three-dimensional `Z2` gauge structure rather than a foliated one, whose `k` grows with `L`.
3. The hop `T_ij` is supported on exactly `11` fine sites, every one a coarse edge site, of `L`-infinity radius `2` about the edge midpoint, identically along
   `x`, `y` and `z`. On the open `5x5x5` coarse block all `144000` pairs of a hop component with a face stabilizer commute, and every `A_ij` flips exactly
   `B_i` and `B_j`. Three closed three-dimensional circuits -- `x,y,z,-x,-y,-z`, a box circuit, a non-planar hexagon -- return to the code as face-stabilizer
   products with phase `+1`.
4. On the open `7x7x7` coarse block the Levin-Wen T-junction sign is `-1` over `10` leg geometries, two non-coplanar triples and one rerouted triple among
   them, every leg keeping endpoint-only syndromes and commuting with every face stabilizer; and the direct two-particle exchange, `E = t13 t21 t32` against
   the reference `S = t13 t32 t21`, is `-1` over `4` triangle geometries including one with all three legs detoured out of the plane.
5. The same code path returns `+1` for a bound pair of two of these excitations, `+1` for the ordinary three-dimensional toric code point charge, and `-1` for
   the two-dimensional toric code `epsilon = e x m`; and a bare `X` string anticommutes with `18` of the encoding's face stabilizers, so it is not a string of
   this code.

**Proof.** Items 1 to 3 are exhaustive symplectic computations with `Z4` phases on the named finite blocks, every relation checked pair by pair rather than
assumed, and the circuit membership established by explicit `F2` expression of the loop operator in the face-stabilizer generators together with its residual
phase. Item 4 uses the three-term T-junction sign, which is manifestly independent of every phase convention for the legs and invariant under deforming a leg
by a stabilizer, and separately the two-particle exchange, whose two words use the same three operators in different orders so every hop phase cancels. Item 5
runs the identical code path on three systems whose answers are fixed in advance. All exact.

**Reading, not theorem.** A fermion here is not a site. It is a pattern: one marked site whose six neighbours together carry an odd count, sitting in a
repeating arrangement of pinned values on the lattice that the law itself picks out.

## Theorem 2 -- the role pattern is what the law selects, and it is selected exactly

**Conclusion.** For the rotation-symmetrised marker rule, `48` templates being `16` translates times `3` axis orientations of the period-`(4,2,2)` pattern,
read on a `5x5x5` window:

1. Each of the `48` sectors has penalty exactly `0` for every one of the `2^24` fillings of its free edge bits on the `4x4x4` torus -- a property of the whole
   cylinder, not a sample, so adversarial fillings are included.
2. Exhaustive branch-on-role constraint propagation on that torus -- branch on which template matches at site `0`, propagate, branch on an undetermined bit
   when propagation stalls, `48` search nodes, no SAT solver -- returns exactly `48` zero-penalty cylinders, exactly those sectors, pairwise inconsistent. The
   zero set is `48 x 2^24` configurations and contains nothing else.
3. The same complete search on the commensurate `8x4x4` torus returns exactly the `48` sectors again, zero set `48 x 2^48`.
4. On the incommensurate tori `5x4x4`, `4x5x4` and `7x4x4`, whose side lengths hold the period `(4,2,2)` in no orientation, every branch closes: there is no
   zero-penalty configuration at all.
5. The `5x5x5` window is minimal. The `3x3x3` window leaves `2` unseparated pin-pairs and the seven-site star leaves `29`; every period-`2` role assignment
   fails at every window size from `3` to `9`; the `5x5x5` window leaves `0` unseparated pin-pairs across the full `48`-template set.

**Proof.** The rule is compiled to per-site match masks over the torus, the window's wrap onto itself checked for consistency and never onto its own centre.
Item 1 is the propagation predicate "penalty `0` for every assignment of the still-undetermined bits", evaluated on each sector's partial assignment. Item 2 is
a complete enumeration: a zero-penalty configuration must have some template matching at site `0`, so branching there is exhaustive, and each branch is either
closed by propagation or completed to a cylinder; the cylinders are compared with the sectors and checked pairwise inconsistent, which turns the count into a
cardinality without inclusion-exclusion. Items 3 and 4 rerun that search. Item 5 applies the separation criterion -- a role is mistakable for another exactly
when every offset pinned in both templates carries the same value, offsets pinned in only one being free bits an adversary sets at will -- to the `3x3x3`,
`5x5x5` and star windows and to all eight period-`2` assignments at four window sizes. All exact.

**Reading, not theorem.** The law has no idea which sites are corners. There are `48` equally good ways to lay the pattern down, and the state settles into one
of them -- the way a magnet settles into an up-down alternation on sites that were all alike before. Item 4 is the other half of the same fact: where the box
cannot hold the period, the arrangement has nowhere to sit and no configuration reaches penalty zero.

## Theorem 3 -- the locality census, and the one place the reading is open

**Conclusion.** On the fine lattice, with star-local, through and across as defined:

1. Of the `16` quantum term types (three `A_ij`, six hop components, three hop totals, `B_i`, three face stabilizers) and the `49` marker term types (the `48`
   templates and the no-role penalty), `4` are star-local -- `A_x`, the `A B_i` component along `x` and along `z`, and `B_i` -- `61` are through with an
   explicitly constructed `6`-connected hub chain, and `0` are across.
2. Over all `48` sectors and all fillings of the free bits, the corner-centred seven-site star realises all `128` of its value patterns, and adjacent pairs
   realise all `4` value pairs. Hence a rule whose direct dependence at a site is only that site's six neighbours, and which reads only their **values**, must
   accept every star pattern that occurs; it is vacuous and pins no role.

**Proof.** Item 1 classifies each support by testing whether it fits in one star and, failing that, by constructing hubs and joining them along `L1` geodesics
until the hub set is `6`-connected, so the through classification is exhibited rather than asserted. Item 2 enumerates the stars occurring in every sector at
every filling. Both exact.

**Scope, stated plainly.** Item 2 is about **value-reading** rules only, whose constraint is a predicate on the recorded values in a star. Rules that read the
possibility state at a site -- what is still admissible there, rather than what value it shows -- are **not** covered, and are under test in a separate lane.

## Theorem 4 -- two dimensions, fully homogeneous

**Conclusion.** The connected one-qubit-per-site rule `IXZZXIIII` on `Z^2`, one generator pattern with support `{(-1,0), (-1,1), (0,-1), (0,0)}`,
`f_X = {(-1,0), (0,0)}`, `f_Z = {(-1,1), (0,-1)}`, has all translates commuting, torus code dimension `k(6) = k(8) = 2`, and exactly three nontrivial charge
classes near the origin. Their Levin-Wen T-junction signs are `+1` over `12` geometries, `+1` over `12`, and `-1` over `18`: two point bosons and one point
fermion. The mutual braid table over the three is `[+1, -1, -1]`, `[-1, +1, -1]`, `[-1, -1, +1]` -- exactly the toric-code `S`-matrix, `+1` on the diagonal, as
it must be for every abelian anyon including a fermion, and `-1` on every mixed pair.

**Proof.** Commutation is checked exhaustively over all translates within reach. The torus dimension is an `F2` rank. The charge classes are the syndromes on a
core block realisable from far away modulo those realisable locally. The T-junction uses thin step-wise legs with clearance between each leg's tube and the
other two far ends checked explicitly, which is what makes the three-term sign gauge invariant. Each braid loop is grown until its centre is farther from the
loop path than any hop window can reach, and every exit route of the probe string is checked. All exact.

## Theorem 5 -- one site per repeating unit, in the Pauli stabilizer class

**Conclusion.** Let a rule be a fully translation-invariant Pauli stabilizer rule on `Z^3` with one qubit per site and any number `t` of generator patterns per
cell. Then its charge module has no nonzero finite-length submodule, so no bounded operator moves a nontrivial point charge along three independent
directions, and in particular no such rule carries a three-dimensional point fermion. Concretely, for unit-cube generator support:

1. Of the `4^8` patterns, `1011` commute with all their translates and `735` of those have support at least `4`; modulo the `48` cubic point-group maps and the
   `6` Clifford relabellings these give `21` inequivalent one-pattern rules of support at least `4` (`28` at support at least `1`) and `423` two-pattern rules.
2. For each of the `21` the ideal `(f_X, f_Z)` is proper -- a common zero with all three coordinates units is exhibited over `GF(2)` -- so the charge module
   `M = R/(f_X, f_Z)` is nonzero and charges exist; and since the ideal is generated by two elements, Krull's height theorem gives height at most `2 < 3`, so
   `M` is never zero-dimensional.
3. The independent finite-window test, which uses none of that algebra, solves for the cluster shape together with the moving operator on a `2x2x2` block of
   generator cells with margin `3`, so every bound state in the block is covered. Over the `21` rules the number of axes carrying *some* mobile nontrivial
   cluster distributes `10, 5, 2, 4` -- four rules move some cluster along each axis separately -- and yet `0` rules have **one** cluster mobile along all
   three at once. The same test on all `423` two-pattern rules also returns `0`.

**Proof of the general statement.** With one qubit per site there are two Pauli degrees of freedom per site, so the syndrome map is `eps: R^2 -> R^t` and
`K = im(eps)` is generated by two elements. A charge `sigma` mobile along three independent vectors `v_1, v_2, v_3` satisfies `(1 + x^{v_i}) sigma = 0` in
`M = R^t / K`, so `Ann(sigma)` contains `(1 + x^{v_1}, 1 + x^{v_2}, 1 + x^{v_3})`, whose variety in the torus is finite; hence `R.sigma` has finite length and
`depth(M) = 0`. But if `rank K = 2` then `K` is free and `depth K = 3`; if `rank K = 1` then `K` is isomorphic to a two-generated ideal `I = h.J` with `h` the
gcd and `ht J = 2`, so `pd(R/I) = 2`, `pd(K) <= 1` and `depth K >= 2`. The depth lemma on `0 -> K -> R^t -> M -> 0` then gives
`depth(M) >= min(3, depth K - 1) >= 1 > 0`, a contradiction; all depths and projective dimensions are taken after localising at the maximal ideal
of the point where `R.sigma` is supported, where `R` is regular local of dimension `3` and Auslander-Buchsbaum applies. Equivalently: a two-generated ideal has height at most `2` by Krull, so in dimension `3` the
charge module can never be zero-dimensional; in dimension `2` the same count gives height at most `2 = dim`, which is why Theorem 4 has room to exist. The
obstruction is the count `dim - 2q >= 1` with `q = 1` qubit per site. Items 1 to 3 are exact computations; the general statement is the argument just given.

**Exact scope.** This covers fully translation-invariant Pauli stabilizer rules with one qubit per site, any number of generator patterns. It does **not**
cover non-stabilizer rules, rules whose ground state forms a superlattice role pattern (Theorem 1 is exactly such a rule, and it escapes because its vacuum is
not the same seen from every site), or more than one qubit per site.

## Corollary -- what is available inside the four axioms

Within the setting declared above, and on the finite clusters named:

1. A fermionic point particle in three dimensions is available inside the four axioms with **ordinary** composition. It is not a site; it is a shaped
   configuration -- a marked corner site whose six neighbours together carry odd parity -- on a superlattice role pattern that the law forms by itself, with
   eight fine sites per fermionic mode.
2. No graded composition clause is required for matter to be fermionic in this setting. The finite discriminator that gives a cross-site sign a readable
   shadow in record statistics is `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md`; the present note supplies a law of the
   ungraded kind whose excitations nonetheless exchange with `-1`, so the premise that a fermion at one qubit per site needs a graded clause is superseded by a
   construction. Earlier work proceeding from that premise -- `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md` and the compiler surveys cited above -- is
   contradicted in none of its computations; its premise is simply no longer the only starting point.
3. The necessity of the role pattern is the structural content. Theorem 5 says a three-dimensional point fermion cannot exist if the vacuum looks the same
   seen from every site: one site per repeating unit is excluded in the Pauli stabilizer class. Theorem 1 supplies a law whose vacuum does not look the same
   from every site, and it works. Eight sites per mode is the current construction, not a proven minimum: whether any repeating unit between two and eight
   sites works is not established here.
4. The two-dimensional case needs none of this. Theorem 4 exhibits a fully homogeneous one-qubit rule on `Z^2` with a point fermion, and the height count
   explains the difference between two dimensions and three.

## What does not move

- This does not decide what the framework's law is. It declares one law, of a form Admissibility permits, and computes with it.
- It supplies no update rule, no formation site, no formation rate, and no values. No coupling, no absolute unit, and no dynamical clause appears anywhere.
- It says nothing about non-stabilizer rules, about more than one qubit per site, or about any repeating unit of between two and eight sites.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

- The possibility-state reading. Theorem 3 item 2 covers only **value-reading** star rules. A rule whose star constraint reads which local possibilities
  remain admissible, rather than which value is recorded, is untouched by it; such a lane should treat Theorem 3 item 2 as the statement to get around and the
  `48`-sector zero set of Theorem 2 as the target to reproduce.
- The minimal repeating unit. Theorem 5 excludes one site per unit; Theorem 1 achieves eight. The interval between is open, and a lane closing it would sharpen
  the corollary considerably.
- The dynamical clause. This note gives a law and its zero-energy configurations, not a tick. A lane writing an update clause should treat Theorems 1 and 2 as
  the stationary content its clause must reproduce or contradict.

## Remaining live routes

1. Larger clusters and other geometries. Whether the `48`-sector count and the frustration persist on much larger boxes is a separate computation.
2. Rules outside the Pauli stabilizer class in three dimensions. Theorem 5 says nothing about them.
3. Species. One spinless `Z2`-charged fermion is constructed; no second species, spin or mass is supplied.
4. A rule of smaller window or period with an equally clean zero set: `5x5x5` is minimal for *this* pattern, and another pattern is another question.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions.

```text
setting: one qubit per site of Z^3; one covariant law; ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
encoding: BK superfast on the coarse sublattice 2Z^3; qubits on coarse edge sites; vertex order -x<-y<-z<+x<+y<+z; A_ji = -A_ij; B_i the six incident Z's; S_f the ordered four-A plaquette product
relations_and_open_block_dimensions: R0-R4 and prod_i B_i = +I on open and periodic 3x3x3; faces only k = V-1 at 27/54/26 and 64/144/63
torus_dimensions: faces only k = V-1+3 at 29, 66, 38 on 3^3, 4^3, 3x3x4; with three Wilson loops 26, 63, 35; full vacuum set k = 3 on all three, L-independent
hop_support_and_commutation: T_ij = (i/2) A_ij (B_i - B_j), 11 fine sites, all coarse edge sites, Linf radius 2, identical along x, y, z; 144000 of 144000 pairs with the 240 faces of the open 5x5x5 commute; 0 wrong syndromes
closed_circuits: x,y,z,-x,-y,-z (weight 16, 11 generators), box (34, 20), non-planar hexagon (43, 27); all in the face-stabilizer group with phase +1
statistics_and_controls: T-junction -1 over 10 geometries and direct exchange -1 over 4 on the open 7x7x7; bound pair +1; 3D toric code point charge +1; 2D toric code epsilon -1; bare X string anticommutes with 18 faces
role_pattern_and_templates: period (4,2,2); corner (s[ax]/2) mod 2, face 0, cube centre 1, edge free; 48 templates = 16 translates x 3 axis orientations; 5x5x5 window
zero_set_4x4x4: 48 cylinders, each penalty 0 for all 2^24 free-bit fillings, pairwise inconsistent, zero set 48 x 2^24, no junk, 48 search nodes, no SAT solver
zero_set_8x4x4_and_incommensurate: 48 sectors, 48 x 2^48; 5x4x4, 4x5x4, 7x4x4 each 0 zero-penalty configurations
window_minimality: 3x3x3 leaves 2 unseparated pin-pairs; 7-site star 29; every period-2 assignment fails at windows 3..9; 5x5x5 leaves 0 over all 48 templates
locality_census: 16 quantum and 49 marker term types; 4 star-local (A_x, A.B_i x, A.B_i z, B_i); 61 through with an explicit 6-connected hub chain; 0 across
star_proposition: corner-centred stars realise 128 of 128 value patterns and adjacent pairs 4 of 4, so no value-reading star-local rule pins a role; possibility-state rules are not covered
two_dimensional_rule: IXZZXIIII, support {(-1,0),(-1,1),(0,-1),(0,0)}; k(6) = k(8) = 2; 3 nontrivial classes; T-junction +1 x12, +1 x12, -1 x18; braid table = toric-code S-matrix
homogeneous_3d_census: 1011 valid of 4^8; 735 at support >= 4; 21 one-pattern rules (28 at support >= 1); 423 two-pattern rules
homogeneous_3d_algebra: M = R/(f_X, f_Z), R = F2[x,y,z] Laurent of dimension 3; all 21 ideals proper, unit-coordinate zero over GF(2); syndrome image 2-generated; Krull height <= 2 < 3; depth M >= 1 > 0
homogeneous_3d_mobility: axes with some mobile cluster 10, 5, 2, 4 over the 21; 0 of 21 and 0 of 423 with one cluster mobile along all three axes
sites_per_mode: 8 fine sites per fermionic mode; current construction, not a proven minimum
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

The law of Theorems 1 to 3 is a **designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the
supplier, and this note supplies one form and computes its consequences, deriving that form from no axiom and claiming for it no privileged status. The
marker rule's direct dependence is a `5x5x5` window, so this note does not claim that rule is nearest-neighbour in form; whether a rule whose direct
dependence is on adjacent sites only, longer reach arising through chains of adjacent conditions, can select the same zero set is open -- for
value-reading star rules Theorem 3 item 2 answers no at this spacing, and for possibility-state rules it is untested here. The
construction is for **one spinless `Z2`-charged fermion species**; no second species, spin, mass, or coupling appears.

Every statement of Theorems 1 to 3 is proved on the named finite clusters -- open coarse blocks `3x3x3`, `4x4x4`, `5x5x5`, `7x7x7`, and coarse tori `3^3`,
`4^3`, `3x3x4`, `4x4x4`, `8x4x4`, `5x4x4`, `4x5x4`, `7x4x4`. Nothing is claimed for infinite lattices or larger boxes; the `L`-independence of Theorem 1 item 2
is across the tori tested, and tori with a side of length `2` are excluded as multigraphs, on which `A_ij` is not determined by its endpoint pair.

Theorem 3 item 2 covers **value-reading** rules only. Whether a rule that reads the possibility state at a site -- what remains admissible there rather than
what is recorded -- can mark the roles star-locally is **open**, and is being tested in a separate lane. The census in item 1 is a statement about the
operators of the assembled law, not about the marker rule read as a constraint system; as a constraint system on values, the marker rule's dependence reaches
the next coarse corner at distance `2`, and every site in between is a free qubit.

The rotation covariance of the marker rule is obtained by **symmetrisation**: the period-`(4,2,2)` pattern is anisotropic, so the rule is the union of the
three axis orientations, and the single orientation an actual state shows is a broken symmetry among `48` equally admissible sectors, not a preference written
into the law. Separately, the encoding's edge order makes `A_ij` carry weights `4`, `6`, `8` along `x`, `y`, `z`; that anisotropy is a gauge convention of the
ordering, not physical, and it is why `A_x` is star-local in the census while `A_y` and `A_z` are through.

Theorem 5 is exact within its stated class and is not widened: fully translation-invariant Pauli stabilizer rules, one qubit per site, any `t`. Its
finite-window part is proved on a `2x2x2` block of generator cells with margin `3` and unit-cube generator support; its algebraic part is general in `t` and
in the support, and rests on Krull's height theorem and the depth lemma, both standard and both stated above with the deduction written out. No axiom is
amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: a construction, not a claim about the framework's law; five exact theorems on named finite clusters; one open
question stated as open (the possibility-state reading); and one quantity given as a construction rather than a bound (eight sites per mode). No statement here
is a floating-point witness -- there are none -- and none depends on a solver whose answer cannot be replayed by hand.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the five context notes
in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at
`PASS=24 FAIL=0` with runtime under the declared `600` seconds and stdout under `5500` characters, a current zero-dependency citation-manifest entry, and
passing repository pipeline, strict-lint, and changed-evidence gates; independent audit remains a separate lane.
