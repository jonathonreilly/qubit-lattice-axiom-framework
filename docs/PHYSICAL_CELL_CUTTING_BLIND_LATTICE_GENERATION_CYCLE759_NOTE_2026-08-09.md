# Finite cutting-kernel integer-lattice and quotient identities — Cycle 759

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [finite rebuild-and-gate runner](../scripts/physical_cell_cutting_blind_lattice_generation_cycle759_2026_08_09.py)

Direct scientific dependencies: none. The runner reconstructs its finite
labelled object from the unit-four-cube coordinates and rules declared in the
source.

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "No downstream framework claim is identified; this packet records finite integer-lattice identities only."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "independent audit of the finite reconstruction, integer arithmetic, and stated boundary"
conditional_surface_status: "bounded to the explicitly reconstructed labelled unit-four-cube incidence object"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "an exhaustive theorem on one finite incidence object, with zero physical or multicell extension"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

For the finite `15,800 x 192` cutting-by-piece incidence matrix `A` and the
`192 x 192` exact-cover matrix `M` reconstructed by the runner, certify these
identities:

1. `A` has rank 88, `M` has rank 105, and each rank is unchanged over every
   field.
2. The 384 support-eight differences between cover pairs sharing four pieces
   generate the integer kernel `K = ker_Z(A)`. The 191 differences from one
   fixed cover also generate `K`; each family contains a 104-row
   determinant-one basis.
3. The row lattice `L = row_Z(A)` has rank 88, `K` has rank 104, and the
   finite quotient `Z^192/(L + K)` has index
   `2^114 x 3 x 5^30`.
4. Two independently certified basis pairs give that same index through the
   stacked determinant and both Gram determinants.
5. The quotient has nontrivial invariant factors

   | order | 2 | 10 | 20 | 40 | 80 | 160 | 320 | 960 |
   |---|---:|---:|---:|---:|---:|---:|---:|---:|
   | multiplicity | 12 | 8 | 2 | 2 | 8 | 8 | 1 | 1 |

   and therefore has 42 nontrivial cyclic factors and exponent 960.

These are finite combinatorial and integer-linear-algebra statements. They
carry zero framework-premise weight and zero physical interpretation.

## Inputs and primitive-registry result

The external scientific-input surface is empty. The 16 labelled coordinates,
adjacency cost, simplex enumeration, exact-cover rule, and group action are
declared inside the runner. Python and NumPy are computational machinery.

The primitive-registry check is **not applicable** to this proof surface: no
registered axiom or primitive is consumed, modified, or proposed. This note
creates no dependency edge to a framework axiom document.

## Finite reconstruction

The runner enumerates all 4,368 five-corner subsets of the labelled unit
four-cube and obtains 2,672 unit normalized-volume simplices. It independently
gates the rounded inverse matrices on both sides over the integers, the exact
orientation sign of every spatial action, the cost floor 6, the 2,736 sample
points, zero label collisions, zero boundary samples, completed cutting size
24, action sizes 24 and 48, and the action-induced row/column permutations.

The resulting object has:

| finite quantity | exact value |
|---|---:|
| minimum-cost cuttings | 15,800 |
| supported pieces | 192 |
| pieces per cutting | 24 |
| cuttings through each supported piece | 1,975 |
| eight-piece exact covers | 192 |

Every exact cover meets every cutting once. The cover matrix is binary and
8-regular on both sides (C0-C2).

## Sharing and support-eight differences

For every cover, the rowwise sharing profile with the other 191 covers is:

| shared pieces | 0 | 1 | 2 | 4 |
|---|---:|---:|---:|---:|
| other covers | 157 | 20 | 10 | 4 |

The runner gates each row's profile and the complete off-diagonal multiset
(C3). Two eight-piece covers sharing `s` pieces have difference support
`2(8-s)`. Exhaustion of all cover pairs gives maximum sharing four, hence
minimum nonzero support eight within this pairwise-difference family. There
are 384 such four-for-four differences, all with entries in `{-1,0,1}`.
Because every cover meets every cutting once, `A` sends every such difference
to zero (C4-C5).

## Integer generation proof

For an integer matrix of rank `r`, a single `r x r` minor of absolute value
one makes its row lattice saturated: the product of its Smith invariant
factors divides that unit minor and is therefore one. The runner finds two
such minors, using forward and reverse column orders, for each load-bearing
row family.

Exact fraction-free elimination gives

`rank(A) = 88`, `rank(M) = 105`, and `rank(D) = 104`,

