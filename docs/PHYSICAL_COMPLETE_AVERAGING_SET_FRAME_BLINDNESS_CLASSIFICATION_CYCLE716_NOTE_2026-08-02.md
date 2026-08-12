# Finite Classification of Frame-Blind Averaging Sets for the Reassembled Static Operator — Cycle 716

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane. This
note changes no axiom, approved primitive, premise registry, policy, queue, or
audit-status surface.

Primary runner:
`scripts/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.py`;
cached stdout:
`logs/runner-cache/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.txt`;
paired receipt:
`outputs/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02_receipt_2026-08-02.json`.

This note contains two distinct finite results. Exact finite group arithmetic,
conditional on the stabilizer sextet measured from the supplied Cycle-696
compiler, identifies a 231-member sufficient family of averaging sets. Four
complete numerical scans — two declared seeded standard-normal inputs at each
of `L = 3, 4` — find exactly that family among all 16777215 nonempty frame
collections. The second statement is about those four inputs; it is not a
generic-source theorem.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "characterize the exceptional source varieties on which additional frame-blind averaging sets occur"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "solve the finite quadratic equalities in source space rather than extrapolating from seeded probes"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Exact finite group classification conditional on the measured sextet, plus complete powerset counts at four declared seeded inputs on L in {3,4}."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the group layer is exhaustive on the 24 rotations, while the response converse is measured only at four finite source vectors and two box sizes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied setting and domain

