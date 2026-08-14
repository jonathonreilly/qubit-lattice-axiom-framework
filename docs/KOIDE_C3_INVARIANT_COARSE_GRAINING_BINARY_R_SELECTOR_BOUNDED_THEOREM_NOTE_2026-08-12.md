---
claim_id: koide_c3_invariant_coarse_graining_binary_r_selector_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For the three group-algebra coefficient channels of an abstract Hermitian C3 circulant, exactly three setwise Aut(C3)-invariant set partitions exist. Conditional on choosing either nontrivial partition and Shannon entropy of its normalized coefficient powers, its uniform point is r=1 or r=1/2. The classification supplies neither a physical partition nor an entropy objective and is not a partition theorem for spectral PVM atoms or Record contents."
upstream_dependencies:
  - minimal_axioms
  - charged_lepton_koide_value_full_chain_of_custody_2026-06-02
  - koide_kappa_spectrum_operator_bridge_theorem_note_2026-04-19
  - koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10
runner: scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py
---

# Aut-Invariant Partitions Of Three Circulant Coefficient Channels

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** an abstract Hermitian circulant `H=aI+bC+bbar C^2`, its three
group-algebra coefficient channels, and setwise invariance under
`Aut(C_3)`.
**Primary runner:**
[`scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py`](../scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py)
**Runner cache:**
[`logs/runner-cache/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.txt`](../logs/runner-cache/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.txt)

## Result Up Front

Let `r=|b|^2/a^2` with `a != 0`. The coefficient channels are the trivial
line and a conjugate pair,

`(a_0,z,zbar)=(sqrt(3)a,sqrt(3)b,sqrt(3)bbar)`.

On their label set `{0,1,2}`, the nontrivial automorphism of `C_3` fixes `0`
and swaps `1,2`. Exactly three of the five set partitions are invariant as
sets of blocks:

1. `{{0,1,2}}`;
2. `{{0},{1},{2}}`;
3. `{{0},{1,2}}`.

The normalized coefficient powers are `(1,r,r)/(1+2r)`. Conditional on
choosing the three-block partition and Shannon entropy of those powers, the
unique uniform point is `r=1`. Conditional on choosing the two-block
partition and aggregating the conjugate pair, the powers are
`(1,2r)/(1+2r)` and the unique uniform point is `r=1/2`. The one-block
partition is `r`-blind.

That is the whole positive result. It is a finite classification with two
conditional consequences, not a binary physical selector. In particular:

- the coefficient channels are not the three spectral-projector atoms;
- no current axiom chooses a coefficient partition or an entropy objective;
- optimizing across the two partitions would favor the three-block maximum
  `log(3)`, not leave two equal global maxima;
- soft/stochastic coarse-grainings and other objectives lie outside the
  theorem.

The charged-lepton custody target remains open. Its identity
`Q_H=1/3+(2/3)r` still sends `r=1/2` to `Q_H=2/3`, but this note does not
derive that input value.

The governing Qualification sentence is: A choice not fixed by the supplied
structure remains a named conditional or open dependency.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The partition enumeration and conditional uniformity equations are exact; the physical coefficient grain and objective remain open."
trace_class: upstream_support
target_claim_id: charged_lepton_koide_r_half_open_selector
target_blocker_text: "choose the physical interior value r; Q=2/3 requires r=1/2"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply a physical bridge from framework content to a coefficient coarse-graining and objective; do not identify coefficient slots with spectral PVM atoms."
conditional_surface_status: "exact partition classification and fixed-partition uniformity; physical selector open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects And Imported Algebra

Let `C` be the standard three-cycle matrix. Then `C^3=I`, `C^dagger=C^2`,
and

`H=aI+bC+bbar C^2`, with `a` real and `b` complex.

