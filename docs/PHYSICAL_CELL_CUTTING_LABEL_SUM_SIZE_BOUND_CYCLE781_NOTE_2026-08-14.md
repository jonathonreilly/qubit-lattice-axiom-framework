---
claim_id: physical_cell_cutting_label_sum_size_bound_cycle781_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Exact label-sum identities and the sharp absolute bound eight for the 15,800 geometric cuttings rebuilt from the declared determinant-one, adjacency-cost-floor unit four-cube candidate class; no multi-cell, lattice-wide, dynamical, or framework interpretation."
upstream_dependencies: []
runner: scripts/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.py
---

# Physical cell cutting: the label sum of a cutting is fixed by its positive half-set count, and the size of the label sum is at most eight

Date: 2026-08-14
Authority: none
Audit: unset.
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

Primary runner:
[`scripts/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.py`](../scripts/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.py)

Cached output:
[`logs/runner-cache/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.txt`](../logs/runner-cache/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.txt)

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: identify a downstream consumer for this exact one-cell label bound; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite geometric-tiling, incidence, label, and obstruction identities for one declared unit four-cube candidate class; no broader physical, dynamical, or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs, exact target, and proof obligations

There are no load-bearing literature, empirical, fitted, observational,
framework, or repository-derived scientific inputs. The runner is standalone,
uses the Python standard library only, and performs no repository reads at
runtime; it therefore has no `AUDIT_INPUT_PATHS` declaration. The current axiom
surface and approved-primitive registry supply no premise used in this proof.

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| 16 vertices of `{0,1}^4` | declared finite domain | definition in this note and runner | no framework identification claimed |
| determinant-one five-corner subsets | candidate 4-simplices | rebuilt exactly from the declared vertices | no imported geometry table |
| four-coordinate adjacency cost | candidate selector | explicit definition; its floor is derived | selector is not claimed physically preferred |
| shifts `(1,2,4,8)/80` | generic exact-cover enumeration grid | declared rational construction | sampling alone is not used as a tiling proof |
| axis 3 in the half-set definition | fixed coordinate convention | declared once; no fitted choice | no coordinate is claimed preferred |
| chamber, label, `g1`, and `W` definitions | finite proof objects | defined and checked here | no external normalization or value |
| sibling-cycle names | provenance-only narrative | not on the reviewed main line | no dependency or citation edge |

The exact target is the theorem stated below for every geometric cutting in the
declared candidate class. The proof obligations are to:

1. enumerate that class exhaustively and certify every selected cover as an
   actual geometric tiling without relying on the sampling grid alone;
2. rebuild the same cutting family independently from chamber incidence;
3. establish the per-piece label, halving, and constant-twelve identities;
4. exhaust the possible same-sign nine-piece families and prove that none can
   extend to a cutting; and
5. derive and census the displayed label-sum formula exactly.

The result is a proposed bounded theorem that still requires independent audit.
It does not edit or reinterpret an axiom, approved primitive, retained claim, or
audit verdict.

## What this cycle asks

The unit four-cube cell object is rebuilt from scratch here as in the sibling cycles
`cycle 779` and `cycle 780`: of the 2672 five-corner sets of unit determinant, the ones at
the adjacency cost floor 6 number 400; exact cover of the cell by floor pieces has 15800
solutions, each of 24 pieces; the pieces that actually occur number 192, each in 1975
cuttings; and the naming of a piece by a start corner together with an order of the four
axes gives 384 namings, 2 per piece. A piece carries a handedness label L equal to the sign
of the axis order times the corner weight parity sign of the start corner, and S(T) denotes
the label sum over the 24 pieces of a cutting T.

The shifted grid is an enumeration device, not the geometric proof. It avoids
every candidate facet, so every genuine cutting in the declared 400-piece
candidate class must appear as a sample exact cover. Conversely, the
`geometric_tiling` gate checks all 15168 simplex pairs that co-occur in a
selected cover and finds an exact weak separator among the 80 nonzero normals
in `{-1,0,1}^4` for each pair. The full-dimensional simplex interiors are
therefore disjoint. Each determinant-one simplex has four-volume `1/24`, so the
24 pieces have the cube's full volume; their closed union is the entire cube.
Thus every selected cover is a genuine geometric cutting, and the enumeration
is exhaustive within the declared candidate class.

`cycle 780` identified the covers as the chambers of the twelve-wall cut of the open cell
and derived the mod-four law: S(T) is divisible by 4 on every cutting. It left the size of
S standing as a measurement. Its own boundary section says so plainly: the census puts S in
the five values -8, -4, 0, 4, 8, so |S| is at most 8 over the 15800 cuttings, and nothing in
that derivation forces the bound, since divisibility restricts S to a lattice and not to an
interval.

