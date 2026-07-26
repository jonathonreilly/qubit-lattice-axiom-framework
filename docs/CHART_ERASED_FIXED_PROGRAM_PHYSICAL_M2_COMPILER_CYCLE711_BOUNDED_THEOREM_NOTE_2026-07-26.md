# Cycle 711 chart-erased fixed-program physical-M2 compiler

**Date:** 2026-07-26

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Primary runner:**
[`scripts/frontier_cycle711_chart_erased_fixed_program_2026_07_26.py`](../scripts/frontier_cycle711_chart_erased_fixed_program_2026_07_26.py)

**Receipt:**
[`outputs/chart_erased_fixed_program_physical_m2_compiler_cycle711_receipt_2026_07_26.json`](../outputs/chart_erased_fixed_program_physical_m2_compiler_cycle711_receipt_2026_07_26.json)

**Canonical runner cache:**
[`logs/runner-cache/frontier_cycle711_chart_erased_fixed_program_2026_07_26.txt`](../logs/runner-cache/frontier_cycle711_chart_erased_fixed_program_2026_07_26.txt)

## Result

The landed Cycle 710 family admits an exact chart erasure on its declared
common-frame signed code space.  Let `G_R` be its physically checked word in
proper-cubic frame `R`, let `pre_R` be the OpenReference input code-chart map,
and let `patch_forward_R` be the PatchGraph output code-chart map.  Exact
signed-Clifford inversion gives

```text
patch_forward_R^-1 G_R pre_R^-1 = W_star
```

for every one of the 24 proper-cubic frames.  The same immutable `W_star` is
the landed Cycle 709 primary word:

- 1,265 primitive gates;
- 22,635 routed nearest-neighbour gates;
- 276 assigned data/code/rail M2;
- maximum route distance 24; and
- zero runtime frame, coframe, tag, gauge, or dispatch opcodes.

All 24 chart-erased logical tableaus have one digest,
`e86fe5c5fc9e7d485782a8f8a3b1127724aaafdf13d30dfaa1a16c55b7edc25f`,
with zero exact, symplectic, or phase mismatch to the Cycle 709 base.
Independently undoing the physical address relabeling returns the identical
1,265-instruction digest
`ca0ba6473136e89ac505013b6e33471ccb2da1d4e74da6f97be5e91238748859`
in all 24 frames.

This is a positive code-chart factorization.  It does not claim that the
current emitted nonidentity-frame circuits were already mere wire
permutations.  Address relabeling alone leaves 44--92 exact code-space
mismatches in every nonidentity frame.  The exact signed-code pre/post
Cliffords are load-bearing; the theorem moves them from executed update gates
into the declared passive input/output code-chart identifications.

## Physical and overlap checks

The runner re-executes the original frame family and the independent controls:

- all 24 original pre/base/post words have zero placement, leakage,
  nearest-neighbour, operand-order, and route-return failures;
- every frame has at least 723 active first-route-SWAP deletion witnesses;
- all 576 proper-cubic products, inverse maps, semantic checks, and locality
  checks remain exact;
- all 96 common-frame restrictions from `3 x 2 x 2` to its two overlapping
  maximal cubes agree;
- two independently storage-permuted fixed physical cubes agree on 80 shared
  augmented addresses, with zero transition terms and graph-A failures;
- 20 no-refit storage-chart rows over five shapes have zero semantic or
  transition failures, with a held maximum of 594 logical qubits; and
- the same frame-argument-free generator has zero exact failures on all eight
  colour origins, all eight fixed-origin translation residues over four
  shapes, and all 24 normalized proper-cubic images of the primary box.

Passive storage permutations are not independently active local coframes.
The adversarial active-coframe fixture remains nontrivial: identity versus
`diag(-1,-1,+1)` differs by 46 OpenReference and 42 PatchGraph terms on the
shared overlap, and by 108/88 terms on one complete physical cube.  Cycle 711
does not silently erase that separate local-interface problem.

## Fixed program-order boundary

The surviving `W_star` has four active colour layers `(0,0)`, `(0,1)`,
`(1,0)`, and `(2,0)`, containing 4, 4, 6, and 6 seams.  Each layer is
support-disjoint.  All six pairs of active layers are nevertheless
noncommuting.  Of the 24 possible active-layer orders, only the reference
order reproduces the target; the largest alternative-order difference is 20
exact symplectic rows.

This classifies the surviving input as one fixed law/program order.  It is not
a runtime coframe selector, physical time, a clock, or a rate.  The same
bounded generator is used at every tested origin, translation residue, and
normalized proper-cubic box.  An order-free or internally scheduled recurrent
law has not been derived.

## Physics and hostile controls

The chart-erased family retains:

| control | exact result |
| --- | ---: |
| one-particle mass residual | `5.551115123125783e-17` |
| contact vacuum/one-particle residual | `0` |
| double-occupation contact phase residual at `g=0.37` | `0` |
| minimum active-colour deletion failures | `50` |
| cleanup-edge deletion failures | `2` each |
| minimum wrong-seam-sign failure | `1` |
| minimum chart-CZ deletion graph-A failures | `2` |
| minimum chart-Z deletion graph-A failures | `1` |
| physical encoded-Z primitive deletion residual | `sqrt(2)` |
| physical encoded-CZ primitive deletion residual | `1.9999999999999998` |

The mass and contact values are unchanged regression fixtures from the landed
Cycle 709/710 chain.  They are not a joint two-cell state-isometry theorem in
this note.

## Supplied, derived, and open structure

Supplied:

- the landed Cycle 709 finite reference word and its factor order;
- Cycle 707 placement, repetition, rail, source-sector, and clean-work code
  spaces;
- the radius-one local port key and local A orientation;
- the exact input/output signed-code chart identifications;
- the serial Manhattan route-and-return implementation;
- the Cycle 219 coin and Cycle 230 contact fixtures; and
- the fixed law/program order of the four noncommuting active layers.

Derived and executed:

- one immutable frame-argument-free `W_star` primitive and routed digest;
- exact chart erasure for all 24 common proper-cubic frames;
- exact 24/576 covariance and common-frame overlap restriction;
- zero-transition descent for independently permuted passive storage charts;
- held-shape, origin, translation, mass/contact, leakage, routing, and active
  deletion controls; and
- the exact noncommuting program-order census.

Open and not claimed:

- a joint two-star state isometry and literal combined
  free-plus-seam-plus-contact physical update;
- independently active neighboring coframe gluing;
- an order-free or internally recurrent local scheduler;
- physical preparation, formation, or enforcement of source/code/work
  sectors;
- off-code canonical completion; and
- any time, source/gravity, Record, Born/probability, realized-history,
  prediction, minimum-content, or axiom consequence.

## No-Go Discipline gate

No negative theorem ships.  The N1--N8 gate rejects any broad obstruction
reading:

- **N1 routes:** passive chart erasure succeeds; local chart-transition,
  owned-interface, direct state-isometry, sparse local scheduler, and
  staggered/internal-controller routes remain live.
- **N2 wall independence:** signed-code chart identification, independent
  local coframes, fixed program order, state-isometry closure, code genesis,
  and recurrence are distinct obligations.
- **N3 hidden inputs:** chart maps, colour origin, factor order, source/code
  sectors, blank route work, and Manhattan routing are named above.
- **N4 residual matching:** the 44--92 address-only mismatch tests executed
  chart Clifford dependence; the 46/42 overlap fixture tests active neighboring
  charts; the 20-row order residual tests layer permutation.  None is an
  end-to-end substrate residual.
- **N5 resolution:** only open boxes, five held shapes, common-frame overlap,
  and normalized proper-cubic images are tested; periodic/holed/many-star
  domains are not exhausted.
- **N6 partial closures:** the chart-erased fixed program is a strict partial
  closure even though recurrence and state-isometry composition remain open.
- **N7 steelman:** absorb the code charts into an explicit state isometry or
  compile a local flat chart transition, then internalize the fixed layer
  program without a host selector.
- **N8 cross-cycle echo:** Cycle 710's common-coframe conditional and Cycle
  709's fixed-program boundary are narrowed, not promoted to constitutional
  evidence.

Therefore there is no minimum-content, impossibility, shared-obstruction, or
axiom-pressure claim.

## TOE dependency effect

Cycle 711 narrows `C_ref`: a runtime 24-state common-coframe register is not
needed on the declared code space if the exact signed-code maps are treated as
passive code-chart identifications.  It also sharpens `C_local`: passive
storage charts glue exactly, while independently active neighboring charts
and the joint physical state isometry remain separate constructive tasks.
`C_wrap` is unchanged because the fixed layer order is a program supply and
is not called time.  `C_num`, `C_int`, and `C_source` are unchanged except for
unchanged mass/contact regression evidence.

## Prior-art and novelty boundary

Change of basis, Clifford conjugation, chart transition functions, graph-code
encodings, edge colouring, and nearest-neighbour routing are standard finite
methods.  No global priority claim is made.  The new bounded result is their
exact executable factorization for this repository's landed Cycle 709/710
signed-CAR compiler: all 24 verified common-frame actions reduce to one
frame-argument-free physical program while the signed-code chart maps and the
noncommuting fixed program order remain explicit.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle711_chart_erased_fixed_program_2026_07_26.py
```

Expected terminal:

```text
CYCLE711_CHART_ERASED_FIXED_PROGRAM_BOUNDED_PASS
```

Authority remains `none`; audit remains `unset`.  Only the independent audit
lane may set an audit verdict or effective status.
