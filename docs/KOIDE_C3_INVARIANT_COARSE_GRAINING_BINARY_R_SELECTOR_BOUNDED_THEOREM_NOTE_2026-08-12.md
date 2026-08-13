---
claim_id: koide_c3_invariant_coarse_graining_binary_r_selector_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "On the three Fourier modes of an abstract Hermitian circulant, the Aut(C3)-invariant partitions are exactly the trivial partition, the three singletons, and singlet-versus-doublet. Uniform power on those last two partitions is r=1 and r=1/2 respectively. Convention-freeness does not choose between them. The note does not force r universally and does not edit an axiom."
upstream_dependencies:
  - minimal_axioms
  - charged_lepton_koide_value_full_chain_of_custody_2026-06-02
  - flavor_r_half_is_a_stationary_point_not_forced_2026-06-02
  - koide_convention_invariant_scalar_selector_doublet_constancy_narrow_theorem_note_2026-07-12
  - r_half_open_backlog_formation_law_probe_batch_exact_support_note_2026-07-13
runner: scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py
---

# C3-Invariant Coarse-Grainings Pin A Binary Interior r Choice

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** abstract Hermitian circulant `H=aI+bC+b̄C²` on a three-label
`C_3` algebra; Aut(`C_3`) acting on Fourier mode labels.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py`](../scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py)
**Runner cache:**
[`logs/runner-cache/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.txt`](../logs/runner-cache/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.txt)

## Result Up Front

The charged-lepton custody map
[`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
leaves the interior value of `r=|b|²/a²` open. On the positive-spectrum
surface, `Q_H=1/3+(2/3)r` and `Q_H=2/3` if and only if `r=1/2`. This note
does not close that selector. It reduces the continuous-looking hunt to a
binary choice between the only two nontrivial Aut(`C_3`)-invariant
coarse-grainings of the three Fourier modes.

1. **Invariant partitions.** Label the Fourier modes `{0,1,2}`, with `0`
   the trivial character and `{1,2}` the conjugate pair. Aut(`C_3`) is the
   involution that swaps `1` and `2`. Of the five partitions of a
   three-element set, exactly three are Aut-invariant: the one-block
   partition, the three singletons, and `{ {0}, {1,2} }`.
2. **Uniform-power points.** Using the landed Hilbert–Schmidt isotype
   weights, the three-singleton (mode) distribution is uniform exactly at
   `r=1`. The two-block (sector) distribution is uniform exactly at
   `r=1/2`. The trivial partition is `r`-blind.
3. **No third invariant entropy target.** There is no other Aut-invariant
   coarse-graining whose uniform-power point could supply a third
   distinguished interior value.
4. **Convention-freeness does not choose.** The parent
   [`KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md`](KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md)
   already records that the unlabeled three-atom PVM is convention-stable
   and that ORBIT-INDEXING is not derived from Record. Both nontrivial
   invariant partitions therefore remain live as named-content structure.
   Maximizing Shannon entropy on one or the other is an extra choice, not
   a theorem of the four axioms.

The current axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) are not
edited. The Qualification burden used here is the last sentence of that
clause:

A choice not fixed by the supplied structure remains a named conditional or open dependency.

This stretch is lane-scoped to the abstract circulant `C_3` family. It does
not assign any value of `r` to a physical fermion sector and does not
re-open the hybrid-chirality no-go.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The Aut(C3) partition classification is exhaustive and finite. Uniform-power identities are exact on the landed Hilbert-Schmidt weights. Physical choice between the two nontrivial coarse-grainings, the formation-weight dictionary, and any charged-lepton assignment remain open."
trace_class: direct_blocker_closure
target_claim_id: charged_lepton_koide_r_half_open_selector
target_blocker_text: "choose the physical interior value r; Q=2/3 requires r=1/2"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Decide which Aut(C3)-invariant coarse-graining, if either, is the physical formation/power grain; do not import r=1/2 universally; do not adopt axiom text."
conditional_surface_status: "exact for the partition classification and the two uniform-power points; physical lane assignment open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `C` be the standard 3-cycle permutation matrix, `C³=I`, `C^†=C²`. An
abstract Hermitian circulant is

`H=aI+bC+b̄C²`, `a∈R`, `b∈C`, `a≠0`.

Write `r=|b|²/a²`. The landed spectral-ratio identity, used only as the
already-assembled custody line and not re-proved here, is