This cycle derives the bound, pointwise and by a finite obstruction, and the mod-four law
comes back out of it as a corollary. The statement proved is sharper than a bound:

> **T.** Let H be the half set defined below and let p and m be the numbers of pieces of a
> cutting T lying in H with label plus one and minus one. Then p + m = 12, both p and m are
> at most 8, and S(T) = 2 (p - m) = 4 (p - 6). Hence p lies between 4 and 8, S(T) lies in
> -8, -4, 0, 4, 8, and |S(T)| is at most 8.

Three ingredients, each local to one piece and its 8 chambers, and each summed over a
cutting by the partition property rebuilt here: a halving identity, a constant count, and
a sealing obstruction. Every chamber meets every cutting in exactly one piece, with 0
failures over the 15800 cuttings (`chamber_partition`). A second exact-cover search that
uses only chamber incidence reproduces the same set of 15800 cuttings
(`chamber_reconstruction`), independently of the shifted sample masks.

## The halving identity

Fix the naming of a piece. Of its 2 namings, take the one whose start corner v0 is the
smaller of the two opposite corners; write sigma for its axis order. On that minimal naming

> L(P) = sign(sigma) times chi(v0),

where sign(sigma) is the sign of the order as a permutation and chi(v0) is plus one on a
start corner of even weight and minus one on one of odd weight. The 8 start corners of
minimal namings realise both values, and the formula matches the label of the piece on all
192 pieces with 0 mismatches (`minimal_naming`).

Now define the **half set**

> H = the pieces whose minimal naming steps axis 3 within its first 2 steps.

H has 96 members, splitting 48 with L = plus one and 48 with L = minus one (`half_set`). The
choice of axis 3 is a choice of one coordinate, made once and kept; the derivation below
never uses which coordinate was taken, and nothing is claimed here about the other three.

A chamber is named (b, s) as in `cycle 780`, with b the order of the four magnitudes of
u = x - centre taken decreasingly and s = (s1, s2, s3) the signs of u at the first three
slots of b; the sign at the fourth slot is not chamber data. Define a function of the
chamber alone,

> g1(b, s) = sign(b) times s1 times s2 times s3 when b ends in axis 3, and 0 otherwise.

**T1.** g1 takes the value minus one on 24 chambers, 0 on 144 and plus one on 24, so its
total over the 192 chambers is 0; and for every piece P,

> the sum of g1 over the 8 chambers of P equals L(P) when P is outside H, and minus L(P)
> when P is inside H.

Both halves are verified on the rebuilt object with 0 failures over the 192 pieces
(`halving_certificate`).

The identity telescopes. A cutting holds each of the 192 chambers in exactly one of its 24
pieces, so summing the per-piece sums over T sums g1 over every chamber exactly once:

> 0 = sum over the chambers of g1 = sum over P in T of (sum of g1 over the chambers of P)
> = S(T) - 2 S_H(T),

where S_H(T) is the label sum over the pieces of T that lie in H. Hence

> **S(T) = 2 S_H(T) on every cutting**, with 0 failures over the 15800
> (`halving_identity`).

The whole label sum is carried by the half set. That is the first reduction: a sum over 24
pieces becomes twice a sum over the pieces of T inside H, and the next section shows there
are always exactly 12 of those.

## The constant twelve

Define a second function of the chamber alone, this time a set:

> W = the chambers whose order carries axis 3 in its second slot, whose last two slots
> ascend, and whose second sign s2 is plus one.

W has 12 members.

**T2.** For every piece P, the number of members of W among the 8 chambers of P is 1 when P
lies in H and 0 when it does not. Verified on all 192 pieces: 1 on each of the 96 pieces of
H and 0 on each of the other 96, with 0 failures (`witness_set`).

Summing over a cutting with the partition property again, the left side counts each of the
12 members of W exactly once and the right side counts the pieces of T inside H:

> **every cutting holds exactly 12 pieces of H**, with 0 failures over the 15800
> (`constant_twelve`).

So p + m = 12 with p and m the counts of half-set pieces of label plus one and minus one,
and S_H = p - m = 2 p - 12. Combined with the halving identity,

> S(T) = 2 S_H(T) = 2 (p - m) = 4 (p - 6).

At this stage S is a function of the single integer p, which lies between 0 and 12; the
mod-four law is already implied, but the size bound still needs p kept away from the ends.

## The sealed families

