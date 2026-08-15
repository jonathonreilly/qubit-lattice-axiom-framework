---
claim_id: formation_class_three_cut_survivors_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among cube-covariant boolean formation predicates, the subclass that vanishes on empty and full and is complement-even has size 2^{N_free}. L1 is one element. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/formation_class_three_cut_survivors_2026_08_15.py
---

# Three Displayed Cuts On The Cube-Covariant Formation Class

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit algebra of the 64 six-ray occupation cells under the
24 proper cube rotations, and the free-bit count after three independently
motivated cuts. No formation law is selected. `f_L1` is displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/formation_class_three_cut_survivors_2026_08_15.py`](../scripts/formation_class_three_cut_survivors_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `S` be the open six-ray star at a distinguished origin of `Z^3`: the six
nearest-neighbor displacements. A **cell** is an occupation pattern
`c ∈ {0,1}^S`. There are exactly 64 cells. The 24 proper cube rotations
permute `S` and therefore permute the 64 cells. A boolean formation
predicate `f : {0,1}^S → {0,1}` is **cube-covariant** when it is constant on
rotation orbits. The rotation action has

`N_orb = 10`

orbits, so the raw cube-covariant class `F_G` has size

`|F_G| = 1024`.

That raw count is leftover-char inventory of the unrestricted class. It is
not the residual of this note. This note applies three displayed cuts,
each independently motivated and not fitted after the fact:

1. vanish on empty: `f(0) = 0`;
2. vanish on full: `f(1) = 0`;
3. complement-even: `f(c) = f(1-c)` for every cell.

**Theorem 1.** The ten orbits partition as one empty orbit, one full orbit,
two complement-fixed orbits, and three complement-pairs.

**Theorem 2.** A complement-even predicate with `f(empty)=f(full)=0` is a
free `{0,1}` assignment to each complement-pair and each remaining
non-empty/non-full complement-fixed orbit. Hence

`N_free = 5`, `|F_cut| = 32 = 2^{N_free}`.

**Theorem 3.** The displayed L1 predicate

`f_L1(c) = 1` iff at least one axis is unbalanced (`c_{+μ} ≠ c_{-μ}`)

lies in `F_cut`. Hamming parity `|c|_1 mod 2` is a different element of
`F_cut`. Because `|F_cut| = 32 > 1`, `f_L1` is not unique. L1 still needs
another extra. Do not adopt a member.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant
under lattice translations and proper cubic rotations.

Those sentences supply the 24 proper cube rotations and nearest-neighbor
covariance used as host symmetry. They do not name a boolean formation
predicate, an empty/full cut, or a complement involution on occupation
cells.

The Admissibility reading note in the same memo states that, read with
Record, the local distribution concerns which possibility a forming record
locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate. The present algebra does not close
that gap.

The Record wording in the same memo is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

These sentences type locking and content-determined readout. They do not
select a member of `F_G` or of `F_cut`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit partition and the free-bit count after the three displayed cuts are exact finite identities. f_L1 is one displayed survivor. Uniqueness fails."
trace_class: negative_route_pruning
target_claim_id: formation_class_three_cut_survivors
target_blocker_text: "how many cube-covariant boolean formation predicates survive vanish-on-empty, vanish-on-full, and complement-even, and whether f_L1 is the unique survivor"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Supply another independent extra if a unique member is required; do not adopt f_L1 or any other survivor."
conditional_surface_status: "exact on the 64-cell six-ray host; no physical formation law is selected"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Index the six rays as

`(+e_1,-e_1,+e_2,-e_2,+e_3,-e_3)`.

A cell is a 6-bit word. Empty is `000000`. Full is `111111`. Complement is
bitwise flip, written `c ↦ 1-c`. The Hamming weight `|c|_1` is the L1
occupation count of the star.

A proper cube rotation is a signed permutation of the three axes with
determinant `+1`. There are 24 such maps. Each permutes the six rays and
therefore acts on cells by permuting bits.

Two cells lie in the same orbit when a proper rotation carries one to the
other. Cube-covariant predicates are arbitrary `{0,1}` assignments to the
`N_orb` orbits. That is the raw class `F_G`.

The displayed L1 member is the occupancy kernel threshold

`f_L1(c) = 1` iff `c_{+μ} ≠ c_{-μ}` for some axis `μ`.

Hamming parity `|c|_1 mod 2` is a different cube-covariant predicate.

It is a function of the L1 count alone. It is displayed comparison data,
not axiom content and not a selected law.

The three cuts are independently motivated:

- empty is the absence of occupation on the star;
- full is the complementary occupation of empty, so a vanish-on-empty
  predicate that is complement-even must also vanish on full, and the
  full cut is written separately because it is the complementary absence
  statement;
- complement-even is indifference of the predicate to swapping occupied
  with unoccupied.

None of the three cuts is fitted to isolate `f_L1`.

## Theorem 1 — Orbit Partition Under Complement

The 24 proper rotations partition the 64 cells into exactly ten orbits.
Representatives and sizes are:

| type | weight | size | complement image |
|---|---:|---:|---|
| empty | 0 | 1 | full |
| full | 6 | 1 | empty |
| `wt1` | 1 | 6 | `wt5` |
| `wt5` | 5 | 6 | `wt1` |
| `opp2` | 2 | 3 | `opp4` |
| `opp4` | 4 | 3 | `opp2` |
| `adj2` | 2 | 12 | `adj4` |
| `adj4` | 4 | 12 | `adj2` |
| `vertex3` | 3 | 8 | `vertex3` |
| `mixed3` | 3 | 12 | `mixed3` |

`opp2` is an opposite pair of rays. `adj2` is two rays that are not
opposite. `vertex3` occupies exactly one ray from each opposite pair.
`mixed3` occupies one opposite pair plus one further ray.

Empty and full are singleton orbits. Complement exchanges them.
Complement also exchanges `wt1` with `wt5`, `opp2` with `opp4`, and
`adj2` with `adj4`. The two weight-three orbits are each complement-fixed
as sets: complement permutes cells inside the orbit but does not leave
the orbit.

Thus the ten orbits partition as

- empty orbits: 1;
- full orbits: 1;
- complement-fixed orbits: 2;
- complement-pairs: 3.

These four counts are exact and sum, with each pair counted as two
orbits, to `1+1+2+6=10`.

## Theorem 2 — Free Bits After The Three Cuts

A cube-covariant predicate is an assignment of a bit to each of the ten
orbits. Complement-even forces equal bits on the two members of each
complement-pair. Vanish-on-empty and vanish-on-full force the empty and
full bits to `0`. Those two orbits already form one complement-pair, so
the pair constraint on empty/full is implied by the two vanish cuts.

The remaining free data are therefore:

- one bit for the pair `{wt1,wt5}`;
- one bit for the pair `{opp2,opp4}`;
- one bit for the pair `{adj2,adj4}`;
- one bit for the complement-fixed orbit `vertex3`;
- one bit for the complement-fixed orbit `mixed3`.

Hence `N_free = 5` and

`|F_cut| = 2^{N_free} = 32`.

Every such assignment is complement-even and vanishes on empty and full.
No further linear relation among these five bits is forced by the three
cuts.

## Theorem 3 — `f_L1` Lies In `F_cut` And Is Not Unique

Unbalanced-axis count is rotation-invariant, so `f_L1` is cube-covariant.
Empty and full are axis-balanced, so `f_L1(empty)=f_L1(full)=0`. Complement
sends `c_{+μ}-c_{-μ}` to its negative, so `n≠0` is complement-even.
Therefore `f_L1 ∈ F_cut`. Hamming parity `|c|_1 mod 2` is a different
element of `F_cut`. `|F_cut| = 32 > 1`, so `f_L1` is not unique. An
explicit second survivor is the indicator of the `vertex3` orbit, which
vanishes on empty and full, is complement-even because that orbit is
complement-fixed, and disagrees with `f_L1` on `wt1`. L1 still needs
another extra. The three displayed cuts do not select a unique member.
Do not adopt `f_L1`. Do not adopt Hamming parity. Do not adopt the
`vertex3` indicator.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| 24 proper cube rotations of the six rays | exact finite group |
| 64 cells and `N_orb = 10` | exact partition |
| complement permutes cells and orbits | exact involution |
| Theorem 1 orbit-type counts | exact |
| Theorem 2 `N_free = 5`, `|F_cut| = 32` | exact |
| Theorem 3 membership of `f_L1` | exact |
| uniqueness of `f_L1` in `F_cut` | closed negatively; not unique |
| leftover-char raw-class count | reconstructed as `|F_G| = 1024`; not the residual |
| physical selection of a member | open |
| formation site, probability, or rate | open |

## Imports And Non-Claims

The live axiom memo is imported only for the quoted Lattice rotation
language, Admissibility covariance, the formation-rate residual, and the
Record lock/content/absence boundary. No boolean predicate is imported
from the axioms.

This note is not leftover-char of the raw class. The raw size
`|F_G| = 1024` is recorded only to separate that inventory from the
three-cut count `|F_cut| = 32`.

No empirical occupation frequency, fitted cut, Hamiltonian, dynamics, or
physical readout map is imported. The comparison class is not treated as
physical law. The six-ray star is supplied mathematical host data for the
finite count. The note does not claim that formation events live on that
star.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the uniqueness question inside the 1024-element class after three independently motivated cuts. |
| V2 | The three-cut free-bit count and the explicit second survivor are new relative to a raw-class inventory. |
| V3 | Orbit sizes, complement pairing, and `|F_cut| = 32` are independently checkable by enumerating 64 cells and 24 rotations. |
| V4 | The partition explains why vanish-on-empty, vanish-on-full, and complement-even leave five free bits rather than one. |
| V5 | It does not relabel `f_L1` as a selected law. Another extra remains. |

## No-Go Discipline Gate

The negative claim is restricted to uniqueness of `f_L1` inside `F_cut`.
No global impossibility of a later extra is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| raw class `F_G` | assign a free bit to each of 10 orbits | size 1024; leftover-char inventory, not the residual |
| three displayed cuts | vanish on empty and full, force `f(c)=f(1-c)` | size 32; executed |
| `f_L1` | form iff at least one axis is unbalanced | one displayed survivor; not unique |
| `vertex3` indicator | fire only on the complement-fixed corner orbit | second displayed survivor |
| further symmetry extra | impose another independent invariance | live route; not executed |
| Record or Admissibility selector | derive a unique member from current axioms | not supplied by the quoted sentences |
| observation | select a predicate empirically | live route; no observation is admitted here |

### N2 — wall independence

A further symmetry, a dynamics-derived selector, and an observational
selector are independent possible extras. The theorem claims no complete
wall collection and no global no-go.

### N3 — hidden-condition scan

The 64-cell host, the 24 proper rotations, the three cuts, and the
definition of `f_L1` are explicit. Physical realization of formation on
the star, and any extra that would cut `F_cut` down to one element, are
not silently assumed.

### N4 — source residual matching

Current Lattice supplies proper cubic rotations about each site. Current
Admissibility is covariant under those rotations and does not supply the
formation site, probability, or rate. Current Record types locking and
content-determined readout. The repaired theorem uses only that
boundary and does not enlarge it.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each of the 64 cells | no exhaustive physical-state classification |
| per site | the six-ray star at one origin | no multisite formation process |
| per mode | checked and not executed | no spectral-mode exhaustion |
| per block | ten-orbit partition and `2^5` count | no physical selector |
| lattice wide | checked and not executed | no global formation no-go |

### N6 — live partial-closure paths

Another independent extra can still select a unique member. Dynamics,
further symmetry, or observation remain live and are not functions of
the three displayed cuts.

### N7 — hostile steelman

**Steelman:** The three cuts are the natural ones, and `f_L1` is the
natural L1 character, so uniqueness is obvious.

**Answer:** Naturality of a displayed member is not uniqueness inside the
cut class. The free-bit count is 5, and an explicit second survivor is
written above.

### N8 — cross-cycle echo

A raw-class leftover-char count answers a different question: how large
is `F_G` before the three cuts. Reusing that inventory as if it were a
uniqueness proof would misstate the residual. The present note separates
the two counts and closes uniqueness negatively.

**Gate disposition:** PASS for the orbit partition, the free-bit count,
and membership of displayed `f_L1` in `F_cut`. FAIL / DO NOT SHIP for
“the three cuts select `f_L1` uniquely,” “adopt `f_L1` as the formation
law,” or any claim that current Record or Admissibility already names a
member.

## Primary Runner

The primary runner rebuilds the 24 proper cube rotations and 64 cells,
enumerates the ten orbits, checks the complement partition, computes
`N_free` and `|F_cut|`, verifies that `f_L1` lies in `F_cut`, and
exhibits a second survivor. It authors no audit verdict.
