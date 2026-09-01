---
claim_id: matter_graded_composition_axiom_update_boundary_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "On three sites of Z^3 the ungraded tensor product and the graded (parity) product of the one-site algebras M_2(C) are exhibited; both contain every one-site algebra faithfully, both generate M_8(C), both agree on every one-site even element, and they differ exactly in the cross-site relation (commutation versus anticommutation of the odd elements), so no sentence of the four axioms, each of which names only one-site data and lattice adjacency, distinguishes them. In the ungraded product every site-local family commutes across sites and a cross-site anticommuting family is nonlocal and needs a total order and a per-site grading axis; every complex Z_2-grading of M_2(C) is Ad(n·sigma) for an unoriented axis; no axis is fixed by the 24 proper cubic rotations; the unital real-algebra automorphisms of M_2(C) commuting with the rotation action are exactly the identity and the antilinear Clifford involution alpha(a + b·sigma) = conj(a) - conj(b)·sigma. Under the graded product with the mode's own parity the site generators satisfy exact CAR with no string, the site order is a representation artifact (one-dimensional even unitary intertwiner space), the parity axis is the ladder's own, every parity-diagonal state annihilates every odd element, the readable one-site content is span{1, n_x}, and the commuting hard-core ladders violate the graded rule. The rotation-covariant real graded product on two sites is Cl(6,0): real dimension 64 versus 32, Hermitian site generators anticommuting across sites, one-site even Hermitian content scalar. Both local structures share the same 32-dimensional parity-even and 32-dimensional parity-odd subspaces of M_8(C); on the 2x2x2 cube at most 7 of the 12 nearest-neighbour bonds are order-adjacent under any total order; and in the real graded product the three-Majorana bilinears form a Hermitian spin-1/2 at each site (su(2), S.S = 3/4), even and commuting across sites. The graded product selects no state and no Hamiltonian. No axiom is amended; a candidate clause is recorded as a science-level decision awaiting the owner."
upstream_dependencies: []
runner: scripts/matter_graded_composition_axiom_update_boundary_check_2026_09_01.py
---

# The composition gap: the four axioms fix every one-site datum and no cross-site product; the graded product is the matter clause