`Q_H := Tr(H²)/(Tr H)² = 1/3+(2/3)r`.

The Fourier mode labels are the three characters of `C_3`:

`χ_0=1`, `χ_1=ω`, `χ_2=ω²`, `ω=exp(2πi/3)`.

Aut(`C_3`) is isomorphic to `Z_2` and sends `C↦C²`, equivalently
`ω↦ω²`. It therefore fixes label `0` and swaps labels `1` and `2`.
A partition `Π` of `{0,1,2}` is Aut-invariant when `σ(Π)=Π` as a set of
blocks, where `σ=(1 2)`.

The landed Hilbert–Schmidt isotype weights, matching the custody L6/L9
normalization, are

`W_0=3a²`, `W_1=3|b|²`, `W_2=3|b|²`.

These are the squared Fourier-coefficient weights
`(|a_0|²,|z|²,|z|²)` with `a_0=√3 a` and `|z|²=3|b|²`. The two-block
aggregates are `W_{{0}}=3a²` and `W_{{1,2}}=6|b|²`.

The two exhibited formation resolutions of
[`R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md`](R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md)
are written `A_carrier={s,d_1,d_2}` and `A_cell={s,d}` with uniform
weights `w=1/3` and `w=1/2`. Their conversion to `r` uses the declared
modeling dictionary `r=(1-w)/(2w)` and is not derived here.

## Exact Target And Obligation Graph

**Exact target.** On the abstract circulant `C_3` family, classify the
Aut-invariant coarse-grainings of the Fourier modes, locate their
uniform-power points on the `r` line, and decide whether convention-freeness
or the four axioms select one of them.

| Obligation | Role | Disposition |
|---|---|---|
| pin the custody open selector | target | quoted; not closed |
| enumerate partitions of a 3-set | Theorem 1 | five partitions |
| impose Aut-invariance | Theorem 1 | three survivors |
| locate uniform-power `r` | Theorem 2 | `r=1` and `r=1/2` |
| exclude a third invariant grain | Theorem 1 | exhaustive |
| derive which grain is physical | residual | open |
| derive the `w↦r` dictionary | non-claim | modeling input |
| assign a fermion sector | non-claim | not attempted |
| re-open hybrid chirality | forbidden | not attempted |

## Theorem 1 — Aut-Invariant Partitions Of Three Fourier Modes

A three-element set has five partitions:

`{ {0,1,2} }`,
`{ {0}, {1}, {2} }`,
`{ {0}, {1,2} }`,
`{ {1}, {0,2} }`,
`{ {2}, {0,1} }`.

Apply `σ=(1 2)`. The last two partitions are exchanged with each other, so
neither is Aut-invariant. The first three are fixed as sets of blocks:

- the one-block partition is fixed;
- the three-singleton partition is fixed because `σ` permutes the blocks
  `{1}` and `{2}` inside the same partition;
- `{ {0}, {1,2} }` is fixed blockwise.

Thus exactly three Aut-invariant partitions exist. There is no fourth. In
particular there is no Aut-invariant 2+1 split that groups the singlet with
exactly one doublet mode.

The three-singleton partition is the unlabeled mode PVM of the parent July 12
note. The two-block partition is the K-orbit / sector grain of that note's
sibling occupancy surface. Theorem 1 does not derive ORBIT-INDEXING and does
not forbid the three-atom PVM. It only says these are the only invariant
grains.

## Theorem 2 — Uniform Power Lives At Opposite Distinguished Points

Normalize the Hilbert–Schmidt weights of Theorem 1's two nontrivial
partitions.

On the three singletons the probability vector is

`(W_0,W_1,W_2)/(W_0+W_1+W_2) = (a², |b|², |b|²)/(a²+2|b|²) = (1, r, r)/(1+2r)`.

This is uniform, `(1/3,1/3,1/3)`, if and only if `1=r`, that is `r=1`.

On the two blocks the probability vector is

`(W_{{0}}, W_{{1,2}})/(3a²+6|b|²) = (1, 2r)/(1+2r)`.

This is uniform, `(1/2,1/2)`, if and only if `1=2r`, that is `r=1/2`.

The one-block partition has a single weight `1` for every `r`.

Shannon entropy on a finite set is uniquely maximized at the uniform
distribution. Therefore the only entropy-maximizing points available to
Aut-invariant coarse-grainings are:

| Invariant grain | Uniform-power point | Custody name |
|---|---|---|
| one block | none (`r`-blind) | — |
| three modes | `r=1` | positivity / hierarchy endpoint |
| singlet versus doublet | `r=1/2` | two-sector balance |

This is the stationary-point fact of
[`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md),
now equipped with an exhaustive invariant-partition classification: there is
no third Aut-invariant entropy target on this three-mode set.

The two exhibited July 13 formation resolutions match the same two grains.
Uniform hazards on carrier members give `w=1/3`. Uniform hazards on K-orbit
cells give `w=1/2`. The declared dictionary `r=(1-w)/(2w)` then sends those
weights to `r=1` and `r=1/2` respectively. That dictionary is a section of
the rectangle `{1/3,1/2}×(0,1)`, not a consequence of Theorem 1 or 2. An
alternate dictionary such as `r=1-w` would send `w=1/2` to `r=1/2` and
`w=1/3` to `r=2/3`, a different interior point. The axioms do not choose
the section.

## Theorem 3 — Named Content Does Not Select The Grain

The July 12 parent proves two facts used here as hypotheses, not re-proved:

- a convention-invariant *fixed-label scalar* selector is constant on the
  conjugate doublet;
- the *unlabeled* three-atom spectral PVM `{P_1,P_ω,P_{ω̄}}` is
  convention-stable, and ORBIT-INDEXING is not derived from Record.

Theorem 1's two nontrivial partitions are exactly those two objects. Both
are compatible with named-content convention-freeness. Choosing the
two-block entropy maximum, or the three-mode entropy maximum, is therefore
an extra choice. It is not supplied by the Qualification clause quoted
above, by Record content-only, or by Aut-invariance.

This is the stretch outcome. The attempted one-step derivation
"convention-free Record ⇒ two-block grain ⇒ `r=1/2`" fails for the reason
already isolated in July 12: convention-freeness stabilizes the three-atom
PVM as well. The new information is that the failure is binary and
exhaustive: after Aut-invariance, the remaining selector is which of those
two grains, if either, is the physical power or formation grain.

The hybrid `γ_CL=Γ_χ` anticommutation no-go is not used and is not reopened.

## Boundary And Non-Claims

- No axiom sentence is edited.
- `r=1/2` is not derived, not forced, and not assigned to a physical
  charged-lepton sector.
- The energy dictionary `r=(1-w)/(2w)` remains a modeling input.
- Equal per-cell versus per-member hazards remain a formation-dynamics
  residual.
- Observational masses, NuFit, and PDG values are not used.
- Non-circulant carriers, non-Aut-invariant grains, and non-affine kernels
  are outside the classification.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axioms and Qualification | premise | quoted; no edit |
| custody chain `Q_H=1/3+(2/3)r` | parent identity | used, not re-proved |
| Hilbert–Schmidt Fourier weights | parent normalization | used as declared weights |
| July 12 convention-stable 3-PVM / no ORBIT-INDEXING | parent negative | cited |
| July 13 two formation resolutions and dictionary | comparison | not selected |
| physical grain choice | residual | open |
| hybrid chirality | forbidden reopen | unused |

The exact advance is an exhaustive Aut-invariant partition classification
together with the location of the two uniform-power points. Independent
audit remains required before any effective status may change.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The custody note's open selector: "choose the physical interior value `r`; `Q=2/3` requires `r=1/2`." This block reduces that hunt to a binary choice between the only two nontrivial Aut-invariant coarse-grainings. |
| V2 | New content? | Yes: exhaustive Aut-invariance on the five partitions of `{0,1,2}`, the identification of those survivors with the two July 13 formation resolutions, and the exact uniform-power locations `r=1` and `r=1/2`. Prior-art on `origin/main` `c820f8e38f`: the stationary-point note names the two extrema; July 12 names convention-stable 3-PVM versus doublet-constant scalars; July 13 exhibits two formation weights. None classifies Aut-invariant partitions of the mode set or proves there is no third invariant grain. |
| V3 | Textbook partition counting plus axioms? | No. The 5-partition count is finite combinatorics, but the load-bearing step is that Aut(`C_3`) is the named-content automorphism already isolated by July 12, and that the HS weights are the custody Fourier coordinates. Those are framework objects. |
| V4 | More than a restatement? | Yes. "r=1/2 is a stationary point" does not say it is one of exactly two invariant uniform-power points. "ORBIT-INDEXING is not from Record" does not enumerate the invariant grains. |
| V5 | One-step relabel? | No. The closest landed facts are the two extrema and the two formation weights. The missing lemma was uniqueness of the invariant partition list. |

## No-Go Discipline Gate

Two scoped negatives are shipped: (i) there is no third Aut-invariant
coarse-graining of the three modes; (ii) convention-freeness and entropy
maximization do not uniquely select `r=1/2`. They are not a global
non-derivability theorem for the charged-lepton value.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Force two-block grain from Record content-only | identify records with Aut-invariant scalar labels | July 12: unlabeled 3-PVM is convention-stable; Theorem 3 records the failure | **ATTEMPTED** |
| Force three-mode grain from convention-freeness | treat the stable 3-PVM as selected | Theorem 3: the two-block grain is equally Aut-invariant | **ATTEMPTED** |
| Invent a third invariant 2+1 split | group the singlet with one doublet mode | Theorem 1: those partitions are not Aut-invariant | **ATTEMPTED** |
| Maximize 3-mode entropy | uniform Fourier weights | Theorem 2: selects `r=1`, the other distinguished point | **ATTEMPTED** |
| Maximize 2-block entropy | uniform sector weights | Theorem 2: selects `r=1/2`, still an extra choice | **ATTEMPTED** |
| Hybrid `γ_CL=Γ_χ` | reopen the anticommuting no-go | out of scope; not used | **RULED OUT BY PRIOR** |
| Import observational `Q=2/3` | fit `r` | forbidden as a derivation input | **RULED OUT BY PRIOR** |

### N2 — wall independence

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| no third invariant grain / grain choice | no: a classification does not pick a grain | no: picking a grain does not enumerate partitions | independent |
| grain choice / energy dictionary | no: a power grain can exist without formation `w` | no: a `w↦r` map does not pick a grain | independent |
| convention-stable 3-PVM / two-block grain | no: July 12 keeps both | no: Aut-invariance keeps both | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| Hilbert–Schmidt Fourier weights | declared parent normalization |
| Aut(`C_3`) as the involution `(1 2)` | named-content automorphism from July 12 |
| finite-support positive `a≠0` | explicit circulant chart |
| "natural" / "standard" | not used as a load-bearing word |
| physical charged-lepton assignment | not assumed |

### N4 — residual matching

The custody selector, the stationary-point residual ("which extremum/lane"),
July 12's undischarged ORBIT-INDEXING, and July 13's unselected formation
atom are the same binary grain choice. This note matches that residual. It
does not re-attack singleton mass, menu restriction, or hybrid chirality.

### N5 — rhetoric audit

"Does not uniquely select `r=1/2`" is checked at:

- per-element: the three mode labels and the two nontrivial partitions;
- per-site: one abstract `C_3` circulant, not a lattice;
- per-mode: Fourier characters `{0,1,2}`;
- per-block: only the Aut-invariant coarse-graining block;
- lattice-wide: not executed.

### N6 — partial-closure path

A convention that *names* ORBIT-INDEXING, or that names 3-mode entropy as
the physical grain, would close the binary choice without enlarging the
axiom list. Those paths remain owner-gated. This note does not take them.

### N7 — steelman

> The two-block grain is the occupancy surface already written in sibling
> notes, so classifying partitions changes nothing: `r=1/2` is still the
> charged-lepton point.

**Answer.** Those sibling notes *supply* ORBIT-INDEXING. The Qualification
clause forbids using a supplied occupancy partition as named axiom content.
The classification shows why a further hunt for a third invariant grain is
empty, and why convention-freeness cannot finish the job. That is a sharper
wall, not a value derivation.

### N8 — cross-cycle echo

Frobenius isotype-weight freedom, operator-spectral no-gos, record-orbit-count
no-gos, corner-determinant obstruction, and Dirac-mass-forces-`r=1` are
different residuals. None enumerates Aut-invariant partitions of the three
Fourier labels. Hybrid chirality remains closed and unused.

## Primary Runner

[`scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py`](../scripts/koide_c3_invariant_coarse_graining_binary_r_selector_2026_08_12.py)
enumerates the five partitions, checks Aut-invariance, and verifies the two
uniform-power identities in exact rational arithmetic.
