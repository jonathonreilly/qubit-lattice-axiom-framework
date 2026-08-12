# Physical cell cutting: fixed-point cover and piece censuses cross in the centre

Date: 2026-08-11
Authority: none
Audit: unset
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: test whether the finite fixed-point/census mechanism has a canonical downstream consumer; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite group-action and incidence identities for the declared unit four-cube object; no broader physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object consists of the 16 vertices of the unit four-cube, the
five-vertex determinant-one simplices at the adjacency-cost minimum, the cuttings formed from
those simplices, and the 384 signed coordinate maps of the cell. These are finite-scope object
choices, not imported physical primitives. The integer counts below are derived by the linked
runner. The two named primes are used only for the diagnostic in section 8.

There are no load-bearing literature, empirical, fitted, external-data, or repository-derived
scientific inputs. NumPy is an implementation dependency and supplies no scientific value.
The runner rebuilds the object from the corners and performs every load-bearing check using
integer arithmetic.

The exact target is to derive the cover and piece census sizes from a finite transitive-action
fixed-point formula and identify their intersection for this object. The proof obligations are:

1. certify that the enumerated 24-simplex selections tile the cell;
2. certify the two transitive actions and their order-two point stabilizers;
3. prove the fixed-point/normalizer formula at the stated finite scope;
4. identify the brute-force row and column censuses with the corresponding equivariant
   relabellings as exact sets; and
5. count and identify the incidence-intertwining pairs.

Each obligation is discharged below and by a named hard gate in the runner. This note makes no
claim about arbitrary cell-cutting systems, physical dynamics, or a lattice-wide construction.

## 1. The exact finite object

The cell has 2672 five-corner unit-determinant subsets, 400 at adjacency-cost floor 6, and
15800 selected 24-piece cuttings. Exactly 192 pieces occur, each in 1975 cuttings, filling
379200 slots. Those pieces carry 192 eight-piece covers. The 384 signed coordinate maps act
freely on the 36864 piece-cover pairs, giving 96 pairwise-disjoint orbit tables whose sum is
the all-ones table. Any four tables therefore form a zero-one matrix, giving a family of
3321960 members. The cover incidence is one member.

The sample lattice used to enumerate candidate cuttings avoids every candidate facet. Gate H25
then supplies an independent exact tiling certificate: all 15168 simplex pairs that co-occur in
a selected cutting are weakly separated by one of the 80 nonzero normals in
`{-1,0,1}^4`. Because every simplex is full-dimensional, its interior is strictly on one side
of such a separator. The 24 determinant-one simplex volumes sum to the unit four-cube volume.
Thus the selected sets are genuine cuttings, while the generic sample makes the enumeration
exhaustive within the declared candidate class.

## 2. Finite fixed-point formula

**Theorem.** Let a finite group `G` act transitively on a finite set `X`, and suppose every
point stabilizer has order 2. Fix `x in X` and write `H = Stab_G(x) = {1,g}`, with `g` the
non-identity element. Then

`|Aut_G(X)| = |Fix_X(g)|`.

**Proof.** Identify `X` with `G/H`. Equivariant bijections of `G/H` are indexed by
`N_G(H)/H`. Since `H={1,g}`, an element normalizes `H` exactly when it centralizes `g`, so

`|Aut_G(X)| = |C_G(g)|/2`.

Every point stabilizer contains one non-identity element, and transitivity makes those elements
conjugate to `g`. Double-counting pairs `(y,k)` with `k` in the conjugacy class of `g` and
`ky=y` gives

`|Cl_G(g)| |Fix_X(g)| = |X| = |G|/2`.

Using `|Cl_G(g)|=|G|/|C_G(g)|` yields
`|Fix_X(g)|=|C_G(g)|/2`, proving the formula. QED.

For covers, the class size is 4 and the fixed count is 48; the centralizer/normalizer has size
96, so its index over the stabilizer is 48. For pieces, the class size is 12 and the fixed
count is 16; the centralizer/normalizer has size 32, so its index is 16.

## 3. Cover and piece actions are inequivalent