Two pieces of one cutting share no chamber: if they did, that chamber would meet the
cutting in more than one piece. So the pieces of T inside H with label plus one form a
pairwise chamber-disjoint family inside the 48 positive half-set pieces, and likewise for
the negative ones. If p were 9 or more, T would contain such a family of 9.

Those families can be listed completely. Inside the 48 positive half-set pieces there are
exactly 24 pairwise chamber-disjoint families of 9, and inside the 48 negative ones exactly
24. The count is cross-checked by two search orders, an extension walk in index order
over the disjointness graph and a take-it-or-leave-it walk carrying the union of chambers
already used, and the two agree as sets and not merely in count (`nine_family_census`).
These are a completeness cross-check for one route, not two independent no-go routes.

**T3.** Each of those 48 families is sealed: it leaves a chamber that no member holds, all 8
of whose holding pieces meet the family. Verified for every one of the 48, with 0 failures
(`sealing_witnesses`).

The obstruction follows at once. Suppose a cutting T contained a sealed family F. The
witness chamber c is held by exactly one piece Q of T, and Q is one of the 8 pieces holding
c, so Q shares a chamber with some member of F. That member is also in T, and two pieces of
one cutting share no chamber, so Q is that member; but no member of F holds c, and Q holds
c. The contradiction means no cutting contains any of the 48 families, hence

> **p is at most 8 and m is at most 8.**

The bound is not a bound on the enumeration: it is the statement that a family of 9 which
exists as a disjoint family cannot be part of a partition of the cell, because the chamber
it strands has nowhere left to go.

## The theorem and its corollary

Put the three together. From the constant twelve, p + m = 12; from sealing, p is at most 8
and m is at most 8, so p is at least 4 and lies between 4 and 8; from the halving identity,
S = 4 (p - 6). Therefore

> S lies in -8, -4, 0, 4, 8 and |S| is at most 8, on every cutting,

with 0 failures over the 15800 cuttings (`size_bound_identity`). Divisibility by 4 is now a corollary
rather than a separate law, and the size bound that `cycle 780` could only measure is
derived pointwise, from the value of p on the single cutting in hand.

The bound is attained at both ends: p takes the value 4 on 120 cuttings and 8 on 120, and
the label sum census matches term for term, -8 on 120, -4 on 2832, 0 on 9896, 4 on 2832 and
8 on 120 (`endpoint_censuses`). The correspondence between the two censuses is the theorem read
backwards, and it is exact, not approximate.

Two controls check that the gates discriminate. Negating g1 at a single chamber breaks the
per-piece identity at exactly 8 pieces, which are precisely the pieces holding that chamber
(`halving_mutation`); and dropping a single piece from H breaks the constant twelve at exactly 1975
cuttings, which are precisely the cuttings through that piece (`half_set_mutation`). Neither number is
imposed: each is measured on the perturbed object and compared with the count the structure
predicts.

## No-Go Discipline Gate

The derived negative boundary is deliberately narrow: among the 15800
geometric cuttings in the declared 400-piece candidate class, no cutting
contains nine half-set pieces of one label sign. It is not a claim about an
arbitrary four-cube triangulation, another candidate selector, a multi-cell
complex, or a lattice theory.

### N1 — five materially distinct attacks

The graph and take-or-leave-it orderings in `nine_family_census` are one
completeness cross-check and are not counted as separate routes. The five
routes below differ in their primary object, hypothesis presentation, or
terminal obligation.

| Attack route and normalization tuple | Attempt and result | Honesty marker |
|---|---|---|
| geometric-cover census `(simplex sample masks; declared 400-piece class; find p>=9 or m>=9)` | Search every exact sample cover after the independent separator-and-volume certificate makes it a geometric cutting. The primary runner's `size_bound_identity` gate scans all 15800 and finds zero bound failures. | **ATTEMPTED** |
| chamber-only reconstruction `(192 chamber masks; exact one-holder equations; find a violating cover)` | Re-enumerate exact covers from chamber incidence without using the shifted sample masks. The `chamber_reconstruction` gate returns the same 15800 covers and zero same-sign bound failures. | **ATTEMPTED** |
| explicit subset containment `(48 complete nine-piece candidates; enumerated cutting sets; find F subset T)` | Form every same-sign chamber-disjoint family of nine and test direct set containment against every cutting. The `direct_noncontainment` gate finds zero contained families. | **ATTEMPTED** |
| seeded completion `(one nine-piece family fixed; remaining chamber exact-cover problem; find any completion)` | Seed an exact-cover search separately with each of the 48 candidates and explore all compatible holders of a minimum-option uncovered chamber. The `seeded_completion` gate finds zero completions. | **ATTEMPTED** |
| local sealing `(one nine-piece family; chamber-holder neighborhoods; find an unfillable chamber)` | Search for a chamber outside the family whose eight holders all intersect it. The `sealing_witnesses` gate supplies such a witness for all 48 families with zero failures. | **ATTEMPTED** |