The [Cycle-696 open-coframe compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
assembles the unwrapped static Hessian `Q(L)`. The 24 proper cubic rotations act
on its degree-of-freedom index by permutation matrices `P_a`; the reassembled
operator in frame `g` is `Q_g = P_g Q P_g^T`. The measured sizes are `n = 98`
at `L = 3` and `n = 279` at `L = 4`.

For a nonempty averaging set `A` and supplied vector `b`, define

    b_A = sum_{a in A} P_a^T b,
    v_A(g) = (b_A / ||b_A||)^T Q_g^{-1} (b_A / ||b_A||).

The normalized response is defined only where `||b_A|| > 0`. The runner returns
`NaN`, a non-passing value, when the average vanishes; such a collection enters
neither the blind nor non-blind population. A hostile witness `b = e_0 - e_35`
with `A` equal to the full group has zero averaged norm at `L = 3` and gates this
domain behavior.

The zero-defect set is recomputed from the compiled operators at tolerance
`1.0e-09` and is measured as

    S = {1, 4, 9, 15, 18, 23}.

Its order-six subgroup and right-coset role are inherited from the finite
[Cycle-714 operator/source pairing result](PHYSICAL_ASSEMBLY_DEFECT_ISOSPECTRALITY_AND_SOURCE_PAIRING_CYCLE714_NOTE_2026-08-02.md)
and the [Cycle-715 finite group complement result](PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md).
Cycle 715's exact finite complement/right-coset arithmetic and covering-subgroup
sufficiency are conditional on a numerical near-zero-defect sextet at
`L in {3,4}`; it does not supply universal necessity. The present runner
recomputes the sextet, group table, and subgroup lattice.

## Imported inputs and proof obligation

The exact target proved here is: conditional on the supplied finite compiler
action and its measured sextet `S` at `L in {3,4}`, every nonempty frame set
whose left stabilizer covers with `S` has a frame-constant normalized quadratic
response for every supplied vector with nonzero averaged norm; separately, the
four declared seeded vectors select exactly that sufficient family in complete
finite powerset scans.

The obligation graph is:

1. **Compiler action and sextet.** The open-box Hessian, 24 frame matrices,
   degree-of-freedom relabelling, and finite-difference operator values are
   imported from the linked Cycle-696 script. Their static-sector physical
   interpretation and numerical precision are supplied support, not derived in
   this note. The sextet is remeasured at both sizes and gated numerically.
2. **Finite group layer.** The anti-homomorphism, 30-subgroup lattice,
   complement orders, right cosets, left stabilizers, and 231-member family are
   recomputed and proved by exhaustive finite arithmetic in the primary runner.
3. **Sufficiency lemma.** Stabilizer invariance of `b_A` and sextet invariance
   of `Q` imply response constancy when `S L(A)` covers the group. This is proved
   below with the nonzero-average hypothesis preserved.
4. **Seeded-scan agreement.** The four finite powerset scans, population gap,
   size census, and all-24 acceptance retests are numerical results produced by
   the primary runner. They establish no source-space quantifier.

The `1.0e-09` sextet threshold, `1.0e-08` response threshold, NumPy arithmetic,
and seeded standard-normal vectors are declared numerical conventions/probes;
they are not approved primitives or physical observations. The strongest
missing lemma is an exact characterization of the quadratic exceptional sets
in source space on which collections outside the covering family become
frame-blind. That problem remains a frontier question and is not needed for the
bounded target above.

## Derived sufficiency on the nonzero-average domain

Let `L(A) = {t : tA = A}` be the left stabilizer of `A`. This is a subgroup,
and `A` is a union of its right cosets. Because the relabelling reverses
products, `P_a P_b = P_{ba}`, one has
`P_t^T b_A = b_{tA} = b_A` for every `t` in `L(A)`.

If `S L(A)` fills all 24 rotations, write any frame as `g = s t` with `s` in
`S` and `t` in `L(A)`. The `t` factor fixes `b_A`, while `s` fixes `Q` and its
inverse. Therefore `v_A(g) = v_A(e)`. This proves sufficiency for every supplied
`b` for which the normalized response is defined.

The runner constructs every subgroup of the finite rotation group without a
generating-rank assumption. Nine subgroups cover with `S`, of orders
`4, 4, 4, 4, 8, 8, 8, 12, 24`. The four order-four covering subgroups are
complements of `S`. Unions of their right cosets, equivalently sets whose left
stabilizer covers with `S`, form a family of 231 collections with size census

| size | 4 | 8 | 12 | 16 | 20 | 24 |
|---|---:|---:|---:|---:|---:|---:|
| family count | 24 | 51 | 80 | 51 | 24 | 1 |

The family has 24 size-four members. Every family member is a union of those
members, but arbitrary unions need not stay in the family: 108 of the 168
disjoint pairs have a union outside it, and 108 of all 276 pairs overlap. The
size-four minimum is a property of this covering-criterion family: the order of
`L(A)` divides `|A|`, and a covering stabilizer has order at least four.

Across all 231 family members and five supplied inputs — two seeded normals,
two single-slot vectors, and the all-ones vector — the worst all-24 spread is
`7.0e-12` at `L = 3` and `1.6e-10` at `L = 4`; the smallest averaging norm is
`2.0e+00`.

## Complete finite scans at four seeded inputs

For each box, the runner instantiates NumPy's `default_rng(base_seed + L)` and
draws a standard-normal vector. Thus the four scans use base seeds 7160 and
7161, with actual RNG seeds 7163 and 7164 at `L = 3`, and 7164 and 7165 at
`L = 4`. Reuse of an integer seed across different vector dimensions does not
identify the vectors.

All 16777215 nonempty collections are scanned in each case:

| box | base seed | classified blind | family match | worst blind | best non-blind | ratio | minimum norm | degenerate |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| `L = 3` | 7160 | 231 | yes | `5.8e-12` | `6.8e-06` | `1.2e+06` | `1.1e+01` | 0 |
| `L = 3` | 7161 | 231 | yes | `7.0e-12` | `4.7e-05` | `6.6e+06` | `9.7e+00` | 0 |
| `L = 4` | 7160 | 231 | yes | `1.6e-10` | `6.6e-05` | `4.2e+05` | `1.6e+01` | 0 |
| `L = 4` | 7161 | 231 | yes | `1.1e-10` | `3.4e-04` | `3.1e+06` | `1.6e+01` | 0 |

At each of these four vectors, the six-size census is exactly the group-family
census above, with count zero on the other eighteen sizes. The gap between the
two numerical populations is at least five orders of magnitude at the declared
`1.0e-08` classification tolerance.

The full scan uses four right-coset representatives as a monotone screen, not
as an assumed equality. Those four representatives are frames, so their spread
cannot exceed the all-24 spread: a screen rejection is conclusive and only
acceptance can require more work. Every one of the 231 screen acceptances in
each scan is re-evaluated on all 24 frames. A separate bounded consistency
sample compares four- and 24-frame spreads over all 2324 collections of size at
most three; its worst differences are `6.2e-12` and `3.0e-10` at `L = 3, 4`.
The sample is not used to authorize the screen.

## Finite source-dependence witnesses

The first seeded input supplies three named spread witnesses. At `L = 3` and
`L = 4`, respectively, the sextet spreads by `2.0e-02` and `1.4e+00`; the
four-set `{1,4,9,23}` spreads by `3.3e-02` and `1.1e+00`; and the least spread
among 72 right cosets of the three noncovering order-four subgroups is
`5.4e-03` and `2.3e-01`.

Other supplied vectors exhibit additional blind sets. Over the 1271625
collections of size at most eight at `L = 3`, the covering family contributes
75 sets, while the slot-0 unit vector has 153 blind sets, the slot-7 unit vector
has 723 (including 24 of size two), and the all-ones vector has a one-point
frame orbit and 1271625 blind sets. These are positive existence witnesses for
source dependence. They delimit the four seeded counts and the size-four
family minimum; they do not define a universal source class.

## Claim boundary and physics reading

The durable result is an exhaustive finite group classification conditional on
the measured sextet, an analytic sufficiency implication on the nonzero-average
domain, and four complete finite response scans at `L = 3, 4`. The supplied
compiler, its open boundary, its static spatial-sector interpretation, its
finite-difference residuals, the `1.0e-08` response tolerance, and the four
source vectors are explicit premises.

No arbitrary-`L`, wrapped-boundary, continuum, source-measure, or physical
averaging prescription is selected here. In particular, four seeded vectors do
not establish a generic-source converse or identify the exceptional algebraic
source sets. What the finite data do show is that the coset-aligned family
saturates the blindness census at four widely separated numerical probes, while
structured vectors can enlarge it substantially.

## Runner and evidence

The primary runner declares `AUDIT_INPUT_PATHS` for the Cycle-696 compiler and
its four transitive script imports and declares `AUDIT_TIMEOUT_SEC = 900`. It
recomputes the 24-frame group law, measured sextet, complete 30-subgroup lattice,
covering family, full-powerset stabilizers, four complete source scans, all-24
acceptance retests, finite witnesses, and zero-average domain rejector. It ends
with `TOTAL: PASS=55 FAIL=0` and writes the paired JSON receipt. The canonical
cache is produced through `scripts/runner_cache.py`, so its header binds both
runner bytes and the declared compiler-source fingerprint.

## Load-bearing dependencies

- [Cycle 714](PHYSICAL_ASSEMBLY_DEFECT_ISOSPECTRALITY_AND_SOURCE_PAIRING_CYCLE714_NOTE_2026-08-02.md)
  supplies the finite operator/source pairing and four-right-coset collapse this
  cycle extends from subgroups to arbitrary sets.
- [Cycle 715](PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md)
  supplies the exact finite complement/right-coset factorization and
  covering-subgroup sufficiency, conditional on its numerical near-zero-defect
  sextet at `L in {3,4}`. The present cycle extends that sufficient construction
  through arbitrary-set left stabilizers; it does not import necessity.
- The linked Cycle-696 script supplies the executable compiler contract and its
  24-frame table; it is a support surface, not audit authority.

## Review record

Review withdrew the submitted universal converse and the phrase “generic
source”: two seeded draws per box do not prove a statement on source space, and
structured vectors in the same runner furnish counterexamples to universal
minimality. Review also made the nonzero-average domain explicit, changed a zero
average from a false pass to `NaN`, replaced a bounded four-frame comparison by
the monotone-screen argument plus all-24 acceptance retests, removed the
generating-rank assumption from subgroup enumeration, disclosed the actual RNG
seed convention, bound cached evidence to the transitive compiler closure, and
added the direct Cycle-714/715 dependency edges. Independent audit remains
required before any effective retained grade.
