---
claim_id: born_cluster_under_support_only_admissibility_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Four reconstructed finite facts (two occupancy laws at neighbor count 2 disagree; Tr(rho P) is not I of one lock; menu identity trace is not I(empty); a scaled projector is not a projector) are arithmetic or type facts on both the current distribution reading and a diagnostic support-only reading of Admissibility. Under the support-only reading, 'the axioms pick neither occupancy law', 'mu is not rho', and 'a lock is not mu' are expected gaps, not TOE walls. Facts 2-4 remain type-splits on both readings. Exactly one of the four reconstructed claims flips from TOE wall to expected gap. The August 5 distribution clause is not dropped; r=1/2 and L_phys are not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/born_cluster_under_support_only_admissibility_hypothetical_2026_08_13.py
---

# Born Cluster Under Support-Only Admissibility (Hypothetical Classification)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** diagnostic classification of four reconstructed finite claims under
two *readings* of Admissibility. Neither reading is adopted as a rewrite.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/born_cluster_under_support_only_admissibility_hypothetical_2026_08_13.py`](../scripts/born_cluster_under_support_only_admissibility_hypothetical_2026_08_13.py)

Parent on `origin/main`:

- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

No other parent is used. No unmerged pull request is cited. Gleason's
theorem is not imported. The decimal `0.5934` is not used.

## Result Up Front

The August 5 Admissibility sentence is still the current memo wording:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

That clause is not dropped here.

Two readings of that wording are quoted as readings, and neither is adopted
as a rewrite:

- **R_dist** (current memo): there is a law-level nearest-neighbor-determined
  distribution; form and values are unspecified.
- **R_supp** (diagnostic): the axiom names only the support / available set;
  no law-level `mu` values exist in the axiom.

Four finite facts are reconstructed by exact arithmetic in this note:

1. Two occupancy laws disagree: `mu1(A|2)=1/3` and `mu2(A|2)=3/8`.
2. `Tr(rho P)=3/5` for `rho=diag(3/5,2/5)`, `P=diag(1,0)`; Record `I` of one
   lock is `1`.
3. Menu identity `I_2` has `Tr=2`; `I(empty)=0`.
4. Scaled `E0=(1/2)P` is not a projector.

Facts 1–4 are true as arithmetic / type facts on both readings
(Theorem 1). Under **R_supp**, “the axioms pick neither `mu1` nor `mu2`”,
“`mu` is not `rho`”, and “a lock is not `mu`” are expected gaps: there is
no axiom-level `mu` to pick. Under **R_dist** those three sentences are
walls, because the axiom names a `mu` without values (Theorem 2). Facts
2–4 remain type-splits under both readings. The diagnostic does not
dissolve the need for a compiler if Born is still a TOE output
(Theorem 3). Of the four reconstructed claims, exactly **one** changes
from “TOE wall” to “expected gap” when the reading flips
`R_dist -> R_supp` (Theorem 4). The displayed count is `1`.

The note does not force `r=1/2`. The note does not adopt `L_phys`. The
note does not adopt a Born axiom and does not edit the four named axioms.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four reconstructed facts are exact arithmetic or type facts on declared finite objects. Classification of mu-picking sentences depends on the quoted reading. The August 5 clause is retained; axiom adoption, r=1/2, L_phys, and a later Born compiler remain open."
trace_class: negative_route_pruning
target_claim_id: born_cluster_under_support_only_admissibility
target_blocker_text: "treat the four reconstructed Born-cluster facts as uniformly TOE-dissolved by a support-only reading, or drop the August 5 distribution clause"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the four reconstructed facts and the displayed wall-to-gap count; neither reading is adopted"
hypothetical_axiom_status: "C4 diagnostic: classify selected claims under support-only Admissibility; clause not dropped"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Two Readings (Quoted, Not Adopted)

The current memo's Admissibility axiom names a nearest-neighbor rule and
then the distribution sentence quoted above. Reading notes in the memo
already say that the distribution is law-level, that “available” /
“admissible” denotes its support, and that the distribution's extensional
form and values are not specified.

**R_dist** reads that wording as written: a law-level `mu` is named; its
form and values remain unspecified.

**R_supp** is a diagnostic counter-reading: keep only the support /
available set as axiom content, and treat law-level `mu` values as absent
from the axiom.

Both readings are quoted. Neither is a rewrite of the memo. A pre-August-5
availability-only axiom is not restored. The August 5 distribution clause
is not dropped.

## Exact Objects

**Occupancy laws at neighbor count 2.** Fix a two-outcome occupancy menu
`{A,B}` at one site whose nearest-neighbor occupancy count is `k=2`. A
candidate occupancy law is a probability vector on that menu. Two explicit
reconstructions, written here and not imported from any pull request:

- `mu1` is the uniform three-slot law at `k=2`: `mu1(A|2)=1/3`,
  `mu1(B|2)=2/3`.
- `mu2` is the three-of-eight law at `k=2`: `mu2(A|2)=3/8`,
  `mu2(B|2)=5/8`.

Identity gates evaluate these as `mu1_at_2()` and `mu2_at_2()`.

**Born pairing.** Let

`rho = diag(3/5, 2/5)`, `P = diag(1,0)`.

Then `Tr(rho P)=3/5`. The identity gate is `born_rho_P()`.

**Record count.** The Record axiom: when present, a record locks exactly
one admissible local possibility; for any finite collection of
pairwise-disjoint records, scalar readout `I` is additive, with
`I(empty)=0`. For one unit lock, `I=1`. The identity gate is `I_one()`.

**Menu identity versus empty readout.** Write `I_2` for the `2 x 2`
identity matrix on the one-site algebra `M_2(C)`. Then `Tr(I_2)=2`. The
Record empty collection has `I(empty)=0`. These are different objects
that share a letter.

**Scaled projector.** Let `E0=(1/2)P`. Then `P^2=P`, so `P` is a
projector, while `E0^2=(1/4)P != (1/2)P`, so `E0` is not a projector.

## Exact Target And Obligation Graph

**Exact target.** Reconstruct the four finite facts from the axiom memo
plus the arithmetic written here. Classify each reconstructed claim under
`R_dist` and under `R_supp`. Count how many flip from “TOE wall” to
“expected gap”. Do not drop the August 5 clause. Do not adopt either
reading.

| Obligation | Role | Disposition |
|---|---|---|
| `1/3 != 3/8` | Fact 1 | proved |
| `Tr(rho P)=3/5 != 1=I(one lock)` | Fact 2 | proved |
| `Tr(I_2)=2 != 0=I(empty)` | Fact 3 | proved |
| `E0=(1/2)P` is not a projector | Fact 4 | proved |
| Facts 1–4 hold on both readings | Theorem 1 | proved |
| mu-picking sentences expected under `R_supp`, walls under `R_dist` | Theorem 2 | classification |
| Facts 2–4 remain type-splits; compiler need is not dissolved | Theorem 3 | classification |
| display the wall-to-gap flip count | Theorem 4 | count `1` |
| do not drop the August 5 clause; do not force `r=1/2`; do not adopt `L_phys` | firewall | held |

## Theorem 1 — The Four Facts Are Reading-Independent Arithmetic

Each fact is a statement about declared finite objects. None of them
quantifies over `R_dist` versus `R_supp`.

**Fact 1.** Cross-multiplying the two occupancy values,

`1/3 - 3/8 = 8/24 - 9/24 = -1/24 != 0`,

so `mu1(A|2) != mu2(A|2)`. The hostile predicate
“`mu1(A|2)=mu2(A|2)`” fails.

**Fact 2.** Matrix multiplication of the displayed diagonal pair gives

`Tr(rho P) = 3/5`.

One unit lock has `I_one()=1`. Then `3/5 != 1`. The hostile predicate
“`Tr(rho P)=I(one lock)`” fails.

**Fact 3.** `Tr(I_2)=1+1=2`. Record additivity supplies `I(empty)=0`.
Then `2 != 0`. The menu identity and the empty readout are different
types.

**Fact 4.** `P^2=P`. For `E0=(1/2)P`,

`E0^2 = (1/4) P^2 = (1/4)P`,

which equals `E0` only if `(1/4)P=(1/2)P`, i.e. only if `P=0`. The
displayed `P` is not zero. So `E0` is not a projector.

These four statements remain true if Admissibility is read as `R_dist`
and remain true if it is read as `R_supp`. They do not depend on which
reading is quoted.

## Theorem 2 — Missing-`mu` Sentences Are Expected Under `R_supp`

Three interpretive sentences are often treated as Born-cluster walls:

- “the axioms pick neither `mu1` nor `mu2`”
- “`mu` is not `rho`”
- “a lock is not `mu`”

Under **R_supp** there is no axiom-level `mu` to pick, to identify with
`rho`, or to confuse with a lock. Each sentence is then a reading of a
missing object. That is an **expected gap**, not a TOE wall.

Under **R_dist** the axiom *names* a law-level nearest-neighbor-determined
`mu` and withholds its values. Then:

- two reconstructed occupancy laws that disagree are a wall (the named
  `mu` is not selected);
- identifying or distinguishing that named `mu` from a density matrix
  `rho` is a wall;
- identifying a Record lock with that named `mu` is a wall.

The diagnostic does not adopt `R_supp`. It only classifies those three
sentences under the quoted reading.

## Theorem 3 — Facts 2–4 Remain Type-Splits; The Compiler Need Survives

Facts 2–4 compare objects that the axioms *do* name, independently of
whether a law-level `mu` is present:

| Pair | Left type | Right type |
|---|---|---|
| `Tr(rho P)` versus `I(one lock)` | rational pairing in `(0,1)` | integer lock count |
| `Tr(I_2)` versus `I(empty)` | trace of the `2 x 2` identity | additive empty readout |
| `E0=(1/2)P` versus `P` | scaled effect | projector |

Each pair remains a type-split under `R_dist` and under `R_supp`. A
support-only reading does not identify `I` with a Born number, does not
identify the menu identity with the empty readout, and does not make a
properly scaled projector into a projector.

If Born is still a TOE output, a compiler from axiom-named objects to a
Born number is still required. This diagnostic does not dissolve that
need. It does not claim that no later compiler exists.

## Theorem 4 — Wall-To-Gap Flip Count

Classify the four reconstructed claims. A claim **flips** when its status
changes from “TOE wall” under `R_dist` to “expected gap” under `R_supp`.
A type-split that remains a type-split under both readings does not flip.

| # | Reconstructed claim | Exact witness | Under `R_dist` | Under `R_supp` | Flips wall → gap? |
|---|---|---|---|---|---|
| 1 | two occupancy laws disagree; axioms pick neither `mu1` nor `mu2` | `mu1_at_2()=1/3 != 3/8=mu2_at_2()` | TOE wall | expected gap | yes |
| 2 | `I` versus Born number | `born_rho_P()=3/5 != 1=I_one()` | type-split | type-split | no |
| 3 | `I_2` versus `I(empty)` | `Tr(I_2)=2 != 0=I(empty)` | type-split | type-split | no |
| 4 | scaled `cP` versus projector `P` | `E0=(1/2)P` is not a projector | type-split | type-split | no |

**Count of `R_dist -> R_supp` wall-to-gap flips: 1**

The three Theorem 2 sentences about a missing `mu` are the interpretive
content of row 1, not three extra reconstructed arithmetic claims. Facts
2–4 stay type-splits, which is why the flip count is not `4` and not `0`.

## Firewalls

- The August 5 distribution clause is current memo content and is not
  dropped.
- A pre-August-5 availability-only rewrite is not adopted.
- `R_supp` is a diagnostic reading, not an axiom edit.
- Do not force `r=1/2`.
- The note does not adopt `L_phys`.
- Gleason's theorem is not imported.
- The decimal `0.5934` is not used.
- No unmerged pull request is cited as a premise.

## No-Go Discipline Gate

The negative claims are restricted to (i) the four reconstructed facts
and (ii) the reading-relative classification of the missing-`mu`
sentences. The gate does not certify that no Born compiler can exist and
does not adopt a support-only axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Identify `mu1(A\|2)` with `mu2(A\|2)` | equate `1/3` and `3/8` | Fact 1: they differ | **ATTEMPTED** |
| Identify `Tr(rho P)` with `I` of one lock | equate `3/5` and `1` | Fact 2: type-split | **ATTEMPTED** |
| Identify `Tr(I_2)` with `I(empty)` | equate `2` and `0` | Fact 3: type-split | **ATTEMPTED** |
| Treat `E0=(1/2)P` as a projector | require `E0^2=E0` | Fact 4: fails | **ATTEMPTED** |
| Read `R_supp` as dissolving Facts 2–4 | drop the compiler need | Theorem 3: type-splits remain | **ATTEMPTED** |
| Drop the August 5 clause / restore pre-August-5 text | axiom rewrite | firewall: clause not dropped | **ATTEMPTED** |
| Force `r=1/2` or adopt `L_phys` | promote a dial or a length | firewall: refused | **ATTEMPTED** |
| Later compiler from extra structure | derive a Born number after a dictionary | not tested; remains live | live |

The broad statement “no later compiler exists” is not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| occupancy-law disagreement / Born-versus-`I` | no: `1/3 != 3/8` does not compare `3/5` to `1` | no: the pairing type-split does not pick `mu` | independent |
| Born-versus-`I` / `I_2`-versus-empty | no: one lock is not the `2 x 2` identity | no: empty readout is not a Born pairing | independent |
| `I_2`-versus-empty / scaled-versus-projector | no: traces do not test `E0^2=E0` | no: projector failure is not a count | independent |
| `R_supp` missing-`mu` / Facts 2–4 | no: deleting `mu` does not identify types | no: type-splits do not restore `mu` | independent |

The sufficient later extra, if any, is a compiler that produces a Born
number from axiom-named objects plus derived dictionaries. That extra is
not counted as a wall closed here.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `mu1(A\|2)=1/3`, `mu2(A\|2)=3/8` | two explicit occupancy laws at `k=2`; not a classification of all laws |
| `rho`, `P` | one diagonal pair; not a Gleason hypothesis |
| `I_one`, `I(empty)` | Record additivity on unit locks |
| `I_2` | `2 x 2` identity matrix |
| `E0=(1/2)P` | one scaled projector |
| `R_dist`, `R_supp` | quoted readings; neither adopted |
| August 5 distribution sentence | retained current wording |
| `r=1/2` | firewall only; not derived |
| `L_phys` | named only to refuse adoption |
| Gleason, `0.5934` | not used |
| unmerged pull requests | not cited |
| observations or fitted frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | August 5 distribution sentence; support is the set of nonzero probabilities on a finite menu; form and values unspecified; one admissible lock; content-only readout; `I` additive with `I(empty)=0`; law supplies odds and the realized state supplies the pick | exact current wording; no Born readout borrowed |

No unmerged pull request is cited. The four arithmetic witnesses are
proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two occupancy values, one Born pairing, one empty count, one scaled projector | no classification of every occupancy law |
| per site | one site, neighbor count `k=2`, one unit lock | no lattice composite |
| per mode | not used | no spectral claim |
| per block | four-fact reconstruction and reading-relative classification | no Born-form derivation; no axiom edit |
| lattice-wide | not executed | no global frequency theorem |

### N6 — live partial-closure paths

1. A later compiler may still derive a unique occupancy law from further
   nearest-neighbor structure.
2. A later dictionary may still relate Record counts to a menu kernel
   after the kernel is itself derived.
3. A later derivation may still force projector-valued grades or reject
   scaled effects on physical grounds.

None of those paths is closed here. None is claimed impossible. C4 does
not dissolve the compiler need if Born remains a TOE output.

### N7 — hostile steelman

> If Admissibility names only a support, then every Born-cluster complaint
> about missing `mu` values is dissolved, so Facts 2–4 stop being walls
> and no compiler is required.

The steelman conflates a missing law-level `mu` with a type identification
that does not mention `mu`. Facts 2–4 compare `I` to a pairing, the menu
identity to the empty readout, and a scaled effect to a projector. Those
objects remain after `mu` is deleted from the reading. Expected gaps
about a missing `mu` do not identify those types.

### N8 — cross-cycle echo

The current memo already separates a named distribution from unspecified
form and values, and already separates law-level odds from the realized
pick. This note applies that split to a diagnostic support-only reading
without restoring pre-August-5 axiom text. It does not reopen the memo.

**Gate disposition:** PASS for (i) the four reconstructed facts,
(ii) missing-`mu` sentences expected under `R_supp` and walls under
`R_dist`, (iii) Facts 2–4 remaining type-splits, and (iv) flip count `1`.
FAIL / DO NOT SHIP for “drop the August 5 clause,” “adopt `R_supp` as
the axiom,” “no later compiler exists,” “force `r=1/2`,” or “adopt
`L_phys`.”

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | distribution clause, support reading note, lock, `I` | supplied; no edit |
| two occupancy laws at `k=2` | Fact 1 witness | constructed here |
| `rho`, `P`, `I_2`, `E0` | Facts 2–4 witnesses | constructed here |
| `R_dist`, `R_supp` | quoted readings | not adopted |
| later compiler, `L_phys`, Born axiom | extras | not adopted |
| Gleason, `0.5934`, unmerged PRs | excluded | not used |

## Review Record

Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing this artifact.