### N2 — wall independence

There is one claimed wall, not a count of independent walls: a same-sign
nine-piece chamber-disjoint family would have to extend to an exact chamber
partition. Direct containment, seeded completion, and local sealing are three
ways of testing that one wall; their number is not presented as a wall count.
The positive and negative label cases are symmetric instances and likewise are
not called independent walls.

### N3 — hidden-condition scan

| Condition | Classification and disposition |
|---|---|
| determinant-one, adjacency-cost-floor candidate class | explicit finite hypothesis; no claim beyond it |
| shifted 625-point grid | enumeration device; genericity checked exactly; not the geometric proof |
| exact separating normals and volume sum | executed geometric certificate for every selected cover |
| 192 used pieces and chamber incidence | derived from the complete geometric-cover census, then independently exact-covered |
| minimal naming and coordinate axis 3 | explicit deterministic naming and fixed coordinate convention |
| label, half set, `g1`, and `W` | definitions local to this theorem; no imported value |
| arbitrary triangulations, other cells, multi-cell systems, dynamics | outside the quantified domain; no negative statement made |
| axioms, approved primitives, observations, fits, standard-QFT assumptions | absent from the proof and not smuggled in |

### N4 — source-residual matching

| Candidate source | Exact residual | Match? | Witness treatment |
|---|---|---|---|
| this note's primary runner | whether any declared cutting contains at least nine `H` pieces of one sign | yes | sole load-bearing computational source |
| `cycle 779` and `cycle 780` names | narrative lineage for the finite object and an earlier measured bound | no landed source at the frozen main coordinate | provenance only; zero witness weight |
| current-main retained/audit corpus and no-go ledgers | an already retained proof or retirement entry for this exact half-set bound | no match found | no citation and zero witness weight |

After the nonmatching references are dropped, the negative proof still has the
complete local runner evidence listed in N1.

### N5 — rhetoric and resolution scope

| Resolution | Executed? | Narrow result |
|---|---|---|
| per-element | yes | all 192 piece incidences, labels, `g1` sums, and `W` counts |
| per-site | no | the one-cell theorem has no framework site variable or sitewise extension |
| per-mode | no | the finite incidence object defines no mode decomposition |
| per-block | yes | all 15800 declared cell cuttings; the same-sign count is at most eight |
| lattice-wide | no | no multi-cell or lattice-wide object is defined or tested |

The primary runner emits these same five substantive lines verbatim in cached
stdout, using `checked and not executed` for the three inapplicable classes.

### N6 — premise, primitive, and convention discipline

The current axiom authority, approved-primitive registry, premise-decision
history, controlled vocabulary, and open convention-ratification surface were
scanned. No framework premise or proposed primitive supplies or is needed for
this finite obstruction. Axis 3 is an explicit coordinate convention inside
the declared object; relabeling coordinates can transport the construction but
is not used to inflate the evidence count. The theorem proposes no new axiom,
primitive, physical selector, or interpretation stance. The topical open
piece-taxonomy work has different claims and files and does not retire or
support this bound.

### N7 — strongest steelman

The strongest counterargument is that a finite shifted grid might miss an
overlap or gap, or might omit a genuine geometric cutting, so a bound over its
exact covers would not be a theorem about the stated cuttings. The runner now
answers both directions independently: genericity makes every genuine cutting
an exact cover of the sample points, while exact separating planes for every
co-occurring simplex pair plus the determinant-volume sum prove that every
enumerated cover tiles the entire cube. The chamber-only reconstruction then
reaches the same family without the sample masks. What remains outside scope is
an arbitrary triangulation or another candidate selector, and the note makes no
negative claim there.

### N8 — prior-art and retirement scan

At frozen `origin/main` SHA
`a950a1aacfb33c10699dc88ac2f441d7024ad109`, searches of the science notes,
audit ledger, and checked-in `NO_GO_LEDGER.md` files found no retained or
conditional claim for this exact half-set size bound or sealed-family
obstruction. The other open cell-cutting PR found by the topical scan concerns
piece taxonomy, count laws, and a wall-letter split; it neither proves nor
supersedes this theorem. There is therefore no earlier route to retire and no
duplicate authority is claimed.

## What this does not establish