The cover stabilizer generator is a single-axis flip in the normal 16-element flip subgroup.
The piece stabilizer generator lies outside that subgroup, so the generators are not conjugate.
The first fixes 0 pieces and the second fixes 0 covers. The two transitive `G`-sets therefore
have nonconjugate stabilizers and are inequivalent. Their equivariant automorphism groups have
the distinct sizes 48 and 16 derived in section 2.

## 4. Exact row and column censuses

The centralizer of the piece stabilizer has 32 maps and yields 16 piece relabellings. Each is a
bijection of the 192 pieces commuting with the group action, checked on 1179648 comparisons
with 0 misses; the relabellings contain the identity and are closed under composition. Their
incidence images equal the 16-member brute-force column census, with symmetric difference 0.

The analogous 48 cover relabellings give incidence images equal to the 48-member brute-force
row census, again with symmetric difference 0. The two census sizes are therefore the two
fixed-point counts, rather than unexplained search counts.

## 5. The crossing is an automorphism count

A member in both censuses supplies a cover relabelling and a piece relabelling that intertwine
the incidence. Testing all `48 * 16 = 768` pairs gives exactly 2 intertwining pairs. Reading
their four table labels gives exactly the two brute-force crossing members, with symmetric
difference 0. Both components are cell maps in the centre, which has size 2, and the two cover
components contain the identity and are closed under composition.

## 6. Independent finite conditions

The row condition leaves 48 members and the column condition leaves 16. Of these, 46 satisfy
only the row condition and 14 satisfy only the column condition; their intersection has size 2.
The incidence has 192 distinct rows and 192 distinct columns, so each member determines its row
and column map. The exact ladder is therefore `3321960 -> 48`, `3321960 -> 16`, and
`48 intersection 16 -> 2`.

The two crossing members form one orbit under the declared non-identity central relabelling:
that map carries the first member to the second entry by entry and carries its four tables to
the other four tables. This is a positive equivalence statement for the finite object; no
finer canonical selection is claimed.

## 7. Finite controls

- The cycle-773 twin, table set `4/5/6/7`, occurs in neither census.
- Swapping any subset of the four central partner tables produces 16 variants; exactly 2 occur
  in the row census and exactly 2 in the column census.
- Of the 352 maps outside the piece-stabilizer centralizer, 0 identify two different coset
  representatives as the same piece map.
- The cover-holder generators close to the 16-element flip subgroup. By comparison, 371 maps
  fix 0 pieces; restricting those to involutions leaves 63, and adjoining the identity yields
  a 64-element set that is not closed under multiplication. These are exact control counts,
  not route-closure claims.

## 8. Block-rank profile at two fixed primes

The incidence has the block-rank profile `9/9/6/6/0` over the sixteen sign patterns, constant
inside each pattern-weight class. Every one of the 16 column-census members has the same tested
profile triple at primes 1000003 and 1000033. At each prime the sixteen block ranks recompose
to 105, equal to the directly measured incidence rank. This establishes constancy of this
specific diagnostic on this census at the two named primes; it makes no statement about other
rank constructions or invariants.

The two crossing matrices each have rank 105 at the first prime. Their sum has row sums 16,
rather than the individual row sums 8, and therefore lies outside the declared family. This is
only a finite control on the two returned matrices.

## 9. Reproduction

Run
[physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.py](../scripts/physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.py).
The reviewed cached output is
[physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.txt](../logs/runner-cache/physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.txt).
The runner declares `AUDIT_TIMEOUT_SEC = 300`, typically completes in under a minute, and stays
well under one gigabyte.

## 10. Review record and boundary

- Review iteration 1 (Sol, 2026-08-11) required finite theorem hypotheses, an exact
  simplex-separation/tiling certificate, exact row-census set equality, fail-closed runner exit,
  and explicit status/import/proof contracts.
- Review narrowed the rank and naming discussion to the positive finite equalities and bounded
  diagnostics actually established here.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent audit remains required before any effective retained status or downstream use.

Within those boundaries, the appropriate review classification is **bounded support** for the
declared exact finite object.