The normalized Fourier-coordinate bridge
[`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
gives

`a_0=sqrt(3)a`, `z=sqrt(3)b`, and `|z|^2=3|b|^2`,

together with Parseval

`lambda_0^2+lambda_1^2+lambda_2^2=a_0^2+2|z|^2`.

This relation is a change of coordinates. The eigenvalues `lambda_j` label
the spectral PVM atoms, whereas `(a_0,z,zbar)` label group-algebra
coefficient channels. A partition of the latter is not thereby a partition
of the former.

The real-isotype theorem
[`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
gives the canonical real split

`pi_+(H)=aI`, `pi_perp(H)=bC+bbar C^2`,

with powers `E_+=3a^2` and `E_perp=6|b|^2`. Splitting the conjugate
coefficient pair before aggregation gives the three powers

`(3a^2,3|b|^2,3|b|^2)`.

Finally, the custody note
[`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
supplies `Q_H=1/3+(2/3)r` and explicitly leaves the physical `r` selector
open. No observational value is used here.

## Theorem 1 — Exact Setwise-Invariant Partition List

There are five set partitions of `{0,1,2}`:

`{{0,1,2}}`, `{{0},{1},{2}}`, `{{0},{1,2}}`,
`{{1},{0,2}}`, and `{{2},{0,1}}`.

The involution `sigma=(1 2)` fixes the first three as sets of blocks and
exchanges the last two. Therefore exactly three setwise
`Aut(C_3)`-invariant partitions exist.

Setwise invariance is essential. The three-singleton partition is fixed only
because `sigma` permutes its two nontrivial blocks. Under the stronger
condition that every block be fixed pointwise as a set, only the one-block
and singlet-versus-doublet partitions remain. This note uses the stated
setwise definition throughout.

The exact negative is correspondingly narrow: there is no other nontrivial
setwise-invariant set partition of these three coefficient labels. It is not
a claim about arbitrary coarse-graining maps.

## Theorem 2 — Conditional Uniformity Within A Fixed Partition

Normalize the three coefficient powers:

`p_3(r)=(1,r,r)/(1+2r)`.

For `r>=0`, equality of its three entries holds exactly when `r=1`. Hence
Shannon entropy within this fixed three-block family is uniquely maximized
at `r=1`.

Aggregate the conjugate pair in the two-block partition:

`p_2(r)=(1,2r)/(1+2r)`.

Equality of its two entries holds exactly when `r=1/2`. Hence Shannon
entropy within this fixed two-block family is uniquely maximized at
`r=1/2`. The one-block normalized vector is `(1)` for every `r`.

These implications are conditional on a fixed partition and on Shannon
entropy. They do not make the two partitions physically exhaustive. They
also cannot be combined into a global binary optimization: the maxima are
`log(3)` and `log(2)`, respectively.

## Current Record Boundary

The current framework wording is pinned in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). Record says
that records form; a present record locks exactly one admissible local
possibility; at most one is present per site; records are permanent; only
records are readable; readout depends on record content alone; and a site
with no record cannot be read.

Nothing in that content supplies:

- a named scalar `I`, finite additivity, or a value at absence;
- a map from record content to `(a_0,z,zbar)`;
- a coefficient partition, probability normalization, entropy functional,
  or selection rule.

Consequently Record does not choose between Theorem 1's partitions. The
adjacent registered-partition chain in PRs #6160--#6162 concerns density-body
laws, effect-only readout, and supplied product lifts. It supplies none of
the coefficient-channel objects above, so there is no load-bearing dependency
edge to that chain.

## Boundary And Non-Claims

- The physical charged-lepton value `r=1/2` remains open.
- Coefficient channels are not called Fourier eigenmodes or PVM atoms.
- A formation-event atom set is not identified with a coefficient partition.
- Other entropies, objectives, soft kernels, and non-partition maps are open.
- No fermion sector, record content, formation law, or dynamics is assigned.
- No axiom sentence is edited.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | It supplies a small exact catalog adjacent to the custody note's open `r` selector, while leaving the physical bridge open. |
| V2 | New content? | Yes: the five partitions are exhaustively tested under setwise `Aut(C_3)` action, and their fixed-partition coefficient-power uniformity points are stated with the coefficient/PVM boundary explicit. |
| V3 | Textbook result plus axioms? | The finite combinatorics is elementary; the framework-specific content is the exact imported circulant coefficient decomposition and the refusal to turn it into Record or spectral-PVM semantics. |
| V4 | More than restatement? | Yes. The parent algebra supplies coefficient powers but does not classify their setwise-invariant partitions. |
| V5 | One-step relabel? | No. The review correction removes an invalid eigenmode identification and preserves only the exact coefficient-space theorem. |

## No-Go Discipline Gate

The note ships one negative: no third nontrivial setwise-invariant set
partition exists on the three coefficient labels. It does not ship a broad
no-go for physical selectors.

### N1 — Materially distinct routes

| Route | Exact attack and outcome | Marker |
|---|---|---|
| Exhaust all set partitions | Bell number `B_3=5`; direct action leaves exactly the stated three | **ATTEMPTED** |
| Require every block to be invariant | This stronger definition removes the three-singleton partition; it is a different claim, exposing definition sensitivity | **ATTEMPTED** |
| Allow equivariant block labels | Permuted output labels can preserve additional maps, but they are not invariant set partitions in the theorem's class | **ATTEMPTED** |
| Allow stochastic/soft coarse-grainings | A continuum of equivariant kernels exists; those are not set partitions and refute only the discarded broad claim | **ATTEMPTED** |
| Change or jointly optimize the objective | Other objectives can select other points; the theorem asserts uniformity only for Shannon entropy within a fixed partition | **ATTEMPTED** |
| Use spectral PVM atoms instead | The Fourier transform relates but does not identify spectral atoms and coefficient slots; this route attacks a different object | **ATTEMPTED** |

### N2 — Wall independence

The single live physical wall is a supplied bridge from framework content to
a coefficient coarse-graining and objective. A physical rule could choose
both together, so the note does not inflate these into independent walls.
The finite partition enumeration neither supplies nor requires that bridge.

### N3 — Hidden-condition scan

| Item | Classification |
|---|---|
| group-algebra coefficient basis | explicit imported algebraic coordinate choice |
| `sigma=(1 2)` | explicit nontrivial `Aut(C_3)` action |
| setwise partition invariance | explicit theorem definition |
| normalized coefficient powers | explicit parent Frobenius decomposition |
| Shannon entropy within a fixed partition | explicit conditional objective |
| physical partition/objective | not assumed; open |

### N4 — Residual matching

The spectrum bridge supplies `a_0=sqrt(3)a`, `z=sqrt(3)b` and Parseval;
the Frobenius theorem supplies `E_+=3a^2`, `E_perp=6|b|^2`; the custody note
supplies the open `r` target. None says coefficient labels are spectral PVM
atoms or Record contents. The theorem matches only the missing finite
coefficient-partition catalog and leaves the custody residual unchanged.

### N5 — Rhetoric audit

- per-element: all three coefficient labels and all five partitions are enumerated explicitly;
- per-site: one abstract circulant is studied, with no lattice-site statement inferred;
- per-mode: spectral eigenmodes are distinguished from coefficient channels rather than conflated;
- per-block: setwise invariance and fixed-partition power aggregation are the only block claims;
- lattice-wide: no lattice dynamics, formation process, or sector assignment is claimed or tested.

### N6 — Partial-closure path

A separately supplied physical rule could name a coefficient partition and
objective without editing the four axioms. That would close the open bridge.
This theorem does not supply or recommend such a rule.

### N7 — Hostile steelman

> The classification is scientifically irrelevant: coefficient slots are
> not spectral outcomes, and even inside coefficient space a soft kernel or
> another invariant functional can select values outside `{1,1/2}`.

**Answer.** Correct against the submitted broad physical-selector reading.
That reading is removed. The surviving result is only the exact finite
classification and two fixed-partition Shannon-uniformity consequences.

### N8 — Cross-cycle echo

Earlier spectrum/PVM work acts on eigenprojectors, while the real-isotype
Frobenius work acts on group-algebra coefficient components. Their labels are
Fourier-dual, not identical. The nearby formation and registered-partition
cycles likewise use different carrier sets and maps. No cross-cycle analogy
is made load-bearing.

## Primary Runner

The runner enumerates all partitions, verifies the exact automorphism action,
checks the symbolic coefficient and aggregate uniformity equations, separates
coefficient powers from spectral eigenvalue powers by a counterexample, pins
the current Record boundary, and checks the audit-compatible note contract.