**The p-census is measured, not derived.** The distribution of p over the 15800 cuttings,
120 at 4, 2832 at 5, 9896 at 6, 2832 at 7 and 120 at 8, is symmetric about 6 and sharply
peaked, and none of that is forced by anything above. The derivation constrains p to the
five values and no further; why the middle value is so much heavier, and why the two ends
carry exactly 120 apiece, is open.

**Family transitivity is measured, not derived.** The 24 families in each half are checked
one at a time, both for the enumeration and for the sealing, and the witness chamber is
found separately for each. Whether the 24 are all alike under the symmetries of the cell,
which would let one sealed family do the work of all of them, is not settled here; no such
action is exhibited, so the regularity visible in the numbers stays a measurement.

**The sharpening deferred by `cycle 780` is not attempted.** That note observed a
divisibility by 4 of one of its two telescoping counts, stronger than the parity its
argument gives, and asked for a certificate taking values modulo 4. Nothing here supplies
one. The present derivation reaches the same divisibility by a different argument, through
p, and so does not answer that question either.

Two further limits are stated plainly. The geometric certificate proves tiling and
exhaustivity only for the 400 determinant-one pieces selected by the declared
adjacency-cost floor; it does not classify arbitrary triangulations of a four-cube.
The claim type is `bounded_theorem`, not a stronger one, because the object is
this finite cell and candidate class as rebuilt: nothing here extends the
identities to another cell, a multi-cell complex, a lattice-wide system, or a
physical dynamics.

## Relation to sibling cycles

The object, handedness label, and chamber picture have narrative lineage in
`cycle 779` and `cycle 780`, but their definitions and every load-bearing fact
are rebuilt here. The mod-four law described for `cycle 780` is re-derived as a
corollary of the sharper identity, and its measured size bound is proved for the
declared class. Nothing in either sibling is withdrawn. All sibling references
are provenance-only names with no citation edges or imported premise: at this
review's frozen main coordinate, those predecessor notes are not on the main
line.

## Gate list with the measured numbers

All 18 gates concern the explicitly rebuilt finite object and use exact integer
or rational arithmetic; no floating point enters any gate. The linked primary
runner uses the standard library only and declares a 120-second audit timeout.

* **`object_rebuild`**: 2672 determinant-one pieces, cost floor 6, 400
  candidates at the floor, 15800 cuttings of 24, 192 used pieces each in 1975,
  and 384 namings, 2 per piece.
* **`geometric_tiling`**: all 15168 co-occurring simplex pairs have an exact
  separator among 80 nonzero ternary normals; 24 unit normalized volumes fill
  the cell.
* **`chamber_partition`**: each of a cutting's 24 pieces holds 8 of the 192
  chambers, each chamber has 8 holders, and there are 0 failures over 15800.
* **`minimal_naming`**: the label formula matches all 192 pieces over 8 start
  corners, with 0 mismatches.
* **`half_set`**: 96 pieces lie in the half set, split 48 and 48 by label.
* **`halving_certificate`**: the chamber values have census 24 negative, 144
  zero, 24 positive, total zero, and 0 per-piece failures.
* **`halving_identity`**: `S = 2 S_H`, with 0 failures over 15800 cuttings.
* **`witness_set`**: `W` has 12 chambers, one inside each half-set piece and
  zero inside every other piece, with 0 failures.
* **`constant_twelve`**: every cutting holds 12 half-set pieces, with 0
  failures over 15800.
* **`chamber_reconstruction`**: an independent chamber-only exact-cover search
  returns exactly the same 15800 cuttings and 0 same-sign bound failures.
* **`nine_family_census`**: there are 24 positive and 24 negative disjoint
  nine-piece families; graph and union-mask searches agree as exact sets.
* **`direct_noncontainment`**: 0 of those 48 families is a subset of an
  enumerated cutting.
* **`seeded_completion`**: exact-cover searches seeded by all 48 families find
  0 completions.
* **`sealing_witnesses`**: all 48 families have an uncovered chamber whose 8
  holders meet the family, with 0 failures.
* **`size_bound_identity`**: `S = 4(p-6)`, `p+m=12`, and `4<=p<=8`, with 0
  failures over 15800.
* **`endpoint_censuses`**: the `p` census is 120, 2832, 9896, 2832, 120 at
  `p=4,5,6,7,8`; the matching `S` census is 120, 2832, 9896, 2832, 120 at
  `S=-8,-4,0,4,8`.
* **`halving_mutation`**: negating `g1` at one chamber breaks exactly its 8
  holding pieces.
* **`half_set_mutation`**: dropping one piece from `H` breaks exactly the 1975
  cuttings through it.