where `D` contains all 384 support-eight differences. Since `A D^T = 0` and
`88 + 104 = 192`, `row_Q(D) = ker_Q(A)`. The integer kernel `K` is saturated,
and the determinant-one minor makes `row_Z(D)` saturated in the same rational
subspace. Thus both equal `Z^192 intersect ker_Q(A)`, proving
`row_Z(D) = K`. The identical rank-and-saturation argument applies to the 191
fixed-cover differences (C6-C10).

The determinant-one minors of `A` and `M` also keep their ranks at 88 and 105
over every prime field. The runner checks thirteen primes directly with one
vectorized routine, reproduces the cover rank with an independent scalar
routine, and exercises a diagonal control whose rank varies with the prime
(C11-C12).

## Certified bases, index, and finite quotient

For each of forward and reverse column order, the runner selects 88 rows of
`A` and 104 rows of `D`. It computes the selected minors over the integers and
requires all four certificates to have absolute determinant one. Each
selected row set is therefore a genuine integer basis of `L` or `K`, rather
than only a basis after reduction modulo one prime.

Let `B_L` and `B_K` denote either certified pair. The runner computes

- `abs(det([B_L; B_K]))`,
- `det(B_L B_L^T)`, and
- `det(B_K B_K^T)`.

All three equal

`2^114 x 3 x 5^30`,

and the forward and reverse pairs agree (C13). The stacked determinant is the
index of `L + K` in `Z^192`; the Gram determinants are independent exact
cross-checks for the primitive orthogonal-complement pair.

For completeness, the group interpretation is elementary. Orthogonal
projection sends an integral vector `z` to a class in `L#/L`, where `L#` is
the dual lattice. Its kernel is `L + K`: if the projection lies in `L`, the
remaining integral vector lies in the primitive complement `K`. Surjectivity
follows because primitivity of `L` makes restriction
`Hom(Z^192,Z) -> Hom(L,Z)` surjective. Hence

`Z^192/(L+K) ~= L#/L`,

and the same argument gives `Z^192/(L+K) ~= K#/K`. Therefore the stacked
matrix and the two Gram matrices are three presentations of the same finite
group. The runner computes their Smith forms directly and gates equality of
the nontrivial invariant factors listed in the target. Their product matches
the independently computed index, their divisibility chain is exact, and the
largest factor gives exponent 960 (C14-C15).

Fixed examples exercise the exact determinant, unit-minor, Smith, and index
routines on singular, nonsaturated, and non-diagonal-Smith cases (C11,
C16-C17). C18 binds elapsed time to the declared 300-second cache timeout and
normalizes peak-memory units by platform.

## Proof-obligation ledger

| obligation | discharge | runner gates |
|---|---|---|
| reconstruct the intended finite object | exact inverse/action checks, exhaustive counts, incidence degrees | C0-C2 |
| prove the universal cover-sharing profile | rowwise counts plus complete multiset | C3 |
| place the 384 differences in the integer kernel | exhaustive sharing/support census and exact zero image | C4-C5 |
| prove both proposed families generate `K` | exact ranks plus unit-minor saturation witnesses | C6-C10 |
| certify characteristic-independent ranks | determinant-one minors, independent modular checks, varying control | C7-C8, C11-C12 |
| use genuine integer bases for the index | four explicit unit-minor certificates and two basis pairs | C13 |
| identify the finite quotient | three Smith presentations, order and exponent checks | C14-C16 |
| exercise index and resource logic | hand-computed index-two control; timeout/RSS gate | C17-C18 |

## Machine evidence and boundary

The primary runner is self-contained and emits 19 contiguous gates followed
by `TOTAL: PASS=19 FAIL=0`. Its canonical cache is generated through the
repository runner-cache tool. The scientific boundary is:

- support-eight minimality concerns only nonzero pairwise differences of the
  192 enumerated covers;
- the generation theorem concerns integer combinations, with coefficient
  length, positivity, and optimization outside scope;
- the quotient calculation concerns this one labelled finite incidence
  object, with physical, multicell, probabilistic, and continuum
  interpretation outside scope;
- the equality `960 = 5 x 192` and the repeated multiplicity eight are
  numerical consequences here, with structural explanations outside scope.

Independent audit remains required before any retained-grade effect.

## Review record

Review narrowed the original negative splitting rhetoric to the positive
finite quotient/index/exponent identities, removed predecessor and axiom
rhetoric, replaced modulo-prime row selections with unit-minor-certified
integer bases, strengthened reconstruction and row-regularity gates, aligned
the resource contract, and retained only canonical discoverability and cache
surfaces. This record is review provenance, not an audit verdict.