**Date:** 2026-09-01
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/matter_graded_composition_axiom_update_boundary_check_2026_09_01.py`](../scripts/matter_graded_composition_axiom_update_boundary_check_2026_09_01.py)
**Runner cache:**
[`logs/runner-cache/matter_graded_composition_axiom_update_boundary_check_2026_09_01.txt`](../logs/runner-cache/matter_graded_composition_axiom_update_boundary_check_2026_09_01.txt)
**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional theorem on three sites: two compositions of the same one-site data, the rotation-equivariant automorphism classification, and the order-freeness of the graded product."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-dimensional theorem and route the candidate composition clause to the owner as a science-level decision."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

Sites are `0, 1, 2` on a line in `Z^3`, with nearest-neighbor pairs `(0,1)` and `(1,2)` and with `(0,2)` not
adjacent; each site carries `M_2(C)`. The target is the conjunction of the eight statements below, which are
exactly the eight check groups `A`--`H` of the primary runner.

1. `T1` (`A`). Both the ungraded tensor product and the graded parity product of the same three one-site
   algebras embed each site algebra by an injective unital `*`-homomorphism, both generate `M_8(C)` of complex
   dimension `64`, both give the same even one-site content, and they differ exactly in the cross-site relation.
2. `T2` (`B`). In the ungraded product a site-local family whose members at distinct sites anticommute is the
   zero family, so a cross-site anticommuting family is not site-local there.
3. `T3` (`C`). Every `Z_2`-grading of the one-site algebra is trivial or `Ad(n·sigma)`; the compatible axes are
   unoriented, and different axes give different odd parts.
4. `T4` (`D`). The proper cubic rotation group has order `24`, fixes no axis, and acts on `R^3` with real
   commutant of dimension `1`; the unital real-algebra automorphisms of `M_2(C)` commuting with `Ad(U_R)` number
   exactly `2`, the identity and an antilinear involution `alpha`.
5. `T5` (`E`). Under the graded product taken with the mode's own parity the site generators satisfy exact
   canonical anticommutation relations with no string factor; the site order is a representation artifact with a
   one-dimensional even intertwiner space; the parity axis is the ladder's own; every parity-diagonal state
   annihilates every odd element; the readable one-site content is `span{1, n_x}`; and the commuting hard-core
   ladders violate the graded rule.
6. `T6` (`F`). On two sites the rotation-covariant real graded product of `Cl(3,0)` presentations is `Cl(6,0)`,
   of real dimension `64` against real dimension `32` for the ungraded `M_2(C) (x) M_2(C) = M_4(C)`; its
   Hermitian site generators anticommute across sites and its one-site even Hermitian content is scalar.
7. `T7` (`G`). The graded product selects no state and no Hamiltonian: two distinct even Hamiltonians and two
   parity eigenstates with distinct exact expectation values coexist on the same graded algebra.
8. `T8` (`H`). The two local structures share the same `32`-dimensional parity-even and `32`-dimensional
   parity-odd subspaces of `M_8(C)`; on the `2 x 2 x 2` cube at most `7` of the `12` nearest-neighbor bonds are
   order-adjacent under any total order; and in the real graded product the three-Majorana bilinears form a
   Hermitian spin-`1/2` at each site, even and commuting across sites.

## Imports and authority

Imported scientific authority: none load-bearing. The Jordan-Wigner realization, graded tensor products of
superalgebras, and Clifford algebras are standard methodology; every object is redeclared here and every
statement is recomputed in full by the primary runner. No observational value, no fitted number, and no
framework premise beyond the sentences quoted verbatim in Corollary 1.1 enters any proof. Non-load-bearing
context pointers, plain file names with no grade and no dependency weight:

- `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md` (Grassmann compatible, not forced
  by operator-algebra and dimension facts).
- `KS_ETA_VS_JW_STRING_CAR_LOCALITY_NO_GO_NOTE_2026-06-02.md` (staggered signs orthogonal to the statistics
  object).
- `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md` (reflection positivity plus ring monodromy select
  neither).
- `GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md` (loop cocycle consistency selects neither).
- `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md` (given
  cross-site graded locality the Grassmann/CAR class is forced on its own surface).
- `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md` (the on-site `2 pi` sign is not
  the cross-site discriminator).
- `GL_F_RECORD_VALUE_DICTIONARY_COMMUTING_LOCK_BOUNDED_THEOREM_NOTE_2026-09-01.md` (record-value dictionaries
  cannot be graded with propagation).

This note re-declares everything it uses and cites none of their grades.

## Obligation graph

The proof is acyclic. Each node after `P0` is checked by the correspondingly lettered runner group.

1. `P0` (proved here): declare sites, matrix units, the ungraded embedding `iota`, the Jordan-Wigner family, the
   graded embedding `kappa`, the total parity `P`, and the rotation lifts.
2. `P1` (`A`): both embeddings injective unital `*`-homomorphisms, both generating `M_8(C)`, even one-site
   content equal, cross-site relations opposite.
3. `P2` (`B`): no nontrivial site-local anticommuting family in the ungraded product, and the Jordan-Wigner
   family is not site-local in it.
4. `P3` (`C`): classify the one-site gradings as unoriented axes.
5. `P4` (`D`): the rotation group, its fixed-axis equations, its real commutant, and the equivariant unital real
   automorphisms.
6. `P5` (`E`): the anticommutation relations, graded locality, order-freeness, parity axis, parity
   superselection, readable content, and the hard-core comparison.
7. `P6` (`F`): the two-site real graded product, its dimension, cross-site anticommutation, one-site even
   Hermitian content, and the bond bilinears.
8. `P7` (`G`): non-selection of state and dynamics.
9. `P8` (`H`): the shared even and odd subspaces, the cube bond count, and the Majorana bilinear spins.

The strongest supported scope is precisely `P0`--`P8`.

## Definitions

Write `one` for the `2 x 2` identity, `s1, s2, s3` for the Pauli matrices, and `E00, E01, E10, E11` for the
matrix units of `M_2(C)`, with `E01 = |0><1|`, so that `E_ij E_kl = delta_jk E_il` and `E00 + E11 = one`. The
**ungraded product** is `M_2(C) (x) M_2(C) (x) M_2(C)`, with site embedding `iota(x, M)` placing `M` in slot `x`
and the identity in the other two slots. The **Jordan-Wigner family** for a total order of the three positions,
with `Z = s3`, is

```text
c_x  = (Z at every position before x) (x) E01 (x) (one after x),
cd_x = c_x^dagger,   n_x = cd_x c_x,   P = s3 (x) s3 (x) s3.
```

The default order is `[0,1,2]`; the order `[2,0,1]` is used in Theorem 5. The **graded product** is the algebra
generated by site copies of `M_2(C)`, each carrying the parity grading `even = span{E00, E11}` and
`odd = span{E01, E10}`, subject to the cross-site rule: odd elements at distinct sites anticommute, and even
elements commute with every element at another site. Its concrete model on `(C^2)^(x)3` is the Jordan-Wigner
realization, with graded site embedding the unital `*`-homomorphism `kappa` given by

```text
kappa(x,E01) = c_x,  kappa(x,E10) = cd_x,  kappa(x,E11) = cd_x c_x,  kappa(x,E00) = c_x cd_x
```

and extended linearly. Both `iota` and `kappa` present the same one-site algebra; they differ only in how the
site copies sit relative to one another. With `R_z = [[0,-1,0],[1,0,0],[0,0,1]]` and
`R_x = [[1,0,0],[0,0,-1],[0,1,0]]`, the proper cubic rotation group is `G = <R_z, R_x>` and the **rotation
action** on the site algebra is `Ad(U_R)` with `SU(2)` lifts `U_z = (one - i s3)/sqrt(2)` and
`U_x = (one - i s1)/sqrt(2)`. The **real graded product** of two `Cl(3,0)` site presentations is `Cl(6,0)`,
realized on `C^8` from three Jordan-Wigner modes by `g_(2m-1) = a_m + a_m^dagger` and
`g_(2m) = i (a_m - a_m^dagger)`, site `0` carrying `(g1,g2,g3)` and site `1` carrying `(g4,g5,g6)`.

## Theorem 1 — the same one-site data supports two compositions

**Conclusion.** For each site `x`, both `iota(x,·)` and `kappa(x,·)` are injective unital `*`-homomorphisms of
`M_2(C)`; both families generate `M_8(C)`; the even one-site content agrees, `kappa(x,E11) = iota(x,E11)` and
`kappa(x,E00) = iota(x,E00)`; the odd content differs for `x >= 1`, already at `kappa(1,E01) != iota(1,E01)`;
and the cross-site relations are opposite.

**Proof.** Both maps carry the sixteen products `E_ij E_kl = delta_jk E_il` correctly, carry adjoints to
adjoints, and carry `E00 + E11` to the identity; stacking the four images as row vectors gives rank `4` in each
case, so each embedding is injective. The `64` Pauli strings built from `iota` images span a space of dimension
`64`, and the `64` normal-ordered monomials `prod_x cd_x^(a_x) c_x^(b_x)` with `a_x, b_x in {0,1}` also span a
space of dimension `64`; since `M_8(C)` has complex dimension `64`, each composition generates the full algebra.
The even one-site elements coincide because `cd_x c_x` and `c_x cd_x` pair a string with its own conjugate and
the `s3` factors cancel; the odd one-site elements differ once a nontrivial string is present, already at site
`1`. The cross-site relations are opposite:

```text
ungraded:  [iota(0,E01), iota(1,E01)] = 0,  {iota(0,E01), iota(1,E01)} = 2 iota(0,E01) iota(1,E01) != 0;
graded:    {c_0,c_1} = 0,  {c_0,cd_1} = 0,  [c_0,c_1] = 2 c_0 c_1 != 0.
```

The three graded identities hold for the non-adjacent pair `(0,2)` as well: the graded rule relates distinct
sites, not adjacent sites.

**Corollary 1.1 — no axiom sentence distinguishes the two products.** The sentences bearing on this surface are,
verbatim:

```text
Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site."  "No site is privileged."
Qubit: "Each site has a domain of local possibilities."  "The full one-site possibility domain has algebraic
presentation `M_2(C)`."  "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and adds no
further primitive structure."  "No possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone."
Admissibility: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and
proper cubic rotations."  "For each site, the probability distribution over the possibilities is determined by,
and varies with, the nearest-neighbor conditions."
Record: "Records form."  "When present, a record locks exactly one admissible local possibility. A site never
carries more than one record; records are permanent."  "Only records are readable. A readout value is determined
by record content alone. A site with no record cannot be read."
Qualification: "A choice not fixed by the supplied structure remains a named conditional or open dependency."
```

Each sentence names one-site data or lattice adjacency. By Theorem 1 the two compositions carry identical
one-site invariants, an identical one-site possibility domain, identical nearest-neighbor conditional laws on
one-site data, and an identical record configuration space, since a record locks one possibility of the same
one-site algebra either way. Both products therefore satisfy every sentence above, and the cross-site
composition rule is, in the Qualification's own words, "A choice not fixed by the supplied structure".

## Theorem 2 — the ungraded product admits no site-local graded family

**Conclusion.** If `f_0 = iota(0,A)` and `f_1 = iota(1,B)` satisfy `{f_0, f_1} = 0`, then `A = 0` or `B = 0`.
The Jordan-Wigner family is therefore not site-local in the ungraded product.

**Proof.** For symbolic complex `2 x 2` matrices the identity `{A (x) one, one (x) B} = 2 (A (x) B)` holds
identically, the third factor carrying the identity throughout, and the block identity
`(A (x) B)[2i:2i+2, 2j:2j+2] = A[i,j] B` holds for all `i, j` symbolically, so `A (x) B = 0` forces `A = 0` or
`B = 0`; anticommutation of a site-local pair therefore forces the pair to vanish. Conversely `c_1` is not
site-local: stacking the four images of `iota(1,·)` together with `c_1` as row vectors gives rank `5` rather
than `4`, and `c_1` fails to commute with `iota(0,s1)`. A cross-site anticommuting family in the ungraded
product needs a total order of the sites and a per-site grading axis, both supplied from outside it.

## Theorem 3 — a grading of the site algebra is an unoriented axis

**Conclusion.** Every `Z_2`-grading of `M_2(C)` implemented by an inner involution is trivial or `Ad(n·sigma)`;
the `*`-compatible ones are exactly those with real unit `n`, and `n` and `-n` give the same grading, so the
datum is an unoriented axis. Different axes give different odd parts.

**Proof.** Every automorphism of `M_2(C)` is inner. For `V = a one + b1 s1 + b2 s2 + b3 s3` with complex
coefficients, `V V = (a^2 + b1^2 + b2^2 + b3^2) one + 2a (b·sigma)`, so `V V` is proportional to the identity
exactly when `a = 0` or `b1 = b2 = b3 = 0`. The second branch is the trivial grading; the first gives
`Ad(b·sigma)`, an automorphism when `b·b != 0`, and rescaling sets `b·b = 1`. The `*`-compatible case is the exact identity
`(b·sigma)(b·sigma)^dagger = (b·conj(b)) one + i (b x conj(b))·sigma` for complex `b`, verified symbolically:
`Ad(V)` preserves the adjoint exactly when `V V^dagger` is scalar, which is the vanishing of `b x conj(b)`;
the runner exhibits that this vanishes for `b` a phase times a real vector and fails for `b = (1, i, 0)`, and
the elementary converse (`b x conj(b) = 0` forces `conj(b)` proportional to `b`, hence `b` a phase times a
real vector) reduces the normalized case to `b = ±n` with `n` real and `n·n = 1`. The axis is the ladder axis: for
`n = e3` the `-1` eigenspace of `Ad(s3)` on `M_2(C)` is exactly `span{E01, E10}` of complex dimension `2` and
the `+1` eigenspace is `span{E00, E11}`, while for `n = e1` the odd part is `span{|+><-|, |-><+|}` with
`|±> = (1, ±1)/sqrt(2)`, which differs from `span{E01, E10}`. The axis is a genuine per-site datum, not a
notational convention.

## Theorem 4 — no covariant complex grading; the covariant grading is antilinear

**Conclusion.** `G = <R_z, R_x>` has order `24`, every element having integer entries and determinant `+1`. The
generator fixed equations, in all four sign combinations, give only `n = 0`, and the real commutant of
`{R_z, R_x}` in `M_3(R)` has dimension `1`. Hence no unoriented axis is rotation invariant and no complex parity
grading of the site algebra is covariant under `Ad(U_R)`. The unital real-algebra automorphisms of `M_2(C)`,
viewed as an `8`-dimensional real algebra with basis `{1, i, s1, s2, s3, i s1, i s2, i s3}`, that commute with
that action are exactly two:

```text
identity;
alpha:  1 -> 1,  i -> -i,  s_k -> -s_k,  i s_k -> i s_k,
equivalently  alpha(a one + b·sigma) = conj(a) one - conj(b)·sigma.
```

**Proof.** Closure of the two generators gives `24` distinct integer matrices of determinant `+1`. The `SU(2)`
lifts satisfy `U s_k U^dagger = sum_j R_jk s_j` exactly for both generators, so the rotation action on the site
algebra is `Ad(U_R)`, acting on the real basis by `1 -> 1`, `i -> i`, `s_k -> sum_j R_jk s_j`, and
`i s_k -> sum_j R_jk i s_j`. Solving `R_z n = ±n` together with `R_x n = ±n` over the reals in all four sign
combinations yields only `n = 0`, and an unoriented axis would have to solve one of those four systems. The real
commutant being `R·1` makes the vector representation irreducible over `R`, which supplies the Schur reduction
used for the classification: an equivariant real-linear map has one `2 x 2` real block `A` on `span{1, i}` and
one common `2 x 2` real block `B` on each `span{s_k, i s_k}`. Imposing unitality and multiplicativity on all
`64` basis products and solving gives exactly the two solutions displayed, and no others. Exact properties of
`alpha`: it squares to the identity; it is antilinear, `alpha(i M) = -i alpha(M)`, exhibited already at
`M = one`; on all eight basis elements it equals `M -> s2 conj(M) s2` with entrywise conjugation; its `-1`
eigenspace is `span_R{s1, s2, s3, i·1}` and its `+1` eigenspace is `span_R{1, i s1, i s2, i s3}`, closed under
products and carrying the quaternion relations, for instance `(i s1)(i s2) = -(i s3)`.

**Consequence.** A complex parity grading cannot be made covariant under the Lattice rotations if those
rotations act on the site algebra, the grading datum being an axis and no axis surviving the `24` rotations. It
is covariant vacuously if the rotations act on site indices only. Which reading is the framework's is a separate
open question about the identification of the internal index with the external one; see
`SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08.md` as a plain-text pointer,
cited with no grade and carrying no weight here.

## Theorem 5 — the graded product with the mode's own parity

**Conclusion.** Take the graded product with each site graded by its own mode parity. Then:

1. The generators satisfy exact canonical anticommutation relations, `{c_x, c_y} = 0` and
   `{c_x, cd_y} = delta_xy`, with no string factor in any relation.
2. Graded locality holds in the total-parity sense: `P c_x P = -c_x` and `P n_x P = n_x`, and even one-site
   elements commute with everything at other sites, including `[n_0, c_1] = [n_0, cd_1] = [n_0, c_2] = 0` and
   `[c_0 cd_0, c_1] = 0`.
3. The site order is a representation artifact: the Jordan-Wigner family for the order `[2,0,1]` also satisfies
   the relations, and the intertwiner space `{W : W c_x^(1) = c_x^(2) W and W cd_x^(1) = cd_x^(2) W}` is
   one-dimensional; its solution commutes with `P`, hence is even, and `W W^dagger` is a scalar multiple of the
   identity, so `W` is unitary up to scale.
4. The ladder fixes its own parity axis: solving `(n·sigma) E01 (n·sigma) = -E01` for real `n` with `n·n = 1`
   gives exactly `n = ±e3`.
5. Parity superselection holds: with `P± = (1 ± P)/2` and symbolic `8 x 8` matrices `X, Y`, the parity-diagonal
   form `rho = P+ X P+ + P- Y P-` satisfies `trace(rho O) = 0` for every one of the `32` odd Pauli strings `O`,
   those with an odd number of factors drawn from `{s1, s2}`.
6. The readable one-site content is even: the even part of `kappa(x, M_2(C))` is `span{1, n_x}`, commutative,
   with `n_x^2 = n_x` and spectrum `{0,1}`; the odd part is `span{c_x, cd_x}`.
7. The commuting hard-core ladders violate the graded rule: `{iota(0,E01), iota(1,E01)} != 0` while
   `{c_0, c_1} = 0`, and by Theorem 2 any site-local family in the ungraded product with `{f_0, f_1} = 0` has
   `f_0 f_1 = 0`.

**Proof.** Items 1, 2, 5, 6, and 7 are direct exact computations on `(C^2)^(x)3`. Item 3 is the solution of a
linear system for a symbolic `8 x 8` complex `W`: the solution space has dimension `1` and its single solution
is even and unitary up to scale, so the two orders give unitarily equivalent presentations of the same graded
algebra and the order carries no content. Item 4 is the solution of `(n·sigma) E01 (n·sigma) = -E01` on the real
unit sphere.

**Reading, not theorem.** On this surface the Record sentence "Only records are readable" and parity
superselection say the same thing: by item 5 no parity-diagonal state gives a nonzero value to any odd element,
and by item 6 the one-site content able to carry a readout value is the even content `span{1, n_x}` with
spectrum `{0,1}`. Odd content is never registered. This is an interpretive alignment of two independent
statements, not a derivation of either from the other, and nothing below depends on it.

## Theorem 6 — the covariant alternative is Cl(6,0) and re-types the site

**Conclusion.** On two sites the rotation-covariant real graded product of the two `Cl(3,0)` site presentations
is `Cl(6,0)`. Its six generators are Hermitian with `{g_a, g_b} = 2 delta_ab`; the `64` ordered products `g_S`
over subsets `S` of `{1,...,6}` are `R`-linearly independent, so the real algebra generated has real dimension
`64`, against real dimension `32` for the ungraded `M_2(C) (x) M_2(C) = M_4(C)`. The Hermitian site generators
anticommute across sites, `{g_j^(0), g_k^(1)} = 0` for all `j, k`. One-site even Hermitian elements are scalars.
The smallest Hermitian even non-scalar elements are the cross-site bond bilinears `i g_j^(0) g_k^(1)`, which are
Hermitian, nonzero, and commute with the total parity `G = (-i)^3 g1 ... g6`, which satisfies `G^2 = 1`.

**Proof.** The six elements built from the three Jordan-Wigner modes are Hermitian and satisfy
`{g_a, g_b} = 2 delta_ab` by direct computation. Real and imaginary parts of the `64` ordered products give a
real `64 x 128` coordinate matrix of rank `64`, which is the stated real dimension; the ungraded two-site
product `M_4(C)` has real dimension `32`. Cross-site anticommutation is checked for all nine generator pairs.
For the one-site even Hermitian content, `(g_a g_b)^dagger = g_b g_a = -g_a g_b` for `a != b`, so a real
combination of `{1, g1 g2, g2 g3, g3 g1}` is Hermitian exactly when the three bivector coefficients vanish,
leaving `R·1`. A cross-site bilinear behaves oppositely,
`(i g_j^(0) g_k^(1))^dagger = -i g_k^(1) g_j^(0) = i g_j^(0) g_k^(1)`, so it is Hermitian, and being even it
commutes with `G`. The phase `(-i)^3 = i` makes `G` Hermitian, and moving each generator through the product
gives `G^2 = 1`.

**Consequence.** This alternative is rotation-covariant and axis-free, but it re-types the site: the site's
Hermitian generators become odd, the one-site even Hermitian content collapses to the scalars, and the readable
content moves to the bond level.

## Theorem 7 — the graded product selects no state and no dynamics

**Conclusion.** The hopping Hamiltonian over nearest-neighbor pairs,
`H_hop = sum over nearest-neighbor (x,y) of (cd_x c_y + cd_y c_x)`, and `H_0 = 0` are both even, `[H, P] = 0`,
and distinct. The parity eigenstates `cd_0 |vac>` and `(cd_0 + cd_1)|vac>/sqrt(2)` have exact `H_hop`
expectation values `0` and `1`.

**Proof.** Each term `cd_x c_y` is a product of two odd elements, hence even, so both Hamiltonians commute with
`P`; they are distinct because `H_hop` is nonzero. Both displayed vectors are eigenvectors of `P` with the same
eigenvalue, and the two expectation values are computed exactly as `0` and `1`. Same algebra, same parity
sector, different dynamics and different values: the composition supplies no dynamical or state content.

## Theorem 8 — the two local structures coexist on one algebra

**Conclusion.** (1) The parity-even elements of the ungraded local structure, the `32` Pauli strings commuting
with `P`, and the parity-even elements of the graded local structure, the `32` normal-ordered monomials of even
degree, span the same `32`-dimensional subspace of `M_8(C)`; the two `32`-dimensional odd subspaces coincide
likewise. (2) On the `2 x 2 x 2` cube of `Z^3`, with its `12` nearest-neighbor bonds, at most `7` bonds are
order-adjacent under any of the `8! = 40320` total orders of its sites, so under every order at least `5`
nearest-neighbor hops `cd_x c_y` carry a string factor in the ungraded frame. (3) In the real graded product of
Theorem 6 the site bilinears `S_x^a = -(i/2) epsilon_abc g_b^(x) g_c^(x)` are Hermitian, satisfy
`[S^a, S^b] = i S^c` at each site with `S·S = 3/4`, commute with the total parity `G`, and commute across the
two sites.

**Proof.** (1) Rank computations: each of the four families has rank `32`, and the union of the two even
families, like the union of the two odd families, still has rank `32`. (2) Enumeration of all `40320` orders,
counting consecutive pairs that are bonds; the maximum is `7`, attained by a Hamiltonian path of the cube, and
`12 - 7 = 5`. (3) Direct exact computation on `C^8`.

**Consequence.** The two compositions are not two theories but two local structures on one algebra, agreeing
on the entire even sector. A lane that works only with even content, occupancy, counts, and bilinears, is
unchanged by a graded clause; a lane that uses odd content must declare which local structure its odd operators
belong to, and in `Z^3` no site order makes both local at once, since on the cube at least five of twelve
nearest-neighbor hops are strings in the ungraded frame. Under the Clifford alternative the coexistence is
internal to one product: the bilinear spin lattice sits in the even sector and the Majorana vectors in the odd
sector, at the price of the extra dimension counted in Theorem 6.

## Corollary — what a graded composition clause would move

The table records what a supplied cross-site graded composition clause would change on this surface. It is a
statement about the clause, not an adoption of it.

| Before | After |
|---|---|
| Statistics selection: graded locality is an open cross-site premise. | Supplied by the composition clause; on the two-candidate surface exhibited here only the CAR class satisfies it. |
| Jordan-Wigner order and string: a supplied input. | A representation artifact of embedding the graded product into the ungraded product; by Theorem 5 the intertwiner space is one-dimensional, so order is not composition content. |
| Grading axis: a per-site choice, and by Theorem 4 not rotation covariant. | The mode's own parity; by Theorem 5 the ladder fixes `n = ±e3`, so no further choice is made. |
| Record readability: one-site possibility. | One-site even content `n_x` with spectrum `{0,1}`; odd content unregistrable. |
| The commuting-lock interface: the graded and operator-level construction class is nonempty. | That class is the composition rule itself. |

## What does not move

- No dynamics, action, matter functional, or Hamiltonian is selected; Theorem 7 exhibits two even Hamiltonians
  on the same algebra. No mass, no generation count, no chirality, and no gauge content is supplied.
- The formation site and the formation rate are untouched, as are the form and the values of the probability
  distribution over the possibilities. No time metric is supplied.
- No audit status is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node
  is created or edited.
- No axiom text is amended, extended, reworded, or reinterpreted. The axiom sentences appear here only as the
  verbatim quotations in Corollary 1.1.

## Interfaces named for other lanes, not moved here

These interfaces are named so that a later note can consume them; nothing here moves them.

- The matter-action statistics binary, count-once versus count-twice, named as open in
  `ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md` (plain-text pointer, no grade): under
  Candidate Q the Berezin functional of one complex mode per site is a determinant, under Candidate C a
  Pfaffian. A clause would fix the binary; this note proves nothing about the action itself.
- A Record-local source density: by Theorem 5 item 6 the readable one-site content is `n_x` with spectrum
  `{0,1}`, and by Theorem 8 it is the even content shared by both local structures. Any lane that sources on
  records has this as its candidate source; no coupling and no absolute unit are supplied here.
- Lanes whose records lock a possibility with nonzero odd component, such as an equatorial projector, name odd
  content as readable; under a graded clause that reading is not available at the one-site level (Theorem 5
  item 5), so those lanes would be re-scoped to the even sector, or would name the ungraded local structure
  explicitly as theirs.

## Candidate clause recorded as a science-level decision

Two candidate composition clauses are recorded below. This note lands neither. **Candidate Q — parity
composition** is the author's recommendation, not the framework's.

```text
Each site's presentation carries the parity grading of one mode. Distinct
sites compose by the graded product: odd elements at distinct sites
anticommute, and even elements commute with every element at another site.
```

Candidate Q adds exactly two structural data: one mode parity per site, and the cross-site rule. It supplies no
site order, no string, no value, no weight, no dynamics, and no lattice direction, the grading being internal.
Read within the graded presentation, "No possibility is privileged" holds of the two parity possibilities, which
stand on equal footing; the clause does distinguish the parity possibilities from their superpositions, and that
is the honest cost. By Theorem 5 the readable one-site content is the even content, so "Only records are
readable" and parity superselection coincide here. The rule speaks of distinct sites rather than adjacent sites,
and by Theorem 1 the relation indeed holds on the non-adjacent pair `(0,2)`. By Theorem 8 the clause removes
nothing from the even sector: both local structures are one algebra with one even sector, so every lane that
works with even content is unchanged, and only lanes using odd content must say which local structure they mean.

**Candidate C — Clifford composition** is the rotation-covariant alternative; the author does not recommend it.

```text
Distinct sites compose by the graded product of their Cl(3,0) presentations.
```

Candidate C is rotation-covariant and axis-free, which is exactly what Theorem 4 shows Candidate Q is not. By
Theorem 6 it makes the site's Hermitian generators odd, so they anticommute across sites; the one-site even
Hermitian content collapses to the scalars; and the lattice algebra on `N` sites becomes `Cl(3N,0)` of real
dimension `2^(3N)` rather than `2 · 4^N`. It re-types the site from a qubit with readable one-site content into
three Majorana partons whose readable content lives on the bonds.

Per the policy workflow quoted here, this note records the decision and does not add the clause.

```text
"If a physics-loop or science worker reaches "we need an extra axiom to close this", the correct action is:
1. Land the work as a bounded no-go boundary note documenting what would close under the proposed axiom.
2. Record the proposed axiom as an explicit science-level decision waiting on human input. 3. Move to a
different lane or a different attack frame. Do not add the axiom and proceed."
```

## Remaining live routes

1. A derivation of the cross-site composition rule from the four axioms together with the approved primitives,
   on a route outside those already tested by the context notes named in "Imports and authority". This note
   proves no such derivation impossible; it proves that the sentences quoted in Corollary 1.1 do not by
   themselves distinguish the two products.
2. An owner-decided clause, Candidate Q or Candidate C, followed by re-derivation of the staggered-carrier chain
   directly on the graded product.
3. A record-supplied grading, in which the locked possibility itself furnishes the parity axis. Named here, not
   developed here.

## Executable claim block

The canonical machine-bound restatement of the eight theorem conclusions.

```text
sites: 3
adjacent_pairs: (0,1) and (1,2); (0,2) not adjacent
generated_algebra_both_compositions: M_8(C)
generated_complex_dimension: 64
pauli_string_span_dimension: 64
normal_ordered_monomial_span_dimension: 64
ungraded_cross_site_commutator: 0
graded_cross_site_anticommutator: 0
graded_rule_restricted_to_adjacent_pairs: false
even_one_site_content_agrees: true
site_grading_form: trivial or Ad(n·sigma), n real unit, unoriented
proper_cubic_group_order: 24
proper_cubic_fixed_axes: 0
vector_representation_real_commutant_dimension: 1
equivariant_unital_real_automorphism_count: 2
equivariant_unital_real_automorphisms: identity, alpha
alpha_linearity: antilinear
alpha_closed_form: M -> s2 conj(M) s2
car_relations_exact_no_string: true
jw_intertwiner_space_dimension: 1
jw_intertwiner_parity: even
parity_axis_solutions: +e3 and -e3
odd_pauli_strings_annihilated: 32
readable_one_site_content: span{1, n_x}
n_x_spectrum: {0, 1}
two_site_real_graded_algebra: Cl(6,0)
two_site_real_graded_dimension: 64
two_site_ungraded_real_dimension: 32
one_site_even_hermitian_content: scalar
even_hamiltonians_exhibited: H_0 = 0 and H_hop
hopping_expectation_values: 0 and 1
even_subspace_shared_dimension: 32
odd_subspace_shared_dimension: 32
cube_nearest_neighbor_bonds: 12
cube_max_order_adjacent_bonds: 7
majorana_bilinear_spins: su(2) per site, S.S = 3/4, even, commuting across sites
axioms_amended: 0
status_values_set: 0
registry_entries_created: 0
runner_result: PASS=37 FAIL=0
```

## Proof boundary

Every statement is proved on three sites, and the `Cl(6,0)` statements of Theorem 6 on two sites. Nothing is
claimed about infinite lattices beyond what these finite statements imply directly. Nothing is claimed about the
existence or non-existence of a derivation of the cross-site composition rule from the four axioms: Corollary
1.1 is a statement about the quoted sentences, not about every possible argument. No no_go claim type is
asserted; this note is a bounded theorem. No axiom is amended, no audit status is set, and no registry entry is
created. The candidate clauses are recorded and not adopted.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", every
axiom sentence used appears verbatim in Corollary 1.1, and every context note named in "Imports and authority"
is a plain-text pointer carrying no grade and no weight. Hard landing conditions are a fresh exact runner and
cache pair closing at `PASS=37 FAIL=0`, a current zero-dependency citation-manifest entry, and passing
repository pipeline, strict-lint, and changed-evidence gates; independent audit remains a separate lane.
