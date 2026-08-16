# Exact rank ceiling 144 and blind-space floor 48 for the full cell-symmetry action

Date: 2026-08-09

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py`](../scripts/physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "identify the eight small matrices whose rank deficits total 39, then test additional structure inside those blocks"
conditional_surface_status: "exact for the declared finite four-cube cutting system and full 384-map symmetry action; no physical law, axiom-level covariance, or multi-cell extension is claimed"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the finite symmetry decomposition, rank ceiling 144, blind-space floor 48, and attaining witness are exact; physical and multi-cell extensions remain open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Result

A preceding computation sampled tables equivariant under the full symmetry of
the unit four-cube. Its largest sampled rank was 144. The result here replaces
that sample maximum with a derivation: every rational table intertwining the
declared 384-map actions has rank at most 144 and piece-domain blind dimension
at least 48, and an explicit integer intertwiner attains both bounds.

The cover incidence table itself has rank 105 and blind dimension 87. Its 39
dimensions of rank deficit are localized exactly among eight of twenty rational
isotypic parts.

## The finite object

The construction starts with the unit four-cube on sixteen corners. Among its
2672 determinant-one five-corner subsets, 400 have the minimum declared
adjacency cost 6. They form 15800 exact cuttings of 24 pieces. Exactly 192 pieces
occur, and they form exactly 192 eight-piece covers.

The group `G` consists of every coordinate permutation followed by independent
coordinate flips. It has 384 distinct maps and is checked under all 147456
products. The induced actions are transitive on both the 192 pieces and the 192
covers. There are 104 orbits on ordered piece pairs, 120 on ordered cover pairs,
and 96 on cover-piece cells. Exact rational elimination gives cutting-table rank
88 with kernel 104 and cover-table rank 105 with kernel 87.

## Imports and provenance

- Measured, fitted, observational, and literature inputs: none.
- Declared mathematical construction choices: the unit four-cube, determinant
  magnitude one, adjacency cost 6, the exact interior sample grid, the full
  384-map coordinate-permutation/flip action, and prime 1000003. These choices
  define the finite theorem's scope.
- Arithmetic implementation: Python integers and `Fraction` supply exact
  rational work; NumPy stores integer and finite-field arrays. Floating-point
  wall time appears solely in the final resource-envelope gate.
- Algebraic facts used: Maschke splitting, Schur's lemma, the Wedderburn form of
  a finite-dimensional semisimple algebra, and rank under reduction modulo a
  prime. Their roles and proof reductions are stated below rather than treated
  as framework premises.

Framework axiom and primitive premise count: zero.

## Exact target and obligation graph

Let `P = Q^192` have one basis vector per piece and `C = Q^192` one basis vector
per cover. A cover-by-piece matrix `B` defines the piece-to-cover map

    T_B : P -> C,       (T_B x)_c = sum_p B[c,p] x_p.

The target is the maximum rank, and hence minimum domain-kernel dimension, over
all rational `G`-intertwiners `P -> C`. The obligations are:

1. **O1, finite object:** enumerate genuine pieces, cuttings, and covers. Proved
   by the determinant, generic-grid, exact-interior-disjointness, exact-cover,
   Gram-reconstruction, and entrywise-kernel controls bound into C0 and C3.
2. **O2, actions:** prove the 384 maps act bijectively on both permutation sets
   and preserve the incidence objects. Proved by exhaustive closure, stability,
   orbit, Burnside, and label-invariance controls in C1 and C2.
3. **O3, central decomposition:** prove that `End_G(P)` has dimension 104, its
   centre has dimension 20, and one central element separates twenty primitive
   rational parts. Proved by C2 and C4-C7.
4. **O4, field bridge:** establish that the modular component ranks equal their
   rational counterparts. Proved by the one-sided rank lemma, global saturation
   identities, and the prime/noncollision controls in C3 and C7-C10.
5. **O5, intertwiner bound:** derive the rank formula over the possible rational
   division endomorphism rings. Proved in the next two sections.
6. **O6, totals:** sum the component bounds to 144 and 48. Proved by C8-C12.
7. **O7, attainability:** exhibit a `G`-intertwining integer matrix of exact
   rational rank 144. Proved by the orbit-matrix controls and C13.

All seven obligations close for the stated finite target. Physical-law,
proper-cubic-only, and multi-cell targets are separate open questions.

## Twenty rational parts and the field bridge

The 104 orbit matrices form a basis of `A = End_G(P)`. Its centre is the kernel
of the 10816 equations imposing commutation with all basis elements. A modular
row selection finds 84 independent equations; exact rational elimination on
those rows also has rank 84. The resulting twenty integer kernel vectors are
then checked against all 10816 equations in both multiplication orders. Thus
`dim_Q Z(A) = 20`.

One integer central element has twenty distinct integer eigenvalues. The exact
row-sum bound is 6009, the successful deterministic trial is 2, and every
eigenvalue has nullity one in the centre multiplication matrix. Three products
on the full 192-square bind that abstract multiplication matrix to its action on
`P`.

The modular bridge uses `p = 1000003`. C7 checks that `p` is prime, is coprime to
`|G| = 384`, exceeds twice the row-sum eigenvalue bound, and leaves the twenty
integer eigenvalues pairwise distinct. For any integer matrix, a nonzero minor
modulo `p` is the reduction of a nonzero integer minor, so

    rank over F_p <= rank over Q,
    nullity over F_p >= nullity over Q.

The twenty modular eigenspaces therefore give one-sided component bounds. Their
dimensions sum to the independently fixed total 192. The ranks of the restricted
piece centralizer and piece-to-cover intertwiner spans sum to the independent
orbit totals 104 and 96. The cover-side squares and dimensions sum to the
independent totals 120 and 192, and the component blind dimensions sum to the
exact rational total 87. Equality at every global total forces equality in every
one-sided component bound. This is the mod-`p`-to-`Q` saturation step; it is why
the following component data are rationally exact.

The twenty part dimensions are

    1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 8, 8, 8, 8, 12, 12, 24, 24, 32, 32.

For each part the runner records a degree `d`, a piece multiplicity `m`, and a
cover multiplicity `mc`. Six independently anchored sums are

    sum of dimensions      192
    sum of m squared       104
    sum of m times mc       96
    sum of mc squared      120
    sum of d times mc      192
    sum of blind            87.

## Rational semisimple rank lemma

Because 384 is invertible in `Q`, averaging any linear projection onto a
`G`-submodule over all `g in G` gives a `G`-equivariant projection. Its kernel is
an invariant complement. Repeating this proves that `P` and `C` are semisimple.

Let `W_i` be the rational irreducible represented by central part `i`, and set
`D_i = End_G(W_i)`. Schur's lemma makes `D_i` a division algebra. For the central
element `z`, the Lagrange polynomials

    e_i = product over j != i of (z - lambda_j)/(lambda_i - lambda_j)

are twenty nonzero orthogonal central idempotents summing to one. Since the whole
centre has dimension twenty, each `e_i Z(A)` is one-dimensional. Hence every
`e_i` is primitive and the centre of each `D_i` is `Q`.

For completeness, the finite-dimensional central-division-algebra step is used
in its dimension form. After a finite splitting extension `L/Q`, a central
division algebra becomes `M_s(L)`; scalar extension preserves dimension, giving
`dim_Q D_i = s_i^2`. This is the sole Schur-index factor retained in the proof.
Write

    P_i = W_i^(n_i),       C_i = W_i^(q_i),
    m_i = n_i s_i,         mc_i = q_i s_i,
    d_i = dim_Q(W_i)/s_i.

Then `End_G(P_i)` has rational dimension `m_i^2`, while
`Hom_G(P_i,C_i)` has dimension `m_i mc_i`; these are exactly the modularly
recovered integers above. A `G`-map on part `i` is a `q_i by n_i` matrix over
`D_i`. Its rank as a `D_i`-linear map is at most `min(n_i,q_i)`, so its rational
rank is at most

    min(n_i,q_i) dim_Q(W_i) = d_i min(m_i,mc_i).

This argument includes nonsplit rational division algebras and uses no silent
absolute-irreducibility assumption.

## The attained ceiling and floor

Summing the component lemma gives every rational `G`-intertwiner `P -> C`

    rank  at most   sum_i d_i min(m_i, mc_i)      = 144,
    blind at least  sum_i d_i max(0, m_i - mc_i) =  48.

The runner forms an integer linear combination of all 96 cover-piece orbit
matrices. Each orbit matrix is checked to intertwine the two actions, and exact
rational elimination gives the combination rank 144. The ceiling and floor are
therefore attained.

For the incidence map, rank 105 and blind dimension 87 place 39 dimensions
inside both extremal values. Twelve parts attain their component floor. The
other eight, listed as `d/m/mc/blind/floor`, are

    2/2/2/2/0    4/2/3/4/0    6/2/3/6/0    8/4/6/8/0
    6/4/3/12/6   6/2/3/6/0    6/4/3/12/6   1/1/1/1/0.

Their component deficits are 2, 4, 6, 8, 6, 6, 6, and 1, summing to 39. Six of
the eight have `mc >= m`; two have `mc < m`. These are exact properties of the
eight component matrices.

## Three exact label comparisons

The even-coordinate-permutation subgroup has order 192 and splits both pieces
and covers into classes of 96 and 96. The associated plus/minus piece vector is
the `d=m=mc=1` part. Every cover contains four pieces from each class, so all 192
cover sums are zero. Dually, each piece lies in four covers from each cover
class, with incidence totals 768 and 768.

For the unique nonidentity full-group element fixing cover zero, the action on
its eight pieces has four 2-cycles and preserves the class label. Its coordinate
permutation sign is 1, its flip-count parity is -1, and their product is -1.

The aggregate class-count identity is fixed for every split value `a` from 0 to
8:

    96 a + 96 (8 - a) = 768,       768 / 192 = 4.

Two geometric labels provide further exact comparisons. Corner parity and the
ordered determinant each agree with the class label on exactly 96 of 192 pieces.
Keeping image corners in source order, the determinant character identity holds
on all 73728 element-piece pairs. Sorting every image piece into its own order
gives 36864 differing pairs, with equality for 4 of the 384 group elements.

These three items are reported as finite observations. Their role is comparison,
rather than explanatory assignment or route pruning.

## Runner and reproducibility

`physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py` declares
`AUDIT_TIMEOUT_SEC = 400` and emits 28 gates followed by
`TOTAL: PASS=28 FAIL=0`. C0-C26 use exact integer, rational, or finite-field
arithmetic. C27 separately checks environment-dependent wall time against the
declared timeout and peak resident memory against 2500 MB. Any failed gate makes
the process exit nonzero.

The runner binds the object, action, orbit, centre, field, component-table, exact
value, witness, label-comparison, source-hygiene, and resource controls directly
into the 28 gate predicates. The canonical cache is keyed to the final runner
SHA and its declared timeout.

## Boundary

The theorem's hypothesis is equivariance under the full 384-map symmetry of the
four-cube. Proper-cubic equivariance defines a broader map class with a separate
rank bound. `MINIMAL_AXIOMS_2026-06-29.md` is named here solely as a non-load-
bearing scope marker, so it intentionally creates no citation-graph dependency.

The result is a finite rational representation theorem. Physical-law and
multi-cell interpretations remain open. The decomposition assigns the 39-unit
rank deficit to eight exact component matrices; identifying additional structure
inside those matrices is the next finite question.

The two identities `ceiling + floor = 192` and
`ceiling - rank = blind - floor` are algebraic bookkeeping. The load-bearing
content is the exact component decomposition, the universal intertwiner bound,
and the rank-144 attaining witness. The central-element and witness coefficients
are deterministic construction choices whose certified role is genericity.
